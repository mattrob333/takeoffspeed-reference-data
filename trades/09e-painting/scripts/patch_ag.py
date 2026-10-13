p='/home/user/takeoffspeed-reference-data/trades/09e-painting/app-gaps.md'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,(a[:70],s.count(a)); s=s.replace(a,b)
rep("""### 2. The tech wall double count and the missing recess returns (PT-4/PT-6, 37.2 SF, 24% of line 296)

The estimator's PT-4 run includes the PT-6 recess back.""",
"""### 2. The tech wall double count and the recess returns (PT-4/PT-6, 37.2 SF, 24% of line 296)

The estimator's PT-4 run includes the PT-6 recess back. It also steps around the recess (10.6 FT against the 9'-9 3/4" wall), so the side returns are already in it at the depth drawn on A-150; only the head and sill returns (about 12.4 SF) are absent.""")
rep("""Add `returns` (LF × depth) for recess and reveal returns. A-704 "PAINT REC""","""Add `returns` (LF × depth) for recess and reveal returns, with a warning when the wall run already traces the returns in plan. A-704 "PAINT REC""")
rep("""The estimator rounds small hand-entered lines up to 5 (F9):""","""The estimator rounds most small hand-entered painting lines up to 5 (F9, 7 of 11 small lines; wallcovering lines 239/240 do not follow it):""")
rep("""- `doors-frames` primes frames that 08 1113 ships primed (09 9100 3.3.B.2: omit primer).""",
    """- `doors-frames` primes frames that 08 1113 ships primed. That matches this estimator's 1P + 2C and 09 9110's HM primer row; 09 9100 3.3.B.2 would allow touch-up priming only, so it is a convention choice.""")
rep("""- Add `shopPrimed: yes` on `doors-frames` to set `primerCoats = 0`.""",
    """- Add an optional `shopPrimed: yes` on `doors-frames` (default off, matching this estimate) to set `primerCoats = 0` or a touch-up fraction.""")
rep("""| Recess / reveal `returns` (LF × depth) | PT-4 returns | A-704 "PAINT RECESS RETURNS ALL SIDES, PT-4" |""",
    """| Recess / reveal `returns` (LF × depth) | PT-4 head/sill returns (side returns already in the run here) | A-704 "PAINT RECESS RETURNS ALL SIDES, PT-4" |""")
rep("""The estimator's PT-1 is 339.1 LF of room-face runs at room heights, with **no opening deduction**.""",
    """The estimator's PT-1 is 339.1 LF of room-face runs at room heights, with **no opening deduction on those runs** (only the A-410 elevation polygons are cut around doors).""")
open(p,'w').write(s)
