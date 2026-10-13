import sys,glob, re, pymupdf
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
n=int(sys.argv[1]); p=page(n); r=p.rect
print('rect',r,'annots',len(list(p.annots())),'xobjects',len(p.get_xobjects()),'images',len(p.get_images()))
d=p.get_drawings()
print('drawings',len(d))
from collections import Counter
c=Counter((tuple(round(x,2) for x in (dd.get('color') or ())), tuple(round(x,2) for x in (dd.get('fill') or ()))) for dd in d)
print(c.most_common(30))
