# 09d: Wall tile, wall covering, FRP

This folder covers estimate lines **235 to 241** (section `WALL FINISH`, drawing reference `A410, A700 - A705`), one bank branch with one storey. It reconstructs quantities and material descriptions only.

| Line | Item | Unit | Estimator | Rebuilt | Δ | Class |
|---|---|---|---|---|---|---|
| 235 | WALL TILE WT-1, 3"x12", Roca Flow, White | SF | 144.19 | 144.20 | +0.01% | measured |
| 236 | WALL TILE WT-2, 3"x12", Roca Flow, Cosmic Sapphire | SF | 46.72 | 46.80 | +0.17% | measured |
| 237 | WALL TILE WT-3, 6"x12", Mosa Murals, Dark Anthracite #2 | SF | 38.42 | 38.40 | −0.05% | measured |
| 238 | WALL TILE WT-9, 3"x12", Roca Flow, Tender Gray | SF | 53.22 | 53.20 | −0.04% | measured |
| 239 | WALL COVERING WC-1, Formula, varies by focus market | SF | 120.00 | 121.20 | +1.00% | derived (LF × H), rounded by the estimator |
| 240 | WALL COVERING @ PT7 PAINT, assumed, V.I.F. | SF | 103.00 | 103.00 | 0.00% | derived (LF × H) on an assumed scope |
| 241 | FRP-1, 48" H, Marlite Pebbled, P100 Classic White | SF | 16.00 | 16.00 | 0.00% | derived (LF × H) |

