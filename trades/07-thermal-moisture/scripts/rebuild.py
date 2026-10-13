"""Rebuild every 07-thermal-moisture estimate quantity from markup legend values (quantities only)."""
import json, math, csv
REF = '/home/user/takeoffspeed-reference-data'
OUT = f'{REF}/trades/07-thermal-moisture'
L = {l['lineNo']: l for l in json.load(open(f'{REF}/reference/estimate/lines.json'))}
ids = [t for t in json.load(open(f'{REF}/reference/estimate/trades.json')) if t['trade'] == '07-thermal-moisture'][0]['lines']
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


R = {
    # A-120 (p4) wall runs, LF
    'A6B': leg(4, 'WALL A6B @ 12\'6"H'), 'A3B': leg(4, 'WALL A3B @ 12\'6"H'), 'A6A': leg(4, 'WALL A6A @ 12\'6"H'),
    'A3A': leg(4, 'WALL A3A @ 12\'6"H'), 'D3C': leg(4, 'WALL D3C @ 12\'6"H 1 SIDE'), 'D3A': leg(4, 'WALL D3A @ 12\'6"H 1 SIDE'),
    'EXT8_129': leg(4, 'EXT 8" STUD WALL @ 12\'9"H'), 'EXT6_123': leg(4, 'EXT 6" STUD WALL @ 12\'3"H SHTNG 10\'3"H'),
    'PAR_72': leg(4, 'PARAPET WALL @ 7\'2"H A310'), 'EXT8_159': leg(4, 'EXT 8" STUD WALL @ 15\'9"H'),
    'EXT8_4': leg(4, 'EXT 8" STUD WALL @ 4\'H'), 'EXT8_159_NOGWB': leg(4, 'EXT 8" STUD WALL @ 15\'9"H NO GWB'),
    'S6_44': leg(4, '6" METAL STUD WALL @ 4\'4" HT, BS GWB'), 'A3A_39': leg(4, 'WALL A3A @ 3\'9"H (NO INS)'),
    # A-130 (p5)
    'ACM3_CANOPY': leg(5, 'ACM-3 ALUMINUM COMPOSITE METAL PANEL CANOPY - 10/A430'), 'EIFS_SOFFIT': leg(5, 'EIFS SOFFIT 1/A310'),
    # A-140 (p7)
    'WALKWAY': leg(7, 'TPO WALKWAY PAD MEMBRANE'), 'CRICKET': leg(7, 'TAPERED POLYISOCYANURATE INSULATION ROOF CRICKET'),
    'HATCH': leg(7, '30"x36" ROOF ACCESS HATCH - 3/A450'), 'RD_FLASH': leg(7, 'FLASHING @ ROOF DRAIN'), 'VENT_FLASH': leg(7, 'FLASHING @ VENT PIPE'),
    'PAR_27': leg(7, 'PARAPET WALL @ 2\'7"H'), 'PAR_17': leg(7, 'PARAPET WALL @ 1\'7"H'), 'PAR_47': leg(7, 'PARAPET WALL @ 4\'7"H'),
    'COP_9A450': leg(7, 'COPING 9/A450'), 'COP_6A450': leg(7, 'COPING 6/A450'), 'COP_3A430': leg(7, 'COPING 3/A430'),
    'RT2': leg(7, 'RT2 ROOFING'), 'CANOPY_EDGE': leg(7, 'CANOPY EDGE 7/A430'), 'HEAD_9A430': leg(7, '9/A430'),
    'HIGHLOW_8A450': leg(7, '8/A450 LAP ROOF 2\', INCL WALL'), 'CURB': leg(7, 'CURB - 1/A450'),
    'LAP_21': leg(7, 'PARAPET LAP @ 2\'1"H - 4,6/A450'), 'LAP_10': leg(7, 'PARAPET LAP @ 1\'H - 4,6/A450'), 'LAP_36': leg(7, 'PARAPET LAP @ 3\'6"H - 4,6/A450'),
    'RT1': leg(7, 'RT1 ROOFING'),
    # A-200 (p11) and A-201 (p12)
    'BRICK_200': leg(11, 'EXT-1: 3-5/8"THK. STANDARD MODULAR BRICK VENEE', prefix=True), 'BRICK_201': leg(12, 'EXT-1: 3-5/8"THK. STANDARD MODULAR BRICK VEN', prefix=True),
    'TWF_200': leg(11, 'THRU WALL FLASHING'), 'TWF_201': leg(12, 'THRU WALL FLASHING'),
    'SEAL_200': leg(11, 'SEALANT W/ BACKER ROD'), 'SEAL_201': leg(12, 'SEALANT W/ BACKER ROD'),
    'ALFL_200': leg(11, 'ALUMINUM FLASHING'), 'ALFL_201': leg(12, 'ALUMINUM FLASHING'),
    'SILL_200': leg(11, 'PRE-FINISHED ALUMINUM SILL'), 'SILL_201': leg(12, 'PRE-FINISHED ALUMINUM SILL'),
    'ACM12_200': leg(11, 'ACM1, ACM2 FINISH - 1/A440'), 'EIFS1_200': leg(11, 'EIFS-1'), 'EIFS2_200': leg(11, 'EIFS-2'),
    'EIFS1_201': leg(12, 'EIFS-1'), 'EIFS2_201': leg(12, 'EIFS-2'), 'SILLPAN_LINEAR_200': leg(11, 'Linear'),
    # A-420 (p17)
    'ACM12_420': leg(17, 'ACM1, ACM2 FINISH - 1/A440'),
    # A-706 (p29)
    'BOOTH_ROOF': leg(29, '6"THK. 16GA. METAL STUD @ 12" O.C W/ 6"THK. SOUND BATT', prefix=True),
    # S-201 (p33)
    'SLAB': leg(33, '4"THK. CONCRETE SLAB ON GRADE', prefix=True),
    'STEM8': leg(33, '8"THK. CONCRETE STEM WALL', prefix=True),
}
H = {'12-6': fi(12, 6), '12-3': fi(12, 3), '12-9': fi(12, 9), '15-9': fi(15, 9), '4-0': 4.0, '1-7': fi(1, 7), '2-7': fi(2, 7), '4-7': fi(4, 7), '7-2': fi(7, 2),
     '2-1': fi(2, 1), '1-0': 1.0, '3-6': fi(3, 6)}

