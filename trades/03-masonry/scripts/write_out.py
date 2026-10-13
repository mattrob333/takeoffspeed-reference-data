import json, math, csv
OUT='/home/user/takeoffspeed-reference-data/trades/03-masonry/'
L={x['lineNo']:x for x in json.load(open('/home/user/takeoffspeed-reference-data/reference/estimate/lines.json'))}
def up(v,s): return round(math.ceil(round(v/s,9))*s,6)
rows=[]
def add(n,desc,source,sv,formula,rq,cls,notes):
    e=L[n]['quantity']; rows.append(dict(lineNo=n,description=desc,unit=L[n]['unit'],estimatorQty=e,source=source,sourceValues=sv,formula=formula,recomputedQty=rq,deltaPct=round((rq-e)/e*100,3),classification=cls,notes=notes))
q31=round(up(157.4,0.5)*1.33,6)
add(31,'4" fully grouted CMU stem wall w/ grout cavity solid','markup p03 (A-110) mauve line "4""THK. CMU STEM WALL W/ GROUT CAVITY SOLID @ 1\'4""H"; A-430 det.4; S-600 sec.1','157.4 FT; H 1\'-4"" (2 courses x 8"")','SF = lfUp05(LF) x ftDec2(H) = 157.5 x 1.33',q31,'derived','Measured run x section height. Exact physical 157.4 x 16/12 = 209.867 (+0.187%). LF rounded up to next 0.5 FT and 1\'-4"" written 1.33 (same habit as 02-concrete lines 27/28). Height = 2\'-0"" stem wall - 8"" brick below FFE. No opening deduction below grade.')
q32=up(163.6+232.1,5)
add(32,'3-5/8" modular brick veneer EXT-1 w/ adj. ties 32"x16"','markup p11 (A-200) + p12 (A-201) purple area "EXT-1: 3-5/8""THK. STANDARD MODULAR BRICK VENEE..."','163.6 + 232.1 SQ FT = 395.7','SF = sfUp5(sum areas)',q32,'measured','Raw sum 395.7 is -1.075%. Round-up step 5/10/50/100 SF all give 400; 5 SF chosen (proved on line 313). Area = running-bond field only (excludes both rowlock courses). Cross-check 149.3 LF x 2.667 ft = 398.1 SF.')
add(33,'3-1/4" x 3-5/8"H half rowlock brick','markup p11 + p12 brownish-red line "3-1/4""THK. x 3-5/8""H HALF ROWLOCK BRICK"','61.4 + 87.9 FT','LF = sum runs',round(61.4+87.9,4),'measured','Residual -0.02% is legend 1-decimal display; workbook carries 2 decimals. Recessed 1/2"" per A-430 det.4.')
add(34,'7-5/8" x 3-5/8"H rowlock sill','markup p11 + p12 green line "7-5/8""THK. x 3-5/8""H ROWLOCK SILL"','61.5 + 88.3 FT','LF = sum runs',round(61.5+88.3,4),'measured','Residual -0.04% is legend precision. Sill at SILL 2\'-8"" datum (A-310); overhang min. 1/2"".')
add(35,'Fluid-applied vapor barrier behind brick','= line 32 (A-310/A-430 FLUID-APPLIED VAPOR BARRIER behind EXT-1)','line 32 = 400 SF','SF = veneerSF',q32,'derived','Estimator reuses the brick SF. Physical extent ~ termination bar to sill (2\'-8"") incl. behind rowlocks, excl. 8"" below grade; the two offset. Same product for EIFS/ACM is line 184 (07), 2983.5 SF - keep brick zones out of it.')
with open(OUT+'reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows([{k:(v.replace('""','"') if isinstance(v,str) else v) for k,v in r.items()} for r in rows])
for r in rows: print(r['lineNo'],r['recomputedQty'],r['deltaPct'])
fx=[
 {"name":"03-masonry line 31: 4\" CMU stem wall below brick (estimator rounding)","formula":"cmuStemWallSF = ceil(runLF/0.5)*0.5 * round(height_ft,2)",
  "inputs":{"runLF":{"value":157.4,"unit":"FT"},"height":{"value":"1'-4\"","unit":"ft-in","decimalFt":1.33},"lfRoundStep":{"value":0.5,"unit":"FT"}},
  "expected":{"quantity":209.475,"unit":"SF"},"tolerancePct":0.01,"source":"line 31 / markup p03 A-110"},
 {"name":"03-masonry line 31 (physical): 4\" CMU stem wall below brick, exact height","formula":"cmuStemWallSF = runLF * height_exact (masonry.cmu-wall net SF, no openings)",
  "inputs":{"runLF":{"value":157.4,"unit":"FT"},"height":{"value":"1'-4\"","unit":"ft-in"},"thickness":{"value":4,"unit":"in"},"grout":{"value":"solid","unit":"choice"}},
  "expected":{"quantity":209.475,"unit":"SF"},"tolerancePct":0.2,"source":"line 31 / markup p03 A-110 (exact 209.867, +0.187%)"},
 {"name":"03-masonry line 32: EXT-1 modular brick veneer field SF","formula":"veneerFieldSF = ceil(sum(areas)/5)*5",
  "inputs":{"areas":{"value":[163.6,232.1],"unit":"SF"},"areaRoundStep":{"value":5,"unit":"SF"},"unitSize":{"value":"modular","unit":"choice"},"finishTag":{"value":"EXT-1","unit":"text"}},
  "expected":{"quantity":400.0,"unit":"SF"},"tolerancePct":0.01,"source":"line 32 / markup p11 A-200 + p12 A-201"},
 {"name":"03-masonry line 33: half rowlock brick LF","formula":"specialCourseLF = sum(runs)",
  "inputs":{"runs":{"value":[61.4,87.9],"unit":"FT"},"course":{"value":"rowlock","unit":"choice"},"unitSize":{"value":"modular","unit":"choice"},"finishTag":{"value":"EXT-1","unit":"text"},"label":{"value":"3-1/4\"THK. x 3-5/8\"H HALF ROWLOCK BRICK","unit":"text"}},
  "expected":{"quantity":149.33,"unit":"LF"},"tolerancePct":0.05,"source":"line 33 / markup p11 + p12"},
 {"name":"03-masonry line 34: rowlock sill LF","formula":"specialCourseLF = sum(runs)",
  "inputs":{"runs":{"value":[61.5,88.3],"unit":"FT"},"course":{"value":"rowlock","unit":"choice"},"unitSize":{"value":"modular","unit":"choice"},"finishTag":{"value":"EXT-1","unit":"text"},"label":{"value":"7-5/8\"THK. x 3-5/8\"H ROWLOCK SILL","unit":"text"}},
  "expected":{"quantity":149.86,"unit":"LF"},"tolerancePct":0.05,"source":"line 34 / markup p11 + p12"},
 {"name":"03-masonry line 35: fluid-applied vapor barrier behind brick","formula":"veneerBarrierSF = veneerFieldSF (line 32)",
  "inputs":{"veneerSF":{"value":400.0,"unit":"SF"},"airBarrier":{"value":"FLUID APPLIED VAPOR","unit":"text"}},
  "expected":{"quantity":400.0,"unit":"SF"},"tolerancePct":0.01,"source":"line 35 / = line 32 (A-310, A-430 det.4)"},
]
json.dump(fx,open(OUT+'fixtures.json','w'),indent=1)
print(len(fx))
