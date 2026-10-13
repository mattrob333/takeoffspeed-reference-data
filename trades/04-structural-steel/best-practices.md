# Structural steel, joists, deck and miscellaneous metals: takeoff best practices

Scope: quantities and material types only. No pricing, labor or productivity.

Local paths are relative to `this repository` unless they start with `/home/user/work` or `/home/user/TakeoffSpeed`.

## 0. Source quality and gaps (read first)

- The web-search budget was exhausted before I could search for estimating handbooks, so every web source below was fetched directly by URL. No RSMeans, no estimator blog posts with percentages, no AISC Code of Standard Practice (403), no BIA Technical Note 31B for lintels (404), no AGA surface-area table (not on the pages I reached), no SDI RD/SD standard text (paywalled; only the standards index was readable).
- The strongest sources I did read in full: the Steel Joist Institute specification SJI 100-2025, the joist manufacturer's Code of Standard Practice section on ESTIMATING (reproduced in the Vulcraft joist manual), the Vulcraft 2026 deck catalog, the OSHA joist-erection and fixed-ladder rules, and the project's own drawings and specification.
- Claims that carry no web link come from one of three places, and I say which: the project files (local path cited), my own arithmetic (marked "computed"), or general estimating convention for which I did not retrieve a source (marked "convention, no source retrieved").
- Section 9 is a second opinion from GPT-6 Astra. It is not independently sourced. Treat its numbers as hypotheses to test against a reference job, not as rules.
- The reference job is a single-storey bank branch. Its steel is HSS-heavy (815 LF of HSS), has KCS joists, and has a canopy frame. Do not generalise percentages from one job.

## 1. What the estimator takes off, and in what units

The reference estimate (`reference/estimate/lines.json`, DIV 05, lines 36-80) is the unit convention a working estimator used on this job. Quantities only:

| Element | How the line is carried | Unit | Reference qty |
|---|---|---|---:|
| HSS / W / C columns, beams, braces | One line per shape and role (COLUMN, BEAM, CHANNEL, BRACING), shape designation in the description | LF | 36 lines, e.g. HSS6x6x3/8 column 236.34 LF |
| Angles (lintel-type, edge, posts) | One line per angle size; short pieces carried as count x length summed to LF | LF | L4x3x1/4 179.93 LF; L2x2x3/16 77.67 LF |
| Bridging and bracing | Angle size and type (X-type, horizontal) | LF | L2-1/2x2-1/2x1/4 X-type 314.8 LF |
| Open-web joists | One line per designation | LF | 12KCS2 53.96; 16KCS3 248.55; 18KCS2 108.49 |
| Roof deck | Profile, gauge, finish, one line | SF | 2,208.37 SF (22 ga, G90) |
| Base and cap plates | Plate size and thickness, count | EA | six sizes, 2 to 16 EA each |
| Roof access ladder | One assembly with its components listed | EA | 1 |
| Bollards (Div 32, not Div 05) | Diameter, height, fill, finish | EA | 5 (dumpster) and 8 (bank standard) |

Observations from the reference estimate and markups (computed in section 8):

- Members, joists and deck are carried as net length or net plan area. No waste, no tonnage and no weight appear on the lines.
- The estimator sums legend rows from several markup pages into one line when the shape matches (C7x9.8 channel: 236.7 + 14.0 + 177.8 = 428.5 LF against 428.46 LF carried).
- Short repeated pieces are measured as count x length: 18 EA of L2x2x3/16 at 4'-0" plus 1 EA at 5'-8" is 77.67 LF, which is exactly the line quantity.
- A "*2" in a markup legend name means two parallel runs (top and bottom chord). Bridging 314.8 LF is (35.5 + 121.9) x 2.

Industry convention is different from the unit column above. The joist maker's own estimating section lists scope by item rather than by LF, and steel is conventionally reported by weight (that last point is convention, no source retrieved) ([SJI COSP Section 5, ESTIMATING](https://www.vulcraft.com/catalogs/JoistGirder/Vulcraft-Steel-Joist-Joist-Girder-Systems-Manual-V2020.3J.pdf), PDF pp. 92-93). A complete takeoff therefore records, for each member, the shape designation, the cut length and the count, so that weight can be computed from a published section table. Weight per foot is part of the designation for W shapes (W12x14 is 14 lb/ft) and channels (C7x9.8 is 9.8 lb/ft); it is not part of the designation for HSS or angles, which need a table lookup (convention, no source retrieved; the AISC shapes database was not reachable).

## 2. Which sheets and spec sections drive it

Reference job sheet map (`reference/markups/pages.json`, `reference/sheets/index.json`):

| Source | What it drives |
|---|---|
| S-203 Roof Framing Plan | Joists (designation, spacing, direction), beams, channels around roof units, bridging symbols, deck direction, SLAB AND DECK SCHEDULE (deck mark RD-1.5) |
| S-301 | Columns, diagonal bracing, more channels and beams |
| S-201 | Column base plates, anchor bolts, footing/pier schedule |
| S-001 to S-003 | General notes: DECKING NOTES, STRUCTURAL STEEL NOTES, STEEL BAR JOIST NOTES, galvanizing rule, bearing and base plate defaults, special inspection |
| S-600 series | Typical details: bearing plates, base plates, lintel schedule, deck edge, joist bearing, bridging |
| A-110, A-200, A-401, A-450 | HSS tube posts at the canopy, roof access ladder (1/A312, 3/A450), bollards, canopy edge |
| Spec 05 1200 STRUCTURAL STEEL FRAMING (PDF p. 84) | Grades, connection standards, special framing rules |
| Spec 05 2100 STEEL JOIST FRAMING (p. 96) | Bridging, strut joists, openings, welds |
| Spec 05 3000 STEEL ROOF DECKING (p. 100) | Deck gauge, laps, fastening, closures |
| Spec 05 5000 METAL FABRICATIONS (p. 113) | Shelf angles, ladders, bollards, loose lintels, galvanizing and priming |
| Spec 05 4000 COLD-FORMED METAL FRAMING (p. 104) | Outside this trade's takeoff, but the canopy stud framing meets the steel on S-203 (the estimate carries it under Div 09) |

