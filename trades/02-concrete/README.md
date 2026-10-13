# 02 — Concrete: slab, footings, stem walls, pads, joints, formwork

Job: single-storey bank branch, Fifth Third Bank, Watson Blvd., Warner Robins GA (Praxis3 project 26302;
structural engineer Mark Nannis). Building area is 1,892 SF actual and 1,900 GSF (G-001).

## Scope (15 estimate lines, 16–30)

| Line | Item | Unit | Estimator qty | Class |
|---|---|---|---:|---|
| 16 | 4" SOG w/ 6x6 W2.9xW2.9 WWF o/ vapor barrier o/ 4" gravel | SF | 1917.6 | measured |
| 17 | 1/2" isolation joint | LF | 39.22 | measured |
| 18 | 1" saw-cut joint | LF | 364.11 | measured |
| 19 | 2'Wx1'D continuous footing (WF20) | CY | 9.196296 | derived |
| 20–26 | Isolated footings F30, F38, F50, F60, F70, F7040, F10050 | CY | 1.0 … 6.5 | counted (schedule dims) |
| 27 | 8" stem wall, 2'-0" high | CY | 9.628148 | derived |
| 28 | 10" stem wall (wing walls), 2'-0" high | CY | 0.522593 | derived |
| 29 | 18"x18"x6" cleanout pad | CY | 0.041667 | specified (1 plumbing-scope pad; the 6 civil pads are Div 32 line 658) |
| 30 | Formwork required | SF | 1420 | derived (rolled-up contact area 1413.87 SF; the 10 SF round-up is a hypothesis fitted to this one line) |

Reinforcing steel, under-slab stone and vapor retarder have no separate quantity lines in this estimate.
They appear only as text in the line descriptions. Excavation and backfill belong to 31-earthwork. The 4" CMU
below-grade wythe (line 31) belongs to 03-masonry.

**Result: 15 of 15 lines reconcile within 1%, and all 15 within 5%** (re-checked 2026-10-13; line 30 also passes at −0.43% on the raw contact area, without the rounding hypothesis). Built from the legend values with exact
feet-and-inch dimensions, the largest deviation is −0.78% (line 28). Built with the estimator's own
conventions, every line matches to 0.000%. Those conventions are: decimal feet rounded to 2 places, the
carried LF values, and formwork rounded up to 10 SF. The formwork rounding is fitted from this single line, so treat it
as a hypothesis. The reproducible quantity is the raw contact area (1413.87 SF from the legend inputs). See `reconciliation.csv`.

## Driving sheets

