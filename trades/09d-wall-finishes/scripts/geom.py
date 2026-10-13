FT=36.0  # pt per ft at 1/2"=1'-0" on a 36x24in sheet (2592x1728 pt)
h=(570.9-372.7)/FT
B=(850.8-580.5)/FT; C=(1313.3-1037.0)/FT
D_left=(1662.2-1518.0)/FT; D_right=(1794.3-1782.3)/FT; door=(1782.3-1662.2)/FT
print('h',round(h,3),'B',round(B,3),'C',round(C,3),'Dl',round(D_left,3),'Dr',round(D_right,3),'door',round(door,3))
room=(B+C+D_left+D_right)*h
print('per room gross tile SF',round(room,2),'x2',round(2*room,2))
p16=120.7+43.8+50.6
print('p16 WT1+WT2+WT9',round(p16,2),'delta%',round((p16-2*room)/(2*room)*100,2))
print('shares',[round(x/p16*100,1) for x in (120.7,43.8,50.6)])
