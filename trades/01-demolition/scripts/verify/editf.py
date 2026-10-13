P='/home/user/takeoffspeed-reference-data/trades/01-demolition/formulas.md'
s=open(P).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a[:60]
    s=s.replace(a,b)
rep("""- **Worked example:** pavement 19,363.6 SF → 19,363.57 in the estimate (−0.0002%). Sidewalk 390.2 →
  390.17. Ramp 442.4 (two polygons: the sidewalk/ramp north of the two-storey building plus a small pad
  west of the one-storey building) → 442.37.""",
"""- **Worked example:** pavement 19,363.6 SF → 19,363.57 in the estimate (−0.0002%). Sidewalk 390.2 →
  390.17. Ramp 442.4 (two polygons: the sidewalk/ramp north of the two-storey building plus a small pad
  west of the one-storey building) → 442.37.
- **CAD check, polygon method:** shoelace on the black 0.48 pt outlines, closed along the building
  outline. Sidewalk: L-walk 331.3 SF + south apron to the gas line 49.0 SF = 380.3 SF (estimator +2.6%).
  Ramp: path 5685 closed along the two-storey outline (1147.3,1001.0) → (1183.6,1000.3) → (1269.5,1001.0)
  → (1269.5,1007.8) = 406.4 SF, plus the 10.8 SF west pad = 417.2 SF (estimator +6.0%). Close the
  polygon in path order: appending the closing vertices in reverse makes a self-intersecting outline
  (that error produced an earlier, wrong 467.8 SF).""")
rep("""- **CAD check, tick-count method:** demolition linetypes put ticks at a fixed paper pitch, so
  `LF ≈ ticks × pitch`.
  - Curb `++++`: the tick halves sit 7.2 pt (2.0 ft) apart along the line, one above and one below it. So
    LF ≈ tick halves × 1.0 ft = 982 × 1.0 = **982 LF** (the estimate is +0.53%).
  - Utilities `///`: there is one tick every 18 pt (5.0 ft). Water has 11 ticks, so ≈ 55 LF; the actual
    line is 696 → 897 pt = 55.83 LF. Power plus telephone (OHP/UGP/TEL) has 222 − 11 − 17 = 194 ticks ×
    5 = **970 LF** (the estimate is −0.48%). Gas has 17 ticks, about 85 LF, and is not in the estimate.""",
"""- **CAD check, tick-count and chain-length methods:** demolition linetypes put ticks at a fixed paper
  pitch, so `LF ≈ ticks × pitch`. The firmer check is the length of the linetype polyline itself.
  - Curb `++++`: the linetype is drawn as 7.2 pt (2.0 ft) pieces with one full crossing tick (a 4.3 pt
    half above and one below the line) at every joint. So LF ≈ crossing ticks × 2.0 ft ≈ 484 × 2.0 =
    967 LF. Measured along the 10 site curb polylines: **975.2 LF** (the estimate is +1.2%).
  - Utilities `///`: the linetype is drawn as 18 pt (5.0 ft) pieces with a `///` text glyph every 18 pt
    along the line (n full pieces carry n + 1 glyphs). Water has 11 glyphs, so ≈ 55 LF; the actual
    line is 696.5 → 897.5 pt = 55.83 LF. The plan carries 222 `///` glyphs (223 with the legend sample):
    dry utilities (OHP/UGP/TEL) 222 − 11 water − 17 gas = 194 × 5 = 970 LF (the estimate is −0.48%).
    Measured along the 7 dry-utility polylines: **983.4 LF** (the estimate is −1.8%). Gas has 17
    glyphs and measures 87.1 LF (16 full 5 ft pieces plus two 3.5 ft ends); it is not in the estimate.
  - Do not count 18 pt pieces with a tight length tolerance: they print as 17.9–18.1 pt, and a ±0.05 pt
    filter finds only about 145 of them.""")
rep("""  - Brick stair steps = **number of treads** on the drawn stair = 7. The unit is "each step", not "each
    stair". The 7 count dots are stacked on one stair.
- **Worked example, stair:** the tread lines on C-1.0 run from y = 953.4 to y = 973.4 pt, a 5.56 ft run.
  Divided by 7 treads that is 9.5"/tread, a normal exterior tread, so the count is **7 EA**. The stair is
  8.7 ft wide.""",
"""  - Brick stair steps = **number of drawn step lines (nosings) between the top landing and the walk**
    = 7. The unit is "each step", not "each stair". The 7 count dots are stacked on one stair.
- **Worked example, stair:** C-1.0 draws 7 grey horizontal step lines across the 8.7 ft wide stair at
  y = 953.4, 955.7, 958.7, 961.8, 964.8, 967.8 and 973.4 pt (the last on the walk edge), below a slanted
  top landing edge from (1149.5, 955.2) to (1180.3, 940.1). The spaces are unequal (7.7", 10.0", 10.3",
  10.0", 10.0", 18.7"), so the plan gives no uniform tread depth; the count of lines is the measure:
  **7 EA**.""")
open(P,'w').write(s)
