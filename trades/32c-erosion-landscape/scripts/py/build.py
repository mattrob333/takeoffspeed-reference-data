"""Rebuild every 32c-erosion-landscape estimate line from its source and write
reconciliation.csv + fixtures.json. Quantities only."""
import json, math, csv, os

REF = '/home/user/takeoffspeed-reference-data'
OUT = REF + '/trades/32c-erosion-landscape'
os.makedirs(OUT, exist_ok=True)
lines = {l['lineNo']: l for l in json.load(open(REF + '/reference/estimate/lines.json'))}
trade = [t for t in json.load(open(REF + '/reference/estimate/trades.json')) if t['trade'] == '32c-erosion-landscape'][0]
ids = trade['lines']

# ---- source values (legend rows, schedule rows, detail values, scaled geometry)
LEG = {
    'p65 CO': 1569.4, 'p65 washout': 25.1, 'p65 fuel': 25.1, 'p65 SD1-NS': 767.9, 'p65 RT-B': 5.1,
    'p65 DS teal': 20298.9, 'p65 DS red': 15581.9,
    'p66 SD2-F': 193.7, 'p66 RT-P': 7.5, 'p66 SS,DS3': 2114.0, 'p66 ST-1': 962.4,
    'p67 Sd2-P': 74.5, 'p67 DS4': 14393.7,
    'p72 pond': 3074.0,
}
PLANT = {'holly': 5, 'redcedar': 11, 'anise': 17, 'waxmyrtle': 15, 'pinestraw': 2500, 'sod': 11500}
BASIN_BOTTOM, GRAVEL_BOTTOM = 435.00, 429.5          # C-4.2
TRENCH_LEN_SCALED = 95.60                             # C-4.0 vector bbox of the 435 stone-bed outline, ft
TRENCH_W_SCALED = 10.27
RTP_DIA = 2.25                                         # C-2.1 Phase 2 sediment storage table

stone_depth = BASIN_BOTTOM - GRAVEL_BOTTOM

def row(n, src, vals, formula, qty, cls, notes, fx=None, tol=1.0):
    return dict(lineNo=n, src=src, vals=vals, formula=formula, qty=qty, cls=cls, notes=notes, fx=fx, tol=tol)

