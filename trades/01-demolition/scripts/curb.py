import pymupdf, math, collections, json
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
FT=20/72
c=collections.Counter(); mids=[]
for x in p.get_drawings():
    if not x.get('color') or x['color'][0]>0.1 or abs((x.get('width') or 0)-0.72)>0.01: continue
    for it in x['items']:
        if it[0]=='l':
            L=math.dist(it[1],it[2])*FT
            m=((it[1].x+it[2].x)/2,(it[1].y+it[2].y)/2)
            if m[0]>1950: continue
            c[round(L,1)]+=1
            if 2.0<L<3.0: mids.append(m)
print(sorted(c.items(),key=lambda kv:-kv[1])[:15])
print(len(mids))
json.dump(mids,open('curbticks.json','w'))
