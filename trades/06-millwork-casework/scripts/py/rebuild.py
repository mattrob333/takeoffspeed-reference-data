"""Rebuild every 06-millwork-casework estimate line from its source values.
Writes reconciliation.csv and fixtures.json into the trade folder."""
import json, csv, os
from fractions import Fraction as F
REF = '/home/user/takeoffspeed-reference-data'
OUT = REF + '/trades/06-millwork-casework'
L = {l['lineNo']: l for l in json.load(open(REF + '/reference/estimate/lines.json'))}
TR = [t for t in json.load(open(REF + '/reference/estimate/trades.json')) if t['trade'] == '06-millwork-casework'][0]['lines']
LEG = {}
for p in json.load(open(REF + '/reference/markups/legends.json')):
    for it in p['items']:
        LEG.setdefault((p['page'], it['name']), it)

def fi(feet=0, inch=0):
    """feet-inches -> feet as Fraction (inch may be Fraction)"""
    return F(feet) + F(inch) / 12
def leg(page, name):
    it = LEG[(page, name)]
    return F(str(it['quantity']))

rows = []   # (lineNo, short, source, sourceValues, formula, recomputed, classification, notes, fixture)
def add(n, short, source, sv, formula, val, cls, notes, fx=None):
    rows.append(dict(n=n, short=short, source=source, sv=sv, formula=formula, val=val, cls=cls, notes=notes, fx=fx))

# ---------------- CHECK DESK (A-708)
add(98, 'Check desk 4\'8-1/2"L x 2\'D x 3\'6"H, PL-5/PL-6', 'A-708 det.1 plan, det.4 elev (no legend on markup p31)', 'units on plan = 1; 4\'-8 1/2" x 2\'-0" x 3\'-6"',
    'EA = count of check-desk units on enlarged plan', F(1), 'counted', 'Furniture schedule TB-08 CHECK WRITING STAND by MILLWORKER, see A-708.',
    dict(formula='count', inputs={'count': {'value': 1, 'unit': 'EA'}}))
# ---------------- TRANSACTION BAR (A-700, A-702)
v = fi(3, 10)
add(99, 'Upper cab 1\'4"D x 3\'4"H, (2) adj shelves, PL-1', 'A-702 det.4 CABINET @ TRANSACTION (called 4/A-702 on A-700 plan: MDF WALL CABINET ABOVE COPIER/PRINTER); legend p25 UPPER CABINET 3.9 FT',
    'overall width 3\'-10" (box 3\'-9" + 1" filler); legend 3.9 FT', 'LF = overall cabinet width as dimensioned', v, 'measured',
    'Estimator typed the dimension (3.83) rather than the PlanSwift reading 3.9 (+1.8%). Depth 1\'-1 1/2" on MFD section 8; estimate says 1\'4"D.',
    dict(formula='cabinet_lf = sum(runs)', inputs={'runs': {'value': [3.8333], 'unit': 'ft'}}))
add(100, 'Base cab 9-1/2"D x 3\'9"H hinged door, adj shelf', 'markup p23 (A-700) legend BASE CABINET (green runs on back elevation 3)', 'legend 4.7 FT (two runs under the PL-4 doors, 2\'-3" boxes + 1 1/2" ends)',
    'LF = PlanSwift linear run', leg(23, 'BASE CABINET'), 'measured', 'Estimate 4.66 is the unrounded PlanSwift value behind the displayed 4.7 (2 x 2\'-4"). Printed boxes 2 x 2\'-3" = 4.50 LF.',
    dict(formula='cabinet_lf = sum(runs)', inputs={'runs': {'value': [4.7], 'unit': 'ft (PlanSwift run, p23 BASE CABINET)'}}))
add(101, 'Pencil drawer 1\'2"D x 1\'11"L', 'markup p23 legend PENCIL DRAWER', 'legend 1.0 EA (yellow dot, back elevation 3)', 'EA = count', leg(23, 'PENCIL DRAWER'), 'counted', 'Note on A-700: pencil drawer at ea. teller station, provided by owner, mounted by millwork.',
    dict(formula='count', inputs={'count': {'value': 1, 'unit': 'EA'}}))