# Estimator lines from other trades used as inputs (quantities only)
LINE32_BRICK = L[32]['quantity']        # 400 SF brick veneer (masonry trade) = ceil5(163.6 + 232.1)
LINE85_CANOPY_CEIL = L[85]['quantity']  # 568.5 SF 5/8" plywood at canopy ceiling (carpentry trade)
LINE88_TRIM = L[88]['quantity']         # 910 LF interior trim at opening, assumed (carpentry trade)

# Openings (A-610 window elevations), feet
WIN = {'A': (fi(12, 11.5), 12, 1), 'B': (fi(9, 11), 12, 1), 'C': (fi(7, 4), 12, 1), 'D': (8, fi(9, 4), 1), 'E': (6, fi(7, 4), 2), 'F': (6, 10, 1),
       'G': (fi(13, 4), fi(9, 4), 1), 'H': (14, fi(9, 4), 1), 'J': (fi(7, 8.25), 12, 1), 'K': (fi(7, 7.625), 10, 1)}
GLAZED_PERIM = sum(2 * (w + h) * n for w, h, n in WIN.values())

# High-low (roof transition) wall, A-140 8/A450 run, rounded up to whole feet by the estimator (46 also = lines 91/92 blocking LF, 35 studs @16")
TRANS_LF = math.ceil(R['HIGHLOW_8A450'])
TRANS_BATT_H = 2.0          # wall height: "LAP ROOF 2', INCL WALL"
TRANS_RIGID_H = 2.5         # 2'-0" wall + 6" over the top (detail 10/A450); estimator convention, back-solved 115/46

out = {}


def put(n, src, vals, formula, q, cls, notes='', fixture=None):
    out[n] = dict(source=src, sourceValues=vals, formula=formula, recomputed=q, classification=cls, notes=notes, fixture=fixture)


