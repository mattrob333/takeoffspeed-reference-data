# 01 — Demolition formulas

Every quantity is a removal scope quantity. None carries waste. Units follow the estimate: LF, SF, CFT, EA.
Sheet scale 1" = 20' (C-1.0), so 72 pt = 20 ft and 1 pt = 0.27778 ft.

## F1 — Building removal volume (lines 3, 4)

- **Inputs:** `footprintSF` (SF, the area of the ⊠-hatched outline under keynote 2, traced in PlanSwift),
  `stories` (EA, from the survey label "TWO STORY BUILDING" / "ONE STORY BUILDING"), `storyHeight` (FT).
- **Rule:** `CF = round(footprintSF × stories × storyHeight, −1)`, i.e. rounded to the nearest 10 CF.
- **Convention:** storyHeight = **10 ft per storey**. This is the estimator's own value, computed from
  this job: 89,780 / 4,489.1 = 19.9996 ft for 2 storeys, and 17,140 / 1,713.7 = 10.0018 ft for 1 storey.
  The plans give only F.F.E. elevations (442.2', 440.3'), never a height. No foundation or basement depth
  is added, even though the line says "AND FOUNDATION".
- **Rounding:** 4,489.1 × 20 = 89,782 → 89,780, and 1,713.7 × 10 = 17,137 → 17,140. Both match "nearest
  10 CF". They also match "footprint rounded to whole SF first" (4,489 × 20, 1,714 × 10). Either reading
  gives the same result here.
- **Worked example:** 4,489.1 SF × 2 × 10 ft = 89,782 CF → **89,780 CFT** (estimate 89,780, 0.000%).
  1,713.7 × 1 × 10 = 17,137 → **17,140 CFT** (0.000%).

## F2 — Area removal (lines 5, 7, 9)

- **Inputs:** `areas[]` (SF), one per closed polygon of one removal type (pavement dot hatch under KN7,
  sidewalk KN9, concrete ramp KN11).
- **Rule:** `SF = Σ areas`. There is no deduction and no thickness. Striping rides on the pavement line
  ("W/ PAVEMENT STRIPING").
- **Worked example:** pavement 19,363.6 SF → 19,363.57 in the estimate (−0.0002%). Sidewalk 390.2 →
  390.17. Ramp 442.4 (two polygons: the sidewalk/ramp north of the two-storey building plus a small pad
  west of the one-storey building) → 442.37.
- **CAD check, polygon method:** shoelace on the black 0.48 pt outlines, closed along the building
  outline. Sidewalk: L-walk 331.3 SF + south apron to the gas line 49.0 SF = 380.3 SF (estimator +2.6%).
  Ramp: path 5685 closed along the two-storey outline (1147.3,1001.0) → (1183.6,1000.3) → (1269.5,1001.0)
  → (1269.5,1007.8) = 406.4 SF, plus the 10.8 SF west pad = 417.2 SF (estimator +6.0%). Close the
  polygon in path order: appending the closing vertices in reverse makes a self-intersecting outline
  (that error produced an earlier, wrong 467.8 SF).
- **CAD check, dot-hatch method:** `SF ≈ dots × pitchX × pitchY × (20/72)²`. The pavement hatch is a
  staggered dot grid at a 7.5 pt in-row pitch and a 7.5 pt row pitch, so each dot stands for
  7.5 × 7.499 × 0.07716 = 4.3397 SF. There are 4,556 dots, giving 19,771.7 SF (the estimator is −2.1%).
  The edge effects of the dot grid make this a ±3% check, not a measure.

## F3 — Linear removal (lines 2, 11, 12, 13, 14)

- **Inputs:** `runs[]` (LF), traced along one demolition linetype: `++++` for curb, `///` for utilities,
  and the survey line labelled METAL HANDRAIL.
- **Rule:** `LF = Σ runs`.
- **Worked examples:** curb 987.2 → 987.22. Water 55.6. Power 965.4 → 965.36. Handrail 76.2. Storm
  107.1 → 107.11.
- **CAD check, tick-count and chain-length methods:** demolition linetypes put ticks at a fixed paper
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
    filter finds only about 145 of them.
  - Storm: JB centre (x = 679.86 pt) to HW centre (x = 1,063.5 pt) = 383.6 pt × 0.27778 =
    **106.57 LF** (the estimate is +0.51%). The pipe line alone is 105.37 LF.
- **Convention:** "power line" (KN5) covers every ticked dry-utility line: overhead power, underground
  power and telephone. Only water (KN6) and storm (KN4) get their own lines.

## F4 — Counts (lines 6, 8, 10, 15)

- **Inputs:** `count` (EA) of tags or symbols.
- **Rules:**
  - Monument sign = count of KN10 tags = 1.
  - Trees = count of `X` DEMOLISH EXISTING TREE symbols = 2. These match the 2 KN8 tags.
  - Storm structures = the structures at the ends of the KN4 storm line (JB + HW) = 2.
  - Brick stair steps = **number of drawn step lines (nosings) between the top landing and the walk**
    = 7. The unit is "each step", not "each stair". The 7 count dots are stacked on one stair.
- **Worked example, stair:** C-1.0 draws 7 grey horizontal step lines across the 8.7 ft wide stair at
  y = 953.4, 955.7, 958.7, 961.8, 964.8, 967.8 and 973.4 pt (the last on the walk edge), below a slanted
  top landing edge from (1149.5, 955.2) to (1180.3, 940.1). The spaces are unequal (7.7", 10.0", 10.3",
  10.0", 10.0", 18.7"), so the plan gives no uniform tread depth; the count of lines is the measure:
  **7 EA**.

## Rounding and precision

The PlanSwift legend prints one decimal. The estimate carries PlanSwift's two decimals (987.22, 390.17,
442.37, 19,363.57, 965.36, 107.11). The derived CFT lines are rounded to 10 CF. An engine fixture should
use a ±0.5% tolerance on measured lines and ±0.1% on the CFT lines.

## Fixture form (`fixtures.json`)

There are 12 fixtures for the 14 lines: the stair steps (line 8) ride on the ramp fixture as
`stairSteps` of `demolition.pavement`, and the storm structures (line 15) ride on the storm-line fixture
as `structures` + `structureType` of `demolition.utility`, because the engine emits those EA lines only
from the parent record (`description` + `areas`, and `utility` + `runs`, are required). `assembly` is
always a registry id. `inputs` keeps the measured values as `{value, unit}`; `engineInputs` is the same
record as the engine's input strings (`"442.4 SF"`, `"987.2 LF"`, `"10'"`, `"7"`, `"yes"`), which is what
`tests/quantities/site-demolition.test.ts` passes. `expectedLines` gives each estimate line with the
engine line key, quantity, unit and tolerance; all 14 pass against the current engine.
