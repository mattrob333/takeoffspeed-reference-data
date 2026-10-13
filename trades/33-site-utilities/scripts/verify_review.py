import math
srim={'S1':438.31,'S2':439.06,'S3':439.39,'S4':439.66,'S5':439.96,'S6':439.86,'S7':440.12,'S8':440.37}
sinv={'S1':431.85,'S2':432.35,'S3':433.27,'S4':433.41,'S5':434.32,'S6':434.46,'S7':434.69,'S8':434.81}
sanr=[('S1-S2',49.92,'S2',432.35,'S1',431.85),('S2-S3',92.03,'S3',433.27,'S2',432.35),('S3-S4',14.14,'S4',433.41,'S3',433.27),('S4-S5',90.70,'S5',434.32,'S4',433.41),('S5-S6',14.14,'S6',434.46,'S5',434.32),('S6-S7',23.03,'S7',434.69,'S6',434.46),('S7-S8',12.00,'S8',434.81,'S7',434.69)]
d=[];w=0;t=0
for n,L,u,iu,dn,idn in sanr:
    dep=((srim[u]-iu)+(srim[dn]-idn))/2+4/12; d.append(dep); w+=L*dep; t+=L; print(n,round(dep,2))
print('san run range',round(min(d),2),round(max(d),2),'weighted',round(w/t,3))
ri={k:round(srim[k]-sinv[k],2) for k in srim}; print('rim-inv',ri)
co={k:ri[k] for k in ['S2','S3','S4','S5','S6','S7']}; print('cleanouts rim-inv range',min(co.values()),max(co.values()))
rim={'A1':435.82,'A2':438.40,'A2.1':440.00,'A2.2':438.85,'A3':439.20,'A4':439.20,'B1':438.25,'B2':435.67,'C1':438.40,'C2':438.01}
storm=[('A1-A2',17.69,'A2',435.09,'A1',435.00),('A2-A2.1',45.97,'A2.1',435.32,'A2',435.09),('A2-A3',92.25,'A3',435.55,'A2',435.09),('A2.1-A2.2',85.26,'A2.2',435.74,'A2.1',435.32),('A3-A4',70.17,'A4',435.90,'A3',435.55),('B1-B2',25.11,'B2',435.00,'B1',434.87),('C1-C2',21.08,'C2',434.86,'C1',434.75)]
sd=[((rim[u]-iu)+(rim[dn]-idn))/2+4/12 for n,L,u,iu,dn,idn in storm]
print('storm range',round(min(sd),2),round(max(sd),2))
print('ceil/round 8.8',math.ceil(8.8),round(8.8),'ceil/round 821.67',math.ceil(821.67),round(821.67))
print('OD 21+18 in ft',(21+18)/12)
for W,D in [(3,5),(2.5,6),(2,7.5),(3.25,5)]:
    print(W,D,822*W*D/27)
san=[49.92,92.03,14.14,90.70,14.14,23.03,12.00]; print(repr(sum(san)),round(sum(san),2))
print('gas', 4.4/152*100, 4.4/156.4*100)
