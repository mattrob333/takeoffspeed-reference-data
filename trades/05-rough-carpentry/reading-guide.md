# Reading guide: rough carpentry on this job

## 1. Where each input lives

| Input | Read it from | Strings on this job |
|---|---|---|
| Exterior wall runs and heights | A-120 markup legend (p4). Each row is `type @ height` | `EXT 8" STUD WALL @ 12'9"H`, `@ 15'9"H`, `@ 15'9"H NO GWB`, `@ 4'H`, `EXT 6" STUD WALL @ 12'3"H SHTNG 10'3"H`, `PARAPET WALL @ 7'2"H A310`, `6" & 3-5/8" METAL STUD @ 18'8"H, BS 1/2" SHTNG ONLY` |
| Parapet face above the deck | A-140 legend (p7) | `PARAPET WALL @ 1'7"H` 46.0, `@ 2'7"H` 38.0, `@ 4'7"H` 96.6. The parapet tops are 17'-4" (low) and 18'-8" (high): 12'9" + 4'7" = 17'4", and 15'9" + 1'7" = 17'4" |
| Sheathing thickness by wall | Wall sections A-310 / A-311 / A-300 and roof details A-450 | "1/2" EXTERIOR SHEATHING" (8" walls, wing walls, step wall); "5/8" EXTERIOR SHEATHING" (A-311 sec. 1, the brick knee wall below the storefront sill, 2'-8" high; the 12'-8 1/4" markup on that section is the measured F.F.E.-to-deck wall height, not a sheathing height); "COMPATIBLE 1/2" GLASS-MAT SHEATHING" (parapet roof side, which is 09a's line, not this trade) |
| Roof plywood | A-140 ROOF TYPES block | RT2: "SINGLE-PLY ROOF MEMBRANE / POLYISO BOARD … TAPERED TO DRAIN / 5/8" PLYWOOD". RT1 sits on steel deck with no plywood. Area = legend `RT2 ROOFING` 285.4 SF |
| Canopy plywood | A-430 det. 10 and det. 7 | "PLYWOOD DECK ON METAL FRAMING INFILL" (soffit), "EXTERIOR SHEATHING" (fascia). Det. 10 dimensions the ACM profiles (1'-0" edge depth = 1" + 10" + 1"; 6" ACM soffit profile), not the sheathing; the only sheathing it dimensions is two 5/8" decks (top under RT-2, bottom above the ACM soffit) and the vertical fascia sheathing is undimensioned. Soffit area = A-130 legend `ACM-3 … CANOPY - 10/A430` 358.7 SF. Edge = A-140 `CANOPY EDGE 7/A430` 138.5 FT |
| Nailer sizes | A-450 det. 1, 6, 8, 9, 10; A-430 det. 3 | "2 X 4 P.T. WOOD NAILER" (curb), "2X P.T. WOOD NAILER" (coping), "2x P.T. WOOD BLOCKING" (roof transition), "BRAKE METAL OVER 1X BLOCKING", "P.T. WOOD BLOCKING" (wing wall) |
| Nailer runs | A-140 legend | `COPING 6/A450` 148.1, `COPING 9/A450` 38.5, `COPING 3/A430` 13.9, `8/A450 LAP ROOF 2', INCL WALL` 45.3, `CURB - 1/A450` 39.9 |
| Casework blocking | A-700 to A-707 legends | A leading `(n)` is the row count: `(7) 1x4 FIRE RETARDANT TREATED BLOCKING` 8.6, `(2) 1x4 WOOD BLOCKING FRAMING` 14.6 / 23.3, `(4) 1x4 …` 9.8, `(2) 1x4 BLOCKING` 15.7, `(5) 2x4 WOOD BLOCKING FRAMING` 1.6, `(3) 2x4 BLOCKING` 8.7 |
| Treatment | A-110 general note F; A-620 note M; spec 06 10 53 | "ALL WOOD BLOCKING, BRIDGING, BRACING, FRAMING, ETC., SHALL BE FIRE RETARDANT TREATED"; "INSTALL FIRE RETARDANT, TREATED BLOCKING IN PARTITIONS AS REQD". Roof members are P.T. (06 10 53 p124: nailers and blocking "in connection with roofing, flashing") |
| Plywood backing | A-700 to A-704 legends | `3/4" PLYWOOD @ 7.67H` (the height is in the name), `(2) 3/4" PLYWOOD @ 1'4"H`, `3/4" PLYWOOD @ 8"H`, `3/4" PLYWOOD` (SF), `1/2" PLYWOOD @ 3'9"H`, `5/8" PLYWOOD BACKING` (SF) |
| IT backboard | E-702 legend and keynote; A-110 keynote P15 | "PROVIDE 8' X (LENGTH AS REQUIRED) X 3/4" FIRE-RATED PLYWOOD BACKBOARDS MOUNTED VERTICALLY ALONG ALL NER ROOM WALLS"; legend 215.3 SF |
| Booth | A-706 legend; det. 2, 9, 11 | `WALL 706` 15.9 FT; booth roof 76.2 SF; "TOP OF BOOTH FRAMING w/ 3/4" PLYWOOD & PAINTED PT-5"; det. 9 build-up 3/4" laminate / 1/4" clip / 1/2" plywood / 6" stud / 1/2" / 1/4 / 3/4 |
| Night-depository blocking | A-201 east elevation markup | `2x6 BLOCKING` 8.8 FT, the purple outline round the depository opening |

## 2. How to read the legend grammar

- **`@ h` is the height multiplier.** `SHTNG h` overrides the wall height for sheathing. `BS` means both sides, and `1 SIDE` means one face.
- **A leading `(n)` is a row or ply count.** Multiply the LF by n. This is the biggest blocking trap: the A-701 row reads 8.6 FT, but it is 60.2 LF.
- **A detail call in the name names the detail that sizes the member.** `COPING 9/A450` means read A-450 det. 9 for the nailer stack. One run can produce several lines (det. 9 yields 2x14 and 1x6; det. 8/10 yields 2x4 and 2x6).
- **Some names say nothing.** Generic rows such as `Linear`, `5`, `7` and `9` belong to millwork, not carpentry. `NO` (NAN EA) on A-704 has no quantity.

## 3. Sizing nailers from a detail (when the size is not printed)

The details print "2X" or "1X" without a width. The width comes from the drawn member against the wall build-up. All of these details are drawn at **nominal** size:

- **6/A450 (3"=1'):** the member is ~2" × ~10" over the 8" stud, 1/2" sheathing and insulation. That makes it a **2x10**.
- **9/A450:** an upper member ~1.5" × ~14", which is a **2x14**. Below it, a ~1" × ~5" member, which is a **1x6** under the brake metal. A thin hatched layer sits on top.
- **8/A450 + 10/A450:** two blocks on the 3-5/8" step wall. The lower block is stud-width, a **2x4**. The upper spans stud, sheathing and insulation (~6.3"), a **2x6**.
- **3/A430:** the blocking spans the 1'-8" wing wall under a 2'-0" coping. The estimator carried **2x16**.

## 4. Cross-checks

- **Wall LF against parapet LF.** A-140 parapets total 180.6 LF. The coping runs total 200.5 LF (6/A450 + 9/A450 + 3/A430). The coping is longer because it also caps the wing walls and the VAT wall.
- **Backboard.** E-702 gives 215.33 SF, which is 26.92 LF × 8'. The A-110 plan trace `PLYWOOD @ 8'H` gives 32.5 LF × 8' = 260 SF (+20.8%). The estimator trusted the elevations. Use the elevation net, not the room perimeter, when both exist.
- **Tech wall.** A-704 has three rows of 37.2 SF on the same polygon: 5/8" plywood, Type X GWB and PT6. They should match.
- **Booth.** The PL-1 wall laminate is 296.9 SF (millwork line 142, 300). If 1/2" plywood is behind all of it, line 81 should be ~286 SF, not 47.7. Flag it.
- **Blocking.** Σ(n × LF) over every A-700-series blocking row (240.7) equals the 1x4 line (240.66). Check this before deciding the 2x4 rows are missing.

## 5. Traps hit on this job

1. **The `(n)` multiplier.** The raw legend LF of the casework blocking is 82.3 LF. The estimator's quantity is 240.66 LF.
2. **Sizes folded into one line.** The 2x4 rows were carried in the 1x4 FRT line, so an AI that splits them perfectly will look −14% on line 89 and +34 LF on 2x4.
3. **No opening deduction on exterior sheathing.** The storefront runs are taken at full height through the glass. An engine that deducts the ~889 SF of exterior glazing and doors (A-610 + A-600) comes out ~29% low against this estimator.
4. **Double-face wing walls.** The `BS 1/2" SHTNG ONLY` row needs faces = 2 (313.6 SF). With one face the line falls 5.1% short.
5. **The parapet roof face is glass-mat, not plywood.** Do not double the parapet rows here (09a carries 658 SF of glass-mat).
6. **Unreconciled 5/8" wall sheathing (line 83).** The A-200 `5/8" PLYWOOD SHEATHING` rectangle (52.1 SF) is drawn off the elevation, so its location is unknown. Ask, or flag it. Do not invent a location. The best-supported 5/8" wall is the A-311 knee wall below the storefront sill (2'-8"), which implies a 61.12 LF run (close to the A-200 half-rowlock 61.4 / rowlock-sill 61.5 FT rows), but no sheathing row measures it. Do not multiply a run by the 12'-8 1/4" markup: that is the measured F.F.E.-to-deck height of the 12'-9" wall.
7. **A wrong drawing reference.** Line 81 cites "S111-S131", sheets that do not exist in this set. The legend that matches is on A-706.
8. **Rounding is per section, not global.** BACKING rounds up to 5 SF. A-140 blocking is rounded by hand. Sheathing and FRT blocking keep their unrounded PlanSwift values.
9. **Penetration blocking is missing.** A-140 note 4 requires "PRESSURE TREATED 2x6 BLOCKING AT INSULATION AROUND ENTIRE PERIMETER" of every penetration, and CURB 1/A450 is 39.9 LF. No line carries it unless lines 91/92 were meant to (their 46 LF matches 8/A450, not the curbs). Report it as a gap, not a quantity.
10. **"ASSUMED" lines.** The 910 LF of trim has no drawing source. Keep it as an allowance with low confidence, and never present it as measured.
