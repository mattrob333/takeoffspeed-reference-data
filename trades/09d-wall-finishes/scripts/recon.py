est={235:144.19,236:46.72,237:38.42,238:53.22,239:120.0,240:103.0,241:16.0}
src={
235:[('p16 A-410 WT1 WALL TILE',120.7),('p27 A-703 WT1 WALL TILE',15.3),('p32 A-705 WT1 WALL TILE',8.2)],
236:[('p16',43.8),('p27',1.4),('p32',1.6)],
237:[('p23 A-700 WT3 TILE',38.4)],
238:[('p16',50.6),('p27',1.3),('p32',1.3)],
}
for k,v in src.items():
    s=round(sum(x for _,x in v),4); print(k,s,est[k],round((s-est[k])/est[k]*100,3))
for k,lf,h in [(239,10.1,12),(240,10.3,10),(241,4,4)]:
    s=lf*h; print(k,s,est[k],round((s-est[k])/est[k]*100,3), 'implied LF',est[k]/h)
