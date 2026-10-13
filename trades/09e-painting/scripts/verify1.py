import math
sof=[(4.2,7.0),(2.7,4),(6.7,1.5),(30.5,3),(35.3,2.5),(28.1,2)]
s=sum(a*b for a,b in sof); print('soffit both-sides', round(s,4))
s1=sum(a*b for a,b in [(4.2,3.5)]+sof[1:]); print('soffit one-sided', round(s1,4), 'diff', round(s-s1,4))
print('516.1+s', round(516.1+s,4), 'vs 802 pct', round((516.1+s-802)/802*100,4))
print('516+286.04', 516+286.04, 'line285 vs s pct', round((s-286.04)/286.04*100,4))
print('516.1+271.5',516.1+271.5)
# F9
c5=lambda x:5*math.ceil(x/5-1e-12)
rows=[(37.2,40),(103.0,105),(74.0,75),(98.4,100),(44.2,45),(9.7,10),(38.4,40),(76.2,77),(802.04,802),(121.2,120),(103.0,103)]
fits=0
for r,c in rows:
    f=c5(r)==c; fits+=f; print(r,c,c5(r),f)
print('fits',fits,'of',len(rows))
print('10.1*12',10.1*12,'10.3*10',10.3*10, 'nearest5(121.2)',5*round(121.2/5),'floor5',5*math.floor(121.2/5))
# 304
print('910-910',910-910, '901.83 vs 910', round((901.83-910)/910*100,3))
# PT-4
print('10.6-9.8125', round(10.6-(9+9.75/12),4), 'tech wall width ft', 9+9.75/12, '403/41.35', round(403/41.35,3))
