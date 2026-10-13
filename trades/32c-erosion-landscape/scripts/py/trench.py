import pymupdf, math, sys
d=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-4.0-GRADING-PLAN-Rev.0.pdf'); p=d[0]
S=20/72  # ft per pt at 1"=20'
def pts(x):
    out=[]
    for it in x['items']:
        if it[0]=='l': out+= [it[1],it[2]]
        elif it[0]=='c':
            a,b,c,e=it[1:5]
            for t in [i/16 for i in range(17)]:
                mt=1-t
                out.append(pymupdf.Point(mt**3*a.x+3*mt*mt*t*b.x+3*mt*t*t*c.x+t**3*e.x, mt**3*a.y+3*mt*mt*t*b.y+3*mt*t*t*c.y+t**3*e.y))
    return out
def area_len(P):
    A=0;L=0
    for i in range(len(P)):
        a=P[i];b=P[(i+1)%len(P)]
        A+=a.x*b.y-b.x*a.y
    for i in range(len(P)-1):
        L+=math.dist((P[i].x,P[i].y),(P[i+1].x,P[i+1].y))
    return abs(A)/2*S*S, L*S
for x in p.get_drawings():
    r=x['rect']
    w=r.width*S;h=r.height*S
    if (abs(w-95.6)<0.2 and abs(h-10.27)<0.2) or (abs(w-113.6)<0.2 and abs(h-28.27)<0.2) or (abs(w-101.6)<.2) or (abs(w-107.6)<.2 and h<30):
        P=pts(x); A,L=area_len(P)
        print(f'bbox {w:.2f} x {h:.2f} ft  area {A:.1f} SF  path length {L:.1f} ft  items {len(x["items"])}  rect {[round(v,1) for v in r]}')
