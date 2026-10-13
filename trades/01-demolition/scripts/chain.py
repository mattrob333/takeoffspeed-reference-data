import json, math
FT=20/72
T=json.load(open('ticks.json'))
n=len(T)
nn=[min(math.dist(T[i],T[j]) for j in range(n) if j!=i) for i in range(n)]
nn_s=sorted(nn); print('nn spacing median',nn_s[n//2], 'min',nn_s[0],'max',nn_s[-1])
# union-find with threshold
TH=30
par=list(range(n))
def f(i):
    while par[i]!=i: par[i]=par[par[i]]; i=par[i]
    return i
for i in range(n):
    for j in range(i+1,n):
        if math.dist(T[i],T[j])<TH: par[f(i)]=f(j)
groups={}
for i in range(n): groups.setdefault(f(i),[]).append(i)
for g in groups.values():
    xs=[T[i][0] for i in g]; ys=[T[i][1] for i in g]
    print(len(g), [round(min(xs)),round(min(ys)),round(max(xs)),round(max(ys))])
