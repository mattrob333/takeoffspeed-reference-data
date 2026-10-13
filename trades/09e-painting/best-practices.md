# Painting (walls, ceilings, doors/frames, trim, MEP): quantity takeoff best practice

Scope: quantities and material types only. No pricing and no labor.

**Research limits, read first.**
- The session's web-search budget ran out after the first query, so every external source below was reached by direct fetch of a known URL (manufacturer data sheets, a federal guide spec, Wikipedia, calculators).
- Manufacturer data sheets and the UFGS are strong sources for coverage and scope. Authoritative public sources for estimator measurement conventions (opening-deduction thresholds, per-door area, overage %) were NOT found. Those items are tagged **[convention, not independently sourced]**. Treat them as defaults to confirm against the owner's or estimator's standard, not as cited fact.
- Project facts cite local reference files, shown as `file:line-or-key`.

---

## 1. What the estimator takes off, and in what units

Specification Section 09 91 00 ("Painting") covers surface preparation and field painting of exposed interior items and surfaces. It includes exposed bare and covered pipes and ducts, hangers, exposed steel and iron, and primed metal on mechanical and electrical equipment ([project spec 09 9100, p320, `text/spec-p320.txt`]). The UFGS 09 90 00 guide spec has the same structure: where a space or surface is painted, it includes exposed piping, conduit and ductwork, supports, hangers, air grilles and registers, and miscellaneous metalwork and insulation coverings ([UFGS 09 90 00 §1.2.3](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2090%2000.pdf)).

| Line family | Takeoff unit | Then the material (gal) | Notes |
|---|---|---|---|
| Wall paint, per paint tag, per substrate, per sheen | SF | Primer gal and finish gal, separately | Group by tag (PT-1...), because color and product differ. The project estimate carries one SF line per tag ([lines.json lineNo 295-299](reference/estimate/lines.json)). |
| Ceiling paint (GWB ceilings, soffits, exposed structure, booth roof) | SF | Primer and finish gal | Exposed structure is its own line, because the surface is rougher and has a larger actual area than plan ([lines 300-302](reference/estimate/lines.json)). |
| Painted door leaves and HM frames | EA by size (frame EA), with SF derived for gallons | Primer and finish gal | The project estimate counts "3'Wx7'H hollow metal frame" as 6 EA ([line 303](reference/estimate/lines.json)). |
| Opening trim, base, casing | LF | Primer and finish gal (derive SF from LF x girth) | The project estimate carries 910 LF of PT-2 at opening trim ([line 304](reference/estimate/lines.json)). |
| Exposed pipe, color or safety paint | LF by nominal size | Finish gal from LF x pi x OD | The project has 3/4" gas 45 LF and 1" gas 10 LF in safety yellow ([lines 306-307](reference/estimate/lines.json)). |
| Painted devices (diffusers, grilles, LSD/LSR) | EA | Usually no gallons (touch-up quantity) | The project has "black paint ceiling diffuser" at 5 EA ([line 305](reference/estimate/lines.json)). |
| CMU / concrete coatings | SF | Block filler or surfacer gal plus coating gal | The project has a cementitious/elastomeric coating on CMU at 241.59 SF ([line 673](reference/estimate/lines.json)). |

Count the wall-covering primer separately from paint. Here PT-7 is a 105 SF primer-only line ("dries clear") under owner-vendor wall covering ([line 298](reference/estimate/lines.json); [spec schedule, p328](text/spec-p328.txt)).

## 2. Sheets and spec sections that drive it

