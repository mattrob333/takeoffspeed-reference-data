import pymupdf, math
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
FT=20/72
targets=[169.35,208.00,211.29,109.85,89.98,40.48,30.11,58.08]
for x in p.get_drawings():
    for it in x['items']:
        if it[0]=='l':
            L=math.dist(it[1],it[2])*FT
            for t in targets:
                if abs(L-t)<0.3: print(t, round(L,3), it[1], it[2])
