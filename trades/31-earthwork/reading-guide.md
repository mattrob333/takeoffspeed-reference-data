# Reading guide — 31 earthwork

How to read this job's plans and specs for footing excavation, backfill, haul-off and grading
cut/fill. Every string below is quoted as printed.

## 1. Where the inputs are

| Input | Sheet / page | What to read |
|---|---|---|
| Footing marks and counts | S-201 plan, markup p33 legend | Plan tags `F30`, `F38`, `F50`, `F60`, `F70`, `F7040`, `F10050`, each with its top-of-footing bracket, e.g. `[-2' - 0"]` above `F50` |
| Footing sizes | S-201 `SPREAD FOOTING SCHEDULE` (MARK / LENGTH / WIDTH / THICKNESS / … / COUNT) | e.g. `F38  3' - 8"  3' - 8"  1' - 0"  5 #4 EA. WAY  3`; `F7040  4' - 0"  7' - 0"  1' - 4"`; `F10050  5' - 0"  10' - 0"  1' - 2"` |
| Wall footing | S-201 `WALL FOOTING SCHEDULE` | `WF20  2' - 0"  1' - 0"  2 #6`. Plan tags `WF20` / `[-2' - 0"]` |
| Wall footing length | p33 legend row `WF20` | `124.2 FT` (periwinkle). Drawn between the dashed spread-footing outlines |
| Stem walls | p33 legend | `8"THK. CONCRETE STEM WALL W/ #4 BARS @ 10" O.C & #4 DOWEL BAR @ 18" O.C @ 2'H` 193.8 FT; `10"THK. CONCRETE STEM WALL W/ #4 BARS @ 10" O.C @ 2'H` 8.4 FT |
| Footing depth | S-201 FOUNDATION PLAN NOTES | "UNLESS NOTED OTHERWISE ON PLANS, TOP OF FOOTINGS AT ALL EXTERIOR FOOTINGS SHALL BE [-2'-0"] BELOW FINISH FLOOR SLAB." The same note covers interior footings. "NUMBER INSIDE OF BRACKETS INDICATES TOP OF FOOTING ELEVATION" |
| Footing section | S-600 sections 1–6 | WF20 under an 8" stem, `#4 CONT. @ 10" o.c. MAX.`, `4" CMU BELOW GRADE.`, `FOR SLAB SUBGRADE SEE GEOTECH. REPORT` |
| Backfill rule | S-201 note | "MAXIMUM EARTH DIFFERENTIAL WHEN BACKFILLING SHOULD NOT EXCEED 2'-0"" |
| Existing / proposed surfaces | C-4.0, markup p73 legend | 14 rows (6 existing, 8 proposed; `439.500 - Proposed` appears twice, 498.8 and 3841.3 SQ FT — keep both), `E` or `P` icon, e.g. `438.500 - Existing 16957.7 SQ FT`, `440.000 - Proposed 20233.7 SQ FT`, `435.000 - Proposed 967.6 SQ FT` |
| Cut / fill volumes | markup p92 `Earthwork Pro Summary` / `WATSON BLVD - SITE` / `C-4.0-GRADING-PLAN-Rev.0` | Columns `Name`, `Cut Total`, `Fill Total`, `Qty`. Rows `440 - Proposed Contour` … `435 - Proposed Contour`. Totals `634.41 CU YD`, `786.25 CU YD`, `151.84 CU YD` |
| Cut/fill picture | markup p91 (C-4.0) | Red hatch = cut, blue hatch = fill, tan = border/existing-only. No legend |
| Grading rules | C-0.1 general notes; C-4.0 GENERAL GRADING NOTES | "ALL CUT OR FILL SLOPES SHALL BE 2:1 OR FLATTER"; "ALL PROPOSED CONTOURS AND SPOT ELEVATIONS REFLECT FINISHED GRADES"; "THE PROPOSED CONTOURS SHOWN IN DRIVES AND PARKING LOTS AND SIDEWALKS ARE FINISHED ELEVATIONS INCLUDING PAVEMENT"; "ALL UNSURFACED AREAS DISTURBED BY GRADING OPERATION SHALL RECEIVE 4 INCHES OF TOPSOIL"; `FFE:441.00` |
| Pond | C-4.2 | `BOTTOM OF INFILTRATION BASIN: 435.00`, `RIM ELEVATION = 436.5`, `TOP OF DAM = 438.25`, `SLOPES TO BE MAXIMUM 3:1`, `BOTTOM OF GRAVEL: 429.5` |
| Soils, compaction | Terracon report (`source/drawings/GeoTechnical/_70 …pdf`, PDF pp. 13–21) | Stripping, proofroll, 98% / 95% / 92% std. Proctor, 8" loose lifts, embedment 18" exterior / 12" interior. No shrink factor |

There is no Division 31 earthwork specification. The spec TOC (p. 9) lists only
`31 3116 Termite Control` and "Geotechnical Report N/A". 03 3000 §3.2 (spec p. 58) sets a back
slope of 1:1.5 for excavations over 5 ft.

## 2. How each formula input is read

1. **Count per spread mark.** Use the p33 legend EA rows, and check them against the schedule's
   COUNT column. Both read: F30 3, F38 3, F50 6, F60 1, F70 1, F7040 1, F10050 1, which is 16
   pads. The legend row `New Count 2 EA` (green) is an unnamed extra. Its two green dots sit on
   the STEEL COLUMN SCHEDULE (A-2.9, C-7), not on footings.