- **Finish plan and finish schedule** (here A-150 and A-170). They give the paint tags (PT-1 to PT-8), where each tag applies, height notes such as "PT1 PAINT @ 12'H", and sheen ([legends.json page 8 and page 10](reference/markups/legends.json)).
- **Reflected ceiling plan** (A-130). It separates ACT, GWB ceilings (PT3), exposed structure, and soffits with their drop heights ([legends.json page 5](reference/markups/legends.json)).
- **Enlarged plans and elevations** (A-410 restrooms, A-704/A-706 booth). They carry painted areas that are not on the main finish plan. The A-410 legend lists "PT1 WALL PAINT 252.6 SF" ([page 16](reference/markups/legends.json)).
- **Door and frame schedule and elevations** (A-600). They decide which frames are hollow metal (field painted) and which are aluminum or prefinished (not painted) ([legends.json page 21](reference/markups/legends.json)).
- **MEP plans and notes** (M-301 ceiling devices, P-303 roof gas pipe). Notes like "PAINT LSD BLACK" and "SAFETY YELLOW PAINT AT ROOF GAS PIPE" create painting quantities that exist only in the MEP sheets ([legends.json pages 53 and 58](reference/markups/legends.json)).
- **Section 09 91 00 and the 09 91 10 paint schedule.** They set the system (primer, finish, coats, sheen) per substrate and name the basis-of-design and approved-equal manufacturers ([spec p322](text/spec-p322.txt), [p328-329](text/spec-p328.txt)). Related sections: 08 11 13 (shop-primed HM frames) ([spec p320](text/spec-p320.txt)), 09 96 53 elastomeric coatings.
- **Product data sheets.** The spec says apply "no thinner than the manufacturer's recommended spreading rate" ([spec 3.3.D, p326](text/spec-p326.txt)), so the data sheet sets the coverage.

## 3. Scope rules: what is and is not painted

From the project spec (09 91 00):
- Paint exposed surfaces, except where schedules say otherwise. Unscheduled items are painted like similar adjacent surfaces ([p320](text/spec-p320.txt)).
- Do not paint prefinished items, concealed surfaces, finished metal surfaces, operating parts, or labels ([p320](text/spec-p320.txt)).
- "Exposed" includes areas visible with fixtures and grilles in place. Surfaces behind movable equipment are painted like exposed ones. Surfaces behind permanently fixed equipment get prime coat only ([3.3.A.4-5, p325](text/spec-p325.txt)).
- Duct interiors visible through registers or grilles get flat nonspecular black. Back sides of access panels are painted to match ([p325](text/spec-p325.txt)).
- Mechanical and electrical painting is limited to items exposed in equipment rooms and occupied spaces. The list includes piping, hangers, supports, ductwork, insulation, motors, accessory items, conduit, switchgear and panelboards ([3.3.E-G, p326-327](text/spec-p326.txt)).
- Omit primer on shop-primed and touched-up metal ([3.3.B.2, p326](text/spec-p326.txt)).
- Block filler goes on CMU "at a rate to ensure complete coverage with pores filled" ([3.3.H, p327](text/spec-p327.txt)).

From UFGS 09 90 00 (same pattern, a useful default when a project spec is silent):
- Not painted unless indicated: surfaces concealed behind fixed panelboards, ductwork and equipment; concealed spaces (above suspended ceilings, furred spaces, attics, crawl spaces, chases); steel embedded in concrete; copper, stainless, aluminum, anodized aluminum, brass and lead; hardware and factory-finished items ([§1.2.2](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2090%2000.pdf)).
- Sprinkler piping in unfinished areas gets primed surfaces plus one coat of red alkyd gloss enamel at 1.0 mil DFT. Piping in finished areas gets primed surfaces plus two coats matching adjacent surfaces ([§3.8.1.h-j](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2090%2000.pdf)).
- Pipe identification and flow arrows are stenciled with white or black paint ([§3.8.1.k-l and §3.9](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2090%2000.pdf)).

Reference-job check: the A-170 schedule rows highlighted for paint (PT-2, PT-5) and the A-600 doors show that aluminum storefront frames and glazing are NOT in the paint scope. The estimate counts only the "hollow metal frame" ([legends.json page 10 notes](reference/markups/legends.json), [line 303](reference/estimate/lines.json)).

## 4. Measurement rules

### 4.1 Walls

