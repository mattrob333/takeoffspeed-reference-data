# 09a — Metal stud framing and gypsum board at walls

One real job: a single-storey bank branch (Fifth Third, Watson Blvd). This folder
reverse-engineers the estimator's 50 wall-framing and wall-board lines
(estimate lines 242–277 and 308–321) from the PlanSwift markups, drawings and
specifications. **Quantities and material descriptions only.**

| File | Contents |
|---|---|
| `README.md` | this page: scope, sources, materials, what was measured, scorecard |
| `formulas.md` | every formula, its inputs, the estimator's conventions and a worked example |
| `reconciliation.csv` | one row per estimate line: source → values → formula → recomputed → Δ% |
| `fixtures.json` | 50 engine test cases (inputs → expected quantity, class tolerance, `knownResidual` flag) |
| `reading-guide.md` | how to read the plans/specs for this trade, the tags and strings used, traps |
| `app-gaps.md` | TakeoffSpeed quantity engine vs this estimate, ranked by quantity impact |
| `best-practices.md` | researched industry practice (pre-existing) |

## Scope (what the 50 lines are)

| Lines | Group | Unit | Count |
|---|---|---|---|
| 242–247 | 5/8" gypsum board at walls + 5 accessory lines | SF, EA, TUBES, ROLLS, LBS | 6 |
| 248–253 | 5/8" Type X at the tech wall + 5 accessories | | 6 |
| 254–259 | 1/2" glass-mat sheathing at parapets + 5 accessories | | 6 |
| 260–265 | 5/8" moisture board at walls + 5 accessories | | 6 |
| 266–271 | 5/8" cementitious backer board + 5 accessories | | 6 |
| 272–277 | 1/4" cementitious backer board + 5 accessories | | 6 |
| 308–311 | metal studs by size/gauge (SF of framed wall, with stud counts by height in the description) | SF | 4 |
| 312 | booth ceiling framing, 6" 16 GA @ 12" o.c. | LF | 1 |
| 313 | canopy framing, 6" @ 16" o.c. | LF | 1 |
| 314–321 | top and bottom runners by size/gauge | LF | 8 |

Out of scope here: gypsum ceilings/soffits and their framing (lines 278–291, trade
09b), plywood sheathing and backing (05 rough carpentry, lines 81–86), insulation (07).

## Driving sheets and markup pages

