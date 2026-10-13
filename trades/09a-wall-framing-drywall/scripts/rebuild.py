"""Rebuild every 09a estimate quantity from markup legend values (quantities only)."""
import json, math, csv, sys
REF = '/home/user/takeoffspeed-reference-data'
L = {l['lineNo']: l for l in json.load(open(f'{REF}/reference/estimate/lines.json'))}
ids = [t for t in json.load(open(f'{REF}/reference/estimate/trades.json')) if t['trade'] == '09a-wall-framing-drywall'][0]['lines']
G = json.load(open(f'{REF}/reference/markups/legends.json'))
def leg(page, name):
    for p in G:
        if p['page'] == page:
            for it in p['items']:
                if it['name'] == name: return float(it['quantity'])
    raise KeyError((page, name))
def fi(f, i=0): return f + i / 12
def ceil_to(x, step): return math.ceil(round(x / step, 9)) * step

# ---- measured rows (page, legend name) ----
R = {
 'A6B': leg(4, 'WALL A6B @ 12\'6"H'), 'A3B': leg(4, 'WALL A3B @ 12\'6"H'), 'A6A': leg(4, 'WALL A6A @ 12\'6"H'),
 'A3A': leg(4, 'WALL A3A @ 12\'6"H'), 'D3C': leg(4, 'WALL D3C @ 12\'6"H 1 SIDE'), 'D3A': leg(4, 'WALL D3A @ 12\'6"H 1 SIDE'),
 'EXT8_129': leg(4, 'EXT 8" STUD WALL @ 12\'9"H'), 'EXT6_123': leg(4, 'EXT 6" STUD WALL @ 12\'3"H SHTNG 10\'3"H'),
 'PAR_72': leg(4, 'PARAPET WALL @ 7\'2"H A310'), 'EXT8_159': leg(4, 'EXT 8" STUD WALL @ 15\'9"H'),
 'EXT8_4': leg(4, 'EXT 8" STUD WALL @ 4\'H'), 'EXT8_159_NOGWB': leg(4, 'EXT 8" STUD WALL @ 15\'9"H NO GWB'),
 'DBL_188': leg(4, '6" & 3-5/8" METAL STUD @ 18\'8"H, BS 1/2" SHTNG ONLY'), 'S6_44': leg(4, '6" METAL STUD WALL @ 4\'4" HT, BS GWB'),
 'A3A_39': leg(4, 'WALL A3A @ 3\'9"H (NO INS)'),
 'MECHO': leg(5, 'MOTORIZED MECHOSHADE'),
 'PAR_27': leg(7, 'PARAPET WALL @ 2\'7"H'), 'PAR_17': leg(7, 'PARAPET WALL @ 1\'7"H'), 'PAR_47': leg(7, 'PARAPET WALL @ 4\'7"H'),
 'PT1_RR': leg(16, 'PT1 WALL PAINT'),
 'WT9_410': leg(16, 'WT9 WALL TILE'), 'WT2_410': leg(16, 'WT2 WALL TILE'), 'WT1_410': leg(16, 'WT1 WALL TILE'),
 'WT1_703': leg(27, 'WT1 WALL TILE'), 'WT2_703': leg(27, 'WT2 WALL TILE'), 'WT9_703': leg(27, 'WT9 WALL TILE'),
 'WT1_705': leg(32, 'WT1 WALL TILE'), 'WT2_705': leg(32, 'WT2 WALL TILE'), 'WT9_705': leg(32, 'WT9 WALL TILE'),
 'WT3_700': leg(23, 'WT3 TILE'), 'CBB14_700': leg(23, '1/4" CEMENTITIOUS BACKER BOARD'),
 'TYPEX_704': leg(28, 'TYPE X GWB'),
 'BOOTH_706': [it for p in G if p['page'] == 29 for it in p['items'] if it['name'].startswith('6"THK. 16GA. METAL STUD')][0]['quantity'],
 'CANOPY_S203': leg(34, '6" METAL STUD CANOPY FRAMING @ 16" O.C'),
}
H = {'12-6': fi(12, 6), '12-9': fi(12, 9), '12-3': fi(12, 3), '7-2': fi(7, 2), '15-9': fi(15, 9), '4-0': 4.0, '18-8': fi(18, 8),
     '4-4': fi(4, 4), '3-9': fi(3, 9), '3-0': 3.0, '2-0': 2.0, '9-0': 9.0, '1-7': fi(1, 7), '2-7': fi(2, 7), '4-7': fi(4, 7)}

