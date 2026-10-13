"""Evaluate results.json against the estimator's colored PlanSwift markup.

    python3 -I compare_to_markup.py [results.json]

The markup (MARKUPS ... p01-10.pdf, page 4) is a 200 dpi raster of the whole
A-120 sheet, so sheet points map to markup pixels by 7199/2592.  For every
measured run we sample the markup colour along its centerline (+-5 pt) and
read which legend row the estimator assigned there.  Legend colours repeat
(A6A = 6in@4'4" = A3A@3'9" green; A6B = EXT 8in NO GWB teal; A3B = 6&3-5/8
salmon), so the colour is interpreted together with our geometry family.
Then the reverse: estimator-coloured pixels farther than 7 pt from any run
are grouped into 'estimator measured, we did not' clusters.

This is evaluation only.  Nothing here feeds back into extract_walls.py.
"""
import json, math, os, sys, glob, re
from collections import Counter, defaultdict
import pymupdf

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
LEGEND = {  # legend swatch colours sampled from the markup legend
    'teal': (100, 178, 178), 'salmon': (255, 101, 101), 'green': (101, 254, 101),
    'yellow': (255, 255, 101), 'blue': (101, 102, 255), 'magenta': (255, 101, 255),
    'brown': (177, 101, 101), 'midgreen': (101, 178, 100), 'olive': (177, 178, 100),
    'slate': (102, 101, 177), 'orchid': (178, 101, 179),
}
EST_LF = {'A6B': 28.4, 'A3B': 34.2, 'A6A': 36.7, 'A3A': 49.9, 'D3C': 3.7, 'D3A': 46.0,
          'EXT8 @12\'9"': 89.7, 'EXT6 @12\'3"': 9.2, 'PARAPET @7\'2"': 5.9, 'EXT8 @15\'9"': 41.5,
          'EXT8 @4\'H': 13.0, 'EXT8 @15\'9" NO GWB': 8.7, '6&3-5/8 BS SHTNG @18\'8"': 8.4,
          '6in @4\'4" BS GWB': 18.3, 'A3A @3\'9"H': 7.7}


def markup_raster():
    f = [f for f in glob.glob(os.path.join(ROOT, 'source/markups/MARKUPS*.pdf')) if '_p01-10' in f][0]
    doc = pymupdf.open(f)
    page = doc[3]
    infos = sorted(page.get_image_info(xrefs=True), key=lambda i: i['bbox'][1])
    parts = [pymupdf.Pixmap(doc, i['xref']) for i in infos]
    W = parts[0].width; Ht = sum(p.height for p in parts)
    out = pymupdf.Pixmap(pymupdf.csRGB, pymupdf.IRect(0, 0, W, Ht), False)
    y = 0
    for p in parts:
        if p.n != 3:
            p = pymupdf.Pixmap(pymupdf.csRGB, p)
        p.set_origin(0, y); out.copy(p, p.irect); y += p.height
    return out


def classify_px(c):
    if max(c) - min(c) < 50:
        return None
    best = min(LEGEND.items(), key=lambda kv: sum((a - b) ** 2 for a, b in zip(kv[1], c)))
    return best[0] if sum((a - b) ** 2 for a, b in zip(best[1], c)) < 60 ** 2 else None


def label(color, family):
    """Estimator legend row implied by colour + our geometry family."""
    interior = family in ('A3', 'A6', 'D3')
    m = {'teal': 'A6B' if family == 'A6' else 'EXT8 @15\'9" NO GWB',
         'salmon': 'A3B' if family == 'A3' else '6&3-5/8 BS SHTNG @18\'8"',
         'green': {'A6': 'A6A', 'A3': 'A3A @3\'9"H'}.get(family, '6in @4\'4" BS GWB'),
         'yellow': 'A3A', 'blue': 'D3C', 'magenta': 'D3A', 'brown': 'EXT8 @12\'9"',
         'midgreen': 'EXT6 @12\'3"', 'olive': 'PARAPET @7\'2"', 'slate': 'EXT8 @15\'9"',
         'orchid': 'EXT8 @4\'H'}
    return m.get(color)


