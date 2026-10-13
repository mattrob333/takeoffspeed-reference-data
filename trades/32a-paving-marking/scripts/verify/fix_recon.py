import csv,io,sys
p=sys.argv[1]
rows=list(csv.reader(open(p,newline='')))
h=rows[0]; ix={k:i for i,k in enumerate(h)}
R={r[0]:r for r in rows[1:]}
def setf(line,field,val): R[line][ix[field]]=val.replace('""','"')
def repl(line,field,old,new):
    old=old.replace('""','"'); new=new.replace('""','"')
    v=R[line][ix[field]]
    assert old in v,(line,field,old)
    R[line][ix[field]]=v.replace(old,new)
# issue 2: pavement section is the geotech report referenced by the C-3.0 Pavement Legend
repl('632','notes','is the estimator\'s assumption: C-3.0 keynote 4 points to C-6.2, which holds no pavement section; the Terracon geotech light-duty section is 2"" SP9.5 + 6"" GAB.',
     'is the estimator\'s assumption. C-3.0 keynote 4 points to C-6.2, which holds no pavement section, but the C-3.0 PAVEMENT LEGEND and General Site Note 9 point to the Terracon geotech report dated 05.04.2026, which is the design section: light duty 2"" SP9.5 + 6"" GAB. The estimator did not follow the legend reference (RFI/clarification).')
repl('633','notes','Assumed section; geotech heavy duty','Assumed section, although the C-3.0 PAVEMENT LEGEND points to the Terracon report for the design section: heavy duty')
# issue 1
repl('634','notes','is the dumpster slab, line 663 (trade 32b), and is missing from legends.json.',
     'shares the same truncated name but is the dumpster slab, line 663 (trade 32b); do not add it here.')
repl('634','notes','Geotech heavy-duty PCC is 6-1/2""; estimate carries 6"".',
     'The C-3.0 PAVEMENT LEGEND points to the Terracon report: PCC heavy duty 6-1/2"" on 4"" GAB (light duty 5"" on 4"" GAB); estimate carries 6"".')
# issue 5
setf('644','notes','One 5\'x18\' access aisle (C-3.0 21/9 area). The traced 97.48 LF is reproduced as measured; how it was cut is not recoverable from the vectors. C-3.0 vectors: the 0.72-pt hatch pen inside the aisle gives 12 diagonal segments totalling 66.06 LF (68.96 LF if the 0.12-pt annotation strokes are included); hatch + two 18\' sides = 102.06 (97.48 is 0.955 of it), hatch + 46\' perimeter = 112.06 (0.870). Neither matches the crosswalk ratio (0.935), so no common short-trace factor is claimed. Text ""4"" WHITE LINES"" is C-6.0 boilerplate; the white stall lines are in line 642.')
# issue 9
setf('674','notes','DISCREPANCY between drawings: C-3.0 itself draws 5 bollards at the enclosure (3 circles on the back wall + 1 at each gate jamb, the other jamb circle being the gate post), while A-190 FLOOR PLAN 4 draws 6 (4 on the back wall at 2\'-4"" / 3\'-7"" / 3\'-9"" / 3\'-0"" / 2\'-0"" + 1 at each gate jamb, leader ""BOLLARD""; the other jamb circles are TE2 gate posts). GPT-6 Astra independently counted 6 on A-190 and 3 back-wall circles on C-3.0. The estimator followed the civil sheet; C-3.0 keynote 11 says ""DUMPSTER ENCLOSURE, REFER TO ARCHITECTURAL PLANS FOR DETAILS"", so 6 is the likely answer pending RFI. A-190 general note: all painted steel pipe bollards receive a bollard cover; the estimate line carries none for this group (material note only).')
# issue 3 and 4
for ln in ('675',):
    setf(ln,'source','line 674 + A-190 section 3 (diameter); depth = estimator assumption')
    setf(ln,'sourceValues','n 5; ""16"" DIA. CONCRETE PIER""; no pier depth on A-190 (pier drawn with break lines); H 3\'-0"" assumed'.replace('""','"'))
    setf(ln,'notes','D carried as 1.33 ft, area 1.39 SF. Exact pi gives 0.7757 (+0.45%). With 6 bollards: 0.926667 CY (+0.154444 per pier). H = 3\'-0"" is an estimator assumption: A-190 section 3 calls out only the 16"" diameter, with no depth (RFI). Civil C-6.0 BOLLARD DETAIL is not used: 24"" dia footing, 4\'-0"" minimum embedment below pavement plus 3"" of concrete below the pipe (4\'-3""), 3\'-0"" minimum exposed, 7\' pipe; at 5 bollards that would be 2.327 CY (4\'-0"") or 2.473 CY (4\'-3""). Keynote 11 sends the enclosure to the architectural plans.'.replace('""','"'))
setf('676','sourceValues','1.39 SF x 3.0 ft (assumed) x 5')
setf('677','sourceValues','1.39 SF x 3.0 ft (assumed) x 5')
# issue 6
setf('714','sourceValues','n 8; "16"" DIA. CONCRETE FILL"; "48"" BELOW GRADE" (top of paving to pipe bottom) + 3"" fill below pipe; 4\'-0"" is the exposed height'.replace('""','"'))
setf('714','notes','H = 4.0 ft is the nominal pipe embedment per ""48"" BELOW GRADE"". The detail adds 3"" of 16"" concrete fill below the pipe bottom (51"" = 4\'-3"" from top of paving); the estimator neither added it nor deducted the concrete paving thickness. At 4\'-3"": 1.39 x 4.25 x 8 / 27 = 1.750370 CY (+6.25%); exact pi at 4\'-3"" = 1.7583. Exact pi at 4.0 gives 1.6548 (+0.45%).'.replace('""','"'))
w=csv.writer(open(p,'w',newline=''),lineterminator='\r\n')
w.writerow(h)
for r in rows[1:]: w.writerow(R[r[0]])
print('ok')
