"""Build reconciliation.csv and fixtures.json for trade 26-electrical.

Every recomputed quantity is computed here from legend values (markup page:row),
never typed as a result.
"""
import csv, json, os, sys

REF = '/home/user/takeoffspeed-reference-data'
OUT = os.path.join(REF, 'trades/26-electrical')
os.makedirs(OUT, exist_ok=True)

lines = {x['lineNo']: x for x in json.load(open(os.path.join(REF, 'reference/estimate/lines.json')))}
trade = [t for t in json.load(open(os.path.join(REF, 'reference/estimate/trades.json'))) if t['trade'] == '26-electrical'][0]
assert len(trade['lines']) == 108

# Legend values. (page, item as printed, qty, unit). Rows marked * are on the
# page image but missing from legends.json (see reading-guide traps).
def L(page, item, qty, unit='EA'):
    return {'page': page, 'item': item, 'qty': qty, 'unit': unit}

# lineNo -> (short description, sources[list of L], classification, formula id, notes)
S = {}
def add(n, short, srcs, cls, formula, notes='', recompute=None):
    S[n] = dict(short=short, srcs=srcs, cls=cls, formula=formula, notes=notes, recompute=recompute)

# ---- E-010 / E-011 site
add(495, '1P4F pole light, 1 head', [L(43, '1P4F LIGHT', 1)], 'counted', 'count-sum', 'E-011 schedule: 1HEAD, pole 27\'-6"; count = pole assemblies')
add(496, '2P4DA pole light, 2 heads 180 deg', [L(43, '2P4DA LIGHT', 4)], 'counted', 'count-sum', 'E-011 schedule: 2HEAD, 180 deg; estimator counts 4 pole assemblies (8 heads), not heads')
add(497, 'Safety switch 30A 3P fused @20A', [L(42, 'SAFETY SWITCH, 30A, 3 POLE, FUSED@ 20A', None)], 'judgment', 'none',
    'PlanSwift legend prints NAN EA (no marker placed); name is the E-001 symbol "30/20". Estimator entered 1 by hand. Plan shows two WP disconnects at keynotes 2 (irrigation) and 3 (DDCV) that are carried as other lines')
add(498, '120V 20A toggle switch in bell box (monument sign)', [L(42, '120V, 20A TOGGLE SWITCH IN METALLIC BELL BOX W/ METALLIC...', 1)], 'counted', 'count-sum', 'keynote 13 monument sign power')
add(499, 'Service disconnect switch', [L(42, 'SERVICE DISCONNECT SWITCH', 1)], 'counted', 'count-sum', 'keynote 5; page 87 repeats it as "5: SERVICE DISCONNECT" 1 EA - not added')
add(500, '120V 20A GFCI WR duplex receptacle (site)', [L(42, '120V, 20A GFCI WEATHER RESISTANT DUPLEX RECEPTACLE', 1)], 'counted', 'count-sum', 'keynote 6 maintenance receptacle; page 87 row 6 is the same device - not added')
add(501, 'Transformer (slab box w/ traffic guard)', [L(42, 'TRANSFORMER SLABBOX W/ TRAFFIC GUARD', 1)], 'counted', 'count-sum', 'keynote 9; utility transformer, contractor slab box + guards')
add(502, 'Electric utility meter', [L(42, 'ELECTRIC UTILITY METER', 1)], 'counted', 'count-sum', 'keynote 4; E-800: 320A cont / 400A self-contained meter base')
add(503, 'Junction box (site)', [L(42, 'JUNCTION BOX', 4)], 'counted', 'count-sum', 'page 87 shows the same 4 boxes again - estimator did not double count')
add(504, 'DDCV hot box', [L(42, 'DDCV HOT BOX', 1)], 'counted', 'count-sum', 'keynote 3: DDCV hotbox power; disconnect NEMA 3R')
add(505, '(2) 4" conduit (telephone service entrance)', [L(42, '(2) 4"DIA CONDUIT', 71.5, 'FT'), L(44, '(2) 4"DIA CONDUIT', 30.2, 'FT')], 'measured', 'conduit-route-lf',
    'E-010 keynote 1 + E-100 keynote 18. Route LF of the pair; NOT x2 conduits')
