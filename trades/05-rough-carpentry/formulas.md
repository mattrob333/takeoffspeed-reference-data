# Formulas: rough carpentry

All arithmetic was done in Python (`trades/05-rough-carpentry/scripts/build.py`). Heights are printed feet-inches converted to decimal feet (12'-9" = 12.75 ft, 1'-7" = 1.58333 ft). Quantities are **net**: the estimator carries no waste in these lines.

## F1. Wall sheathing area

- **Inputs:** each wall run `LF` (FT, from the A-120/A-140 legend), sheathing height `H` (FT; from the legend name, or from a `SHTNG h` suffix when one is present), and `faces` (1 for the exterior face; 2 when the legend says `BS … SHTNG`).
- **Rule:** `SF = Σ LF × H × faces`, with **no opening deduction**. Storefront runs are traced through the glass at full height.
- **Conventions (estimator's, from this job):** wall height is taken to the deck (A-120) and parapet height above the deck (A-140) as separate rows, so the parapet face is added on top. A `SHTNG 10'3"H` suffix replaces the 12'3" wall height. The roof-side face of a parapet is glass-mat (09a), not plywood, so parapets count once.
- **Worked example (line 82, 1/2" plywood at exterior wall, estimate 3,057.0775 SF):**

| Legend row | LF | H (ft) | faces | SF |
|---|---:|---:|---:|---:|
| EXT 8" STUD WALL @ 12'9"H | 89.7 | 12.75 | 1 | 1,143.675 |
| EXT 6" STUD WALL @ 12'3"H SHTNG 10'3"H | 9.2 | 10.25 | 1 | 94.300 |
| PARAPET WALL @ 7'2"H A310 | 5.9 | 7.1667 | 1 | 42.283 |
| EXT 8" STUD WALL @ 15'9"H | 41.5 | 15.75 | 1 | 653.625 |
| EXT 8" STUD WALL @ 4'H | 13.0 | 4.00 | 1 | 52.000 |
| EXT 8" STUD WALL @ 15'9"H NO GWB | 8.7 | 15.75 | 1 | 137.025 |
| 6" & 3-5/8" METAL STUD @ 18'8"H, BS 1/2" SHTNG ONLY | 8.4 | 18.6667 | 2 | 313.600 |
| A-140 PARAPET WALL @ 1'7"H | 46.0 | 1.5833 | 1 | 72.833 |
| A-140 PARAPET WALL @ 2'7"H | 38.0 | 2.5833 | 1 | 98.167 |
| A-140 PARAPET WALL @ 4'7"H | 96.6 | 4.5833 | 1 | 442.750 |
| **Total** | | | | **3,050.258 (−0.22%)** |

- The residual of −6.82 SF is **not** fully explained by legend rounding on its own. Rounding ten LF values to 0.1 ft can move the total by at most Σ 0.05 × H × faces = 5.59 SF. Using the heights the estimator measured on A-300/A-310 (4'-7 1/16" for the 4'-7" parapet, 1'-7 1/8" for the 1'-7" parapet, 15'-9 1/16" on both 15'-9" rows) raises the recomputation to **3,051.50 SF (−0.18%)**, +1.24 SF. The remaining 5.58 SF would need every LF to have been rounded down by the full 0.05 ft, so about 1.2 SF of the residual is unexplained at printed heights.
- Line 81 uses the same form with one row: `WALL 706` 15.9 LF × 3.0 ft × 1 = 47.7 SF. The calculation is exact, but **3.0 ft is printed nowhere**. Full-height plywood behind the PL-1 laminate on both faces would be 15.9 × 9 × 2 = 286.2 SF.
- Line 83 (5/8", estimate 162.9919 SF) is **unresolved**. The drawing-supported candidate is the brick knee wall below the storefront sill: A-311 sec. 1 highlights "5/8" EXTERIOR SHEATHING" in the knee-wall callout stack, and that wall is 2'-8" high (F.F.E. to SILL). The implied run is 162.9919 / 2.6667 = 61.12 LF. The nearest legend rows are the A-200 `3-1/4"THK. x 3-5/8"H HALF ROWLOCK BRICK` 61.4 FT (× 2'-8" = 163.73, +0.45%) and `ROWLOCK SILL` 61.5 FT (164.00, +0.62%), but neither is a sheathing row, so no recomputation is claimed. The A-200 `5/8" PLYWOOD SHEATHING` area (52.1 SF) is kept separately, location unknown. The blue 12'-8 1/4" markup on A-311 is the measured F.F.E.-to-roof-deck height of the 12'-9" wall, not a sheathing height. The earlier chain, 52.1 + 8.7 LF (NO GWB) × 12'-8 1/4" = 162.48, was a backward fit and is dropped: the NO GWB run is a 15'-9" wall, and 52.1 + 8.7 × 12'-9" = 163.03 fits just as well.

## F2. Area sheathing and backing

- **Inputs:** traced area(s) `A` (SF), `layers` (count), and slope factor `s` (1.0 for flat).
- **Rule:** `SF = Σ A × s × layers`.
- **Worked examples:**
  - Line 84: `RT2 ROOFING` 285.4 SF × 1.0 = 285.4. The estimate is 285 (+0.14%).
  - Line 86: estimate 152 = 2 × 76.2 booth-roof area (152.4). The top layer is "3/4" PLYWOOD FRAMING. PAINTED PT-5" (A-706). The second layer is read as the ceiling-side "PLYWOOD SUBSTRATE" behind the PL-1 ceiling (A-706 det. 7/8, on Z-clips), whose thickness is not printed. The two 76.2 SF legend rows on p29 are the PT5 finish and the metal-stud booth-roof framing assembly on the same polygon, not two plywood layers.
  - Line 87: E-702 backboard 215.3 SF. The estimate of 215.33 is the unrounded value: 26.92 LF of elevation × 8'-0".
  - Line 85 (canopy ceiling, **unresolved**): the best numeric fit is soffit 358.7 SF (A-130 ACM-3) + canopy edge 138.5 LF × 1.5 ft = 566.45 SF (−0.36%). The 1.5 ft factor is fitted, not printed: (568.5 − 358.7) / 138.5 = 1.515 ft. A-430 det. 10 dimensions the ACM profiles (1'-0" = 1" + 10" + 1" is the edge depth; the bottom 6" to a 1/2" joint is the ACM soffit profile). The only sheathing it dimensions is two 5/8" decks (2 3/4" | 5/8" | 6" | 5/8" | 2" = 1'-0"), plus an undimensioned vertical "EXTERIOR SHEATHING" on 1 5/8" stud infill.

## F3. Backing panels from height-tagged runs, rounded up to 5 SF

- **Inputs:** runs `LF` with height `h` from `… PLYWOOD @ h` (FT), the row multiplier `n` from a leading `(n)`, `faces`, and plain areas `A` (SF).
- **Rule:** `SF = ceil5( Σ n × LF × h × faces + Σ A )`.
- **Convention (estimator's):** every BACKING line is rounded up to the next 5 SF. This rule reproduces lines 145, 146 and 147 exactly. The painting trade rounds the same 37.2 SF up to 40 in the same way.
- **Worked examples:**
  - Line 145: 4.0 LF × 3.75 ft × 2 faces = 30.0, and ceil5 leaves 30.
  - Line 146:

    | Legend row | Calculation | SF |
    |---|---|---:|
    | (2) 3/4" @ 1'4"H | 2 × 3.7 × 1.3333 | 9.867 |
    | 3/4" @ 8"H | 1.6 × 0.6667 | 1.067 |
    | 3/4" @ 7.67H | 8.6 × 7.67 | 65.962 |
    | A-702 | | 46.9 |
    | A-703 | | 8.0 |
    | **Total** | | **131.795** |

    ceil5(131.795) = **135** (the raw total is −2.4%).
  - Line 147: ceil5(37.2) = **40** (raw −7.0%).

## F4. Blocking LF by rows

- **Inputs:** each run `LF` (FT) and `rows` (the `(n)` prefix in the legend; 1 if absent).
- **Rule:** `LF = Σ rows × LF`. Board feet for purchasing are `LF × t × w / 12`, using nominal sizes.
- **Worked example (line 89, estimate 240.66 LF):**

  | Row | Calculation | LF |
  |---|---|---:|
  | (7) 1x4 FRT | 7 × 8.6 | 60.2 |
  | (2) 1x4 | 2 × 14.6 | 29.2 |
  | (4) 1x4 | 4 × 9.8 | 39.2 |
  | (2) 1x4 | 2 × 23.3 | 46.6 |
  | (2) 1x4 | 2 × 15.7 | 31.4 |
  | (5) 2x4 | 5 × 1.6 | 8.0 |
  | (3) 2x4 | 3 × 8.7 | 26.1 |
  | **Total** | | **240.7 (+0.02%)** |

- **Convention (estimator's):** the two 2x4 rows were folded into the 1x4 FRT line. The 1x4 rows alone total 206.6 LF (−14.2%).
- BF of line 89 is 240.66 × 4/12 = 80.2 BF.

## F5. Roof nailers: run LF of the condition, member size from the detail

- **Inputs:** the condition run `LF` (coping, curb or step-wall LF from A-140), and the member size(s) read from the called detail. When a detail stacks two members, each becomes its own line at the same LF.
- **Rule:** `LF(size) = run LF`. The estimator then rounds by judgment: 45.3→46 is ceil to 1 LF; 38.5→40 and 13.9→15 are ceil to 5 LF; 148.1→148 is round to nearest.

| Line | Run (legend) | Detail | Member | Raw LF | Estimate | Δ raw |
|---|---|---|---|---:|---:|---:|
| 91 | 8/A450 LAP ROOF 2', INCL WALL | A-450 det. 8/10 (two stacked P.T. members on the 3-5/8" step wall) | 2x4 | 45.3 | 46 | −1.5% |
| 92 | same | same | 2x6 | 45.3 | 46 | −1.5% |
| 93 | COPING 3/A430 | A-430 det. 3 (P.T. blocking across the 1'-8" wing wall) | 2x16 | 13.9 | 15 | −7.3% |
| 94 | COPING 6/A450 | A-450 det. 6 "2X P.T. WOOD NAILER", ~10" drawn | 2x10 | 148.1 | 148 | +0.07% |
| 95 | COPING 9/A450 | A-450 det. 9, wide nailer over wall + EIFS | 2x14 | 38.5 | 40 | −3.75% |
| 96 | same | A-450 det. 9 "BRAKE METAL OVER 1X BLOCKING" | 1x6 | 38.5 | 40 | −3.75% |

- **Alternative reading of the 46 LF (lines 91/92).** The A-140 legend also has `PARAPET WALL @ 1'7"H` = 46.0 FT exactly. If that were the source, 46 would be unrounded and the ceil-to-1 LF entry in the rounding rule above would disappear. It is rejected because the coping at the 1'-7" parapet (det. 6/A450) carries one 2x10 nailer (line 94), while det. 8/10 at the step wall shows the stacked 2x4 + 2x6, and the olive 8/A450 run on markup p7 follows the high-low step line.
- Board feet: 2x10 is 148 × 20/12 = 246.7 BF; 2x14 is 40 × 28/12 = 93.3 BF; 2x16 is 15 × 32/12 = 40.0 BF.

## F6. Opening-perimeter blocking

- **Rule:** `LF = traced perimeter of the opening`.
- **Worked example (line 97):** the night-depository outline on the A-201 east elevation is 8.8 FT. The estimate of 8.78 is the unrounded value.

## F7. Allowances (no formula)

- **Line 88:** interior trim at openings, 910 LF, marked "ASSUMED". For reference, the opening perimeters from the schedules total 570.3 LF:
  - interior doors on 2 sides: 238.7 LF
  - exterior doors on the interior side: 63.0 LF
  - windows on 4 sides: 268.6 LF

  The opening frames are hollow-metal and aluminium, and no detail calls for casing.
- **Line 90:** 2x4 FRT blocking, 10 LF. No legend row is left once line 89 is built.

## Sheets (purchase only, not carried by the estimator)

- **Rule:** `sheets = ceil(SF / 32)` for 4×8 panels.
- **Worked example:** line 82 is 3,057.08 / 32 = 95.53, so 96 sheets net. Line 87 is 215.33 / 32 = 6.73, so 7 sheets. The 8-ft backboards waste little because they are full-height panels.