add(102, 'PL-3 finish', 'markup p23 legend PL3 FINISH (red band, back elev 3 + elev 6)', 'legend 6.6 SF; back elev 3 band 9\'-7 3/4" x ~6-7 1/2"; elev 6 band 35 1/2" x 7 1/2"',
    'SF = Σ traced finish faces; estimator rounds up to whole SF', leg(23, 'PL3 FINISH'), 'measured', 'Estimate 7.0 = 6.6 rounded up (+6.1%). By printed dims the two bands are 9.646x0.625 + 2.958x0.625 = 7.88 SF, so the traced band was drawn shallower than the 7 1/2" dimension.',
    dict(formula='laminate_face_sf = sum(areas)', inputs={'areas': {'value': [6.6], 'unit': 'SF'}}))
v = (fi(10, F(27, 4)) - 2 * fi(0, F(5, 4))) * fi(3, F(17, 2))
add(103, 'PL-4 finish', 'markup p23 legend PL-4 FINISH 38.4 (same polygon as WT3 TILE 38.4 and 1/4" backer 38.4 on front elev 4)', 'tile field (10\'-6 3/4" - 2 x 1 1/4" waterfall) x 3\'-8 1/2"',
    'SF = (bar length - 2 x waterfall edge) x knee-wall height; interior PL-4 face taken = customer-side tile face', v, 'derived',
    'Detail 9: PL-4 over 1/2" plywood backing @ interior side. The estimator re-used the front tile polygon for the back PL-4 face.',
    dict(formula='laminate_face_sf = W x H', inputs={'faces': {'value': [[10.3542, 3.7083]], 'unit': 'ft x ft'}}))
add(104, 'PL-5 finish', 'markup p23 legend PL-5 FINISH (peach, elev 6 wire-tray face 46 1/4" wide)', 'legend 6.2 SF', 'SF = traced face; estimator rounds to whole SF', leg(23, 'PL-5 FINISH'), 'measured',
    'Estimate 6.0 = 6.2 rounded down (-3.2%). Printed: 46 1/4" x 18" = 5.78 SF; with the 3" notch band 46 1/4" x 21" = 6.74 SF.',
    dict(formula='laminate_face_sf = sum(areas)', inputs={'areas': {'value': [6.2], 'unit': 'SF'}}))
add(105, 'Mockett MAX6-94 18" brush grommet', 'markup p23 legend (purple dots) + A-700 plan note "(3 TOTAL)"', 'legend 3.0 EA', 'EA = count', leg(23, 'MOCKETT MAX6-94 18" BRUSH GROMMET, SATIN FINISH'), 'counted', 'Plan note prints the total: (3 TOTAL).',
    dict(formula='count', inputs={'count': {'value': 3, 'unit': 'EA'}}))
add(106, 'Richelieu PC2026Z869 square grommet (transaction bar)', 'markup p23 legend (teal dot)', 'legend 1.0 EA', 'EA = count', leg(23, 'RICHELIEU PC2026Z869 SQUARE GROMMET'), 'counted', '',
    dict(formula='count', inputs={'count': {'value': 1, 'unit': 'EA'}}))
# ---------------- BACK COUNTER (A-701)
add(107, 'Base cab 2\'D x 2\'10"H, (2) separate drawers', 'markup p24 legend "5" (magenta run = section 5 printer/VAT cabinet); A-701 elev 2 bay 2\'-0"', 'bay 2\'-0"; legend 2.0 FT',
    'LF = Σ box widths of that section type', fi(2, 0), 'measured', 'Estimate 2.02 is the unrounded PlanSwift reading (legend displays 2.0). Legend rows named only by section number 5/7/9.',
    dict(formula='cabinet_lf = sum(modules)', inputs={'modules': {'value': [2.0], 'unit': 'ft'}}))
v = fi(1, 4) * 2 + fi(1, 6) * 2
add(108, 'Base cab 2\'D x 2\'10"H, (2) drawer', 'markup p24 legend "7" (cyan) ; A-701 elev 2 bays 1\'-4", 1\'-4", 1\'-6", 1\'-6"', 'Σ = 1\'-4"+1\'-4"+1\'-6"+1\'-6"; legend 5.7 FT',
    'LF = Σ box widths', v, 'measured', 'Estimate 5.66 = 5\'-8" truncated.', dict(formula='cabinet_lf = sum(modules)', inputs={'modules': {'value': [1.3333, 1.3333, 1.5, 1.5], 'unit': 'ft'}}))
