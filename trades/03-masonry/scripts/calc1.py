b=[163.6,232.1]; hr=[61.4,87.9]; rs=[61.5,88.3]; tw=[101.6,111.5]
print('brick',sum(b),'hr',sum(hr),'rs',sum(rs),'thru-wall',sum(tw))
print('brick/hr LF height', sum(b)/sum(hr), 'brick/rs',sum(b)/sum(rs))
print('per page height', b[0]/hr[0], b[1]/hr[1])
print('400/149.33',400/149.33)
print('CMU 157.4*4/3',157.4*4/3,' 157.5*1.33',157.5*1.33,' 209.475/1.33',209.475/1.33,' 209.475*3/4',209.475*0.75)
print('delta cmu legend',(157.4*4/3-209.475)/209.475*100, (157.4*1.33-209.475)/209.475*100)
print('delta brick',(sum(b)-400)/400*100,'hr',(sum(hr)-149.33)/149.33*100,'rs',(sum(rs)-149.86)/149.86*100)
import math; print('ceil10',math.ceil(sum(b)/10)*10,'ceil50',math.ceil(sum(b)/50)*50,'ceil100',math.ceil(sum(b)/100)*100)
