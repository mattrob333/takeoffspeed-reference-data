# Rebuild every 09c-flooring estimate line from its source and write reconciliation.csv + fixtures.json
import json, csv, math
ROOT='/home/user/takeoffspeed-reference-data'
OUT=ROOT+'/trades/09c-flooring/'
lines={l['lineNo']:l for l in json.load(open(ROOT+'/reference/estimate/lines.json'))}
trade=[t for t in json.load(open(ROOT+'/reference/estimate/trades.json')) if t['trade']=='09c-flooring'][0]['lines']
leg={}
for p in json.load(open(ROOT+'/reference/markups/legends.json')):
    for it in p['items']: leg[(p['page'],it['name'])]=it['quantity']
L=lambda pg,name: leg[(pg,name)]
PT=18.0  # A-150 sheet pt per ft at 1/4"=1'-0" (2592x1728 pt sheet)
# --- geometry read from the A-150 vector layer (sheet pt) ---
elec_w=(1140.1-1018.0)/PT; elec_h=(637.4-440.9)/PT          # ELEC./I.T. 106 inside faces
door106=(1081.0-1021.0)/PT; wall106=(441.7-432.8)/PT          # door opening and wall depth at 106
mat_w=(1080.6-1044.6)/PT; mat_h=(608.6-554.6)/PT              # MAT-1 rectangle as drawn
lvt_w=(1197.4-1022.1)/PT; lvt_h=(835.4-662.2)/PT              # LVT-1 plank hatch extents, GATHERING AREA 103
door100=(933.5-824.1)/PT; door110=(321.2-264.1)/PT            # weather vestibule pair, employee lounge exterior door
# --- A-410 geometry (09d-wall-finishes, 36 pt/ft at 1/2"=1'-0") ---
B=(850.8-580.5)/36; C=(1313.3-1037.0)/36; Dl=(1662.2-1518.0)/36; Dr=(1794.3-1782.3)/36
band_walls=B+C+Dl+Dr
elevA=7+3.5/12          # 7'-3 1/2" printed on RESTROOM ELEVATION - A
wt8_run2=3.67+0.22      # second traced WT-8 run on elevation A (left of door + jamb pier), scaled from markup p16 pixels
FT1=946.11; WT1=144.19; WT2=46.72; WT9=53.22; WT3=38.42
def ceil_to(x,inc): return math.ceil(x/inc-1e-9)*inc
rows=[]; fx=[]
def add(n,desc,src,sv,formula,recomp,cls,notes,fixture=None):
    l=lines[n]; est=l['quantity']
    d=round((recomp-est)/est*100,2)
    rows.append(dict(lineNo=n,description=desc,unit=l['unit'],estimatorQty=est,source=src,sourceValues=sv,formula=formula,recomputedQty=round(recomp,2),deltaPct=d,classification=cls,notes=notes))
    if fixture:
        f=dict(name=fixture[0],formula=fixture[1],inputs=fixture[2],expected=dict(quantity=est,unit=l['unit']),tolerancePct=fixture[3],source=fixture[4]); fx.append(f)
    return d
con_geom=elec_w*elec_h-mat_w*mat_h+door106*wall106/2
add(217,'SEALED CONCRETE CON-1 Benjamin Moore Corotech clear','markup p08 (A-150) CON-1 FLOORING; ELEC./I.T. 106','68.8 SF',
    'area of the CON-1 polygon: room net of the MAT-1 footprint, to the door centreline',L(8,'CON-1 FLOORING'),'measured',
    f'Geometry check from A-150 vectors: {elec_w:.3f} x {elec_h:.3f} ft = {elec_w*elec_h:.2f} SF - MAT-1 {mat_w:.0f}x{mat_h:.0f} = 6.00 SF + half door strip {door106:.2f} x {wall106/2:.3f} = {door106*wall106/2:.2f} SF -> {con_geom:.2f} SF ({(con_geom-68.78)/68.78*100:+.2f}%). The sealed concrete is net of the mat.',
    ('CON-1 sealed concrete = CON-1 polygon area','tagArea',{'areas_sf':{'ELEC./I.T. 106 (net of MAT-1, to door centreline)':68.8}},0.5,'217 / markup p08'))
