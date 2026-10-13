import json, csv, math
from fractions import Fraction as F
OUT='/home/user/takeoffspeed-reference-data/trades/02-concrete/'
import os; os.makedirs(OUT, exist_ok=True)
L={l['lineNo']:l for l in json.load(open('/home/user/takeoffspeed-reference-data/reference/estimate/lines.json'))}
ft=lambda f,i=0: f+i/12
r2=lambda x: round(x,2)          # estimator's 2-decimal-feet convention
rows=[]; fx=[]
def add(no, short, source, sv, formula, rec, est_conv, cls, notes, fixture=None):
    e=L[no]['quantity']; d=(rec-e)/e*100
    dc=(est_conv-e)/e*100
    rows.append(dict(lineNo=no, description=short, unit=L[no]['unit'], estimatorQty=e, source=source, sourceValues=sv, formula=formula,
                     recomputedQty=round(rec,6), deltaPct=round(d,3), classification=cls,
                     notes=f"{notes} Estimator-convention rebuild = {est_conv:.6f} ({dc:+.3f}%)."))
    if fixture: fixture['expected']={'quantity':round(rec,6),'unit':L[no]['unit']}; fixture['estimatorQty']=e; fx.append(fixture)
    print(no, L[no]['unit'], e, round(rec,6), f"{d:+.3f}%", 'conv', round(est_conv,6), f"{dc:+.4f}%")

# 16 slab
add(16,'4" SOG w/ 6x6 W2.9xW2.9 WWF o/ vapor barrier o/ 4" gravel','markup p33 (S-201) teal area "4"THK. CONCRETE SLAB ON GRADE..."','area 1917.6 SQ FT','SF = measured slab area (no blockout deduction)',1917.6,1917.6,'measured',
    'One PlanSwift area over the whole building slab inside stem walls; SOG-4 (S-201 slab schedule). Gross bldg area 1892 SF (G-001) is a +1.35% cross-check.',
    {'name':'SOG-4 slab on grade area','formula':'slab_sf = sum(area_i)','inputs':{'areas':[{'value':1917.6,'unit':'SF'}]},'tolerancePct':0.5,'source':'line 16 / markup p33'})
# 17 isolation joint
add(17,'1/2" isolation joint','markup p33 medium-green "ISOLATION JOINT - 8/S680"','39.2 FT','LF = sum of traced column-blockout diamond sides',39.2,39.22,'measured',
    'Green diamonds around column base plates (8/S-680, NOMAFLEX); slab-edge 1/2" joint filler at stem walls (S-600) NOT included. Legend prints 1 decimal; estimator carried 39.22.',
    {'name':'Isolation joint at column blockouts','formula':'joint_lf = sum(run_i)','inputs':{'runs':[{'value':39.2,'unit':'LF'}],'type':'isolation','width':'1/2"'},'tolerancePct':0.5,'source':'line 17 / markup p33'})
# 18 saw cut
add(18,'1" saw-cut joint','markup p33 yellow "SAW-CUT JOINT - 3/S680"','364.1 FT','LF = sum of traced S.C.J. lines',364.1,364.11,'measured',
    'Depth label 1" = T/4 of 4" slab per 3/S-680. Pixel trace of the 9 yellow runs (5 E-W, 4 N-S) gives ~352 LF (-3.3%, dots hide parts) as an independent check.',
    {'name':'Saw-cut control joints','formula':'joint_lf = sum(run_i)','inputs':{'runs':[{'value':364.1,'unit':'LF'}],'type':'saw-cut','depthIn':{'value':1,'unit':'in','rule':'slab thickness / 4'}},'tolerancePct':0.5,'source':'line 18 / markup p33'})
# 19 WF20
wf=124.2
add(19,"2'Wx1'D continuous footing w/ (2) #6",'markup p33 periwinkle "WF20" + S-201 WALL FOOTING SCHEDULE',"124.2 FT; W 2'-0\"; T 1'-0\"",'CY = LF x W x D / 27',wf*2*1/27,124.15*2*1/27,'derived',
    'WF20 traced between spread-footing outlines (net, no overlap). Estimator LF 124.15 (legend shows 124.2).',
    {'name':'WF20 continuous footing concrete','formula':'cy = lf * width_ft * depth_ft / 27','inputs':{'lf':{'value':124.2,'unit':'LF'},'width':{'value':"2'-0\"",'ft':2},'depth':{'value':"1'-0\"",'ft':1}},'tolerancePct':1,'source':'line 19 / markup p33'})
