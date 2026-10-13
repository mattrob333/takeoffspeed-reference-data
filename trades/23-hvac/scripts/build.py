import json, math, csv, re
OUT='/home/user/takeoffspeed-reference-data/trades/23-hvac/'
L={l['lineNo']:l for l in json.load(open('/home/user/takeoffspeed-reference-data/reference/estimate/lines.json'))}
rect={'8x10':31.1,'14x12':7.3,'20x12':94.4,'24x12':13.3,'16x12':41.4,'10x10':7.4,'8x8':10.6,'12x12':9.8}
rnd={'8':113.7,'6':18.0,'10':10.5,'14':10.2}
rsf=sum(2*sum(map(int,k.split('x')))/12*v for k,v in rect.items())
osf=sum(math.pi*int(d)/12*v for d,v in rnd.items())
S=rsf+osf
rows=[]; fx=[]
def add(n,desc,src,sv,formula,re,cls,notes,fixture=None):
    l=L[n]; q=l['quantity']
    d=round((re/q-1)*100,3) if q else 0
    rows.append([n,desc,l['unit'],q,src,sv,formula,round(re,2),d,cls,notes])
    if fixture: 
        fname,inputs,tol,source=fixture
        fx.append({'name':f'23-hvac line {n}: {desc}','formula':fname,'inputs':inputs,'expected':{'quantity':q,'unit':l['unit']},'tolerancePct':tol,'source':source})
P53='markup p53 (M-301)'; P54='markup p54 (M-302)'
add(445,'Allowance for duct fittings (area 2000 SF)','judgment (no markup)','G-001 "1900 GSF" / "1892 S.F."; title block "1,900 SF"; estimate text "AREA: 2000 SF"','1 LS; area basis 2000 SF in description',1,'allowance/judgment','No markup or schedule. Same 2000 SF area-basis allowance as plumbing 403, electrical 510, low-voltage 622. Covers fittings (elbows, transitions, takeoffs, spin-ins), hangers, sealant, turning vanes, flexible connections, access doors not taken off.')
rin={k+'_LF':{'value':v,'unit':'LF','legendItem':f'{k} DUCT','markupPage':53} for k,v in rect.items()}
oin={k+'in_round_LF':{'value':v,'unit':'LF','legendItem':f'{k}" DUCT','markupPage':53} for k,v in rnd.items()}
sv_r='; '.join(f'{k} {v} FT' for k,v in rect.items()); sv_o='; '.join(f'{k}" {v} FT' for k,v in rnd.items())
add(446,'26 ga galvanized metal ductwork','markup legend p53 (M-301): 8 rectangular + 4 round rigid duct rows; M-001 gauge note','%s; %s; 26 ga = 0.906 lb/SF'%(sv_r,sv_o),'LBS = [Σ LF×2(W+H)/12 + Σ LF×πD/12] × 0.906 lb/SF; no seam/fitting/waste allowance',S*0.906,'derived',f'Rigid surface {rsf:.2f} SF rect + {osf:.2f} SF round = {S:.2f} SF. M-001 Part 2.1.B: rectangular 26 ga all sizes; round <=14" 26 ga (all round here <=14"). Flex excluded. Estimator rounded to nearest 100 lb (1200.28 -> 1200).',
    ('duct sheet-metal LBS = bare rigid surface SF x lb/SF(gauge)',{**rin,**oin,'gauge':{'value':26,'unit':'ga','source':'M-001 Part 2 1.B'},'lbPerSF':{'value':0.906,'unit':'lb/SF','basis':'26 ga galvanized'},'seamAllowance':{'value':0,'unit':'fraction'}},0.5,'446 / markup p53'))
add(447,'1.5" fiberglass duct insulation','derived from line 446 inputs (markup p53 rigid duct rows)','same 12 rigid-duct rows; flex excluded','SF = Σ LF×2(W+H)/12 (rect) + Σ LF×πD/12 (round) = bare sheet-metal surface; thickness not in the formula',S,'derived',f'= {S:.2f} SF, rounded 1325. Every rigid run (supply AND return) wrapped; no liner, no 8t stretch-out, no lap, no waste. Spec 23 0713 2.2.A calls 2.2" R-6 FSK wrap on unlined supply and 1" liner in all return and 25 ft downstream of each RTU; estimator carried one 1.5" wrap line on all rigid duct.',
    ('duct insulation SF = bare rigid duct surface SF',{**rin,**oin,'insulationThickness':{'value':1.5,'unit':'in','note':'estimator text; not used in the area'},'lapIn':{'value':0,'unit':'in'}},0.5,'447 / markup p53'))
