"""Measure wall lengths by partition type from a PDF floor plan's vector geometry.

Prototype for sheet A-120 (DIMENSIONAL FLOOR PLAN), but nothing in the
measuring code is tuned to that sheet's answers: it reads line work, wall-type
tags and dimension strings straight from the PDF.

    python3 -I extract_walls.py [sheet.pdf] [--out DIR] [--clip x0 y0 x1 y1]

Quantities only (linear feet). No prices.

Method (see README.md for the evaluation):

 1. Line work.  Collect axis-aligned stroked segments.  In this drawing set the
    cut wall lines are black 0.5 pt strokes; a gypsum board layer shows up as a
    pair of 0.5 pt lines 0.94 pt apart (5/8" at 1/4" = 1'-0").  Collinear
    pieces on the same coordinate are merged.

 2. Stud cavities.  A wall body is a pair of parallel lines whose spacing equals
    a stud depth at scale (3-5/8" = 5.44 pt, 6" = 9.0 pt, 8" = 12.0 pt) with no
    other cut line between them.  For every stretch of the cavity we check
    whether a board line sits 0.94 pt outside each face:
        3-5/8" + board both sides -> A3 family (A3A/A3B; ~4-7/8" overall)
        3-5/8" + board one side   -> D3 family (D3A/D3C)
        6"     + board both sides -> A6 family (A6A/A6B; ~7-1/4" overall)
        8"                         -> exterior 8" stud wall
        6" one side / bare, 3-5/8" bare -> reported as 'other' (not a typed partition)
    On the one-sided pass the bare face may be a thin (0.24 pt) line, because
    the D3 walls on this sheet draw their unfinished face that way.

 3. Runs.  Collinear bodies of one class are merged across junction gaps
    (<= 14 pt, where a crossing wall interrupts a face).  Gaps that contain door
    frame strokes (0.79 pt) and are <= 90 pt are openings: the 'net' length
    excludes them, the 'gross' length bridges them (the estimator's PlanSwift
    convention is to run through doors).  Run ends are extended to the
    centerline of a perpendicular partition they butt into; a partition that
    butts into an exterior wall stops at the exterior wall's inside face.
    Runs are then cut into pieces at every T-junction.

 4. Types.  Wall-type tags are text spans (A3A, D3C, ...) inside diamonds.  Each
    tag has a leader ending in a heavy 2.52 pt tick drawn across the wall it
    marks.  We follow tick -> leader -> diamond to bind tick to tag, then give
    the tag to the piece the tick crosses (same thickness family preferred).
    Untagged pieces take the type of the nearest tagged piece of the same
    thickness family through the junction graph (cost = feet travelled, +0.5 ft
    per corner, so straight continuation wins ties).  If the runner-up type is
    within 1 ft the piece is marked 'propagated-ambiguous' for review.  Pieces
    with no tagged neighbour stay 'untagged <family>'.  Thickness alone can
    separate A3/A6/D3 families but never A from B (same assembly geometry).
    Pieces with no board on either face are reported as 'bare cavity' and are
    not partitions (on A-120: a booth bench back).
 5. Scale.  Nominal 1/4" = 1'-0" (18 pt per ft).  Every printed dimension
    string is paired with the two dimension ticks that bracket it and the
    measured span is compared with the printed value; the median ratio is
    reported and used.

 6. Exterior.  8" stud cavities are exterior walls (types/heights come from
    wall sections, not the plan).  As a secondary figure the exterior wall
    line is continued across storefront/window openings between solid runs.

Outputs: results.json (LF per type, per run with endpoints) and overlay.png.
Evaluation against the estimator's markup: compare_to_markup.py.
Coordinates are PDF points, origin top-left of the page (pymupdf space).
"""
import json, math, os, re, statistics, sys
from collections import defaultdict

import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_PDF = os.path.join(os.path.dirname(os.path.dirname(HERE)),
                           'source/drawings/Architectural/A-120-DIMENSIONAL-FLOOR-PLAN-Rev.0.pdf')
# Floor-plan viewport on A-120 (excludes the drive-up canopy plan above it,
# the notes column and the title block).  An app would get this from the AI
# ("where is the plan viewport?") or from the PDF's viewport/OCG structure.
DEFAULT_CLIP = (430, 440, 1760, 1500)

PT_PER_IN_PAPER = 72.0
NOMINAL_SCALE_IN_PER_FT = 0.25          # 1/4" = 1'-0"
PT_PER_FT = PT_PER_IN_PAPER * NOMINAL_SCALE_IN_PER_FT   # 18.0
def real_in_to_pt(inches):
    return inches / 12.0 * PT_PER_FT

BOARD = real_in_to_pt(5 / 8)              # 0.9375 pt
STUDS = {'3-5/8': real_in_to_pt(3.625),   # 5.44
         '6': real_in_to_pt(6.0),         # 9.0
         '8': real_in_to_pt(8.0)}         # 12.0
