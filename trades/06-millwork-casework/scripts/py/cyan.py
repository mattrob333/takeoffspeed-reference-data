import glob, re, pymupdf
from collections import Counter
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(30); r=p.rect; z=8
def crop(box):
    x0,y0,x1,y1=box
    clip=pymupdf.Rect(r.width*x0,r.height*y0,r.width*x1,r.height*y1)
    return p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=clip,alpha=False)
def isc(s,i,col,tol):
    return all(abs(s[i+k]-col[k])<=tol for k in range(3))
for name,box in [('plan2',(0.76,0.62,0.88,0.76)),('plan1',(0.76,0.78,0.88,0.90))]:
    pix=crop(box); s=pix.samples; w,h=pix.width,pix.height
    c=Counter()
    for y in range(h):
        for x in range(w):
            i=(y*w+x)*3
            R,G,B=s[i],s[i+1],s[i+2]
            if B>180 and G>180 and R<120: c[(R//16*16,G//16*16,B//16*16)]+=1
    print(name,c.most_common(5))
    cy=[[ (lambda i: s[i]<140 and s[i+1]>170 and s[i+2]>170)((y*w+x)*3) for x in range(w)] for y in range(h)]
    mg=[[ (lambda i: s[i]>200 and s[i+1]<140 and s[i+2]>200)((y*w+x)*3) for x in range(w)] for y in range(h)]
    # magenta bbox
    xs=[x for x in range(w) if any(mg[y][x] for y in range(h))]; ys=[y for y in range(h) if any(mg[y][x] for x in range(w))]
    print(' magenta bbox x',xs[0],xs[-1],'y',ys[0],ys[-1])
    # horizontal runs: rows with many cyan
    rows=[(y,sum(cy[y])) for y in range(h) if sum(cy[y])>40]
    cols=[(x,sum(cy[y][x] for y in range(h))) for x in range(w) if sum(cy[y][x] for y in range(h))>40]
    print(' rows',rows); print(' cols',cols)
    # extents of runs for those rows/cols
    for y,_ in rows:
        xx=[x for x in range(w) if cy[y][x]]; print('  row',y,'x',xx[0],xx[-1],'len',xx[-1]-xx[0]+1)
    for x,_ in cols:
        yy=[y for y in range(h) if cy[y][x]]; print('  col',x,'y',yy[0],yy[-1],'len',yy[-1]-yy[0]+1)
print('--- runs plan1')
pix=crop((0.76,0.78,0.88,0.90)); s=pix.samples; w,h=pix.width,pix.height
cyf=lambda x,y: (lambda i: s[i]<140 and s[i+1]>170 and s[i+2]>170)((y*w+x)*3)
for x in (855,858,860,861,862,865,936,938,939,940,942):
    runs=[];start=None
    for y in range(h):
        if cyf(x,y):
            if start is None: start=y
        elif start is not None:
            runs.append((start,y-1)); start=None
    print(x,[(a,b,b-a+1) for a,b in runs if b-a>2])
for y in (588,590,592,593,595):
    xx=[x for x in range(w) if cyf(x,y)]; print('row',y, xx[:3], xx[-3:] if xx else None, len(xx))
