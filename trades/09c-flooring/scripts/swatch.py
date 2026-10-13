import pymupdf,glob,re,sys
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(int(sys.argv[1])); z=4
pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z))
W,H=pix.width,pix.height
x=int(float(sys.argv[2])*W)
prev=None;start=0
for y in range(int(0.64*H),int(0.98*H)):
    c=pix.pixel(x,y)
    if c!=prev:
        if prev is not None and y-start>=8: print(round(start/H,4),y-start,prev)
        prev=c;start=y
