# SUPERSEDED 2026-10-13: the published files in trades/32b-site-structures/ were hand-corrected after review (legend row 384.3 present, 666/667 fixtures, bond-beam ambiguity, formula unit conversions). Do not re-run this to regenerate them.
"""Rebuild every 32b-site-structures estimate line from its source and write
reconciliation.csv + fixtures.json. Quantities only."""
import csv, json, math, sys

REF = '/home/user/takeoffspeed-reference-data'
OUT = REF + '/trades/32b-site-structures'
L = {l['lineNo']: l for l in json.load(open(REF + '/reference/estimate/lines.json'))}
TR = [t for t in json.load(open(REF + '/reference/estimate/trades.json')) if t['trade'] == '32b-site-structures'][0]['lines']

def circ(d_in):
    """Estimator's circle area: diameter in feet rounded to 2 dp, area rounded to 2 dp."""
    d = round(d_in / 12, 2)
    return round(math.pi * d * d / 4, 2)

# ---- source values (markup legends / sheets) ----
ADA_SIGNS = 1          # p72 C-3.0 'ADA PARKING SIGN - C6.0' 1.0 EA
STOP = 3               # p72 '12: R1-1:STOP SIGN' 3.0 EA
DNE = 2                # p72 '13: RF-1: DO NOT ENTER SIGN' 2.0 EA
TRANSFORMER_SF = 16.0  # p72 '14: TRANSFORMER PAD' 16.0 SQ FT
CLEANOUTS = 6          # p77 C-5.0 'SANITARY CLEANOUTS' 6.0 EA
PAD_IN = 18            # P-301/P-302 note 3 '18"X18"X6" THICK CONCRETE PAD'
DUMP_SLAB_SF = 384.3   # p72 '21: HEAVY DUTY CONCRETE PAVE...' 384.3 SQ FT (purple row)
WALL_LF = 36.22        # p72 'DUMPSTER ENCLOSURE WALL' 36.2 FT (estimate keeps 36.22)
FTG_W, FTG_T = 2.0, 1.0            # A-190 wall section 3: 2'-0" x 1'-0"
CMU_H = 8.0                        # A-190: 6'-8" exposed + 1'-4" below grade
EXPOSED_H = round(6 + 8 / 12, 2)   # 6'-8" -> 6.67 (estimator rounding)
EXC_W = FTG_W + 2 * 1.0            # 1' working space each side -> 4.0
EXC_D = round(1 + 16 / 12, 2)      # 1'-0" footing + 1'-4" CMU below grade -> 2.33
CMU_BELOW_CY = 1.16                # estimator's wall-below-grade volume (36.22 x 0.65 x 1.33 / 27 = 1.1597)
GROUT_CY_SF = 0.0112               # estimator convention (job-derived)
MORTAR_CF_SF = 0.1675              # estimator convention (job-derived) = 0.67 ft x 25%
WALL_LF_ROUND = round(WALL_LF)     # 36 for every per-LF accessory line
WEEP_FACTOR = 0.33                 # estimator: 36 x 0.33 (4" strip, suspected unit slip)
GATES = 1                          # p72 'DUMPSTER GATE' 1.0 EA
DUMPSTERS = 2                      # A-190 plan 4: two boxes '2 YARD DUMPSTER'
MONUMENT = 1                       # p72 'PROPOSED MONUMENT SIGN' 1.0 EA
CANOPY_SF = 61.7                   # p89 A-401 canopy row 61.7 SQ FT
ATM = 1                            # p89 A-401 ATM row 1.0 EA
POLES = 1 + 4                      # p43 E-011 '1P4F LIGHT' 1.0 + '2P4DA LIGHT' 4.0
POLE_D_IN, POLE_BURY, POLE_EXP = 18, 6.0, 2.5   # E-012 pole base detail 3: 1'-6", 6'-0", 2'-6"

rows = []  # lineNo, src, srcVals, formula, recomputed, cls, notes, fixture
def add(n, src, vals, formula, q, cls, notes, fx=None):
    rows.append(dict(n=n, src=src, vals=vals, formula=formula, q=q, cls=cls, notes=notes, fx=fx))

