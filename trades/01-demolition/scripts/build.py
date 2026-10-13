import json, csv, math
R='/home/user/takeoffspeed-reference-data'
OUT=R+'/trades/01-demolition/'
lines={l['lineNo']:l for l in json.load(open(R+'/reference/estimate/lines.json'))}
leg={i['name'].replace('  ',' '):i for pg in json.load(open(R+'/reference/markups/legends.json')) if pg['page']==64 for i in pg['items']}
def L(name): return leg[name]['quantity']
FT=20/72
def r10(x): return round(x/10)*10
rows=[]; fx=[]
def add(n,desc,src,sv,formula,rec,cls,notes,fixture=None):
    e=lines[n]['quantity']
    d=(rec/e-1)*100
    rows.append(dict(lineNo=n,description=desc,unit=lines[n]['unit'],estimatorQty=e,source=src,sourceValues=sv,formula=formula,recomputedQty=round(rec,4),deltaPct=round(d,3),classification=cls,notes=notes))
    if fixture: fixture['source']=f'line {n} / markup p64 (C-1.0)'; fixture['estimatorQty']=e; fx.append(fixture)
# 2 curb
v=L('1: REMOVE EXISTING CURB & GUTTER')
add(2,'KN1 remove existing curb & gutter','markup p64 teal linear "1: REMOVE EXISTING CURB & GUTTER"',f'{v} FT','LF = sum of traced curb runs',v,'measured',
 f'Traced along the CAD curb-demolition linetype (black line with ++++ ticks). CAD cross-check: 982 tick halves on C-1.0, one tick pair every 7.2 pt = 2.0 ft, so 982 x 1.0 ft = 982 LF; the estimator is {round((lines[2]["quantity"]/982-1)*100,2)}% over that. Mixed 24" C&G and 24" roll curb, all on one line.',
 dict(name='KN1 curb & gutter removal',formula='lf = sum(run_i)',inputs={'runs':[{'value':v,'unit':'LF'}],'curbType':'CURB & GUTTER','keynote':'1'},expected={'quantity':v,'unit':'LF'},tolerancePct=0.5))
# 3 two-story
a=L('2: REMOVE EXISTING TWO STORY BUILDING STRUCTURE AND FOUNDATION'); raw=a*2*10; rec=r10(raw)
add(3,'KN2 remove existing 2-story building & foundation','markup p64 red area "2: ... TWO STORY BUILDING..." + survey label "TWO STORY BUILDING"',f'{a} SQ FT; 2 stories; 10 ft/story (estimator convention)','CFT = footprint SF x stories x 10 ft, rounded to nearest 10 CF',rec,'derived',
 f'Unrounded {raw:.1f} CF ({(raw/lines[3]["quantity"]-1)*100:+.3f}%). The plans give no building height (the survey shows only F.F.E.= 442.2\'), so the 10 ft/story is the estimator\'s own convention: 89780/4489.1 = {lines[3]["quantity"]/a:.4f} ft. No foundation depth is added. CAD hatch polygon on C-1.0 = 4463.1 SF ({(a/4463.1-1)*100:+.2f}% PlanSwift vs CAD).',
 dict(name='KN2 two-storey building removal volume',formula='cf = round(footprint_sf * stories * story_height_ft, -1)',inputs={'footprintAreas':[{'value':a,'unit':'SF'}],'stories':{'value':2,'unit':'EA'},'storyHeight':{'value':10,'unit':'FT','basis':'estimator convention, no height on plans'},'rounding':'nearest 10 CF'},expected={'quantity':rec,'unit':'CF'},tolerancePct=0.1))
