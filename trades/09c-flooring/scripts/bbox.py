# bbox (ft) and pixel area of one overlay colour inside a crop of markup p08
import pymupdf,glob,re,sys
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
pg,x0,y0,x1,y1=int(sys.argv[1]),*map(float,sys.argv[2:6]); col=tuple(map(int,sys.argv[6].split(','))); tol=int(sys.argv[7]) if len(sys.argv)>7 else 12
sppf=float(sys.argv[8]) if len(sys.argv)>8 else 18.0
p=page(pg); z=6; r=p.rect
pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=pymupdf.Rect(r.width*x0,r.height*y0,r.width*x1,r.height*y1))
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
pxft=z*sppf*1190.52/2592
X=[];Y=[];c=0
for i in range(W*H):
    R,G,B=s[i*n],s[i*n+1],s[i*n+2]
    if abs(R-col[0])<tol and abs(G-col[1])<tol and abs(B-col[2])<tol:
        c+=1; X.append(i%W); Y.append(i//W)
if c: print('px',c,'SF',round(c/pxft**2,2),'bbox ft',round((max(X)-min(X)+1)/pxft,2),'x',round((max(Y)-min(Y)+1)/pxft,2))
else: print('none')
