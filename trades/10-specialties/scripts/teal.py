import sys,glob,re,pymupdf,collections
sys.path.insert(0,'/nonexistent')
ROOT='/home/user/takeoffspeed-reference-data'
n=int(sys.argv[1])
for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
    a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
    if a<=n<=b: pg=pymupdf.open(f)[n-a]
W,H=pg.rect.width,pg.rect.height
print('page',W,H)
annots=list(pg.annots())
print('annots',len(annots))
cols=collections.Counter()
for d in pg.get_drawings():
    if d.get('fill') and d.get('fill_opacity',1)<1:
        cols[tuple(round(c,2) for c in d['fill'])]+=1
print(cols.most_common(20))