add(506, '1" conduit (AV at remote drive-thru)', [L(41, '1"DIA CONDUIT', 4.8, 'FT'), L(41, '1"DIA CONDUIT', 15.4, 'FT')], 'measured', 'conduit-route-lf',
    'Two legend rows, same name (magenta 4.8 stubs "1"C FOR AV", brown 15.4 canopy-to-building run). legends.json lost the 4.8 row. Estimator carried a round 20.0')
add(507, '(2) 2" conduit (VTM/ATM data)', [L(41, '(2) 2"DIA CONDUIT', 15.4, 'FT'), L(42, '(2) 2"DIA CONDUIT', 61.8, 'FT'), L(44, '(2) 2"DIA CONDUIT', 30.2, 'FT')], 'measured', 'conduit-route-lf',
    'Three pages summed (RDT detail, site plan secondary/data route, E-100 keynote 17). Route LF, not x2')
add(508, '(2) 5" conduit (HV primary)', [L(42, '(2) 5"DIA CONDUIT', 11.4, 'FT')], 'measured', 'conduit-route-lf', 'keynote 8, property line to transformer; route LF')
add(509, 'Stub-out & terminate per utility', [L(42, 'STUBOUT & TERMINATE PER UTILITY COMPANY REQUIREMENT...', 1)], 'counted', 'count-sum', 'keynote 7')
add(510, 'Allowance: wiring, conduit & fittings (2000 SF)', [], 'allowance', 'area-allowance',
    'No drawn source. Basis area 2,000 SF = title-block 1,900 SF rounded up to the next 500/1000; same 2,000 SF basis on plumbing 403, HVAC 445, low voltage 622. Covers all undrawn branch wiring and riser feeders')

# ---- E-130 luminaires (page 46)
lum = [
    (511, 'A', 8, 'Type A 2x2 LED troffer (estimate tag reads AE)', 'estimate tag column says AE but description/model is type A (no -EL); quantity = legend A'),
    (512, 'AE', 6, 'Type AE 2x2 LED troffer w/ EM battery', ''),
    (513, 'B', 3, 'Type B recessed linear', ''),
    (514, 'C', 53, 'Type C Tacada pendant', 'schedule note: provide ten (10) extra for attic stock - estimator did not add'),
    (515, 'F3', 1, 'Type F3 3ft wall striplight', ''),
    (516, 'FEM', 2, 'Type FEM 48in suspended strip w/ EM', ''),
    (518, 'G1', 22, 'Type G1 5in downlight', ''),
    (519, 'GEM', 2, 'Type GEM 5in downlight w/ EM', ''),
    (520, 'J', 9, 'Type J 6in square downlight', 'estimate tag column blank ("120 J:")'),
    (521, 'JE', 4, 'Type JE 6in square downlight w/ EM', ''),
    (523, 'PB', 1, 'Type PB Paravo pendant', ''),
    (524, 'S', 2, 'Type S 4ft strip LED', ''),
    (525, 'T', 7, 'Type T 2ft T-bar LED', ''),
    (526, 'TE', 9, 'Type TE 2ft T-bar LED w/ EM', ''),
    (527, 'U1', 2, 'Type U1 in-ground LED', ''),
    (528, 'U3', 1, 'Type U3 in-ground LED', ''),
    (530, 'X1', 4, 'Type X1 recessed exit sign', ''),
    (531, 'X2', 2, 'Type X2 wall exit sign', ''),
    (532, 'X3', 1, 'Type X3 EM egress wallpack', ''),
]
for n, tag, q, short, note in lum:
    add(n, short, [L(46, tag, q)], 'counted', 'count-sum', ('fixture tag ' + tag + '; ' + note).strip('; '))
for n, tag, q, short, note in [
    (517, 'G', 26.8, 'Type G linear cove wall washer (LF)', 'schedule: LENGTH AS SPECIFIED ON PLANS; PlanSwift linear measure'),
    (522, 'L', 30.4, 'Type L Tetra contour LED (LF)', 'linear measure'),
    (529, 'UC', 9.1, 'Type UC undercabinet strip (LF)', 'linear measure; schedule note: ten (10) extra for attic stock - not added'),
]:
    add(n, short, [L(46, tag, q, 'FT')], 'measured', 'linear-fixture-lf', note)
