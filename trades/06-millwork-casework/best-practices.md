# Architectural millwork, casework and countertops: takeoff best practice

Scope: quantities and material types only (no pricing, no labor). Trade folder `trades/06-millwork-casework/`.
Reference job: single-storey bank branch (Div 06 casework 06 4116, countertops 12 3623 and 12 3669).

How to read the citations: every general claim links to a source. Claims about the reference job cite repo files
(`reference/...`, `source/...`, `text/...`) and were computed with python. Items that only come from
a second-opinion model (GPT-6 Astra) or from search-result snippets I could not open in full are marked
**[unverified]** and collected in section 11.

---

## 1. What an estimator takes off, and in which unit

| Item | Unit | Rule | Source |
|---|---|---|---|
| Base cabinet runs | LF along the front, per run | Measured on the interior elevations; keep base and upper on separate lines | [Ruh glossary](https://www.ruh.ai/industrial/construction/glossary/casework), [Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/) |
| Upper / wall cabinet runs | LF | Separate line from base | same |
| Tall units, sink bases, corner units, appliance cabinets | EA | Discrete items are counted, not run through the LF rate | [Ruh glossary](https://www.ruh.ai/industrial/construction/glossary/casework) |
| Casework in LF, then converted to a cabinet count | LF then EA | Takeoff done in LF and converted to box counts | [HiTech Digital](https://www.hitechdigital.com/blog/benefits-of-millwork-quantity-takeoffs-cost-estimation) **[unverified: search snippet only]** |
| Doors, drawers, adjustable shelves, pull-outs, file rails, glass panels | EA each | Counted separately from the cabinet run | [Universe Estimating](https://universeestimating.com/millwork-estimating-101/) |
| Finished ends, fillers, scribe strips, end panels | EA / LF / SF as drawn | Counted as their own item | [Universe Estimating](https://universeestimating.com/millwork-estimating-101/), [Ruh glossary](https://www.ruh.ai/industrial/construction/glossary/casework) |
| Countertops | SF for ordering/fabrication, LF for installed run | Run length x depth, in inches, divide by 144 | [Slabwise](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid), [Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/) |
| Backsplash / end splash | LF x height (SF) or separate LF line | Added separately from the top | [Slabwise](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings) |
| Finished edge profiles | LF of edge that is actually profiled | Record the profile type | [Slabwise](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings) |
| Sink / cooktop / faucet / grommet cutouts | EA, each its own line | | [Slabwise](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid) |
| Seams | EA with location noted | | [Slabwise](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings) |
| Wall paneling, door faces, ceiling panels | SF | | [Universe Estimating](https://universeestimating.com/millwork-estimating-101/) |
| Trim, handrail, shelf runs | LF, to the outside of finished ends | | [Universe Estimating](https://universeestimating.com/millwork-estimating-101/) |
| Lumber | board feet by species, thickness, grade | | [Universe Estimating](https://universeestimating.com/millwork-estimating-101/) |
| Sheet goods (plywood, MDF, particleboard cores) | panel count, kept off the lumber list | Mixing hides waste | [Universe Estimating](https://universeestimating.com/millwork-estimating-101/) |
| Hardware | EA, listed by manufacturer number when the spec names a brand | | [Universe Estimating](https://universeestimating.com/millwork-estimating-101/) |
| Blocking / backing | LF by section, SF by thickness | Confirm who furnishes it (see 4.5) | [Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/), [AWS Sec. 10](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf) |

Takeoff hygiene: confirm the scale on every sheet and check revision dates against the addenda list
([Universe Estimating](https://universeestimating.com/millwork-estimating-101/)); calibrate on a known dimension such as
a 3'-0" door or a 24" base cabinet ([Slabwise](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings));
state quantity and dimensions clearly for every item ([TrueCADD](https://www.truecadd.com/news/millwork-material-estimation-process-guide)).

---

## 2. Which documents drive it

- **Interior elevations and sections** give heights, configuration, door/drawer counts; the **casework plan** gives locations;
  the **casework schedule and details** give material, AWI grade and countertop spec
  ([Ruh glossary](https://www.ruh.ai/industrial/construction/glossary/casework)).
- **Floor plan alone is not enough.** Elevations and schedules hold configuration, hardware and finish
  ([Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/)).
- Review plans, elevations and finish schedules to find every millwork element, then count linear, square and unit quantities
  ([HiTech Digital](https://www.hitechdigital.com/blog/benefits-of-millwork-quantity-takeoffs-cost-estimation) **[unverified: snippet]**).
- Match every elevation tag to a schedule line and flag any tag with no match
  ([Universe Estimating](https://universeestimating.com/millwork-estimating-101/)).
- **Specs:** the casework section (06 41 00 family, here 06 4116) and the countertop sections (12 36 xx, here 12 3623 and 12 3669).
  Specs reference the joint AWI/AWMAC/WI standard and a grade of Economy / Custom / Premium
  ([AWS Sec. 10, 1.1](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)).
  If nothing is specified the AWS default is Custom grade, Type A (frameless), adjustable shelves, flush overlay
  ([AWS Sec. 10, 3.1](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)).
- Shop drawings (after award) are where blocking sizes, cutouts and joint locations get fixed; the specs require them to show
  location of each item, blocking, and cutouts for electrical and other items
  (`text/spec-p135.txt`, 06 4116 1.3.C; `text/spec-p353.txt`, 12 3623 1.2.C).

### Reference job: where the millwork lives

- Enlarged plans and details: A-700 Transaction Bar, A-701 Back Counter, A-702 Library, A-703 Service Counter, A-704 Tech Wall and
  Lounge Booth, A-705 Employee Lounge, A-706 Booth, A-707 Work Room, A-708 Check Desk
  (`reference/sheets/index.json`).
- Finish tags: PL-1/PL1 appears on A-701 to A-707, SLD-1 on A-150, A-700, A-701, A-703, PL-2/PL2 on A-150, A-705, A-707, A-708
  (text-layer grep of `text/A-*.txt`).
- Other sheets with casework content: A-110/A-120 plans (a PL2 countertop and backsplash markup is on A-110), A-410 restroom
  elevations (adjustable melamine shelving in the janitor closet), A-160 furniture and equipment (grommets).
- Specs (`reference/sheets/spec_index.json`): 06 1053 Misc. Rough Carpentry (p.122), 06 1600 Sheathing (p.128),
  06 4116 PL-faced architectural cabinets (p.134), 06 6400 Plastic paneling (p.142), 12 3623 PL-clad countertops (p.353),
  12 3669 Quartz agglomerate countertops (p.358).

---

## 3. Standard measurement rules

### 3.1 Cabinets (LF and EA)

1. Measure each run along the front face from the elevation dimensions, one run per type (base / upper / tall), and carry
   depth, height, door/drawer count and finish tag with it
   ([Ruh glossary](https://www.ruh.ai/industrial/construction/glossary/casework)).
2. Corners: measure to the **centerline** at corner cabinets, not the outside corner, so the corner is not counted twice
   ([Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/)).
   Also AWS notes that corners formed by tall, wall or base casework create non-usable space unless otherwise specified
   ([AWS Sec. 10, 1.2.7.1](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)).
3. Do not copy a similar run; measure each one ([Universe Estimating](https://universeestimating.com/millwork-estimating-101/)).
4. Sanity-check dimensions against AWS ranges (these are ranges, not requirements; coordinate with the specified size)
   ([AWS Sec. 10, 1.5.5](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)):

   | Type | Height | Depth |
   |---|---|---|
   | Base, stand-up counter (floor to top of deck) | 34" to 36" | 24" to 30" |
   | Base, vanity | 31" to 38" | 24" to 30" |
   | Base, sit-down | 28" to 32" (knee space 24-1/2") | 24" to 30" |
   | Wall-hung (including light apron) | 12" to 48" | 12-1/2" to 14" |
   | Tall storage | 72" to 96" | 12-1/2" to 30" |
   | Reception counter | 34"-36" standing side; 28"-32" sit-down | 24"-30" employee side plus 8" more top at customer side |
   | **Teller counter** | 50"-54" customer side at security hood; 40"-42" teller-side transaction top | 24"-32" employee side top plus 8" at customer side |

   The teller and reception rows matter for a bank: transaction-bar tops are taller than normal counters, so a standard 34" base
   assumption is wrong there.
5. Cabinet construction facts that follow from the AWS, useful for what to list under each cabinet line
   ([AWS Sec. 10](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)):
   - Type A is frameless (front edges of body components edge-banded); Type B is face-frame (1.2.17).
   - Interface styles: overlay (flush, reveal, lipped) or flush inset (1.2.18).
   - Finished ends are **integral**, not applied, unless specified otherwise (1.2.7.2).
   - Base/toe is integral or separate at the manufacturer's option (1.2.7.3).
   - The Cabinet Design Series cabinets are drawn with integral finished ends and scribes not exceeding 1-1/2" (1.2.20.1.4).
   - Shelf design load: 40 lb/sq ft general, 50 lb/sq ft for school, hospital, library shelving, max 200 lb per shelf; deflection
     limit L/144 (1.2.21).
   - Storage, janitor and utility-room cabinets are built to Economy grade regardless of project grade unless specified
     otherwise (1.2.7.4). Check whether the spec overrides this for the janitor-closet shelving.
6. Surface categories decide which laminate / material grade goes where, so they decide the material list
   ([AWS Sec. 10, 1.2.10 to 1.2.14](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)):
   - Exposed: everything visible with doors and drawers closed, knee spaces, cabinet bottoms over 42" AFF, tops under 80" AFF.
   - Semi-exposed: interiors seen when doors/drawers open, drawer sides/backs/bottoms, bottoms between 24" and 42" AFF.
   - Concealed: toe space, sleepers and solid sub-tops, bottoms under 24" AFF, underside of countertops, faces of adjoining ends
     that butt together.
   - For decorative-laminate casework at Custom and Premium, exposed exterior surfaces take HPDL; semi-exposed take LPDL
     (1.2.14.1.2, 1.2.14.3.2). In this job the spec instead calls for NEMA LD 3 grades HGS on exposed horizontal, vertical and edge
     surfaces and VGS on semi-exposed surfaces (`text/spec-p137.txt`), so follow the spec.

### 3.2 Countertops (SF, LF, EA)

1. Area = length x depth for each rectangle, in inches, / 144. Split L and U shapes at the inside corner so the overlap is
   counted once ([Slabwise](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid),
   [Slabwise how-to](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings)).
   Worked: 8.0 ft x 2.125 ft + 6.0 ft x 2.125 ft = 29.75 SF (same source).
2. Measure to the cabinet edge, not the wall, and check whether dimensions are to finish face or to stud (drywall about 1/2",
   tile about 3/8" to 3/4") ([Slabwise](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid),
   [Slabwise how-to](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings)).
3. Depth: use the drawn depth. The residential default of 25.5" is a 24" cabinet plus 1.5" overhang
   ([Slabwise](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings));
   a commercial spec overrides it. 12 3623 requires 1" front and end overhang over base cabinets
   (`text/spec-p356.txt`, 2.4.A). Reception/teller tops add 8" at the customer side
   ([AWS Sec. 10, 1.5.5.4 and 1.5.5.5](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)).
4. Seating overhangs on islands are material the floor plan does not show: 12" to 15" is typical
   ([Slabwise how-to](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings)).
   Anything that overhangs needs support; the AWS puts casework and countertop coordination on the casework manufacturer for the
   top and stretchers ([AWS Sec. 10, 1.5.6](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)).
5. Backsplash: usually a 4" or 6" strip, run length x height; full-height splashes (about 18" to 22") add much more material
   ([Slabwise how-to](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings),
   [Slabwise](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid)).
   Example: 10 ft run of 4" splash = 3.33 SF; 14 ft = about 4.7 SF
   ([Slabwise how-to](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings),
   [Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/)).
   Tile backsplash by another trade is excluded
   ([Slabwise how-to](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings)).
6. End splash: spec-driven. 12 3669 lists backsplashes, **end splashes**, apron fronts and wall panels as in scope, with the end
   splash matching the backsplash (`text/spec-p358.txt`, `spec-p360.txt`).
7. Waterfall / apron panels are their own pieces: about 37.25" tall x 25.5" deep (about 6.6 SF) in the residential example
   ([Slabwise how-to](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings)).
   **In this job 12 3669 says "All 90 degree outside edges shall have waterfall finish"** (`spec-p360.txt`, 2.2.B.4), which has to be
   resolved against the drawings: an edge detail or a note on the enlarged plan decides whether each outside corner or free end
   carries a full-height panel.
8. Edges: count the front edge of every run plus any exposed end not against a wall; for islands every outward-facing edge.
   A 4' x 6' island with all four sides profiled is 20 LF
   ([Slabwise how-to](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings)).
   Built-up front edge: 12 3669 specifies 3/4" quartz with the front edge built up from the same material (`spec-p360.txt`, 2.2.C),
   so the build-up strip is extra material by edge LF x build-up depth, not extra full-slab area.
9. Cutouts: each sink, cooktop, faucet hole is its own EA line; the cutout area is generally not subtracted from billed/ordered
   area because the slab is still purchased ([Slabwise](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid)).
   Deduction policy varies by shop (100%, none, or only openings over 2 SF): compute gross area first, then apply the stated policy
   ([Slabwise how-to](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings)).
10. Seams: a run longer than the slab needs a seam. Engineered stone slabs are about 54" to 63" wide
    ([Slabwise how-to](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings)); the Wilsonart guide
    specification gives a minimum slab size of 55" x 120" and 2 cm (0.79") or 3 cm (1.18") thicknesses
    ([Wilsonart guide spec 12 36 61.19](https://images.wilsonart.com/media/Technical_Resources/en/specification_guide-12_3661_19_quartz_surfacing_countertops.pdf)).
    Record seam EA and location. Field joints in laminate tops are secured with concealed clamping devices within 6" of front and
    back edges at intervals not over 24" (`spec-p356.txt`, 12 3623 3.2.C.1), which is a hardware count driven by joints.
11. Plastic-laminate tops: the substrate/core is a quantity too. 12 3623 requires 3/4" exterior-grade plywood core and a
    plastic-laminate backer sheet NEMA LD 3 Grade BKL on the underside (`text/spec-p355.txt`, 2.1.H-J).
    Drawings may call thicker built-up tops (1" or 1-1/2" plywood), so take the thickness from the detail, not the spec default.
    Laminate postformed tops use HGP grade and flat work HGS ([Wilsonart HD laminate TDS](https://images.wilsonart.com/media/Technical_Resources/en/highdefinitiontechdata.pdf)
    gives HGP thickness 0.039" +/- 0.005").
12. Accessibility drives some heights and clear lengths, so they should be read as dimensions on the drawings, not assumed
    ([ADA 2010 Standards ch. 9](https://www.access-board.gov/ada/chapter/ch09/)):
    work/dining surfaces 28" to 34" AFF (902.3); sales and service counters need a portion at least 36" long and no higher than 36"
    (parallel approach) or at least 30" long with knee and toe space (forward approach) (904.4); check-out counters 38" max (904.3.2).

### 3.3 Shelving, brackets, standards, cleats

- Shelves: LF with depth and thickness recorded, EA if sized individually, and the support type (bracket, standard, cleat) counted
  on its own line ([Universe Estimating](https://universeestimating.com/millwork-estimating-101/) lists brackets and hardware as
  counted items; AWS lists shelf standards and rests, metal brackets and filler panels as casework inclusions in
  [Sec. 10, 2.2](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)).
- Bracket spacing comes from the bracket maker and the load, not from a general rule. For concealed countertop brackets, the A&M
  Hybrid sheet is reported to specify 16" to 24" spacing, 3" minimum overhang, and anchoring into studs; the manufacturer
  Chemical Concepts recommends 16" to 20" ([A&M Hybrid install sheet](https://directsupplyinc.com/phocadownload/hybrid-bracket-surface-install.pdf),
  [Chemical Concepts](https://www.chemical-concepts.com/product/counterbalance-hybrid-bracket/)) **[unverified: search snippets, not opened]**.
  Count = ceil(run / spacing) + 1, then adjust for end offsets; use the specified model and the spacing on its data sheet
  (GPT-6 cross-check formula, **[unverified]**).
- Quartz overhang limits differ by maker; one maker's quality agreement requires solid substrate and legs or corbels at no more
  than 36" centers beyond 18" overhang for 2 cm and 21" for 3 cm
  ([MSI QA agreement](https://cdn.msisurfaces.com/files/downloads/q-premium-natural-quartz-quality-assurance-agreement-2010.pdf))
  **[unverified: snippet]**. The specified product's own guide governs; do not carry a generic number.

### 3.4 Wall panels, laminate-faced panels, Z-clips

- Measure panels in SF by material and thickness; trims and reveals in LF
  ([Universe Estimating](https://universeestimating.com/millwork-estimating-101/)).
- Wall surfacing with a defined grain or pattern is installed vertically, which fixes the sheet orientation for yield
  ([AWS Sec. 10, 1.5.4](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)).
- Z-clip hung panels: clip type, thickness (lift-off), spacing and blocking come from the clip maker and the panel weight;
  continuous Z-bar on the wall with pre-cut clips on the panel is a common arrangement
  ([Woodweb Z-clip tips](https://woodweb.com/knowledge_base/ZClip_Panel_Installation_Tips.html)). A 4' x 8' panel typically gets
  three continuous rails at three heights ([Monarch Metal](https://www.monarchmetal.com/?p=659)) **[unverified: snippet]**.
  Rail length = sum of panel widths x number of rows, plus wall-side rail; take rows from the detail.
- FRP wall panels are normally Div 09, but they show up on millwork plans (FRP-1 on A-150/A-410). Estimating: wall area divided by
  the 48" panel width, plus inside-corner, divider and cap moldings
  ([Home Depot FRP guide](https://homedepot.com/c/ah/how-to-install-frp-paneling/9ba683603be9fa5395fab901f292fee3)) **[unverified: snippet]**.

---

## 4. Deductions, additions, scope boundaries

### 4.1 What is deducted

- Cabinet frontage: exclude appliance/open spaces; count the adjacent fillers and panels separately (GPT-6 cross-check, **[unverified]**;
  consistent with AWS listing fillers and scribe strips as separate casework items in
  [Sec. 10, 2.2.19](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)).
- Base molding: deduct door openings of about 3 ft; do not deduct narrower openings because the base returns
  ([Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/)).
- Countertop cutouts: **not** deducted from ordered material
  ([Slabwise](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid),
  [Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/)).

### 4.2 What is added

- Overhangs, returns, backsplashes, end splashes, waterfall panels, built-up edges (see 3.2).
- Door casing: two sides and one head per opening; window casing adds stool and apron
  ([Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/)).
- Fillers, scribes, finished ends, toe base, trim and moldings needed for installation
  ([AWS Sec. 10, 2.2](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)).

### 4.3 Typical casework exclusions (AWS)

Field installation (unless specified), cutting for field-applied vents or hardware, fillers/build-up/sub-tops for tile and stone
countertops, vinyl/rubber/carpet base, metal brackets that are part of the building structure, security panels unless specified,
tote trays and base leveling adjusters unless specified, furring, stripping, blocking, grounds or stub walls, mirrors/glass unless
part of the cabinet, plumbing and electrical fixtures, tile countertops, sink rims, special equipment housed in cabinets
([AWS Sec. 10, 2.3](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)).
Typical inclusions: cabinets, shelving, doors, hinges, drawer guides, pulls, glass doors with hardware, trim and moldings necessary
for installation, filler panels and scribe strips, rough and finish hardware that is part of the cabinet, and cutouts for sinks
([AWS Sec. 10, 2.2](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)).

### 4.4 Blocking and backing: who owns it

- The AWS says structural members, grounds, blocking, backing, furring and brackets that become part of the walls are not furnished
  or installed by the woodwork manufacturer or installer, and that contract documents should require this
  ([AWS Sec. 10, 1.3.3 and 1.5.1](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)).
- This job's 06 4116 reverses part of that: the section **includes** wood furring, blocking, shims and hanging strips for installing
  the cabinets unless concealed within other construction before cabinet installation, which stay in 06 1053
  (`text/spec-p134.txt`, 06 4116 1.1.A.2 and 1.1.B.1). So the takeoff must split blocking by when it is concealed.
  Take the species and treatment from the drawing note (this job has "1x4 fire retardant treated blocking", "2x4 wood blocking",
  "2x6 blocking", per `reference/markups/legends.json`).
- Note on notation: "(7) 1x4 FIRE RETARDANT TREATED BLOCKING" on a detail means 7 rows; LF = run measured x number of rows
  (see section 9, check against the estimate).

---

## 5. Coverage, yield and waste

No standard publishes a single millwork waste factor: the one AWI estimating seminar description says only that it covers waste
factors and materials takeoff, with no figures ([Woodweb: AWI Estimating Seminar](https://woodweb.com/knowledge_base/What_is_the_AWI_Estimating_Seminar_About.html)).
The numbers below are practitioner allowances and disagree with each other; carry them as explicit assumptions and replace them with
nested yields where possible.

| Material | Allowance | Basis / source |
|---|---|---|
| Fabricated cabinets and tops built to size | none on the quantity itself | built to size; waste lives in the shop's material (convention in the app's [millwork.ts](TakeoffSpeed repo: lib/quantities/trades/fitout/millwork.ts)) |
| Sheet goods (plywood, MDF, particleboard) | 10% to 15% | [Universe Estimating](https://universeestimating.com/millwork-estimating-101/) |
| General millwork materials | 5% to 10% | [TrueCADD](https://www.truecadd.com/news/millwork-material-estimation-process-guide) |
| Solid stock | 20% to 30% | [Universe Estimating](https://universeestimating.com/millwork-estimating-101/) |
| Sequence-matched veneer | 25% to 35% | [Universe Estimating](https://universeestimating.com/millwork-estimating-101/) |
| Rectangular countertop | about 10% | [Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/) |
| L- or U-shaped countertop | 15% to 20% | [Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/) |
| Quartz, typical layout | 15% to 20% (also stated as 15% to 25% for granite/natural stone) | [Slabwise](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid) |
| Simple vanity tops | 10% to 15% | [Slabwise](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid) |
| Veined/book-matched slabs | 30%+; a veined slab may yield only about 60% | [Slabwise](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid), [Slabwise how-to](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings) |
| Base molding | 10% (simple) to 15% (many corners) | [Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/) |
| Crown | 15%; 20% to 25% on vaulted/coffered ceilings | [Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/) |
| Edge banding | 5% to 10% provisional, not a manufacturer requirement | GPT-6 cross-check **[unverified]** |

Yield bases (sizes you need to convert SF to pieces):

- **HPL sheets** (Wilsonart HD): 48" x 96", 60" x 96", 60" x 120", 60" x 144" (32, 40, 50, 60 SF)
  ([Wilsonart HD laminate TDS](https://images.wilsonart.com/media/Technical_Resources/en/highdefinitiontechdata.pdf)).
  Verify per pattern; not every size is stocked.
- **Quartz:** minimum slab 55" x 120" (about 45.8 SF gross) ([Wilsonart guide spec](https://images.wilsonart.com/media/Technical_Resources/en/specification_guide-12_3661_19_quartz_surfacing_countertops.pdf));
  usable area about 55 to 60 SF per engineered quartz slab, 55 to 65 SF for granite and natural stone
  ([Slabwise](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid)). The two figures conflict (gross 55 x 120
  = 45.8 SF is below the cited "usable" 55 to 60 SF): confirm the actual slab size with the supplier, not a rule of thumb.
- **Sheet stock:** nominal 4' x 8' = 32 SF ([GPT-6 cross-check](#11-unverified-items-and-gaps), **[unverified]**).
- Weight: 2 cm quartz about 10 lb/SF and 3 cm about 15 lb/SF, which matters for the substrate and support quantities
  ([Wilsonart guide spec](https://images.wilsonart.com/media/Technical_Resources/en/specification_guide-12_3661_19_quartz_surfacing_countertops.pdf)).
- Nesting software replaces generic percentages when shop drawings exist
  ([HiTech Digital](https://www.hitechdigital.com/blog/benefits-of-millwork-quantity-takeoffs-cost-estimation) **[unverified: snippet]**).

---

## 6. Material breakdown an estimator lists

Primary materials by item, with the accessories that follow from them.

### 6.1 Laminate-faced cabinets (06 4116 style)

- Core: particleboard (ANSI A208.1 Grade M-2), MDF (ANSI A208.2 Grade 130), softwood plywood (DOC PS 1), hardwood plywood
  (HPVA HP-1); thermoset (melamine) decorative panels for drawer boxes and some interiors
  (`spec-p138.txt`, 06 4116 2.2.B-C).
- Faces: HPDL NEMA LD 3 by grade: HGS horizontal/vertical/edges, HGP postformed, VGS semi-exposed, BKL concealed backs
  (`spec-p137.txt`, 2.1.H-K). The grade tells the sheet type to list. HGP is the thinner postforming grade and general-purpose
  HGS is flat work only ([Wilsonart HD laminate TDS](https://images.wilsonart.com/media/Technical_Resources/en/highdefinitiontechdata.pdf)).
- Edge banding: PVC tape minimum 0.018" thick matching the laminate on laminate shelves; PVC or polyester banding on thermoset
  panels (`spec-p137.txt`, 2.1.J).
- Adhesives: unpigmented contact cement for laminate, hot-melt for edges (`text/spec-p139.txt`, 2.4.D).
- Hardware named in the spec: frameless concealed European hinges BHMA A156.9 B01602 110 degrees self-closing; back-mounted solid
  metal wire pulls 4" long, 5/16" diameter; shelf rests BHMA B04013; Grade 1 full-extension side-mounted drawer slides; door and
  drawer locks (E07121, E07041) only if the drawings call for locks; silencers BHMA A156.16; finishes BHMA 626 or 652
  (`spec-p138.txt` and `spec-p139.txt`, 2.3).
- Install: wall cabinets fastened through the back near top and bottom and at ends, not more than 16" o.c., with No. 10 screws and
  1-1/2" penetration into blocking (`text/spec-p140.txt`, 3.2.F.2). Fastener counts are not normally taken off
  but the **blocking LF** that these rules require is.

### 6.2 Hardware counts

| Item | Rule | Source |
|---|---|---|
| Hinges per door | Depends on door height and weight. Chart reading: 2 hinges to about 40" and 15 lb, 3 to about 60" (15-30 lb), 4 to about 80" (30-45 lb), 5 to about 100" (45-60 lb); the distance between hinges must exceed the door width. Read off a rendered chart, so treat as approximate. | [Blum Clip Top chart via Richelieu](https://static.richelieu.com/documents/docsGr/100/760/5/1007605/1395028.pdf), p.2 |
| Pulls | One per door/drawer front unless the drawing says two or handleless | GPT-6 cross-check **[unverified]** |
| Drawer slides | One pair per drawer | GPT-6 cross-check **[unverified]** |
| Adjustable shelf pins | About four per shelf | GPT-6 cross-check **[unverified]** |
| Locks | Only where scheduled or noted | [Universe Estimating](https://universeestimating.com/millwork-estimating-101/) (list hardware by manufacturer number) |
| Grommets | Count from drawings (model and location); spec fallback 1 per 4 ft of countertop (12 3669 2.3.A, 2" OD, black, plastic, supplied for field install) | `spec-p360.txt`; drawings A-700, A-701, A-707 name grommets (text grep) |

### 6.3 Laminate countertops (12 3623)

3/4" exterior plywood core (or the thicker built-up substrate shown), HPDL HGS face, BKL backer, edge per drawing, field-joint
clamping hardware, silicone sealant at tops, splashes and walls, support brackets where drawn
(`spec-p355.txt`, `spec-p356.txt`, `spec-p357.txt`). A particleboard core (ANSI A208.1, 45 lb density) is the common manufacturer
default ([VT Industries guide spec](https://www.vtindustries.com/webres/File/tops-surfaces/specifications/high-pressure-decorative-laminate-countertops-guide-specification-10_7_19.pdf));
follow the project spec when it names plywood.

### 6.4 Quartz agglomerate countertops (12 3669)

Quartz slab (ICPA SS-1) of the named product, 3/4" tops with built-up front edge, 3/4" backsplash and matching end splash, plywood
(DOC PS 1 Grade C-C Plugged) or particleboard subtop, seam adhesive color-matched to the top, metal splines where indicated,
wire-management grommets, and sealant per 07 9200 (`spec-p359.txt` to `spec-p361.txt`). Fabricate without joints where possible
(`spec-p360.txt`, 2.2.F), so seams are a layout decision rather than a default. Slab thickness note: Wilsonart's own guide spec
offers 2 cm and 3 cm; a 3/4" built-up top is a project-specific detail
([Wilsonart guide spec](https://images.wilsonart.com/media/Technical_Resources/en/specification_guide-12_3661_19_quartz_surfacing_countertops.pdf)).

### 6.5 Shelving and brackets

Shelf board (melamine or laminate over plywood/MDF), edge banding, brackets by model (this job names KV 180 and A&M HYB brackets
in the estimate descriptions), or standards and rests, or wood cleats.

### 6.6 Wall panels and backing

Panel substrate, laminate face, Z-clips or rails, reveals, and plywood backing behind panels or casework. Backing is measured as
run x height (SF) on the details: "3/4" PLYWOOD @ 7.67H" 8.6 FT is 8.6 x 7.67 = 66.0 SF (python, see section 9).

---

## 7. Common mistakes and how to check

Mistakes (each from a cited source):

1. Estimating from the floor plan alone; elevations and schedules carry configuration, hardware and finish
   ([Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/)).
2. Combining upper and lower cabinet footage into one line
   ([Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/),
   [Ruh glossary](https://www.ruh.ai/industrial/construction/glossary/casework)).
3. Pricing/measuring countertops at the cabinet-run LF despite overhangs and returns; omitting fillers and scribe pieces
   ([Ruh glossary](https://www.ruh.ai/industrial/construction/glossary/casework)).
4. Copying a similar run instead of measuring each one; missing finished ends
   ([Universe Estimating](https://universeestimating.com/millwork-estimating-101/)).
5. Ignoring the AWI grade, or missing a Premium call-out in Div 06 on drawings that look basic; leaving exclusions
   (blocking, electrical, plumbing, stone, appliances) unstated
   ([Universe Estimating](https://universeestimating.com/millwork-estimating-101/)).
6. Mixing lumber and sheet goods on one list, which hides waste
   ([Universe Estimating](https://universeestimating.com/millwork-estimating-101/)).
7. Using a lump allowance for hardware when the spec names a brand
   ([Universe Estimating](https://universeestimating.com/millwork-estimating-101/)).
8. Wrong material tier (laminate rate on a quartz spec)
   ([Virtual Estimation](https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/)).
9. Leaving out internal components and not updating when the design changes
   ([TrueCADD](https://www.truecadd.com/news/millwork-material-estimation-process-guide)).
10. Double-counting L-shape corners; not adding overhang material on islands; scale not calibrated
    ([Slabwise how-to](https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings)).
11. Letting the AWS 80" / 42" / 24" surface-height thresholds go unchecked, which changes which laminate or panel is exposed
    ([AWS Sec. 10, 1.2.10 to 1.2.12](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)).

Checks that need no pricing:

- Every elevation tag maps to a schedule line and a plan location
  ([Universe Estimating](https://universeestimating.com/millwork-estimating-101/)).
- Footage cross-check: base LF vs the countertop run LF on the same plan; countertop LF should exceed cabinet LF where there are
  returns, overhangs or end splashes ([Ruh glossary](https://www.ruh.ai/industrial/construction/glossary/casework)).
- Finish-tag census: every PL-x / SLD-x tag on the finish schedule has a measured SF or LF; every measured SF has a tag.
- Corner check: sum of leg lengths minus overlap squares equals the total area
  ([Slabwise](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid)).
- Hand measurement tolerance: about +/-0.5" on runs under 10 ft, +/-5% for preliminary quantity, 1% to 2% for a firm count
  ([Slabwise](https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid)); estimating accuracy targets of 5% to
  10% for bid and 3% for post-shop-drawing quantities
  ([Universe Estimating](https://universeestimating.com/millwork-estimating-101/)).
- Spec vs drawing conflict log (grommets, waterfall, overhang, substrate thickness): list every conflict and which source was used.
- Re-read the spec grade twice ([Universe Estimating](https://universeestimating.com/millwork-estimating-101/)).

---

## 8. What an AI takeoff must read from the drawings and specs

From **drawings** (enlarged plans, interior elevations, sections, details, finish plan, schedules):

1. Every run of casework by type (base / upper / tall / vanity / transaction bar / desk), with overall front length and each box
   width where dimensioned, depth, height, door and drawer counts, configuration words ("(3) DRAWER", "TRASH", "SINK BASE").
2. Finish tag for each face (PL-1, PL-2, SLD-1, melamine) and the tag's meaning from the finish legend.
3. Countertop plan outline per leg: length, depth, overhang, corner treatment, free ends versus wall ends; substrate and thickness
   from the section (1", 1-1/2" built-up, etc.); support (brackets, corbels, cabinets).
4. Splash height and extent (4" PL splash, full-height, end splash), wall edge versus free edge.
5. Cutout schedule: sinks, grommets (count and model), outlets, cable cutouts.
6. Edge profile and edge LF, plus waterfall panels and aprons.
7. Shelving: depth, material, number of shelves, bracket or standard model.
8. Panels: area, Z-clip rows, reveals, backing plywood run x height, blocking rows "(n) 1x4".
9. Heights AFF for counter tops, teller counters and shelves (the AWS exposure thresholds and ADA clear lengths need them).
10. Notes such as "typical", "similar", "see detail", "N.I.C.", "by owner", or "by others" that move items in or out of scope.

From **specifications**:

1. Grade (Premium here), construction type (frameless), interface (reveal overlay with 1/2" reveal), core materials, laminate
   grades, edge banding spec.
2. Named hardware (hinge type and opening angle, pull length, slides grade, locks) and any counts the spec fixes
   (grommet per 4 ft).
3. Countertop overhang, thickness, edge, backer, joint rules.
4. Scope split for blocking between sections (06 4116 vs 06 1053).
5. Submittal requirements that imply quantities (shop drawings showing blocking and cutouts).
6. Spec-versus-drawing conflicts: report both and use the drawing for locations and counts and the spec for materials.

From the **AWS** standard when the spec only names the standard: default grade, finished ends integral, exposure thresholds, shelf
loading, countertop/casework coordination ([AWS Sec. 10](https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf)).

Output discipline for an AI: report net measured quantity and a separate order quantity with the waste basis named; list
assumptions; never fabricate a count for hardware the drawings do not show. Fabricated units carry no waste in the quantity; raw
stock does (see section 5).

---

## 9. Reference job observations (computed from the repo data)

Computed with python from `reference/markups/legends.json` and `reference/estimate/lines.json` (quantities only).

| Check | Markup legend | Estimate line | Note |
|---|---|---|---|
| SLD-1 quartz top, SF | 73.4 (A-700) + 18.1 (A-701) + 19.7 (A-703) = 111.2 | 111.14 | The estimate carries **net** area; no waste, no cutout deduction |
| PL2 top, SF | 11 (A-110) + 17.4 (A-705) + 22.6 (A-707) = 51.0 | 52 (18 + 12 + 11 + 11, whole SF) | Quantities appear rounded to whole SF |
| PL2 4" backsplash, LF | 13.6 (A-707) + 5.5 (A-110) = 19.1 | 20 (14 + 6) | Splash carried in LF, not SF |
| 3/4" plywood backing, SF | (2 x 3.7 x 1'4") 9.9 + 1.1 + (8.6 x 7.67) 66.0 + 46.9 + 8.0 = 131.8 | 135 | LF x height conversion confirmed |
| 5/8" plywood backing, SF | 37.2 | 40 | Rounded up |
| Booth wall laminate, SF | 296.9 | 300 | Rounded |
| Booth ceiling laminate, SF | 64.2 | 64 | |
| 1x4 FRT blocking, LF (A-701, A-702, A-703, A-705, A-707) | 7x8.6 + 2x14.6 + 4x9.8 + 2x23.3 + 2x15.7 = 206.6 | 240.66 (all) | The "(n)" prefix is a row count; the markup subset does not reach the total, so other pages carry more |
| Melamine shelving (janitor closet), LF | 12.7 (A-410) | 13.0 | |
| Base cabinet LF captured in legends | 10.0 | 39.5 total in estimate | Cabinet runs are not all legend-measured; elevations drive the rest |

Reading the table: the estimator measured countertop SF directly as plan area, splashes as LF at a stated height, plywood backing as
run x height, blocking as run x rows, and shelves and cabinets as LF. A takeoff engine that adds a waste factor to countertop SF
overshoots the estimate line by design, so carry net quantity as the primary result and show the slab/sheet order quantity separately.

Spec-versus-drawing notes found while doing this: the quartz spec requires 1 grommet per 4 ft of top and waterfall finish at all
90-degree outside edges, while the drawings name specific grommets and counts (A-700 shows "GROMMET, SATIN ALUM. (3 TOTAL)"); the
estimate carries 1 EA grommet line. Resolve by taking drawing counts first and the spec rate as a cross-check.

Engine comparison (do not edit): `lib/quantities/trades/fitout/millwork.ts` already keeps cabinets as LF with box counts in the spec,
keeps fabricated units at no waste, carries countertop net SF plus separate LF splash, EA cutout and LF edge lines, computes slab yield by
area with a seam count of ceil(leg / slab long side) - 1, and derives hinges from door height. Gaps relative to the above: no
teller/transaction-counter height sanity bands (it warns on base height outside 24" to 48"), no overhang-support (bracket) spacing rule
for countertops, and hinge counts follow a formula whose constants live outside the repo files I could grep, so verify them against the
Blum chart in 6.2.

---

## 10. Source list

- AWI/AWMAC/WI, Architectural Woodwork Standards 1st ed. 2009, Section 10 Casework: https://woodworkinstitute.com/wp-content/uploads/2014/09/WI_AWS_sec10NM.pdf
- Wilsonart HD laminate technical data (sheet sizes, HGP thickness): https://images.wilsonart.com/media/Technical_Resources/en/highdefinitiontechdata.pdf
- Wilsonart guide specification 12 36 61.19 Quartz Surfacing Countertops: https://images.wilsonart.com/media/Technical_Resources/en/specification_guide-12_3661_19_quartz_surfacing_countertops.pdf
- VT Industries HPDL countertops guide specification: https://www.vtindustries.com/webres/File/tops-surfaces/specifications/high-pressure-decorative-laminate-countertops-guide-specification-10_7_19.pdf
- Blum Clip Top general specifications (hinges per door chart), Richelieu catalog: https://static.richelieu.com/documents/docsGr/100/760/5/1007605/1395028.pdf
- 2010 ADA Standards, chapter 9 built-in elements: https://www.access-board.gov/ada/chapter/ch09/
- Slabwise, how to do a countertop takeoff: https://slabwise.com/guides/how-to-do-a-countertop-takeoff-from-construction-drawings
- Slabwise, countertop fabrication takeoff: https://slabwise.com/guides/what-is-a-takeoff-for-a-countertop-fabrication-bid
- Virtual Estimation, millwork and casework estimating: https://thevirtualestimation.com/blog/millwork-casework-estimating-cabinets-countertops-trim/
- Universe Estimating, millwork estimating 101: https://universeestimating.com/millwork-estimating-101/
- TrueCADD, material estimation for millwork: https://www.truecadd.com/news/millwork-material-estimation-process-guide
- Ruh, casework glossary: https://www.ruh.ai/industrial/construction/glossary/casework
- Woodweb, AWI estimating seminar: https://woodweb.com/knowledge_base/What_is_the_AWI_Estimating_Seminar_About.html
- Woodweb, Z-clip panel installation tips: https://woodweb.com/knowledge_base/ZClip_Panel_Installation_Tips.html
- Project specs (local): `text/spec-p134.txt` to `spec-p141.txt` (06 4116), `spec-p353.txt` to `spec-p357.txt` (12 3623), `spec-p358.txt` to `spec-p362.txt` (12 3669)

---

## 11. Unverified items and gaps

- Web search stopped answering partway through this research (the per-turn search budget was exhausted), so several intended
  sources were not retrieved: AWS Section 11 (Countertops) text, the Wilsonart Quartz Fabrication and Installation Guidelines
  (QZ0200, the copy I downloaded was truncated and image-based), a Cambria/other maker overhang table, and a Marlite FRP
  installation sheet. Seam placement, maximum unsupported overhang, and countertop-support spacing therefore remain **open**:
  take them from the product guide named in the spec.
- Items marked **[unverified: snippet]** come from search-result summaries of pages I did not open in full (HiTech Digital,
  A&M/Chemical Concepts bracket sheets, MSI QA agreement, Monarch Metal, Home Depot FRP guide). Re-open before relying on the number.
- Items marked GPT-6 cross-check come from a single question to GPT-6 Astra (generic, no project data): pulls one per front, one
  slide pair per drawer, four shelf pins per shelf, 5% to 10% edge-banding allowance, 48 x 96 sheet = 32 SF, bracket count formula
  ceil(run / spacing) + 1, record countertop area gross before cutouts. They are plausible practice, not cited standards.
- The waste table mixes sources whose bases differ (some are estimating-service blogs); they are starting points only. The quartz
  usable-area figure (55 to 60 SF) conflicts with the 55" x 120" minimum slab size (45.8 SF gross); treat it as supplier-confirmed only.
- The Blum hinge-count thresholds were read by eye from a rendered chart in a 2004 Richelieu catalog; confirm against the current
  Blum planning tool for the specific hinge and door weight.
- The AWS text used is the 1st edition (2009, grade rules excluded from the free copy); later editions (NAAWS) may change figures.
  Check the edition named in the project spec (this job's spec says only "Architectural Woodwork Standards").
