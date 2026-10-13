"""09a wall framing + drywall: rebuild every estimate quantity from markup legend rows.
Quantities only. Writes reconciliation.csv and fixtures.json into the trade folder and
prints a summary plus TakeoffSpeed-engine comparison numbers."""
import json, math, csv
from fractions import Fraction as F

REF = '/home/user/takeoffspeed-reference-data'
OUT = f'{REF}/trades/09a-wall-framing-drywall'
L = {l['lineNo']: l for l in json.load(open(f'{REF}/reference/estimate/lines.json'))}
IDS = [t for t in json.load(open(f'{REF}/reference/estimate/trades.json')) if t['trade'] == '09a-wall-framing-drywall'][0]['lines']
G = json.load(open(f'{REF}/reference/markups/legends.json'))


def leg(page, name, prefix=False):
    for p in G:
        if p['page'] == page:
            for it in p['items']:
                if it['name'] == name or (prefix and it['name'].startswith(name)):
                    return float(it['quantity'])
    raise KeyError((page, name))


def fi(f, i=0):
    return f + i / 12


def ceil_to(x, step):
    return math.ceil(round(x / step, 9)) * step


# ---------------- measured legend rows: key -> (page, sheet, legend name, value, unit) ----------------
SRC = {
    'A6B': (4, 'A-120', 'WALL A6B @ 12\'6"H'), 'A3B': (4, 'A-120', 'WALL A3B @ 12\'6"H'),
    'A6A': (4, 'A-120', 'WALL A6A @ 12\'6"H'), 'A3A': (4, 'A-120', 'WALL A3A @ 12\'6"H'),
    'D3C': (4, 'A-120', 'WALL D3C @ 12\'6"H 1 SIDE'), 'D3A': (4, 'A-120', 'WALL D3A @ 12\'6"H 1 SIDE'),
    'EXT8_129': (4, 'A-120', 'EXT 8" STUD WALL @ 12\'9"H'), 'EXT6_123': (4, 'A-120', 'EXT 6" STUD WALL @ 12\'3"H SHTNG 10\'3"H'),
    'PAR_72': (4, 'A-120', 'PARAPET WALL @ 7\'2"H A310'), 'EXT8_159': (4, 'A-120', 'EXT 8" STUD WALL @ 15\'9"H'),
    'EXT8_4': (4, 'A-120', 'EXT 8" STUD WALL @ 4\'H'), 'EXT8_159_NOGWB': (4, 'A-120', 'EXT 8" STUD WALL @ 15\'9"H NO GWB'),
    'DBL_188': (4, 'A-120', '6" & 3-5/8" METAL STUD @ 18\'8"H, BS 1/2" SHTNG ONLY'),
    'S6_44': (4, 'A-120', '6" METAL STUD WALL @ 4\'4" HT, BS GWB'), 'A3A_39': (4, 'A-120', 'WALL A3A @ 3\'9"H (NO INS)'),
    'MECHO': (5, 'A-130', 'MOTORIZED MECHOSHADE'),
    'PAR_27': (7, 'A-140', 'PARAPET WALL @ 2\'7"H'), 'PAR_17': (7, 'A-140', 'PARAPET WALL @ 1\'7"H'), 'PAR_47': (7, 'A-140', 'PARAPET WALL @ 4\'7"H'),
    'ROOFSTEP': (7, 'A-140', '8/A450 LAP ROOF 2\', INCL WALL'),
    'PT1_RR': (16, 'A-410', 'PT1 WALL PAINT'),
    'WT9_410': (16, 'A-410', 'WT9 WALL TILE'), 'WT2_410': (16, 'A-410', 'WT2 WALL TILE'), 'WT1_410': (16, 'A-410', 'WT1 WALL TILE'),
    'WT1_703': (27, 'A-703', 'WT1 WALL TILE'), 'WT2_703': (27, 'A-703', 'WT2 WALL TILE'), 'WT9_703': (27, 'A-703', 'WT9 WALL TILE'),
    'WT1_705': (32, 'A-705', 'WT1 WALL TILE'), 'WT2_705': (32, 'A-705', 'WT2 WALL TILE'), 'WT9_705': (32, 'A-705', 'WT9 WALL TILE'),
    'WT3_700': (23, 'A-700', 'WT3 TILE'), 'CBB14_700': (23, 'A-700', '1/4" CEMENTITIOUS BACKER BOARD'),
    'TYPEX_704': (28, 'A-704', 'TYPE X GWB'),
    'BOOTH_706': (29, 'A-706', '6"THK. 16GA. METAL STUD @ 12" O.C'),
    'CANOPY_S203': (34, 'S-203', '6" METAL STUD CANOPY FRAMING @ 16" O.C'),
}
R = {k: leg(p, n, prefix=(k == 'BOOTH_706')) for k, (p, s, n) in SRC.items()}
H = {'12-6': fi(12, 6), '12-9': fi(12, 9), '12-3': fi(12, 3), '7-2': fi(7, 2), '15-9': fi(15, 9), '4-0': 4.0, '18-8': fi(18, 8),
     '4-4': fi(4, 4), '3-9': fi(3, 9), '3-0': 3.0, '2-0': 2.0, '9-0': 9.0, '1-7': fi(1, 7), '2-7': fi(2, 7), '4-7': fi(4, 7)}
