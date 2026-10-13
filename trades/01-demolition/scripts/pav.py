import pymupdf, math
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
FT=20/72
x=p.get_drawings()[10401]
subs=[];cur=[]
for it in x['items']:
    a=it[1]; b=it[-1]
    if cur and math.dist(cur[-1],a)>0.05:
        subs.append(cur); cur=[]
    if not cur: cur=[a]
    if it[0]=='c':
        # sample bezier
        p0,p1,p2,p3=it[1:5]
        for t in [i/8 for i in range(1,9)]:
            xx=(1-t)**3*p0.x+3*(1-t)**2*t*p1.x+3*(1-t)*t*t*p2.x+t**3*p3.x
            yy=(1-t)**3*p0.y+3*(1-t)**2*t*p1.y+3*(1-t)*t*t*p2.y+t**3*p3.y
            cur.append(pymupdf.Point(xx,yy))
    else: cur.append(b)
subs.append(cur)
def area(pts):
    return abs(sum(pts[i].x*pts[(i+1)%len(pts)].y-pts[(i+1)%len(pts)].x*pts[i].y for i in range(len(pts))))/2
tA=0
for s in subs:
    L=sum(math.dist(s[i],s[i+1]) for i in range(len(s)-1))*FT
    closed=math.dist(s[0],s[-1])<0.5
    A=area(s)*FT*FT
    print(len(s), round(L,1), closed, round(A,1), [round(v) for v in (min(q.x for q in s),min(q.y for q in s),max(q.x for q in s),max(q.y for q in s))])
    if closed: tA+=A
print('closed area total',round(tA,1))
