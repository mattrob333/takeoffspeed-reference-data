import json, math, csv
OUT='/home/user/takeoffspeed-reference-data/trades/03-masonry/'
L={x['lineNo']:x for x in json.load(open('/home/user/takeoffspeed-reference-data/reference/estimate/lines.json'))}
ceil_to=lambda v,s: math.ceil(round(v/s,9))*s
def d(a,b): return (a-b)/b*100
# sources
cmu_lf=157.4; cmu_h_txt="1'-4\""; cmu_h2=1.33; cmu_h=16/12
brick=[163.6,232.1]; hr=[61.4,87.9]; rs=[61.5,88.3]
r={}
cmu_lf_r=ceil_to(cmu_lf,0.5)
r[31]=round(cmu_lf_r*cmu_h2,6); phys31=cmu_lf*cmu_h
bsum=round(sum(brick),4); r[32]=ceil_to(bsum,5)
r[33]=round(sum(hr),4); r[34]=round(sum(rs),4); r[35]=r[32]
print('31',cmu_lf_r,r[31],d(r[31],L[31]['quantity']),'phys',phys31,d(phys31,L[31]['quantity']),'raw*1.33',cmu_lf*1.33,d(cmu_lf*1.33,L[31]['quantity']))
print('32',bsum,r[32],d(r[32],400),'raw',d(bsum,400))
print('33',r[33],d(r[33],L[33]['quantity']));print('34',r[34],d(r[34],L[34]['quantity']))
# cross checks
fieldH=32/12
print('field-height check: rowlock LF x 2.667 =',sum(hr)*fieldH, d(sum(hr)*fieldH,400))
print('avg measured height', bsum/sum(hr), bsum/sum(rs))
print('per elevation avg h', [round(b/h,4) for b,h in zip(brick,hr)])
print('cmu LF - rowlock LF', cmu_lf-sum(hr), (cmu_lf-sum(hr))/cmu_lf*100)
print('brick units modular 144/(8*8/3)=',144/(8*8/3),'x400=',400*144/(8*8/3),'x395.7=',bsum*6.75)
print('rowlock units/LF 12/(8/3)=',12/(8/3),' x149.86=',149.86*4.5,' half rowlock 149.33*4.5=',149.33*4.5, 'full bricks if 2 halves per brick', 149.33*4.5/2)
print('ties drawing 32x16: per SF',144/(32*16),' 400SF->',400*144/(32*16),' SF/tie',32*16/144)
print('ties spec spacing 24x18:',400*144/(24*18),' SF/tie',24*18/144,'  spec min 1/2SF:',400/2)
print('ties TMS 2.67:',400/2.67)
print('CMU 4x8x16 units 1.125/SF x 209.475 =',209.475*1.125,' courses',16/8)
print('grout solid 4in engine 0.11 CF/SF:',209.475*0.11,'CF',209.475*0.11/27,'CY')
print('weeps base flashing 149.33 LF @24:',math.ceil(149.33*12/24)+1)
print('engine veneer net=395.7 ties',bsum*144/(32*16))
json.dump({'r':r,'phys31':phys31},open('/home/user/work/03-masonry/results.json','w'))
