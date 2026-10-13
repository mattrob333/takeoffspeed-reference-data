# Reading guide: painting

How to read this job's plans and specs to get every painting input, with the actual strings on the sheets. It is written for an AI reader feeding the TakeoffSpeed engine.

## 1. Sheets to open, in order

1. **A-170 SCHEDULES**, group "PAINT" (and the CEILINGS group row `GWB-1 PAINTED GYP. … PT-3`, which ties painted gypsum ceilings to PT-3). This is a raster table with no text layer, so read it as an image (zoom ≥ 3). It is the tag dictionary: tag → TYPE (PAINT / PRIMER), MFR, MODEL, COLOR, REMARKS (sheen and notes). Write down every tag, including any that never appears on a plan (PT-2 appears only here and in note G).
2. **A-150 FINISH PLAN.** It gives which tag goes on which room and which wall, and its general notes give coats and sheens (G, J) and the Level 5 note (N).
3. **A-130 REFLECTED CEILING PLAN.** Ceiling tags (`PT-3` printed under the height), heights (`9' - 0"A.F.F.`), the exposed-ceiling rooms ("EXPOSED CEILING / ALL WALLS TO DECK"), soffits, and note E.
4. **Enlarged plans and elevations** that carry their own paint callouts: A-410 (restrooms, "PT-1, TYP" above tile), A-704 (tech wall PT-4 and PT-6), A-706 (booth PT-5).
5. **A-600 DOOR SCHEDULE.** The frame material per door type (only HM frames are painted).
6. **M-301 keynotes** (5 and 8, paint black) and **P-403 "PIPE PAINTING NOTE"**. MEP paint scope exists only in these notes.
7. **Spec 09 9110 PAINT SCHEDULE** (p328–329) for the system per substrate, and **09 9100** (p320–327) for rules: duct interiors black behind grilles, omit primer on shop-primed metal, prime-only behind fixed equipment. **08 1113** p214 says the frames ship primed, while 09 9110 still lists a primer system for HM frames (see trap 6).

## 2. Symbols and tags on this job

| What you see | Where | Meaning |
|---|---|---|
| Hexagon stack `PT-1 / WB-1 / FT-1` inside a room | A-150 | Room finishes: walls PT-1, base WB-1, floor FT-1. The wall tag applies to **every wall of the room** unless a wall-specific tag overrides it. |
| A single hexagon `PT-7` with two leader arrows to the ends of one wall | A-150 Meeting Room 105 north wall | A wall-specific override: only the wall between the two arrow tips. |
| `PT-8` with leaders to both ends of the west wall | A-150 Meeting Room 105 | West (window) wall is PT-8. |
| `PL-2 / PT-4` with leaders | A-150 Phone Room 114 north wall | That wall gets PL-2 (laminate) **and** PT-4 paint. The estimator measured 5.3 FT of PT-4 at 9'. |
| `PT-4 / PT-7` with leaders | A-150 Gathering Area 103 north wall | Tech wall: PT-4 (with PT-6 in the recess per A-704). The PT-7 half of the tag was not taken off. |
| `PT-3` under a height tag in a ceiling area | A-130 | Painted gypsum ceiling, paint tag PT-3. |
| Pale yellow "EXPOSED CEILING" areas | A-130 Janitor 115, Elec/IT 106 | Open to deck; walls go to structure. |
| `SOFFIT @ 5'9"H, GWB @ 2'6"H` (markup item names) | A-130 markup p05 | Soffit run at 5'-9" with a 2'-6" gypsum face. That face is painted PT-3. |
| "PT-1, TYP" / "(PT-1 )" | A-410 elevations | Walls above the 5'-6" tile band. |
| Hexagon keynote `5` beside an LSD diffuser | M-301 | "IN UPPER CEILING. PAINT BLACK." |
| Keynote `8` | M-301 | "LSR(3) WITH FULL SIZE SHEETMETAL PLENUM, 12" HIGH. INSIDE TO BE PAINTED FLAT BLACK." |

