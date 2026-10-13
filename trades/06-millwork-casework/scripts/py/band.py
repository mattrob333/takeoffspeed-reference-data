import sys, glob, re, pymupdf
from collections import Counter
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(23); r=p.rect; z=8
def crop(x0,y0,x1,y1):
    clip=pymupdf.Rect(r.width*x0,r.height*y0,r.width*x1,r.height*y1)
    return p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=clip,alpha=False),clip
pix,clip=crop(0.60,0.43,0.83,0.48)
s=pix.samples;w,h=pix.width,pix.height
c=Counter()
for y in range(0,h,3):
  for x in range(0,w,3):
    i=(y*w+x)*3; c[(s[i]//8*8,s[i+1]//8*8,s[i+2]//8*8)]+=1
print(c.most_common(8))
def mask(pix,R,G,B,tol=30):
    s=pix.samples;w,h=pix.width,pix.height
    return [[abs(s[(y*w+x)*3]-R)<=tol and abs(s[(y*w+x)*3+1]-G)<=tol and abs(s[(y*w+x)*3+2]-B)<=tol for x in range(w)] for y in range(h)]
for name,box in [('e3',(0.60,0.43,0.83,0.48)),('e6',(0.70,0.18,0.80,0.25))]:
    pix,clip=crop(*box); m=mask(pix,250,100,100)
    w,h=pix.width,pix.height
    cols=[x for x in range(w) if any(m[y][x] for y in range(h))]
    rows=[y for y in range(h) if any(m[y][x] for x in range(w))]
    heights=[sum(m[y][x] for y in range(h)) for x in cols]
    from statistics import median
    print(name,'x',cols[0],cols[-1],'width px',cols[-1]-cols[0]+1,'rows',rows[0],rows[-1],'median col height',median(heights),'area px',sum(heights))
