import pymupdf, collections, math
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
dr=p.get_drawings()
FT=20/72
def area(pts):
    a=0
    for i in range(len(pts)):
        x1,y1=pts[i];x2,y2=pts[(i+1)%len(pts)]
        a+=x1*y2-x2*y1
    return abs(a)/2
res=[]
for i,x in enumerate(dr):
    r=x['rect']
    w,h=r.width*FT,r.height*FT
    if w>20 and h>20 and w<200 and h<200:
        pts=[]
        for it in x['items']:
            if it[0]=='l': pts+= [it[1],it[2]]
            elif it[0]=='re': pts+=[it[1].tl,it[1].tr,it[1].br,it[1].bl]
            elif it[0]=='qu': pts+=[it[1].ul,it[1].ur,it[1].lr,it[1].ll]
        # dedupe consecutive
        q=[]
        for pt in pts:
            if not q or (abs(q[-1].x-pt.x)>1e-3 or abs(q[-1].y-pt.y)>1e-3): q.append(pt)
        A=area([(p_.x,p_.y) for p_ in q])*FT*FT
        res.append((i,round(r.x0),round(r.y0),round(w,1),round(h,1),len(x['items']),x.get('fill') is not None,x.get('closePath'),round(A,1),x.get('width'),x.get('color'),x.get('dashes')))
for r in sorted(res,key=lambda r:r[1]): print(r)