HLBL = {'12-6': "12'-6\"", '12-9': "12'-9\"", '12-3': "12'-3\"", '7-2': "7'-2\"", '15-9': "15'-9\"", '4-0': "4'-0\"", '18-8': "18'-8\"",
        '4-4': "4'-4\"", '3-9': "3'-9\"", '3-0': "3'-0\"", '2-0': "2'-0\"", '9-0': "9'-0\"", '1-7': "1'-7\"", '2-7': "2'-7\"", '4-7': "4'-7\""}


def pg(k):
    return f'p{SRC[k][0]}'


# ---------------- stud groups (line -> [(row keys, height key, judgment note)]) ----------------
STUDS = {
    308: [(['A3B', 'A3A', 'D3C', 'D3A'], '12-6', ''), (['A3A_39'], '3-9', ''), (['DBL_188'], '18-8', '3-5/8" half of the double-stud wall'),
          (['MECHO'], '3-0', 'height 3\' is the estimator\'s assumption (A-430 det. 8 undimensioned)'), (['ROOFSTEP'], '2-0', 'high-low roof step wall, A-450 det. 8 & 10')],
    309: [(['A6B', 'A6A'], '12-6', ''), (['S6_44'], '4-4', '')],
    310: [(['PAR_72'], '9-0', '6" lower wall under the 7\'2" parapet at the VAT (A-310 sec. 1); 9\' is the estimator\'s height'),
          (['EXT6_123'], '12-3', ''), (['DBL_188'], '18-8', '6" half of the double-stud wall')],
    311: [(['PAR_17'], '1-7', ''), (['PAR_27'], '2-7', ''), (['EXT8_4'], '4-0', ''), (['PAR_47'], '4-7', ''), (['PAR_72'], '7-2', 'upper 8" part of the VAT wall'),
          (['EXT8_129'], '12-9', ''), (['EXT8_159', 'EXT8_159_NOGWB'], '15-9', '')],
}
EST_COUNTS = {308: {'2-0': 35, '3-0': 56, '3-9': 6, '12-6': 101, '18-8': 6}, 309: {'4-4': 14, '12-6': 50},
              310: {'9-0': 4, '12-3': 7, '18-8': 6}, 311: {'1-7': 35, '2-7': 29, '4-0': 10, '4-7': 73, '7-2': 5, '12-9': 68, '15-9': 38}}
RUNNER_OF = {314: 308, 318: 308, 315: 309, 319: 309, 316: 310, 320: 310, 317: 311, 321: 311}

out, fixtures = {}, []


