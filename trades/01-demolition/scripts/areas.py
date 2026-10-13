import pymupdf, math
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
D=p.get_drawings(); FT=20/72
def pts(i):
    q=[]
    for it in D[i]['items']:
        if not q: q.append((it[1].x,it[1].y))
        q.append((it[-1].x,it[-1].y))
    return q
def area(q):
    return abs(sum(q[k][0]*q[(k+1)%len(q)][1]-q[(k+1)%len(q)][0]*q[k][1] for k in range(len(q))))/2*FT*FT
ramp=pts(5685)+[(1269.5,1007.8),(1269.5,1001.0),(1183.6,1000.3),(1147.3,1001.0)]
print('ramp/sidewalk N of two-story', round(area(ramp),1))
walk=pts(4082)+[(897.4,764.0),(897.6,882.2)]
print('sidewalk L around one-story', round(area(walk),1))
print('4083 south piece', round(area(pts(4083)),1))
print('one-story',round(area(pts(1290)),1),'two-story',round(area(pts(1291)),1))
