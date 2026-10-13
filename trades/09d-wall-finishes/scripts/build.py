import csv, json
OUT='/home/user/takeoffspeed-reference-data/trades/09d-wall-finishes/'
def d(r,e): return round((r-e)/e*100,2)
rows=[]
def add(lineNo,desc,unit,est,source,sv,formula,rec,cls,notes):
    rows.append(dict(lineNo=lineNo,description=desc,unit=unit,estimatorQty=est,source=source,sourceValues=sv,formula=formula,recomputedQty=round(rec,2),deltaPct=d(rec,est),classification=cls,notes=notes))
wt1=[120.7,15.3,8.2]; wt2=[43.8,1.4,1.6]; wt9=[50.6,1.3,1.3]
add(235,'WALL TILE WT-1 3x12 ROCA FLOW WHITE','SF',144.19,
 'markup p16 (A-410) WT1 WALL TILE; p27 (A-703) WT1 WALL TILE; p32 (A-705) WT1 WALL TILE',
 'A-410 120.7 SF; A-703 15.3 SF; A-705 8.2 SF','sum of WT1 field areas traced on interior elevations (field net of WT-2/WT-9 accent tiles)',sum(wt1),'measured',
 'A-410 area covers both restrooms (Womens elevations B/C/D traced, polygons copied for Mens per note MENS SIMILAR TO WOMENS). Fixtures, mirror, equipment not deducted. Legend shows 1 decimal; line carries PlanSwift precision.')
add(236,'WALL TILE WT-2 3x12 ROCA FLOW COSMIC SAPPHIRE','SF',46.72,
 'markup p16 (A-410), p27 (A-703), p32 (A-705) WT2 WALL TILE','A-410 43.8; A-703 1.4; A-705 1.6 SF','sum of WT-2 accent tiles traced tile-by-tile on elevations',sum(wt2),'measured',
 '0.17% is legend 1-decimal display rounding. Schedule MIX 20% would give 48.83 SF (+4.5%); estimator traced the drawn pattern instead.')
add(237,'WALL TILE WT-3 6x12 MOSA MURALS DARK ANTHRACITE','SF',38.42,
 'markup p23 (A-700) WT3 TILE; A-700 detail 4 TRANSACTION BAR - FRONT ELEVATION','38.4 SF; vector field 10\'-4 3/8" x 3\'-8 1/2" = 38.44 SF',
 'tile field W x H on the front elevation (inside the SLD-1 waterfall edge)',38.4,'measured',
 'Same 38.4 SF area also carried as 1/4" CEMENTITIOUS BACKER BOARD and PL-4 FINISH on p23 (other trades). Geometry check 38.44 SF (+0.05%).')
add(238,'WALL TILE WT-9 3x12 ROCA FLOW TENDER GRAY','SF',53.22,
 'markup p16 (A-410), p27 (A-703), p32 (A-705) WT9 WALL TILE','A-410 50.6; A-703 1.3; A-705 1.3 SF','sum of WT-9 tiles traced on elevations (lower grey band + accents)',sum(wt9),'measured',
 'Schedule MIX 20% would give 48.83 SF (-8.3%). Restroom split 56/20/24 vs schedule 60/20/20.')
add(239,'WALL COVERING WC-1 FORMULA VARIES BY FOCUS MARKET','SF',120.0,
 'markup p08 (A-150) WC1 @ 12\'H; A-130 WEATHER VESTIBULE 100 ceiling 12\'-0" A.F.F.','10.1 FT x 12 ft','run LF x height (height in the legend name = ceiling height)',10.1*12,'derived',
 'Recomputed 121.2 SF is +1.0%. 120 = 10.0 LF x 12 ft: estimator rounded the run (or overrode the quantity); not provable from the data. Spec p015 matrix lists vinyl wall covering as Owner-furnished, Owner-installed.')
add(240,'WALL COVERING @ PT7 PAINT - ASSUMED WALL COVERING, V.I.F','SF',103.0,
 'markup p08 (A-150) WALL COVERING @ 10\'H ABOVE PT7 (also PT7 @ 10\'); A-170 PT-7 = PRIMER, SHIELDZ UNIVERSAL WALLCOVERING / ROMAN PRO-999','10.3 FT x 10 ft (MEETING ROOM 105 ceiling 10\'-0" A.F.F.)','run LF x height; wallcovering inferred from a wallcovering-primer-only paint tag',10.3*10,'derived (judgment: assumed scope)',
 'PT-7 is a clear-drying wallcovering primer COORDINATE w/ OWNER VENDOR; nothing on the drawings shows a wallcovering tag on this wall, so the estimator assumed one and marked it V.I.F.')
add(241,'FRP-1 48in H MARLITE PEBBLED P100 CLASSIC WHITE','SF',16.0,
 'markup p08 (A-150) FRP-1 @ 4\'H; A-410 JANITOR CLOSET ELEVATIONS 1 & 3 (FRP PANEL @ MOP SINK, BOTH SIDES, 4\'-0"); P-101 MOP SINK FIAT MSK-2424 24"x24"','4.0 FT x 4 ft (2 walls x 2\'-0" at a 24"x24" corner mop sink)','run LF x height',4.0*4,'derived',
 'Run = the two walls behind the corner mop sink. Height 4\'-0" from the elevation = 48" H in the finish schedule.')
