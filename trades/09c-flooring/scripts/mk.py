import pymupdf,glob,re,sys,collections
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(int(sys.argv[1]))
print(p.rect, 'annots',len(list(p.annots())))
dr=p.get_drawings()
print('drawings',len(dr))
c=collections.Counter()
for g in dr:
    k=(g['type'],tuple(round(x,2) for x in g['fill']) if g.get('fill') else None, tuple(round(x,2) for x in g['color']) if g.get('color') else None, g.get('fill_opacity'))
    c[k]+=1
for k,v in c.most_common(60): print(v,k)