def put(n, src, vals, formula, q, cls, notes=''):
    out[n] = dict(source=src, sourceValues=vals, formula=formula, recomputed=q, classification=cls, notes=notes)


def fx(name, formula, inputs, n, tol, src):
    fixtures.append(dict(name=name, formula=formula, inputs=inputs, expected=dict(quantity=L[n]['quantity'], unit=L[n]['unit']),
                         tolerancePct=tol, source=f'line {n} / {src}'))


def tol_for(est, q):
    d = abs(q / est - 1) * 100
    return 0.01 if d < 0.005 else math.ceil(d * 2 + 0.2) / 2


stud_summary = {}
for n, groups in STUDS.items():
    sf, lf, parts, rows_in = 0.0, 0.0, [], []
    cnt = {}
    for keys, h, note in groups:
        g_lf = sum(R[k] for k in keys)
        sf += g_lf * H[h]; lf += g_lf
        cnt[h] = math.ceil(round(g_lf * 12 / 16, 9))
        parts.append(f"{'+'.join(f'{k} {R[k]}' for k in keys)} LF [{','.join(sorted({pg(k) for k in keys}))}] x {HLBL[h]}")
        rows_in.append({'runLF': round(g_lf, 2), 'height_ft': round(H[h], 6), 'height': HLBL[h], 'rows': keys})
    mism = {HLBL[h]: (cnt[h], EST_COUNTS[n][h]) for h in cnt if cnt[h] != EST_COUNTS[n][h]}
    stud_summary[n] = dict(sf=sf, lf=lf, cnt=cnt)
    judg = '; '.join(f'{HLBL[h]}: {note}' for _, h, note in groups if note)
    put(n, 'markups ' + '/'.join(sorted({pg(k) for keys, _, _ in groups for k in keys})), '; '.join(parts),
        'SF = sum(LF_row x H_row)', sf, 'derived (measured LF x height)',
        (f'{judg}. ' if judg else '') + f'stud-count note check ceil(LF x 12/16): ' +
        ('all groups match' if not mism else 'mismatches (calc, est) ' + ', '.join(f'{k} {v}' for k, v in mism.items())))
    fx(f'stud-sf-{n}', 'stud_sf = sum(runLF x height)', {'groups': rows_in, 'spacing_in': 16, 'units': 'LF, ft'}, n, tol_for(L[n]['quantity'], sf),
       '/'.join(sorted({pg(k) for keys, _, _ in groups for k in keys})))

for n, parent in RUNNER_OF.items():
    lf = stud_summary[parent]['lf']
    put(n, f'same legend rows as line {parent}', ' + '.join(f'{R[k]}' for keys, _, _ in STUDS[parent] for k in keys),
        'runner LF = sum(row LF) of the stud line (top = bottom; no door deduction)', lf, 'derived (measured LF)',
        f'estimator carries {L[n]["quantity"] - lf:+.1f} LF more than the legend rows; no legend row accounts for it')
    fx(f'runner-{n}', 'runner_lf = sum(runLF)', {'runLF': [round(R[k], 2) for keys, _, _ in STUDS[parent] for k in keys], 'units': 'LF'}, n,
       tol_for(L[n]['quantity'], lf), f'rows of line {parent}')

put(312, 'markup p29 (A-706)', f'booth roof framing area {R["BOOTH_706"]} SF', 'LF = ceil(SF) x 12 / 12" o.c.', math.ceil(R['BOOTH_706']) * 12 / 12,
    'derived (measured area)', 'joists at 12" o.c. = 1 LF per SF of framed area; area rounded up to whole SF (76.2 -> 77; PT-5 line 302 uses the same 77)')
fx('booth-ceiling-framing-312', 'lf = ceil(areaSF) x 12 / spacing_in', {'areaSF': R['BOOTH_706'], 'spacing_in': 12}, 312, 0.01, 'p29')
put(313, 'markup p34 (S-203)', f'canopy framing area {R["CANOPY_S203"]} SF', 'LF = ceil5(SF) / 1.33  (16" o.c. written as 1.33 ft)', ceil_to(R['CANOPY_S203'], 5) / 1.33,
    'derived (measured area)', 'area rounded up to next 5 SF (416.9 -> 420); 1.33 is the estimator\'s rounded 16/12; exact 12/16 gives 315.0 (-0.25%)')
