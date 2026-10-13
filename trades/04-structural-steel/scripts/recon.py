import json, csv
from fractions import Fraction as F
ROOT='/home/user/takeoffspeed-reference-data'
OUT=ROOT+'/trades/04-structural-steel'
L={l['lineNo']:l for l in json.load(open(ROOT+'/reference/estimate/lines.json'))}
def ft(f,i=0,n=0,d=1): return f+(i+F(n,d))/12
rows=[]; fx=[]
def add(no, short, source, values, formula, recomputed, cls, notes, fixture=None):
    est=L[no]['quantity']; unit=L[no]['unit']
    rec=round(float(recomputed),2)
    d=round((rec-est)/est*100,2) if est else 0.0
    rows.append(dict(lineNo=no,description=short,unit=unit,estimatorQty=est,source=source,sourceValues=values,formula=formula,recomputedQty=rec,deltaPct=d,classification=cls,notes=notes))
    if fixture:
        name,form,inputs,tol=fixture
        fx.append({"name":name,"formula":form,"inputs":inputs,"expected":{"quantity":est,"unit":unit},"tolerancePct":tol,"source":f"line {no} / {source}"})
S=lambda *v: sum(F(str(x)) for x in v)
# columns
add(36,'HSS1-1/2x1-1/2x3/16 tube column','A-200 legend p11 (6 EA @ 1\'7"H); detail A-430 canopy sign support','6 EA x 1.58 ft','LF = count x height(ft, rounded to 0.01)',6*F('1.58'),'derived','Legend gives EA at a printed height; estimator converts 1\'7" to 1.58 ft (exact 1.5833 -> 9.50 LF, +0.2%).',
    ('tube-post-lf','member.lf = count x heightFt',{"count":{"value":6,"unit":"EA"},"height":{"value":"1'-7\"","unit":"ft-in"}},0.5))
add(37,'HSS4x4x1/4 column','S-301 legend p36 (5.6 FT) + S-203 legend p34 HSS4x4x1/4 POST @ 1\'4"H (6 EA)','5.6 FT + 6 EA x 1.3333 ft','LF = measured LF + count x height',S('5.6')+6*ft(1,4),'derived','S-603 note: HSS 4x4x1/4 post at each high roof joist on the grid-B beams; 6 posts x 1\'-4" = 8.0 LF.',
    ('hss4-column-plus-posts','member.lf = sum(measured LF) + count x heightFt',{"measuredLF":[{"value":5.6,"unit":"LF"}],"posts":{"count":6,"height":"1'-4\""}},1))
for no,short,vals,parts,note in [
 (38,'HSS5x5x3/8 column','20.3 + 18.9',['20.3','18.9'],'Two columns A-2.9 (S-301 elev 6) and C-7 (S-203 frame elev 3); schedule S-201 lists exactly 2 HSS5X5X3/8.'),
 (39,'HSS6x6x1/2 column','19.7',['19.7'],'One column B-6 (S-301 elev 10); schedule lists 1.'),
 (40,'HSS6x6x3/8 column','61.4 (S-203 p35) + 175.0 (S-301 p36)',['61.4','175'],'Sum of both pages. Audit: S-203 frame elevations repeat C-6 and D-6 (already on S-301 elev 10) and measure D-5, which the schedule calls HSS6X6X1/4. Schedule-true quantity is ~175 LF (9 columns).'),
 (41,'HSS7x7x1/2 column','97.3',['97.3'],'5 columns (A-1, A.5-1, B-1, C-2, C-3), each measured once in elevation, base plate to top of parapet channel (pixel check 97.14 LF).'),
 ]:
    add(no,short,f'S-203 p35 / S-301 p36 legends',vals,'LF = sum of legend rows across pages',sum(F(p) for p in parts),'measured',note,
        (f'line{no}-column-lf','member.lf = sum(legend LF)',{"lengths":[{"value":float(p),"unit":"LF"} for p in parts]},1))