# 148 acoustic sealant
interior = ['A6B', 'A3B', 'A6A', 'A3A', 'D3C', 'D3A', 'A3A_39', 'S6_44']
ext_gwb = ['EXT8_129', 'EXT6_123', 'EXT8_159', 'EXT8_4']
int_lf = sum(R[k] for k in interior); ext_lf = sum(R[k] for k in ext_gwb)
put(148, 'markup p4 (A-120) wall runs; A-620 partition details/notes K', f'interior runs {"+".join(str(R[k]) for k in interior)} = {int_lf:.1f} LF; exterior runs with interior GWB {"+".join(str(R[k]) for k in ext_gwb)} = {ext_lf:.1f} LF',
    'LF = 4 x interior partition LF (head + base, both faces) + 1 x exterior-wall LF (base bead, interior face)', 4 * int_lf + ext_lf, 'derived (inferred convention)',
    'dwg ref "A1.1" is not a sheet in this set; rule back-solved (second opinion GPT-6 Astra agreed); alternative 4xA + 2x(D, exterior, low walls) = 1055.0. Not confirmed by a legend row.',
    dict(formula='acousticSealantLF', inputs={'interiorPartitionLF': {'value': round(int_lf, 3), 'unit': 'LF'}, 'interiorBeadsPerLF': {'value': 4, 'unit': 'beads'}, 'exteriorWallLF': {'value': round(ext_lf, 3), 'unit': 'LF'}, 'exteriorBeadsPerLF': {'value': 1, 'unit': 'beads'}}, tol=0.5))
# 149 sealant at openings
put(149, 'line 88 (910 LF opening trim, assumed) + A-610 window elevations', f'line 88 = {LINE88_TRIM} LF; glazed unit perimeters A,B,C,D,E(x2),F,G,H,J,K = {GLAZED_PERIM:.4f} LF',
    'LF = opening-trim LF (line 88) + sum 2(W+H) of every glazed unit (one bead), then ceil to 10', LINE88_TRIM + GLAZED_PERIM, 'allowance/judgment (inferred)',
    f'raw {LINE88_TRIM + GLAZED_PERIM:.2f} -> ceil10 1330; back-solved, depends on an assumed line; round 1330 likely an allowance. Doors-only per A-600 note 2 would be 2 faces x (6x17 + 17.33) = 238.7 LF.',
    dict(formula='openingSealantLF', inputs={'trimLF': {'value': LINE88_TRIM, 'unit': 'LF'}, 'glazedPerimeterLF': {'value': round(GLAZED_PERIM, 4), 'unit': 'LF'}, 'roundUpTo': {'value': 10, 'unit': 'LF'}}, tol=1.0))
# 150 / 189 sealant w/ backer rod
seal = R['SEAL_200'] + R['SEAL_201']
for n in (150, 189):
    put(n, 'markups p11 (A-200) + p12 (A-201) "SEALANT W/ BACKER ROD"', f'{R["SEAL_200"]} + {R["SEAL_201"]} LF', 'LF = sum of measured elevation runs', seal, 'measured',
        'DUPLICATE: lines 150 and 189 carry the same 221.96 LF (double count of one measurement)' if n == 189 else 'same quantity repeated at line 189',
        dict(formula='sumRuns', inputs={'runs': {'value': [R['SEAL_200'], R['SEAL_201']], 'unit': 'LF'}}, tol=0.5))
# 151 XPS
put(151, 'markup p33 (S-201) slab + 8" stem wall; detail 1/G-003', f'slab {R["SLAB"]} SF; 8" stem wall {R["STEM8"]} LF x 2\'-0" turn-down', 'SF = slab area + perimeter LF x 2\'-0" vertical leg',
    R['SLAB'] + R['STEM8'] * 2, 'derived', 'G-003 says XPS only "where req\'d zones >4" (Warner Robins is zone 3A: likely not required); implied perimeter 190.2 LF vs 193.8 measured',
    dict(formula='underSlabXpsSF', inputs={'slabSF': {'value': R['SLAB'], 'unit': 'SF'}, 'perimeterLF': {'value': R['STEM8'], 'unit': 'LF'}, 'turnDown': {'value': 2.0, 'unit': 'FT'}}, tol=0.5))
# 152 / 153 sound blankets (partition type ...B = to structure w/ batt)
put(152, 'markup p4 (A-120) WALL A3B @ 12\'6"H', f'{R["A3B"]} LF x 12.5 ft', 'SF = LF x framing height (one cavity layer, no deductions)', R['A3B'] * 12.5, 'measured+derived', 'A3B: series A, 3-5/8" studs, height B "slab to structure w/ batt" (A-620 Table D)',
    dict(formula='cavityInsulationSF', inputs={'runLF': {'value': R['A3B'], 'unit': 'LF'}, 'height': {'value': 12.5, 'unit': 'FT'}}, tol=0.5))