fx('canopy-framing-313', 'lf = ceil(areaSF/5)*5 / 1.33', {'areaSF': R['CANOPY_S203'], 'spacing_in': 16, 'spacingFtConvention': 1.33}, 313, 0.01, 'p34')

# ---------------- boards ----------------
GROSS = [('A6B', '12-6', 2), ('A3B', '12-6', 2), ('A6A', '12-6', 2), ('A3A', '12-6', 2), ('D3C', '12-6', 1), ('D3A', '12-6', 1),
         ('EXT8_129', '12-9', 1), ('EXT6_123', '12-3', 1), ('EXT8_159', '15-9', 1), ('EXT8_4', '4-0', 1), ('S6_44', '4-4', 2), ('A3A_39', '3-9', 2)]
gross = sum(R[k] * H[h] * f for k, h, f in GROSS)
TILE_W = ['WT1_410', 'WT2_410', 'WT9_410', 'WT1_703', 'WT2_703', 'WT9_703', 'WT1_705', 'WT2_705', 'WT9_705']
tile_walls = sum(R[k] for k in TILE_W)
tile_all = tile_walls + R['WT3_700']
gwb = gross - R['PT1_RR'] - tile_walls - R['TYPEX_704']
put(242, 'markup p4 (A-120) less p16/p27/p32/p28 specialty areas',
    f'gross {gross:.2f} SF = ' + ' + '.join(f'{k} {R[k]}x{HLBL[h]}x{f}' for k, h, f in GROSS) +
    f'; less MR (restroom PT1) {R["PT1_RR"]}, wall tile {tile_walls:.1f}, Type X {R["TYPEX_704"]}',
    'SF = sum(LF x H x faces) - MR area - wall-tile (cement board) area - Type X area', gwb, 'derived (measured LF x height x faces, net of specialty boards)',
    'faces: A-series 2, D-series 1, exterior walls 1 (interior face), "BS GWB" rows 2; parapets, "NO GWB" and "BS 1/2" SHTNG ONLY" rows excluded; no door/window deduction; residual -9.3 SF')
fx('gwb-walls-242', 'sf = sum(runLF x height x faces) - sum(specialtyAreaSF)',
   {'rows': [{'key': k, 'runLF': R[k], 'height_ft': round(H[h], 6), 'faces': f} for k, h, f in GROSS],
    'specialtyAreaSF': {'MR_restroomPaint': R['PT1_RR'], 'wallTile': round(tile_walls, 1), 'typeX': R['TYPEX_704']}}, 242, tol_for(L[242]['quantity'], gwb), 'p4,p16,p27,p28,p32')

put(248, 'markup p28 (A-704)', f'TYPE X GWB {R["TYPEX_704"]} SF', 'SF = ceil5(measured SF)', ceil_to(R['TYPEX_704'], 5), 'measured (area)', '37.2 -> 40: rounded UP to the next 5 SF (round-to-5 would give 35)')
fx('typex-248', 'sf = ceil(areaSF/5)*5', {'areaSF': R['TYPEX_704']}, 248, 0.01, 'p28')
par = [('PAR_17', '1-7'), ('PAR_27', '2-7'), ('PAR_47', '4-7'), ('PAR_72', '7-2')]
par_exact = sum(R[k] * H[h] for k, h in par)
par_ceil = sum(math.ceil(round(R[k] * H[h], 9)) for k, h in par)
put(254, 'markups p7 (A-140) + p4 (A-120)', '; '.join(f'{k} {R[k]} LF x {HLBL[h]} = {R[k]*H[h]:.2f}' for k, h in par),
    'SF = sum(ceil(LF x H)) per parapet row, one (roof-side) face', par_ceil, 'derived (measured LF x height)',
    f'unrounded sum = {par_exact:.2f} SF ({(par_exact/658-1)*100:+.2f}%); per-row ceil to whole SF reproduces 658 exactly')
