"""09b ceilings: rebuild every estimate quantity from markup legend rows; write reconciliation.csv + fixtures.json."""
import json, csv, math
REF='/home/user/takeoffspeed-reference-data'; OUT=f'{REF}/trades/09b-ceilings'
L={l['lineNo']:l for l in json.load(open(f'{REF}/reference/estimate/lines.json'))}
IDS=[t for t in json.load(open(f'{REF}/reference/estimate/trades.json')) if t['trade']=='09b-ceilings'][0]['lines']
G=json.load(open(f'{REF}/reference/markups/legends.json'))
def leg(page,name):
    for p in G:
        if p['page']==page:
            for it in p['items']:
                if it['name']==name: return float(it['quantity'])
    raise KeyError(name)
GWB=leg(5,'5/8" GWB CEILING O/ 3-5/8" METAL STUD FRAMING (PT3)')
AC1=leg(5,'AC1 CEILING'); AC2=leg(5,'AC2 CEILING'); BAR=leg(6,'2"x8" BAFFLE SYSTEM - BAR-1')
# soffit rows: key -> (legend name, LF, framing height ft, board height ft, faces)
SOF=[('SOFFIT @ 3\'6"H, GWB BS',3.5,3.5,2),('SOFFIT @ 6\'6"H, GWB @ 4\'H',6.5,4.0,1),('SOFFIT @ 3\'6"H, GWB @ 1\'6"H',3.5,1.5,1),
     ('SOFFIT @ 4\'6"H, GWB @ 3\'H',4.5,3.0,1),('SOFFIT @ 5\'9"H, GWB @ 2\'6"H',5.75,2.5,1),('SOFFIT @ 2\'H',2.0,2.0,1)]
SOF=[(n,leg(5,n),fh,bh,f) for n,fh,bh,f in SOF]
BR=[(n,leg(5,n),h) for n,h in [('3-5/8" METAL STUD BRACING @ 48" O.C @ 5\'H',5.0),('3-5/8" METAL STUD BRACING @ 48" O.C @ 8\'H',8.0)]]
DIV=1.33   # estimator's 16" O.C. divisor (16/12 rounded)
SHEET=32; ADH=0.031; TAPE=0.00075; SCREW=0.0375/7; MUD=0.53
soffit_sf=sum(lf*bh*f for n,lf,fh,bh,f in SOF)
F=sum(lf*fh for n,lf,fh,bh,f in SOF)
brace=sum(lf/4*h for n,lf,h in BR)
soffit_studs=F/DIV+brace
alt_third=(F+sum(lf*h for n,lf,h in BR)/3)/DIV
print('soffit SF',soffit_sf,'F',F,'brace',brace,'studs',soffit_studs,'alt(1/3 in divisor)',alt_third)
E=lambda n:L[n]['quantity']
def d(est,rec): return round((rec-est)/est*100,3)
short=lambda n:L[n]['description'].split('\n')[0][:70]
rows=[]; fx=[]
def add(n,source,sv,formula,rec,cls,notes,fname=None,inputs=None,tol=0.5,fsrc=None):
    rows.append(dict(lineNo=n,description=short(n),unit=L[n]['unit'],estimatorQty=E(n),source=source,sourceValues=sv,formula=formula,recomputedQty=round(rec,6),deltaPct=d(E(n),rec),classification=cls,notes=notes))
    if fname: fx.append(dict(name=f'L{n} {short(n)}',formula=fname,inputs=inputs,expected=dict(quantity=E(n),unit=L[n]['unit']),tolerancePct=tol,source=fsrc or f'line {n} / markup p5 (A-130)'))
# ---- flat GWB ceiling
add(278,'markup p5 (A-130) legend "5/8" GWB CEILING O/ 3-5/8" METAL STUD FRAMING (PT3)" (bright green area)',f'{GWB} SQ FT','SF = measured area (net, no waste)',GWB,'measured',
    'Estimator carried 516.0, legend reads 516.1 (rounded down to a whole SF). Same SF feeds PT-3 ceiling paint line 300 (802 = 516 + 286.04).',
    'gypsum-board.ceiling.board-sf',{'areaSF':{'value':GWB,'unit':'SF'},'layers':{'value':1,'unit':'EA'}},0.1)
