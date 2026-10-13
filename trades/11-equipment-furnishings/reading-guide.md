# Reading guide — appliances, equipment, shades, furniture

## 1. Sheets to open, in order

1. **A-110 FLOOR PLAN, general notes and keynotes.** These set responsibility before you count anything.
   - D: "BANK EQUIPMENT TO BE SUPPLIED AND INSTALLED BY VENDOR"
   - K: "FURNITURE AND MILLWORK TO BE PROVIDED BY OWNER VENDOR. G.C. TO COORDINATE LOCATION OF BLOCKING, PLUMBING, ELECTRICAL…"
   - unlettered: "APPLIANCES PROVIDED AND INSTALLED BY G.C. U.N.O"
   - keynote P9: REMOTE TELLER TERMINAL
   - keynote P14: LOCATION OF MOOD MEDIA AND MECHOSHADE CONTROLS

   The notes block prints the letters A…R in one column and the note text in another (in the text layer they come out as two separate lists). Note K is the 11th text entry.
2. **A-170 SCHEDULES.** There are four tables. None has a QTY column, so every quantity comes from plan counts or from the F2 convention.
   - APPLIANCE SCHEDULE: ITEM # / DESCRIPTION / MFR / MODEL # / PROV. BY / INST. BY / LOCATION / COMMENTS.
   - BANK EQUIPMENT SCHEDULE: same columns, every row VENDOR / VENDOR.
   - FURNITURE SCHEDULE: ITEM # / DESCRIPTION / MANUFACTURER / DIMENSIONS / MODEL / COLOR. There are 59 rows, from CH-01 to WS-02.
   - FINISHES SCHEDULE: row `MECHO | MOTORIZED MECHOSHADE | MECHOSHADE | THERMOVEIL DENSE BASKET WEAVE 1300 SERIES | 1319: SILVER BIRCH | 5% OPEN…`.

   The sheet has almost no text layer (844 characters, just the table titles), so the schedules must be read from the image. Render crops at zoom 3, for example `render.py sheet A-170 out.png 0.09 0.37 0.52 0.66 3`.
