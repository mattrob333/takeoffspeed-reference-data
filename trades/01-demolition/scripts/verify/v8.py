import pymupdf, math, json
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
D=p.get_drawings(); FT=20/72
C=json.load(open('util_chains.json'))
for ci,idx in C[:9]:
    Ls=[round(sum(math.dist(it[1],it[2]) for it in D[i]['items']),1) for i in idx]
    print(ci, len(idx), Ls)