# ---- stud groups: (row label, LF, height key, source) ----
STUD_2FT_LF_INFERRED = 35 * 16 / 12   # 35 studs @ 16" o.c. -> 46.67 LF (no legend row found; see notes)
STUDS = {
 308: [('A3B+A3A+D3C+D3A @12\'6"', R['A3B'] + R['A3A'] + R['D3C'] + R['D3A'], '12-6', 'p4'),
       ('A3A @3\'9" (no ins)', R['A3A_39'], '3-9', 'p4'),
       ('3-5/8" half of double-stud wall @18\'8"', R['DBL_188'], '18-8', 'p4'),
       ('mecho-shade furring @3\'', R['MECHO'], '3-0', 'p5'),
       ('unlocated 3-5/8" row @2\' (inferred from 35 studs)', STUD_2FT_LF_INFERRED, '2-0', 'inferred')],
 309: [('A6B+A6A @12\'6"', R['A6B'] + R['A6A'], '12-6', 'p4'), ('6" wall @4\'4" BS GWB', R['S6_44'], '4-4', 'p4')],
 310: [('VAT lower wall under 7\'2" parapet @9\'', R['PAR_72'], '9-0', 'p4'), ('EXT 6" @12\'3"', R['EXT6_123'], '12-3', 'p4'),
       ('6" half of double-stud wall @18\'8"', R['DBL_188'], '18-8', 'p4')],
 311: [('parapet @1\'7"', R['PAR_17'], '1-7', 'p7'), ('parapet @2\'7"', R['PAR_27'], '2-7', 'p7'), ('EXT 8" @4\'', R['EXT8_4'], '4-0', 'p4'),
       ('parapet @4\'7"', R['PAR_47'], '4-7', 'p7'), ('parapet @7\'2" (A-310)', R['PAR_72'], '7-2', 'p4'), ('EXT 8" @12\'9"', R['EXT8_129'], '12-9', 'p4'),
       ('EXT 8" @15\'9" (+NO GWB)', R['EXT8_159'] + R['EXT8_159_NOGWB'], '15-9', 'p4')],
}
EST_COUNTS = {308: {'2-0': 35, '3-0': 56, '3-9': 6, '12-6': 101, '18-8': 6}, 309: {'4-4': 14, '12-6': 50},
              310: {'9-0': 4, '12-3': 7, '18-8': 6}, 311: {'1-7': 35, '2-7': 29, '4-0': 10, '4-7': 73, '7-2': 5, '12-9': 68, '15-9': 38}}
RUNNER_OF = {314: 308, 318: 308, 315: 309, 319: 309, 316: 310, 320: 310, 317: 311, 321: 311}

out = {}
def put(n, src, vals, formula, q, cls, notes=''):
    out[n] = dict(source=src, sourceValues=vals, formula=formula, recomputed=q, classification=cls, notes=notes)

for n, rows in STUDS.items():
    sf = sum(lf * H[h] for _, lf, h, _ in rows)
    cnt = {h: math.ceil(round(lf * 12 / 16, 9)) for _, lf, h, _ in rows}
    mism = {h: (cnt[h], EST_COUNTS[n][h]) for h in cnt if cnt[h] != EST_COUNTS[n][h]}
    vals = '; '.join(f'{lab}: {lf:.2f} LF x {H[h]:.4f} ft [{src}]' for lab, lf, h, src in rows)
    put(n, 'markups ' + ', '.join(sorted({s for *_, s in rows if s != 'inferred'})), vals, 'SF = sum(LF_row x H_row)', sf,
        'measured+derived' if n != 308 else 'measured+derived (one inferred row)',
        f'stud counts ceil(LF x 12/16) per height: {cnt}; differs from estimator note at {mism}' if mism else f'stud counts ceil(LF x 12/16) per height all match the estimator note {cnt}')
