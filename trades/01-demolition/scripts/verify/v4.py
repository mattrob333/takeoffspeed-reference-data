import pymupdf, math, json
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
ws=[w for w in p.get_text('words') if w[4]=='///' and w[0]<1950]
T=[((w[0]+w[2])/2,(w[1]+w[3])/2) for w in ws]
n=len(T); print('site ticks',n)
par=list(range(n))
def f(i):
    while par[i]!=i: par[i]=par[par[i]]; i=par[i]
    return i
for i in range(n):
    for j in range(i+1,n):
        if math.dist(T[i],T[j])<22: par[f(i)]=f(j)
g={}
for i in range(n): g.setdefault(f(i),[]).append(i)
for k,v in sorted(g.items(), key=lambda kv:-len(kv[1])):
    xs=[T[i][0] for i in v]; ys=[T[i][1] for i in v]
    print(len(v), [round(min(xs)),round(min(ys)),round(max(xs)),round(max(ys))])
json.dump(T,open('ticks_site.json','w'))
