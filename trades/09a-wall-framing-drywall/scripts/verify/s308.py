from fractions import Fraction as F
import itertools
def search(target, rows, heights, lo=-10, hi=30):
    # rows: base LF in tenths; heights: Fractions; enumerate deltas for all but last, solve last exactly
    T=F(target)
    sols=[]
    rng=range(lo,hi+1)
    for ds in itertools.product(rng, repeat=len(rows)-1):
        s=sum(F(rows[i]+ds[i],10)*heights[i] for i in range(len(rows)-1))
        rem=(T-s)/heights[-1]*10
        if rem.denominator==1 and rows[-1]+lo<=rem<=rows[-1]+hi:
            sols.append(tuple((rows[i]+ds[i])/10 for i in range(len(rows)-1))+(float(rem)/10,))
    return sols
rows308=[1338,77,84,740,453]   # 12'6 group, 3'9, 18'8, 3', 2'
for lab,h188 in [('56/3',F(56,3)),('18.67',F('18.67'))]:
    H=[F(25,2),F(15,4),h188,F(3),F(2)]
    s=search('2180.195',rows308,H)
    print('308',lab,len(s), sorted(set(x[2] for x in s)), s[:3])
