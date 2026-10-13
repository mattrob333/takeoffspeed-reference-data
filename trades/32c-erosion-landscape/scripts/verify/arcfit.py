import pymupdf, glob, re, math, sys
ROOT='/home/user/takeoffspeed-reference-data/source/markups/'
def page(n):
    for f in sorted(glob.glob(ROOT+'MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(66)
print('page rect',p.rect)
Z=16
clip=pymupdf.Rect(0.355*792,0.665*612,0.39*792,0.70*612)
pix=p.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip)
w,h,n=pix.w,pix.h,pix.n; s=pix.samples
ftpp=(720/792)/Z
# sample around the arc: print colour histogram in lower-left region
cols={}
for y in range(180,245):
    for x in range(140,245):
        o=(y*w+x)*n; c=(s[o]//16*16,s[o+1]//16*16,s[o+2]//16*16); cols[c]=cols.get(c,0)+1
for c,k in sorted(cols.items(),key=lambda t:-t[1])[:15]: print(c,k)
pts=[]
for y in range(h):
    for x in range(w):
        o=(y*w+x)*n; r,g,b=s[o],s[o+1],s[o+2]
        if r>200 and 90<g<190 and b<190 and r-g>50 and r-b>30: pts.append((x,y))
print('salmon px',len(pts))
def fit(pts):
    N=len(pts)
    Sx=sum(x for x,y in pts); Sy=sum(y for x,y in pts)
    Sxx=sum(x*x for x,y in pts); Syy=sum(y*y for x,y in pts); Sxy=sum(x*y for x,y in pts)
    Sxxx=sum(x**3 for x,y in pts); Syyy=sum(y**3 for x,y in pts); Sxyy=sum(x*y*y for x,y in pts); Sxxy=sum(x*x*y for x,y in pts)
    import numpy as np
    M=np.array([[Sxx,Sxy,Sx],[Sxy,Syy,Sy],[Sx,Sy,N]],float); v=np.array([-(Sxxx+Sxyy),-(Sxxy+Syyy),-(Sxx+Syy)],float)
    a,b,c=np.linalg.solve(M,v); cx,cy=-a/2,-b/2; R=math.sqrt(cx*cx+cy*cy-c)
    return cx,cy,R
cx,cy,R=fit(pts)
ang=sorted(math.atan2(y-cy,x-cx) for x,y in pts)
gaps=[ang[i+1]-ang[i] for i in range(len(ang)-1)]+[ang[0]+2*math.pi-ang[-1]]
span=2*math.pi-max(gaps)
rad=[math.hypot(x-cx,y-cy) for x,y in pts]
print('centre',round(cx,1),round(cy,1),'R px',round(R,1),'stroke px',round(max(rad)-min(rad),1),'dia ft',round(2*R*ftpp,3))
print('span deg',round(math.degrees(span),1),'arc len ft',round(span*R*ftpp,3),'inner',round(span*min(rad)*ftpp,3),'outer',round(span*max(rad)*ftpp,3))
from PIL import Image
im=Image.frombytes('RGB',(w,h),bytes(pix.samples) if n==3 else bytes(pix.samples))
for x,y in pts: im.putpixel((x,y),(0,255,0))
im.save('arcmask.png')
