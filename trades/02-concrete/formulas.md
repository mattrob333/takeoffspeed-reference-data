# Concrete formulas (02-concrete)

## Conventions

- All lengths are in feet. Convert a printed ft-in string exactly: 3'-8" = 3 + 8/12 = 3.6667 ft.
- **Estimator's convention (observed, not recommended):** this estimator converts every ft-in dimension
  to decimal feet *rounded to 2 places* before multiplying:
  - 3'-8" → 3.67, 1'-2" → 1.17, 1'-4" → 1.33, 8" → 0.67, 10" → 0.83.

  This is the only way lines 21–28 match to the sixth decimal. Measured as exact rebuild against estimate:
  - The ft-in rounding alone moves lines 21–26 by −0.29% to +0.25%. On the stem lines it is −0.50% on line 27
    (0.67 for 8") and +0.40% on line 28 (0.83 for 10").
  - The stem LF rounded up to 0.5 FT adds a further −0.10% (line 27, 193.8 against 194.0) and −1.18% (line 28, 8.4 against 8.5).
  - Combined, that is −0.60% and −0.78%.

  The app should use exact fractions and accept a 1% tolerance against this estimator.
- CY = CF ÷ 27. No waste is carried on any line, so every estimate quantity is net.
- PlanSwift legends print one decimal. The estimate carries PlanSwift's full value: 39.22, 364.11 and
  124.15 against legend values of 39.2, 364.1 and 124.2.

---

## F1 Slab on grade area — line 16 (measured)

- **Inputs:** `areas[]` (SF), each slab polygon of one slab mark (SOG-4) traced inside the stem walls.
- **Rule:** `slab_sf = Σ areas`. There is no deduction for column blockouts or for the isolation diamonds.
- **Derived (not carried as separate lines by this estimator):**
  - concrete CY = SF × T ÷ 27
  - stone CY = SF × base T ÷ 27
  - vapor retarder SF ≈ SF, plus laps and turn-ups
  - WWF SF = SF
- **Worked example:** the teal area is 1917.6 SF, so line 16 = **1917.6 SF** (Δ 0.00%). The implied concrete is
  1917.6 × 4/12 ÷ 27 = 23.674 CY. The implied #57 stone is the same, 23.674 CY. Neither is carried in the estimate.

## F2 Joint length — lines 17, 18 (measured)

- **Inputs:** `runs[]` (LF), traced on the foundation plan; `type`; `width` or `depth` from the detail.
- **Rule:** `joint_lf = Σ runs`.
  - Saw-cut depth label = slab T ÷ 4 (3/S-680, 1/4 "T"), so a 4" slab gives "1" SAW-CUT JOINT".
  - Isolation joint = the sides of each column-blockout diamond (8/S-680) that lie inside the slab.
- **Worked example:**
  - Saw-cut: 364.1 LF, so line 18 = **364.1** against 364.11 (Δ −0.003%).
  - Isolation: 39.2 LF, so line 17 = **39.2** against 39.22 (Δ −0.05%).
- **Cross-check (saw-cut):** S-201 limits spacing to ≤ 12'-6". The drawn grid is 5 E-W and 4 N-S lines over a slab about 45' across.
  A pixel trace of the 9 yellow runs gives 352 LF, −3.3%, because the count dots hide parts of the lines.

## F3 Continuous footing concrete — line 19 (derived)

- **Inputs:**
  - `lf` (LF): the WF20 run, traced **between** spread-footing outlines, so it is already net of overlap.
  - `width` and `depth` (ft): from the WALL FOOTING SCHEDULE.
- **Rule:** `cy = lf × W × D ÷ 27`.
- **Worked example:**
  - From the legend: 124.2 × 2 × 1 ÷ 27 = **9.2000 CY**, against 9.196296 (Δ +0.04%).
  - With the estimator's LF: 124.15 × 2 × 1 ÷ 27 = 9.196296, an exact match.

## F4 Isolated (spread) footing concrete — lines 20–26 (counted × schedule)

- **Inputs:**
  - `count` (EA): footing-mark dots on p33. These equal the schedule COUNT column and the plan tags.
  - `L`, `W`, `D` (ft): from the SPREAD FOOTING SCHEDULE.
- **Rule:** `cy = count × L × W × D ÷ 27`.
- **Worked examples:**

  | Line | Mark | Exact | CY | Estimator (2-dec ft) | Est. qty | Δ exact |
  |---|---|---|---:|---|---:|---:|
  | 20 | F30 | 3 × 3 × 3 × 1 = 27 CF | 1.0000 | same | 1.0 | 0.00% |
  | 21 | F38 | 3 × 3.6667² × 1 = 40.333 CF | 1.4938 | 3 × 3.67² × 1 = 40.407 | 1.496544 | −0.18% |
  | 22 | F50 | 6 × 5 × 5 × 1.1667 = 175.0 CF | 6.4815 | 6 × 25 × 1.17 = 175.5 | 6.5 | −0.28% |
  | 23 | F60 | 1 × 6 × 6 × 1.3333 = 48.0 CF | 1.7778 | 36 × 1.33 = 47.88 | 1.773333 | +0.25% |
  | 24 | F70 | 1 × 7 × 7 × 1.3333 = 65.333 CF | 2.4198 | 49 × 1.33 = 65.17 | 2.413704 | +0.25% |
  | 25 | F7040 | 1 × 7 × 4 × 1.3333 = 37.333 CF | 1.3827 | 28 × 1.33 = 37.24 | 1.379259 | +0.25% |
  | 26 | F10050 | 1 × 10 × 5 × 1.1667 = 58.333 CF | 2.1605 | 50 × 1.17 = 58.5 | 2.166667 | −0.29% |