for n,d,lv,item in [(448,6,6.9,'6"DIA FLEXIBEL DUCT'),(449,8,50.1,'8"DIA FLEXIBLE DUCT'),(450,10,4.8,'10"DIA FLEXIBLE DUCT'),(451,14,3.1,'14"DIA FLEXIBLE DUCT')]:
    add(n,f'{d}" dia flexible duct',f'markup legend {P53}',f'"{item}" {lv} FT','LF = legend LF (net, no waste)',lv,'measured','Legend prints 1 decimal; estimate keeps PlanSwift precision. Factory-insulated (spec 23 3100 2.5.B R-4.2 min); not added to line 447.',
        ('measured LF = legend LF',{'flex_LF':{'value':lv,'unit':'LF','legendItem':item,'markupPage':53},'diameter':{'value':d,'unit':'in'}},1.0,f'{n} / markup p53'))
add(452,'Refrigerant piping, size not given','markup legend p53 (M-301)','"REFRIGERANT PIPING, SIZE NOT GIVEN" 30.9 FT','LF = legend LF (one route LF, not liquid + suction)',30.9,'measured','Route FCU-1 to roof penetration on M-301 only; the roof run on M-302 (HP-1 to penetration, dashed) was not measured. M-301 keynote 2: size per manufacturer. Spec 23 2300 2.4.A: suction insulated 1-1/2" AP Armaflex - no insulation line carried.',
    ('measured LF = legend LF',{'route_LF':{'value':30.9,'unit':'LF','legendItem':'REFRIGERANT PIPING, SIZE NOT GIVEN','markupPage':53}},1.0,'452 / markup p53'))
