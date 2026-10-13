# Flooring takeoff best practice: floor tile, grout, carpet, resilient, base, transitions, sealed concrete, mats

Scope: quantities and material types only. No pricing, no labor productivity.
Written 2026-10-13 for the 09c-flooring trade (CSI 09 30 00 tiling, 09 65 13 resilient base, 09 65 19 resilient tile, 09 68 13 tile carpeting, plus sealed concrete and floor mats as finish items).

## 0. How to read this document

Every number is graded:

- **PUBLISHED**: a manufacturer data sheet, guide specification or standards-derived spec states it. A link follows.
- **CONVENTION**: estimator practice. No authoritative published figure was reached. Treat as a default the contractor can override, and print the percentage on the takeoff.
- **PROJECT**: taken from this job's drawings, specification or estimate lines. Not general practice.
- **DERIVED**: arithmetic done here (Python) from the inputs shown.

Limits of this research (read before relying on it):

- The web-search budget ran out before the planned searches ran. Everything below comes from direct page and PDF fetches. RSMeans, the TCNA Handbook, ANSI A108/A118 text, CRI 104/105, and the carpet-tile, rubber-base, Schluter, sealer and mat manufacturers' own data sheets were not reachable. Where those matter, a federal or VA guide specification that restates the rule is cited instead.
- No published source was found for waste percentages on carpet tile, LVT/LVP, rubber base or metal trim. They are CONVENTION. A GPT-6 Astra second opinion is recorded where used; it is not a citable source.
- The Schluter stock length (8'2-1/2", 2.5 m) comes from one retailer listing title, not Schluter's own page (Schluter's site returned HTTP 405). Verify before ordering.
- Tile thickness for the project tile (Florida Tile Aventis 24x24) and the project grout joint width were not found in the drawings; the grout figures are therefore ranges.

---

## 1. What an estimator takes off, and in which units

| Item | Measured quantity | Unit | Follows from it (see section 5) |
|---|---|---|---|
| Floor tile (porcelain / ceramic) by finish tag | Net installed area | SF | Tile count or cartons, thinset, grout, membrane, movement-joint sealant, trims |
| Grout by tag (a grout tag can serve several tile tags, floor and wall) | Tile area it fills, then product quantity by joint geometry | SF of tile, then lb or kits | Sealer if specified |
| Carpet tile by tag | Net area per pattern polygon | SF | Tiles (EA), adhesive or connectors, edge/transition trim |
| Broadloom | Net area, then cut layout | SF, then SY or LY of roll | Seams LF, cushion SY, adhesive |
| Resilient tile / plank (VCT, LVT, rubber tile) | Net area | SF | Boxes, adhesive, underlayment/patch |
| Sheet resilient | Net area, then roll layout | SF, then LY | Seam LF, weld rod, integral cove |
| Sealed / polished concrete | Net area | SF | Sealer gallons by coats, joint filler, crack repair |
| Resilient base (rubber, vinyl) | Wall run net of door openings | LF | Coils or 4 ft pieces, corners EA if preformed, adhesive |
| Tile base / bullnose base | Wall run | LF (pieces by piece length) | Corner and end pieces, grout, sealant at floor junction |
| Transitions, thresholds, edge trims (metal, rubber, vinyl, stone) | Interface length | LF, plus EA of pieces | Stick lengths, end caps, miter pieces, bedding mortar |
| Entrance / anti-static / walk-off mats | Count and mat size | EA, with SF of recess | Mat well or recess, frame, edge trim |
| Floor prep (patch, level, underlayment, moisture mitigation, testing) | Area, thickness or test count | SF, bags, EA tests | Often a qualification or allowance rather than a quantity |
| Attic stock | Per spec | boxes, SF or LF | Separate line, never netted into waste |

Notes:

- Estimating software treats tile as SF of material placed, with LF and EA as alternates for trims and pieces ([Estimating Edge, wall ceramic tile take-off](https://www.estimatingedge.com/knowledgebase/wall-ceramic-tile/), blog-level; the page does not describe waste or deductions).
- Keep three numbers apart on every line: net installed quantity, waste or pack rounding, and attic stock. Specs request attic stock as its own deliverable (section 4.5).
- Unit traps: LVT can be metric (25 cm x 1 m is 2.69 SF per plank, DERIVED), carpet is sold by SY or by tile, base by LF, grout by kit or lb, thinset by bag.

## 2. Which sheets and spec sections drive the takeoff

General practice:

- **Finish plan / floor pattern plan** gives the extent of each floor material inside a room (borders, inset patterns, walk-off zones), tile layout start point, transition locations and base tags. This is the primary measurement sheet.
- **Finish legend / finish schedule** gives the tag, product, size, colour and often the grout and base tag. Tags tie area, base and trim together.
- **Dimensioned floor plan** gives wall runs and room extents when the finish plan is not to scale.
- **Door schedule and details** give door widths and thresholds; they locate transitions and break base.
- **Enlarged plans and elevations** (restrooms, casework) give tile base, wall tile, and where base is on casework.
- **Transition and threshold details** give the profile, which fixes the trim product and any underlayment build-up.
- **Specification sections**: 09 30 00 (tile, thinset, grout type, membrane, joints), 09 65 13 (base height, style, corners, accessories), 09 65 19 (resilient tile), 09 68 13 (carpet tile), 09 67 00 / 03 35 00 where resinous or polished concrete is specified.
- The federal guide spec lists the same drivers: installation drawings must show areas, carpet types, pile direction, seam locations and edge-molding locations ([UFGS 09 68 00 §3.4](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2068%2000.pdf), PUBLISHED).

This project (PROJECT):

- Sheet A-150 Finish Plan carries every flooring tag, key notes F001 to F004, general notes, and four transition details (FTS-1 to FTS-4). A-120 is the dimensional floor plan; A-410 enlarged restroom plans carries the wall tile, ceramic bullnose base WT-8 and Schluter trims; A-600 is the door schedule; A-170 is the schedule sheet (`reference/markups/pages.json`).
- Spec sections and pages (`reference/sheets/spec_index.json`): 093000 Tiling p.282; 096513 Resilient Base and Accessories p.304; 096519 Resilient Tile Flooring p.309; 096813 Tile Carpeting p.315. There is no section for sealed concrete or mats in the index.
- Spec says floor tile is TCA F113 thinset on concrete, grout "polymer-modified sanded grout or epoxy grout, as scheduled", crack-suppression membrane "as indicated" ([spec p.288](file://text/spec-p288.txt)). Default tile joint is 1/4 inch unless indicated ([spec p.287](file://text/spec-p287.txt)). Floor transition trim is "as indicated on Drawings" ([spec p.285](file://text/spec-p285.txt)).
- Spec for resilient tile (09 65 19) describes ASTM F1066 VCT, 12 by 12 in., 0.125 in. ([spec p.311](file://text/spec-p311.txt)), while the finish plan schedules LVT-1 as 25 cm x 1 m Interface plank. The drawings' product governs; flag the conflict.
- Spec base is Style A straight where carpet, Style B cove where resilient flooring, 4 in. high, 0.125 in. thick, coils, job-formed inside and outside corners ([spec p.305](file://text/spec-p305.txt)).
- Finish plan general notes A and B say to recheck all measurements and that field verification of quantities is required before ordering; note C centres a doorway material change under the door; note D requires thresholds or transition strips between differing materials ([A-150 text layer](file://text/A-150.txt)).

## 3. Measurement rules

### 3.1 Floor areas

- **Boundary.** Measure net finished area per tag to the finished face of walls (before the base). This is the standard reading of "net installed". The federal specs sit on this assumption: flooring "installed" quantities are accounted per product type, colour and pattern ([UFGS 09 65 00 §1.8](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2065%2000.pdf), PUBLISHED for the per-type accounting; the wall-face boundary is CONVENTION).
- **Split by pattern polygon.** Measure each material polygon separately and subtract insets from the field. On A-150 the carpet field has diamond-shaped insets of other carpet tags; the field area is net of the insets (PROJECT, section 8).
- **Door openings.** Where a finish changes at a door, split at the detailed break. Project note C centres the change under the door ([A-150](file://text/A-150.txt)); the federal guide spec locates mouldings under the door centreline and says they are not required where a threshold is provided ([UFGS 09 65 00 §3.13](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2065%2000.pdf), PUBLISHED). Count the floor in the door opening once, in the material that runs through (CONVENTION).
- **Seam placement at doors (carpet).** Seams at doorways run parallel to and centred under doors, never perpendicular to doors or at pivot points ([UFGS 09 68 00 §3.4.1](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2068%2000.pdf), PUBLISHED).
- **Deductions.** No published threshold exists. Deduct columns, shafts and fixed casework only where the spec or details say flooring does not go beneath them. Do not deduct floor boxes, drains or small penetrations (CONVENTION; GPT-6 Astra recommended a 0 SF threshold, a repo estimator-logic note recommends deducting items over 4 SF, so state the rule used).
- **Loose mats** laid on finished floor do not deduct the floor beneath (CONVENTION, GPT-6 second opinion). A recessed mat does, and adds a recess (section 5.8).
- **Slopes and drains.** Mortar-bed slope to drains is not less than 1/16 in. per foot ([VA 09 30 13 §3.3](https://www.wbdg.org/FFC/VA/VANCAS/VANCA093013.pdf), PUBLISHED). A sloped tile floor needs a bed or leveling quantity that a flat SF line hides.
- **Tile layout.** Specs say lay tile in a grid, centre the field in both directions, and minimise pieces smaller than half a tile ([Daltile 09 30 13 guide spec §3.3](https://digitalassets.daltile.com/content/dam/Daltile/website/resources/trade-professionals/architects-designers/AD_fillableform.pdf), PUBLISHED; same wording in the [project spec p.286](file://text/spec-p286.txt)). Layout drives cut waste (section 4.2).
- **Wainscot** is laid "to dimensions indicated or to next full tile beyond" ([Daltile 09 30 13](https://digitalassets.daltile.com/content/dam/Daltile/website/resources/trade-professionals/architects-designers/AD_fillableform.pdf), PUBLISHED); installed height can exceed the drawn height. This is the wall-finishes trade, see `../09d-wall-finishes/best-practices.md`.
- **Stairs**: treads, risers and nosings count as EA and LF, landings as area (CONVENTION; federal spec lists treads, risers and stringers as separate items, [UFGS 09 65 00 §2.12](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2065%2000.pdf), PUBLISHED). None on this single-storey job.

### 3.2 Base (LF)

- Measure the actual wall run that receives base: room perimeter, minus door and cased openings, plus returns into jambs, plus column and pilaster perimeters. Base does not cross a door (CONVENTION; the spec applies base to "walls, columns, pilasters, casework and cabinets in toe spaces, and other permanent fixtures", [project spec p.307](file://text/spec-p307.txt)).
- Base on casework: include toe-space base only where the spec says so, and do not also count wall base behind the same cabinet (CONVENTION, GPT-6 second opinion; the project spec text above supports including casework toe spaces).
- **Style follows the floor**: Style A straight with carpet, Style B cove with resilient flooring, Style C butt-toe cove with 1/8 in. flooring ([UFGS 09 65 00 §2.10](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2065%2000.pdf), PUBLISHED; same in [project spec p.305](file://text/spec-p305.txt)). Base next to carpet and base next to tile can be different products in one room, so base LF must be split by adjoining floor, not just by room.
- **Corners.** Job-formed corners add no separate item; the federal note recommends job-formed corners because preformed returns are short and get knocked off ([UFGS 09 65 00 §2.10 note](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2065%2000.pdf), PUBLISHED). Job-formed corners use straight pieces with returns of not less than 3 in. and mitred inside corners ([project spec p.307](file://text/spec-p307.txt)). Count inside and outside corners separately as EA only when preformed corners are specified (CONVENTION).
- **Integral cove (sheet goods).** Extends the flooring up the wall 4 or 6 in., with a cap strip and a fillet strip of minimum 3/4 in. radius at the perimeter and fixed vertical interruptions ([UFGS 09 65 00 §2.11](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2065%2000.pdf), PUBLISHED). Quantities: SF of cove goods, LF of cap, LF of fillet.
- **Tile base** has its own trim shapes: base cove, internal corners, external corners (surface bullnose), base cap ([Daltile 09 30 13 §2](https://digitalassets.daltile.com/content/dam/Daltile/website/resources/trade-professionals/architects-designers/AD_fillableform.pdf), PUBLISHED). Take these off as LF plus EA of corner and end pieces.

### 3.3 Transitions, thresholds and trims (LF and EA)

- Provide a transition where flooring terminates higher than the adjacent floor and wherever the material changes; locate it under the door centreline ([UFGS 09 65 00 §3.13](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2065%2000.pdf), PUBLISHED).
- Edge geometry: vertical lip not over 1/4 in.; a change in level between 1/4 and 1/2 in. is bevelled at a slope no steeper than 1:2 ([UFGS 09 65 00 §2.13](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2065%2000.pdf), PUBLISHED). Tile guide specs limit thresholds to 1/2 in. above the adjacent floor with 1:2 bevels ([Daltile 09 30 13 §2.3](https://digitalassets.daltile.com/content/dam/Daltile/website/resources/trade-professionals/architects-designers/AD_fillableform.pdf), PUBLISHED). The project key note F004 repeats the 1/4 to 1/2 in. rule ([A-150](file://text/A-150.txt), PROJECT).
- Stone thresholds are one piece, full width of the door opening, notched to the jamb profile ([VA 09 30 13 §2.8](https://www.wbdg.org/FFC/VA/VANCAS/VANCA093013.pdf), PUBLISHED). Interface length for a door transition is therefore the door opening width, jamb to jamb (CONVENTION).
- Carpet edges meeting hard flooring are protected with moulding ([UFGS 09 68 00 §3.4](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2068%2000.pdf), PUBLISHED).
- Metal trims come in fixed stick lengths and must be mitred at joints and intersections where the drawings say so (project note on every FTS detail, [A-150](file://text/A-150.txt), PROJECT). Order by profile, height, finish and stick length; a 2.5 m (about 8'2-1/2") stick is common ([retailer listing, blog-level](https://www.ceramed.ca/en/products/schluter-jolly-wall-edge-molding-aluminium-white-glossy-1-2-12-5-mm-x-8-2-1-2); verify at Schluter). Round up per run, not on the project total, because offcuts from short runs are not reusable.

## 4. Coverage, yield and waste factors

### 4.1 Thinset mortar (PUBLISHED, one manufacturer)

[Custom Building Products VersaBond HP](https://www.custombuildingproducts.com/products/versabond-hp-high-performance-large-and-heavy-tile-mortar) coverage per 50 lb bag, stated "for estimating purposes":

| Trowel | SF per 50 lb bag |
|---|---|
| 1/4 x 1/4 x 1/4 square notch | 90 to 100 |
| 1/4 x 3/8 x 1/4 square notch | 60 to 67 |
| 1/2 x 1/2 x 1/2 square notch | 42 to 47 (the maker does not recommend this trowel) |
| 3/4 x 9/16 x 3/8 U-notch at 45 degrees | 34 to 38 |
| 3/4 x 9/16 x 3/8 U-notch at 30 degrees | 42 to 47 |

Same page: at least 80 percent mortar contact in dry areas, at least 95 percent in wet areas and exteriors; back-troweling raises usage and should be allowed for. A guide spec requires 95 percent coverage for exterior floors, wet areas, pool decks and laundries ([Daltile 09 30 13 §3.2](https://digitalassets.daltile.com/content/dam/Daltile/website/resources/trade-professionals/architects-designers/AD_fillableform.pdf), PUBLISHED). Large-format tile such as 24 x 24 sits at the low end of the chart or below it. GPT-6 Astra suggested 40 to 50 SF/bag at 1/2 x 1/2 and 30 to 40 with back-buttering (CONVENTION, not citable). The notch must come from the spec or the tile maker; do not default silently.

### 4.2 Tile overage

No standard fixes tile waste. Published guidance is blog-level:

| Layout | Overage | Source |
|---|---|---|
| Straight, large tile | 5 to 7 percent | [Flooring Clarity](https://www.flooringclarity.com/how-much-extra-tile-project/) |
| Straight, medium tile | 7 to 10 percent | same |
| Small tile or mosaic | 10 to 20 percent | same |
| Diagonal or complex | 15 to 25 percent | same |
| Straight or grid, simple (wall calculator) | 10 percent | [DG Floors](https://dgfloors.com/wall-tile-calculator/) |
| Diagonal, patterns, many cut-outs | 15 percent | same |
| Herringbone, mosaic, large-format with big offcuts | 20 percent | same |

Method: net area times (1 plus overage), then round up to whole cartons ([DG Floors](https://dgfloors.com/wall-tile-calculator/)). Small fixtures are not deducted because the allowance absorbs the cuts (same source). State the percentage and the layout reason on the takeoff. GPT-6 Astra gave 10 percent straight and 15 to 20 percent diagonal for 24 x 24 porcelain, consistent with the range above (CONVENTION).

### 4.3 Grout

- **Geometry.** Joint volume per SF = 144 x J x (L + W + J) x D / ((L + J) x (W + J)), cubic inches, for tile L x W, joint J and joint depth D (the tile thickness for a fully filled joint). This is the formula the TakeoffSpeed engine implements (`lib/quantities/trades/interiors/flooring.ts`); a simpler form, 144 x (L + W) x J x D / (L x W), differs by under 5 percent for the sizes below (DERIVED).
- **Manufacturer rule.** Laticrete points to its coverage chart (DS 254.3), says actual coverage varies with job-site conditions, tile size and joint size, and says to "add 10% for waste, spillage and clean-up", plus another 10 to 15 percent for unglazed quarry tile ([LATICRETE SPECTRALOCK PRO data sheet](https://cdnmdm.laticrete.com/ProductAssets/Product%20Documents/lds6850_spectralock-pro-grout-la-en.pdf); the "at least 10 percent" rule is repeated in [Laticrete's grout calculator article](https://www.laticrete.com/blog/2023/october/the-power-of-the-grout-calculator), PUBLISHED). The calculator takes tile dimensions, joint specification and area.
- **Worked numbers** (DERIVED, thickness and joint are illustrative because neither is on the drawings I read):

| Tile | Joint | Depth | Cubic in. per SF | US gal per 1000 SF (net) |
|---|---|---|---|---|
| 24 x 24 | 1/4 in. | 3/8 in. | 1.11 | 4.8 |
| 24 x 24 | 1/8 in. | 3/8 in. | 0.56 | 2.4 |
| 24 x 24 | 1/4 in. | 5/16 in. | 0.92 | 4.0 |
| 3 x 12 | 1/8 in. | 5/16 in. | 2.25 | 9.7 |
| 3 x 12 | 1/16 in. | 5/16 in. | 1.15 | 5.0 |

- Add 10 percent (Laticrete) on top of the net volume. The engine's grout coverage factor of 2.5 times net joint volume (`docs/QUANTITY_ENGINE.md` line 105) is labelled "manufacturer charts"; I could not verify a 2.5 multiplier against a published chart, so treat it as an unverified default and compare against the chosen grout's own chart.
- **Type and joint width.** Unsanded grout is for joints 1/8 in. and narrower, sanded for 1/8 in. and wider ([VA 09 30 13 §2.6](https://www.wbdg.org/FFC/VA/VANCAS/VANCA093013.pdf), PUBLISHED). Epoxy grout is ANSI A118.3 and cement grout A118.7 ([project spec p.284](file://text/spec-p284.txt)). Guide-spec joint widths: porcelain 1/4 or 3/8 in., ceramic mosaic 1/16 or 1/8 in., glazed wall tile 1/16 or 1/8 in., quarry 1/4 or 3/8 in., unless indicated ([Daltile 09 30 13 §3.3](https://digitalassets.daltile.com/content/dam/Daltile/website/resources/trade-professionals/architects-designers/AD_fillableform.pdf), PUBLISHED). VA says porcelain paver joints maximum 1/8 in. ([VA 09 30 13 §3.8](https://www.wbdg.org/FFC/VA/VANCAS/VANCA093013.pdf), PUBLISHED). Specs disagree, so read the project's own joint width.
- **Epoxy kits.** Kits are not standardized sizes. Convert by the product's published coverage, round to whole kits, and include resin, hardener and filler components (CONVENTION, GPT-6 second opinion).

### 4.4 Carpet, resilient, sheet goods

- **Carpet tile** modules and layouts: monolithic, quarter-turn, ashlar, brick, herringbone, random ([UFGS 09 68 00 §3.4.2](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2068%2000.pdf), PUBLISHED). Pattern drives waste: GPT-6 Astra suggested 3 to 5 percent monolithic, 5 to 10 percent ashlar, and warned that rectangular planks (12 x 36, 18 x 36) may not allow quarter-turn without manufacturer approval (CONVENTION; verify with the carpet maker, no published figure reached).
- **Broadloom** roll width is 12 ft (or 6 ft minimum usable width where specified) ([UFGS 09 68 00 §2.1.5](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2068%2000.pdf), PUBLISHED). Breadths run parallel with pile in one direction, patterns match, and corridors under 6 ft wide are laid lengthwise ([UFGS 09 68 00 §3.4.1](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2068%2000.pdf), PUBLISHED). Quantity is by cut layout: drops = ceil(room width across the roll / roll width), each drop = run length plus trim allowance (and pattern repeat), converted to SY. SF divided by 9 under-orders because the roll cannot be cut to the room.
- **Resilient tile and plank** (LVT, VCT): 5 to 10 percent for plank is a CONVENTION (GPT-6 second opinion); order whole cartons.
- **Sheet resilient** minimises seams and avoids cross seams; weld rod follows seam length when heat welding is specified ([UFGS 09 65 00 §3.4 and §2](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2065%2000.pdf), PUBLISHED).
- **Substrate.** Resilient floors need flatness within 3/16 in. in 10 ft ([UFGS 09 65 00 §3.2](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2065%2000.pdf), PUBLISHED). Tile on thinset needs 1/8 in. in 10 ft, and on a mortar bed 1/4 in. in 10 ft ([VA 09 30 13 §3.2](https://www.wbdg.org/FFC/VA/VANCAS/VANCA093013.pdf), PUBLISHED). Fill cracks, holes and depressions with trowelable patching or leveling compound ([project spec p.306](file://text/spec-p306.txt)). Flatness fails drive a patch or leveler quantity (bags = area x average depth / bag yield, from product data; no universal SF allowance exists).
- **Moisture and pH.** Concrete moisture testing per ASTM F1869 or F2170 and alkalinity testing before resilient flooring ([UFGS 09 65 00 §3.3](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2065%2000.pdf), PUBLISHED); the project requires substrate pH between 5 and 9 ([spec p.307](file://text/spec-p307.txt)). Concrete is at least 90 days old before carpet ([UFGS 09 68 00 §3.3](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2068%2000.pdf), PUBLISHED). Test counts and mitigation are qualifications unless the spec lists them.

### 4.5 Base, trims, attic stock

- **Base stock**: 4 ft pieces up to 100 or 120 ft coils; some thermoset rubber base is made only in 4 ft lengths ([UFGS 09 65 00 §2.10 note](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2065%2000.pdf), PUBLISHED). Base is installed in lengths "as long as practical" ([project spec p.307](file://text/spec-p307.txt)). Waste: 5 to 10 percent is a CONVENTION (GPT-6 second opinion; no published figure). Carry LF net, then coils or pieces rounded up.
- **Attic stock, project**: 10 percent of tiling materials ([spec p.282](file://text/spec-p282.txt)); 10 percent of resilient base and accessories ([p.304](file://text/spec-p304.txt)); 10 percent of resilient tile ([p.309](file://text/spec-p309.txt)); 10 percent of carpet tile ([p.315](file://text/spec-p315.txt)).
- **Attic stock, generic references**: tile 3 percent of installed amount ([Daltile guide spec §1.4](https://digitalassets.daltile.com/content/dam/Daltile/website/resources/trade-professionals/architects-designers/AD_fillableform.pdf)); resilient tile 5 per 1000 tiles and sheet 5 SF per 1000 SF, base 20 LF of each type and colour ([UFGS 09 65 00 §1.8](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2065%2000.pdf)); carpet 3 percent of total of each type, pattern and colour ([UFGS 09 68 00 §3.7.1](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2068%2000.pdf)). All are bracketed defaults in guide specs; the project spec's own percentage governs.
- **Trim waste**: no source. GPT-6 Astra gave 5 to 10 percent preliminary and said stock-length cutting, not a percentage, controls it.

### 4.6 Sealed concrete

- Clear topical sealer: 200 to 400 SF per gallon per coat, 1 to 2 coats; gallons = SF x coats / coverage plus loss (CONVENTION, GPT-6 second opinion; product-dependent, take the specified product's data sheet). Densifier is a separate product only if specified. Crack and joint repair and joint filler are separate lines. Remove curing compound or sealer before bonding floors next to it (project spec says substrates are free of curing compounds and sealers, [p.286](file://text/spec-p286.txt)).

## 5. Material breakdown an estimator lists

### 5.1 Floor tile
Field tile by tag (cartons); trim and specials (bullnose, cove, corners, tapered transition tile); latex-portland thinset by bags; grout by tag (cement or epoxy); crack-suppression or waterproof membrane SF when indicated; patch and primer as scoped; movement-joint sealant LF and backer rod where indicated (the spec says form joints during installation and never saw-cut them, [Daltile 09 30 13 §3.3](https://digitalassets.daltile.com/content/dam/Daltile/website/resources/trade-professionals/architects-designers/AD_fillableform.pdf), PUBLISHED); grout sealer if specified (project spec p.285). Movement joints above concrete joints sit directly over them (same source).

### 5.2 Carpet tile
Tiles by tag (EA from SF / tile SF, cartons); releasable or permanent adhesive, or connectors; patch and leveler; edge or transition trims at hard surfaces. Entrance carpet may be tile or a cut mat finished with a tapered vinyl edge ([UFGS 09 68 00 §3.4.3](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2068%2000.pdf), PUBLISHED).

### 5.3 Broadloom
SY by cut layout, cushion SY if separate, seam adhesive or tape LF, adhesive, edge strips LF.

### 5.4 LVT / VCT / rubber tile
Boxes by tag; adhesive for full-spread glue-down ([project spec p.313](file://text/spec-p313.txt)); patch and leveler; underlayment where the detail calls for it (the project's FTS-2 and FTS-4 details show 1/4 in. cement board underlayment over the slab, staggered and seams filled, [A-150](file://text/A-150.txt), PROJECT); transition trims.

### 5.5 Sheet resilient
Roll LY by cut layout, adhesive, heat-weld rod LF, integral cove goods SF, cap strip LF, fillet strip LF.

### 5.6 Base
Base by tag in coils or 4 ft pieces, adhesive, preformed corners EA if specified, caulk at masonry tops ([UFGS 09 65 00 §3.14](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2065%2000.pdf), PUBLISHED).

### 5.7 Transitions
Metal or resilient profile by type, height and finish, in stock lengths; bedding mortar for anchor legs ("secure anchor leg in mortar bond", FTS-4 detail, PROJECT); miter and corner pieces; end caps; or a stone or marble threshold (one piece, door width).

### 5.8 Mats
Count of mats and sizes; recess or well depth and its floor-system build-up where the detail shows one; edge trims; static-dissipative or grounding accessories only when the spec calls for them (CONVENTION, GPT-6 second opinion). Do not use a mat's catalogue size as its takeoff SF without checking: a 36 x 48 in. mat is 12 SF (DERIVED).

### 5.9 Prep and extras
Patching and leveling, primer, underlayment, moisture mitigation, moisture and pH testing, and attic stock. Carry as separate lines or print a qualification (see section 6, mistake 9).

## 6. Common mistakes and how to check a takeoff

1. **Reading product from the spec when the drawings change it.** Check: the finish legend and the spec product agree; where they differ (this job: VCT 12 x 12 in the spec, LVT plank on the plan), the drawings govern and the conflict is flagged.
2. **Double-counting nested patterns.** Check: sum of carpet polygons in a room equals room area less other materials; the field must be net of its insets.
3. **Dividing broadloom SF by 9.** Check: roll LY is at least ceil(room width / roll width) times run length.
4. **Applying room-level waste to the whole job.** Check: waste is per tag and per layout, and attic stock is a separate line.
5. **Base taken as full perimeter.** Check: base LF is below perimeter by the door widths; base style matches the adjoining floor (A with carpet, B with resilient).
6. **Transitions missed or double-counted.** Check: one transition per material change at a door, LF equal to the opening; none where both sides are the same material (the project's own detail table lists four types; every door in the finish plan should resolve to a type or to none).
7. **Trim stick rounding.** Check: sticks = ceil(run LF / stick length) per run, with mitre pieces added.
8. **Grout area equals tile area on the wrong tag.** Check: each grout tag lists the tile tags it serves; floor and wall tile can share one grout tag.
9. **Silent prep and underlayment.** Check: cement board, leveler, moisture mitigation and testing are either quantities or printed exclusions.
10. **Mat sizes and SF mismatch.** Check: mat count times catalogue size against the drawn recess.
11. **Unit confusion.** Check: metric product sizes converted, cartons rounded up, SY versus SF labelled.
12. **Not checking tile and wall-tile sources on other sheets.** Check: base tile (bullnose WT-8) and metal trims on the enlarged restroom sheet are in the flooring takeoff once.

Tie-outs (checks that should hold):

- Sum of floor material areas per room is at most room area plus door strips.
- Tile count is at least net SF / tile SF.
- Base LF is at most the room perimeter.
- Broadloom drops times roll width is at least the room width.
- Net quantities per finish tag equal the finish-plan legend within measurement noise (section 8: all but one tag match to 0.05).

## 7. What an AI takeoff must read from the drawings and specs

From the finish plan and legend:
1. Every floor finish tag with product, size, colour, and which polygons carry it, including nested inset patterns.
2. Base tags and heights per room, and the base type next to each floor.
3. Transition tags (FTS-n), locations, and the detail's profile and build-up (underlayment, anchor leg).
4. Key notes (F001 to F004) and general notes that change measurement: centring the break under the door, miter all trims, field-verify quantities.
5. Layout start point for tile (the plan marks one) and any pattern direction.
6. Grout tag per tile tag; the grout product type (epoxy or cement) and colour.

From details and enlarged plans:
7. Wall-tile and tile-base extents, trim shapes, and where metal trims run on walls.
8. Recessed mat locations, recess depth and frame.

From the specification:
9. Joint width, setting method (TCA method number), membrane scope, grout type.
10. Base height, style, thickness, corner type and length (coil or 4 ft).
11. Resilient tile size and adhesive; carpet tile size, install method, adhesive.
12. Substrate limits: flatness, pH, moisture test method, curing days.
13. Attic stock quantities per section.
14. Whether flooring is required under fixed casework (decides deductions).

Do not invent: product size, tile thickness, joint width, carton coverage and box size are read from product data or the spec. If absent, report SF or LF only and flag the missing fact rather than assuming a default.

## 8. Project cross-check (this job, DERIVED from `reference/estimate/lines.json` and `reference/markups/legends.json`)

Estimate lines 217 to 234 carry flooring, grout, base and transitions as net legend quantities, in SF and LF, with no waste applied, no thinset, no grout product quantity, no underlayment and no attic stock. Net quantities match the two-reader markup legend within 0.05 on every item except one:

| Tag | Markup legend | Estimate line | Note |
|---|---|---|---|
| CON-1 sealed concrete | 68.8 SF | 68.78 SF | Sealer coverage not carried |
| CR-1 carpet tile 12x36 | 131.4 SF | 131.36 SF | |
| CR-2 carpet tile 12x36 | 435.7 SF | 435.67 SF | |
| CR-3 carpet tile 12x36 | 27.1 SF | 27.08 SF | |
| CR-4 walk-off 18x36 | 82.4 SF | 82.42 SF | |
| FT-1 tile 24x24 | 946.1 SF | 946.11 SF | 236.5 tiles; 261 at 10 percent, 273 at 15 percent (DERIVED) |
| LVT-1 plank 25 cm x 1 m | 94.0 SF | 93.95 SF | 34.9 planks at 2.691 SF each |
| MAT-1 | 6.0 SF | 10.0 SF | Estimate shows 36 x 48 in., which is 12 SF; three different numbers |
| WB-1 rubber base 4 in. | 404.7 LF | 404.72 LF | 102 four-foot pieces or 3.4 coils of 120 ft net |
| WT-8 bullnose base | 11.3 LF (A-410) | 11.28 LF | 3 x 12 pieces, about 11 to 12 pieces net |
| FTS-1 | 51.6 LF | 51.63 LF | 7 sticks at 8'2-1/2" |
| FTS-2 | 29.0 LF | 28.99 LF | 4 sticks |
| FTS-3 | 12.2 LF | 12.24 LF | 2 sticks |
| FTS-4 | 10.0 LF | 10.02 LF | 2 sticks |
| Schluter cove trim | 51.9 LF (A-410) | 51.87 LF | 7 sticks |
| Schluter trim | 39.6 LF (A-410) | 39.55 LF | 5 sticks |

Other findings:

- Grout lines are in SF, not product units: GR-1 1050 SF against FT-1 946.11 SF (ratio 1.110) and GR-3 300 SF against wall tile WT-1, WT-2 and WT-9 totalling 244.13 SF (ratio 1.229). Both fit ceil50(1.10 × tile SF) (formulas.md F3); the 1.229 ratio is the round-up step to 50 SF, not a waste factor. WT-3 (transaction bar, 38.42 SF) is not in GR-3: A-170 schedules the transaction bar under GR-1 ("TRANSACTION BAR & FLOOR TILE"), and the estimator's GR-1 fits without it at 10 percent. There is no GR-2 line, though the tags run GR-1 and GR-3; confirm in the finish legend.
- The FTS-2 and FTS-4 details call for 1/4 in. cement board underlayment over the slab under the vinyl plank and the MAT-1 area. No estimate line carries this material (no underlayment line was found in Div 09). Its area would follow from LVT-1 (93.95 SF) and the MAT-1 footprint.
- The carpet total including walk-off is 676.53 SF (DERIVED) and carpet tile count is about 199 12x36 tiles plus 19 18x36 tiles net.
- Attic stock of 10 percent applies to tile (about 94.6 SF of FT-1), base, resilient tile and carpet tile per the project spec; none is carried.
- The plan shows insets of CR-1, CR-3 and CR-2 inside the carpet field; the legend's areas are the net polygons, which is the correct treatment.

## 9. App-engine alignment (for comparison; the engine is not edited)

The engine in `lib/quantities/trades/interiors/flooring.ts` already follows most of this: one record per finish tag, trowel-driven thinset bags, joint-volume grout, roll cut layouts for broadloom and sheet, base net of doors with returns and optional preformed corners, and adhesive by coverage. Gaps against this document:

- Grout multiplier of 2.5 is unverified against published charts (section 4.3).
- No transition stick-length rounding or miter pieces; no cement-board underlayment tied to a transition detail; no attic-stock lines from the spec (section 4.5).
- Waste by layout (diagonal, ashlar) and rectangular-plank layout restrictions are manufacturer-dependent and need explicit inputs.
- The 4 SF casework or column deduction threshold in `docs/commercial-v2/estimator-logic/flooring.md` is a convention without a source here.

## 10. Open items to close with a follow-up search

- TCNA Handbook movement-joint (EJ171) spacing and ANSI A108.02 flatness text for large-format tile.
- Carpet tile maker (Interface, Mohawk, Mannington) guidance on waste, planks and quarter-turn.
- Rubber-base maker data (Johnsonite/Tarkett, Roppe, Flexco) on coil lengths, premolded corner leg length and carton counts.
- Schluter data sheets for SCHIENE, RENO-U, RENO-RAMP and RENO-TK stick lengths.
- Epoxy grout maker's coverage chart for 24 x 24 at the project joint width, and the project tile's thickness.
- Sealer data sheet for the specified clear product on CON-1.
- An RSMeans or comparable published flooring measurement rule set for floor areas under doors and casework.
