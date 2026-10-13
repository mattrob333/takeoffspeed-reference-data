import sys, glob, re
import pymupdf
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
n=int(sys.argv[1]); Z=4
p=page(n)
pix=p.get_pixmap(matrix=pymupdf.Matrix(Z,Z))
W,H,nc=pix.width,pix.height,pix.n
s=pix.samples
def px(x,y):
    i=(y*W+x)*nc; return s[i],s[i+1],s[i+2]
# find vertical runs of saturated colour: for each column, longest run of non-gray saturated pixel
x0,x1,y0,y1=[int(float(v)*d) for v,d in zip(sys.argv[2:6],[W,W,H,H])]
res=[]
for x in range(x0,x1):
    run=0;start=None;best=(0,0,0,None)
    for y in range(y0,y1):
        r,g,b=px(x,y)
        sat=max(r,g,b)-min(r,g,b)
        if sat>120:
            if run==0: start=y; col=(r,g,b)
            run+=1
            if run>best[0]: best=(run,start,y,col)
        else: run=0
    if best[0]>150: res.append((x,)+best)
# collapse adjacent columns
grp=[]
for r in res:
    if grp and r[0]-grp[-1][-1][0]<=2: grp[-1].append(r)
    else: grp.append([r])
ptsPerFt=1191/36*0.25  # markup pt per foot at 1/4"=1'-0" (36in sheet on 1191pt page)
for g in grp:
    m=max(g,key=lambda r:r[1])
    print('x=%d len_px=%d y=%d..%d col=%s  -> %.2f ft'%(m[0],m[1],m[2],m[3],m[4],m[1]/Z/ptsPerFt))