beams=[(42,'HSS4x4x1/4 beam',['40.2']),(43,'HSS5x5x1/4 beam',['21.5']),(44,'HSS6x2x1/4 beam',['3']),(45,'HSS6x4x3/8 beam (row 1, brown)',['22.2']),(46,'HSS6x4x3/8 beam (row 2, periwinkle)',['9.0']),(47,'HSS6x6x3/8 beam',['3.1']),(48,'HSS8x2x1/4 beam',['76.7']),(49,'HSS8x3x1/4 beam',['36.9']),(50,'HSS8x6x1/4 beam',['33.6']),(51,'HSS10x6x1/4 beam',['65.2']),(52,'W8x10 beam',['13.5']),(53,'W10x12 beam',['51.5','4.8']),(54,'W10x22 beam',['11.9']),(55,'W12x14 beam',['74.7']),(56,'W12x22 beam',['15']),(57,'W14x26 beam',['19.5']),(58,'W14x30 beam',['20.1']),(59,'W16x26 beam',['20.1'])]
for no,short,parts in beams:
    src='S-203 legend p34' + (' + S-301 legend p36' if no==53 else '')
    note='Plan length measured on S-203 framing plan, roughly face to face of supports.'
    if no==45: note='Row printed on the p34 legend image (22.2 FT, brown) but MISSING from legends.json items (only the 9.0 row was transcribed; the notes mention both).'
    if no==46: note='Second HSS6x4x3/8 legend row; estimator keeps two lines (different swatches; plan shows t/s 12\'-8 5/8" and 10\'-8 5/8" runs).'
    if no==53: note='51.5 LF on the roof plan + 4.8 LF strut on S-301 elev 9 (line B, between braces), a different member.'
    add(no,short,src,' + '.join(parts),'LF = sum of legend rows',sum(F(p) for p in parts),'measured',note,
        (f'line{no}-beam-lf','member.lf = sum(legend LF)',{"lengths":[{"value":float(p),"unit":"LF"} for p in parts]},1))
for no,short,parts,src,note in [
 (60,'C5x6.7 channel',['53.4'],'S-203 legend p34','RTU / roof-opening frames per S-681 details 3 and 10 ("A" members C5x6.7 U.N.O.).'),
 (61,'C7x9.8 channel',['236.7','14','177.8'],'S-203 p34 + S-203 p35 + S-301 p36','Parapet channels and canopy channels. Risk: plan (236.7) and elevation (177.8) runs may repeat the same parapet channels; not verifiable from the overlay because the canopy fill is the same yellow.'),
 (62,'C8x11.5 channel',['10.1','14.5'],'S-203 p35 + S-301 p36','S-203 frame elev 2 (line D, 6-5) + S-301 elev 11 (line 2); different members.'),
 (63,'HSS4x4x1/4 diagonal bracing',['28.6'],'S-301 legend p36','Knee/diagonal braces in elevations 5 and 9, work point to work point.'),
 (64,'HSS6x6x1/4 diagonal bracing',['59.6'],'S-301 legend p36','Diagonal braces in elevations 4, 5, 6.'),
 (66,'L3x3x1/4 horizontal bracing',['19.1'],'S-203 legend p34','H.B. symbols on plan (S-203 key, S-682 detail 1).'),
 (68,'L3x3x3/16 angle',['99.4'],'S-203 legend p34','Continuous L3x3x3/16 at deck edge per S-683 details 5/6.'),
 (69,'L4x3x1/4 LLV angle',['179.9'],'S-203 legend p34','Roof perimeter closure angle per S-203 note and spec 05 1200 3.x K (4x3x1/4 continuous).'),
 (70,'12KCS2 roof joist',['54.0'],'S-203 legend p34','3 joists x 18.0 ft. Grid B to C is 14.96 ft: the low-roof joists were drawn from ~3.1 ft north of grid B (same strip as the deck overlap).'),
 (71,'16KCS3 roof joist',['248.6'],'S-203 legend p34','10 joists x 24.86 ft (A to B = 25.17 ft c/c).'),
 (72,'18KCS2 roof joist',['108.5'],'S-203 legend p34','4 joists x 27.13 ft vs B to D 23.99 ft (+3.1 ft each, see line 70).'),
 ]:
    add(no,short,src,' + '.join(parts),'LF = sum of legend rows',sum(F(p) for p in parts),'measured',note,
        (f'line{no}-lf','sum(legend LF)',{"lengths":[{"value":float(p),"unit":"LF"} for p in parts]},1))
add(65,'L2-1/2x2-1/2x1/4 X-type bridging','S-203 legend p34: RIGID JOIST BRACING *2 (121.9 FT) + L2-1/2 X-TYPE BRIDGING *2 (35.5 FT)','(121.9 + 35.5) x 2','LF = (horizontal rows LF + X rows plan LF) x 2',(S('121.9')+S('35.5'))*2,'derived','"*2" in the legend name is the multiplier: horizontal bracing at top AND bottom chord; X bridging = 2 diagonals. X diagonals taken at plan length (no joist-depth slope). Size per S-682 detail 1 and spec 05 1200 (L2-1/2); S-203 key and spec 05 2100 O say 2x2x1/4.',
    ('bridging-star2','bridging.lf = (sum(rigid rows) + sum(X rows)) x 2',{"rigidRows":{"value":121.9,"unit":"LF"},"xRowsPlan":{"value":35.5,"unit":"LF"},"multiplier":2},1))
