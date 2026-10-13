import pymupdf, glob
f=glob.glob('/home/user/takeoffspeed-reference-data/source/markups/*_p01-10.pdf')[0]
pg=pymupdf.open(f)[5]; r=pg.rect
Z=4
pix=pg.get_pixmap(matrix=pymupdf.Matrix(Z,Z))
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
def yellow(x,y):
    i=(y*W+x)*n; p=s[i:i+3]; return p[0]>200 and p[1]>200 and p[2]<190
pxft=36*(1190.52/2592)*Z
# scan horizontal at several y (fraction of page height of detail 5 rows)
for fy in (0.25,0.30,0.35):
    y=int(H*fy); runs=[]; inrun=False
    for x in range(int(W*0.1),int(W*0.5)):
        yv=yellow(x,y)
        if yv and not inrun: start=x; inrun=True
        if not yv and inrun: runs.append((start,x)); inrun=False
    runs=[r for r in runs if r[1]-r[0]>=3]
    print(fy,len(runs),[round((b-a)/pxft*12,1) for a,b in runs][:5])
    xs=[(a+b)/2 for a,b in runs]
# vertical extents of each run at fy=0.30
y=int(H*0.30); runs=[];inrun=False
for x in range(int(W*0.1),int(W*0.5)):
    yv=yellow(x,y)
    if yv and not inrun: start=x; inrun=True
    if not yv and inrun: runs.append((start,x)); inrun=False
runs=[r for r in runs if r[1]-r[0]>=3]
tot=0; L=[]
for a,b in runs:
    x=(a+b)//2; y0=y
    while y0>0 and (yellow(x,y0-1) or yellow(x,y0-2) or yellow(x,y0-3)): y0-=1
    y1=y
    while y1<H-1 and (yellow(x,y1+1) or yellow(x,y1+2) or yellow(x,y1+3)): y1+=1
    L.append(round((y1-y0)/pxft,2)); tot+=(y1-y0)/pxft
print(len(L),L,round(tot,2))
