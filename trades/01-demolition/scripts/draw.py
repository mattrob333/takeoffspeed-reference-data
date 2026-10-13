import pymupdf, math
src=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')
p=src[0]
x=p.get_drawings()[10401]
doc=pymupdf.open(); pg=doc.new_page(width=2592,height=1728)
pg.show_pdf_page(pg.rect, src, 0)
sh=pg.new_shape()
for it in x['items']:
    if it[0]=='l': sh.draw_line(it[1],it[2])
    elif it[0]=='c': sh.draw_bezier(*it[1:5])
sh.finish(color=(1,0,0),width=4); sh.commit()
pix=pg.get_pixmap(matrix=pymupdf.Matrix(1,1),clip=pymupdf.Rect(550,550,1450,1450)); pix.save('path10401.png')
