import pymupdf, math
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
FT=20/72
for w in (1.44,0.84,0.48):
  print('width',w)
  for i,x in enumerate(p.get_drawings()):
    r=x['rect']
    if r.x0>1950 or not x.get('color') or x['color'][0]>0.1 or abs((x.get('width') or 0)-w)>0.01: continue
    L=sum(math.dist(it[1],it[2]) if it[0]=='l' else (math.dist(it[1],it[4]) if it[0]=='c' else 0) for it in x['items'])*FT
    if L>8: print(' ',i,[round(v) for v in r],len(x['items']),round(L,1))
