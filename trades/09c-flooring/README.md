# 09c: Flooring, grout, base, transitions

This folder covers estimate lines **217 to 234**: section `FLOORING` with the sub-sections `GROUT`, `BASE` and `TRANSITION`, drawing reference `A150`. The job is a single-storey bank branch. Only quantities and material descriptions are reconstructed here.

| Line | Item | Unit | Estimator | Rebuilt | Δ | Class |
|---|---|---|---:|---:|---:|---|
| 217 | SEALED CONCRETE CON-1, Benjamin Moore Corotech, clear | SF | 68.78 | 68.80 | +0.03% | measured |
| 218 | CARPET CR-1, 12"x36", Mohawk Lichen, Stone Community | SF | 131.36 | 131.40 | +0.03% | measured |
| 219 | CARPET CR-2, 12"x36", Mohawk Lichen, Micro Bloom II | SF | 435.67 | 435.70 | +0.01% | measured |
| 220 | CARPET CR-3, 12"x36", Mohawk Lichen, Macro Bloom II | SF | 27.08 | 27.10 | +0.07% | measured |
| 221 | WALK-OFF CARPET CR-4, 18"x36", Mannington Charge, Fluid | SF | 82.42 | 82.40 | −0.02% | measured |
| 222 | CERAMIC TILE FT-1, 24"x24", Florida Tile Aventis, Velvet | SF | 946.11 | 946.10 | −0.00% | measured |
| 223 | LVT-1, 25 cm x 1 m, Interface On Grain 4.5 mm | SF | 93.95 | 94.00 | +0.05% | measured |
| 224 | ANTI-STATIC MAT MT-1, 36"x48", Mats Inc. | SF | 10.00 | 6.00 | −40.0% | allowance/judgment |
| 225 | GROUT GR-1, Custom Building epoxy, 335 Winter Gray | SF | 1050 | 1050 | 0.00% | derived |
| 226 | GROUT GR-3, Custom Building epoxy, 543 Driftwood | SF | 300 | 300 | 0.00% | derived |
| 227 | RUBBER BASE WB-1, 4", Johnsonite Traditional, #48 Grey | LF | 404.72 | 404.70 | −0.00% | measured |
| 228 | BULLNOSE BASE WT-8, 3"x12", Roca Flow, Tender Gray | LF | 11.28 | 11.30 | +0.18% | measured |
| 229 | TRANSITION FTS-1, Schluter Schiene AE100 (carpet to tile) | LF | 51.63 | 51.60 | −0.06% | measured |
| 230 | TRANSITION FTS-2, Schluter Schiene AE100 (vinyl to tile) | LF | 28.99 | 29.00 | +0.03% | measured |
| 231 | TRANSITION FTS-3, Schluter Reno-U AE100 (tile to concrete) | LF | 12.24 | 12.20 | −0.33% | measured |
| 232 | TRANSITION FTS-4, Schluter Reno-Ramp AERP (concrete to mat) | LF | 10.02 | 10.00 | −0.20% | measured |
| 233 | SCHLUTER COVE TRIM | LF | 51.87 | 51.90 | +0.06% | measured |
| 234 | SCHLUTER TRIM | LF | 39.55 | 39.60 | +0.13% | measured |

**Reconciliation: 17 of the 18 lines rebuild within 1% (and within 5%). The one that does not is MAT-1.** The eight geometry checks below are also all within 1%. Fifteen lines are a PlanSwift legend value copied straight into the estimate. Each legend value is printed to one decimal and the estimate line carries the full PlanSwift precision, which is why the differences are at most 0.33%. The two grout lines are derived from tile area by a round-up rule (see below). MAT-1 is a judgment number. Three separate figures exist for it: drawn 6 SF, scheduled 12 SF, estimate 10 SF.

Eight of the measured lines were also checked against geometry, either read from the A-150 / A-410 vector layer, taken from the printed A-410 plan dimensions, or scaled from the markup. All eight rebuild within 1%:

