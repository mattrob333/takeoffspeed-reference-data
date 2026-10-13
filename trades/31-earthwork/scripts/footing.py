# Building footing excavation / backfill / haul reconstruction (lines 629-631)
F=[('F30',3,3,1,3),('F38',3+8/12,3+8/12,1,3),('F50',5,5,14/12,6),('F60',6,6,16/12,1),('F70',7,7,16/12,1),('F7040',7,4,16/12,1),('F10050',10,5,14/12,1)]
TOF=2.0   # S-201: top of footing [-2'-0"] below finish floor
WF_LF, WF_W, WF_T = 124.2, 2.0, 1.0
WS_WALL, WS_PAD = 1.0, 0.5
rows=[]
wf_cf = WF_LF*(WF_W+2*WS_WALL)*(WF_T+TOF)
rows.append(('WF20', f'{WF_LF} x ({WF_W}+2x{WS_WALL}) x ({WF_T}+{TOF})', wf_cf))
pad_cf=0
for n,L,W,T,c in F:
    v=(L+2*WS_PAD)*(W+2*WS_PAD)*(T+TOF)*c
    pad_cf+=v
    rows.append((n, f'{c} x ({L:.4f}+1) x ({W:.4f}+1) x ({T:.4f}+2)', v))
for r in rows: print(f'{r[0]:7s} {r[1]:45s} {r[2]:9.3f} CF {r[2]/27:8.4f} CY')
exc=(wf_cf+pad_cf)/27
print('pads CY',round(pad_cf/27,4),'WF CY',round(wf_cf/27,4),'EXCAVATION CY',round(exc,4),'est 119.8 delta%',round((exc/119.8-1)*100,3))
conc={19:9.196296,20:1.0,21:1.496544,22:6.5,23:1.773333,24:2.413704,25:1.379259,26:2.166667,27:9.628148,28:0.522593}
c=sum(conc.values())
print('estimator concrete (lines 19-28) CY',round(c,6))
bf=exc-c; haul=exc-bf
print('BACKFILL',round(bf,4),'delta%',round((bf/83.7-1)*100,3),'| from rounded exc',round(119.8-c,4))
print('HAUL',round(haul,4),'delta%',round((haul/36.1-1)*100,3))
# nominal concrete from schedule (exact dims), for the app
ftg_nom=(WF_LF*WF_W*WF_T+sum(L*W*T*c for n,L,W,T,c in F))/27
stem_nom=(193.8*8/12*2+8.4*10/12*2)/27
print('nominal footing',round(ftg_nom,4),'nominal stem (legend LF)',round(stem_nom,4),'sum',round(ftg_nom+stem_nom,4),'haul delta% nominal',round(((ftg_nom+stem_nom)/36.1-1)*100,3),'backfill nominal',round(exc-ftg_nom-stem_nom,4),round(((exc-ftg_nom-stem_nom)/83.7-1)*100,3))
# alternatives (sensitivity)
def total(ws_wall, ws_pad, tof=TOF):
    return (WF_LF*(WF_W+2*ws_wall)*(WF_T+tof)+sum((L+2*ws_pad)*(W+2*ws_pad)*(T+tof)*c for n,L,W,T,c in F))/27
print('1ft both sides everywhere',round(total(1,1),4),'6in everywhere',round(total(0.5,0.5),4),'neat (0)',round(total(0,0),4))
# F38 note: one F38 tagged [-1'-0"] (top of footing 1 ft below FF) - estimator used -2'-0" for all
print('if one F38 at -1-0',round(exc-((3+8/12+1)**2*1)/27,4))
# displaced by slab+gravel in the top 8" of the dig (excavation measured from FF)
plan_sf=WF_LF*(WF_W+2*WS_WALL)+sum((L+1)*(W+1)*c for n,L,W,T,c in F)
print('excavated plan SF',round(plan_sf,2),'top 8in (4in slab + 4in gravel) CY',round(plan_sf*8/12/27,4))
# 4in CMU below grade (line 31) not deducted from backfill
print('4in CMU below grade line31 CY',round(209.475*3.625/12/27,4))
# footing-only excavation ratio
print('exc per CY concrete',round(119.8/c,4))