a12 = circ(12); a8 = circ(8); a18 = circ(POLE_D_IN)
ada = a12 * 3.5 * ADA_SIGNS / 27
add(651, 'p72 C-3.0 legend + C-6.0 ADA SIGN MOUNTING DETAIL', f'"ADA PARKING SIGN - C6.0" {ADA_SIGNS} EA; C-6.0 "3\'-6"" MIN." embed; 12" hole dia assumed (8" STD pipe inside)',
    'CY = round(pi/4 x round(D_ft,2)^2, 2) x H x n / 27 = 0.79 x 3.5 x 1 / 27', ada, 'derived',
    'Count measured; hole diameter is the estimator\'s choice (detail shows only the 8" concrete-filled pipe); 3\'-6" from the detail. Circle area carried as 0.79 SF (2-dp rounding).',
    dict(formula='pierConcreteCY = round(pi*round(D,2)^2/4,2) * H * n / 27', inputs={'D': [12, 'in'], 'H': [3.5, 'ft'], 'n': [1, 'EA']}))
add(652, '= line 651 (excavation, no over-dig)', '0.79 SF x 3.5 ft x 1', 'excavation CY = pier concrete CY (full depth buried)', ada, 'derived', 'Pier poured against earth: excavation equals concrete volume.',
    dict(formula='pierExcavationCY = round(pi*round(D,2)^2/4,2) * buried * n / 27', inputs={'D': [12, 'in'], 'buried': [3.5, 'ft'], 'n': [1, 'EA']}))
add(653, '= line 652 (haul-off, no backfill)', '0.79 SF x 3.5 ft x 1', 'haul CY = excavation CY', ada, 'derived', 'No backfill around a pier: all spoil hauled. Bank CY, no swell.',
    dict(formula='pierHaulCY = pierExcavationCY', inputs={'D': [12, 'in'], 'buried': [3.5, 'ft'], 'n': [1, 'EA']}))
s8 = a8 * 3.0 * (STOP + DNE) / 27
add(654, 'p72 C-3.0 legend + C-6.0 TRAFFIC SIGN MOUNTING DETAIL', f'"12: R1-1:STOP SIGN" {STOP} EA + "13: RF-1: DO NOT ENTER SIGN" {DNE} EA; C-6.0 "8" DIA. MIN. CONC. FOOTING", 3\'',
    'CY = round(pi/4 x 0.67^2, 2) x 3 x (3+2) / 27 = 0.35 x 3 x 5 / 27', s8, 'derived',
    'STOP and DO NOT ENTER share the traffic sign mounting detail, so their footings are one line (5).',
    dict(formula='pierConcreteCY = round(pi*round(D,2)^2/4,2) * H * n / 27', inputs={'D': [8, 'in'], 'H': [3.0, 'ft'], 'n': [5, 'EA']}))
add(655, '= line 654', '0.35 SF x 3 ft x 5', 'excavation CY = pier concrete CY', s8, 'derived', 'Per footing type (8" x 3\'), not merged with the 12" ADA footing.',
    dict(formula='pierExcavationCY = round(pi*round(D,2)^2/4,2) * buried * n / 27', inputs={'D': [8, 'in'], 'buried': [3.0, 'ft'], 'n': [5, 'EA']}))
add(656, '= line 655', '0.35 SF x 3 ft x 5', 'haul CY = excavation CY', s8, 'derived', 'No backfill.',
    dict(formula='pierHaulCY = pierExcavationCY', inputs={'D': [8, 'in'], 'buried': [3.0, 'ft'], 'n': [5, 'EA']}))
add(657, 'p72 C-3.0 legend', f'"14: TRANSFORMER PAD" {TRANSFORMER_SF} SQ FT', 'SF = measured area', TRANSFORMER_SF, 'measured',
    'C-3.0 keynote 14 "CONCRETE TRANSFORMER PAD PER UTILITY OWNER\'S REQUIREMENTS" - no detail; 10" thickness is the estimator\'s assumption ("ASSUMED DETAILS").',
    dict(formula='padSF = sum(measured areas)', inputs={'area': [16.0, 'SF']}))
co = CLEANOUTS * (PAD_IN / 12) ** 2
add(658, 'p77 C-5.0 legend + P-301/P-302 plumbing note 3 + P-501 cleanout-to-grade detail', f'"SANITARY CLEANOUTS" {CLEANOUTS} EA; "18"X18"X6" THICK CONCRETE PAD"',
    'SF = n x (18/12)^2 = 6 x 2.25', co, 'counted',
    'Count from the civil utility legend; pad size from the plumbing note. Estimate text says 8" thick, plumbing note/detail says 6" (thickness does not affect the SF quantity). P-302 legend also shows one "18x18x6 THK. CONCRETE PAD FOR CLEAN O..." 1 EA (building-side cleanout, inside the 6).',
    dict(formula='padSF = n * W * L', inputs={'n': [6, 'EA'], 'W': [18, 'in'], 'L': [18, 'in']}))
