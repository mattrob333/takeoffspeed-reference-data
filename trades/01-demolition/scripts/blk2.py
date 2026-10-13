import pymupdf, math
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
FT=20/72
tot=0
for i,x in enumerate(p.get_drawings()):
    r=x['rect']
    if r.x0>1950 or not x.get('color') or x['color'][0]>0.1 or abs((x.get('width') or 0)-0.72)>0.01: continue
    L=sum(math.dist(it[1],it[2]) if it[0]=='l' else (math.dist(it[1],it[4]) if it[0]=='c' else 0) for it in x['items'])*FT
    if L>15 and len(x['items'])>1: print(i,[round(v) for v in r],len(x['items']),[it[0] for it in x['items']][:3],round(L,1)); tot+=L
print(tot)
