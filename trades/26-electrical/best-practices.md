# Electrical (Div 26): devices, fixtures, conduit, panels. Best practice for quantity takeoff

Scope: quantities and material types only. Researched 2026-10-13.
Estimate lines for this trade: 495-602 (108 lines), see [`reference/estimate/trades.json`](../../reference/estimate/trades.json).

**Source quality, read first.** There is no free, authoritative published standard for electrical takeoff waste or make-up allowances. Paywalled industry estimating manuals were not read. What exists online is (a) NEC code rules, which fix *how many supports, boxes and free-conductor inches* a run needs, quoted here through ECM/Mike Holt/Access Board pages and not from the NFPA text itself, and (b) estimator-software vendor guides that give practice-based percentages. Where a number comes from a vendor guide it is labelled "practice", not "standard". Check any code number against the NEC edition the AHJ has adopted.

---

## 1. What the estimator takes off, and in what unit

| Class | Unit | Rule | Source |
|---|---|---|---|
| Luminaires (incl. exit and emergency units) | EA by fixture type tag; linear LED/cove/tape types in LF | Count from the lighting plan against the luminaire schedule, one total per type written on the schedule. Exit lights are the item most likely to be missed. | [Red Rhino, Light Fixtures](https://hardhatis.com/lee-light-fixtures/) |
| Receptacles, switches, sensors, data outlets | EA by device type | Symbols are counted "each"; mark each counted symbol so it is counted once. | [ECM, Estimating Basics: The Takeoff](https://www.ecmweb.com/content/article/20890261/estimating-basics-the-takeoff) |
| Branch-circuit conduit and wire | LF, measured along the routed path; wire as conductor-LF by size and insulation | "Measure conduit and wire runs, factoring in the actual routing path, not just point-to-point distance." Circuit runs are measured with the drawing scale; drops for switches, receptacles and panels are added to run lengths. | [IT Supply Chain guide](https://itsupplychain.com/mastering-electrical-construction-takeoffs-a-step-by-step-guide-for-estimators/), [ECM](https://www.ecmweb.com/content/article/20890261/estimating-basics-the-takeoff) |
| Feeders and service | LF of conduit and of each conductor, listed from the one-line/riser diagram, labelled "from / to" | Feeder wire is generally #4 and larger; every feeder is highlighted and its length written on the takeoff sheet. | [Red Rhino, Building Feeders](https://hardhatis.com/lee-building-feeders/) |
| Panels, switchboards, transformers, disconnects | EA by scheduled assembly | Count panels and measure feeders and service runs last. | [ECM](https://www.ecmweb.com/content/article/20890261/estimating-basics-the-takeoff) |
| Boxes, covers, plates, whips, connectors, straps, hangers | EA, derived from the primary items above | List "supports, ells, condulets, adapters, and special fittings" per feeder; small-bore items are the ones most often left off. | [Red Rhino, Building Feeders](https://hardhatis.com/lee-building-feeders/), [McCormick checklist](https://www.mccormicksys.com/blog/am-i-missing-anything-an-estimating-checklist-for-electrical-plumbing-mechanical-contractors/) |
| Site duct and underground | LF per route, with the number of ducts in the description; trench and encasement quantities separate | See section 3.5. | [Heldenfels, burial depth](https://heldenfels.com/underground-duct-bank-burial-depth-cover-requirements/) |
| Penetrations, core drills, fire seals | EA, listed under the run that needs them | Count core drills, fire seals, water seals and concrete cutting/patching under each feeder. | [Red Rhino, Building Feeders](https://hardhatis.com/lee-building-feeders/) |

Takeoff order (any consistent order is acceptable): ECM describes lighting first (fixtures, switches, receptacles), then branch-circuit wiring, then individual circuits and home runs, then special systems (TV, phone, Cat 5, alarm, security, sound), then panels, feeders and service. Alternatives are page-by-page (impractical by hand) and service-first (many page changes). "Whatever system you develop, be sure to use the same procedures every time." [ECM](https://www.ecmweb.com/content/article/20890261/estimating-basics-the-takeoff). Measure branch circuits 2-wire first, then 3-wire, then 4-wire (same source). Most takeoffs are organised in eight sections: lighting, distribution, devices, branch circuits, equipment circuits, feeder circuits, site work, special systems (search-result summary of the [Simpro](https://www.simprogroup.com/blog/take-off-commercial-electrical-job) / [Housecall Pro](https://www.housecallpro.com/resources/estimate-electrical-work/) guides; the Simpro page returned 403, so treat as secondary).

## 2. Which sheets and specification sections drive it

General practice: count fixtures from the lighting plan and the fixture schedule; devices from the power/auxiliary plan; panels and feeders from panel schedules and the riser/one-line; check against keynotes and the specification ([Drawer.ai](https://drawer.ai/blog/how-to-do-a-construction-takeoff-for-electrical-estimators)). Electrical scope also hides on architectural, mechanical and plumbing drawings ([search summary of McCormick / Drawer.ai guides](https://www.mccormicksys.com/blog/am-i-missing-anything-an-estimating-checklist-for-electrical-plumbing-mechanical-contractors/)).

For this job (Fifth Third bank branch, 1,900 SF) the electrical set is indexed in [`reference/sheets/index.json`](../../reference/sheets/index.json):

| Need | Sheet(s) |
|---|---|
| Symbols, abbreviations | E-001 legend |
| Minimums that fix material (conduit size/type, wire, burial, whips) | E-002 general notes (notes 19, 22, 25, 26, 27, 29 matter most) |
| Site power, duct runs, site lights, meter, transformer, disconnect | E-010 (site plan), E-011 (photometric, pole lights), E-012 (details: hand hole, pole base, ground rod) |
| Receptacles, switches, data outlets, junction boxes, conduit stubs | E-100 (power and auxiliary), E-101 (roof: disconnects, weatherproof GFCI, pitch pocket, outlet box hood) |
| Luminaires and linear lighting | E-130 plan with E-600 luminaire/sensor schedule; E-601-E-603 exterior cutsheets |
| Security and fire alarm devices | E-150, E-160 (Div 28, see section 6) |
| Panels, gear, backboards, rack, ground bar | E-702 (IT/electrical room elevation), E-610 panel schedules, E-800 riser |
| Wall-mounted boxes at specific heights (shade switches, data, 3-gang recessed) | E-701-E-704 elevations |
| Conduit and wiring methods, boxes, devices, floor boxes, firestop | Spec 260100 (p.443), 261000 (p.452), 260923 lighting control (p.448), 263000 lighting (p.438); see [`spec_index.json`](../../reference/sheets/spec_index.json) and [`source/specifications.pdf`](../../source/specifications.pdf) |

What this project's own documents fix (read from the sheets and spec text, not from the web): E-002 note 26 sets conduit minimum 1/2" indoor and 3/4" outdoor/under slab, EMT only with compression fittings, home runs hard-piped, MC for fixture whips only; note 29 forbids MC/flex in open ceilings; note 27 sets 24" minimum burial to top of conduit; note 25 requires an insulated green equipment ground in every circuit (conduit is not the ground); note 22 says low-voltage wiring is not shown unless called out; note 19 sets #12 minimum and THHN/THWN above ground. Spec 261000 lists RGS, IMC, EMT, schedule 40 PVC, FMC/LFMC, expansion fittings at expansion joints, plaster rings in plaster/masonry walls and covers on every junction box, and floor boxes on minimum 7" centres.

## 3. Measurement rules

### 3.1 Conduit routing and drops
- Measure at right angles, including every 90-degree turn; never on a diagonal. The slack covers unknown obstructions. [Red Rhino, Tips and Methods](https://hardhatis.com/lee-tips-and-methods/), [Red Rhino, Building Feeders](https://hardhatis.com/lee-building-feeders/).
- Vertical legs are not on plan. Add the drop from ceiling/deck to each device and panel, and the rise from slab-level boxes. Estimators who measure only horizontal distance "consistently undercount conduit". [Drawer.ai, home runs](https://drawer.ai/blog/what-is-a-home-run-in-electrical-work-takeoff-guide). An example from one guide: outlets at about 18" and switches at about 48" above floor, so a drop under a 10 ft ceiling is about 8.5 ft ([Housecall Pro guide](https://www.housecallpro.com/resources/estimate-electrical-work/) (from a search snippet; the page itself was not opened), unverified; use the elevations in this job instead).
- Underground risers into the bottom of a panelboard are usually about 5 ft on a first-floor application; risers out of the top run from panel top to roof/deck less the hanger drop; compute risers at each end of every conduit. [Red Rhino, Building Feeders](https://hardhatis.com/lee-building-feeders/).
- Conduit symbols on the plan are diagrammatic. The job's own E-002 note 28 says routing is symbolic; take the path from architectural/structural conditions.
- An alternative to tracing every branch run is an average drop length times device count, for instance about 17 ft in one contractor's description, with home-run trunks measured explicitly ([Mike Holt forum](https://forums.mikeholt.com/threads/estimating-large-commercial-buildings-1m-bcw.143047/latest), practitioner anecdote).
- Trade-size limits that bound the material list: EMT trade size 1/2 to 4; PVC not below 1/2 or above 6. [ECM, EMT](https://www.ecmweb.com/national-electrical-code/qa/article/21270216/stumped-by-the-code-nec-requirements-for-using-and-installing-emt), [ECM, PVC](https://www.ecmweb.com/national-electrical-code/qa/article/21127210/stumped-by-the-code-nec-requirements-for-pvc-conduit).

### 3.2 Wire and cable
- Wire quantity = conduit length x conductors in the run, plus make-up. List by AWG size and insulation type separately ([Housecall Pro guide](https://www.housecallpro.com/resources/estimate-electrical-work/) (from a search snippet; the page itself was not opened)).
- Wire count per home run must come from the panel schedule and circuit notes. A shared (multi-wire) neutral serves two or three breakers in one home run; counting each circuit independently overcounts, and assuming one universal count causes conduit-fill errors. [Drawer.ai, home runs](https://drawer.ai/blog/what-is-a-home-run-in-electrical-work-takeoff-guide). On this job E-002 note 24 forbids shared neutrals unless the panel schedule says so, and note 25 adds a ground to every circuit.
- Box make-up: NEC 300.14 requires at least 6 in. of free conductor at each outlet, junction and switch point, and where the opening is under 8 in. the conductor must extend at least 3 in. outside it. [ECM, Apprentice's Guide to Article 300](https://www.ecmweb.com/national-electrical-code/article/21248556/the-apprentices-guide-to-article-300), [Mike Holt forum](https://forums.mikeholt.com/threads/300-14-and-free-conductor-length.32873/post-511796). Through-conductors that are not spliced or terminated are exempt (same sources). Practice: a 6-12 in. pigtail at each device and a 2-3 ft loop at each panel ([Housecall Pro guide](https://www.housecallpro.com/resources/estimate-electrical-work/) (from a search snippet; the page itself was not opened)).
- Feeder make-up (practice): usually 7 ft at a switchboard and 5 ft at a panelboard, or 12 ft for both ends of a run; add make-up where the pull goes through pull or junction boxes. Ground wire needs make-up too. [Red Rhino, Building Feeders](https://hardhatis.com/lee-building-feeders/), [Red Rhino, Tips and Methods](https://hardhatis.com/lee-tips-and-methods/).
- Voltage-drop upsizing changes wire size, not run length, but it changes the material description. E-002 note 18 on this job makes the electrical contractor responsible for it (3% branch, 2% feeder, 5% total).

### 3.3 Supports, fittings and counts that follow from length
These are code rules; the sheet or spec may be stricter.

| Raceway | Rule | Source |
|---|---|---|
| EMT (NEC 358.30) | Secure within 3 ft of each box, cabinet or termination fitting and at intervals no greater than 10 ft; 5 ft allowed at a termination where structure prevents 3 ft; the 3 ft rule applies to terminations, not couplings; runs through bored holes at 3 ft or less count as supported. | [ECM, EMT](https://www.ecmweb.com/national-electrical-code/qa/article/21270216/stumped-by-the-code-nec-requirements-for-using-and-installing-emt) |
| RMC/IMC | Within 3 ft of terminations and every 10 ft along runs (study-guide summary; the straight-run extension table was inconsistent on that page, so check the NEC). | [Open Exam Prep](https://open-exam-prep.com/study-guides/mn-electrician/ch12-raceways-cables/metal-and-nonmetallic-raceways) |
| PVC (NEC 352.30) | Secure within 3 ft of each box/termination; maximum support spacing 3 ft for 1/2-1 in., 5 ft for 1-1/4-2 in., 6 ft for 2-1/2-3 in., 7 ft for 3-1/2-5 in., 8 ft for 6 in. (the 3 ft row is confirmed in the [2023-based ECM piece](https://www.ecmweb.com/national-electrical-code/violations/article/55325459/illustrated-catastrophes-making-waves-at-the-beach); the full table is from [Open Exam Prep](https://open-exam-prep.com/study-guides/mn-electrician/ch12-raceways-cables/metal-and-nonmetallic-raceways) and a [2015 CDE reference](https://2027staging.ffa.org/wp-content/uploads/2026/06/19/cde_2015_agmech_electricalsys_electrical_skill_reference_materials-1.pdf)). | as listed |
| PVC expansion fittings (352.44) | Required in a straight run between secured points when expected length change is 1/4 in. or more; manufacturer instructions set count and setting. | [ECM, PVC securing](https://www.ecmweb.com/national-electrical-code/qa/article/20905099/stumped-by-the-code-nec-requirements-for-securing-and-supporting-pvc-conduit) |
| Bends | No more than 360 degrees of bends between pull points (four quarter bends). Each pull point is a box or conduit body to count. | [Open Exam Prep](https://open-exam-prep.com/study-guides/mn-electrician/ch12-raceways-cables/metal-and-nonmetallic-raceways) |
| Flexible metal conduit whip | A tap to a luminaire up to 6 ft (1.8 m) is exempt from securing and supporting (410.117(C), exception to 348.30(A)); luminaire tap conductors 18 in. to 6 ft. | [IAEI](https://iaeimagazine.org/columns/focus-on-the-code/question-can-you-daisy-chain-connections-to-fixtures/), [Mike Holt forum](https://forums.mikeholt.com/threads/what-determins-a-fixture-whip.15937/latest) |
| Stock length | EMT is furnished in nominal 10 ft lengths (ANSI C80.3 listing; retail EMT to 2 in. is listed as 10 ft). Whether the coupling is inside or outside the 10 ft is not stated by sources found. | [ANSI C80.3](https://webstore.ansi.org/standards/nema/ansic802020-2436476), [True Value 1 in. EMT](https://www.truevalue.com/product/emt-conduit-steel-thinwall-1-in-x-10-ft/) |

So per run: straps = ceil(length / support interval) + terminations x 1 (the 3 ft termination strap); connectors at each box entry (2 per run where both ends terminate in boxes); couplings = ceil(length / 10) - 1 for EMT; locknuts, bushings and fire-seals where the spec requires them. The job's spec 261000 additionally calls for insulated throat connectors or locknut plus bushing at every conduit end, and grounding wedge lugs or bonding bushings at panels and pull boxes.

### 3.4 Boxes, devices and covers
- Box count = device locations + junctions + pull points. A gang box takes one cover plate per gang assembly, not one per device. Quad receptacle = two duplex devices on one 4-11/16 or 2-gang box (GPT-6 cross-check, no web source; confirm against the device legend).
- Box fill (NEC 314.16) sets box size, hence description: each 12 AWG conductor takes 2.25 in3, a device yoke counts as two conductors of the largest connected wire, clamps and fittings count once; 2020 NEC counts the first four grounding conductors as one allowance. [Leviton 2020 NEC summary](https://captaincode2020.leviton.com/node/246), [ECM, Box fill part VI](https://www.ecmag.com/section/codes-standards/box-fill-calculations-part-vi) (via search summary; verify in the adopted edition).
- Mounting heights from the elevation sheets decide the vertical-drop length. Accessible reach is 15 in. minimum to 48 in. maximum above the floor for light switches and receptacles; floor receptacles, maintenance-only and dedicated-use receptacles are exempt. [Access Board, Chapter 3 Operable Parts](https://www.access-board.gov/ada/guides/chapter-3-operable-parts/).
- Receptacle quantity is normally counted from the plan, not computed. Where it must be checked, the 6 ft rule says no point along the wall floor line is more than 6 ft from an outlet, for wall space 2 ft or wider; the "12 ft spacing" is a consequence of that. [Mike Holt forum](https://forums.mikeholt.com/goto/post?id=1171926) (the sources found were dwelling-unit; commercial depends on occupancy and AHJ).
- Lighting control: ceiling occupancy sensors cover roughly 300 to 2,000 sq ft depending on model (WPIR 300, CI-305-1 500, W-2000H 900, CI-205 1,200, CX-105 2,000 in retailer listings), and low-voltage sensors need a power pack, listed as its own item. [LCOMP CI-205](https://www.lcomp.com/Lighting/Lighting-Controls/Motion-Sensors/LEGRAND-WATTSTOPPER/Ceiling-Mount-Occupancy-Sensor-White-Infrared/CI205/p/75418291330-1), [LCOMP WPIR](https://www.lcomp.com/Lighting/Lighting-Controls/Motion-Sensors/LEGRAND-WATTSTOPPER/Ceiling-Mount-Occupancy-Sensor-White-Infrared/WPIR/p/75418226103-1). Coverage is nominal; the sensor count is the plan symbol count, with coverage used only as a plausibility check. This job's spec (p.455) states sensor coverage up to 1,000 sq ft, 180 degrees.

### 3.5 Underground and site
- Minimum cover (NEC Table 300.5, circuits 1,000 V and below, measured to top of conduit/encasement): direct-buried cable 24 in.; RMC/IMC 6 in.; PVC listed for direct burial 18 in.; any raceway under 2 in. of concrete 12 in.; every method 24 in. under a road or parking lot. [Heldenfels](https://heldenfels.com/underground-duct-bank-burial-depth-cover-requirements/). Trench depth = cover + conduit package + bedding (same source). The job's note 27 sets 24 in., which governs.
- Duct bank concrete: cross-section area minus conduit area, times run length, over 27 for cubic yards; using the internal conduit area slightly overstates concrete. [Mike Holt forum, duct bank calculations](https://forums.mikeholt.com/threads/duct-bank-calculations.60081). Spacers fix the conduit spacing assumed in the ampacity calculation, and wider spacing means more concrete per foot ([Heldenfels, spacers](https://heldenfels.com/duct-bank-spacers-types-spacing-installation/)). No source found gave a standard spacer interval; take it from the spec or the spacer manufacturer.
- Hand holes, pole bases, ground rods and similar are EA items taken from the site details (job: E-012).

## 4. Coverage, yield and waste

| Item | Allowance | Basis |
|---|---|---|
| EMT, GRC, flex conduit | at least 10% added for trim-off and waste | Practice: [Red Rhino, Building Feeders](https://hardhatis.com/lee-building-feeders/) |
| Conduit 1 in. and under | about 10% over from cutting waste on an average job | Practice: [Red Rhino, Tips and Methods](https://hardhatis.com/lee-tips-and-methods/) |
| MC cable | 10-25% | Practice: [Red Rhino, Building Feeders](https://hardhatis.com/lee-building-feeders/) |
| MC cable and wire #6 and smaller | 15-20% or more over | Practice: [Red Rhino, Tips and Methods](https://hardhatis.com/lee-tips-and-methods/) |
| Wire left on a partial spool | counts as waste (example: 80 ft left x 4 wires = 320 ft) | [Red Rhino, Tips and Methods](https://hardhatis.com/lee-tips-and-methods/) |
| Whole takeoff | 10-15% for waste, errors and unforeseen items (generic guide) | [Electrical Takeoff Sheet PDF](https://apps.altnews.in/sites/u35FF5/244912/Electrical%20Takeoff%20Sheet.pdf), low authority |
| Devices, fixtures, panels | none; they are counted, not cut | convention (no source gives a device waste factor) |

Rules for using them: build percentages from your own records of the same job type; count make-up separately from waste so it is not hidden inside a percentage; round to stock lengths after applying waste, once. [Red Rhino, Tips and Methods](https://hardhatis.com/lee-tips-and-methods/). A GPT-6 Astra cross-check (unsourced, not a standard) proposed lower figures, 2-5% conduit and 3-5% wire cutting waste on a routed, make-up-included quantity; the spread between that and the 10% above is exactly why waste is a company setting, not a constant. The job's wire, conduit and fittings inside the building are not itemised in the estimate (see section 8), so no job-specific waste can be backed out.

## 5. Material breakdown an estimator lists

Primary item, then what follows. Sources for the accessory lists: [Red Rhino, Light Fixtures](https://hardhatis.com/lee-light-fixtures/), [Red Rhino, Building Feeders](https://hardhatis.com/lee-building-feeders/), [McCormick checklist](https://www.mccormicksys.com/blog/am-i-missing-anything-an-estimating-checklist-for-electrical-plumbing-mechanical-contractors/), [search summary of fixture-takeoff references](https://hardhatis.com/lee-light-fixtures/).

- **Luminaire**: the fixture by type tag and catalogue number; strut and structural supports, seismic wires, pendants/cables and hooks; emergency battery pack or emergency driver and dimming driver when a plan note requires one even if the schedule does not list it; dimmers or scene controllers for fixtures shown as controlled; outlet/junction box and flexible whip (up to 6 ft, see 3.3); hold-down clips and suspension material for grid-ceiling units; splice and fixture wire.
- **Device (receptacle, switch, data outlet)**: device by type and rating (tamper-resistant, GFCI, surge, USB, weather-resistant, motor-rated, dimmer); box by gang and depth; cover plate (engraved, blanked, weatherproof "in-use" for exterior); ring in plaster or masonry; connectors; pigtails; wire nuts; labels (E-002 note 36 requires panel/circuit labels on plates).
- **Conduit run**: conduit by type and size; couplings, connectors, straps/hangers and anchors, bushings, locknuts, elbows/condulets, expansion fittings, pull string, fire-seal at rated penetrations, sleeves; boxes or pull boxes at the 360-degree limit.
- **Wire**: each conductor size and insulation; EGC sized with the phase conductors; connectors/lugs; identification.
- **Panel or switchboard**: scheduled assembly; breakers by pole count and ampere; feeders in and out; lugs; directory; backboard and nameplate; ground bus bar; working-space clearance (NEC Article 110, E-002 note 37).
- **Disconnect**: switch by poles, ampere, enclosure type and fusing; fuses; whip to equipment; mounting.
- **Site duct**: conduit LF by size, trench LF, spacers, sweeps/elbows, caps, pull rope, warning tape, hand holes, concrete if encased, restoration if in scope (E-002 note 27 asks for detectable warning tape where the AHJ requires it).

Allowances: unidentified fixtures are listed as "unknown" with a description and an RFI, never omitted ("DO NOT LEAVE IT OUT!"). [Red Rhino, Light Fixtures](https://hardhatis.com/lee-light-fixtures/).

## 6. Scope boundaries to resolve before counting
- Fire alarm: E-160 on this job states that all fire-alarm devices are by a licensed fire-alarm contractor; the electrician normally keeps power, boxes and pathways. Security (E-150) and data/telecom are likewise often low-voltage vendor work with electrical pathways. Estimator discipline: record in writing who furnishes and who installs every FA, security, data, utility and owner-equipment item. (E-160 text read from [the sheet](../../source/drawings/Electrical/E-160-ELECTRICAL-FIRE-ALARM-PLAN-Rev.0.pdf); the general rule is a GPT-6 cross-check.)
- Items outside the electrical set often missed: temporary power, demolition and patching, permits, specialty systems, testing and commissioning. [McCormick checklist](https://www.mccormicksys.com/blog/am-i-missing-anything-an-estimating-checklist-for-electrical-plumbing-mechanical-contractors/), [Drawer.ai](https://drawer.ai/blog/how-to-do-a-construction-takeoff-for-electrical-estimators).
- Utility-supplied items (meter, transformer, primary conduit): the job's E-002 note 10 makes the contractor provide conduit to the point of interception where required and says the utility information is preliminary. Equipment ownership split must be read per project.

## 7. Common mistakes and how to check a takeoff

| Mistake | Check | Source |
|---|---|---|
| Counting only horizontal distance | Add drops/rises for every device, panel and riser | [Drawer.ai, home runs](https://drawer.ai/blog/what-is-a-home-run-in-electrical-work-takeoff-guide) |
| Scale error | Verify the scale on every sheet used for length; reduced copies can put a measurement "off by as much as 100%"; keep a per-sheet calibration log | [ECM](https://www.ecmweb.com/content/article/20890261/estimating-basics-the-takeoff), [Drawer.ai, 12 causes](https://drawer.ai/blog/12-causes-of-pdf-electrical-takeoff-errors) |
| Double-counting at sheet seams | List every match line; count boundary devices on one sheet only | [Drawer.ai, 12 causes](https://drawer.ai/blog/12-causes-of-pdf-electrical-takeoff-errors) |
| Similar symbols confused (voltage, emergency, mounting, controls) | One pass per type, reconciled to the fixture or panel schedule | same |
| Hidden scope on referenced sheets | Index the set, open every referenced schedule, riser, keynote list and detail | same |
| Hand markups, clouds, RFI stamps ignored | Dedicated pass; treat unexplained markup as possible scope | same |
| Revisions not tracked | Revision log; recount only changed areas | same |
| Other trades' layers hiding devices | Count from electrical-only sheets; run a clash check afterward | same |
| Circuits assigned to the wrong panel | Reconcile every circuit callout to the panel schedule and one-line; flag implausible panel totals | [Drawer.ai, 12 causes](https://drawer.ai/blog/12-causes-of-pdf-electrical-takeoff-errors), [Drawer.ai, home runs](https://drawer.ai/blog/what-is-a-home-run-in-electrical-work-takeoff-guide) |
| Home runs that cross sheets missed | Do not close a sheet until every circuit callout is traced to its panel | [Drawer.ai, home runs](https://drawer.ai/blog/what-is-a-home-run-in-electrical-work-takeoff-guide) |
| Unreadable tag guessed | Mark unresolved instead of guessing | [Drawer.ai, 12 causes](https://drawer.ai/blog/12-causes-of-pdf-electrical-takeoff-errors) |
| Click-counting fatigue | Zone the sheet; cap uninterrupted counting at 45-60 min; second pass on dense sheets; second estimator reviews one sheet in five | same |
| Reading plans but not specs, general notes, addenda | Specs define wiring method, box type, labeling, testing | [McCormick](https://www.mccormicksys.com/blog/am-i-missing-anything-an-estimating-checklist-for-electrical-plumbing-mechanical-contractors/) |
| Small-bore items missing | Hangers, straps, bushings, locknuts, wire nuts, penetration seals | [McCormick](https://www.mccormicksys.com/blog/am-i-missing-anything-an-estimating-checklist-for-electrical-plumbing-mechanical-contractors/) |
| Exit lights missed | Second visual pass specifically for exits | [Red Rhino, Light Fixtures](https://hardhatis.com/lee-light-fixtures/) |
| Sizing from square-foot averages | Takeoff from the drawings; averages only as a plausibility check | [search summary of Trimble / Drawer.ai mistakes lists](https://drawer.ai/blog/top-7-estimating-mistakes-to-avoid-for-electrical-estimators) |

Final-check method: with a proper takeoff, "you should have no need to refer to the plans or specifications" when building the bill of materials ([ECM](https://www.ecmweb.com/content/article/20890261/estimating-basics-the-takeoff)); verify counts against panel, device and fixture schedules, keynotes and specs; document assumptions; have someone peer-check ([IT Supply Chain](https://itsupplychain.com/mastering-electrical-construction-takeoffs-a-step-by-step-guide-for-estimators/), [Drawer.ai](https://drawer.ai/blog/how-to-do-a-construction-takeoff-for-electrical-estimators)).

Additional cross-checks that follow from the rules above (derived, not sourced as a list): luminaire count by type equals the schedule's "quantity" if the schedule has one; sum of branch breakers on the panel schedule matches circuits traced; the number of conduit ends equals the number of box/panel entries; every fixture whip has a box; every exterior device has a weather-rated cover; every linear fixture type (cove, tape, pendant strip) is in LF and not EA.

## 8. What an AI takeoff must read, and what this job shows

**Read from the drawings**
1. The symbol legend (E-001) before any count; project symbols differ. [Drawer.ai, 12 causes](https://drawer.ai/blog/12-causes-of-pdf-electrical-takeoff-errors).
2. The luminaire schedule (E-600): type tag, mounting, source and driver, emergency variant (catalogue number suffix such as "-EL"), and whether the unit is EA or LF.
3. The panel schedules (E-610) and riser (E-800): panel tag, main, bus, voltage/phase, circuit-to-load mapping, spare and space.
4. Device tags and keynotes on E-100/E-130/E-700 and the elevations E-701-E-704, which carry the mounting height and gang counts.
5. Scale on every sheet; do not mix.
6. Match lines and cross-sheet references (the job's estimate lines cite ranges such as "E100 - E704").

**Read from the specifications and general notes**: wiring methods allowed and forbidden, minimum conduit and wire sizes, burial depth, box and plate types, firestop, labeling, and scope notes. Convert them into accessory lines.

**What this job's reference estimate shows** (project files, [`lines.json`](../../reference/estimate/lines.json), [`legends.json`](../../reference/markups/legends.json)):
- The estimator itemised **devices and equipment individually**: 19 receptacle lines (71 EA), 18 switch/control lines (41 EA), 3 data-outlet lines (17 EA), 5 junction-box lines (20 EA), 23 luminaire lines (140 EA plus 66.27 LF of linear lighting), panels, disconnects and IT-room items. Variants are separate lines when the description differs (tamper-resistant, GFCI, black plate, engraved plate, USB).
- **Linear lighting** is in LF from the measured run: L 30.4 LF on the markup against 30.36 LF in the estimate, G 26.8 against 26.78, UC 9.1 against 9.13 ([E-130 markup legend, page 46](../../reference/markups/legends.json)).
- **Counts combine pages.** Quad receptacles in the estimate (17) are the E-100 plan count (3) plus the E-702 elevation count (14); GFCI duplex (7) is 6 on E-100 plus 1 on E-702; combination data outlets (15) is 14 on E-100 plus 1 on E-703; junction boxes (10) is 9 on E-100 plus 1 on E-130. An AI must merge plan and elevation counts and must decide, per device, whether the elevation symbol is the same device as a plan symbol or a separate one; this is the main double-count risk on this set and is not resolvable from the legends alone.
- **Site conduit is taken as route length, with the duct count in the name.** "(2) 4in conduit" is 71.5 + 30.2 = 101.7 LF in the estimate (101.71), not doubled; "(2) 2in" is 15.4 + 61.8 + 30.2 = 107.4 (107.37). So the estimate quantity is trench/route LF, and duct-LF would be twice that; the unit column does not say which. Resolve the convention before comparing an AI result. The 1 in. line is 20.0 LF in the estimate against 4.8 + 15.4 = 20.2 LF on the two same-name E-010 markup rows (page 41), rounded to whole feet; see [reconciliation line 506](reconciliation.csv).
- **Branch conduit, wire, fittings and supports inside the building are not itemised**: the estimate carries one lump-sum allowance line "WIRING, CONDUITS & FITTINGS ETC, AREA: 2000 SF" (line 510). The only interior conduit lines are two short IMC stub groups ((4) 3/4 in. IMC 19.61 LF and (4) 2 in. IMC with string 19.54 LF). So the estimate does not provide ground truth for branch conduit or wire length, and any AI-generated figure for it cannot be validated against this job; use the rules in sections 3-4 and flag it as derived.
- Fire alarm, security and parts of Div 28 are listed on their own sheets (E-150, E-160) and belong to [trade 28](../28-low-voltage-fire-alarm/); the E-702 security panels (7 EA) sit in this trade's lines.
- Backboard: fire-rated 3/4 in. plywood on E-702 is measured in SQ FT (215.3 on the markup), which is an area item inside an electrical trade.

## 9. Gaps and open questions
- No free authoritative source for conduit/wire waste or make-up exists; the 10-25% figures are one vendor's practice. Treat as defaults to be overridden.
- Standard spacer interval, fittings-per-100-ft, and boxes-per-device ratios were not found in citable form.
- NEC rule text was not read from NFPA 70; every code number above is second-hand and edition-dependent.
- Paywalled industry estimating manuals (NECA, SMACNA) could not be accessed.