v = fi(0, F(21, 2))
add(109, 'Base cab 2\'D x 2\'10"H, (5) drawer', 'markup p24 legend "9" (brown) ; A-701 elev 2 bay 10 1/2"', 'bay 10 1/2" = 0.875 LF; legend 0.9 FT',
    'LF = box width; estimator carried a 1 LF minimum', v, 'allowance/judgment', 'Estimate 1.0 = 0.875 rounded up to whole LF (+14%); no source gives 1.0.',
    None)
add(110, '11"D PL shelf, PL-1 (back counter)', 'A-701 axonometric 3 (2 shelves in each side bay) + plan 1 bays 1\'-0"', '4 shelves x 1\'-0" bay', 'LF = shelves x bay width', 4 * fi(1, 0), 'counted', 'No legend row; counted from the axonometric. Elevation dims the right bay 1\'-1 1/2" (4.25 LF if used).',
    dict(formula='shelf_lf = sum(runs) x shelves', inputs={'runs': {'value': [1.0, 1.0], 'unit': 'ft'}, 'shelves': {'value': 2, 'unit': 'EA'}}))
add(111, 'Richelieu PC2026Z869 square grommet (back counter)', 'markup p24 legend (blue dot) ; A-701 plan note', 'legend 1.0 EA', 'EA = count', leg(24, 'RICHELIEU PC2026Z869 SQUARE GROMMET'), 'counted', '',
    dict(formula='count', inputs={'count': {'value': 1, 'unit': 'EA'}}))
add(112, 'PL-1 finish (back counter)', 'markup p24 legend PL-1 FINISH (green: upper face of elevation 2 + plan footprint)', 'legend 83.1 SF; pixel check: elevation face ~12.06 x 5.36 = 64.6 SF + plan 8\'-8" x 2\'-1" = 18.06 SF = 82.7 SF',
    'SF = Σ traced PL-1 faces', leg(24, 'PL-1 FINISH'), 'measured', 'The plan polygon sits on the SLD-1 top; the estimator counted the footprint as PL-1 surface as well as the elevation face.',
    dict(formula='laminate_face_sf = sum(areas)', inputs={'areas': {'value': [83.1], 'unit': 'SF'}}))
# ---------------- LIBRARY (A-702)
v = 4 * fi(1, F(15, 4))
add(113, 'Base cab 1\'D x 2\'8"H, (2) drawer, PL-1 (library)', 'markup p25 legend BASE CABINET (yellow) ; A-702 elev 2 boxes 4 x 1\'-3 3/4"', 'legend 5.3 FT; printed 4 x 1\'-3 3/4" = 5.25',
    'LF = Σ box widths; estimator rounds up to 0.5 LF', leg(25, 'BASE CABINET'), 'measured', 'Estimate 5.5 = 5.3 rounded up to the half foot (+3.8%; +4.8% vs printed 5.25). Estimate cites A701; the library is on A-702.',
    dict(formula='cabinet_lf = sum(runs)', inputs={'runs': {'value': [5.3], 'unit': 'ft (PlanSwift run, p25 BASE CABINET; printed 4 x 1\'-3 3/4" = 5.25)'}}))
v = fi(8, F(21, 2)) + 2 * (2 * fi(2, F(27, 4)) + fi(0, F(3, 2)))
add(114, '1\'D PL shelf, PL-1 (library)', 'markup p25 legend Linear 19.4 FT (blue lines on elev 2)', 'top fixed shelf 3\'-6"+1 1/2"+2\'-6 3/4"+1 1/2"+2\'-6 3/4" = 8\'-10 1/2"; 2 adjustable shelves x (2 x 2\'-6 3/4" + 1 1/2")',
    'LF = Σ shelf runs x tiers', v, 'derived', 'Legend 19.4 (unnamed "Linear" item). Estimate 19.5 rounded up.', dict(formula='shelf_lf = run1 + run2 x 2', inputs={'runs': {'value': [8.875, 5.25, 5.25], 'unit': 'ft'}, 'shelves': {'value': 1, 'unit': 'EA'}}))
