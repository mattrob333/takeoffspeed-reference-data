F=lambda f,i=0: f+i/12
wins={'A':(F(12,11.5),12,1),'C':(F(7,4),12,1),'D':(8,F(9,4),1),'E':(6,F(7,4),2),'G':(F(13,4),F(9,4),1),'H':(14,F(9,4),1)}
wp=sum(2*(w+h)*n for w,h,n in wins.values()); print('window perims (1 side, 4 sides)',wp)
wp3=sum((w+2*h)*n for w,h,n in wins.values()); print('window head+jambs',wp3)
# doors: interior B x5, C x1, F sliding 3'4"x7' x1 ; exterior pair 6x8 x2 (one with auto), single 3x8 x1
intd=[(3,7)]*6+[(F(3,4),7)]
extd=[(6,8),(6,8),(3,8)]
d1=sum(w+2*h for w,h in intd); print('int doors 1 side',d1,'2 sides',2*d1)
de=sum(w+2*h for w,h in extd); print('ext doors int side',de)
print('total A', wp+2*d1+de, 'total B', wp3+2*d1+de)
