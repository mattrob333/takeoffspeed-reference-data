import pymupdf, math
src=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')
p=src[0]
FT=20/72
doc=pymupdf.open(); pg=doc.new_page(width=2592,height=1728)
pg.show_pdf_page(pg.rect, src, 0)
sh=pg.new_shape()
for x in p.get_drawings():
    if not x.get('color') or x['color'][0]>0.1 or abs((x.get('width') or 0)-0.72)>0.01: continue
    for it in x['items']:
        if it[0]=='l':
            L=math.dist(it[1],it[2])*FT
            if abs(L-1.2)<0.05: sh.draw_line(it[1],it[2]); 
sh.finish(color=(1,0,0),width=1.2)
for x in p.get_drawings():
    if not x.get('color') or x['color'][0]>0.1 or abs((x.get('width') or 0)-0.72)>0.01: continue
    for it in x['items']:
        if it[0]=='l':
            L=math.dist(it[1],it[2])*FT
            if abs(L-1.0)<0.05: sh.draw_line(it[1],it[2]); 
sh.finish(color=(0,0,1),width=1.2)
sh.commit()
pg.get_pixmap(matrix=pymupdf.Matrix(5,5),clip=pymupdf.Rect(1140,880,1260,960)).save('curbticks.png')