add(218,'CARPET TILE CR-1 12x36 Mohawk Lichen Stone Community','markup p08 (A-150) CR1 FLOORING','131.4 SF',
    'sum of CR-1 field polygons (MEETING ROOM 105 + RELAXED SEATING 102) net of the CR-2/CR-3 insets',L(8,'CR1 FLOORING'),'measured',
    'CR-1 is the blue field around the stepped-diamond insets in 105 and 102. Field is net of the insets (no double count). No waste, no 10% attic stock (spec 09 6813 1.2.H).',
    ('CR-1 carpet tile = Σ CR-1 field polygons net of insets','tagArea',{'areas_sf':{'MEETING ROOM 105 + RELAXED SEATING 102 field':131.4}},0.5,'218 / markup p08'))
add(219,'CARPET TILE CR-2 12x36 Mohawk Lichen Micro Bloom II','markup p08 (A-150) CR2 FLOORING','435.7 SF',
    'sum of CR-2 polygons: PHONE 114, WORK 111, TRANSACTION BAR 108, BOOTH 104 + diamond insets in 105 and 102',L(8,'CR2 FLOORING'),'measured',
    'Yellow hatched polygons. Floor under the SLD-1 transaction counters is not deducted (spec 09 6813 3.3.E extends carpet into toe spaces).',
    ('CR-2 carpet tile = Σ CR-2 polygons','tagArea',{'areas_sf':{'PHONE 114 + WORK 111 + TRANSACTION BAR 108 + BOOTH 104 + insets 105/102':435.7}},0.5,'219 / markup p08'))
add(220,'CARPET TILE CR-3 12x36 Mohawk Lichen Macro Bloom II','markup p08 (A-150) CR3 FLOORING','27.1 SF',
    'CR-3 inner diamond inset in RELAXED SEATING 102',L(8,'CR3 FLOORING'),'measured','Green cross-hatched inset inside the CR-2 ring inside the CR-1 field.',
    ('CR-3 carpet tile = CR-3 inset polygon','tagArea',{'areas_sf':{'RELAXED SEATING 102 inner inset':27.1}},0.5,'220 / markup p08'))
add(221,'WALK-OFF CARPET CR-4 18x36 Mannington Charge Fluid','markup p08 (A-150) CR4 FLOORING','82.4 SF',
    'CR-4 polygon = WEATHER VESTIBULE 100 to the door centrelines',L(8,'CR4 FLOORING'),'measured','Cyan polygon. Same cyan is reused for FTS3 TRANSITION on p08; read by item name, not colour.',
    ('CR-4 walk-off = WEATHER VESTIBULE 100 polygon','tagArea',{'areas_sf':{'WEATHER VESTIBULE 100':82.4}},0.5,'221 / markup p08'))
add(222,'CERAMIC TILE FT-1 24x24 Florida Tile Aventis Velvet','markup p08 (A-150) FT1 FLOORING','946.1 SF',
    'sum of FT-1 polygons (all magenta rooms: ENTRY, VESTIBULE 116, LIBRARY, SERVICE COUNTER, EMPLOYEE LOUNGE, restrooms, JANITOR)',L(8,'FT1 FLOORING'),'measured',
    'Net area, no waste; 236.5 tiles of 4 SF net. 10% attic stock (spec 09 3000 1.2.E) not carried as a separate line.',
    ('FT-1 floor tile = Σ FT-1 polygons','tagArea',{'areas_sf':{'all FT-1 rooms':946.1}},0.5,'222 / markup p08'))
