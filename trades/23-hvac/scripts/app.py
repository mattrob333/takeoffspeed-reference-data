import math
rect={'8x10':31.1,'14x12':7.3,'20x12':94.4,'24x12':13.3,'16x12':41.4,'10x10':7.4,'8x8':10.6,'12x12':9.8}
rnd={8:113.7,6:18.0,10:10.5,14:10.2}
W={26:0.906,24:1.156}
def rsf(): return sum(2*(sum(map(int,k.split('x'))))/12*v for k,v in rect.items())
def osf(): return sum(math.pi*d/12*v for d,v in rnd.items())
R,O=rsf(),osf()
print('rect SF',R,'round SF',O)
# A: gauge 26 read, default allowances
A=R*0.906*1.15+O*0.906*1.10
print('A lbs net',A,'with 5% waste',A*1.05, 'delta%',(A/1200-1)*100,(A*1.05/1200-1)*100)
# B: gauge table rect<=12 ->26, <=30 ->24; round <=14 ->26
lb26=lb24=0
for k,v in rect.items():
    w,h=map(int,k.split('x')); sf=2*(w+h)/12*v
    if max(w,h)<=12: lb26+=sf*0.906*1.15
    else: lb24+=sf*1.156*1.15
lb26+=O*0.906*1.10
print('B 26ga',lb26,'24ga',lb24,'total',lb26+lb24,(lb26+lb24)/1200-1)
# C: allowances 0, gauge 26
print('C',(R+O)*0.906)
for t in (1.5,2.2):
    wr=sum((2*sum(map(int,k.split('x')))+8*t+2)/12*v for k,v in rect.items())
    wo=sum((math.pi*(d+2*t)+2)/12*v for d,v in rnd.items())
    print('wrap t',t,wr,wo,wr+wo,'delta%',((wr+wo)/1325-1)*100,'with10%',(wr+wo)*1.1,((wr+wo)*1.1/1325-1)*100)
# joints
def joints(L,sec=5): return math.ceil(L*12/(sec*12))+1 if L>0 else 0
