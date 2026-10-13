import pymupdf,collections,sys
d=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Architectural/A-410-ENLARGED-RESTROOM-PLANS-&-ELEVATIONS-Rev.0.pdf'); p=d[0]
FT=36.0
regions={'B':(580.5,850.8),'C':(1037.0,1313.3),'D':(1518.0,1794.3)}
y0,y1=372.0,571.5
acc=collections.defaultdict(float)
for g in p.get_drawings():
    f=g.get('fill')
    if not f: continue
    R=g['rect']
    if R.y0<y0-1 or R.y1>y1+1: continue
    for k,(a,b) in regions.items():
        if R.x0>=a-1 and R.x1<=b+1:
            # area of path approximated by rect if items are rects/quads; else use rect
            area=0
            for it in g['items']:
                if it[0]=='re': area+=it[1].width*it[1].height
                elif it[0]=='qu': area+=it[1].rect.width*it[1].rect.height
            if area==0: area=R.width*R.height
            acc[(k,tuple(round(c,2) for c in f))]+=area/FT/FT
for k,v in sorted(acc.items()): print(k,round(v,2))