add(533, 'Drive-thru alert light', [L(44, 'DRIVE THRU ALERT LIGHT', 1)], 'counted', 'count-sum', 'E-100 keynote 15')

# ---- E-100 receptacles (page 44 unless noted)
def p44(n, short, item, q, note='', cls='counted'):
    add(n, short, [L(44, item, q)], cls, 'count-sum', note)
p44(534, 'Duplex receptacle 20A 125V', 'DUPLEX RECEPTACLE, 20A, 125V', 6)
add(535, 'GFCI duplex receptacle 20A', [L(44, 'GFCI DUPLEX RECEPTACLE, 20A, 125V', 6), L(49, 'GFCI DUPLEX RECEPTACLE, 20A, 125V', 1)], 'counted', 'count-sum', 'plan + IT room enlarged plan on E-702')
add(536, 'Quad receptacle 20A', [L(44, 'QUAD RECEPTACLE, 20A, 125V', 3), L(49, 'QUAD RECEPTACLE, 20A, 125V', 14)], 'counted', 'count-sum', 'plan + E-702 IT room (14); the separate p44 row "QUAD RECEPTACLE 20A, 125V" (no comma) 1 EA is line 546')
p44(537, 'TR GFCI duplex receptacle', 'TEMPER RESISTANT GFCI DUPLEX RECEPTACLE, 20A, 125V', 1, 'second of two same-name rows (the first prints NAN EA); the marker is the dishwasher receptacle, keynotes 21 + 24')
p44(538, 'TR quad receptacle', 'TAMPER RESISTANT QUAD RECEPTACLE, 20A, 125V', 7)
p44(539, 'Simplex receptacle', 'SIMPLEX LEFT RECEPTACLE, 20A, 125V', 1)
p44(540, 'TR duplex w/ black plate', 'TAMPER RESISTANT DUPLEX RECEPTACLE, 20A, 125V W/ BLACK COVER PLATE', 5, 'transaction-bar keynote 1: black plates below counter')
add(541, 'TR GFCI duplex w/ engraved plate', [L(44, 'TEMPER RESISTANT GFCI DUPLEX RECEPTACLE, 20A, 125V', None)], 'judgment', 'none',
    'No marker: the matching legend row prints NAN EA. Keynote 24 (engraved "GFCI PROTECTED") appears 3 times on E-100 (REF, EWC, DW) and those 3 are already carried by lines 550, 542 and 537 -> probable duplicate of 537')
p44(542, 'GFCI duplex w/ engraved plate', 'GFCI DUPLEX RECEPTACLE, 20A, 125V- PROVIDE FACTORY ENGRAVED COVER PLATE ...', 1, 'keynote 24 at EWC')
p44(543, 'Duplex w/ cover plate', 'DUPLEX RECEPTACLE, 20A, 125V W/ COVER PLATE', 2)
add(544, 'GFCI WP duplex w/ metallic cover (roof)', [L(45, 'GFCI WEATHERPROOF DUPLEX RECEPTACLE, 20A 120V W/ METALLIC COVER', 2)], 'counted', 'count-sum', 'E-101 keynote 1 maintenance receptacle at RTUs')
p44(545, 'USB duplex (Legrand R26USBACWCCV6)', 'USB DUPLEX RECETACLE, 20A, 125V', 1, 'keynote 7')
p44(546, 'Quad receptacle 20A (separate row)', 'QUAD RECEPTACLE 20A, 125V', 1, 'first legend row on page 44 (magenta); missing from legends.json')
p44(547, 'Surge protective duplex (Leviton T5380W)', 'DUPLEX RECEPTACLE, SURGE PROTECTIVE (LEVITON T5380W) 20A, 125V', 3)
p44(548, 'USB duplex receptacle', 'USB DUPLEX RECEPTACLE, 20A, 125V', 7)
p44(549, 'TR duplex receptacle', 'TEMPER RESISTANT DUPLEX RECEPTACLE, 20A, 125V', 5)
p44(550, 'TR duplex w/ engraved plate', 'TEMPER RESISTANT DUPLEX RECEPTACLE, 20A, 125V- PROVIDE FACTORY ENGRAVED...', 1, 'keynote 24 at REF')
p44(551, 'Quad w/ black device & plate (booths)', '20A, 125V QUAD RECEPTACLE W/ BLACK DEVICE & COVER PLATES', 2, 'keynote 9 booths')
p44(552, 'USB duplex w/ black device & plate', 'USB DUPLEX RECEPTACLE, 20A, 125V W/ BLACK DEVICE & COVER PLATES', 1)

