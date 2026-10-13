import glob,re,pymupdf
for f in sorted(glob.glob('source/markups/MARKUPS*.pdf')):
    a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
    if a<=34<=b: p=pymupdf.open(f)[34-a]
Z=8; S=1190.52/2592; OY=(841.92-1728*S)/2; PPF=18*S
print('scale',S,'offsetY',OY,'pt/ft',PPF)
def m(sy): return S*sy+OY
gridB=m(942.1); gridC=m(1211.8); gridD=m(1374.3); gridA=m(489.5)
print('grid A,B,C,D markup y',[round(v,2) for v in (gridA,gridB,gridC,gridD)])
clip=pymupdf.Rect(560,380,960,700)
pix=p.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip)
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
def px(x,y): i=(y*W+x)*n; return s[i],s[i+1],s[i+2]
def runs(xpt):
    best=None
    for dx in range(-3,4):
        x=int(round((xpt-clip.x0)*Z))+dx
        on=[]
        for y in range(H):
            c=px(x,y); side=px(x+16,y)
            on.append((side[0]-c[0])>20 or (side[1]-c[1])>20 or (c[1]<20 and c[0]<130))
        # longest run allowing gaps of 6px
        start=None;gap=0;res=[]
        for y,o in enumerate(on):
            if o:
                if start is None: start=y
                last=y;gap=0
            elif start is not None:
                gap+=1
                if gap>40: res.append((start,last));start=None;gap=0
        if start is not None: res.append((start,last))
        r=max(res,key=lambda t:t[1]-t[0])
        if best is None or r[1]-r[0]>best[1]-best[0]: best=r
    y0=clip.y0+best[0]/Z; y1=clip.y0+best[1]/Z
    return y0,y1
out=[]
for xpt,l,end in [(595.75,'18KCS2',gridD),(642.56,'18KCS2',gridD),(683.88,'18KCS2',gridD),(725.62,'18KCS2',gridD),(763.0,'12KCS2',gridC),(804.81,'12KCS2',gridC),(847.5,'12KCS2',gridC)]:
    y0,y1=runs(xpt)
    L=(y1-y0)/PPF
    print(l,xpt,'y',round(y0,2),round(y1,2),'len ft',round(L,2),'start N of B ft',round((gridB-y0)/PPF,2),'end vs grid ft',round((y1-end)/PPF,2))