# 4 one-story
a=L('2: REMOVE EXISTING ONE STORY BUILDING STRUCTURE AND FOUNDATION'); raw=a*1*10; rec=r10(raw)
add(4,'KN2 remove existing 1-story building & foundation','markup p64 bright-green area "2: ... ONE STORY BUILDING..." + survey label "ONE STORY BUILDING"',f'{a} SQ FT; 1 story; 10 ft/story','CFT = footprint SF x stories x 10 ft, rounded to nearest 10 CF',rec,'derived',
 f'Unrounded {raw:.1f} CF ({(raw/lines[4]["quantity"]-1)*100:+.3f}%). 17140/1713.7 = {lines[4]["quantity"]/a:.4f} ft, so the same 10 ft/story. CAD hatch rectangle 52.4\' x 32.9\' = 1716.4 SF ({(a/1716.4-1)*100:+.2f}%).',
 dict(name='KN2 one-storey building removal volume',formula='cf = round(footprint_sf * stories * story_height_ft, -1)',inputs={'footprintAreas':[{'value':a,'unit':'SF'}],'stories':{'value':1,'unit':'EA'},'storyHeight':{'value':10,'unit':'FT','basis':'estimator convention'},'rounding':'nearest 10 CF'},expected={'quantity':rec,'unit':'CF'},tolerancePct=0.1))
# 5 sidewalk
v=L('9: REMOVE EXISTING SIDEWALK')
add(5,'KN9 remove existing sidewalk','markup p64 yellow area "9: REMOVE EXISTING SIDEWALK"',f'{v} SQ FT','SF = sum of traced sidewalk areas',v,'measured',
 'Yellow L-shaped walk on the north and west sides of the one-storey building ("CONCRETE SIDEWALK", 3 KN9 tags). CAD cross-check: CAD walk polygon closed on the building line = 380.8 SF (-2.4%). Another 67.3 SF apron at the south end is in CAD, and the trace appears to include part of it. Thickness is not shown.',
 dict(name='KN9 sidewalk removal',formula='sf = sum(area_i)',inputs={'areas':[{'value':v,'unit':'SF'}],'description':'SIDEWALK','keynote':'9'},expected={'quantity':v,'unit':'SF'},tolerancePct=0.5))
# 6 sign
add(6,'KN10 remove existing monument sign','markup p64 periwinkle count dot "10: REMOVE EXISTING  MONUMENT SIGN"','1 EA','EA = count of KN10 tags',1,'counted',
 'One count dot on the survey "BRICK SIGN" at the Watson Blvd frontage. The C-1.0 text layer has exactly one "10" keynote tag.',
 dict(name='KN10 monument sign removal',formula='ea = count(tag 10)',inputs={'count':{'value':1,'unit':'EA'},'feature':'MONUMENT SIGN','keynote':'10'},expected={'quantity':1,'unit':'EA'},tolerancePct=0))
# 7 ramp
v=L('11: REMOVE EXISTING CONCRETE RAMP')
add(7,'KN11 remove existing concrete ramp','markup p64 magenta area "11: REMOVE EXISTING CONCRETE RAMP"',f'{v} SQ FT','SF = sum of traced ramp/sidewalk areas',v,'measured',
 'Two magenta areas: (a) "CONCRETE SIDEWALK/RAMP" and the north "RAMP" strip between the brick steps and the two-storey building; (b) a small pad on the west side of the one-storey building with a KN11 tag. CAD polygon for (a), closed on the building line = 467.8 SF. The trace for (a) runs about 6-13% under the CAD polygon: it stops at the stair and the handrail lines. Keynote 11 reads "RAMP AND STAIRS"; the stairs are split out to line 8.',
 dict(name='KN11 concrete ramp removal',formula='sf = sum(area_i)',inputs={'areas':[{'value':v,'unit':'SF'}],'description':'CONCRETE RAMP','keynote':'11'},expected={'quantity':v,'unit':'SF'},tolerancePct=0.5))
