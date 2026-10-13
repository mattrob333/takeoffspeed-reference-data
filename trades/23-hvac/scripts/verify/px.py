import pymupdf,glob,re,os,sys
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(os.path.join(ROOT,'source/markups/MARKUPS*.pdf'))):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(53); W,H=p.rect.width,p.rect.height
Z=6; x0f,y0f,x1f,y1f=0.24,0.28,0.36,0.38
clip=pymupdf.Rect(W*x0f,H*y0f,W*x1f,H*y1f)
pix=p.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip,alpha=False)
s=pix.samples;PW,PH,n=pix.width,pix.height,pix.n
def px(x,y): i=(y*PW+x)*n; return tuple(s[i:i+3])
for y in range(250,340,2):
    row=[px(x,y) for x in range(150,700,1)]
    print(y, px(400,y), px(450,y))