put(153, 'markup p4 (A-120) WALL A6B @ 12\'6"H', f'{R["A6B"]} LF x 12.5 ft', 'SF = LF x framing height', R['A6B'] * 12.5, 'measured+derived', 'estimator 356.25 = 28.5 LF x 12.5: legend shows 28.4 (display rounding of the run)',
    dict(formula='cavityInsulationSF', inputs={'runLF': {'value': R['A6B'], 'unit': 'LF'}, 'height': {'value': 12.5, 'unit': 'FT'}}, tol=0.5))
# 154 3-1/2" batt at the high-low (roof transition) wall
put(154, 'markup p7 (A-140) "8/A450 LAP ROOF 2\', INCL WALL"; details 8 & 10/A450', f'ceil({R["HIGHLOW_8A450"]}) = {TRANS_LF} LF x {TRANS_BATT_H} ft', 'SF = ceil(LF) x wall height', TRANS_LF * TRANS_BATT_H, 'derived',
    'labelled "at exterior walls" but it is the 3-5/8" stud high-low wall (detail 8/A450: 3-5/8" MTL. STUDS & BATT INSULATION); same 46 LF as 2x4/2x6 blocking lines 91/92 and the 35 studs @ 2\' in line 308; raw 45.3 x 2 = 90.6 (-1.5%)',
    dict(formula='cavityInsulationSF', inputs={'runLF': {'value': TRANS_LF, 'unit': 'LF'}, 'height': {'value': TRANS_BATT_H, 'unit': 'FT'}}, tol=0.5))
# 155 5-1/2" batt at EXT 6" wall
put(155, 'markup p4 (A-120) EXT 6" STUD WALL @ 12\'3"H', f'{R["EXT6_123"]} LF x 12.25 ft', 'SF = LF x framing height', R['EXT6_123'] * 12.25, 'measured+derived', 'estimator 113.3125 = 9.25 LF x 12.25 (legend displays 9.2)',
    dict(formula='cavityInsulationSF', inputs={'runLF': {'value': R['EXT6_123'], 'unit': 'LF'}, 'height': {'value': 12.25, 'unit': 'FT'}}, tol=1.0))
# 156 8" batt = 8" stud SF (line 311)
rows8 = [('PAR_17', '1-7'), ('PAR_27', '2-7'), ('EXT8_4', '4-0'), ('PAR_47', '4-7'), ('PAR_72', '7-2'), ('EXT8_129', '12-9'), ('EXT8_159', '15-9'), ('EXT8_159_NOGWB', '15-9')]
sf8 = sum(R[k] * H[h] for k, h in rows8)
put(156, 'markups p4 (A-120) + p7 (A-140), all 8" stud rows', '; '.join(f'{k} {R[k]} x {H[h]:.4f}' for k, h in rows8), 'SF = sum(LF x H) over every 8" stud row (equals the 8" stud SF, line 311)', sf8, 'measured+derived',
    'identical to line 311 (2652.875); includes 656 SF of roof parapets above the deck, where the cavity batt is not needed thermally',
    dict(formula='cavityInsulationSF', inputs={'runs': {'value': [[R[k], round(H[h], 6)] for k, h in rows8], 'unit': 'LF x FT'}}, tol=0.5))
# 157 2" rigid at roof transition wall
put(157, 'markup p7 (A-140) 8/A450 run; detail 10/A450', f'ceil({R["HIGHLOW_8A450"]}) = {TRANS_LF} LF x {TRANS_RIGID_H} ft', 'SF = ceil(LF) x (wall height 2\'-0" + 6" over top)', TRANS_LF * TRANS_RIGID_H, 'derived (estimator convention)',
    '2.5 ft back-solved; detail 10/A450 shows "2" RIGID INSULATION & GIRTS" up the face and over the blocking',
    dict(formula='rigidBandSF', inputs={'runLF': {'value': TRANS_LF, 'unit': 'LF'}, 'height': {'value': TRANS_RIGID_H, 'unit': 'FT'}}, tol=0.5))
# 158 / 159 roof insulation
put(158, 'markup p7 (A-140) RT2 ROOFING', f'{R["RT2"]} SF', 'SF = round(RT2 area)', round(R['RT2']), 'measured', 'RT2 build-up: 2" polyiso (tapered to drain, 1" min) over 5/8" plywood; same 285 as plywood line 84',
    dict(formula='roofInsulationSF', inputs={'areaSF': {'value': R['RT2'], 'unit': 'SF'}, 'round': {'value': 1, 'unit': 'SF'}}, tol=0.5))