R = [
 row(684, 'p65 C-2.0 legend "CO: CONSTRUCTION EXIT"', '1569.4 SQ FT (maroon area)', 'SF = ceil(legend SF) = ceil(1569.4)',
     math.ceil(LEG['p65 CO']), 'measured',
     'Area drawn over the Co pad at Westgate Drive. Estimator rounded up to whole SF. Detail C-2.5 CRUSHED STONE CONSTRUCTION EXIT: N.S.A. R-2 (1.5"-3.5") stone, 6" MIN, 20\' MIN x 50\' MIN, geotextile underliner, tire washrack, culvert if needed - all ride on this SF line; no stone CY or fabric SF line.',
     dict(formula='constructionExitSF = ceil(sum(areas))', inputs={'areas': {'value': [1569.4], 'unit': 'SF'}, 'thickness': {'value': 6, 'unit': 'in'}}, unit='SF')),
 row(685, 'p65 C-2.0 legend "CONCRETE WASHOUT" + C-2.5 CONCRETE WASHDOWN detail', '25.1 SQ FT symbol; detail "PROVIDE 7\'x7\' CONCRETE WASHOUT AREA", 10 MIL liner', 'EA = count of washout areas = 1',
     1, 'counted', 'Legend measured the area of the drawn symbol (25.1 SF, about 5\'x5\'), but the line is 1 EA of the detailed 7\'x7\' pit. Size and liner from the detail text.',
     dict(formula='washoutEA = count', inputs={'count': {'value': 1, 'unit': 'EA'}, 'size': {'value': '7\'-0" x 7\'-0"', 'unit': 'ft'}}, unit='EA')),
 row(686, 'p65 C-2.0 legend "FUEL STORAGE"', '25.1 SQ FT (olive area)', 'SF = round(legend SF) = round(25.1)',
     round(LEG['p65 fuel']), 'measured', 'No detail in the set (estimate says NO DETAILS). The drawn box is the same 25.1 SF as the washout symbol; carried as 25 SF.',
     dict(formula='fuelStorageSF = round(sum(areas))', inputs={'areas': {'value': [25.1], 'unit': 'SF'}}, unit='SF')),
 row(687, 'p65 C-2.0 legend "SD1-NS: SEDIMENT BARRIER - NON SENSITIVE"', '767.9 FT (slate-blue run along the LOD)', 'LF = ceil(legend LF) = ceil(767.9)',
     math.ceil(LEG['p65 SD1-NS']), 'measured',
     'Installed once in Phase 1 and maintained; not repeated on C-2.1/C-2.2. Estimate text "30\\" DIA COMPOST FILTER SOCK - WOODE STAKES 2\' O.C." The C-2.5 COMPOST FILTER SOCK detail says "AT LEAST 18\\" DIA" and dimensions 30" MIN (stake height above grade) - 30" is not the sock diameter. Stakes at 2\' O.C. = 385 EA (not a separate line).',
     dict(formula='sedimentBarrierLF = ceil(sum(runs))', inputs={'runs': {'value': [767.9], 'unit': 'LF'}, 'stakeSpacing': {'value': 2, 'unit': 'ft'}}, unit='LF')),
 row(688, 'p65 C-2.0 legend "RT-B: SLOTTED BOARD DAM RETROFIT"', '5.1 FT printed; raw PlanSwift 5.14', 'LF = legend LF (printed 5.1; estimate carries raw 5.14)',
     LEG['p65 RT-B'], 'measured', 'Short run across the outlet weir at the pond south side. The estimate carries the unrounded PlanSwift value (5.14); the legend prints 1 dp. Recomputed from the printed 5.1 the delta is -0.78%.',
     dict(formula='linearPracticeLF = sum(runs)', inputs={'runs': {'value': [5.14], 'unit': 'LF'}}, unit='LF')),
 row(689, 'p65 C-2.0 legend "DS1, DS2 & DU" (teal row)', '20298.9 SQ FT printed; raw 20298.88', 'SF = teal polygon SF (printed 20298.9)',
     LEG['p65 DS teal'], 'measured', 'The LOD was traced as two polygons on C-2.0, both labelled "DS1, DS2 & DU": teal (west/south, 20298.88) and red (east/north-east, 15581.92). The teal one is Phase 1. Sum 35880.8 SF = 0.824 AC vs the printed LIMITS OF DISTURBANCE 0.9 AC (39204 SF).',
     dict(formula='stabilizationSF = sum(areas)', inputs={'areas': {'value': [20298.88], 'unit': 'SF'}, 'practices': {'value': ['mulch', 'temporary-seed', 'dust-control']}}, unit='SF')),
 row(690, '= line 689 (same polygon, practice DS2)', '20298.88 SF', 'DS2 SF = DS1 SF of the same zone', 20298.88, 'derived',
     'One area, three practices (Ds1/Ds2/Du are stacked on the same tag). Each practice is its own SF line.',
     dict(formula='stabilizationSF = sum(areas)', inputs={'areas': {'value': [20298.88], 'unit': 'SF'}}, unit='SF')),
 row(691, '= line 689 (same polygon, practice DU)', '20298.88 SF', 'DU SF = DS1 SF of the same zone', 20298.88, 'derived', 'Dust control area = stabilization zone area.',
     dict(formula='stabilizationSF = sum(areas)', inputs={'areas': {'value': [20298.88], 'unit': 'SF'}}, unit='SF')),
 row(692, 'p66 C-2.1 legend "SD2-F: TRMPORARY INLETE SEDIMENT TRAP( FILTER FABRI..."', '193.7 FT (green squares round 4 Sd2-F inlets)', 'LF = ceil(legend LF) = ceil(193.7)',
     math.ceil(LEG['p66 SD2-F']), 'measured', '4 Sd2-F tags on C-2.1; 193.7/4 = 48.4 LF of fabric frame per inlet as drawn. Detail C-2.6 FABRIC AND SUPPORTING FRAME FOR INLET PROTECTION (Sd2-F).',
     dict(formula='inletProtectionLF = ceil(sum(runs))', inputs={'runs': {'value': [193.7], 'unit': 'LF'}, 'inlets': {'value': 4, 'unit': 'EA'}}, unit='LF')),
 row(693, 'p66 C-2.1 legend "RT-P: PERFORATED HALF-ROUND PIPE RETROFIT"', '7.5 FT printed (raw 7.45-7.55); C-2.1 table Half Round CMP Diameter 2.25 FT', 'unresolved: printed legend 7.5 LF; no rounding rule used elsewhere on this job gives 7.0',
     LEG['p66 RT-P'], 'measured (unresolved rounding)', 'Printed legend 7.5 FT, estimate 7.0 LF (+7.1% from the legend). Two explanations fit and neither is provable: (a) the raw PlanSwift value was 7.45-7.49 and was rounded to the nearest foot (other lines are rounded to whole units, though CO 1569.4 went UP to 1570); (b) pi x the 2.25 FT Half Round CMP Diameter in the C-2.1 sediment storage table = 7.07 LF (+0.98%). Stone fill (3"-4", C-2.6 Rt-P detail) rides on the line. Physically the retrofit is 1 EA: one 2.25 FT dia half-round CMP 2.00 FT high on the weir (second opinion GPT-6 Astra agrees: pipe LF runs along its axis = 2.00 LF; the plan arc is not an axial length). No fixture: not reproducible from a printed source within 1%.',
     None),
 row(694, 'p65 C-2.0 legend "DS1, DS2 & DU" (red row)', '15581.9 SQ FT printed; raw 15581.92', 'SF = red polygon SF (printed 15581.9)', LEG['p65 DS red'], 'measured',
     'Phase 2 stabilization uses the second (red) LOD polygon measured on the Phase 1 sheet; C-2.1 has Ds1/Ds2/Du tags but no area row of its own.',
     dict(formula='stabilizationSF = sum(areas)', inputs={'areas': {'value': [15581.92], 'unit': 'SF'}}, unit='SF')),
 row(695, '= line 694 (practice DS2)', '15581.92 SF', 'DS2 SF = zone SF', 15581.92, 'derived', 'Same zone, second practice.',
     dict(formula='stabilizationSF = sum(areas)', inputs={'areas': {'value': [15581.92], 'unit': 'SF'}}, unit='SF')),
 row(696, '= line 694 (practice DU)', '15581.92 SF', 'DU SF = zone SF', 15581.92, 'derived', 'Same zone, third practice.',
     dict(formula='stabilizationSF = sum(areas)', inputs={'areas': {'value': [15581.92], 'unit': 'SF'}}, unit='SF')),
 row(697, 'p66 C-2.1 legend "SS, DS3: AREA"', '2114 SQ FT (periwinkle ring = pond side slopes)', 'SF = legend SF', LEG['p66 SS,DS3'], 'measured',
     'Pond side-slope ring between the stone bed and the top of bank. Cross-check: pond area 3074 - stone bed (ST-1) 962.4 = 2111.6 SF (-0.11%).',
     dict(formula='stabilizationSF = sum(areas)', inputs={'areas': {'value': [2114], 'unit': 'SF'}, 'practices': {'value': ['permanent-seed', 'matting']}}, unit='SF')),
 row(698, '= line 697 (practice SS)', '2114 SF', 'SS SF = DS3 SF of the same ring', 2114.0, 'derived', 'Slope stabilization (C-2.5 SLOPE STABILIZATION (Ss), rolled erosion control product) on the same ring.',
     dict(formula='stabilizationSF = sum(areas)', inputs={'areas': {'value': [2114], 'unit': 'SF'}}, unit='SF')),
 row(699, '= line 692 (Phase 2 SD2-F carried into Phase 3)', '194 LF; C-2.2 legend instead shows "TEMPORARY INLET SEDIMENT  TRAP (CURB INLET PROTEC..." 74.5 FT (Sd2-P)', 'LF = line 692 LF',
     194.0, 'derived', 'Estimator repeated the Phase 2 Sd2-F quantity for Phase 3. C-2.2 actually calls Sd2-P (curb inlet protection, "pigs in blanket", C-2.5) at 4 inlets and the estimator measured it at 74.5 FT, but that row feeds no line. Physically Phase 3 = 74.5 LF of Sd2-P (-61.6%).',
     dict(formula='carry = line692 LF', inputs={'phase2LF': {'value': 194, 'unit': 'LF'}}, unit='LF')),
 row(700, 'p67 C-2.2 legend "DS4"', '14393.7 SQ FT printed; raw 14393.68 (maroon, all pervious final areas)', 'SF = legend SF (printed 14393.7)', LEG['p67 DS4'], 'measured',
     'Final stabilization with sodding over every pervious area except the pond. Overlaps the landscape SOD (line 706, 11500 SF from the plant list) - both are carried.',
     dict(formula='stabilizationSF = sum(areas)', inputs={'areas': {'value': [14393.68], 'unit': 'SF'}, 'practices': {'value': ['sod']}}, unit='SF')),
 row(701, 'p83 L-1.0 PLANT LIST row "American Holly / Ilex opaca \'Greenleaf\'"', 'QUANTITY 5; MIN. SIZE 6\' HT.; 12\' O.C.; B&B', 'EA = schedule QTY', PLANT['holly'], 'specified',
     'Schedule carried verbatim. Plan callout says (11) AMERICAN HOLLY and the plan shows 11 holly symbols; the schedule rows look swapped with Eastern Redcedar. Not resolved by the estimator.',
     dict(formula='plantEA = scheduleQty', inputs={'scheduleQty': {'value': 5, 'unit': 'EA'}, 'planCounts': {'value': [11], 'unit': 'EA'}}, unit='EA', tol=0.0)),
 row(702, 'p83 L-1.0 PLANT LIST row "Eastern Redcedar / Juniperus virginiana"', 'QUANTITY 11; 6\' HT.; 40\' O.C.; B&B', 'EA = schedule QTY', PLANT['redcedar'], 'specified',
     'Plan callouts (1) + (5) EASTERN REDCEDAR = 6. Schedule total 16 trees vs plan 17.',
     dict(formula='plantEA = scheduleQty', inputs={'scheduleQty': {'value': 11, 'unit': 'EA'}, 'planCounts': {'value': [1, 5], 'unit': 'EA'}}, unit='EA', tol=0.0)),
 row(703, 'p83 L-1.0 PLANT LIST row "Florida Sunshine Anise / Illicium parviflorum \'Florida Sunshine\'"', 'QUANTITY 17; 3 GAL; 5\' O.C.', 'EA = schedule QTY (= callouts 7+3+7)', PLANT['anise'], 'specified',
     'Plan callouts (7)+(3)+(7) = 17 agree. Estimate prints "GAL: 3\'" - it is 3 GAL.',
     dict(formula='plantEA = scheduleQty', inputs={'scheduleQty': {'value': 17, 'unit': 'EA'}, 'planCounts': {'value': [7, 3, 7], 'unit': 'EA'}}, unit='EA', tol=0.0)),
 row(704, 'p83 L-1.0 PLANT LIST row "Don\'s Dwarf Wax Myrtle / Myrica cerifera \'Don\'s Dwarf\'"', 'QUANTITY 15; 3 GAL; 5\' O.C.', 'EA = schedule QTY (= callouts 6+9)', PLANT['waxmyrtle'], 'specified',
     'Plan callouts (6)+(9) = 15 agree.',
     dict(formula='plantEA = scheduleQty', inputs={'scheduleQty': {'value': 15, 'unit': 'EA'}, 'planCounts': {'value': [6, 9], 'unit': 'EA'}}, unit='EA', tol=0.0)),
 row(705, 'p83 L-1.0 PLANT LIST row "Pinestraw / Mulch A"', '2,500 S.F.', 'SF = schedule SF', PLANT['pinestraw'], 'specified',
     'Designer quantity, not measured. L-1.1 note 6: all beds mulched 3" (pinestraw, wood chips). No bale count line.',
     dict(formula='mulchSF = sum(areas)', inputs={'areas': {'value': [2500], 'unit': 'SF'}, 'depth': {'value': 3, 'unit': 'in'}}, unit='SF')),
 row(706, 'p83 L-1.0 PLANT LIST row "Sod / ---"', '11,500 S.F.', 'SF = schedule SF', PLANT['sod'], 'specified',
     'Designer quantity, not measured ("ALL QUANTITIES ARE FOR A GENERAL GUIDE ONLY"). Overlaps DS4 sodding 14393.68 SF (line 700) on the same lawns.',
     dict(formula='sodSF = sum(areas)', inputs={'areas': {'value': [11500], 'unit': 'SF'}}, unit='SF')),
 row(708, 'p72 C-3.0 legend "23: PROPOSED STORMWATER PO..."', '3074 SQ FT (magenta, pond to the 438 contour)', 'SF = legend SF', LEG['p72 pond'], 'measured',
     'Reference line; pond earthwork is in the grading quantity (31-earthwork). The 438 contour on C-4.0 scales to 3056 SF (-0.6%).',
     dict(formula='pondAreaSF = sum(areas)', inputs={'areas': {'value': [3074], 'unit': 'SF'}}, unit='SF')),
 row(709, '= line 708 (pond area); C-4.2 "6 OZ/SY NON-WOVEN GEOTEXTILE FABRIC"', '3074 SF', 'fabric SF = pond SF (no sides, no laps)', 3074.0, 'derived',
     'Estimator convention: fabric = pond plan area. The C-4.2 trench section wraps fabric on the bottom and sides of the stone bed only: 948 SF bottom + 206 ft perimeter x 5.5 ft = about 2081 SF (-32%).',
     dict(formula='geotextileSF = pondAreaSF', inputs={'pondArea': {'value': 3074, 'unit': 'SF'}}, unit='SF')),
 row(710, 'C-4.0 / C-4.2 stone bed (keynote 7) length, scaled; = ST-1 area / bed width', 'bed outline 95.60 ft x 10.27 ft (C-4.0 vectors at 1"=20\'); ST-1 962.4 SF', 'LF = ceil(bed length) = ceil(95.6)',
     math.ceil(TRENCH_LEN_SCALED), 'measured', 'No legend row. One 6" perforated HDPE underdrain along the trench centreline. Equivalent: 962.4 SF / 10 ft = 96.2 -> 96.',
     dict(formula='underdrainLF = ceil(sum(runs))', inputs={'runs': {'value': [95.6], 'unit': 'LF'}}, unit='LF')),
 row(711, '= line 708 x C-4.2 stone depth', f'3074 SF x (BOTTOM OF INFILTRATION BASIN 435.00 - BOTTOM OF GRAVEL 429.5 = {stone_depth} ft)', 'CY = pond SF x (basin bottom - gravel bottom) / 27',
     LEG['p72 pond'] * stone_depth / 27, 'derived',
     'Exact to 6 dp. The estimator applied the stone depth over the whole pond footprint (3074 SF, top of bank). The stone bed is only the 435 bottom (ST-1 962.4 SF, C-4.2 "MINIMUM SURFACE AREA OF 950 SF"): 962.4 x 5.5 / 27 = 196.0 CY (-68.7%).',
     dict(formula='storageStoneCY = area * (basinBottom - gravelBottom) / 27', inputs={'area': {'value': 3074, 'unit': 'SF'}, 'basinBottom': {'value': 435.00, 'unit': 'ft'}, 'gravelBottom': {'value': 429.5, 'unit': 'ft'}}, unit='CY')),
]
assert [r['lineNo'] for r in R] == ids, ([r['lineNo'] for r in R], ids)