dev=[
(453,'LSD (2-48") 185 CFM','"LSD (2-48")" 1.0 EA (magenta)','LSD (2-48") / 185 CFM',1,'Air distribution schedule LSD(X): X = number of 1" slots; 48" = 4\'-0" long; Titus MLTI-39 with insulated plenum.'),
(454,'LSD (3-48") 185 CFM','"LSD (3-48")" 1.0 EA (cyan, first of two rows)','LSD (3-48") / 185 CFM',1,'Two legend rows share the name LSD (3-48"); colour on plan separates 185 (cyan) from 330 (olive).'),
(455,'LSD (2-48") 140 CFM','"LSD (2-48")CFM: 140" 6.0 EA','LSD (2-48") / 140 CFM',6,''),
(456,'LSD (3-48") 330 CFM','"LSD (3-48")" 1.0 EA (olive, second row)','LSD (3-48") / 330 CFM',1,'Row missing from legends.json (duplicate name dropped); read from the legend image.'),
(457,'LSD (1-48") 110 CFM','"LSD (1-48")" 1.0 EA (indigo)','LSD (1-48") / 110 CFM',1,''),
(458,'LSD (1-48") 90 CFM','"LSD (1-48")CFM: 90" 1.0 EA','LSD (1-48") / 90 CFM',1,''),
(459,'LSD (2-24") 60 CFM','"LSD (2-24")" 2.0 EA (teal, first row)','LSD (2-24") / 60 CFM',2,'24" long = schedule "LD (X)" 2\'-0" slot diffuser.'),
(460,'LSD (2-24") 150 CFM','"LSD (2-24")" 2.0 EA (salmon, second row)','LSD (2-24") / 150 CFM',2,'Row missing from legends.json; read from legend image.'),
(461,'LSR (3-48") 350 CFM','"LSR (3-48")" 1.0 EA','LSR (3-48") / 350 CFM',1,'Keynote 8: full-size 12" high sheet-metal plenum, painted flat black (paint in Div 09 line 305).'),
(462,'24x24 supply diffuser 80 CFM, 6" neck','"24"x24" SUPPLY AIR DIFFUSER" 1.0 EA (magenta)','80S',1,'Neck from schedule S(CFM): 0-100 -> 6"ø. Five legend rows share this name (one per CFM); four are missing from legends.json.'),
(463,'12x12 supply diffuser 65 CFM, 6" neck','"12"x12" SUPPLY AIR DIFFUSERCFM: 65" 2.0 EA','65S',2,'Schedule: 0-90 CFM -> 6"ø, face 12x12.'),
(464,'24x24 supply diffuser 60 CFM, 6" neck','"24"x24" SUPPLY AIR DIFFUSER" 1.0 EA (brown)','60S',1,'Row missing from legends.json.'),
(465,'24x24 supply diffuser 160 CFM, 8" neck','"24"x24" SUPPLY AIR DIFFUSER" 1.0 EA (medium green)','160S',1,'Schedule 101-210 CFM -> 8"ø. Row missing from legends.json.'),
(466,'24x24 supply diffuser 370 CFM, 12" neck','"24"x24" SUPPLY AIR DIFFUSER" 1.0 EA (indigo)','370S',1,'Schedule 331-480 -> 12"ø. Row missing from legends.json.'),
(467,'24x24 supply diffuser 240 CFM, 10" neck','"24"x24" SUPPLY AIR DIFFUSER" 1.0 EA (bright green)','240S',1,'Schedule 211-330 -> 10"ø. Row missing from legends.json.'),
(468,'24x24 return grille 12x12 neck 360 CFM','"24"x24" RETURN AIR GRILLENECK SIZE: 12"x12"CFM: 360" 1.0 EA','360R 12"x12"',1,'Titus 50F eggcrate.'),
(469,'24x24 return grille 10x10 neck 220 CFM','"24"x24" RETURN AIR GRILLE" 2.0 EA (purple)','220R 10"x10"',2,'Row missing from legends.json.'),
(470,'24x24 return grille 8x8 neck 50 CFM','"24"x24" RETURN AIR GRILLE" 1.0 EA (teal)','50R 8"x8"',1,'Row missing from legends.json; teal dot sits on the 50R tag.'),
(471,'24x24 return grille 8x8 neck 65 CFM','"24"x24" RETURN AIR GRILLENECK SIZE: 8"x8"CFM: 65" 1.0 EA','65R 8"x8"',1,''),
(472,'24x24 return grille 16x16 neck 895 CFM','"24"x24" RETURN AIR GRILLE" 1.0 EA (yellow)','895R 16"x16"',1,'The one un-suffixed RAG row in legends.json; yellow dot sits on 895R.'),
(473,'24x24 return grille 16x16 neck 1000 CFM','"24"x24" RETURN AIR GRILLENECK SIZE: 16"x16"CFM: 1000" 1.0 EA','1000R 16"x16"',1,''),
]
for n,desc,leg,tag,q,note in dev:
    add(n,desc,f'markup legend {P53}; M-301 plan tags; M-101 air distribution schedule',f'{leg}; plan text tag "{tag}" x{q}','EA = count of device tag+size+CFM on M-301 (= legend count)',q,'counted',note,
        ('count = placements of tag+size+CFM',{'count':{'value':q,'unit':'EA','legendItem':re.match(r'^"(.*)" [\d.]+ EA',leg).group(1),'legendRow':leg,'planTag':tag,'markupPage':53}},0,f'{n} / markup p53'))
