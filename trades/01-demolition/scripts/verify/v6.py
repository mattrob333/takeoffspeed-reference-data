import pymupdf, math, json, collections
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
FT=20/72
D=p.get_drawings()
T=json.load(open('ticks_site.json'))
objs=[]
for i,x in enumerate(D):
    col=x.get('color'); w=x.get('width') or 0
    if x['type']!='s' or not col or max(col)>0.1 or abs(w-0.72)>0.01: continue
    ls=[((it[1].x,it[1].y),(it[2].x,it[2].y)) for it in x['items'] if it[0]=='l']
    if not ls or len(ls)!=len(x['items']): continue
    L=sum(math.dist(a,b) for a,b in ls)
    objs.append((i,ls[0][0],ls[-1][1],L,ls))
# chain by drawing order
chains=[]; cur=[objs[0]]
for o in objs[1:]:
    prev=cur[-1]
    if o[0]==prev[0]+1 and math.dist(prev[2],o[1])<0.2: cur.append(o)
    else: chains.append(cur); cur=[o]
chains.append(cur)
def dps(pt,a,b):
    ax,ay=a; bx,by=b; px,py=pt
    dx,dy=bx-ax,by-ay; L2=dx*dx+dy*dy
    t=max(0,min(1,((px-ax)*dx+(py-ay)*dy)/L2)) if L2 else 0
    return math.dist(pt,(ax+t*dx,ay+t*dy))
cnt=collections.Counter(); assigned=0
for t in T:
    best=None;bd=1e9
    for ci,c in enumerate(chains):
        for o in c:
            for a,b in o[4]:
                d=dps(t,a,b)
                if d<bd: bd=d;best=ci
    if bd<5: cnt[best]+=1; assigned+=1
print('assigned',assigned)
res=[]
for ci,nt in cnt.most_common():
    c=chains[ci]; L=sum(o[3] for o in c)*FT
    xs=[q[0] for o in c for s in o[4] for q in s]; ys=[q[1] for o in c for s in o[4] for q in s]
    n18=sum(1 for o in c if abs(o[3]-18)<0.05)
    res.append((ci,nt,len(c),n18,round(L,1)))
    print('chain',ci,'firstobj',c[0][0],'ticks',nt,'objs',len(c),'18pt objs',n18,'LF',round(L,1),'ticks*5',nt*5,'bbox',[round(min(xs)),round(min(ys)),round(max(xs)),round(max(ys))])
print('sum LF', round(sum(r[4] for r in res),1), 'sum ticks', sum(r[1] for r in res))
# overall 18pt objects
print('total 18pt objs', sum(1 for o in objs if abs(o[3]-18)<0.05))
json.dump([[ci,[o[0] for o in chains[ci]]] for ci,_ in cnt.most_common()],open('util_chains.json','w'))
