# 03 — Masonry formulas

All arithmetic was run in Python (`trades/03-masonry/scripts/build.py`, `calc1.py`).
Inputs are read from the markup legends (`reference/markups/legends.json`) and the details
cited. "Estimator convention" means a habit inferred from this job's numbers, not a standard.

## Estimator conventions used by this trade

| Id | Rule | Basis on this job |
|---|---|---|
| C1 `ftDec2` | Feet-inches heights are written as 2-decimal feet: 1'-4" → **1.33**, 2'-8" → 2.67, 8" → 0.67 | Line 31 = 157.5 × 1.33 exactly. The same habit appears in 02-concrete lines 23–25 and 27–28 |
| C2 `lfUp05` | A legend LF that feeds a height multiplication is rounded **up to the next 0.5 FT**: 157.4 → 157.5 | Line 31 = 209.475 is reproduced only by 157.5 × 1.33. 02-concrete line 27 (193.8 → 194.0) and line 28 (8.4 → 8.5) show the same step |
| C3 `sfUp5` | A measured finish area is rounded **up to the next 5 SF**: 395.7 → 400 | Line 32. A 10, 50 or 100 SF step also gives 400 here, so line 32 cannot tell them apart. Neither can 09a line 313 (416.9 → 420 under both ceil5 and ceil10). The lines that do discriminate 5 from 10 are 09a line 260 (252.6 → 255; ceil10 gives 260), 09a line 266 (282.6 → 285; ceil10 290), 07 line 179 (274.4 → 275 SF; ceil10 280) and 07 line 168 (13.9 → 15 LF; ceil10 20). 07 line 160 = ceil5(488.3) + ceil5(395.7) = 490 + 400 = 890 corroborates that 400 is the figure the estimator carries for the brick (it does not discriminate the step either). Per sheet, 163.6 → 165 and 232.1 → 235 also sum to 400 |
| C4 | Special-course LF lines are carried **unrounded** (2 decimals from PlanSwift) | Lines 33 and 34 are 149.33 and 149.86, against legend sums of 149.3 and 149.8 |
| C5 | The barrier behind the veneer = the veneer SF line | Line 35 = line 32 = 400 |

---

## F1 `cmuStemWallSF`: CMU below grade under the veneer (line 31)

