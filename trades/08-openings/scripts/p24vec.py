import pymupdf, glob, re, collections
ROOT='/home/user/takeoffspeed-reference-data'
for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
    a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
    if a<=24<=b: p=pymupdf.open(f)[24-a]
W,H=p.rect.width,p.rect.height
print('page',W,H, 'annots',len(list(p.annots())))
c=collections.Counter()
dr=p.get_drawings()
for d in dr:
    col=d.get('color'); fill=d.get('fill')
    for k in (col,fill):
        if k and (max(k)-min(k))>0.2: c[tuple(round(x,3) for x in k)]+=1
print(c.most_common(20))
