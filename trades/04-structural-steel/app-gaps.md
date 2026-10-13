# App gaps — 04 structural steel vs `lib/quantities/trades/structure/structural-steel.ts`

The engine was run on this job's inputs (net mode) with `trades/04-structural-steel/scripts/engine_run.ts`.
Output is in `engine_out.txt`. Assemblies used: `structural-steel.member`, `.plate`, `.joist`,
`.bridging`, `.deck`, `.misc`.

## What it already does right

- **Member LF by shape + role** (`member`) reproduced all 34 measured LF lines exactly from the legend
  values: columns, beams, channels, braces, angles. With a `location` it also keeps the two HSS6x4x3/8 rows
  (22.2 / 9.0) apart.
- **Count × length** works through the `"1'-4\" x 6"` length syntax: line 37 = 13.6, line 67 = 77.6667
  (estimate 77.67), line 36 = 9.50 (estimate 9.48; the estimator rounded 1'-7" to 1.58 ft, so −0.2%).
- **Horizontal bridging ×2 chords** = 121.9 × 2 = 243.8 LF, the same rule as the estimator's "*2".
- **Deck** SF is the sum of the areas (2208.4), with lap and waste kept out of net.
- **Plates** (base and cap) carry the schedule count and size: lines 74–79 are exact. **Misc** ladder count
  is exact.
- The shape weight table (`steel-shapes.ts`) parses every designation on this job. Tonnage is outside this
  quantity-only audit.

## What it computes differently (with numbers)

| # | Item | Estimator | Engine | Δ | Cause |
|---|---|---:|---:|---:|---|
| D1 | L2-1/2x2-1/2x1/4 bridging (line 65) | 314.8 LF in **one** line | 243.8 (horizontal) + 76.37 (X) = 320.17 LF in **two** lines | +5.37 LF (+1.7%) | X rows go through bays × 2 × √(s² + d²) (s = 55", d = 16"); the estimator takes plan length × 2. The engine also splits the line by type. |
| D2 | HSS1-1/2 tube column (line 36) | 9.48 LF | 9.50 LF | +0.02 (+0.2%) | Exact 1'-7" vs the estimator's 1.58 ft. Keep exact. |
| D3 | Joist EA lines | none | `joist-count` = 1 EA per designation when fed legend totals | — | `spans` must be one per joist; a PlanSwift legend gives only the total LF. |
| D4 | Validation warnings | — | "column longer than 40 ft", "K-series joist spans over 60 ft" | — | Same cause: legend totals fed as single lengths trip per-member checks. |
| D5 | Extra lines | — | tonnage (steel, joists), connection allowance 10%, anchor bolts and grout when given, deck squares | n/a | Not in this estimate. Net-mode scoring should ignore or report them separately. |

## Inputs it lacks

1. **Aggregated legend totals with a count**: `totalLF` + `count` (or `perMember` optional) on `member`
   and `joist`, so legend rows can be used without inventing per-member lengths.
2. **Column schedule as a record**: grid IDs by size, used to de-duplicate column runs across sheets and
   to drive base and cap plate counts.
3. **Cap-plate table lookup** (column size → plate) with a stated fallback for missing sizes (estimator
   used HSS6X6 → 12x6-1/2 for HSS7X7).
4. **Plates per post / per member** (line 74: one 5x5x1/4 plate per tube post).
5. **Legend multiplier** ("*2", "*N") and **dimension-in-name** parsing (`@ 4'L`, `@ 1'4"H`) for count
   items, converting EA to LF.
6. **X-bridging at plan length** as a convention option, with the row inputs in plan LF.
7. **Deck polygon union**, or an overlap input, so that double-painted strips are netted.

## Concrete changes, ranked by quantity impact

| Rank | Change | Impact on this job |
|---|---|---|
| G1 | **De-duplicate column runs by grid ID against the column schedule.** Add `columnSchedule` (size → grid IDs) and require each column run to carry its grid ID. Flag a run whose grid is already measured or whose size disagrees with the schedule. | HSS6x6x3/8: estimate 236.34 LF vs schedule-true ≈ 171.9 LF (−64.5 LF, −27%): 8 full-height runs 155.68 LF + B-4 16.2 ft (S-201 schedule bar −1'-0" to t/s 15'-2 1/4"; 172.9 LF if its base is 2'-0" down). Of the difference, 40.86 LF is C-6 and D-6 repeated (S-203 elevations 2/3 vs S-301 elevation 10) and 20.21 LF is D-5, which should be a new **HSS6x6x1/4 COLUMN** line (missing from the estimate). The remaining 3.40 LF is 2.84 LF of stray-run excess (19.03 ft against B-4's 16.19 ft, if the stray run is B-4, which is unproven) plus 0.56 LF of legend-vs-pixel rounding. A column-height check against the to-scale schedule bars would catch it. |
| G2 | **Net overlapping deck polygons** (union, or a warning when two deck areas of the same mark overlap). | Deck 2208.4 vs union ≈ 2024.6 SF (−183.8 SF, −8.3%); ~193 SF strip along grid B counted twice. GPT-6 Astra second opinion: ~170–185 SF. |
| G3 | **Check joist length against the bearing grid span** (warn when the measured length exceeds the support-to-support span by more than the seat/extension allowance). | **Confirmed.** 12KCS2 53.96 vs 3 × 14.958 = 44.88 LF grid to grid (−9.08, −16.8%) or 40.64 LF as drawn; 18KCS2 108.49 vs 4 × 23.99 = 95.96 LF (−12.53, −11.5%) or 90.32 LF as drawn. S-203 vectors: both high- and low-roof joists bear on the grid-B beam. On p34 the low-roof markup lines start at the top of the double-painted deck band, 3.3 ft north of B: the same snapped line as G2. GPT-6 Astra reads the crop the same way. |
| G4 | **Match plan and elevation runs of the same member** (C7x9.8 236.7 plan + 177.8 elevation + 14.0). Require grid/elevation location on channel runs and warn when a plan run and an elevation run share a grid line at the same top of steel. | ≈ 30 LF (6.9%) at risk on line 61 (428.46 LF). The plan trace (236.7) follows the canopy outlines (their bounding-box perimeters sum to ~264 ft), not the bare parapets on grid A or grid 7, so the parapet-top channels on S-301 are counted once. The two lower C7X9.8 runs in S-301 elevations 7 and 11 (15.0 + 14.6 = 29.6 LF) can repeat the canopy outline where it runs along line C (3–2) and line 2 (B–C). Not provable from the overlay (same yellow fill). |
| G5 | **X-bridging convention** `structural-steel.x-bridging-length = plan×2 | diagonal`, and an option to emit horizontal + X under one line when they share a shape. | ±5.4 LF on line 65 (1.7%). |
| G6 | **Aggregated inputs** (`totalLF`, `count`) for `member` and `joist`, so that legend totals do not produce 1 EA joist counts or false > 40 ft / > 60 ft warnings. | Fixes D3/D4: joist EA becomes 3 / 10 / 4 instead of 1 / 1 / 1. |
| G7 | **Cap and base plates from the column schedule** (count by size via the S-681 table; base plate count from the schedule COUNT, cross-checked to columns = 18). | Lines 75–79 become computed instead of typed; it catches BP12 9 (legend) vs 10 (schedule). |
| G8 | **Legend-name parsing**: `*N` multiplier; `@ L'` / `@ H"` dimensions on EA items → LF. | Lines 36, 37, 65, 67 become reproducible without manual entry (≈ 415 LF in total). |
| G9 | **Anchor rods from the ANCHOR BOLT SCHEDULE** (count column), off by default when the estimate puts them in concrete. | 56 × 3/4" + 24 × 1" EA; not carried in this estimate (scope note only). |
| G10 | **Spec/drawing conflict warnings** for A.X. size (L2-1/2 vs L2x2x1/4), deck gauge (22 vs 20 ga) and ladder material (aluminum vs steel). | Material choice, no quantity change. |

## Engine output (net mode) vs estimate, all 45 lines

All member, joist, deck, plate and misc lines match the estimate within 0.4%. The only line-level
differences are D1 (bridging split, +1.7%) and D2 (+0.2%). Lines G1–G4 above are places where **both**
the estimator and the engine (fed the estimator's measurements) differ from the drawings.