add(67,'L2x2x3/16 angle','S-203 legend p34: L2x2x3/16 @ 4\'L (18 EA) + @ 5\'8"L (1 EA)','18 x 4.0 + 1 x 5.6667','LF = sum(count x stated length)',18*4+ft(5,8),'derived','Counts are measured (dots at the joist closest to beam midspan, S-602 note "2x2x3/16 ANGLE TO JOIST TOP CHORD AT JOIST CLOSEST TO BEAM MIDSPAN"); the 4\' and 5\'8" lengths are the estimator\'s own (not dimensioned on the drawings).',
    ('kicker-angles','member.lf = sum(count_i x length_i)',{"groups":[{"count":18,"length":"4'-0\""},{"count":1,"length":"5'-8\""}]},0.5))
add(73,'1-1/2" WR type B 22ga G90 roof deck','S-203 legend p34 (2208.4 SQ FT); deck schedule RD-1.5 on S-203/S-201','2208.4 SF','SF = sum of deck polygons (plan projection, no lap/waste)',S('2208.4'),'measured','Pixel rebuild: envelope 2024.6 SF + 193.0 SF band drawn twice along grid B = 2217.6 SF (+0.4%). Net plan area ~2025 SF; the strip is a double count (GPT-6 Astra second opinion agrees, ~170-185 SF).',
    ('deck-sf','deck.sf = sum(areas)',{"areas":[{"value":2208.4,"unit":"SF"}]},1))
add(74,'5x5x1/4 steel base plate','A-200 legend p11 HSS1-1/2 TUBE POST 6 EA; A-430 detail: 1/4"x5"x5" STEEL PLATE','6 posts x 1','EA = count of tube posts x 1 plate',6,'derived','One plate per canopy sign tube post.',
    ('plate-per-post','plate.count = posts x platesPerPost',{"posts":6,"platesPerPost":1},0))
for no,mark,cnt,legend in [(75,'BP12',10,9),(76,'BP14',4,4),(77,'BP1518',4,4)]:
    add(no,f'{mark} base plate','S-201 BASE PLATE SCHEDULE (COUNT column)',f'{mark} COUNT = {cnt} (legend count {legend})','EA = schedule count',cnt,'specified',f'Schedule count; the p33 legend counted {legend} {mark} marks.'+(' The estimator trusted the schedule over the markup count.' if cnt!=legend else ''),
        (f'{mark.lower()}-count','plate.count = schedule COUNT',{"mark":mark,"scheduleCount":cnt},0))
add(78,'11x5-1/2x3/4 cap plate','S-201 column schedule + S-681 detail 8 cap plate table (HSS5X5 -> 3/4"x11"x5-1/2")','HSS5X5X3/8 columns: A-2.9, C-7 = 2','EA = number of columns whose size maps to this plate',2,'derived','Cap plate per column from the cap-plate table.',
    ('cap-plate-hss5','capPlates = count(columns with size class HSS5X5)',{"columnsBySize":{"HSS5X5":2}},0))
add(79,'12x6-1/2x3/4 cap plate','S-201 column schedule + S-681 detail 8 (HSS6X6 -> 3/4"x12"x6-1/2")','HSS6X6 (11) + HSS7X7 (5) = 16','EA = HSS6X6 columns + HSS7X7 columns',11+5,'derived','The cap table has no HSS7X7 row; the estimator used the HSS6X6 plate for the 5 HSS7X7 columns (judgment).',
    ('cap-plate-hss6-7','capPlates = count(HSS6X6) + count(HSS7X7)',{"columnsBySize":{"HSS6X6":11,"HSS7X7":5}},0))
add(80,'Aluminum roof access ladder 1\'9"W x 13\'4"H','A-110 legend p3 (1 EA); A-450 detail 3 ROOF HATCH & LADDER','1 EA','EA = legend count',1,'counted','Description from A-450 detail 3 (13\'-4" overall, 1-1/4" serrated rungs, 3/16" aluminum wall bracket, safety post). Spec 05 5000 describes galvanized steel ladders; the estimator followed the detail.',
    ('ladder-count','misc.count',{"count":1},0))
rows.sort(key=lambda r:r['lineNo'])
with open(OUT+'/reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
fx.sort(key=lambda x:int(x['source'].split()[1]))
json.dump(fx,open(OUT+'/fixtures.json','w'),indent=1)
n=len(rows); w1=sum(abs(r['deltaPct'])<=1 for r in rows); w5=sum(abs(r['deltaPct'])<=5 for r in rows)
print(n,w1,w5,len(fx))
for r in rows: print(r['lineNo'],r['estimatorQty'],r['recomputedQty'],r['deltaPct'],r['classification'])
