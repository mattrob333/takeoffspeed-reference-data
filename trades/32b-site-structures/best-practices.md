# Best practice: site concrete and structures (footings, pads, dumpster enclosure, monument sign, canopy, ATM) - quantities and material types only

Scope: small cast-in-place and masonry site elements around a building: pier and strip footings, concrete pads, bollards, a CMU trash enclosure with gate, a monument sign, a drive-up canopy and an ATM island. Prices, labor and productivity are out of scope.

How to read this file. Every factual claim carries a link. Tags: **(primary)** = standard, manufacturer, trade-association or master-spec text that I read in full; **(secondary)** = estimating blog or vendor page, read; **(search summary)** = seen only in a search-result summary, not read in full; **(model)** = a second opinion from GPT-6 Astra, unsourced and not independently verified; **(project)** = a file in this repository (`source/specifications.pdf`, `source/drawings/...`, `reference/estimate/lines.json`). Arithmetic marked **derived** was done in Python.

Honest summary of the evidence. There is no published "site structures takeoff standard". What is citable: the geometry (cylinder, prism, stadium shape), manufacturer yield data (Sonotube volumes, NCMA unit/mortar/grout tables, pipe dimensions, rebar unit weights), the ready-mix ordering guidance (4-10% over volumetric), joint rules (NRMCA CIP 6), cover (ACI 318 via ACI FAQ) and the project's own specification text. Everything else (rebar waste %, CMU waste, swell factor, chair counts) is estimator convention and the sources disagree. So: measure net installed quantities, state the convention, and keep waste, overbreak and swell as separate, visible steps.

---

## 1. What an estimator takes off, and in which units

