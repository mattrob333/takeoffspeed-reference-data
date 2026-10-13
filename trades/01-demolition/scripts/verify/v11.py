import pymupdf, math
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
D=p.get_drawings(); FT=20/72
x=D[5685]
prev=None
for it in x['items']:
    print(it[0], [(round(q.x,2),round(q.y,2)) for q in it[1:]], 'gap' if prev and math.dist(prev,(it[1].x,it[1].y))>0.01 else '')
    prev=(it[-1].x,it[-1].y)
