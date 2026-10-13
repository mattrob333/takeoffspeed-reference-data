import math
rect={'8x10':31.1,'14x12':7.3,'20x12':94.4,'24x12':13.3,'16x12':41.4,'10x10':7.4,'8x8':10.6,'12x12':9.8}
rnd={8:113.7,6:18.0,10:10.5,14:10.2}
flex={6:6.9,8:50.1,10:4.8,14:3.1}
tot=0;rl=0;rr=0
for k,v in rect.items():
    w,h=map(int,k.split('x')); p=2*(w+h)/12; a=p*v; tot+=a; rl+=v; print(k,v,round(p,3),round(a,2))
rs=0
for d,v in rnd.items():
    p=math.pi*d/12; a=p*v; rs+=a; rr+=v; print(d,v,round(p,3),round(a,2))
print('rect SF',round(tot,2),'round SF',round(rs,2),'sum',round(tot+rs,2),'LF rect',rl,'LF round',rr)
fs=sum(math.pi*d/12*v for d,v in flex.items()); print('flex SF',round(fs,2))
S=tot+rs
for lbsf in (0.906,0.781,1.156):
    print(lbsf, round(S*lbsf,1), round((S+fs)*lbsf,1))
print('1200/S',1200/S,'1325/S',1325/S,'1325/(S+fs)',1325/(S+fs), '1200/1325', 1200/1325)
print('rect only *0.906',tot*0.906, '1325/rect',1325/tot)
