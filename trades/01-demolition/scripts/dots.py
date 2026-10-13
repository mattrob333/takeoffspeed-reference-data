import pymupdf, math, collections
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
FT=20/72
pts=set()
for x in p.get_drawings():
    if not x.get('color') or x['color'][0]>0.1: continue
    for it in x['items']:
        if it[0]=='l' and math.dist(it[1],it[2])<0.05 and it[1].x<1950:
            pts.add((round(it[1].x,2),round(it[1].y,2)))
pts=sorted(pts); print(len(pts))
ys=collections.Counter(round(p_[1],1) for p_ in pts); xs=collections.Counter(round(p_[0],1) for p_ in pts)
yl=sorted(ys); xl=sorted(xs)
dy=collections.Counter(round(yl[i+1]-yl[i],2) for i in range(len(yl)-1)); dx=collections.Counter(round(xl[i+1]-xl[i],2) for i in range(len(xl)-1))
print('dy',dy.most_common(5)); print('dx',dx.most_common(5))
print('bbox',min(p_[0] for p_ in pts),max(p_[0] for p_ in pts),min(p_[1] for p_ in pts),max(p_[1] for p_ in pts))
rows=collections.defaultdict(list)
for x_,y_ in pts: rows[round(y_,1)].append(x_)
d=collections.Counter()
for y_,r in rows.items():
    r.sort()
    for i in range(len(r)-1): d[round(r[i+1]-r[i],2)]+=1
print('in-row dx',d.most_common(6))
yl=sorted(rows); print('row pitch mean',(yl[-1]-yl[0])/(len(yl)-1), len(yl))
