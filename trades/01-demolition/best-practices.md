# Demolition: best practices for quantity takeoff

Scope of this note: quantities and material/scope types only. No prices, labor hours or markups.
Reference job: single-storey bank branch, Warner Robins GA. Demolition there is *site and structure* demolition (DIV 02 on the estimate), not interior selective demolition.

## 0. Provenance and limits (read first)

- The web-search budget for this run was exhausted after the first calls, so no search-engine discovery was possible. Every external source below was fetched directly from a URL (state DOT specification books, a USACE/NAVFAC guide specification, EPA, eCFR text, OSHA). Handbook/manufacturer sources named in the brief (RSMeans, USG, ClarkDietrich, Armstrong, NECA, SMACNA, PHCC, CRSI, ACI) are not reachable that way and are **not cited**. Anything not backed by a link is explicitly marked `[NO SOURCE]` so it is not mistaken for sourced practice.
- Evidence tiers used below: `[SPEC]` = published agency or federal text; `[JOB]` = this project's own drawings/specs/estimate lines (local files, quantities only); `[ENGINE]` = TakeoffSpeed's current code (comparison only); `[NO SOURCE]` = convention that could not be verified.
- Sources (short names used in the text):
  - **NYSDOT-2** NYSDOT Standard Specifications (USC), Sept 1 2026, Vol. 2, Sections 201-202, 206: https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf
  - **NYSDOT-3** same, Vol. 3, Sections 606, 614: https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol3.pdf
  - **UFGS** UFGS 02 41 00 Demolition and Deconstruction (Aug 2022): https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2002%2041%2000.pdf
  - **EPA-C&D** EPA, Estimating 2003 Building-Related Construction and Demolition Materials Amounts: https://www.epa.gov/sites/default/files/2017-09/documents/estimating2003buildingrelatedcanddmaterialsamounts.pdf (landing page: https://www.epa.gov/smm/estimating-2003-building-related-construction-and-demolition-materials-amounts)
  - **NESHAP** 40 CFR 61.145 (asbestos, demolition and renovation): https://www.law.cornell.edu/cfr/text/40/61.145 ; EPA summary: https://www.epa.gov/asbestos/asbestos-laws-and-regulations
  - **OSHA-850** 29 CFR 1926.850 Preparatory operations: https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.850 ; **OSHA-852** Chutes: https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.852
  - **DBH** Diameter at breast height (general reference): https://en.wikipedia.org/wiki/Diameter_at_breast_height

## 1. What the estimator takes off, and in which units

Demolition is **scope removal**, not purchased material: each line is "remove X" and carries no waste factor. Units follow what is simplest to measure and what the contract measures by.

