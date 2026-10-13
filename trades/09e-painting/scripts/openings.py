from itertools import product
def ft(f,i=0): return f+i/12
win={'A':(ft(12,11.5),12,1),'C':(ft(7,4),12,1),'D':(8,ft(9,4),1),'E':(6,ft(7,4),2),'G':(ft(13,4),ft(9,4),1),'H':(14,ft(9,4),1)}
wper=sum(2*(w+h)*n for w,h,n in win.values()); print('window perimeters',round(wper,2))
whead_jamb=sum((w+2*h)*n for w,h,n in win.values()); print('window head+jambs',round(whead_jamb,2))
doors_int={'HM 3x7':(3,7,6),'F slider 3-4x7':(ft(3,4),7,1),'int SF pair 6x8':(6,8,1)}
doors_ext={'ext pair 6x8':(6,8,1),'E 3x8':(3,8,1)}
def dper(d): return sum((w+2*h)*n for w,h,n in d.values())
print('int door 1 side',dper(doors_int),'ext door 1 side',dper(doors_ext))
hm=3+14; print('HM frames 6 x 2 sides x 17 =',6*2*17)
tot1 = wper + 2*dper(doors_int) + dper(doors_ext)
print('win perim + int doors both sides + ext doors 1 side', round(tot1,2))
tot2 = wper + dper(doors_int)+dper(doors_ext); print('all one side', round(tot2,2))
print('910/tot2',910/tot2,'1330/tot2',1330/tot2,'1330/910',1330/910)
