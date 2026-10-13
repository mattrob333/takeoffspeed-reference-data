import sys, glob, re, collections
import pymupdf
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(int(sys.argv[1]))
print('rect',p.rect,'rot',p.rotation)
annots=list(p.annots() or [])
print('annots',len(annots))
for a in annots[:10]: print(a.type, a.colors, a.rect)
d=p.get_drawings()
print('drawings',len(d))
c=collections.Counter()
for x in d:
    c[(tuple(round(v,2) for v in x['color']) if x.get('color') else None, x.get('width') and round(x['width'],2), x.get('stroke_opacity') and round(x['stroke_opacity'],2))]+=1
for k,v in c.most_common(40): print(k,v)
