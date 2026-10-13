import math
def fi(f,i=0): return f+i/12
EST={308:2180.195,309:897.989,310:322.77,311:2652.875}
CNT={308:{(2,0):35,(3,0):56,(3,9):6,(12,6):101,(18,8):6},
     309:{(4,4):14,(12,6):50},
     310:{(9,0):4,(12,3):7,(18,8):6},
     311:{(1,7):35,(2,7):29,(4,0):10,(4,7):73,(7,2):5,(12,9):68,(15,9):38}}
RUN={308:270.5,309:84.3,310:24.0,311:341.0}
for n,c in CNT.items():
    for sp_name,sp in [('4/3',4/3),('1.33',1.33),('1.333',1.333)]:
        sf=sum(k*fi(*h)*sp for h,k in c.items())
        print(n,sp_name,'count*sp*H =',round(sf,4),'est',EST[n],'d%',round((sf/EST[n]-1)*100,3))
    lf=sum(k*4/3 for k in c.values())
    print(n,'sum count*4/3 LF',round(lf,3),'runner',RUN[n],' sum counts',sum(c.values()))
