import pymupdf
p=pymupdf.open('source/drawings/Structural/S-201-Structural-Plan---Foundation-Rev.0.pdf')[0]
W,H=p.rect.width,p.rect.height
x0,y0,x1,y1=0.42*W,0.015*H,0.78*W,0.30*H
hs=set();vs=set()
for dr in p.get_drawings():
    for it in dr['items']:
        if it[0]=='l':
            a,b=it[1],it[2]
            if not (x0<a.x<x1 and y0<a.y<y1): continue
            if abs(a.y-b.y)<0.3 and abs(a.x-b.x)>500: hs.add(round(a.y,1))
            if abs(a.x-b.x)<0.3 and abs(a.y-b.y)>80 and (dr.get('width') or 0)>1: vs.add((round(a.x,1),round(min(a.y,b.y),1),round(max(a.y,b.y),1),dr.get('width')))
print('H lines',sorted(hs))
for v in sorted(vs): print('bar',v)
for w in p.get_text('words'):
    if x0<w[0]<x1 and y0<w[1]<y1 and (w[4][0] in 'ABCDE' and '-' in w[4] or w[4] in ("0'","13'","16'","Roof","Level")): print([round(c,1) for c in w[:4]],w[4])