# 8 steps
add(8,'KN11 remove existing brick stair steps','markup p64 rose-brown count dots (7 stacked) "11: REMOVE EXISTING BRICK STAIR STEPS"','7 EA','EA = count of treads/risers on the drawn stair',7,'counted',
 'Seven translucent dots are stacked on the one "BRICK STEPS" stair north of the two-storey building, so EA = each step, not each stair. CAD: tread lines between y=953.4 and 973.4 pt give a 5.56 ft run, 8.7 ft wide, about 9.5" per tread over 7 treads. GPT-6 Astra counted 8 lines and 7 tread spaces independently. The survey also labels brick steps on the west side of the two-storey building, but those sit inside the building hatch and are not counted.',
 dict(name='KN11 brick stair steps removal',formula='ea = count(treads)',inputs={'stairSteps':{'value':7,'unit':'EA'},'keynote':'11'},expected={'quantity':7,'unit':'EA'},tolerancePct=0))
# 9 pavement
v=L('7: REMOVE EXISTING PAVEMENT W/ PAVEMENT STRIPING')
add(9,'KN7 remove existing pavement w/ striping','markup p64 medium-green area "7: REMOVE EXISTING PAVEMENT W/ PAVEMENT STRIPING"',f'{v} SQ FT','SF = sum of traced pavement areas',v,'measured',
 f'All asphalt parking lot and drive inside the curb lines, 10 KN7 tags. CAD cross-check: the "DEMOLISH EXISTING PAVEMENT" dot hatch has 4556 dots on a 7.5 x 7.5 pt (2.083 ft) staggered grid, 4.3397 SF/dot = 19,771.7 SF ({(v/19771.67-1)*100:+.2f}%). Striping rides on the area line with no separate LF. Thickness is unknown, and there is no saw-cut line even though GDN 3 requires a full-depth saw cut at the limits.',
 dict(name='KN7 asphalt pavement removal incl. striping',formula='sf = sum(area_i)',inputs={'areas':[{'value':v,'unit':'SF'}],'description':'PAVEMENT','incidentals':'PAVEMENT STRIPING','keynote':'7'},expected={'quantity':v,'unit':'SF'},tolerancePct=0.5))
# 10 trees
add(10,'KN8 remove existing trees/vegetation','markup p64 slate-blue count dots "8: REMOVE EXISTING TREES/VEGETATION"','2 EA','EA = count of X tree symbols (KN8)',2,'counted',
 'Two "X" DEMOLISH EXISTING TREE symbols on C-1.0: one by the crosstie border north of the one-storey building, and one in the PINESTRAW ISLAND on the west. There are 2 KN8 tags. No DBH is labelled, so the trees are unsized.',
 dict(name='KN8 tree removal (unsized)',formula='ea = count(X symbols)',inputs={'unsized':{'value':2,'unit':'EA'},'keynote':'8'},expected={'quantity':2,'unit':'EA'},tolerancePct=0))
# 11 water
v=L('6: REMOVE EXISTING WATER LINE AND ASSOCIATED STRUCTURES')
add(11,'KN6 remove existing water line & structures','markup p64 teal linear "6: REMOVE EXISTING WATER LINE..."',f'{v} FT','LF = traced length of ticked W line',v,'measured',
 f'One E-W "W" line across the west parking lot, from the Westgate Dr. curb to the sidewalk (KN6 tags x2). CAD line from x=696 to 897 pt = 55.83 LF ({(lines[11]["quantity"]/55.83-1)*100:+.2f}%), carrying 11 demolition ticks at 5.0 ft spacing. The KN6 tag at the ICV south of the two-storey building has no separate LF.',
 dict(name='KN6 water line removal',formula='lf = sum(run_i)',inputs={'runs':[{'value':v,'unit':'LF'}],'utility':'WATER','keynote':'6'},expected={'quantity':v,'unit':'LF'},tolerancePct=0.5))
