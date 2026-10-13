F=[('F30',3,3,1,3),('F38',3+8/12,3+8/12,1,3),('F50',5,5,14/12,6),('F60',6,6,16/12,1),('F70',7,7,16/12,1),('F7040',7,4,16/12,1),('F10050',10,5,14/12,1)]
def iso(ws,dadd):
    return sum((L+2*ws)*(W+2*ws)*(T+dadd)*c for n,L,W,T,c in F)/27
def wf(LF,ws,dadd): return LF*(2+2*ws)*(1+dadd)/27
def stem(ws,h=2): return (193.8*(8/12+2*ws)*h + 8.4*(10/12+2*ws)*h)/27
print('iso:')
for ws in (0,0.5,1,1.5,2):
    print(ws,[round(iso(ws,d),2) for d in (0,1,2)])
print('wf124:')
for ws in (0,0.5,1,1.5,2):
    print(ws,[round(wf(124.2,ws,d),2) for d in (0,1,2)])
print('stem:')
for ws in (0,0.5,1,1.5,2):
    print(ws,round(stem(ws),2))
target=119.8
res=[]
for a in (0,0.5,1,1.5,2):
  for da in (0,1,2):
    for b in (0,0.5,1,1.5,2):
      for db in (0,1,2):
        for s in (None,0,0.5,1,1.5,2):
          v=iso(a,da)+wf(124.2,b,db)+(stem(s) if s is not None else 0)
          res.append((abs(v-target),v,a,da,b,db,s))
res.sort()
for r in res[:15]: print([round(x,3) if isinstance(x,float) else x for x in r])
