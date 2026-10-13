# Formulas: 32a paving, marking, signs, bike racks, bollards

All arithmetic was checked with Python (`trades/32a-paving-marking/scripts/calc.py`, `build.py`). Units: SF, LF, EA, CY, ft.

**Notation**

- `ceil()` rounds up to the next whole unit.
- `r2()` rounds to 2 decimals (half-up).
- "Legend" means the PlanSwift legend on markup page 72 (C-3.0), unless noted otherwise.

---

## F1. Measured pavement area by duty (asphalt)

- **Inputs:** `areas[]` (SF) = the PlanSwift polygons of one pavement duty, measured to the curb face or gutter lip.
- **Rule:** `SF = Σ areas`, carried at PlanSwift precision (2 dp). No rounding and no waste.
- **Convention:** one line per duty. The layer stack goes in the description only. The thickness of each layer does not change the SF quantity.
- **Worked example:**
  - Line 633: legend `3:HEAVY DUTY ASPHALT PAVEME...` = **11,367.3 SF**.
  - Line 632: legend `4: STANDARD DUTY ASPHALT PAV...` = 2,459.2 SF, which the estimate prints as **2,459.18**. The legend shows 1 dp; the estimate keeps 2.

## F2. Concrete flatwork area (same-section merge, ceiling)

- **Inputs:** `areas[]` (SF) of every keynote polygon that shares one section text.
- **Rule:** `SF = ceil(Σ areas)`.
- **Convention:** this is the estimator's own rule. Concrete flatwork, ramp and curb quantities are rounded **up** to a whole unit. It appears on four lines here:
  - 747.6 → 748
  - 1,834.7 → 1,835
  - 113.3 → 114 (this one shows it is a ceiling, not nearest rounding)
  - 993.9 → 994

  Keynotes with identical text ("HEAVY DUTY CONCRETE PAVEMENT, SEE SHEET C-6.2") are merged into one line, except where the use differs (the dumpster slab stays separate, line 663).
- **Worked example (line 634):** keynote 21 at the ADA stall/aisle (teal) is 241.8 SF, and keynote 18 at the drive-thru slab (bright green) is 505.8 SF. 241.8 + 505.8 = 747.6, and ceil gives **748 SF**.

## F3. Sidewalk area

- **Inputs:** `areas[]` (SF) of the sidewalk polygons (keynote 5). The ramps are measured separately.
- **Rule:** `SF = ceil(Σ areas)`.
- **Worked example (line 635):** ceil(1,834.7) = **1,835 SF**.

## F4. Sidewalk expansion joint from area

- **Inputs:**
  - `sidewalkSF` (SF): line 635 after rounding.
  - `spacing` (ft): from the C-6.0 SIDEWALK DETAIL, "EXPANSION JOINTS REQUIRED AT ALL STRUCTURES, MAX. SPACING TO BE 25'", with "1/4" EXP. JOINT".
- **Rule:** `LF = sidewalkSF / spacing`.
- **Basis:** a walk of width W and length L = SF/W gets L/spacing transverse joints, each W long. So LF = (SF/W/spacing) × W = SF/spacing, and W drops out. This lets the joint LF be computed from the area alone, with no centerline runs.
- **Worked example (line 636):** 1,835 / 25 = **73.4 LF**. The unrounded 1,834.7 / 25 gives 73.388 (−0.016%).
- **Not included:** the 1/2" joint at the building pad and the 15# felt at parallel curbs (both are C-6.0 notes). Joints at structures are not added either.

## F5. Curb ramp area

- **Inputs:**
  - `rampAreas[]` (SF): keynote 6 polygons including the flares.
  - `ramps` (EA): count of keynote-6 tags.
- **Rule:** `SF = ceil(Σ rampAreas)`.
- **Worked example (line 637):** 113.3 SF over 2 ramps (C-3.0 tags keynote 6 twice; average 56.65 SF each). ceil gives **114 SF**.

## F6. Curb and gutter length

- **Inputs:** `runs[]` (LF) along the curb face, following the radii. Ties to existing curb are excluded.
- **Rule:** `LF = ceil(Σ runs)`.
- **Worked example (line 638):** ceil(993.9) = **994 LF**. The profile from C-6.0 (6" x 12" curb with 18" gutter, 4" GAB) goes in the description.

## F7. Stripe length (SSWL, stop bar)

- **Inputs:**
  - `runs[]` (LF) as drawn
  - `width` (in)
  - `color`
- **Rule:** `LF = Σ runs` at PlanSwift precision. Coats and width do not change the LF.
- **Worked example:**
  - Line 642, 4" SSWL: **441.31 LF** (legend 441.3).
  - Line 646, 24" stop bar: **49.58 LF** (legend 49.6). These are 2 bars at an average of 24.79 LF each, across the 24' drives.

## F8. Striped crosswalk, traced linework

- **Inputs:**
  - `runs[]` (LF) = everything traced on the crosswalk: both edge lines plus both sides of every bar.
  - Geometry for checking: crossing length C, walk width W, bar count, bar width.
- **Rule (estimator):** `LF = Σ traced runs`. This is not the crossing length.
- **Geometry check (CAD vectors of C-3.0):**
  - C = 22.5', W = 5', four 2' x 5' bars.
  - The estimator's method gives 2C + 2·bars·W = 45 + 40 = 85.0 LF.
  - The estimate's 79.46 is 0.935 × 85. The trace probably stopped short of the curb lines.
  - Paint area would be 4×2×5 + 45 × 4/12 = 55 SF.
- **Worked example (line 643):** legend 79.5 FT, estimate **79.46 LF**.

## F9. ADA access-aisle 45-degree hatch, traced linework

