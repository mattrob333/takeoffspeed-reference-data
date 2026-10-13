import itertools, math
# line 162 alternative decompositions
RT1,RT2=1864.3,285.4; LAP21,LAP1,LAP36=43.3,56.5,87.8; HL=45.3; EDGE=138.5; CURB=39.9; HATCH=11; HEAD=119.4; COP6,COP9,COP3=148.1,38.5,13.9
target=3042.774; field=RT1+RT2; laps=LAP21*25/12+LAP1+LAP36*3.5
base=field+laps
hs=[i/12 for i in range(0,61)]  # 0..5 ft in inches
hits=[]
for hl in hs:
  for ed in hs:
    for cb in [0,1,1.5,8/12]:
      for ht in [0,1,1.5,8/12]:
        v=base+HL*hl+EDGE*ed+CURB*cb+HATCH*ht
        if abs(v-target)/target<0.001: hits.append((round(abs(v-target),3),hl,ed,cb,ht,round(v,3)))
hits.sort(); print('162 fits within 0.1% (|d|, HL h, EDGE h, curb h, hatch h, value):',len(hits)); [print('  ',h) for h in hits[:25]]
# with laps excluded? (parapet wall rows instead)
# line 156: exact 2652.875?
rows={'P17':(46.0,19/12),'P27':(38.0,31/12),'E4':(13.0,4),'P47':(96.6,55/12),'P72':(5.9,86/12),'E129':(89.7,12.75),'E159':(41.5,15.75),'E159N':(8.7,15.75)}
print('156 sum',sum(a*b for a,b in rows.values()), 'target 2652.875 diff',2652.875-sum(a*b for a,b in rows.values()))
# try one LF perturbed within +-0.5
for k,(a,b) in rows.items():
    rest=sum(x*y for kk,(x,y) in rows.items() if kk!=k)
    need=(2652.875-rest)/b
    print(f'  if {k} LF were {need:.4f} (legend {a})')
# line 151: 190.2 perimeter?
print('151 implied perim',(2298-1917.6)/2, ' 193.8-190.2=',193.8-190.2)
# line 149 door-based search
doors=[(6,8,1),(3,8,1),(3,7,5),(3,7,1),(6,8,1),(3+4/12,7,1)]  # pair, E single, B x5, C, auto pair, F
jh=sum((2*h+w)*n for w,h,n in doors); per=sum(2*(w+h)*n for w,h,n in doors)
print('149 doors jambs+head',jh,' full perim',per, ' glazed 419.0625')
GP=419.0625
for a in range(0,5):
  for b in range(0,5):
    for c in range(0,5):
      v=a*jh+b*per+c*GP
      if v and abs(v-1330)<12: print('   ',a,'xJH +',b,'xPER +',c,'xGLZ =',round(v,2))