add(115, 'PL-1 countertop over 3/4" plywood (library)', 'markup p25 legend PL1 COUNTERTOP (teal) ; A-702 plan 1', 'legend 4.8 SF; printed 5\'-3" x 1\'-0" = 5.25 SF',
    'SF = Σ leg x depth; estimator rounds up to whole SF', leg(25, 'PL1 COUNTERTOP'), 'measured', 'Estimate 5.0 (+4.2% vs legend, -4.8% vs printed 5.25).',
    dict(formula='countertop_sf = sum(areas)', inputs={'areas': {'value': [4.8], 'unit': 'SF (p25 PL1 COUNTERTOP; printed 5\'-3" x 1\'-0" = 5.25)'}}))
add(116, 'PL-1 finish (library)', 'markup p25 legend PL-1 FINISH (salmon: elevation 2 faces incl. cased opening + plan)', 'legend 95.6 SF', 'SF = Σ traced PL-1 faces', leg(25, 'PL-1 FINISH'), 'measured',
    'One salmon polygon on elev 2 extends past the millwork to the right (over-trace).', dict(formula='laminate_face_sf = sum(areas)', inputs={'areas': {'value': [95.6], 'unit': 'SF'}}))
# ---------------- SERVICE COUNTER (A-703)
add(117, 'Base cab 1\'10"D x 2\'8"H (sink base), PL-1', 'A-703 elev 2 last bay 2\'-2" (section 3, undermount sink)', 'bay 2\'-2"', 'LF = box width', fi(2, 2), 'specified', 'No legend row on p26/p27; read from the elevation dimension string 1\'-6" x5 + 2\'-2".',
    dict(formula='cabinet_lf = sum(modules)', inputs={'modules': {'value': [2.1667], 'unit': 'ft'}}))
add(118, '(3) drawer base 1\'11"D x 2\'8"H, PL-1', 'A-703 elev 2 bays 3-5 (section 4)', '3 x 1\'-6"', 'LF = Σ box widths', 3 * fi(1, 6), 'specified', '', dict(formula='cabinet_lf = sum(modules)', inputs={'modules': {'value': [1.5, 1.5, 1.5], 'unit': 'ft'}}))
add(119, 'Trash base 1\'11"D x 2\'8"H, PL-1', 'A-703 elev 2 bays 1-2 (sections 6 shred bin, 5 trash & recycle)', '2 x 1\'-6"', 'LF = Σ box widths', 2 * fi(1, 6), 'specified', 'Shred-bin cabinet (Iron Mountain lock) grouped with the trash base.',
    dict(formula='cabinet_lf = sum(modules)', inputs={'modules': {'value': [1.5, 1.5], 'unit': 'ft'}}))
v = fi(3, 0) + 2 * fi(3, 4)
add(120, 'Upper cab 1\'D x 3\'H, (2) adj shelf, PL-1', 'A-703 elev 2 upper dimension string', '3\'-0" + 3\'-4" + 3\'-4"', 'LF = Σ upper box widths', v, 'specified', 'Estimate 9.66 = 9\'-8" truncated.',
    dict(formula='cabinet_lf = sum(modules)', inputs={'modules': {'value': [3.0, 3.3333, 3.3333], 'unit': 'ft'}}))
add(121, '11"D PL shelf, PL-1 (service counter)', 'A-703 axonometric + elev 2 left bay 3\'-0" under the uppers', '2 shelves x 3\'-0"', 'LF = shelves x bay width', 2 * fi(3, 0), 'counted', '',
    dict(formula='shelf_lf = sum(runs) x shelves', inputs={'runs': {'value': [3.0], 'unit': 'ft'}, 'shelves': {'value': 2, 'unit': 'EA'}}))
# ---------------- JANITOR (A-410)
add(122, '1\'6"D adj white melamine shelves on HD bracket (janitor)', 'markup p16 legend 1\'6"D ADJUSTABLE WHITE MELAMINE SHELVES (mauve, 3 lines on janitor elev 1)', 'legend 12.7 FT = 3 shelves x ~4.23 ft as drawn; plan wall 4\'-6 3/8"',
    'LF = shelves x wall run; estimator rounds up to whole LF', leg(16, '1\'6"D ADJUSTABLE WHITE MELAMINE SHELVES ON HEAVY DUTY BRACKET'), 'measured',
    'Estimate 13 (+2.4%). Printed: 3 x 4\'-6 3/8" = 13.59 LF (-4.3%). Note: brackets "spaced equally (not to exceed 2\'-0")".',
    dict(formula='shelf_lf = sum(runs) x shelves', inputs={'runs': {'value': [4.2333], 'unit': 'ft'}, 'shelves': {'value': 3, 'unit': 'EA'}}))
