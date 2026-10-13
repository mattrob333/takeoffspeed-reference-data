from fractions import Fraction as F
T=F('322.77')
for lab,h in [('56/3',F(56,3)),('18.67',F('18.67'))]:
    sols=[]
    for a in range(0,200):            # 9' group (any LF 0..19.9)
        for b in range(82,123):       # 12'3" row 9.2 -1..+3
            rem=(T-F(a,10)*9-F(b,10)*F(49,4))/h*10
            if rem.denominator==1 and 74<=rem<=114: sols.append((a/10,b/10,int(rem)/10))
    print(lab,len(sols),sols[:12])
# 310 without any 9' group
for lab,h in [('56/3',F(56,3)),('18.67',F('18.67'))]:
    print('no-9ft',lab,[(b/10,c/10) for b in range(0,400) for c in range(0,200) if F(b,10)*F(49,4)+F(c,10)*h==T][:10])