fx('glassmat-parapet-254', 'sf = sum(ceil(runLF x height)) ; faces = 1', {'rows': [{'key': k, 'runLF': R[k], 'height_ft': round(H[h], 6)} for k, h in par]}, 254, 0.01, 'p7,p4')
put(260, 'markup p16 (A-410)', f'PT1 WALL PAINT (restroom elevations) {R["PT1_RR"]} SF', 'SF = ceil5(restroom painted-wall SF)', ceil_to(R['PT1_RR'], 5),
    'measured (area)', 'MR board = the painted (non-tile) wall faces in the wet rooms; FRP-1 (16 SF) is not included')
fx('mr-board-260', 'sf = ceil(areaSF/5)*5', {'areaSF': R['PT1_RR']}, 260, 0.01, 'p16')
put(266, 'markups p16, p27, p32, p23', f'WT1/WT2/WT9 on walls {tile_walls:.1f} + WT3 at transaction bar {R["WT3_700"]} = {tile_all:.1f} SF', 'SF = ceil5(sum of wall-tile SF)',
    ceil_to(tile_all, 5), 'measured (area)', 'includes the WT3 38.4 SF at the transaction bar, which also carries the 1/4" backer (line 272): 38.4 SF of backer counted twice; walls only = ceil5(244.2) = 245')
fx('cement-board-266', 'sf = ceil(sum(tileAreaSF)/5)*5', {'tileAreaSF': {k: R[k] for k in TILE_W + ['WT3_700']}}, 266, 0.01, 'p16,p23,p27,p32')
put(272, 'markup p23 (A-700)', f'1/4" CEMENTITIOUS BACKER BOARD {R["CBB14_700"]} SF', 'SF = ceil5(measured SF)', ceil_to(R['CBB14_700'], 5), 'measured (area)', 'transaction-bar face under WT3 tile')
fx('cement-board-quarter-272', 'sf = ceil(areaSF/5)*5', {'areaSF': R['CBB14_700']}, 272, 0.01, 'p23')

# ---------------- accessory lines (per-SF ratios of the parent board line) ----------------
RAT = {'NO. OF SHEETS': ('sheets = SF / 32 (4x8)', F(1, 32)), 'ADHESIVE': ('tubes = SF x 0.031', F(31, 1000)),
       'TAPING': ('rolls = SF x 0.00075 (0.375 LF/SF / 500 LF roll)', F(3, 4000)),
       'DRYWALL SCREWS': ('lb = SF x 3/560 (0.0053571 lb/SF)', F(3, 560)), 'MUD PLASTER': ('lb = SF x 0.53', F(53, 100))}
PARENTS = [242, 248, 254, 260, 266, 272]
for parent in PARENTS:
    for k in range(1, 6):
        n = parent + k
        d = L[n]['description']
        f, r = RAT[d]
        pq = L[parent]['quantity']
        exact = pq * float(r)
        chain = out[parent]['recomputed'] * float(r)
        put(n, f'line {parent}', f'parent SF {pq} (estimator) / {out[parent]["recomputed"]:.3f} (rebuilt)', f, chain, 'derived (estimator ratio)',
            f'ratio exact on the estimator parent: {exact:.6f} vs {L[n]["quantity"]} ({(exact/L[n]["quantity"]-1)*100:+.4f}%); recomputedQty uses the rebuilt parent')
        fx(f'{d.lower().replace(".", "").replace(" ", "-")}-{n}', f, {'parentSF': pq, 'ratio': f'{r.numerator}/{r.denominator}'}, n, 0.01, f'line {parent}')