**Reconciliation: 7 of 7 lines reconciled. 6 lines are within 0.2%; WC-1 is +1.00% (the estimator's 10 × 12 against the measured 10.1 LF), so all 7 are within 1.5% and within 5%.** One scope finding sits outside the lines: a second PT-7 tag (Gathering Area 103) implies about 106 SF of assumed wall covering that nobody carried (see Open points). Each tile line is the sum of the PlanSwift areas for its tag across the elevation sheets. The other three lines are a PlanSwift linear run multiplied by the height written in the legend item name. WC-1 is the only line that is not exact (see below).

## Scope

- **Ceramic wall tile.** Tile bands in the two restrooms (A-410), the backsplashes at the service counter (A-703) and the employee lounge (A-705), and the tiled front face of the transaction bar (A-700).
- **Wall covering.** WC-1 on the weather vestibule wall (A-150). A wall covering is also assumed over the PT-7 wallcovering primer on the meeting room feature wall (A-150). A-150 tags PT-7 a second time, on the Gathering Area 103 north wall; that one was not measured (Open points).
- **FRP.** FRP-1 on the two wet walls behind the janitor's corner mop sink (A-150, A-410).
- **Not in these lines.** WT-8 bullnose base is line 228 (flooring, 11.28 LF). Schluter cove trim and Schluter trim are lines 233 and 234 (flooring transitions). Grout GR-3 is line 226. Cementitious backer board is lines 266 and 272 (gypsum board). Paint, including PT-7 primer, is lines 295 to 299. Each of those belongs to its own trade folder. This folder uses them only as cross-checks.

## Driving sheets

| Sheet | What it gives this trade |
|---|---|
| **A-170 SCHEDULES**, *FINISHES SCHEDULE*, group "WALL TILE / COVERING" (raster table with no text layer, so read it as an image) | Tag → product, size and remarks. WT-1 "GLOSS FINISH, MIX 60%, TOP TRIM: SCHLUTER JOLLY J AE WITH INSIDE & OUTSIDE CORNER TRIM ACCESSORIES"; WT-2 "MIX 20%"; WT-9 "MIX 20%. COVE TRIM: SCHLUTER DILEX-AHK 1S AE WITH INSIDE & OUTSIDE TRIM ACCESSORIES"; WT-3 "GLOSS FINISH"; WT-8 "BULLNOSE AS BASE"; WT-10 "FLAGSHIP BRANCH ONLY" (not used on this job); WC-1 "FORMULA / VARIES / VARIES BY FOCUS MARKET"; FRP-1 "MARLITE / 48" H / PEBBLED / P100 CLASSIC WHITE / JANITOR CLOSET WET WALLS". PAINT group: PT-7 "PRIMER / SHIELDZ / UNIVERSAL WALLCOVERING / ROMAN PRO-999 ULTRA PRIME / PRIMER (DRIES CLEAR), COORDINATE w/ OWNER VENDOR". |
| **A-150 FINISH PLAN** (markup p08) | Locates the plan tags: WC-1 (Weather Vestibule 100), PT-7 and PT-8 (Meeting Room 105), a stacked PT-4 / PT-7 pair on the Gathering Area 103 north wall (measured only as `PT4 @ 10'H` 10.6 FT), FRP-1 (Janitor 115), WT-1/WT-2/WT-9 (Mens 113, Womens 112). It carries the three linear wall-finish runs. |
| **A-410 ENLARGED RESTROOM PLANS & ELEVATIONS** (markup p16) | Restroom elevations B, C and D (9, 8, 7), with a 5'-6" tile band. Plan note "MENS INTERIOR ELEVATIONS ARE SIMILAR TO WOMENS INTERIOR ELEVATIONS"; markers 7/8/9 appear in both rooms. The enlarged plan numbers the rooms MEN'S 112 / WOMEN'S 111 against A-150's 113 / 112, so match by name. Janitor closet elevations 1 and 3: "FRP PANEL @ MOP SINK, BOTH SIDES", 4'-0" high. |
| **A-700 TRANSACTION BAR** (markup p23) | Detail 3 BACK ELEVATION prints the bar 10'-6 3/4" from FACE OF WALL (11'-9" overall); less the two 1 1/4" SLD-1 returns, the WT-3 field is 10'-4 1/4" wide. Detail 4 FRONT ELEVATION: WT-3 field 3'-8 1/2" high, with the note "PROVIDE FLEXIBLE CAULK JOINT AROUND PERIMETER OF TILE IN LIEU OF GROUT JOINT". Detail 7 calls for "1/4" CEMENTITIOUS BACK BOARD … WT-3 AS SCHEDULED, CAULK PERIMETER". |
| **A-703 SERVICE COUNTER** (markup p27; p26 is the same sheet with millwork only) | Detail 2 MILLWORK ELEVATION: 32" backsplash tile from the 3'-0" bay to the end panel, 3'-4" + 3'-4" + 1". |
| **A-705 EMPLOYEE LOUNGE** (markup p32) | Detail 2 ELEVATION: 1'-6 1/2" backsplash, 2'-4" × 3 + 2". |
| **A-130 REFLECTED CEILING PLAN** | Band heights for full-height finishes: WEATHER VESTIBULE 12'-0" A.F.F. (WC-1 @ 12'H) and MEETING ROOM 10'-0" A.F.F. (PT7 / WC @ 10'). |
| **A-620** general note N | "ALL PARTITIONS SCHEDULED TO RECEIVE TILE OR FRP, SHALL BE CONSTRUCTED OF WATER-RESISTANT CORE GYPSUM WALL BOARD." This is a substrate for gypsum board, not a quantity in this trade. |
| **P-101** | "MOP SINK BASIN FIAT MSK-2424 24"X24"X10"". This size gives the FRP run: two walls of 2'-0". |

## Spec sections (project manual page numbers)

| Section | Pages | What it specifies |
|---|---|---|
| 09 3000 TILING | 282–288 | p282: "Furnish 10 percent attic stock of tiling materials" (an extra the estimator did not carry). p283: ANSI A137.1 Standard grade; basis of design, grout colour and trim units "as indicated or scheduled on Drawings"; "Provide base cove shapes". p284: crack-suppression membrane Laticrete Blue 92; thin-set latex-portland cement mortar ANSI A118.4; polymer-modified grout ANSI A118.7; epoxy grout ANSI A118.3. p287: joints 1/4" unless indicated otherwise; grid pattern; avoid cuts smaller than half a tile. p288: wall installations on studs follow TCA W247, with thin-set and polymer-modified sanded grout. |
| 06 6400 PLASTIC PANELING (the FRP) | 142–145 | p143: glass-fibre-reinforced plastic to ASTM D 5319, basis of design Marlite; flame spread ≤ 25 and smoke ≤ 450 (ASTM E 84); **nominal thickness at least 0.09 inch**; molded pebble texture; colour as scheduled. One-piece vinyl trim (division bars, inside and outside corners, caps), nylon drive rivets, adhesive ≤ 50 g/L VOC. p144: mildew-resistant silicone sealant. p145: full spread of adhesive plus fasteners in oversized holes sealed with sealant. |
| 09 9110 PAINT SCHEDULE | 328 | "Only where noted on Finish Plans — Gypsum Board — Roman PRO-999 Ultra Prime". This is the PT-7 wallcovering primer row. |
| 01 2200 attachment, responsibility matrix | 15 (page 2 of 4) | **"Vinyl wall covering — Designed/Selected O, O — Furnished by Owner — Installed by Owner."** Compare this with the A-170 note for WC-1 ("Contact: Tyler Gilbert") and the PT-7 note "COORDINATE w/ OWNER VENDOR". |
| 09 7200 Wall Coverings | none (TOC p6 only) | The table of contents lists 09 7200, but the manual does not contain the section. No wallcovering type, weight or width is specified. |