# ---------------- LOUNGE BOOTH (A-704)
add(123, 'Employee locker 2\'8"W x 1\'2"D x 6\'8"H', 'A-704 plan 8 + A-708 det.9 LOCKER ELEVATION (2\'-8" verify, "LOCKERS BY FURNITURE VENDOR")', '1 locker unit', 'EA = count', F(1), 'counted',
    'Double-count risk: furniture line 367 carries LOCKERS LK-01 1 EA. Legend p28 row "NO" (NAN EA) has no quantity.', dict(formula='count', inputs={'count': {'value': 1, 'unit': 'EA'}}))
add(124, 'Booth table 2\'6"W x 3\'D x 2\'5"H, PL-5 top, Mockett TL28P-3 leg', 'markup p28 legend TABLE (teal dot on section 6)', 'legend 1.0 EA', 'EA = count', leg(28, 'TABLE'), 'counted', '',
    dict(formula='count', inputs={'count': {'value': 1, 'unit': 'EA'}}))
add(125, 'Booth seating 3\'W x 2\'D x 3\'2"H, PL-1, cushions', 'A-704 plan 8 (two benches either side of table) + section 6', '2 benches', 'EA = count', F(2), 'counted', 'No legend row.',
    dict(formula='count', inputs={'count': {'value': 2, 'unit': 'EA'}}))
# ---------------- EMPLOYEE LOUNGE (A-705)
add(126, '1\'6"H 3/4" MDF removable panel w/ 6" face (sink knee space)', 'markup p32 legend "7" (green run = section 7 @ sink); elev 2 bay 2\'-8 1/2"', 'legend 2.7 FT; printed 2\'-8 1/2" = 2.708',
    'LF = knee-space width', leg(32, '7'), 'measured', 'Estimate 2.75 (+1.9% vs legend).', dict(formula='apron_lf = sum(apronRuns)', inputs={'apronRuns': {'value': [2.7], 'unit': 'ft (p32 legend 7; printed 2\'-8 1/2")'}, 'apronHeight': {'value': 1.5, 'unit': 'ft'}}))
add(127, '(3) drawer base 2\'D x 2\'8"H, PL-1 (lounge)', 'A-705 elev 2 bays 2 and 3 (section 5)', '1\'-6" + 1\'-3"', 'LF = Σ box widths', fi(1, 6) + fi(1, 3), 'specified', '',
    dict(formula='cabinet_lf = sum(modules)', inputs={'modules': {'value': [1.5, 1.25], 'unit': 'ft'}}))
add(128, 'Trash base 2\'D x 2\'8"H, PL-1 (lounge)', 'A-705 elev 2 bay 1 (section 4)', '1\'-6"', 'LF = box width', fi(1, 6), 'specified', '', dict(formula='cabinet_lf = sum(modules)', inputs={'modules': {'value': [1.5], 'unit': 'ft'}}))
v = fi(1, 6) + 3 * fi(2, 4)
add(129, 'Upper cab 1\'D x 2\'6"H, (2) adj shelf, PL-1 (lounge)', 'A-705 elev 2 upper dimension string', '1\'-6" + 2\'-4" + 2\'-4" + 2\'-4"', 'LF = Σ upper box widths', v, 'specified', 'Estimate 8.49 (8.5 typed as 8.49).',
    dict(formula='cabinet_lf = sum(modules)', inputs={'modules': {'value': [1.5, 2.3333, 2.3333, 2.3333], 'unit': 'ft'}}))
v = fi(8, 8) * fi(2, 0)
add(130, 'PL-2 countertop over 1" plywood (lounge)', 'markup p32 legend PL2 COUNTERTOP FINISH O/ 1"THK. PLYWOOD (red, plan 1)', 'legend 17.4 SF; printed 8\'-8" x 2\'-0" = 17.33',
    'SF = run x depth; estimator rounds up to whole SF', leg(32, 'PL2 COUNTERTOP FINISH O/ 1"THK. PLYWOOD'), 'measured', 'Estimate 18 (+3.4%).',
    dict(formula='countertop_sf = sum(areas)', inputs={'areas': {'value': [17.4], 'unit': 'SF (p32 legend; printed 8\'-8" x 2\'-0" = 17.33)'}}))
