import math, itertools
FT1=946.11; WT3=38.42; WT1=144.19; WT2=46.72; WT9=53.22; WT8sf=11.28*0.25
scopes={
 'GR1=FT1 | GR3=WT1+WT2+WT9':(FT1, WT1+WT2+WT9),
 'GR1=FT1+WT3 | GR3=WT1+WT2+WT9':(FT1+WT3, WT1+WT2+WT9),
 'GR1=FT1 | GR3=WT1+WT2+WT9+WT8':(FT1, WT1+WT2+WT9+WT8sf),
 'GR1=FT1+WT3 | GR3=WT1+WT2+WT9+WT8':(FT1+WT3, WT1+WT2+WT9+WT8sf),
 'GR1=FT1 | GR3=WT1+WT2+WT9+WT3':(FT1, WT1+WT2+WT9+WT3),
}
target=(1050,300)
for name,(a,b) in scopes.items():
    for inc in (10,25,50,100):
        ok=[w for w in range(0,31) if math.ceil(a*(1+w/100)/inc)*inc==target[0] and math.ceil(b*(1+w/100)/inc)*inc==target[1]]
        if ok: print(f'{name:40s} ceil to {inc:3d}: waste% that fit {ok[0]}..{ok[-1]}')
    print(name,'net',round(a,2),round(b,2),'ratio to line',round(1050/a,4),round(300/b,4))
print('10% check', round(FT1*1.1,2), round((WT1+WT2+WT9)*1.1,2))
