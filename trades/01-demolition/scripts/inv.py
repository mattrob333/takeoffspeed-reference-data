import pymupdf, math, collections
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
FT=20/72
agg=collections.defaultdict(lambda:[0,0.0,0])
for x in p.get_drawings():
    r=x['rect']
    if r.x0>1950: continue
    col=tuple(round(c,2) for c in x['color']) if x.get('color') else None
    key=(col, round(x.get('width') or 0,2), x.get('dashes'), x.get('fill') is not None)
    L=0
    for it in x['items']:
        if it[0]=='l': L+=math.dist(it[1],it[2])
        elif it[0]=='c': L+=math.dist(it[1],it[4])
    a=agg[key]; a[0]+=1; a[1]+=L*FT; 
for k,v in sorted(agg.items(), key=lambda kv:-kv[1][1])[:40]: print(v[0], round(v[1],1), k)
