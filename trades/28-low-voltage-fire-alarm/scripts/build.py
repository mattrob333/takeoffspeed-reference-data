import json, csv, math
ROOT='/home/user/takeoffspeed-reference-data/'
OUT=ROOT+'trades/28-low-voltage-fire-alarm/'
L={l['lineNo']:l for l in json.load(open(ROOT+'reference/estimate/lines.json'))}
T=[t for t in json.load(open(ROOT+'reference/estimate/trades.json')) if t['trade']=='28-low-voltage-fire-alarm'][0]['lines']
leg={pg['page']:pg for pg in json.load(open(ROOT+'reference/markups/legends.json'))}
p47={it['name']:it for it in leg[47]['items']}
p48=leg[48]['items']
tags=json.load(open('/home/user/work/28-low-voltage-fire-alarm/tag_counts.json'))
# E-160 symbol counts read from the drawing (symbol shapes per E-001 legend), cross-checked by text layer F=11 (9 HS + 2 PS) and GPT-6 Astra
fa_plan={'FACP':1,'FAA':1,'SMOKE':1,'PULL':2,'HS':9,'V':3}
# p48 legend: the 9.0 EA purple row is missing from legends.json (duplicate truncated name); read from the markup image legend
p48_rows={'PULL':('FIRE ALARM PULL S...',2,'slate blue'),'HS':('FIRE ALARM ADA AP... (purple)',9,'purple'),'FAA':('FIRE ALARM ANNUC...',1,'teal'),
          'FACP':('FIRE ALARM CONTR...',1,'red'),'SMOKE':('FIRE ALARM SMOKE...',1,'green'),'V':('FIRE ALARM ADA AP... (yellow)',3,'yellow'),'ALW':('ALLOWANCE FOR W...',1,'blue')}
for k in ('PULL','FAA','FACP','SMOKE','V','ALW'):
    nm=p48_rows[k][0].split(' (')[0]
    assert any(i['name']==nm and i['quantity']==p48_rows[k][1] for i in p48), k