for n, parent in RUNNER_OF.items():
    lf = sum(r[1] for r in STUDS[parent])
    put(n, f'same rows as line {parent}', ' + '.join(f'{r[1]:.2f}' for r in STUDS[parent]), 'runner LF = sum(row LF) (top = bottom, no door deduction)', lf, 'derived')

put(312, 'markup p29 (A-706)', f'booth roof framing area {R["BOOTH_706"]} SF', 'LF = ceil(SF) x 12/12" o.c.', math.ceil(R['BOOTH_706']) * 12 / 12, 'derived', 'joists at 12" o.c.: 1 LF per SF; area rounded up to whole SF (76.2 -> 77)')
put(313, 'markup p34 (S-203)', f'canopy framing area {R["CANOPY_S203"]} SF', 'LF = ceil5(SF) / 1.33 (16" o.c. as 1.33 ft)', ceil_to(R['CANOPY_S203'], 5) / 1.33, 'derived', 'area rounded up to next 5 SF (416.9 -> 420); 1.33 is the estimator\'s rounded 16/12; with 4/3 the result is 315.0')

# ---- boards ----
gross_rows = [('A6B', 'A6B', '12-6', 2), ('A3B', 'A3B', '12-6', 2), ('A6A', 'A6A', '12-6', 2), ('A3A', 'A3A', '12-6', 2),
              ('D3C', 'D3C', '12-6', 1), ('D3A', 'D3A', '12-6', 1), ('EXT8_129', 'EXT8_129', '12-9', 1), ('EXT6_123', 'EXT6_123', '12-3', 1),
              ('EXT8_159', 'EXT8_159', '15-9', 1), ('EXT8_4', 'EXT8_4', '4-0', 1), ('S6_44', 'S6_44', '4-4', 2), ('A3A_39', 'A3A_39', '3-9', 2)]
gross = sum(R[k] * H[h] * f for _, k, h, f in gross_rows)
tile_on_walls = sum(R[k] for k in ['WT1_410', 'WT2_410', 'WT9_410', 'WT1_703', 'WT2_703', 'WT9_703', 'WT1_705', 'WT2_705', 'WT9_705'])
tile_all = tile_on_walls + R['WT3_700']
gwb = gross - R['PT1_RR'] - tile_on_walls - R['TYPEX_704']
put(242, 'markup p4 (A-120) less p16/p27/p32/p28 specialty areas',
    f'gross faces {gross:.3f} SF (' + ' + '.join(f'{k} {R[k]}x{H[h]:.3f}x{f}' for _, k, h, f in gross_rows) + f'); less restroom PT1 {R["PT1_RR"]}, wall tile {tile_on_walls:.1f}, Type X {R["TYPEX_704"]}',
    'SF = sum(LF x H x GWB faces) - MR area - wall-tile (CBU) area - Type X area', gwb, 'derived (net of specialty boards)',
    'faces: A-series 2, D-series 1, exterior 1 (interior face), BS rows 2; parapet 7\'2", NO GWB and sheathing-only rows excluded; no opening deduction; residual within LF display rounding (+/-0.05 LF per row)')
put(248, 'markup p28 (A-704)', f'TYPE X GWB {R["TYPEX_704"]} SF', 'SF = ceil5(measured SF)', ceil_to(R['TYPEX_704'], 5), 'measured', '37.2 -> 40')
par = [('PAR_17', '1-7'), ('PAR_27', '2-7'), ('PAR_47', '4-7'), ('PAR_72', '7-2')]
par_exact = sum(R[k] * H[h] for k, h in par)
par_ceil = sum(math.ceil(round(R[k] * H[h], 9)) for k, h in par)
put(254, 'markups p7 (A-140) + p4 (A-120)', '; '.join(f'{k} {R[k]} LF x {H[h]:.4f}' for k, h in par), 'SF = sum(ceil(LF x H)) per parapet row, one (roof-side) face', par_ceil, 'derived',
    f'unrounded sum = {par_exact:.3f} SF ({(par_exact/658-1)*100:+.2f}%); per-row ceil to whole SF reproduces 658 exactly')
