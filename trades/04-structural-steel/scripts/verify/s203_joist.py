import pymupdf
d=pymupdf.open('source/drawings/Structural/S-203-Structural-Plan---Roof-Rev.0.pdf');p=d[0]
segs=set()
for dr in p.get_drawings():
    for it in dr['items']:
        if it[0]=='l':
            a,b=it[1],it[2]
            if abs(a.x-b.x)<0.5 and abs(a.y-b.y)>150:
                y0,y1=sorted([a.y,b.y])
                segs.add((round(a.x,1),round(y0,1),round(y1,1),round(dr.get('width') or 0,2),str(dr.get('dashes')),str(dr.get('color'))))
for s in sorted(segs):
    if 1215<s[0]<2050 and 450<s[1]<1400: print(s,'ft',round((s[2]-s[1])/18,2))