- **Method.** Linear footage of each painted wall run (both faces counted separately where both are painted) multiplied by the painted height. The height comes from the finish plan note, the section or the RCP, not from a default. The reference markups do exactly this: PT1 wall runs are measured per height group (6'6", 8'6", 9', 10', 11', 12', 12'6") ([legends.json page 8](reference/markups/legends.json)). The commercial tools support the same workflow: measure linear, area, and surface-area, with doors and windows excluded while measuring ([STACK](https://www.stackct.com/blog/painting-estimating/)).
- **Worked reference check (python).** The seven PT1 run groups give LF x H = 751.2 + 165.0 + 337.5 + 31.9 + 518.0 + 1053.9 + 600.0 = 3457.4 SF. Adding the A-410 restroom area of 252.6 SF gives 3710.0 SF, against the estimate's PT-1 line of 3710.84 SF ([legends.json pages 8 and 16](reference/markups/legends.json), [line 295](reference/estimate/lines.json)). The difference is 0.84 SF (0.02%). **Conclusion: on this job the finish-plan wall runs are gross LF x H, with no opening deductions for doors or interior glazing.** The A-410 elevation polygons are the exception: they are cut around the restroom doors, except the estimator's copy of elevation A, which is a full rectangle (about 23 SF of door left in). This reproduces the reference quantity; it is a property of this estimator's method, not an industry rule.
- **Openings (deduct or not).** Consumer calculators and software deduct them (door about 20 SF and window about 12 SF appear as defaults in [Inch Calculator](https://www.inchcalculator.com/paint-calculator/); [FreshBooks](https://www.freshbooks.com/hub/estimates/estimate-painting-jobs) says to subtract windows and doors). The reference estimate does not. **[convention, not independently sourced]**: commercial practice is split between gross measure with no deduction (openings offset by returns, jambs, cut-in) and deducting openings above a size threshold. Record which convention is used. Because the project spec requires frames and trim to be painted separately, deducting door openings from wall area while also carrying frames as their own line is the consistent pairing.
- **Wall coverings and tile.** Subtract zones that are not painted (tile, FRP, wallcovering). The reference finish plan separates "WALL COVERING @ 10'H ABOVE PT7 10.3 FT", "PT7 @ 10' 10.3 FT" and "FRP-1 @ 4'H 4 FT" ([legends.json page 8](reference/markups/legends.json)). Heights matter: PT7 is 10.3 LF x 10' = 103 SF, which matches the estimate's 105 SF PT-7 primer line within 2 SF ([line 298](reference/estimate/lines.json)).
- **Heights.** Paint goes to the underside of the ceiling or deck. In rooms with ACT, paint typically runs to the ceiling grid line or above, so take height from the wall type or section, not from the ACT height alone. Where the structure is exposed, the wall continues to the underside of deck (12'6" on this job) ([legends.json page 8](reference/markups/legends.json)).
- **Do not use wall paint SF as a stand-in for GWB board SF.** The board takeoff counts both faces plus soffits, while paint counts only scheduled faces and tags.

### 4.2 Ceilings and soffits

- Paint area for a flat gypsum ceiling is plan area (the reference RCP legend lists "5/8" GWB CEILING (PT3) 516.1 SF"). Soffits and bulkheads are measured as LF x developed face height (down face plus any returns) and added to that ceiling tag ([legends.json page 5](reference/markups/legends.json)).
- **Reference reconciliation (python).** The six soffit rows on page 5, LF x GWB face height, are 4.2 x 7.0 (`SOFFIT @ 3'6"H, GWB BS`: BS = both sides, 2 x 3.5) + 2.7 x 4 + 6.7 x 1.5 + 30.5 x 3 + 35.3 x 2.5 + 28.1 x 2 = 29.4 + 10.8 + 10.05 + 91.5 + 88.25 + 56.2 = **286.2 SF**, which is the soffit board line (286.04, [line 285](reference/estimate/lines.json)). 516.1 + 286.2 = **802.3 SF** against the estimate's PT-3 ceiling line of 802.0 SF (+0.04%); the parent board lines give 516.0 + 286.04 = 802.04, carried as 802 ([lines 278, 285, 300](reference/estimate/lines.json); formulas F3). PT-3 is every gypsum board SF that faces the room, ceiling plus soffit faces.
- **Exposed structure** is on its own line ("PT-3 at exposed structure", 100 SF in the estimate versus 98.4 SF in the legend) ([line 301](reference/estimate/lines.json), [legends.json page 5](reference/markups/legends.json)). The estimate counts plan area. A deck-and-joist surface factor is a separate, larger number; apply it only when a source states one. The engine here leaves it unset and warns ([painting.ts ceilings](TakeoffSpeed repo: lib/quantities/trades/interiors/painting.ts)).
- ACT panels and grid are not painted unless the spec says so, and the paint takeoff should never include ACT areas. Spec text: sections for acoustical ceilings are separate (09 51 13), and painting excludes prefinished items ([spec p320](text/spec-p320.txt)).

### 4.3 Doors and frames

- **Count by size and by type, and keep leaf and frame separate.** Only field-painted items count: HM frames, and HM or paint-grade wood leaves. Prefinished wood doors, aluminum storefront and glass doors do not. The reference job has six 3'x7' HM-framed doors on A-600 (Type B welded frames x5, Type C knock-down frame x1; 2 + 1 + 3 across the three legend rows) and the estimate carries 6 EA ([legends.json page 21](reference/markups/legends.json), [line 303](reference/estimate/lines.json)). The estimate line is the frame only; the leaf is described as solid-core wood on the drawing, so check whether the leaf is scheduled for paint, stain or factory finish before adding it.
- **Area for gallons (derived geometry, python).**
  - One 3'x7' leaf has two faces of 21 SF each = 42 SF.
  - Its four edges at 1-3/4" thick add (2x3 + 2x7) x 1.75" / 12 = 2.92 SF.
  - The frame is 2x7 + 3 = 17 LF of head and jambs. At an 11" girth that is 15.6 SF, at 12" it is 17.0 SF.
  - Six frames with leaves come to about 363 SF; six frames alone come to about 94 SF.
- **[convention, not independently sourced]** The engine assumes frame girth of jamb depth + 5.25" (two 2" faces and two 5/8" stops) and 1-3/4" leaf thickness ([painting.ts conventions](TakeoffSpeed repo: lib/quantities/trades/interiors/painting.ts)). Confirm against the frame elevation and the SDI profile used.
- Doors with shop-primed frames: the frames ship shop-primed (08 1113 "Exposed Finish: Prime", [p214](text/spec-p214.txt)). 09 9100 3.3.B.2 lets the field primer be touch-up only on intact shop primer ([p326](text/spec-p326.txt)), but p320 says this section's priming is "in addition to shop priming" ([p320](text/spec-p320.txt)) and 09 9110 still lists a primer system for "Hollow Metal Frames and Doors" (SW ProCryl B66-1310 / BM V131 / PPG Pitt Tech, [p328](text/spec-p328.txt)). Carrying a full primer coat, as this estimator did (1P + 2C), is a defensible contractor convention; flag it rather than drop it.

### 4.4 Trim, base, casing

- Take trim in LF by type and profile, and only for paint-grade trim. Convert to SF only to estimate gallons: perimeter (girth) x length / 144 ([Inch Calculator trim method](https://www.inchcalculator.com/paint-calculator/)).
- The reference estimate has 910 LF of PT-2 at opening trim and no legend row produces that number. I could not reconcile it from the legends and the drawings I read. An AI takeoff must therefore read the keynote or finish note that defines "opening trim" (head, jambs, returns at windows, storefront, cased openings) before measuring it ([line 304](reference/estimate/lines.json)).
- Resilient base (09 65 13) and wall base are not paint. The reference markup lists "WB-1 404.7 FT" as a separate base item ([legends.json page 8](reference/markups/legends.json)).

### 4.5 MEP: pipe, ductwork, devices

- **Pipe.** Surface area per LF is pi x OD. Use the ASME outside diameters by nominal size: 1/2" = 0.840", 3/4" = 1.050", 1" = 1.315", 1-1/2" = 1.900", 2" = 2.375", 3" = 3.500", 4" = 4.500", 6" = 6.625" ([Nominal Pipe Size](https://en.wikipedia.org/wiki/Nominal_Pipe_Size)). Computed (python): 3/4" = 0.275 SF/LF; 1" = 0.344 SF/LF; 2" = 0.622 SF/LF; 4" = 1.178 SF/LF.
- Reference check: 45 LF of 3/4" plus 10 LF of 1" gas pipe is 15.8 SF. The legend measured 44.2 LF and 9.7 LF (and 53.9 LF total on the roof-gas safety-yellow row), so the estimate is a rounded-up version of the measured runs ([lines 306-307](reference/estimate/lines.json), [legends.json page 58](reference/markups/legends.json)). Roof gas pipe is exterior; confirm the exterior system (the spec schedule's exterior steel row) applies.
- **Insulated pipe and duct.** Painting follows insulation covering when the spec lists insulation as painted. Measure the jacket OD, not the bare pipe OD. UFGS excludes zinc-coated, aluminum and copper under insulation, and ferrous piping under insulation ([§1.2.3.b](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2090%2000.pdf)).
- **Ductwork.** Perimeter x length for exposed duct. The reference M-301 legend measures duct by size (for example 20x12 = 94.4 FT) but the estimate carries no duct paint line, so the engine should paint ducts only when the spec or the exposed-structure plan says "exposed ductwork painted" ([legends.json page 53](reference/markups/legends.json), [spec p326-327](text/spec-p326.txt)).
- **Devices.** Count EA (diffusers, grilles, LSD/LSR). Reference: "PAINT LSD BLACK 4 EA" plus "PAINT BLACK LSR 1 EA" = 5, which is the estimate's "BLACK PAINT CEILING DIFFUSER 5 EA" ([legends.json page 53](reference/markups/legends.json), [line 305](reference/estimate/lines.json)).

## 5. Coverage, coats, and waste

All coverage values below are **per coat** and **at the manufacturer's recommended film thickness**. Gallons = SF x coats / coverage.

| Product (as scheduled in this project or its approved equal) | Coverage per gallon | Basis |
|---|---|---|
| SW ProMar 200 Zero VOC Latex Primer (data sheet code B28W12600; the 09 9110 schedule writes B28W2600) | 400 SF at 4 mils wet / 1.0 mil dry | [SW PDS](https://www.sherwin-williams.com/document/PDS/en/035777967874/) |
| SW ProMar 200 Zero VOC Interior Latex Flat (B30 series). **Proxy:** the scheduled wall finish is the Eg-Shel B20-12651 (09 9110 p328; A-170 "ProMar 200 HP Zero VOC"), whose data sheet was not opened; the flat-series figure stands in for it | 350-400 SF at 4 mils wet / 1.4 mils dry (flat series) | [SW PDS](https://www.sherwin-williams.com/document/PDS/en/650992951/) |
| SW ProMar 400 Zero VOC Interior Latex Flat (B30 4600 series, ceilings) | 350-400 SF at 4 mils wet / 1.1 mils dry | [SW PDS](https://www.sherwin-williams.com/document/PDS/en/035777104361/) |
| SW Loxon Acrylic Block Surfacer (CMU, concrete) | 50-100 SF at 16 mils wet / 8.8 mils dry | [SW PDS](https://www.sherwin-williams.com/document/PDS/en/035777875315/) |
| SW Pro Industrial Pro-Cryl Universal Primer (metal) | 160-320 SF (5-10 mils wet / 1.9-3.8 dry); theoretical 609 SF at 1 mil dry | [SW PDS](https://www.sherwin-williams.com/document/PDS/en/035777354971/) |
| BM Regal Select Flat (N547) | 400-450 SF at 3.6-4.0 mils wet / 1.6-1.9 dry | [BM TDS](https://media.benjaminmoore.com/WebServices/prod/assets/production/datasheets/TDS_0547/N547_TDS_US.pdf) |
| BM 253 Super Spec Sealer (ceiling primer in the BM column) | 400-500 SF at 3.6 mils wet / 1.1 dry | [BM TDS](https://media.benjaminmoore.com/WebServices/prod/assets/production/datasheets/TDS_0253/253_TDS_US.pdf) |
| BM P22 alkyd urethane enamel (HM frames, steel) | 375-425 SF at 3.8-4.3 mils wet / 1.8-2.1 dry | [BM TDS](https://media.benjaminmoore.com/WebServices/prod/assets/production/datasheets/TDS_0P22/P22_TDS_US.pdf) |
| BM P06 alkyd metal primer (steel detailing) | 450-550 SF at 2.9-3.6 mils wet / 1.7-2.1 dry | [BM TDS](https://media.benjaminmoore.com/WebServices/prod/assets/production/datasheets/TDS_0P06/P06_TDS_US.pdf) |

Observations that matter for an AI:
- Block surfacer is **1/4 to 1/8 the coverage** of wall latex. A single CMU wall quantity run through a drywall rate understates gallons several times over. The ProMar 200 data sheet system lists "1 coat ConFlex Block Filler" plus 2 coats latex for block ([SW PDS system list](https://www.sherwin-williams.com/document/PDS/en/650992951/)).
- Metal primer coverage on a rust-inhibitive or universal primer can be about half of latex coverage (160-320 SF for Pro-Cryl). Use the data sheet range, not the wall latex rate ([SW PDS](https://www.sherwin-williams.com/document/PDS/en/035777354971/)).
- The ProMar 200 data sheet system for drywall is 1 coat primer + 2 coats finish, which is the "1P + 2C" in this job's schedule ([SW PDS](https://www.sherwin-williams.com/document/PDS/en/650992951/), [lines 295-304](reference/estimate/lines.json)).
- The data sheet ranges are "approximate spreading rates calculated on volume solids"; they do not include application losses ([SW Pro-Cryl PDS](https://www.sherwin-williams.com/document/PDS/en/035777354971/)). That is where waste is added.

**Coats.** Take them from the schedule, not a default. Project spec: primer coat to material that is not already prime-coated, then finish coats; add coats until opaque and uniform; edges, corners and welds must reach the same DFT as flat surfaces ([3.3.B.3, 3.3.I-J, p326-327](text/spec-p326.txt)). UFGS: minimum 1.5 mil DFT per coat unless the tables say otherwise; "do not omit undercoats or primers" ([§2.1](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2090%2000.pdf)). Benjamin Moore recommends two coats of Regal Select for full color development ([BM TDS](https://media.benjaminmoore.com/WebServices/prod/assets/production/datasheets/TDS_0547/N547_TDS_US.pdf)).

**Waste / overage.**
- Round gallons up to the next purchasable container (1 or 5 gal) ([Inch Calculator](https://www.inchcalculator.com/paint-calculator/)).
- One calculator suggests up to 20% extra on porous or rough surfaces and up to 30% for first-time painting of a surface ([Omni Calculator](https://www.omnicalculator.com/construction/paint)). That is a consumer source.
- **[convention, not independently sourced]** The engine uses 5% on paint and primer ([painting.ts wasteClasses](TakeoffSpeed repo: lib/quantities/trades/interiors/painting.ts)). The spec requires matching approved samples and touch-up at the end of the job ([spec 3.6.B, p327](text/spec-p327.txt)), so keep a separate touch-up allowance for each color rather than burying it in waste.
- Keep waste out of the SF line. Carry net SF as measured and add overage only on the gallon line (the same principle as the physical-waste rule in the project CLAUDE.md).

## 6. Material breakdown the estimator lists

For each paint tag and substrate:
1. Primer or sealer (product, gallons). Examples here: ProMar 200 primer on GWB walls; 253 Super Spec Sealer (BM) or ProMar 200 primer on ceilings; Universal Metal Primer or Pro-Cryl on HM frames; block filler or surfacer on CMU. Source-limit rule: primer and finish from the same manufacturer ([spec 1.3.B, p321](text/spec-p321.txt)).
2. Finish coat (product, color, sheen, gallons). Sheen is part of the item: eggshell walls, flat ceilings, semi-gloss HM and trim ([spec 09 91 10 schedule, p328](text/spec-p328.txt)).
3. Specialty: elastomeric coating on exterior CMU (block filler first), pipe-bollard and gate enamels, safety-yellow gas pipe and bollards ([spec 09 91 10, p329](text/spec-p329.txt); [lines 306-307, 674](reference/estimate/lines.json)).
4. Tint and color count: each distinct color or sheen is a separate batch. In this job PT-1 to PT-8 plus EPT-1 are nine product lines ([lines 295-304, 673](reference/estimate/lines.json)).
5. Prep and consumables that follow from the scope: patching and filler, caulk at trim, masking, drop cloths, sandpaper, rollers and brushes. The spec requires cleaning, hardware removal and reinstall, protection of other work, "Wet Paint" signs and touch-up ([spec 3.2, 3.6, p323-327](text/spec-p323.txt)). Quantities for these are lump-sum or allowance lines, not takeoff lines, unless the estimate itemizes them.
6. Attic stock / touch-up gallons, if the spec asks. This spec does not.
7. VOC and low-emitting product requirement. Flat and nonflat paint 50 g/L, primers 100 g/L ([spec 2.2.D, p323](text/spec-p323.txt)). ProMar 200 Zero VOC is listed as less than 50 g/L ([SW PDS](https://www.sherwin-williams.com/document/PDS/en/650992951/)); Loxon Block Surfacer is 86 g/L ([SW PDS](https://www.sherwin-williams.com/document/PDS/en/035777875315/)), so a CMU surfacer inside the weatherproofing line needs a compliance check against the primer limit.

## 7. Common mistakes and checks

1. **Applying one coverage rate to every substrate.** Use the table above. CMU needs filler at 50-100 SF/gal; metal primers can be 160-320 SF/gal.
2. **Painting what the spec excludes.** Prefinished items, aluminum, concealed spaces, finished metal, operating parts and labels are not painted (see section 3). Check every counted item against the exclusion list.
3. **Missing scope that lives only on MEP sheets.** Diffusers painted black, gas pipe safety yellow, and bollards painted yellow come from MEP and site notes. They are not on the finish plan ([legends pages 53, 58](reference/markups/legends.json)).
4. **Wrong height.** A single default (8' or 9') on a plan with seven height groups (6'6" to 12'6") is wrong by thousands of SF. Check: run the PT1 groups through LF x H and compare with the schedule total (section 4.1).
5. **Double counting.** Wall-covering areas, FRP and tile are not paint. Primer-only lines (PT-7) are not finish paint.
6. **Double or no deduction of openings.** Decide gross vs net once for the whole job and say which.
7. **Dropping primer when the schedule says 1P + 2C,** or adding primer to shop-primed metal ([spec 3.3.B.2, p326](text/spec-p326.txt)).
8. **Mixing tags.** PT-1 at 3710.84 SF must not absorb PT-4 (153.62 SF), PT-6 (40 SF) or PT-8 (75 SF); each has its own product and color ([lines 295-299](reference/estimate/lines.json)).
9. **Rounding too early.** Carry SF unrounded, round gallons up at the end and only per product.
10. **Checks to run (python, never by head).**
    - Sum of LF x H per tag vs the tag's SF line.
    - Door and frame count vs A-600 legend rows (6 vs 6 here).
    - Pipe LF x pi x OD / 12 vs the SF used for gallons.
    - Gallons: SF x coats / coverage, then compare gallons per 1000 SF across tags for outliers.
    - Ceiling tag SF vs ACT/GWB/exposed-structure legend rows from the RCP.

## 8. What an AI takeoff must read from the drawings and specs

From the finish plan and schedule:
- The paint tag for every wall run, ceiling area, door/frame group and trim group, with product, color and sheen.
- Painted height for every wall run. Read the height note; if only a ceiling height is given, read the wall section for top-of-paint.
- Which walls get wall covering, FRP or tile (and to what height), so they can be excluded.

From the reflected ceiling plan:
- GWB ceilings versus ACT versus exposed structure; every soffit with its LF and face height(s).

From the door schedule and elevations:
- Frame material (HM, aluminum, wood), leaf material and finish (paint, stain, prefinished, laminate), size and count, pair or single, and frame depth.

From MEP and site sheets:
- Notes with the words "PAINT", "SAFETY YELLOW", "BLACK", "PAINTED" and every exposed run or device they refer to; pipe size, service and whether the run is interior or exterior; whether duct and insulation are exposed and painted per the spec.

From the specs (09 91 00, 09 91 10):
- The system by substrate: primer, number of finish coats, sheen, product and approved equal ([p328-329](text/spec-p328.txt)).
- Exclusions, MEP scope, prime-only locations (behind fixed equipment), and the VOC limits.
- Product data (coverage) for each scheduled product. If the product data is not in the project documents, use the manufacturer data sheet ranges above and say which end of the range was used.

Output should carry, per line: tag, product, sheen/color, substrate, net quantity and unit, coats, coverage used and its source, and the openings convention used. That is what lets a reviewer reproduce the figure.

## 9. Engine comparison notes (for the repo owner)

- The engine's `painting.walls` assembly deducts openings and excluded zones ([painting.ts `wallArea`](TakeoffSpeed repo: lib/quantities/trades/interiors/painting.ts)). On this job the reference estimate is gross LF x H (section 4.1). If the engine is scored against this reference, expect it to come in lower by the opening area unless openings are left out.
- Engine conventions are 350 SF/gal finish on smooth surfaces, 300 SF/gal for gypsum primer, 75 SF/gal for block filler on CMU, 350 SF/gal for metal primer and finish ([painting.ts conventions](TakeoffSpeed repo: lib/quantities/trades/interiors/painting.ts)). The data sheets above support 350-400 on smooth finish and 50-100 on block surfacer. Metal primer at 350 sits above the 160-320 range of Pro-Cryl but inside the 450-550 range of BM P06; the scheduled product decides.
- The engine's 12" default frame girth and 5.25" extra girth are labeled SDI profile assumptions. I could not source them online in this session.

## Sources actually opened

- Sherwin-Williams PDS: [ProMar 200 Flat B30](https://www.sherwin-williams.com/document/PDS/en/650992951/), [ProMar 200 Primer](https://www.sherwin-williams.com/document/PDS/en/035777967874/), [ProMar 400 Flat](https://www.sherwin-williams.com/document/PDS/en/035777104361/), [Loxon Block Surfacer](https://www.sherwin-williams.com/document/PDS/en/035777875315/), [Pro-Cryl Universal Primer](https://www.sherwin-williams.com/document/PDS/en/035777354971/)
- Benjamin Moore TDS: [N547](https://media.benjaminmoore.com/WebServices/prod/assets/production/datasheets/TDS_0547/N547_TDS_US.pdf), [253](https://media.benjaminmoore.com/WebServices/prod/assets/production/datasheets/TDS_0253/253_TDS_US.pdf), [P22](https://media.benjaminmoore.com/WebServices/prod/assets/production/datasheets/TDS_0P22/P22_TDS_US.pdf), [P06](https://media.benjaminmoore.com/WebServices/prod/assets/production/datasheets/TDS_0P06/P06_TDS_US.pdf)
- [UFGS 09 90 00 Paints and Coatings](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2090%2000.pdf)
- [Nominal Pipe Size (outside diameters)](https://en.wikipedia.org/wiki/Nominal_Pipe_Size)
- Calculators and tool pages (consumer or tool-vendor level; weak for commercial rules): [Inch Calculator](https://www.inchcalculator.com/paint-calculator/), [Omni Calculator](https://www.omnicalculator.com/construction/paint), [FreshBooks](https://www.freshbooks.com/hub/estimates/estimate-painting-jobs), [STACK](https://www.stackct.com/blog/painting-estimating/), [Benjamin Moore calculator](https://www.benjaminmoore.com/en-us/paint-calculator) (assumes 2 coats, excludes ceiling)
- Industry standards index (titles not visible without download; the project spec cites PDCA P1 for touch-up procedures): [PCA Industry Standards](https://www.pcapainted.org/industry-standards/)
- Project files: `reference/estimate/lines.json` (quantities and descriptions only), `reference/markups/legends.json`, `text/spec-p320.txt` to `spec-p329.txt`, `TakeoffSpeed repo: lib/quantities/trades/interiors/painting.ts`
