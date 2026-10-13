FT=20/72
def area(q): return abs(sum(q[k][0]*q[(k+1)%len(q)][1]-q[(k+1)%len(q)][0]*q[k][1] for k in range(len(q))))/2*FT*FT
P=[(1306.2,1007.9),(1306.3,985.2),(1306.3,930.7),(1311.5,922.6),(1306.4,922.3),(1292.9,922.7),(1287.1,922.0),(1291.1,929.0),(1289.6,974.5),(1227.4,975.0),(1182.5,975.0),(1180.9,973.4),(1148.3,973.3),(1147.9,990.2),(1147.3,1001.0)]
full=P+[(1269.5,1007.8),(1269.5,1001.0),(1183.6,1000.3)]
print('5685 + bldg notch closure',round(area(full),1))
# split: ramp strip N of y=974.5 (x 1289.6-1306.3) and walk
ramp=[(1306.3,974.5),(1306.3,930.7),(1311.5,922.6),(1306.4,922.3),(1292.9,922.7),(1287.1,922.0),(1291.1,929.0),(1289.6,974.5)]
print('N-S ramp strip to y=974.5',round(area(ramp),1))
walk=[(1306.2,1007.9),(1306.3,974.5),(1289.6,974.5),(1227.4,975.0),(1182.5,975.0),(1180.9,973.4),(1148.3,973.3),(1147.9,990.2),(1147.3,1001.0),(1183.6,1000.3),(1269.5,1001.0),(1269.5,1007.8)]
print('walk', round(area(walk),1))
# reviewer's: close on y=1000.3-1001 straight
rv=P[1:]+[(1183.6,1000.3),(1306.3,1001.0)]
print('closed straight on y~1001 (east edge x=1306.3)', round(area(rv),1))
pad=(1007.3-993.6)*(892.4-882.2)*FT*FT; print('west pad',round(pad,1))
for c in (467.8, 383.6, 454.3): print(c, round((442.37-pad)/c*100-100,1), round((442.37)/(c+pad)*100-100,1))
good=P+[(1183.6,1000.3),(1269.5,1001.0),(1269.5,1007.8)]
g=area(good); print('5685 + building line closure (correct order)', round(g,1))
print('walk+ramp check', round(area(walk)+area(ramp),1))
print('estimator minus pad vs good', round((442.37-pad)/g*100-100,2), 'total vs good+pad', round(442.37/(g+pad)*100-100,2), 'good+pad', round(g+pad,1))
