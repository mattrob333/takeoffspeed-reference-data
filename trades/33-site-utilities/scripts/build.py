import json, csv, math
OUT='/home/user/takeoffspeed-reference-data/trades/33-site-utilities/'
L={l['lineNo']:l for l in json.load(open('/home/user/takeoffspeed-reference-data/reference/estimate/lines.json'))}
r2=lambda x: round(x,6)
st18=[17.69,45.97,92.25,85.26,70.17,21.08]; st15=[25.11]; san=[49.92,92.03,14.14,90.70,14.14,23.03,12.00]
S18=sum(st18); S15=sum(st15); SS=sum(san)
Ldr = S18+S15+SS+168.18
Lr = round(Ldr)
exc = Lr*3*5/27
haul = 42.0
bf = exc-haul
pipevol = sum(Lx*math.pi/4*(d/12)**2 for Lx,d in [(S18,18),(S15,15),(SS,6),(168.18,8)])
rows=[]
def add(n,desc,source,sv,formula,rq,cls,notes):
    e=L[n]['quantity']; d= None if rq is None else (rq-e)/e*100
    rows.append(dict(lineNo=n,description=desc,unit=L[n]['unit'],estimatorQty=r2(e),source=source,sourceValues=sv,formula=formula,
      recomputedQty='' if rq is None else r2(rq),deltaPct='' if d is None else (round(d,3)+0.0 if abs(d)>=0.0005 else 0.0),classification=cls,notes=notes))
