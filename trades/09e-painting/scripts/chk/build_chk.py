import json, csv, math, os
OUT='/home/user/work/09e-painting/chk'
L={l['lineNo']:l for l in json.load(open('/home/user/takeoffspeed-reference-data/reference/estimate/lines.json'))}
ceil5=lambda x: 5*math.ceil(round(x,6)/5)
ceil1=lambda x: math.ceil(round(x,6))
ceil10=lambda x: 10*math.ceil(round(x,6)/10)
def ft(f,i=0): return f+i/12
rows=[]; fx=[]
def add(n,desc,source,vals,formula,q,cls,notes,raw=None):
    e=L[n]['quantity']; d=(q-e)/e*100
    rows.append(dict(lineNo=n,description=desc,unit=L[n]['unit'],estimatorQty=e,source=source,sourceValues=vals,formula=formula,
        recomputedQty=round(q,2),deltaPct=round(d,2),classification=cls,notes=notes))
    print(n, e, round(q,3), f'{d:+.3f}%', '' if raw is None else f'raw {raw:.2f} ({(raw-e)/e*100:+.2f}%)')
# 295 PT-1
pt1=[(62.6,12,"12'H"),(15,11,"11'H"),(39.7,8.5,"8'6\"H"),(4.9,6.5,"6'6\"H"),(51.8,10,"10'H"),(117.1,9,"9'H"),(48,12.5,"12'6\"H")]
runs=sum(a*b for a,b,_ in pt1); a410=252.6; q=runs+a410
add(295,'PT-1 WALL PAINT SW PROMAR 200 HP ZERO VOC SW9166 (1P+2C)','markup p08 (A-150) PT1 PAINT @ <H> x7; markup p16 (A-410) PT1 WALL PAINT',
    '; '.join(f'{a} FT @ {h}' for a,_,h in pt1)+f' (= {runs:.1f} SF); A-410 {a410} SQ FT',
    'SF = sum(run LF x painted height per run, height = room ceiling height from A-130 or 12.5 ft to structure) + traced elevation area',q,
    'derived (LF x H) + measured (area)','339.1 LF of runs on A-150; restrooms 112/113 measured as areas above the tile band on A-410 elevations (both rooms). Delta is legend 1-decimal display; line carries PlanSwift precision. No opening deduction visible in the method.')
fx.append(dict(name='PT-1 wall paint = sum(run x height) on finish plan + restroom elevation area',formula='painting.walls (runTimesHeight per height group + areas)',
  inputs=dict(runs=[dict(run_lf=a,height_ft=b,legend=f'PT1 PAINT @ {h}') for a,b,h in pt1],areas_sf={'A-410 restrooms above tile (both rooms)':a410},primerCoats=1,finishCoats=2),
  expected=dict(quantity=L[295]['quantity'],unit='SF'),tolerancePct=0.5,source='295 / markup p08, p16'))
# 296 PT-4
q=5.3*9+10.6*10
add(296,'PT-4 WALL PAINT BM REGAL SELECT 2066-10 BLUE (1P+2C)','markup p08 (A-150) PT4 @ 9\'H; PT4 @ 10\'H','5.3 FT @ 9 ft; 10.6 FT @ 10 ft',
    'SF = sum(run LF x height)',q,'derived (LF x H)','9 ft group = Phone Room 114 north wall (PL-2/PT-4 tag, 9\'-0" ACT); 10 ft group = Gathering Area 103 north tech wall (PT-4/PT-7 tag, 10\'-0" GWB ceiling; A-704). Tech-wall run is not net of the PT-6 recess back wall (37.2 SF carried again on line 297); recess returns (PT-4, A-704) not added.')
fx.append(dict(name='PT-4 accent walls = sum(run x height)',formula='painting.walls (runTimesHeight)',inputs=dict(runs=[dict(run_lf=5.3,height_ft=9.0,where='Phone Room 114'),dict(run_lf=10.6,height_ft=10.0,where='Gathering Area 103 tech wall')],primerCoats=1,finishCoats=2),
  expected=dict(quantity=L[296]['quantity'],unit='SF'),tolerancePct=0.5,source='296 / markup p08'))
