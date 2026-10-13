import math
rect={'8x10':31.1,'14x12':7.3,'20x12':94.4,'24x12':13.3,'16x12':41.4,'10x10':7.4,'8x8':10.6,'12x12':9.8}
rnd={8:113.7,6:18.0,10:10.5,14:10.2}
sfr={k:lf*2*sum(map(int,k.split('x')))/12 for k,lf in rect.items()}
sfo={d:lf*math.pi*d/12 for d,lf in rnd.items()}
R=sum(sfr.values()); O=sum(sfo.values()); T=R+O
print('rect',round(R,2),'round',round(O,2),'total',round(T,2),'lbs',round(T*0.906,2))
r26=sum(v for k,v in sfr.items() if max(map(int,k.split('x')))<=12); r24=R-r26
print('rect26 SF',round(r26,2),'rect24 SF',round(r24,2),'26ga SF total',round(r26+O,2))
g26=(r26+O)*0.906; g24=r24*1.156
print('gauge only: %.1f @26 + %.1f @24 = %.1f (%+.1f%% vs 1200)'%(g26,g24,g26+g24,(g26+g24)/1200*100-100))
s26=(r26*1.15+O*1.10)*0.906; s24=r24*1.156*1.15
print('with seams: %.1f + %.1f = %.1f (%+.1f%%)'%(s26,s24,s26+s24,(s26+s24)/1200*100-100))
print('seams only 26ga: %.1f (%+.1f%%)'%((R*1.15+O*1.10)*0.906,((R*1.15+O*1.10)*0.906)/1200*100-100))
print('1200*1.15=',1200*1.15)
print('with seams + 5%% waste gauge: %.1f'%((s26+s24)*1.05))
print('1324.81*0.906=',round(1324.81*0.906,2))