| Item class | Takeoff unit | Basis / what the sources say |
|---|---|---|
| Whole building (superstructure + foundation) | Reference job: cubic feet (footprint x height). Public-agency practice: lump sum per building | NYSDOT measures "disposal of buildings" as a lump sum per specific building ([NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf), 202-4.02). The reference estimate carries the two buildings as 89,780 CFT and 17,140 CFT `[JOB]` (estimate lines 3-4). |
| Below-grade structure / foundations | Cubic yards "computed from the payment lines" | NYSDOT 202-4.06 (substructures, nearest whole CY, [NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf)) |
| Slabs / pavements / flatwork | SF (plan area of the hatch) | NYSDOT slab removal in SF to nearest whole SF, **no deductions for openings** (202-4.07, [NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf)). Reference job: pavement 19,363.6 SF, sidewalk 390.2 SF, ramp 442.4 SF `[JOB]` (legend page 64). |
| Curb and curb & gutter | LF along the curb line | Reference job 987.2 LF `[JOB]`. Linear removal of rail/barrier is measured in feet along its axis, exclusive of end assemblies (NYSDOT 606-4.06/4.07, [NYSDOT-3](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol3.pdf)); the same rule is the right analogue for handrail and fence. |
| Utility lines and their structures | LF of line + EA of structures (inlets, manholes, poles, vaults) + EA cap/cut points | Reference job: storm 107.1 LF + 2 EA structures, water 55.6 LF, power 965.4 LF `[JOB]`. Utilities must be shut off/capped outside the building line before demolition starts ([OSHA-850](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.850), 1926.850(c)); UFGS 3.1.2: "Shut off and cap utilities for future use, as indicated" ([UFGS](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2002%2041%2000.pdf)). |
| Trees | EA (by trunk diameter), stump included | NYSDOT 614-4.03: "number of trees, including their stumps if specified"; 614-5.03: payment per tree includes stump removal ([NYSDOT-3](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol3.pdf)). Clearing and grubbing as an area item is per acre or lump sum (201-4.01/.02, [NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf)). Reference job: 2 EA `[JOB]`. |
| Discrete site features (monument sign, brick steps, etc.) | EA | Reference job: sign 1 EA, brick stair steps 7 EA `[JOB]`. |
| Saw cutting at limits | LF | Required by C-1.0 general note 3 `[JOB]`; see section 3. |
| Hazardous-material abatement | LS with named responsible party; quantity thresholds drive the regulatory path | See section 3. NYSDOT 202-5.06: asbestos removal, abatement and disposal are measured as their own item, outside the building removal ([NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf)). |
| Debris haul-off / disposal | CY loose or tons, **only if measured as its own item** apart from the removal item | NYSDOT includes disposal in the building removal item (202-5.02). `[ENGINE]` emits haul-off lines only on request. |

Lines in the reference estimate (the 14 DIV 02 demolition lines, estimate lines 2-15, `[JOB]`; line 1 is permits/supervision/cleanup/dumpster): curb & gutter 987.22 LF; 2-story building 89,780 CFT; 1-story building 17,140 CFT; sidewalk 390.17 SF; monument sign 1 EA; concrete ramp 442.37 SF; brick stair steps 7 EA; pavement with striping 19,363.57 SF; trees/vegetation 2 EA; water line 55.6 LF; power line 965.36 LF; metal handrail 76.2 LF; storm sewer (marked ASSUMED) 107.11 LF; storm structure 2 EA.

## 2. Sheets and spec sections that drive it

- **Civil demolition plan (C-1.0)** `[JOB]`: the only sheet that holds the removal scope. It has a graphic legend (demolish structures, pavement, utilities, curb/gutter, trees) and 11 key notes (1 curb & gutter; 2 building/structure and foundation; 3 sanitary sewer; 4 storm sewer; 5 power; 6 water; 7 pavement; 8 trees/vegetation; 9 sidewalk; 10 monument sign; 11 concrete ramp and stairs). Seven general demolition notes govern: (1) erosion control and tree protection fencing in place before any demolition; (2) comply with laws on harmful materials incl. lead paint and asbestos; (3) **saw cut existing pavement full depth at edge of demolition limits**; (4) all removed items leave the site or are disposed of legally; (5) boundary/topographic survey basis; (7) vertical depth of dry and pressurized utilities is unknown. Scale 1" = 20'.
- **Survey (ALTA/NSPS, 2 sheets)**: building identity and floor elevations (C-1.0 labels "TWO STORY BUILDING F.F.E.=442.2'" and "ONE STORY BUILDING F.F.E.=440.3'" from the survey). Building height is not drawn anywhere on C-1.0; see section 3.
- **C-0.1 general notes, C-2.x erosion/sediment control sheets, L-1.0 landscape**: tree-protection fencing, limits of disturbance, trees to remain vs. remove.
- **C-3.0 / C-4.0 (site and grading)**: show what replaces the removed pavement/buildings and the limit of work; use to confirm the demolition limit and to find items on the survey that are *not* keynoted for removal (to remain).
- **Specification Division 01**: 01 74 19 Construction Waste Management and Disposal `[JOB]` (spec pages 26-37): end-of-project salvage/recycling rate of **75 percent by weight** of non-hazardous solid waste; demolition waste streams named for recycling: asphalt paving, concrete, concrete reinforcing steel, brick, CMU, wood studs and joists, plywood/OSB, wood paneling and trim, structural and miscellaneous steel; demolition waste reported on Form CWM-8. That section cross-references **02 41 16 Structure Demolition** and **02 41 19 Selective Demolition**, and the table of contents lists them, but **neither section is in the specification book supplied** (only 01 74 19 mentions them) `[JOB]`. For this job the drawing notes are the only demolition specification; an AI must not invent removal depths or hazmat responsibility that no document states.
- Typical specification content for the missing sections, for reference: removal depth of structures ("to grade", "top of foundation walls", or a stated depth below grade), interior-wall removal to top of slab, basement slabs broken up for drainage, sidewalks/curbs/gutters/light bases removed as indicated ([UFGS](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2002%2041%2000.pdf), 3.1.1); paving and slabs removed to a stated depth below grade with neat saw cuts at limits (3.1.4).