# ---------------- WORK ROOM (A-707, A-708)
add(131, 'Base cab 2\'D x 2\'8"H drawer + adj shelf, PL-1', 'A-707 elev 3 (section 6) box 1\'-5" + 1" filler', '1\'-5" + 1"', 'LF = box + filler', fi(1, 5) + fi(0, 1), 'specified', '', dict(formula='cabinet_lf = sum(runs)', inputs={'runs': {'value': [1.5], 'unit': 'ft'}}))
add(132, 'Base cab 2\'D x 3\'4"H (2) adj shelves, PL-1', 'A-707 elev 4 bay 3 (section 7)', '2\'-6"', 'LF = box width', fi(2, 6), 'specified', '', dict(formula='cabinet_lf = sum(modules)', inputs={'modules': {'value': [2.5], 'unit': 'ft'}}))
add(133, 'Drawer base 2\'D x 3\'4"H, PL-1', 'A-707 elev 4 bay 2 (section 8)', '1\'-3"', 'LF = box width', fi(1, 3), 'specified', '', dict(formula='cabinet_lf = sum(modules)', inputs={'modules': {'value': [1.25], 'unit': 'ft'}}))
add(134, 'Trash base 2\'D x 3\'4"H, PL-1', 'A-707 elev 4 bay 1 (section 9, waste document container)', '1\'-6"', 'LF = box width', fi(1, 6), 'specified', '', dict(formula='cabinet_lf = sum(modules)', inputs={'modules': {'value': [1.5], 'unit': 'ft'}}))
v = (2 * fi(2, F(15, 2)) + fi(0, 1)) + (fi(0, F(7, 4)) * 2 + 2 * fi(2, F(17, 2)))
add(135, 'Upper cab 1\'2"D x 3\'H (2) adj shelves, PL-3', 'A-707 elev 4 + elev 3 upper dims; markup p30 legend Linear 16.5 FT (red line through uppers)', '(2 x 2\'-7 1/2" + 1") + (1 3/4" + 2 x 2\'-8 1/2" + 1 3/4"); legend 16.5 / 1.5 = 11.0',
    'LF = Σ upper runs incl. fillers', v, 'derived', 'TRAP: the Linear 16.5 was traced on 3/4"=1\' elevations while the page scale was set for the 1/2"=1\' plans (x1.5).',
    dict(formula='cabinet_lf = sum(runs)', inputs={'runs': {'value': [5.3333, 5.7083], 'unit': 'ft'}}))
v = 2 * fi(7, F(75, 8))
add(136, '18"D 3/4" white melamine shelves on KV180 bracket', 'A-708 det.12 SHELF AT NIGHT DROP (2 shelves, FULL LENGTH OF WALL); A-120 work-room west wall 7\'-9 3/8"', '2 shelves x 7\'-9 3/8"',
    'LF = shelves x wall length', v, 'derived', 'Two green lines on A-708 det.12 carry no legend (no legend on p31).',
    dict(formula='shelf_lf = sum(runs) x shelves', inputs={'runs': {'value': [7.7813], 'unit': 'ft'}, 'shelves': {'value': 2, 'unit': 'EA'}}))
v1 = (fi(0, F(7, 4)) + 2 * fi(2, F(17, 2))) * fi(2, 0) + fi(0, F(7, 4) + F(61, 8)) * fi(0, F(41, 4))
add(137, 'PL-2 countertop over 1-1/2" plywood w/ support bracket', 'A-707 plan 1 (pairs with elev 3, SUPPORT BRACKET); markup p30 legend PL-2 COUNTERTOP 22.6 SF covers plans 1+2', '5\'-6 3/4" x 2\'-0" + stub 9 3/8" x 10 1/4"',
    'SF = Σ rectangles of the top', v1, 'derived', 'Estimate 12 (rounded up). Plans 1+2 = 22.46 SF vs legend 22.6.',
    dict(formula='countertop_sf = sum(runs) x depth + stub', inputs={'runs': {'value': [5.5625], 'unit': 'ft'}, 'depth': {'value': 2.0, 'unit': 'ft'}, 'stub': {'value': [0.78125, 0.85417], 'unit': 'ft x ft'}}))