rows = []
for n in IDS:
    l = L[n]; o = out[n]
    est = l['quantity']; rq = o['recomputed']
    dd = (rq / est - 1) * 100
    desc = l['description'].split('\n')[0].strip()
    if desc in RAT:
        p = [x for x in PARENTS if x < n][-1]
        desc = f'{desc} ({L[p]["description"].split(" AT")[0]})'
    rows.append(dict(lineNo=n, description=desc, unit=l['unit'], estimatorQty=round(est, 6), source=o['source'], sourceValues=o['sourceValues'],
                     formula=o['formula'], recomputedQty=round(rq, 6), deltaPct=round(dd, 3), classification=o['classification'], notes=o['notes']))
with open(f'{OUT}/reconciliation.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
json.dump(fixtures, open(f'{OUT}/fixtures.json', 'w'), indent=1)
for r in rows:
    print(r['lineNo'], r['unit'], r['estimatorQty'], round(r['recomputedQty'], 4), f"{r['deltaPct']:+.3f}%")
w1 = sum(abs(r['deltaPct']) <= 1 for r in rows); w5 = sum(abs(r['deltaPct']) <= 5 for r in rows)
print('within1', w1, 'within5', w5, 'of', len(rows), 'fixtures', len(fixtures))
print('gross', round(gross, 3), 'tile_walls', round(tile_walls, 2), 'tile_all', round(tile_all, 2), 'gwb', round(gwb, 3), 'par_exact', round(par_exact, 3))

# ---------------- engine comparison (reviewed-commercial profile, one record per legend row, single run) ----------------
print('\nENGINE-STYLE stud SF = ceil(run*12/16) x H x 16/12 per record (run-end 0):')
for n, groups in STUDS.items():
    e = 0.0
    for keys, h, _ in groups:
        for k in keys:
            e += math.ceil(round(R[k] * 12 / 16, 9)) * H[h] * 16 / 12
    print(n, round(e, 2), 'est', L[n]['quantity'], f'{(e/L[n]["quantity"]-1)*100:+.2f}%', ' legend-LFxH', round(stud_summary[n]['sf'], 2))
# default profile: run-end +1 per run
print('default profile run-end +1:')
for n, groups in STUDS.items():
    e = sum((math.ceil(round(R[k] * 12 / 16, 9)) + 1) * H[h] * 16 / 12 for keys, h, _ in groups for k in keys)
    print(n, round(e, 2), f'{(e/L[n]["quantity"]-1)*100:+.2f}%')
# runner = stud count x spacing (doc claim)
for n in (308, 309, 310, 311):
    c = sum(EST_COUNTS[n].values()) * 16 / 12
    print('runner as count x 16/12', n, round(c, 2), 'vs est', L[n + 6]['quantity'], f'{(c/L[n+6]["quantity"]-1)*100:+.2f}%')
# door deductions if openings are entered on the partitions
doors_sf = 6 * 3 * 7 + (3 + 4 / 12) * 7
print('door SF per face', round(doors_sf, 2), 'x2 faces', round(2 * doors_sf, 2), f'{-2*doors_sf/L[242]["quantity"]*100:.2f}% of 242')
# backer board via engine backerBoardLines
for n in (266, 272):
    sf = L[n]['quantity']
    print('backer', n, 'sheets@15', round(sf / 15, 3), 'vs', L[n + 1]['quantity'], '| mesh tape rolls', round(sf * 0.53 / 150, 4), 'vs tape', L[n + 3]['quantity'],
          '| screws EA', sf * 1.5)
# booth illustration
print('booth illustrative: 8ft x', round(76.2 / 8, 3), 'span: joists', math.ceil(8 * 12 / 12) + 1, 'x', round(76.2 / 8, 3), '=', round((math.ceil(8) + 1) * 76.2 / 8, 2))
print('canopy exact 12/16', round(420 * 0.75, 3), 'no-ceil', round(416.9 * 0.75, 3))
print('screw ratio profile 0.005357 on 242:', round(6004.8655 * 0.005357, 4), 'vs', L[246]['quantity'])
