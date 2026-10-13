import pymupdf,glob,re,os,sys
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(os.path.join(ROOT,'source/markups/MARKUPS*.pdf'))):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(53); W,H=p.rect.width,p.rect.height
Z=4; box=[float(v) for v in sys.argv[1:5]]
clip=pymupdf.Rect(W*box[0],H*box[1],W*box[2],H*box[3])
pix=p.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip,alpha=False)
s=pix.samples;PW,PH,n=pix.width,pix.height,pix.n
ptft=18*W/2592; pxft=ptft*Z
print('px/ft',round(pxft,2))
def purp(x,y):
    i=(y*PW+x)*n; r,g,b=s[i],s[i+1],s[i+2]
    return r-g>40 and b-g>40 and abs(r-b)<30
# horizontal runs
runs=[]
for y in range(PH):
    x=0
    while x<PW:
        if purp(x,y):
            x0=x
            while x<PW and purp(x,y): x+=1
            if x-x0>40: runs.append(('H',y,x0,x))
        x+=1
for x in range(PW):
    y=0
    while y<PH:
        if purp(x,y):
            y0=y
            while y<PH and purp(x,y): y+=1
            if y-y0>40: runs.append(('V',x,y0,y))
        y+=1
# merge adjacent parallel runs (same direction, within 3px, overlapping)
groups=[]
for r in runs:
    for g in groups:
        if g[0]==r[0] and abs(g[-1][1]-r[1])<=2 and min(g[-1][3],r[3])-max(g[-1][2],r[2])>0:
            g.append(r); break
    else: groups.append([r[0],r])
for g in groups:
    d=g[0]; rs=g[1:]
    a=min(r[2] for r in rs); b=max(r[3] for r in rs); c=sum(r[1] for r in rs)/len(rs)
    if d=='H': fx=(box[0]+a/Z/W, box[0]+b/Z/W); fy=box[1]+c/Z/H; print(d,'y=%.4f x=%.4f-%.4f'%(fy,*fx),'len %.2f ft'%((b-a)/pxft),'thick',len(rs))
    else: fy=(box[1]+a/Z/H, box[1]+b/Z/H); fx=box[0]+c/Z/W; print(d,'x=%.4f y=%.4f-%.4f'%(fx,*fy),'len %.2f ft'%((b-a)/pxft),'thick',len(rs))