# ---- switches
add(553, 'Disconnect switch (unrated)', [L(46, 'DISCONNECT SWITCH', 3), L(51, 'DISCONNECT SWITCH', 1), L(55, 'DISCONNECT SWITCH', 2)], 'counted', 'count-sum',
    'E-130 (3, incl. keynote 1 bank logo sign) + E-704 janitor elevation (1) + M-503 mechanical controls detail (2)')
add(554, '3-pole disconnect switch', [L(55, '3-POLE DISCONNECT SWITCH', 1)], 'counted', 'count-sum', 'from the mechanical sheet M-503')
p44(555, 'Single switch 120/277V toggle', 'SINGLE SWITCH, 120/277V, TOOGLE TYPE', 6)
p44(556, 'Motor rated single switch', 'MOTOR RATED SINGLE SWITCH, 120/277V, TOOGLE TYPE', 2)
p44(557, 'Weatherproof single switch', 'WEATHERPROOF SINGLE SWITCH, 120/277V, TOOGLE TYPE', 1, 'keynote 6 irrigation control disconnecting means')
p44(558, '20/2 NF disconnect switch', '20/2 NF DISCONNECT SWITCH', 1, 'plan text reads 30/2 NF in keynote 3 (2kW water heater) and "30/NF 3R" on the plan; estimator carried the legend name 20/2')
add(559, 'NEMA 3R fusible disconnect (RTU)', [L(45, 'DISCONNECT SWITCH, PROVIDE NEMA 3R FUSIBLE DISCONNECT SWITCH', 3)], 'counted', 'count-sum', 'E-101 keynote 2; plan ratings 30/25 3R (1) and 100/90 3R (2)')
def p46(n, short, item, q, note=''):
    add(n, short, [L(46, item, q)], 'counted', 'count-sum', note)
p46(560, 'Switch bank', 'SWITCH BANK FOR SWITCHES', 1, 'keynote 11, switch bank detail 3/E-130')
p46(561, 'LV dimming override switch w/ plate', 'LOW VOLTAGE DIMMING OVERRIDE SWITCH W/ COVER PLATE', 3)
p46(562, 'Open/close gang switch (drive-thru)', 'OPEN/CLOSE GANG SWITCH W/ (1) COVER PLATE FOR BOTH', 2, 'keynote 3')
p46(563, 'Dimmer switch 20A', 'DIMMER SWITCH, 20A, 120/277V', 3)
p46(564, 'LV dimmer switch', 'LOW VOLTAGE DIMMER SWITCH', 2)
p46(565, 'Single switch 20A 120/277V', 'SINGLE SWITCH 20A, 120/277V', 2)
p46(566, 'LV 2-hour manual override switch', 'LOW VOLTAGE 2-HOUR MANUAL OVERRIDE SWITCH', 1)
p46(567, 'LV 2-hour override dimmer switch', 'LOW VOLTAGE 2-HOUR MANUAL OVERRIDE DIMMER SWITCH', 1)
add(568, 'MechoShade control switch', [L(50, 'MECHOSHADES CONTROL SWITCH', 4)], 'counted', 'count-sum', 'E-703 elevations; E-100 keynote 4: IOT furnishes, EC installs')
p44(569, 'Volume control switch (by others, install)', 'VOLUMN CONTROL SWITCH BY OTHERS, GC TO INSTALL ONLY', 1)
add(570, 'Mood Media switch', [L(50, 'MOOD MEDIA SWITCH', 1)], 'counted', 'count-sum', 'E-703')

