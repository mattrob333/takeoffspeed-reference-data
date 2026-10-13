import csv
P='/home/user/takeoffspeed-reference-data/trades/01-demolition/reconciliation.csv'
rows=list(csv.DictReader(open(P,newline='')))
fields=list(rows[0].keys())
N={r['lineNo']:r for r in rows}
N['2']['notes']=('Traced along the CAD curb-demolition linetype (black 0.72 pt line with full crossing ticks, ++++). '
 'CAD cross-check on C-1.0: the linetype is drawn as 7.2 pt (2.0 ft) pieces with one full crossing tick at every joint, so LF ~ crossing ticks x 2.0 ft '
 '(about 484 ticks = 967 LF). Measured along the linetype itself, the 10 site curb polylines total 975.2 LF (legend sample excluded); the estimator is +1.2% over that. '
 'Mixed 24" C&G and 24" roll curb, all on one line.')
N['4']['notes']=('Unrounded 17137.0 CF (-0.018%). 17140/1713.7 = 10.0018 ft, so the same 10 ft/story. '
 "CAD hatch outline polygon (path 1290, 5 vertices, slightly skewed) = 1716.4 SF by shoelace, about 52.1' x 32.9' effective; its bounding box is 52.4' x 32.9' = 1724.7 SF. PlanSwift vs CAD polygon -0.16%.")
N['5']['notes']=('Yellow L-shaped walk on the north and west sides of the one-storey building ("CONCRETE SIDEWALK", 3 KN9 tags). '
 'CAD cross-check on the black 0.48 pt walk outline (path 4082): L-walk closed on the building line = 331.3 SF, plus the south apron down to the gas line '
 '(880.8-898.3 x 882.2-918.7 pt) = 49.0 SF, together 380.3 SF. The yellow trace includes the apron and stops at the gas line; the dotted corner south of it is pavement (line 9). '
 'Estimator +2.6% over 380.3 SF. Thickness is not shown.')
N['7']['notes']=('Two magenta areas: (a) "CONCRETE SIDEWALK/RAMP" and the north "RAMP" strip between the brick steps and the two-storey building, ending at the right-hand METAL HANDRAIL line (x = 1306.3 pt) and flaring at the curb; '
 '(b) a small pad on the west side of the one-storey building with a KN11 tag. '
 'CAD cross-check: the black 0.48 pt outline (path 5685) closed along the two-storey building outline (1147.3,1001.0)-(1183.6,1000.3)-(1269.5,1001.0)-(1269.5,1007.8) = 406.4 SF '
 '(walk 340.0 + N-S ramp 66.3); pad (b) 993.6-1007.3 x 882.2-892.4 pt = 10.8 SF; CAD total 417.2 SF. The estimator is +6.0% over CAD (+6.2% on (a) alone). '
 'GPT-6 Astra reads the trace as covering the walk strip and the ramp strip up to the curb, nothing east of the rail, and the stair treads not visibly included. '
 'Keynote 11 reads "RAMP AND STAIRS"; the stairs are split out to line 8.')
N['8']['notes']=('Seven translucent dots are stacked on the one "BRICK STEPS" stair north of the two-storey building, so EA = each step, not each stair. '
 'CAD: 7 grey 0.96 pt horizontal step lines across the 8.7 ft wide stair at y = 953.4, 955.7, 958.7, 961.8, 964.8, 967.8 and 973.4 pt (the last on the walk edge), '
 'with a slanted top landing edge from (1149.5,955.2) to (1180.3,940.1). The spaces are unequal: 7.7", 10.0", 10.3", 10.0", 10.0" and 18.7", so no uniform tread can be read. '
 'EA = number of drawn step lines between the top landing and the walk = 7. GPT-6 Astra independently counted 7 grey tread lines and would record 7 steps, '
 'though the plan alone does not fix a riser count. The survey also labels brick steps on the west side of the two-storey building, but those sit inside the building hatch and are not counted.')
N['11']['notes']=('One E-W "W" line across the west parking lot, from the Westgate Dr. curb to the sidewalk (KN6 tags x2). '
 'CAD line from x = 696.5 to 897.5 pt = 55.83 LF (-0.41%): 10 full 18 pt (5.0 ft) linetype pieces plus two 10.4 pt ends, carrying 11 "///" tick glyphs at an 18 pt pitch '
 '(GPT-6 Astra also counts 11). The KN6 tag at the ICV south of the two-storey building has no separate LF.')
N['12']['notes']=('The red traces follow every utility line drawn with the "DEMOLISH EXISTING UTILITIES" /// linetype except water and gas: '
 'the OHP/UGP fan from the pole at the north R/W (the north R/W runs and the diagonals) and the TEL loop around the east and south of the two-storey building. '
 'CAD cross-check on C-1.0: the linetype is drawn as 18 pt (5.0 ft) pieces with one "///" text glyph every 18 pt along the line. The text layer holds 223 "///" glyphs, 222 on the plan '
 '(1 in the legend): 141 + 53 on the dry utilities, 17 on gas, 11 on water. Dry ticks 194 x 5.0 ft = 970 LF (-0.48%). '
 'Measured along the 7 dry-utility polylines themselves (chained in drawing order): 265.9 + 178.6 + 169.1 + 107.5 + 102.1 + 90.1 + 70.1 = 983.4 LF; the estimator is -1.8% under that. '
 'The telephone line is lumped into "power".')
w=csv.DictWriter(open(P,'w',newline=''),fieldnames=fields,quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
w.writeheader(); [w.writerow(r) for r in rows]
