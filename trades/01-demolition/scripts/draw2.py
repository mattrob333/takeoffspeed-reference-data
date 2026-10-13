import pymupdf, math
src=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')
p=src[0]; D=p.get_drawings()
FT=20/72
doc=pymupdf.open(); pg=doc.new_page(width=2592,height=1728)
pg.show_pdf_page(pg.rect, src, 0)
cols={4082:(1,0,0),4083:(0,0.6,0),5685:(0,0,1)}
for i,c in cols.items():
    sh=pg.new_shape()
    for it in D[i]['items']:
        if it[0]=='l': sh.draw_line(it[1],it[2])
        elif it[0]=='c': sh.draw_bezier(*it[1:5])
    sh.finish(color=c,width=2.5); sh.commit()
    print(i,[ (round(it[1].x,1),round(it[1].y,1),round(it[-1].x,1),round(it[-1].y,1)) for it in D[i]['items']])
pg.get_pixmap(matrix=pymupdf.Matrix(2.5,2.5),clip=pymupdf.Rect(850,730,1330,1020)).save('walks.png')
