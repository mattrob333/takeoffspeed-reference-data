import pymupdf
src=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')
p=src[0]
ws=[w for w in p.get_text('words') if w[4]=='///']
print(len(ws))
doc=pymupdf.open(); pg=doc.new_page(width=2592,height=1728)
pg.show_pdf_page(pg.rect, src, 0)
sh=pg.new_shape()
for w in ws:
    sh.draw_circle(pymupdf.Point((w[0]+w[2])/2,(w[1]+w[3])/2),3)
sh.finish(color=(0,0,1),fill=(0,0,1)); sh.commit()
pg.get_pixmap(matrix=pymupdf.Matrix(1,1),clip=pymupdf.Rect(400,250,1600,1450)).save('ticks.png')
import json; json.dump([((w[0]+w[2])/2,(w[1]+w[3])/2) for w in ws],open('ticks.json','w'))
