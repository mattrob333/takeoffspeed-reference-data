# 03 — Masonry and stone/brick veneer

The brick wainscot band and the 4" CMU below it, around the base of the bank building.
This covers **5 estimate lines** (Div 04, lineNo 31–35), listed in
`reference/estimate/trades.json`. It covers quantities and material descriptions only.

**Result:** all 5 lines rebuild from a markup legend, and all 5 land within 1% of the
estimator's quantity once the estimator's two rounding habits are applied. Three of the five
match exactly (31, 32, 35). The two rowlock lines are within 0.04%, because the legend prints one decimal
and the workbook carries two.

| Line | Item (shortened) | Unit | Estimator | Rebuilt | Δ | Class |
|---|---|---|---|---|---|---|
| 31 | 4" fully grouted CMU stem wall, grout cavity solid | SF | 209.475 | 209.475 | 0.000% | derived (measured LF × section height) |
| 32 | 3-5/8" modular brick veneer EXT-1, adj. ties 32"×16" | SF | 400 | 400 | 0.000% | measured (area, rounded up to 5 SF) |
| 33 | 3-1/4" × 3-5/8"H half rowlock brick | LF | 149.33 | 149.3 | −0.020% | measured |
| 34 | 7-5/8" × 3-5/8"H rowlock sill | LF | 149.86 | 149.8 | −0.040% | measured |
| 35 | Fluid-applied vapor barrier (behind the brick) | SF | 400 | 400 | 0.000% | derived (= line 32) |

Without the rounding conventions, the physical rebuild is 209.87 SF for line 31 (+0.19%) and 395.7 SF for lines 32 and 35 (−1.08%). The legend sums include a p12 markup overshoot of ≈ 3.5 ft past the NE corner of the East elevation. Measured strictly from the drawing, lines 32/35 are ≈ 386.5 SF (−3.4% vs 400) and lines 33/34 are ≈ 145.8 / 146.3 LF (−2.4%). The reconciled quantities above keep the legend values, because they are what the estimator measured.

| File | Contents |
|---|---|
| `formulas.md` | Every formula, its inputs, the estimator's conventions and a worked example |
| `reconciliation.csv` | Line → source → formula → recomputed quantity → delta → classification |
| `fixtures.json` | 6 engine test cases: one per line, plus an exact-geometry variant of line 31 (expected = its own formula, 209.8667; the estimator's 209.475 is the comparison value) |
| `reading-guide.md` | Which sheets, legends and details to read, the exact strings, cross-checks and traps |
| `app-gaps.md` | How the TakeoffSpeed masonry module compares, with ranked changes |
| `best-practices.md` | Researched industry practice (written earlier; an errata block at the top points to `formulas.md` where they differ) |

## Scope

The estimate's Div 04 MASONRY has three groups:

| Section path | Lines | What |
|---|---|---|
| CMU | 31 | 4" CMU below grade under the brick, two courses (1'-4"), on the strip footing outboard of the 8" concrete stem wall. The cavity between CMU/brick and the stem wall is grouted solid up to grade. |
| EXTERIOR FINISH | 32 | EXT-1 running-bond field brick, from the top of the CMU (8" below F.F.E.) up to the underside of the half rowlock |
| EXTERIOR FINISH > ROWLOCK | 33, 34 | Two special courses capping the band: a half rowlock recessed 1/2", then a full rowlock sill (overhang min. 1/2") at the 2'-8" sill line |
| EXTERIOR FINISH > VAPOR BARRIER | 35 | Fluid-applied vapor barrier on the sheathing behind the brick band |

The brick is a **wainscot band, not full-height veneer.** It runs from 8" below F.F.E. up to the sill at +2'-8". EIFS-1, ACM and storefront are above it.

**Neighbouring lines in other trades (not covered here):**
- Thru-wall flashing 213.07 LF (line 187), pre-finished aluminium sill (185), aluminium flashing (186), the 2983.5 SF fluid-applied barrier behind EIFS/ACM (184) and the 2" rigid insulation behind the finishes (160) are all in 07-thermal-moisture.
- The 8" concrete stem wall and footing under the CMU are in 02-concrete (lines 27, 28).
- The 8" CMU dumpster-enclosure wall with its grout and mortar (lines 668–670) is in 32b-site-structures.
- Line 8, "remove existing brick stair steps", is demolition.

## Driving sheets