| Line | Geometry rebuild | Δ vs estimate |
|---|---|---:|
| 217 CON-1 | ELEC./I.T. 106: 6.783 × 10.917 = 74.05 SF − MAT-1 2'×3' (6.00) + half door strip 3.00 clear opening × 0.247 (0.74) = 68.79 SF | +0.02% |
| 223 LVT-1 | GATHERING AREA 103 plank hatch: 9.739 × 9.622 = 93.71 SF | −0.26% |
| 230 FTS-2 | open sides of the LVT rectangle: 2 × 9.622 + 9.739 = 28.98 LF | −0.03% |
| 232 FTS-4 | perimeter of the drawn mat: 2 × (2 + 3) = 10.00 LF | −0.20% |
| 231 FTS-3 | thresholds 106 (3.00 clear, between the 2" frame members) + 110 (3.17) + 100 (6.08) = 12.25 LF | +0.08% |
| 234 Schluter trim | top of the 5'-6" tile band on walls B, C and D net of the restroom door, from the A-410 plan dimensions: Men's 7.667 + 7.677 + 4.667, Women's 7.531 + 7.677 + 4.531 = 39.75 LF | +0.51% |
| 228 WT-8 | two walls traced on elevation A: Women's east wall, which has no door (full 7'-3 1/2" = 7.29), + Men's west wall net of Janitor door 115 (3.67 + 0.22 = 3.89) = 11.18 LF | −0.87% |
| 233 Schluter cove trim | all four walls of both restrooms net of the three doors 112, 113 and 115, from the A-410 plan dimensions: 61.10 − 3 × 3.00 = 52.10 LF (= the top-trim walls 39.75 + the WT-8 walls 12.35) | +0.45% |

## Scope

- **Field flooring by finish tag.** Sealed concrete CON-1 in ELEC./I.T. 106. Carpet tile CR-1, CR-2 and CR-3 (12"x36", half lap) in PHONE 114, WORK ROOM 111, MEETING ROOM 105, TRANSACTION BAR 108, BOOTH 104 and RELAXED SEATING 102, where the stepped-diamond insets are CR-2 and CR-3 inside a CR-1 field. Walk-off carpet CR-4 (18"x36") in WEATHER VESTIBULE 100. Ceramic floor tile FT-1 (24"x24", the schedule's wording) in every other room. LVT-1 plank in GATHERING AREA 103.
- **Mat.** MT-1 anti-static mat on the sealed concrete in ELEC./I.T. 106.
- **Grout.** GR-1 is for floor tile (the schedule says "TRANSACTION BAR & FLOOR TILE"). GR-3 is for the restroom and backsplash wall tile ("SERVICE AREA, EMPLOYEE LOUNGE, RESTROOM WALLS"). The estimator carries both in SF.
- **Base.** WB-1 4" rubber base throughout, plus WT-8 3"x12" ceramic bullnose used as base on the restroom side walls that RESTROOM ELEVATION A shows: the Men's west wall (with Janitor door 115) and the similar Women's east wall (no door).
- **Transitions and tile trims.** FTS-1 to FTS-4 Schluter profiles on A-150. Also the Schluter cove trim (WT-9 "COVE TRIM: SCHLUTER DILEX-AHK 1S AE") and the Schluter top trim (WT-1 "TOP TRIM: SCHLUTER JOLLY J AE"), both measured on A-410.
- **Not carried by the estimator** (with the evidence for each):
  - thinset, grout product units (lb or kits), adhesives, carpet connectors.
  - 1/4" cement-board underlayment under the LVT and mat (A-150 details 2 and 4). About 99.95 SF; line 272 is 1/4" backer **at walls**, 40 SF.
  - "FLOAT SLAB 3'-0" FOR FINISHES TO ALIGN" (detail 1).
  - crack-suppression membrane "as indicated" (spec 09 3000 2.3); none is indicated.
  - 10% attic stock in all four flooring sections.
  - waste.
  - sealer gallons.
  - stick rounding.

## Driving sheets

| Sheet | Markup page | What it gives this trade |
|---|---|---|
| **A-150 FINISH PLAN** | p08 | Every floor tag, the four transition details FTS-1 to FTS-4, detail 5 THRESHOLD @ DIRTT DOOR, key notes F001 to F004, general notes A to Q, and the "TILE START POINT". Legend rows: `CON-1 FLOORING 68.8 SQ FT`, `CR1 FLOORING 131.4`, `CR2 FLOORING 435.7`, `CR3 FLOORING 27.1`, `CR4 FLOORING 82.4`, `FT1 FLOORING 946.1`, `LVT1 FLOORING 94.0`, `MAT-1 FLOORING 6.0 SQ FT`, `WB-1 404.7 FT`, `FTS1 TRANSITION 51.6 FT`, `FTS2 TRANSITION 29.0`, `FTS3 TRANSITION 12.2`, `FTS-4 TRANSITION 10.0`. |
| **A-170 SCHEDULES**, FINISHES SCHEDULE (raster table, no text layer) | p10 | Groups FLOOR FINISHES, TRANSITION STRIP, GROUT, WALL TILE / COVERING and WALL BASE & TRIM. They give tag → manufacturer, size, series, colour and remarks (rows quoted in reading-guide.md §1). |
| **A-410 ENLARGED RESTROOM PLANS & ELEVATIONS** | p16 | WT-8 base on RESTROOM ELEVATION A (10/A-410, the Men's west wall with Janitor door 115; the Women's east wall is "similar" without a door), the Schluter strip at the top of the 5'-6" band on elevations B, C and D, and the Schluter cove trim at the floor on all four walls (B, C and D at the foot of the band, and A at the WT-8 base, where elevation A's "SCHLUTER COVER TRIM" leader points). Legend rows: `WT-8 BASE 11.3 FT`, `SCHLUTER COVE TRIM 51.9 FT`, `SCHLUTER TRIM 39.6 FT`. |
| **A-600 DOOR SCHEDULE** | p21 | Door widths at the transitions: 100 and 101 are 6'-0" pairs, 105 is 3'-4" (DIRTT), and 106, 110, 111, 112, 113, 114 and 115 are 3'-0". |
| A-120 DIMENSIONAL FLOOR PLAN, A-110 | p04, p03 | Room dimensions for a cross-check only. The finish plan polygons were what the estimator measured. |

## Spec sections (project-manual page numbers)

| Section | Pages | What it specifies for quantities |
|---|---|---|
| 09 3000 TILING | 282–288 | p282: "Furnish 10 percent attic stock of tiling materials". p283: ANSI A137.1 Standard grade; basis of design "as indicated or scheduled on Drawings"; "Provide base cove shapes". p284: crack-suppression membrane Laticrete Blue 92 (ANSI A118.12); latex-portland thin-set (A118.4); polymer-modified grout (A118.7). p284–285: water-cleanable epoxy grout (A118.3, ≤ 65 g/L VOC). p285: grout sealer; "Floor Transition Trim Elements: As indicated on Drawings". p286: grid pattern, centre the fields, no pieces under half a tile; tile extends under equipment. p287: "install tile with 1/4 inch joint widths" unless otherwise indicated; expansion joints over slab joints; grout sealer on floor grout. p288: floors on concrete TCA F113 (thin-set, "polymer-modified sanded grout or epoxy grout, as scheduled", membrane "as indicated"); walls on studs TCA W247. |
| 09 6513 RESILIENT BASE AND ACCESSORIES | 304–308 | p304: 10% attic stock. p305: ASTM F1861 Type TS thermoset rubber, Group I; **Style A straight in carpet areas, Style B cove in resilient areas**; 0.125" thick; **4" high**; coils; outside and inside corners job-formed. p306: rubber molding accessories "Refer to Drawings". p307: base on "walls, columns, pilasters, casework and cabinets in toe spaces"; job-formed corners with returns of at least 3"; pH 5 to 9. p308: reducer strips at exposed edges. |
| 09 6519 RESILIENT TILE FLOORING | 309–314 | p309: 10% attic stock. p311: VCT, ASTM F1066 Class 2, 0.125", **12"x12"**, basis of design Armstrong Excelon. This conflicts with the drawings' LVT-1 25 cm x 1 m Interface plank; the drawings govern. p313: full-spread adhesive; "Extend floor tiles to center of door openings". |
| 09 6813 TILE CARPETING | 315–319 | p315: 10% attic stock. p316–317: basis of design and size "As scheduled on Drawings"; electrostatic propensity < 3.5 kV. p317: pressure-sensitive releasable adhesive. p319: extend into toe spaces and door reveals; pattern parallel to walls. |
| 03 3000 CAST-IN-PLACE CONCRETE | 55–56 | p55–56 §2.3 "CURING COMPOUNDS & SEALERS": approved sealers Dress & Seal 30, Master Seal, Kure-N-Seal. The finish schedule's CON-1 product, Benjamin Moore Corotech High Performance clear acrylic, governs the sealed floor. No coat count or coverage is given. |
| 12 4813 ENTRANCE FLOOR MATS AND FRAMES | 363–366 | Roll-up aluminium-rail mats in recessed frames. There is no such mat on this plan: the vestibule gets CR-4 walk-off carpet. MT-1 is an anti-static mat that the section does not cover. |

## Material types and specified properties

| Tag | Material | Size | Properties (A-170 unless noted) | Where |
|---|---|---|---|---|
| CON-1 | sealed concrete, Benjamin Moore Corotech High Performance | — | clear acrylic | ELEC./I.T. 106 |
| CR-1 | carpet tile, Mohawk Lichen Collection, Stone Community (GT472) 949 Stone | 12"x36" (3.0 SF) | installation half lap | field in 105 and 102 |
| CR-2 | Mohawk Lichen, Micro Bloom II (GT475) 975 Felted Fringe Stone | 12"x36" | half lap | 114, 111, 108, 104, plus the insets in 105 and 102 |
| CR-3 | Mohawk Lichen, Macro Bloom II (GT474) 975 Felted Fringe | 12"x36" | half lap | inner inset in 102 |
| CR-4 | walk-off carpet, Mannington Commercial Charge, Fluid (32367) | 18"x36" (4.5 SF) | horizontal brick ashlar | 100 |
| FT-1 | ceramic tile (A-170 and estimate wording; "porcelain" appears in no source), Florida Tile Aventis, Velvet | 24"x24" (4.0 SF) | unpolished; GR-1 grout; 1/4" joint per spec; TCA F113 | all FT-1 rooms |
| LVT-1 | luxury vinyl tile, Interface On Grain 4.5 mm, Earthen Forms A03305 Bespoke Timber | 25 cm x 1 m (2.691 SF) | ashlar with glued perimeter; on 1/4" cement board (detail 2) | 103 |
| LVT-2 | Mohawk C0135 Matayo Plus Stone, 972A Sonic Silver | 12"x24" | **scheduled but not used on the plan**, so no line | — |
| MT-1 | anti-static mat, Mats Inc., black | 36"x48" (12 SF) scheduled; 2'-0"x3'-0" drawn | anti-static / anti-fatigue | 106 |
| GR-1 | epoxy grout, Custom Building, 335 Winter Gray | — | ANSI A118.3 | floor tile (and the transaction bar per the schedule) |
| GR-3 | epoxy grout, Custom Building, 543 Driftwood | — | ANSI A118.3 | restroom walls and backsplashes |
| WB-1 | rubber base, Johnsonite Traditional Wall Base, #48 Grey | 4" | F1861 TS, 0.125", coils, job-formed corners | every room |
| WT-8 | bullnose tile, Roca Flow, Tender Gray (FLOTG10-S4312) | 3"x12" | "BULLNOSE AS BASE" | restroom side walls: Men's west (elevation A, net of door 115) and Women's east (similar, no door) |
| FTS-1 | Schluter Schiene AE100, satin aluminium | 3/8" | carpet to tile; detail 1 calls it "RENO-TK TRIM 3/8" (ATK 100AT)". Schedule and detail differ. | carpet/tile edges |
| FTS-2 | Schluter Schiene AE100 | 3/8" | vinyl tile to ceramic tile, over 1/4" cement board | LVT edges |
| FTS-3 | Schluter Reno-U AE100 | 3/8" | tile to sealed concrete | thresholds |
| FTS-4 | Schluter Reno-Ramp AERP, anodised | — | sealed concrete to mat; anchor leg in mortar bond beneath MAT-1 | mat perimeter |
| (trim) | Schluter Jolly J AE (WT-1 top trim), Schluter Dilex-AHK 1S AE (WT-9 cove trim) | — | with inside and outside corner accessories | restroom tile band |

## What the estimator measured, and in which units

- **Areas (SF)** are PlanSwift area polygons on the A-150 finish plan, one item per finish tag. A field is measured net of its insets. Each polygon runs to the door centreline (general note C and spec 09 6519 3.3.E). The CON-1 area is net of the mat. Nothing is deducted for millwork or counters.
- **Runs (LF)** are PlanSwift linear items:
  - WB-1 base on A-150.
  - FTS-1 to FTS-4 on A-150, drawn along the material boundaries and thresholds. FTS-4 is drawn round the mat.
  - WT-8 and the two Schluter trims on A-410.
- **Grout (SF)** is derived, not measured: ceil to 50 SF of (tile SF of the tiles the grout serves × 1.10).
- **Mat (SF)** is an override, 10 SF.
- No waste, attic stock, stick rounding or purchase units appear on any line. Every quantity is net, except the grout and mat round-ups.

See `formulas.md` for each rule, `reconciliation.csv` for the line-by-line numbers, `fixtures.json` for the engine test cases, `reading-guide.md` for how to read each input, and `app-gaps.md` for the comparison with the TakeoffSpeed engine. Scratch scripts are in `trades/09c-flooring/scripts/`: `build.py` rebuilds every line and writes the CSV and fixtures, and `grout.py` tests the grout rules.

## Verification

A reviewer's eight findings were re-checked against the sources. All recomputation is in `trades/09c-flooring/scripts/verify_fix.py`; the renders and second-opinion transcripts are in `trades/09c-flooring/scripts/09c-flooring-verify/`. Models: Claude Opus 5.5 (the review, the re-check, every edit) and GPT-6 Astra (independent readings of the same crops, via `tools/ask_gpt.py`).

What was checked, and what changed:

1. **WT-8 (228) is a correct line, not a door-crossing error.** On the A-410 plan, marker 10 (elevation A) is only in MEN'S 112, so elevation A is the Men's west wall and its door is JANITOR 115. Doors 113 and 112 are in the south walls, so the "similar" Women's east wall has no door. The two yellow runs scale 7.24 and 3.66 + 0.23 (132.75 px/ft). GPT-6 Astra, given the plan and the marked elevation, gave the same reading unprompted: Men's west wall net of 115 plus the Women's east wall with no door. Changed: the README table, the WT-8 rule in formulas.md F4, the reading-guide §4 entry and the §6 trap, CSV row 228, and the fixture labels. The 7.90 and 7.78 "net-of-door" figures were removed.
2. **Door 106 is 3.00 ft clear, not 3.33.** On the A-150 vector layer the 2" frame members are at x 1021.0–1024.0 and 1078.0–1081.0 pt. 3.33 was frame-outside to frame-outside. 3.00 equals the A-600 3'-0". The cyan run scales 2.92 ft; GPT-6 Astra read it as about 3.02 ft, spanning the clear opening. Changed: FTS-3 rebuilds at 12.25 LF (+0.08%, was +2.8%) and CON-1 at 68.79 SF (+0.02%, was +0.14%). The FTS-3 fixture now takes the three openings {3.00, 3.17, 6.08} instead of the legend value 12.2. The 110 and 100 values are the storefront wall openings on the vector layer; they are slightly wider than the 3'-0" and 6'-0" leaves, so they do not equal the schedule widths exactly, but they are kept as measured.
3. **Cove trim (233) reconciles.** From the plan dimensions, both restroom perimeters (61.10) net of three doors (112, 113, 115) give 52.10 LF (+0.45%). GPT-6 Astra computed the same three alternatives and picked this one; it also saw olive runs on the two side walls. Changed: formulas.md F4, CSV row 233, and app-gaps row 3 and change 2. The cove-trim fixture now sums the eight plan walls instead of the legend value. The old candidate 54.4 (+4.9%) was not reproducible: net of two doors the figure is 55.10.
4. **Top trim (234) from plan dimensions.** 39.75 LF (+0.51%) replaces the elevation-scaled 39.04 (−1.3%). The fixture dropped the unused `measured_lf` and its 1.5% tolerance, and now runs at 1.0%.
5. **GR-3 scope in best-practices §8.** Corrected to WT-1 + WT-2 + WT-9 = 244.13 SF (ratio 1.229 is the ceil-50 step). WT-3 is scheduled under GR-1.
6. **FT-1 wording.** "Porcelain" was removed. A-170 and estimate line 222 both say ceramic tile, and spec p283 says only "Standard grade".
7. **Engine mat assembly.** `flooring.ts` `mat` also takes `recessedFrame`, and with it emits `mat-frame:<tag>` = 2 × (W + H) × count LF. app-gaps row 5 and gap 2 now say the perimeter exists only as a recessed-frame line, not as `transition:<FTS-n>`.
8. **Geometry-check count.** Six became eight (seven rows, plus the cove-trim composition), and all eight are now within 1%.

Points where the review was not followed literally:

- README has no explicit "unresolved" list at the cited lines 105–108. The cited claims sat in the geometry table and in the CSV and formulas notes, and were fixed there.
- The WT-8 fixture keeps its 1.0% tolerance for a −0.87% result. That is the precision of two runs scaled from the markup.
- Elevation A prints 7'-3 1/2" while the plan depth of the same wall is 7'-8 1/8". The estimator followed the elevation, and this drawing conflict is recorded in CSV row 228.

The line-level reconciliation is unchanged at 17 of 18 within 1%. `build.py` predates these fixes; the edited CSV and fixtures supersede its output.