def main(path):
    res = json.load(open(path))
    ppf = res['scale']['pt_per_ft_used']
    pm = markup_raster()
    S = pm.width / 2592.0
    st, smp = pm.stride, pm.samples

    def px(x, y):
        X, Y = int(x * S), int(y * S)
        if not (0 <= X < pm.width and 0 <= Y < pm.height):
            return (255, 255, 255)
        i = Y * st + X * 3
        return (smp[i], smp[i + 1], smp[i + 2])

    rows = []
    confusion = defaultdict(float)
    for r in res['runs']:
        (x0, y0), (x1, y1) = r['start_pt'], r['end_pt']
        horiz = r['orient'] == 'H'
        L = math.hypot(x1 - x0, y1 - y0)
        n = max(2, int(L / 1.0))
        votes = Counter(); covered = 0
        for k in range(n + 1):
            x = x0 + (x1 - x0) * k / n; y = y0 + (y1 - y0) * k / n
            here = Counter()
            for d in [v * 0.5 for v in range(-10, 11)]:
                c = classify_px(px(x, y + d) if horiz else px(x + d, y))
                if c:
                    here[c] += 1
            if here:
                covered += 1
                votes[here.most_common(1)[0][0]] += 1
        fam = r['geometry_class'] if r['geometry_class'] in ('A3', 'A6', 'D3', 'EXT8') else 'other'
        est = label(votes.most_common(1)[0][0], fam) if votes and covered / (n + 1) >= 0.3 else None
        frac = covered / (n + 1)
        rows.append(dict(id=r['id'], ours=r['type'], src=r['type_source'], lf=r['gross_lf'],
                         estimator=est or '(not marked)', marked_fraction=round(frac, 2)))
        confusion[(r['type'], est or '(not marked)')] += r['gross_lf']

    # reverse: estimator pixels far from every run
    segs = [(r['start_pt'], r['end_pt']) for r in res['runs']]
    def dseg(p, a, b):
        ax, ay = a; bx, by = b; px_, py_ = p
        L2 = (bx - ax) ** 2 + (by - ay) ** 2
        t = 0 if L2 == 0 else max(0, min(1, ((px_ - ax) * (bx - ax) + (py_ - ay) * (by - ay)) / L2))
        return math.hypot(px_ - ax - t * (bx - ax), py_ - ay - t * (by - ay))
    x0, y0, x1, y1 = res['clip_pt']
    miss = defaultdict(list)
    step = 1.5
    yy = y0
    while yy < y1:
        xx = x0
        while xx < x1:
            c = classify_px(px(xx, yy))
            # skip the markup's legend box (lower-left of the plan)
            if c and not (xx < 720 and yy > 1420):
                if min(dseg((xx, yy), a, b) for a, b in segs) > 7:
                    miss[c].append((xx, yy))
            xx += step
        yy += step
    clusters = []
    for c, pts in miss.items():
        pts = set(pts); seen = set()
        for p in list(pts):
            if p in seen:
                continue
            comp = []; stack = [p]; seen.add(p)
            while stack:
                q = stack.pop(); comp.append(q)
                for dx in (-step, 0, step):
                    for dy in (-step, 0, step):
                        nb = (round(q[0] + dx, 6), round(q[1] + dy, 6))
                        for cand in ((q[0] + dx, q[1] + dy), nb):
                            if cand in pts and cand not in seen:
                                seen.add(cand); stack.append(cand)
            if len(comp) < 6:
                continue
            xs = [q[0] for q in comp]; ys = [q[1] for q in comp]
            span = max(max(xs) - min(xs), max(ys) - min(ys))
            clusters.append(dict(color=c, bbox_pt=[round(min(xs)), round(min(ys)), round(max(xs)), round(max(ys))],
                                 approx_lf=round(span / ppf, 1), pixels=len(comp)))
    clusters.sort(key=lambda d: -d['approx_lf'])
    out = dict(per_run=rows,
               confusion_lf=[dict(ours=a, estimator=b, lf=round(v, 1)) for (a, b), v in sorted(confusion.items())],
               estimator_marked_not_measured=[c for c in clusters if c['approx_lf'] >= 1.0])
    with open(os.path.join(os.path.dirname(path), 'markup_comparison.json'), 'w') as f:
        json.dump(out, f, indent=1)
    print('LF by (our type -> estimator colour/legend row):')
    for d in out['confusion_lf']:
        print(f"  {d['ours']:30s} -> {d['estimator']:26s} {d['lf']:6.1f}")
    print('estimator-marked, not measured by us (>=1 ft):')
    for c in out['estimator_marked_not_measured']:
        print('  ', c)


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'results.json'))
