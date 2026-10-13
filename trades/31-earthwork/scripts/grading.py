rows=[('440',0,51.72),('440',1.78,151.02),('440',0,224.56),('440',0,199),('440',0,2.11),('440',0,12.81),
('439.5',61.2,84.11),('439.5',15.69,0),('439',27.56,37.98),('439',58.96,18.35),('438',47.33,4.59),('437',25.2,0),('436.5',238.52,0),('435',158.17,0)]
cut=sum(r[1] for r in rows); fill=sum(r[2] for r in rows)
print('cut',round(cut,4),'fill',round(fill,4),'net',round(fill-cut,4))
# per row net check vs printed Qty
qty=[51.72,149.24,224.56,199,2.11,12.81,22.91,-15.69,10.42,-40.61,-42.74,-25.2,-238.52,-158.17]
print('row nets ok', all(abs((r[2]-r[1])-q)<0.005 for r,q in zip(rows,qty)), round(sum(qty),4))
# page 73 legend areas (SF)
prop={'440':[20233.7],'439.5':[3841.3,498.8],'439':[4284.7],'436.5':[2167.8],'435':[967.6],'438':[716.1],'437':[438.2]}
exist={437.5:2991.5,439.5:11373.4,441.0:5128.9,440.0:1531.8,438.5:16957.7,439.0:3080.6}
Ap=sum(sum(v) for v in prop.values()); Ae=sum(exist.values())
print('proposed SF',round(Ap,1),'existing SF',round(Ae,1),'existing mean elev',round(sum(z*a for z,a in exist.items())/Ae,3))
grp={}
for z,c,f in rows: grp.setdefault(z,[0,0]); grp[z][0]+=c; grp[z][1]+=f
for z,(c,f) in grp.items():
    A=sum(prop[z]); net=(f-c)*27
    print(z,'SF',round(A,1),'cut',round(c,2),'fill',round(f,2),'net CF',round(net,1),'avg depth',round(net/A,3),'implied existing',round(float(z)-net/A,3))
# pond check
print('pond regions 435+436.5 SF', 967.6+2167.8, 'vs C-3.0 legend 23 stormwater pond 3074')
sumApz=sum(float(z)*sum(v) for z,v in prop.items())
print('area-weighted proposed elev',round(sumApz/Ap,3),'implied existing under proposed',round((sumApz-(fill-cut)*27)/Ap,3))