| Item | Unit | Notes / basis |
|---|---|---|
| Round pier footings (bollards, light poles, signs, bike racks, gate posts) | EA, with CY each and CY total | Volume = pi x (D/2)^2 x depth / 27 ([toolgrit guide](https://www.toolgrit.com/guides/concrete-volume-explained) (search summary); Sonoco chart below). Count by type: diameter and depth are the key. |
| Strip/continuous footings (enclosure wall) | LF, then CY | CY = LF x width x depth / 27 ([handoff.ai](https://handoff.ai/blog/concrete-takeoff) (secondary); [ConstructConnect](https://www.constructconnect.com/blog/6-concrete-takeoff-tips-for-estimators-contractors) (secondary): "divide that number by 27"). Linear takeoff suits continuous footings, count takeoff suits isolated ones (handoff.ai; stackct summary (search summary)). |
| Pads and slabs (trash pad, apron, transformer pad, clean-out pads, ATM island) | SF (area, with thickness), then CY | Area x thickness / 27. Thickened edges/footings are added as separate volumes without overlapping the base slab (model). |
| Reinforcing steel (bars) | LF by size, then LB (or tons) | Convert with nominal unit weights (section 5). Laps, hooks, dowels and bends are included in scheduled length, not hidden in a waste percentage (model; project spec 03 20 00 requires laps per ACI/30 d). |
| Welded wire reinforcement | SF of sheet area (laps added) | Lap rule in section 3.4. |
| Bar supports, tie wire | EA / LB | Counted from the layout; see section 5. |
| Formwork | SFCA (contact area) or LF of edge form | Only for formed faces; earth-cast faces are not formed ([handoff.ai](https://handoff.ai/blog/concrete-takeoff) lists forms separately from concrete; model: "Do not automatically form edges cast against earth"). Fiber tube forms are counted EA/LF instead. |
| Tube forms (Sonotube-type) | EA by diameter and cut length | Standard 4', 8', 12' lengths in 6"-12" ([Sonoco](https://es-la.sonoco.com/sites/default/files/technical-files/Sonotube%C2%AE%20Builders%20Tube%C2%AE%20concrete%20forms.pdf) (primary)). |
| CMU wall (enclosure) | SF of net wall, then units EA by type | 8 x 16 in. unit face = 8/9 SF; 119 units per 100 SF incl. 5% breakage ([NCMA/CMHA TEK 04-02A](https://www.cmha.org/resource/tek-04-02a/) (primary)). Bond-beam, corner, jamb/KO units are counted by type inside that total. |
| Grout in cores and bond beams | CF or CY | [TEK 04-02A Table 3](https://www.cmha.org/wp-content/uploads/2018/08/TEK-04-02A-Table-3.png) (primary), section 5. |
| Mortar | CF / bags | [TEK 03-11](https://www.cmha.org/resource/tek-03-11/) (primary), section 5. |
| Precast/stone wall cap | LF installed, EA pieces (straight, corner, end) | (model); project: A-190 detail 5 / line 672. |
| Concrete-filled steel pipe bollards | EA, pipe LF (exposed + embed), fill CY | Pipe by actual ID/OD ([Continental Steel](https://continentalsteel.com/item/pipe-and-tubing/seamless-and-welded-pipe/wsp-600-280) (primary)). |
| Excavation, backfill, haul-off at footings | CY (bank), loose CY for hauling | Section 3.6. |
| Gates, posts, hardware, signage panels | EA | Counted, with the footing as a separate line. |
| Monument sign, canopy, ATM | EA (item) plus interface items | Usually furnished by others; the site contractor's scope is the foundation, anchor bolts/templates, conduit stub-ups, hand hole and bollards. See section 6. |
| Conduit stub-ups and hand hole at ATM/sign/canopy | EA / LF / size | Section 6. |

Reporting rule that avoids most disputes: output **net geometric quantity, waste/overbreak %, and order quantity** as three separate numbers per line ([NRMCA CIP 31](https://www.prairie.com/wp-content/uploads/sites/4/2024/12/31p_OrderingReadyMixedConcrete.pdf) (primary) ties the 4-10% over-order to waste, over-excavation, form spreading and settlement; handoff.ai (secondary) adds waste "as a separate line"; model: "Keep net installed quantities separate from order quantities").

---

## 2. Which sheets and spec sections drive it

Generic: civil site plan (locations, dumpster, monument sign, bollards, bike racks, transformer pad, light poles), civil/site construction details (bollard, pad, sign foundation, curb, ADA), architectural enclosure sheet (plan, wall section, elevations, cap detail, gate), bank-equipment sheet (ATM island, canopy, bollards, conduit stub-ups), structural general notes and typical details (cover, laps, joints, dowels), electrical site plan/details (pole bases, transformer slab, monument sign power), geotechnical report (bearing, groundwater, rock), and specifications. Review plans and specs for inconsistencies and check each sheet's scale before measuring ([ConstructConnect](https://www.constructconnect.com/blog/6-concrete-takeoff-tips-for-estimators-contractors) (secondary)). Sign foundation scope typically lists footings with pedestals or drilled piers, conduit and anchor-rod assemblies ([NCDOT sign foundations](https://connect.ncdot.gov/resources/safety/Signing%20and%20Delineation%20Library/Overhead%20and%20Dynamic%20Message%20Sign%20Foundations%20SP09%20R007.aspx) (search summary)).

CSI sections: 03 20 00 Concrete Reinforcement, 03 30 00 Cast-in-Place Concrete, 04 22 00 Concrete Unit Masonry, 05 50 00 Metal Fabrications (bollards, gates), 10 14 00 Signage, 32 13 13 Concrete Paving, 32 31 00 Fences and Gates, 31 23 00 Excavation and Fill, 26 05 43 underground ducts/handholes.

**This job (project).**
- Sheets (see `reference/sheets/index.json`): A-190 Trash Enclosure and Details (plan, wall section, elevations, wall cap, key notes TE1-TE5); A-401 Bank Equipment Plans and Details (drive-thru island, typical bollard, ATM conduit stub-up notes, canopy); A-402 cut sheets; C-3.0 Site Plan (dumpster wall, bollards, gate, transformer pad, monument sign, bike racks, signs); C-6.0-C-6.3 construction details; C-1.0 (existing monument sign demolition); C-2.0 (concrete washout); E-010 (transformer slab, monument sign power), E-012 (pole base detail 3/E-012); S-201 foundation plan, S-680 typical foundation details (cover, isolation joints, saw-cut joints), S-685, S-001/S-002 notes.
- Spec sections indexed in `reference/sheets/spec_index.json`: 032000 Concrete Reinforcement (spec p.45), 033000 Cast-in-Place Concrete (p.49), 055000 Metal Fabrications (p.113; bollards p.118 and p.120), 072616 Below-Grade Vapor Retarders (p.162), 099100/099653 (CMU coating). **There is no unit-masonry (04 22 00) or site-paving/fence (32 xx) section in the indexed spec**, so CMU, enclosure gate, sign and bollard requirements come from drawing notes and 03/05 sections, and must be read from A-190/C-sheets.
- Project spec rules that change quantities (project): reinforcing cover 3" for footings (spec p.47 and p.59); bars lapped 30 diameters unless noted (p.46-47); main steel not spliced unless shown (p.59); welded wire fabric lapped minimum 6" and wired at side and end laps (p.59); dowels the same size as the vertical wall reinforcement set in footings at each vertical bar (p.59); accessories over earth are precast concrete block bar supports (p.55); slab bar supports at 4'-0" o.c. for bottom steel and high chairs at 3'-6" o.c. each way for two-way flat-slab top steel (p.48); block-wall horizontal reinforcement as welded wire ladder type (p.55); bollards from Schedule 40 pipe, capped with 1/4" plate, filled solid, set in formed or core-drilled holes at least 8" deep and 3/4" larger than the OD with the annulus grouted (p.118, p.120).

---

## 3. Standard measurement rules

### 3.1 Round piers and tube-formed footings
- Net volume = pi x (D/2)^2 x H / 27 CY. Manufacturer chart for fiber tubes: 0.20, 0.35, 0.55, 0.80 cubic feet per foot of height at 6, 8, 10, 12 in. nominal diameter; diameters are nominal, "if critical, you need to measure" ([Sonoco](https://es-la.sonoco.com/sites/default/files/technical-files/Sonotube%C2%AE%20Builders%20Tube%C2%AE%20concrete%20forms.pdf), primary). Derived check: the cylinder formula gives 0.196, 0.349, 0.545, 0.785 CF/ft, so the chart equals the formula; for 16" it is 1.396 CF/ft = 0.0517 CY/ft, for 18" 1.767 CF/ft, for 24" 3.142 CF/ft = 0.116 CY/ft (derived).
- Measure depth from the stated datum: depth below finished grade vs. footing height including above-grade stub. Take the bottom elevation, not just the stated "H", where the detail shows both an exposed and a buried portion (A-401 typical bollard: 48" below grade plus 3" under the pipe, 16" dia. fill; project).
- Do not use the pier shaft volume for footings that have an enlarged base, bell or pad; compute each solid separately.
- If the pipe or post is embedded, the net concrete outside the pipe is footing volume minus pipe OD volume over the embedded length, and the pipe is filled separately (model); most estimators ignore the displacement and say so in a note. Do not count the embedded fill twice (model).

### 3.2 Strip footings and stem walls (enclosure)
- Measure length on the footing centerline, with one convention for corners, and no separate "corner" LF at ordinary centerline corners (model). Deduct gate openings only if the detail interrupts the footing, and add gate-post foundations separately (model).
- Net CY per LF for a 2'-0" x 1'-0" footing = 2 x 1 / 27 = 0.0741 CY/LF (derived).
- Top bars: count longitudinal bars x length, add corner bends, laps and dowels at each vertical bar (project spec p.59).
- Footing top elevation vs. finished grade drives stem height: the masonry measured to the footing top includes the buried portion (see 3.3).

### 3.3 CMU wall
- Net wall area = length x height - openings. For standard 8 x 16 units: 8/9 SF per unit, 119 units/100 SF with a 5% allowance; the count is independent of unit width; deduct openings first; count pilasters, corners and bond-beam units separately; non-modular layouts and many corners raise unit and mortar quantities ([TEK 04-02A](https://www.cmha.org/resource/tek-04-02a/), primary). A shorter rule of thumb is 113 units/100 SF (no waste) with 3/8" joints ([TEK 03-11](https://www.cmha.org/resource/tek-03-11/), primary). 113 x 1.05 = 118.65 (derived), which reconciles the two figures.
- Height: from top of footing (or top of dowel course) to underside of cap. Do not measure from finished grade only. Derived from this job: A-190 shows 6'-8" above grade plus 1'-4" to footing top, i.e. 8.0 ft; the reference estimate has 289.76 SF over 36.2 LF, which is exactly 8.00 ft (derived; project: line 668, legend `DUMPSTER ENCLOSURE WALL` 36.2 FT).
- Bond beam: LF per course; the units replace plain units in the total (model). Precast cap: LF measured on the wall centerline; confirm piece lengths and corner pieces.
- Reinforcement: vertical bars at the spaced cells (count per run from the detail, with a bar at ends/jambs/corners), plus dowels from the footing, bond-beam bars, and any ladder wire. Count length with the lap required by spec (30 d here; project). Vertical bar count per run is about ceil(L / spacing) + 1 as a preliminary check only (model).
- Grout and mortar: section 5.

### 3.4 Slabs, pads, aprons
- Concrete CY = area x thickness / 27. Convert inches directly: CY = SF x in / 324 (derived).
- Dumpster pad/apron minimum references: Duke standard 6" thick, 3,000 psi, #4 at 12" each way, over 4" ABC, with a 5 ft deep apron ([Duke 11 82 13](https://facilities.duke.edu/sites/default/files/11%2082%2013_SolidWasteBins_FINAL.pdf), primary master spec); City of Albuquerque 6" slab, 4,000 psi, 6x6-10/10 WWM, slope 1/8" per ft, 6" apron with expansion joint ([Albuquerque](https://www.cabq.gov/solidwaste/documents/enclosurespecificationswordsfont14.pdf), primary). Use as a **checklist of what the detail may contain**, never as a default; the project drawings govern.
- Welded wire: the lap is measured between outermost cross wires; for plain WWR the ACI 439.5R-18 lap is one square plus 2 in. (8" for 6x6), while some owners fix 8" ([ASCC](https://ascconline.org/Home/News/articleType/ArticleView/articleId/51/WWR-Lap-Splice-Requirements) (primary-level trade association); [Indiana DOT / Everett WA specs](https://www.in.gov/dot/div/contracts/standards/rsp/sep11/700/737-B-188%20120401.pdf) (search summary)). This project's spec says 6" minimum (spec p.59), so a conflict exists and must be flagged, not resolved silently.
- Bars in a mat: count per direction ceil(width / spacing) + 1 (model), cut with end cover, then add laps by stock length. The check value for #4 at 12" each way is about 2 LF/SF or 1.34 lb/SF (derived: 2 x 0.668), higher for small pads because of perimeter bars (model).
- Joints: maximum spacing 24 to 36 times slab thickness and never over 15 ft; panels square, length not over 1.5 x width; contraction joint depth at least 1/4 of the slab thickness (not less than 1 in.) ([NRMCA CIP 6](https://www.prairie.com/wp-content/uploads/sites/4/2024/12/06p_JointsinConcreteSlabsonGrade.pdf), primary). Isolation joints at walls/footings and where slabs meet curbs or other obstructions (same source). Joint filler and sealant are measured LF.
- Vapor retarder: lap 6 in. unless the manufacturer says otherwise ([ASTM E1643 as cited](https://softbank.iust.ac.ir/Railway/Codes/ASTM-standard/ASTM_2004_Standards/ASTM%202004%20PART%20IB/ASTM%202004%20Volume%2004.11%20Building%20Constructions%20(I)%20E%2072%20-%20E%201670/E%201643%20-%2098%20%20_RTE2NDM_.pdf) (search summary)). Measure area plus laps and perimeter turn-up if detailed.

### 3.5 Cover, bends and what the dimension on the drawing means
- Specified cover is 3 in. for concrete cast against and permanently in contact with ground (footings, grade beams, caissons) ([ACI FAQ 903](https://www.concrete.org/frequentlyaskedquestions.aspx?faqid=903), primary). Use it to compute bar lengths: footing length minus 2 x cover, plus hooks. This job: 3" footing cover (project spec p.47/p.59; A-190 shows "3\" CLEAR").
- Hook dimensions and bend allowances come from the engineer's details or ACI/CRSI standard hooks; A-190 calls out "90 deg std ACI hook" (project).

### 3.6 Excavation, backfill and haul-off
- Footing excavation is a **bank** volume larger than the concrete: trench width = footing width + working space, depth to bottom of footing (from finished grade, not top of footing). Concrete over-excavation (overbreak) is a reason NRMCA lists for ordering 4-10% more ([CIP 31](https://www.prairie.com/wp-content/uploads/sites/4/2024/12/31p_OrderingReadyMixedConcrete.pdf)); do not count the same overdig both in the geometric excavation and again in a concrete waste percentage (model).
- Haul-off is loose volume: bank CY x (1 + swell). A 25% swell (factor 1.25) is the usual illustrative default; typical ranges quoted are 15-30% (clay 20-40%, sand 5-15%, gravel 10-25%) ([Trimble ProContractor](https://help.trimble.com/en/procontractor/procontractor/earthwork/earthwork/summary-tab/enter-swell-and-yield-factors) (primary-level vendor docs, 1.25 example only), [Vertigraph glossary](https://www.vertigraph.com/learn/glossary/swell-factor) (search summary)). Take the actual factor from the geotechnical report.
- Haul-off = excavated - backfill that is reused (consistent bank basis), and backfill is excavation minus the concrete and wall volume below grade (derived on this job: excavation 12.50 CY - backfill 8.66 CY = 3.84 CY haul-off, equal to the line 667 haul-off; project).
- Maximum earth differential when backfilling is a structural note here (S-201: 2'-0"; project).

---

## 4. Standard coverage/yield and waste factors, with their basis

| Material | Factor | Basis |
|---|---|---|
| Ready-mix concrete | Order 4% to 10% over the volumetric quantity; hardened volume is 1-2% less than fresh; avoid small clean-up loads under 4 CY; truck capacity 8-12 CY; ~4,000 lb per CY | [NRMCA CIP 31](https://www.prairie.com/wp-content/uploads/sites/4/2024/12/31p_OrderingReadyMixedConcrete.pdf) (primary) |
| Concrete, other rules of thumb | about 10% on slabs/footings ([handoff.ai](https://handoff.ai/blog/concrete-takeoff), secondary); piers 5-10%, up to 15% for hand-dug holes that bell out ([toolgrit](https://www.toolgrit.com/guides/concrete-volume-explained), search summary); 3-5% formed work and 5-10% earth-cast (model). | Blog level; the NRMCA 4-10% is the citable range. |
| Concrete returned by ordering errors | NRMCA estimates returned concrete 1-5%, sometimes 10%, mostly from over-ordering | [NRMCA TIP 19 (search summary)](https://www.nrmca.org/wp-content/uploads/2020/04/TIP19w.pdf) |
| CMU units | 119 per 100 SF incl. 5% for waste and breakage; 113 per 100 SF net | [TEK 04-02A](https://www.cmha.org/resource/tek-04-02a/), [TEK 03-11](https://www.cmha.org/resource/tek-03-11/) (primary) |
| Mortar | 8.5 CF per 100 SF of wall incl. 10% waste, 3/8" joints, face-shell bedding. One 70 lb masonry-cement bag lays about 30 hollow units; 1 ton of sand per 8 bags (about 240 units per ton) | [TEK 03-11](https://www.cmha.org/resource/tek-03-11/), [TEK 04-02A](https://www.cmha.org/resource/tek-04-02a/) (primary) |
| Grout | CF per 100 SF of wall by wall width and grouted-cell spacing, two-core units, **3% waste included** (table below) | [TEK 04-02A Table 3](https://www.cmha.org/wp-content/uploads/2018/08/TEK-04-02A-Table-3.png) (primary) |
| Rebar | 3-5% cutting/lap waste (sometimes 5-10% small orders) | [handoff/ArcSite search summary](https://www.arcsite.com/blog/best-practices-for-accurate-material-estimation-for-concrete) (search summary), (model); no primary source found. |
| Welded wire sheets | add lap area; no cited waste % | section 3.4 |
| Earth (haul-off) | swell 1.25 illustrative | section 3.6 |

TEK 04-02A Table 3 (CF of grout per 100 SF of wall, vertical cells, includes 3% waste) for the widths and spacings relevant here: 8 in. wall: 9.1 at 32 in. o.c., 12.1 at 24, 18.1 at 16, 36.1 at 8 in. (full grout); 6 in. wall: 6.4 at 32, 8.6 at 24, 12.8 at 16, 25.6 at 8; 12 in. wall: 14.8 at 32, 19.7 at 24, 29.5 at 16, 58.9 at 8 ([Table 3 image, read](https://www.cmha.org/wp-content/uploads/2018/08/TEK-04-02A-Table-3.png)). Bond beams, horizontal grouting and pilasters need extra grout beyond the table (TEK 04-02A text). Smaller projects see more grout waste (TEK 04-02A).

Pipe: 6 in. nominal Schedule 40 is 6.625 in. OD, 6.065 in. ID, 0.280 in. wall, 18.97 lb/ft plain end ([Continental Steel](https://continentalsteel.com/item/pipe-and-tubing/seamless-and-welded-pipe/wsp-600-280), primary). Concrete fill per foot of pipe = pi/4 x 6.065^2 / 144 = 0.2006 CF/ft = 0.00743 CY/ft (derived), so 8 ft of pipe holds 1.60 CF = 0.059 CY (derived example). Do not use the nominal 6 in. for fill volume.

Rebar unit weights, ASTM A615 nominal (lb/ft): #3 0.376, #4 0.668, #5 1.043, #6 1.502, #7 2.044, #8 2.670, #9 3.400, #10 4.303, #11 5.313 ([CMC reference table](https://www.cmc.com/getmedia/83bc1448-b2ed-47b1-9b4e-56951d4b7212/1_Mechanical_Properties-NEW.pdf), distributor primary data; same values in the ASTM A615 scope on [ASTM](https://store.astm.org/a0615_a0615m-22.html)). Lap lengths "40 d" are a rule of thumb only; the true Class B tension lap depends on bar size, strength, cover, spacing and coating, so take the lap from the drawings (search summary: [rebar calculator pages](https://pro.buildingclub.info/en/steel/rebar-calculator-ft-lbs-cost/)); this project says 30 diameters (spec p.46-47).

---

## 5. Material breakdown an estimator lists (primary materials and what follows from them)

**Pier footing (per type):** concrete (CY, strength from detail; this job 3,000 psi minimum at the A-401 drive-thru island foundation; the A-401 bollard detail shows no strength); tube form EA/LF if used; vertical bars and ties/spirals (LF -> LB); anchor bolts with nuts and washers where a base plate or pole sits on it (EA, size from the base detail); excavation (CY bank); backfill; haul-off (loose CY); bar supports (precast blocks over earth per this spec).

**Strip footing + CMU enclosure:** footing concrete (CY); longitudinal bars and dowels (LB); formed edges if formed; excavation, backfill, haul-off; CMU units by type (standard, bond-beam, corner, KO/lintel, jamb) with 8 x 8 x 16 as the standard unit; vertical reinforcing bars (#5 here) (LB); bond-beam bars (LB); grout (CY) for reinforced cells and bond beams; mortar (CF or bags + sand); through-wall flashing, weeps/weep screen, sealant and control-joint material if shown; precast cap (LF) on a mortar bed with stainless dowels (A-190 detail 5; project); wall coating (SF, this job 5/8" cementitious coating painted). Gate: steel leaf size and count, gate posts (bollard-type 6" posts here), hardware items listed in the key notes (cane bolt, support wheel, signage); post footings.

**Bollards:** pipe (EA, LF by cut length), fill concrete (CY), cap plate if specified, cover/sleeve and reflective tape or paint (finish items counted EA), footing (above), excavation/haul-off. This job: Schedule 40 pipe, 1/4" cap plate, annulus grout, fill solid (spec p.118, p.120), bollard cover per A-401 note.

**Pads/slabs:** concrete (CY or SF at thickness), base (gravel/ABC SF x depth -> CY), vapor retarder (SF + laps), WWR (SF + laps) or bars (LB), supports and tie wire, edge forms (LF), expansion/isolation joint (LF), saw-cut/control joints (LF), curing compound (SF), finish (broom, SF). 3,000-psi concrete bag/yield conversions come from the supplier, not from a generic table.

**Drive-up island / foundation (ATM, canopy):** concrete island with a thickened foundation (CY), top and bottom mats of bars (LB), anchor bolts or embeds supplied by the equipment vendor (template EA), canopy column base plates and anchors (EA), conduit stub-ups (EA, size, LF) and a hand hole, pull strings and flex conduit (EA/LF), bollards (EA) around the ATM, and a vendor-coordination allowance (see section 8). Drive-thru analogs (speaker post): concrete foundation with four anchor bolts and embedded conduit, set 6-10 in. above the lane, template-placed bolts ([HME install guide (search summary)](https://www.hme.com/techPdfs/400G262%20Rev%20F.pdf)); highway handhole practice: conduits enter 12 in. below the top, are capped if unused ([Iowa DOT (search summary)](https://ia.iowadot.gov/erl/Apr_2008/US/content/8020.htm)). Treat these as analogies; the ATM vendor's template governs.

**Monument sign:** if "design and permit by others", the site contractor's takeoff is usually EA for the sign, the sign foundation as designed by others (not in drawings, flag it), and the power conduit/disconnect (E-010 "monument sign power"). If the foundation is detailed: drilled pier or spread footing concrete (CY), cage bars (LB), anchor rods (hot-dip galvanized, survey-verified elevation and location, no grout under base plate per [Oregon DOT TM622 (search summary)](https://www.oregon.gov/ODOT/Engineering/202601/TM622.pdf)), conduit.

**Sign posts (traffic signs):** post (EA/LF), panel (EA), footing for the post (CY), bolts. This job: 2'-0" embedment, 8" dia. pipe footings for some (C-6; project line 648, 654).

---

## 6. Special cases and how the three "by others" items are handled

- Canopy, ATM and monument sign are vendor items. The drawings say "prefabricated canopy ... coordinate with bank equipment vendor", "ATM by bank equipment vendor", "proposed monument sign, design and permit by others" (A-401, C-3.0; project). Quantity rules: (1) count the item EA once, never size it by guesswork; (2) never create dimensional numbers the drawing does not give; (3) list the interface scope that the drawings do give: bollards, conduit stub-ups (ATM: one 3/4" conduit for power; one 2" conduit with two pull strings for data/security; canopy: one 3/4" conduit for power and one 3/4" with a pull string for security; 6" deep well open to gravel for stub-ups; flex coiled in the hand hole; A-401 stub-up notes; project), the island/foundation concrete, anchor/bolt templates; (4) record the unknown (canopy footing sizes, sign foundation) as an open question, not as zero.
- Light pole footings, transformer slab and ground pad are electrical-site items with civil/electrical sheets (E-010, E-012; project); decide once which trade owns the concrete and avoid double-count.
- Existing monument sign removal belongs to demolition (C-1.0, 1 EA; project).

---

## 7. Common mistakes and how to check a takeoff

1. **Using the nominal diameter for pipe fill** or ignoring displacement of the pipe in the footing; verify with the pipe table (Continental Steel) and cylinder formula.
2. **Wrong volume formula for round piers**; one calculator site's pier formula (diameter x height x 0.7854, no division by 27) is dimensionally wrong ([search summary](https://api.copychief.com/?p=48056)). Check: 24"-dia x 3 ft = 0.349 CY (derived).
3. **Counting buried masonry as height above grade** or measuring from grade to cap while the footing top is 1'-4" lower (this job: 6'-8" + 1'-4" = 8'-0").
4. **Double-counting overbreak** in both excavation geometry and concrete waste; mixing bank, loose and compacted yards (model; Trimble).
5. **Applying waste before deductions or twice**; do not add waste to a published consumption rate that already includes it (TEK 04-02A 119 units includes 5%; TEK 03-11 mortar includes 10%; Table 3 grout includes 3%).
6. **Hiding laps inside the waste %**; take scheduled laps, hooks and dowels explicitly (model; spec p.46-47, p.59).
7. **Ignoring cover**, which shortens every footing bar; 3" for ground-contact footings ([ACI FAQ](https://www.concrete.org/frequentlyaskedquestions.aspx?faqid=903)).
8. **Omitting the small items**: jamb bars, corner bars, footing dowels at each vertical bar, gate-post footings, cap pieces, weep screen, anchor bolts and templates, conduit stubs, hand hole, joint filler, vapor retarder laps. Common estimating misses include "odd items" ([handoff.ai](https://handoff.ai/blog/concrete-takeoff)).
9. **Treating "2 LF/SF" as exact for small pads**; perimeter and second mats change it (model).
10. **Ordering short loads**; NRMCA advises against clean-up loads under 4 CY ([CIP 31](https://www.prairie.com/wp-content/uploads/sites/4/2024/12/31p_OrderingReadyMixedConcrete.pdf)). On a job where every footing is under 3 CY the order logic is about grouping pours.
11. **Using a master-spec dumpster detail as the project detail**; the Duke and Albuquerque numbers differ (6" slab with #4 at 12" vs. 6" slab with 6x6-10/10 mesh) and neither is this job.

Checks: (a) every EA item has a matching footing or an explicit "by others"; (b) footing CY / count = cylinder formula for the stated D and H; (c) CMU SF / (LF x height) = 1.0 after deductions; (d) units/100 SF within 113-119 (plus special units); (e) grout CF/100 SF compared with Table 3 for the stated spacing, so "full grout" or "9.1" is a visible choice; (f) bar LB / footing LF is plausible (e.g. 3 #5 = 3.13 lb/LF, derived); (g) excavation >= footing + working space, haul-off = excavation - backfill; (h) counts on the plan equal counts in the legend, once per symbol (do not count a bollard on both site and enlarged plans).

**Calibration from this job's reference estimate (quantities only, project).** Pier footings: reference concrete volumes equal net cylinder volumes within about 1% (e.g. 16"x4' x 8 = 1.647 CY vs 1.655 CY formula; 12" x 3'-6" = 0.1024 vs 0.1018 CY, derived), with excavation and haul-off equal to the footing volume (no overdig, no swell, no waste). Wall footing: 2'x1' x 36.2 LF = 2.68 CY, exactly the formula, with excavation 12.50 CY (9.3 SF of trench cross-section per LF, 3.5x the footing, derived), backfill 8.66, haul-off 3.84 CY. CMU: 289.76 SF = 36.2 LF x 8.00 ft; grout 3.245 CY = 30.2 CF/100 SF (derived), which is 84% of the TEK full-grout figure (36.1) and 3.3x the TEK 8"-at-32" figure (9.1), and mortar 1.798 CY = 16.7 CF/100 SF (derived), about twice TEK's 8.5. That means the reference estimator grouted heavily (A-190 shows KO bond-beam units grouted solid and #5 at 32" max) and used a mortar rate above NCMA's face-shell rule. A takeoff that applies the TEK partial-grout figure will be far below the reference; the grout convention (full vs. reinforced cells + bond beam) must be an explicit, stated input. **Not found in the reference estimate by keyword search:** the A-401 drive-thru island and thickened foundation (stadium 20'-0" x 4'-0", R2'-0" ends, 10'-0" thickened foundation, 4'-0" x 2'-6" section with #5 at 12" each way, 3,000 psi; derived areas: island 76.6 SF; thickened section 10 x 4 x 2.5 ft = 3.70 CY, whole island at 2'-6" would be 7.09 CY). Check whether it is carried elsewhere (e.g. flatwork) before declaring a miss.

---

## 8. What an AI takeoff must read from the drawings and specs

1. **Enumerate site objects from the legend/symbols, then find each object's detail.** For every footing/pad/pier symbol: type tag, count (once per symbol across site and enlarged plans), diameter or L x W, depth below grade, reinforcement (size, number, spacing, direction), concrete strength, cover, lap rule.
2. **Wall elevations and sections**: height above grade, height below grade to footing top, cap detail, bond beam courses, vertical bar size and spacing, KO/grouted-solid cells, flashing, weeps, openings and gate width.
3. **Footing/stem section and notes**: width x depth, bar count/size, dowel size/spacing, footing continuity at gates, isolation joint filler, vapor retarder.
4. **Pad/slab detail**: thickness, base thickness, mesh or bars, slope, joint spacing, edge conditions, control-joint spacing vs. NRMCA limits (24-36 x thickness, <= 15 ft).
5. **Bollard/post details**: pipe size and schedule, exposed height, embed, footing diameter/depth, whether fill is concrete, finish/cover. Read spec 05 50 00 for set-in-hole requirements.
6. **Bank equipment sheet**: island plan dimensions (including radii), thickened-foundation extents, section depth and above-grade projection, bar mats, conduit stub-up list (size, count, pull strings, hand hole), canopy column locations and "by vendor" notes, bollard count and heights.
7. **Civil plan**: location and count of enclosure, signs, monument sign, bike racks, transformer pad, clean-out pads; geotechnical notes for bearing/excavation and swell; existing items to remove.
8. **Specs**: reinforcement cover, lap rules, bar supports, WWR lap, joint types, concrete strengths by element, masonry grout type and placement (the 03 33 00/03 20 00 pages here), bollard spec, anything giving unit weights or tolerances. Record where a spec section is missing (no 04 22 00 or 32-series here).
9. **Mark conflicts and unknowns explicitly**: e.g. WWR lap 6" in spec vs 8" ACI-439 rule for 6x6; "(assumed details)" notes on civil sheets; vendor-furnished items with no dimensions. Output net quantities, the rule used, waste/overbreak, and order quantity as separate numbers, and never convert an unknown into a number or a zero.
10. **Stay consistent with ownership**: the enclosure, bollards, pads, sign footings and conduit stubs each sit in one trade line; the same concrete cannot also appear as slab, paving or electrical.

---

## 9. Source quality and gaps

- Strongest: NCMA TEK 04-02A and 03-11, NRMCA CIP 31 and CIP 6 (hosted on prairie.com), Sonoco Builder's Tube data sheet, Continental Steel pipe table, CMC rebar table, ACI FAQ on 3" cover, ASCC WWR article, Duke and City of Albuquerque master standards, and the project's own drawings/specs.
- Weak or missing: no primary source found for rebar waste %, bar chair counts per area (CRSI Manual of Standard Practice not accessible; the project spec gives its own spacing), concrete waste for tiny pours beyond NRMCA 4-10%, ATM-specific foundation requirements (vendor site-prep guide not found), monument-sign foundations (only DOT sign-foundation analogies), and estimating-software conventions for deductions in site walls.
- Second opinion (GPT-6 Astra, via `tools/ask_gpt.py`) was used only to cross-check conventions; items marked (model) have no external citation and should be confirmed against company practice.
- No prices, labor hours or productivity were read, used or recorded in this file.