parent={279:278,280:278,281:278,282:278,283:278,286:285,287:285,288:285,289:285,290:285}
base={278:GWB,285:soffit_sf}
acc={'NO. OF SHEETS':('sheets = SF / 32 (4x8 sheet)',lambda s:s/SHEET,'gypsum-board.sheets',{'sheetSF':{'value':32,'unit':'SF'}}),
     'ADHESIVE':('tubes = SF x 0.031 (about 1 tube per 4x8 sheet)',lambda s:s*ADH,'gypsum-board.adhesive-tubes',{'tubesPerSF':{'value':ADH,'unit':'TUBES/SF'}}),
     'TAPING':('rolls = SF x 0.375 LF/SF / 500 LF per roll = SF x 0.00075',lambda s:s*TAPE,'gypsum-board.tape-rolls',{'tapeLFperSF':{'value':0.375,'unit':'LF/SF'},'rollLF':{'value':500,'unit':'LF'}}),
     'DRYWALL SCREWS':('lb = SF x 0.0375 / 7 (= SF / 186.67)',lambda s:s*SCREW,'gypsum-board.screws-lb',{'lbPerSF':{'value':SCREW,'unit':'LB/SF','basis':'0.0375/7'}}),
     'MUD PLASTER':('lb = SF x 0.53',lambda s:s*MUD,'gypsum-board.compound-lb',{'lbPerSF':{'value':MUD,'unit':'LB/SF'}})}
def derived(n):
    p=parent[n]; key=L[n]['description'].strip()
    form,fn,fname,extra=acc[key]
    rec=fn(base[p]); exact=fn(E(p))
    inp={'boardSF':{'value':E(p),'unit':'SF','from':f'line {p}'}}; inp.update(extra)
    add(n,f'derived from line {p} ({E(p)} SF)',f'parent SF {E(p)} (line {p}); from legend {round(base[p],3)} SF',form,rec,'derived',
        f'Estimator ratio, computed from this job: {E(n)}/{E(p)} = {E(n)/E(p):.7f}; exact on the parent ({exact:.6f}). Same ratio on every 09 gypsum board group (lines 242-277).',
        fname,inp,0.05,f'line {n} / derived from line {p}')
for n in (279,280,281,282,283): derived(n)
add(284,'derived from line 278 (A-130 GWB ceiling area)',f'{GWB} SF (legend); 516.0 SF (line 278)','LF = SF / 1.33 (16" O.C.: SF x 12/16 with 16/12 rounded to 1.33)',GWB/DIV,'derived',
    'Ceiling joists as an area rule: 516/1.33 = 387.969925 exactly. No track, hangers or end members carried. A-130 legend names the system (5/8" GWB over 3-5/8" metal stud framing); A-630 details 1/3/4 show 3-5/8" mtl stud framing @ 16" O.C.',
    'metal-framing.ceiling-joists-area-rule',{'areaSF':{'value':516.0,'unit':'SF','from':'line 278'},'divisor':{'value':1.33,'unit':'FT','basis':'16" O.C. -> 16/12 rounded'}},0.05)
# ---- soffit
sv='; '.join(f'{n.split(", ")[0].replace("SOFFIT ","")}{"/"+n.split(", ")[1] if ", " in n else ""} {lf} FT' for n,lf,fh,bh,f in SOF)
add(285,'markup p5 (A-130) six SOFFIT legend rows (linear)',sv,'SF = Σ LF x board height x faces (BS = both sides = 2 faces; "SOFFIT @ 2\'H" = 2 ft one face); no soffit bottom, no ends',soffit_sf,'derived',
    'With legend LFs rounded to 0.1 ft the result is 286.20 (+0.16 SF); exact 2-decimal LFs that round to the legend reproduce 286.04 exactly (e.g. 4.23, 2.65, 6.73, 30.48, 35.27, 28.06 — the same set that reproduces line 291). Board height is the exposed fascia, not the framing height.',
    'gypsum-board.soffit.board-sf-by-legend-height',{'runs':[{'name':n,'lf':{'value':lf,'unit':'LF'},'boardHeight':{'value':bh,'unit':'FT'},'faces':{'value':f,'unit':'EA'}} for n,lf,fh,bh,f in SOF]},0.5)