- **Inputs:** `runLF` (FT, legend p03 A-110 `4"THK. CMU STEM WALL W/ GROUT CAVITY SOLID @ 1'4"H`); `height` (ft-in, from the legend name, confirmed by 2 courses × 8" on A-430 det. 4 and S-600 sec. 1).
- **Rule (estimator):** `SF = lfUp05(runLF) × ftDec2(height)`
- **Rule (physical):** `SF = runLF × height_exact`. The engine's `masonry.cmu-wall` net SF does this, with no openings deducted. A door or storefront does not interrupt masonry below grade.
- **Where the height comes from:** `CMU H = stem-wall height (TOF −2'-0" to F.F.E.) − brick below F.F.E. (8" = 3 brick courses) = 1'-4"` = 2 CMU courses. It is not dimensioned on any sheet. The estimator typed it into the legend name.
- **Worked example:** `lfUp05(157.4) = 157.5`; `157.5 × 1.33 = 209.475 SF` (estimate 209.475, Δ 0.000%). The physical value is `157.4 × 16/12 = 209.8667 SF` (+0.187%); fixture 2 tests this value at 0.01%, with 209.475 as the comparison value.
- **Derived quantities the estimate does not carry:** 4×8×16 CMU at 1.125 /SF gives 235.7 units. The cell grout and the cavity grout to grade have no quantity line (app-gaps G3).

## F2 `veneerFieldSF`: brick veneer field area (line 32)

- **Inputs:** `areas[]` (SF, one PlanSwift area per elevation sheet, EXT-1). p11 A-200 = 163.6, p12 A-201 = 232.1.
- **Rule:** `SF = sfUp5(Σ areas)`. The areas cover the running-bond band in height, from the base flashing line to the underside of the half rowlock. They exclude the special courses and the bank-equipment (VAT) opening on the east elevation, so no separate opening deduction applies.
- **Overshoot on p12 (the legend sum includes it).** At the north (left) end of the East elevation, the p12 purple area runs **≈ 3.5 ft past the building's NE corner onto blank paper**. The clean A-201 shows no brick, return, wing wall or pier there. That is ≈ 9.2 SF (9.0–9.4 SF depending on the height used, 2.62 ft measured or 2.667 ft from the detail) of the 232.1 SF, about 2.3% of 395.7. The north, south and west bands have no overshoot. A strict-from-drawing takeoff gives `395.7 − 9.2 ≈ 386.5 SF` (−2.3% vs 395.7, **−3.4% vs 400**). The reconciled quantity stays 400, because the estimator's legend includes the overshoot. The area ÷ LF check below does not catch it, because the rowlock lines overshoot by the same length (F3, F4).
- **Worked example:** `163.6 + 232.1 = 395.7`; `ceil(395.7 / 5) × 5 = 400 SF` (estimate 400, Δ 0.000%; raw 395.7 is −1.075%).
- **Cross-check (section height):** half-rowlock LF × field height `149.3 × 32/12 = 398.1 SF` (−0.47% vs 400). The measured average height is `395.7 / 149.3 = 2.650 ft`, against the detail's 2.667 ft: 12 brick courses = 8" below plus 2'-0" above F.F.E.
- **Basis not pinned.** A second derivation of 400 needs no round-up step: rowlock-sill LF × the 2'-8" field height written as 2.67, `149.86 × 2.67 = 400.13`, rounded to a whole SF. The area basis is preferred because (a) the PlanSwift EXT-1 areas exist and are the brick's own measured item; (b) Div 07 line 160 adds 400 to ceil5(488.3) of measured ACM area, i.e. it treats 400 as a rounded measured area; (c) on this trade the estimator carries an LF × height product unrounded (line 31 = 209.475), so an LF basis would show as 400.13, or 400.5 with the line-31 habit (`lfUp05(149.86) × 2.67 = 150 × 2.67`); and (d) the half-rowlock LF, the course directly on the field brick, gives 398.7, not 400. So both the step (5 vs 10 SF) and the basis (area vs LF × 2.67) stay open; the quantity does not.

## F3 `specialCourseLF`: half rowlock (line 33)

- **Inputs:** `runs[]` (FT, legend `3-1/4"THK. x 3-5/8"H HALF ROWLOCK BRICK`). p11 = 61.4, p12 = 87.9.
- **Rule:** `LF = Σ runs` (no rounding, C4).
- **Worked example:** `61.4 + 87.9 = 149.3 LF` (estimate 149.33, −0.020%; the residual is legend display precision).
- **Overshoot:** the p12 line runs ≈ 3.5 LF past the NE corner (F2). Strict from the drawing: `149.3 − 3.5 ≈ 145.8 LF`. The legend sum, and the reconciled quantity, include it.

## F4 `specialCourseLF`: rowlock sill (line 34)

- **Inputs:** `runs[]` (FT, legend `7-5/8"THK. x 3-5/8"H ROWLOCK SILL`). p11 = 61.5, p12 = 88.3.
- **Rule:** `LF = Σ runs`.
- **Worked example:** `61.5 + 88.3 = 149.8 LF` (estimate 149.86, −0.040%).
- **Overshoot:** the p12 green line also runs ≈ 3.5 LF (3.6 measured) past the NE corner (F2). Strict from the drawing: `149.8 − 3.5 ≈ 146.3 LF`.
- **Cross-check:** the sill runs 0.5 LF longer than the half rowlock (149.8 vs 149.3), because the sill overhangs and returns at the band ends. Both run ≈ 8.1 LF (5.1%) shorter than the CMU plan run (157.4). The plan line is drawn on the wall line through corners and continues below the VAT opening and storefront jambs; the elevation courses do not.

## F5 `veneerBarrierSF`: fluid-applied vapor barrier behind the brick (line 35)

- **Inputs:** `veneerSF` (line 32 result).
- **Rule:** `SF = veneerSF` (C5). Physically the barrier covers the sheathing from the base termination bar to the sill (≈ 2'-8"), including behind the rowlocks, but not the 8" of brick below grade. Those two differences roughly cancel (GPT-6 Astra second opinion agrees).
- **Worked example:** `= 400 SF` (estimate 400, Δ 0.000%).
- **Trade boundary:** line 184 in Div 07 carries 2983.5 SF of the same product for the EIFS/ACM walls. Do not include the brick zones in that record as well.

---

## Derived checks (no estimate line; for the engine's companion outputs)

### F6 `brickUnits`
`units = SF × 144 / ((L + j) × (H + j))`. For modular brick with the BIA module (3 courses = 8", 8" length module) that is 6.75 /SF. **400 × 6.75 = 2,700 brick** (395.7 → 2,671). With a literal 2-1/4" + 3/8" joint the rate is 144 / (8 × 2.625) = 6.857 /SF (+1.6%).

### F7 `rowlockUnits`
A rowlock shows the unit's 2-1/4" bed face (plus joint) along the wall: `units/LF = 12 / (H + j)`. Module 8/3" → 4.5 /LF; literal 2.625" → 4.571 /LF.
- Rowlock sill: 149.86 × 4.5 = 674 units.
- Half rowlock: 149.33 × 4.5 = 672 cut pieces. Each 7-5/8" brick yields two 3-1/4" pieces, about 336 brick cut in half; the spec requires a saw cut.

### F8 `veneerTies`
`ties = SF × 144 / (sH × sV)`.
- Drawings (A-200 CJ detail, A-430 det. 4), 32" × 16": 3.556 SF/tie → 400 SF = **112.5 → 113 ties**.
- Spec 04 2113 §3.6.A.5, ≤ 24" × 18" **and** ≥ 1 per 2 SF: the area minimum governs → **200 ties**, plus ties within 12" of openings.
- Spec 04 2113 §3.6.A.2 adds a third rule: "Provide one anchor at each stud in each horizontal joint between sheathing boards" (8" studs at 16" O.C.). It can add anchors along the band, but the sheathing joint layout is not drawn, so no count is given.
- TMS 402 2.67 SF/tie: 150 ties.
The drawing spacing breaks both the spec and TMS limits (reading-guide trap 4).

### F9 `weeps`
`weeps = ceil(run × 12 / 24) + 1` per flashing run, at 24" O.C. (A-430, spec 3.9.C.3). Along the base and sill lines (≈ 149.3 LF each if treated as one run): 76 per line. The real count needs each elevation run separately. The thru-wall flashing LF itself (213.1) belongs to Div 07.
