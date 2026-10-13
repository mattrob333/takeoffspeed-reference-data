import pymupdf, math, sys
p = pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-3.0-SITE-PLAN-Rev.0.pdf')[0]
F=20/72.0; W,H=p.rect.width,p.rect.height
x0,y0,x1,y1=map(float,sys.argv[1:5])
minL=float(sys.argv[5]) if len(sys.argv)>5 else 1
for d in p.get_drawings():
    for it in d['items']:
        if it[0]!='l': continue
        a,b=it[1],it[2]
        if x0<=a.x/W<=x1 and y0<=a.y/H<=y1 and x0<=b.x/W<=x1 and y0<=b.y/H<=y1:
            L=math.hypot(b.x-a.x,b.y-a.y)*F
            if L>=minL: print(round(a.x/W,4),round(a.y/H,4),round(b.x/W,4),round(b.y/H,4),'L=%.2f'%L,'w',d.get('width'),'c',d.get('color'),'fill',d.get('fill'))
