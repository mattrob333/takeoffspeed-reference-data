# 03 — Masonry: reading the plans and specs

How to read this job's drawings and spec for the masonry quantities, with the strings exactly as
printed.

## 1. Find out what kind of masonry the job has

1. **Exterior Finish Schedule** on A-200 and A-201 (top band of the sheet). One masonry row:
   `EXT-1 | STANDARD MODULAR BRICK VENEER | ACME BRICK | SLATE GRAY | MORTAR MANUFACTURER: COOSA , MORTAR COLOR: OLD LIME PUTTY`.
   No EXT-2 masonry row appears in this schedule. A-202 (perspective views) prints `EXT-2` beside `EXT-1`, but no measured item or estimate line uses it. The other tags are EIFS, ACM, AL, GL and M-1.
2. **Elevation callouts** on A-200/A-201: `BRICK ROWLOCK, EXT-1` (upper line, at the top of the band) and `BRICK WATERTABLE, EXT-1` (lower line, pointing at the band itself). The estimator's line descriptions do not use the word "watertable". The band is the running-bond field brick (line 32), and the "rowlock" callout covers both special courses (lines 33, 34).
3. **Wall sections** A-310 (3 sections) and A-311: the build-up from outside in, `EXT-1 ROWLOCK BRICK SILL` / `EXT-1 HALF ROWLOCK, RECESSED` / `EXT-1 RUNNING BOND BRICK` / `AIR SPACE & RIGID INSULATION` (R-10) / `FLUID-APPLIED VAPOR BARRIER` / `1/2" EXT. SHEATHING` / `8" MTL. STUD & BATT INSULATION`, and below grade `CMU FULLY GROUTED BELOW GRADE` / `FULLY GROUTED MASONRY BELOW GRADE`. The datum `SILL 2'-8"` is the top of the band.
4. **The governing detail** is A-430 detail 4, `SECTION DETAIL @ MASONRY BASE` (1 1/2" = 1'-0"). Read from it:
   - `4" CMU FULLY GROUTED BELOW GRADE`: **2 courses** on the footing (16" = 1'-4"). This is the CMU height.
   - `GROUT CAVITY BELOW GRADE`: the gap between the CMU/brick and the 8" concrete stem wall is grouted.
   - `STANDARD MODULAR BRICK COURSING`: **12 courses** = 32", from 8" below `0'-0" LEVEL 01` up to the underside of the half rowlock (+2'-0").
   - `HALF ROWLOCK BRICK, RECESSED 1/2"`, then `ROWLOCK BRICK SILL, OVERHANG MIN. 1/2"` with the sill top at `2'-8"`.
   - `ADJUSTABLE BRICK TIES @ 32" O.C. HORIZ. & 16" O.C. VERT.`, `CONTINUOUS THRU-WALL FLASHING`, `WEEPS @ 24" O.C.`, `CONTINUOUS MORTAR NET`, `TERMINATION BAR & SEALANT`, `FLUID-APPLIED VAPOR BARRIER`.
   - Detail 5 `MASONRY SILL TO EIFS` is the same band where EIFS sits above.
5. **Structural** S-600 sections 1–2 (`Section at Exterior Wall`): `4" CMU BELOW GRADE. FOR BRICK VINEER. AND WALL TIES BACK TO METAL STUD SEE ARCH.`, `GROUT CAVITY SOLID UP TO GRADE`, and the 8" stem wall on the strip footing (footing `1'-0"` deep). Both sections also print `SHELF ANGLE, FOR BRICK VENEER. AND WALL TIES BACK TO METAL STUD SEE ARCH.` with the leader at the top of the band under the punched window. A-430 det. 4 shows no shelf angle: the brick bears on the CMU and is capped by the rowlock sill with flashing at 2'-8" (trap 11). S-001 `CONCRETE MASONRY NOTES` give the mortar (Type S), grout (ASTM C476, f'g 2250 psi), f'm 2250 psi, and "do not fill cells … except below grade".
6. **Spec** 04 2113 (spec pages 67–77) for brick, ties, flashing and weeps. Section 04 7200 (stone) has no use on this job, and the manual has no CMU section.

## 2. Read the markup legends

| Page (sheet) | Legend row, as printed | Qty | Colour | What the colour covers |
|---|---|---|---|---|
| p03 (A-110) | `4"THK. CMU STEM WALL W/ GROUT CAVITY SOLID @ 1'4"H` | 157.4 FT | mauve | A line traced on the outside face of the exterior wall, wherever the brick band is: the full west wall down to grid D, the north wall both sides of the roof-leader bump-out, the east wall, and the south-east return along grid H |
| p11 (A-200) | `EXT-1: 3-5/8"THK. STANDARD MODULAR BRICK VENEE...` | 163.6 SQ FT | purple/magenta | The brick band on the North and West elevations, from the cyan base line up to the underside of the rowlocks. The rowlock courses above it are not shaded |
| p11 | `3-1/4"THK. x 3-5/8"H HALF ROWLOCK BRICK` | 61.4 FT | brownish red | A line along the top of the band |
| p11 | `7-5/8"THK. x 3-5/8"H ROWLOCK SILL` | 61.5 FT | green | A line just above the red one |
| p12 (A-201) | `EXT-1: 3-5/8"THK. STANDARD MODULAR BRICK VEN...` | 232.1 SQ FT | purple/magenta | East and South elevations. The band is notched around the VAT / night-depository opening on the East elevation. **At the north (left) end of the East elevation the area runs ≈ 3.5 ft past the NE corner onto blank paper** (≈ 9.2 SF; trap 12) |
| p12 | `3-1/4"THK. x 3-5/8"H HALF ROWLOCK BRICK` | 87.9 FT | brownish red | as p11, plus the same ≈ 3.5 ft overshoot at the NE corner |
| p12 | `7-5/8"THK. x 3-5/8"H ROWLOCK SILL` | 88.3 FT | green | as p11, plus the same ≈ 3.5 ft overshoot at the NE corner |

The legend names are truncated by PlanSwift (`VENEE...`, `VEN...`). Match on `EXT-1:` and `BRICK`.
The `THRU WALL FLASHING` rows (101.6 / 111.5 FT, light cyan) on the same pages, and `ALUMINUM FLASHING`, `PRE-FINISHED ALUMINUM SILL` and `SEALANT W/ BACKER ROD`, belong to Div 07.

## 3. How each formula input is read

| Input | Read from | This job |
|---|---|---|
| CMU run LF | p03 mauve legend row | 157.4 FT (estimator carries 157.5, rounded up to 0.5) |
| CMU height | Legend name `@ 1'4"H`. Confirm it from A-430 det. 4 (2 CMU courses) or from stem-wall height − brick below grade: 2'-0" − 8" | 1'-4" = 1.33 ft (estimator) |
| CMU thickness | `4" CMU` (A-430, S-600). A-620 Table C gives 4 = 3-5/8" actual | 4" |
| Grout | `FULLY GROUTED` / `GROUT CAVITY SOLID UP TO GRADE` | solid, plus the cavity |
| Brick area per elevation | p11 / p12 purple legend rows | 163.6 + 232.1 SF |
| Unit size | Finish schedule `STANDARD MODULAR`; spec 2.2.C.6 `3-5/8 inches wide by 2-1/4 inches high by 7-5/8 inches long` | modular |
| Special-course LF | p11 / p12 red and green legend rows | 61.4 + 87.9; 61.5 + 88.3 |
| Course type | A-430 det. 4 labels | rowlock (half, recessed) + rowlock sill |
| Tie spacing | A-200/A-201 detail `BRICK CONTROL JOINT` (`BRICK TIES @ 32" O.C. HORIZ. & 16" O.C. VERT.`), A-430 det. 4 | 32" × 16". This conflicts with the spec; see trap 4 |
| Barrier product | A-310 / A-430 `FLUID-APPLIED VAPOR BARRIER`; spec 07 2726 (BOD Grace Perm-A-Barrier Liquid / VPL, ≥ 35 mils dry) | SF = brick SF |
| Weep spacing | A-310/A-430 `THRU-WALL FLASHING & WEEPS @ 24" O.C.`; spec 3.9.C.3 | 24" |

## 4. Cross-checks

- **Band height:** brick SF ÷ half-rowlock LF = 395.7 / 149.3 = 2.650 ft. The detail gives 12 courses = 2.667 ft. A ratio near 2.67 confirms that the area excludes the rowlocks. A ratio near 3.3 (2'-8" sill + 8" below grade) would mean the rowlocks were counted twice.
- **Course pairs:** the half rowlock and the rowlock sill always run together, so their LF should agree within a few feet (149.3 vs 149.8).
- **Plan vs elevation:** the CMU plan run (157.4) should be a few percent longer than the elevation course runs (149.3). The plan line goes through corners and below openings; the courses stop at storefront jambs. A gap above about 10% means a wall was missed on one view.
- **Barrier = brick SF** for the masonry section. The Div 07 barrier line (184, 2983.5 SF) must not include the brick zones as well.
- **Flashing** (Div 07 line 187 = 101.6 + 111.5 = 213.1 LF) is longer than the band (149.3). It also covers sill and head flashing at openings, so do not use it as the band length.

## 5. Traps hit on this job

1. **The brick is a wainscot band, not full-height veneer.** Most of each elevation is EIFS (yellow) and ACM (teal). Only the purple strip at the base is masonry.
2. **Field brick vs special courses.** The area must stop under the half rowlock. Measuring up to the 2'-8" sill datum and also taking the two rowlock LF counts the top ~8" twice. That is about 100 SF of extra brick area here (149.3 × 0.67).
3. **Brick goes 8" below F.F.E.** In the elevations the purple drops below the `F.F.E. 0'-0"` line to the cyan base flashing line. A takeoff that starts the brick at F.F.E. under-counts by about 25% (8" of 32").
4. **Tie spacing conflict.** The drawings say 32" horiz. × 16" vert. (3.56 SF per tie). Spec 04 2113 §3.6.A.5 says not more than 24" horiz. × 18" vert., with at least 1 anchor per 2 SF. TMS 402 allows 2.67 SF for wire ties. Ties for 400 SF: 113 by the drawings, 134 by the spec spacing, 200 by the spec's 1-per-2-SF rule, which governs. Spec §3.6.A.2 adds a third rule, "one anchor at each stud in each horizontal joint between sheathing boards", which can add anchors along the band; the sheathing joint layout is not drawn, so it has no count here. Raise an RFI. The estimate carries no tie count; the spacing is only in line 32's description.
5. **"Half rowlock" is a cut unit.** It is 3-1/4" deep, so each 7-5/8" brick gives two pieces after a saw cut (spec 3.2.B). Unit counts should be about half the full-rowlock count in whole brick, plus cutting.
6. **The CMU height is not dimensioned.** "1'-4"" appears only in the estimator's legend name. Derive it from 2 courses on A-430 det. 4, or from the 2'-0" stem-wall depth (02-concrete) minus 8" of brick below grade.
7. **The CMU is outboard of the concrete stem wall, not instead of it.** The 8" concrete stem wall (02-concrete line 27) runs the full perimeter. The 4" CMU sits on the same strip footing only under the brick. Do not deduct one from the other.
8. **Grout cavity.** "GROUT CAVITY SOLID UP TO GRADE" is grout between the CMU/brick and the stem wall. It is a real material quantity, but the estimate folds it into line 31's description and never quantifies it.
9. **Truncated legend names.** `VENEE...` / `VEN...`: get the full description from the finish schedule and spec, not from the legend.
10. **Similar strings in other trades.** "10 MIL VAPOR BARRIER" (under the slab, 02-concrete) and "FLUID-APPLIED VAPOR BARRIER" (behind the brick, line 35, and behind the EIFS, line 184) are three different scopes. "BRICK" also appears in toilet accessories (BOBRICK) and in demolition ("REMOVE EXISTING BRICK STAIR STEPS").
11. **S-600 names a shelf angle that A-430 does not show.** S-600 sections 1 and 2 print `SHELF ANGLE, FOR BRICK VENEER. AND WALL TIES BACK TO METAL STUD SEE ARCH.` at the top of the brick, under the punched window. A-430 det. 4 has no angle: the brick bears on the CMU and the rowlock sill caps it at 2'-8". No estimate line carries a brick shelf angle (Div 05 lines 67–69 are joist, deck-edge and roof-closure angles). Do not add a Div 05 shelf angle, or brick above the window, from S-600 alone. Raise it with the tie conflict (trap 4). The S-600 `1'-7"` is horizontal (stem wall face to footing edge), so it does not conflict with the 2'-0" stem wall.
12. **The p12 markup overshoots the NE corner.** The EXT-1 area and both rowlock lines run ≈ 3.5 ft past the north end of the East elevation onto blank paper (≈ 9.2 SF and ≈ 3.5 LF each). The clean A-201 shows nothing there. A strict takeoff from the drawing gives ≈ 386.5 SF, 145.8 LF and 146.3 LF. The estimator's legend values include the overshoot. The area ÷ LF ratio check (§4) does not catch it, because the area and the lines overshoot together; compare each run's ends with the drawn building corners.
