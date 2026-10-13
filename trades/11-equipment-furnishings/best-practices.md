# Best practice: quantity takeoff for appliances, equipment, shades, furniture (and the Div 10 / Div 12 items that travel with them)

Scope: quantities and material types only. No prices, labor or productivity. Trade folder `11-equipment-furnishings`.
Job: single-storey bank branch (Fifth Third Bank, Watson Blvd., Warner Robins GA; Praxis3 permit set 07/02/2026).

Source quality key. **[P]** primary (code, standard text, manufacturer data sheet or install instruction, or the project's own spec/drawings). **[S]** secondary (vendor guide, fabricator blog, owner design standard, sample bid clarifications). Where I could not reach a primary source the claim is tagged [S] or listed in section 10. The web-search budget ran out before every gap could be closed; section 10 lists what is still unverified.

---

## 1. What an estimator takes off, and in which unit

This trade is mostly a count-and-schedule trade. The unit is almost always **EA by schedule tag**, with a handful of SF/LF measured items.

| Item class | Typical CSI | Unit | What is counted/measured | Basis |
|---|---|---|---|---|
| Toilet accessories (dispensers, grab bars, mirrors, waste, hooks, mop holder, napkin disposal) | 10 28 00 | EA per tag, per room | Each accessory by schedule tag, per room; grab bars by length and orientation | Spec 10 2800 requires a "Product Schedule ... types, quantities, sizes, and installation locations by room" ([local spec p335](file://text/spec-p335.txt)); a published owner schedule allows "1 per WC" for tissue dispensers and "1 per accessible WC" for the horizontal grab bar ([Winnipeg A850 schedule](https://legacy.winnipeg.ca/finance/findata/matmgt/documents/2025/63-2025_B/63-2025B_Addendum_3/63-2025B_Addendum_3-Drawing_A850-R1.pdf)) [S] |
| Signage (tactile room signs, restroom signs, occupant-load sign) | 10 14 00 | EA per schedule line | Each sign by size/type; mount per ADA | [ADA 703.4](https://www.access-board.gov/ada/) [P] |
| Fire extinguishers + cabinets/brackets | 10 41 13, 10 44 16 | EA, counted twice: cabinet (or bracket) and extinguisher | Recessed cabinets (F.E.C.) and surface-mounted extinguishers (F.E.) are different items | Project legend on G-001 shows both ([local G-001](file://text/G-001.txt)); spec 10 4413 / 10 4416 ([local p339-346](file://text/spec-p339.txt)) |
| Appliances | 11 31 00 | EA per AE tag | Each scheduled appliance, only where the schedule says the GC provides and/or installs | Project A-170 Appliance Schedule has "PROV. BY / INST. BY" columns ([local A-170](file://trades/11-equipment-furnishings/scripts/research/equipment/a170.png)) |
| Bank equipment (cash chest, VAT, ATM, recyclers, etc.) | 11 17 00 | EA per BE tag | Normally vendor-furnished and vendor-installed; GC carries only rough-in/coordination | Project A-170 Bank Equipment Schedule: every row is VENDOR/VENDOR |
| Window shades (motorized roller) | 12 24 13 | SF of shade (fabric width x drop), plus EA for motors/controls/pockets | One shade per opening bay; width and drop from the opening | Project spec 12 2413 ([local p347-352](file://text/spec-p347.txt)); estimate carries SF |
| Countertops (quartz, solid surface, laminate) | 12 36 23, 12 36 69 | SF of top; LF of splash/edge/apron if separated; EA cutouts | Net area by rectangle, 25.5 in typical depth; splashes separate | [Slabwise takeoff](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid), [Slabwise L-shape](https://slabwise.com/guides/how-to-calculate-square-footage-for-l-shaped-countertops) [S] |
| Entrance floor mats and frames | 12 48 13 | EA (or SF) per mat, plus LF of frame | Mat size "as indicated", single unit per location | Project spec 12 4813 ([local p363-365](file://text/spec-p363.txt)) |
| Loose furniture (chairs, sofas, tables, planters, lockers, shelving) | 12 50 00 / FF&E | EA per furniture tag | Count tags on the furniture plan, reconcile to the furniture schedule | A-160 plan + A-170 Furniture Schedule |

Boundary to keep clear: plastic-laminate **cabinets and PL countertops** are architectural millwork (Div 06 / 12 3623 in the spec). In this job's estimate, PL countertops sit in DIV 06 (millwork) and the quartz/solid-surface top sits in DIV 12. A takeoff must pick one home for each item and not count it twice.

---

## 2. What drives it on this job (sheets and spec sections)

Sheets (see `reference/sheets/index.json`):
- **A-160 Furniture & Equipment plan**: where each furniture (CH, SS, TB, ST, WS, PL...) and equipment (AE, BE) tag lands. Tags are counted by reading the plan.
- **A-170 Schedules**: Appliance Schedule (item, description, mfr, model, **PROV. BY, INST. BY**, location, comments), Bank Equipment Schedule (same columns), Furniture Schedule (dimensions, model, color, no PROV/INST columns), Finishes Schedule (MECHO shade, SLD-1, PL-1..6, MT-1 mat).
- **A-410 Toilet room enlarged plans and elevations**: accessory tags TA-1..TA-10, grab-bar heights (33-36 in) and clearances.
- **G-001 Cover / life safety**: signage schedule, F.E. and F.E.C. symbols, note "provide fire extinguishers per NFPA 10 as required", extinguisher type "10LB UL RATED 4A:80B:C" ([local G-001](file://text/G-001.txt)).
- **A-130 Reflected ceiling plan**: motorized MechoShade symbol, run lengths and the note "GC TO PROVIDE, INSTALL AND COORDINATE PROGRAMMING OF MOTORIZED MECHOSHADES" ([local A-130](file://text/A-130.txt)).
- **A-700 to A-708 millwork elevations**: countertop extents and splash/overhang details.
- **E-703 / E-100 series**: MechoShade control switch locations (4 EA in the estimate).
- **A-150 floor finish plan**: MT-1 anti-static mat and entrance mat recesses.
- **P-series plumbing**: electric water cooler, wall valve box for countertop drinking equipment (these sit in Div 22 in the estimate, so do not double count them in Div 11).

Spec sections present in `reference/sheets/spec_index.json`: 10 2800 Toilet Accessories (p335), 10 4413 Fire Extinguisher Cabinets (p339), 10 4416 Fire Extinguishers (p344), 12 2413 Roller Window Shades (p347), 12 3623 PL Countertops (p353), 12 3669 Quartz Agglomerate Countertops (p358), 12 4813 Entrance Floor Mats and Frames (p363). There is **no spec section for signage, appliances (11 31 00), bank equipment or furniture**; those are defined only by the A-170 schedules and notes. An AI must therefore treat A-170 as the contract definition for these items.

---

## 3. Measurement rules

### 3.1 Count items (toilet accessories, extinguishers, appliances, furniture, signs)
- Count by **tag, by room**, from the plan elevations and schedule; check that the two agree. Spec 10 2800 itself asks for a product schedule "by room of each accessory required" ([local p335](file://text/spec-p335.txt)).
- Do not add waste or spares to count items. The only published "extra stock" rule found is for shades: 5 percent of units installed per size/colour/material, minimum 2 units, in a university master spec ([University of Houston 12 24 13](https://www.uh.edu/facilities-planning-construction/vendor-resources/owners-design-criteria/master-specs/pdf/12-2413-window-roller-shades-manual-09.2023.pdf)) [S]. Apply it only if this project's spec requires attic stock (the project's 12 2413 as extracted does not).
- Dual-use items: a grab bar has a **length and an orientation**; count a 42 in horizontal and an 18 in vertical bar as different items.

### 3.2 Toilet accessories: rules that fix quantity and location
- **Grab bars at a water closet** ([ADA 2010 Standards 604.5, 609](https://www.access-board.gov/ada/)) [P]: side-wall bar at least 42 in long, within 12 in of the rear wall, extending at least 54 in from the rear wall; rear-wall bar at least 36 in long, extending 12 in minimum one side of the WC centerline and 24 in minimum the other. Bar cross-section 1-1/4 to 2 in diameter; 1-1/2 in wall clearance; mounted 33 to 36 in above finish floor to top of gripping surface.
- Spec 10 2800 3.1.B: grab bars installed to withstand at least 250 lbf downward (ASTM F 446) ([local p336-337](file://text/spec-p336.txt)). Bobrick's install sheet for its swing-up bar says 500 lb at any point and requires adequate backing in the wall ([Bobrick 4998 install](https://www.bobrick.com/wp-content/uploads/4998_ii.pdf)) [P].
- **Toilet tissue dispenser**: centerline 7 to 9 in in front of the WC, outlet 15 to 48 in above floor ([ADA 604.7](https://www.access-board.gov/ada/)) [P]. One per water closet is the usual schedule convention ([Winnipeg A850](https://legacy.winnipeg.ca/finance/findata/matmgt/documents/2025/63-2025_B/63-2025B_Addendum_3/63-2025B_Addendum_3-Drawing_A850-R1.pdf)) [S].
- **Mirror** above a lavatory: bottom of reflecting surface 40 in max above floor; elsewhere 35 in max ([ADA 603.3](https://www.access-board.gov/ada/)) [P].
- Dispenser vs grab bar: a protruding dispenser must be more than 12 in above or 1-1/2 in below the grab bar, or at the end; recessed dispensers are allowed at bar ends ([Bradley ADA design guide](https://s3.amazonaws.com/s3-absupply-net/pdf/Bradley_ADA_Design_Guide.pdf)) [S]. This matters because a conflict means an extra backing/relocation item, not a quantity change.
- Reach: everything a user must reach should be within 48 in of the floor ([Bradley guide](https://s3.amazonaws.com/s3-absupply-net/pdf/Bradley_ADA_Design_Guide.pdf)) [S].
- Recessed waste receptacle: Bobrick B-3644 needs a framed opening 16 in wide x 29-1/4 in high and 4 in minimum recess depth, 12 gal, mount 42 to 46 in off floor ([Bobrick B-3644 data sheet](https://www.bobrick.com/wp-content/uploads/B-3644_td.pdf)) [P]. The estimator lists the cabinet; the framing is carried by the wall trade.

### 3.3 Signage
- Tactile sign: baseline of lowest tactile character at least 48 in, baseline of highest at most 60 in above floor; on the latch side of a single door, on the inactive leaf of a pair with one active leaf, to the right of the right-hand door for two active leaves; 18 x 18 in clear floor space beyond swing ([ADA 703.4](https://www.access-board.gov/ada/)) [P].
- Count signs by schedule line and room. The project's G-001 legend counts 3 (6x4 tactile), 1 (men's), 1 (women's) ([local legends](file://reference/markups/legends.json), page 2).
- Site/ADA parking signs, stop signs and monument signs are Div 32 on this job; keep them out of Div 10.

### 3.4 Fire extinguishers and cabinets
- Travel distance to an extinguisher: 75 ft or less for Class A hazards ([OSHA 29 CFR 1910.157(d)(2)](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.157)) [P]. NFPA 10 uses the same 75 ft figure and measures it as actual walking distance, so partitions and door swings lengthen it ([Serviced Fire Equipment NFPA 10 guide](https://servicedfireequipment.com/nfpa-10-placement-spacing-guide/)) [S].
- Mounting: extinguishers of 40 lb or less: top no higher than 5 ft above floor; over 40 lb: top no higher than 3-1/2 ft; bottom at least 4 in above floor ([same guide](https://servicedfireequipment.com/nfpa-10-placement-spacing-guide/)) [S].
- Area limit (secondary table, NFPA 10 Table 6.2.1.1 itself not retrieved): light hazard, 3,000 sq ft per unit of A rating up to a cap of 11,250 sq ft per extinguisher; so a 4-A unit covers up to 11,250 sq ft. The vendor table lists 2A = 6,000, 3A = 9,000, 4A = 11,250 sq ft for light hazard and 4A = 6,000 sq ft for ordinary hazard ([same guide](https://servicedfireequipment.com/nfpa-10-placement-spacing-guide/)) [S]. Arithmetic check: 2 x 3,000 = 6,000 and 3 x 3,000 = 9,000, consistent with that rule (python verified).
- Rule of thumb that follows (my inference from the two limits above): the count is the **larger** of the area-based count and the travel-distance-based count. In a small single-storey building the 75 ft travel distance usually governs, not the 11,250 sq ft area.
- Take off **two lines per location**: the cabinet (recessed or semi-recessed, if scheduled) and the extinguisher. Surface-mounted extinguishers have a bracket instead of a cabinet. The project spec lists all three: cabinets (10 4413), extinguishers, and mounting brackets (10 4416 2.3) ([local p344-346](file://text/spec-p344.txt)).
- Cabinet size and wall depth must be coordinated; spec 10 4413 1.3 says "Coordinate sizes and locations of fire protection cabinets with wall depths" ([local p339](file://text/spec-p339.txt)).

### 3.5 Window shades (roller)
- Unit: **square feet = fabric width x drop**, one shade per opening bay (or per spec-defined run). Width and drop must come from the opening, not from the plan run length alone.
- Commercial fabrication deductions in an owner master spec for between-jamb installs: width = jamb-to-jamb less 1/4 in per side (1/2 in total), +/- 1/8 in; length = head-to-sill less 1/4 in ([UH 12 24 13](https://www.uh.edu/facilities-planning-construction/vendor-resources/owners-design-criteria/master-specs/pdf/12-2413-window-roller-shades-manual-09.2023.pdf)) [S]. Retail guides show fabric about 1 to 1-1/2 in narrower than ordered width to clear brackets/motor and no deduction on height ([Select Blinds measuring guide](https://selectblinds.com/measure/measure-roller-shades.html)) [S] (consumer guide, so use only as a sanity check).
- Seams and battens: avoid them where possible; where width-to-length ratio is 1:4 or greater, battens and seams at uniform spacing; where roll width is less than shade width, railroad the fabric ([UH 12 24 13](https://www.uh.edu/facilities-planning-construction/vendor-resources/owners-design-criteria/master-specs/pdf/12-2413-window-roller-shades-manual-09.2023.pdf)) [S]. Project spec repeats the 1:4 batten rule ([local p351](file://text/spec-p351.txt)).
- Installed clearance: opaque shadebands not closer than 2 in to the interior face of glass (project spec 3.2.A.1, [local p351](file://text/spec-p351.txt)).
- Fabric stock widths constrain how tall a shade can be without railroading: a dealer listing shows ThermoVeil 1300 stocked in 63 in and 96 in widths, with 126 in only in some colours ([Sweets listing](https://sweets.construction.com/manufacturer/cube-care-company-nst154185/products/motorized-shades-nst869812-p)) [S, verify with the manufacturer].
- Motorized extras are counted separately: motor per shade, **keyed control station** (open/close/off, two keys per station), limit switches, power disconnect, wiring from controls to motors (project spec 2.2.B, [local p348-349](file://text/spec-p348.txt)).

### 3.6 Countertops
- Measure **net area by rectangle**: length x depth / 144. For an L, split at the inside corner so the corner square is counted once; add peninsula or seating overhang as its own rectangle ([Slabwise L-shape](https://slabwise.com/guides/how-to-calculate-square-footage-for-l-shaped-countertops)) [S].
- Depth: typical kitchen top 25 to 25.5 in (24 in cabinet + 1 to 1-1/2 in overhang); vanity tops about 22 in; using 24 in instead of 25.5 in under-measures by about 6 percent ([Slabwise L-shape](https://slabwise.com/guides/how-to-calculate-square-footage-for-l-shaped-countertops)) [S]. 24/25.5 = 0.941, so the shortfall is 5.9 percent (python verified). Always read the depth from the millwork section, not the default.
- Measure to the cabinet edge, not the wall (walls bow) ([Slabwise takeoff](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid)) [S].
- Backsplash: standard 4 in integral splash, or 18 to 36 in full-height; keep splash area out of the top total unless bundled ([Slabwise L-shape](https://slabwise.com/guides/how-to-calculate-square-footage-for-l-shaped-countertops)) [S]. The project spec lists separate quartz **countertops, backsplashes, end splashes, apron fronts and wall panels** (12 3669 1.2) and says tops are 3/4 in thick with a built-up front edge, 3/4 in backsplash, matching end splash, and "all 90 degree outside edges shall have waterfall finish" ([local p358-360](file://text/spec-p359.txt)). Take off tops, splashes, end splashes, aprons and waterfall returns as separate lines.
- Cutouts: sink and appliance cutouts are not normally deducted from billed area ([Slabwise takeoff](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid)) [S]; count each cutout as an EA item. Project spec: undercounter fixtures cut in shop from the fixture template; coordinate utility penetrations (1.8).
- Seams: required when the run exceeds slab length; standard quartz slabs about 122 x 55.5 in (47 sq ft) and jumbo 132 x 65.5 in (60 sq ft) ([Cambria seams](https://www.cambriausa.com/cambria-style/blog/what-to-know-about-quartz-surface-seams)) [S]. Seams are best placed over cabinet support, away from sink cutouts. Project spec: "Fabricate countertops without joints where possible" ([local p360](file://text/spec-p360.txt)).
- Plastic laminate tops: substrate thickness and edge detail are in the millwork keynote (the estimate lines show 3/4, 1 and 1-1/2 in plywood tops with brackets); count the substrate, brackets, and edge band with the top.

### 3.7 Entrance mats and frames
- Mats are custom sized: the project spec says "Mat Size: As indicated", single unit per installation, recessed frames of extruded aluminum with latex leveling screed, vinyl trim closure, and concrete fill/grout ([local p363-365](file://text/spec-p363.txt)).
- Frame LF = mat perimeter; frame shipped separately in advance for standard rectangles; non-rectangular mats need a template ([Construction Specialties FAQ](https://admin.c-sgroup.com/entrance-flooring/faq)) [P]. Rail depth 11 mm with a 13 mm recessed frame in the UK data ([NBS Source Pedimat](https://source.thenbs.com/en/gb/product/cs-pedisystems-pedimat-entrance-matting-systems/qA78QqMZULYGVV9rvxjyVv/rRpJQ1G19KzWufoAU2XQzq)) [S]; take the US depth from the project submittal.
- The recess itself is a concrete-trade item: spec 1.2 "Coordinate size and location of recesses in concrete".

### 3.8 Appliances and equipment: what the GC counts
- Count the appliance **only where the schedule makes it GC scope**. On A-170 the Appliance Schedule shows AE-01 to AE-04 and AE-06 as GC provided / GC installed, AE-07 as vendor provided / GC installed, and AE-09 to AE-15 (TVs, wall mount, security monitor, charging cabinet, MFP) as vendor / vendor. All Bank Equipment (BE-01 to BE-11) is vendor / vendor (read from [A-170 render](file://trades/11-equipment-furnishings/scripts/research/equipment/a170.png)).
- Ownership codes are standard: OFOI = owner furnished and owner installed; OFCI = owner furnished, contractor installed; CFCI = contractor furnished and installed ([California courts cost-responsibility matrix](https://courts.ca.gov/system/files/solicitation-request-document/cmar-indioconstruct-rfp-attachi.pdf)) [S]. FF&E is normally bought and installed by the owner or a separate contractor, while the GC carries coordination, blocking, rough-ins and final connections ([constructionbids.ai FF&E glossary](https://constructionbids.ai/resources/glossary/ffe)) [S]. "NIC" marks an item the design team has excluded from the GC scope ([EngineerFix NIC](https://engineerfix.com/what-does-nic-not-in-contract-mean-in-construction/)) [S]. A real bid-clarification list excludes "appliances, furniture, furniture partitions, equipment" ([NE Construction clarifications](https://www.neconstruction.com/hubfs/All%20Proposal%20Documents/Wood%20River/Clarifications%20Wood%20River.pdf)) [S]. Always take the Prov. By / Inst. By columns over these defaults.

---

## 4. Coverage, yield and waste factors (with basis)

| Item | Factor | Basis |
|---|---|---|
| Count items (accessories, signs, appliances, furniture, extinguishers) | No waste | Counted installed quantity |
| Roller shades, attic stock | 5 percent of units per size/colour/material, minimum 2 units (only if spec asks) | [UH master spec 12 24 13](https://www.uh.edu/facilities-planning-construction/vendor-resources/owners-design-criteria/master-specs/pdf/12-2413-window-roller-shades-manual-09.2023.pdf) [S] |
| Roller shade fabric | Net SF of finished shade; width deduction 1/2 in total (between jambs) | same [S]; fabric waste from roll width is the fabricator's, not the GC's |
| Countertop slab purchase | Laminate post-form 10 percent, custom laminate 10-15, engineered quartz 15, granite 15-20, marble 15-25, butcher block 10-15 | [Slabwise L-shape table](https://slabwise.com/guides/how-to-calculate-square-footage-for-l-shaped-countertops) [S]; a second article gives 10-15 simple vanity, 15-20 quartz kitchens, 30+ for book-matched ([Slabwise takeoff](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid)) [S]. These are fabricator purchasing factors. A GC/estimator carries **installed net SF** unless the bid method is material-only |
| Quartz slab size | 122 x 55.5 in (47 sq ft); 132 x 65.5 in (60 sq ft) | [Cambria](https://www.cambriausa.com/cambria-style/blog/what-to-know-about-quartz-surface-seams) [S]; another fabricator guide says 55-60 sq ft standard ([Slabwise takeoff](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid)) [S]. Confirm with the supplier |
| Seam allowance | Seam when run exceeds slab length; about 0.75 sq ft per seam in a calculator page | [calculator page, weak](https://www.diysmarthomehub.com/?p=18848) [S, low confidence] |
| Fire extinguisher coverage | 3,000 sq ft per A-unit light hazard, cap 11,250 sq ft; 75 ft travel | [Serviced Fire Equipment](https://servicedfireequipment.com/nfpa-10-placement-spacing-guide/) [S], [OSHA 1910.157](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.157) [P] |
| Takeoff accuracy targets | Firm bid 1-2 percent; plan takeoff 5-10 percent margin (countertops) | [Slabwise takeoff](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid) [S] |

No published coverage/yield exists for furniture, appliances or shades beyond the above; do not invent one.

---

## 5. Material breakdown: primary items and what follows from them

**Toilet accessories** (spec 10 2800: ASTM A 666 type 304 stainless 0.031 in, mirrors ASTM C 1503 6 mm, universal keys):
- Primary: tissue dispenser, towel dispenser, soap dispenser, recessed/surface waste, grab bars (42 in, 36 in, 18 in), mirror, sanitary napkin disposal, coat hook, mop holder.
- Follows: **blocking/backing** for grab bars (wood backing 2 in minimum or 12-ga steel plate per one manufacturer; Bobrick calls for 3/16 in steel with drilled and tapped holes) ([Swanstone grab bar info](https://xrefs2.plumbersstock.com/Swanstone/Grab-Bar-Info.pdf) [S], [Bobrick 4998](https://www.bobrick.com/wp-content/uploads/4998_ii.pdf) [P]); framed rough openings for recessed units (B-3644: 16 x 29-1/4 in, 4 in deep) ([Bobrick B-3644](https://www.bobrick.com/wp-content/uploads/B-3644_td.pdf)); tamper-resistant fasteners (spec 2.1.E).

**Fire extinguishers**: extinguisher 10 lb, 4-A:60-B:C per spec 10 4416 (drawing legend says 4A:80B:C; a mismatch to flag); recessed/semi-recessed cabinet or steel bracket with red "FIRE EXTINGUISHER" decals; framed wall opening, trim (spec 10 4413/10 4416).

**Roller shades** (spec 12 2413, MechoShade basis, ThermoVeil Dense Basket Weave 1300 series, 5 percent open, colour 1319 Silver Birch per A-170): shadeband fabric; roller tube; motor; brackets/endcaps; bottom hem bar with light seal; **recessed shade pocket** with end plates and removable bottom closure panel + wall clip; keyed control station (2 keys/station); limit switches; low-voltage control wiring. A MechoShade pocket product also provides a wiring raceway ([Mecho pocket spec](https://www.arcat.com/specification/mecho-34104/09_54_00msi)) [S]. Pockets must be coordinated with the ceiling trade; the spec places them in "site-constructed ceiling recess".

**Countertops**: top (3/4 in quartz, built-up edge), backsplash (3/4 in), end splash, apron front, waterfall returns, plywood subtop (spec 2.1: exterior softwood plywood C-C Plugged), adhesive, splines at joints, sealant at walls (07 9200), cutouts, support brackets for overhangs.

**Entrance mats**: mat (28 oz level-cut nylon pile inserts on 2 in aluminum rails, vinyl cushions), recessed aluminum base frame, latex leveling screed, vinyl end trim, concrete fill/grout ([local p363-365](file://text/spec-p363.txt)).

**Appliances (rough-in requirements that follow; verify on the actual submittal)**:
- Quench Q8CT countertop cooler: cold potable water only, 40 to 60 psi, 3/8 in OD compression angle stop, dedicated 120 V/15 A circuit with the outlet within 6 ft and no extension cords, 14 x 20 in countertop space with at least 18 in clearance above, 3/8 to 1 in water-line hole (installer can drill to 2 in through laminate or Corian only) ([Culligan Quench Q8 install requirements](https://quench.culligan.com/wp-content/uploads/2024/12/InstallationRequirements_Q8_11202024_LR.pdf)) [P]. This is why a countertop cutout/grommet and a wall valve box (Div 22) follow from AE-06.
- GE PDT145SGL dishwasher: 24 x 24 x 34-1/2 in opening (retailer listing), outlet within 6 ft, drain hose 10 ft max in generic GE manuals ([GE quick spec](https://static.pcrichard.com/docs/PDT145SGLBB_Quick_Specs.pdf)) [S].
- Refrigerator (AE-03) with interior water dispenser: a water stub is implied by the schedule note; microwave (AE-02) counter-top plug-in; microwave drawer (AE-01) built into base cabinet with power.
- Elkay EZSTL8C bi-level cooler (Div 22 on this job): 115 V, 8 GPH, indoor use; related model lists 4 A ([Elkay spec sheet](https://hdsupplysolutions.com/wcsstore/ExtendedSitesCatalogAssetStore/product/fm/additional/74/749450_Spec%20Sheet_Original.pdf)) [S].
- ADA: refrigerator/freezer clear floor space parallel approach, centerline offset 24 in max; at least 50 percent of freezer space at or below 54 in ([ADA 804.6.6](https://www.access-board.gov/ada/)) [P]. Work surfaces 28 to 34 in high ([ADA 902.3](https://www.access-board.gov/ada/)) [P].

**Furniture**: count by tag; the sub-components (pillows PW-01..03, charge station, planter) are separate tags. Anchoring, power/data grommets and locker bases are listed on the schedule only when GC scope; table grommet locations are flagged on A-160.

---

## 6. Standard practice for conflicting scopes

1. Read PROV. BY / INST. BY first. Price/quantity only the GC-provided or GC-installed rows.
2. For "vendor provided, GC installed" (AE-07 here), carry install quantity but not the item.
3. For vendor/vendor items, carry only **rough-in and coordination** (power, data, blocking, conduit stubs) located by the electrical/plumbing sheets. The ATM, drive-up VAT tube and canopy on this job are explicitly "by bank equipment vendor, coordinate prior to rough-in" (estimate lines 712/717; [A-130 CP3](file://text/A-130.txt)).
4. Keep a one-line clarification for every TBD (CH-06, SS-05 on the furniture schedule list "TBD").

---

## 7. Common mistakes and how to check

| Mistake | Check |
|---|---|
| Counting vendor-installed items as GC scope (or the reverse) | Reconcile every AE/BE tag against Prov./Inst. columns; list excluded tags |
| Counting plan tags but missing items only in the schedule (or the reverse) | Two-way tag reconciliation: plan tag set = schedule tag set |
| Double counting at trade boundaries (PL countertops in millwork vs Div 12, EDF in Div 22 vs Div 11, shade control switches in Div 26 vs 12) | One home per item; cross-list |
| Counting one grab bar per toilet room | Per WC: side-wall 42 in plus rear 36 in bar, plus any vertical bar the detail shows ([ADA 604.5](https://www.access-board.gov/ada/)) |
| Missing the extinguisher when counting the cabinet | Two lines per location (cabinet + extinguisher), plus surface-mounted units with brackets |
| Shade SF from plan run length x one assumed drop | Use each opening's width and drop; check fabric roll width, pockets, 1:4 batten ratio |
| Countertop depth 24 in instead of 25.5 in | Read millwork section: about 6 percent short ([Slabwise](https://slabwise.com/guides/how-to-calculate-square-footage-for-l-shaped-countertops)) |
| Counting backsplash/apron/waterfall inside the top area | Separate lines per spec 12 3669 1.2 |
| Applying fabricator slab waste to an installed-quantity takeoff | Carry net SF; only add waste when the bid method is material purchase |
| Forgetting backing | Grab bars, FE cabinets, recessed waste, shades pockets, countertop brackets all need a wall/ceiling item |
| Ignoring "TBD" schedule rows | Flag; do not default |
| Mixed units from the schedule (SH-03 "53 W x 18 D x 70.5 H") | Furniture is EA; dimensions are not measured quantities |

Sanity ratios: an estimate quantity should reconcile with plan measure within a few percent (countertops are typically held to 5 to 10 percent on plan takeoff per [Slabwise](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid) [S]).

---

## 8. What an AI takeoff must read from the drawings and specs

1. **Schedules first**: A-170 (appliances, bank equipment, furniture, finishes). Capture ID, description, model, dimensions, **Prov./Inst. by**, location, comments (e.g. "18 in ADA compliant", "interior water dispenser", "provide power in base cabinet" for AE-14).
2. **Plans second**: A-160 tags (OCR the tag text, count each occurrence, note duplicates like CH-11 x4), A-410 enlarged toilet rooms (tag, mounting height, grab-bar length), G-001 signage and F.E./F.E.C. symbols, A-130 shade symbol with run and heights.
3. **Specs third**: for each item the spec section tells material, thickness, accessories and "provided by" language (for example 12 2413: pocket and closure panel; 12 3669: waterfall edges, no joints; 12 4813: mat per location).
4. **Elevations/sections**: heights for shades (sill/head), countertop depth and overhang, backsplash height, mounting heights.
5. **Cross-sheet notes**: "GC to provide, install and coordinate programming of motorized MechoShades" (A-130); vendor-coordination notes at ATM/canopy.
6. **Existence checks**: no spec for signage, appliances, furniture; flag that these have only the schedule.
7. Unit decisions: shades in SF; countertops in SF; cabinets/millwork in LF; everything else in EA; never convert furniture dimensions into area.

---

## 9. Cross-check against this job's reference data (quantities only)

Computed in python. Estimate = `reference/estimate/lines.json`; markup = `reference/markups/legends.json`.

| Item | Reference estimate | Markup legend | Observation |
|---|---|---|---|
| SLD-1 quartz top | 111.14 SF | 73.4 (A-700) + 18.1 (A-701) + 19.7 (A-703) = 111.2 SF | Difference 0.06 SF; area is a sum of three elevation sheets |
| PL2 countertop | 18 + 12 + 11 + 11 = 52 SF | 11 (A-110) + 22.6 (A-707) + 17.4 (A-705) = 51.0 SF | Difference 1.0 SF |
| Motorized shade | 1,184.4 SF (labelled "75 LF") | 74 FT (A-130) | 1,184.4/75 = 15.79; 1,184.4/74 = 16.01. Consistent with about 74 LF x about 16 ft drop; the estimate carries SF where the plan measure is LF, so the drop must come from an elevation (storefront height). |
| Mats | MT-1 36 x 48 in = 12.0 SF each, estimate 10 SF | MAT-1 6 SF | Three different numbers for one anti-static mat; read A-150 and A-170 to resolve |
| Furniture tags | Plan tag counts on A-160 equal the estimate counts for all tags checked (CH-01 2, CH-02 2, CH-03 2, CH-04 3, CH-06 2, CH-07 1, CH-08 1, CH-10 2, CH-11 4, PL-02 2, SS-01 2, SS-03 1, TB-01 1, TB-02 2, TB-04A 1, TB-05B 1, WS-01 1) | n/a | Counting plan tags reproduces the estimate |
| Appliances | AE-01, 02, 03, 04, 06, 07 | n/a | Exactly the rows A-170 gives to the GC for provide or install; AE-09, 10, 13 appear on the plan but are vendor/vendor and correctly absent |
| Signs | 3 + 1 + 1 | 3 + 1 + 1 | Match |
| Toilet accessories | per A-410: 2 each TA-1, 2, 5, 4, 6; TA-3 2 x 42 in + 2 x 18 in; TA-8 1; TA-9 2; TA-10 1 | n/a | Two restrooms; verify whether a 36 in rear bar (ADA 604.5.2) is drawn, since only 42 in horizontal and 18 in vertical bars are listed |
| Fire extinguishers | 2 cabinets | n/a | Drawing shows both F.E. (surface) and F.E.C. (recessed) symbols with a 10 lb 4A:80B:C extinguisher; no extinguisher line item exists in the estimate, and the spec says 4-A:60-B:C. Count both and flag the rating mismatch |

---

## 10. Gaps and unverified items

- NFPA 10 Table 6.2.1.1 and ADA Section 216 (which signs are required) were not read at source; the extinguisher area table is from a vendor guide that is arithmetically consistent with the 3,000 sq ft per A-unit light-hazard rule but is secondary.
- No RSMeans or other cost-guide unit-of-measure table could be retrieved; units in section 1 come from project spec/estimate conventions and published schedules, not from a cost book.
- No AWI/NAAWS countertop section, laminate sheet size, or solid-surface sheet yield could be retrieved (search budget exhausted); laminate/solid-surface waste factors rest on fabricator blogs.
- No MechoShade measuring guide or max-size chart could be retrieved; the shade deductions come from an owner master spec and a consumer guide.
- Keurig K4500 (AE-07) plumbing configuration, Whirlpool WRFC2036RZ and Sharp SMD3070ASY install data not retrieved.
- A second-opinion query to GPT-6 Astra was started (per the user's permission to use the OpenAI key); its answer had not returned when this was written and none of its figures is used above.