WALL_STROKE = 0.5
DOOR_STROKE = 0.79
TICK_STROKE = 2.52
AXIS_TOL = 0.06
COORD_TOL = 0.15
JUNCTION_GAP = 14.0     # pt; ~9" (a crossing wall interrupting one face)
OPENING_GAP = 90.0      # pt; 5'-0" maximum single opening bridged
MIN_PIECE = 2.0         # pt
EXTEND_INTO_EXTERIOR = False   # partitions end at the exterior wall's inside face
TAG_RE = re.compile(r'^[AD]\d[A-Z]$')


# ----------------------------------------------------------------- geometry io
def collect_lines(drawings, clip, pred):
    """Axis-aligned stroked segments passing pred(drawing) -> merged (c, s, e)."""
    H, V = defaultdict(list), defaultdict(list)
    for d in drawings:
        if d['type'] not in ('s', 'fs') or not pred(d):
            continue
        for it in d['items']:
            if it[0] != 'l':
                continue
            a, b = it[1], it[2]
            if not (clip.contains(a) and clip.contains(b)):
                continue
            if abs(a.y - b.y) < AXIS_TOL:
                H[round((a.y + b.y) / 2, 2)].append((min(a.x, b.x), max(a.x, b.x)))
            elif abs(a.x - b.x) < AXIS_TOL:
                V[round((a.x + b.x) / 2, 2)].append((min(a.y, b.y), max(a.y, b.y)))
    return merge_collinear(H), merge_collinear(V)


def merge_collinear(D):
    # cluster coordinates within 0.05 pt, then union touching intervals
    out = []
    keys = sorted(D)
    groups, cur = [], []
    for k in keys:
        if cur and k - cur[-1] > 0.05:
            groups.append(cur); cur = []
        cur.append(k)
    if cur:
        groups.append(cur)
    for g in groups:
        c = sum(g) / len(g)
        iv = sorted(x for k in g for x in D[k])
        s, e = iv[0]
        for a, b in iv[1:]:
            if a <= e + 0.1:
                e = max(e, b)
            else:
                out.append((c, s, e)); s, e = a, b
        out.append((c, s, e))
    return sorted(out)


def union_cover(lines, c, a, b, tol=COORD_TOL):
    """Sub-intervals of [a,b] covered by lines at coordinate c."""
    iv = sorted((max(a, s), min(b, e)) for (c2, s, e) in lines
                if abs(c2 - c) <= tol and e > a and s < b)
    out = []
    for s, e in iv:
        if out and s <= out[-1][1] + 0.3:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out


def subtract(iv, cuts):
    res = [iv]
    for s, e in cuts:
        nr = []
        for a, b in res:
            if e <= a or s >= b:
                nr.append((a, b)); continue
            if s > a: nr.append((a, s))
            if e < b: nr.append((e, b))
        res = nr
    return res


def in_cover(cov, x):
    return any(s - 0.01 <= x <= e + 0.01 for s, e in cov)


# ------------------------------------------------------------- wall bodies
def classify(stud, nb):
    if stud == '3-5/8':
        return {2: 'A3', 1: 'D3', 0: 'other-3-5/8-bare'}[nb]
    if stud == '6':
        return {2: 'A6', 1: 'other-6-one-side', 0: 'other-6-bare'}[nb]
    return 'EXT8'


