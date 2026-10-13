P='/home/user/takeoffspeed-reference-data/trades/01-demolition/reading-guide.md'
s=open(P).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a[:70]
    s=s.replace(a,b)
rep("One-storey: a rectangle 52.4' × 32.9' = 1,716 SF. |",
    "One-storey: a slightly skewed 5-vertex outline, 1,716.4 SF in CAD (bounding box 52.4' × 32.9'; about 52.1' × 32.9' effective) and 1,713.7 SF traced. |")
rep("Count the treads (grey parallel lines): 7. |",
    "Count the drawn step lines (grey horizontal lines) from the top landing down to the walk edge: 7. Their spacing is unequal (7.7\" to 18.7\"), so count lines; do not divide a run by a tread depth. |")
rep("""- **Tick counting:** demolition linetypes have a fixed tick pitch. Use LF ≈ ticks × pitch: `///` every
  5.0 ft, and `++++` one pair every 2.0 ft. Curb gives 982 LF (vs 987.2) and power/TEL gives 970 LF
  (vs 965.4).""",
"""- **Tick counting:** demolition linetypes have a fixed tick pitch. Use LF ≈ ticks × pitch: `///` every
  5.0 ft (the ticks are `///` text glyphs in the text layer, 222 on the plan), and `++++` one full
  crossing tick every 2.0 ft. Power/TEL gives 194 × 5 = 970 LF (vs 965.4) and curb ≈ 484 × 2 = 967 LF
  (vs 987.2).
- **Chain length:** the firmer check is the length of the linetype polylines themselves, chained in
  drawing order (each polyline is a run of 18 pt or 7.2 pt pieces). Power/TEL 983.4 LF (estimator −1.8%),
  curb 975.2 LF (+1.2%), water 55.8 LF, gas 87.1 LF. Do not chain by shared endpoints alone: the
  utility and curb linetypes are both black 0.72 pt and merge where they cross.""")
rep("the GAS line (about 85 LF, 17 ticks) from", "the GAS line (87.1 LF, 17 ticks) from")
open(P,'w').write(s)