put(159, 'markup p7 (A-140) RT1 ROOFING', f'{R["RT1"]} SF', 'SF = round(RT1 area), carried once for the whole 6" (3 x 2") stack', round(R['RT1']), 'measured', 'RT1: 3 layers 2" polyiso R-34.2, first layer fastened, others adhered; estimator carries plan SF, not SF per layer',
    dict(formula='roofInsulationSF', inputs={'areaSF': {'value': R['RT1'], 'unit': 'SF'}, 'round': {'value': 1, 'unit': 'SF'}}, tol=0.5))
# 160 2" rigid behind exterior finish = ACM wall line + brick line
acm = R['ACM12_200'] + R['ACM12_420']
brick = R['BRICK_200'] + R['BRICK_201']
put(160, 'lines 181 + 32 (p11, p17 ACM1/ACM2; p11, p12 EXT-1 brick)', f'ceil5({R["ACM12_200"]}+{R["ACM12_420"]}) = {ceil_to(acm, 5)} + ceil5({R["BRICK_200"]}+{R["BRICK_201"]}) = {ceil_to(brick, 5)}',
    'SF = ceil5(ACM wall SF) + ceil5(brick veneer SF)', ceil_to(acm, 5) + ceil_to(brick, 5), 'derived', 'rigid insulation shown behind ACM (1, 2/A430) and in brick cavity (4, 5/A430); not behind EIFS (EIFS carries its own EPS); raw 884.0',
    dict(formula='rigidBehindCladdingSF', inputs={'acmSF': {'value': round(acm, 3), 'unit': 'SF'}, 'brickSF': {'value': round(brick, 3), 'unit': 'SF'}, 'roundUpTo': {'value': 5, 'unit': 'SF'}}, tol=0.5))
# 161 booth ceiling sound batt
put(161, 'markup p29 (A-706) booth roof framing w/ 6" sound batt', f'{R["BOOTH_ROOF"]} SF', 'SF = round(measured booth-roof area)', round(R['BOOTH_ROOF']), 'measured', 'same area as booth roof framing (line 312) and PT5 (line 302)',
    dict(formula='roofInsulationSF', inputs={'areaSF': {'value': R['BOOTH_ROOF'], 'unit': 'SF'}, 'round': {'value': 1, 'unit': 'SF'}}, tol=0.5))
# 162 membrane
laps = R['LAP_21'] * H['2-1'] + R['LAP_10'] * H['1-0'] + R['LAP_36'] * H['3-6']
field = R['RT1'] + R['RT2']
hl = R['HIGHLOW_8A450'] * 2
edge = R['CANOPY_EDGE'] * 2.5
memb = field + laps + hl + edge
put(162, 'markup p7 (A-140): RT1, RT2, PARAPET LAP rows, 8/A450, CANOPY EDGE', f'field {R["RT1"]}+{R["RT2"]} = {field:.1f}; laps {R["LAP_21"]}x2.0833+{R["LAP_10"]}x1+{R["LAP_36"]}x3.5 = {laps:.3f}; high-low {R["HIGHLOW_8A450"]}x2 = {hl:.1f}; canopy edge {R["CANOPY_EDGE"]}x2.5 = {edge:.2f}',
    'SF = roof field + sum(parapet lap LF x lap height) + high-low LF x 2\' + canopy-edge LF x 2.5\' (fascia girth 12"+12"+6")', memb, 'derived (decomposition inferred)',
    'field + laps + high-low are measured rows; the canopy-edge 2.5 ft is inferred (girth from line 183) - the split is not unique (GPT-6 Astra fit: + 16" canopy wrap + 4\'6" high-low + 12" curbs/hatch = 3043.1)',
    dict(formula='membraneSF', inputs={'fieldSF': {'value': round(field, 3), 'unit': 'SF'}, 'flashings': {'value': [[R['LAP_21'], round(H['2-1'], 6)], [R['LAP_10'], 1.0], [R['LAP_36'], 3.5], [R['HIGHLOW_8A450'], 2.0], [R['CANOPY_EDGE'], 2.5]], 'unit': 'LF x FT'}}, tol=0.5))
