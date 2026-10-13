import pymupdf,glob,re,sys,collections
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
n=int(sys.argv[1]); x0,y0,x1,y1=map(float,sys.argv[2:6]); z=float(sys.argv[6]) if len(sys.argv)>6 else 4
p=page(n); r=p.rect
pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=pymupdf.Rect(r.width*x0,r.height*y0,r.width*x1,r.height*y1))
s=pix.samples; c=collections.Counter()
for i in range(0,len(s),pix.n):
    c[(s[i]//8*8,s[i+1]//8*8,s[i+2]//8*8)]+=1
for k,v in c.most_common(int(sys.argv[7]) if len(sys.argv)>7 else 15): print(k,v)
print('px/pt',z,'size',pix.width,pix.height)
