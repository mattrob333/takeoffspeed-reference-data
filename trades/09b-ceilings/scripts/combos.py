import itertools
LF={'a':4.2,'b':2.7,'c':6.7,'d':30.5,'e':35.3,'f':28.1}
opts={'a':[0,3.5,7],'b':[0,4,8,6.5,13],'c':[0,1.5,3,3.5,7],'d':[0,3,6,4.5,9],'e':[0,2.5,5,5.75,11.5],'f':[0,2,4]}
T=286.04
res=[]
for combo in itertools.product(*[opts[k] for k in 'abcdef']):
    v=sum(LF[k]*c for k,c in zip('abcdef',combo))
    err=sum(0.05*c for c in combo)
    if abs(v-T)<=err+1e-9: res.append((abs(v-T),combo,round(v,3),round(err,3)))
for r in sorted(res)[:20]: print(r)
print(len(res))
# studs
T2=571.3675
fr={'a':[3.5,7],'b':[6.5,4],'c':[3.5,1.5],'d':[4.5,3],'e':[5.75,2.5],'f':[2,4,0]}
G={'g':(27.1,5),'h':(28.1,8)}
for k in [0,0.25,1/3,0.33,0.5,1]:
  for combo in itertools.product(*[fr[x] for x in 'abcdef']):
    v=sum(LF[x]*c for x,c in zip('abcdef',combo))+k*(27.1*5+28.1*8)
    err=sum(0.05*c for c in combo)+k*0.05*13
    if abs(v-T2)<=err: print('studs k',k,combo,round(v,3),round(err,3))