cnt=[
(474,'EF-1 exhaust fan Greenheck SP-B90','"EF-1" 1.0 EA',P53,1,'M-101 exhaust fan schedule; ceiling fan, integral backdraft damper, disconnect (note 4).'),
(475,'EF-2 exhaust fan Greenheck SP-B110','"EF2" 1.0 EA',P53,1,''),
(476,'EF-3 exhaust fan Greenheck SP-B110','"EF3" 1.0 EA',P53,1,''),
(477,'RTU-1 rooftop heat pump unit Carrier','"RTU-1" 1.0 EA',P54,1,'M-101 RTU schedule (model printed 48FEDA05J3M5-8W4D0; estimate text reads 48FRDA..., a transcription slip). 18" curb is carried in roofing line 171, not here.'),
(478,'RTU-2 rooftop heat pump unit Carrier','"RTU-2" 1.0 EA',P54,1,''),
(479,'Mini-split FCU-1/HP-1 Mitsubishi (indoor+outdoor)','"HP-1" 1.0 EA',P54,1,'One system counted at the outdoor unit HP-1; indoor FCU-1 on M-301 keynote 11 not counted separately (one line = one system).'),
(480,'1-1/2" RTU condensate drain w/ P-trap & vented cap','"1-1/2" RTU CONDENSATE DRAIN W/ P-TRAP & REMOVEABLE VENTED CAP" 1.0 EA',P54,1,'M-302 shows keynote 2 at BOTH RTUs (one tag marked, one not). Drawings support 2 EA; estimator counted 1. Pipe is plumbing line 417.'),
(481,'Supply air temperature sensor','"SUPPLY AIR TEMPERATURE SENSOR" 2.0 EA',P53,2,'Symbols SAT and ST on M-301 (one per RTU supply).'),
(482,'Return air temperature sensor','"RETURN AIR TEMPERATURE SENSOR" 2.0 EA',P53,2,'Symbols RAT and RT on M-301 (one per RTU return).'),
(483,'CO2 sensor','"CARBON DIOXIDE (C02) SENSOR" 2.0 EA',P53,2,'Symbol C x2 at the RTU thermostats (grid line C excluded).'),
(484,'VOC sensor','"VOC SENSOR" 1.0 EA',P53,1,'Symbol V (M-002: VOC sensor in supply duct, BAPI).'),
(485,'Temperature sensor','"TEMPERATURE SENSOR" 4.0 EA',P53,4,'Symbol S at the RTU zones (yellow dots).'),
(486,'Outdoor air temperature sensor','"OUTDOOR AIR TEMPERATURE SENSOR" 2.0 EA',P54,2,'Symbol OAT at each RTU on M-302.'),
(487,'Thermostat control','"THERMOSTAT CONTROL" 4.0 EA',P53,4,'Symbol T x4 (M-101: KMC FlexStat by IOT, installed by MC).'),
(488,'24x22 exhaust hood (gravity ventilator) eq. Greenheck FGR','"24"x22" EXHAUST HOOD, NOA 19-0802.02 EQUAL TO GREENHECK FGR" 1.0 EA',P54,1,'M-302 keynote 6; serves 8" exhaust duct up from EF.'),
(489,'Remote cable operated damper','"REMOTE CABLE OPERATED DAMPER" 13.0 EA',P53,13,'= keynote 6 tags (8, at slot plenums) + keynote 7 tags (5, at ceiling diffusers) on M-301. Not one per device: 15 LSD + 7 supply diffusers = 22 devices.'),
(490,'Petroleum-based wax controlled (VAV) damper','"PETROLEUM BASED WAX CONTROLLED DAMPER" 1.0 EA',P53,1,'Keynote 9 tag x1 (Acutherm Therma-Fuser equal; note: credit in southern projects).'),
(491,'Manual damper','"MANUAL DAMPER" 1.0 EA',P53,1,'Plan text "MD IN VERTICAL".'),
(492,'Particle counter eq. Sensirion SP530','"PARTICLE COUNTER EQUAL TO SENSIRION AG SP530" 1.0 EA',P53,1,'Symbol PC (M-002: in return duct).'),
(493,'Temperature & RH display','"TEMPERATURE & RELATIVE HUMIDITY DISPLAY" 1.0 EA',P53,1,'Symbol TR with keynote 10.'),
(494,'Titus SB steel sectorizing baffle','"TITUS SB STEEL SECTORIZING BAFFLE" 1.0 EA',P53,1,'Keynote 12 tag x1.'),
]
for n,desc,leg,pg,q,note in cnt:
    add(n,desc,f'markup legend {pg}',leg,'EA = legend count (symbol/tag count on the sheet)',q,'counted',note,
        ('count = placements of the symbol/tag',{'count':{'value':q,'unit':'EA','legendItem':re.match(r'^"(.*)" [\d.]+ EA',leg).group(1),'markupPage':53 if pg==P53 else 54}},0,f'{n} / {pg}'))
assert len(rows)==50, len(rows)
with open(OUT+'reconciliation.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow('lineNo,description,unit,estimatorQty,source,sourceValues,formula,recomputedQty,deltaPct,classification,notes'.split(',')); w.writerows(rows)
json.dump(fx,open(OUT+'fixtures.json','w'),indent=1)
print(len(rows),len(fx)); 
for r in rows: 
    if abs(r[8])>0.001: print(r[0],r[3],r[7],r[8])
print('S',S,rsf,osf)
