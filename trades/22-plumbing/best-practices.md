# Plumbing (Div 22): piping, fixtures, drains, gas. Quantity-takeoff best practice

Scope: quantities and material types only. No pricing, labor or productivity.
Project evidence below is from the reference job (single-storey bank branch, Praxis3 permit set, 1,900 SF) and is cited by file path, not URL.

**How to read the citations.** Links are the sources I could actually open or see excerpted. Where a page blocked fetch (HTTP 403/404) and I only saw a search excerpt, the line says "(search excerpt)". Where I found no authoritative source, the line says **UNSOURCED** or is listed in section 11. The web-search budget for this session ran out, so a few topics (hubless coupling bracing, IPC 709.1 table text, roof-drain sizing, trap primers) are only partly covered.

---

## 1. What the estimator takes off, and in which units

| Item class | Unit | Notes |
|---|---|---|
| Pipe, each system x size x material x location | LF | One takeoff item per system, size and material. Water, sanitary, vent, storm and gas are usually on different sheets ([zzTakeoff](https://www.zztakeoff.com/trades/plumbing-takeoff-software); [Simpro](https://www.simprogroup.com/blog/take-off-commercial-plumbing-job), search excerpt). |
| Fixtures (WC, LAV, sinks, mop sink, fountain) | EA by tag | Check the count against the fixture schedule ([zzTakeoff](https://www.zztakeoff.com/trades/plumbing-takeoff-software)). |
| Floor, roof, canopy and overflow drains; cleanouts; hose bibs, hydrants; valves; equipment | EA by tag/type | Valves and cleanouts are counted ([zzTakeoff](https://www.zztakeoff.com/trades/plumbing-takeoff-software)). |
| Fittings | EA by size and type, or a carried allowance when not drawn | See 3.3. |
| Hangers, supports, riser clamps, rod | EA / LF derived from LF of pipe and the spacing rule | STACK's plumbing assemblies derive hangers from the linear takeoff and a spacing you enter ([search excerpt of STACK help](https://help-preconstruction.stackct.com/docs/stack-quick-start-assemblies-division-22-plumbing)). |
| Pipe insulation | LF by pipe size and thickness | Carried as its own linear quantity by size and thickness; paired supply and return double the footage ([search excerpt, RUH glossary](https://www.ruh.ai/industrial/construction/glossary/hydronic-piping)). |
| Gas pipe paint | LF | Reference job carries "safety yellow paint at roof gas pipe" in the plumbing markup (P-303) and in Div 09 (see section 9). |

A complete commercial takeoff is a full inventory of fixtures, pipe sizes and lengths, and every fitting, valve and hanger. One fixture ties into several systems (water, sanitary, vent, storm, gas), each on its own sheet ([Simpro](https://www.simprogroup.com/blog/take-off-commercial-plumbing-job), search excerpt). RSMeans' plumbing estimating text organises the work around pipe and fittings for interior plumbing and takeoff quantity sheets ([publisher listing](https://www.abebooks.co.uk/9780876297049/Means-Plumbing-Estimating-Methods-Third-0876297041/plp), search excerpt of table of contents). I could not open the book, so its conventions are not reproduced here.

## 2. Sheets and spec sections that drive it

**Generic (any job):** plumbing plans per system (sanitary/foundation, domestic water, roof/storm, gas), the isometric/riser diagrams, the schedules (fixtures, piping, drains, water heater), details, and general notes. Also the architectural plans, because architectural drawings are the reference to check against ([FieldPulse](https://www.fieldpulse.com/resources/blog/plumbing-takeoff)). Gather the site plan, architectural, mechanical and demolition drawings as well (same source). Civil drawings own everything past the building line.

**This job:**

| Need | Where |
|---|---|
| Abbreviations, symbols | `P-001` (text: `text/P-001.txt`) |
| Piping schedule: system, size band, material, joint, fitting type, horizontal and vertical hanger spacing, notes A to K and 1 to 4 | `P-101` |
| Sanitary and storm below slab, fixture tags, invert elevations ("REFER TO CIVIL I.E. (-)2'-0\""), key notes | `P-301` |
| Domestic water, vent, fixtures, above-ceiling piping, shutoff valves, hose bibs, wall valve box | `P-302` |
| Roof storm: roof drains, overflow drains, canopy drains, RTU gas, condensate | `P-303` |
| Isometrics | `P-401`, `P-402` (risers), `P-403` (gas assembly per RTU) |
| Details: cleanout pad, hanger/insulation shield, water heater, hose bib, roof hydrant, drain box | `P-501` |
| Common results, space priority, code compliance | Spec 22 05 00 (page 367) |
| Insulation: thickness, where required, where not | Spec 22 07 00 (pages 382-383) |
| Pipe materials, joints, valves, cleanouts, floor drains, trap primers, slope, vent offsets | Spec 22 10 00 (pages 384-390) |
| Fixture trim, P-traps, stops, ADA mixing valves | Spec 22 40 00 (page 391 on) |
| Gas paint note | `P-403` "PIPE PAINTING NOTE" |

## 3. Standard measurement rules

### 3.1 Pipe length
- Measure along the pipe centerline on the plan, by system, size and material, and add the vertical rises and drops read from risers, elevations and notes (for example "4\" UP TO RD", "3\" DN", "1\" NG UP TO A/C"). A plan-only measurement misses verticals. Plumbing plans are diagrammatic, so route, rise and drop must be read from the notes and isometrics. Spec 22 05 00 1.3B in this job states "The engineering drawings are diagrammatic".
- Sizes change along a run. Break the run at every size change and add each piece to its own size item. In the reference job the same size appears on several sheets and is summed: 1-1/4" CW = 2.0 ft (P-301) + 62.5 ft (P-302) = 64.5 ft against the estimate's 64.58 ft; 3" storm = 33.5 + 25.8 + 91.2 = 150.5 ft against 150.59 ft (python check, `reference/markups/legends.json` vs `reference/estimate/lines.json`).
- **Slope does not change length meaningfully.** An 86.73 ft run at 1/8 in per ft drops 0.90 ft, and the hypotenuse is 0.0047 ft longer than the plan length (python). Slope matters instead for invert elevations, trench depth and the vertical drop to carry into the next system. Spec 22 10 00 1.3I requires drainage piping to slope "not less than 1 percent" in the direction of flow; the code minimums are 1/4 in/ft for 2-1/2" and smaller and 1/8 in/ft for 3" to 6" ([study-guide summary of IPC 704.1](https://open-exam-prep.com/study-guides/icc-commercial-plumbing/sanitary-drainage-systems/drainage-installation-slopes); secondary source, search excerpt only, verify in the adopted code).
- **Measured through or deducted?** Two conventions exist, so state which one the quantity uses.
  - "Measured through" runs centerline to centerline and includes in-line components; fittings are then counted separately, as in the ASTM insulation measurement practice excerpt ([ASTM C1409-98 text](https://softbank.iust.ac.ir/Railway/Codes/ASTM-standard/ASTM_2004_Standards/ASTM%202004%20PART%20IB/ASTM%202004%20Volume%2004.06%20Thermal%20Insulation_%20Environmental%20Acoustics/C%201409%20-%2098%20%20_QZE0MDKTOTG_.pdf), search excerpt; the page itself flags it as superseded).
  - "Cut length" deducts the fitting take-off values (ASME B16.9) from the run, which is the rule for welded process piping ([EPCLAND](https://epcland.com/quantity-take-off-piping/)). This is a process-piping source, so treat it as a different convention, not plumbing practice.
  - Reference-job evidence: the estimate's pipe LF equals the plan-measured legend LF within 0.1 ft for all 17 pipe lines, with no deduction for fittings and no waste added (python comparison). Treat that as "measured through, net".
- Underground pipe that stays outside the building is a Div 33 line in this estimate (6" sanitary sewer 295.96 LF, underground gas service 152 LF, 6 exterior 4" cleanouts). The plumbing sheets stop at the "REFER TO CIVIL" notes. Take the split from the notes and do not count both.

### 3.2 What to count and what not to
- Count each size of each system separately. Do not net hot and cold together.
- Do not count a pipe twice because it appears on two sheets (floor plan and isometric). Measure on one sheet and use the other as a check ([Simpro](https://www.simprogroup.com/blog/take-off-commercial-plumbing-job), search excerpt: check isometrics against the plan view).
- Count a typical repeated unit once and multiply ([zzTakeoff](https://www.zztakeoff.com/trades/plumbing-takeoff-software)).
- Do not deduct for valves or fixtures connections; valves are counted EA (above).

### 3.3 Fittings
- Count fittings from the drawings and isometrics when they are drawn (tees, wyes, long-sweep 90s, transitions, couplings, unions, reducers). An EPCLAND process-piping page lists ignoring small-bore fittings as a common error ([EPCLAND](https://epcland.com/quantity-take-off-piping/)).
- When they are not drawn, carry an allowance. I found **no published fitting-per-100-LF ratio** in any open source I could read ([FieldPulse](https://www.fieldpulse.com/resources/blog/plumbing-takeoff) and [Simpro](https://www.simprogroup.com/blog/take-off-commercial-plumbing-job) do not give one). The TakeoffSpeed engine defaults (15 EA/100 LF drainage, 20 EA/100 LF water, 15 EA/100 LF gas in `TakeoffSpeed repo: lib/quantities/trades/mep/pipe.ts`) are labelled there as "estimator rule of thumb" and are **UNSOURCED**.
- The reference estimate does not count fittings at all. It carries one lump-sum line "ALLOWANCE PROVIDED FOR FITTING & VALVES: 2000 SF" (line 403, qty 1 LS), so fittings quantity cannot be validated against it.
- Design-mandated fittings that must be counted explicitly because the drawings call them out (reference job): double combo wye at the low-flow WC connection (P-301 key note 7); horizontal intercepting trap under the exterior wall with cleanout left as an air inlet (P-301 key note 5); eccentric reducers flat-on-top for horizontal water size changes (spec 22 10 00 1.3F); dielectric unions at dissimilar metals (P-303 general note 4); unions at appliance connections; hubless couplings with stainless bands (1-1/2" to 3" two bands, 4" to 8" four bands, spec 22 10 00 2.1C).

### 3.4 Hubless joints
For hubless cast iron, each joint takes one shielded coupling, so couplings follow joint count, which follows stick length (10 ft lengths are permitted at 10 ft hanger spacing per the IPC table note; see 4.1). Count one coupling per actual joint, including each pipe-to-fitting joint, not one per fitting (GPT-6 Astra second opinion, section 12; uncited). Example, python: 58.18 ft of 2" vent in 10 ft sticks has 5 straight-pipe-to-pipe joints, and every fitting adds its own joints on top. Read the fitting joints from the isometric.

### 3.5 Openings, corners, laps, heights
These wall-trade concepts map to plumbing as follows.
- **Wall and floor penetrations**: each exposed pipe through a wall, floor or ceiling takes a chrome escutcheon where visible (spec 22 40 00 1.1D) and a sleeve or firestop where the wall is rated. The sleeve/firestop count is read from the wall type schedule and is not shown on plumbing sheets. **UNSOURCED** as to quantity rules.
- **Heights** drive mounting accessories and vertical pipe: lavatory rim 34" AFF max, drinking fountain spout 36" AFF, wall hydrant 24" centerline above grade, mop-sink wall faucet per elevations (fixture schedule text in estimate lines 422, 424, 429, `P-501`). Vertical rise to a fixture = ceiling or slab elevation minus fixture connection height.
- **Roof penetrations** (vent through roof, gas up to RTU, roof drains) are counted EA as flashing/curb items; the vent through roof must offset so it terminates at least 15 ft from any HVAC outside-air intake (spec 22 10 00 1.3J).

## 4. Standard spacing and coverage figures with basis

### 4.1 Hanger and support spacing (maximum, feet)
Basis: IPC Table 308.5 as reproduced in the Connecticut State Building Inspector document ([CT DAS, IPC/IMC proposed amendment text](https://portal.ct.gov/-/media/DAS/Office-of-State-Building-Inspector/2022-CCPs/22-004-SBC-Roger-Stolting---PEX-Piping.pdf), text extracted with PyMuPDF) and the reference job's own schedule (`P-101`).

| Material | Horizontal | Vertical | Source note |
|---|---|---|---|
| Cast iron | 5, or 10 where 10 ft lengths are installed | 15 | CT doc table note b; `P-101` notes 1-2 add one extra hanger at each joint |
| Copper or copper-alloy tubing, 1-1/4" and smaller | 6 | 10 | CT doc; `P-101` ("1-1/4" and smaller": 6 / 10) |
| Copper tubing, 1-1/2" and larger | 10 | 10 | CT doc; `P-101` |
| Copper or copper-alloy pipe | 12 | 10 | CT doc |
| Steel pipe | 12 | 15 | CT doc |
| PVC pipe | 4 | 10, with a mid-story guide | CT doc; `P-101` shows 4 / 10 |
| ABS pipe | 4 | 10 | CT doc |

Conflicts: [Engineering Toolbox DWV table](https://engineeringtoolbox.com/drainage-pipe-supports-d_1106.html) lists PVC and ABS vertical spacing at 4 ft, DWV copper 10/10 and cast iron 5/15 with "the base of each stack must be supported". A [Chicago local amendment excerpt](https://dev-codelibrary.amlegal.com/codes/chicago/latest/chicago_il/0-0-0-2539846) (search excerpt) also lists PVC vertical at 4 ft. The adopted code edition and any local amendment decide, and the project schedule overrides both when it is stricter.

Gas pipe, [IFGC Table 415.1 as printed in the 2021 Seattle Fuel Gas Code ch. 4](https://seattle.gov/documents/departments/sdci/codes/fuelgascode/2021sfgcchapter4.pdf) (text extracted with PyMuPDF):

| Steel pipe size | Spacing |
|---|---|
| 1/2" | 6 ft |
| 3/4" or 1" | 8 ft |
| 1-1/4" or larger, horizontal | 10 ft |
| 1-1/4" or larger, vertical | every floor level |

Smooth-wall tubing: 1/2" OD 4 ft, 5/8" or 3/4" OD 6 ft, 7/8" or 1" OD horizontal 8 ft. CSST follows the manufacturer. The reference schedule is stricter than the code table for 1-1/4" to 1-1/2" gas (8 ft vs 10 ft) (`P-101`).

Steel pipe hanger spans and rod sizes by pipe size (7 ft at 1/2" to 1", 12 ft at 3", with 3/8" rod through 2" and 1/2" rod at 2-1/2" to 4"; the page's column labels are garbled, so verify against the linked PDF) are on [Engineering Toolbox](https://www.engineeringtoolbox.com/piping-support-d_362.html). Clemson's Div 22 standard sets 3/8" as the smallest hanger rod ([search excerpt](https://cufacilities.sites.clemson.edu/documents/departments/pdc/code-and-procurement/ae-standards/divisions/D_22.pdf)).

**Hanger count rule.** Number of hangers = ceiling(run length / spacing), plus one if both ends of an open run need a hanger. A practice-quiz answer of 25 for 198 ft at 8 ft is wrong: 198/8 = 24.75, so 25 spaces and 26 hangers with a starting one (python; the quiz is the [EstatePass item](https://www.estatepass.ai/contractor/questions/fl-projmgmt-e-methods-prod-t01-020/), search excerpt). Add the extra hanger per joint when the schedule says so (`P-101` note 1), add a hanger on both sides of concentrated loads such as valves ([Engineering Toolbox](https://www.engineeringtoolbox.com/piping-support-d_362.html)), and exclude below-slab and underground pipe (`P-101` general note G).

Worked example (python), spacing from `P-101`:

| Run | LF | Spacing | Hangers (ceil) | Hangers (ceil + 1) |
|---|---|---|---|---|
| 1" HW | 162.22 | 6 | 28 | 29 |
| 1-1/4" CW | 62.5 | 6 | 11 | 12 |
| 3/4" gas | 44.21 | 8 | 6 | 7 |
| 4" vent (hubless) | 47.29 | 5 | 10 | 11 |

### 4.2 Cleanouts (count rules)
- At the base of each waste or soil stack; at each change of direction greater than 45 degrees; at most 100 ft apart on horizontal drains and building sewers; where several direction changes occur in one run, one cleanout per 40 ft of developed length is required; cleanout size equals the pipe size up to 4", and at least 4" for larger pipe ([PHCP Pros summary of IPC 708.3 and 708.7](https://www.phcppros.com/articles/1902-code-requirements-for-drainage-system-cleanouts); [constructionbids.ai](https://constructionbids.ai/resources/glossary/cleanout)).
- UPC differs: a cleanout for each 100 ft or fraction, and for each aggregate horizontal change over 135 degrees ([PHCP Pros](https://www.phcppros.com/articles/1902-code-requirements-for-drainage-system-cleanouts)). Confirm the adopted code.
- Reference job: floor cleanouts at least 4" with scoriated bronze plate (spec 22 10 00 2.1E). Exterior cleanouts are brought to grade in an 18"x18"x6" concrete pad (`P-303` general note 3, `P-501`). The estimate carries the pad twice: 1 EA / 0.041667 CY in Div 03 (matches 18x18x6 in = 0.0417 CY, python) and 6 pads in Div 32.

### 4.3 Gas appliance connections
Per [IFGC 408.4](https://seattle.gov/documents/departments/sdci/codes/fuelgascode/2021sfgcchapter4.pdf): a sediment trap downstream of the appliance shutoff valve, as close to the inlet as practical, as a tee with a capped vertical nipple, unless the appliance has one. The reference job's per-RTU kit (`P-403` notes): manual shutoff valve, drip leg, two test ports (1/8" NPT plugs) upstream and downstream of the regulator, line pressure regulator, union, flexible connector reduced to RTU inlet size. Two RTUs shown, so 2 of each.

### 4.4 Trap sizes (for fixture accessories)
Minimum trap sizes commonly listed for IPC Table 709.1: lavatory 1-1/4", drinking fountain 1-1/4", domestic kitchen sink 1-1/2", floor drain 2" ([study-guide extract](https://open-exam-prep.com/study-guides/va-plumber/sanitary-drainage-systems/drainage-fixture-units), secondary; search excerpt). Water closets have integral traps. The schedule model (for example McGuire P-trap numbers in the reference job) overrides these.

### 4.5 Pipe stock lengths and coils (yield)
Copper tube per CDA: straight lengths 20 ft for Types K and L up through 8"; coils 60 ft and 100 ft for 1/4" to 1", 60 ft for 1-1/4" and 1-1/2", 40 or 45 ft for 2" for K and L ([CDA table](https://copper.org/applications/plumbing/cth/technical-data/tables/cth_table1.php), 403 on fetch, figures from search excerpt; the [archived copy](https://archive.copper.org/applications/plumbing/cth/technical-data/tables/cth_table1.php) returned 401). Example (python): 162.22 ft of 1" HW in 20 ft sticks is 9 sticks at 0%, 5% and 10% waste, so rounding to stock length absorbs the waste.
Stock lengths for PVC and hubless cast iron: not verified (the schedule's note 2 in `P-101` only confirms 10 ft cast iron lengths exist).

## 5. Waste factors and their basis
- **Only published figure found:** 5 to 10% cutting contingency for pipe, 5% typical and up to 10% on complex routing, 10-15% for small bore, with a recommendation not to apply one blanket percentage to all sizes and materials ([EPCLAND](https://epcland.com/quantity-take-off-piping/)). This is a process-piping source, so it is a starting point, not plumbing-specific data.
- No plumbing-specific waste percentage is published in the sources I could read ([FieldPulse](https://www.fieldpulse.com/resources/blog/plumbing-takeoff) says explicitly it gives none; [zzTakeoff](https://www.zztakeoff.com/trades/plumbing-takeoff-software) also gives none).
- Recommended handling: report **net LF** as the takeoff quantity (it matches the reference estimate within 0.1 ft), then convert to purchase quantity by stock length (20 ft copper sticks, coils for soft 1/2"-3/4" below slab, 10 ft DWV sticks) and keep waste as a separate, labelled line. Reference job: pipe waste is 0% in the estimate.
- Counted items (fixtures, drains, valves) carry no waste.
- Below-slab soft copper must be continuous with no joints (spec 22 10 00 2.2C; `P-303` general note 7), so coil leftover is real waste and is not offset by reusing short cuts.

## 6. Material breakdown an estimator lists

**DWV pipe run** (sanitary, vent, storm): pipe by size; fittings (wye, tee, sanitary tee, 45, long-sweep 90, reducer, increaser, test tee, trap adapters, cleanout tee and plug); joint material (hubless couplings with shield and bands per joint, or PVC primer and solvent cement for socket joints, spec 22 10 00 2.1A-C); hangers and rod per 4.1, with one extra hanger per joint where scheduled; riser clamps per floor; polyethylene encasement of cast and ductile iron in corrosive soils (`P-101` note H); sleeves and firestop; cleanouts; test plugs. Hub drain reducer fittings one nominal size larger than the connected pipe (spec 22 10 00 2.1I).

**Domestic water run**: copper tube by size and temper (hard Type L above grade, soft Type K continuous below slab); wrought copper fittings; solder or press joints; hangers and rod; riser clamps; isolation valves (ball valves, full port at 3/4" and smaller, stem extensions for insulation, spec 22 10 00 2.2G-H); balancing valves with two gauge taps (2.2I); check valves; dielectric unions at dissimilar metals; insulation (see below); labels (`P-501`, "PROVIDE PIPE LABELS REF. SPECIFICATIONS"); pressure-reducing valve set at 60 psi, pressure gauge, whole-building sediment filter and replacement cartridge (`P-501`, `P-302` key note 5).

**Insulation** (spec 22 07 00): pipe insulation by size and thickness. Hot water: 1-1/2" thick for pipe 1-1/2" and smaller, 2" thick above 1-1/2". Cold water: 1" thick. Fibreglass with all-service jacket and vapor barrier tape; closed-cell elastomeric for any insulated pipe below ground; continuous over valve bodies, fittings and penetrations; not over hot-water unions, gauges or handwheels. Cold water in interior plumbing chases with no exterior wall, and drained-down exterior cold water, are exempt. Hanger insulation shields per hanger manufacturer (`P-101` note F). Note the conflict on this job: `P-302` says "ALL HOT AND COLD WATER LINES TO BE INSULATED" while spec 22 07 00 3.2A exempts interior chase cold water. Flag and ask.

**Fixture** (per tag): fixture; trim or faucet; supplies with stops (WC angle stop 3/8" in the schedule); P-trap model; tailpiece/outlet; wall-hung carrier or fixture support; ASSE 1070 point-of-use mixing valve on every lavatory hot connection (spec 22 40 00 1.1J); insulation kit on trap, stops and supplies for ADA fixtures (estimate line 424 names the McGuire PRO-WRAP kit); escutcheons; WC seat; vacuum breaker on mop-sink faucet; hose and hook for mop sink. The tag schedule in the estimate shows how much accessory text sits in the fixture note itself (lines 421-440).

**Drains**: floor drain with trap primer connection and trap insert (JR Smith 2010, estimate line 433); canopy drain; roof drain with sump receiver, under-deck clamp, gravel guard; overflow drain with 2" dam, installed 2" higher than the primary (`P-303` key note 1); roof hydrant drain tube to nearest drain; hose bib drain tube (copper) to nearest drain.

**Trap primers**: required at floor drains, floor sinks, trench drains and hub drains, except where the drain routes to the storm system; tapped off top of horizontal line with isolation valve (spec 22 10 00 1.3K). In this job, 1/2" soft copper below slab to prime floor drains (`P-302` key note 4). Count one primer connection per floor drain and add the tube LF.

**Water heater**: heater; shutoff valves on inlet and outlet at 4 to 5 ft AFF; circulation pump; expansion tank; ASME T&P relief valve; vacuum relief valve; safety pan; thermostatic mixing valve; dielectric unions; aquastat; timer (`P-302` key note 3, `P-501`).

**Gas**: pipe by size; fittings (malleable iron threaded, or welded or press); shutoff valve, drip leg, test ports, regulator, union and flex connector per appliance (see 4.3); hangers to 4.1; safety-yellow paint on exterior roof-level gas pipe (`P-403` note) with paint LF taken from the same pipe run; meter by gas company (EA 1, furnished by others).

## 7. Division boundaries (what NOT to include in Div 22)
Reference-job estimate shows these elsewhere: exterior sewer and storm piping, gas service line and exterior cleanouts (Div 33); cleanout concrete pads (Div 03 and Div 32); roof access hatch (Div 08); gas pipe paint (Div 09 "MEP PAINT", 45 LF of 3/4" and 10 LF of 1" against 53.9 LF on the plan markup, python); sanitary napkin disposal (Div 10). Rule: the building line and the civil sheet's "refer to civil" note set the cut; a takeoff that spans both double-counts.

## 8. Common mistakes and how to check
1. **Missing verticals and drops.** Check: every "UP", "DN", "TO RD", "TO CD" note on the plan has a length added.
2. **Summing the same pipe on two sheets** (floor plan and isometric) or **missing a size that spans sheets** (1-1/4" CW is on P-301 and P-302). Check: build one table by system x size x sheet and total it.
3. **One material for all of a system.** Reference job: below-slab sanitary PVC (spec 2.1A), above-ground hubless cast iron (2.1B), copper allowed 2-1/2" and smaller. Split by location from the schedule.
4. **Ignoring the piping schedule's hanger and joint rules** (extra hanger at each hubless joint; 10 ft spacing only with 10 ft pipe lengths).
5. **Counting fixtures from the plan only.** Check against the fixture schedule and the riser diagram ([zzTakeoff](https://www.zztakeoff.com/trades/plumbing-takeoff-software)). Reference job: CD 7 EA on P-302 is canopy drains, a different thing from RD 2 and OD 2 on P-303.
6. **Incomplete plumbing notes and architectural conflicts**; ask the client ([FieldPulse](https://www.fieldpulse.com/resources/blog/plumbing-takeoff)). Example: `P-302` insulation note vs spec 22 07 00 exemption (section 6).
7. **Ignoring small-bore fittings and assuming all valves of a size are identical** ([EPCLAND](https://epcland.com/quantity-take-off-piping/)).
8. **Using a blanket waste percentage** ([EPCLAND](https://epcland.com/quantity-take-off-piping/)).
9. **Cleanouts counted only where drawn.** Run the 4.2 rules on the layout: stack bases, turns over 45 degrees, 100 ft, 40 ft.
10. **Dropping accessories that live in schedule notes** (trap inserts, insulation kits, mixing valves, hose and hook, replacement filter cartridge).
11. **Double counting across divisions** (section 7).
12. **Unusual site conditions** such as steep slopes or deep foundations, which add materials ([FieldPulse](https://www.fieldpulse.com/resources/blog/plumbing-takeoff)). Check the invert elevations on P-301: depth below finish grade sets trench depth.

Cross-checks that can be run without any price: fixture-unit sanity (each fixture has waste, vent, cold, and hot where applicable); every floor drain has a trap primer or storm routing; every roof drain has an overflow drain; every gas appliance has the 4.3 kit; sum of pipe LF by system equals the sum of segment lengths on the isometric within a few percent.

## 9. Reference-job comparison (python, ground truth quantities only)

| Estimate line | Description | Plan markup total | Estimate qty (LF) |
|---|---|---|---|
| 404 | 3" storm | 150.5 | 150.59 |
| 405 | 4" storm | 172.7 | 172.7 |
| 406 | 1-1/2" sanitary | 3.6 | 3.55 |
| 407 | 3" sanitary | 86.7 | 86.73 |
| 408 | 4" sanitary | 21.9 | 21.94 |
| 409-411 | 2", 3", 4" vent | 58.2, 12.8, 47.3 | 58.18, 12.78, 47.29 |
| 412, 414, 415, 413 | 1-1/4", 1", 3/4" CW, 1/2" Type K | 64.5, 45.5, 44.5, 15.3 | 64.58, 45.52, 44.44, 15.34 |
| 416 | 1" HW | 162.2 | 162.22 |
| 418-420 | 1" gas (9.7 + 18.6), 3/4" gas | 28.3, 44.2 | 9.71 + 18.6, 44.21 |
| 417 | 1-1/2" condensate (size assumed on drawing) | 34.5 | 34.52 |

Counts: floor drains 3, canopy drains 7, roof drains 2, overflow drains 2, WC 2, LAV 2 (one fixture line with 2 EA), downspout nozzles 2, hose bibs 2, wall valve box 1, drain box 1, shutoff valves 2 plus manual shutoff 2, isolation and balancing valve 1, gas meter 1. Lines 421-444 are fixtures, drains, hydrants, valves and equipment, each carried with its full schedule text.

What the ground truth does not itemise: pipe material per line (except line 413), fittings, hangers, insulation, sleeves, trap primers, gas drip legs, regulators, test ports. A takeoff scored against it should therefore match on net LF and EA counts and treat the rest as optional detail.

The legend does not separate horizontal from vertical LF, so whether the markup includes rises is unconfirmed (open item).

## 10. What an AI takeoff must read from the drawings and specs
1. **Legend and abbreviations** (`P-001`): SAN, V, ST, CW, HW, NG, B/G, A/C, UP, DN, VTR, FCO, WCO, NFGH, EOD, TW.
2. **Piping schedule** (`P-101`): material, joint and fitting type by system, size band and location; hanger spacing columns; extra-hanger and 10-ft-length notes.
3. **Fixture and equipment schedules**: tag, model, mounting, accessories in the notes (P-trap model, stops, insulation kit, carrier, mixing valve, flow rate), furnished-by.
4. **Per-sheet key notes**: they carry count-driving instructions (double combo wye, intercepting trap, trap primers, hydrant drain, filter, expansion tank, circulation pump, shutoff valve heights).
5. **Elevations**: invert elevations and "UP/DN" annotations; fixture mounting heights for vertical rises.
6. **Isometrics and risers** to resolve verticals and to check totals.
7. **Pipe size labels** along each run; size changes mid-run; line-type legend (the same colour may mean different systems on different sheets).
8. **Spec 22 05 00 to 22 40 00**: where insulation is and is not required, valve types and port sizes, cleanout sizes, floor drain series, slope, vent termination offsets, trap primer rule, domestic-manufacturer requirement.
9. **Boundary notes**: "REFER TO CIVIL", "BY GAS COMPANY", "BY OTHERS" and the building line.
10. **Conflicts to surface, not resolve silently**: drawing note vs spec (insulation), plan vs schedule counts, schedule vs code (the project schedule is stricter on gas hanger spacing).

## 11. Gaps and unverified items
- No source found for: fittings per 100 LF by system; plumbing-specific waste percentages; PVC DWV stock lengths; sleeve/firestop count rules; hubless coupling support/bracing distances; roof-drain and leader sizing; trap primer code section. The web-search budget for this session was exhausted before these could be searched.
- Fetch failed (403/404/401): Simpro, STACK, ICC code library, UpCodes, Copper.org (current and archive), the Building Code Forum. Facts from those pages are labelled "search excerpt".
- The IPC 308.5 figures come from a Connecticut State Building Inspector document that reproduces the table (as proposed amendments), not from the ICC text.
- Section 12 is a GPT-6 Astra second opinion (`tools/ask_gpt.py`). It has no web citations. Its numbers are rules of thumb and its code section numbers are unverified pointers; no other section depends on it except the hubless-coupling sentence in 3.4.

## 12. Second opinion from a different provider (GPT-6 Astra, uncited)
Asked for components per pipe run and per fixture, measurement conventions, fitting heuristics and waste, with each statement labelled code, convention or rule of thumb. Raw answer: `trades/22-plumbing/scripts/research/plumbing/gpt1.txt`. None of the section numbers below were checked against the code text; treat them as pointers to look up.

**Agrees with the sourced sections above**
- Report the measurement convention. Centerline through fitting intersections with fittings counted separately is common but not universal. Do not mix net-cut and through-fitting quantities or deduct fittings twice.
- Count fittings, valves, fixtures and accessories individually, and set package boundaries so fixture hookups are not counted twice.
- Support intervals: IPC 308 / Table 308.5 and IFGC 415 / Table 415.1 (both confirmed above).
- Cleanouts are located and sized by IPC 708, not by a fittings-per-foot allowance.

**Adds, to be verified**
- Hubless DWV: one coupling per actual joint including pipe-to-fitting joints; transition couplings separate.
- Sediment traps and appliance shutoffs follow IFGC 408.4 and 409.5, and not every appliance needs a trap (consistent with the exemptions printed in 408.4: ranges, dryers, fireplaces, grills).
- Penetrations: count the listed firestop system per IBC 714, not generic caulk per hole.
- Trap-seal protection IPC 1002.4.1: count either the primer valve, distribution unit and tubing, or the permitted alternative, not both. Emergency (secondary) roof drainage IPC 1108. Backflow protection IPC 608. Water-hammer arrestors at quick-closing valves IPC 604.9. Hot-water pipe insulation IECC C404.4. Testing IPC 312 and IFGC 406. Drainage connection patterns IPC 706.
- Test devices (plugs, caps, gauges): size to simultaneous test sections, not total joint count.
- Plastic DWV cement and primer from the manufacturer's coverage per joint size, not a gallon-per-foot rule.

**Rules of thumb it offers (labelled provisional by the model, no source)**

| System | Directional/branch/reducer fittings per 100 LF (excludes couplings, valves, cleanouts) |
|---|---|
| Underground sanitary | 4 to 10 |
| Aboveground sanitary | 8 to 16 |
| Storm | 3 to 8 |
| Vent | 8 to 16 |
| Domestic copper | 12 to 25 |
| Natural gas | 4 to 10 |

Waste: cast iron 3 to 5%, plastic DWV 5 to 10%, copper and rigid steel gas 3 to 5%, insulation and jacketing 5 to 10%. The model states there are no universal waste percentages. These ranges overlap the EPCLAND 5 to 10% figure in section 5 but have no independent source. Against the app's flat fitting defaults (15 per 100 LF drainage, 20 water, 15 gas), the model's ranges put the drainage default inside the aboveground sanitary and vent range (8 to 16) but above underground sanitary (4 to 10) and storm (3 to 8), the water default inside 12 to 25, and the gas default above 4 to 10. Do not use either set to produce a final number without a contractor-confirmed rate.