# isolated footings
iso=[(20,'F30',3,(3,0),(3,0),(1,0),"3'x3'x1'D isolated ftg (4) #4 EW"),
     (21,'F38',3,(3,8),(3,8),(1,0),"3'8\"x3'8\"x1'D isolated ftg (5) #4 EW"),
     (22,'F50',6,(5,0),(5,0),(1,2),"5'x5'x1'2\"D isolated ftg (5) #5 EW"),
     (23,'F60',1,(6,0),(6,0),(1,4),"6'x6'x1'4\"D isolated ftg (7) #5 EW"),
     (24,'F70',1,(7,0),(7,0),(1,4),"7'x7'x1'4\"D isolated ftg (7) #6 EW"),
     (25,'F7040',1,(4,0),(7,0),(1,4),"7'x4'x1'4\"D isolated ftg (7)+(5) #6 T&B"),
     (26,'F10050',1,(5,0),(10,0),(1,2),"5'x10'x1'2\"D isolated ftg (9)+(5) #6 T&B")]
isoF=0; isoFconv=0
for no,tag,n,a,b,d,short in iso:
    A,B,D=ft(*a),ft(*b),ft(*d)
    rec=n*A*B*D/27; conv=n*r2(A)*r2(B)*r2(D)/27
    isoF+=n*2*(A+B)*D; isoFconv+=n*2*(r2(A)+r2(B))*r2(D)
    dims=f"{a[0]}'-{a[1]}\" x {b[0]}'-{b[1]}\" x {d[0]}'-{d[1]}\""
    add(no,short,f'markup p33 count "{tag}" + S-201 SPREAD FOOTING SCHEDULE',f'{n} EA; {dims}','CY = count x L x W x D / 27',rec,conv,'counted',
        f'Legend count {n} EA = schedule COUNT {n} = plan tags (text layer has {n}+1 incl. schedule row). Estimator rounds ft-in to 2-decimal feet ({r2(A)} x {r2(B)} x {r2(D)}).',
        {'name':f'{tag} isolated footing concrete','formula':'cy = count * L_ft * W_ft * D_ft / 27','inputs':{'count':{'value':n,'unit':'EA'},'L':{'value':f"{a[0]}'-{a[1]}\"",'ft':round(A,6)},'W':{'value':f"{b[0]}'-{b[1]}\"",'ft':round(B,6)},'D':{'value':f"{d[0]}'-{d[1]}\"",'ft':round(D,6)}},'tolerancePct':1,'source':f'line {no} / markup p33'})
# stem walls
s8,s10=193.8,8.4
add(27,'8" stem wall #4@10" + #4 dowel @18"','markup p33 slate-blue 8" stem wall @ 2\'H; S-600 secs 1-5','193.8 FT; H 2\'-0"; T 8"','CY = LF x H x T / 27',s8*2*(8/12)/27,194.0*2*0.67/27,'derived',
    'Continuous around perimeter incl. over spread footings. H = TOF [-2\'-0"] to FF. Estimator used 194.0 LF x 2 x 0.67 (exact); legend 193.8 - LF apparently rounded up to next 0.5 FT.',
    {'name':'8in stem wall concrete','formula':'cy = lf * height_ft * thickness_ft / 27','inputs':{'lf':{'value':193.8,'unit':'LF'},'height':{'value':"2'-0\"",'ft':2},'thickness':{'value':'8"','ft':round(8/12,6)}},'tolerancePct':1,'source':'line 27 / markup p33'})
add(28,'10" stem wall #4@10" (wing walls)','markup p33 olive 10" stem wall @ 2\'H; S-600 sec 6 (10 3/4")','8.4 FT; H 2\'-0"; T 10"','CY = LF x H x T / 27',s10*2*(10/12)/27,8.5*2*0.83/27,'derived',
    'Two wing-wall stubs (W stub at 3/S-203, S stub at 6/S-600). Drawing says 10 3/4" - estimator used 10" (10.75" would give 0.557 CY, +6.7%). Estimator: 8.5 LF x 2 x 0.83 exact.',
    {'name':'10in wing-wall stem concrete','formula':'cy = lf * height_ft * thickness_ft / 27','inputs':{'lf':{'value':8.4,'unit':'LF'},'height':{'value':"2'-0\"",'ft':2},'thickness':{'value':'10"','ft':round(10/12,6)}},'tolerancePct':1,'source':'line 28 / markup p33'})