v2 = fi(5, 4) * fi(2, 0)
add(138, 'PL-2 countertop over 1-1/2" plywood', 'A-707 plan 2 (pairs with elev 4)', '5\'-4" x 2\'-0"', 'SF = run x depth', v2, 'derived', 'Estimate 11 (rounded up, +3.1%).',
    dict(formula='countertop_sf = sum(runs) x depth', inputs={'runs': {'value': [5.3333], 'unit': 'ft'}, 'depth': {'value': 2.0, 'unit': 'ft'}}))
add(139, 'PL-2 4"H backsplash over 3/4" plywood (work room)', 'markup p30 legend 4"H PL2 BASE O/ 3/4"THK. PLYWOOD (cyan, plans 1+2)', 'legend 13.6 FT; back edges 5\'-4" + 6\'-4 1/8" = 11.68 + ~1.9 LF of side returns',
    'LF = Σ wall edges of the tops; estimator rounds up to whole LF', leg(30, '4"H PL2 BASE O/ 3/4"THK. PLYWOOD'), 'measured', 'Estimate 14 (+2.9%). Same cyan as the (2) 1x4 blocking row: read by legend, not colour.',
    dict(formula='backsplash_lf = sum(edges)', inputs={'backsplash': {'value': [13.6], 'unit': 'ft'}}))
# ---------------- PHONE ROOM (A-110, A-708)
add(140, 'PL-2 countertop over 1-1/2" plywood w/ 21" A&M HYB bracket (phone room)', 'markup p03 (A-110) legend PL2 COUNTERTOP (olive, 1/4" plan)', 'legend 11.0 SF (~5\'-6" room width x 2\'-0")', 'SF = traced plan area', leg(3, 'PL2 COUNTERTOP'), 'measured',
    'Measured at 1/4"=1\' on the floor plan; A-708 det.10 prints 3\'-9 7/8" for the elevation width (conflict).', dict(formula='countertop_sf = sum(runs) x depth', inputs={'runs': {'value': [5.5], 'unit': 'ft'}, 'depth': {'value': 2.0, 'unit': 'ft'}}))
add(141, 'PL-2 4"H backsplash over 3/4" plywood (phone room)', 'markup p03 legend BACKSPLASH (slate blue line, back wall)', 'legend 5.5 FT', 'LF = back-wall edge; estimator rounds up to whole LF', leg(3, 'BACKSPLASH'), 'measured', 'Estimate 6 (+9.1%) - rounding, not a measurement.',
    dict(formula='backsplash_lf = sum(edges)', inputs={'backsplash': {'value': [5.5], 'unit': 'ft'}}))
# ---------------- BOOTH (A-706)
v = 2 * fi(8, 0) * fi(9, 0) + 2 * fi(7, 6) * fi(9, 0) + 2 * fi(0, 9) * fi(9, 0) + fi(10, F(1, 2)) * fi(0, 9)
add(142, '13/16" PL-1 laminate wall panels on Z-clips (booth)', 'markup p29 legend 13/16"THK. PLASTIC LAMINATE FINISH ATTACH W/ Z-CLIPS - PL1 (purple) = 296.9 SF; A-706 plan 1, RCP 11, elev 6', '2 outside faces 8\'-0" x 9\'-0" + 2 inside 7\'-6" x 9\'-0" + 2 jambs 9" x 9\'-0" + header 10\'-0 1/2" x 9"',
    'SF = Σ panel faces W x H', v, 'derived', 'Legend 296.9 includes polygons traced on the NTS 3D view (det.10) and one that runs past the booth on section 5; estimate 300 matches the dimensioned faces (299-305 by reading).',
    dict(formula='paneling_sf = sum(W x H)', inputs={'faces': {'value': [[8.0, 9.0], [8.0, 9.0], [7.5, 9.0], [7.5, 9.0], [0.75, 9.0], [0.75, 9.0], [10.0417, 0.75]], 'unit': 'ft x ft'}}))
v = fi(7, 6) * fi(8, F(13, 2))
add(143, '13/16" PL-1 laminate ceiling panels on Z-clips (booth)', 'markup p29 legend ...AT CEILING... (blue, RCP 11) 64.2 SF', '7\'-6" x (1\'-4" + 4\'-6 1/2" + 2\'-8")', 'SF = ceiling W x L inside booth walls', v, 'derived', '',
    dict(formula='paneling_sf = W x L', inputs={'areas': {'value': [64.0625], 'unit': 'SF'}}))