with open(OUT+'reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
for r in rows: print(r['lineNo'],r['estimatorQty'],r['recomputedQty'],r['deltaPct'])
print('within1',sum(abs(r['deltaPct'])<=1.0 for r in rows),'within5',sum(abs(r['deltaPct'])<=5 for r in rows))

fx=[
 {"name":"WT-1 wall tile = sum of traced WT-1 field areas","formula":"tagArea","inputs":{"areas_sf":{"A-410 restrooms (both)":120.7,"A-703 service counter backsplash":15.3,"A-705 employee lounge backsplash":8.2}},"expected":{"quantity":144.19,"unit":"SF"},"tolerancePct":0.5,"source":"235 / markup p16, p27, p32"},
 {"name":"WT-2 wall tile = sum of traced WT-2 accent areas","formula":"tagArea","inputs":{"areas_sf":{"A-410 restrooms (both)":43.8,"A-703":1.4,"A-705":1.6}},"expected":{"quantity":46.72,"unit":"SF"},"tolerancePct":0.5,"source":"236 / markup p16, p27, p32"},
 {"name":"WT-3 transaction bar front tile field","formula":"bandArea","inputs":{"walls_ft":[10.3646],"walls_printed":["10'-4 3/8\" (scaled, not dimensioned)"],"height_ft":3.7083,"height_printed":"3'-8 1/2\"","openings":[]},"expected":{"quantity":38.42,"unit":"SF"},"tolerancePct":0.5,"source":"237 / markup p23, A-700 detail 4"},
 {"name":"WT-9 wall tile = sum of traced WT-9 areas","formula":"tagArea","inputs":{"areas_sf":{"A-410 restrooms (both)":50.6,"A-703":1.3,"A-705":1.3}},"expected":{"quantity":53.22,"unit":"SF"},"tolerancePct":0.5,"source":"238 / markup p16, p27, p32"},
 {"name":"WC-1 weather vestibule north wall to ceiling","formula":"runTimesHeight","inputs":{"run_lf":10.1,"height_ft":12.0,"height_basis":"WC1 @ 12'H; A-130 WEATHER VESTIBULE 12'-0\" A.F.F."},"expected":{"quantity":120.0,"unit":"SF"},"tolerancePct":1.0,"source":"239 / markup p08 (recomputes 121.2, +1.0%; estimator used 10 LF)"},
 {"name":"Assumed wallcovering over PT-7 wallcovering primer","formula":"runTimesHeight","inputs":{"run_lf":10.3,"height_ft":10.0,"primerTag":"PT-7","assumed":True},"expected":{"quantity":103.0,"unit":"SF"},"tolerancePct":0.1,"source":"240 / markup p08"},
 {"name":"FRP-1 behind 24x24 corner mop sink","formula":"runTimesHeight","inputs":{"walls_ft":[2.0,2.0],"height_ft":4.0,"basis":"FRP PANEL @ MOP SINK, BOTH SIDES; MSK-2424; 48\" H"},"expected":{"quantity":16.0,"unit":"SF"},"tolerancePct":0.1,"source":"241 / markup p08, A-410 det 1 & 3"},
 {"name":"CROSS-CHECK restroom tile band, both rooms (WT-1+WT-2+WT-9 on A-410)","formula":"bandArea x roomRepeat","inputs":{"walls_ft":[7.5083,7.675,4.0056,0.3333],"walls_basis":"A-410 elevations B, C, D (D = 4'-0\" left of door + 4\" right of door frame), scaled from vectors at 1/2\"=1'-0\"","height_ft":5.5,"height_printed":"5'-6\"","openings":"door in D excluded from the wall list","roomRepeat":2,"repeat_basis":"NOTE: MENS INTERIOR ELEVATIONS ARE SIMILAR TO WOMENS"},"expected":{"quantity":215.1,"unit":"SF"},"tolerancePct":0.5,"source":"235+236+238 restroom share / markup p16"},
 {"name":"CROSS-CHECK A-703 service counter backsplash (WT-1+WT-2+WT-9)","formula":"bandArea","inputs":{"walls_ft":[6.75],"walls_printed":["3'-4\" + 3'-4\" + 1\""],"height_ft":2.6667,"height_printed":"32\""},"expected":{"quantity":18.0,"unit":"SF"},"tolerancePct":0.5,"source":"markup p27 / A-703 detail 2"},
 {"name":"CROSS-CHECK A-705 employee lounge backsplash (WT-1+WT-2+WT-9)","formula":"bandArea","inputs":{"walls_ft":[7.1667],"walls_printed":["2'-4\" x 3 + 2\""],"height_ft":1.5417,"height_printed":"1'-6 1/2\"","note":"microwave in front of the band not deducted"},"expected":{"quantity":11.1,"unit":"SF"},"tolerancePct":1.0,"source":"markup p32 / A-705 detail 2"},
 {"name":"CROSS-CHECK schedule mix fallback for the WT-1/2/9 blend","formula":"tagArea = blendArea x mixPct","inputs":{"blend_sf":244.13,"mix":{"WT-1":0.6,"WT-2":0.2,"WT-9":0.2}},"expected":{"quantity":146.48,"unit":"SF"},"tolerancePct":0.5,"source":"A-170 FINISHES SCHEDULE MIX 60%/20%/20% (WT-1 shown; estimator 144.19 = +1.6%, WT-2 +4.5%, WT-9 -8.3%)"}
]
json.dump(fx,open(OUT+'fixtures.json','w'),indent=1)
