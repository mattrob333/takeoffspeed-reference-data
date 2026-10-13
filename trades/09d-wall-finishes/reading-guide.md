# Reading guide: wall tile, wall covering, FRP

## 1. Start from the finish schedule (A-170)

A-170 SCHEDULES has a **FINISHES SCHEDULE** in its right half. It is a raster table with **no text layer**, so you have to render it and read it as an image. Text extraction returns only the title "FINISHES SCHEDULE". The table has the columns `ITEM | DESCRIPTION | MANUF. | SIZE | SERIES | COLOR | REMARKS`, and the trade's rows sit under the group heading **WALL TILE / COVERING**:

```
WT-1  WALL TILE  ROCA  3" x 12"  FLOW  WHITE (FLOWH17-312)   GLOSS FINISH, MIX 60% / TOP TRIM: SCHLUTER JOLLY J AE / WITH INSIDE & OUTSIDE CORNER TRIM ACCESSORIES
WT-2  WALL TILE  ROCA  3" x 12"  FLOW  COSMIC SAPPHIRE (FLOCB09-312)  GLOSS FINISH, MIX 20%
WT-3  WALL TILE  MOSA  6" x 12"  MURALS  DARK ANTHRACITE #2 (30610-1530)  GLOSS FINISH
WT-8  BULLNOSE   ROCA  3" x 12"  FLOW  TENDER GRAY (FLOTG10-S4312)  BULLNOSE AS BASE
WT-9  WALL TILE  ROCA  3" x 12"  FLOW  TENDER GRAY (FLOTG10-312)  GLOSS FINISH, MIX 20%. / COVE TRIM: SCHLUTER DILEX-AHK 1S AE / WITH INSIDE & OUTSIDE TRIM ACCESSORIES
WT-10 WALL TILE  SOUTH CYPRESS  PICKET  MIX BLUE  FLAGSHIP BRANCH ONLY
WC-1  WALL COVERING  FORMULA  VARIES  VARIES BY FOCUS MARKET  Contact: Tyler Gilbert
FRP-1 FIBERGLASS REINFORCED PLASTIC  MARLITE  48" H  PEBBLED  P100 CLASSIC WHITE  JANITOR CLOSET WET WALLS
```

Also read the **PAINT** group, because it holds `PT-7 PRIMER SHIELDZ UNIVERSAL WALLCOVERING ROMAN PRO-999 ULTRA PRIME — PRIMER (DRIES CLEAR), COORDINATE w/ OWNER VENDOR`. The **GROUT** group holds `GR-3 … EPOXY 543 DRIFTWOOD — SERVICE AREA, EMPLOYEE LOUNGE, RESTROOM WALLS`, which is the grout for these tiles.

Each schedule row gives you three things:
- **MIX %**: the WT-1, WT-2 and WT-9 rows together are *one blended band*, not three bands.
- **Trim callouts**: the Jolly top trim on the WT-1 row and the Dilex cove on the WT-9 row, each "WITH INSIDE & OUTSIDE (CORNER) TRIM ACCESSORIES". These feed the Schluter lines in flooring.
- **Scope words**: "FLAGSHIP BRANCH ONLY" means WT-10 is not on this job. "JANITOR CLOSET WET WALLS" means FRP-1 goes only there.

## 2. Find every place each tag appears