## Material types

| Tag | Material | Size | Properties | Where |
|---|---|---|---|---|
| WT-1 | ceramic wall tile, Roca Flow White (FLOWH17-312) | 3"x12" | gloss, 60% of the blend; Schluter Jolly J AE top trim with inside and outside corners | restroom band field, backsplashes |
| WT-2 | Roca Flow Cosmic Sapphire (FLOCB09-312) | 3"x12" | gloss, 20% of the blend (dark accent tiles) | restroom band, backsplashes |
| WT-9 | Roca Flow Tender Gray (FLOTG10-312) | 3"x12" | gloss, 20% of the blend; Schluter Dilex-AHK 1S AE cove trim with inside and outside trim accessories | restroom lower band and accents, backsplashes |
| WT-3 | Mosa Murals Dark Anthracite #2 (30610-1530) | 6"x12" | gloss; on 1/4" cementitious backer; caulked perimeter | transaction bar front |
| WC-1 | Formula wall covering | "VARIES" | "VARIES BY FOCUS MARKET"; owner-furnished and owner-installed per the spec matrix | weather vestibule wall, full height |
| (PT-7) | Shieldz universal wallcovering primer, Roman Pro-999 | — | clear primer, coordinate with the owner vendor | meeting room feature wall (estimator assumed a wall covering here); also tagged on the Gathering Area 103 north wall (not measured) |
| FRP-1 | Marlite FRP, pebbled, P100 Classic White | 48" H | ≥ 0.09" thick, Class A (FS ≤ 25) | janitor closet wet walls |

## What the estimator measured

- **Tile: SQ FT areas traced on the interior elevations, one PlanSwift area item per tag per sheet.** The WT-1 area is the field net of the accent tiles: WT-1 + WT-2 + WT-9 equals the gross band (A-410 215.1 SF against 214.74 to 214.96 SF from the vectors; A-703 18.0 against 6'-9" × 32" = 18.0; A-705 11.1 against 7'-2" × 1'-6 1/2" = 11.05). The WT-2 and WT-9 accent tiles were traced tile by tile, so the split follows the drawn pattern and not the scheduled MIX %. Fixtures, mirrors and appliances in front of the band (WC, lav, TA-06 mirror, Keurig, Quench, microwave) were **not** deducted. The door in elevation D was excluded. On A-410 the estimator traced the Women's elevations and then copied the polygons, offset below the views, to count the Men's room ("MENS … SIMILAR TO WOMENS"). The legend total is therefore for two rooms.
- **Wall covering and FRP: FT runs on the finish plan A-150, with the height written in the item name.** These are `WC1 @ 12'H` 10.1 FT, `WALL COVERING @ 10'H ABOVE PT7` 10.3 FT and `FRP-1 @ 4'H` 4.0 FT. The SF is the run times that height.
- **Tile lines in the estimate add the tag's legend rows across A-410, A-703 and A-705.** WT-3 occurs only on A-700.
- **No waste and no attic stock in any line.** Every quantity is net. Spec 09 3000 asks for 10% attic stock and nobody carried it.

## Open points

