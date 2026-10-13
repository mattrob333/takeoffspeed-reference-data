import pymupdf, json
src=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')
p=src[0]; D=p.get_drawings()
C=json.load(open('util_chains.json'))
cols=[(1,0,0),(0,0.7,0),(0,0,1),(1,0.5,0),(0.8,0,0.8),(0,0.7,0.7),(0.5,0.3,0),(1,0,0.5),(0.3,0.3,1)]
doc=pymupdf.open(); pg=doc.new_page(width=2592,height=1728)
pg.show_pdf_page(pg.rect, src, 0)
sh=pg.new_shape()
for k,(ci,idx) in enumerate(C[:9]):
    for i in idx:
        for it in D[i]['items']:
            sh.draw_line(it[1],it[2])
    sh.finish(color=cols[k],width=3)
sh.commit()
pg.get_pixmap(matrix=pymupdf.Matrix(1.2,1.2),clip=pymupdf.Rect(650,560,1400,1330)).save('util_overlay.png')