3. **A-160 FURNITURE & EQUIPMENT PLAN** (1/4" = 1'-0"). Tags are printed as text, such as `CH-04` or `TB-04A`, so a regex count over `text/A-160.txt` gives the plan count: `[A-Z]{2}-\d{2}[A-Z]?`. On this job that count equals the PlanSwift legend on markup p9 for every tag the estimator marked.
4. **A-130 RCP.** The LEGEND - RCP symbol "MOTORIZED MECHOSHADE" is a long thin rectangle drawn on the interior face of the glazing. Also read keynote CP4, general note G, and the ceiling height tags (`12' - 0"A.F.F.`, `ACT-1`), which give the drop context at each run.
5. **A-630 details 6/7, A-311 / A-310 sections, A-430 detail 9.** These show the pocket, the storefront head and the sill (2'-8" where there is a knee wall). They give the real drop. A-311 has two heads: section 1, WALL SECTION AT STOREFRONT, dimensions SILL 2'-8" + 5'-5" + 1'-11" = 10'-0" (T.O. LOW PARAPET 17'-4" − 7'-4" checks it); section 3, WALL SECTION AT ENTRY VESTIBULE, prints T.O. STOREFRONT 12'-0". Read the section titles; do not apply the 12'-0" vestibule head to every run.
6. **A-705 / A-704 enlarged elevations.** These show where appliance and AV tags sit inside casework. Use them to confirm placements the plan doesn't show.

## 2. How each formula input is read on this job

| Input | Where | Actual string |
|---|---|---|
| Appliance tag in scope | A-170 Appliance Schedule, INST. BY column = GC | `AE-01 MICROWAVE DRAWER SHARP SMD3070ASY GC GC EMPLOYEE LOUNGE` … `AE-07 COFFEE MAKER KEURIG K4500 VENDOR GC SERVICE` |
| Appliance placements | A-160 bubbles / p9 legend | `AE02 1.0 EA`, `AE03 1.0 EA`, `AE04 1.0 EA`, `AE06 1.0 EA`, `AE07 1.0 EA`; AE-01 absent |
| Remote teller terminal | A-110 keynote P9 / p3 legend | `REMOTE TELLER TERMINAL 1.0 EA` |
| Furniture tag list | A-170 Furniture Schedule ITEM # | `CH-01` … `WS-02` (59 rows), including `SS-05 TBD TBD` and `TB-08 CHECK WRITING STAND MILLWORKER … SEE SHEET A-708 FOR DETAILS` |
| Furniture placements | A-160 / p9 legend | `SS01 2.0`, `TB01 1.0`, `CH01 2.0`, `CH11 4.0`, `CH02 2.0`, `TB02 2.0`, `PL02 2.0`, `SS03 1.0`, `CH06 2.0`, `CH10 2.0`, `CH03 2.0`, `TB04A 1.0`, `CH04 3.0`, `WS01 1.0`, `CH07 1.0`, `ST02? 1.0`, `CH08 1.0` |
| Furniture line text | A-170 DESCRIPTION + DIMENSIONS | `LAVA - CH-04 SIZE: 27.25"W X 22"D X 33.25"-37.25"H X 17.75-22"SH` (seven lines deviate from the schedule; see trap 11) |
| Unsuffixed plan tag | A-160 bubble `SS-03` on one sofa symbol; A-170 rows SS-03A 66.5"W and SS-03B 95.75"W | drawn sofa 95.5 in wide x 33.3 in deep, three seat cushions → SS-03B |
| Shade run LF | p5 legend | `MOTORIZED MECHOSHADE 74.0 FT` (red swatch, linear icon) |
| Shade drop | estimator: 16 ft (not printed). Drawings: ceiling tags at each run (10'-0", 11'-0", 12'-0"), storefront head 10'-0" (A-311 section 1) or 12'-0" (section 3, entry vestibule), SILL 2'-8" | `2' - 8"`, `5'-5"`, `1'-11"`, `7'-4"`, `T.O. LOW PARAPET 17' - 4"` (section 1); `T.O. STOREFRONT 12' - 0"` (section 3) |
| Shade product | A-170 MECHO row + spec 12 2413 2.3 B | `ThermoVeil 1300`, `5 percent`, `16.8 oz./sq. yd.` |

## 3. Cross-checks

- **Legend count vs text-layer count (A-160).** Counting every tag string in the A-160 text layer agrees with every p9 legend row: CH-01 2, CH-02 2, CH-03 2, CH-04 3, CH-06 2, CH-07 1, CH-08 1, CH-10 2, CH-11 4, PL-02 2, SS-01 2, SS-03 1, ST-02 1, TB-01 1, TB-02 2, TB-04A 1, WS-01 1, and AE-02/03/04/06/07 1 each. The text layer also has TB-05B 1, AE-09 1, AE-10 1, AE-13 1, BE-06 1 and BE-10 2. The estimator either has no legend row for these or excluded them as vendor scope.
- **Shade LF vs storefront widths.** The eight traced runs total 73.76 LF against 74.0 on the legend. Each run is one storefront bay: Relaxed Seating east is 4'-6" + 4'-4" + 4'-6" = 13'-4", traced 13.36.
- **Schedule highlights vs lines.** The green highlights on p10 (AE-01…AE-07) are exactly the six appliance lines. The MS-03 highlight is carried at 1 EA like every other unplaced row.
- **Shade LF in the description vs SF.** "(75 LF)" is the run rounded up. SF / LF should equal the drop you believe. Here it is 16.0, which is a red flag against storefront heads of 10'-0" (A-311 section 1) and 12'-0" (section 3).

## 4. Traps

1. **The schedules have no QTY column.** Do not invent schedule quantities. The quantity is the plan count, or 1 EA V.I.F. if the tag is not placed.
2. **The A-160 title says FURNITURE & EQUIPMENT, but the plan also tags vendor items:** AE-09 tech wall display, AE-10 TV, AE-13 security monitor, BE-06 phone, BE-10 VAT tube. The estimator left all of them out because the schedule says VENDOR / VENDOR. Read the INST. BY column, not the sheet title.
3. **AE-01 is on the schedule but not on any plan or elevation** (A-705 shows only AE-02 MICROWAVE). It is still carried as 1 EA. A placement-only counter misses it.
4. **The unsuffixed SS-03 on the plan has two candidate schedule rows, SS-03A and SS-03B.** Measure the symbol: the one sofa under the bubble is a three-seat piece 95.5 in wide, so it is SS-03B (95.75 in). SS-03A (66.5 in) is not drawn; both together would be 162.25 in. The estimator's two lines at 1 EA each are one counted line (SS-03B) and one F2 convention line (SS-03A). Other suffixed pairs (SS-02L/R, SS-04L/R, SS-07A/B, TB-03A…D, TB-04A/B, TB-05A…D) are not placed and get 1 EA each. TB-04A is placed and TB-04B is not.
5. **"ST02?" is printed with a question mark in the PlanSwift legend.** The estimator was unsure whether the phone-room bubble is ST-02 SLIM PED W/ CUSHION or MS-01 PHONE ROOM PEDESTAL. The plan text says `ST-02`. Both rows end up at 1 EA (ST-02 counted, MS-01 by convention), so the question doesn't change the quantities.
6. **TBD rows.** CH-06 (TBD / TBD) is placed twice, so it is carried as "CHAIR - CH-06" at 2 EA. SS-05 (TBD / TBD) is not placed and is not carried.
7. **TB-08 CHECK WRITING STAND is on the furniture schedule but built by the MILLWORKER (A-708).** It is not a furniture line. It belongs to millwork.
8. **TB-05B is tagged on A-160 but has no PlanSwift count.** It lands at 1 only through the convention. On a job with two placements this would undercount.
9. **The shade drop is not printed anywhere.** The estimator used 16 ft. The documents support a drop at or below 12'-0": ceiling or pocket down to floor or a 2'-8" sill. Treat 16 ft as a house convention and flag it.
10. **One PlanSwift reader took the MECHOSHADE unit as SQ FT.** It is a linear item and prints `74.0 FT`. The area exists only inside PlanSwift (LF × height property).
11. **The furniture schedule has typos, and the estimate re-keys rather than copies it.** Schedule typos the estimate copied: CH-08 `35.4"D` (should be H) and CH-11 `30"SH` on a 29"H chair. The schedule prints SS-02L/R `16.5' SH` (foot mark), and the estimator corrected it to `16.5"SH`. The estimator also introduced his own errors: SS-01 `26.25"D x 26.25"W` became `26.25"W X 26.25"W`, ST-02 `18 7/8"D` became `18"7/8"D`, WS-01 `9'W OR 10'W` became `9"W OR 10"W`, CH-09 `17.5"-21.5"SH` became `17.25"-21.5"SH`, and SS-07B `18"SH` became `16.5" SH`. Carry the printed schedule string and flag the typo; do not "fix" dimensions in item text. Note that this estimate does not carry the printed string on every line, so text-match scoring against it will show these seven lines as differences.
12. **Electrical owns the MechoShade control switches (E-703, 4 EA, line 568) and the keynote P14 control location.** Framing trades own the pocket framing and blocking (A-310 "3 5/8" MTL. STUD FURRING AT MECHO-SHADES", A-430 "BLOCKING AT MECHOSHADE PER MANUFACTURER"). Don't count them here.
