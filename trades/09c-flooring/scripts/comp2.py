# generic: connected components of colour on markup page; args: page sppf(sheet pt/ft) r,g,b tol x0 y0 x1 y1 [minpx]
import pymupdf,glob,re,sys
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
pg=int(sys.argv[1]); sppf=float(sys.argv[2]); col=tuple(map(int,sys.argv[3].split(','))); tol=int(sys.argv[4]); box=tuple(map(float,sys.argv[5:9])); mn=int(sys.argv[9]) if len(sys.argv)>9 else 30
p=page(pg); z=float(__import__("os").environ.get("Z","8")); r=p.rect
pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=pymupdf.Rect(r.width*box[0],r.height*box[1],r.width*box[2],r.height*box[3]))
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
pxft=z*sppf*1190.52/2592
m=bytearray(W*H)
for i in range(W*H):
    if abs(s[i*n]-col[0])<tol and abs(s[i*n+1]-col[1])<tol and abs(s[i*n+2]-col[2])<tol: m[i]=1
comps=[]
for st in range(W*H):
    if not m[st]: continue
    stack=[st]; m[st]=0; c=0; x0=y0=10**9; x1=y1=-1
    while stack:
        q=stack.pop(); x,y=q%W,q//W; c+=1
        x0=min(x0,x);x1=max(x1,x);y0=min(y0,y);y1=max(y1,y)
        for d in (1,-1,W,-W):
            t=q+d
            if 0<=t<W*H and m[t]: m[t]=0; stack.append(t)
    if c>=mn: comps.append((c,round((x1-x0+1)/pxft,3),round((y1-y0+1)/pxft,3),round(box[0]+x0/W*(box[2]-box[0]),4),round(box[1]+y0/H*(box[3]-box[1]),4),round(y0/pxft,3)))
comps.sort(key=lambda c:(c[4],c[3]))
print('pxft',round(pxft,2))
for c in comps: print(c)
