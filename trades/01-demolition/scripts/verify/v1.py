import pymupdf, math, collections
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
ws=[w for w in p.get_text('words') if '/' in w[4]]
print('words with /:',len(ws), collections.Counter(w[4] for w in ws).most_common(5))
FT=20/72
D=p.get_drawings()
c=collections.Counter()
for i,x in enumerate(D):
    col=x.get('color'); w=x.get('width') or 0
    for it in x['items']:
        if it[0]=='l':
            L=math.dist(it[1],it[2])
            c[(round(w,2), round(L,1), bool(col and max(col)<0.1))]+=1
for k,v in sorted(c.items(),key=lambda kv:-kv[1])[:30]: print(k,v)