# ---- outlets, boxes, sensors
add(571, 'Combination data outlet', [L(44, 'COMBINATION DATA OUTLET', 14), L(50, 'COMBINATION DATA OUTLET', 1)], 'counted', 'count-sum', 'E-100 plan + E-703 elevation')
p44(572, 'Combo data outlet w/ black plate', 'COMBINATION DATA OUTLET W/ BLACK COVER PLATE', 1)
p44(573, 'Combo data outlet w/ black device & plate', 'COMBINATION DATA OUTLET W/ BLACK DEVICE & COVER PLATE', 1)
add(574, 'Junction box (building)', [L(44, 'JUNCTION BOX', 9), L(46, 'JUNCTION BOX', 1)], 'counted', 'count-sum', 'site boxes are line 503; C-4.0 "JUNCTION BOX" is a storm structure (not electrical)')
p44(575, 'Junction box w/ 2in cut-in box', 'JUNCTION BOX W/ 2"W CUTIN BOX', 2, 'keynote 1 door operator')
p44(576, '4in square junction box (night depository)', '4" SQUARE JUNCTION BOX', 1, 'keynote 5')
p44(577, 'Double gang deep junction box', 'JUNCTION BOX W/ DOUBLE GANG, DEEP JBOX', 1, 'keynote 12')
p46(578, 'Weatherproof junction box', 'WEATHER PROOF JUNCTION BOX', 6, 'keynote 12 (E-130) open/close sign')
p44(579, 'Motion sensor (assumed)', 'MOTION SENSOR, ASSUMED', 6, 'plan symbol "MS"; estimator labelled the type an assumption')
p46(580, 'Occupancy sensor', 'OCCUPANCY SENSOR', 10)

# ---- E-702 IT room
def p49(n, short, item, q, note=''):
    add(n, short, [L(49, item, q)], 'counted', 'count-sum', note)
p49(581, 'Security panel', 'SECURITY PANEL', 7, 'E-702 keynote 9 on the backboard')
p49(582, 'Telecommunication box', 'TELECOMMUNICATION BOX', 1)
p49(583, 'Digital alarm communicator transmitter', 'DIGITAL ALARM COMMUNICATOR TRANSMITTER', 1)
p49(584, 'Dimmer panel', 'DIMMER PANEL', 1)
p49(585, 'Panduit two-post rack w/ managers', 'PANDUIT TWO POST CABLE MANAGMENT RACK SYSTEM', 1, 'keynotes 16-17')
p49(586, '18in Homaco ladder rack', '18" STEEL HOMACO LADDER RACK', 1, 'keynote 18; carried as 1 EA (not LF)')
p49(587, 'Ground bus bar 12x2x1/4 Cu', 'GROUND BUS BAR, 12"x2"x1/4" COPPER GROUND BAR W/ STANDOFF INSULATORS...', 1, 'keynote 14')
add(588, 'Panel PP 208/120 3ph 400A MCB', [L(49, 'PANEL PP', 1)], 'counted', 'count-sum', 'specified by E-610 schedule and E-800 riser (400A)')
add(589, 'Panel RP-A 208/120 3ph 225A MLO', [L(49, 'PANEL RP-A', 1)], 'counted', 'count-sum', 'E-610 / E-800 (225A feeder 4-#4/0 in 3"C)')
add(590, 'IOT BMS LCP-SA lighting control panel', [L(46, 'INTERNET OF TEAM BMS LCP-SA LIGHTING CONTROL PANEL', 1)], 'counted', 'count-sum', 'also on page 49 as "LCP" 1 EA - same panel, counted once')
p46(591, 'Photosensor', 'PHOTOSENSOR', 4)

