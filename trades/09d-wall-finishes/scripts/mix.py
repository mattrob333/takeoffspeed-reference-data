est={'WT-1':144.19,'WT-2':46.72,'WT-9':53.22}
mix={'WT-1':0.60,'WT-2':0.20,'WT-9':0.20}
tot=sum(est.values()); print('band total',round(tot,2))
for k in est: r=tot*mix[k]; print(k,'mix-derived',round(r,2),'est',est[k],'delta%',round((r-est[k])/est[k]*100,2),'actual share',round(est[k]/tot*100,1))
# per location
loc={'A-410 restrooms (x2)':(120.7,43.8,50.6),'A-703 service counter':(15.3,1.4,1.3),'A-705 employee lounge':(8.2,1.6,1.3)}
for k,v in loc.items(): s=sum(v); print(k,round(s,2),[round(x/s*100,1) for x in v])
# backsplash geometry
bs703=(6+9/12)*(32/12); bs705=(2*3+4*3/12+2/12)*(1+6.5/12)
print('A-703 6\'-9\" x 32\" =',round(bs703,3),'legend',15.3+1.4+1.3)
print('A-705 7\'-2\" x 1\'-6.5\" =',round(bs705,3),'legend',round(8.2+1.6+1.3,2))
print('WT3 10\'-4 3/8\" x 3\'-8 1/2\" =',round((10+4.375/12)*(3+8.5/12),3))
print('FRP 2x(24in/12) x 4 =',2*2*4)
print('WC1 10.1x12=',round(10.1*12,2),' 10x12=',10*12,' PT7 WC 10.3x10=',round(10.3*10,2))
