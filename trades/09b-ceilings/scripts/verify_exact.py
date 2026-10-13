# Independent exactness check (exact integer arithmetic). Units: LF in 1/100 ft, heights in 1/4 ft.
import itertools
from collections import Counter
L=[4.2,2.7,6.7,30.5,35.3,28.1]
fh4=[14,26,14,18,23,8]        # framing height x4 : 3.5,6.5,3.5,4.5,5.75,2
bf4=[28,16,6,12,10,8]         # board height x faces x4: 3.5*2,4,1.5,3,2.5,2
def rng(v): c=round(v*100); return list(range(c-5,c+5))   # 2-dec values that round half-up to v
R=[rng(v) for v in L]
FA=Counter(); FAb=Counter()
for combo in itertools.product(*R):
    fa=sum(a*b for a,b in zip(combo,fh4))   # framing area in 1/400 SF
    bd=sum(a*b for a,b in zip(combo,bf4))   # board SF in 1/400
    FA[fa]+=1
    if bd==28604*4: FAb[fa]+=1
print('board-exact sets', sum(FAb.values()))
target=429.599624
G=rng(27.1); H=rng(28.1)
def count(fac, rule):
    n=0
    for fa,c in fac.items():
        F=fa/400
        for g in G:
            for h in H:
                br=(5*g+8*h)/100   # sum braceLF*height
                if rule=='adopted': v=F/1.33+br/4
                elif rule=='third': v=(F+br/3)/1.33
                elif rule=='k033': v=(F+0.33*br)/1.33
                if round(v,6)==target: n+=c
    return n
for r in ('adopted','third','k033'):
    print(r,'board-exact & stud-exact:',count(FAb,r),'| all 10^8 combos stud-exact:',count(FA,r))
# legend-value results
F=452.125; br=27.1*5+28.1*8
print('legend adopted',F/1.33+br/4,'third',(F+br/3)/1.33,'k033',(F+0.33*br)/1.33)
for v in (F/1.33+br/4,(F+br/3)/1.33): print('delta%',(v-target)/target*100)
print('429.599624*1.33=',429.599624*1.33,' 90*1.33=',90*1.33)