# ---- misc
add(592, 'Outlet box hood (roof)', [L(45, 'OUTLET BOX HOOD', 1)], 'counted', 'count-sum', 'E-101 detail keynote 5')
add(593, 'Wired remote controller', [L(55, 'WIRED REMOTE CONTROLLER', 1)], 'counted', 'count-sum', 'mechanical sheet M-503')
p44(594, 'Push button w/ 2in cut-in box', 'PUSH BUTTON W/ 2"W CUTIN BOX', 2, 'keynote 1')
p44(595, 'Push button w/ 2-gang push plate & box', 'PUSH BUTTON W/ GANG DOOR PUSH PLATE & ELECTRIC BOX FOR PUSH PLATE', 2, 'keynote 25')
p44(596, 'Recessed floor box Legrand RFBA4C', 'RECESSED FLOOR BOX LEGRAND WIREMOLD #RFBA4C300G, RFBADP, RFBA24C4EXT,...', 1, 'keynote 13')
p46(597, 'Dimmable power pack', 'DIMMABLE POWER PACK LIGHTING CONTROL DEVICE', 7, 'plan symbol "DP"')
add(598, 'Pitch pocket', [L(45, 'PITCH POCKET', 1)], 'counted', 'count-sum', 'E-101 detail keynote 4')
add(599, '1-gang box', [L(50, '1-GANG BOX', 5)], 'counted', 'count-sum', 'E-703 elevations')
add(600, 'Recessed 3-gang box Arlington TVBS507', [L(50, 'RECESSED ELECTRICAL BOX (ARLINGTON BOXES TVBS507 3-GANG)', 1)], 'counted', 'count-sum', 'E-703')
add(601, '(4) 3/4in IMC (transaction bar power)', [L(44, '(4) 3/4"DIA IMC CONDUIT', 19.6, 'FT')], 'measured', 'conduit-route-lf', 'E-100 keynote 8 under-slab; route LF of the bundle, NOT x4')
add(602, '(4) 2in IMC w/ string (transaction bar data)', [L(44, '(4) 2"DIA IMC W/ STRING CONDUIT', 19.5, 'FT')], 'measured', 'conduit-route-lf', 'E-100 keynote 8; route LF, NOT x4')

missing = [n for n in trade['lines'] if n not in S]
assert not missing, missing

rows, fixtures = [], []
cnt = {'within1': 0, 'within5': 0}
for n in trade['lines']:
    x = lines[n]; s = S[n]
    est = x['quantity']; unit = x['unit']
    vals = [v for v in s['srcs']]
    srcstr = ' + '.join(f"p{v['page']} '{v['item']}'" for v in vals) if vals else 'none (allowance)'
    sv = ' + '.join(f"{'NAN' if v['qty'] is None else v['qty']} {v['unit']}" for v in vals)
    rec = None
    if s['cls'] == 'allowance':
        rec = 1.0
        sv = 'title block 1,900 SF (E-010..E-800); estimator basis 2,000 SF'
        formula = '1 LS; basis area = ceil(1900/500)*500 = 2000 SF'
    elif s['formula'] == 'none':
        formula = 'no reproducible source'
    else:
        if any(v['qty'] is None for v in vals):
            raise SystemExit(f'NaN in reproducible line {n}')
        rec = round(sum(v['qty'] for v in vals), 2)
        formula = {'count-sum': 'qty = sum of legend counts (EA)',
                   'conduit-route-lf': 'LF = sum of measured route lengths (conduit count stays in the description)',
                   'linear-fixture-lf': 'LF = measured linear fixture length'}[s['formula']]
    delta = None if rec is None else round((rec - est) / est * 100, 2)
    if delta is not None and s['cls'] != 'allowance':
        if abs(delta) <= 1.0 + 1e-9: cnt['within1'] += 1
        if abs(delta) <= 5.0 + 1e-9: cnt['within5'] += 1
    rows.append({'lineNo': n, 'description': s['short'], 'unit': unit, 'estimatorQty': est, 'source': srcstr,
                 'sourceValues': sv, 'formula': formula, 'recomputedQty': '' if rec is None else rec,
                 'deltaPct': '' if delta is None else delta, 'classification': s['cls'], 'notes': s['notes']})
    if s['cls'] in ('allowance', 'judgment'):
        continue
    if s['formula'] == 'count-sum':
        inputs = {'counts': [{'page': v['page'], 'legendItem': v['item'], 'value': v['qty'], 'unit': 'EA'} for v in vals]}
        fx_formula = 'count = Σ legend counts across markup pages (each physical device counted once)'
        tol = 0
    else:
        key = 'routeLengths' if s['formula'] == 'conduit-route-lf' else 'lengths'
        inputs = {key: [{'page': v['page'], 'legendItem': v['item'], 'value': v['qty'], 'unit': 'LF'} for v in vals]}
        if s['formula'] == 'conduit-route-lf':
            import re
            m = re.match(r'\((\d+)\)', x['description'])
            inputs['conduitsInRoute'] = {'value': int(m.group(1)) if m else 1, 'unit': 'EA', 'use': 'description only; LF is NOT multiplied'}
            fx_formula = 'LF = Σ route lengths (bundle LF; conduits-in-route kept as a label)'
        else:
            fx_formula = 'LF = Σ measured linear fixture runs'
        tol = 1.0
    fixtures.append({'name': f'26-electrical line {n}: {s["short"]}', 'formula': fx_formula, 'inputs': inputs,
                     'expected': {'quantity': est, 'unit': 'LF' if unit == 'LF' else unit}, 'tolerancePct': tol,
                     'source': f'line {n} / markup p' + ', p'.join(str(v['page']) for v in vals)})

