import sys, glob, re, pymupdf
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
n=int(sys.argv[1]); x0,y0,x1,y1=map(float,sys.argv[2:6]); zoom=float(sys.argv[6]); ptft=float(sys.argv[7])
p=page(n); r=p.rect
clip=pymupdf.Rect(r.width*x0,r.height*y0,r.width*x1,r.height*y1)
pix=p.get_pixmap(matrix=pymupdf.Matrix(zoom,zoom),clip=clip,alpha=False)
s=pix.samples; W,H=pix.width,pix.height
red=dark=0; rows={}
for y in range(H):
  cnt=0
  for x in range(W):
    i=(y*W+x)*3; R,G,B=s[i],s[i+1],s[i+2]
    if R-G>40 and R-B>40 and G<150:
        red+=1; cnt+=1
        if R<150 and G<60: dark+=1
  rows[y]=cnt
pf=(zoom*ptft)**2
print('red SF',round(red/pf,1),'dark SF',round(dark/pf,1))
# dark band rows