lvt_geom=lvt_w*lvt_h
add(223,'LVT-1 25cm x 1m Interface On Grain 4.5mm Bespoke Timber','markup p08 (A-150) LVT1 FLOORING; GATHERING AREA 103','94.0 SF',
    'LVT-1 polygon = GATHERING AREA 103 rectangle',L(8,'LVT1 FLOORING'),'measured',
    f'Vector check: plank hatch {lvt_w:.3f} x {lvt_h:.3f} ft = {lvt_geom:.2f} SF ({(lvt_geom-93.95)/93.95*100:+.2f}%). 34.9 planks at 2.691 SF. Spec 09 6519 describes 12x12 VCT; the drawings govern.',
    ('LVT-1 = GATHERING AREA 103 rectangle','rectArea',{'rooms_ft':[[round(lvt_w,3),round(lvt_h,3)]],'rooms_printed':['scaled 9.74 x 9.62 ft (A-150 vector hatch extents)']},0.5,'223 / markup p08, A-150'))
mat_drawn=mat_w*mat_h
add(224,'ANTI-STATIC MAT MT-1 36x48 Mats Inc. black','markup p08 (A-150) MAT-1 FLOORING; A-170 MT-1 36" x 48"',
    f'legend 6.0 SF (drawn {mat_w:.0f}\'-0" x {mat_h:.0f}\'-0"); schedule 3\'x4\' = 12 SF',
    'no reproducible rule: 10 = measured 6.0 SF rounded up to the next 5 or 10 SF (estimator habit), or the FTS-4 perimeter 10.02 LF carried as SF',
    mat_drawn,'allowance/judgment',
    f'Three different numbers: drawn 6.0 SF, scheduled 12.0 SF, estimate 10.0 SF. Recomputed value is the measured drawn area; the estimate is +{(10-6)/6*100:.0f}% over it and -{(12-10)/12*100:.1f}% under the schedule size. Best hypothesis: drawn 6.0 SF rounded up to the next 5 or 10 SF (the estimator rounds up elsewhere), or the FTS-4 10.02 LF value reused; neither is provable. The engine should carry 12 SF (count x scheduled size) and flag the drawn-size conflict.')
gr1=ceil_to(FT1*1.10,50); gr3=ceil_to((WT1+WT2+WT9)*1.10,50)
add(225,'GROUT GR-1 Custom Building epoxy 335 Winter Gray','A-170 GROUT GR-1 TRANSACTION BAR & FLOOR TILE; line 222 FT-1',
    'FT-1 946.11 SF',f'ceil50(FT-1 SF x 1.10) = ceil50({FT1*1.10:.2f})',gr1,'derived',
    'Grout carried as SF of tile served (not lb/kits). Ratio 1050/946.11 = 1.110. Rule fits both grout lines with 6-10% (10% = spec 09 3000 1.2.E attic stock rate) and round-up to 50 SF; with WT-3 (38.42) included the fitting range is 3-6%. Two data points: the rule is a convention fit, not proven. WT-3 grout is not in either line.',
    ('GR-1 grout area = ceil50(1.10 x FT-1 SF)','groutAreaRoundUp',{'tile_sf':{'FT-1':946.11},'allowancePct':10,'roundUpTo_sf':50},0.1,'225 / A-170, line 222'))
add(226,'GROUT GR-3 Custom Building epoxy 543 Driftwood','A-170 GROUT GR-3 SERVICE AREA, EMPLOYEE LOUNGE, RESTROOM WALLS; lines 235/236/238',
    'WT-1 144.19 + WT-2 46.72 + WT-9 53.22 = 244.13 SF',f'ceil50((WT-1+WT-2+WT-9) x 1.10) = ceil50({(WT1+WT2+WT9)*1.10:.2f})',gr3,'derived',
    'Same rule as GR-1. Ratio 300/244.13 = 1.229 is the round-up step, not a waste factor. Adding WT-8 bullnose (11.28 LF x 3" = 2.82 SF) does not change the result; adding WT-3 does (350).',
    ('GR-3 grout area = ceil50(1.10 x restroom/backsplash wall tile SF)','groutAreaRoundUp',{'tile_sf':{'WT-1':144.19,'WT-2':46.72,'WT-9':53.22},'allowancePct':10,'roundUpTo_sf':50},0.1,'226 / A-170, lines 235, 236, 238'))
