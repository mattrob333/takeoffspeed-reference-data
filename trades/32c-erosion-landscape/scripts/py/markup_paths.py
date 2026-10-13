import pymupdf, glob, re, sys, math, collections
ROOT='/home/user/takeoffspeed-reference-data/source/markups/'
def page(n):
    for f in sorted(glob.glob(ROOT+'MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
n=int(sys.argv[1]); p=page(n)
S=(36*20)/p.rect.width   # ft per pt: 36in sheet at 1"=20' on a page this wide
print('page',p.rect,'ft/pt',S)
dr=p.get_drawings()
by=collections.defaultdict(list)
for x in dr:
    col=x.get('color') or x.get('fill')
    if col is None: continue
    col=tuple(round(c,2) for c in col)
    if len(set(col))==1: continue  # skip greys/black
    by[col].append(x)
for col,xs in sorted(by.items(), key=lambda t:-len(t[1])):
    L=0
    for x in xs:
        for it in x['items']:
            if it[0]=='l': L+=math.dist(it[1],it[2])
            elif it[0]=='re': pass
    print(col, len(xs), 'line length ft', round(L*S,1))