assert not any(i['quantity']==9 for i in p48)   # confirms the dropped row
SEC={603:'LIGHT'}
rows=[]; fixtures=[]
def pct(e,r): return round((r-e)/e*100,2)
for n in T:
    l=L[n]; e=l['quantity']; desc=l['description'].replace('\n',' / ')
    if l['keynote'] is not None:   # security device by schedule number, E-150 / markup p47
        k=str(l['keynote']); leg_q=p47[k]['quantity']; plan=tags[k]
        sec=l['section']
        cam = k in ('3','14','16','17')
        formula='count(tag) — security-device by schedule number' + (' (camera)' if cam else '')
        src=f"markup p47 (E-150) legend row '{k}' ({p47[k]['color']})"
        sv=f"legend {leg_q} EA; plan tags main {plan['main']} + drive-thru {plan['driveThru']} = {plan['total']}"
        rec=leg_q
        note=f"E-150 SECURITY DEVICE SCHEDULE #{k}; section {sec}"
        if plan['total']!=e:
            note+=f"; PLAN SHOWS {plan['total']} tags (main {plan['main']} incl. teller-line AI/18 under transaction bar + drive-thru {plan['driveThru']}); estimator dotted {leg_q} — teller-line AI not dotted on p47 ({pct(e,plan['total'])}% vs plan)"
        if plan['driveThru']: note+=f"; {plan['driveThru']} in view 2 SECURITY PLAN REMOTE DRIVE THRU"
        rows.append([n,desc,l['unit'],e,src,sv,'Qty = Σ tag bubbles dotted on the security plan (both views)',rec,pct(e,rec),'counted',note])
        fixtures.append({'name':f"L{n} security #{k} {l['description'].split(': ',1)[1]}",'formula':'low-voltage.camera' if cam else 'low-voltage.security-device',
            'inputs':{'tag':k,'description':l['description'].split(': ',1)[1],'section':sec,'count':{'value':[plan['main'],plan['driveThru']] if plan['driveThru'] and plan['total']==e else [leg_q],'unit':'EA','perSheet':'E-150 view 1, view 2' if plan['driveThru'] and plan['total']==e else 'E-150 (as dotted on markup p47)'}},
            'expected':{'quantity':e,'unit':'EA','item':l['description']},'tolerancePct':0,'source':f"line {n} / markup p47 legend '{k}'"+(' — plan shows 3, estimator 2' if plan['total']!=e else '')})
    else:
        d=l['description']
        if 'ALLOWANCE' in d:
            area_tb=1900; slab=1917.6
            basis=math.ceil(area_tb/1000)*1000
            rows.append([n,'ALLOWANCE FOR WIRE, CABLE & CONDUIT FITTINGS / AREA: 2000 SF','LS',e,"markup p48 (E-160) legend 'ALLOWANCE FOR W...' (blue dot on sheet note 3/4)",
              f"legend 1 EA; title block 1,900 SF; slab legend p33 1917.6 SF; area basis printed 2000 SF = ceil(1900/1000)×1000 = {basis}",
              '1 LS per system; area printed = gross SF rounded up to 1,000 SF',1,pct(e,1),'allowance',
              'Quantity is a 1 LS marker; covers FA wire/cable/conduit/fittings (none measured — no FA or security cable LF line in DIV 28). Same 2000 SF basis on DIV 22 (403), DIV 23 (445), DIV 26 (510). Area rounding is estimator convention (judgment).'])
            fixtures.append({'name':f'L{n} DIV 28 wire/cable/conduit allowance','formula':'low-voltage.allowance','inputs':{'area':{'value':1900,'unit':'SF','source':'E-160 title block 1,900 SF'},'areaRoundUpTo':{'value':1000,'unit':'SF','note':'estimator convention (proposed)'}},
                'expected':{'quantity':1,'unit':'LS','item':'ALLOWANCE PROVIDED FOR WIRE, CABLE & CONDUIT FITTINGS / AREA: 2000 SF'},'tolerancePct':0,'source':f'line {n} / markup p48'})
            continue
        key={'FIRE ALARM CONTROL PANEL':'FACP','FIRE ALARM ANNUCIATOR':'FAA','FIRE ALARM SMOKE DETECTOR':'SMOKE','FIRE ALARM PULL STATION':'PULL',
             'FIRE ALARM ADA APPROVED HORN/STROBE ALARM':'HS','FIRE ALARM ADA APPROVED VISUAL ALARM':'V'}[d]
        name,q,col=p48_rows[key]; plan=fa_plan[key]
        sym={'FACP':'boxed FACP','FAA':'boxed FAA','SMOKE':'circled D (ceiling)','PULL':'boxed F, no triangle','HS':'boxed F + triangle','V':'triangle with V'}[key]
        note={'FACP':'E-001 legend FACP; also drawn on E-702 IT-room elevation (not re-counted)',
              'FAA':'at main entry vestibule, beside a horn/strobe',
              'SMOKE':'IT room, next to FACP — spec 28 7210 §2.2.F requires a ceiling smoke detector within 5 ft of the FACP',
              'PULL':'one at east exit beside a horn/strobe (double F box), one MOUNTED ON MULLION at entry',
              'HS':'legends.json OMITS this 9.0 EA purple row (duplicate truncated name FIRE ALARM ADA AP...); read from p48 image. Text layer F=11 = 9 HS + 2 PS. 110 cd per E-160 note 6',
              'V':'two restrooms + one in the shower/locker alcove; 110 cd per E-160 note 6'}[key]
        sec=l['section']
        fam={'FACP':'low-voltage.fa-panel','FAA':'low-voltage.fa-panel'}.get(key,'low-voltage.fa-device')
        rows.append([n,d,l['unit'],e,f"markup p48 (E-160) legend '{name.split(' (')[0]}' ({col})",f"legend {q} EA; plan symbols {plan} ({sym})",'Qty = Σ symbols of the type on the FA plan',q,pct(e,q),'counted',note])
        inp={'description':d.replace('FIRE ALARM ','',1) if fam=='low-voltage.fa-device' else d,'count':{'value':[plan],'unit':'EA','perSheet':'E-160'}}
        if fam=='low-voltage.fa-device':
            inp['deviceType']={'SMOKE':'smoke-detector','PULL':'pull-station','HS':'horn-strobe','V':'strobe'}[key]
        fixtures.append({'name':f'L{n} {d}','formula':fam,'inputs':inp,'expected':{'quantity':e,'unit':'EA','item':d},'tolerancePct':0,'source':f"line {n} / markup p48 legend '{name}'"})
hdr=['lineNo','description','unit','estimatorQty','source','sourceValues','formula','recomputedQty','deltaPct','classification','notes']
with open(OUT+'reconciliation.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(hdr); w.writerows(rows)
json.dump(fixtures,open(OUT+'fixtures.json','w'),indent=2)
print(len(rows),len(fixtures), sum(1 for r in rows if abs(r[8])<=1), sum(1 for r in rows if abs(r[8])<=5))
# app-gap numbers
print('coverage smoke ceil(1900/900)=',math.ceil(1900/900))
doors=5
print('access-door: readers',doors,'strikes',doors,'vs 4 ->',pct(4,doors),'%; contacts',doors,'vs 2 ->',pct(2,doors),'%; REX',doors,'; PS purchase',math.ceil(doors/4),'; controllers',math.ceil(doors/2))
print('backboxes from fa-device', 9+3+2+1, 'bases',1)
print('tag18 plan vs est', pct(2,3))
print('FA devices total', 1+1+1+2+9+3, 'security devices total', sum(L[n]['quantity'] for n in T if L[n]['keynote']))
