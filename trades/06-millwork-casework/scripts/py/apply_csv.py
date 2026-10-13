import csv, io
P='/home/user/takeoffspeed-reference-data/trades/06-millwork-casework/reconciliation.csv'
rows=list(csv.reader(open(P,newline='')))
H=rows[0]; ix={h:i for i,h in enumerate(H)}
def upd(line, **kw):
    for r in rows[1:]:
        if r[0]==str(line):
            for k,v in kw.items(): r[ix[k]]=v
            return
    raise KeyError(line)
upd(102, source='A-700 back elev 3 + elev 6 (PL-3 band under the SLD-1 edge); markup p23 legend PL3 FINISH (coral)',
    sourceValues='back elev 3 band 10\'-6 3/4" - 11" = 9\'-7 3/4"; elev 6 band 11" + 24 1/2" = 35 1/2"; band height 6 1/4" (left string 1 1/4" SLD-1 edge / 6 1/4" PL-3 / 1 1/4"); legend 6.6 SF',
    formula='SF = Σ band length x 6 1/4"; estimator rounds up to whole SF', recomputedQty='6.565', deltaPct='6.63', classification='derived',
    notes='Estimate 7.0 = legend 6.6 rounded up. The 7 1/2" string includes the 1 1/4" quartz edge above the band; the coral polygon starts at the underside of that edge (pixel height ~6"), so the legend equals the printed area.')
upd(116, sourceValues='front elevation 9\'-1 1/2" x 8\'-6" minus CASED OPENING 3\'-6" x 7\'-0" (faces: 1 1/2" stile x 8\'-6" + head 3\'-6" x 1\'-6" + 5\'-6" x 8\'-6"); legend 95.6 SF',
    formula='SF = Σ exposed front-face W x H net of the cased opening', recomputedQty='53.06', deltaPct='80.92', classification='measured (legend unreliable)',
    notes='Legend defect, not rounding. Pixel check of the p25 salmon polygon (8\'-6" = 631 px at zoom 3): upper millwork ~37 SF, cased-opening fill ~19 SF, overrun past the millwork over blank sheet/title block ~23 SF, plan polygon ~9 SF; ~42 SF of the elevation polygon is outside the millwork and the drawer fronts are not covered. Estimate 96 = 95.6 rounded up. Adding the cased-opening jamb/head linings (2 x 7\'-0" x 1\'-4" + 3\'-6" x 1\'-4" = 23.3 SF) gives 76.4 SF; no face set reproduces 96.')
upd(139, source='A-707 plan 1 + plan 2 (back walls: bottom edge of plan 1, top edge of plan 2); markup p30 legend 4"H PL2 BASE O/ 3/4"THK. PLYWOOD (cyan)',
    sourceValues='plan 1: 6\'-4 1/8" - 7 5/8" = 5\'-8 1/2" back + notch 1\'-1 3/4" + 7 5/8" + stub end 10 1/4"; plan 2: 5\'-4" back; legend 13.6 FT',
    formula='LF = Σ wall-abutting top edges traced in cyan; estimator rounds up to whole LF', recomputedQty='13.677', deltaPct='2.36', classification='derived',
    notes='Estimate 14 = legend 13.6 rounded up (legend -0.6% vs printed). Pixel trace (p30, zoom 8): one cyan polyline on plan 1 along back edge 69.8", notch 13.8" and 7.5", stub end 10.2"; plan 2 back 64.4"; no cyan on the plan-1 left end or plan-2 right end (no 2\'-0" return). Cyan on the 6\'-4 1/8" and 5\'-4" front edges belongs to the same-colour (2) 1x4 blocking row.')
upd(140, sourceValues='legend 11.0 SF (~5\'-4" to 5\'-6" wall to wall x 2\'-0")',
    notes='Measured at 1/4"=1\' on the floor plan. A-708 det.10 draws the top wall to wall (scales ~5\'-4" against the 3\'-9 7/8" string); 3\'-9 7/8" is the wall-to-pedestal (MS-03) clearance, not the top width.')
upd(142, sourceValues='4 faces 8\'-0" x 9\'-0" (outside: plan 1 8\'-0"; inside: section 5 1\'-11 1/2" + 1/2" + 4\'-0" + 1/2" + 1\'-11 1/2" = 8\'-0") + 2 jambs 9" x 9\'-0" + header 10\'-0 1/2" x 9"',
    recomputedQty='309.031', deltaPct='-2.92', classification='measured',
    notes='Estimate 300 = legend 296.9 rounded up (+1.0%). The legend is not a clean measurement: the section-5 polygon runs ~2x the booth length past the booth over the title block, and two polygons sit on the NTS 3D view (det.10). Inside faces stopped at the PNL-1 pocket (7\'-8") give 303.03 SF. No wall face prints 7\'-6" (that is the ceiling length, RCP 11).')
upd(344, sourceValues='p23 = plan top 41.1 (bar 10\'-6 3/4" x 2\'-11 1/2" + right end 1\'-2 1/4" x 1\'-9 5/8" + return 2\'-0" x 3\'-10 1/4") + vertical/waterfall faces ~32.3 (legend minus plan; elev 3,4,5,6); p24 8\'-8" x 2\'-1" = 18.06; p26 9\'-10" x 2\'-0" = 19.67')
o=io.StringIO(); csv.writer(o,lineterminator='\r\n').writerows(rows); open(P,'w',newline='').write(o.getvalue())
# counts
import collections
d=[abs(float(r[ix['deltaPct']])) for r in rows[1:]]
print('n',len(d),'<=1',sum(x<=1.0 for x in d),'<1',sum(x<1.0 for x in d),'<=5',sum(x<=5 for x in d))
print('over5',[(r[0],r[ix['deltaPct']]) for r in rows[1:] if abs(float(r[ix['deltaPct']]))>5])
print('1-5',[(r[0],r[ix['deltaPct']]) for r in rows[1:] if 1<abs(float(r[ix['deltaPct']]))<=5])
print(collections.Counter(r[ix['classification']] for r in rows[1:]))