# Allowance fixture (convention test)
fixtures.append({'name': '26-electrical line 510: wiring/conduit/fittings allowance basis area', 'formula': 'allowance basis SF = ceil(gross SF / 500) × 500; quantity 1 LS',
                 'inputs': {'grossArea': {'value': 1900, 'unit': 'SF', 'read': 'title block "1,900 SF"'}, 'roundTo': {'value': 500, 'unit': 'SF'}},
                 'expected': {'quantity': 1, 'unit': 'LS', 'basisArea': 2000}, 'tolerancePct': 0, 'source': 'line 510 / title block E-010; same basis on lines 403, 445, 622'})

with open(os.path.join(OUT, 'reconciliation.csv'), 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
json.dump(fixtures, open(os.path.join(OUT, 'fixtures.json'), 'w'), indent=1)

from collections import Counter
print('lines', len(rows), 'fixtures', len(fixtures), cnt)
print(Counter(r['classification'] for r in rows))
for r in rows:
    if r['deltaPct'] not in ('', 0, 0.0): print('DELTA', r['lineNo'], r['estimatorQty'], r['recomputedQty'], r['deltaPct'])
# totals for the docs
tot = Counter()
for r in rows:
    tot[(r['classification'], r['unit'])] += 1
print(tot)
ea = sum(r['estimatorQty'] for r in rows if r['unit'] == 'EA')
lf = sum(r['estimatorQty'] for r in rows if r['unit'] == 'LF')
print('EA total', ea, 'LF total', round(lf, 2))
cond = [r for r in rows if r['lineNo'] in (505, 506, 507, 508, 601, 602)]
import re
lf_route = sum(r['estimatorQty'] for r in cond)
lf_conduit = sum(r['estimatorQty'] * (int(re.match(r'\((\d+)\)', lines[r['lineNo']]['description']).group(1)) if re.match(r'\((\d+)\)', lines[r['lineNo']]['description']) else 1) for r in cond)
print('conduit route LF', round(lf_route, 2), 'conduit LF if multiplied', round(lf_conduit, 2), 'ratio', round(lf_conduit / lf_route, 3))
for r in cond:
    m = re.match(r'\((\d+)\)', lines[r['lineNo']]['description']); k = int(m.group(1)) if m else 1
    print(r['lineNo'], r['estimatorQty'], 'x', k, '=', round(r['estimatorQty'] * k, 2))
lum_ea = sum(r['estimatorQty'] for r in rows if 511 <= r['lineNo'] <= 533 and r['unit'] == 'EA')
lum_lf = sum(r['estimatorQty'] for r in rows if 511 <= r['lineNo'] <= 533 and r['unit'] == 'LF')
print('interior+site luminaires EA', lum_ea, 'linear LF', round(lum_lf, 2))
rec_ea = sum(r['estimatorQty'] for r in rows if 534 <= r['lineNo'] <= 552)
print('receptacles EA', rec_ea)
sw = sum(r['estimatorQty'] for r in rows if 553 <= r['lineNo'] <= 570)
print('switches EA', sw)