## 3. Reading each formula input

| Input | Read it from | This job's strings / values |
|---|---|---|
| Paint tag per wall | A-150 room stack, then wall overrides | default `PT-1`; overrides `PT-4`, `PT-7`, `PT-8`, `PT-6` (A-704 only) |
| Run LF per wall face | the finish plan, one face per room; scaled or dimensioned from A-120 | markup legends `PT1 PAINT @ 9'H 117.1 FT` and others (p08) |
| Painted height per run | the RCP height of the room: `12' - 0"A.F.F.`, `11' - 0"A.F.F.`, `10' - 0"A.F.F.`, `9' - 0"A.F.F.`, `8' - 6"A.F.F.`, `6' - 6"A.F.F.`; exposed rooms → partition height to structure | 12'-6" ("ALL WALLS TO DECK"; the same height the framing takeoff uses) |
| Elevation-traced areas | A-410 elevation A full height less the door, B–D above the tile band; A-704 recess | `PT1 WALL PAINT 252.6 SQ FT` (both restrooms; the estimator's copy of A keeps the door, about 23 SF); `PT6 37.2 SQ FT` |
| Gypsum ceiling area | A-130 painted-gyp areas tagged PT-3 | `5/8" GWB CEILING O/ 3-5/8" METAL STUD FRAMING (PT3) 516.1 SQ FT` |
| Soffit faces | A-130 soffit rows: LF × GWB face height ("BS" = both sides) | 4.2 @ 2 × 3.5; 2.7 @ 4; 6.7 @ 1.5; 30.5 @ 3; 35.3 @ 2.5; 28.1 @ 2 → 286.2 SF |
| Exposed structure | A-130 exposed-ceiling plan area | `EXPOSED STRUCTURE 98.4 SQ FT` |
| Booth roof | A-706 detail 2 BOOTH ROOF FRAMING PLAN | `PT5 FINISH @ BOOTH ROOF 76.2 SQ FT` |
| Painted frames | A-600 door types whose frame is HM | `TYPE B … W/ WELDED HOLLOW METAL FRAME` 3 + 2; `TYPE C … W/ KNOCK-DOWN HOLLOW METAL FRAME` 1 |
| Painted devices | M-301 keynote tags 5 and 8 | 4 + 1 |
| Painted pipe LF by size | P-303 roof plan gas runs, limited by the P-403 note | `3/4"DIA GAS PIPE 44.2 FT`, `1"DIA GAS PIPE 9.7 FT` |
| Coats | A-150 note G / J "ONE COAT PRIMER, TWO COATS PAINT"; A-170 TYPE column; 09 9110 | 1P + 2C on walls and ceilings; PT-7 = primer only; HM frames shop-primed (field primer carried by convention, flag it) |
| Sheen | A-170 REMARKS, then A-150 note G | PT-1 eggshell, PT-2 semi-gloss, PT-3 flat, PT-5 semi-gloss, PT-6 eggshell (A-704: flat black) |

## 4. Cross-checks that caught real issues

- **Paint runs against the base.** WB-1 is 404.7 FT. Paint runs (PT-1 339.1 + PT-4 15.9 + PT-7 10.3 + PT-8 7.4) plus WC-1 10.1 and FRP-1 4.0 total 386.8 FT. That is close, which is a reasonable sign that every room face was covered once. The 18 FT gap fits base running along casework and short returns.
- **Pipe paint row against pipe rows.** `SAFETY YELLOW PAINT AT ROOD GAS PIPE` 53.9 = 44.2 + 9.7. The paint scope equals the roof gas pipe exactly, and the P-301 underground and interior 1" natural gas pipe (18.6 FT) is correctly left unpainted.
- **Ceiling paint against board.** PT-3 802 = ceiling board 516.0 (line 278) + soffit board 286.04 (line 285). If the painting total and the board total disagree, one of them is missing a surface.
- **Frames against the door lines.** 6 = lines 191 (3) + 192 (2) + 193 (1). The storefront doors (194–196) and the Type F slider (190) are aluminium and stay out.
- **Areas sharing one value.** A-704 carries `PT6`, `TYPE X GWB` and `5/8" PLYWOOD BACKING` at 37.2 SF each. Three trades read the same recess area.

## 5. Traps

1. **Tag conflicts between sheets.**
   - A-130 note E says "ALL GYPSUM BOARD CEILING PAINTED … ARE TO BE PT-1", while the same sheet tags the ceilings `PT-3`, A-170 defines PT-3 as FLAT, and the A-170 FINISHES SCHEDULE CEILINGS group has the row `GWB-1 | PAINTED GYP. | - | - | - | PT-3`, which assigns PT-3 to painted gypsum ceilings outright. Two schedule sources (the RCP tags and the GWB-1 row), plus note G "ALL CEILINGS TO BE FLAT", outweigh the one general note, so take PT-3, as the estimator did. Log an RFI to close note E, but the schedule supports PT-3.
   - PT-5 is "SEMI-GLOSS" on A-170, but line 302 says "EGGSHELL".
   - PT-6 is "EGGSHELL" on A-170, but A-704 says "FLAT BLACK".
2. **A primer tag that looks like paint.** PT-7 TYPE = PRIMER (Roman Pro-999, dries clear) under an owner-supplied wallcovering. It takes one coat and no finish coats. The estimate wrote "one coat of primer with two coats of paint".
3. **Double tags.** The Gathering Area 103 north wall reads `PT-4 / PT-7`, and only the PT-4 part was carried. On the tech wall, PT-6 (the recess back) sits inside the PT-4 run, so subtract it from PT-4 or you count it twice. The recess returns are PT-4 ("PAINT RECESS RETURNS ALL SIDES"). The estimator's 10.6 FT run already steps around the recess on the markup (front, both side returns, back; it is 0.8 ft longer than the 9'-9 3/4" wall on A-704 detail 4), so the side returns are in at the shallow depth drawn on A-150. Only the head and sill returns (2 × 7'-9 3/4" × 9 1/2" = 12.4 SF) are missing. Check the trace before adding returns, or you count the sides twice.
4. **Exposed rooms change the height.** Janitor 115 and Elec/IT 106 have no ceiling height tag. Their walls are painted to structure: 12'-6", the partition height, not any RCP number.
5. **Soffit item names hold two heights.** In `SOFFIT @ 4'6"H, GWB @ 3'H`, the first number is the soffit elevation and the second is the gypsum face. Paint takes the face. `GWB BS` doubles it.
6. **Shop-primed frames.** Frames ship shop-primed (08 1113 p214 "Exposed Finish: Prime"). 09 9100 3.3.B.2 ("Omit primer on metal surfaces that have been shop primed and touchup painted") lets the field primer be touch-up only, but p320 says this section's priming is in addition to shop priming and 09 9110 p328 still lists a primer system for "Hollow Metal Frames and Doors" (SW ProCryl B66-1310 / BM V131 / PPG Pitt Tech). Count the frames, carry the primer as a contractor convention (the estimator's 1P + 2C is defensible), and flag it.
7. **MEP paint scope lives in notes, not legends.** No legend or schedule lists painted diffusers or pipe. Only M-301 keynotes 5 and 8 and the P-403 pipe note do. Spec 09 9100 3.3.A.6 adds duct interiors visible through grilles (flat black), which nobody carried.
8. **The opening-trim line is an assumption.** No sheet shows paint-grade casing. Line 304 copies the 910 LF "ASSUMED" carpentry line. Do not reproduce it as measured.
9. **Raster markups.** The PlanSwift pages are images. The paint runs sit under coloured room fills of the same palette, so a colour mask cannot separate runs from fills. Use the legend totals, and use the heights in the item names.
10. **Small lines are rounded up.** If you compare raw legend values with the estimate, PT-6 is −7%. That gap is the estimator's rounding up to 5 (formulas F9), not a measurement error.
