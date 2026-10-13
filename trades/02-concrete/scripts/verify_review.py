import math
from fractions import Fraction as F
r2=lambda x: round(x,2)
print("stem 194.0*2*0.67/27 =", 194.0*2*0.67/27)
print("stem 193.8*2*(8/12)/27 =", 193.8*2*(8/12)/27, "delta", (193.8*2*(8/12)/27/9.628148-1)*100)
print("implied LF exact 8/12:", 9.628148*27/(2*(8/12)))
print("F50 6*25*1.17/27 =", 6*5*5*1.17/27, " exact", 6*25*(14/12)/27)
# formwork
wf=124.2*1*2
spread = 3*2*(3+3)*1 + 3*2*(F(44,12)*2)*1 + 6*2*(10)*F(14,12) + 1*2*12*F(16,12) + 1*2*14*F(16,12) + 1*2*11*F(16,12) + 1*2*15*F(14,12)
spread=float(spread)
stem=(193.8+8.4)*2*2
pad=4*1.5*0.5
print("wf",wf,"spread",spread,"stem",stem,"pad",pad)
s=wf+spread+stem; print("sum no pad",s, "with pad", s+pad, "delta before rounding %", (s+pad)/1420*100-100, "no pad delta", s/1420*100-100)
c10=lambda x: math.ceil(x/10)*10; n10=lambda x: round(x/10)*10
print("legend ceil10", c10(s+pad), "round10", n10(s+pad))
# estimator inputs
wfe=124.15*2*1
spe= 3*2*6*1 + 3*2*(3.67*2)*1 + 6*2*10*1.17 + 2*12*1.33 + 2*14*1.33 + 2*11*1.33 + 2*15*1.17
ste=(194.0+8.5)*2*2
se=wfe+spe+ste+pad
print("estimator sum", se, "ceil10", c10(se), "round10", n10(se))
# ft-in rounding deltas lines 21-28 exact vs estimate
est={21:1.496544,22:6.5,23:1.773333,24:2.413704,25:1.379259,26:2.166667,27:9.628148,28:0.522593}
ex={21:3*(44/12)**2/27,22:6*25*(14/12)/27,23:36*(16/12)/27,24:49*(16/12)/27,25:28*(16/12)/27,26:50*(14/12)/27,27:193.8*2*(8/12)/27,28:8.4*2*(10/12)/27}
for k in est: print(k, "exact", round(ex[k],6), "delta %", round((ex[k]/est[k]-1)*100,3))
# ft-in rounding alone on stems (LF from estimator)
print("27 ftin-only", (194.0*2*(8/12)/27/9.628148-1)*100, "LF-only", (193.8*2*0.67/27/9.628148-1)*100)
print("28 ftin-only", (8.5*2*(10/12)/27/0.522593-1)*100, "LF-only", (8.4*2*0.83/27/0.522593-1)*100)
print("wing 10.75:", 8.4*2*(10.75/12)/27, (8.4*2*(10.75/12)/27/0.522593-1)*100, "diff vs 10in exact", 8.4*2*(10.75/12)/27 - 8.4*2*(10/12)/27)