def find_bodies(L5, L2, orient):
    """Return wall bodies for one orientation.

    L5: cut wall lines (0.5 pt).  L2: thin lines (0.24 pt), used only as the
    bare face of a one-sided wall.  Patterns are matched most-specific first
    and every accepted body claims its band (faces + boards) over its extent,
    so a later, looser pattern cannot reuse those lines (e.g. a D3 board line
    plus an unrelated line 12 pt away must not read as an 8" exterior wall).
    """
    L5s = sorted(L5)
    bodies = []
    claimed = []          # (lo, hi, a, b) bands already explained by a body

    def between(c1, c2, a, b):
        return [(s, e) for (c, s, e) in L5s if c1 + 0.25 < c < c2 - 0.25 and e > a and s < b]

    def free(lo, hi, a, b):
        cuts = [(ca, cb) for (l2, h2, ca, cb) in claimed if min(hi, h2) - max(lo, l2) > 0.3]
        return subtract((a, b), cuts)

    def pieces_for(c1, c2, stud, a, b, need_left, need_right):
        out = []
        for x, y in subtract((a, b), between(c1, c2, a, b)):
            if y - x < 1.0:
                continue
            bl = union_cover(L5s, c1 - BOARD, x, y)
            br = union_cover(L5s, c2 + BOARD, x, y)
            cuts = sorted({x, y} | {v for s, e in bl + br for v in (s, e) if x < v < y})
            segs = []
            for u, v in zip(cuts, cuts[1:]):
                m = (u + v) / 2
                segs.append([u, v, in_cover(bl, m), in_cover(br, m)])
            merged = []
            for sg in segs:   # absorb slivers into the previous piece
                if merged and (sg[1] - sg[0] < MIN_PIECE or merged[-1][2:] == sg[2:]):
                    merged[-1][1] = sg[1]
                else:
                    merged.append(sg)
            for u, v, fl, fr in merged:
                if (need_left and not fl) or (need_right and not fr):
                    continue
                out.append(dict(orient=orient, c1=c1, c2=c2, stud=stud, a=u, b=v,
                                board_l=fl, board_r=fr, cls=classify(stud, int(fl) + int(fr))))
        return out

    def accept(cands):
        for bd in cands:
            lo = bd['c1'] - (BOARD if bd['board_l'] else 0)
            hi = bd['c2'] + (BOARD if bd['board_r'] else 0)
            for x, y in free(lo, hi, bd['a'], bd['b']):
                if y - x < 1.0:
                    continue
                q = dict(bd, a=x, b=y)
                bodies.append(q)
                claimed.append((lo, hi, x, y))

    def pairs(stud_names):
        cands = []
        for i, (c1, s1, e1) in enumerate(L5s):
            for (c2, s2, e2) in L5s[i + 1:]:
                g = c2 - c1
                if g > max(STUDS.values()) + 0.3:
                    break
                stud = next((k for k in stud_names if abs(g - STUDS[k]) <= COORD_TOL), None)
                a, b = max(s1, s2), min(e1, e2)
                if stud and b - a >= 1.0:
                    cands += pieces_for(c1, c2, stud, a, b, False, False)
        return cands

    # pass 1: 3-5/8" and 6" cavities with both faces cut; boarded both sides first
    c = pairs(('3-5/8', '6'))
    accept([b for b in c if b['board_l'] and b['board_r']])
    accept([b for b in c if (b['board_l'] or b['board_r']) and not (b['board_l'] and b['board_r'])])
    # pass 2: one-sided 3-5/8" walls whose bare face is a thin line
    cands = []
    for (c1, s1, e1) in L5s:
        for (c2, s2, e2) in L2:
            for side in (-1, +1):
                if abs((c2 - c1) * side - STUDS['3-5/8']) > COORD_TOL:
                    continue
                a, b = max(s1, s2), min(e1, e2)
                if b - a < 1.0:
                    continue
                lo, hi = min(c1, c2), max(c1, c2)
                cands += pieces_for(lo, hi, '3-5/8', a, b, side > 0, side < 0)
    accept([b for b in cands if b['cls'] == 'D3'])
    # pass 3: 8" exterior stud cavities, then bare cavities (reported as 'other')
    c = pairs(('8',))
    accept(c)
    accept([b for b in pairs(('3-5/8', '6')) if not (b['board_l'] or b['board_r'])])
    return absorb_short_pieces(bodies)


def absorb_short_pieces(bodies, max_len=40.0):
    """Inside one continuous cavity, a short stretch that lost a board on one
    side (another wall butts against that face, a casework return, ...) is the
    same wall: give it the class of its longer neighbour."""
    groups = defaultdict(list)
    for bd in bodies:
        groups[(round(bd['c1'], 1), round(bd['c2'], 1), bd['stud'])].append(bd)
    for bl in groups.values():
        bl.sort(key=lambda b: b['a'])
        for i, bd in enumerate(bl):
            if bd['b'] - bd['a'] > max_len:
                continue
            nb = [bl[j] for j in (i - 1, i + 1) if 0 <= j < len(bl)
                  and min(abs(bl[j]['a'] - bd['b']), abs(bd['a'] - bl[j]['b'])) < 1.0
                  and bl[j]['cls'] != bd['cls'] and bl[j]['b'] - bl[j]['a'] > bd['b'] - bd['a']
                  and not bl[j]['cls'].startswith('other') and bl[j]['cls'] != 'EXT8']
            if nb and not bd['cls'] == 'EXT8':
                best = max(nb, key=lambda b: b['b'] - b['a'])
                bd['cls'] = best['cls']; bd['board_l'] = best['board_l']; bd['board_r'] = best['board_r']
                bd['absorbed'] = True
    return bodies


# ---------------------------------------------------------------- runs
def has_door(door_lines, orient, c1, c2, a, b):
    H, V = door_lines
    lo, hi = c1 - 4, c2 + 4
    for (c, s, e) in (H if orient == 'H' else V):     # parallel frame/leaf strokes
        if lo <= c <= hi and e > a and s < b:
            return True
    for (c, s, e) in (V if orient == 'H' else H):     # jamb strokes
        if a - 1 <= c <= b + 1 and e > lo and s < hi:
            return True
    return False


