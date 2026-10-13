import math
runs=[(332.42,18),(25.11,15),(295.96,6),(168.18,8)]
others={'wat':(138.27,1),'gas':(152,2),'pow':(72.88,4),'tel':(74.43,4)}
print('nominal pipe vol CF', sum(L*math.pi/4*(d/12)**2 for L,d in runs))
for d in range(0,13):
    c=sum(L*math.pi/4*((D+d)/12)**2 for L,D in runs)
    s=sum(L*((D+d)/12)**2 for L,D in runs)
    print(f'delta {d}in circle {c:8.1f} CF {c/27:6.2f} CY | square {s:8.1f} CF {s/27:6.2f} CY')
# bedding below pipe of thickness t across width W plus pipe
pv=sum(L*math.pi/4*(D/12)**2 for L,D in runs)
for W in (2,2.5,3):
  for t in (2,3,4,6):
    b=821.67*W*t/12
    print('W',W,'t',t,'bed',round(b,1),'pipe+bed CY',round((b+pv)/27,2),'bed CY',round(b/27,2))
# OD+18in width bedding 4in + pipe
v=sum(L*(((D/12)+1.5)*(4/12)+math.pi/4*(D/12)**2) for L,D in runs); print('ODwidth 4in bed+pipe CY',v/27)