| Sheet | Markup page | Use |
|---|---|---|
| **S-201** Structural Plan – Foundation | **p33** | Every measured item. The slab area, WF20 runs, both stem walls, both joint types and the footing-tag counts are all marked up here. It also carries the SPREAD FOOTING SCHEDULE, WALL FOOTING SCHEDULE, SLAB AND DECK SCHEDULE (SOG-4) and the Foundation Plan Notes. |
| **S-600** Wall Sections – Foundation | p37 (no legend) | Stem wall 8" with #4 @ 10" and #4 dowels @ 18". 1/2" joint filler at the slab edge. Detail 6 "Section at Foundation and Wing Wall" shows a **10 3/4"** wing-wall stem. S-201 also prints `10 3/4"` on the plan at the south stub, beside the 6/S-600 "At Wing Wall" callout. The footing is 1'-0" thick. |
| **S-680** Typical Details (Foundation) | — | 3/S-680 sawcut joint at 1/4 "T" (1" in a 4" slab). 8/S-680 isolation joint at column base plates, "NOMAFLEX" or equal, around diamond blockouts. |
| S-001 / S-002 General Notes | — | Slab-on-grade notes 3 and 6: 4", 3000 psi, flat-sheet WWF 6x6-W2.9xW2.9, on a vapor barrier. Joint spacing is ≤ 15 ft on S-001 but ≤ 12'-6" on S-201. Concrete strengths are 3000 psi for SOG and for foundations and piers (S-002). Cover is 3" at footings. |
| **P-302** Plumbing Domestic Floor Plan | **p57** | General note 3: "ALL OUTSIDE CLEANOUTS SHALL BE BROUGHT TO GRADE AND EMBEDDED IN 18"X18"X6" THICK CONCRETE PAD". The single legend count dot sits on this note. P-301 repeats the note. |
| C-5.0 Utility Plan | p77 | 6 EA SANITARY CLEANOUTS. They belong to site work: Div 33 line 729 carries the 6 cleanouts, and Div 32 line 658 carries their 6 pads (18"x18"x8", 13.5 SF, ref C-3.0). They are **not** part of line 29. |

## Specification sections (source/specifications.pdf)

| Section | Pages | Requirements that bear on quantity or description |
|---|---|---|
| 03 2000 Concrete Reinforcement | 45–48 | ASTM A615 Gr 60 bars (p46). WWF to ASTM A185 (p46). WWF lapped 6" both ways, wired at 18" o.c., and kept within 2" of slab edges (p47). Cover 3" in footings and 3" for walls cast against earth (p47). Bar supports at ≤ 4'-0" o.c. (p47). |
| 03 3000 Cast-in-Place Concrete | 49–66 | Formwork to ACI 347; PS-1 plyform, Class II, exterior, mill-oiled (p55, p57). Control joints are 24 ga galvanized keyed type, ½" less than slab depth (p55). Fill for slabs on grade: "#57 stone, 4" thick **where shown on drawings**" (p55). The drawings do not show a stone thickness: S-201 SOG-4 says "ON A GRAVEL BED OR SAND CUSHION AS RECOMMENDED BY THE GEOTECHNICAL REPORT", and S-001 note 6 says "ON A VAPOR BARRIER ON A NON EXPANSIVE FILL SUBGRADE". Curing compound to ASTM C309 Type 1 (p55). Preformed expansion joint filler to ASTM D1751 (ref. p50). WWF 1" clear to the top of the slab (p59). Steel-trowel interior floors (p61). Floor flatness and levelness FF/FL (p62). |
| 07 2616 Below-Grade Vapor Retarders | 162–163 | **15 mil**, ASTM E1745 Class A (Stego Wrap 15 basis of design). Lap 6" and tape. Lap over footings or seal to the foundation walls. |

## Materials and their specified properties

- **Slab on grade SOG-4**: 4" thick, 3000 psi, 145 pcf. WWF 6x6-W2.9xW2.9 in flat sheets (sheets, not rolls), set 1" clear
  to the top. Placed on a vapor retarder over a gravel bed or sand cushion (S-201) / non-expansive fill (S-001).
  - The estimate line's "4"THK. GRAVEL BED" is the estimator's reading of the conditional spec clause ("4" thick where shown on
    drawings"). It is not drawn. It is a description assumption only, and the SF does not change.
  - The estimate line says "10 MIL VAPOR BARRIER". The spec says **15 mil**. The difference changes the description only, not the SF.
- **WF20 wall footing**: 2'-0" wide × 1'-0" thick, (2) #6 continuous, 3" cover, top of footing at [-2'-0"].
- **Spread footings** (schedule, S-201):

  | Mark | L × W × T | Reinforcement | Count |
  |---|---|---|---:|
  | F30 | 3'-0" × 3'-0" × 1'-0" | 4 #4 E.W. | 3 |
  | F38 | 3'-8" × 3'-8" × 1'-0" | 5 #4 E.W. | 3 |
  | F50 | 5'-0" × 5'-0" × 1'-2" | 5 #5 E.W. | 6 |
  | F60 | 6'-0" × 6'-0" × 1'-4" | 7 #5 E.W. | 1 |
  | F70 | 7'-0" × 7'-0" × 1'-4" | 7 #6 E.W. | 1 |
  | F7040 | 4'-0" × 7'-0" × 1'-4" | 7 #6 SW, 5 #6 LW, top and bottom | 1 |
  | F10050 | 5'-0" × 10'-0" × 1'-2" | 9 #6 SW, 5 #6 LW, top and bottom | 1 |

- **Stem walls**: 8" thick with #4 @ 10" o.c. continuous and #4 dowels @ 18" o.c., 3000 psi. The wing-wall stem is
  drawn 10 3/4" (S-201 plan dimension at the 6/S-600 callout, and 6/S-600 itself) with #4 @ 10" at each face. Height is 2'-0", from top of footing [-2'-0"] to finish floor.
- **Joints**:
  - Saw-cut: cut to T/4 = 1", within 12–24 h of the pour (3/S-680). S-201 limits spacing to ≤ 12'-6" and the panel aspect ratio to ≤ 1.5.
  - Isolation at column bases: ½" "NOMAFLEX" or equal around diamond blockouts (8/S-680).
- **Cleanout pad**: 18" × 18" × 6" thick concrete pad (J.R. Smith 4258 or equal), from P-301/P-302 note 3. The six civil
  cleanouts on C-5.0 already have their pads in Div 32 line 658 (18"x18"x8", 6 EA, 13.5 SF). Do not add them to line 29.

## What the estimator measured (PlanSwift, markup p33 unless noted)

| Legend row | Qty | Unit | Feeds |
|---|---:|---|---|
| 4"THK. CONCRETE SLAB ON GRADE W/ 6x6 W2.9xW2.9 WIRE MESH O/ VAPOR BARRIER O/ GRAVEL BED (teal area) | 1917.6 | SQ FT | 16 |
| ISOLATION JOINT - 8/S680 (medium green) | 39.2 | FT | 17 |
| SAW-CUT JOINT - 3/S680 (yellow) | 364.1 | FT | 18 |
| WF20 (periwinkle) | 124.2 | FT | 19, 30 |
| F30 / F38 / F50 / F60 / F70 / F7040 / F10050 (count dots) | 3/3/6/1/1/1/1 | EA | 20–26, 30 |
| 8"THK. CONCRETE STEM WALL … @ 2'H (slate blue) | 193.8 | FT | 27, 30 |
| 10"THK. CONCRETE STEM WALL … @ 2'H (olive) | 8.4 | FT | 28, 30 |
| 18"x18"x6"THK. CONCRETE PAD FOR CLEAN O… (p57, olive) | 1 | EA | 29, 30 |

The other rows on p33 belong to other trades and are not part of this one:
- BP12, BP1518 and BP14 are base plates (steel).
- "New Count" is 2 EA green dots on the column schedule at columns A-2.9 and C-7.

The estimator took only three kinds of quantity from the markup: area for the slab, length for footings,
walls and joints, and counts for spread footings and the pad. All three-dimensional work was done in the
estimate. CY = LF × section ÷ 27 or count × L × W × D ÷ 27, and formwork = Σ contact area.

## Files

- `formulas.md` — every formula, with a worked example from this job.
- `reconciliation.csv` — one row per estimate line.
- `fixtures.json` — 15 engine test cases.
- `reading-guide.md` — how to read S-201, S-600, S-680 and P-302 for this trade, and the traps.
- `app-gaps.md` — comparison with `lib/quantities/trades/structure/concrete.ts`. It includes an actual engine run on these inputs.

## Verification (2026-10-13)

An adversarial reviewer raised 9 issues. Claude (Opus 5.5) checked each against the sources and recomputed every number in
python (`trades/02-concrete/scripts/verify_review.py`). GPT-6 Astra gave an independent second opinion on the S-201 wing-wall
crop, the stem-line rounding split and the formwork rounding (`trades/02-concrete/scripts/review/gpt-verify-2026-10-13.txt`).

Checks made:
- Estimate lines 29, 436, 658 and 729 were read for quantity and description only.
- P-301 and P-302 notes, and the p57 and p77 legends.
- Spec pages 55, 162 and 163.
- S-201 text and a 5× render at the 6/S-600 callout.
- S-001 note 6.
- The S-201 spread-footing schedule against the line 25 and 26 labels.
- fixtures.json was evaluated against reconciliation.csv. All 15 agree, and all 15 are within tolerance.

What changed:
1. **Cleanout pads (reviewer right).** Div 32 line 658 already carries the six C-5.0 pads (18"x18"x8", 6 EA, 13.5 SF = 6 × 1.5 × 1.5).
   The "count 6 pads under line 29" guidance would double count them, so it is gone from:
   - `reading-guide.md` trap 9
   - `formulas.md` F6
   - reconciliation row 29
   - this README

   `app-gaps.md` item 5 is now a cross-trade de-duplication warning, and the P-402 FCO mention is dropped.
2. **Stem LF and F50 (reviewer right).** `best-practices.md` no longer says "implies 194.97 LF" or "rounded some lines up".
   Both are the 2-decimal-feet convention: 194.0 × 2 × 0.67 / 27 = 9.628148, and 6 × 25 × 1.17 / 27 = 6.500000.
3. **Formwork sum (reviewer right).** `best-practices.md` §3.7 and §8 now include the 3.0 SF of pad edges: 1413.87 SF, −0.43% before rounding.
4. **Vapor retarder (reviewer right).** `best-practices.md` now cites 07 2616:
   - 15 mil, ASTM E1745 Class A, Stego Wrap 15 basis of design
   - 6" taped laps, lapped over the footings
   - roll example: the 15 mil product, 14' x 140', 2 rolls

   The estimate's "10 MIL" is flagged as wrong against the spec. The SF is unaffected.
5. **Footing label order (reviewer right).** The schedule is L × W. Line 25 prints W × L and line 26 prints L × W, so `app-gaps.md` item 6
   now matches on the dimension set.
6. **Ft-in rounding range (reviewer partly right).** The old "−0.6% to +0.4%" was imprecise, but the reviewer's attribution was wrong:
   - On the stem lines most of the deviation is the thickness rounding (−0.50% on line 27, +0.40% on line 28).
   - The LF round-up adds only −0.10% and −1.18%. GPT-6 Astra got the same split.
   - `formulas.md` and `reading-guide.md` now give the split.
7. **Wing wall 10 3/4" (reviewer right).** S-201 itself prints `10 3/4"` beside the 6/S-600 "At Wing Wall" callout. It is now cited alongside 6/S-600 in:
   - this README
   - the reading guide
   - `formulas.md` F5
   - reconciliation row 28
   - the wing-wall fixture (`perDrawings` 0.557407 CY)
8. **Formwork rounding (reviewer right).** ceil10 is now labelled a hypothesis from one line:
   - 1413.87 → ceil10 1420, but nearest-10 gives 1410.
   - 1415.26 → 1420 either way.

   The fixture now carries a `note` and `rawContactSf` 1413.87. The 1% tolerance is the real test.
9. **#57 stone (reviewer right).** The spec clause is "4" thick **where shown on drawings**", and no thickness is drawn (S-201 SOG-4: gravel bed or sand cushion per geotech). The 4" base is now marked as a description assumption.

No quantity, expected value or delta changed. The reconciliation count stays at 15 of 15 within 1%.