def build_runs(bodies, door_lines):
    groups = defaultdict(list)
    # cluster bodies of one orientation+class by centerline (within 0.4 pt)
    for (o, cls) in sorted({(b['orient'], b['cls']) for b in bodies}):
        bl = sorted((b for b in bodies if b['orient'] == o and b['cls'] == cls),
                    key=lambda b: b['c1'] + b['c2'])
        k = 0; prev = None
        for b in bl:
            m = (b['c1'] + b['c2']) / 2
            if prev is not None and m - prev > 0.4:
                k += 1
            groups[(o, cls, k)].append(b); prev = m
    runs = []
    for key, bl in groups.items():
        bl.sort(key=lambda b: b['a'])
        cur = None
        for bd in bl:
            if cur is not None:
                gap = bd['a'] - cur['b']
                if gap <= JUNCTION_GAP:
                    cur['b'] = max(cur['b'], bd['b']); cur['bodies'].append(bd); continue
                if gap <= OPENING_GAP and has_door(door_lines, bd['orient'], cur['c1'], cur['c2'], cur['b'], bd['a']):
                    cur['openings'].append((cur['b'], bd['a']))
                    cur['b'] = max(cur['b'], bd['b']); cur['bodies'].append(bd); continue
                runs.append(cur)
            cur = dict(orient=bd['orient'], cls=bd['cls'], c1=bd['c1'], c2=bd['c2'],
                       a=bd['a'], b=bd['b'], bodies=[bd], openings=[])
        runs.append(cur)
    for r in runs:
        r['c'] = (r['c1'] + r['c2']) / 2
        lo = r['c1'] - (BOARD if r['cls'] in ('A3', 'A6', 'D3') else 0)
        hi = r['c2'] + (BOARD if r['cls'] in ('A3', 'A6') else 0)
        r['half'] = (hi - lo) / 2 + 0.6
        r['a0'], r['b0'] = r['a'], r['b']
    return runs


def extend_to_junctions(runs):
    """Extend run ends to the centerline of a perpendicular wall they butt into.
    Returns junction edges (i, end, j, kind) with kind 'L' (end meets end of j)
    or 'T' (end meets the middle of j)."""
    edges = []
    for i, r in enumerate(runs):
        for end in ('a', 'b'):
            x = r[end + '0']
            best = None
            for j, q in enumerate(runs):
                if q['orient'] == r['orient'] or j == i:
                    continue
                # q's centerline coordinate must be near our end (within q's half width + slack)
                d = abs(q['c'] - x)
                if d > q['half'] + 2.5:
                    continue
                # our centerline must fall within q's extent (+ our half width)
                if not (q['a0'] - r['half'] - 2.5 <= r['c'] <= q['b0'] + r['half'] + 2.5):
                    continue
                inward = (q['c'] - x) * (1 if end == 'b' else -1)
                if inward < -1.0 and d > 1.5:   # q must be ahead of the end, not behind it
                    continue
                if best is None or d < best[0]:
                    best = (d, j)
            if best:
                j = best[1]; q = runs[j]
                if q['cls'] != 'EXT8' or r['cls'] == 'EXT8' or EXTEND_INTO_EXTERIOR:
                    r[end] = q['c']
                # else: a partition stops at the inside face of the exterior
                # wall (where its own cavity lines already end)
                kind = 'L' if min(abs(r['c'] - q['a0']), abs(r['c'] - q['b0'])) <= r['half'] + 3 else 'T'
                edges.append((i, end, j, kind))
    return edges


def length_pt(r, net=False):
    L = r['b'] - r['a']
    if net:
        L -= sum(e - s for s, e in r['openings'])
    return L


def exterior_glazing_spans(runs, all_lines, max_gap=540.0, min_cover=0.7):
    """Exterior 8in runs on one wall line, separated by storefront/window
    openings.  A gap is bridged when parallel lines (frames, sills, glass)
    cover >= 70% of it inside the wall band.  Returns (orient, c, s, e)."""
    H, V = all_lines
    ext = [r for r in runs if r['cls'] == 'EXT8']
    lines_by = defaultdict(list)
    for r in ext:
        key = (r['orient'], round(r['c']))
        lines_by[key].append(r)
    spans = []
    for (o, _), rs in lines_by.items():
        rs.sort(key=lambda r: r['a'])
        c = rs[0]['c']
        par = H if o == 'H' else V
        for r1, r2 in zip(rs, rs[1:]):
            s, e = r1['b'], r2['a']
            if e - s <= 3 or e - s > max_gap:
                continue
            if any(q['cls'] != 'EXT8' and q['orient'] == o and abs(q['c'] - c) < 4 and q['a'] < e and s < q['b']
                   for q in runs):
                continue    # the gap is another wall (e.g. a 6in segment), not glazing
            cov = union_cover([(c, max(s, ls), min(e, le)) for (lc, ls, le) in par
                               if abs(lc - c) <= 14 and le > s and ls < e], c, s, e, tol=0.01)
            if sum(v - u for u, v in cov) / (e - s) >= min_cover:
                spans.append((o, c, s, e))
    return spans


