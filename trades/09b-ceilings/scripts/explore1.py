import itertools
gwb=516.0; s=286.04
print('sheets',gwb/32, s/32)
print('adh',gwb*0.031, s*0.031)
print('tape',gwb*0.00075, s*0.00075)
print('screw',gwb*0.0375/7, s*0.0375/7, 40*0.0375/7)
print('mud',gwb*0.53, s*0.53)
print('studs',gwb/1.33, 429.599624*1.33, 429.599624*16/12)
# soffit rows: (LF, soffit height, gwb height)
rows={'3_6_BS':(4.2,3.5,None),'6_6_4':(2.7,6.5,4.0),'3_6_1_6':(6.7,3.5,1.5),'4_6_3':(30.5,4.5,3.0),'5_9_2_6':(35.3,5.75,2.5),'2H':(28.1,2.0,None)}
br={'br5':(27.1,5.0),'br8':(28.1,8.0)}
for k,(lf,h,g) in rows.items(): print(k, lf*h, lf*(g or 0), lf*h*2)