- **Inputs:**
  - `runs[]` (LF) of hatch lines plus the aisle outline as traced
  - aisle 5' x 18'
  - line width 4"
  - color BLUE
- **Rule (estimator):** `LF = Σ traced runs`.
- **Geometry check (C-3.0 vectors, `pymupdf get_drawings()`):** keep line items whose endpoints lie inside the 5' x 18' aisle rectangle and whose dx/dy is 0.8–1.25 (45°). The 0.72-pt hatch pen gives 12 segments totalling **66.06 LF**; including the 0.12-pt annotation strokes in the same box gives 16 segments, 68.96 LF.
  - Hatch + two 18' sides = 102.06 (97.48 is 0.955 of it).
  - Hatch + full perimeter 46' = 112.06 (0.870).
  - Neither ratio matches the crosswalk's 0.935 (F8), so no common short-trace factor exists. The traced 97.48 LF is reproduced as measured; how the estimator cut it is not recoverable. (An earlier draft gave 58.18 LF for the hatch; that sum missed one full 7.05' diagonal and the 0.83' corner stub, and does not reproduce.)
- **Worked example (line 644):** legend 97.5 FT, estimate **97.48 LF**.

## F10. Counted items

- **Inputs:** `count` (EA) of the legend symbols (circles) on the plan. Cross-check against the keynote tags and the enlarged plans.
- **Rule:** `EA = count`.

| Line | Item | Count | Cross-check |
|---|---|---|---|
| 645 | ADA painted symbol | 1 | = accessible stalls; C-3.0 note 5: 1 HC space |
| 647 | Arrow | 2 | keynote 15, two arrow leaders |
| 648 | ADA sign | 1 | one per accessible stall; van plaque because that stall is van accessible |
| 649 | STOP R1-1 | 3 | keynote 12 tagged 3× |
| 650 | DO NOT ENTER R5-1 | 2 | keynote 13 tagged 2× |
| 659 | Bike rack | 2 | keynote 19 "BIKE RACK(S)" |
| 674 | Dumpster bollard | 5 | C-3.0 draws 5 (3 back wall + 2 gate jambs); **A-190 plan 4 shows 6** (4 back wall + 2 gate jambs) |
| 713 | Drive-thru bollard | 8 | A-401 enlarged plan shows 8 |

## F11. Pier footing concrete (estimator rounding)

- **Inputs:**
  - `n` = items × footings per item (EA)
  - `D` = pier diameter (ft)
  - `H` = pier depth below grade (ft)
- **Rule:** `CY = r2(π/4 × r2(D)²) × H × n / 27`.
- **Convention:** the diameter is rounded to 2 dp in feet (16" → 1.33), and then the circle area is rounded to 2 dp (1.33 → **1.39 SF**; 1.00 → **0.79 SF**). Exact π gives 1.396263 and 0.785398 SF, which is +0.45% and −0.58%.

  This convention is the estimator's own and matches the 32b sign and light-pole footings. The pipe volume is not deducted. The slab or paving over the pier is not deducted either.
- **Worked examples:**

| Line | Footing | Calculation | CY |
|---|---|---|---|
| 660 | Bike rack, 2 racks × 2 legs, 1'-0" × 1'-0" (assumed; no detail) | 0.79 × 1.0 × 4 / 27 | **0.117037** |
| 675 | Dumpster bollard, A-190 "16" DIA. CONCRETE PIER"; H = 3'-0" is an **estimator assumption** (A-190 section 3 gives the diameter only, pier drawn with break lines, no depth: RFI) | 1.39 × 3.0 × 5 / 27 | **0.772222** (with 6 bollards: 0.926667) |
| 714 | Drive-thru bollard, A-401 detail 8, "16" DIA. CONCRETE FILL"; H = 4.0 ft is the nominal pipe embedment "48" BELOW GRADE" (top of paving to pipe bottom). The detail adds 3" of fill below the pipe (51" total); the estimator did not add it or deduct the paving | 1.39 × 4.0 × 8 / 27 | **1.647407** (at 4'-3": 1.750370, +6.25%) |

The civil C-6.0 BOLLARD DETAIL is not used by either group: 24" dia footing, "4' MINIMUM" embedment from the pavement surface to the pipe bottom plus 3" of concrete below the pipe, "3' MINIMUM" exposed above the pavement, 6" x 7' pipe. At 5 dumpster bollards it would give π × 1² × 4.0 × 5 / 27 = 2.327 CY (4'-0") or 2.473 CY (4'-3").

## F12. Pier excavation and haul-off

- **Inputs:** the F11 result.
- **Rule:** `excavation CY = pier CY` (the whole pier is buried and poured against earth), and `haul-off CY = excavation CY` (no backfill, bank measure, no swell).
- **Worked example:** lines 661 and 662 = 0.117037; 676 and 677 = 0.772222; 715 and 716 = 1.647407.

## F13. Footing count for multi-leg items

- **Inputs:**
  - `items` (EA)
  - `footingsPerItem`: from the detail, or the estimator's assumption for the bike rack (2, an inverted-U rack)
- **Rule:** `n = items × footingsPerItem`.
- **Worked example:** bike rack 2 × 2 = 4 ("NO OF FOOTINGS: 4", line 660).

---

## Cross-check formula (not an estimate line): impervious area

`impervious ≈ building + asphalt + concrete flatwork + ramps + pads + curb LF × 2.0'` (the C&G width is 24").

1,900 + 11,367.3 + 2,459.2 + 1,834.7 + 113.3 + 747.6 + 384.3 + 16 + 993.9 × 2 = **20,810.2 SF**. The C-3.0 Site Summary gives 21,033 SF, so the difference is −1.06%. A larger gap would mean a missed area or a scale error.
