import math
# C-4.0 storm structures: rim, and pipes: (name, size_in, length, up_struct, dn_struct, inv_up, inv_dn)
rim={'A1':435.82,'A2':438.40,'A2.1':440.00,'A2.2':438.85,'A3':439.20,'A4':439.20,'B1':438.25,'B2':435.67,'C1':438.40,'C2':438.01}
storm=[('A1-A2',18,17.69,'A2','A1',435.09,435.00),('A2-A2.1',18,45.97,'A2.1','A2',435.32,435.09),
('A2-A3',18,92.25,'A3','A2',435.55,435.09),('A2.1-A2.2',18,85.26,'A2.2','A2.1',435.74,435.32),
('A3-A4',18,70.17,'A4','A3',435.90,435.55),('B1-B2',15,25.11,'B2','B1',435.00,434.87),('C1-C2',18,21.08,'C2','C1',434.86,434.75)]
# C-5.0 sanitary
srim={'S1':438.31,'S2':439.06,'S3':439.39,'S4':439.66,'S5':439.96,'S6':439.86,'S7':440.12,'S8':440.37}
san=[('S1-S2',6,49.92,'S2','S1',432.35,431.85),('S2-S3',6,92.03,'S3','S2',433.27,432.35),('S3-S4',6,14.14,'S4','S3',433.41,433.27),
('S4-S5',6,90.70,'S5','S4',434.32,433.41),('S5-S6',6,14.14,'S6','S5',434.46,434.32),('S6-S7',6,23.03,'S7','S6',434.69,434.46),('S7-S8',6,12.00,'S8','S7',434.81,434.69)]
OD={18:21.5/12,15:17.7/12,6:6.275/12}   # ASSUMED outside diameters (ft); verify against product submittal
def run(rows,rims,clear=1.0,bed=0.5):
    tot=0;disp=0;L=0
    for n,sz,l,u,d,iu,idn in rows:
        gu=rims[u];gd=rims[d]
        # depth = ground - invert + wall(approx OD-ID)/2 + bedding
        id_=sz/12; od=OD[sz]
        wall=(od-id_)
        hu=gu-iu+wall+bed; hd=gd-idn+wall+bed
        h=(hu+hd)/2
        w=od+2*clear
        v=l*w*h/27
        pd=l*math.pi*od**2/4/27
        tot+=v;disp+=pd;L+=l
        print(f'{n:10s} {sz:2d}" L={l:6.2f} avgH={h:5.2f} W={w:4.2f} CY={v:6.1f} disp={pd:5.1f}')
    return tot,disp,L
print('STORM'); a=run(storm,rim); print(a)
print('SAN'); b=run(san,srim); print(b)
print('total trench CY',a[0]+b[0],'pipe displacement CY',a[1]+b[1])
print('--- sloped Type C 1.5:1 above 5ft for sanitary (W + m*H, simple full slope)')
def sloped(rows,rims,m,clear=1.0,bed=0.5):
    t=0
    for n,sz,l,u,d,iu,idn in rows:
        id_=sz/12; od=OD[sz]; wall=od-id_
        h=((rims[u]-iu)+(rims[d]-idn))/2+wall+bed
        w=od+2*clear
        t+=l*h*(w+m*h)/27
    return t
for m in (0.75,1.0,1.5): print(m, round(sloped(san,srim,m),1), round(sloped(storm,rim,m),1))
# structure excavation example: 4ft dia MH / 2x2 grate inlets, simple: footprint (OD+2ft)^2 x depth
import math
for name,dia,depth in [('B1 JB 4ft dia',4.0,3.38+0.5+0.5),('B2 OCS 4ft dia',4.0,0.67+0.5+0.5)]:
    pass
# round structure: 4' dia precast wall ~5in -> OD 4.83 ft; excavation dia = OD+2*1ft
od=4.0+2*5/12
for d in (3.38,4.0):
    print('4ft dia structure excav CY',round(math.pi*((od+2)/2)**2*(d+0.67+0.5)/27,2), 'depth',d+0.67+0.5)
