import csv, json, os
OUT='/home/user/takeoffspeed-reference-data/trades/31-earthwork'
L={x['lineNo']:x for x in json.load(open('/home/user/takeoffspeed-reference-data/reference/estimate/lines.json'))}
# ---- footing earthwork
F=[('F30',3,3,1,3),('F38',3+8/12,3+8/12,1,3),('F50',5,5,14/12,6),('F60',6,6,16/12,1),('F70',7,7,16/12,1),('F7040',7,4,16/12,1),('F10050',10,5,14/12,1)]
TOF=2.0; WF=(124.2,2.0,1.0); WSW=1.0; WSP=0.5
exc=(WF[0]*(WF[1]+2*WSW)*(WF[2]+TOF)+sum((l+2*WSP)*(w+2*WSP)*(t+TOF)*c for n,l,w,t,c in F))/27
conc_lines={19:9.196296,20:1.0,21:1.496544,22:6.5,23:1.773333,24:2.413704,25:1.379259,26:2.166667,27:9.628148,28:0.522593}
ftgCY=sum(v for k,v in conc_lines.items() if k<=26); stemCY=conc_lines[27]+conc_lines[28]
conc=ftgCY+stemCY
bf=exc-conc; haul=exc-bf
# ---- grading
rows=[('440',0,51.72),('440',1.78,151.02),('440',0,224.56),('440',0,199),('440',0,2.11),('440',0,12.81),
('439.5',61.2,84.11),('439.5',15.69,0),('439',27.56,37.98),('439',58.96,18.35),('438',47.33,4.59),('437',25.2,0),('436.5',238.52,0),('435',158.17,0)]
cut=round(sum(r[1] for r in rows),6); fill=round(sum(r[2] for r in rows),6); net=round(fill-cut,6)
def d(r,e): return round((r/e-1)*100,3)
spread_txt='; '.join(f'{n} {c}x {l:.3f}x{w:.3f}x{t:.3f}' for n,l,w,t,c in F)
rec=[
 (629,'EXCAVATION PROVIDED FOR FOOTING','p33 S-201 legend (WF20 124.2 FT; F30 3, F38 3, F50 6, F60 1, F70 1, F7040 1, F10050 1 EA) + S-201 WALL/SPREAD FOOTING SCHEDULES + S-201 note TOP OF FOOTINGS [-2\'-0"] BELOW FINISH FLOOR',
  f'WF20 124.2 LF x 2\'-0" x 1\'-0"; {spread_txt} (ft); TOF 2.0 ft below FF; working space 1\'-0"/side wall trench, 6"/side pads',
  'CY = [LF_wf x (W+2x1) x (T+2) + sum n x (L+2x0.5) x (W+2x0.5) x (T+2)] / 27 = (1490.4 + 1743.0) / 27 = 55.20 + 64.56',exc,'derived',
  'Depth measured from FINISH FLOOR (TOF -2\'-0" + footing T). Working space is the estimator convention inferred from this job: 1\' each side for the continuous trench (same as dumpster line 665), 6" each side (L+1, W+1) for spread pads. Estimate prints 1 dp. GPT-6 independently found the same split. All footings at -2\'-0" (one F38 tagged [-1\'-0"] was not reduced).'),
 (630,'BACKFILL PROVIDED FOR FOOTING','line 629 - concrete lines 19-28 (S-201 footings + stem walls)',
  f'excavation {exc:.4f} CY; footings lines 19-26 = {ftgCY:.6f} CY; stem walls lines 27-28 = {stemCY:.6f} CY',
  'backfill CY = excavation - footing concrete - stem wall concrete = 119.7556 - 25.9258 - 10.1507',bf,'derived',
  'All stem walls (8" x 193.8 LF + 10" x 8.4 LF, 2\'-0" H, legend p33) are deducted, including the runs over spread footings. Slab, gravel bed and 4" CMU below grade (line 31) are not deducted. No compaction/shrink factor.'),
 (631,'HAULING OFF EXTRA MATERIAL','line 629 - line 630',
  f'excavation {exc:.4f} CY - backfill {bf:.4f} CY',
  'haul CY = excavation - backfill = footing + stem wall concrete (displaced soil)',haul,'derived',
  'Bank CY, no swell. Equals the concrete volume of lines 19-28 (36.08 -> 36.1).'),
 (639,'CUT REQUIRED FOR GRADING','p92 PlanSwift Earthwork Pro Summary (C-4.0), from p73 existing/proposed elevation areas',
  'Cut Total column, 14 proposed-contour regions: '+' + '.join(f'{r[1]}' for r in rows if r[1]),
  'cut CY = sum of region Cut Totals (printed total 634.41)',cut,'measured',
  'PlanSwift Earthwork Pro overlays 6 existing elevation areas (41,063.9 SF) and 14 proposed flat-elevation regions (33,148.2 SF incl. the 3,841.3 SF 439.5 row missing from legends.json) to FINISHED grade. Pond (435 / 436.5 regions) is included (estimate line 708 note).'),
 (640,'FILL REQUIRED FOR GRADING','p92 PlanSwift Earthwork Pro Summary (C-4.0)',
  'Fill Total column: '+' + '.join(f'{r[2]}' for r in rows if r[2]),
  'fill CY = sum of region Fill Totals (printed total 786.25)',fill,'measured',
  'Compacted/in-place CY to finished grade; no pavement-section, slab or topsoil adjustment.'),
 (641,'NET FILL','lines 640 - 639 (= p92 Qty total)',
  f'fill {fill} CY - cut {cut} CY',
  'net CY = fill - cut (plain volumetric balance, no shrink/swell)',net,'derived',
  'Positive = import. Printed Qty column total 151.84. No shrinkage applied although fill is compacted measure.'),
]
with open(os.path.join(OUT,'reconciliation.csv'),'w',newline='') as fh:
    w=csv.writer(fh); w.writerow(['lineNo','description','unit','estimatorQty','source','sourceValues','formula','recomputedQty','deltaPct','classification','notes'])
    for ln,desc,src,sv,fo,rq,cl,no in rec:
        e=L[ln]['quantity']; assert L[ln]['unit']=='CY'
        w.writerow([ln,desc,'CY',e,src,sv,fo,round(rq,4),d(rq,e),cl,no])
        print(ln,e,round(rq,4),d(rq,e))
