import pymupdf, math
pix=pymupdf.Pixmap('p66-arc16.png'); w,h=pix.w,pix.h
Z=16; ftpp=(720/792)/Z   # 1"=20' on a 36" (792 pt wide... 11x? ) -- same scale assumption as reviewer
pts=[]
for y in range(h):
    for x in range(w):
        r,g,b=pix.pixel(x,y)[:3]
        if r>190 and r-b>30 and 30<g<95: pts.append((x,y))
print('arc px',len(pts))
def solve(A,v):
    A=[row[:]+[v[i]] for i,row in enumerate(A)]
    for i in range(3):
        for j in range(i+1,3):
            f=A[j][i]/A[i][i]
            for k in range(4): A[j][k]-=f*A[i][k]
    s=[0,0,0]
    for i in (2,1,0): s[i]=(A[i][3]-sum(A[i][k]*s[k] for k in range(i+1,3)))/A[i][i]
    return s
def fit(pts):
    N=len(pts); Sx=sum(x for x,y in pts); Sy=sum(y for x,y in pts)
    Sxx=sum(x*x for x,y in pts); Syy=sum(y*y for x,y in pts); Sxy=sum(x*y for x,y in pts)
    Sxxx=sum(x**3 for x,y in pts); Syyy=sum(y**3 for x,y in pts); Sxyy=sum(x*y*y for x,y in pts); Sxxy=sum(x*x*y for x,y in pts)
    a,b,c=solve([[Sxx,Sxy,Sx],[Sxy,Syy,Sy],[Sx,Sy,N]],[-(Sxxx+Sxyy),-(Sxxy+Syyy),-(Sxx+Syy)])
    cx,cy=-a/2,-b/2; return cx,cy,math.sqrt(cx*cx+cy*cy-c)
cx,cy,R=fit(pts)
# reject outliers far from circle and refit
pts=[p for p in pts if abs(math.hypot(p[0]-cx,p[1]-cy)-R)<8]
cx,cy,R=fit(pts)
rad=sorted(math.hypot(x-cx,y-cy) for x,y in pts)
ang=sorted(math.atan2(y-cy,x-cx) for x,y in pts)
gaps=[ang[i+1]-ang[i] for i in range(len(ang)-1)]+[ang[0]+2*math.pi-ang[-1]]
span=2*math.pi-max(gaps)
lo,hi=rad[int(0.05*len(rad))],rad[int(0.95*len(rad))]
print('pts',len(pts),'centre',round(cx,1),round(cy,1),'R px',round(R,2),'stroke 5-95% px',round(lo,1),round(hi,1))
print('ft/px',ftpp,'dia ft',round(2*R*ftpp,3))
print('span deg',round(math.degrees(span),1))
print('arc len centreline ft',round(span*R*ftpp,3),'inner',round(span*lo*ftpp,3),'outer',round(span*hi*ftpp,3))
print('half circumference of drawn arc ft',round(math.pi*R*ftpp,3))
