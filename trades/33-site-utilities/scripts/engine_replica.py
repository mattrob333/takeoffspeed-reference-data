import math
storm=[(17.69,438.40,435.09,435.82,435.00,18,21),(45.97,440.00,435.32,438.40,435.09,18,21),(92.25,439.20,435.55,438.40,435.09,18,21),(85.26,438.85,435.74,440.00,435.32,18,21),(70.17,439.20,435.90,439.20,435.55,18,21),(25.11,435.67,435.00,438.25,434.87,15,17.7),(21.08,438.01,434.86,438.40,434.75,18,21)]
san=[(49.92,439.06,432.35,438.31,431.85),(92.03,439.39,433.27,439.06,432.35),(14.14,439.66,433.41,439.39,433.27),(90.70,439.96,434.32,439.66,433.41),(14.14,439.86,434.46,439.96,434.32),(23.03,440.12,434.69,439.86,434.46),(12.00,440.37,434.81,440.12,434.69)]
def run(L,rs,is_,re,ie,idi,od,below=4,cover=12):
    w=max(od+24,1.25*od+12,24)/12
    wall=max((od-idi)/2,0)
    d=((rs-is_)+(re-ie))/2+(wall+below)/12
    exc=L*w*d/27; pipe=L*math.pi/4*(od/12)**2/27
    zone=min((below+od+cover)/12,d); bed=L*w*zone/27-pipe
    return exc,bed,pipe,w,d
tot={}
for name,rows in (('storm',[(r[0],r[1],r[2],r[3],r[4],r[5],r[6]) for r in storm]),('san',[(r[0],r[1],r[2],r[3],r[4],6,6.275) for r in san])):
    e=b=p=0
    for r in rows:
        x=run(*r); e+=x[0]; b+=x[1]; p+=x[2]
    tot[name]=(e,b,p); print(name,'exc',round(e,2),'bedding',round(b,2),'pipe',round(p,2),'backfill',round(e-b-p,2),'haul',round(b+p,2))
E=sum(v[0] for v in tot.values()); B=sum(v[1] for v in tot.values()); P=sum(v[2] for v in tot.values())
print('total exc',round(E,4),'bed',round(B,4),'backfill',round(E-B-P,4),'haul',round(B+P,4))
print('vs estimator exc',round((E-456.666667)/456.666667*100,2),'% ; haul', round((B+P-42)/42*100,1),'%; backfill',round((E-B-P-414.666667)/414.666667*100,1))
print('est-mode engine', 456.4833, (456.4833-456.666667)/456.666667*100, 429.2586,(429.2586-414.666667)/414.666667*100, 27.2247,(27.2247-42)/42*100)