| Sheet | Markup page | Used for |
|---|---|---|
| A-110 Floor Plan | p03 | Legend row `4"THK. CMU STEM WALL W/ GROUT CAVITY SOLID @ 1'4"H` = **157.4 FT**, a mauve line along the exterior wall face wherever the brick band occurs |
| A-200 Exterior Elevations (North, West) | p11 | `EXT-1: 3-5/8"THK. STANDARD MODULAR BRICK VENEE...` **163.6 SQ FT**; `3-1/4"THK. x 3-5/8"H HALF ROWLOCK BRICK` **61.4 FT**; `7-5/8"THK. x 3-5/8"H ROWLOCK SILL` **61.5 FT**; Exterior Finish Schedule row EXT-1; detail CJ "BRICK CONTROL JOINT" (ties 32" O.C. horiz. & 16" O.C. vert.) |
| A-201 Exterior Elevations (East, South) | p12 | EXT-1 **232.1 SQ FT**; half rowlock **87.9 FT**; rowlock sill **88.3 FT** |
| A-310 / A-311 Exterior Wall Sections | p14 / p15 | Wall build-up: `EXT-1 ROWLOCK BRICK SILL`, `EXT-1 HALF ROWLOCK, RECESSED`, `EXT-1 RUNNING BOND BRICK`, `FLUID-APPLIED VAPOR BARRIER`, `CMU FULLY GROUTED BELOW GRADE`, SILL datum **2'-8"** |
| A-430 Section Details, detail 4 "SECTION DETAIL @ MASONRY BASE" | p18 | 2 CMU courses (16" = 1'-4"); 12 courses of field brick (8" below + 2'-0" above F.F.E.); `GROUT CAVITY BELOW GRADE`; `ADJUSTABLE BRICK TIES @ 32" O.C. HORIZ. & 16" O.C. VERT.`; `WEEPS @ 24" O.C.`; `CONTINUOUS MORTAR NET`; termination bar |
| S-600 Wall Sections, Foundation, sections 1 & 2 | p37 | `4" CMU BELOW GRADE. FOR BRICK VINEER`, `GROUT CAVITY SOLID UP TO GRADE`, 8" concrete stem wall on the strip footing. Also `SHELF ANGLE, FOR BRICK VENEER. AND WALL TIES BACK TO METAL STUD SEE ARCH.` at the top of the band, which A-430 det. 4 does not show (reading-guide trap 11) |
| S-001 General Notes, "CONCRETE MASONRY NOTES" | — | Type S mortar (ASTM C270), grout ASTM C476 f'g 2250 psi, f'm 2250 psi, "do not fill cells … except below grade", running bond |
| A-620, Table C "Masonry width schedule" | — | 4" CMU = 3-5/8" actual |

## Specification sections

| Section | Pages | What it fixes for quantities |
|---|---|---|
| 04 2113 Brick Veneer Masonry | spec p67–77 | §2.2.C face brick ASTM C216, Grade SW, Type FBX, Basis of Design **Acme Brick, Slate Gray**, actual size **3-5/8" W × 2-1/4" H × 7-5/8" L** (standard modular). §2.2.B uncored units at sill ends; special shapes at corners and jambs. §2.3 portland cement-lime mortar, coloured cement product, pigments ≤ 10% of cement. §2.5.C slip-in adjustable veneer anchors, BOD **Hohmann & Barnard HB-213-2X**, 3/16" hot-dip galvanized wire. §2.6 flashing: asphalt-coated copper 5 oz, BOD **Mortar Net TotalFlash** with stainless termination bar, drip edge and preformed corners. §2.7 Mortar Net weep vents; cavity drainage mesh 10" high. §2.8 Type N mortar, preblended. §3.6.A.5 anchors **max 18" O.C. vertical, 24" O.C. horizontal, at least 1 per 2 SF**, plus extra anchors within 12" of openings. §3.7 expansion joints ≥ 3/8". §3.9 flashing 6" past ends with 2" end dams; weeps **24" O.C.** |
| 04 7200 Architectural Stone Veneer | spec p78–83 | The body is a cast-stone section ("Comply with ASTM C 1364", p79). Not used on this job: no stone or cast stone line or legend |
| 07 2726 Fluid-Applied Membrane Air Barriers | spec p164– | The fluid-applied barrier product behind the veneer (line 35); also carried for EIFS/ACM in 07 |

