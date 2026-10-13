import json, csv, re, math
R='/home/user/takeoffspeed-reference-data'
OUT=R+'/trades/11-equipment-furnishings'
L={x['lineNo']:x for x in json.load(open(R+'/reference/estimate/lines.json'))}
T=[x for x in json.load(open(R+'/reference/estimate/trades.json')) if x['trade']=='11-equipment-furnishings'][0]['lines']
leg={}
for g in json.load(open(R+'/reference/markups/legends.json')):
    for i in g['items']: leg[(g['page'],i['name'])]=(i['quantity'],i['unit'])
def tagof(d):
    m=re.search(r'- ?([A-Z]{2}-?\d{2}[A-Z]?)\b',d.split('\n')[0]); return m.group(1) if m else None
# shade run decomposition (pixels on markup p5 raster, 49.99 px/ft at 1/4"=1'-0")
PXFT=7199/36*0.25
segs=[('Employee Lounge 109, east storefront',303,10.0),('Transaction Bar 108, east storefront',301,11.0),
      ('Relaxed Seating 102, east storefront',668,12.0),('Relaxed Seating 102, south storefront',698,12.0),
      ('Entry 101, south storefront',656,12.0),('Weather Vestibule 100, west storefront',361,12.0),
      ('Booth 104, west storefront',403,12.0),('Meeting Room 105, west storefront',298,10.0)]
seg_ft=[(n,round(p/PXFT,2),h) for n,p,h in segs]
seg_total=sum(f for _,f,_ in seg_ft)
ceil_sf=sum(f*h for _,f,h in seg_ft)
SHADE_LF_LEGEND=74.0; DROP=16.0
placed={}  # A-160 legend p9
for (pg,name),(q,u) in leg.items():
    if pg==9: placed[name.replace('?','')]=q
