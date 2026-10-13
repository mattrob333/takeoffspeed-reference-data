# 09a formulas — wall framing and wall board

Every number below was computed with python (`trades/09a-wall-framing-drywall/scripts/rebuild3.py`).
**Heights are carried in two-decimal feet**, the estimator's convention: 12'-6" = 12.50,
4'-4" = 4.33, 18'-8" = 18.67, 1'-7" = 1.58, 2'-7" = 2.58, 4'-7" = 4.58, 7'-2" = 7.17.
Three lines need this, assuming 0.1-ft run lengths (the estimate quantities carry only
3–4 decimals, which supports that assumption):
- 309: near the legend (60–72 LF and 15–23 LF), 897.989 has exactly one 0.1-ft
  decomposition, 65.5 × 12.50 + 18.3 × 4.33. With
  4'-4" = 13/3 there is none: every term is a multiple of 1/60 SF, and 897.989 is not.
- 308 and 310: with 18'-8" = 56/3 there is no 0.1-ft decomposition at all. Every 308 term
  is a multiple of 1/120 SF (2180.195 is not), and every 310 term is a multiple of 1/120 SF
  (322.77 is not). With 18.67, the 18'-8" run must be ≡ 1.0 ft mod 2.5 ft (8.5 or 11.0 near the
  legend), and every solution near the legend rows (each row −1.0…+3.0 LF) uses 8.5 LF,
  on both lines. The legend shows 8.4.
The parapet heights are two-decimal only for consistency, because no line separates 1.58
from 1.5833. On any line the difference is ≤ 0.6 SF. LF values are PlanSwift legend values,
displayed to 0.1 ft.

## F1. Stud framing area (lines 308–311)

- **Inputs:** for each legend row of the stud size/gauge: run length `LF` (ft) and the
  framing height `H` (ft) typed in the row name; stud spacing `s` (in) is 16 for every line.
- **Rule:** `stud_SF = Σ (LF_row × H_row)`, in SF of framed wall. Spacing is **not** in the
  SF; it is applied when the SF is converted to sticks (`studs ≈ SF × 12/s / H`).
- **Description note:** `NO. OF STUDS @ H = ceil(Σ LF at H × 12 / 16)` reproduces 12 of the
  17 height groups (5 + 2 + 3 + 7). `round(LF / 1.33)` reproduces 13 of 17, and so does
  `ceil(LF / 1.33)`. Every miss is ±1 stud, so the count is an informational note, not the
  carried quantity. No single rule matches all 17 on the legend LF.
- **Row → line assignment (this job):**

| Line | Rows (LF × H) | Σ LF | SF rebuilt | Estimate | Δ |
|---|---|---|---|---|---|
| 308 3-5/8" 20 GA | A3B 34.2 + A3A 49.9 + D3C 3.7 + D3A 46.0 = 133.8 × 12.50; A3A 7.7 × 3.75; 3-5/8" half of double wall 8.4 × 18.67; mecho-shade furring 74.0 × 3 (p5, *inferred*); roof step wall 45.3 × 2 (p7, *inferred*) | 269.2 | 2170.803 | 2180.195 | −0.43% |
| 309 6" 20 GA | A6B 28.4 + A6A 36.7 = 65.1 × 12.50; 6" low wall 18.3 × 4.33 | 83.4 | 892.989 | 897.989 | −0.56% |
| 310 6" 16 GA | 9'-0" group 5.9 × 9 (*estimator judgment, no drawing basis*); EXT 6" 9.2 × 12.25; 6" half of double wall 8.4 × 18.67 | 23.5 | 322.628 | 322.770 | −0.04% |
| 311 8" 16 GA | parapets 46.0 × 1.58, 38.0 × 2.58, 96.6 × 4.58 (p7), 5.9 × 7.17 (p4); EXT 8" 13.0 × 4, 89.7 × 12.75, (41.5 + 8.7) × 15.75 | 339.4 | 2641.776 | 2652.875 | −0.42% |

