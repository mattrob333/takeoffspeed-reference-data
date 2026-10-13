import pymupdf, collections, glob
f=glob.glob('/home/user/takeoffspeed-reference-data/source/markups/*_p01-10.pdf')[0]
doc=pymupdf.open(f); pg=doc[4]
print(pg.rect, 'annots', len(list(pg.annots())))
for a in pg.annots(): print(a.type, a.info.get('subject'), a.colors, a.rect)
d=pg.get_drawings()
print('drawings',len(d))
c=collections.Counter()
for x in d:
    c[(tuple(round(v,2) for v in (x.get('color') or ())), tuple(round(v,2) for v in (x.get('fill') or ())), x.get('fill_opacity'), x.get('stroke_opacity'), round(x.get('width') or 0,2))]+=1
for k,v in c.most_common(60): print(v,k)