2. **L, W, T.** Read these from the schedule. Convert feet-inches exactly: 3'-8" = 3.6667,
   1'-2" = 1.1667, 1'-4" = 1.3333. F7040 is printed LENGTH 4'-0", WIDTH 7'-0"; the area is the
   same either way.
3. **WF20 length.** Take the measured 124.2 FT run. It is *not* the building perimeter (≈202 ft),
   because the wall footing stops at each spread-footing outline.
4. **Stem walls.** Take both stem rows: 202.2 FT in total. They run the full perimeter, over the
   WF20 and over the perimeter pads, and their height is "@ 2'H" (top of footing −2'-0" up to
   the slab).
5. **Depth.** Depth = bracket value + footing T: 2 + 1 = 3.0 ft for WF20, F30 and F38; 3.1667 ft
   for F50 and F10050; 3.3333 ft for F60, F70 and F7040.
6. **Working space.** This is the estimator's convention, not printed anywhere: 1'-0" each side of
   the trench and 6" each side of a pad. See `formulas.md` §1.
7. **Grading rows.** Read all 14 rows of p92 in order. Keep the duplicate elevations (six
   `440 - Proposed Contour` rows are six separate regions). A cell printed as just ` CU YD` is 0.
   The `Qty` column is signed fill − cut, so negative means net cut. Read the totals line once:
   it is printed twice, once underlined and once on the `Totals` row.

## 3. Cross-checks

| Check | This job |
|---|---|
| Haul-off = concrete placed below FF (footings + stem walls) | 36.1 vs 25.9258 + 10.1507 = 36.0765 ✓ |
| Backfill = excavation − haul | 119.8 − 36.1 = 83.7 ✓ |
| Each p92 row: Qty = Fill − Cut | 14 of 14 ✓ |
| Σ rows = printed totals | 634.41 / 786.25 / 151.84 ✓ |
| Pond regions vs C-3.0 keynote 23 area | 967.6 + 2,167.8 = 3,135.4 SF vs 3,074 SF (2% apart) |
| Implied existing elevation under each region (formulas.md §4) | 438.55–439.61, inside the 437.5–441.0 existing rows ✓ |
| Estimate line 708 note | "POND EARTHWORK HAS BEEN ADDED TO THE GRADING QUANTITY" ✓ (435 and 436.5 regions) |
| Same estimator's dumpster footing (line 665) | 1' working space each side, depth = T + wall below grade: the same convention as WF20 ✓ |

## 4. Traps

1. **Do not use the stem LF for the trench, or the WF LF for the stem.** WF20 is 124.2 FT and the
   stem walls are 202.2 FT. Excavation uses WF20 plus the pads; backfill deducts all 202.2 FT of
   stem.
2. **Working space differs between trench and pad.** One working-space value for both would give
   143.14 CY (1' everywhere, +19.5%) or 105.96 CY (6" everywhere, −11.6%).
3. **The depth datum is finish floor, not grade.** The brackets are top of footing below FF. One
   F38 is tagged `[-1' - 0"]`. The estimator dug it at −2'-0" like the rest; honouring the tag
   gives 118.95 CY (−0.7%).
4. **Digging from FF overstates soil excavation.**
   - The top 8" of every dig (4" slab + 4" gravel) is not soil. That is 1,045.13 SF of excavated
     plan × 8" = 25.81 CY.
   - The grading model also brings the building area only to the 440 region, 1 ft below FFE
     441.00. The 441→440 slice of the footing dig (38.71 CY) is therefore above the graded pad.
   - The estimator accepted both. The app should flag them, not copy them silently.
5. **The grading is to finished grade.** The notes say the contours "ARE FINISHED ELEVATIONS
   INCLUDING PAVEMENT". The Earthwork Pro regions were drawn at those elevations, so no pavement
   box-out is in 639/640. With the estimate's own assumed sections, the box-out alone is about
   881 CY:
   - heavy-duty asphalt 11,367.3 SF × 20.5" = 719.23 CY;
   - standard asphalt 2,459.18 SF × 16.5" = 125.24 CY;
   - 6" concrete pavement 748 SF = 13.85 CY;
   - 4" sidewalk 1,835 SF = 22.65 CY.

   The building slab and gravel (1,917.6 SF × 8") add 47.35 CY. Allowing for the box-out would
   swing the plain balance from +151.84 import to about 729 CY of export before subbase import.
   This is the single largest earthwork judgement on the job. Topsoil stripping (C-0.1: 4"
   topsoil on disturbed unsurfaced areas; Terracon: strip building and parking areas) is not
   taken off either.
6. **Stone storage under the pond is not excavated.** Line 711 carries 626.185 CY of stone
   (3,074 SF × 5.5 ft, from 435.00 down to 429.5). The grading cut stops at 435.00, and no line
   excavates or hauls that 626 CY of soil. It is a cross-trade gap, not part of these 6 lines.
7. **There is no shrink or swell.** Net fill 151.84 is plain fill − cut, and haul-off is bank CY.
   The geotech gives no factor. Do not add one when matching this estimate. Show it as a
   separate, labelled judgement.
8. **p91 has no legend.** The hatch colours carry no names. The numbers are on p92 only, and p92
   is a PlanSwift report with a text layer, so read the text, not pixels.
9. **Do not double count site earthwork.** Sign, bollard, light-pole and bike-rack piers, the
   dumpster footing and the pipe trenches have their own EXCAVATION / BACKFILL / HAULOFF lines
   in the 32b and 33 trades. Lines 629–631 are the building foundation (S-201) only.