Rules that matter for reading the drawings:

- Which of the drawing and the spec governs when they disagree is a contract question. Estimate the drawing value and flag the conflict. This job has several (section 5.3).
- Joist and deck suppliers produce placement plans and shop drawings; the bid takeoff is made from the structural plans ([SJI COSP Section 5.1, plans for bidding](https://www.vulcraft.com/catalogs/JoistGirder/Vulcraft-Steel-Joist-Joist-Girder-Systems-Manual-V2020.3J.pdf)). The joist maker's bridging layout is final; if the engineer shows bridging, it is for reference only ([SJI FAQ, bridging](https://steeljoist.org/faqs/topic/bridging/)). On this job the engineer shows bridging as a plan symbol and a note, and the estimator measured it, so both views exist.

## 3. Standard measurement rules

### 3.1 Members (W, HSS, channel, angle, plate)

- Measure each member by designation and length, with count. Carry the designation exactly as drawn. The designation fixes the weight for W shapes and channels (convention; see section 1).
- Measure the member as detailed, not grid to grid. Where a beam frames to a column face, the cut length is the clear dimension plus any end plate or setback; where it sits on a column cap, the length runs over the column (convention, no source retrieved).
- Do not deduct bolt holes, copes or small cutouts from weight (convention, no source retrieved; GPT also states this, section 9).
- HSS columns: height is base-plate top to the framing it carries, not floor to floor. Check this against sections. Reference: HSS4x4x1/4 posts at 1'-4" high are carried as 6 EA x 1.333 ft = 8.0 LF in the 13.6 LF line (computed, section 8).
- Steel is specified by grade per shape family. This job: W shapes and channels ASTM A992 Gr 50, HSS ASTM A500 (Fy = 46 ksi), everything else A36 (`trades/04-structural-steel/scripts/research/steel_spec_084.txt`, spec 05 1200 2.1.A). Separate lines or tonnage by grade when the spec splits them. For background on the grades, see [Wikipedia, Structural steel](https://en.wikipedia.org/wiki/Structural_steel) and [Wikipedia, Hollow structural section](https://en.wikipedia.org/wiki/Hollow_structural_section) (A500 is the common HSS grade; A1085 is a newer, tighter-tolerance standard).
- Steel density for any computed weight: 484 to 503 lb/ft3 per [Wikipedia, Steel](https://en.wikipedia.org/wiki/Steel); 490 lb/ft3 (0.2836 lb/in3) is the standard working value (the 490 figure is convention; the range is sourced). Plate weight is therefore length x width x thickness (in3) x 0.2836 lb/in3 (computed).

### 3.2 Open-web steel joists

- Designation reading: nominal depth in inches, series letters (K, LH, DLH), section number. "18K4" is 18 in. deep, K-series, section 4. The depth is taken at mid-span ([SJI 100-2025, designation text](https://steeljoist.org/wp-content/uploads/2026/03/SJI_100_K-LH-DLH-JG_Final_050126.pdf)). K-Series covers depths 10 to 30 in. and spans to 60 ft; LH covers 18 to 48 in. and spans to 96 ft; DLH covers 52 to 120 in. and spans to 240 ft (same document; also [Wikipedia, Open web steel joist](https://en.wikipedia.org/wiki/Open_web_steel_joist)).
- KCS is a K-Series variant for constant shear and moment (rooftop units, concentrated loads). Designations run section 1 to 5, depths 10 to 30 in., maximum uniform capacity 550 plf ASD or 825 plf LRFD, and the load/load alternate designation cannot be used with it ([SJI 100-2025](https://steeljoist.org/wp-content/uploads/2026/03/SJI_100_K-LH-DLH-JG_Final_050126.pdf); [Vulcraft products, standard joists](https://www.vulcraft.com/products/standardjoist)).
- Length: carry joist LF as the plan shows it, count joists by designation, and note any extended ends or sloped bearing. SJI 100 defines span in Figure 5.2-1; I did not extract that definition, so confirm whether the plan length is clear span or bearing to bearing. The manufacturer's weight table gives approximate pounds per foot "that do not include accessories" ([Vulcraft joist manual, KCS load table, PDF p. 157](https://www.vulcraft.com/catalogs/JoistGirder/Vulcraft-Steel-Joist-Joist-Girder-Systems-Manual-V2020.3J.pdf)).
- Weights read from that table for this job's designations: 12KCS2 = 8.0 plf, 16KCS3 = 10.5 plf, 18KCS2 = 9.0 plf. Applied to the carried lengths that is 4,018 lb, about 2.0 tons (computed, section 8).
- Bearing seats: standard seat depth 2-1/2 in. for K1-12, 5 in. for LH02-17 and 7-1/2 in. for LH18-25 and DLH. Standard clear bearing length is 4 in. for K and 6 in. for LH/DLH; minimum bearing on steel is 2-1/2 in. for K ([SJI 100-2025, Tables 5.4-1 and 5.4-3](https://steeljoist.org/wp-content/uploads/2026/03/SJI_100_K-LH-DLH-JG_Final_050126.pdf)). These matter to the takeoff only through the support: the supporting beam flange or bearing plate must be wide enough, and joists that cannot get bearing must be staggered (S-001 STEEL BAR JOIST NOTES, note 3).

### 3.3 Bridging

- SJI requires top and bottom chord bridging, horizontal or diagonal. The number of rows of top chord bridging comes from Table 5.5-1 by section number and span, and bottom chord rows must be at least the number of top chord rows ([SJI 100-2025, Section 5.5](https://steeljoist.org/wp-content/uploads/2026/03/SJI_100_K-LH-DLH-JG_Final_050126.pdf); same table in the [Vulcraft Bridging Guide](https://www.vulcraft.com/catalogs/JoistGirder/Vulcraft-Bridging-Guide-2020.pdf)).
- K-Series rows by span (feet), from the table, for the sections this job uses:

| Section | Depth | 1 row | 2 rows | 3 rows |
|---|---|---|---|---|
| K5 (12KCS2 maps here) | 12K to 24K | up to 20 | over 20 to 30 | over 30 to 42 |
| K6 (18KCS2) | 14K to 24K | up to 20 | over 20 to 31 | over 31 to 42 |
| K9 (16KCS3) | 16K to 24K | up to 22 | over 22 to 34 | over 34 to 48 |

  The KCS load table gives the equivalent K section ("Bridging Table Section Number": 12KCS2 is 5, 16KCS3 is 9, 18KCS2 is 6) and says the KCS designation itself is not used to set bridging ([Vulcraft joist manual, KCS table, p. 157](https://www.vulcraft.com/catalogs/JoistGirder/Vulcraft-Steel-Joist-Joist-Girder-Systems-Manual-V2020.3J.pdf)). The same table lists 35-0 ft as the span at which 18KCS2 needs bolted diagonal erection bridging; 12KCS2 and 16KCS3 show NA.
- Erection bridging: where the span reaches the table value, the row nearest mid-span must be bolted diagonal, installed before the hoisting lines are released. Over 60 ft, all rows are bolted diagonal; over 60 ft to 100 ft needs two bolted rows near the third points ([OSHA 1926.757(d)](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.757); [Vulcraft Bridging Guide](https://www.vulcraft.com/catalogs/JoistGirder/Vulcraft-Bridging-Guide-2020.pdf)).
- Uplift: where wind uplift governs, a single line of bottom chord bridging goes near the first bottom chord panel point ([SJI 100-2025, 5.12](https://steeljoist.org/wp-content/uploads/2026/03/SJI_100_K-LH-DLH-JG_Final_050126.pdf)). This job's note says it directly: "at the end of each roof joist provide a continuous row of bridging at the last bottom chord panel point for uplift, typical at each end" (S-001 STEEL BAR JOIST NOTES, note 7). That is a bridging line at each end of every roof joist, in addition to the span rows.
- Anchorage: every bridging line must be anchored at its ends by a beam, wall anchor or X-bridging termination ([SJI FAQ, bridging](https://steeljoist.org/faqs/topic/bridging/)). Bridging anchors and anchorage are not in the joist maker's scope; the specifying professional shows the termination ([SJI COSP in the Vulcraft manual, Sections 5.2(b) and 6.1](https://www.vulcraft.com/catalogs/JoistGirder/Vulcraft-Steel-Joist-Joist-Girder-Systems-Manual-V2020.3J.pdf)).
- Quantity geometry (computed): horizontal bridging is one continuous angle per row run across the joists, so LF per row = number of joist spaces x joist spacing (plus the run to the anchor). X-bridging is two diagonals per joist space, each sqrt(spacing^2 + depth^2), where depth is the vertical distance between chord attachments. Do not count bridging along the joist span.
- Job rule: the plan notes ask for "continuous horizontal rigid bracing at top and bottom chord of joist, add X-type bridging in the first panel and at every sixth panel" (S-203 notes; spec 05 2100 2.3.C and 2.3.D). The estimator carried 121.9 ft of rigid bracing (x2 for top and bottom) and 35.5 ft of additional X bridging (x2), both as L2-1/2x2-1/2x1/4, for 314.8 LF.

### 3.4 Roof deck

- Measure deck as net plan SF of the area to be covered: roof plan area bounded by the framing, with openings deducted where sheets are omitted and with the deck turning down at edges only if detailed. Reference: the line is 2,208.37 SF and the markup legend is 2,208.4 SF, so net plan area with no lap or waste (computed, section 8).
- Sheet purchase differs from net coverage: side laps are inside the cover width (the catalog's cover width is the net width), and end laps are extra. The purchase takeoff is sheet count x length, not SF.
- B-deck (1.5 in. deep) is rolled with 30 in. or 36 in. cover widths in gauges 24, 22, 20, 19, 18 and 16 ([Vulcraft Deck Solutions 2026, product offer, PDF p. 6](https://www.vulcraft.com/catalogs/Deck/VulcraftDeckSolutions_2026.pdf)). S-203's schedule reads: 1-1/2 in. wide rib Type B, 22 ga (t = 0.0295 in.), G90, Gr 50, 5/8 in. puddle welds with welding washers, 36/4 pattern at end and intermediate supports, 12 in. o.c. at the perimeter, #10 TEK side-lap screws at 18 in. o.c. maximum, minimum end lap 4 in. at supports only.
- Deck edge, opening framing: openings over 12 in. square get 4x3x1/4 angles, long leg down, and the same for roof drains (spec 05 3000 2.3 and 05 2100 2.5). The spec calls for framing only above that 12 in. threshold. Deck on a different plane than its support gets a 3/16 in. bent plate (spec 05 1200 2.1.G and S-001 note 12).
- Weight of 22 ga 1.5B deck is 1.6 psf and 20 ga is 2.0 psf; base metal thickness 0.0295 in. and 0.0358 in. ([Vulcraft Deck Solutions 2026, 1.5B section properties](https://www.vulcraft.com/catalogs/Deck/VulcraftDeckSolutions_2026.pdf), PDF p. 78). For 2,208.37 SF at 22 ga: 3,533 lb, 1.77 tons (computed).

### 3.5 Base plates, cap plates, anchor bolts and connections

- Count plates by size and thickness, then compute weight from plate volume. Reference plate schedule: 5x5x1/4 (6), 12x12x3/4 (10), 14x14x1 (4), 15x18x3/4 (4), 11x5-1/2x3/4 cap (2), 12x6-1/2x3/4 cap (16), about 1,060 lb in total (computed, section 8).
- Defaults on the general notes apply to every column and bearing without its own detail: base plate with (4) 3/4 in. diameter x 14 in. anchor bolts, and 5/8x12x7-1/2 in. bearing plates on 1 in. grout with (2) 3/4 in. anchor bolts under beams bearing on masonry (S-001 STRUCTURAL STEEL NOTES 3 and 4). Anchor rods are ASTM F1554 (spec 05 1200 2.1.C). The anchor bolts are set in the concrete trade's work; count them but note who furnishes.
- Caps: 1/2 in. cap plate where a roof member does not frame over a column (tubes and pipes); 1/4 in. cap plate at HSS outlooker ends (S-001 notes 14 and 16).
- Connections that are not detailed: allow a percentage of member weight and say so. No published percentage came from a source I could retrieve. The app engine uses 10 percent with a stated range of 7.5-10 percent for simple shear framing and 12-15 percent for braced or moment frames (`TakeoffSpeed repo: lib/quantities/trades/structure/structural-steel.ts`, convention `structural-steel.connection-pct`). That is the engine's stated basis, not a retrieved source. Credit measured plates against the allowance so they are not counted twice.
- Bolts: A325 for bolted connections unless noted; A307 only for bolts set in concrete (spec 05 1200 2.1.B and 2.1.D). Welds: E70 electrodes, AWS D1.1 (spec 05 1200 2.1.E). Joist end welds: 1/8 in. x 2 in. fillet each side for roof joists (spec 05 2100 3.1.D). OSHA's minimum for K-Series end attachment is two 1/8 in. fillet welds 1 in. long, or two 1/2 in. bolts ([OSHA 1926.757(b)](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.757)).

### 3.6 Miscellaneous metals

- Loose lintels: one angle or shape per opening, length = clear span + bearing at each end. Spec 05 5000 2.10.B sets bearing at 1/12 of the clear span, not less than 8 in. each side; S-600 lintel notes say bear all lintels a minimum of 8 in. at each end. Galvanize lintels in exterior walls. These are furnished under Div 05 and installed under Div 04 (spec 05 5000 1.1.B).
- Shelf angles: LF of angle as sized, mitered and welded at corners, open joints at expansion and control joints about 2 in. larger than the joint; galvanize when in exterior walls (spec 05 5000 2.7).
- Roof access ladder: spec 05 5000 2.8 describes a steel ladder (16 in. between siderails, 3/8x2-1/2 in. flat-bar siderails, 3/4 in. diameter rungs, brackets not more than 60 in. o.c., galvanized, ANSI A14.3). The OSHA fixed-ladder rule gives rungs 10 to 14 in. o.c., 16 in. clear rung width, siderails extending 42 in. above the landing, and 7 in. clearance behind the rungs ([OSHA 1910.23](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.23)). The estimate carries an aluminum ladder with wall brackets and safety post (EA 1.0, A110, 3/A450). That is a drawing-versus-spec difference; carry the drawing and flag it. Count ladder as EA, then list rungs (height / rung spacing), siderail LF, brackets (height / 60 in. rounded up, plus top and bottom) and safety post as components (computed from the spec numbers).
- Bollards: Schedule 40 steel pipe, 1/4 in. steel cap plate, filled with concrete, anchored 8 in. minimum into formed or core-drilled holes (spec 05 5000 2.9 and 3.3). A 6 in. Schedule 40 pipe is 6.625 in. outside diameter with 0.280 in. wall and 18.97 lb/ft ([Engineering ToolBox, steel pipe dimensions](https://www.engineeringtoolbox.com/steel-pipes-dimensions-d_43.html)). Concrete fill per foot is pi/4 x 6.065^2 in2 = 0.2006 ft2, so a 5 ft bollard holds about 1.0 CF and a 6.5 ft total length (5 ft plus embedment) about 1.3 CF of fill, before concrete in the footing hole (computed). Pipe, cap, fill, footing hole and finish (paint or wrap) are each separate lines.
- Steel angle and channel framing at rooftop units: "provide C5x6.7 framing at the perimeter of each roof unit, maximum span of channel 7'-6", with wood blocking between deck and channel" (spec 05 1200 2.1.O). The reference estimate carries C5x6.7 at 53.35 LF; channel framing for the roof hatch is also called for on S-203.
- Elevator rail tubes (spec 05 1200 2.1.P, T.S. 6x6x1/4 vertical tube at each rail location) apply only if the project has an elevator. The estimate has no elevator line, so none are carried.

### 3.7 Finishes and coatings

- The structural general notes say all exterior exposed steel is galvanized G90 unless the architect says otherwise (S-001 STRUCTURAL STEEL NOTES, note 17). Spec 05 5000 requires ASTM A123 galvanizing for other iron and steel products and ASTM A153 for hardware, and shop priming with a universal primer on items not galvanized, except items embedded in concrete or masonry (spec 05 5000 2.12). The AGA separates A123 (single pieces or fabrications) from A153 (fasteners and small centrifuged hardware) ([AGA, coating specifications](https://galvanizeit.org/specification-and-inspection/coating-specifications)).
- Quantity basis for coating: galvanizing is by weight of fabricated steel, so the takeoff needs tonnage by item, flagged galvanized or not. Primer or paint is by surface area, which for sections comes from the section perimeter times length (convention, no source retrieved).
- Deck: G90 is the zinc coating class on the sheet. Do not add a separate galvanizing quantity to coil-coated or galvanized deck ([Vulcraft Deck Solutions 2026, finish notes](https://www.vulcraft.com/catalogs/Deck/VulcraftDeckSolutions_2026.pdf); the catalog lists G90 and painted finishes as options).
- Touch-up: field welds on shop-primed steel are touched up with the same paint, and galvanized damage is repaired with high-zinc paint (spec 05 5000 3.4 and spec 05 3000 3.3). Carry touch-up as a lump or per weld LF only if the estimate separates it.

## 4. Coverage, yield and waste factors, with their basis

| Factor | Value | Basis |
|---|---|---|
| Steel density | 484-503 lb/ft3; 490 working value | [Wikipedia, Steel](https://en.wikipedia.org/wiki/Steel) for the range; 490 is convention |
| 22 ga 1.5B deck weight | 1.6 psf; t = 0.0295 in. | [Vulcraft Deck Solutions 2026](https://www.vulcraft.com/catalogs/Deck/VulcraftDeckSolutions_2026.pdf), PDF p. 78 |
| 20 ga 1.5B deck weight | 2.0 psf; t = 0.0358 in. | same |
| B-deck cover width | 30 in. or 36 in. | same, PDF p. 6 |
| Deck end lap | 4 in. on this job (drawing); 2-1/2 in. in the spec; the engine assumes 2 in. | S-203 schedule; spec 05 3000 2.1.C; engine convention `structural-steel.deck-end-lap-in` (SDI source not retrieved) |
| Deck support fastening | 36/4 pattern, 5/8 in. puddle welds with washers; 12 in. o.c. at perimeter | S-203 schedule. Spec says welds at 6 in. o.c. at all bearing points (spec 05 3000 3.1.C) |
| Side-lap fastening | #10 TEK screws at 18 in. o.c. maximum (drawing); self-tapping #10 at 6 in. o.c. or button-punched interlock (spec) | S-203; spec 05 3000 3.1.F. Side-lap types are nested, interlocking (weld or button punch) or screwed ([SDI FAQ](https://sdi.org/resources/faqs/)) |
| Deck bearing on supports | 2 in. minimum | spec 05 3000 3.1.G |
| Deck closures | Profile closures of steel (20 ga with 1 in. return lip) or neoprene (1 in. strips); end closures 20 ga | [Vulcraft Deck Solutions 2026, accessories, PDF p. 11](https://www.vulcraft.com/catalogs/Deck/VulcraftDeckSolutions_2026.pdf) |
| Deck accessories named by SDI | Ridge caps, flat plates and sump pans | [SDI FAQ](https://sdi.org/resources/faqs/) |
| Welding washers | Not less than 1 in. diameter and 1/16 in. thick; may be omitted on 22 ga with a testing letter | spec 05 3000 2.2 |
| Joist bridging rows | By span and section, Table 5.5-1 | [SJI 100-2025](https://steeljoist.org/wp-content/uploads/2026/03/SJI_100_K-LH-DLH-JG_Final_050126.pdf) |
| Joist weight | Approximate plf from the load table, excluding accessories | [Vulcraft joist manual, p. 157](https://www.vulcraft.com/catalogs/JoistGirder/Vulcraft-Steel-Joist-Joist-Girder-Systems-Manual-V2020.3J.pdf) |
| Joist headers | Furnished by the joist maker when the joist end reaction is 10,000 lb or less; not above that | [SJI COSP 2.8 in the Vulcraft manual](https://www.vulcraft.com/catalogs/JoistGirder/Vulcraft-Steel-Joist-Joist-Girder-Systems-Manual-V2020.3J.pdf), PDF p. 90 |
| Connection allowance | 10 percent of member weight in the engine; 7.5-10 percent simple shear, 12-15 percent braced or moment | engine convention only; no retrieved source |
| Member cutting waste | 5 percent in the engine; 3-5 percent repetitive, 5-10 percent short mixed HSS (GPT, hypothesis) | engine convention and section 9; no retrieved source |
| Deck cut waste | 5 percent in the engine; 3-5 percent simple, 5-10 percent irregular (GPT, hypothesis) | same |
| Grout under plates | 0.42-0.45 CF per 50 lb bag; 10 percent waste | engine convention only |

Reference-job evidence on waste: the estimate carries net quantities. Joists, deck, columns and beams all equal the markup legends to within rounding, so any waste or tonnage factor is applied later by the estimator or supplier. If your output must match this estimate's lines, apply no waste to member, joist or deck LF and SF.

Deck arithmetic that follows from the S-203 schedule (computed, assuming the 36/4 pattern means 4 welds across the 36 in. sheet width at each support, which is standard SDI notation but which I did not find defined in the sources I could read):

- Support welds: 4 per 3 ft of support line, 1.333 per LF of support line, or (4/3)/p per SF where p is the support spacing in feet.
- Side-lap screws at 18 in. o.c.: 0.667 per LF of side lap; with 3 ft sheets, about 0.222 per SF before edge corrections.
- End lap of 4 in. adds 0.333 SF per LF of lap line (computed).

## 5. Material breakdown an estimator lists

### 5.1 Primary materials

- Structural steel shapes by designation and grade: W, C, L, HSS (square, rectangular, round), plate, flat bar. Carry LF and count; add weight when it is needed.
- Open-web joists by designation and span; joist girders if drawn; extended ends and ceiling extensions where shown; headers within the maker's scope ([SJI COSP Section 5.2](https://www.vulcraft.com/catalogs/JoistGirder/Vulcraft-Steel-Joist-Joist-Girder-Systems-Manual-V2020.3J.pdf)).
- Roof deck by profile, gauge, finish and grade (1-1/2 in. Type B, 22 ga, G90, 50 ksi).
- Miscellaneous metals: lintels, shelf angles, ladders, bollards, supports for equipment and coiling grilles (spec 05 5000 1.1).

### 5.2 Accessories that follow from the primaries

| Primary | Follows from it |
|---|---|
| Joists | Bridging (horizontal angle, X-bridging angle), bridging clips and bolts for erection bridging, bridging anchors or end terminations (by others), bearing plates and anchor bolts at masonry, strut-joist bolts and slotted bearing plates (spec 05 2100 2.2 and 3.1.A), opening headers, uplift bridging at each end |
| Joist scope that the maker does not furnish | Slab reinforcement, decking and its attachments, miscellaneous framing between joists for openings, loose bearing plates and anchors, erection bolts, horizontal bracing from joist to joist or to walls, bridging anchors, wood nailers, moment plates, shear studs ([SJI COSP 5.2(c) in the Vulcraft manual](https://www.vulcraft.com/catalogs/JoistGirder/Vulcraft-Steel-Joist-Joist-Girder-Systems-Manual-V2020.3J.pdf), PDF p. 93) |
| Roof deck | Welding washers, puddle welds, side-lap screws or button punches, profile and end closures, edge and opening angles (4x3x1/4), cant or bent plates where deck planes change, pour stops (on floor deck), ridge and flat plates, sump pans at drains |
| Columns | Base plates, anchor rods with nuts and washers, grout, cap plates, shear tabs or clip angles, splice plates |
| Beams | Shop-welded or bolted connection material, bearing plates on masonry, stiffeners |
| Roof units | C5x6.7 perimeter channel (span 7'-6" max), wood blocking between deck and channel, hatch framing |
| Lintels | Bearing at each end, galvanizing, built-in anchors (by Div 04) |
| Bollards | Concrete fill, anchor embedment hole, grout in annular space, cap plate, paint or wrap |
| Ladder | Rungs, siderails, wall brackets, safety post, galvanizing or anodizing |
| All steel | Galvanizing or shop primer, field touch-up paint, welds, bolts A325/A307, testing and inspection (special inspection table on S-003: deck welds and side laps inspected periodically) |

### 5.3 Conflicts between drawing and spec on this job (carry the drawing, flag the rest)

| Item | Drawing | Spec | Estimate carries |
|---|---|---|---|
| Deck gauge | 22 ga, t = 0.0295 in. (S-203) | 20 ga (spec 05 3000 2.1.A) | 22 ga |
| End lap | 4 in. min at supports | 2-1/2 in. min | not carried |
| Side-lap fastener spacing | 18 in. o.c. #10 TEK | 6 in. o.c. | not carried |
| Support weld spacing | 36/4, 12 in. o.c. at perimeter | 6 in. o.c. at all bearing points | not carried |
| Ladder | aluminum (estimate source line) | steel, galvanized (spec 05 5000 2.8) | aluminum |
| Spec section number | S-002 submittals list "05 3100 STEEL DECKING" | Section is 05 3000 | n/a |

## 6. Common mistakes and how to check a takeoff

1. Missing opening and edge framing. Roof openings over 12 in. square, roof drains, hatch and unit perimeters, and roof-level changes all need their own angles or channels. Check by walking every opening on the mechanical and plumbing roof plans against S-203.
2. Counting bridging along the span. Bridging runs across joists. On this job bridging is 314.8 LF against 411.0 LF of joist, a ratio of 0.77 (computed); test any job against its own rows and spacing rather than against that ratio.
3. Missing the uplift row. S-001 note 7 adds a bottom chord bridging line at each end of every roof joist.
4. Double counting connection allowance. Measured base and cap plates, bearing plates and angles must be credited against the percentage allowance.
5. Using nominal rather than detailed length for short HSS pieces. Posts at 1'-4" and 1'-7" high are short enough that a few inches changes the line by more than 5 percent.
6. Confusing coverage with purchase. Deck net coverage SF is not the sheet order. End laps (4 in. here) add to the order, side laps do not.
7. Missing galvanizing. S-001 note 17 makes all exposed exterior steel G90; the canopy HSS, the ladder, lintels in exterior walls, shelf angles and bollards all inherit it.
8. Losing items assigned elsewhere. Anchor bolts and embeds are set by the concrete trade; lintels are installed by masonry; elevator tubes and equipment supports can sit in Div 05 or in the equipment trade. Say who furnishes and who installs on each line (spec 05 5000 1.1.B).
9. Missing the same shape on a second sheet. The same shape appears on S-203 and S-301 and must be summed (C7x9.8 appears on markup pages 34, 35 and 36).
10. Quoting weight for joists with accessories. The maker's plf excludes accessories; bridging, extensions and headers add weight ([Vulcraft joist manual, p. 157](https://www.vulcraft.com/catalogs/JoistGirder/Vulcraft-Steel-Joist-Joist-Girder-Systems-Manual-V2020.3J.pdf)).

Reasonableness checks (computed on this job):

- Length reconciliation: legend rows sum to the estimate line within rounding for every member shape that appears in the markup legends, with one item to note: HSS4x4x1/4 column (13.6 carried against 5.6 on the legend, the other 8.0 being the six 1'-4" posts on S-203). HSS6x4x3/8 beam is not an exception: the p34 legend has two rows with the same name (22.2 and 9.0 FT), and the estimator keeps them as two lines (22.24 and 8.98).
- Weight screen, partial: W shapes 4,079 lb (2.04 tons), channels 4,838 lb (2.42 tons), KCS joists 4,018 lb (2.01 tons), 22 ga deck 3,533 lb (1.77 tons), angles about 2,957 lb (5 sizes, area-based approximation without fillets), plates about 1,060 lb: about 20,485 lb or 10.2 tons before any HSS. That is about 9.3 psf of deck area before HSS, and the job carries 815 LF of HSS, so the finished figure is well above that. A typical-frame psf screen (GPT suggests 6-12 psf, section 9) does not fit a small, column-dense building with a canopy frame; use the screen only to flag order-of-magnitude errors.
- Quantity-per-area check: deck SF should be close to the roof plan area inside the framing minus the openings, and it should not be less than the plan area under joists. Joist LF divided by deck SF is 411.0 / 2,208.37 = 0.19 LF per SF, which means an average joist spacing near 5.4 ft if all joists run the full roof (computed; check against the plan spacing).

## 7. What an AI takeoff must read from the drawings and specs

From the structural drawings (S-001 to S-003, S-201, S-203, S-301, S-600 series):

- Every framing mark on S-203 and S-301: shape designation exactly as written (HSS6x6x3/8, W12x14, C7x9.8, L4x3x1/4 LLV), and the role (column, beam, brace, outlooker, post).
- Joist designations, spans, spacing and direction; strut joists (S.J.); joists with extended ends; bearing conditions (on steel, on masonry); bridging notes (A.X. additional X bridging, rigid horizontal bracing, H.B. horizontal brace angle).
- Deck: profile, gauge, finish, grade, attachment pattern, laps, direction arrows; openings and unit weights.
- Plate and anchor schedules; base plate types on S-201; the default notes for columns and masonry bearings; cap plates.
- General notes that add scope: galvanizing (note 17), uplift bridging (joist note 7), 3/16 in. bent plate where deck planes change (note 12), headed studs and elevator closure angles if an elevator exists.
- Typical details that fix lengths: lintel schedule and bearing (8 in. minimum), deck edge, bearing seats, joist-to-wall connections.

From the specification (05 1200, 05 2100, 05 3000, 05 5000):

- Grades per shape family; bolt and weld standards; any grade split that changes tonnage categories.
- Opening framing rules (12 in. square threshold), strut joist ends, bridging sizes (3/4 in. angle for floor diagonal bridging; X brace in the first panel and every sixth panel where horizontal bridging is used on roofs).
- Deck gauge, galvanizing class, laps and fastening, with the conflicts against the drawings listed.
- Metal fabrications: what is included (shelf angles, ladders, bollards, loose lintels) and who installs.
- Coating requirements: galvanizing standards and shop primer.

From the architectural, civil and mechanical sheets:

- A-110, A-200, A-401, A-450 for canopy posts, ladder, hatch, bollards and roof curbs; mechanical roof plans for unit and opening locations that need framing; civil C-3.0 and C-4 for dumpster bollards and gates.

How the AI should behave:

- Output shape designations as drawn, with source sheet. Do not invent weights; take W and C weights from the designation and look up HSS and angle weights, or mark them "weight to be taken from the section table".
- Report net quantities and state which allowances (connections, waste, laps) it has not applied. This job's estimate is net.
- Resolve drawing versus spec conflicts explicitly and show both values.
- Cross-check every count-times-length line (posts, short angles) with the dimension on the detail, and sum identical shapes across sheets.

## 8. Reference-job reconciliation (computed in Python, scratch at `trades/04-structural-steel/scripts/research/steel/`)

| Check | Computation | Result vs estimate |
|---|---|---|
| X-type bridging | (35.5 + 121.9) x 2 | 314.8 LF, equals line 65 |
| L2x2x3/16 angles | 18 x 4.0 + 5.667 | 77.67 LF, equals line 67 |
| HSS4x4x1/4 column | 6 x 1.333 + 5.6 | 13.6 LF, equals line 37 |
| HSS1-1/2 tube posts | 6 x 1.583 | 9.50 LF vs 9.48 (rounding of height) |
| C7x9.8 channel | 236.7 + 14.0 + 177.8 | 428.5 vs 428.46 |
| HSS6x6x3/8 column | 61.4 + 175.0 | 236.4 vs 236.34 |
| W10x12 beam | 51.5 + 4.8 | 56.3 vs 56.26 |
| Deck | legend 2,208.4 SF | line 2,208.37 SF |
| Joists | legend 54.0, 248.6, 108.5 | lines 53.96, 248.55, 108.49 |
| Weights | W 4,078.6 lb; C 4,838.2 lb; KCS 4,017.9 lb | 2.04, 2.42, 2.01 tons |
| Deck weight | 2,208.37 SF x 1.6 psf | 3,533 lb |
| Angles (area-based, no fillets) | L2x2x3/16 2.43 lb/ft; L3x3x3/16 3.71; L4x3x1/4 5.74; L3x3x1/4 4.89; L2-1/2x2-1/2x1/4 4.04 | about 2,957 lb total |
| Plates | volume x 0.2836 lb/in3 | 1,060 lb total |
| Bollard fill, 6 in. Sch 40 | pi/4 x 6.065^2 / 144 x 5 ft | 1.00 CF |

The app engine (`structural-steel.ts`, `steel-shapes.ts`) already carries members, plates, joists, bridging, deck, railing and misc assemblies, with a 10 percent connection allowance and 5 percent waste classes by default. Two defaults to review against this job: the engine's deck end lap is 2 in. while S-203 asks for 4 in. minimum and the spec 2-1/2 in., and the engine's 5 percent member and deck waste would put the engine above this estimate, which is net.

## 9. Second opinion (GPT-6 Astra, not independently sourced)

Proposed conventions to test, each marked by the model as either standard or its own rule of thumb. Not facts.

- Do not deduct bolt holes, ordinary copes or minor notches from member weight; record major cutouts separately. Plate weight is volume in in3 x 0.283 lb/in3.
- Connection allowance on primary member weight, excluding deck and joists: 5-10 percent for conventional W-shape simple framing, 10-15 percent for HSS-heavy, moment or gusset-intensive framing. Credit measured plates against it.
- Member purchase waste: 3-5 percent for repetitive W, channel and angle work; 5-10 percent for short, mixed HSS cuts. Deck cut waste: 3-5 percent on simple rectangular roofs, 5-10 percent on irregular roofs, excluding end laps.
- A 4 in. end lap adds 0.333 SF per LF of lap line, about 1.7 percent for repeated 20 ft sheet runs.
- Bridging budget shortcut: 1, 2 or 3 rows for spans up to 20, over 20 to 30 and over 30 to 40 ft. The SJI table above overrides this and is close for K3 and K4 (1 row to 18 or 20 ft, 2 rows to 26 or 30 ft, 3 rows to 40 or 41 ft).
- Horizontal bridging about 2 x rows x spacing LF per joist; X-bridging about 2 x rows x sqrt(spacing^2 + depth^2) per joist.
- 36/4 attachment: (4/3) / p welds per SF for support spacing p in feet; #10 screws at 18 in. o.c.: about 0.222 per SF (these match section 4's arithmetic).
- Reasonableness screen of 6-12 psf total frame, joists, bridging, connections and deck per roof SF. As shown in section 6, this job exceeds that range before HSS is added, so the screen is a prompt to look, not a rule.
- Five mistakes it named: missing opening framing, duplicate connection allowances, bridging counted along spans, confusing deck coverage with purchased area, using plan area on sloped roofs.

Check against the SJI table: GPT's 3-row limit of 40 ft is within 2 ft of the table for K5 and K6 (3 rows to 42 ft), but the shortcut stops at 40 ft while the table adds a fourth row above 42 ft for these sections. Use the table.

## 10. Reference list

Web (all fetched directly):

- [SJI 100-2025, Standard Specification for K, LH, DLH Joists and Joist Girders](https://steeljoist.org/wp-content/uploads/2026/03/SJI_100_K-LH-DLH-JG_Final_050126.pdf)
- [SJI FAQ, bridging](https://steeljoist.org/faqs/topic/bridging/)
- [SJI FAQ, joists](https://steeljoist.org/faqs/topic/joists/)
- [Vulcraft Steel Joist and Joist Girder Systems Manual V2020.3J (includes SJI COSP and KCS load tables)](https://www.vulcraft.com/catalogs/JoistGirder/Vulcraft-Steel-Joist-Joist-Girder-Systems-Manual-V2020.3J.pdf)
- [Vulcraft Bridging Guide 2020](https://www.vulcraft.com/catalogs/JoistGirder/Vulcraft-Bridging-Guide-2020.pdf)
- [Vulcraft Deck Solutions 2026](https://www.vulcraft.com/catalogs/Deck/VulcraftDeckSolutions_2026.pdf)
- [Vulcraft, standard joists](https://www.vulcraft.com/products/standardjoist) and [roof deck](https://www.vulcraft.com/products/roofdeck)
- [SDI FAQs](https://sdi.org/resources/faqs/) and [SDI standards index](https://sdi.org/codes-standards/sdi-standards/) (ANSI/SDI RD-2017 and SD-2022 exist; text not read)
- [OSHA 1926.757, open web steel joists](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.757)
- [OSHA 1910.23, ladders](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.23)
- [AGA, coating specifications](https://galvanizeit.org/specification-and-inspection/coating-specifications)
- [Engineering ToolBox, steel pipe dimensions](https://www.engineeringtoolbox.com/steel-pipes-dimensions-d_43.html)
- [Wikipedia, Steel](https://en.wikipedia.org/wiki/Steel), [Structural steel](https://en.wikipedia.org/wiki/Structural_steel), [Hollow structural section](https://en.wikipedia.org/wiki/Hollow_structural_section), [Open web steel joist](https://en.wikipedia.org/wiki/Open_web_steel_joist)
- [STACK, structural steel takeoff page](https://www.stackct.com/blog/structural-steel-estimating/) (confirms LF and count units in takeoff software; no percentages)

Project files:

- `reference/estimate/lines.json` (DIV 05 lines 36-80; Div 32 lines 674 and 713)
- `reference/markups/legends.json` (pages 34-36, S-203 and S-301)
- `reference/sheets/spec_index.json`
- `text/S-001.txt`, `S-002.txt`, `S-003.txt`, `S-203.txt`, `S-301.txt`
- `trades/04-structural-steel/scripts/research/steel_spec_084.txt` (05 1200), `steel_spec_096.txt` (05 2100), `steel_spec_100.txt` (05 3000), `steel_spec_113.txt` (05 5000)
- Engine for comparison: `TakeoffSpeed repo: lib/quantities/trades/structure/structural-steel.ts` and `steel-shapes.ts`
- Downloaded vendor PDFs and extracted text: `trades/04-structural-steel/scripts/research/steel_src/`
