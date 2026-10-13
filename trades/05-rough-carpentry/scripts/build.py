import json, math, csv
from fractions import Fraction as Fr
def ft(f,i=0): return f+i/12
def ceil5(x): return math.ceil(round(x,6)/5)*5
L={l['lineNo']:l for l in json.load(open('/home/user/takeoffspeed-reference-data/reference/estimate/lines.json'))}
rows=[]
def add(n,short,src,vals,formula,rq,cls,notes):
    est=L[n]['quantity']; u=L[n]['unit']
    d=round((rq-est)/est*100,3) if rq is not None else ''
    rows.append(dict(lineNo=n,description=short,unit=u,estimatorQty=est,source=src,sourceValues=vals,formula=formula,recomputedQty=round(rq,4) if rq is not None else '',deltaPct=d,classification=cls,notes=notes))
    return rq
# ---- 81 booth wall
r81=15.9*3.0
add(81,'1/2" plywood sheathing at booth wall','markup p29 (A-706) legend WALL 706 (cyan, plan 1: the two booth walls)','WALL 706 15.9 FT; height factor 3.0 ft (not printed anywhere)','SF = LF x 3.0',r81,'derived (unsourced height)','Exact numerically (15.9 x 3 = 47.7) but no drawing gives 3\'-0"; A-706 det. 9 / A-620 series E show 1/2" plywood substrate behind PL-1 on both faces of the 9\'-0" booth walls (15.9 x 9 x 2 = 286.2 SF) so 47.7 SF looks like a short take or a partial scope. dwg ref "S111-S131" names sheets that do not exist in this set.')
# ---- 82 exterior 1/2"
ext=[('A-120 EXT 8" STUD WALL @ 12\'9"H',89.7,ft(12,9),1),('A-120 EXT 6" STUD WALL @ 12\'3"H SHTNG 10\'3"H',9.2,ft(10,3),1),('A-120 PARAPET WALL @ 7\'2"H A310',5.9,ft(7,2),1),('A-120 EXT 8" STUD WALL @ 15\'9"H',41.5,ft(15,9),1),('A-120 EXT 8" STUD WALL @ 4\'H',13.0,4.0,1),('A-120 EXT 8" STUD WALL @ 15\'9"H NO GWB',8.7,ft(15,9),1),('A-120 6" & 3-5/8" METAL STUD @ 18\'8"H, BS 1/2" SHTNG ONLY',8.4,ft(18,8),2),('A-140 PARAPET WALL @ 1\'7"H',46.0,ft(1,7),1),('A-140 PARAPET WALL @ 2\'7"H',38.0,ft(2,7),1),('A-140 PARAPET WALL @ 4\'7"H',96.6,ft(4,7),1)]
r82=sum(a*h*f for _,a,h,f in ext)
for nme,a,h,f in ext: print(f'  {nme:60s} {a:6.1f} x {h:7.4f} x {f} = {a*h*f:9.3f}')
print('82 sum',r82)
add(82,'1/2" plywood sheathing at exterior wall','markups p4 (A-120) exterior wall rows + p7 (A-140) parapet rows','89.7x12\'9" + 9.2x10\'3" (SHTNG) + 5.9x7\'2" + 41.5x15\'9" + 13.0x4\'0" + 8.7x15\'9" + 8.4x18\'8"x2 faces + 46.0x1\'7" + 38.0x2\'7" + 96.6x4\'7"','SF = sum(LF x sheathing height x faces); faces = 1 (exterior face), 2 for the "BS 1/2" SHTNG ONLY" wing walls; no opening deduction',r82,'derived (measured LF x height)','Residual -6.8 SF is within the rounding of ten 0.1-ft legend readings (+/-0.05 LF x height ~ +/-0.6 SF per row). Excludes the high-low roof step wall (8/A450, 45.3 LF x 2\'-0" = 90.6 SF) although det. 8 shows 1/2" sheathing on it.')
# ---- 83 5/8" ext
r83=52.1+8.7*ft(12,8.25)
add(83,'5/8" plywood sheathing at exterior wall','markup p11 (A-200) legend 5/8" PLYWOOD SHEATHING; A-311 sec. 1 measured dim 12\'-8 1/4" + highlighted "5/8" EXTERIOR SHEATHING"; A-120 NO GWB row','52.1 SF + 8.7 LF x 12\'-8 1/4"','SF = legend area + LF x storefront-zone height (reconstruction)',r83,'derived (low-confidence reconstruction)','UNRESOLVED. Only 52.1 SF is directly labelled 5/8". Other candidates: half rowlock 61.4 LF x 2\'-8" sill knee wall = 163.73 (+0.45%); 52.1 + ACM1/ACM2 108.7 = 160.8 (-1.34%). 162.9919 has 4 decimals, so it is a product of unrounded PlanSwift values; none of the chains is confirmed by the drawings.')
# ---- 84 roof
add(84,'5/8" plywood sheathing at roof (canopy roofs, RT2)','markup p7 (A-140) legend RT2 ROOFING (very light cyan)','RT2 ROOFING 285.4 SF; RT2 roof type: membrane / tapered polyiso / 5/8" PLYWOOD','SF = RT2 roof area (flat, slope factor 1.0)',285.4,'measured','Estimator typed 285 (dropped the 0.4). RT1 main roof is on steel deck and gets no plywood.')
# ---- 85 canopy ceiling
r85=358.7+138.5*1.5
add(85,'5/8" plywood sheathing at canopy ceiling','markup p5 (A-130) ACM-3 canopy soffit + p7 (A-140) CANOPY EDGE 7/A430','358.7 SF + 138.5 LF x 1\'-6" (1\'-0" fascia + 6" bottom return, A-430 det. 10)','SF = soffit area + edge LF x edge wrap',r85,'derived (low-confidence reconstruction)','A-430 det. 10/7: "PLYWOOD DECK ON METAL FRAMING INFILL" under the ACM-3 soffit; "EXTERIOR SHEATHING" at the fascia. The 1\'-6" wrap is my reading, not printed as a sheathing dimension; GPT-6 second opinion agreed it is the best fit but unverified.')
# ---- 86 booth ceiling
r86=76.2*2
add(86,'3/4" plywood sheathing at booth ceiling','markup p29 (A-706) legend PT5 FINISH @ BOOTH ROOF / 6"THK. 16GA STUD ... W/ 3/4"THK. PL... (both 76.2 SF, booth roof framing plan 2)','76.2 SF x 2 layers (top "3/4" PLYWOOD FRAMING. PAINTED PT-5" + underside plywood substrate for the PL-1 laminate ceiling)','SF = booth roof area x 2',r86,'derived (measured area x layers)','Estimator 152 = 152.4 truncated (or 2 x 76). Underside could also be taken from the PL-1 ceiling area 64.2 SF (76.2 + 64.2 = 140.4, -7.6%); the estimator used 2 x roof area.')
# ---- 87 IT backboard
add(87,'3/4" FR plywood backboard at IT room','markup p49 (E-702) legend 3/4"THK. FIRE RATED PLYWOOD BACKBOARD (purple)','215.3 SF (E-702 keyed note: 8\' x length as required x 3/4" fire-rated plywood on all NER room walls)','SF = sum(elevation width x 8\'-0")',215.3,'measured','Estimate 215.33 = unrounded PlanSwift value (26.92 LF x 8\'). Cross-check: A-110 legend PLYWOOD @ 8\'H 32.5 FT x 8 = 260 SF (+20.8%) traces the room perimeter on plan; the estimator used the elevation net.')
# ---- 88 trim
add(88,'Interior trim at opening, ASSUMED','none (A-600 door schedule cited; no trim detail exists)','910 LF typed; opening perimeters from A-600/A-610 give 2 sides x interior doors (238.7) + exterior doors interior side (63) + windows 4 sides (268.6) = 570.3 LF','allowance',None,'allowance/judgment','The description says ASSUMED. Doors are hollow-metal frames and storefront is aluminium, so no casing detail exists to reproduce 910 LF. Coincidence noted, not claimed: WB-1 wall base 404.7 LF x 2.25 = 910.6.')
# ---- 89 1x4 FRT
blk=[('p24 A-701 (7) 1x4 FIRE RETARDANT TREATED BLOCKING',7,8.6),('p25 A-702 (2) 1x4 WOOD BLOCKING FRAMING',2,14.6),('p26 A-703 (4) 1x4 WOOD BLOCKING FRAMING',4,9.8),('p30 A-707 (2) 1x4 WOOD BLOCKING FRAMING',2,23.3),('p32 A-705 (2) 1x4 BLOCKING',2,15.7),('p23 A-700 (5) 2x4 WOOD BLOCKING FRAMING',5,1.6),('p32 A-705 (3) 2x4 BLOCKING',3,8.7)]
r89=sum(n*l for _,n,l in blk); r89_1x4=sum(n*l for t,n,l in blk if '1x4' in t)
print('89',r89,'1x4 only',r89_1x4)
add(89,'1x4 FRT blocking','markups p23-p32 (A-700..A-707) every "(n) size BLOCKING" legend row','(7)x8.6 + (2)x14.6 + (4)x9.8 + (2)x23.3 + (2)x15.7 + (5)x1.6 + (3)x8.7','LF = sum(rows n x legend LF)',r89,'derived (measured LF x rows)','The 1x4 rows alone give 206.6 LF (-14.2%); the estimator also folded the two 2x4 rows (8.0 + 26.1 LF) into this 1x4 line. FRT for all of them per A-110 note F and spec 06 10 53 2.3 E (concealed blocking).')
add(90,'2x4 FRT blocking','none','10 LF typed','allowance',None,'allowance/judgment','No legend row is left over (both 2x4 rows are inside line 89). Round 10 LF reads as an allowance, e.g. for A-701 "2x8 WOOD BLOCKING" at the VAT and A-704 tech-wall blocking that carry no legend row.')
add(91,'2x4 treated blocking (A-140)','markup p7 (A-140) legend 8/A450 LAP ROOF 2\', INCL WALL; A-450 det. 8/10 high-low roof','45.3 LF; det. 8 shows two stacked P.T. members on the 3-5/8" step wall: lower 2x within the stud width, upper 2x over insulation','LF = run LF x 1 row; estimator ceil to whole LF (46)',45.3,'measured (+ estimator rounding)','ceil(45.3) = 46 reproduces it. Alternative source with a matching size but not length: CURB 1/A450 39.9 LF (det. 1 "2 X 4 P.T. WOOD NAILER").')
add(92,'2x6 treated blocking (A-140)','same run as line 91 (8/A450, 45.3 LF); A-450 det. 10 "2x P.T. WOOD BLOCKING" ~6" wide','45.3 LF','LF = run LF; ceil to whole LF (46)',45.3,'measured (+ estimator rounding)','A-140 note 4 also requires P.T. 2x6 blocking at insulation around every roof penetration (curbs 39.9 LF, hatch, vents) and no separate line carries it - a likely omission.')
add(93,'2x16 treated blocking (A-140)','markup p7 (A-140) legend COPING 3/A430 (wing-wall coping)','13.9 LF; A-430 det. 3: P.T. WOOD BLOCKING across the 1\'-8" wing wall under a 2\'-0" coping','LF = coping LF; estimator rounds up to 5 LF (15)',13.9,'measured (+ estimator rounding)','ceil5(13.9) = 15. 2x16 is the nearest nominal to the ~1\'-8" wide wall top.')
add(94,'2x10 treated blocking (A-140)','markup p7 (A-140) legend COPING 6/A450','148.1 LF; A-450 det. 6 "2X P.T. WOOD NAILER" across the 8" stud + sheathing + insulation wall (~10" drawn)','LF = coping LF',148.1,'measured','Estimate 148 = 148.1 rounded down.')
add(95,'2x14 treated blocking (A-140)','markup p7 (A-140) legend COPING 9/A450 (high parapet with EIFS)','38.5 LF; A-450 det. 9 upper 2x nailer ~14" wide (wall + EIFS)','LF = coping LF; rounded up to 5 LF (40)',38.5,'measured (+ estimator rounding)','ceil5(38.5) = 40.')
add(96,'1x6 treated blocking (A-140)','same run as line 95 (COPING 9/A450 38.5 LF)','38.5 LF; A-450 det. 9 "BRAKE METAL OVER 1X BLOCKING" (lower member ~5-6" wide)','LF = coping LF; rounded up to 5 LF (40)',38.5,'measured (+ estimator rounding)','ceil5(38.5) = 40.')
add(97,'2x6 blocking (night depository)','markup p12 (A-201) legend 2x6 BLOCKING (purple outline round the night-depository opening, east elevation)','8.8 FT','LF = opening perimeter as traced',8.8,'measured','Estimate 8.78 = unrounded PlanSwift value. Untreated in the description; A-110 note F would make interior blocking FRT and the opening is in an exterior wall.')
r145=4.0*3.75*2
add(145,'1/2" plywood backing (transaction bar knee wall)','markup p23 (A-700) legend 1/2" PLYWOOD @ 3\'9"H','4.0 LF x 3\'-9" x 2 faces (A-700: tile face over 1/4" backer on plywood; "PL-4 OVER 1/2" PLYWOOD BACKING @ INTERIOR SIDE")','SF = LF x H x faces; backing section rounds up to 5 SF',r145,'derived (measured LF x height x faces)','30.0 exactly; ceil5 leaves it at 30.')
b146=[('A-700 (2) 3/4" PLYWOOD @ 1\'4"H',2*3.7*ft(1,4)),('A-700 3/4" PLYWOOD @ 8"H',1.6*ft(0,8)),('A-701 3/4" PLYWOOD @ 7.67H',8.6*7.67),('A-702 3/4" PLYWOOD',46.9),('A-703 3/4" PLYWOOD',8.0)]
raw146=sum(v for _,v in b146); print('146 raw',raw146, [round(v,3) for _,v in b146])
add(146,'3/4" plywood backing (casework)','markups p23 (A-700), p24 (A-701), p25 (A-702), p27 (A-703) 3/4" PLYWOOD rows','(2)x3.7x1\'4" = 9.87 + 1.6x8" = 1.07 + 8.6x7.67 = 65.96 + 46.9 + 8.0 = 131.79 SF','SF = ceil5(sum LF x H x n + sum SF)',ceil5(raw146),'derived (measured, ceil to 5 SF)','Raw sum 131.79 SF is -2.4%; the backing section rounds up to the next 5 SF (same rule gives 30 and 40 on lines 145/147). A-707 "4"H PL2 BASE O/ 3/4" PLYWOOD" (13.6 LF) is excluded - it belongs to millwork line 139.')
add(147,'5/8" plywood backing (tech wall)','markup p28 (A-704) legend 5/8" PLYWOOD BACKING','37.2 SF (tech-wall recess, same polygon as TYPE X GWB and PT6)','SF = ceil5(area)',ceil5(37.2),'measured (ceil to 5 SF)','Raw 37.2 is -7.0%; painting line 297 rounds the same 37.2 to 40.')
with open('/home/user/takeoffspeed-reference-data/trades/05-rough-carpentry/reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
for r in rows: print(r['lineNo'],r['estimatorQty'],r['recomputedQty'],r['deltaPct'],r['classification'])
json.dump(rows,open('/home/user/work/05-rough-carpentry/rows.json','w'),indent=1)
