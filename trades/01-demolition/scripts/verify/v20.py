exec(open('v19.py').read().split("ref=samples")[0])
ref=samples(C[0][1],8)+samples(C[7][1],8)
best=max(((cov(ref,dx,dy,2),dx,dy) for dx in range(-60,61,4) for dy in range(-60,61,4)))
print('coarse',best)
_,bx,by=best
best=max(((cov(ref,dx,dy,1),dx,dy) for dx in range(bx-4,bx+5) for dy in range(by-4,by+5)))
print('fine',best)
_,dx,dy=best
for (ci,idx),nm in zip(C,names):
    print(nm, round(cov(samples(idx),dx,dy,3)*100,1),'%')
json.dump([dx,dy],open('reg.json','w'))