## 3. Standard measurement rules

### 3.1 Areas (pavement, sidewalk, ramps)
- Measure the closed hatch polygon from the demolition plan at the plan scale; one line per pavement type/keynote. No deductions for openings inside a removed slab ([NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf), 202-4.07).
- Items "W/" something (e.g. "pavement w/ pavement striping") are one line; the striping rides on the pavement SF `[JOB]`. Some agency specs measure pavement-marking removal as its own item (NYSDOT 417-5) ([NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf)); on this job it is not separate.
- Thickness and base: demolition notes may require removal "including aggregate base" to a stated depth ([UFGS](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2002%2041%2000.pdf), 3.1.4). If thickness is not shown on C-1.0 or the geotechnical report, it cannot be derived; quantity stays in SF.
- Building footprints, sidewalks and ramps sit inside or beside pavement polygons: take pavement net of the building footprints so area is not counted twice `[NO SOURCE]`. Sanity check: the reference job's demolition areas sum to 6,202.8 + 19,363.6 + 390.2 + 442.4 = 26,399 SF against a 41,909 SF parcel (0.962 ac, printed on C-1.0), i.e. 63% of the lot, so a total above the parcel area would be an error (calculated in Python).

### 3.2 Buildings
- Two public conventions exist. (a) Lump sum per building, which is how an agency bids it ([NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf), 202-4.02). (b) Volume = footprint x height, the cubic-foot method, which is how the reference estimate carries it (CFT) `[JOB]`.
- Reference-job derivation (calculated in Python): 2-story 89,780 CFT / 4,489.1 SF footprint = **19.9996 ft**; 1-story 17,140 CFT / 1,713.7 SF = **10.0018 ft**. So the estimator took footprint x 10 ft per story, rounded the volume to the nearest 10 CFT, and did **not** add basement or foundation depth, although the keynote says "structure and foundation". Neither C-1.0 nor the survey states a building height, so the 10 ft/story is an estimator assumption `[JOB]`, not a drawn dimension.
- Footprint comes from the hatched building outline on C-1.0 (scale 1" = 20'), cross-checked against the survey outline. L-shaped or stepped buildings are measured as the sum of their parts.
- Foundation scope: "remove foundation walls to the depth of the lowest cellar floor, break up any cellar floor, remove any walkways or other materials, backfill the hole and grade the site" ([NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf), 202-3.02 H); a federal guide spec leaves the depth as a project choice ("to grade / top of foundation walls / [x] below grade", [UFGS](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2002%2041%2000.pdf), 3.1.1). The takeoff must read the stated depth; absent one, say so.
- Pre-demolition survey is a precondition, not a quantity: OSHA requires a written engineering survey of the structure by a competent person before demolition starts ([OSHA-850](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.850), 1926.850(a)); UFGS requires recording elevations of foundation-wall tops, finish floors and conflicting utilities before work (1.11, [UFGS](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2002%2041%2000.pdf)).
- Septic tanks, leaching basins and cesspools tied to a demolished building are pumped, then removed or collapsed in place and backfilled in compacted lifts ([NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf), 202-3.02 I). Watch for them where C-1.0 shows sanitary sewer removal (key note 3).

### 3.3 Linear items and utilities
- Length along the drawn linetype at plan scale, following bends; stop at the removal limit (cut-and-cap point). Utility depth is unknown on this set (general note 7), so only LF can be taken, never trench volume.
- Where the route is inferred from structures only, the estimator labels the line "ASSUMED" (reference storm sewer, 107.1 LF) `[JOB]`; an AI should carry that flag and lower confidence.
- Structures on a line (inlets, manholes, poles, vaults) are counted as EA and listed separately from the LF.
- Pipe left in place is abandoned and capped/filled, a different line from "remove". Flowable fill is its own specification section in public specs (NYSDOT Section 204, Table of Contents in [NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf)). The TakeoffSpeed engine computes fill from nominal bore `[ENGINE]`.
- Overhead and underground power, telephone, gas and fiber are shown on the survey base; only those keynoted or in the "demolish existing utilities" linetype are in scope (this job keynotes power as number 5).

### 3.4 Saw cutting
- C-1.0 general note 3 requires full-depth saw cut at the edge of demolition limits `[JOB]`; federal practice says the same ("neat sawcuts at limits of pavement removal", [UFGS](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2002%2041%2000.pdf), 3.1.4). The takeoff quantity is LF along the boundary **where pavement remains on the other side**, not the full perimeter of the hatch.
- Agencies often make saw cutting incidental: NYSDOT includes "any sawcutting performed in order to facilitate removal" in the slab-removal item (202-5.07/5.08, [NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf)) and in trench surface restoration (206-5.04). The reference demolition legend (page 64) has **no saw-cut row** `[JOB]`, so either it was treated as incidental or it was missed; the estimate's only saw-cut line (364.1 FT, S-201) is a slab control joint (3/S680) and must not be confused with demolition saw cutting `[JOB]`.

### 3.5 Trees
- Count each X-marked tree; record trunk diameter at breast height. DBH is measured 4.5 ft above ground ([NYSDOT-3](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol3.pdf), 614-3.03; general reference [DBH](https://en.wikipedia.org/wiki/Diameter_at_breast_height) for slope and swelling rules). Stump grinding to 6 in below grade with compacted topsoil backfill is part of the tree removal unless a separate item is stated (614-3.03/3.04/5.03).
- Trees that remain need protection fencing: 4-6 ft high fence at a radius of 1.5 ft per inch of DBH ([UFGS](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2002%2041%2000.pdf), 1.3.3 and CRZ definition); C-1.0 general note 1 requires tree protection fencing before any demolition `[JOB]`.
- Tree and landscape-bed removal quantities from C-1.0 ("trees/vegetation", 2 EA) should be reconciled with the landscape sheets (L-1.0) so a tree is not in both demolition and clearing.

### 3.6 Hazardous materials (quantity thresholds)
- Federal asbestos rule: before demolition or renovation the owner/operator must "thoroughly inspect" the affected facility; the full notification/work-practice requirements apply when regulated asbestos-containing material is at least **260 linear feet on pipes, 160 square feet on other components, or 35 cubic feet** off components where length/area could not be measured; notice is due at least **10 working days** before asbestos work begins, and must be updated when the amount changes by **20 percent** ([NESHAP](https://www.law.cornell.edu/cfr/text/40/61.145), 61.145(a),(b)). Residential buildings of four or fewer units are excluded ([EPA summary](https://www.epa.gov/asbestos/asbestos-laws-and-regulations)); a bank branch is not.
- OSHA also requires testing/purging of hazardous chemicals and gases in pipes or tanks before demolition ([OSHA-850](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.850), 1926.850(e)).
- Takeoff treatment: LS line naming the material, the survey/report, and who abates (owner, licensed abatement contractor, or GC). C-1.0 general note 2 puts compliance with laws on lead paint and asbestos on the contractor but supplies no survey or quantity `[JOB]`, so the abatement quantity is "unknown, excluded or allowed by the estimator", never a made-up number.

### 3.7 Selective (interior) demolition (not present on this job; rules for other jobs)
- Interior removals are measured on the demolition floor plan and sections: partitions in LF x height (SF), ceilings and flooring in SF of the hatch, doors/frames/fixtures in EA; slab and wall openings by plan area with **no deduction of openings inside a removed slab** ([NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf), 202-4.07). Cut lines follow the demolition keynotes (UFGS: roofing cut along straight lines; remove only what is needed to make connections, 3.1.5, [UFGS](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2002%2041%2000.pdf)). Handling of door/window deductions on partitions, and typical wall heights, is `[NO SOURCE]` here.

## 4. Conversion, yield and waste factors (with basis)

Removal lines take **no waste factor**. Factors below apply only when disposal or hauling is a separate quantity.

| Factor | Value | Basis |
|---|---|---|
| Nonresidential building demolition debris, by weight | **158 lb per SF of building** (range 36 to 358; 27 surveyed buildings; AGC 2004 survey of 15 projects also 158); single examples: office 101, concrete-block frame 173, department store 165, institutional 182 | [EPA-C&D](https://www.epa.gov/sites/default/files/2017-09/documents/estimating2003buildingrelatedcanddmaterialsamounts.pdf), Table 2-4, section 2.1.4 |
| Same, applied to the reference job | gross floor area 4,489.1 x 2 + 1,713.7 = 10,691.9 SF -> about **845 tons** at 158 lb/SF; 192 to 1,914 tons across the 36-358 range; 540 tons at the office-building 101 lb/SF (calculated in Python). The report's "building size" is treated here as floor area; the source does not define it further. | EPA-C&D Table 2-4 |
| Waste diversion target for this job | 75% by weight of non-hazardous waste; asphalt, concrete, rebar, brick, CMU, wood and steel to be recycled/salvaged | project spec 01 74 19, page 27 `[JOB]` |
| Engine loose debris from buildings | 0.33 CY loose per CY of building volume | `[ENGINE]` convention `demolition.building-debris-ratio`; its stated basis is a rule of thumb. No published source was reachable; `[NO SOURCE]`. For the reference buildings (106,920 CF = 3,960 CY) it gives 1,307 CY loose. |
| Engine pavement bulking | 50% (in place to loose) | `[ENGINE]` convention `demolition.pavement-bulking-pct`; it cites Caterpillar swell tables (40-70%). The handbook could not be fetched; `[NO SOURCE]` for this note. |
| Milled/processed asphalt (RAP) unit weight | 120 to 140 lb/ft3 (1,940 to 2,300 kg/m3), i.e. 1.62 to 1.89 short tons per CY (calculated in Python). Not an intact-pavement or loose-truckload density; match the density to the physical state of the volume. | [FHWA, Reclaimed Asphalt Pavement - Material Description](https://www.fhwa.dot.gov/publications/research/infrastructure/structures/97148/rap131.cfm) |
| Loose/bank conversion | loose = bank x (1 + swell%); bank = loose / (1 + swell%). Arithmetic only; no verified swell percentage for broken concrete or asphalt was found. | arithmetic |
| Pavement in-place volume | SF x thickness / 12 / 27 = CY. Reference pavement 19,363.6 SF: 239 CY at 4 in, 359 CY at 6 in (calculated in Python); thickness is not on C-1.0, so this is illustrative | arithmetic only |

The EPA weight factor and the engine's volume ratio are not interchangeable and disagree in kind (tons vs. CY). Use the EPA factor as an order-of-magnitude **cross-check on a haul-off or disposal quantity**, not as a removal quantity. Where a bidder is asked for tons, ask the hauler for the unit weights they scale at.

## 5. Material breakdown: the removal item and what follows from it

| Primary removal | Follow-on quantities an estimator lists |
|---|---|
| Building structure and foundation | Backfill and compaction of the resulting basement/void/depression, using clean demolition fill or satisfactory soil as specified ([UFGS](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2002%2041%2000.pdf), 2.1; [NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf), 202-3.02 H); temporary fence around any hole not promptly backfilled (same); utility shut-off and cap outside the building line ([OSHA-850](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.850)); dust control by wetting ([NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf), 202-3.01); asbestos/hazmat abatement as a separate item; sorted hauling to recycling streams per 01 74 19 `[JOB]`. |
| Pavement / sidewalk / ramp / curb | Full-depth saw cut at limits where pavement remains (C-1.0 note 3); crushing/grinding and storage of material to be reused on site, otherwise removal from site ([UFGS](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2002%2041%2000.pdf), 3.1.4); disposal or recycling haul-off (asphalt and concrete are on the job's recycling list, 01 74 19 `[JOB]`). |
| Trees | Stump grinding 6 in below grade; stump-hole backfill with compacted topsoil ([NYSDOT-3](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol3.pdf), 614-3.03); chipping/disposal of wood (no burning) ([NYSDOT-2](https://www.dot.ny.gov/main/business-center/engineering/specifications/english-spec-repository/2026_9_specs_usc_tc_vol2.pdf), 201-3); protection fencing for trees that stay. |
| Utility lines | Cut and cap at limits; structures removed (EA); abandon-in-place alternative with fill; trench backfill if removed (earthwork trade); coordination with the utility owner (C-1.0 key notes 3, 5, 6 `[JOB]`; [OSHA-850](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.850), 1926.850(c)). |
| Whole-job | Erosion control and tree protection in place first (C-1.0 note 1); debris chutes if removing floors (chutes steeper than 45 degrees fully enclosed; openings up to 48 in; [OSHA-852](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.852)); waste-management plan and Form CWM-8 reporting (01 74 19 `[JOB]`). |

## 6. Common mistakes and checks

1. **Duplicate keynote numbers.** On C-1.0, key note 2 appears on two buildings and key note 11 on both ramp and brick steps `[JOB]` (legend page 64). Key the quantity by keynote **and** description, never by keynote alone.
2. **Un-keynoted items.** The metal handrail (76.2 LF) has no keynote number but is in the legend `[JOB]`; read linework labels, not only key notes. Listed key notes can also have no quantity: key note 3 (sanitary sewer) has no row in the reference legend `[JOB]`; report "none shown", do not fabricate.
3. **Assumed heights.** Building height is not on C-1.0. The reference used 10 ft per story; the TakeoffSpeed engine defaults to 12 ft per story, which inflates the reference buildings by exactly 20% (2-story: 4,489.1 SF x 24 ft = 107,738 CF vs 89,782 CF at 20 ft; calculated in Python). Always flag a derived height and keep the source of each assumption.
4. **Double counting area.** Pavement net of building footprints; sidewalks/ramps net of pavement. Total demolition area must be below the parcel area (section 3.1).
5. **Missing saw cut or conflating it with slab control joints** (section 3.4).
6. **Hatch vs. "to remain".** Curb on C-1.0 is labelled 24" C&G or 24" roll curb `[JOB]`; only the portion drawn with the demolition curb linetype is removed, so check each run against the legend symbol rather than the label, especially along the right-of-way streets.
7. **Unit slips:** CFT vs CY (divide by 27), SF vs SY (divide by 9), "FT" in the legend vs LF in the estimate, inches written without the inch mark on tree and pipe labels.
8. **Treating a lump-sum building as a measured quantity** when the bid form asks for a lump sum; and the reverse, giving an LS with no volume basis when the estimate carries CFT.
9. **Putting waste on a removal line.** Removal is scope; waste belongs on purchased material only.
10. **Abatement.** Missing hazmat survey: carry an LS with "by owner / by abatement contractor / unknown", plus the NESHAP thresholds as a flag ([NESHAP](https://www.law.cornell.edu/cfr/text/40/61.145)).
11. **Order-of-magnitude check:** debris tons vs. 158 lb/SF x floor area; total demolition SF vs. parcel area; tree count vs. X marks on the plan; building footprint vs. survey outline; storm/utility LF vs. profile sheets.

## 7. What an AI takeoff must read to get demolition right

From **C-1.0** and the survey:
1. The graphic legend (hatch -> structure/pavement/utility/curb/tree) and the key-note table; map every keynote bubble to its linework or hatch.
2. Each hatched polygon (area), curb/utility line (length), X tree and spot symbol (count), using the printed scale 1" = 20' and verifying against dimensioned or labelled values (building outline vs survey).
3. Text labels that change the quantity: "ASSUMED", "ONE STORY / TWO STORY", "F.F.E.", pipe size and material labels (8" sewer, 15" HDPE), tree diameters, "SCALED ONLY", "unable to locate".
4. General notes: saw cut at limits, tree protection, erosion control, hazardous-material compliance, "removed from the site or disposed of in a legal manner", unknown utility depth.
5. Which features are **to remain** (greyed linework) so they are excluded.

From the **specification**:
1. Whether 02 41 16 / 02 41 19 exist and what they say about removal depth, saw cutting, backfill, salvage, hazmat responsibility; if missing (as here), state that the drawing notes are the only source.
2. 01 74 19: diversion percentage (75%) and the recycled material list, which decides whether hauling is split by stream.
3. Allowance items or bid-form items that make disposal a separate quantity.

From **other drawings**: landscape (trees to remain/remove), erosion control (limits of disturbance, protection fencing), grading and site plans (what is replaced), geotech (pavement section and fill), and architectural plans (new building footprint relative to demolished buildings).

Output shape that makes the takeoff checkable: one line per (keynote, description), unit, quantity, how derived (polygon area, run length, count), a flag for each assumed dimension (height, thickness, depth), and a pointer to the sheet region.

## 8. Gaps against the TakeoffSpeed engine (`lib/quantities/trades/site/demolition.ts`)

Comparison only; nothing was changed.
- Story height default 12 ft vs 10 ft in the reference estimate (see section 6, item 3). The engine already warns when height is assumed and caps confidence at low.
- Engine saw-cut and debris assemblies exist; the reference estimate carries neither for demolition, so treat them as optional lines unless the bid form asks.
- The engine's tree assembly bands by diameter; the reference estimate carries trees as a flat 2 EA with no diameter, consistent with C-1.0 not labelling diameters `[JOB]`.
- The two published volume/bulking conventions (0.33 CY/CY, 50% swell) could not be verified from a fetchable source in this pass; treat them as unverified inputs.

Second-opinion note (GPT, as requested): it also could not name a verified source for cubic-foot building-volume conventions, concrete/asphalt swell percentages or selective-demolition opening deductions, and said so. It offered Wisconsin DOT Sections 204 and 690 (measurement units SY/LF for removals, separate LF items for sawing) and an FHWA concrete unit weight of 150 lb/ft3; the Wisconsin URLs returned 404 and the FHWA page did not show the value when fetched, so none of those are cited here. The one GPT lead that verified is the FHWA RAP unit weight in section 4.

## 9. Open items for a follow-up pass (blocked by the search budget)

- RSMeans/Gordian takeoff conventions for cubic-foot building demolition (what height is measured: grade, footing, or roof/parapet; whether basement is included).
- Published swell factors for broken concrete and asphalt (equipment handbooks), and unit weights of concrete and asphalt for tons-to-CY conversion.
- A pavement/curb/sidewalk removal measurement clause from a Southeast DOT (GDOT Section 202) to complement the NYSDOT language; the TxDOT and NYSDOT Vol. 2 sections that were reachable did not cover pavement-removal measurement.
- Selective-demolition measurement rules from a handbook (opening deductions, standard wall heights).
