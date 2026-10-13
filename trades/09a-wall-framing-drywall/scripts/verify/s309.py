from fractions import Fraction as F
target=F('897.989')
sols=[]
for Hname,Hs in [('13/3',F(13,3)),('4.33',F('4.33')),('4.333',F('4.333'))]:
  for Hb_name,Hb in [('12.5',F('12.5'))]:
    for a10 in range(600,721):
      for b10 in range(150,231):
        v=F(a10,10)*Hb+F(b10,10)*Hs
        if v==target: sols.append((Hname,a10/10,b10/10,float(v)))
        elif abs(v-target)<F(1,2000): sols.append(('near',Hname,a10/10,b10/10,float(v)))
print(sols)
import math
print('ceil 65.5*.75',math.ceil(65.5*.75),'ceil 65.1*.75',math.ceil(65.1*.75))
print('65.1x12.5+18.3x4.33',65.1*12.5+18.3*4.33,'gap',897.989-(65.1*12.5+18.3*4.33))
print('runner 65.5+18.3',65.5+18.3)
