# Formulas — 04 structural steel, joists, deck, misc. metals

Units: LF = linear feet, SF = square feet, EA = each. Feet-and-inch heights convert as ft + in/12. Every
number below was computed with Python (`trades/04-structural-steel/scripts/recon.py`).

## F1. Member LF by shape and role (beams, channels, angles, braces, joists)

- **Inputs:** `lengths[]` (LF): every legend row for the same shape and role, on every markup page that carries it.
- **Rule:** `LF = Σ lengths`. Each physical member is measured once: plan length for beams, channels,
  angles, H.B. and joists, and work point to work point in elevation for diagonal braces.
- **Convention:** the estimator keeps two legend rows of the same shape as two lines when they were
  drawn as separate items (HSS6x4x3/8: 22.24 and 8.98 LF, two swatches, runs at t/s 12'-8 5/8" and
  10'-8 5/8"; both rows, 22.2 and 9.0 FT, are in legends.json p34). Key the line by shape + role +
  location/elevation, and never merge legend rows that share a name.
- **Check (joists):** measured joist LF ≤ count × bearing-grid span (+ seat/extension allowance). On this
  job the low-roof joists fail it: lines 70 and 72 carry 53.96 and 108.49 LF against 3 × 14.958 = 44.88 and
  4 × 23.99 = 95.96 LF grid to grid (40.64 and 90.32 LF as drawn on S-203). The markup lines start 3.3 ft
  north of grid B, at the top of the double-painted deck band (see F6); this is a confirmed measurement
  error, not a convention. The fixtures still reproduce the estimator's LF.
- **Worked example (line 61, C7x9.8):** 236.7 (S-203 p34) + 14.0 (S-203 p35) + 177.8 (S-301 p36) =
  **428.5 LF** (estimator 428.46).
- **Worked example (line 53, W10x12):** 51.5 (plan) + 4.8 (S-301 elev 9 strut) = **56.3 LF** (56.26).

## F2. Column LF from elevations

- **Inputs:** one run per column (LF), from the bottom of the base plate (top of pier/footing) to the top
  of steel, here the top of the parapet channel. The scale on S-301/S-203 frame elevations is
  3/16" = 1'-0", which is 6.2007 pt/ft on the half-size markup pages.
- **Rule:** `LF = Σ run_i` over the unique column grid IDs of that size.
- **Cross-check rule:** `count(runs) = count(column schedule entries of that size)`. The column schedule
  (S-201) gives 18 columns: HSS7X7X1/2 ×5, HSS6X6X3/8 ×9, HSS5X5X3/8 ×2, HSS6X6X1/2 ×1, HSS6X6X1/4 ×1.
- **Worked example (line 41, HSS7x7x1/2):** 5 columns (A-1, A.5-1, B-1, C-2, C-3). Pixel runs 19.25 +
  19.03 + 19.25 + 19.35 + 20.27 = 97.14 LF; legend **97.3 LF** = estimate 97.3. Average 19.46 ft per
  column = 2'-0" below FFE (top of footing per S-201) + ~17.5 ft to the top of the parapet channel.
- **Worked example (line 40, HSS6x6x3/8):** legend 61.4 (p35) + 175.0 (p36) = **236.4 LF** (236.34). On
  schedule it should be ≈ 172 LF: 8 full-height columns measured on p36 (155.68 LF) + B-4. B-4 is the
  low-roof column; its S-201 schedule bar (drawn to scale, 9 pt/ft) runs from 1'-0" below Level 1 to
  15.19 ft, the t/s 15'-2 1/4" of the grid-B HSS4X4X1/4 beam, so 16.2 ft (17.2 ft if its base is 2'-0"
  down like the others). The p35 runs repeat C-6 and D-6 (40.86 LF), and D-5 (20.21 LF) is HSS6X6X1/4.
  The stray 19.03 ft run on p36, if it is B-4, over-states it by ~1.8–2.8 ft (unproven). See app-gaps.md G1.

## F3. Posts at a stated height (EA → LF)

