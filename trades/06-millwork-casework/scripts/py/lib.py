import glob, re, pymupdf
from collections import Counter
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(25); r=p.rect; z=3
clip=pymupdf.Rect(r.width*0.58,r.height*0.38,r.width*0.99,r.height*0.72)
pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=clip,alpha=False)
s=pix.samples;w,h=pix.width,pix.height
c=Counter()
for y in range(h):
  for x in range(w):
    i=(y*w+x)*3; c[(s[i]//16*16,s[i+1]//16*16,s[i+2]//16*16)]+=1
print([k for k in c.most_common(12)])
def coloured(i):
    R,G,B=s[i],s[i+1],s[i+2]
    return R>150 and R-G>60 and R-B>60   # salmon, red, brown overlays
ppf=(932-253)/ (109.5/12)  # from overall 9'-1 1/2" in px... approximate, measure below
# find extents
cols={}
for y in range(h):
  for x in range(w):
    if coloured((y*w+x)*3): cols.setdefault(x,[]).append(y)
xs=sorted(cols); print('x range',xs[0],xs[-1])
# area by x-bands
def area(x0,x1,y0=0,y1=10**6):
    return sum(1 for x in range(x0,x1) for y in cols.get(x,[]) if y0<=y<y1)
tot=area(0,w)
print('total px',tot)
for name,(a,b) in {'left of 3-6 bay':(0,323),'cased bay':(323,523),'millwork right':(523,933),'overrun':(933,w)}.items():
    print(name, area(a,b), 'below y215', area(a,b,215,10**6))