| Tag | Plan tag (A-150 FINISH PLAN) | Elevation that sizes it |
|---|---|---|
| WT-1 / WT-2 / WT-9 | MENS 113, WOMENS 112 (tag stack `PT-1 / WT-1 / WT-2 / WT-9`). The enlarged plan 6/A-410 numbers the same rooms MEN'S 112 and WOMEN'S 111; match rooms by name. | A-410 RESTROOM ELEVATION B (9), C (8), D (7). Elevation A (10) has **no** tile, only the WT-8 base. |
| WT-1 / WT-2 / WT-9 (backsplash) | not tagged on A-150 | A-703 SERVICE COUNTER MILLWORK ELEVATION (2); A-705 EMPLOYEE LOUNGE ELEVATION (2) |
| WT-3 | not tagged on A-150 | A-700 TRANSACTION BAR FRONT ELEVATION (4); section 7 "WT-3 AS SCHEDULED, CAULK PERIMETER" |
| WC-1 | WEATHER VESTIBULE 100 (hexagon `WC-1` with leaders to the two ends of the north wall) | none. Height comes from A-130 "12' - 0" A.F.F." |
| PT-7 | MEETING ROOM 105 (`PT-7` on the north wall; `PT-8` on the west wall) | none. Height comes from A-130 "10' - 0" A.F.F." |
| PT-7 (second tag) | GATHERING AREA 103 north wall (stacked `PT-4 / PT-7` pair, leaders to both ends of the wall) | none. A-130 gives `10' - 0"A.F.F.` The A-704 tech wall details show only PT-4 / PT-6. PT-7 is tagged twice on A-150: Meeting Room 105 north wall (measured, 10.3 LF) and Gathering Area 103 north wall (stacked PT-4 / PT-7, 10.6 LF at 10'-0", not measured). Under F6 this is a second assumed wall covering of about 106 SF (V.I.F.), not carried by the estimator. |
| FRP-1 | JANITOR 115 (`FRP-1` leader into the mop-sink corner) | A-410 JANITOR CLOSET ELEVATION (1) and (3): "FRP PANEL @ MOP SINK, BOTH SIDES", 4'-0" |

The backsplash and transaction-bar tile appear **only on the A-700 series millwork sheets**. A reader that works only from the finish plan will miss about 67 SF of tile, which is 24% of all the tile.

## 3. How to read each input

- **Band height.** Read the dimension string on the elevation: `5'-6"` on A-410 B, C and D, `32"` on A-703, `1'-6 1/2"` on A-705, `3'-8 1/2"` on A-700 (the tile, not the `3'-9 3/4"` overall that includes the 1 1/4" SLD-1 top).
- **Band length.**
  - A-703: the top dimension chain `1" | 3'-0" | 3'-4" | 3'-4" | 1"`. The tile starts after the 3'-0" tall-cabinet bay, so the length is 3'-4" + 3'-4" + 1" = 6'-9".
  - A-705: the top chain `1'-6" | 2'-4" | 2'-4" | 2'-4" | 2"`. The tile starts after the 1'-6" open cabinet, so the length is 7'-2".
  - A-410: the elevations carry **no width dimension**. Scale them (1/2" = 1'-0" is 36 pt/ft on the 2592 × 1728 pt, 36" × 24" sheet), or take the room dimensions from ENLARGED RESTROOM PLAN 6/A-410, which prints the strings `7' - 8"`, `7' - 8 1/8"` and `7' - 6 3/8"`. Those match the scaled elevation widths of 7.51 to 7.68 ft.
  - A-700: the width is not on the front elevation (4), but it is on the back elevation (3) and the plan: `10'-6 3/4"` from FACE OF WALL to the outside of the waterfall edge (11'-9" overall). Deduct the two 1 1/4" SLD-1 returns drawn at the ends of the tile field: 10'-4 1/4". Scaling the front elevation at 3/4" = 1'-0" (54 pt/ft) gives 10'-4 3/8", a confirmation only.
- **Doors in a band.** Elevation D on A-410 has the entry door through the full band height. Take it out of the wall length: 4'-0" left of the door plus the 4" strip right of the frame. Do not deduct it as an opening.
- **Fixtures.** The WCs, lavs, TA-06 mirror, dispensers, Keurig, Quench and microwave all stand in front of the tile. The estimator deducted none of them.
- **Run on plan (WC, PT-7, FRP).** Measure the finished face between the corners the tag's leaders point to. Do **not** use the A-120 dimension strings blindly. The Meeting Room "10'-9 1/4"" and the vestibule "7'-11 1/8" + 3'-0 3/8"" are to grid and stud lines, while the finish runs measured 10.3 and 10.1 LF.
- **Full-height finishes.** Take the height from the RCP ceiling tag of that room (A-130: `12' - 0"A.F.F. PT-3` in the Weather Vestibule, `10' - 0"A.F.F. ACT-1` in the Meeting Room). The markup writes it into the item name (`WC1 @ 12'H`, `PT7 @ 10'`).
- **FRP run.** The P-101 fixture schedule gives `MOP SINK BASIN FIAT MSK-2424 24"X24"X10"`. "BOTH SIDES" means 2 walls × 2'-0".

## 4. The PlanSwift markups for this trade

| Markup page | Sheet | Rows used |
|---|---|---|
| p08 | A-150 | `WC1 @ 12'H 10.1 FT`, `PT7 @ 10' 10.3 FT`, `WALL COVERING @ 10'H ABOVE PT7 10.3 FT`, `FRP-1 @ 4'H 4.0 FT` |
| p16 | A-410 | `WT1 WALL TILE 120.7 SQ FT` (cyan), `WT2 WALL TILE 43.8 SQ FT` (magenta), `WT9 WALL TILE 50.6 SQ FT` (blue) |
| p23 | A-700 | `WT3 TILE 38.4 SQ FT` (purple/orchid). The same rectangle is also used for `1/4" CEMENTITIOUS BACKER BOARD 38.4` and `PL-4 FINISH 38.4`. |
| p27 | A-703 | `WT1 15.3`, `WT2 1.4`, `WT9 1.3 SQ FT`. p26 is the same sheet A-703 with millwork rows only. |
| p32 | A-705 | `WT1 8.2`, `WT2 1.6`, `WT9 1.3 SQ FT` (p32 comes after A-708 at p31) |

Legend names drop the hyphen (`WT1`, `WC1`) while the drawing tags keep it (`WT-1`, `WC-1`). Match on the normalised tag.

## 5. Cross-checks

1. **Blend total equals the band.** WT-1 + WT-2 + WT-9 on a sheet must equal Σ walls × band height. The results are A-410 215.1 against 214.7, A-703 18.0 against 18.0, and A-705 11.1 against 11.05. If the three add up to three times the band, every tag was given the full band.
2. **Blend split against the schedule MIX.** The job is 59.1 / 19.1 / 21.8% against the scheduled 60 / 20 / 20. A large departure, more than about 10 points, means a tag was missed.
3. **Top trim against band length.** The Schluter top trim should be about Σ walls on the restroom elevations: 2 × 19.52 = 39.0 LF against line 234 at 39.55 LF.
4. **Backer and tile.** On A-700 the 1/4" cementitious backer (38.4 SF on p23) equals the WT-3 tile area.
5. **Primer and wall covering.** PT-7 paint (line 298) is 105 SF and the wall covering over it (line 240) is 103 SF. Both come from the same 10.3 LF wall.

## 6. Traps hit on this job

- **The finish schedule is an image.** A text-only reader never sees the MIX %, the trims, FRP "48" H", or that PT-7 is a primer.
- **"Similar to" rooms.** The three tiled elevations are referenced from both rooms (markers 7/8/9 in each on 6/A-410; marker 10 appears only in the Men's) and drawn once; the plan note makes the Men's similar. Forgetting the × 2 halves the restroom tile, about 107 SF. In the markup the estimator pasted a second offset copy of the Women's polygons below the elevations.
- **Room numbers disagree between sheets.** 6/A-410 numbers the rooms MEN'S 112 and WOMEN'S 111; A-150 and the door tags use MENS 113 / WOMENS 112. Match rooms by name.
- **A stacked wall tag means both treatments on that wall.** The Gathering Area 103 `PT-4 / PT-7` pair was measured only as PT-4. Read every hexagon in a stack, and flag the PT-7 wall covering implied there (about 106 SF, V.I.F.). The 09e painting folder flags the same PT-7 shortfall (`trades/09e-painting/README.md`, line 85).
- **A blend is not three bands.** WT-1, WT-2 and WT-9 share one 5'-6" band. Giving each tag the full band triples the tile (732 SF against 244 SF).
- **Accent tiles are traced, not ratioed.** The MIX % misses WT-9 by 8% on this job.
- **The millwork sheets carry tile.** The A-700 series holds 67.5 SF of tile (WT-3 and the two backsplashes) that is not tagged on the finish plan.
- **The wall covering is probably by owner.** The spec matrix (p15) lists "Vinyl wall covering" as furnished and installed by the Owner, A-170 gives a vendor contact for WC-1, and PT-7 says "COORDINATE w/ OWNER VENDOR". The estimator carried both wall coverings anyway (223 SF), and one of them is labelled assumed.
- **No 09 7200 section.** The TOC lists Wall Coverings, but the manual does not contain it. There is no width, weight or type to read, which is why the size reads "VARIES".
- **WT-10 "FLAGSHIP BRANCH ONLY"** is in the schedule but is not used. Do not take it off.
- **Height on wall-finish runs.** For the PlanSwift FT rows the height lives only in the item name. A reader that takes the FT number as SF is off by a factor of 4 to 12.
- **WC-1 rounding.** The estimator wrote 120 SF (10 × 12) against the 10.1 FT run. Expect a 1% difference here and do not tune a formula to absorb it.