add(663, 'p72 C-3.0 legend (purple row)', f'"21: HEAVY DUTY CONCRETE PAVE..." {DUMP_SLAB_SF} SQ FT', 'SF = measured area (enclosure floor + apron)', DUMP_SLAB_SF, 'measured',
    'Legend prints 384.3; estimate keeps PlanSwift precision 384.31. This purple row is visible on the page image but is MISSING from legends.json/legends.csv (only the teal 241.8 row of the same name was captured). Thickness/rebar from A-190 section 3 ("6" CONCRETE SLAB ON GRADE W/#4 AT 12" O.C. EACH WAY", "10 MIL VAPOR BARRIER").',
    dict(formula='slabSF = sum(measured areas)', inputs={'area': [384.3, 'SF']}))
ftg = WALL_LF * FTG_W * FTG_T / 27
add(664, 'p72 legend wall LF x A-190 section 3', f'"DUMPSTER ENCLOSURE WALL" 36.2 FT (36.22); footing 2\'-0" x 1\'-0"', 'CY = LF x W x T / 27 = 36.22 x 2 x 1 / 27', ftg, 'derived',
    'Footing runs the measured wall centerline; no deduction or extension at the gate posts.',
    dict(formula='wallFootingCY = LF * W * T / 27', inputs={'LF': [36.22, 'LF'], 'W': [24, 'in'], 'T': [12, 'in']}))
exc = WALL_LF * EXC_W * EXC_D / 27
add(665, 'wall LF x A-190 section 3', '36.22 LF; trench 2\'-0" + 2 x 1\'-0" = 4.0\'; depth 1\'-0" + 1\'-4" = 2.33\'', 'CY = LF x (W + 2 x 1\') x (T + CMU below grade) / 27 = 36.22 x 4 x 2.33 / 27', exc, 'derived',
    'Depth carried as 2.33 (2 dp), not 2-1/3 (0.14% lower). Working space 1\' each side is the estimator convention (same as the building footings).',
    dict(formula='wallFootingExcavationCY = LF * (W + 2*ws) * round(T + belowGrade, 2) / 27', inputs={'LF': [36.22, 'LF'], 'W': [2.0, 'ft'], 'ws': [1.0, 'ft'], 'T': [1.0, 'ft'], 'belowGrade': [16, 'in']}))
bf = exc - ftg - CMU_BELOW_CY
add(666, 'lines 665 - 664 - CMU below grade', '12.502607 - 2.682963 - 1.16 CY', 'backfill CY = excavation - footing - CMU below grade (1.16 CY)', bf, 'derived',
    'Wall-below-grade volume the estimator carried is exactly 31.32 CF = 1.16 CY (36.22 x 0.65 x 1.33 / 27 = 1.1597 rounded); nominal 8" x 1\'-4" gives 1.1924 CY. Physical formula reproduces within 0.2%.',
    dict(formula='wallFootingBackfillCY = excavation - footing - LF*t*belowGrade/27', inputs={'LF': [36.22, 'LF'], 'W': [2.0, 'ft'], 'ws': [1.0, 'ft'], 'T': [1.0, 'ft'], 'belowGrade': [16, 'in'], 't': [8, 'in']}, tol=0.5))
haul = exc - bf
add(667, 'line 665 - line 666', '12.502607 - 8.659644 CY', 'haul CY = excavation - backfill = footing + CMU below grade', haul, 'derived',
    'Haul-off is the displaced volume, bank CY, no swell. Nominal-dimension formula gives 3.8754 (+0.84%).',
    dict(formula='wallFootingHaulCY = LF*W*T/27 + LF*t*belowGrade/27', inputs={'LF': [36.22, 'LF'], 'W': [2.0, 'ft'], 'T': [1.0, 'ft'], 'belowGrade': [16, 'in'], 't': [8, 'in']}, tol=1.0))
cmu = WALL_LF * CMU_H
add(668, 'wall LF x A-190 section 3 heights', '36.22 LF x (6\'-8" + 1\'-4")', 'SF = LF x H(top of footing to underside of cap) = 36.22 x 8.0', cmu, 'derived',
    'Height includes the 1\'-4" of CMU below grade; no gate deduction (wall stops at the gate posts).',
    dict(formula='cmuSF = LF * H', inputs={'LF': [36.22, 'LF'], 'H': [8.0, 'ft']}))
