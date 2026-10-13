# Concrete takeoff best practices: slab on grade, footings, stem walls, pads, joints, formwork

Scope: quantities and material types only. No pricing, labor or productivity.

## 0. Source quality and gaps (read first)

- The web-search budget was exhausted before the research finished. Every source below was fetched directly and read. Several sources I wanted were not reachable: RSMeans, ACI 302.1R and ACI 301 text, the CRSI Manual of Standard Practice, NRMCA CIPs, the ICC code viewer (403) and ASTM pages (403).
- Section 9 is a second opinion from GPT-6 Astra. It is not independently sourced. Treat every number in it as a hypothesis to test against the reference job, not as a rule.
- Measurement conventions stated without a link (no deduction for rebar, measure footings on the centreline, deduct blockouts, SFCA definition, thickened-slab add-ons) are general estimating practice. I did not retrieve a source for them.
- Where a claim has no link, it comes from the project's own drawings, specification or estimate and cites a local file.
- The reference data lives in `this repository`. Local citations use paths relative to it.

## 1. What the estimator takes off, and in what units

The reference estimate (`reference/estimate/lines.json`, DIV 03 lines 16-30) shows the unit convention used by a working estimator on this job:

| Element | Description carried on the line | Unit | Qty |
|---|---|---|---:|
| Slab on grade | 4" slab, 6x6-W2.9xW2.9 mesh, "10 mil" vapor barrier (the spec requires 15 mil), 4" gravel bed (one line) | SF | 1917.6 |
| Isolation joint | 1/2" | LF | 39.22 |
| Saw-cut joint | 1" deep | LF | 364.11 |
| Continuous footing | 2'W x 1'D with (2) #6 | CY | 9.196 |
| Isolated footings | one line per size (3x3, 3'8", 5x5, 6x6, 7x7, 7x4, 5x10) with bar schedule | CY | 1.0 to 6.5 each |
| Stem wall | 8" with #4 @ 10" + #4 dowels @ 18"; 10" with #4 @ 10" | CY | 9.628; 0.523 |
| Pad | 18x18x6 cleanout pad | CY | 0.042 |
| Formwork | "FORMWORK REQUIRED" (one lump line) | SF | 1420 |
| Under-slab insulation (Div 07) | 2" XPS | SF | 2298 |

Conventions this shows:

- Slabs are carried in SF (area) with the build-up in the description. The CY would be area x thickness / 27, so 1917.6 SF at 4" is 23.67 CY. The estimator did not list it.
- Footings, stem walls and pads are carried in CY.
- Joints are carried in LF.
- Formwork is carried in SF of contact area (SFCA).
- Rebar is not a separate tonnage line in this estimate. The bars are described inside each footing and wall line. A standalone rebar takeoff (LF by bar size, then weight, then tons) is still the usual practice.
- Mesh (WWF) is described inside the slab line and is not given in sheets or rolls.
- Excavation and backfill for footings (Div 31, 119.8 CY and 83.7 CY) are separate lines. Concrete is not net of them.

Standard concrete-trade units per general estimating practice:

- Concrete volume: cubic yards. A slab or footing is length x width x thickness in feet, then divided by 27 ([Concrete Network calculator](https://www.concretenetwork.com/concrete/howmuch/calculator.htm)).
- Quick slab check: for a 4" slab, SF / 81 = CY ([Concrete Network](https://www.concretenetwork.com/concrete/howmuch/calculator.htm)).
- Non-concrete materials are counted separately: anchors, rebar, rolls of mesh ([Procore, concrete takeoff](https://www.procore.com/library/concrete-takeoff)).

Rebar bar sizes and unit weights for converting LF to pounds ([Wikipedia, Rebar](https://en.wikipedia.org/wiki/Rebar)):

| Bar | lb/ft | Diameter (in) |
|---|---:|---:|
| #3 | 0.376 | 0.375 |
| #4 | 0.668 | 0.500 |
| #5 | 1.043 | 0.625 |
| #6 | 1.502 | 0.750 |
| #7 | 2.044 | 0.875 |
| #8 | 2.670 | 1.000 |

## 2. Sheets and spec sections that drive it (this job)

| Source | What it supplies |
|---|---|
| `S-201` Foundation plan (`text/S-201.txt`) | Footing marks (F30, F38, F50, F60, F70, F7040, F10050), wall footing WF20, stem wall extents, saw-cut joint (S.C.J.) and isolation-joint locations, dummy-joint dowel bars, joint-spacing note |
| `S-001` / `S-002` General notes | Concrete notes: cover, slab-on-grade build-up and strength, joint rules, truck-dock and dumpster slab rule, hook rule, wall footing default |
| `S-600` Wall sections (foundation) | Wall footing 1'-0" deep, 2 #6 continuous, 3" clear, #4 @ 10" max, 1/2" joint filler, WWF in flat sheets |
| `S-680` Typical details (foundation) | Column and footing detail, base-plate grout bed, pier reinforcing, 3/S680 saw-cut joint, 8/S680 isolation joint, 1/2" smooth dowel @ 18" at the floor joint |
| `P-301` / `P-302` Plumbing foundation and floor plans | Cleanout pads (18x18x6) |
| `A-110` Floor plan | Masonry stem wall (4" CMU, grout cavity solid) belongs to masonry, not concrete |
| `A-190`, `C-3.0`, `C-6.0`, `A-401`, `E-012` | Site concrete: dumpster slab and footing, sidewalk, curb, transformer pad, bollard and light-pole footings. These sit in Div 32, outside this trade folder. |
| `G-003` | Insulation section referenced by the under-slab XPS line |
| Spec 03 2000 Concrete Reinforcement (`text/spec-p045.txt` to `spec-p048.txt`) | Grade, laps, bar supports, cover, mesh lap |
| Spec 03 3000 Cast-in-Place Concrete (`spec-p049.txt` to `spec-p066.txt`) | Mix, form materials, control joint inserts, #57 stone fill, curing, joints |
| Spec 07 2616 Below-Grade Vapor Retarders (`spec-p162.txt`, `spec-p163.txt`) | 15 mil, ASTM E1745 Class A, Stego Wrap 15 basis of design, 6" taped laps, lap over footings |

Verified facts from the project documents:

- Slab on grade at the building is 4" thick, 3000 psi, with flat sheets of 6x6-W2.9xW2.9 mesh on a vapor barrier over non-expansive fill (S-001 slab-on-grade note 6). The estimate adds "10 mil vapor barrier" and "4" gravel bed".
  - The drawings say only "vapor barrier", but spec 07 2616 sets the product: "Multilayer polyolefin sheet material complying with ASTM E 1745, Class A. 15 mil thickness", basis of design Stego Wrap 15 (`spec-p162.txt`).
  - Spec 07 2616 also requires joints overlapped 6" and sealed with tape, and the retarder lapped over the footings or sealed to the foundation walls (`spec-p163.txt`).
  - The estimate's "10 MIL" text is therefore wrong against the spec. The SF is unaffected.
  - The "4" gravel bed" is the estimator's reading of a conditional spec clause ("4" thick where shown on drawings"). No thickness is drawn: S-201 SOG-4 says "ON A GRAVEL BED OR SAND CUSHION AS RECOMMENDED BY THE GEOTECHNICAL REPORT". Treat it as a description assumption. The SF does not change.
- The dumpster slab is 6" thick, 4000 psi (S-001 note 7). The estimate describes it as #4 @ 12" and a 10 mil vapor barrier in Div 32.
- Spec 03 3000 requires "#57 stone, 4" thick where shown" as slab fill (`spec-p055.txt`).
- Spec 03 3000 requires 24 gauge galvanized keyed control-joint inserts, held with 1" x 1/8" ribbed stakes at 1'-0" o.c., with the joint 1/2" less in depth than the slab (`spec-p055.txt`).
- Spec 03 2000 requires mesh lapped 6" at both side and end laps, wired at 18" o.c., extending to within 2" of the slab edges (`spec-p047.txt`).
- Spec 03 2000 requires bar supports at 4'-0" o.c. maximum, the first within 1'-0" of the end (`spec-p047.txt`).
- Spec 03 2000 requires cover of 3" for footings, 3" where cast against earth, and 3/4" for slabs (`spec-p047.txt`).
- Spec 03 2000 requires continuous bars to be lapped 30 diameters (`spec-p047.txt`).
- Spec 03 2000 requires steel to be ASTM A615 Grade 60 (`spec-p046.txt`).
- Spec 03 2000 requires dowels to be wired in place before the pour (`spec-p047.txt`).
- The S-001 note that a hook is "in addition to the length given" is a bar-length rule (S-001 concrete note 3).
- Formwork is the contractor's design to ACI 347 (`spec-p057.txt`). Round column forms are Sonotube (`spec-p055.txt`).

Conflicts a takeoff must resolve and flag:

- S-001 limits joint spacing to 15 ft. S-201 limits it to 12'-6". Both state a 1.5 maximum panel aspect ratio. The sheet closest to the work (S-201) governs, but the estimator measured actual S.C.J. lines, not a derived grid.
- The mesh lap is 6" in the project spec. The UFGS rule of cross-wire spacing plus 2" gives 8" for 6x6 mesh. The project spec governs.
- Weld-wire mesh "in flat sheets" is a project requirement (S-600, S-001). A roll quantity is therefore the wrong purchase unit here.

## 3. Standard measurement rules

### 3.1 Concrete volume

- Volume = L x W x D / 27 per element. Compute from the schedule dimensions (footing mark x count), not from scaled outlines ([Concrete Network](https://www.concretenetwork.com/concrete/howmuch/calculator.htm)).
- Rebar volume is not deducted. Rebar, mesh, chamfers and pipe sleeves are ignored in net concrete volume. This is general practice and I did not find a link for it. The reference estimate behaves this way: footing CY equals pure geometry (see section 8).
- Stem wall: length x thickness x height, with height taken from top of footing to top of wall. Continuous footings are measured as LF x width x depth. At intersections and corners, measure along the centreline of the footing run. Where the drawings step the footing, take each step height separately (S-001 allows footing step-offs of 2'-0" vertical, spaced not less than 4'-0").
- Spread (isolated) footing: count by mark. The mark schedule gives size, depth and bar count.
- Strip footings are commonly 2 to 3 times wider than the wall above ([Wikipedia, Shallow foundation](https://en.wikipedia.org/wiki/Shallow_foundation)). Use this only as a sanity check on a scaled width.
- Piers: the base-plate detail on S-680 adds a pier when the footing is more than 2'-0" below the floor. Volume = pier width x depth x height. These are easy to miss.

### 3.2 Slab on grade

- Area: net slab area from the foundation or architectural plan. Deduct openings (blockouts for equipment pits, floor depressions) as shown. Add thickened-slab areas, steps and slab-edge thickenings as separate volume.
- Slab depth: verify the thickness note per area. The same job has 4" (building), 6" (dumpster) and 8" (truck-dock rule) slabs.
- Thickness rule of thumb for ordering: add 1/4" to the thickness for the concrete budget ([Concrete Network](https://www.concretenetwork.com/concrete/howmuch/calculator.htm)). This covers subgrade variation. It is an order allowance, not a net quantity.

### 3.3 Reinforcing

- Rebar: measured as length per bar mark x count, converted to pounds with the weights in section 1 and to tons. Lap splices and hooks are added to the scheduled lengths.
- Hooks: on this job the hook is added to the stated length (S-001 concrete note 3).
- Laps: the project spec laps continuous bars 30 diameters (`spec-p047.txt`). The app engine assumes 40 diameters when no schedule is given (`TakeoffSpeed repo: lib/quantities/trades/structure/concrete.ts`, convention `concrete.lap-bar-diameters`).
- Welded wire mesh: overlap the cross-wire spacing plus 2" per the federal guide spec ([UFGS 03 30 00 section 3.5.6](https://nibs-s3-wbdg3-production.s3.us-east-1.amazonaws.com/FFC/DOD/UFGS/UFGS%2003%2030%2000.pdf)). The project spec says 6" and governs (`spec-p047.txt`).
- Mesh is made as sheets up to about 50 ft long or rolls up to 600 ft, and up to about 12 ft wide ([Wire Reinforcement Institute FAQ](https://wirereinforcementinstitute.org/welded-wire-reinforcement/welded-wire-faqs)). Net sheet coverage is (width - lap) x (length - lap).
- Cutting mesh at joints: the federal guide spec cuts 50 percent of the mesh on the exact line of each control joint ([UFGS 03 30 00 section 3.11.3](https://nibs-s3-wbdg3-production.s3.us-east-1.amazonaws.com/FFC/DOD/UFGS/UFGS%2003%2030%2000.pdf)). S-201 says to discontinue mesh at keyed construction joints (`S-201.txt`).
- Dowels and extra bars: S-201 calls for 2 #4 x 3'-0" bars at intersections of dummy joints where the joint is not continuous. This is a counted item with no linear run, and an AI will miss it unless it reads the plan notes.

### 3.4 Joints

- Saw-cut (contraction) joints: measured in LF along each S.C.J. line on S-201. Conventional saw cuts are one-fourth the slab depth ([ACI FAQ 915](https://www.concrete.org/tools/frequentlyaskedquestions.aspx?faqid=915)). For the 4" slab that is a 1" cut, matching the estimator's "1" saw-cut joint" line.
- Saw-cut timing is typically 4 to 12 hours after placement, shorter in hot weather ([ACI FAQ 915](https://www.concrete.org/tools/frequentlyaskedquestions.aspx?faqid=915)). The project detail says 12 to 24 hours (S-680 text). This affects the schedule, not the quantity.
- Isolation joints: measured in LF at slab edges against walls, around column blockouts and at foundation walls, with premolded filler 1/2" thick extending the full slab depth ([UFGS 03 30 00 section 3.11.2](https://nibs-s3-wbdg3-production.s3.us-east-1.amazonaws.com/FFC/DOD/UFGS/UFGS%2003%2030%2000.pdf)). The estimate has 39.22 LF at 1/2" and the S-600 detail shows 1/2" joint filler.
- Joint definitions ([ACI FAQ 864](https://www.concrete.org/tools/frequentlyaskedquestions.aspx?faqid=864)):
  - A contraction joint is a groove that creates a weakened plane.
  - An isolation joint separates sections to allow movement in three directions.
  - A construction joint is a planned interface between placements.
- Construction (keyed) joints: the federal guide spec calls for keyways at least 1-1/2" deep in walls and slabs ([UFGS 03 30 00 section 3.11.1](https://nibs-s3-wbdg3-production.s3.us-east-1.amazonaws.com/FFC/DOD/UFGS/UFGS%2003%2030%2000.pdf)). On this job a keyed construction joint uses the 24 gauge keyed insert (S-201 notes).
- Joint sealant is a separate line, usually Div 07. Joints at exposed floors receive filler and sealant (S-680 note). Joints under finished flooring may be left unsealed until the flooring work.

### 3.5 Vapor retarder

- **This project (governs):** spec 07 2616 requires a 15 mil multilayer polyolefin sheet, ASTM E1745 Class A, under 0.012 perms (ASTM E96), with Stego Wrap 15 as basis of design (Raven Vapor Block 15 and Reef Griffolyn 15 Mil Green also accepted). It also requires Stego Tape and Stego Mastic (`spec-p162.txt`), joints overlapped 6" and taped, and the retarder lapped over footings or sealed to the foundation walls (`spec-p163.txt`). The estimate's "10 MIL" description does not meet this. The SF is unaffected.
- Generic federal guide spec, for comparison only: ASTM E1745 Class A, 10 mil minimum, permeance maximum 0.04 perms ([UFGS 03 30 00 section 2.4.6](https://nibs-s3-wbdg3-production.s3.us-east-1.amazonaws.com/FFC/DOD/UFGS/UFGS%2003%2030%2000.pdf)).
- Generic install rule: greatest practicable widths to minimise joints, lap joints a minimum of 12" and tape. The project spec's 6" lap governs here ([UFGS 03 30 00 section 3.5.2](https://nibs-s3-wbdg3-production.s3.us-east-1.amazonaws.com/FFC/DOD/UFGS/UFGS%2003%2030%2000.pdf)). Building Science Corporation's digest states that slabs in ground contact are required to have a Class I vapor retarder below the slab ([BSD-106](https://buildingscience.com/documents/digests/bsd-106-understanding-vapor-barriers)).
- Roll example (the specified product): Stego Wrap 15-Mil comes in 14' x 140' rolls of 1,960 SF, with permeance 0.0086 perms and "Exceeds ASTM E1745 Class A, B & C" ([Stego Wrap 15-Mil](https://www.stegoindustries.com/products/vapor-retarder-15-mil-a), fetched 2026-10-13).
- Accessories that follow: seam tape, mastic, pre-cut pipe boots and termination bar ([Stego product list](https://www.stegoindustries.com/)).
- Quantity: slab area plus turn-ups at edges plus lap allowance, converted to rolls. A 14' x 140' roll with 6" laps on width and length covers 1,883.25 SF net, so 1917.6 SF needs 1.02 rolls before the lap over the footings (python). A bid order is 2 whole rolls.

### 3.6 Base course and under-slab insulation

- Base: 4" of #57 stone under the slab on this job (`spec-p055.txt`). Volume = slab area x 4" / 27. For 1917.6 SF that is 23.67 CY in place, before compaction or overage.
- The XPS (2298 SF) exceeds the slab (1917.6 SF) by about 20 percent, which is a signal that the insulation also runs at thickened edges or perimeters. It belongs to Div 07 but should be cross-checked against the slab area.

### 3.7 Formwork

- Formwork is measured as contact area (SFCA): the area of concrete surface that touches a form. Faces poured neat against earth, tops and bottoms bearing on earth take no form.
- Form materials: plywood to NIST PS 1 B-B concrete form grade ([UFGS 03 30 00 section 2.1](https://nibs-s3-wbdg3-production.s3.us-east-1.amazonaws.com/FFC/DOD/UFGS/UFGS%2003%2030%2000.pdf)). The project requires PS-1 concrete form plywood, Class 11, exterior grade (`spec-p055.txt`).
- Accessories: form ties, chamfer strips and release agent ([UFGS 03 30 00 sections 2.2.1, 2.2.4](https://nibs-s3-wbdg3-production.s3.us-east-1.amazonaws.com/FFC/DOD/UFGS/UFGS%2003%2030%2000.pdf)). The federal guide spec chamfers above-grade exposed edges at 3/4" ([UFGS 03 30 00 section 3.3](https://nibs-s3-wbdg3-production.s3.us-east-1.amazonaws.com/FFC/DOD/UFGS/UFGS%2003%2030%2000.pdf)).
- Formwork can be reused. Reuse is a cost matter, not a quantity matter, so SFCA is measured once per element and the reuse factor is applied outside the quantity.

Formwork geometry rule that reproduces the reference estimate (derived in section 8):

- Stem walls: 2 faces x height x LF.
- Continuous footing: 2 sides x depth x LF.
- Isolated footing: 4 sides, 2 x (A + B) x depth, per footing.
- Cleanout pad: 4 edges, 2 x (1.5 + 1.5) x 0.5 = 3.0 SF.
- The sum is 248.4 + 353.67 + 808.8 + 3.0 = 1413.87 SF, which is 0.43 percent below the estimator's 1420 SF before rounding.
- The estimate reports the total rounded up to the next 10 SF, which gives 1420. That rounding is a hypothesis fitted from this one line. With the estimator's own inputs the raw sum is 1415.26 SF, and round-to-nearest-10 gives 1420 too. Measure and score the raw contact area.

## 4. Coverage, yield and waste

| Item | Factor | Basis |
|---|---|---|
| Concrete overage | 5 to 10 percent for a slab or similar pour | "Experienced contractors usually assume 5-10%" ([Omni Calculator](https://www.omnicalculator.com/construction/concrete-slab)) |
| Concrete overage | "Never order the exact amount"; add a margin and 1/4" of thickness | [Concrete Network](https://www.concretenetwork.com/concrete/howmuch/calculator.htm) |
| Concrete density for weight checks | 150 lb/CF | [Omni Calculator](https://www.omnicalculator.com/construction/concrete-slab) |
| Slab yield | 81 SF per CY at 4" | [Concrete Network](https://www.concretenetwork.com/concrete/howmuch/calculator.htm) |
| Mesh sheet net coverage | (width - lap) x (length - lap) | [WRI FAQ](https://wirereinforcementinstitute.org/welded-wire-reinforcement/welded-wire-faqs) for sheet dimensions, [UFGS 3.5.6](https://nibs-s3-wbdg3-production.s3.us-east-1.amazonaws.com/FFC/DOD/UFGS/UFGS%2003%2030%2000.pdf) for lap |
| Mesh support spacing | 12" support spacing for wires smaller than W4.0 under ACI 301, with WRI noting it does not guarantee tolerance | [WRI FAQ](https://wirereinforcementinstitute.org/welded-wire-reinforcement/welded-wire-faqs) |
| Bar supports | 4'-0" o.c. maximum, first within 1'-0" of the end | project spec 03 2000 (`spec-p047.txt`) |
| Vapor retarder lap | 6" and tape on this project (07 2616, `spec-p163.txt`); 12" and tape in the generic federal spec | [UFGS 03 30 00 3.5.2](https://nibs-s3-wbdg3-production.s3.us-east-1.amazonaws.com/FFC/DOD/UFGS/UFGS%2003%2030%2000.pdf) |
| Curing compound | project requires ASTM C309 Type 1 | `spec-p055.txt` |

Waste and overage are applied after the net quantity. Do not bake them into the net takeoff line. The reference estimate's CY lines are net geometry (section 8). The app's own waste classes are `concrete`, `concrete-reinforcing`, `concrete-accessories` and `concrete-base` (`TakeoffSpeed repo: lib/quantities/trades/structure/concrete.ts`).

I did not find a citable source for rebar scrap percentage, formwork waste or mesh waste. Section 9 lists what the second opinion proposed.

## 5. Material breakdown an estimator lists

Primary:

- Ready-mix concrete by strength: 3000 psi (building slab, S-001), 4000 psi (dumpster slab, S-001). The spec sets minimum cement of 498 lb (5.3 bags) per CY at 3,000 psi and 611 lb (6.5 bags) at 4,000 psi, adding 47 lb for pumped mixes, with slump 3" to 5" (4" to 6" if pumped) (`spec-p054.txt`).
- Reinforcing steel by bar size, Grade 60 (`spec-p046.txt`).
- Welded wire fabric in flat sheets, 6x6-W2.9xW2.9.

Accessories that follow from the primaries:

- Under slab: #57 stone base, vapor retarder with tape, mastic and pipe boots, rigid insulation where shown.
- Reinforcing accessories: chairs and bolsters (CRSI supports range from plain concrete blocks to plastic chairs and wire supports, [CRSI, Placing Bars](https://www.crsi.org/reinforcing-basics/reinforced-concrete/placing-bars/)), tie wire (16 gage black soft iron per [UFGS 3.5.10](https://nibs-s3-wbdg3-production.s3.us-east-1.amazonaws.com/FFC/DOD/UFGS/UFGS%2003%2030%2000.pdf)), joist chairs of #6 wire on this project (`spec-p046.txt`).
- Dowels: smooth dowels 1/2" diameter x 2'-0" @ 1'-6" o.c., greased one end, at the floor joint (S-680 detail text); #4 dowels @ 18" at stem walls (estimate line 27); 2 #4 x 3'-0" at dummy-joint intersections (S-201 note).
- Joints: 24 gauge galvanized keyed form (`spec-p055.txt`); 1/2" premolded filler; sealant and backer rod if called.
- Formwork: PS-1 plywood, lumber, form ties, chamfer strip, release agent, stakes. Round column forms (Sonotube) where piers are round.
- Embeds: anchor bolts and base-plate grout (S-680 shows a 1-1/2" non-shrink grout bed, 5,000 psi).
- Curing: ASTM C309 Type 1 compound or polyethylene sheeting, burlap (`spec-p055.txt`, `spec-p056.txt`).
- Testing and special inspection are in the specification but are not quantity items.

## 6. Common mistakes and checks

Mistakes seen when the sources are compared with this job:

1. Treating the slab as a CY line when the estimator carried SF. Pick the unit the downstream pricing needs and show both (CY = SF x t / 12 / 27).
2. Using a generic joint spacing instead of measuring the S.C.J. lines. S-001 says 15 ft, S-201 says 12'-6". The measured quantity (364.11 LF) is what counts.
3. Missing dummy-joint dowels, step-down footing volume and piers under steel columns, because they appear in notes and details instead of on a schedule.
4. Counting both stem wall faces and footing sides as formed when the sheet shows footings poured neat. Check each footing section for a "neat" or "against earth" note before assigning SFCA.
5. Including the CMU stem wall (A-110, 157.4 LF) with concrete stem walls. They are different trades and materials.
6. Adding waste into the net line, then adding it again at pricing.
7. Taking site concrete (curb, sidewalk, pads) in the building concrete trade. The reference estimate carries these in Div 32.
8. Applying the wrong lap. Use the project spec (30 db bars, 6" mesh) over generic rules.

Cross-checks that work on this job:

- Continuous footing: LF x width x depth / 27. 124.2 LF x 2 x 1 / 27 = 9.200 CY against 9.196 CY in the estimate.
- Isolated footing: count x A x B x D / 27 per mark. Total 16.716 CY against the estimate's 16.730 CY (a 0.08 percent difference from rounding).
- Slab: SF / 81 = CY for 4" (23.67 CY).
- Cleanout pad: 1.5 x 1.5 x 0.5 / 27 = 0.0417 CY, matching the estimate's 0.041667.
- Stem wall: 8" wall, 2'-0" high, 193.8 LF gives 9.570 CY against 9.628 CY (−0.60%). The estimate reproduces exactly as 194.0 LF x 2 x 0.67 / 27 = 9.628148. The estimator converts ft-in to 2-decimal feet (8" → 0.67) and uses 194.0 LF, which is the legend's 193.8 apparently rounded up to 0.5 FT (8.4 → 8.5 on the wing wall). Of the −0.60%, about −0.50% is the thickness rounding and −0.10% is the LF. Hold agreement to about 1 percent on linear measurements.
- Vapor retarder and mesh: net area should equal slab area before laps. Compare with the XPS area.
- Reinforcing weight check: 2 #6 over 124.2 LF is 373.1 lb (2 x 124.2 x 1.502).

## 7. What an AI takeoff must read from the drawings and specs

From the drawings:

1. Footing marks, sizes and bar callouts (plan tags and the footing schedule on S-201 and S-680), with counts per mark.
2. Wall footing default (S-001: 12" thick, 6" spread each side of masonry, 2 #6 continuous) versus the S-600 section (2'W x 1'D here). The section overrides the default.
3. Stem wall thickness, height, bar size and spacing, and dowel spacing, from the foundation sections.
4. Top-of-footing and slab elevations. S-201 puts interior and exterior footing tops 2'-0" below the finish slab unless a different elevation is bracketed, so wall height follows from these elevations. Footing steps are marked on the plan.
5. Slab thickness per zone, mesh designation, vapor retarder, base thickness and material (plan note, S-001 note 6/7, spec).
6. Joint symbols: S.C.J. (saw-cut), C.J. (construction joint, keyed, discontinue mesh), isolation joints at columns and walls. Measure each run.
7. Notes about extra bars at joint intersections and around openings (S-001 note 4 says to place the reinforcing that would occur in line with the opening equally either side, cutting no steel in the field).
8. Pads and non-structural concrete on MEP sheets (cleanout pads on P-302, equipment pads on mechanical sheets).
9. Insulation under slab (G-003 section, Div 07 notes).

From the specification:

1. Strength, slump and cement content per element (`spec-p054.txt`).
2. Reinforcing grade, laps, cover, supports and mesh lap (`spec-p046.txt`, `spec-p047.txt`).
3. Form materials and joint hardware (`spec-p055.txt`, `spec-p057.txt`).
4. Curing method and compound (`spec-p055.txt`, `spec-p056.txt`, `spec-p063.txt`, `spec-p064.txt`).
5. Slab fill and subbase (`spec-p055.txt`).

Parsing rules for the reader:

- Where a sheet note and a general note disagree, prefer the sheet-specific note and flag the conflict.
- Read legend items from markup pages literally. The S-201 legend measured WF20, 8" and 10" stem walls, SAW-CUT JOINT, ISOLATION JOINT, F-marks and BP-marks, and the slab area (`reference/markups/legends.json`, page 33). It did not measure formwork, base course or vapor retarder. Those were derived.
- Read the unit from the legend (FT, SQ FT, EA) and derive volume from the description.
- Never invent a depth. If a footing depth or wall height is not stated, mark it unresolved.
- Do not mix in the CMU stem wall (page 3, A-110) or the S-201 base-plate (BP) marks, which are steel items.

## 8. Reconciliation with the reference estimate (computed with python)

| Check | Computed | Estimate | Diff |
|---|---:|---:|---:|
| Slab CY at 4" (1917.6 SF) | 23.674 | not listed | n/a |
| Continuous footing, 124.2 LF x 2' x 1' | 9.200 CY | 9.196 CY | 0.04% |
| Isolated footings, sum of seven marks | 16.716 CY | 16.730 CY | 0.08% |
| Stem wall 8" x 2'H x 193.8 LF | 9.570 CY | 9.628 CY | 0.6% |
| Stem wall 10" x 2'H x 8.4 LF | 0.5185 CY | 0.5226 CY | 0.8% |
| Cleanout pad 18x18x6 | 0.04167 CY | 0.041667 CY | 0.0% |
| Formwork: stems 2 faces (808.8) + continuous footing 2 sides (248.4) + isolated footing sides (353.67) + pad edges (3.0) | 1413.87 SF raw; 1420 SF rounded up to 10 SF (hypothesis) | 1420 SF | −0.43% raw; 0.00% rounded |

Alternatives for the formwork check, which did not match:

- Stem wall one face only: 1006.5 SF.
- Stem walls plus continuous footing without the isolated footings: 1057.2 SF.

So the estimator formed both faces of the stem walls and the sides of every footing.

Other observations:

- Isolated-footing CY. F50 (six at 5x5x1'2") computes to 6.481 CY with exact feet. It is carried as 6.5 CY because the estimator converts 1'-2" to 1.17 ft: 6 x 5 x 5 x 1.17 / 27 = 6.500000. That is the 2-decimal-feet convention, which also reproduces lines 21, 23, 24, 25 and 26 to the sixth decimal. It is not rounding up of the line.
- The slab, stem wall and footing quantities carry no waste. The comparison above confirms net geometry.
- The app engine's formwork defaults (continuous footing and grade beam: 2 formed faces; spread footing: 4 sides; wall: 2 faces) match this job (`concrete.ts`, conventions `concrete.formed-faces`, `concrete.isolated-formed-sides`, `concrete.wall-formed-faces`).
- The app's vapor lap is 6" (convention `concrete.vapor-lap-in`), which matches project spec 07 2616. UFGS uses 12" (section 3.5). With the specified 14' x 140' Stego Wrap 15 roll, 1917.6 SF needs 1.02 rolls at a 6" lap or 1.06 at 12", so either lap orders 2 rolls.

## 9. Second opinion (GPT-6 Astra, not independently sourced)

These are proposed conventions to test, not facts. Each is marked provisional by the model.

- Concrete overage: slabs 3 to 5 percent; formed footings 3 to 5 percent; footings poured neat against earth 5 to 10 percent; walls 2 to 5 percent.
- Rebar: 3 to 5 percent cutting waste on scheduled lengths. If lengths are not scheduled, 5 to 10 percent combined lap and waste as a placeholder only.
- Chairs at 3 ft each way: about area / 9, plus boundary supports. Bolster rows at 3 ft: about area / 3 LF. Do not count both.
- Dowel count per run: ceil(run / spacing) + 1.
- Saw-cut LF for a rectangular panel grid: (nL - 1) x W + (nW - 1) x L, adjusted for openings and construction or isolation joints.
- Slab edge formwork: a 4" edge is 0.333 SF per LF.
- Do not deduct reinforcing steel volume from concrete.

Note a conflict with the verified project spec: the project spec puts bar supports at 4'-0" o.c. maximum, so the 3 ft chair grid is tighter than the contract requires. The model's 8 to 12 ft panel suggestion for a 4" slab is also tighter than the 12'-6" limit on S-201. Use the project's numbers.

## 10. Reference list

Web:

- [Concrete Network concrete calculator](https://www.concretenetwork.com/concrete/howmuch/calculator.htm)
- [Omni Calculator, concrete slab](https://www.omnicalculator.com/construction/concrete-slab)
- [Procore, concrete takeoff](https://www.procore.com/library/concrete-takeoff)
- [ACI FAQ 915, saw-cut timing and depth](https://www.concrete.org/tools/frequentlyaskedquestions.aspx?faqid=915)
- [ACI FAQ 864, joint definitions](https://www.concrete.org/tools/frequentlyaskedquestions.aspx?faqid=864)
- [ACI FAQ 897, slab-on-ground design reference](https://www.concrete.org/tools/frequentlyaskedquestions.aspx?faqid=897)
- [UFGS 03 30 00 Cast-in-Place Concrete](https://nibs-s3-wbdg3-production.s3.us-east-1.amazonaws.com/FFC/DOD/UFGS/UFGS%2003%2030%2000.pdf)
- [Wire Reinforcement Institute FAQ](https://wirereinforcementinstitute.org/welded-wire-reinforcement/welded-wire-faqs)
- [CRSI, Placing Bars](https://www.crsi.org/reinforcing-basics/reinforced-concrete/placing-bars/)
- [CRSI, Rebar Properties](https://www.crsi.org/reinforcing-basics/reinforcing-steel/rebar-properties/) (grades and ASTM specifications only; no size table)
- [Wikipedia, Rebar](https://en.wikipedia.org/wiki/Rebar)
- [Wikipedia, Shallow foundation](https://en.wikipedia.org/wiki/Shallow_foundation)
- [Building Science Corporation BSD-106](https://buildingscience.com/documents/digests/bsd-106-understanding-vapor-barriers)
- [Stego Wrap 15-Mil](https://www.stegoindustries.com/products/vapor-retarder-15-mil-a)

Project files (all under `this repository` or `/home/user/work`):

- `reference/estimate/lines.json` (DIV 03 lines 16-30; Div 07 line 151; Div 31 lines 629-630)
- `reference/markups/legends.json` (page 33, S-201)
- `text/S-001.txt`, `S-201.txt`, `S-600.txt`, `S-680.txt`
- `text/spec-p045.txt` to `spec-p066.txt`; `spec-p162.txt`, `spec-p163.txt` (07 2616)
- Engine for comparison: `TakeoffSpeed repo: lib/quantities/trades/structure/concrete.ts`
