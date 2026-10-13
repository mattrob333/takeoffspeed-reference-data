import json
# legend values (independently read from legends.json above)
p16={'WT1':120.7,'WT2':43.8,'WT9':50.6}
p27={'WT1':15.3,'WT2':1.4,'WT9':1.3}
p32={'WT1':8.2,'WT2':1.6,'WT9':1.3}
p23={'WT3':38.4}
est={235:144.19,236:46.72,237:38.42,238:53.22,239:120.0,240:103.0,241:16.0}
rec={}
rec[235]=p16['WT1']+p27['WT1']+p32['WT1']
rec[236]=p16['WT2']+p27['WT2']+p32['WT2']
rec[238]=p16['WT9']+p27['WT9']+p32['WT9']
rec[237]=p23['WT3']
rec[239]=10.1*12
rec[240]=10.3*10
rec[241]=4.0*4
for k in sorted(rec):
    d=(rec[k]-est[k])/est[k]*100
    print(k, 'est',est[k],'rec',round(rec[k],4),'delta%%', round(d,4), 'within1' if abs(d)<=1 else 'OUT', repr(d))
# band checks
bandA410=2*(7.5083+7.675+4.0056+0.3333)*5.5
print('A410 band',bandA410, 'legend sum',sum(p16.values()), (sum(p16.values())-bandA410)/bandA410*100)
print('A703 band',6.75*(32/12), 'legend',sum(p27.values()))
print('A705 band',(2+4/12)*3+2/12, ((2+4/12)*3+2/12)*(1+6.5/12),'legend',sum(p32.values()))
print('A700',(10+4.375/12)*(3+8.5/12))
blend=est[235]+est[236]+est[238]
print('blend',blend,[round(blend*m,2) for m in (.6,.2,.2)],[round((blend*m-e)/e*100,2) for m,e in ((.6,144.19),(.2,46.72),(.2,53.22))])
print('shares job',[round(x/blend*100,1) for x in (144.19,46.72,53.22)])
print('restroom shares',[round(x/sum(p16.values())*100,1) for x in p16.values()])
print('A703 shares',[round(x/sum(p27.values())*100,1) for x in p27.values()])
print('A705 shares',[round(x/sum(p32.values())*100,1) for x in p32.values()])
print('A700 sheet 67.5?', 38.4+18.0+11.1, (38.4+18.0+11.1)/(blend+38.42)*100)
print('topedge', 2*(7.5083+7.675+4.0056+0.3333), (2*(7.5083+7.675+4.0056+0.3333)-39.55)/39.55*100)
# fixtures
F=json.load(open('/home/user/takeoffspeed-reference-data/trades/09d-wall-finishes/fixtures.json'))
for f in F:
    i=f['inputs']; q=None
    if 'areas_sf' in i: q=sum(i['areas_sf'].values())
    elif 'blend_sf' in i: q=i['blend_sf']*i['mix']['WT-1']
    elif 'walls_ft' in i: q=sum(i['walls_ft'])*i['height_ft']*i.get('roomRepeat',1)
    elif 'run_lf' in i: q=i['run_lf']*i['height_ft']
    e=f['expected']['quantity']; d=abs(q-e)/e*100
    print('FIXTURE',f['name'][:60],'computed',round(q,4),'expected',e,'delta%%', round(d,6),'tol',f['tolerancePct'], 'PASS' if d<=f['tolerancePct'] else 'FAIL', 'strictFAIL' if d>=f['tolerancePct'] else '')