# pad
add(29,'18"x18"x6" cleanout pad','markup p57 (P-302) olive count on General Note 3; P-301/P-302 note 3','1 EA; 18"x18"x6"','CY = count x L x W x T / 27',1*1.5*1.5*0.5/27,1*1.5*1.5*0.5/27,'specified',
    'Count dot is on the note, not on a plan symbol: 1 pad is a judgment count. C-5.0 shows 6 SANITARY CLEANOUTS and P-402 1 FCO; note 3 says ALL outside cleanouts get a pad (6 pads = 0.25 CY).',
    {'name':'Cleanout pad concrete','formula':'cy = count * L_ft * W_ft * T_ft / 27','inputs':{'count':{'value':1,'unit':'EA'},'L':{'value':'18"','ft':1.5},'W':{'value':'18"','ft':1.5},'T':{'value':'6"','ft':0.5}},'tolerancePct':1,'source':'line 29 / markup p57'})
# formwork
wfF=wf*1*2; swF=(s8+s10)*2*2; padF=4*1.5*0.5
raw=wfF+isoF+swF+padF
conv_raw=124.15*1*2+isoFconv+(194.0+8.5)*2*2+padF
rec=math.ceil(raw/10)*10; conv=math.ceil(conv_raw/10)*10
print('formwork components', round(wfF,3), round(isoF,3), round(swF,3), padF, 'raw', round(raw,3), 'conv raw', round(conv_raw,3))
add(30,'Formwork required (all foundation contact area)','derived from lines 19-29 sources (p33, p57)',f'WF {wfF:.2f} + spread {isoF:.2f} + stem {swF:.2f} + pad {padF:.2f} = {raw:.2f} SF','SF = ceil10( WF_LF x D x 2 + sum(n x 2(L+W) x D) + stem_LF x H x 2 + pad 2(L+W) x T )',rec,conv,'derived',
    f'Contact area of every foundation element, all sides formed, slab edge not formed (cast on stem wall); total rounded UP to next 10 SF. Raw {raw:.2f} SF ({(raw-1420)/1420*100:+.2f}% vs 1420 before rounding).',
    {'name':'Foundation formwork contact area (rolled up)','formula':'sf = ceil(sum(contact_sf_i)/10)*10','inputs':{'continuousFooting':{'lf':124.2,'depthFt':1,'faces':2},'isolatedFootings':[{'tag':t,'count':n,'Lft':round(ft(*a),6),'Wft':round(ft(*b),6),'Dft':round(ft(*d),6),'sides':4} for _,t,n,a,b,d,_ in iso],'stemWalls':[{'lf':193.8,'heightFt':2,'faces':2},{'lf':8.4,'heightFt':2,'faces':2}],'pad':{'count':1,'Lft':1.5,'Wft':1.5,'Tft':0.5},'roundUpTo':{'value':10,'unit':'SF'}},'tolerancePct':1,'source':'line 30 / markup p33, p57'})

with open(OUT+'reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f, fieldnames=['lineNo','description','unit','estimatorQty','source','sourceValues','formula','recomputedQty','deltaPct','classification','notes'])
    w.writeheader(); [w.writerow(r) for r in rows]
json.dump(fx, open(OUT+'fixtures.json','w'), indent=1)
print('within1', sum(abs(r['deltaPct'])<=1 for r in rows), 'within5', sum(abs(r['deltaPct'])<=5 for r in rows), 'n', len(rows), 'fixtures', len(fx))
# extras
print('10.75in alt', 8.4*2*(10.75/12)/27, (8.4*2*(10.75/12)/27-0.522593)/0.522593*100)
print('6 pads', 6*1.5*1.5*0.5/27)
print('slab vs gross', (1917.6-1892)/1892*100)
print('stem-WF', 193.8-124.2, 'stem total', 193.8+8.4)
print('slab CY', 1917.6*4/12/27, 'base CY', 1917.6*4/12/27)
