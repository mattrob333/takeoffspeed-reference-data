# Formulas — 32b site concrete and structures

Units: LF, SF and CY. Inputs are read from the markup legends and the details. Every number
below was recomputed in Python (`reconciliation.csv`). Quantities are **net**: the estimator
adds no waste and no swell to any line in this trade.

## Estimator conventions found on this job

| Convention | Value | Basis (computed from this job) |
|---|---|---|
| Circle area | `round(π/4 × round(D_ft, 2)², 2)` | 12" → 0.79, 8" → 0.35, 16" → 1.39, 18" → 1.77 SF. Only this rounding reproduces 0.102407, 0.194444, 0.772222 (16" bollards, another trade), 1.647407 and 2.786111 CY. Exact π gives 0.1018 / 0.1939 / 2.7816 (−0.6% to −0.2%) |
| Pier excavation | buried depth only; haul-off = excavation (no backfill) | 652/653, 655/656, 719/720 |
| Footing working space | 1'-0" each side | 665: trench width 4.0 for a 2'-0" footing |
| Depths and heights | carried to 2 decimals (2'-4" → 2.33, 6'-8" → 6.67) | 665, 673 |
| Per-LF wall accessories | `round(wall LF)` = 36 | 671, 672, 680, 681, 682 (the measured run is 36.22) |
| Grout, 8" CMU | 0.0112 CY per SF of wall (0.3024 CF/SF) | 669 = 289.76 × 0.0112 exactly |
| Mortar, 8" CMU | 0.1675 CF per SF of wall (= 0.67 ft × 25%) | 670 = 289.76 × 0.1675 / 27 exactly |
| Coating faces | 1 (outside face only) | 673. A-190 section 3 shows the coating outside and paint inside |

---

## F1 Pier footing concrete (sign posts, light poles)

- **Inputs:** footing count `n` (EA, from a legend count); diameter `D` (in); buried depth `B`
  (ft); exposed height `E` (ft, 0 when flush).
- **Rule:** `CY = round(π/4 × round(D/12, 2)², 2) × (B + E) × n / 27`
- **Worked examples:**
  - Line 651, ADA sign: n = 1 (`ADA PARKING SIGN - C6.0` 1.0 EA), D = 12", B = 3.5'.
    0.79 × 3.5 × 1 / 27 = **0.102407 CY**.
  - Line 654, traffic signs: n = 3 STOP + 2 DO NOT ENTER = 5, D = 8", B = 3'.
    0.35 × 3 × 5 / 27 = **0.194444 CY**.
  - Line 718, light poles: n = 1 (1P4F) + 4 (2P4DA) = 5, D = 18", B = 6', E = 2.5'.
    1.77 × 8.5 × 5 / 27 = **2.786111 CY**.

## F2 Pier excavation and haul-off

- **Rule:** `excavation CY = area × B × n / 27`, and `haul CY = excavation CY`.
  The concrete is poured against earth, so nothing is backfilled and there is no over-dig.
- **Worked examples:**
  - 652/653: 0.79 × 3.5 × 1 / 27 = 0.102407.
  - 655/656: 0.35 × 3 × 5 / 27 = 0.194444.
  - 719/720: 1.77 × **6.0** × 5 / 27 = **1.966667**. The 2'-6" exposed base is formed, not dug.
- Keep **one excavation/haul pair per footing type** (12" and 8" stay separate).

## F3 Measured pad and slab area

- **Rule:** `SF = Σ measured areas`. Pads drawn as dimensioned squares use
  `SF = n × W × L`.
- **Worked examples:**
  - 657 transformer pad: legend 16.0 SQ FT → **16 SF**.
  - 658 cleanout pads: 6 (C-5.0 `SANITARY CLEANOUTS`) × 1.5' × 1.5' (18"×18" plumbing note)
    = **13.5 SF**.
  - 663 enclosure slab and apron: the purple/mauve legend row (page 72, `21: HEAVY DUTY CONCRETE
    PAVE...` 384.3 SQ FT) → **384.31 SF**.
- Thickness is descriptive only (10" assumed, 6" or 8", 6"). The estimate carries these lines
  in SF and has no CY line.

## F4 Wall footing concrete

- **Inputs:** wall LF `L` (legend `DUMPSTER ENCLOSURE WALL` 36.22); footing W = 2'-0" and
  T = 1'-0" (A-190 section 3).
- **Rule:** `CY = L × W × T / 27`
- **Example:** 36.22 × 2 × 1 / 27 = **2.682963 CY** (664).

## F5 Wall footing excavation

- **Inputs:** `L`; W; working space `ws` = 1'; depth `Dp` = T + CMU below grade
  = 1'-0" + 1'-4", carried as 2.33.
- **Rule:** `CY = L × (W + 2·ws) × round(Dp, 2) / 27`
- **Example:** 36.22 × 4.0 × 2.33 / 27 = **12.502607 CY** (665). With an exact 2⅓, the
  result is 12.5205 (+0.14%).

## F6 Wall footing backfill and haul-off

- **Rule (estimator):**
  - `backfill = excavation − footing − CMU below grade`
  - `haul = excavation − backfill = footing + CMU below grade`
  - The estimator carried the CMU below grade as **1.16 CY** (31.32 CF).
- **Rule (physical):** `CMU below grade = L × t × h / 27` with t = 8" and h = 1'-4",
  which gives 1.1924 CY.
- **Example:**
  - Backfill: 12.502607 − 2.682963 − 1.16 = **8.659644 CY** (666).
  - Haul: 2.682963 + 1.16 = **3.842963 CY** (667).
  - The physical formula gives 8.6272 (−0.37%) and 3.8754 (+0.84%). Both are inside 1%.
    Backfill uses the 2.33 depth from F5: 12.502607 − 2.682963 − 1.192428 = 8.627216. The
    engine's 8.6451 (−0.17%) comes from the exact 2⅓ depth (excavation 12.5205). Haul does
    not use the excavation, so it is +0.84% either way.
  - `fixtures.json` 666/667 carry the estimator's 1.16 CY as an input (`cmuBelowGradeCY`) at
    0.1% tolerance, with the physical results in their `note`.

## F7 CMU wall area

- **Inputs:** `L`; height `H` from the top of the footing to the underside of the cap
  = 6'-8" + 1'-4" = 8'-0".
- **Rule:** `SF = L × H`. There is no gate deduction: the runs stop at the gate posts.
- **Example:** 36.22 × 8.0 = **289.76 SF** (668).

## F8 Grout (estimator convention)

- **Rule:** `CY = CMU SF × 0.0112`
- **Example:** 289.76 × 0.0112 = **3.245312 CY** (669).
- **Basis:** the rate is solid grout for 8" CMU (the NCMA rate is about 0.26 CF/SF;
  0.3024 is about 16% over it).
- **Physical cross-check (S-001 note 4):** grout the reinforced cells, the bond beam and every
  cell below grade.
  - Below grade: 36.22 × 1.333 = 48.29 SF solid.
  - Bond beam: 36.22 × 0.667 = 24.15 SF solid.
  - Remaining wall: 36.22 × 6.0 × 8/32 = 54.33 SF of cells.
  - Total 126.77 SF × 0.26 CF/SF = 32.96 CF = **1.22 CY**, about 0.38 times the estimator's
    rate.
  - **If two reinforced courses** (see F10: the K.O. block course one below the bond beam):
    below grade 48.29 SF + two solid courses 2 × 24.15 = 48.32 SF + remaining wall
    36.22 × 5.333 × 8/32 = 48.29 SF = 144.89 SF × 0.26 = 37.67 CF = **1.40 CY** (about 0.43
    times the estimator's).

## F9 Mortar (estimator convention)

- **Rule:** `CY = CMU SF × 0.1675 / 27`
- **Example:** 289.76 × 0.1675 / 27 = **1.797585 CY** (670).
- **Basis:** 0.1675 = 0.67 ft thickness × 25%. Against the trade rule (1.125 block/SF ×
  8.5 CF / 100 block = 0.0956 CF/SF → 1.0262 CY), the estimator's rate is 1.75 times higher.

## F10 Per-LF wall accessories

- **Rule:** `LF = round(L)`
- **Example:** round(36.22) = **36 LF**. This covers:
  - the bond beam with 1 cont. #5 (671; 1 course reproduces the estimator);
  - the 4" precast stone cap (672);
  - the thru-wall flashing with integral drip (680);
  - the continuous drip (681);
  - the continuous sealant (682).
- Unrounded, each would be 36.22 (+0.61%).
- **Bond beam courses (671), ambiguous.** A-190 section 3 puts the "BOND BEAM W/ 1 CONT. #5"
  leader on the top course under the cap, and the "K.O. BLOCK W/ (1) #5 CONT., GROUTED SOLID."
  leader on the next course down, where a bar dot is drawn. That may be two reinforced
  courses: `LF = round(L) × courses` = 2 × 36 = **72 LF**. The estimator carried 36 (one
  course). The fixture keeps `courses = 1` and notes the alternative.

## F11 Wall coating

- **Inputs:** `L`; exposed height = 6'-8" (6.67); faces = 1.
- **Rule:** `SF = L × round(exposed H, 2) × faces`
- **Example:** 36.22 × 6.67 × 1 = **241.5874 SF** (673). With an exact 6⅔, the result is
  241.4667 (−0.05%).

## F12 Weep screen (estimator; flagged)

- **Rule (estimator):** `LF = round(L) × 0.33`
- **Example:** 36 × 0.33 = **11.88 LF** (683).
- **Basis (inferred):** 0.33 ft = 4". This looks like the area of a 4" strip (SF) entered under
  the LF unit.
- **Physical rule:** `LF = L` along the base of each coated face, which gives 36.22 LF.
  A fixture for the estimator's number must carry the flag.

## F13 Counts

- **Rule:** `EA = legend count`, or a count on the enlarged plan.
- **This job:**
  - Gate (678): `DUMPSTER GATE` 1.
  - 2-yard dumpsters (679): 2 boxes on A-190 plan 4.
  - Monument sign (707): `PROPOSED MONUMENT SIGN` 1.
  - ATM (717): `ATM BY BANK EQUIPMENT VENDOR ...` 1.

## F14 Canopy

- **Rule:** `SF = round(measured footprint)`
- **Example:** legend 61.7 SQ FT → **62 SF** (712). The column count (2) goes into the
  description.