# 163 cover board
put(163, 'markup p7 RT1 + transition wall (detail 10/A450 1/4" cover board on wall face)', f'round({R["RT1"]}) + {TRANS_LF} LF x 2 ft', 'SF = round(RT1) + transition LF x wall height', round(R['RT1']) + TRANS_LF * TRANS_BATT_H, 'derived',
    'RT2 has no cover board (plywood); drawings say 1/4" cover board, spec 07 5423 2.6 says 1/2" glass-mat gypsum - estimator followed the drawings',
    dict(formula='coverBoardSF', inputs={'fieldSF': {'value': round(R['RT1']), 'unit': 'SF'}, 'wallLF': {'value': TRANS_LF, 'unit': 'LF'}, 'wallHeight': {'value': TRANS_BATT_H, 'unit': 'FT'}}, tol=0.5))
put(164, 'markup p7 TAPERED ... ROOF CRICKET', f'{R["CRICKET"]} SF', 'SF = measured cricket area (unrounded)', R['CRICKET'], 'measured', 'magenta crickets overlap RT1 (orange on markup): not additional field area',
    dict(formula='areaSF', inputs={'areaSF': {'value': R['CRICKET'], 'unit': 'SF'}}, tol=0.5))
put(165, 'markup p7 RT1 + RT2', f'{R["RT1"]} + {R["RT2"]} SF', 'SF = sum of roof field areas', field, 'measured', 'no vapor retarder in 07 5423 or roof types ("ASSUMED"); estimator raw 2149.28',
    dict(formula='areaSF', inputs={'areaSF': {'value': [R['RT1'], R['RT2']], 'unit': 'SF'}}, tol=0.5))
put(166, 'markup p7 CURB - 1/A450; detail 1/A450', f'{R["CURB"]} LF x 1 ft', 'SF = ceil5(curb LF x 1 ft)', ceil_to(R['CURB'] * 1.0, 5), 'derived (estimator convention)', 'detail 1/A450: pressure-sensitive A/VB on deck flutes and up the curb; 1 ft strip is the estimator\'s width (curb is 18" high)',
    dict(formula='stripSF', inputs={'runLF': {'value': R['CURB'], 'unit': 'LF'}, 'width': {'value': 1.0, 'unit': 'FT'}, 'roundUpTo': {'value': 5, 'unit': 'SF'}}, tol=0.5))
put(167, 'markup p7 TPO WALKWAY PAD MEMBRANE', f'{R["WALKWAY"]} SF', 'SF = measured hatch area (unrounded)', R['WALKWAY'], 'measured', 'keynote R11',
    dict(formula='areaSF', inputs={'areaSF': {'value': R['WALKWAY'], 'unit': 'SF'}}, tol=0.5))
for n, k, rule, note in [(168, 'COP_3A430', 'ceil5', '3/A430 coping @ wing wall 2\'-0" wide (girth ~2\'7"); 0.040 alum per 07 6200 2.x'),
                          (169, 'COP_6A450', 'round', '6/A450 roof coping; estimator dropped 0.1 LF (148.1 -> 148); ceil5 would be 150'),
                          (170, 'COP_9A450', 'ceil5', '9/A450 coping detail (girth ~2\'4")')]:
    v = R[k]; q = ceil_to(v, 5) if rule == 'ceil5' else round(v)
    put(n, f'markup p7 COPING {k.split("_")[1]}', f'{v} LF', f'LF = {rule}(measured LF)', q if rule == 'ceil5' else v, 'measured', note,
        dict(formula='runLF', inputs={'runLF': {'value': v, 'unit': 'LF'}, **({'roundUpTo': {'value': 5, 'unit': 'LF'}} if rule == 'ceil5' else {})}, tol=0.5))
put(171, 'markup p7 CURB - 1/A450', f'{R["CURB"]} LF', 'LF = ceil5(curb perimeter LF)', ceil_to(R['CURB'], 5), 'measured', 'curb perimeters of RTU-1, RTU-2 (M-302)',
    dict(formula='runLF', inputs={'runLF': {'value': R['CURB'], 'unit': 'LF'}, 'roundUpTo': {'value': 5, 'unit': 'LF'}}, tol=0.5))
put(172, 'markup p7 30"x36" ROOF ACCESS HATCH (1 EA); spec 07 7200 hatch 30x36', '1 EA x 2 x (30" + 36")', 'LF = count x 2(W+L)', R['HATCH'] * 2 * (30 + 36) / 12, 'counted+specified', '',
    dict(formula='curbPerimeterLF', inputs={'count': {'value': R['HATCH'], 'unit': 'EA'}, 'size': {'value': [30, 36], 'unit': 'IN'}}, tol=0.5))
