import sys, glob, re
import pymupdf
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
n=int(sys.argv[1]); Z=4
target=tuple(int(v) for v in sys.argv[2].split(','))
x0f,x1f,y0f,y1f=map(float,sys.argv[3:7])
p=page(n)
pix=p.get_pixmap(matrix=pymupdf.Matrix(Z,Z))
W,H,nc=pix.width,pix.height,pix.n
s=pix.samples
def close(x,y,t=55):
    i=(y*W+x)*nc
    return abs(s[i]-target[0])<t and abs(s[i+1]-target[1])<t and abs(s[i+2]-target[2])<t
x0,x1,y0,y1=int(x0f*W),int(x1f*W),int(y0f*H),int(y1f*H)
ptsPerFt=1191/36*0.25
cols=[]
for x in range(x0,x1):
    ys=[y for y in range(y0,y1) if close(x,y)]
    if not ys: continue
    # merge with gap tolerance
    segs=[];a=ys[0];b=ys[0]
    for y in ys[1:]:
        if y-b<=60: b=y
        else: segs.append((a,b)); a=b=y
    segs.append((a,b))
    L=max(segs,key=lambda t:t[1]-t[0])
    if L[1]-L[0]>120: cols.append((x,L))
grp=[]
for c in cols:
    if grp and c[0]-grp[-1][-1][0]<=3: grp[-1].append(c)
    else: grp.append([c])
for g in grp:
    m=max(g,key=lambda c:c[1][1]-c[1][0])
    L=m[1][1]-m[1][0]
    print('x=%.3f y=%.3f..%.3f len=%.2f ft (width %d px)'%(m[0]/W,m[1][0]/H,m[1][1]/H,L/Z/ptsPerFt,len(g)))