# ---------------------------------------------------------------- tags
def read_tags(page, drawings, clip):
    tags = []
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                t = s['text'].strip()
                if TAG_RE.match(t) and clip.contains(pymupdf.Point(s['bbox'][0], s['bbox'][1])):
                    x0, y0, x1, y1 = s['bbox']
                    tags.append(dict(tag=t, x=(x0 + x1) / 2, y=(y0 + y1) / 2))
    ticks = []
    thin = []
    for d in drawings:
        if d['type'] != 's':
            continue
        if abs(d['width'] - TICK_STROKE) < 0.01:
            for it in d['items']:
                if it[0] == 'l':
                    ticks.append((it[1], it[2]))
        elif d['width'] < 0.3:
            for it in d['items']:
                if it[0] == 'l':
                    thin.append((it[1], it[2]))
    out = []
    for a, b in ticks:
        mx, my = (a.x + b.x) / 2, (a.y + b.y) / 2
        orient = 'V' if abs(a.x - b.x) < 0.1 else ('H' if abs(a.y - b.y) < 0.1 else 'D')
        # follow the leader: thin segment starting at a tick end; hop up to 3 segments
        best = None
        for e in (a, b):
            frontier = [(e.x, e.y)]
            for _hop in range(3):
                nxt = []
                for (px, py) in frontier:
                    for u, v in thin:
                        for P, Q in ((u, v), (v, u)):
                            if math.dist((P.x, P.y), (px, py)) < 0.8 and math.dist((P.x, P.y), (Q.x, Q.y)) > 1.5:
                                for t in tags:
                                    dd = math.dist((Q.x, Q.y), (t['x'], t['y']))
                                    if dd < 16 and (best is None or dd < best[0]):
                                        best = (dd, t, 'leader')
                                nxt.append((Q.x, Q.y))
                frontier = nxt[:20]
                if best:
                    break
        if best is None and tags:
            t = min(tags, key=lambda t: math.dist((mx, my), (t['x'], t['y'])))
            best = (math.dist((mx, my), (t['x'], t['y'])), t, 'nearest')
        out.append(dict(x=mx, y=my, tick_orient=orient, tag=best[1]['tag'], bind=best[2],
                        tag_xy=(round(best[1]['x'], 1), round(best[1]['y'], 1))))
    return tags, out


def family(tag):
    return tag[:2]   # 'A3', 'A6', 'D3'


# ---------------------------------------------------------------- scale check
def parse_ftin(t):
    m = re.fullmatch(r"(\d+)'-(\d+)(?: (\d+)/(\d+))?\"", t.strip())
    if m:
        ft, inch, n, d = m.groups()
        return int(ft) * 12 + int(inch) + (int(n) / int(d) if n else 0)
    m = re.fullmatch(r"(\d+)(?: (\d+)/(\d+))?\"", t.strip())
    if m:
        inch, n, d = m.groups()
        return int(inch) + (int(n) / int(d) if n else 0)
    return None


def calibrate(page, drawings):
    """Pair each printed dimension with the dimension ticks bracketing it."""
    # Dimension ticks are 45-degree slashes drawn as two half-segments; the
    # point where the halves meet lies on the dimension line.
    ends = []
    for d in drawings:
        if d['type'] == 's' and abs(d['width'] - 0.86) < 0.01:
            for it in d['items']:
                if it[0] == 'l':
                    a, b = it[1], it[2]
                    if abs(a.x - b.x) > 1 and abs(a.y - b.y) > 1:
                        ends += [(a.x, a.y), (b.x, b.y)]
    ends.sort()
    ticks = []
    for i, p in enumerate(ends):
        for q in ends[i + 1:i + 6]:
            if abs(q[0] - p[0]) < 0.05 and abs(q[1] - p[1]) < 0.05:
                ticks.append(p)
    samples = []
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            t = ''.join(s['text'] for s in l['spans']).strip()
            inches = parse_ftin(t)
            if not inches or inches < 24:
                continue
            x0, y0, x1, y1 = l['bbox']
            dx, dy = l['dir']
            if abs(dy) < 0.01:      # horizontal text sits just above its dimension line
                row = [p for p in ticks if y1 - 4 <= p[1] <= y1 + 8]
                cx = (x0 + x1) / 2
                left = [p for p in row if p[0] < x0 + 1]
                right = [p for p in row if p[0] > x1 - 1]
                if not left or not right:
                    continue
                pl = max(left, key=lambda p: p[0]); pr = min(right, key=lambda p: p[0])
                if abs(pl[1] - pr[1]) > 0.5:
                    continue
                span = pr[0] - pl[0]
            elif abs(dx) < 0.01:    # vertical text sits just left of its dimension line
                col = [p for p in ticks if x1 - 4 <= p[0] <= x1 + 8]
                above = [p for p in col if p[1] < y0 + 1]
                below = [p for p in col if p[1] > y1 - 1]
                if not above or not below:
                    continue
                pa = max(above, key=lambda p: p[1]); pb = min(below, key=lambda p: p[1])
                if abs(pa[0] - pb[0]) > 0.5:
                    continue
                span = pb[1] - pa[1]
            else:
                continue
            nominal = inches / 12 * PT_PER_FT
            ratio = span / nominal
            if 0.8 < ratio < 1.25:   # discard pairings that clearly grabbed the wrong ticks
                samples.append(dict(text=t, inches=round(inches, 3), measured_pt=round(span, 2),
                                    nominal_pt=round(nominal, 2), ratio=round(ratio, 5)))
    return samples


