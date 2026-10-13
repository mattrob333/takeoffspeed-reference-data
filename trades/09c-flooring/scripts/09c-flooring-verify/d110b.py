import pymupdf
ROOT='/home/user/takeoffspeed-reference-data/'
pg=pymupdf.open(ROOT+'source/drawings/Architectural/A-150-FINISH-PLAN-Rev.0.pdf')[0]
dr=pg.get_drawings()
seen=set()
for d in dr:
    for it in d['items']:
        if it[0]=='l':
            p,q=it[1],it[2]
            # short horizontal-ish lines at y in 255-330 near x range? find x of lines ending at y 264.1 or 321.2
            for a in (p,q):
                if abs(a.y-264.1)<0.4 or abs(a.y-321.2)<0.4:
                    k=(round(p.x,1),round(p.y,1),round(q.x,1),round(q.y,1),d.get('width') and round(d['width'],2))
                    if k not in seen: seen.add(k); print(k)
