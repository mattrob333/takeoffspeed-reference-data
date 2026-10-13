import pymupdf
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
D=p.get_drawings()
for i in (5685,4082,4083,1290,1291):
    x=D[i]; print(i,x['type'],x.get('color'),round(x.get('width') or 0,2),x['rect'])
    q=[]
    for it in x['items']:
        if not q: q.append((round(it[1].x,1),round(it[1].y,1)))
        q.append((round(it[-1].x,1),round(it[-1].y,1)))
    print('  ',q)