spread=[{'mark':n,'length':{'value':round(l,6),'unit':'ft'},'width':{'value':round(w,6),'unit':'ft'},'thickness':{'value':round(t,6),'unit':'ft'},'count':{'value':c,'unit':'EA'}} for n,l,w,t,c in F]
geo={'wallFooting':{'mark':'WF20','length':{'value':124.2,'unit':'LF'},'width':{'value':2,'unit':'ft'},'thickness':{'value':1,'unit':'ft'}},
     'spreadFootings':spread,'topOfFootingBelowFF':{'value':2,'unit':'ft'},
     'workingSpaceWallPerSide':{'value':1,'unit':'ft'},'workingSpacePadPerSide':{'value':0.5,'unit':'ft'}}
conc_in={'footingConcrete':{'value':round(ftgCY,6),'unit':'CY','from':'estimate lines 19-26'},'stemWallConcrete':{'value':round(stemCY,6),'unit':'CY','from':'estimate lines 27-28 (8" x 193.8 LF + 10" x 8.4 LF x 2\'-0" H)'}}
fx=[
 {'name':'31-earthwork line 629: EXCAVATION PROVIDED FOR FOOTING','formula':'excavationCY = [wf.length*(wf.width+2*wsWall)*(wf.thickness+tof) + sum(n*(L+2*wsPad)*(W+2*wsPad)*(T+tof))] / 27','inputs':geo,'expected':{'quantity':119.8,'unit':'CY'},'tolerancePct':0.1,'source':'629 / p33 S-201 legend + S-201 schedules'},
 {'name':'31-earthwork line 630: BACKFILL PROVIDED FOR FOOTING','formula':'backfillCY = excavationCY(geometry) - footingConcrete - stemWallConcrete','inputs':{**geo,**conc_in},'expected':{'quantity':83.7,'unit':'CY'},'tolerancePct':0.1,'source':'630 / line 629 - lines 19-28'},
 {'name':'31-earthwork line 631: HAULING OFF EXTRA MATERIAL','formula':'haulCY = excavationCY - backfillCY (= footingConcrete + stemWallConcrete, bank CY, no swell)','inputs':{**geo,**conc_in},'expected':{'quantity':36.1,'unit':'CY'},'tolerancePct':0.1,'source':'631 / line 629 - line 630'},
 {'name':'31-earthwork line 639: CUT REQUIRED FOR GRADING','formula':'cutCY = sum(region.cut)','inputs':{'regions':[{'proposedElev':{'value':float(z),'unit':'ft'},'cut':{'value':c,'unit':'CY'},'fill':{'value':f,'unit':'CY'}} for z,c,f in rows]},'expected':{'quantity':634.41,'unit':'CY'},'tolerancePct':0.01,'source':'639 / p92 Earthwork Pro Summary (C-4.0)'},
 {'name':'31-earthwork line 640: FILL REQUIRED FOR GRADING','formula':'fillCY = sum(region.fill)','inputs':{'regions':[{'proposedElev':{'value':float(z),'unit':'ft'},'cut':{'value':c,'unit':'CY'},'fill':{'value':f,'unit':'CY'}} for z,c,f in rows]},'expected':{'quantity':786.25,'unit':'CY'},'tolerancePct':0.01,'source':'640 / p92 Earthwork Pro Summary (C-4.0)'},
 {'name':'31-earthwork line 641: NET FILL','formula':'netFillCY = fillCY - cutCY (shrinkPct = 0)','inputs':{'cut':{'value':634.41,'unit':'CY'},'fill':{'value':786.25,'unit':'CY'},'shrinkPct':{'value':0,'unit':'%'}},'expected':{'quantity':151.84,'unit':'CY'},'tolerancePct':0.01,'source':'641 / p92 Qty total'},
]
json.dump(fx,open(os.path.join(OUT,'fixtures.json'),'w'),indent=1)
print('fixtures',len(fx))