put(260, 'markup p16 (A-410)', f'PT1 WALL PAINT (restrooms) {R["PT1_RR"]} SF', 'SF = ceil5(restroom painted wall SF)', ceil_to(R['PT1_RR'], 5), 'measured', 'MR board on wet-room wall faces that are painted (above tile)')
put(266, 'markups p16, p27, p32, p23', f'WT1/WT2/WT9 on walls {tile_on_walls:.1f} + WT3 bar {R["WT3_700"]} = {tile_all:.1f} SF', 'SF = ceil5(all wall-tile SF)', ceil_to(tile_all, 5), 'measured',
    'includes WT3 38.4 SF at the transaction bar, which also carries the 1/4" backer (line 272): 38.4 SF counted twice; walls only would be ceil5(244.2) = 245')
put(272, 'markup p23 (A-700)', f'1/4" CEMENTITIOUS BACKER BOARD {R["CBB14_700"]} SF', 'SF = ceil5(measured SF)', ceil_to(R['CBB14_700'], 5), 'measured', 'transaction-bar face under WT3')

# ---- accessory lines (ratios of the parent SF line) ----
RAT = {'NO. OF SHEETS': ('sheets = SF / 32 (4x8)', lambda s: s / 32), 'ADHESIVE': ('tubes = SF x 0.031', lambda s: s * 0.031),
       'TAPING': ('rolls = SF x 0.00075 (0.375 LF/SF / 500 LF roll)', lambda s: s * 0.00075),
       'DRYWALL SCREWS': ('lb = SF x 3/560 (0.0053571 lb/SF)', lambda s: s * 3 / 560), 'MUD PLASTER': ('lb = SF x 0.53', lambda s: s * 0.53)}
for parent in [242, 248, 254, 260, 266, 272]:
    for k in range(1, 6):
        n = parent + k
        d = L[n]['description']
        f, fn = RAT[d]
        pq = L[parent]['quantity']
        put(n, f'line {parent}', f'parent SF {pq}', f, fn(pq), 'derived (estimator ratio)',
            f'from recomputed parent {out[parent]["recomputed"]:.3f} SF -> {fn(out[parent]["recomputed"]):.4f}')

rows = []
for n in ids:
    l = L[n]; o = out[n]
    est = l['quantity']; rq = o['recomputed']
    d = (rq / est - 1) * 100
    desc = l['description'].split('\n')[0].strip()
    if desc in RAT: desc = f'{desc} ({L[[p for p in [242,248,254,260,266,272] if p < n][-1]]["description"].split(" AT")[0]})'
    rows.append(dict(lineNo=n, description=desc, unit=l['unit'], estimatorQty=round(est, 6), source=o['source'], sourceValues=o['sourceValues'],
                     formula=o['formula'], recomputedQty=round(rq, 6), deltaPct=round(d, 3), classification=o['classification'], notes=o['notes']))
json.dump(dict(R=R, gross=gross, tile_on_walls=tile_on_walls, tile_all=tile_all, par_exact=par_exact, rows=rows), open('/home/user/work/09a-wall-framing-drywall/rebuild.json', 'w'), indent=1)
for r in rows: print(r['lineNo'], r['unit'], r['estimatorQty'], round(r['recomputedQty'], 4), f"{r['deltaPct']:+.2f}%", r['notes'][:110])
print('within1', sum(abs(r['deltaPct']) <= 1 for r in rows), 'within5', sum(abs(r['deltaPct']) <= 5 for r in rows), 'of', len(rows))
print('gross', gross, 'tile_on_walls', tile_on_walls, 'tile_all', tile_all)