# 297 PT-6
raw=37.2; q=ceil5(raw)
add(297,'PT-6 WALL PAINT BM REGAL SELECT 1603 GRAPHITE EGGSHELL (1P+2C)','markup p28 (A-704) PT6','37.2 SQ FT (tech wall recess back wall; same 37.2 as TYPE X GWB and 5/8" PLYWOOD BACKING rows)',
    'SF = ceil5(traced elevation area)',q,'measured (area) + estimator rounding','Raw 37.2 SF is -7.0%. A-704: "PAINT THE BACK WALL IN RECESS FLAT BLACK, PT-6" (schedule says EGGSHELL; note says FLAT BLACK). Vector check 7\'-9 3/4" x 4\'-9 1/4" = 37.27 SF.',raw)
fx.append(dict(name='PT-6 tech wall recess = traced area, rounded up to 5 SF',formula='painting.walls (areas) + ceilTo5',inputs=dict(areas_sf={'A-704 recess back wall':37.2},rounding='ceil to 5 SF (estimator hand-entry convention)'),
  expected=dict(quantity=40.0,unit='SF'),tolerancePct=0.1,source='297 / markup p28'))
# 298 PT-7
raw=10.3*10; q=ceil5(raw)
add(298,'PT-7 SHIELDZ UNIVERSAL WALLCOVERING PRIMER ROMAN PRO-999','markup p08 (A-150) PT7 @ 10\'','10.3 FT @ 10 ft (Meeting Room 105 north wall)',
    'SF = ceil5(run LF x height)',q,'derived (LF x H) + estimator rounding','Raw 103 SF (-1.9%), same 10.3 FT x 10\' as line 240 wallcovering (103 SF, not rounded). Schedule A-170: PT-7 = PRIMER (dries clear), so the estimate text "one coat primer with two coats of paint" overstates coats. Gathering Area 103 north wall also carries a PT-4/PT-7 tag; no PT-7 was measured there.',raw)
fx.append(dict(name='PT-7 wallcovering primer = run x height, rounded up to 5 SF',formula='painting.walls (runTimesHeight, primerCoats=1, finishCoats=0) + ceilTo5',inputs=dict(run_lf=10.3,height_ft=10.0,where='Meeting Room 105 north wall',primerCoats=1,finishCoats=0,rounding='ceil to 5 SF'),
  expected=dict(quantity=105.0,unit='SF'),tolerancePct=0.1,source='298 / markup p08'))
# 299 PT-8
raw=7.4*10; q=ceil5(raw)
add(299,'PT-8 WALL PAINT BM REGAL SELECT 797 ATHENS BLUE EGGSHELL (1P+2C)','markup p08 (A-150) PT8 @ 10\'','7.4 FT @ 10 ft (Meeting Room 105 west wall)',
    'SF = ceil5(run LF x height)',q,'derived (LF x H) + estimator rounding','Raw 74 SF (-1.3%). West wall is a window wall; window not deducted.',raw)
fx.append(dict(name='PT-8 meeting room feature wall = run x height, rounded up to 5 SF',formula='painting.walls (runTimesHeight) + ceilTo5',inputs=dict(run_lf=7.4,height_ft=10.0,primerCoats=1,finishCoats=2,rounding='ceil to 5 SF'),
  expected=dict(quantity=75.0,unit='SF'),tolerancePct=0.1,source='299 / markup p08'))
# 300 PT-3 ceiling
soff=[(4.2,7.0,'SOFFIT @ 3\'6"H, GWB BS (both sides 2 x 3.5)'),(2.7,4,'SOFFIT @ 6\'6"H, GWB @ 4\'H'),(6.7,1.5,'SOFFIT @ 3\'6"H, GWB @ 1\'6"H'),(30.5,3,'SOFFIT @ 4\'6"H, GWB @ 3\'H'),(35.3,2.5,'SOFFIT @ 5\'9"H, GWB @ 2\'6"H'),(28.1,2,'SOFFIT @ 2\'H')]
soffSF=sum(a*b for a,b,_ in soff); ceil_=516.1; q=ceil_+soffSF
print(' soffit SF',soffSF,' via estimate lines 278+285 =',L[278]['quantity']+L[285]['quantity'])
add(300,'PT-3 CEILING PAINT SW PROMAR 200 HP ZERO VOC SW9166 FLAT (1P+2C)','markup p05 (A-130) 5/8" GWB CEILING (PT3) + six SOFFIT rows; = estimate line 278 (516.0) + line 285 (286.04)',
    f'GWB ceiling 516.1 SQ FT; soffits '+'; '.join(f'{a} FT x {b} ft' for a,b,_ in soff)+f' = {soffSF:.2f} SF',
    'SF = GWB ceiling area + sum(soffit LF x soffit GWB face height); equals ceiling board line + soffit board line',q,
    'derived (sum of parent board lines)','Lines 278 + 285 = 802.04, carried as 802. A-130 note E says gypsum ceilings are PT-1, but the RCP tags read PT-3 and A-170 PT-3 = FLAT; the estimator followed the tags. Transaction bar ceiling (AC2/BAR-1) excluded.')