# 12 power
v=L('5: REMOVE EXISTING POWER LINE AND ASSOCIATED STRUCTURES')
add(12,'KN5 remove existing power line & structures','markup p64 red linear "5: REMOVE EXISTING POWER LINE..."',f'{v} FT','LF = traced length of all ticked dry-utility lines (OHP/UGP/TEL)',v,'measured',
 f'The red traces follow every utility line drawn with the "DEMOLISH EXISTING UTILITIES" /// linetype except water and gas. That is the two OHP/UGP diagonals from the pole at the north R/W and the TEL loop around the east and south of the two-storey building. CAD cross-check: 222 /// ticks on site, minus 11 water and 17 gas = 194 ticks x 5.0 ft = 970 LF ({(lines[12]["quantity"]/970-1)*100:+.2f}%). The telephone line is lumped into "power".',
 dict(name='KN5 power/telecom line removal',formula='lf = sum(run_i)',inputs={'runs':[{'value':v,'unit':'LF'}],'utility':'POWER','keynote':'5'},expected={'quantity':v,'unit':'LF'},tolerancePct=0.5))
# 13 handrail
v=L('REMOVE EXISTING METAL HANDRAIL')
add(13,'Remove existing metal handrail (no keynote)','markup p64 bright-green linear "REMOVE EXISTING METAL HANDRAIL"',f'{v} FT','LF = traced length along survey "METAL HANDRAIL" lines',v,'measured',
 'Traced along the survey linework labelled "METAL HANDRAIL": the edge of the walk from the steps to the ramp (30.2 ft), both sides of the north ramp (14.6 + 23.7 ft) and short pieces on both sides of the brick stair. CAD bracket: 68.5 LF without the stair sides and 79.6 LF with the full stair sides; 76.2 sits inside. No keynote, because the engineer did not keynote it; the estimator added it under GDN "all appurtenances".',
 dict(name='Metal handrail removal',formula='lf = sum(run_i)',inputs={'runs':[{'value':v,'unit':'LF'}],'feature':'METAL HANDRAIL'},expected={'quantity':v,'unit':'LF'},tolerancePct=0.5))
# 14 storm
v=L('4: REMOVE EXISTING STORM SEWER LINE AND ASSOCIATED STRUCTURES - ASSUMED')
add(14,'KN4 remove existing storm sewer line - ASSUMED','markup p64 yellow linear "4: ... STORM SEWER LINE ... - ASSUMED" (under legend box)',f'{v} FT','LF = traced length JB to HW',v,'measured',
 f'Hidden under the PlanSwift legend on the markup. The line runs along the south property line, from the JB (TOP 438.35, I.E. OUT 434.75) to the HW 15" HDPE (TOP 438.00, I.E. IN 434.96). CAD: pipe line 105.37 LF, JB centre to HW centre 106.57 LF ({(lines[14]["quantity"]/106.57-1)*100:+.2f}%). "ASSUMED" because no KN4 tag is placed on the plan; keynote 4 exists only in the KEY NOTES list.',
 dict(name='KN4 storm sewer removal (assumed)',formula='lf = sum(run_i)',inputs={'runs':[{'value':v,'unit':'LF'}],'utility':'STORM SEWER','size':'15"','material':'HDPE','assumed':True,'keynote':'4'},expected={'quantity':v,'unit':'LF'},tolerancePct=0.5))
# 15 structures
add(15,'KN4 remove existing storm structure','markup p64 periwinkle count dots "4: REMOVE EXISTING STORM STRUCTURE" (under legend box)','2 EA','EA = count of structures at ends of line 14',2,'counted',
 'Two faint dots under the legend: the JB at the west end and the 15" HDPE headwall at the east end of the storm line. The buried manhole further north ("MANHOLE NOTE FIELD LOCATED (COVERED UP/ BURIED)") is not counted.',
 dict(name='KN4 storm structures removal',formula='ea = count(structures on line)',inputs={'structures':{'value':2,'unit':'EA'},'structureType':'STORM STRUCTURE','utility':'STORM SEWER'},expected={'quantity':2,'unit':'EA'},tolerancePct=0))
with open(OUT+'reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
json.dump(fx,open(OUT+'fixtures.json','w'),indent=1)
for r in rows: print(r['lineNo'],r['estimatorQty'],r['recomputedQty'],r['deltaPct'],r['classification'])
print('within1',sum(abs(r['deltaPct'])<=1 for r in rows),'within5',sum(abs(r['deltaPct'])<=5 for r in rows),len(rows),len(fx))
