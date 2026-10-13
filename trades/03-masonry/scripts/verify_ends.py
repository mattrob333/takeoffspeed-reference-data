# For each elevation band: compare purple extents (markup) with brick-hatch extents (clean sheet), as page fractions.
import pymupdf, sys, glob, json, re, os
ROOT='/home/user/takeoffspeed-reference-data'
def markup(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
def sheet(s):
    for x in json.load(open(ROOT+'/reference/sheets/index.json')):
        if x['sheet']==s and x['pages']==1: return pymupdf.open(ROOT+'/'+x['file'])[0]
def runs(mask):
    out=[];st=None
    for i,v in enumerate(mask+[False]):
        if v and st is None: st=i
        if not v and st is not None:
            if i-st>15: out.append((st,i-1))
            st=None
    return out
for pg,sh in ((11,'A-200'),(12,'A-201')):
    m=markup(pg); pm=m.get_pixmap(matrix=pymupdf.Matrix(2,2)); W,H=pm.width,pm.height
    s=pm.samples; n=pm.n
    def px(x,y): i=(y*W+x)*n; return s[i],s[i+1],s[i+2]
    # rows with lots of purple
    prow={}
    for y in range(0,H,2):
        c=0
        for x in range(0,W,2):
            r,g,b=px(x,y)
            if r>140 and b>140 and g<130: c+=1
        if c>40: prow[y]=c
    # group rows into bands
    ys=sorted(prow); bands=[];cur=[]
    for y in ys:
        if cur and y-cur[-1]>6: bands.append(cur);cur=[]
        cur.append(y)
    if cur: bands.append(cur)
    for bnd in bands:
        y=bnd[len(bnd)//2]
        mask=[]
        for x in range(W):
            r,g,b=px(x,y); mask.append(r>140 and b>140 and g<130)
        print(f'p{pg} band y={y/H:.3f} purple runs (frac):',[(round(a/W,4),round(b/W,4)) for a,b in runs(mask)])