add(227,'RUBBER BASE WB-1 4in Johnsonite Traditional #48 Grey','markup p08 (A-150) WB-1','404.7 FT',
    'sum of traced WB-1 wall runs, every room (carpet, tile, LVT and concrete rooms), net of door openings',L(8,'WB-1'),'measured',
    'One base line for all rooms although spec 09 6513 2.2.B asks Style A straight at carpet and Style B cove at resilient flooring. WB-1 is tagged in the restrooms too, where A-410 shows WT-8 tile base. 10% attic stock not carried.',
    ('WB-1 rubber base = Σ traced wall runs','tracedRun',{'runs_lf':{'all rooms, A-150':404.7}},0.5,'227 / markup p08'))
wt8=elevA+wt8_run2
add(228,'BULLNOSE BASE WT-8 3x12 Roca Flow Tender Gray','markup p16 (A-410) WT-8 BASE; RESTROOM ELEVATION - A',
    f'11.3 FT = run 1 7\'-3 1/2" ({elevA:.3f}) + run 2 {wt8_run2:.2f}',
    'sum of the two yellow runs traced along the base of elevation A',L(16,'WT-8 BASE'),'measured',
    f'Two runs on elevation A: one full width across the door ({elevA:.2f} LF) and one net of the door ({wt8_run2:.2f} LF); together {wt8:.2f} LF ({(wt8-11.28)/11.28*100:+.1f}%). Read as Womens + Mens (similar), but one run crosses the 3\'-0" door: a net-of-door takeoff is 2 x {wt8_run2:.2f} = {2*wt8_run2:.2f} LF.',
    ('WT-8 bullnose base = Σ traced runs on elevation A','tracedRun',{'runs_lf':{'elevation A run 1 (full width incl. door)':round(elevA,3),'elevation A run 2 (net of door)':wt8_run2}},1.0,'228 / markup p16'))
add(229,'TRANSITION FTS-1 Schluter Schiene AE100 satin alum (carpet to tile)','markup p08 (A-150) FTS1 TRANSITION; A-150 detail 1, key notes F001-F003','51.6 FT',
    'sum of carpet/tile boundaries: carpet door openings + open carpet edges (BOOTH, RELAXED SEATING, TRANSACTION BAR, WEATHER VESTIBULE)',L(8,'FTS1 TRANSITION'),'measured',
    'Dark-grey runs at nine FTS-1 call-outs plus F001 (transaction bar ADA panel), F002 (meeting room DIRTT door, detail 5) and F003 (booth millwork face). No stick rounding.',
    ('FTS-1 = Σ carpet-to-tile boundary LF','tracedRun',{'runs_lf':{'all carpet/tile interfaces, A-150':51.6}},0.5,'229 / markup p08'))
fts2=2*lvt_h+lvt_w
add(230,'TRANSITION FTS-2 Schluter Schiene AE100 (vinyl plank to tile)','markup p08 (A-150) FTS2 TRANSITION; A-150 detail 2','29.0 FT',
    'open sides of the LVT-1 rectangle: 2 x depth + width (north side is wall)',L(8,'FTS2 TRANSITION'),'measured',
    f'Vector check: 2 x {lvt_h:.3f} + {lvt_w:.3f} = {fts2:.2f} LF ({(fts2-28.99)/28.99*100:+.2f}%). Detail 2 adds 1/4" cement board under the LVT that no estimate line carries.',
    ('FTS-2 = open perimeter of the LVT-1 area','boundaryRun',{'sides_ft':[round(lvt_h,3),round(lvt_w,3),round(lvt_h,3)],'basis':'west, south, east edges of GATHERING AREA 103; north edge is the wall'},0.5,'230 / markup p08, A-150'))
