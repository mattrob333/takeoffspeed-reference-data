import csv, json, io
T='/home/user/takeoffspeed-reference-data/trades/07-thermal-moisture'
# ---------- reconciliation.csv
with open(f'{T}/reconciliation.csv', newline='') as f:
    rd=csv.DictReader(f); cols=rd.fieldnames; rows=list(rd)
R={r['lineNo']:r for r in rows}
r=R['148']
r['source']='markup p4 (A-120) wall runs; A-620 partition base/head details A-B01, A-T01, D-B01, D-T01; note K'
r['sourceValues']='A-series 28.4+34.2+36.7+49.9 = 149.2 LF; D-series 3.7+46.0 = 49.7 LF; low walls 7.7+18.3 = 26.0 LF; exterior runs with interior GWB 89.7+9.2+41.5+13.0 = 153.4 LF'
r['formula']='LF = 4 x A-series LF (A-B01 2 base + A-T01 2 head) + 2 x (D-series + low walls + exterior GWB walls) LF (D-B01 1 base + D-T01 1 head on the one finished face; low walls 2 base, no head)'
r['recomputedQty']='1055.0'; r['deltaPct']='0.142'
r['classification']='derived (inferred convention)'
r['notes']=('Not confirmed: no legend row, and dwg ref "A1.1" is not a sheet in this set. The stated rule follows the A-620 details '
 '(beads = head + base per finished face, no head bead on partial-height walls); exterior walls have no sealant detail and are treated like D. '
 'A second fit, 4 x all interior LF (224.9) + 1 x exterior LF = 1053.0 (-0.05%), is numerically closer but contradicts D-B01 (one bead, gypsum side only) '
 'and puts head beads on the low walls. Applying D-T02 (no sealant) to D3C and no head bead on the 4\'H exterior wall would give 1038.3 (-1.4%). Neither fit is confirmed.')
r=R['149']
r['source']='none (A-600 door schedule cited; no opening-sealant takeoff on A-600 or A-610)'
r['sourceValues']='1330 LF typed; coincidence check: line 88 (910.0 LF, itself "ASSUMED") + one bead around every glazed unit A,B,C,D,E(x2),F,G,H,J,K (419.0625 LF) = 1329.0625'
r['formula']='allowance'; r['recomputedQty']=''; r['deltaPct']=''
r['classification']='allowance/judgment'
r['notes']=('Round 1330 reads as an allowance. The 910 + 419.06 = 1329.06 match (-0.07%) is a coincidence check, not a rule: it depends on an assumed line and counts the interior storefronts J and K. '
 'No door-only or window-only combination of A-600/A-610 perimeters lands within 12 LF of 1330. Doors-only per A-600 note 2 would be 2 faces x (6x17 + 17.33) = 238.7 LF.')
r=R['156']
r['notes']=('Carried from the framing line 311 (2652.875 SF) as the estimator computed it. The legend-based rebuild is 10.52 SF short (-0.40%); '
 'the residual is unexplained and is not display rounding (one row would have to move by 0.8 LF or more, e.g. 89.7 -> 90.52 or 41.5 -> 42.17). '
 'Includes 656 SF of roof parapets above the deck, where the cavity batt is not needed thermally.')
r=R['161']
r['notes']=('76 = round(76.2) from the p29 row "6"THK. 16GA. METAL STUD @ 12" O.C W/ 6"THK. SOUND BATT ..." (76.2 SF). The painting line 302 (PT-5 at booth roof) '
 'carries the same 76.2 SF rounded up to 77 SF; line 312 is a 77 LF stud quantity on the same legend row, a length, not an area.')
r=R['162']
r['sourceValues']='field 1864.3+285.4 = 2149.7; parapet laps 43.3x25/12 + 56.5x1 + 87.8x3.5 = 454.008; high-low 45.3x2 = 90.6; canopy edge 138.5 x 4/12 = 46.167 (detail 10/A430)'
r['formula']='SF = roof field + sum(parapet lap LF x lap height) + high-low LF x 2\' + canopy-edge LF x 4" wrap; leaves a residual the measured rows do not explain'
r['recomputedQty']='2740.475'; r['deltaPct']='-9.935'
r['classification']='derived, not reconciled (residual +302 SF)'
r['notes']=('Field, laps and high-low are measured rows. Detail 10/A430 says "WRAP MEMBRANE 4" MIN. OVER EDGE OF CANOPY" and detail 7/A430 draws the membrane turning about 3-1/2" down the edge, '
 'so the edge adds 46.17 SF; the ACM fascia girth (12"+12"+6", line 183) is the ACM, not the membrane. About 302.3 SF of the estimator\'s 3042.774 is not reproducible from any measured row. '
 'Numerical fits that close the gap are not unique (515 combinations of high-low height, edge girth, curb and hatch flashing land within 0.1%; e.g. adding crickets 262.1 + curb 39.9 x 1 gives 3042.47) and none is drawing-supported.')
with open(f'{T}/reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f, fieldnames=cols, lineterminator='\n'); w.writeheader(); w.writerows(rows)
# ---------- fixtures.json
F=json.load(open(f'{T}/fixtures.json'))
out=[]
for fx in F:
    n=fx['name'][:4]
    if n in ('L149','L162'): continue
    if n=='L148':
        fx['inputs']={
          'groups': {'value': [
             {'name':'A-series partitions (GWB both sides, to structure)','lf':149.2,'beads':4},
             {'name':'D-series partitions (GWB one side)','lf':49.7,'beads':2},
             {'name':'low walls (A3A @ 3\'9", 6" @ 4\'4"), base only','lf':26.0,'beads':2},
             {'name':'exterior stud walls with interior GWB','lf':153.4,'beads':2}],
           'unit':'LF x beads'}}
        fx['formula']='acousticSealantLF'
        fx['source']='line 148 / markup p4 (A-120) wall runs; A-620 details A-B01, A-T01, D-B01, D-T01'
        fx['recomputed']=1055.0
    if n=='L169':
        fx['inputs']['round']={'value':1,'unit':'LF'}
        fx['recomputed']=148
    if n=='L156':
        fx['note']='expected is the framing line 311 value; the legend rows rebuild to 2642.36 (-0.40%), residual unexplained (not display rounding); 0.5% tolerance covers it'
    out.append(fx)
json.dump(out, open(f'{T}/fixtures.json','w'), indent=1, ensure_ascii=False)
print(len(out))
