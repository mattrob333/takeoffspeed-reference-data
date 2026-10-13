# 04 — Structural steel, joists, deck, misc. metals

Job: single-storey bank branch, Fifth Third Bank, Watson Blvd., Warner Robins GA (Praxis3 project 26302;
structural engineer Mark Nannis). Steel frame of HSS columns with HSS and W-shape roof beams, K-series
(KCS) roof joists, 1-1/2" wide-rib roof deck, braced frames, parapet and canopy channels, and a roof
access ladder. The building has a high roof (16'-0") over grids A–B and a low roof (13'-0") over B–D/E.

## Scope (45 estimate lines, 36–80)

| Lines | Item | Unit | Class |
|---|---|---|---|
| 36 | HSS1-1/2x1-1/2x3/16 tube column (canopy sign posts) | LF | derived (6 EA x 1'-7") |
| 37 | HSS4x4x1/4 column | LF | derived (elevation LF + 6 posts x 1'-4") |
| 38–41 | HSS5x5x3/8, HSS6x6x1/2, HSS6x6x3/8, HSS7x7x1/2 columns | LF | measured (frame elevations) |
| 42–59 | HSS and W-shape beams (18 lines; HSS6x4x3/8 appears twice) | LF | measured (roof framing plan) |
| 60–62 | C5x6.7, C7x9.8, C8x11.5 channels | LF | measured |
| 63–64 | HSS4x4x1/4 and HSS6x6x1/4 diagonal bracing | LF | measured |
| 65 | L2-1/2x2-1/2x1/4 X-type bridging (incl. rigid joist bracing) | LF | derived (legend "*2" multiplier) |
| 66 | L3x3x1/4 horizontal bracing (H.B.) | LF | measured |
| 67 | L2x2x3/16 angle (kickers at joists closest to beam midspan) | LF | derived (counts x the estimator's lengths) |
| 68–69 | L3x3x3/16 deck-edge angle, L4x3x1/4 LLV closure angle | LF | measured |
| 70–72 | 12KCS2, 16KCS3, 18KCS2 roof joists | LF | measured |
| 73 | 1-1/2" wide rib type B 22 ga G90 roof deck | SF | measured |
| 74 | 5"x5"x1/4" steel base plate | EA | derived (one per tube post) |
| 75–77 | BP12, BP14, BP1518 base plates | EA | specified (base plate schedule COUNT) |
| 78–79 | 11"x5-1/2" and 12"x6-1/2" x 3/4" cap plates | EA | derived (column schedule x cap-plate table) |
| 80 | 1'9"W x 13'4"H aluminum roof access ladder | EA | counted |

**Result: 45 of 45 lines reconcile within 1%, and all 45 within 5%.** Largest deviation is +0.37% (line 62).
It comes from the legend's 1-decimal display against the estimator's 2-decimal values. Class mix: 34
measured, 7 derived, 3 specified, 1 counted. No line is a pure allowance. Two derived inputs are still
the estimator's own judgment: the 4' and 5'-8" kicker-angle lengths (line 67) and the HSS6X6 cap plate
used on the HSS7X7 columns (line 79). See `reconciliation.csv`.

Reconciling to the markup is not the same as matching the drawings. Of the 45 lines, 41 match the drawings
as far as checked. Four are confirmed to differ: line 40 HSS6x6x3/8 column (236.34 vs ≈ 172 LF on schedule),
line 70 12KCS2 (53.96 vs 44.88 LF grid to grid), line 72 18KCS2 (108.49 vs 95.96 LF) and line 73 deck
(2208.37 vs ≈ 2025 SF). Line 61 C7x9.8 has an unproven ≈ 30 LF (7%) overlap risk. Lines 70, 72 and 73 share
one cause: a line snapped 3.3 ft north of grid B on p34.

Not carried in this estimate, though the drawings define them: anchor rods (S-201 ANCHOR BOLT SCHEDULE: 56
of 3/4" and 24 of 1", which equals 10x4 + 4x4 and 4x6), steel tonnage, connection material, grout under
base plates, the BP16 detail, deck accessories and closures, the 2-1/2"x2-1/2"x3/16" parapet-channel
midspan supports (S-603), the 6"x6" metal stud canopy framing (09a), and bollards (32a/32b).

## Driving sheets

| Sheet | Markup page | Use |
|---|---|---|
| **S-203** Structural Plan – Roof | **p34** (33-row legend; HSS6x4x3/8 BEAM appears twice, 22.2 and 9.0 FT, both in legends.json), **p35** (4-row legend) | Every beam, joist, angle, H.B., rigid bracing, X-bridging, C5x6.7 and C7x9.8 on the plan. Also the deck area, kicker-angle dots and the HSS4x4 post dots. p35 is a second markup copy of S-203 whose legend covers only frame elevations 2 and 3 (columns and channels). The sheet also carries the SLAB AND DECK SCHEDULE (RD-1.5), FRAMING KEY and Roof Framing Plan Notes. |
| **S-301** Elevations – Steel Frames | **p36** (10-row legend) | Column LF (each column marked once, base plate to top of parapet channel), diagonal braces, parapet C7x9.8/C8x11.5 and the W10x12 strut in elev 9. |
| **S-201** Structural Plan – Foundation | p33 | STEEL COLUMN SCHEDULE (18 columns by grid), BASE PLATE SCHEDULE (BP12 10, BP14 4, BP1518 4, with COUNT column) and ANCHOR BOLT SCHEDULE. Legend counts BP12 9, BP14 4, BP1518 4. |
| **S-681** Typical Details (Steel) | — | Detail 8 cap-plate table, 9 rows: W8 → 3/4"x14"x8-1/2", W10 → 3/4"x16"x10-1/2", HSS4X4 → 3/4"x10"x4-1/2", HSS5X5 → 3/4"x11"x5-1/2", HSS6.00 ROUND → 3/4"x13"x7-1/2", HSS6X6 → 3/4"x12"x6-1/2", HSS8X8 → 3/4"x14"x8-1/2", HSS12X4 → 3/4"x12-1/2"x9", HSS12.75 ROUND → 3/4"x14"x19" (no HSS7X7 row). Details 3 and 10: C5x6.7 frames at RTUs and openings. Detail 9: splice. |
| **S-682** Typical Details (Steel) | — | Detail 1: L3X3X1/4 (H.B.) and L2-1/2X2-1/2X1/4 (A.X.). Detail 4: bar joist roof construction, rod or angle bottom-chord extensions at the joist closest to beam midspan. |
| **S-602 / S-603** Wall Sections | p39 / p40 (no legend) | S-602: "2" x 2" x 3/16" ANGLE TO JOIST TOP CHORD AT JOIST CLOSEST TO BEAM MIDSPAN". S-603: "HSS 4" x 4" x 1/4" POST AT EACH HIGH ROOF JOIST". |
| S-683 Enlarged Steel Details | — | L3X3X3/16 continuous at deck edge, L4X3X1/4 (LLV) at joist bearing and C7X9.8 parapet channel. |
| S-001 General Notes | — | Structural steel notes: base plates and (4) 3/4" anchor bolts where not shown, plus 5/8"x12"x7-1/2" bearing plates. |
| **A-200** Exterior Elevations | **p11** | "HSS1-1/2"x1-1/2"x3/16" TUBE POST @ 1'7"H" 6 EA. |
| A-430 Section Details | — | Canopy-mounted signage support: 1-1/2"x1-1/2"x3/16" HSS tubes on a 1/4"x5"x5" steel plate. |
| **A-110** Floor Plan | **p3** | "1'9"W ROOF ACCESS LADDER - 1/A312" 1 EA; keynote P2. |
| **A-450** Roof Details | p20 (no legend) | Detail 3 ROOF HATCH & LADDER: O'Keefe's 500 aluminum fixed ladder, 13'-4" overall (verify), 1-1/4" serrated rungs, 3/16" aluminum wall bracket, safety post, 12'-8" F.F. to top of deck. |

## Specification sections (source/specifications.pdf)

| Section | Pages | What it fixes for quantities |
|---|---|---|
| 05 1200 Structural Steel Framing | 84–95 | W shapes and channels A992 Gr 50; HSS A500 Gr B Fy 46 ksi; other steel A36 (p85, p89). Anchor rods F1554 Gr 36 and A325 bolts (p89). "AX" = additional X bridging, L2-1/2x2-1/2x1/4 (p89). H.B. = L3x3x1/4 from top chord to column (p89). L2-1/2x2-1/2x1/4 where joists change direction (p89). Min 4x3x1/4 continuous closure angle at perimeters and high/low roofs (2.1.K, p90). |
| 05 2100 Steel Joist Framing | 96–99 | SJI K-series; bridging per SJI. Where horizontal bridging is used, a vertical X brace in the first panel and every 6th panel (p98). Roof joists welded 1/8"x2" each side (p98). Bottom-chord extensions where shown (p99). **"AX" = 2"x2"x1/4" angles (p99, item O)**, which conflicts with 05 1200. Shop primer 0.50 mil (p99). |
| 05 3000 Steel Roof Decking | 100–103 | **Spec says 20 gauge** A1008/A653, 33 ksi (p101), but the S-203 deck schedule says 22 ga (t = 0.0295") G90, 50 ksi, and the estimator followed the drawing. End laps not less than 2-1/2" (p101; the schedule says 4" min). 2" min bearing; 5/8" puddle welds 6" o.c. at supports (p102). |
| 05 5000 Metal Fabrications | 113–121 | Ladders delegated design (p114). Spec ladders are **steel**, 3/4" rungs, galvanized (p118), but A-450 shows an aluminum O'Keefe's ladder, and the estimator followed A-450. Also bollards and loose lintels (p118; carried in other trades). |

## Materials and specified properties

| Material | Property (source) |
|---|---|
| HSS columns, beams, braces, posts | ASTM A500 Gr B, Fy 46 ksi (05 1200 p85/p89) |
| W shapes, channels | ASTM A992 Gr 50 (p89) |
| Angles, plates | ASTM A36 (p89); base plates "36 KSI" (S-201 schedule title) |
| Base plates | BP12 12x12x3/4 w/ 3/4" headed anchors, 8" embed; BP14 14x14x1 w/ 3/4"; BP1518 15x18x3/4 w/ 1" (S-201) |
| Cap plates | 3/4" thick by column size (S-681 det 8) |
| Roof joists | 12KCS2, 16KCS3, 18KCS2 (S-203); SJI; shop primed |
| Bridging / bracing | Continuous horizontal rigid bracing at top and bottom chord + X in first panel and every 6th panel (S-203 key); A.X. L2-1/2x2-1/2x1/4 (S-682 det 1; 05 1200), but 2x2x1/4 in S-203 key and 05 2100 O |
| Roof deck RD-1.5 | 1-1/2" wide rib type B, 22 ga (t = 0.0295"), galvanized G90, 50 ksi; 5/8" puddle welds w/ washers, 36/4 pattern, perimeter 12" o.c., #10 TEK side laps 18" o.c., min end lap 4" at supports (S-203/S-201 SLAB AND DECK SCHEDULE) |
| Ladder | Aluminum fixed ladder, O'Keefe's 500 basis of design, 1'-9" wide, 13'-4" overall, 1-1/4" serrated rungs, 3/16" wall bracket, safety post (A-450 det 3) |

## What the estimator measured

- **Columns, LF, in elevation (S-301, S-203 frame elevations):** one vertical run per column, from the
  base plate (below Level 1) to the top of the parapet channel. Each column is meant to be marked once,
  in one elevation. A pixel rebuild of p36 gives HSS7x7x1/2 = 5 runs, 97.14 LF (legend 97.3). It gives
  HSS6x6x3/8 = 8 runs plus one stray run drawn off any elevation, 174.71 LF (legend 175.0). On p35,
  S-203 elevations 2 and 3 add 3 more HSS6x6x3/8 runs (61.07 LF; legend 61.4). Of those, C-6 and D-6
  repeat S-301 elevation 10, and D-5 is HSS6X6X1/4 in the schedule. The stray run probably stands in for
  B-4, the low-roof column, which the to-scale S-201 schedule draws only 16.2 ft long (−1'-0" to t/s
  15'-2 1/4"), so schedule-true is ≈ 172 LF. See app-gaps.md G1.
- **Posts at a height, EA → LF:** HSS4x4x1/4 POST @ 1'4"H (6 EA) and HSS1-1/2 TUBE POST @ 1'7"H (6 EA)
  are count items carrying the height in the name. The estimator multiplies them out (1'7" taken as 1.58 ft).
- **Beams, channels, angles, H.B., joists, LF, in plan (S-203):** plan length of each member. The
  low-roof joist lines (12KCS2, 18KCS2) start 3.3 ft north of grid B, at the top of the deck overlap band,
  although every joist bears on the grid-B beam on S-203. This is a confirmed over-measure: +9.08 and
  +12.53 LF against grid-to-grid spans (lines 70, 72).
- **Bridging "*2":** RIGID JOIST BRACING *2 (121.9 FT) and L2-1/2 X-TYPE BRIDGING *2 (35.5 FT) are plan
  runs. The "*2" means two pieces per run (top + bottom chord; two diagonals), and both go into one L2-1/2 line.
- **Deck, SF, in plan:** two polygons (high roof, low roof). They overlap in a strip about 3.6–3.8 ft deep at
  grid B (top edge 3.3 ft north of the B beam line), which is counted twice (about 170–190 SF).
- **C7x9.8, plan and elevation:** the plan trace (236.7 FT) follows the canopy outlines. S-301 (177.8 FT)
  holds the parapet-top channels plus two lower canopy C7X9.8 runs (elev 7 and 11, 29.6 FT). Only those
  two runs can repeat the plan.
- **Counts:** kicker-angle dots (18 + 1) and the ladder. Plates come from schedules, not from the markup.

## Files

- `formulas.md`: every formula with inputs, rules, conventions and a worked example from this job.
- `reconciliation.csv`: one row per estimate line (45 rows).
- `fixtures.json`: 45 engine test cases.
- `reading-guide.md`: how to read S-201/S-203/S-301/S-68x for this trade, the tags, the cross-checks and the traps.
- `app-gaps.md`: comparison with `lib/quantities/trades/structure/structural-steel.ts`, run through the engine.

Scratch work (pixel-run measurements, engine run, GPT-6 Astra second opinions) is in `trades/04-structural-steel/scripts/`.

## Verification

On 2026-10-13 the reviewer's eight findings were checked against the sources by Claude (Opus 5.5), with
GPT-6 Astra (`tools/ask_gpt.py`) as a second reader on two image crops. All arithmetic was done in Python.
The scripts and crops are in `trades/04-structural-steel/scripts/verify/`; `numbers.py` holds every figure
quoted below.

| # | Finding | Checked how | Verdict | Change |
|---|---|---|---|---|
| 1 | HSS6x4x3/8 22.2 FT row "missing" from legends.json | Dumped legends.json p34: 33 items, item 33 = 22.2 FT brown ("duplicate name restored"), item 6 = 9.0 FT | Reviewer right; the old note was stale | Line-45 note, reading-guide trap 1 (now "duplicate names must not be merged"), README p34 row |
| 2 | Low-roof joist over-length left unconfirmed | S-203 vectors (18 pt/ft): 16KCS3 strokes end 0.75 ft north of the B beam (y 942.1), 18KCS2 and 12KCS2 start 0.66 ft south of it, 90.32 and 40.64 LF as drawn. p34 pixels (8.2675 pt/ft): low-roof lines start at y 429.5, the band top, 3.3 ft north of B, and end at C and D. GPT-6 Astra: "purple low-roof joist markups start at the top edge of the dark band… olive high-roof markups end at the grid-B beam" | Reviewer right (I measure 3.3 ft, not 3.4–3.8) | Lines 70/72 marked as confirmed errors with drawing-true LF (44.88 / 95.96 grid to grid); app-gaps G3, formulas F1/F6 and conventions, reading-guide §5 and trap 9 |
| 3 | B-4 assumed full height; reviewer says it stops at 13'-0" (≈14–15 ft, total ≈170 LF) | S-201 schedule vectors: bars are to scale (9 pt/ft). The B-4 bar runs from y 249.6 to 103.9, i.e. 1'-0" below Level 1 to 15.19 ft, which matches the t/s 15'-2 1/4" of the grid-B HSS4X4X1/4 beam. Other bars run −2'-0" to 17.3–18.5 ft. GPT-6 Astra: top ≈ 15.2 ft, bottom −1 ft, length ≈ 16.2 ft | Partly right. B-4 is short, but it does not stop at 13'-0" | Schedule-true ≈ 172 LF (155.68 + 16.2; 172.9 with a 2'-0" base). The stray run over-states B-4 by ~1.8–2.8 ft, still unproven. Updated line 40, F2, app-gaps G1, trap 4 and README |
| 4 | C7x9.8 exposure overstated (178 → ≈30 LF) | p34 crops along grid A and grid 7: no yellow trace outside the canopies. Canopy bounding-box perimeters sum to 264 ft. p36 pixels: lower C7X9.8 in elev 7 = 15.02 ft, elev 11 = 14.60 ft | Reviewer right: ≈ 29.6 LF (6.9%) | Line-61 note, app-gaps G4, trap 12, README |
| 5 | best-practices §6 lists HSS6x4x3/8 as an exception | Same legends.json dump | Reviewer right | Bullet reworded |
| 6 | Spec citation "3.x K" | spec-p090.txt: K follows 2.1 MATERIAL items G–J and precedes 2.2 CONNECTIONS | Reviewer right | 2.1.K (p90) in README and the line-69 note |
| 7 | S-681 cap-plate table has 9 rows | Rendered S-681 detail 8 | Reviewer right | README S-681 row, F8, reading-guide §2. The 13x7-1/2 plate is attributed to HSS6.00 ROUND |
| 8 | Fixtures hide judgment calls | Recomputed: 6 × 1'-7" = 9.50 (0.21% off 9.48); the literal table gives 11, and 16 only with the fallback | Reviewer right | Line-36 fixture: `heightRoundingFt: 0.01` and tolerance 0.1%, so the exact answer now fails. Lines 78/79: `capPlateTable`, `capPlateFallback`, `plate` inputs and notes |

Reviewer pointers that did not exist: README had no "key finding 3" or "unresolved item 2", and its p34 row
did not mention a missing row. The substance was applied to the README text that does exist.

Not changed: every estimator quantity and every recomputed value. The reconciliation count is still 45 of
45 within 1% of the markup. The new paragraph under **Result** separates markup agreement from drawing
agreement: 4 lines confirmed to differ from the drawings, 1 with an open ≈ 30 LF risk. One open point
surfaced during this check and was not re-derived: the double-painted band measures about 3.6–3.8 ft ×
46.5 ft (≈ 170 SF) at single columns, against the earlier 193 SF pixel rebuild. Line 73 notes and G2 keep
the 193 SF figure, with the range 170–190 SF stated here.