- **Inputs:** `count` (EA, legend count item), `height` (ft-in, printed in the legend name "@ 1'4"H").
- **Rule:** `LF = count × height_ft`, plus any measured LF of the same shape and role.
- **Convention:** the estimator rounds the height to 2 decimal feet first (1'-7" → 1.58).
- **Worked example (line 36):** 6 × 1.58 = **9.48 LF** (exact 6 × 1.5833 = 9.50, +0.2%).
- **Worked example (line 37):** 5.6 (S-301, two short HSS4x4 posts in elev 8) + 6 × 1.3333 (S-203
  HSS4x4x1/4 POST @ 1'4"H, one per high-roof joist on the grid-B beams, S-603) = 5.6 + 8.0 = **13.6 LF**.

## F4. Bridging and rigid joist bracing with the "*2" multiplier

- **Inputs:** `rigidRows` (LF of the plan line "RIGID JOIST BRACING *2"), `xRows` (LF of plan line
  "X-TYPE BRIDGING *2"), multiplier 2 printed in the legend name.
- **Rule (estimator):** `LF = (Σ rigidRows + Σ xRows) × 2`. The rigid bracing runs at top and bottom
  chord ("continuous horizontal rigid bracing at top and bottom chord", S-203 framing key). The X-bridging
  has 2 diagonals per bay, taken at plan length, with no allowance for the diagonal over the joist depth.
  Both go in one line under the A.X. size L2-1/2x2-1/2x1/4.
- **Worked example (line 65):** (121.9 + 35.5) × 2 = **314.8 LF** (314.8).
- **Geometric alternative (engine):** X LF = ceil(row / s) × 2 × √(s² + d²). With s = 55" (joist spacing
  ~4'-5" to 4'-9"), d = 16": 8 bays × 2 × 4.773 = 76.37 LF instead of 71.0 LF (+5.4 LF on the line, +1.7%).

## F5. Counted angles with a stated length

- **Inputs:** `groups[] = {count, length}`, where the count is the legend dots and the length comes from
  the legend name ("L2x2x3/16 ANGLE @ 4'L").
- **Rule:** `LF = Σ count_i × length_i`.
- **Basis:** S-602 "2" x 2" x 3/16" ANGLE TO JOIST TOP CHORD AT JOIST CLOSEST TO BEAM MIDSPAN", one dot
  per such joist. The drawings give no length; 4'-0" (and one 5'-8") is the estimator's own allowance.
- **Worked example (line 67):** 18 × 4.0 + 1 × 5.6667 = **77.67 LF** (77.67).

## F6. Roof deck area

- **Inputs:** `areas[]` (SF), the deck polygons in plan on S-203, one deck mark (RD-1.5).
- **Rule (estimator):** `SF = Σ areas`: horizontal projection, no end-lap, side-lap or waste allowance.
  Overlapping polygons are not netted.
- **Worked example (line 73):** **2208.4 SF** (2208.37). Pixel rebuild on p34: polygon envelope
  2024.6 SF + darker double-painted strip 193.0 SF along grid B = 2217.6 SF (+0.4%).
- **Correct rule:** `SF = area(∪ polygons)` ≈ 2024.6 SF (−183.8 SF, −8.3%). Lap and waste belong in
  order quantities, not in the net SF. The band is about 3.6–3.8 ft deep with its top edge 3.3 ft north
  of grid B, and the low-roof joist lines (lines 70, 72) start from that top edge: one snapped line caused
  both errors.

## F7. Base plates from the schedule

- **Inputs:** BASE PLATE SCHEDULE on S-201: `mark, width, length, thickness, COUNT`.
- **Rule:** `EA = schedule COUNT`. Cross-check against `Σ count(plan tags)` and the column count (18).
- **Worked example (lines 75–77):** BP12 **10**, BP14 **4**, BP1518 **4** (sum 18 = 18 columns). The p33
  legend counted BP12 9; the estimator took the schedule.

## F8. Cap plates from column schedule × cap-plate table

- **Inputs:** column count by size class (S-201 column schedule); cap-plate table (S-681 detail 8: column
  size → plate, 9 rows: W8 3/4x14x8-1/2, W10 3/4x16x10-1/2, HSS4X4 3/4x10x4-1/2, HSS5X5 3/4x11x5-1/2,
  HSS6.00 ROUND 3/4x13x7-1/2, HSS6X6 3/4x12x6-1/2, HSS8X8 3/4x14x8-1/2, HSS12X4 3/4x12-1/2x9,
  HSS12.75 ROUND 3/4x14x19); `capPlateFallback` for sizes not in the table.
- **Rule:** `EA(plate p) = Σ count(columns whose size maps to p)`.
- **Convention:** the table has no HSS7X7 row. The estimator gave the 5 HSS7X7 columns the HSS6X6 plate
  (12"x6-1/2"x3/4"), i.e. fallback = next smaller listed square HSS. Applied literally, the table maps
  only 11 columns to this plate and leaves the 5 HSS7X7 unmapped. A width-based alternative would be
  3/4"x13"x7-1/2", but that row belongs to HSS6.00 ROUND, not to any square tube. The fixture carries the
  table and the fallback as explicit inputs.
- **Worked example (line 78):** HSS5X5: A-2.9, C-7 → **2 EA** 11"x5-1/2"x3/4".
- **Worked example (line 79):** HSS6X6 (9 × 3/8 + 1 × 1/2 + 1 × 1/4 = 11) + HSS7X7 (5) = **16 EA** 12"x6-1/2"x3/4".

## F9. Plates per post

- **Inputs:** `posts` (EA), `platesPerPost` (from detail).
- **Rule:** `EA = posts × platesPerPost`.
- **Worked example (line 74):** A-200 6 tube posts × 1 (A-430: "1/4" x 5" x 5" STEEL PLATE") = **6 EA**.

## F10. Counted misc metals

- **Rule:** `EA = legend count`; the description comes from the referenced detail.
- **Worked example (line 80):** A-110 legend 1 EA; A-450 det 3 → 1'9"W × 13'4"H aluminum ladder w/ 1-1/4"
  serrated rungs, 3/16" aluminum wall bracket, safety post = **1 EA**.

## Conventions observed on this job (estimator's own)

| Convention | Value | Basis on this job |
|---|---|---|
| Height rounding before multiply | ft to 2 decimals (fixture input `heightRoundingFt: 0.01`) | 1'-7" → 1.58 (line 36) |
| "*N" in a legend name | multiply LF by N | lines 65 (×2) |
| Column length | base plate to top of parapet channel | p36 pixel runs, 19.46 ft average (HSS7x7) |
| X-bridging length | plan length × 2 (no depth) | line 65 |
| Kicker angle length | 4'-0" (one 5'-8") | line 67; not dimensioned |
| Cap plate for unlisted column size | next listed smaller square HSS (HSS6X6 plate on HSS7X7; fixture input `capPlateFallback`) | line 79 |
| Plate counts | schedule COUNT over markup count | line 75 (10 vs 9) |
| Deck | sum of polygons, overlaps not netted, no lap or waste | line 73 |
| Joists | plan length of each joist line; the low-roof lines start 3.3 ft north of grid B (confirmed error, not a convention to copy) | lines 70, 72 |