# ---------------------------------------------------------------- main
def main(argv):
    args = list(argv)
    pdf = DEFAULT_PDF
    outdir = HERE
    clip = DEFAULT_CLIP
    while args:
        a = args.pop(0)
        if a == '--out': outdir = args.pop(0)
        elif a == '--clip': clip = tuple(float(args.pop(0)) for _ in range(4))
        else: pdf = a
    page = pymupdf.open(pdf)[0]
    drawings = page.get_drawings()
    clip = pymupdf.Rect(*clip)
    black = lambda d: d.get('color') == (0.0, 0.0, 0.0)

    # 1. line work
    L5 = collect_lines(drawings, clip, lambda d: black(d) and abs(d['width'] - WALL_STROKE) < 0.01)
    L2 = collect_lines(drawings, clip, lambda d: (d['width'] or 0) < 0.3)
    DOOR = collect_lines(drawings, clip, lambda d: black(d) and abs(d['width'] - DOOR_STROKE) < 0.01)
    n_oblique = sum(1 for d in drawings if d['type'] == 's' and black(d) and abs(d['width'] - WALL_STROKE) < 0.01
                    for it in d['items'] if it[0] == 'l' and clip.contains(it[1])
                    and abs(it[1].x - it[2].x) >= AXIS_TOL and abs(it[1].y - it[2].y) >= AXIS_TOL)

    # 2. bodies
    bodies = find_bodies(L5[0], L2[0], 'H') + find_bodies(L5[1], L2[1], 'V')

    # 3. runs + junctions
    runs = build_runs(bodies, DOOR)
    runs = [r for r in runs if r['b'] - r['a'] >= 3.0]
    edges = extend_to_junctions(runs)

    # 4. tags -> runs
    tags, ticks = read_tags(page, drawings, clip)
    for r in runs:
        r['ticks'] = []
    unbound = []
    for t in ticks:
        want = 'H' if t['tick_orient'] == 'V' else 'V'
        best = None
        for i, r in enumerate(runs):
            if r['orient'] != want or r['cls'] not in ('A3', 'A6', 'D3'):
                continue
            along, perp = (t['x'], t['y']) if want == 'H' else (t['y'], t['x'])
            d = abs(perp - r['c'])
            if d <= r['half'] + 3 and r['a'] - 2 <= along <= r['b'] + 2:
                score = d + (0 if r['cls'] == family(t['tag']) else 50)
                if best is None or score < best[0]:
                    best = (score, i, along)
        if best:
            runs[best[1]]['ticks'].append((best[2], t['tag'], t))
        else:
            unbound.append(t)

    # 5. split every run at T-junctions (where another run's end butts into
    #    its middle) and between two different tags, so that each piece is a
    #    wall segment between junctions.
    cuts_at = defaultdict(set)
    for (i, end, j, kind) in edges:
        if kind == 'T':
            cuts_at[j].add(round(runs[i]['c'], 2))
    pieces = []
    for idx, r in enumerate(runs):
        cuts = sorted(x for x in cuts_at[idx] if r['a'] + 3 < x < r['b'] - 3)
        tk = sorted(r['ticks'], key=lambda x: x[0])
        bounds = [r['a']] + cuts + [r['b']]
        # two different tags with no junction between them: cut half-way
        extra = []
        for (p1, t1, _), (p2, t2, _) in zip(tk, tk[1:]):
            if t1 != t2 and not any(p1 < x < p2 for x in bounds):
                extra.append((p1 + p2) / 2)
        bounds = sorted(bounds + extra)
        for k, (u, v) in enumerate(zip(bounds, bounds[1:])):
            q = dict(r)
            q.update(a=u, b=v, parent=idx, seq=k,
                     openings=[(max(s, u), min(e, v)) for s, e in r['openings'] if e > u and s < v],
                     ticks=[x for x in tk if u - 0.01 <= x[0] <= v + 0.01])
            pieces.append(q)
    runs = pieces

    # adjacency between pieces: shared end points (junctions) and collinear
    # continuation inside one parent run
    adj = defaultdict(list)
    def ends(r):
        if r['orient'] == 'H':
            return [(r['a'], r['c']), (r['b'], r['c'])]
        return [(r['c'], r['a']), (r['c'], r['b'])]
    for i, r in enumerate(runs):
        for j in range(i + 1, len(runs)):
            q = runs[j]
            if r['cls'] != q['cls']:
                continue
            if r['parent'] == q['parent'] and abs(r['seq'] - q['seq']) == 1:
                adj[i].append((j, 'C')); adj[j].append((i, 'C')); continue
            touch = min(math.dist(p, s) for p in ends(r) for s in ends(q))
            if touch <= 3.0 and r['orient'] != q['orient']:
                adj[i].append((j, 'L')); adj[j].append((i, 'L'))
            elif touch <= 3.0 and abs(r['c'] - q['c']) < 0.6:
                adj[i].append((j, 'C')); adj[j].append((i, 'C'))

    # 6. type assignment.  A piece crossed by a tag tick takes that tag.  Other
    #    pieces take the type whose tagged pieces are nearest through the
    #    junction graph (same thickness family only).  Cost = feet travelled,
    #    plus 0.5 ft per corner, so a straight continuation wins a tie with a
    #    corner.  When the runner-up type is within 1 ft the piece is flagged
    #    ambiguous: code cannot decide it; a reviewer/AI should.
    import heapq
    for r in runs:
        r['type'] = r['ticks'][0][1] if r['ticks'] else None
        r['type_source'] = 'tag' if r['ticks'] else None
        r['candidates'] = {}
    types = sorted({r['type'] for r in runs if r['type']})
    for T in types:
        dist = [float('inf')] * len(runs)
        pq = []
        for i, r in enumerate(runs):
            if r['type'] == T:
                dist[i] = 0.0; heapq.heappush(pq, (0.0, i))
        while pq:
            d0, i = heapq.heappop(pq)
            if d0 > dist[i]:
                continue
            for j, kind in adj[i]:
                if runs[j]['cls'] != family(T) or runs[j]['type_source'] == 'tag':
                    continue
                step = (runs[j]['b'] - runs[j]['a']) / PT_PER_FT + (0.5 if kind == 'L' else 0.0)
                if d0 + step < dist[j]:
                    dist[j] = d0 + step; heapq.heappush(pq, (dist[j], j))
        for i, r in enumerate(runs):
            if r['type_source'] != 'tag' and dist[i] < float('inf'):
                r['candidates'][T] = round(dist[i], 2)
    for r in runs:
        if r['type_source'] == 'tag':
            continue
        if r['candidates']:
            ranked = sorted(r['candidates'].items(), key=lambda kv: kv[1])
            r['type'] = ranked[0][0]
            r['type_source'] = 'propagated'
            if len(ranked) > 1 and ranked[1][1] - ranked[0][1] < 1.0:
                r['type_source'] = 'propagated-ambiguous'
        else:
            r['type'] = {'EXT8': 'EXT 8in stud (exterior)',
                         'other-6-one-side': '6in stud, board one side',
                         'other-6-bare': 'bare 6in cavity (not a wall?)',
                         'other-3-5/8-bare': 'bare 3-5/8in cavity (not a wall?)'}.get(r['cls'], 'untagged ' + r['cls'])
            r['type_source'] = 'geometry-only'

    # 7. scale
    cal = calibrate(page, drawings)
    ratios = [c['ratio'] for c in cal]
    med = statistics.median(ratios) if ratios else 1.0
    pt_per_ft = PT_PER_FT * med

    # 8. exterior line through storefront / windows (secondary metric)
    ALL = collect_lines(drawings, clip, lambda d: True)
    glaz = exterior_glazing_spans(runs, ALL)

    # 9. report
    def ft(x): return round(x / pt_per_ft, 2)
    per_type = defaultdict(lambda: dict(gross_lf=0.0, net_lf=0.0, runs=0))
    run_out = []
    for i, r in enumerate(runs):
        g, n = length_pt(r), length_pt(r, net=True)
        k = r['type']
        per_type[k]['gross_lf'] += g / pt_per_ft
        per_type[k]['net_lf'] += n / pt_per_ft
        per_type[k]['runs'] += 1
        if r['orient'] == 'H':
            p0, p1 = (r['a'], r['c']), (r['b'], r['c'])
        else:
            p0, p1 = (r['c'], r['a']), (r['c'], r['b'])
        run_out.append(dict(id=i, type=k, type_source=r['type_source'], geometry_class=r['cls'],
                            orient=r['orient'],
                            start_pt=[round(v, 2) for v in p0], end_pt=[round(v, 2) for v in p1],
                            thickness_in=round((r['c2'] - r['c1'] + BOARD * (int(r['bodies'][0]['board_l']) + int(r['bodies'][0]['board_r']))) / PT_PER_FT * 12, 2),
                            gross_lf=ft(g), net_lf=ft(n),
                            openings_lf=[ft(e - s) for s, e in r['openings']],
                            candidates=r['candidates'] or None, parent_run=r['parent'],
                            tags=[{'tag': t, 'tick_pt': [round(x['x'], 1), round(x['y'], 1)], 'bind': x['bind']}
                                  for _, t, x in r['ticks']]))
    summary = {k: dict(gross_lf=round(v['gross_lf'], 1), net_lf=round(v['net_lf'], 1), runs=v['runs'])
               for k, v in sorted(per_type.items())}
    result = dict(
        sheet=os.path.basename(pdf), clip_pt=list(clip),
        units='linear feet (LF), wall centerline; gross = through door openings, net = openings removed',
        scale=dict(nominal='1/4" = 1\'-0" (18 pt/ft)', calibration_samples=len(cal),
                   median_ratio=round(med, 5),
                   ratio_min=round(min(ratios), 5) if ratios else None,
                   ratio_max=round(max(ratios), 5) if ratios else None,
                   pt_per_ft_used=round(pt_per_ft, 4), samples=cal),
        counts=dict(wall_lines_H=len(L5[0]), wall_lines_V=len(L5[1]), oblique_wall_segments_ignored=n_oblique,
                    bodies=len(bodies), runs=len(runs), tags=len(tags), ticks=len(ticks),
                    ticks_unbound=len(unbound)),
        per_type=summary,
        exterior_through_glazing=dict(
            note='EXT 8in wall line continued across storefront/window openings between solid 8in runs; '
                 'the plan cannot say which height/assembly applies above or below the glass',
            lf=round(sum(e - s for _, _, s, e in glaz) / pt_per_ft, 1),
            spans=[dict(orient=o, c_pt=round(c, 2), from_pt=round(s, 2), to_pt=round(e, 2), lf=ft(e - s))
                   for o, c, s, e in glaz]),
        runs=run_out,
        unbound_ticks=[dict(tag=t['tag'], at=[round(t['x'], 1), round(t['y'], 1)]) for t in unbound])
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, 'results.json'), 'w') as f:
        json.dump(result, f, indent=1)
    draw_overlay(pdf, runs, clip, os.path.join(outdir, 'overlay.png'), glaz)
    for k, v in summary.items():
        print(f'{k:28s} gross {v["gross_lf"]:7.1f}  net {v["net_lf"]:7.1f}  runs {v["runs"]}')
    print('exterior line through glazing', result['exterior_through_glazing']['lf'], 'LF')
    print('scale median ratio', round(med, 5), 'from', len(cal), 'dimension strings')
    return result