rows=[];fx=[]
def pct(a,b): return round((a-b)/b*100,3) if b else 0.0
for n in T:
    x=L[n]; d=x['description']; first=d.split('\n')[0].strip(); q=x['quantity']; u=x['unit']
    tag=tagof(d); short=first[:70]
    if n==337:
        r=dict(source='A-170 Appliance Schedule row AE-01 (green-highlighted, PROV BY GC / INST BY GC); no A-160 placement (A-160 legend has no AE01)',sv='schedule row present, plan count 0, no QTY column',
               formula='scheduled GC-provided appliance not placed on plan -> 1 EA',rq=1.0,cls='specified',notes='Microwave drawer sits in Employee Lounge millwork (A-705 shows only AE-02 MICROWAVE); estimator carried 1 EA from schedule')
        fx.append(dict(name='AE-01 microwave drawer scheduled, not placed',formula='scheduled-unplaced-count',inputs={'scheduleRow':'AE-01','planCount_EA':0,'providedBy':'GC','installedBy':'GC'},expected={'quantity':1,'unit':'EA'},tolerancePct=0,source='337 / A-170 (markup p10)'))
    elif n in (338,339,340,341,342):
        t=tag.replace('-',''); lq=placed[t]
        r=dict(source=f'Markup p9 (A-160) legend row {t}',sv=f'{t} = {lq} EA',formula='count of tag placements',rq=lq,cls='counted',
               notes='A-170 row green-highlighted; '+('PROV BY VENDOR / INST BY GC (AE-07)' if n==342 else 'PROV BY GC / INST BY GC'))
        fx.append(dict(name=f'{tag} appliance count',formula='tag-count',inputs={'placements_EA':[lq]},expected={'quantity':q,'unit':'EA'},tolerancePct=0,source=f'{n} / markup p9'))
    elif n==343:
        lq=leg[(3,'REMOTE TELLER TERMINAL')][0]
        r=dict(source='Markup p3 (A-110) legend row REMOTE TELLER TERMINAL; keynote P9',sv=f'{lq} EA',formula='count of keynote P9 symbols',rq=lq,cls='counted',notes='A-200/A-201 say REMOTE TELLER TERMINAL BY BANK VENDOR; estimator still carries it 1 EA (install/coordination)')
        fx.append(dict(name='Remote teller terminal count',formula='tag-count',inputs={'placements_EA':[lq]},expected={'quantity':q,'unit':'EA'},tolerancePct=0,source='343 / markup p3'))
    elif n==345:
        rq=round(SHADE_LF_LEGEND*DROP,2)
        r=dict(source='Markup p5 (A-130) legend row MOTORIZED MECHOSHADE (red run along interior face of storefront); A-170 Finishes Schedule MECHO; spec 12 2413',
               sv=f'run LF = 74.0 FT (legend, displayed to 0.1); 8 runs rebuilt from the markup raster = {seg_total:.2f} LF; drop 16 ft (estimator)',
               formula='SF = run LF x 16 ft drop; description LF = ceil(run LF)',rq=rq,cls='derived',
               notes=f'1184.4/74.0 = {1184.4/74:.4f}; exact if hidden LF = 74.025. 16 ft is not on any drawing (storefront head 12\'-0", ceilings 10\'-12\'); ceiling-height drop would give {ceil_sf:.1f} SF. Description (75 LF) = ceil(74.025)')
        fx.append(dict(name='Motorized MechoShade SF from run LF x estimator drop',formula='shade-sf-run-x-drop',inputs={'runLF_ft':74.025,'drop_ft':16},expected={'quantity':1184.4,'unit':'SF'},tolerancePct=0.1,source='345 / markup p5'))
        fx.append(dict(name='Motorized MechoShade SF from legend LF (display precision)',formula='shade-sf-run-x-drop',inputs={'runLF_ft':74.0,'drop_ft':16},expected={'quantity':1184.4,'unit':'SF'},tolerancePct=0.5,source='345 / markup p5'))
        fx.append(dict(name='MechoShade description LF rounding',formula='ceil',inputs={'runLF_ft':74.025},expected={'quantity':75,'unit':'LF'},tolerancePct=0,source='345 description "(75 LF)"'))
    else:
        t=tag.replace('-','')
        base=re.sub(r'[AB]$','',t) if t.startswith('SS03') else t
        if base in placed:
            lq=placed[base]
            extra=' (plan tag SS-03 carries no suffix; estimator carried SS-03A and SS-03B 1 EA each)' if base!=t else ''
            r=dict(source=f'Markup p9 (A-160) legend row {base if base!="ST02" else "ST02?"}',sv=f'{base} = {lq} EA',formula='count of tag placements',rq=lq,cls='counted',notes='OFCI per A-110 General Note K'+extra)
            fx.append(dict(name=f'{tag} furniture count',formula='tag-count',inputs={'placements_EA':[lq]},expected={'quantity':q,'unit':'EA'},tolerancePct=0,source=f'{n} / markup p9'))
        else:
            plan_note=' TB-05B IS tagged once on A-160 (text layer) but was not marked in the PlanSwift legend; plan count 1 = convention 1.' if tag=='TB-05B' else ''
            r=dict(source=f'A-170 Furniture Schedule row {tag}; no A-160 legend row',sv='schedule row present, plan placements 0 (per markup)',
                   formula='scheduled furniture tag not placed -> 1 EA (V.I.F.)',rq=1.0,cls='specified',notes='Estimator convention stated in section note: NOT FOUND ON PLANS ... ASSUMED 1 EA, PLEASE V.I.F.'+plan_note)
            fx.append(dict(name=f'{tag} scheduled-only furniture',formula='scheduled-unplaced-count',inputs={'scheduleRow':tag,'planCount_EA':0,'unplacedConvention_EA':1},expected={'quantity':q,'unit':'EA'},tolerancePct=0,source=f'{n} / A-170 (markup p10)'))
    rows.append([n,short,u,q,r['source'],r['sv'],r['formula'],r['rq'],pct(r['rq'],q),r['cls'],r['notes']])
with open(OUT+'/reconciliation.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['lineNo','description','unit','estimatorQty','source','sourceValues','formula','recomputedQty','deltaPct','classification','notes']); w.writerows(rows)
json.dump(fx,open(OUT+'/fixtures.json','w'),indent=1)
import collections
print(len(rows), collections.Counter(r[9] for r in rows), sum(1 for r in rows if abs(r[8])<=1), sum(1 for r in rows if abs(r[8])<=5), len(fx))
for r in rows:
    if r[8]!=0: print(r[0],r[3],r[7],r[8])
print('segments',seg_ft,round(seg_total,3),'ceilSF',round(ceil_sf,1),'1184.4/16=',1184.4/16, 'pct legend vs seg', pct(seg_total,74.0))
