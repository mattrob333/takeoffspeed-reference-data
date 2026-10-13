import math, itertools
from fractions import Fraction as F
exec(open('s308.py').read().split('rows308=')[0])
rows308=[1338,77,84,740,453]
H=[F(25,2),F(15,4),F('18.67'),F(3),F(2)]
s=search('2180.195',rows308,H)
est=[101,6,6,56,35]
r=lambda x: math.floor(x/1.33+0.5)
c=lambda x: math.ceil(round(x*0.75,9))
okc=[x for x in s if [c(v) for v in x]==est]; okr=[x for x in s if [r(v) for v in x]==est]
print(len(s),'ceil-all-match',len(okc),okc[:5]); print('round1.33-all-match',len(okr),okr[:5])
