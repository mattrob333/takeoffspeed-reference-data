import math
r=lambda x,n=6: round(x,n)
A16=1.39  # estimator 2dp circle area
print('675 at 3.0 x5', r(A16*3*5/27), ' x6', r(A16*3*6/27), ' 6th pier', r(A16*3/27))
print('civil 24in x 3.0 x5', r(math.pi*1*3*5/27,3), '(old 1.744 check)')
print('civil 24in x 4.0 x5', r(math.pi*1*4*5/27,3), ' x 4.25 x5', r(math.pi*1*4.25*5/27,3))
print('civil 24in x 4.0 x6', r(math.pi*1*4*6/27,3), ' x 4.25 x6', r(math.pi*1*4.25*6/27,3))
print('714 at 4.0', r(A16*4*8/27), ' at 4.25', r(A16*4.25*8/27), 'pct', r((4.25/4-1)*100,2), 'exact pi 4.25', r(math.pi*(16/12/2)**2*4.25*8/27,4))
print('exact pi 4.0', r(math.pi*(16/12/2)**2*4*8/27,4))
print('A-190 back wall dims sum in', 28+43+45+36+24, 'ft', (28+43+45+36+24)/12)
print('expansion 1835/25', 1835/25, ' control 5ft 5ft walk lines', 1835/5/5, 'LF', 1835/5)
h=[7.09,2.07,4.57,7.05,7.05,7.05,7.07,7.07,7.07,5.82,3.32,0.83]
print('hatch 0.72pt', round(sum(h),2), len(h), '+36', round(sum(h)+36,2), round(97.48/(sum(h)+36),3), '+46', round(sum(h)+46,2), round(97.48/(sum(h)+46),3))
rv=h+[0.35,0.66,0.76,1.13]; print('incl 0.12pt strokes', round(sum(rv),2), len(rv))
print('crosswalk', round(79.46/85,3))
