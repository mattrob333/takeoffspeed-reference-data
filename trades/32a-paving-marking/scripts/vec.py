import pymupdf, math, collections, sys
p = pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-3.0-SITE-PLAN-Rev.0.pdf')[0]
FT_PER_PT = 20/72.0  # 1"=20'
dr = p.get_drawings()
print('paths', len(dr))
segs=[]
for d in dr:
    w = d.get('width') or 0
    for it in d['items']:
        if it[0]=='l':
            a,b=it[1],it[2]
            L=math.hypot(b.x-a.x,b.y-a.y)*FT_PER_PT
            segs.append((round(w,2),L,a,b,d.get('color'),d.get('dashes')))
cnt=collections.Counter((s[0]) for s in segs)
print(cnt.most_common(20))
# segments ~18 ft
for tgt in (18,):
    hits=[s for s in segs if abs(s[1]-tgt)<0.3]
    print(tgt, len(hits), collections.Counter((s[0],s[4]) for s in hits))
    for s in hits: print(round(s[1],2), s[0], round(s[2].x/p.rect.width,3), round(s[2].y/p.rect.height,3), round(s[3].x/p.rect.width,3), round(s[3].y/p.rect.height,3))
print('---- all 0.72 black segments > 2 ft in site window')
W,H=p.rect.width,p.rect.height
tot=0
rows=[]
for s in segs:
    if s[0]==0.72 and s[4]==(0.0,0.0,0.0) and s[1]>2:
        x0,y0=s[2].x/W,s[2].y/H
        if 0.2<x0<0.65 and 0.3<y0<0.75:
            rows.append((round(x0,3),round(y0,3),round(s[3].x/W,3),round(s[3].y/H,3),round(s[1],2),s[5]))
rows.sort()
for r in rows: print(r)
print('n',len(rows),'sum',round(sum(r[4] for r in rows),2))