- **WC-1 is 120.0 against 121.2 SF.** 120 = 10.0 LF × 12'. The legend clearly shows 10.1 FT, and the other two runs on the same page convert exactly, so this is a one-off rounding or override. It cannot be proven from the data. GPT-6 Astra reached the same conclusion independently.
- **PT-7 is tagged twice on A-150.** Meeting Room 105 north wall (measured, 10.3 LF) and Gathering Area 103 north wall (stacked PT-4 / PT-7, 10.6 LF at 10'-0", not measured). Under F6 this is a second assumed wall covering of about 10.6 × 10 = 106 SF (V.I.F.), not carried by the estimator. Line 240 is unchanged. The A-704 tech wall details show only PT-4 / PT-6 on that wall, so the extent is uncertain. The 09e painting folder flags the same PT-7 primer shortfall (`trades/09e-painting/README.md`, line 85).
- **Scope.** The spec matrix makes vinyl wall covering owner-furnished and owner-installed, yet the estimator carried 223 SF of wall covering (lines 239 and 240). Line 240 has no wall covering drawn at all; it is inferred from a primer-only paint tag. Both lines need a by-owner / V.I.F. flag rather than a firm quantity.
- The working files and cross-check scripts are in `trades/09d-wall-finishes/scripts/` (`geom.py`, `pix.py`, `colarea.py`, `mix.py`, `engine-run.ts`, and the GPT answers in `gpt-q*.txt`). Review crops are in `trades/09d-wall-finishes/scripts/09d-review/`.

## Verification

A reviewer raised nine points on this folder. Each one was checked against the source by Claude Opus 5.5, with GPT-6 Astra as a second opinion (`trades/09d-wall-finishes/scripts/gpt-q3.txt`). All arithmetic was done in python, and the engine was rerun with `tsx`. All nine were confirmed and fixed. No estimate line value changed.

| # | Point | Checked | Change |
|---|---|---|---|
| 1 | Second PT-7 tag at Gathering Area 103 | A-150 text layer (PT-4 at 0.416,0.401; PT-7 at 0.433,0.401) and crop; legend p08 has only `PT4 @ 10'H` 10.6 FT on that wall; A-130 `10' - 0"A.F.F.`; 10.6 × 10 = 106.0. GPT-6 Astra said the leaders show where the tags apply, not that both cover the whole wall, and A-704 shows only PT-4 / PT-6. | Open point, reading-guide section 2 row and trap, F6 note, app-gaps item 6 stacked-tag rule. Line 240 kept at 103.0. The 106 SF is carried as a flag (up to 106 SF, V.I.F.). |
| 2 | Two restroom wall sets | 2 × 19.552 × 5.5 = 215.07 against 2 × 19.522 × 5.5 = 214.74 | `engine-run.ts` rerun with the fixture widths (engine 214.7442 SF). app-gaps now quotes 214.74 / 243.79 / 107.37 / 731.4. |
| 3 | WT-3 width has a printed basis | A-700 text: `10'-6 3/4"` and `11'-9"` on detail 3. Vectors: field 814.51 to 1374.19 pt = 10'-4 3/8", returns 1.25" each. 10'-4 1/4" × 3'-8 1/2" = 38.397 SF (−0.06%). GPT-6 Astra agreed. | F1, reconciliation row 237, fixture 3 (walls_ft 10.3542) and reading-guide section 3 use the printed basis. Vectors are kept as the confirmation, and the engine row is rerun at 38.40 SF. |
| 4 | WC-1 fixture on the 1.0% boundary | (121.2 − 120)/120 = 0.9999999999999905% in float, exactly 1/100 in rationals | Tolerance set to 1.5%, with the reason given in `source`. README and app-gaps item 5 updated. |
| 5 | `repeat` name collision | `wall-finishes.ts` line 135 is `repeat` (pattern repeat in inches); line 148 reads it with `qOpt` | Proposal renamed to `roomRepeat`, with a note to keep the two apart |
| 6 | Fixture 7 input shape | fixtures 5 and 6 use `run_lf` | Fixture 7 now has `run_lf` 4.0 and a `run_basis` |
| 7 | `openings` read string | `WALL_INPUTS` line 24: "door / window / fixture opening" | app-gaps item 6 has the new read string |
| 8 | WT-9 remark truncated | A-170 crop, WT-9 REMARKS | "WITH INSIDE & OUTSIDE TRIM ACCESSORIES" added in the README tables and reading-guide section 1 |
| 9 | Restroom markers and room numbers | 6/A-410: MEN'S 112 (markers 7/8/9/10), WOMEN'S 111 (7/8/9); A-150 and the door tags use 113 / 112 | Reading-guide section 6 reworded, numbering trap added, and the README A-410 row and app-gaps item 2 aligned |

All 11 fixtures recompute within their tolerance. Reconciliation count: 7 of 7 lines reconciled (6 within 0.2%, WC-1 +1.00%).
