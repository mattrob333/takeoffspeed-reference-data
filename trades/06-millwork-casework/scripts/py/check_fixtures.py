import json
F=json.load(open('/home/user/takeoffspeed-reference-data/trades/06-millwork-casework/fixtures.json'))
def ev(f):
    i=f['inputs']; fm=f['formula']; g=lambda k: i[k]['value']
    if fm=='count': return g('count')
    if fm.startswith('cabinet_lf'): return sum(g('runs') if 'runs' in i else g('modules'))
    if fm.startswith('shelf_lf'): return sum(g('runs'))*g('shelves')
    if fm=='laminate_face_sf = W x H': return sum(a*b for a,b in g('faces'))
    if fm.startswith('laminate_face_sf') or fm.startswith('countertop_sf = sum(areas)'): return sum(g('areas'))
    if fm=='countertop_sf = sum(runs) x depth': return sum(g('runs'))*g('depth')
    if fm.startswith('countertop_sf = sum(runs) x depth + stub'): a,b=g('stub'); return sum(g('runs'))*g('depth')+a*b
    if fm.startswith('backsplash'): return sum(g('backsplash'))
    if fm.startswith('apron'): return sum(g('apronRuns'))
    if fm=='paneling_sf = sum(W x H)': return sum(a*b for a,b in g('faces'))
    if fm=='paneling_sf = W x L': return sum(g('areas'))
    if fm.startswith('reveal'): return sum(g('reveals'))
    raise Exception(fm)
bad=0
for f in F:
    v=ev(f); e=f['expected']['quantity']; d=(v-e)/e*100
    if abs(d)>f['tolerancePct']: bad+=1; print('FAIL',f['name'],v,e,round(d,2))
print('fixtures',len(F),'fail',bad)