def short(d):
    d = d.replace('\n', ' / ')
    return d if len(d) <= 70 else d[:67] + '...'

rows = []
fixtures = []
for r in R:
    l = lines[r['lineNo']]
    est = l['quantity']
    dp = (r['qty'] - est) / est * 100
    r['dp'] = dp
    rows.append([r['lineNo'], short(l['description']), l['unit'], round(est, 6), r['src'], r['vals'], r['formula'], round(r['qty'], 6), f'{dp:.3f}', r['cls'], r['notes']])
    fx = r['fx']
    if fx:
        fixtures.append({
            'name': f"32c-erosion-landscape line {r['lineNo']}: {short(l['description'])}",
            'formula': fx['formula'], 'inputs': fx['inputs'],
            'expected': {'quantity': round(est, 6), 'unit': fx['unit']},
            'tolerancePct': fx.get('tol', r['tol']),
            'source': f"line {r['lineNo']} / {r['src']}",
        })

with open(OUT + '/reconciliation.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['lineNo', 'description', 'unit', 'estimatorQty', 'source', 'sourceValues', 'formula', 'recomputedQty', 'deltaPct', 'classification', 'notes'])
    w.writerows(rows)
json.dump(fixtures, open(OUT + '/fixtures.json', 'w'), indent=1)

n1 = sum(abs(r['dp']) <= 1 for r in R)
n5 = sum(abs(r['dp']) <= 5 for r in R)
print('lines', len(R), 'within1', n1, 'within5', n5, 'fixtures', len(fixtures))
for r in R:
    print(r['lineNo'], lines[r['lineNo']]['quantity'], round(r['qty'], 6), f"{r['dp']:+.3f}%", r['cls'])

# side calculations used in the docs
print('--- side calcs')
print('LOD polygons sum SF', 20298.88 + 15581.92, 'AC', (20298.88 + 15581.92) / 43560, 'printed LOD SF', 0.9 * 43560)
print('pond - ST-1', 3074 - 962.4, 'vs 2114 delta%', ((3074 - 962.4) - 2114) / 2114 * 100)
print('stone on ST-1 CY', 962.4 * stone_depth / 27, 'delta vs est %', (962.4 * stone_depth / 27 - lines[711]['quantity']) / lines[711]['quantity'] * 100)
print('stone on scaled bed 948.1 CY', 948.1 * stone_depth / 27)
print('fabric wrap bed SF', 948.1 + 206.0 * stone_depth, 'delta %', ((948.1 + 206.0 * stone_depth) - 3074) / 3074 * 100)
print('Sd2-P phase3 delta %', (74.5 - 194) / 194 * 100, 'SD2-F per inlet', 193.7 / 4)
print('sock stakes @2ft', math.ceil(768 / 2) + 1)
print('exit stone CY @6in', 1570 * 0.5 / 27, 'exit min SF', 20 * 50)
print('pi*2.25', math.pi * 2.25, 'delta%', (math.pi * 2.25 - 7) / 7 * 100, 'half circ', math.pi * 2.25 / 2)
print('RT-B printed delta', (5.1 - 5.14) / 5.14 * 100, 'RT-P printed delta', (7.5 - 7) / 7 * 100)
print('ST-1 / 10', 962.4 / 10, 'stadium 95.6x10.27', 95.6 * 10.27 - (4 - math.pi) * (10.27 / 2) ** 2)
print('DS4 + DS3 + pinestraw', 14393.68 + 2114, 'site pervious 20876', 'sod+DS4', 11500 + 14393.68)
print('pinestraw bales @50SF', math.ceil(2500 / 50), 'mulch CY at 3in', 2500 * 0.25 / 27)
print('mulch 2 t/ac on DS1 ph1', 20298.88 / 43560 * 2, 'ph2', 15581.92 / 43560 * 2)
print('washout 7x7 SF', 49, 'legend', 25.1)
print('trees schedule', 5 + 11, 'plan', 11 + 6)