for n in (286,287,288,289,290): derived(n)
add(291,'markup p5 (A-130) six SOFFIT rows + two 3-5/8" METAL STUD BRACING rows',sv+'; bracing @48" 5\'H 27.1 FT; @48" 8\'H 28.1 FT',
    'LF = Σ(soffit LF x framing height)/1.33 + Σ(bracing LF / 4 x bracing height)',soffit_studs,'derived',
    f'Soffit framing area {F:.3f} SF / 1.33 = {F/DIV:.3f} LF + bracing (27.1/4x5 + 28.1/4x8) = {brace:.3f} LF. Framing counted once even on BS soffits. 429.599624 x 1.33 = 571.3675; exact 2-decimal LFs reproduce it (e.g. soffits 4.23, 2.65, 6.73, 30.48, 35.27, 28.06 and bracing 27.12, 28.05). Alternative (bracing inside the divisor at 1/3 density) gives {alt_third:.2f} (+{(alt_third/E(291)-1)*100:.2f}%).',
    'metal-framing.soffit-studs-area-rule',{'soffits':[{'name':n,'lf':{'value':lf,'unit':'LF'},'framingHeight':{'value':fh,'unit':'FT'}} for n,lf,fh,bh,f in SOF],
     'bracing':[{'name':n,'lf':{'value':lf,'unit':'LF'},'height':{'value':h,'unit':'FT'},'spacing':{'value':48,'unit':'in'}} for n,lf,h in BR],'divisor':{'value':1.33,'unit':'FT'}},0.5)
# ---- ACT and baffles
add(292,'markup p5 (A-130) legend "AC1 CEILING" (teal area)',f'{AC1} SQ FT','SF = measured area (tile + grid in one line, net, no waste, no attic stock)',AC1,'measured',
    'Legend prints 948.7 (1 decimal); estimator 948.75 (2 decimals of the same PlanSwift value, 948.745-948.749). ACT-1 = USG Mars 88135 24x24x7/8 SLT edge on Donn DX 15/16 grid (A-170).',
    'ceilings.act.area',{'areaSF':{'value':AC1,'unit':'SF'},'module':'2x2','tag':'ACT-1'},0.1)
add(293,'markup p5 (A-130) legend "AC2 CEILING" (magenta area, transaction bar 108)',f'{AC2} SQ FT','SF = measured area (net)',AC2,'measured',
    'Estimate text says 24"x24"x5/8"; A-170 schedule and A-131 note say 24"x48"x5/8" (2x4 Armstrong 1729 Tech Black) on Gordon MT-7/CT-7 grid with WA-2 angle. A-131 note: ACT-2 tile and grid provided by owner vendor, installed by GC.',
    'ceilings.act.area',{'areaSF':{'value':AC2,'unit':'SF'},'module':'2x4','tag':'ACT-2'},0.1)
add(294,'markup p6 (A-131) legend "2"x8" BAFFLE SYSTEM - BAR-1" (yellow lines on detail 5)',f'{BAR} FT; 37 yellow baffle lines (pixel measure 369.2 FT)','LF = Σ length of each baffle run (37 runs @ 8" O.C.)',BAR,'measured',
    '37 runs counted on markup p6; field 24\' wide / 8" O.C. = 36 spaces + 1 = 37 runs; average 10.02 ft per run. Owner-furnished (SEAS .040" aluminium beams, Dark Wood II); GC installs.',
    'ceilings.baffles.rows',{'measuredLF':{'value':BAR,'unit':'LF'},'rows':{'value':37,'unit':'EA'},'rowSpacing':{'value':8,'unit':'in'}},0.1,'line 294 / markup p6 (A-131)')
rows.sort(key=lambda r:r['lineNo'])
assert [r['lineNo'] for r in rows]==IDS
with open(f'{OUT}/reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
fx.sort(key=lambda x:int(x['name'].split()[0][1:]))
json.dump(fx,open(f'{OUT}/fixtures.json','w'),indent=2)
for r in rows: print(r['lineNo'],r['estimatorQty'],r['recomputedQty'],r['deltaPct'],r['classification'])
print('within1',sum(abs(r['deltaPct'])<=1 for r in rows),'fixtures',len(fx))
