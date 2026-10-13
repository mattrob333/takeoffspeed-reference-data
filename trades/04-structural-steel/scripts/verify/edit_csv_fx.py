import csv, json
D='/home/user/takeoffspeed-reference-data/trades/04-structural-steel/'
rows=list(csv.DictReader(open(D+'reconciliation.csv')))
fields=list(rows[0].keys())
notes={
'40':"Sum of both pages. Audit: S-203 frame elevations (p35) repeat C-6 and D-6 (already on S-301 elev 10, 40.86 LF) and measure D-5 (20.21 LF), which the schedule calls HSS6X6X1/4. Schedule-true is ~172 LF: 8 full-height runs on p36 (155.68 LF) + B-4, the low-roof column, whose S-201 schedule bar runs from 1'-0\" below Level 1 to ~15.2 ft (the t/s 15'-2 1/4\" of the grid-B HSS4X4X1/4 beam), 16.2 ft (17.2 ft if its base is 2'-0\" down like the others). The stray 19.03 ft p36 run, if it is B-4, over-states it by ~1.8-2.8 ft (unproven).",
'45':"First of two HSS6x4x3/8 rows in legends.json p34 (item 33: 22.2 FT brown, 'duplicate name restored'; item 6: 9.0 FT periwinkle). The estimator keeps them as two lines (lines 45 and 46); duplicate legend names must not be merged.",
'61':"Plan trace (236.7, p34) follows the canopy outlines (north, east, south-east L, south-west L; bounding-box perimeters sum ~264 ft), not the bare parapets on grid A or grid 7 (no yellow line there). S-301 (177.8, p36) = parapet-top channels on the frame lines + two lower C7X9.8 runs in elevations 7 and 11 (15.0 + 14.6 = 29.6 LF, the ones with the canopy rain-leader note). Overlap exposure is those ~30 LF (6.9% of the line) where the plan canopy outline runs along line C (3-2) and line 2 (B-C); not provable from the overlay because the canopy fill is the same yellow.",
'69':"Roof perimeter closure angle per S-203 note and spec 05 1200 2.1.K (p90): min 4x3x1/4 continuous at roof perimeters and high/low roofs.",
'70':"3 joists x 17.99 ft. Confirmed measurement error: on S-203 the low-roof joists bear on the grid-B beam (strokes start 0.7 ft south of B; 13.47-13.59 ft each, 40.64 LF as drawn), but the p34 markup lines start at the top of the double-painted deck band, 3.3 ft north of grid B (same root cause as the deck strip, line 73). Drawing-true: 3 x 14.958 = 44.88 LF grid to grid (-9.08 LF, -16.8%), or 40.64 LF as drawn.",
'71':"10 joists x 24.86 ft (A to B = 25.17 ft c/c). High-roof markup lines end at the grid-B beam.",
'72':"4 joists x 27.12 ft. Confirmed measurement error (see line 70): low-roof markup lines start 3.3 ft north of grid B and end at grid D; S-203 strokes are 22.53-22.63 ft each (90.32 LF as drawn). Drawing-true: 4 x 23.99 = 95.96 LF grid to grid (-12.53 LF, -11.5%), or 90.32 LF as drawn.",
}
for r in rows:
    if r['lineNo'] in notes: r['notes']=notes[r['lineNo']]
with open(D+'reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
fx=json.load(open(D+'fixtures.json'))
table={"W8":"3/4x14x8-1/2","W10":"3/4x16x10-1/2","HSS4X4":"3/4x10x4-1/2","HSS5X5":"3/4x11x5-1/2","HSS6.00 ROUND":"3/4x13x7-1/2","HSS6X6":"3/4x12x6-1/2","HSS8X8":"3/4x14x8-1/2","HSS12X4":"3/4x12-1/2x9","HSS12.75 ROUND":"3/4x14x19"}
for f in fx:
    s=f['source']
    if s.startswith('line 36 '):
        f['inputs']['heightRoundingFt']=0.01
        f['formula']='member.lf = count x round(heightFt, heightRoundingFt)'
        f['tolerancePct']=0.1
        f['notes']="Estimator convention: 1'-7\" rounded to 1.58 ft before multiplying. Without the rounding input the exact answer is 6 x 1.5833 = 9.50 LF (+0.21%), which this tolerance rejects on purpose."
    if s.startswith('line 78 ') or s.startswith('line 79 '):
        f['inputs']['capPlateTable']=table
        f['inputs']['capPlateFallback']='next-smaller-listed-square-HSS'
        f['inputs']['plate']='3/4x11x5-1/2' if s.startswith('line 78 ') else '3/4x12x6-1/2'
        f['formula']='capPlates(plate) = count(columns whose size maps to plate via capPlateTable; unlisted sizes via capPlateFallback)'
        if s.startswith('line 79 '):
            f['notes']="S-681 det 8 has 9 rows and no HSS7X7. The estimator's fallback (next smaller listed square HSS = HSS6X6 plate) gives 11 + 5 = 16. Applying the table literally gives 11 EA plus 5 unmapped HSS7X7 columns; the width-based alternative would be 3/4x13x7-1/2 (the HSS6.00 ROUND row)."
json.dump(fx,open(D+'fixtures.json','w'),indent=1,ensure_ascii=False)
# verify fixtures
from fractions import Fraction as F
f36=[f for f in fx if f['source'].startswith('line 36 ')][0]
h=1+F(7,12); val=6*round(float(h),2); exact=6*float(h)
print('f36',val,abs(val/9.48-1)*100<=0.1, 'exact passes?',abs(exact/9.48-1)*100<=0.1)
cols={"HSS6X6":11,"HSS7X7":5,"HSS5X5":2}
def plates(plate,fallback=True):
    n=0
    for size,c in cols.items():
        p=table.get(size)
        if p is None and fallback: p=table['HSS6X6'] if size=='HSS7X7' else None
        if p==plate: n+=c
    return n
print('79',plates('3/4x12x6-1/2'),'literal',plates('3/4x12x6-1/2',False),'78',plates('3/4x11x5-1/2'))
print(len(rows),len(fx))