fx.append(dict(name='PT-3 gypsum ceiling + soffit faces',formula='painting.ceilings (gypsum areas) with soffit faces = sum(LF x face height)',
  inputs=dict(ceiling_sf=516.1,soffits=[dict(run_lf=a,face_height_ft=b,legend=c) for a,b,c in soff],primerCoats=1,finishCoats=2),
  expected=dict(quantity=802.0,unit='SF'),tolerancePct=0.5,source='300 / markup p05; lines 278, 285'))
# 301 exposed
raw=98.4; q=ceil5(raw)
add(301,'PT-3 PAINT AT EXPOSED STRUCTURE (1P+2C)','markup p05 (A-130) EXPOSED STRUCTURE','98.4 SQ FT plan area (Janitor 115 + Elec/IT 106, "EXPOSED CEILING ALL WALLS TO DECK")',
    'SF = ceil5(plan area x 1.0)',q,'measured (area) + estimator rounding','Raw -1.6%. Plan area only: no deck-flute or joist surface factor. 1-1/2" Type B deck plus joists would add roughly 25-50% real surface.',raw)
fx.append(dict(name='Exposed structure paint = plan area, rounded up to 5 SF',formula='painting.ceilings (exposed-structure, surfaceFactor 1.0) + ceilTo5',inputs=dict(areas_sf={'Janitor 115 + Elec/IT 106':98.4},surfaceFactor=1.0,rounding='ceil to 5 SF'),
  expected=dict(quantity=100.0,unit='SF'),tolerancePct=0.1,source='301 / markup p05'))
# 302 PT-5
raw=76.2; q=ceil1(raw)
add(302,'PT-5 BOOTH ROOF BM REGAL SELECT 2037-30 KELLY GREEN','markup p29 (A-706) PT5 FINISH @ BOOTH ROOF','76.2 SQ FT (booth roof framing plan, top of 3/4" plywood)',
    'SF = ceil1(plan area)',q,'measured (area) + estimator rounding','Raw -1.0%. Rounded to whole SF here, not to 5 (same 76.2 -> 77 as line 312 booth framing LF). Schedule A-170 says PT-5 SEMI-GLOSS; the line says EGGSHELL. 09 9110 groups "Top of Booth Ceiling (PT-5)" with steel; A-706 says 3/4" plywood. Plywood edges ("ALL EDGES TO BE PAINTED GREEN") not added.',raw)
fx.append(dict(name='PT-5 booth roof = plan area, rounded up to whole SF',formula='painting.ceilings (other) + ceilTo1',inputs=dict(areas_sf={'A-706 booth roof framing plan':76.2},rounding='ceil to 1 SF'),
  expected=dict(quantity=77.0,unit='SF'),tolerancePct=0.1,source='302 / markup p29'))
# 303 frames
q=2+1+3
add(303,'3x7 HM FRAME PT-2 SW PROMAR 200 SEMI-GLOSS (1P+2C)','markup p21 (A-600) door legend rows with HOLLOW METAL FRAME; = estimate lines 191+192+193',
    '3\'Wx7\'H TYPE B W/ WELDED HM FRAME 3 EA + 2 EA; TYPE C W/ KNOCK-DOWN HM FRAME 1 EA','EA = count of doors with hollow metal frames',q,'counted',
    'Doors are solid-core wood (factory finish by door trade), so only frames are painted. Storefront and the Type F slider are aluminium, not painted. 08 1113 p214 frames ship "Exposed Finish: Prime" and 09 9100 3.3.B.2 says omit primer on shop-primed metal, so the carried field primer coat is conservative.')
fx.append(dict(name='Painted HM frames = count of HM-framed doors',formula='painting.doors-frames (frames count)',inputs=dict(frames=[{'size':"3'-0\" x 7'-0\"",'count':3,'type':'B welded'},{'size':"3'-0\" x 7'-0\"",'count':2,'type':'B welded, card reader'},{'size':"3'-0\" x 7'-0\"",'count':1,'type':'C knock-down'}]),
  expected=dict(quantity=6.0,unit='EA'),tolerancePct=0.0,source='303 / markup p21'))