grout = cmu * GROUT_CY_SF
add(669, 'line 668 x estimator grout ratio', '289.76 SF x 0.0112 CY/SF', 'CY = CMU SF x 0.0112 (= 0.3024 CF/SF)', grout, 'derived',
    'Job-derived convention: 0.0112 CY/SF exactly. That is a solid-grout rate for 8" CMU (NCMA ~0.26 CF/SF + ~16%), although the section grouts only the #5 @ 32" cells and the K.O. bond beam.',
    dict(formula='groutCY = cmuSF * 0.0112', inputs={'cmuSF': [289.76, 'SF'], 'groutCYperSF': [0.0112, 'CY/SF']}))
mortar = cmu * MORTAR_CF_SF / 27
add(670, 'line 668 x estimator mortar ratio', '289.76 SF x 0.1675 CF/SF', 'CY = CMU SF x 0.1675 / 27', mortar, 'derived',
    'Job-derived convention: 0.1675 CF/SF = 0.67 ft wall x 25% (a gross-volume share, ~1.75x the 8.5 CF/100 block rule).',
    dict(formula='mortarCY = cmuSF * 0.1675 / 27', inputs={'cmuSF': [289.76, 'SF'], 'mortarCFperSF': [0.1675, 'CF/SF']}))
for n, what in [(671, 'bond beam (1 course at top)'), (672, 'precast cap'), (680, 'thru-wall flashing w/ integral drip'), (681, 'continuous drip'), (682, 'continuous sealant')]:
    add(n, 'wall LF (rounded) + A-190 section 3 / wall cap detail 5', '36.22 LF -> 36', f'LF = round(wall LF) for the {what}', WALL_LF_ROUND, 'derived',
        'Estimator rounded the 36.22 measured LF to 36 for every per-LF wall accessory; unrounded gives 36.22 (+0.61%).',
        dict(formula='capLF = round(wallLF)', inputs={'wallLF': [36.22, 'LF']}))
coat = WALL_LF * EXPOSED_H
add(673, 'wall LF x A-190 exposed height', '36.22 LF x 6\'-8" (6.67)', 'SF = LF x exposed height x 1 face', coat, 'derived',
    'One face only: section 3 puts "PAINTED 5/8" CEMENTITIOUS COATING ON CMU WALL TO EPT-1" on the outside face and "EXPOSED CMU PAINTED TO MATCH EIFS-1" inside. Height 6\'-8" carried as 6.67.',
    dict(formula='coatingSF = wallLF * round(exposedH,2) * faces', inputs={'wallLF': [36.22, 'LF'], 'exposedH': [80, 'in'], 'faces': [1, 'EA']}))
add(678, 'p72 C-3.0 legend', f'"DUMPSTER GATE" {GATES} EA', 'EA = count', GATES, 'counted', 'One 16\'-0" x 6\'-8" double-leaf gate; TE2 posts, TE3 sign, TE4 cane bolt, TE5 wheel ride in the description, not as lines.',
    dict(formula='count', inputs={'count': [1, 'EA']}))
add(679, 'A-190 floor plan 4', 'two boxes labelled "2 YARD DUMPSTER"', 'EA = count', DUMPSTERS, 'counted', 'Counted on the enlarged plan (one label, two containers); not on any legend.',
    dict(formula='count', inputs={'count': [2, 'EA']}))
add(683, 'wall LF (rounded) x 0.33', '36 LF x 0.33', 'LF = 36 x 0.33 (estimator)', round(WALL_LF_ROUND * WEEP_FACTOR, 4), 'derived',
    'Reproduces exactly but the basis is inferred: 0.33 ft = 4" looks like an area conversion (SF of a 4" strip) carried under LF. A weep screed runs the base of the coated face, physically ~36.22 LF. Flag, do not copy.',
    dict(formula='weepLF = round(wallLF) * 0.33  (estimator; physical = wallLF)', inputs={'wallLF': [36.22, 'LF'], 'factor': [0.33, 'ft']}))
add(707, 'p72 C-3.0 legend', f'"PROPOSED MONUMENT SIGN" {MONUMENT} EA', 'EA = count', MONUMENT, 'counted', 'Keynote: "PROPOSED MONUMENT SIGN, DESIGNED AND PERMITTED BY OTHERS"; no footing taken off.',
    dict(formula='count', inputs={'count': [1, 'EA']}))
