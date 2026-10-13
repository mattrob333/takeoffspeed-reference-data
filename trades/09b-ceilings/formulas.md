# 09b Ceilings: formulas

All arithmetic was run in Python (`trades/09b-ceilings/scripts/build.py`, `verify_exact.py`). Legend values are
the PlanSwift numbers on markup pages 5 (A-130) and 6 (A-131). "Convention" means the estimator's own
ratio, computed from this job, not a published value. Every delta is (recomputed − estimator) / estimator.

## F1 Gypsum ceiling board (line 278)

- **Inputs:** `areaSF` (SF) of the RCP condition "5/8" GWB CEILING O/ 3-5/8" METAL STUD FRAMING (PT3)"; `layers` (EA) = 1.
- **Rule:** board SF = Σ plan area of the gypsum ceiling × layers. Net. No waste, no deduction for fixtures.
- **Worked:** 516.1 SF × 1 = 516.1 SF. The estimator carried **516.0** (rounded down to the whole SF): recomputed 516.1 is +0.02%.

## F2 Board accessories (lines 279–283 and 286–290)

One ratio set applies to every gypsum board group in this estimate (walls 242–277 use the same set).

| Line item | Rule | Ratio basis (convention, computed from this job) | Flat ceiling (516.0 SF) | Soffit (286.04 SF) |
|---|---|---|---:|---:|
| NO. OF SHEETS (EA) | SF / 32 | 4x8 sheet; 16.125 / 516 = 0.03125 | 16.125 | 8.93875 |
| ADHESIVE (TUBES) | SF × 0.031 | about 1 tube per 4x8 sheet; 15.996 / 516 = 0.031 | 15.996 | 8.86724 |
| TAPING (ROLLS) | SF × 0.375 LF/SF ÷ 500 LF/roll = SF × 0.00075 | 0.387 / 516 = 0.00075 | 0.387 | 0.21453 |
| DRYWALL SCREWS (LBS) | SF × 0.0375 / 7 (= SF ÷ 186.67) | 2.764286 / 516 = 0.00535714 = 0.0375/7 | 2.764286 | 1.532357 |
| MUD PLASTER (LBS) | SF × 0.53 | 273.48 / 516 = 0.53 | 273.48 | 151.6012 |

Every value is exact on the parent line (difference 0.000000). Recomputed from the legend
(516.1 / 286.20) they are +0.02% and +0.06%.

The tape ratio (0.375 LF/SF) matches USG's ~370 LF per 1,000 SF. The compound ratio (0.53 lb/SF) is about
3.8× USG's ready-mixed 138 lb per 1,000 SF. It is a house figure (it may include a Level 4 three-coat
allowance and waste), so keep it a convention.

## F3 Ceiling joists, area rule (line 284)

