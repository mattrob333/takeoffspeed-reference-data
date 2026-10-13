import itertools, math
runs = {'st18':332.42,'st15':25.11,'san6':295.96,'gas':152.0,'hdr8':168.18,'wat1':138.27,'pow':72.88,'tel':74.43,'ud6':96.0}
targets = {'exc':12330,'bf':11196,'haul':1134}
areas = sorted(set([a*b for a in [1,1.5,2,2.5,3,3.5,4,4.5,5,6] for b in [1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,7,8]]))
keys=list(runs)
res=[]
for r in range(1,len(keys)+1):
    for sub in itertools.combinations(keys,r):
        L=sum(runs[k] for k in sub)
        for mode,Lv in (('raw',L),('round',round(L)),('ceil',math.ceil(L)),('sumround',sum(round(runs[k]) for k in sub))):
            for t,tv in targets.items():
                for A in areas:
                    if abs(Lv*A-tv)<=0.5:
                        res.append((t,sub,mode,Lv,A,Lv*A))
for x in res: print(x)