add(712, 'p89 A-401 legend', f'"PREFABRIFATED CANOPY ..." {CANOPY_SF} SQ FT', 'SF = round(measured area)', round(CANOPY_SF), 'measured', 'Legend 61.7 SF, carried as 62 (whole SF). "W/ COLUMNS 2" from the plan (canopy column & baseplate x2).',
    dict(formula='canopySF = round(measured area)', inputs={'area': [61.7, 'SF']}))
add(717, 'p89 A-401 legend', f'"ATM BY BANK EQUIPMENT VENDOR ..." {ATM} EA', 'EA = count', ATM, 'counted', 'Vendor item; description carries the A-401 conduit stub-up requirements.',
    dict(formula='count', inputs={'count': [1, 'EA']}))
lp = a18 * (POLE_BURY + POLE_EXP) * POLES / 27
add(718, 'p43 E-011 legend + E-012 pole base detail 3', f'"1P4F LIGHT" 1 + "2P4DA LIGHT" 4 = {POLES} poles; 1\'-6" dia, 6\'-0" below + 2\'-6" above grade', 'CY = round(pi/4 x 1.5^2,2) x 8.5 x 5 / 27 = 1.77 x 8.5 x 5 / 27', lp, 'derived',
    'One base per pole (both fixture types are pole mounted, "SEE DETAIL FOR POLE HEIGHT").',
    dict(formula='pierConcreteCY = round(pi*round(D,2)^2/4,2) * (buried+exposed) * n / 27', inputs={'D': [18, 'in'], 'buried': [6.0, 'ft'], 'exposed': [2.5, 'ft'], 'n': [5, 'EA']}))
lpx = a18 * POLE_BURY * POLES / 27
add(719, 'line 718 buried part', '1.77 SF x 6.0 ft x 5', 'excavation CY = area x buried depth x n / 27', lpx, 'derived', 'Only the 6\'-0" below grade is excavated; the 2\'-6" exposed base is formed.',
    dict(formula='pierExcavationCY = round(pi*round(D,2)^2/4,2) * buried * n / 27', inputs={'D': [18, 'in'], 'buried': [6.0, 'ft'], 'n': [5, 'EA']}))
add(720, '= line 719', '1.77 SF x 6.0 ft x 5', 'haul CY = excavation CY', lpx, 'derived', 'No backfill.',
    dict(formula='pierHaulCY = pierExcavationCY', inputs={'D': [18, 'in'], 'buried': [6.0, 'ft'], 'n': [5, 'EA']}))

assert sorted(r['n'] for r in rows) == sorted(TR), set(TR) ^ {r['n'] for r in rows}
rows.sort(key=lambda r: r['n'])
fixtures = []
with open(OUT + '/reconciliation.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['lineNo', 'description', 'unit', 'estimatorQty', 'source', 'sourceValues', 'formula', 'recomputedQty', 'deltaPct', 'classification', 'notes'])
    within1 = within5 = 0
    for r in rows:
        l = L[r['n']]
        est = l['quantity']
        rq = round(r['q'], 6)
        d = 0.0 if est == 0 else (rq - est) / est * 100
        within1 += abs(d) <= 1; within5 += abs(d) <= 5
        desc = l['description'].split('\n')[0].strip()
        path = ' > '.join(l['sectionPath'] or [])
        if desc in ('EXCAVATION REQUIRED', 'HAULOFF', 'BACKFILL REQUIRED', 'CONTINUOUS DRIP', 'CONTINUOUS SEALANT', 'STUCCO WEEP SCREEN', '2 YARD DUMPSTER'):
            desc = f'{path}: {desc}'
        desc = desc[:90]
        w.writerow([r['n'], desc, l['unit'], est, r['src'], r['vals'], r['formula'], rq, f'{d:.3f}', r['cls'], r['notes']])
        fx = r['fx']
        fixtures.append({
            'name': f'32b-site-structures line {r["n"]}: {desc}',
            'formula': fx['formula'],
            'inputs': {k: {'value': v[0], 'unit': v[1]} for k, v in fx['inputs'].items()},
            'expected': {'quantity': est, 'unit': l['unit']},
            'tolerancePct': fx.get('tol', 0.1),
            'source': f'line {r["n"]} / {r["src"]}',
        })
json.dump(fixtures, open(OUT + '/fixtures.json', 'w'), indent=1)
print('lines', len(rows), 'within1', within1, 'within5', within5)
for r in rows:
    est = L[r['n']]['quantity']; print(r['n'], est, round(r['q'], 6), f"{(r['q']-est)/est*100:.4f}%")
