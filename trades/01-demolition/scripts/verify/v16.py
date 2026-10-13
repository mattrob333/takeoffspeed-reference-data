import pymupdf, math, json
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
D=p.get_drawings(); FT=20/72
C=json.load(open('util_chains.json'))[:9]
for ci,idx in C:
    L=sum(math.dist(it[1],it[2]) for i in idx for it in D[i]['items'])*FT
    print(ci, idx[0], round(L,2))
def pts(i):
    q=[]
    for it in D[i]['items']:
        if not q: q.append((it[1].x,it[1].y))
        q.append((it[-1].x,it[-1].y))
    return q
def area(q): return abs(sum(q[k][0]*q[(k+1)%len(q)][1]-q[(k+1)%len(q)][0]*q[k][1] for k in range(len(q))))/2*FT*FT
b=pts(1291)  # building outline; take vertices from (1147.3,1001) going backwards to (1269.5,1007.8)
print([ (round(x,2),round(y,2)) for x,y in b])
clos=[b[11],b[10],b[9]]  # (1183.6,1000.3),(1269.5,1001.0),(1269.5,1007.8)
print('closure',clos)
r=pts(5685)+clos
print('ramp polygon', round(area(r),2))
print('one-story', round(area(pts(1290)),2), 'two-story', round(area(pts(1291)),2))
