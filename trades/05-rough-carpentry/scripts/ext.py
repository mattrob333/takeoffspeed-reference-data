from itertools import combinations
rows = {
 'EXT8_129 89.7x12.75': 89.7*12.75,
 'EXT6 9.2x10.25(shtng)': 9.2*10.25,
 'EXT6 9.2x12.25': 9.2*12.25,
 'PAR72 5.9x7.1667': 5.9*(7+2/12),
 'EXT8_159 41.5x15.75': 41.5*15.75,
 'EXT8_4 13x4': 13*4,
 'EXT8_159NOGWB 8.7x15.75': 8.7*15.75,
 'DBL 8.4x18.667': 8.4*(18+8/12),
 'PAR17 46x1.5833': 46*(1+7/12),
 'PAR27 38x2.5833': 38*(2+7/12),
 'PAR47 96.6x4.5833': 96.6*(4+7/12),
 'ROOFSTEP 45.3x2': 45.3*2,
 'PLAP21 43.3x2.0833': 43.3*(2+1/12),
 'PLAP1 56.5x1':56.5,
 'PLAP35 87.8x3.5':87.8*3.5,
}
for k,v in rows.items(): print(f'{k:30s} {v:10.3f}')
target=3057.0775
names=list(rows)
res=[]
for r in range(1,len(names)+1):
  for c in combinations(names,r):
    if 'EXT6 9.2x10.25(shtng)' in c and 'EXT6 9.2x12.25' in c: continue
    s=sum(rows[n] for n in c)
    if abs(s-target)/target<0.004: res.append((abs(s-target),s,c))
res.sort()
for r in res[:15]: print(round(r[1],3), round((r[1]-target)/target*100,3), r[2])