There is **no CMU specification section** (04 2200 appears only in the S-002 special-inspection table). The CMU properties come from S-001 notes and the details.

## Material types and specified properties

| Material | Properties (source) |
|---|---|
| EXT-1 face brick | Standard modular, 3-5/8 × 2-1/4 × 7-5/8 actual; Acme Brick, Slate Gray; ASTM C216 SW/FBX; IRA < 30 g/30 in²/min (spec 2.2.C, A-200 finish schedule) |
| Mortar | Coosa, colour Old Lime Putty (finish schedule); Type N portland cement-lime (spec 2.8.C); Type S under S-001 for structural CMU |
| Half rowlock | 3-1/4" deep (cut) × 3-5/8" high, recessed 1/2" (A-430 det. 4) |
| Rowlock sill | 7-5/8" deep × 3-5/8" high, overhang min. 1/2", flashing and weeps under it (A-430 det. 4/5) |
| Veneer ties | Adjustable, 32" O.C. horizontal × 16" O.C. vertical on the drawings. This conflicts with spec 3.6.A.5; see reading-guide trap 4 |
| 4" CMU | 4" nominal (3-5/8" actual), two 8" courses below grade, fully grouted, cavity grouted solid to grade (A-430, S-600, S-001) |
| Fluid-applied vapor barrier | On 1/2" exterior sheathing over 8" metal studs, behind the air space and R-10 rigid insulation (A-310, A-430) |

## What the estimator measured

- **One LF run** on the floor plan for the CMU, with the height typed into the legend name (`@ 1'4"H`). The SF = LF × 1.33.
- **One SF area per elevation sheet** for the field brick. In height, the PlanSwift area covers the running-bond band only. It excludes the two rowlock courses, which are measured as lines along the top of the band. Measured area ÷ rowlock LF = 2.65 ft, against the detail's 2'-8" (2.667 ft) of field brick. In length, the p12 area (and both p12 rowlock lines) run ≈ 3.5 ft past the NE corner of the East elevation onto blank paper, ≈ 9.2 SF. The ratio check cannot see this, because area and lines overshoot together. The north, south and west bands stop at the drawn corners.
- **One LF line per course per sheet** for the half rowlock and the rowlock sill, drawn along the top of the band on every elevation.
- **No measurement** for the vapor barrier. It reuses the brick SF.
- **Nothing counted** for brick units, ties, mortar, weeps, grout or control joints. These are carried in the line descriptions, not as quantities. The thru-wall flashing is measured (101.6 + 111.5 FT) but carried in Div 07 (line 187, 213.07 LF).

Units: SF for CMU, brick and barrier; LF for the special courses. The estimator rounds heights to 2-decimal feet (1'-4" → 1.33), rounds the CMU run up to the next 0.5 FT, and rounds the brick area up to the next 5 SF. These are the same habits seen in 02-concrete (lines 27/28: LF up to 0.5), 09a (lines 260 and 266: 252.6 → 255 and 282.6 → 285, area up to 5 SF) and 07 (line 179: 274.4 → 275 SF).

## Open items

- Line 32's round-up step cannot be pinned from this line. Rounding to 5, 10, 50 or 100 SF all give 400 SF from 395.7. 5 SF is chosen because lines that discriminate 5 from 10 elsewhere on the job all use 5: 09a lines 260 (252.6 → 255) and 266 (282.6 → 285), 07 line 179 (274.4 → 275) and 07 line 168 (13.9 → 15 LF). 07 line 160 = ceil5(488.3) + ceil5(395.7) = 890 corroborates that 400 is what the estimator carries for the brick.
- Line 32's **basis** cannot be pinned either. Rowlock-sill LF × 2.67 ft (the 2'-8" field height) = 149.86 × 2.67 = 400.13, rounded to a whole SF, also gives 400 with no round-up step. The area basis is preferred: the EXT-1 areas exist, line 160 treats 400 as a rounded measured area, the trade carries LF × H products unrounded (line 31), and the half-rowlock LF gives 398.7. See formulas F2.
- **p12 overshoot:** see above. The 395.7 baseline and the engine comparison (app-gaps) inherit it.
- **S-600 shelf angle** versus A-430 det. 4 (no angle): no estimate line carries one. Raise it with the tie conflict.
- The **grout in the cavity below grade** ("GROUT CAVITY SOLID UP TO GRADE", S-600) and the **CMU cell grout** carry no quantity line. They are implied by line 31's description only.
- Tie spacing: drawings say 32" × 16" (3.56 SF/tie, 113 ties per 400 SF). The spec says ≤ 24" × 18" and ≥ 1 per 2 SF (200 ties), and §3.6.A.2 adds one anchor at each stud in each horizontal sheathing joint (not countable; the joint layout is not drawn). The estimate carries no tie count, so the conflict is unresolved in the bid.

## Verification

A reviewer's eight findings on this folder were each re-checked on 2026-10-13, using Python for every number. Claude Opus 5.5 did the checks and the edits. GPT-6 Astra (`tools/ask_gpt.py`) gave an independent second opinion on the p12 overshoot images and on the rounding hypotheses. Scratch files are in `trades/03-masonry/scripts/` (`verify_overshoot.py`, `verify_calc.py`, `gpt-verify1.txt`, `gpt-verify2.txt`, `v-*.png`).

| # | Finding | Checked | Verdict | Change |
|---|---|---|---|---|
| 1 | p12 EXT-1 area and rowlock lines overshoot the NE corner | Rendered p12 and the clean A-201 at the same crop. Pixel scan: purple and red start at x = 205 and green at x = 198; the brick hatch starts at x = 434 (zoom 8). Scale from the drawn 2'-0" field (65 px/ft) gives 3.52 ft; the 1/4" sheet scale gives 3.46 ft. Area 9.0–9.4 SF. GPT-6 Astra: "approximately 3½ feet … no return, wing wall, pier". The other six band ends (p11 ×4, p12 ×2) were cropped against the clean sheets (`ends-montage.png`) and all stop at the drawn brick edge | Right | F2–F4, reading-guide §1.5/§2/trap 12, app-gaps, README, reconciliation notes 32–34. Reconciled quantities unchanged. The reviewer's 10.3 SF upper bound was not reproduced; 9.2 SF is used |
| 2 | Line 313 does not discriminate 5 from 10 SF | ceil5 and ceil10 of 416.9 are both 420. 252.6, 282.6, 274.4 and 13.9 discriminate, and all follow ceil5. Line 160 = 490 + 400 = 890. GPT-6 Astra agrees | Right | C3, README, reconciliation line 32 |
| 3 | Fixture 2's expected value is not its own formula | 157.4 × 16/12 = 209.8667; gap to 209.475 is 0.187% against 0.2% tolerance | Right | Fixture 2 expected = 209.8667 at 0.01%, with 209.475 kept in `source`. All 6 fixtures reproduce at their tolerance |
| 4 | LF × 2.67 alternative basis for 400 | 149.86 × 2.67 = 400.126; 149.33 × 2.67 = 398.71; lfUp05(149.86) × 2.67 = 400.5. GPT-6 Astra: "credible alternative—not proof" | Right | F2, README open items, reconciliation line 32 |
| 5 | best-practices contradicts the reconciliation | Legend rows 61.5 + 88.3 = 149.8 exist; 209.475 ÷ 16/12 = 157.106; ceil(149.33/2) = 75 vs ceil(149.3 × 12/24) + 1 = 76. Spec p79–80: 04 7200 is titled Architectural Stone Veneer, but its body says "Comply with ASTM C 1364" and "Cast stone units" | Right except the 04 7200 wording: "cast stone" describes the section body correctly | Errata block at the top of best-practices; both names reconciled there and in the README spec table; the "labor" phrase removed |
| 6 | S-600 shelf-angle callout not on A-430 | S-600.txt lines 34–36 and 72–74; crop of section 1; no "shelf" in A-430/A-310/A-311 text; Div 05 angle lines 67–69 are joist, deck-edge and roof-closure angles | Right | README driving sheets, reading-guide §1.5 and trap 11 |
| 7 | Spec §3.6.A.2 third anchor rule | spec-p075.txt lines 63–64 | Right | F8, reading-guide trap 4, README open item (no count) |
| 8 | "Four of the five match exactly" | Δ 0.000% on 31, 32, 35 only | Right | README result: three of five |

Reconciliation count after review: 5 of 5 lines rebuilt within 1%. 3 match exactly (31, 32, 35) and 2 are within 0.04% (33, 34). The strict-from-drawing values for lines 32–35 are recorded beside them, not in place of them.