| Sheet | Markup page | Used for |
|---|---|---|
| A-120 Dimensional Floor Plan | p4 | all wall runs (15 legend rows: tag @ height, exterior walls, parapet @ 7'2", double-stud wall, low walls) |
| A-130 Reflected Ceiling Plan | p5 | MOTORIZED MECHOSHADE 74 LF (3-5/8" furring at shades) |
| A-140 Roof Plan | p7 | parapets @ 1'7", 2'7", 4'7"; "8/A450 LAP ROOF 2', INCL WALL" (high-low roof step wall) |
| A-410 Enlarged Restrooms | p16 | PT1 WALL PAINT 252.6 SF (→ MR board), WT1/WT2/WT9 wall tile |
| A-700 Transaction Bar | p23 | WT3 TILE 38.4 SF, 1/4" CEMENTITIOUS BACKER BOARD 38.4 SF |
| A-703 Service Counter | p27 | WT1/WT2/WT9 backsplash tile |
| A-704 Tech Wall | p28 | TYPE X GWB 37.2 SF |
| A-705 Employee Lounge | p32 | WT1/WT2/WT9 backsplash tile |
| A-706 Booth | p29 | booth roof framing 76.2 SF (6" 16 GA @ 12" o.c.) |
| S-203 Roof Framing Plan | p34 | 6" METAL STUD CANOPY FRAMING @ 16" O.C 416.9 SF |
| A-620 Interior Partition Schedule | (p1 highlight only) | tag grammar: series / stud depth / height designator; Table A faces |
| A-310, A-311, A-300 wall sections | p14/p15 (highlights only) | exterior 8"/6" studs; typical 8" stud continuous F.F.E. to T.O. low parapet 17'-4"; 1/2" glass-mat at parapets; VAT wall (sec. 1): 6" recess wall F.F.E. to roof framing (~12'-3"), 8" 7'-2" wall on the canopy beam above |
| A-430 det. 8 & 9 / A-450 det. 8 & 10 | — | 3-5/8" furring at mecho-shades (no height given); 3-5/8" studs at the high-low roof step (no height given) |
| S-001 / S-002 | — | cold-formed steel notes; exterior stud size schedule by height band, wind zone and deflection (43–97 mil; see reading-guide trap 11) |

## Specification sections (PDF page numbers of `source/specifications.pdf`)

| Section | Pages | What it fixes for quantities |
|---|---|---|
| 05 40 00 Cold-Formed Metal Framing | 104–112 | exterior studs delegated design; tracks match stud thickness (p106–107); horizontal bridging ≤ 48" (p111) |
| 09 22 16 Non-Structural Metal Framing | 267–272 | studs/runners ASTM C645, gauge and depth "as indicated on Drawings" (p269); slip-type head (p269); **16" o.c. unless indicated** (p270); two jamb studs per door, runner at heads (p271) |
| 09 29 00 Gypsum Board | 273–281 | 5/8" Type X (p274); MR 5/8" Type X core (p275); **Type X on all vertical surfaces unless indicated** (p278); vertical application, screws (p278–279); Level 4 finish exposed, Level 1 concealed (p280) |
| 06 16 00 Sheathing | 128–132 | parapet sheathing = glass-mat ASTM C1177, "Type X, 5/8 inch unless indicated otherwise" (p131) |
| 09 30 00 Tiling | 282– | no backer-board requirement; backer comes from A-620 series B/C and the elevations |

## Material types and their specified properties

| Material (estimate line) | Specified properties | Source |
|---|---|---|
| 3-5/8" 20 GA studs @ 16" o.c. (308) | C645 C-studs, 20 ga = 0.0312" (30 mil) per A-620 gauge table; 16" o.c. default | A-620; 09 22 16 p269–270 |
| 6" 20 GA studs @ 16" (309) | interior 6" partitions (A6A/A6B tags) | A-620, A-120 |
| 6" 16 GA studs @ 16" (310) | Exterior and high-parapet 6" studs, carried at 16 GA = 0.0566" (54 mil). For the 12'-3" VAT recess wall (9.2 LF), S-002 (Zone 4, L/360) calls 600S162-43 (18 GA, 0.0451"); it is -68 at L/600 and -54 in Zone 5 | S-002, A-310, A-430 |
| 8" 16 GA studs @ 16" (311) | Exterior 8" walls and parapets, carried at 16 GA. S-002 (Zone 4, L/360) calls 800S162-43 up to 11'-0", -54 to 16'-6" and -68 to 20'-0". The wall + parapet rows (282.5 LF) are one continuous 17'-4" stud on A-310, so they are 800S162-68 (14 GA), heavier than carried. The separate 7'-2" VAT wall (5.9 LF) is -43. The 2'-7" parapet and 4' wall (51.0 LF) are unresolved. A-200 requires ≥ 16 GA behind ACM | S-002, A-310/311, A-200 |
| 6" 16 GA @ 12" o.c. booth ceiling (312) | "6" 16 GAUGE METAL STUD FRAMING AT 12" O.C." | A-706 det. 11 |
| 6" canopy framing @ 16" (313) | stud joist canopy framing (gauge not stated) | S-203 legend, A-430 |
| Top/bottom runners (314–321) | U-track, unpunched, matching stud thickness | 05 40 00 p106–107; 09 22 16 p269 |
| 5/8" gypsum board at walls (242) | spec requires 5/8" Type X on vertical surfaces (estimate says "5/8" THK. GYPSUM BOARD") | 09 29 00 p274, p278 |
| 5/8" Type X at tech wall (248) | over in-wall plywood, PT-6 | A-704 |
| 1/2" glass-mat sheathing at parapet (254) | drawings call 1/2" glass-mat under the roof membrane; spec default 5/8" Type X "unless indicated" | A-310; 06 16 00 p131 |
| 5/8" moisture board (260) | MR, 5/8" Type X core, ASTM D3273 score 10 | 09 29 00 p275; A-620 note N |
| 5/8" cementitious backer (266) | cement board at tile (A-620 series B/C "5/8" CEMENT BOARD") | A-620 |
| 1/4" cementitious backer (272) | transaction-bar tile substrate | A-700 |

## What the estimator measured

Linear runs (FT) on the floor plan and roof plan, each PlanSwift item named with its
**wall tag and height** (`WALL A3A @ 12'6"H`, `EXT 8" STUD WALL @ 15'9"H NO GWB`,
`PARAPET WALL @ 4'7"H`). Heights are typed into the item name, not scaled. Areas
(SQ FT) were measured on enlarged elevations for every non-standard board (Type X,
tile, restroom paint) and on the A-706 / S-203 plans for framed tops. Nothing is
counted (EA) for this trade; the stud counts in the description are notes derived
from LF.

The estimate expresses studs as **SF of framed wall (Σ LF × height)**, runners as
**LF = Σ run LF** (top = bottom), and every board accessory as a fixed per-SF ratio of
its board line.

## Scorecard

| | Lines |
|---|---|
| Rebuilt from a source within 1% | **46 / 50** |
| Within 5% | **50 / 50** |
| Exact (Δ < 0.005%) | 32 |
| Outside 1% | 315/319 (6" 20 GA runners, −1.07%), 316/320 (6" 16 GA runners, −2.08%) |
| Fixtures passing at their class tolerance | **45 / 50**: 0.01% for exact formulas, 0.5% for LF × H and Σ LF |
| Fixtures flagged `knownResidual` (expected to fail) | 309 (−0.56%), 315/319 (−1.07%), 316/320 (−2.08%) |

By classification: 4 measured areas (248, 260, 266, 272, each rounded up to the next
5 SF); 6 derived from measured LF × height (stud SF 308–311, glass-mat 254, wall board
242); 2 derived from measured areas (312 booth, 313 canopy); 8 runner lines derived
from measured LF; 30 accessory lines derived by the estimator's per-SF ratios. No line
is a direct count or a schedule quantity, and none is a pure allowance. See
`reconciliation.csv`.

Judgment, inference and fitting are kept separate from what was read:
- **Line 310, 9'-0" group (53.1 SF, ~5.9 LF): estimator judgment with no drawing basis.**
  No 9' 6" wall is drawn. A-310 sec. 1 shows the 6" VAT wall at ~12'-3", which is the
  9.2 LF `@ 12'3"H` row already in 310. The group may double count the recess wall.
  Without it, 310 is −16.5%.
- **Line 308, 3'-0" (mecho furring) and 2'-0" (roof step) groups: the row assignments are
  inferred.** They come from the stud-count notes plus the A-430 det. 8/9 and A-450 det. 8
  material callouts, not from a legend height or a drawing dimension.
- **Line 254: per-row ceil is a fitted rounding.** It is the only variant that gives 658,
  and it is seen on no other line. The unrounded sum is −0.39%.
- **Heights in two-decimal feet (4.33, 18.67).** Line 309 has one exact decomposition near
  the legend, and 308/310 are impossible with exact 18'-8" (formulas.md).

The residuals are small and one-sided, and they are **unexplained**. Every stud SF and
runner line is 0.04–2.1% *below* the estimate. Each gauge carries 0.5–1.6 LF of wall that no
legend row shows. That exceeds what display rounding can produce: on 308, +9.39 SF against
at most 3.87 SF, and on 311, +11.10 SF against at most 3.21 SF. No legend-only decomposition
reproduces 308. The only exact decomposition of 309 needs 65.5 LF at 12'-6" against 65.1 on
the legend.

## Unresolved

1. The +0.5…+1.6 LF per gauge in the runners (314–321) and the matching stud SF residuals
   on 308 and 311.
2. Why 309 carries 65.5 LF at 12'-6" (legend 65.1), and why its runner is 84.3 LF and not
   83.8 LF.
3. The 9'-0" 6" group in 310: what the estimator meant by it.
4. The −9.4 SF residual on 242. No exact face/deduction decomposition has been found.
5. The true stud length (and so the S-002 gauge) of the 2'-7" parapet (38.0 LF) and the
   4' exterior 8" wall (13.0 LF).
6. Stud-count notes: no single rule reproduces all 17 height groups. `ceil(LF × 12/16)`
   matches 12 of 17, and `round(LF / 1.33)` matches 13 of 17.

## Verification

A review of this folder raised 7 findings, and this pass checked each one. All numbers were
recomputed in python; scripts are in `trades/09a-wall-framing-drywall/scripts/` (`counts.py`,
`rebuild3.py`, `verify/*.py`). Claude Opus 5.5 did the independent recomputation, rendering
and source reading. GPT-6 Astra (`tools/ask_gpt.py`) gave second opinions in two places:
- On the S-002 band reading and stud continuity (`verify/gpt-s002.txt`), it agreed that the
  8" stud on A-310 runs continuously to 17'-4", which puts it in the 16'-6" to 20'-0" band.
- It checked the divisibility proofs (`verify/gpt-modular.txt`). It confirmed that 308 and
  310 are impossible with exact 18'-8", and 309 with exact 4'-4". It corrected one
  overstatement: 8.5 LF at 18'-8" is forced only near the legend values, since 11.0 is also
  residue-compatible. formulas.md now says so.

The reviewer's earlier GPT-6 Astra answers (the VAT wall at ~12'-3"; 309 = 65.5 × 12.50 +
18.3 × 4.33) were read and agree with this pass.

| # | Finding | Verdict | What changed |
|---|---|---|---|
| 1 | Stud-count statistics used 18 groups, not 17 | **Right.** There are 17 groups (5 + 2 + 3 + 7). `ceil(LF × 0.75)` matches 12/17, and `round(LF/1.33)` matches 13/17 (so does `ceil(LF/1.33)`). | Corrected in formulas.md F1 and reading-guide §4. `counts.py` now computes the denominator. |
| 2 | 310's 9'-0" group attributed to a 6" wall under the VAT parapet | **Right.** Measured A-310 sec. 1 from the vector sheet: 54.03 pt/ft (the SILL check gives 2.665 ft = 2'-8"). The 6" wall top is at 12.20 ft and the 8" wall runs from 10.20 ft to 17.33 ft (7.13 ft). No legend row on p4, p5 or p7 has a 9' height. | Reclassified as estimator judgment with no drawing basis in reconciliation.csv, formulas.md, reading-guide traps 2 and 9, app-gaps gap 6 and change 5, and the README judgment list. A drawing-faithful 310 is −16.5%. |
| 3 | 309 uses two-decimal heights | **Right.** A brute-force search finds 65.5 × 12.5 + 18.3 × 4.33 = 897.989 as the only solution, and none with 13/3. This pass also found that 308 and 310 cannot be reproduced with exact 18'-8" at all. | Heights are now two-decimal feet throughout. The rebuild, fixtures (`height_ft` 4.33, 18.67, 1.58, …) and the formulas.md header and F1 decomposition were updated. The runner +0.5 LF is recorded as surviving the decomposition. |
| 4 | Parapet per-row ceil fitted to one number | **Right.** Only ceil-per-row gives 658 (alternatives: 655–657 and 660), and line 311 uses the same rows unrounded. The booth's ceil(76.2) (312/302) is a whole-area ceil, not per-row ceil inside a sum. | F5 is marked as a fitted single-data-point rule. The fixture tolerance is 0.5%, which covers the unrounded −0.39%. The reconciliation classification is now "fitted rounding". app-gaps change 11 is softened. |
| 5 | Fixture tolerances derived from each line's own residual | **Right.** `tol_for` gave 2.5% to a −2.08% line. | There is now one tolerance per class (0.01% exact, 0.5% LF × H and Σ LF), with `toleranceBasis`, `estimatorDeltaPct` and `knownResidual` on every LF-based fixture. 5 fixtures now fail by design. |
| 6 | 308/311 residuals beyond rounding; "edited after takeoff" unsupported | **Right.** The rounding bounds are 3.87 and 3.21 SF, against residuals of 9.39 and 11.10 SF on two-decimal heights (9.42 and 10.52 SF on exact-fraction heights). The 308 search reproduces 0 exact solutions and 1315 with 18.67, all at 8.5 LF; none of them also satisfies the five `ceil` count notes. The 2'/3' assignments rest on the count notes, and `35 @ 2'` needs > 45.33 LF. | The "edited or hidden" sentence is removed, and the residuals are labelled unexplained. The 2'/3' groups are labelled inferred, and the mecho callout is corrected to A-430 det. 8 & 9. The 242 decomposition search was not re-run and is cited as the reviewer's. |
| 7 | S-002 misquoted, gauge flattening understated | **Partly right.** The band quote was wrong: 6" is 600S162-43 up to 12'-6" in Zone 4 / L/360, not up to 11'-0". The consequence is wrong for most of the rows the reviewer named. The schedule also has Wind Zone 5 and L/600 columns. A-310 shows the 4'-7" and 1'-7" parapet rows are the top of one continuous 17'-4" stud, which is 800S162-68 (heavier than 16 GA), not 43 mil. Only the separate 7'-2" VAT wall (5.9 LF) and the 6" 12'-3" wall (9.2 LF) are 43 mil in Zone 4 / L/360. The 2'-7" parapet and 4' wall (51.0 LF) are unresolved. A-200 sets ≥ 16 GA behind ACM. | Trap 11, the README material table and app-gaps "Gauge by height" were rewritten with every column and the per-row consequences. The reviewer's "193.6 LF at 43 mil" was not adopted. |

The scorecard is unchanged at 46/50 within 1%, 50/50 within 5% and 32 exact. Fixtures pass
45/50 at class tolerance, with the 5 failures flagged `knownResidual`.
