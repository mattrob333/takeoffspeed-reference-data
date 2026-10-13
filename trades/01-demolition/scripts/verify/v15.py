import pymupdf, math, collections, json
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
D=p.get_drawings(); FT=20/72
util=set(i for _,idx in json.load(open('util_chains.json'))[:9] for i in idx)
def L(it): return math.dist(it[1],it[2])
objs=[]
for i,x in enumerate(D):
    col=x.get('color'); w=x.get('width') or 0
    if x['type']!='s' or not col or max(col)>0.1 or abs(w-0.72)>0.01 or i in util: continue
    its=[it for it in x['items'] if it[0]=='l']
    if len(its)!=len(x['items']) or not its: continue
    tot=sum(L(it) for it in its)
    if tot<0.05 or tot>200: continue   # dots and long boundaries
    head = L(its[0])>3.9 and L(its[0])<4.7 and len(its)>1
    tail = L(its[-1])>3.9 and L(its[-1])<4.7 and len(its)>1
    core=its[(1 if head else 0):(len(its)-1 if tail else len(its))]
    a=(core[0][1].x,core[0][1].y) if core else None
    b=(core[-1][2].x,core[-1][2].y) if core else None
    objs.append(dict(i=i,head=head,tail=tail,along=sum(L(it) for it in core),a=a,b=b))
print('candidate objs',len(objs))
full=[o for o in objs if o['head'] and o['tail']]
print('full ticked objs',len(full), collections.Counter(round(o['along'],1) for o in full).most_common(6))
# chain by drawing order adjacency of along endpoints
chains=[];cur=[objs[0]]
for o in objs[1:]:
    pr=cur[-1]
    if o['i']==pr['i']+1 and pr['b'] and o['a'] and math.dist(pr['b'],o['a'])<0.3: cur.append(o)
    else: chains.append(cur);cur=[o]
chains.append(cur)
cc=[c for c in chains if sum(1 for o in c if o['head'] and o['tail'])>=3]
tot=0; nt=0; nfull=0
for c in cc:
    Lc=sum(o['along'] for o in c)*FT; tot+=Lc
    halves=sum(o['head']+o['tail'] for o in c); nt+=halves; nfull+=sum(1 for o in c if o['head'] and o['tail'])
    print('chain from',c[0]['i'],'objs',len(c),'LF',round(Lc,1),'halves',halves)
print('curb chains',len(cc),'total LF',round(tot,1),'tick halves',nt,'full objs',nfull,'full*2ft',nfull*2)
print('est vs chain', round(987.22/tot*100-100,2))
for c in cc:
    xs=[q[0] for o in c for q in (o['a'],o['b']) if q]; ys=[q[1] for o in c for q in (o['a'],o['b']) if q]
    print(c[0]['i'], [round(min(xs)),round(min(ys)),round(max(xs)),round(max(ys))])
inc=set(o['i'] for c in cc for o in c)
rest=[o for o in objs if o['i'] not in inc and (o['head'] or o['tail'])]
print('ticked objs outside chains',len(rest),[ (o['i'],round(o['along']*FT,2)) for o in rest][:30])
site=[c for c in cc if c[0]['i']!=13565]
T=sum(o['along'] for c in site for o in c)*FT
H=sum(o['head']+o['tail'] for c in site for o in c)
F=sum(1 for c in site for o in c if o['head'] and o['tail'])
print('SITE curb chain LF',round(T,1),'halves',H,'full 7.2pt pieces',F,'pieces*2ft',F*2,'est vs chain %',round(987.22/T*100-100,2))
# the 0.72 black lines along the curb but untagged: check objects without ticks adjacent geometrically to chain ends
ends=[q for c in site for q in (c[0]['a'],c[-1]['b'])]
near=[o for o in objs if o['i'] not in inc and o['a'] and any(math.dist(o['a'],e)<0.5 or math.dist(o['b'],e)<0.5 for e in ends)]
print('untick objs touching chain ends',[(o['i'],round(o['along']*FT,1)) for o in near])
