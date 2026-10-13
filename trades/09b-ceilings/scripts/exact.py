import itertools
from fractions import Fraction as Fr
def rng(v): 
    c=round(v*100); return [Fr(c+d,100) for d in range(-5,5)]
L=[4.2,2.7,6.7,30.5,35.3,28.1]
bc=[Fr(7),Fr(4),Fr(3,2),Fr(3),Fr(5,2),Fr(2)]
fc=[Fr(7,2),Fr(13,2),Fr(7,2),Fr(9,2),Fr(23,4),Fr(2)]
T=Fr(28604,100)
sols=[]
R=[rng(v) for v in L]
for combo in itertools.product(*R):
    if sum(a*b for a,b in zip(combo,bc))==T:
        sols.append((combo,sum(a*b for a,b in zip(combo,fc))))
print('board exact solutions',len(sols))
G=rng(27.1); H=rng(28.1)
studs=429.599624
mine=set(); gpt=set()
for g in G:
  for h in H:
    mine.add((g,h,Fr(33,100)*(5*g+8*h)))
    gpt.add((g,h,Fr(5,4)*g+2*h))
cm=cg=0; ex_m=ex_g=None
for combo,F in sols:
    for g,h,b in mine:
        v=float((F+b)/Fr(133,100))
        if abs(v-studs)<6e-7: cm+=1; ex_m=(combo,g,h)
    for g,h,b in gpt:
        v=float(F/Fr(133,100)+b)
        if abs(v-studs)<6e-7: cg+=1; ex_g=(combo,g,h)
print('mine',cm,ex_m); print('gpt',cg,ex_g)
for k in (Fr(1,3),Fr(1,4)/Fr(133,100)*Fr(133,100)):
    pass
# also k=1/3 inside
c3=0
for combo,F in sols:
  for g in G:
    for h in H:
      v=float((F+(5*g+8*h)/3)/Fr(133,100))
      if abs(v-studs)<6e-7: c3+=1
print('third',c3)
