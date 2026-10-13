import pymupdf, glob, re, math
ROOT='/home/user/takeoffspeed-reference-data/source/markups/'
def page(n):
    for f in sorted(glob.glob(ROOT+'MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(66)
print('images on page', len(p.get_images()), 'drawings', len(p.get_drawings()))
Z=16
clip=pymupdf.Rect(0.355*792,0.665*612,0.39*792,0.70*612)
pix=p.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip)
pix.save('p66-arc16.png')
w,h,n=pix.w,pix.h,pix.n; s=pix.samples
ftpp=(720/792)/Z
print('ft per px',ftpp,'image',w,h)
cols={}
pts=[]
for y in range(h):
    for x in range(w):
        o=(y*w+x)*n; r,g,b=s[o],s[o+1],s[o+2]
        if max(abs(r-g),abs(g-b),abs(r-b))>40:
            c=(r//16*16,g//16*16,b//16*16); cols[c]=cols.get(c,0)+1
        if r>170 and g>140 and b<130 and r-b>80: pts.append((x,y))   # yellow / orange
for c,k in sorted(cols.items(),key=lambda t:-t[1])[:12]: print(c,k)
print('yellow-ish px',len(pts))
if len(pts)>10:
    # least squares circle fit
    Sx=sum(x for x,y in pts); Sy=sum(y for x,y in pts); N=len(pts)
    Sxx=sum(x*x for x,y in pts); Syy=sum(y*y for x,y in pts); Sxy=sum(x*y for x,y in pts)
    Sxxx=sum(x**3 for x,y in pts); Syyy=sum(y**3 for x,y in pts); Sxyy=sum(x*y*y for x,y in pts); Sxxy=sum(x*x*y for x,y in pts)
    # solve [Sxx Sxy Sx; Sxy Syy Sy; Sx Sy N] [a b c] = [-(Sxxx+Sxyy), -(Sxxy+Syyy), -(Sxx+Syy)]
    M=[[Sxx,Sxy,Sx],[Sxy,Syy,Sy],[Sx,Sy,N]]; v=[-(Sxxx+Sxyy),-(Sxxy+Syyy),-(Sxx+Syy)]
    # gaussian elimination
    import copy
    A=[row[:]+[v[i]] for i,row in enumerate(M)]
    for i in range(3):
        piv=A[i][i]
        for j in range(i+1,3):
            f=A[j][i]/piv
            for k in range(4): A[j][k]-=f*A[i][k]
    sol=[0,0,0]
    for i in (2,1,0):
        sol[i]=(A[i][3]-sum(A[i][k]*sol[k] for k in range(i+1,3)))/A[i][i]
    a,b,c=sol; cx,cy=-a/2,-b/2; R=math.sqrt(cx*cx+cy*cy-c)
    ang=sorted(math.atan2(y-cy,x-cx) for x,y in pts)
    gaps=[ang[i+1]-ang[i] for i in range(len(ang)-1)]+[ang[0]+2*math.pi-ang[-1]]
    span=2*math.pi-max(gaps)
    xs=[x for x,y in pts]; ys=[y for x,y in pts]
    print('centre',round(cx,1),round(cy,1),'R px',round(R,1),'dia ft',round(2*R*ftpp,2))
    print('bbox ft',round((max(xs)-min(xs))*ftpp,2),round((max(ys)-min(ys))*ftpp,2))
    print('arc span deg',round(math.degrees(span),1),'arc len ft',round(span*R*ftpp,2))
