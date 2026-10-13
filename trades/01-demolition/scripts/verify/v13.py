import pymupdf, math
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
D=p.get_drawings(); FT=20/72
for i,x in enumerate(D):
    r=x['rect']
    if r.x1<1140 or r.x0>1200 or r.y1<935 or r.y0>980: continue
    if x['type']!='s': continue
    segs=[(round(it[1].x,1),round(it[1].y,1),round(it[2].x,1),round(it[2].y,1)) for it in x['items'] if it[0]=='l']
    print(i, x.get('color'), round(x.get('width') or 0,2), segs[:8], len(segs))
