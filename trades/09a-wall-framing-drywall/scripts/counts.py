import math, itertools
EST={308:{'2-0':35,'3-0':56,'3-9':6,'12-6':101,'18-8':6},309:{'4-4':14,'12-6':50},310:{'9-0':4,'12-3':7,'18-8':6},
     311:{'1-7':35,'2-7':29,'4-0':10,'4-7':73,'7-2':5,'12-9':68,'15-9':38}}
ROWS={308:{'12-6':[34.2,49.9,3.7,46.0],'3-9':[7.7],'18-8':[8.4],'3-0':[74.0],'2-0':[45.3]},
      309:{'12-6':[28.4,36.7],'4-4':[18.3]},
      310:{'9-0':[5.9],'12-3':[9.2],'18-8':[8.4]},
      311:{'1-7':[46.0],'2-7':[38.0],'4-0':[13.0],'4-7':[96.6],'7-2':[5.9],'12-9':[89.7],'15-9':[41.5,8.7]}}
rhu=lambda x: math.floor(x+0.5+1e-9)
rules={'ceil(sum*0.75)':lambda r:math.ceil(round(sum(r)*.75,9)),'round(sum*0.75)':lambda r:rhu(sum(r)*.75),
 'sum ceil(row*0.75)':lambda r:sum(math.ceil(round(x*.75,9)) for x in r),'sum round(row*0.75)':lambda r:sum(rhu(x*.75) for x in r),
 'round(sum/1.33)':lambda r:rhu(sum(r)/1.33),'ceil(sum/1.33)':lambda r:math.ceil(sum(r)/1.33),'floor(sum*.75)+1':lambda r:math.floor(sum(r)*.75)+1}
NG=sum(len(v) for v in ROWS.values())  # 17 height groups (5+2+3+7)
for name,f in rules.items():
    miss=[(n,h,f(r),EST[n][h]) for n in ROWS for h,r in ROWS[n].items() if f(r)!=EST[n][h]]
    print(f'{name:22s} matches {NG-len(miss)}/{NG} mismatches {len(miss)}/{NG}', miss)
