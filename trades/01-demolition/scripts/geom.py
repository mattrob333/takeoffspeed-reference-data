import pymupdf, sys, collections
d=pymupdf.open('/home/user/takeoffspeed-reference-data/source/markups/MARKUPS - FIFTH THIRD BANK WATSON BLVD_p61-70.pdf')
p=d[64-61]
print(p.rect, 'annots', len(list(p.annots())))
dr=p.get_drawings()
print('drawings',len(dr))
c=collections.Counter()
for x in dr:
    key=(x.get('type'), tuple(round(v,2) for v in x['fill']) if x.get('fill') else None, tuple(round(v,2) for v in x['color']) if x.get('color') else None, x.get('fill_opacity'))
    c[key]+=1
for k,v in c.most_common(60): print(v,k)
