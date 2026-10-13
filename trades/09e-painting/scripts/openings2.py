def ft(f,i=0): return f+i/12
ext_win={'A':(ft(12,11.5),12,1),'C':(ft(7,4),12,1),'D':(8,ft(9,4),1),'E':(6,ft(7,4),2),'G':(ft(13,4),ft(9,4),1),'H':(14,ft(9,4),1),'B':(ft(9,11),12,1),'F':(6,10,1)}
int_win={'J':(ft(7,8.25),12,1),'K':(ft(7,7.625),10,1)}
doors_int={'HM 3x7':(3,7,6),'F slider':(ft(3,4),7,1),'int SF pair 6x8':(6,8,1)}
doors_ext={'ext pair 6x8':(6,8,1),'E 3x8':(3,8,1)}
P=lambda d: sum(2*(w+h)*n for w,h,n in d.values())
U=lambda d: sum((w+2*h)*n for w,h,n in d.values())
r={}
r['ext win perim (8 types)']=P(ext_win)
r['int win perim (J,K)']=P(int_win)
r['int doors 3-side']=U(doors_int)
r['ext doors 3-side']=U(doors_ext)
for k,v in r.items(): print(k, round(v,2))
c1=r['ext win perim (8 types)']+2*r['int win perim (J,K)']+2*r['int doors 3-side']+r['ext doors 3-side']
print('ext win 1 face + int win 2 faces + int doors 2 faces + ext doors 1 face =',round(c1,2))
c2=2*(r['ext win perim (8 types)']+r['int win perim (J,K)']+r['int doors 3-side']+r['ext doors 3-side'])
print('everything 2 faces =',round(c2,2))
c3=r['ext win perim (8 types)']+r['int win perim (J,K)']+r['int doors 3-side']+r['ext doors 3-side']
print('everything 1 face =',round(c3,2), ' x2', round(2*c3,2), ' x3',round(3*c3,2))
print('1330/c1',1330/c1,'910/c1',910/c1)
