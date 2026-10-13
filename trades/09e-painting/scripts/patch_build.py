p='/home/user/work/09e-painting/build.py'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,(a[:60],s.count(a)); s=s.replace(a,b)
rep("""'339.1 LF of runs on A-150; restrooms 112/113 measured as areas above the tile band on A-410 elevations (both rooms). Delta is legend 1-decimal display; line carries PlanSwift precision. No opening deduction visible in the method.'""",
"""'339.1 LF of runs on A-150 (no opening deduction on the A-150 runs). Restrooms 112/113 are traced as areas on the A-410 elevations: elevation A full height (base to ceiling) less the door, B/C/D above the 5\\'-6" tile to the 9\\'-0" ceiling; each polygon is duplicated for the Men\\'s room, and the duplicate of A is a full rectangle that omits the door cut-out (about 23 SF high). Pixel check: A 39.8 + 62.9 SF (door cut 23.6), B/C/D 52.7/53.8/42.5 SF; GPT-6 Astra 252.5 SF. Delta is legend 1-decimal display; line carries PlanSwift precision.'""")
rep("""Tech-wall run is not net of the PT-6 recess back wall (37.2 SF carried again on line 297); recess returns (PT-4, A-704) not added.')""",
"""Tech-wall run is not net of the PT-6 recess back wall (37.2 SF carried again on line 297). The 10.6 FT run steps around the recess on the p08 raster (left pier front, return, recess back, return, right pier front; pixel trace 10.59 ft against the 9\\'-9 3/4" A-704 overall width, GPT-6 Astra traces the same path), so the two side returns are in the run at the depth drawn on A-150 (about 0.39 ft, vs 9 1/2" on A-704) and at the full 10 ft height. The head and sill returns of the recess (2 x 7\\'-9 3/4" x 9 1/2" = 12.4 SF) cannot come from a plan run and are not carried.')""")
rep("""A-130 note E says gypsum ceilings are PT-1, but the RCP tags read PT-3 and A-170 PT-3 = FLAT; the estimator followed the tags.""",
"""A-130 note E says gypsum ceilings are PT-1, but the RCP tags read PT-3, A-170 PT-3 = FLAT, and the A-170 FINISHES SCHEDULE CEILINGS group row GWB-1 PAINTED GYP. assigns PT-3 explicitly; two schedule sources back the estimator\\'s PT-3 against one general note (RFI still advisable).""")
rep("""08 1113 p214 frames ship "Exposed Finish: Prime" and 09 9100 3.3.B.2 says omit primer on shop-primed metal, so the carried field primer coat is conservative.')""",
"""08 1113 p214 frames ship "Exposed Finish: Prime". 09 9100 3.3.B.2 omits the field primer only where the shop primer is intact and touched up, p320 says this section\\'s priming is in addition to shop priming, and 09 9110 p328 still schedules a primer for Hollow Metal Frames and Doors (SW ProCryl B66-1310 / BM V131 / PPG Pitt Tech). The carried 1P+2C is a defensible contractor convention; flag it.')""")
rep("""    'LF = line 88 (assumed). Back-fit hypothesis: 2 faces x (sum door 2H+W + sum window perimeters), rounded up to 10',back,
    'allowance/judgment (copied from an ASSUMED carpentry line)','No drawing""",
"""    'LF = line 88 (copied; assumed allowance)',L[88]['quantity'],
    'copied/allowance (from an ASSUMED carpentry line; not a measured reconciliation)','recomputedQty is the copied line 88 value, not a rebuild. No drawing""")
rep("""print('within1',sum(abs(r['deltaPct'])<=1 for r in rows),'within5',sum(abs(r['deltaPct'])<=5 for r in rows))""",
"""meas=[r for r in rows if not r['classification'].startswith('copied')]
print('measured within1',sum(abs(r['deltaPct'])<=1 for r in meas),'measured within5',sum(abs(r['deltaPct'])<=5 for r in meas),'of',len(meas),'+ copied',len(rows)-len(meas))""")
# fixture area label
rep("""areas_sf={'A-410 restrooms above tile (both rooms)':a410}""","""areas_sf={'A-410 restrooms, both rooms (elev A full height less door, B/C/D above tile; copy of A omits door)':a410}""")
open(p,'w').write(s)
