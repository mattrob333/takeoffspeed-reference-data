import pymupdf, glob, re, collections, math
ROOT='/home/user/takeoffspeed-reference-data'
for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
    a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
    if a<=64<=b: pg=pymupdf.open(f)[64-a]
print(pg.rect, pg.rotation)
D=pg.get_drawings(); print(len(D))
c=collections.Counter((tuple(round(v,2) for v in x['color']) if x.get('color') else None, round(x.get('width') or 0,2), x['type']) for x in D)
for k,v in c.most_common(25): print(k,v)
