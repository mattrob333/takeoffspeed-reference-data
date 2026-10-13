import pymupdf, math, json, collections
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
FT=20/72
D=p.get_drawings()
T=json.load(open('ticks_site.json'))
segs=[]
for i,x in enumerate(D):
    col=x.get('color'); w=x.get('width') or 0
    if x['type']!='s' or not col or max(col)>0.1 or abs(w-0.72)>0.01: continue
    for it in x['items']:
        if it[0]=='l':
            a=(it[1].x,it[1].y); b=(it[2].x,it[2].y)
            if math.dist(a,b)>0.01: segs.append((i,a,b))
print('0.72 black segs',len(segs))
# distance from tick to segment
def dps(pt,a,b):
    ax,ay=a; bx,by=b; px,py=pt
    dx,dy=bx-ax,by-ay; L2=dx*dx+dy*dy
    t=max(0,min(1,((px-ax)*dx+(py-ay)*dy)/L2)) if L2 else 0
    return math.dist(pt,(ax+t*dx,ay+t*dy))
# for each tick find closest seg distance
ds=[]
for t in T:
    best=min(segs,key=lambda s:dps(t,s[1],s[2]))
    ds.append(dps(t,best[1],best[2]))
print('tick->seg dist', sorted(ds)[::20], max(ds))
# graph by endpoint
key=lambda q:(round(q[0]*2)/2,round(q[1]*2)/2)
adj=collections.defaultdict(list)
for k,(i,a,b) in enumerate(segs):
    adj[key(a)].append(k); adj[key(b)].append(k)
# union segments sharing endpoints (tolerant: snap within 0.6)
par=list(range(len(segs)))
def f(i):
    while par[i]!=i: par[i]=par[par[i]]; i=par[i]
    return i
pts=collections.defaultdict(list)
for k,(i,a,b) in enumerate(segs):
    for q in (a,b):
        for dx in (-0.5,0,0.5):
            for dy in (-0.5,0,0.5):
                pts[(round(q[0]*2)/2+dx, round(q[1]*2)/2+dy)].append(k)
for v in pts.values():
    for k in v[1:]: par[f(k)]=f(v[0])
comp=collections.defaultdict(list)
for k in range(len(segs)): comp[f(k)].append(k)
# components with ticks
tick_comp=collections.Counter()
for t in T:
    best=min(range(len(segs)),key=lambda k:dps(t,segs[k][1],segs[k][2]))
    tick_comp[f(best)]+=1
tot=0
for c,nt in tick_comp.most_common():
    L=sum(math.dist(segs[k][1],segs[k][2]) for k in comp[c])*FT
    xs=[q[0] for k in comp[c] for q in segs[k][1:]]; ys=[q[1] for k in comp[c] for q in segs[k][1:]]
    print('comp',c,'ticks',nt,'nseg',len(comp[c]),'LF',round(L,1),'bbox',[round(min(xs)),round(min(ys)),round(max(xs)),round(max(ys))])
json.dump({'segs':segs},open('segs.json','w'))
