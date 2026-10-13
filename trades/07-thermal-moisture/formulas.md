# Formulas: 07 thermal and moisture protection

Every quantity below was rebuilt in Python (`trades/07-thermal-moisture/scripts/rebuild.py`)
from the legend values in `reference/markups/legends.json`. Units: LF = linear feet,
SF = square feet. Heights printed as feet-inches convert exactly (12'6" = 12.5 ft,
2'1" = 25/12 ft).

## Rounding conventions (the estimator's, measured on this job)

| Rule | Definition | Lines | Evidence |
|---|---|---|---|
| `ceil5` | round up to the next multiple of 5 | 166, 168, 170, 171, 175–183, 188, plus the parts of 160 | 1638.9→1640, 274.4→275, 8.8→10, 488.3→490, 358.7→360, 138.5→140, 13.9→15, 38.5→40, 39.9→40, 119.4→120, 24.4→25 |
| `round1` | round to a whole SF/LF | 158, 159, 161, 169, and the RT1 part of 163 | 285.4→285, 1864.3→1864, 76.2→76, 148.1→148 (ceil5 would give 150: the one exception) |
| `ceilFt` | round the run up to a whole foot | high-low wall in 154, 157, 163 | 45.3→46, confirmed by blocking lines 91/92 (46 LF) and 35 studs @ 16" at 2' (line 308) |
| none | carry the measured sum unrounded | 150, 164, 165, 167, 185–187, 189 | 221.96, 262.06, 2149.28, 286.79, 48.27, 101.18, 213.07 (162's 3042.774 is also unrounded, but not a measured sum) |

The rounding is part of the estimator's convention. The app should apply it as a
presentation step (or skip it in `mode: 'net'`), never inside the arithmetic.

---

## F1 Cavity insulation SF (batts and sound blankets in stud walls)

- **Inputs:** run LF of each wall row (A-120 legend, by tag), framing height H (ft) from the row name.
- **Rule:** `SF = Σ (LF_row × H_row)`. One layer per cavity. Openings, studs and tracks are **not**
  deducted. The batt goes to the full framing height, which is height letter **B** "to structure w/ batt".
- **Which rows:** A-620 Table D height letters **B, D, F** carry batt (A3B, A6B). Note B makes every exterior-faced
  wall insulated. The batt thickness follows the stud depth: 3-5/8" → 3-1/2", 6" → 5-1/2", 8" → 8".
- **Worked examples:**
  - Line 152 (3-1/2" SAB): A3B 34.2 LF × 12.5 = **427.5 SF** (exact).
  - Line 153 (5-1/2" SAB): A6B 28.4 × 12.5 = 355.0, against the estimate's 356.25 = 28.5 × 12.5 (the legend shows 0.1 LF of display rounding; −0.35%).
  - Line 155 (5-1/2" batt): EXT 6" @ 12'3" 9.2 × 12.25 = 112.7, against 113.3125 = 9.25 × 12.25 (−0.54%).
  - Line 156 (8" batt): the sum over every 8" stud row, which equals the 8"-stud SF of line 311:
    46×1.5833 + 38×2.5833 + 13×4 + 96.6×4.5833 + 5.9×7.1667 + 89.7×12.75 + 41.5×15.75 + 8.7×15.75 = **2642.36** against 2652.875 (−0.40%).
    The estimate line is carried from framing line 311 as the estimator computed it. The legend rebuild is 10.52 SF short, and
    that residual is **unexplained**. It is not display rounding: closing it would need one row to move by 0.8 LF or more
    (89.7 → 90.52, or 41.5 → 42.17). The fixture keeps a 0.5% tolerance to absorb this gap, not because the gap is understood.
    This includes **656.0 SF of roof parapets** above the deck.
  - Line 154 (3-1/2" batt "at exterior walls"): this is the high-low wall (8/A450). ceilFt(45.3) = 46 LF × 2.0 = **92 SF** (exact).

## F2 Booth-ceiling sound batt (line 161)

`SF = round1(booth roof area)` = round(76.2) = **76**, from the p29 row "6"THK. 16GA. METAL STUD @ 12" O.C W/ 6"THK. SOUND BATT …" (76.2 SQ FT).

## F3 Rigid board in a band (line 157, roof transition wall)

- **Inputs:** run LF, band height (ft).
- **Rule:** `SF = ceilFt(LF) × (wall height + 6" over the top)`.
- **Convention:** 2.5 ft, back-solved (115 / 46). Detail 10/A450 shows the 2" rigid running up the
  transition wall and over the 2x blocking.
- **Example:** 46 × 2.5 = **115 SF** (exact).

## F4 Rigid board behind cladding (line 160)

- **Inputs:** the ACM wall SF and the brick veneer SF (the two claddings drawn with rigid insulation: 1, 2/A430 ACM and 4, 5/A430 masonry).
- **Rule:** `SF = ceil5(ACM1/2 SF) + ceil5(brick SF)`. In other words, line 181 + line 32. EIFS is not included because its EPS is part of the EIFS line.
- **Example:** ceil5(108.7 + 379.6 = 488.3) = 490, plus ceil5(163.6 + 232.1 = 395.7) = 400, gives **890** (exact). The raw sum is 884.0.

## F5 Under-slab XPS with a perimeter turn-down (line 151)

- **Inputs:** slab SF (S-201 legend), insulated perimeter LF (8" stem wall run), turn-down depth (2'-0", G-003 detail 1).
- **Rule:** `SF = slab SF + perimeter LF × 2.0`.
- **Example:** 1917.6 + 193.8 × 2 = **2305.2** against 2298 (+0.31%). The estimate implies a 190.2 LF perimeter.
  The detail says "where req'd zones > 4". Warner Robins is zone 3A (COMcheck), so this scope is optional.

## F6 Roof insulation and cover board

- Line 159: `SF = round1(RT1 area)` = **1864**. One line covers the whole 6" stack. The estimator does
  **not** multiply by the 3 layers of 2".
- Line 158: `SF = round1(RT2 area)` = **285**.
- Line 164 tapered crickets: the measured cricket area, **262.1**. It is not added to the field, because the crickets sit on top of RT1.
- Line 163 cover board: `SF = round1(RT1) + ceilFt(high-low LF) × 2.0` = 1864 + 46 × 2 = **1956** (exact).
  The cover board continues up the transition wall face (8 and 10/A450). RT2 gets none.

## F7 Roof vapor barrier (line 165)

`SF = RT1 + RT2` = 1864.3 + 285.4 = **2149.7** against 2149.28 (+0.02%). This barrier is "assumed": the TPO spec
does not call for one. Confidence should be low.

## F8 Single-ply membrane (line 162), not reconciled

- **Inputs:** roof field SF, plus each flashing run with its developed height.
- **Rule (measured rows only):** `SF = field + Σ(parapet-lap LF × lap height) + high-low LF × 2' + canopy-edge LF × 4"`.
- **Example:** 2149.7 + (43.3 × 25/12 + 56.5 × 1 + 87.8 × 3.5 = 454.008) + 45.3 × 2 = 90.6, plus
  138.5 × 4/12 = 46.17, gives **2740.47** against 3042.774 (−9.9%).
- **Basis:** the PARAPET LAP rows carry their membrane height in the row name. The 8/A450 row says
  "LAP ROOF 2', INCL WALL". Detail 10/A430 says "ROOF SYSTEM RT-2, WRAP MEMBRANE 4" MIN. OVER EDGE OF CANOPY",
  and detail 7/A430 draws the membrane turning about 3-1/2" down the edge. The 12" + 12" + 6" girth in line 183 belongs to the ACM fascia, not the membrane.
- **Residual:** about **302.3 SF** of the estimator's 3042.774 cannot be reproduced from any measured row. Fits that close the
  gap are not unique: 515 combinations of high-low height (0–5 ft), edge girth (0–5 ft) and curb and hatch flashing (0, 8, 12 or 18 in)
  land within 0.1%. One example is adding the crickets (262.1) plus curbs × 1 ft (39.9), giving 3042.47. None of them has drawing support.
- **Test use:** there is no fixture for this line. Score the membrane on the measured terms and report the gap rather than fitting it.

## F9 Strip barrier at curbs (line 166)

`SF = ceil5(curb LF × 1.0 ft)` = ceil5(39.9) = **40**. Detail 1/A450 shows a PSA air/vapor barrier on the deck
flutes and up the wall. The 1 ft width is the estimator's choice; the curb itself is 18" high.

## F10 Linear sheet metal and accessories

`LF = ceil5(measured run)`, or round1 for line 169.

| Line | Run | Measured | Result |
|---|---|---|---|
| 168 coping 2'7" | COPING 3/A430 | 13.9 | 15 |
| 169 coping 2' | COPING 6/A450 | 148.1 | 148 (round1) |
| 170 coping 2'4" | COPING 9/A450 | 38.5 | 40 |
| 171 18" RTU curb | CURB - 1/A450 | 39.9 | 40 |
| 177 counter flashing | CURB - 1/A450 | 39.9 | 40 |
| 175 two-piece head flashing | 9/A430 | 119.4 | 120 |
| 176 self-adhered flashing strip | 9/A430 (same run, the same detail calls both) | 119.4 | 120 |
| 183 ACM canopy fascia | CANOPY EDGE 7/A430 | 138.5 | 140 |
| 188 integrated sill pan | A-200 "Linear" (storefront sills at the slab, doors excluded) | 24.4 | 25 |

## F11 Hatch curb (line 172)

`LF = count × 2 × (W + L)` = 1 × 2 × (30" + 36") / 12 = **11 LF**. The 30 × 36 size is confirmed by spec 07 7200 (p200).

## F12 Counts (lines 173, 174)

Drain flashing **11 EA** and vent flashing **3 EA**, from the dots on A-140.

## F13 Cladding areas (lines 178–182)

`SF = ceil5(Σ elevation areas)`.

| Line | Areas | Raw | Result |
|---|---|---|---|
| 178 EIFS-1 | 599.9 + 1039.0 | 1638.9 | 1640 |
| 179 EIFS-2 | 189.7 + 84.7 | 274.4 | 275 |
| 180 EIFS soffit (A-130) | 8.8 | 8.8 | 10 |
| 181 ACM1/2 (A-200 + A-420) | 108.7 + 379.6 | 488.3 | 490 |
| 182 ACM-3 canopy soffit (A-130) | 358.7 | 358.7 | 360 |

## F14 Fluid-applied wall vapor barrier (line 184)

`SF = line 178 + 179 + 180 + 181 + canopy-ceiling sheathing (line 85)` = 1640 + 275 + 10 + 490 + 568.5 = **2983.5** (exact).
This adds the rounded cladding lines, not raw areas. Brick has its own barrier line 35 (400 SF, masonry trade).

## F15 Elevation linear items, unrounded sums (lines 150, 185–187, 189)

| Line | Item | Runs | Sum | Estimate | Delta |
|---|---|---|---|---|---|
| 185 | sill | 28.9 + 19.4 | 48.3 | 48.27 | |
| 186 | aluminium flashing | 31.2 + 70.0 | 101.2 | 101.18 | |
| 187 | thru-wall flashing | 101.6 + 111.5 | 213.1 | 213.07 | |
| 150 = 189 | sealant with backer rod | 65.7 + 156.2 | 221.9 | 221.96 | −0.03% |

The small residuals are legend display rounding. Lines 150 and 189 are the **same measurement entered twice**.

## F16 Acoustic sealant at partitions (line 148), inferred convention

- **Inputs:** run LF by group: A-series partitions (GWB both sides, to structure), D-series (GWB one side), low walls, and
  exterior stud walls with an interior GWB face.
- **Rule (follows the details):** count beads as head + base per finished face, with no head bead on partial-height walls.
  `LF = 4 × A + 2 × (D + low + exterior)`.
  - A-B01 draws two base beads (one at each runner flange) and A-T01 draws two head beads, so A = 4.
  - D-B01 draws one "CONTINUOUS ACOUSTICAL SEALANT" bead, on the gypsum-board side only. D-T01 draws one "CONTINUOUS SEALANT" bead. So D = 2.
  - The 3'9" and 4'4" low walls take the two-sided base detail, and no head detail exists for them, so low = 2.
  - The exterior walls have no sealant detail. They are treated like D (one GWB face), giving 2.
- **Example:** A 28.4 + 34.2 + 36.7 + 49.9 = 149.2. D 3.7 + 46.0 = 49.7. Low 7.7 + 18.3 = 26.0. Exterior 89.7 + 9.2 + 41.5 + 13.0 = 153.4.
  4 × 149.2 + 2 × (49.7 + 26.0 + 153.4) = **1055.0** against 1053.5 (+0.14%).
- **Second fit, equally unconfirmed:** 4 × all interior LF (224.9) + 1 × exterior LF = 1053.0 (−0.05%). This one is numerically closer, but
  it contradicts D-B01 (four beads on a one-face wall) and puts head beads on walls that do not reach a head. If D-T02 (no sealant) is applied
  to D3C and the 4'H exterior wall gets no head bead, the detail rule drops to 1038.3 (−1.4%). So **neither rule is confirmed**.
- **Basis:** A-620 partition base and head details, and note K. Spec 07 9200 3.3.G says "both faces of partitions at perimeters". The line's
  drawing reference, "A1.1", is not a sheet in this set.

## F17 Sealant at openings (line 149), allowance

- **Rule:** none. The 1330 LF is carried as an allowance, with low confidence. There is no fixture for it.
- **Coincidence check (not a rule):** opening-trim LF (line 88, 910, itself "assumed") + Σ 2(W+H) of every glazed unit = 1329.06.
  The glazed perimeters are A 49.92, B 43.83, C 38.67, D 34.67, E 2 × 26.67, F 32.00, G 45.33, H 46.67, J 39.38 and K 35.27, a total of 419.06.
  This sum rests on another assumed line and includes the interior storefronts J and K. It is close to 1330 but does not explain it.
- **Measured alternatives:** no door-only or window-only combination of A-600/A-610 perimeters lands within 12 LF of 1330
  (jambs + head 182.33 LF, full perimeters 218.67 LF, glazed 419.06 LF, 0–4 faces each). A door-only reading of A-600 note 2
  (2 faces × jambs + head of 7 interior doors) would give 238.7 LF.