## F5 Stem wall concrete — lines 27, 28 (derived)

- **Inputs:**
  - `lf` (LF): the wall traced continuously around the perimeter, through the spread footings.
  - `height` (ft): top of footing [-2'-0"] to finish floor, so 2'-0". The legend name also says "@ 2'H".
  - `thickness` (ft): from the S-600 section.
- **Rule:** `cy = lf × H × T ÷ 27`.
- **Worked examples:**
  - Line 27, 8": 193.8 × 2 × 0.6667 ÷ 27 = **9.5704 CY**, against 9.628148 (Δ −0.60%).
    The estimator's 194.0 × 2 × 0.67 ÷ 27 = 9.628148 matches exactly.
  - Line 28, 10": 8.4 × 2 × 0.8333 ÷ 27 = **0.5185 CY**, against 0.522593 (Δ −0.78%).
    The estimator's 8.5 × 2 × 0.83 ÷ 27 = 0.522593 matches exactly.
    The drawn thickness is 10 3/4". It is printed on the S-201 plan at the 6/S-600 "At Wing Wall" callout, and in 6/S-600.
    Read literally that is 8.4 × 2 × 10.75/12 ÷ 27 = 0.557407 CY (+6.66%), so the estimate's 10" is a simplification.
- **Estimator LF:** the estimator's LF (194.0 and 8.5) is the legend value (193.8 and 8.4) rounded *up* to the next 0.5 FT.
  This is the only non-PlanSwift input in the trade.

## F6 Pad concrete — line 29 (specified)

- **Inputs:** `count` (EA); `L × W × T` from the plumbing note: 18" × 18" × 6".
- **Rule:** `cy = count × L × W × T ÷ 27`.
- **Worked example:** 1 × 1.5 × 1.5 × 0.5 ÷ 27 = **0.041667 CY**, an exact match.
  - The count dot sits on note 3, not on a symbol. Line 29 is the one pad on the plumbing scope (P-301 shows the
    intercepting-trap cleanout under the external wall, and refers the exterior cleanout locations to civil).
  - The six C-5.0 cleanout pads are carried in Div 32 line 658 (18"x18"x8", 6 EA, 13.5 SF = 6 × 1.5 × 1.5). Do not
    add the civil cleanouts here, or they are counted twice.

## F7 Formwork, rolled up — line 30 (derived)

- **Inputs:** every foundation element above, and the number of formed faces. This estimator forms everything:
  - footings: 2 sides (continuous) and 4 sides (spread)
  - stem walls: 2 faces
  - pad: 4 edges
  - slab edge: not formed, because it is cast on and against the stem wall
- **Rule:** `sf = Σ contact_sf`, reported by this estimator as 1420. The rounding `ceil10(...)` is a **hypothesis**
  fitted from this one line (see below). The contact-area terms are:
  - continuous footing = LF × D × 2
  - spread footings = Σ count × 2(L + W) × D
  - stem walls = Σ LF × H × 2
  - pad = count × 2(L + W) × T
- **Worked example:**

  | Component | Calculation | SF |
  |---|---|---:|
  | WF20 | 124.2 × 1 × 2 | 248.40 |
  | Spread | F30 36 + F38 44 + F50 140 + F60 32 + F70 37.33 + F7040 29.33 + F10050 35 | 353.67 |
  | Stem walls | (193.8 + 8.4) × 2 × 2 | 808.80 |
  | Pad | 4 × 1.5 × 0.5 | 3.00 |
  | **Σ** | | **1413.87** |

  Rounding the sum up to the next 10 SF gives **1420 SF**, Δ 0.00%. Before rounding it is −0.43%.
  With the estimator's own inputs (124.15 LF, 2-decimal feet, 194.0 + 8.5 LF) the sum is 1415.26 SF, which also gives 1420.
- **Why the rounding is a hypothesis:**
  - It rests on a single observation. Any raw sum in (1410, 1420] gives 1420 under ceil10.
  - With the estimator's own inputs (1415.26), round-to-nearest-10 also gives 1420. With the legend inputs (1413.87) it would give 1410.
  - So the reproducible quantity is the raw contact area: 1413.87 SF from the legend, 1415.26 SF with the estimator's inputs.
  - The real test is the 1% fixture tolerance, which the raw 1413.87 passes (−0.43%).
- **Basis:** this is a fully formed contact area. GPT-6 Astra checked the result independently and reached the same
  combination: slab edge excluded and no end forms. It also confirmed that the round-up is not uniquely identified (2026-10-13).
- **Alternatives that do not match:**
  - Adding slab-edge forms (202.2 × 4/12 = 67.4 SF) gives 1481.
  - Earth-forming the footings (−602 SF) gives about 812.

## Ratios this job yields (estimator's convention, for reference)

- Formwork SF per CY of foundation concrete: 1420 ÷ 36.118 CY (lines 19–29) = 39.3 SF/CY.
  This is a job statistic only. Compute contact area instead.
- Stem LF − WF20 LF = 193.8 − 124.2 = 69.6 LF. That length is the wall over spread footings at the perimeter, where the
  continuous footing is not measured.
