import pymupdf,glob,re,sys
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
pg=int(sys.argv[1]); col=tuple(map(int,sys.argv[2].split(','))); tol=int(sys.argv[3]); x0,y0,x1,y1=map(float,sys.argv[4:8]); ftpw=float(sys.argv[8])
p=page(pg); z=8; r=p.rect
pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=pymupdf.Rect(r.width*x0,r.height*y0,r.width*x1,r.height*y1))
W,H=pix.width,pix.height
for y in range(H):
    xs=[x for x in range(W) if all(abs(a-b)<tol for a,b in zip(pix.pixel(x,y)[:3],col))]
    if len(xs)>20:
        print(y, len(xs), 'span ft', round((xs[-1]-xs[0])/W*(x1-x0)*ftpw,3), 'from', round(x0+xs[0]/W*(x1-x0),4),'to',round(x0+xs[-1]/W*(x1-x0),4))