- **Inputs:** `areaSF` (SF) = line 278; `divisor` = 1.33 ft (16" O.C.).
- **Rule:** stud LF = SF / 1.33. This is SF × 12 / 16 with 16/12 written as 1.33. No member count, no end
  member, no perimeter track, no hangers.
- **Worked:** 516.0 / 1.33 = **387.969925** LF (exact, all six decimals). The exact 16/12 rule gives 387.000 (−0.25%).
- Sheet basis: the A-130 legend names the system ("5/8" GWB CEILING O/ 3-5/8" METAL STUD FRAMING"), and A-630 detail 1
  (cloud ceiling section) prints "3 5/8" MTL STUD FRAMING @ 16" OC". Only detail 1 gives that size: A-630 detail 3 reads
  "5/8" GYP BD ON MTL FRAMING @ 16" O.C." with no size, and detail 4 (the cloud light cove) reads "6" METAL STUD FRAMING"
  (see F5).

## F4 Soffit board from legend heights (line 285)

- **Inputs per soffit condition:** `lf` (LF) of run; `boardHeight` (FT) = the "GWB @ x'H" value, or the soffit height
  when the name has no GWB height; `faces` (EA) = 2 for "GWB BS" (both sides), else 1.
- **Rule:** SF = Σ lf × boardHeight × faces. No soffit bottom, no end returns. The framing height ("SOFFIT @ x'H") does
  **not** drive board unless no GWB height is given.
- **Worked (legend LFs):**

| Condition | LF | Board ht | Faces | SF |
|---|---:|---:|---:|---:|
| SOFFIT @ 3'6"H, GWB BS | 4.2 | 3.5 | 2 | 29.40 |
| SOFFIT @ 6'6"H, GWB @ 4'H | 2.7 | 4.0 | 1 | 10.80 |
| SOFFIT @ 3'6"H, GWB @ 1'6"H | 6.7 | 1.5 | 1 | 10.05 |
| SOFFIT @ 4'6"H, GWB @ 3'H | 30.5 | 3.0 | 1 | 91.50 |
| SOFFIT @ 5'9"H, GWB @ 2'6"H | 35.3 | 2.5 | 1 | 88.25 |
| SOFFIT @ 2'H | 28.1 | 2.0 | 1 | 56.20 |
| **Total** | | | | **286.20** |

  Estimator 286.04: +0.16 SF (+0.06%). The legend prints LF to 0.1 ft, so the maximum rounding error here is
  ±0.05 × Σ(boardHeight × faces) = ±1.0 SF, so 286.04 is inside the rounding band. With six free LFs, the existence of
  2-decimal LF sets that hit 286.04 exactly is compatibility with the rule, not proof of it.
- Alternatives tried and rejected: framing height × LF (452.1 SF, +58%), both faces on every run (572.4), adding a
  1 ft soffit bottom (+107.5 SF).

## F5 Soffit framing plus bracing, area rule (line 291)

- **Inputs:** each soffit `lf` (LF) and `framingHeight` (FT) = the "SOFFIT @ x'H" value; each bracing run `lf` (LF),
  `height` (FT) and `spacing` = 48 in; `divisor` = 1.33.
- **Rule:**
  `studs LF = Σ(lf × framingHeight) / 1.33 + Σ(braceLF / (48/12) × braceHeight)`
  Framing is counted once per run, even on "GWB BS" soffits (one stud line carries both faces). Bracing is one member
  of the stated height every 48" along the run.
- **Worked (legend LFs):**
  - framing area = 4.2×3.5 + 2.7×6.5 + 6.7×3.5 + 30.5×4.5 + 35.3×5.75 + 28.1×2 = 14.70 + 17.55 + 23.45 + 137.25 + 202.975 + 56.20 = **452.125 SF**
  - 452.125 / 1.33 = 339.944 LF
  - bracing = 27.1/4 × 5 + 28.1/4 × 8 = 33.875 + 56.200 = **90.075 LF**
  - total = **430.019 LF**. Estimator 429.599624: +0.10%.
- **Where bracing enters is a convention, not a finding.** Two bracing terms fit equally well:
  - adopted: braceLF / 4 × height, added after the divisor: 452.125 / 1.33 + 90.075 = **430.019** (+0.10%);
  - alternative: braceLF × height / 3, inside the divisor: (452.125 + 360.3 / 3) / 1.33 = **430.244** (+0.15%).

  The two results are 0.05% apart and both are well inside the error of the 0.1-ft legend LFs, so the legend cannot tell
  them apart. A brute force over every 2-decimal LF set that rounds to the legend (`verify_exact.py`, exact integer
  arithmetic) finds both rules reproducing 429.599624 exactly: 2,042 of the 10^8 soffit + bracing combinations under the
  adopted rule and 13,065 under the alternative. That test has eight free LFs and does not discriminate. The adopted
  form is kept because it reads straight from the condition name (one brace of the stated height every 48"); the
  fixture tolerance (0.5%) covers both. Bracing is about 21% of this line, so a tool that has no bracing input
  understates it by about 90 LF.
- Basis: A-630 detail 1 (cloud ceiling section) shows "3 5/8" ANGLE BRACING @ 48" O.C." and "3 5/8" MTL STUD FRAMING
  @ 16" OC" running to the deck.
- **Stud size disagreement (not in the estimate).** The estimator carries every soffit stud as 3-5/8". Two details call
  6": A-630 detail 4 "CEILING DETAIL" (the 9" × 10" cloud light cove, referenced from detail 1, so part of the Gathering
  Area cloud edge = the 30.5 FT "SOFFIT @ 4'6"H, GWB @ 3'H" row) reads "6" METAL STUD FRAMING", and A-131 detail 1
  "BAFFLE CEILING AT BULKHEAD" reads "5/8" GYP. BD. ON 6" MTL FRAMING @ 16" O.C." for the steel-beam wrap at the ACT-2
  edge (only the wall face there is "3 5/8" METAL FRAMING"). The quantity rule is unchanged; the size split is an RFI.

## F6 Acoustical ceiling area (lines 292, 293)

- **Inputs:** `areaSF` (SF) of the RCP condition per ACT tag; `module` (2x2 / 2x4); `tag`.
- **Rule:** SF = measured plan area (tile and grid in one SF line). Net. No waste, no attic stock, no fixture deduction.
- **Worked:** ACT-1 = 948.7 SF (legend 1 decimal), estimator 948.75 (2 decimals of the same PlanSwift value). ACT-2 =
  244.8 SF, estimator 244.81. Deltas −0.005% and −0.004%.
- Not carried but specified: 10% attic stock (09 5113 §1.2.D, p.289), which would be 94.9 SF ACT-1 and 24.5 SF ACT-2.
  Tile count, if wanted: ACT-1 948.75/4 = 237.2 tiles (2x2); ACT-2 244.81/8 = 30.6 tiles (2x4, per A-170).

## F7 Baffles (line 294)

- **Inputs:** each baffle run length (LF), or `fieldWidth` (FT) + `rowSpacing` (in) + `rowLength` (FT).
- **Rule:** LF = Σ run lengths. Row count from a field = floor(fieldWidth × 12 / rowSpacing) + 1.
- **Worked:** 37 yellow runs on markup p6 detail 5 (pixel measure 369.2 FT). Legend 370.8 FT, estimator 370.76 LF.
  Field check: 24'-0" across ÷ 8" O.C. = 36 + 1 = 37 runs; 370.76 / 37 = 10.02 ft average (runs vary from about
  8.7 to 10.4 ft where the bulkheads cut in).
- Owner furnishes BAR-1; the GC line is installation scope in LF.

## Classification

| Class | Lines |
|---|---|
| measured | 278, 292, 293, 294 |
| derived (formula on measured) | 279–291 |
| counted / specified / allowance | none |