- **Exact decomposition of 309:** 65.5 × 12.50 + 18.3 × 4.33 = 818.75 + 79.239 = 897.989.
  It is the only solution over 60–72 LF and 15–23 LF at 0.1-ft steps. The estimator carried
  65.5 LF at 12'-6" where the legend shows 65.1. The extra 0.4 LF × 12.5 = 5.000 SF is exactly
  the gap. `ceil(65.5 × 0.75) = 50` matches the stud-count note, and 65.1 (49) does not. The
  runner is still unexplained: 65.5 + 18.3 = 83.8 LF vs 84.3 LF carried (+0.5 LF).
- **The 308 and 311 residuals are unexplained.** 308 is +9.39 SF and 311 is +11.10 SF. The
  largest possible display-rounding effect is ±0.05 LF per row × Σ heights = 3.87 SF for 308
  and 3.21 SF for 311, so rounding cannot explain them. No legend-only decomposition
  reproduces 308 (see the heights note above). With 18.67, all 1315 solutions within
  −1.0…+3.0 LF per row put 8.5 LF at 18'-8" and add 1–3 LF to the mecho and roof-step rows.
  None of them also matches all five stud-count notes under `ceil(LF × 0.75)`.
- **308's 2'-0" and 3'-0" row assignments are inferred, not read.**
  - The `MOTORIZED MECHOSHADE` row (p5) carries no height. A-430 det. 8 and 9
    ("3 5/8" MTL STUD FURRING AT MECHO-SHADE LOCATIONS") give no dimension. The 3' height
    comes from the stud-count note: `ceil(74.0 × 0.75) = 56` ✓.
  - The roof-step row `8/A450 LAP ROOF 2', INCL WALL` (p7) matches the A-450 det. 8
    callout "3 5/8" MTL. STUDS". Det. 8 gives no height, and the 2' in the row name may be
    the membrane lap. The note "35 @ 2'" needs more than 45.33 LF; the row is 45.3 LF,
    which gives 34.
- **Conventions:**
  - One legend row can feed two stud lines. The 18'8" double wall
    (`6" & 3-5/8" METAL STUD @ 18'8"H`) feeds 308 and 310 with the same 8.4 LF; the
    drawings support this.
  - Line 310 also carries a **9'-0" group that no drawing shows**. Its residual,
    322.77 − 112.7 − 156.828 = 53.24 SF, is 5.92 LF × 9 ft. The rebuild borrows the 5.9 LF of
    `PARAPET WALL @ 7'2"H A310` for it as an assumption. A-310 section 1 contradicts a 9'
    wall. The 6" VAT wall runs from F.F.E. to the roof framing, ~12.2 ft by scale. That wall
    is the `EXT 6" STUD WALL @ 12'3"H` row (9.2 LF, wrapping the recess on three sides on
    p4), which is already in 310. The 8" 7'-2" wall sits outboard on the canopy beam, not on
    a 9' wall. Treat the 9' group as estimator judgment or a possible double count of the
    recess wall. A drawing-faithful takeoff gives 269.53 SF on 310 (−16.5%).
  - Parapet studs are carried at the parapet height above the roof, separately from the
    wall below.
  - Openings are not deducted, and no extra jamb, corner or end studs are added: the SF is
    gross wall area.
- **Worked example (310):** 5.9 × 9 = 53.1 (judgment group); 9.2 × 12.25 = 112.7;
  8.4 × 18.67 = 156.828; Σ = 322.628 SF (estimate 322.77). With 18.67, the only 0.1-ft
  solution near the legend is 5.3 × 9 + 9.5 × 12.25 + 8.5 × 18.67, so even the 9' group's
  5.9 LF is not established. Stud-count check: `NO. OF STUDS @ 12'-3": ceil(9.2 × 0.75) = ceil(6.9) = 7` ✓.

## F2. Runners (lines 314–321)

- **Inputs:** the same legend rows as the stud line.
- **Rule:** `top_runner_LF = bottom_runner_LF = Σ LF_row` (no door deduction, no head or
  sill track at openings, no splice allowance).
- **Worked example (317/321, 8" 16 GA):** 46 + 38 + 13 + 96.6 + 5.9 + 89.7 + 41.5 + 8.7 =
  339.4 LF; the estimate carries 341.0 (−0.47%). The four gauges carry +1.3, +0.9, +0.5 and
  +1.6 LF beyond the legend rows. No legend row explains the extra, and it is larger than
  display rounding (max ±0.05 LF per row). These residuals are unexplained. The fixtures
  for 315/319 (−1.07%) and 316/320 (−2.08%) are flagged `knownResidual` and fail at the
  0.5% class tolerance.
- **Not the rule:** `stud count × 16/12` (272.0, 85.3, 22.7, 344.0 → +0.55%, +1.23%,
  −5.56%, +0.88%) fits worse than `Σ LF`.

## F3. Standard 5/8" gypsum board at walls (line 242)

- **Inputs:** each wall legend row `LF`, height `H`, faces `f`; specialty board areas
  measured on elevations (SF).
- **Faces rule** (A-620 Table A + legend wording):
  A-series tags (A3A, A3B, A6A, A6B) `f = 2`; D-series and rows named "1 SIDE" `f = 1`;
  exterior stud walls (EXT 8"/6") `f = 1` (interior face); rows named "BS GWB" `f = 2`;
  rows named "NO GWB", "BS 1/2" SHTNG ONLY" and parapets `f = 0`.
- **Rule:** `SF = Σ (LF × H × f) − MR_area − wall_tile_area − TypeX_area`. The board height
  is the full stud height: no 6"-above-ceiling cut, and no door or window deduction.
- **Worked example:** gross = 28.4×12.5×2 + 34.2×12.5×2 + 36.7×12.5×2 + 49.9×12.5×2 +
  3.7×12.5 + 46.0×12.5 + 89.7×12.75 + 9.2×12.25 + 41.5×15.75 + 13.0×4 + 18.3×4.33×2 +
  7.7×3.75×2 = **6529.48 SF**. Less restroom PT1 252.6, wall tile 244.2
  (120.7 + 43.8 + 50.6 + 15.3 + 1.4 + 1.3 + 8.2 + 1.6 + 1.3) and Type X 37.2, this gives
  **5995.48 SF** (estimate 6004.8655, −0.16%). The deductions use the *unrounded* specialty
  areas. Using their rounded-up line quantities (255 + 285 + 40) gives 5949.48 (−0.92%).
  The −9.4 SF residual is unexplained. The review pass searched every 0/1/2 face assignment
  of the 21 p4/p5/p7 rows and every deduction subset, and found no exact decomposition of
  6004.8655; this pass did not re-run that search.

## F4. Specialty board areas (lines 248, 260, 266, 272)

- **Rule:** `SF = ceil(measured_SF / 5) × 5`, the next 5 SF up.
- 248 Type X: ceil5(37.2) = **40** (round-to-5 would give 35, so the rounding is up).
- 260 moisture board = restroom painted wall area: ceil5(252.6) = **255**.
- 266 5/8" cement board = all wall-tile areas: ceil5(244.2 + 38.4) = ceil5(282.6) = **285**.
  This includes the WT3 transaction-bar tile, which also carries the 1/4" backer (see F5).
- 272 1/4" cement board: ceil5(38.4) = **40**.

## F5. Parapet glass-mat sheathing (line 254)

- **Inputs:** parapet rows `LF`, parapet height `H` (above roof), one face (roof side, under the membrane).
- **Rule (fitted, single data point):** `SF = Σ ceil(LF × H)` per row, each row rounded up
  to a whole SF. This rule fits 658 but nothing else corroborates it. No other line in the
  job ceils rows inside a sum, and line 311 uses the same four rows unrounded. The nearest
  analogue, the whole-SF ceil of the single booth area (F7, also used by paint line 302), is
  a different rule. Treat the 0.39% gap between the unrounded sum and 658 as rounding noise;
  it is not a proven convention. The fixture tolerance (0.5%, the LF × H class) covers the
  unrounded value.
- **Worked example:** 46.0×1.58 = 72.68 → 73; 38.0×2.58 = 98.04 → 99; 96.6×4.58 = 442.43 → 443;
  5.9×7.17 = 42.30 → 43; Σ = **658**.
- **Alternatives from the same inputs:**

| Rounding | Two-decimal heights | Exact-fraction heights |
|---|---|---|
| None | 655.45 (−0.39%) | 656.03 (−0.30%) |
| Round each row | 655 | 656 |
| Ceil of the total | 656 | 657 |
| Ceil to 5 SF | 660 | 660 |
| Ceil each row | **658** | **658** |

  Only ceil-per-row gives 658.

## F6. Board accessories (5 lines per board line; same ratios for all six boards)

Inputs: parent board SF (the estimator's rounded line quantity). Ratios are the
estimator's house convention, identical for gypsum, Type X, MR, glass-mat and both
cement boards. All 30 lines reproduce exactly on the estimator's parent.

| Line | Rule | Basis (this job) | Worked example on 242 (6004.8655 SF) |
|---|---|---|---|
| NO. OF SHEETS (EA) | SF / 32 | 4×8 sheet, no waste, fractional | 187.652047 |
| ADHESIVE (TUBES) | SF × 0.031 | ≈ 1 tube per 4×8 sheet (32 × 0.031 = 0.992) | 186.150831 |
| TAPING (ROLLS) | SF × 0.00075 | 0.375 LF tape per SF ÷ 500 LF roll | 4.503649 |
| DRYWALL SCREWS (LBS) | SF × 3/560 = SF × 0.0053571 | e.g. 1.2 screws/SF ÷ 224 screws/lb (any pair with that ratio) | 32.168922 |
| MUD PLASTER (LBS) | SF × 0.53 | 530 lb compound per 1,000 SF | 3182.578715 |

The ratios were derived from this job: each child ÷ parent is constant to 6
significant figures across all six parents (e.g. 0.214286 / 40 = 0.00535714 = 3/560).

## F7. Booth ceiling framing (line 312)

- **Inputs:** framed booth-roof area `A` (SF, p29), joist spacing `s` = 12".
- **Rule:** `LF = ceil(A) × 12 / s`; at 12" o.c. that is 1 LF of joist per SF.
- **Worked example:** ceil(76.2) = 77 × 12/12 = **77 LF** (PT-5 booth-roof paint, line 302,
  uses the same 77).

## F8. Canopy framing (line 313)

- **Inputs:** canopy framing area `A` (SF, S-203 p34), spacing 16".
- **Rule:** `LF = ceil5(A) / 1.33`. 1.33 is the estimator's rounded 16/12 ft, so this is
  `ceil5(A) × 12/16` with the spacing rounded.
- **Worked example:** ceil5(416.9) = 420 / 1.33 = **315.789474 LF** (exact). With 12/16
  exactly: 315.0 (−0.25%). The same 1.33 convention appears in the ceiling-framing line
  284 (516 / 1.33).

## Conventions summary

| Convention | Value | Basis |
|---|---|---|
| Stud quantity unit | SF of framed wall = Σ LF × H | lines 308–311 |
| Heights | two-decimal feet (4.33, 18.67) | 309 exact; 308/310 impossible with exact 18'-8" |
| Stud spacing | 16" o.c. unless detailed (booth 12") | 09 22 16 p270; A-706 |
| Openings | not deducted from studs, runners or board | 242 and 308–321 reconcile without deductions |
| Board height | full stud height on every finished face | 242 |
| Specialty area rounding | ceil to 5 SF | 248, 260, 266, 272 |
| Parapet sheathing rounding | ceil to whole SF per row (*fitted to one line*) | 254 only; not corroborated |
| Framed-top rounding | ceil to whole SF (booth), ceil to 5 SF (canopy) | 312, 313 |
| 16" o.c. as feet | 1.33 | 313 (and 09b line 284) |
| Waste | none in quantity lines (sheets fractional) | 243 = 242 / 32 exactly |