fts3=door106+door110+door100
add(231,'TRANSITION FTS-3 Schluter Reno-U AE100 (tile to sealed concrete)','markup p08 (A-150) FTS3 TRANSITION; A-150 detail 3, key note F004; A-600 door schedule','12.2 FT',
    'door openings to concrete: ELEC./I.T. 106 + exterior doors 110 and 100 (F004)',L(8,'FTS3 TRANSITION'),'measured',
    f'Cyan runs at three thresholds: 106 ({door106:.2f}), 110 exterior ({door110:.2f}), 100 exterior pair ({door100:.2f}) = {fts3:.2f} LF ({(fts3-12.24)/12.24*100:+.1f}%; door-schedule leaf widths 3+3+6 = 12.0, -2.0%). The schedule says TILE TO SEALED CONCRETE; the estimator also used it at the two exterior doors flagged F004 (one of them is CR-4 carpet, not tile).',
    ('FTS-3 = Σ threshold openings','tracedRun',{'runs_lf':{'ELEC./I.T. 106 + exterior 110 + exterior 100':12.2}},0.5,'231 / markup p08'))
fts4=2*(mat_w+mat_h)
add(232,'TRANSITION FTS-4 Schluter Reno-Ramp AERP (sealed concrete to mat)','markup p08 (A-150) FTS-4 TRANSITION; A-150 detail 4','10.0 FT',
    'perimeter of the drawn MAT-1 rectangle = 2 x (2 + 3)',L(8,'FTS-4 TRANSITION'),'measured',
    f'Vector check: 2 x ({mat_w:.0f} + {mat_h:.0f}) = {fts4:.2f} LF (exact). With the scheduled 36"x48" mat the perimeter is 14.0 LF (+40%).',
    ('FTS-4 = perimeter of MAT-1','perimeter',{'rect_ft':[mat_w,mat_h],'basis':'MAT-1 as drawn on A-150 (2\'-0" x 3\'-0")'},0.5,'232 / markup p08, A-150'))
add(233,'SCHLUTER COVE TRIM (Dilex-AHK 1S AE per A-170 WT-9)','markup p16 (A-410) SCHLUTER COVE TRIM','51.9 FT',
    'sum of olive runs traced on A-410 (floor/wall junction of the tiled restroom walls)',L(16,'SCHLUTER COVE TRIM'),'measured',
    f'Runs are mostly hidden under the tile fills; visible pieces lie on the restroom plan side walls. Geometry candidates: 2 x band walls {2*band_walls:.2f} + WT-8 runs 11.28 = {2*band_walls+11.28:.2f} (-3.0%); 2 rooms full perimeter less doors about 54.4 (+4.9%). Neither within 1%; the legend is the source.',
    ('Schluter cove trim = Σ traced runs','tracedRun',{'runs_lf':{'A-410 restrooms':51.9}},0.5,'233 / markup p16'))
add(234,'SCHLUTER TRIM (Jolly J AE top trim per A-170 WT-1)','markup p16 (A-410) SCHLUTER TRIM','39.6 FT',
    'top edge of the 5\'-6" tile band = Σ tiled wall lengths (B + C + D net of door) x 2 restrooms',L(16,'SCHLUTER TRIM'),'measured',
    f'Geometry check: 2 x ({B:.3f} + {C:.3f} + {Dl:.3f} + {Dr:.3f}) = {2*band_walls:.2f} LF ({(2*band_walls-39.55)/39.55*100:+.1f}%). Backsplash tile on A-703/A-705 gets no trim line.',
    ('Schluter top trim = 2 x Σ band walls','bandTopEdge',{'walls_ft':[round(B,3),round(C,3),round(Dl,3),round(Dr,3)],'rooms':2,'measured_lf':39.6},1.5,'234 / markup p16, A-410'))
assert [r['lineNo'] for r in rows]==trade
with open(OUT+'reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
json.dump(fx,open(OUT+'fixtures.json','w'),indent=1)
for r in rows: print(r['lineNo'],r['estimatorQty'],r['recomputedQty'],r['deltaPct'],r['classification'])
print('within1',sum(abs(r['deltaPct'])<=1 for r in rows),'within5',sum(abs(r['deltaPct'])<=5 for r in rows),'fixtures',len(fx))
print('geom', round(con_geom,3), round(lvt_geom,3), round(fts2,3), round(fts3,3), round(fts4,3), round(wt8,3), round(2*band_walls,3), round(band_walls,3))
print('door106',round(door106,3),'door110',round(door110,3),'door100',round(door100,3),'wall106',round(wall106,3))
