import pymupdf, math, collections
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
D=p.get_drawings()
for i in range(11110,11135):
    x=D[i]; 
    print(i, x['type'], x.get('color'), x.get('fill'), round(x.get('width') or 0,2), [ (it[0], [ (round(q.x,1),round(q.y,1)) for q in it[1:] if hasattr(q,'x')]) for it in x['items']][:4], x['rect'])
ws=[w for w in p.get_text('words') if w[4]=='///']
print([ (round(w[0],1),round(w[1],1),round(w[2],1),round(w[3],1)) for w in ws if 690<w[0]<900 and 870<w[1]<1000])