put(173, 'markup p7 FLASHING @ ROOF DRAIN', f'{R["RD_FLASH"]} EA', 'EA = count', R['RD_FLASH'], 'counted', '11 dots = roof drains + overflows + canopy drains', dict(formula='count', inputs={'count': {'value': R['RD_FLASH'], 'unit': 'EA'}}, tol=0))
put(174, 'markup p7 FLASHING @ VENT PIPE', f'{R["VENT_FLASH"]} EA', 'EA = count', R['VENT_FLASH'], 'counted', '', dict(formula='count', inputs={'count': {'value': R['VENT_FLASH'], 'unit': 'EA'}}, tol=0))
for n in (175, 176):
    put(n, 'markup p7 "9/A430" run (storefront head @ canopy)', f'{R["HEAD_9A430"]} LF', 'LF = ceil5(measured LF)', ceil_to(R['HEAD_9A430'], 5), 'measured',
        'detail 9/A430: two-piece alum. head flashing AND self-adhered flashing strip, so both lines take the same run',
        dict(formula='runLF', inputs={'runLF': {'value': R['HEAD_9A430'], 'unit': 'LF'}, 'roundUpTo': {'value': 5, 'unit': 'LF'}}, tol=0.5))
put(177, 'markup p7 CURB - 1/A450 (counterflashing skirt, detail 1/A450)', f'{R["CURB"]} LF', 'LF = ceil5(curb LF)', ceil_to(R['CURB'], 5), 'measured', '',
    dict(formula='runLF', inputs={'runLF': {'value': R['CURB'], 'unit': 'LF'}, 'roundUpTo': {'value': 5, 'unit': 'LF'}}, tol=0.5))
for n, a, b, note in [(178, 'EIFS1_200', 'EIFS1_201', '3" EIFS-1 walls'), (179, 'EIFS2_200', 'EIFS2_201', '5" EIFS-2 (vestibule parapet)')]:
    s = R[a] + R[b]
    put(n, 'markups p11 (A-200) + p12 (A-201)', f'{R[a]} + {R[b]} SF', 'SF = ceil5(sum of elevation areas)', ceil_to(s, 5), 'measured', f'{note}; raw {s:.1f}',
        dict(formula='areaSF', inputs={'areaSF': {'value': [R[a], R[b]], 'unit': 'SF'}, 'roundUpTo': {'value': 5, 'unit': 'SF'}}, tol=0.5))
put(180, 'markup p5 (A-130) EIFS SOFFIT 1/A310', f'{R["EIFS_SOFFIT"]} SF', 'SF = ceil5(measured)', ceil_to(R['EIFS_SOFFIT'], 5), 'measured', '',
    dict(formula='areaSF', inputs={'areaSF': {'value': R['EIFS_SOFFIT'], 'unit': 'SF'}, 'roundUpTo': {'value': 5, 'unit': 'SF'}}, tol=0.5))
put(181, 'markups p11 (A-200) + p17 (A-420) ACM1, ACM2 FINISH - 1/A440', f'{R["ACM12_200"]} + {R["ACM12_420"]} SF', 'SF = ceil5(sum)', ceil_to(acm, 5), 'measured', f'raw {acm:.1f}',
    dict(formula='areaSF', inputs={'areaSF': {'value': [R['ACM12_200'], R['ACM12_420']], 'unit': 'SF'}, 'roundUpTo': {'value': 5, 'unit': 'SF'}}, tol=0.5))
put(182, 'markup p5 (A-130) ACM-3 CANOPY - 10/A430', f'{R["ACM3_CANOPY"]} SF', 'SF = ceil5(measured)', ceil_to(R['ACM3_CANOPY'], 5), 'measured', 'canopy soffit, RCP area',
    dict(formula='areaSF', inputs={'areaSF': {'value': R['ACM3_CANOPY'], 'unit': 'SF'}, 'roundUpTo': {'value': 5, 'unit': 'SF'}}, tol=0.5))
put(183, 'markup p7 (A-140) CANOPY EDGE 7/A430', f'{R["CANOPY_EDGE"]} LF', 'LF = ceil5(measured)', ceil_to(R['CANOPY_EDGE'], 5), 'measured', 'fascia 12" top x 12" front x 6" base (girth 2.5 ft) carried as LF',
    dict(formula='runLF', inputs={'runLF': {'value': R['CANOPY_EDGE'], 'unit': 'LF'}, 'roundUpTo': {'value': 5, 'unit': 'LF'}}, tol=0.5))
