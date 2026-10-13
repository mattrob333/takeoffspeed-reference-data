import math
# Brick veneer: reference line 32 = 400 SF; legends 163.6 + 232.1 = 395.7
sf=400.0
net=675*sf/100; waste5=net*1.05
print('brick net',net,'with5%',waste5)
mort_cf=5.5*sf/100
print('mortar net cf',mort_cf,'+15%',mort_cf*1.15,'+25%',mort_cf*1.25, 'via per-1000', 8.1*net/1000)
print('legend sum',163.6+232.1)
# ties
for name,v,h in [('drawing 16x32',16,32),('spec 18x24',18,24)]:
    a=v*h/144; print(name,'sf/tie',round(a,3),'ties/400sf',round(sf/a,1))
print('1 per 2 sf',sf/2)
print('BIA steel stud max 2.67 sf ->',round(sf/2.67,1),'; recommended 2.0 ->',sf/2.0)
# rowlock lines
print('rowlock sum legends',61.4+87.9,'ref',149.33)
# CMU 8x8x16: face area
face=8*16/144; print('face sf',face,'units/100sf net',100/face,'+5%',100/face*1.05)
cmu=289.76
print('cmu units net',cmu/face,'+5%',cmu/face*1.05, 'TEK 119/100',119*cmu/100)
g32=9.1*cmu/100; print('grout 32 o.c. cf',g32,'cy',g32/27,' @16:',18.1*cmu/100/27,' @8:',36.1*cmu/100/27)
ref_g=3.245312*27; ref_m=1.797585*27
print('ref grout cf',ref_g,'per100sf',ref_g/cmu*100,'ref mortar cf',ref_m,'per 100sf',ref_m/cmu*100)
# TEK: 1 ton sand (25 cf) lays 240 conventional units
print('mortar cf est from sand rule', cmu/face*1.05/240*25)
print('grout bag count 8in vertical: cores',(g32/0.66))
# bag yields: 80-lb preblended mortar 16 units/bag
print('80lb mortar bags',cmu/face*1.05/16)
# veneer weep count formula example 100 LF at 24 o.c.
print('weeps for 149.33 LF @24', math.ceil(149.33/2))
