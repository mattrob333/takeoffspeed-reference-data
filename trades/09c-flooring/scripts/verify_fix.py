# Recompute the figures changed by the review fixes (09c-flooring)
PT=18.0
door106_clear=(1078.0-1024.0)/PT; door106_oof=(1081.0-1021.0)/PT
door110=(321.2-264.1)/PT; door100=(933.5-824.1)/PT
wall106=(441.7-432.8)/PT
room=((1140.1-1018.0)/PT)*((637.4-440.9)/PT)
mat=((1080.6-1044.6)/PT)*((608.6-554.6)/PT)
def d(q,e): return (q-e)/e*100
print('door106 clear',round(door106_clear,3),'outside-frame',round(door106_oof,3),'110',round(door110,3),'100',round(door100,3),'half wall',round(wall106/2,4))
fts3=door106_clear+door110+door100; print('FTS-3',round(fts3,3),'%+.2f'%d(fts3,12.24))
fts3_fixture=3.00+3.17+6.08; print('FTS-3 fixture 3.00+3.17+6.08',round(fts3_fixture,2),'%+.2f'%d(fts3_fixture,12.24))
strip=door106_clear*wall106/2; con=room-mat+strip
print('room',round(room,2),'mat',round(mat,2),'strip',round(strip,3),'CON-1',round(con,2),'%+.2f'%d(con,68.78))
print('cross-check CON-1+MAT drawn 68.8+6.0=',68.8+6.0,' room+strip',round(room+strip,2))
# A-410 plan dims
mw=7+8/12; md=7+8.125/12; ww=7+6.375/12; door=3.0; elA=7+3.5/12
per=2*(mw+md)+2*(ww+wd) if False else 2*(mw+md)+2*(ww+md)
print('perimeters',round(per,3),'net 3 doors',round(per-3*door,3),'%+.2f'%d(per-3*door,51.87),'net 2 doors',round(per-2*door,3),'%+.2f'%d(per-2*door,51.87))
top=[mw,md,mw-door,ww,md,ww-door]; T=sum(top)
print('top trim plan dims',[round(x,3) for x in top],round(T,3),'%+.2f'%d(T,39.55))
old=2*(7.508+7.675+4.006+0.333); print('old top trim elev scaled',round(old,3),'%+.2f'%d(old,39.55))
wt8_plan=(md-door)+md; wt8_elev=(elA-door)+elA; wt8_runs=elA+3.67+0.22
print('WT-8 runs',round(wt8_runs,3),'%+.2f'%d(wt8_runs,11.28),'by elevation width',round(wt8_elev,3),'%+.2f'%d(wt8_elev,11.28),'by plan depth',round(wt8_plan,3),'%+.2f'%d(wt8_plan,11.28))
cove=T+wt8_plan; print('cove = top-trim walls + WT-8 walls (plan)',round(cove,3),'%+.2f'%d(cove,51.87))
cove_e=T+wt8_runs; print('cove = top trim plan + WT-8 measured runs',round(cove_e,3),'%+.2f'%d(cove_e,51.87))
print('old candidates 39.04+11.28',round(39.04+11.28,2),'%+.2f'%d(39.04+11.28,51.87))
print('engine gap: band-only cove',round(T,2),'vs 51.87 =',round(T-51.87,2),'%+.2f'%d(T,51.87),'; with WT-8 walls +',round(wt8_plan,2))
print('grout scope',round(144.19+46.72+53.22,2),round(144.19+46.72+38.42+53.22,2),'ratio',round(300/244.13,3),'1.10x',round(244.13*1.1,2))