vb = L[178]['quantity'] + L[179]['quantity'] + L[180]['quantity'] + L[181]['quantity'] + LINE85_CANOPY_CEIL
recomp184 = ceil_to(R['EIFS1_200'] + R['EIFS1_201'], 5) + ceil_to(R['EIFS2_200'] + R['EIFS2_201'], 5) + ceil_to(R['EIFS_SOFFIT'], 5) + ceil_to(acm, 5) + LINE85_CANOPY_CEIL
put(184, 'lines 178 + 179 + 180 + 181 + 85', f'EIFS1 1640 + EIFS2 275 + EIFS soffit 10 + ACM 490 + canopy-ceiling sheathing (line 85) {LINE85_CANOPY_CEIL}', 'SF = sum of the rounded EIFS and ACM wall lines + canopy ceiling sheathing SF', recomp184, 'derived',
    'fluid-applied VB behind EIFS and ACM and on the canopy sheathing (10/A430); brick VB is its own line 35 (400 SF, masonry); ACM-3 canopy (360) not added - the canopy sheathing area stands in for it',
    dict(formula='sumAreasSF', inputs={'areasSF': {'value': [1640, 275, 10, 490, LINE85_CANOPY_CEIL], 'unit': 'SF'}}, tol=0.5))
for n, a, b, what in [(185, 'SILL_200', 'SILL_201', 'PRE-FINISHED ALUMINUM SILL'), (186, 'ALFL_200', 'ALFL_201', 'ALUMINUM FLASHING'), (187, 'TWF_200', 'TWF_201', 'THRU WALL FLASHING')]:
    put(n, f'markups p11 + p12 "{what}"', f'{R[a]} + {R[b]} LF', 'LF = sum of elevation runs (unrounded)', R[a] + R[b], 'measured', '',
        dict(formula='sumRuns', inputs={'runs': {'value': [R[a], R[b]], 'unit': 'LF'}}, tol=0.5))
put(188, 'markup p11 (A-200) "Linear" run, green line along storefront sill at slab', f'{R["SILLPAN_LINEAR_200"]} LF', 'LF = ceil5(measured LF)', ceil_to(R['SILLPAN_LINEAR_200'], 5), 'measured',
    'the unnamed "Linear" row is the sill pan: storefront glazing sills at slab (detail 6/A430), doors excluded',
    dict(formula='runLF', inputs={'runLF': {'value': R['SILLPAN_LINEAR_200'], 'unit': 'LF'}, 'roundUpTo': {'value': 5, 'unit': 'LF'}}, tol=0.5))

rows, fixtures = [], []
for n in ids:
    l = L[n]; o = out[n]
    est = l['quantity']; rq = o['recomputed']
    d = (rq / est - 1) * 100
    desc = l['description'].split('\n')[0].strip()
    rows.append(dict(lineNo=n, description=desc, unit=l['unit'], estimatorQty=round(est, 6), source=o['source'], sourceValues=o['sourceValues'], formula=o['formula'],
                     recomputedQty=round(rq, 4), deltaPct=round(d, 3), classification=o['classification'], notes=o['notes']))
    fx = o['fixture']
    if fx:
        fixtures.append({'name': f'L{n} {desc[:60]}', 'formula': fx['formula'], 'inputs': fx['inputs'], 'expected': {'quantity': est, 'unit': l['unit']}, 'tolerancePct': fx['tol'],
                         'source': f'line {n} / {o["source"]}', 'classification': o['classification'], 'recomputed': round(rq, 4)})
with open(f'{OUT}/reconciliation.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
json.dump(fixtures, open(f'{OUT}/fixtures.json', 'w'), indent=1)
for r in rows:
    print(r['lineNo'], r['unit'], r['estimatorQty'], r['recomputedQty'], f"{r['deltaPct']:+.3f}%", r['classification'])
print('n', len(rows), 'within1', sum(abs(r['deltaPct']) <= 1 for r in rows), 'within5', sum(abs(r['deltaPct']) <= 5 for r in rows), 'fixtures', len(fixtures))
print('int_lf', int_lf, 'ext_lf', ext_lf, 'glazed', GLAZED_PERIM, 'laps', laps, 'memb', memb, 'sf8', sf8, 'acm', acm, 'brick', brick)