add(721,'15" DIA storm pipe line','C-4.0 STORM PIPES table (p74 LENGTH column highlighted)','B1-B2 15" HDPE 25.11','LF = sum(LENGTH) where SIZE = 15"',S15,'specified','One row. No PlanSwift legend row for storm pipe: the length is the engineer\'s table value (C-4.1 profile rounds it to 25 LF).')
add(722,'18" DIA storm pipe line','C-4.0 STORM PIPES table (p74 LENGTH column highlighted)','A1-A2 17.69 + A2-A2.1 45.97 + A2-A3 92.25 + A2.1-A2.2 85.26 + A3-A4 70.17 + C1-C2 21.08','LF = sum(LENGTH) where SIZE = 18"',S18,'specified','Six rows, all HDPE @ 0.50%. Table lengths are structure-to-structure station differences (centre to centre); no fitting or laying allowance.')
add(723,'6" sanitary sewer pipe line','C-5.0 SANITARY PIPES table; p77 legend 6" SANITARY PIPE LINE 295.8 FT','S1-S2 49.92 + S2-S3 92.03 + S3-S4 14.14 + S4-S5 90.70 + S5-S6 14.14 + S6-S7 23.03 + S7-S8 12.00','LF = sum(LENGTH) for the 6" PVC rows',SS,'specified','Table total 295.96 = station of S8-SSBC (2+95.96). The p77 PlanSwift polyline reads 295.8 (-0.05%); the estimator typed the table total.')
add(724,'1: underground gas service line','p77 C-5.0 legend "1: UNDERGROUND GAS SERVICE LINE - COORDI..."','156.4 FT','LF = legend LF',156.4,'measured','UNRESOLVED: estimate carries 152; the 156.4 polyline is +2.89% over it (deltaPct basis here and in README: (recomputed - estimate)/estimate; the same 4.4 LF gap is 2.81% of the legend). 152 appears on no sheet. Most likely re-measured or trimmed by hand (e.g. to the meter or the property line). Utility-coordinated service; size not shown on C-5.0.')
add(725,'8" HDPE header pipe for roof drain','p74 C-4.0 legend "8" HDPE HEADER PIPE FOR ROOF DRAIN"','168.2 FT (168.18 at 2 dp)','LF = legend LF',168.18,'measured','Legend prints 1 decimal; the estimate carries PlanSwift\'s 2-decimal value. C-4.0 keynote 5: min slope 1%. No profile or invert data.')
add(726,'8: 1" PVC domestic water line','p77 C-5.0 legend "8: 1" PVC DOMESTIC WATERINE"','138.3 FT (138.27)','LF = legend LF',138.27,'measured','Spelling WATERINE carried from the legend into the estimate. Spec 22 1000 2.2A (p386) wants Type K copper for service entrance piping 3" and smaller; civil says 1" PVC. Conflict; see reading guide.')
add(727,'3: underground power service','p77 C-5.0 legend "3: UNDERGROUND POWER SERVICE."','72.9 FT (72.88)','LF = legend LF (route length)',72.88,'measured','Route LF, conduit count not stated on C-5.0. E-010 has the conduit detail (trade 26).')
add(728,'4: underground telephone service','p77 C-5.0 legend "4: UNDERGROUND TELEPHONE SERVICE"','74.4 FT (74.43)','LF = legend LF (route length)',74.43,'measured','Route LF.')
add(729,'4" sanitary cleanouts w/ recessed brass plug','p77 legend SANITARY CLEANOUTS 6 EA; C-5.0 SANITARY STRUCTURES S2..S7-SSCO','6 EA; 6 SSCO rows','EA = count(structure rows TYPE = CLEANOUT)',6,'counted','Size and plug from C-6.2 DETAIL - CLEANOUT TO GRADE (4" DIA MIN PIPE, RECESSED BRASS CLEANOUT PLUG, 18"x18"x 8" CONCRETE PAD OR 18" SQUARE CONCRETE COLLAR IN ALL PAVED AREAS - pad is trade 32b line 658, 18"X18"X8" THK).')
add(730,'A2-2-STGI hooded grate inlet','p74 legend A2-2-STGI: HOODED GRATE INLET 5 EA; C-4.0 STORM STRUCTURES','A2, A2.2, A3, A4, C2 -STGI','EA = count(structure rows TYPE = HOODED GRATE INLET)',5,'counted','Dots placed on the table rows, not on the plan. STGI = GDOT STD 1019A TYPE E (structure types box); C-6.1 has the GDOT inlet detail, yet the estimate says NO DETAILS.')
add(731,'Yard inlet','p74 legend YARD INLET 1 EA; C-4.0 STORM STRUCTURES','A2.1-STYI','EA = count(TYPE = YARD INLET)',1,'counted','STYI = NYOPLAST INLET W/DOME; C-6.2 shows the 1899CGD 18" dome grate.')
add(732,'4\'-0" DIA precast junction box','p74 legend JUNCTION BOX 1 EA; C-4.0 STORM STRUCTURES','B1-STJB (C1-STJB is EXISTING)','EA = count(TYPE = JUNCTION BOX and not EXISTING)',1,'counted','Size 4\'-0" DIA is the estimator\'s assumption (no detail) - stated in the line.')
add(733,'4\'-0" DIA precast outlet control structure','p74 legend OUTLET CONTROL STRUCTURE 1 EA; C-4.0 STORM STRUCTURES','B2-STOCS','EA = count(TYPE = OUTLET CONTROL STRUCTURE)',1,'counted','STOCS "SEE DETAILS SHEET C-6.2" but C-6.2 carries no OCS detail; C-4.2 shows the concrete riser with overflow inlet, rim 436.5. Size assumed.')
add(734,'5: 8"x8"x1" tapping saddle and corporation stop','p77 legend "5: PROPOSED 8"x8"x1" TAPPING SADDLE AND CO..."','1 EA','EA = legend count',1,'counted','C-5.0 keynote 5; C-6.3 DETAIL - TAPPING SLEEVE.')
add(735,'9: 1" domestic water meter','p77 legend "9: 1" DOMESTIC WATER METER"','1 EA','EA = legend count',1,'counted','Keynote 9 (meter AND RPZ in one note) split into two lines. C-6.3 STANDARD WATER METER DETAIL.')
add(736,'9: 1" domestic RPZ backflow preventer','p77 legend "9: 1" DOMESTICRPZ BACKFLOW PREVENTER"','1 EA','EA = legend count',1,'counted','Second item of keynote 9.')
add(737,'2: connection at existing manhole (core and grout)','p77 legend "2: CONNECTION AT EXISTING MANHOLE FOR SANI..."; C-5.0 S1-SSMH (EXISTING)','1 EA','EA = legend count',1,'counted','C-6.2 SECTION - DROP TIE-IN TO EXIST. MANHOLE. Existing invert 431.63 not verified (field-verify note).')
add(738,'A1-STHW 6" concrete headwall','p74 legend "A1-STHW: HEADWALL" 8.8 FT','8.8 FT','LF = legend LF rounded to whole feet',round(8.8),'measured','Estimator rounded the 8.8 FT polyline to whole feet (+2.3% over the raw legend). Ceil and round-to-nearest both give 9 (one sample); the direction is unverified. STHW = GDOT STD 1001B HEADWALL; one structure (A1). "6"" thickness is the estimator\'s.')
add(739,'2: irrigation backflow','p42 E-010 legend IRRIGATION BACKFLOW 1 EA + p87 E-010 legend "2: IRRIGATION BACKFLOW" 1 EA','1 + 1','EA = sum of legend counts across pages (as the estimator did)',1+1,'counted','Reproduced by construction (not grounded): exact only because the fixture replicates the estimator\'s double count. DOUBLE COUNT: p87 is a reprint of E-010; both dots sit on the same keynote-2 device. Physical count is 1 (C-5.0 keynote 10: reuse existing 1" irrigation meter, replace with new meter + RPZ if required). Engine should dedupe -> 1.')
add(740,'Excavation for pipe trenching','derived: lines 721+722+723+725; section is the estimator\'s (W x D = 15 SF inferred); C-4.0/C-5.0 rim-invert tables for the depth check',f'L = round(25.11+332.42+295.96+168.18 = {Ldr:.2f}) = {Lr} LF; W = 3.0 ft; D = 5.0 ft','CY = round(sum gravity pipe LF) x W x D / 27',exc,'derived (section inferred)','Reproduced by construction (not grounded): exact to 6 dp, but only the product W x D = 15 SF is fixed by the data (3x5, 2.5x6, 2x7.5 fit identically). 3.0 ft width is an estimator convention: the C-6.2 detail (O.D. + 18" MAX) is a City sanitary-PVC bedding standard stating a maximum, and by O.D. it gives 21" + 18" = 39" = 3.25 ft for 18" N-12 HDPE (2.02 ft for 6" PVC); the storm runs have no bedding detail (C-0.1 type 3: install per ASTM D2321). 5.0 ft is consistent with the length-weighted rim-to-invert + 4" bedding over the 14 storm+sanitary table rows (5.01 ft). Gas, water, power, telephone excluded (utility-installed or shallow). One uniform section for all four pipes.')
add(741,'Backfill for pipe trenching','derived: line 740 - line 742',f'{exc:.6f} - 42','CY = excavation CY - haul CY',bf,'derived from allowance','Reproduced by construction (not grounded): exact only because it subtracts the unexplained 42 CY haul allowance (line 742) from the inferred line-740 section. Same convention as earthwork lines 629-631: backfill = hole - what goes in it. Depends on the 42 CY haul (line 742). No compaction/shrink factor.')
add(742,'Hauloff (pipe trenching)','no reproducible source; whole-CY allowance','42 CY (=1134 CF); nominal pipe volume of the 4 runs = {:.1f} CF = {:.2f} CY'.format(pipevol,pipevol/27),'haul CY = estimator allowance (displaced pipe + bedding, rounded to whole CY)',None,'allowance/judgment','42 is a whole number while 740/741 are thirds of a CY: typed, not computed. Nominal pipe displacement is 27.22 CY; pipe + 2" bedding x 3\' (or 3" x 2\') rounds to 42.44 -> 42 but the detail calls 4" min bedding (-> 57.66). Treat as allowance; ratio 42/456.67 = 9.20%.')
with open(OUT+'reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print('exc',exc,'bf',bf,'pipevol',pipevol, pipevol/27, 'ratio',42/exc)
for r in rows: print(r['lineNo'],r['estimatorQty'],r['recomputedQty'],r['deltaPct'],r['classification'])
# fixtures
fx=[]
def F(n,formula,inputs,qty,tol,src):
    fx.append({'name':f'33-site-utilities line {n}: {L[n]["description"].splitlines()[0][:70]}','formula':formula,'inputs':inputs,'expected':{'quantity':r2(qty),'unit':L[n]['unit']},'tolerancePct':tol,'source':f'line {n} / {src}'})
F(721,'pipeLF = sum(runs where size=15")',{'runs':{'value':st15,'unit':'ft'},'size':{'value':15,'unit':'in'},'material':{'value':'HDPE','unit':'text'}},S15,0.01,'C-4.0 STORM PIPES table (p74)')
F(722,'pipeLF = sum(runs where size=18")',{'runs':{'value':st18,'unit':'ft'},'size':{'value':18,'unit':'in'},'material':{'value':'HDPE','unit':'text'}},S18,0.01,'C-4.0 STORM PIPES table (p74)')
F(723,'pipeLF = sum(runs)',{'runs':{'value':san,'unit':'ft'},'size':{'value':6,'unit':'in'},'material':{'value':'PVC','unit':'text'}},SS,0.01,'C-5.0 SANITARY PIPES table (p77)')
for n,v,src in [(725,168.18,'p74 C-4.0 legend 168.2 FT'),(726,138.27,'p77 C-5.0 legend 138.3 FT'),(727,72.88,'p77 C-5.0 legend 72.9 FT'),(728,74.43,'p77 C-5.0 legend 74.4 FT')]:
    F(n,'pipeLF = legend LF (2-dp PlanSwift value)',{'runs':{'value':[v],'unit':'ft'}},v,0.1,src)
for n,v,inp,src in [(729,6,{'type':{'value':'cleanout','unit':'text'},'count':{'value':6,'unit':'EA'}},'p77 legend + C-5.0 SSCO rows S2-S7'),
    (730,5,{'type':{'value':'inlet','unit':'text'},'count':{'value':5,'unit':'EA'}},'p74 legend + C-4.0 STGI rows A2,A2.2,A3,A4,C2'),
    (731,1,{'type':{'value':'yard-inlet','unit':'text'},'count':{'value':1,'unit':'EA'}},'p74 legend + A2.1-STYI'),
    (732,1,{'type':{'value':'junction-box','unit':'text'},'count':{'value':1,'unit':'EA'},'excludedExisting':{'value':['C1-STJB'],'unit':'text'}},'p74 legend + B1-STJB'),
    (733,1,{'type':{'value':'control-structure','unit':'text'},'count':{'value':1,'unit':'EA'}},'p74 legend + B2-STOCS'),
    (734,1,{'kind':{'value':'tapping-saddle','unit':'text'},'count':{'value':1,'unit':'EA'}},'p77 legend keynote 5'),
    (735,1,{'kind':{'value':'meter','unit':'text'},'count':{'value':1,'unit':'EA'}},'p77 legend keynote 9'),
    (736,1,{'kind':{'value':'backflow','unit':'text'},'count':{'value':1,'unit':'EA'}},'p77 legend keynote 9'),
    (737,1,{'kind':{'value':'connection','unit':'text'},'count':{'value':1,'unit':'EA'}},'p77 legend keynote 2')]:
    F(n,'EA = count',inp,v,0,src)
F(738,'headwallLF = legend LF rounded to whole feet (ceil vs nearest unverified: both give 9)',{'wallLength':{'value':8.8,'unit':'ft'},'roundTo':{'value':1,'unit':'ft'}},9,0,'p74 C-4.0 legend A1-STHW 8.8 FT')
F(739,'EA = sum(legend counts over pages) [estimator double count; dedupe gives 1]',{'pageCounts':{'value':[1,1],'unit':'EA'},'pages':{'value':[42,87],'unit':'page'}},2,0,'p42 + p87 E-010 legends')
F(740,'trenchExcCY = round(sum(L)) * W * D / 27',{'runs':{'value':[round(S15,2),round(S18,2),round(SS,2),168.18],'unit':'ft'},'trenchWidth':{'value':3.0,'unit':'ft'},'depth':{'value':5.0,'unit':'ft'},'roundLengthTo':{'value':1,'unit':'ft'}},exc,0.05,'lines 721+722+723+725; estimator section 3 ft x 5 ft (inferred, not detail-backed)')
F(741,'trenchBackfillCY = trenchExcCY - haulCY',{'excavation':{'value':r2(exc),'unit':'CY'},'haul':{'value':42,'unit':'CY'}},bf,0.05,'line 740 - line 742')
json.dump(fx,open(OUT+'fixtures.json','w'),indent=1)
print(len(fx),'fixtures')