TYPE_COLORS = {
    'A3A': (0.95, 0.80, 0.0), 'A3B': (0.95, 0.25, 0.25), 'A6A': (0.1, 0.75, 0.1),
    'A6B': (0.0, 0.6, 0.65), 'D3A': (0.9, 0.2, 0.85), 'D3C': (0.15, 0.3, 0.95),
    'EXT 8in stud (exterior)': (0.55, 0.3, 0.15),
}


def draw_overlay(pdf, runs, clip, out, glaz=(), zoom=1.1):
    doc = pymupdf.open(pdf)
    pg = doc[0]
    sh = pg.new_shape()
    for r in runs:
        col = TYPE_COLORS.get(r['type'], (0.5, 0.5, 0.5))
        if r['orient'] == 'H':
            p0, p1 = (r['a'], r['c']), (r['b'], r['c'])
        else:
            p0, p1 = (r['c'], r['a']), (r['c'], r['b'])
        sh.draw_line(p0, p1)
        sh.finish(color=col, width=3.2, stroke_opacity=0.75, lineCap=1)
        if r['type_source'] == 'propagated-ambiguous':
            sh.draw_line(p0, p1)
            sh.finish(color=(0, 0, 0), width=0.8, dashes='[2 2] 0')
        for s, e in r['openings']:      # openings drawn dashed white over the run
            q0, q1 = ((s, r['c']), (e, r['c'])) if r['orient'] == 'H' else ((r['c'], s), (r['c'], e))
            sh.draw_line(q0, q1)
            sh.finish(color=(1, 1, 1), width=1.4, dashes='[3 3] 0')
    for o, c, s, e in glaz:
        p0, p1 = ((s, c), (e, c)) if o == 'H' else ((c, s), (c, e))
        sh.draw_line(p0, p1)
        sh.finish(color=TYPE_COLORS['EXT 8in stud (exterior)'], width=1.6, dashes='[5 3] 0', stroke_opacity=0.8)
    sh.commit()
    # legend
    y = clip.y1 - 13 * (len(TYPE_COLORS) + 5)
    x = clip.x1 - 190
    pg.draw_rect(pymupdf.Rect(x - 6, y - 14, clip.x1 - 4, clip.y1 - 4), color=(0, 0, 0), fill=(1, 1, 1), width=0.5)
    pg.insert_text((x, y), 'vector-measured runs (gross)', fontsize=9)
    for k, col in list(TYPE_COLORS.items()) + [('untagged / other', (0.5, 0.5, 0.5))]:
        y += 13
        pg.draw_line((x, y - 3), (x + 22, y - 3), color=col, width=3.2)
        pg.insert_text((x + 28, y), k, fontsize=8.5)
    y += 13
    pg.draw_line((x, y - 3), (x + 22, y - 3), color=TYPE_COLORS['EXT 8in stud (exterior)'], width=1.6, dashes='[5 3] 0')
    pg.insert_text((x + 28, y), 'EXT line through glazing', fontsize=8.5)
    y += 13
    pg.draw_line((x, y - 3), (x + 22, y - 3), color=(0, 0, 0), width=0.8, dashes='[2 2] 0')
    pg.insert_text((x + 28, y), 'type ambiguous (needs review)', fontsize=8.5)
    y += 13
    pg.draw_line((x, y - 3), (x + 22, y - 3), color=(1, 1, 1), width=3)
    pg.draw_line((x, y - 3), (x + 22, y - 3), color=(0.4, 0.4, 0.4), width=1.4, dashes='[3 3] 0')
    pg.insert_text((x + 28, y), 'door opening (gross only)', fontsize=8.5)
    pg.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), clip=clip).save(out)


if __name__ == '__main__':
    main(sys.argv[1:])
