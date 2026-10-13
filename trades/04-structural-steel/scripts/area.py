import sys, glob, re, pymupdf, collections
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
n=int(sys.argv[1]); x0,y0,x1,y1=map(float,sys.argv[2:6]); zoom=float(sys.argv[6])
p=page(n); r=p.rect
clip=pymupdf.Rect(r.width*x0,r.height*y0,r.width*x1,r.height*y1)
pix=p.get_pixmap(matrix=pymupdf.Matrix(zoom,zoom),clip=clip,alpha=False)
s=pix.samples
c=collections.Counter()
for i in range(0,len(s),3):
    c[(s[i]//16*16,s[i+1]//16*16,s[i+2]//16*16)]+=1
for k,v in c.most_common(int(sys.argv[7]) if len(sys.argv)>7 else 20): print(k,v)
print('px',pix.width,pix.height)