# 304 trim
d1=6*(3+14)+(ft(3,4)+14)+(6+16)+(6+16)+(3+16)
win={'A':(ft(12,11.5),12,1),'C':(ft(7,4),12,1),'D':(8,ft(9,4),1),'E':(6,ft(7,4),2),'G':(ft(13,4),ft(9,4),1),'H':(14,ft(9,4),1)}
w1=sum(2*(w+h)*n for w,h,n in win.values()); back=2*(d1+w1)
print(' trim back-fit doors',d1,'windows',w1,'x2',back,'ceil10',ceil10(back))
add(304,'PT-2 PAINT AT OPENING TRIM (SEMI-GLOSS)','estimate line 88 INTERIOR TRIM AT OPENING, ASSUMED (910 LF); no markup legend row',
    f'line 88 = 910 LF. Back-fit: doors (2H+W) {d1:.2f} LF + EA-counted window perimeters {w1:.2f} LF = {d1+w1:.2f} LF one face',
    'LF = line 88 (assumed). Back-fit hypothesis: 2 faces x (sum door 2H+W + sum window perimeters), rounded up to 10',back,
    'allowance/judgment (copied from an ASSUMED carpentry line)','No drawing shows interior wood trim at openings (storefront and HM frames have no casing); the parent line says ASSUMED. The 2-face back-fit gives 901.83 -> 910 after rounding up to 10 (-0.9% before rounding), but it counts exterior faces and leaves out storefront windows B, F, J and K, so it is a plausible fit, not a proven source. GPT-6 Astra reached the same conclusion.')
# 305 diffusers
q=4+1
add(305,'BLACK PAINT CEILING DIFFUSER','markup p53 (M-301) PAINT LSD BLACK; PAINT BLACK LSR','4 EA (keynote 5 "IN UPPER CEILING. PAINT BLACK." on LSD diffusers) + 1 EA (keynote 8 LSR(3) plenum "INSIDE TO BE PAINTED FLAT BLACK")',
    'EA = count of keynote-5 devices + keynote-8 devices',q,'counted','M-301 text layer: keynote 5 bubbles x4 in plan (the fifth "5" is grid bubble 5), keynote 8 x1. 09 9100 3.3.A.6: paint duct interiors visible through grilles flat black (not carried separately).')
fx.append(dict(name='Black-painted diffusers = keynote-tagged device count',formula='painting.mep (device count)',inputs=dict(count_by_keynote={'5 IN UPPER CEILING. PAINT BLACK. (LSD)':4,'8 LSR(3) plenum painted flat black':1},color='BLACK',device='CEILING DIFFUSER'),
  expected=dict(quantity=5.0,unit='EA'),tolerancePct=0.0,source='305 / markup p53'))
# 306, 307 gas
for n,size,lf in ((306,'3/4"',44.2),(307,'1"',9.7)):
    q=ceil5(lf)
    add(n,f'{size} DIA ROOF GAS PIPE SAFETY YELLOW PAINT','markup p58 (P-303) '+f'{size}DIA GAS PIPE; SAFETY YELLOW PAINT AT ROOD GAS PIPE 53.9 FT',f'{lf} FT (roof gas pipe of this size); 44.2 + 9.7 = 53.9 = safety-yellow row',
        'LF = ceil5(roof gas pipe LF of this size)',q,'measured (LF) + estimator rounding',
        f'Raw {(lf-L[n]["quantity"])/L[n]["quantity"]*100:+.1f}%. P-403 PIPE PAINTING NOTE: "EXTERIOR ROOF-LEVEL NATURAL GAS PIPING SHALL BE PAINTED SAFETY YELLOW"; interior gas piping above ceilings stays unpainted, so the P-301 1" natural gas pipe (18.6 FT) is correctly excluded. Gas piping lines 418/420 carry 9.71 / 44.21 LF unrounded.',lf)
    fx.append(dict(name=f'Safety-yellow roof gas pipe {size}',formula='painting.mep (pipe LF) + ceilTo5',inputs=dict(pipeSize=size,service='GAS',color='SAFETY YELLOW',pipe_lf=lf,rounding='ceil to 5 LF'),
      expected=dict(quantity=L[n]['quantity'],unit='LF'),tolerancePct=0.1,source=f'{n} / markup p58'))
with open(f'{OUT}/reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
json.dump(fx,open(f'{OUT}/fixtures.json','w'),indent=1)
print(len(rows),'rows',len(fx),'fixtures')
print('within1',sum(abs(r['deltaPct'])<=1 for r in rows),'within5',sum(abs(r['deltaPct'])<=5 for r in rows))