v = 4 * 2 * fi(9, 0) + 2 * fi(8, F(13, 2))
add(144, '1/2" Fry Reglet U-channel reveal MWU5050 (booth)', 'markup p29 legend 1/2" FRY REGLET U-CHANNEL REVEAL 89.3 FT (red)', '4 wall faces x 2 verticals x 9\'-0" + 2 ceiling runs x 8\'-6 1/2"',
    'LF = Σ reveal runs', v, 'derived', 'UNIT ERROR: estimate unit SF, quantity is LF. The two 4\'-0" cross lines on RCP 11 are recessed linear lights, not reveals.',
    dict(formula='reveal_lf = sum(reveals)', inputs={'reveals': {'value': [9, 9, 9, 9, 9, 9, 9, 9, 8.5417, 8.5417], 'unit': 'ft'}}))
# ---------------- SLD-1 (A-700, A-701, A-703)
v = leg(23, 'SLD-1 COUNTERTOP') + leg(24, 'SLD-1 COUNTERTOP') + leg(26, 'SLD-1 COUNTERTOP')
add(344, 'Solid surface SLD-1 Wilsonart quartz Niwa Q1002', 'markup legends SLD-1 COUNTERTOP p23 73.4 + p24 18.1 + p26 19.7', 'p23 = plan top ~40.5 + waterfall/vertical faces ~33 (elev 3,4,5,6); p24 8\'-8" x 2\'-1" = 18.06; p26 9\'-10" x 2\'-0" = 19.67',
    'SF = Σ legend areas across sheets (tops + waterfall faces)', v, 'measured', 'Estimate 111.14 = unrounded PlanSwift sum. Section note: millwork by owner vendor (General note K), GC install assumed.',
    dict(formula='countertop_sf = sum(areas)', inputs={'areas': {'value': [73.4, 18.1, 19.7], 'unit': 'SF'}}))

assert sorted(r['n'] for r in rows) == sorted(TR), (sorted(r['n'] for r in rows), TR)
out = []
fixtures = []
for r in sorted(rows, key=lambda r: r['n']):
    l = L[r['n']]
    est = F(str(l['quantity']))
    rec = r['val']
    d = (est - rec) / rec * 100
    out.append(dict(lineNo=r['n'], description=r['short'], unit=l['unit'], estimatorQty=float(est), source=r['source'], sourceValues=r['sv'], formula=r['formula'],
                    recomputedQty=round(float(rec), 3), deltaPct=round(float(d), 2), classification=r['cls'], notes=r['notes']))
    if r['fx']:
        fm = r['fx']['formula']
        asm = ('millwork.cabinet-run' if fm.startswith('cabinet') else 'millwork.countertop' if fm.startswith(('countertop', 'backsplash')) else
               'millwork.shelving' if fm.startswith('shelf') else 'millwork.laminate-face' if fm.startswith('laminate') else
               'millwork.paneling' if fm.startswith(('paneling', 'reveal', 'apron')) else 'millwork.accessory or millwork.built-unit')
        fixtures.append({'name': f"L{r['n']} {r['short']}", 'formula': fm, 'engineAssembly': asm, 'inputs': r['fx']['inputs'],
                         'expected': {'quantity': round(float(rec), 3), 'unit': 'LF' if r['n'] == 144 else l['unit']}, 'tolerancePct': 1.0,
                         'estimatorQty': float(est), 'estimatorUnit': l['unit'], 'estimatorDeltaPct': round(float(d), 2), 'classification': r['cls'],
                         'source': f"line {r['n']} / {r['source'].split(';')[0]}"})
os.makedirs(OUT, exist_ok=True)
with open(OUT + '/reconciliation.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
json.dump(fixtures, open(OUT + '/fixtures.json', 'w'), indent=1)
n1 = sum(abs(o['deltaPct']) <= 1.0 for o in out); n5 = sum(abs(o['deltaPct']) <= 5.0 for o in out)
print('lines', len(out), 'within1', n1, 'within5', n5, 'fixtures', len(fixtures))
from collections import Counter
print(Counter(o['classification'] for o in out))
for o in out:
    flag = '' if abs(o['deltaPct']) <= 1 else ('*' if abs(o['deltaPct']) <= 5 else '**')
    print(o['lineNo'], o['unit'], o['estimatorQty'], o['recomputedQty'], o['deltaPct'], o['classification'], flag)
