import pymupdf, math, collections
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
D=p.get_drawings(); FT=20/72
n=0
for i,x in enumerate(D):
    col=x.get('color'); w=x.get('width') or 0
    if x['type']!='s' or not col or max(col)>0.1 or abs(w-0.72)>0.01: continue
    r=x['rect']
    if 1000<r.x0<1040 and 1300<r.y0<1340:
        print(i, [(it[0],[(round(q.x,2),round(q.y,2)) for q in it[1:]]) for it in x['items']][:6], len(x['items']))
        n+=1
    if n>40: break
