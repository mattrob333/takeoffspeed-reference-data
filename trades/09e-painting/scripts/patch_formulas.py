p='/home/user/takeoffspeed-reference-data/trades/09e-painting/formulas.md'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,(a[:70],s.count(a)); s=s.replace(a,b)
rep("""Openings are **not** deducted in the estimator's method. Tile, FRP and wallcovering zones are excluded because they are never traced as paint runs: the restrooms are carried as elevation areas above the band, and the WC-1 and FRP-1 walls have their own runs.""",
"""Openings are **not** deducted from the finish-plan runs (the A-150 LF × H rows). Traced elevation areas can deduct them: on A-410 the elevation A polygon is cut around the door and the D polygons are notched at the door head, although the estimator's duplicate of A for the Men's room is a full rectangle that leaves about 23 SF of door in. Tile, FRP and wallcovering zones are excluded because they are never traced as paint runs: the restrooms are carried as elevation areas (A full height, B/C/D above the tile band), and the WC-1 and FRP-1 walls have their own runs.""")
rep("""| PT1 WALL PAINT (p16, A-410, both restrooms) | | | 252.60 |""",
    """| PT1 WALL PAINT (p16, A-410, both restrooms; A full height less door, B/C/D above tile, copy of A without door cut) | | | 252.60 |""")
rep("""**Line 296 (PT-4).** 5.3 × 9 + 10.6 × 10 = 47.7 + 106.0 = **153.70** SF, against 153.62 (+0.05%; the display bound is ±0.95).""",
    """**Line 296 (PT-4).** 5.3 × 9 + 10.6 × 10 = 47.7 + 106.0 = **153.70** SF, against 153.62 (+0.05%; the display bound is ±0.95). The 10.6 FT tech-wall run steps around the A-704 recess (front, both side returns at the depth drawn on A-150, recess back), so it already holds the side returns and also the 37.2 SF PT-6 back wall.""")
rep("""**Rule (as carried):** `LF_paint = LF_trim(line 88) = 910`.""",
    """**Rule (as carried):** `LF_paint = LF_trim(line 88) = 910`. `reconciliation.csv` therefore carries `recomputedQty` 910, `deltaPct` 0, classification `copied/allowance`; the back-fit below lives in the notes only.""")
rep("""**Rule (observed on this job):**
- A quantity that the estimator copies by hand from a single small legend row is rounded **up to the next multiple of 5**: `ceil5(x) = 5 × ⌈x / 5⌉`.""",
"""**Rule (observed on most small painting lines, not a job-wide habit):**
- A quantity that the estimator copies by hand from a single small legend row is usually rounded **up to the next multiple of 5**: `ceil5(x) = 5 × ⌈x / 5⌉`.""")
rep("""**Basis.** Every example on this job is listed here:""",
    """**Basis.** Every small hand-entered example found on this job, including two wallcovering lines (folder 09d) built from the same A-150 runs:""")
rep("""| 802.04 (300) | 802 | 805 | no, nearest |
""","""| 802.04 (300) | 802 | 805 | no, nearest |
| 121.2 (239, WC-1: `WC1 @ 12'H` 10.1 FT × 12) | 120 | 125 | no, rounded down / nearest 5 |
| 103.0 (240, `WALL COVERING @ 10'H ABOVE PT7` 10.3 FT × 10) | 103 | 105 | no, unrounded |
""")
rep("""The rule fits seven of nine. GPT-6 Astra""",
    """The rule fits **7 of 11**. The same raw 103 SF (10.3 FT × 10) is carried as 105 on line 298 and as 103 on line 240, so the rounding is a per-line hand choice rather than a rule. GPT-6 Astra""")
open(p,'w').write(s)
