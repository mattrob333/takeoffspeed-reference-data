import csv, json, math
OUT='/home/user/takeoffspeed-reference-data/trades/32a-paving-marking/'
L={l['lineNo']:l for l in json.load(open('/home/user/takeoffspeed-reference-data/reference/estimate/lines.json'))}
r2=lambda x: round(x+1e-12,2)
pier=lambda D,H,n: r2(math.pi/4*r2(D)**2)*H*n/27
rows=[]
def add(n,desc,src,vals,formula,rec,cls,notes):
    e=L[n]['quantity']; d=(rec-e)/e*100
    rows.append(dict(lineNo=n,description=desc,unit=L[n]['unit'],estimatorQty=e,source=src,sourceValues=vals,formula=formula,recomputedQty=round(rec,6),deltaPct=f'{d:.3f}',classification=cls,notes=notes))
P72='p72 C-3.0 legend'
add(632,'4: STANDARD DUTY ASPHALT PAVEMENT (assumed section)',P72,'"4: STANDARD DUTY ASPHALT PAV..." 2459.2 SQ FT (brown)','SF = measured polygon area (PlanSwift value carried to 2 dp)',2459.2,'measured','Estimate keeps PlanSwift precision 2459.18; legend prints 1 dp. Brown = parking stalls + drive-thru lanes. Section (1-1/2" 9.5 / 3" 19 / 12" Type 2 subbase / geotextile) is the estimator\'s assumption: C-3.0 keynote 4 points to C-6.2, which holds no pavement section; the Terracon geotech light-duty section is 2" SP9.5 + 6" GAB.')
add(633,'3: HEAVY DUTY ASPHALT PAVEMENT (assumed section)',P72,'"3:HEAVY DUTY ASPHALT PAVEME..." 11367.3 SQ FT (cyan)','SF = measured polygon area',11367.3,'measured','Cyan = drive aisles and entrance throat to the curb face. Assumed section; geotech heavy duty = 1-1/4" SP9.5 + 1-3/4" SP19 + 8" GAB. Thickness does not change the SF line.')
add(634,'21: 6" HEAVY DUTY CONCRETE PAVEMENT - FOR PARKING',P72,'"21: HEAVY DUTY CONCRETE PAVE..." 241.8 SQ FT (teal) + "18: HEAVY DUTY CONCRETE PAVE..." 505.8 SQ FT (bright green)','SF = ceil(sum of same-section concrete pavement areas) = ceil(241.8 + 505.8 = 747.6)',math.ceil(241.8+505.8),'measured','Two keynotes with identical text (18 drive-thru equipment slab, 21 ADA stall/aisle) merged into one line and rounded UP to a whole SF. The second "21" row (purple 384.3 SF) is the dumpster slab, line 663 (trade 32b), and is missing from legends.json. Geotech heavy-duty PCC is 6-1/2"; estimate carries 6".')
add(635,'4" CONCRETE SIDEWALK W/ 6x6-W2.9xW2.9 WWF, 3000 PSI',P72,'"5: CONCRETE SIDEWALK -C6.0" 1834.7 SQ FT (green)','SF = ceil(measured area) = ceil(1834.7)',math.ceil(1834.7),'measured','Rounded up to whole SF (1834.7 -> 1835). Thickness, WWF, 3000 PSI, 98% Std Proctor from C-6.0 SIDEWALK DETAIL. Ramps are measured separately (line 637), not inside this area.')
add(636,'1/4" EXPANSION JOINT (sidewalk)','line 635 + C-6.0 SIDEWALK DETAIL note','sidewalk 1835 SF; "EXPANSION JOINTS REQUIRED AT ALL STRUCTURES, MAX. SPACING TO BE 25\'" ; "1/4" EXP. JOINT"','LF = sidewalk SF / joint spacing = 1835 / 25',1835/25,'derived','Transverse joints every 25 ft across a walk of width W: (SF/W/25) joints x W = SF/25, independent of W. Uses the rounded 1835 (unrounded 1834.7 gives 73.388, -0.016%). No joints added at the building (C-6.0 calls 1/2" there) or at curb (15# felt).')
add(637,'6: GDOT STANDARD ADA RAMP WITH DETECTABLE WARNING',P72,'"6: GDOT STANDARD ADA RAMP WI..." 113.3 SQ FT (olive), 2 ramps (keynote 6 tagged twice on C-3.0)','SF = ceil(measured area) = ceil(113.3)',math.ceil(113.3),'measured','Rounded UP (113.3 -> 114, not nearest). Two ramps averaging 56.65 SF. Detail is GDOT standard on C-6.1; the detectable warning surface is not split out.')
add(638,'6"Wx12"H CONCRETE CURB W/ 18"W GUTTER ON 4" GAB',P72,'"1: 24" CURB & GUTTER - C6.0" 993.9 FT (slate blue)','LF = ceil(measured run) = ceil(993.9)',math.ceil(993.9),'measured','Rounded up to whole LF. Profile from C-6.0 CURB & GUTTER DETAIL (6" top, 1\'-0" curb, 1\'-6" gutter, graded aggregate base). One curb type; the C-3.0 "24" ROLL CURB" labels are existing Westgate Dr curb, not measured.')
add(642,'4"W SINGLE SOLID WHITE LINE (SSWL)',P72,'"16: 4" W SINGLE SOLID WHITE LINE (..." 441.3 FT (red/salmon)','LF = measured stripe runs (2 dp)',441.3,'measured','Red runs = stall lines of the 11 stalls plus drive-thru lane separator/curved lane line. C-6.0 ADA PARKING DETAIL: 4" white lines, two coats (coats do not change LF).')
add(643,'WHITE STRIPED PEDESTRIAN CROSSING/CROSSWALK',P72,'"17: WHITE STRIPED PEDESTRIAN CR..." 79.5 FT (bright green)','LF = traced crosswalk linework (two edge lines + bar sides)',79.5,'measured','Not the crossing length: the green trace outlines the 5\'-wide crosswalk (C-3.0 keynote 17). CAD: two 22.5\' edge lines + four 2\'x5\' bars -> 2x22.5 + 8x5 = 85.0 LF; estimator 79.46 = 0.935 x 85 (traced short of the curb lines, or calibration). Paint area would be 4x2x5 + 45 LF x 4" = 55 SF.')
add(644,'4" BLUE 45 DEG HATCH (ADA aisle) / 4" WHITE LINES',P72,'"4" W DA 45 DEGREE PAVEMENT MARKI..." 97.5 FT (yellow)','LF = traced hatch lines + aisle outline',97.5,'measured','One 5\'x18\' access aisle (C-3.0 21/9 area). CAD hatch segments total 58.18 LF; + two 18\' sides = 94.18 (-3.4%); + full 46\' perimeter = 104.18 (+6.9%); 97.48 = 0.936 x 104.18, the same ratio as the crosswalk. Text "4" WHITE LINES" is C-6.0 boilerplate; the white stall lines are in line 642.')
add(645,'3\'x3\' ADA PAINTED PARKING SYMBOL (blue field, 3" white border)',P72,'"ADA PAINTED PARKING SIGN" 1.0 EA (blue circle)','EA = count of accessible stalls (symbol per stall)',1,'counted','C-6.0 ADA PARKING SYMBOL DETAIL: paint 3\'-0" x 3\'-0" blue field with 3" white border in all HC stalls; C-3.0 note 5: 1 HC space, van accessible.')
add(646,'24" WHITE STOP BAR',P72,'"24" WHITE STOP BAR - C6.0" 49.6 FT (purple)','LF = measured bar length across the lane(s)',49.6,'measured','Two bars (C-3.0 keynote 2 tagged twice: Westgate Dr entrance and drive-thru exit by the DO NOT ENTER signs), avg 24.79 LF each, about the 24\' drive width. C-6.0 STOP BAR DETAIL: "CONTINUE BAR TO EDGE OF PAVEMENT".')
add(647,'3\'-8"x9\'-4" ARROW MARKING',P72,'"ARROW MARKING" 2.0 EA (teal circles)','EA = count of arrow symbols (keynote 15, two leaders)',2,'counted','Size from C-6.0 PAVEMENT MARKING DETAIL; the detail note says reduce dimensions 50% for parking lots and drives (1\'-10" x 4\'-8"); the estimator wrote the road size.')
add(648,'ADA PARKING SIGN R7-8 + VAN ACCESSIBLE R7-8P5 ON TUBE IN 8" PIPE',P72,'"ADA PARKING SIGN - C6.0" 1.0 EA (magenta circle)','EA = count (one per accessible stall)',1,'counted','Assembly from C-6.0 ADA SIGN MOUNTING DETAIL and ADA SIGN DETAIL (12"x18" + 12"x6" .080 aluminum, 2"x2"x.188" tube 2\' into 8" STD pipe filled w/ concrete). Footing is line 651 (trade 32b).')
add(649,'12: R1-1 STOP SIGN 30"x30" ON 2" GALV CHANNEL',P72,'"12: R1-1:STOP SIGN" 3.0 EA (olive circles)','EA = count of keynote-12 symbols',3,'counted','C-3.0 tags keynote 12 three times (two by the 13 tags). Mounting per C-6.0 TRAFFIC SIGN MOUNTING DETAIL; footing line 654 (32b).')
add(650,'13: DO NOT ENTER SIGN',P72,'"13: RF-1: DO NOT ENTER SIGN" 2.0 EA (slate blue circles)','EA = count of keynote-13 symbols',2,'counted','Keynote text says R5-1; "RF-1" in the legend/estimate is a typo. Two of the three STOP tags sit beside the two DO NOT ENTER tags; each sign is counted and footed on its own (line 654: 3 + 2 = 5 footings).')
add(659,'BIKE RACK 1.25" DIA SCH 40 PIPE',P72,'"19:BIKE RACK" 2.0 EA (cyan circles)','EA = count',2,'counted','Keynote 19 "BIKE RACK(S), SEE SHEET C-6.0 FOR DETAILS" but C-6.0 has no bike rack detail: pipe size is the estimator\'s assumption.')
add(660,'1\'-0" DIA x1\'-0"H BIKE RACK FOOTING (4)','line 659 x 2 legs','2 racks x 2 footings; D 1.0 ft; H 1.0 ft (assumed)','CY = round(pi/4 x round(D,2)^2, 2) x H x n / 27 = 0.79 x 1.0 x 4 / 27',pier(1.0,1.0,4),'derived','Footings per rack (2, inverted-U) and size are estimator assumptions (no detail). Circle area carried as 0.79 SF, same convention as the sign and light-pole footings in trade 32b.')
add(661,'BIKE RACK: EXCAVATION REQUIRED','= line 660','0.79 SF x 1.0 ft x 4','excavation CY = pier concrete CY',pier(1.0,1.0,4),'derived','Pier poured against earth, full depth buried.')
add(662,'BIKE RACK: HAULOFF','= line 661','0.79 SF x 1.0 ft x 4','haul CY = excavation CY (no backfill, bank CY)',pier(1.0,1.0,4),'derived','No swell.')
add(674,'6" DIA x5\'-0"H CONCRETE FILLED GALV STEEL BOLLARD (YELLOW)','p72 C-3.0 legend + A-190 wall section 3 / keynote TE1','"DUMPSTER BOLLARDS" 5.0 EA (brown circles); A-190: 6" dia, 5\'-0" above slab','EA = count',5,'counted','DISCREPANCY: A-190 FLOOR PLAN 4 shows 6 bollards (4 along the back wall + 1 at each gate jamb, leader "BOLLARD"; the other jamb circles are TE2 gate posts). GPT-6 independently counted 6. Estimate takes 5 from the C-3.0 markup.')
add(675,'16" DIA x3\'-0"H BOLLARD FOOTING (5) - dumpster','line 674 + A-190 section 3','n 5; "16" DIA. CONCRETE PIER"; depth 3\'-0"','CY = round(pi/4 x 1.33^2, 2) x 3.0 x 5 / 27 = 1.39 x 15 / 27',pier(16/12,3.0,5),'derived','D carried as 1.33 ft, area 1.39 SF. Exact pi gives 0.7757 (+0.45%). With 6 bollards: 0.9267 CY. Civil C-6.0 BOLLARD DETAIL (24" dia, 3\' min) is not used: architectural detail governs the enclosure.')
add(676,'DUMPSTER BOLLARDS: EXCAVATION REQUIRED','= line 675','1.39 SF x 3.0 ft x 5','excavation CY = pier concrete CY',pier(16/12,3.0,5),'derived','Full pier depth excavated; slab thickness not deducted.')
add(677,'DUMPSTER BOLLARDS: HAULOFF','= line 676','1.39 SF x 3.0 ft x 5','haul CY = excavation CY',pier(16/12,3.0,5),'derived','No backfill.')
add(713,'6" DIA STEEL BOLLARD & WRAP PER FIFTH THIRD STANDARD','p89 A-401 legend','"6" DIA STEEL BOLLARD & WRAP PER FIFTH THIRD STANDARD" 8.0 EA (magenta circles)','EA = count',8,'counted','A-401 ENLARGED drive-thru island plan shows 8 circles. Covers 24" and 48" high (note); estimate does not split heights.')
add(714,'16" DIA x4\'-0"H BOLLARD FOOTING (8) - drive thru','line 713 + A-401 TYPICAL BOLLARD 8','n 8; "16" DIA. CONCRETE FILL", "48" BELOW GRADE" / 4\'-0"','CY = 1.39 x 4.0 x 8 / 27',pier(16/12,4.0,8),'derived','Exact pi gives 1.6548 (+0.45%).')
add(715,'DRIVE THRU BOLLARDS: EXCAVATION REQUIRED','= line 714','1.39 SF x 4.0 ft x 8','excavation CY = pier concrete CY',pier(16/12,4.0,8),'derived','')
add(716,'DRIVE THRU BOLLARDS: HAULOFF','= line 715','1.39 SF x 4.0 ft x 8','haul CY = excavation CY',pier(16/12,4.0,8),'derived','')
assert len(rows)==28
with open(OUT+'reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
for r in rows: print(r['lineNo'],r['unit'],r['estimatorQty'],r['recomputedQty'],r['deltaPct'],r['classification'])
print('within1',sum(abs(float(r['deltaPct']))<=1 for r in rows),'within5',sum(abs(float(r['deltaPct']))<=5 for r in rows))
# fixtures
V=lambda v,u:{'value':v,'unit':u}
fx=[]
def F(n,name,formula,inputs,q,tol,src):
    fx.append({'name':f'32a line {n}: {name}','formula':formula,'inputs':inputs,'expected':{'quantity':q,'unit':L[n]['unit']},'tolerancePct':tol,'source':src})
F(632,'standard duty asphalt SF','SF = sum(areas)',{'areas':[V(2459.18,'SF')]},2459.18,0.01,'632 / p72 brown 2459.2 SQ FT')
F(633,'heavy duty asphalt SF','SF = sum(areas)',{'areas':[V(11367.3,'SF')]},11367.3,0.01,'633 / p72 cyan 11367.3 SQ FT')
F(634,'heavy duty concrete pavement SF (keynotes 21 + 18 merged)','SF = ceil(sum(areas))',{'areas':[V(241.8,'SF'),V(505.8,'SF')],'rounding':'ceil to whole SF'},748,0.01,'634 / p72 teal 241.8 + bright green 505.8')
F(635,'concrete sidewalk SF','SF = ceil(area)',{'areas':[V(1834.7,'SF')],'rounding':'ceil to whole SF'},1835,0.01,'635 / p72 green 1834.7')
F(636,'sidewalk 1/4" expansion joint LF','LF = sidewalkSF / expansionSpacing',{'sidewalkSF':V(1835,'SF'),'expansionSpacing':V(25,'ft')},73.4,0.1,'636 / C-6.0 sidewalk detail 25\' max')
F(637,'GDOT ADA ramp SF','SF = ceil(sum(rampAreas))',{'rampAreas':[V(113.3,'SF')],'ramps':V(2,'EA'),'rounding':'ceil to whole SF'},114,0.01,'637 / p72 olive 113.3')
F(638,'24" curb & gutter LF','LF = ceil(sum(runs))',{'runs':[V(993.9,'LF')],'rounding':'ceil to whole LF'},994,0.01,'638 / p72 slate blue 993.9 FT')
F(642,'4" SSWL LF','LF = sum(runs)',{'runs':[V(441.31,'LF')],'width':V(4,'in'),'color':'WHITE'},441.31,0.05,'642 / p72 red 441.3 FT')
F(643,'striped crosswalk traced LF','LF = traced linework (as measured)',{'runs':[V(79.46,'LF')],'crossingLength':V(22.5,'ft'),'walkWidth':V(5,'ft'),'bars':V(4,'EA'),'barWidth':V(2,'ft')},79.46,0.1,'643 / p72 bright green 79.5 FT')
F(644,'ADA aisle 45-degree hatch traced LF','LF = traced linework (as measured)',{'runs':[V(97.48,'LF')],'aisle':{'W':V(5,'ft'),'L':V(18,'ft')},'width':V(4,'in'),'color':'BLUE'},97.48,0.1,'644 / p72 yellow 97.5 FT')
F(645,'ADA painted symbol EA','EA = accessible stalls',{'accessibleStalls':V(1,'EA'),'size':'3\'-0" x 3\'-0"'},1,0,'645 / p72 blue circle 1 EA')
F(646,'24" stop bar LF','LF = sum(runs)',{'runs':[V(49.58,'LF')],'width':V(24,'in'),'bars':V(2,'EA')},49.58,0.05,'646 / p72 purple 49.6 FT')
F(647,'arrow marking EA','EA = count',{'count':V(2,'EA'),'size':'3\'-8" x 9\'-4"'},2,0,'647 / p72 teal circles 2 EA')
F(648,'ADA parking sign assembly EA','EA = accessible stalls',{'count':V(1,'EA'),'signCode':'R7-8 + R7-8P5'},1,0,'648 / p72 magenta circle 1 EA')
F(649,'STOP sign EA','EA = count',{'count':V(3,'EA'),'signCode':'R1-1','panel':'30" x 30"'},3,0,'649 / p72 olive circles 3 EA')
F(650,'DO NOT ENTER sign EA','EA = count',{'count':V(2,'EA'),'signCode':'R5-1'},2,0,'650 / p72 slate blue circles 2 EA')
F(659,'bike rack EA','EA = count',{'count':V(2,'EA')},2,0,'659 / p72 cyan circles 2 EA')
for n,lab in [(660,'bike rack footing CY'),(661,'bike rack excavation CY'),(662,'bike rack haul-off CY')]:
    F(n,lab,'CY = round(pi/4*round(D,2)^2,2) * H * racks * footingsPerRack / 27',{'racks':V(2,'EA'),'footingsPerRack':V(2,'EA'),'diameter':V(1.0,'ft'),'depth':V(1.0,'ft'),'circleAreaRounding':'2 dp'},0.117037,0.01,f'{n} / p72 19:BIKE RACK 2 EA')
F(674,'dumpster bollard EA','EA = count',{'count':V(5,'EA')},5,0,'674 / p72 DUMPSTER BOLLARDS 5 EA (A-190 plan shows 6)')
for n,lab in [(675,'dumpster bollard footing CY'),(676,'dumpster bollard excavation CY'),(677,'dumpster bollard haul-off CY')]:
    F(n,lab,'CY = round(pi/4*round(D,2)^2,2) * H * n / 27',{'count':V(5,'EA'),'diameter':V(16,'in'),'depth':V(3.0,'ft'),'circleAreaRounding':'2 dp'},0.772222,0.01,f'{n} / A-190 section 3 + p72')
F(713,'drive-thru bollard EA','EA = count',{'count':V(8,'EA')},8,0,'713 / p89 A-401 legend 8 EA')
for n,lab in [(714,'drive-thru bollard footing CY'),(715,'drive-thru bollard excavation CY'),(716,'drive-thru bollard haul-off CY')]:
    F(n,lab,'CY = round(pi/4*round(D,2)^2,2) * H * n / 27',{'count':V(8,'EA'),'diameter':V(16,'in'),'depth':V(4.0,'ft'),'circleAreaRounding':'2 dp'},1.647407,0.01,f'{n} / A-401 detail 8 + p89')
json.dump(fx,open(OUT+'fixtures.json','w'),indent=1)
print('fixtures',len(fx))
