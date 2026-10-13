import pymupdf, math, collections
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
FT=20/72
for target in (1.2,1.0):
    mids=[]
    for x in p.get_drawings():
        if not x.get('color') or x['color'][0]>0.1 or abs((x.get('width') or 0)-0.72)>0.01: continue
        for it in x['items']:
            if it[0]=='l':
                L=math.dist(it[1],it[2])*FT
                m=((it[1].x+it[2].x)/2,(it[1].y+it[2].y)/2)
                if m[0]<1950 and abs(L-target)<0.05: mids.append(m)
    mids=list(set((round(a,1),round(b,1)) for a,b in mids))
    n=len(mids)
    nn=sorted(min(math.dist(mids[i],mids[j]) for j in range(n) if j!=i) for i in range(n))
    print(target,n,'nn median pt',nn[n//2], 'q10',nn[n//10],'q90',nn[9*n//10])
    xs=[m[0] for m in mids]; ys=[m[1] for m in mids]; print(min(xs),max(xs),min(ys),max(ys))
