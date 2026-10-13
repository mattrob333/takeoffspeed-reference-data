import pymupdf
ROOT='/home/user/takeoffspeed-reference-data/'
pg=pymupdf.open(ROOT+'source/drawings/Architectural/A-150-FINISH-PLAN-Rev.0.pdf')[0]
dr=pg.get_drawings()
def near(v,t): return abs(v-t)<0.3
for tgt in (264.1,321.2,824.1,933.5):
    hits=set()
    for d in dr:
        for it in d['items']:
            if it[0]=='l':
                p,q=it[1],it[2]
                for a in (p,q):
                    if near(a.x,tgt): hits.add((round(p.x,1),round(p.y,1),round(q.x,1),round(q.y,1),d.get('width') and round(d['width'],2)))
            elif it[0]=='re':
                r=it[1]
                if near(r.x0,tgt) or near(r.x1,tgt): hits.add(('re',round(r.x0,1),round(r.y0,1),round(r.x1,1),round(r.y1,1)))
    print(tgt, sorted(hits, key=str)[:14])
