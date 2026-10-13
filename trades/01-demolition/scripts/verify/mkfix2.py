import json
P='/home/user/takeoffspeed-reference-data/trades/01-demolition/fixtures.json'
F=json.load(open(P))
keys={'KN1 curb & gutter removal':(2,'curb:CURB & GUTTER'),
'KN2 two-storey building removal volume':(3,'building:2:44891/10:20'),
'KN2 one-storey building removal volume':(4,'building:1:17137/10:10'),
'KN9 sidewalk removal':(5,'remove:SIDEWALK'),
'KN10 monument sign removal':(6,'feature:MONUMENT SIGN:'),
'KN7 asphalt pavement removal incl. striping':(9,'remove:PAVEMENT'),
'KN8 tree removal (unsized)':(10,'tree:unsized'),
'KN6 water line removal':(11,'utility:remove:WATER'),
'KN5 power/telecom line removal':(12,'utility:remove:POWER'),
'Metal handrail removal':(13,'linear:METAL HANDRAIL:')}
new=[]
for f in F:
    if f['assembly']=='demolition.building':
        f['inputs']={'keynote':'2',**f['inputs']}
        f['engineInputs']={'keynote':'2',**f['engineInputs']}
    if 'expectedLines' not in f:
        ln,k=keys[f['name']]
        f['expectedLines']=[{'line':ln,'key':k,'quantity':f['expected']['quantity'],'unit':f['expected']['unit'] if f['expected']['unit']!='CF' else 'CF','tolerancePct':f['tolerancePct'],'estimatorQty':f['estimatorQty']}]
    # order keys
    order=['name','assembly','formula','inputs','engineInputs','expected','expectedLines','tolerancePct','source','estimatorQty']
    new.append({k:f[k] for k in order if k in f} | {k:v for k,v in f.items() if k not in order})
json.dump(new,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
