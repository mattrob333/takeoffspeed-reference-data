# Best practice: storm and sanitary utilities, inlets, structures, trenching - quantities and material types only

Scope: underground storm drain, sanitary sewer, roof-drain header, water and gas service, power and telecom service routes, drainage and sanitary structures (inlets, junction boxes, outlet control structure, cleanouts, manholes, headwall), the infiltration basin stone bed, and the trench excavation, bedding and backfill that go with them. Prices, labor and productivity are out of scope. Written 2026-10-13 for the single-storey bank branch in this repository (Fifth Third Bank, Watson Blvd, Warner Robins GA).

## Evidence labels (read first)

The WebSearch budget for this session was exhausted before any query returned results, so I could not search. I fetched specific pages directly. No manufacturer installation guide (ADS, Uni-Bell, ACPA, NPCA), no RSMeans page and no estimating-blog page was readable; those are listed as open items in section 10 rather than asserted.

- **[WEB]** a page I fetched and read this session. The link is the source.
- **[WEB-GUIDE]** a Unified Facilities Guide Specification (UFGS) section, a US Department of Defense master specification. It is authoritative for "what a specifier asks for", not a universal industry rule. Its bracketed blanks are unfilled in the guide.
- **[PROJECT]** read in this repository (paths relative to `` unless absolute).
- **[GPT, unverified]** second opinion from GPT-6 Astra (`tools/ask_gpt.py`, transcript `trades/33-site-utilities/scripts/ask1.txt`). It named standards but I did not open any of them. Its own text says the clearance, bedding, waste, density, slack and swell figures are provisional. Treat as leads to verify.
- **derived** arithmetic done in Python (`trades/33-site-utilities/scripts/worked.py`).

---

## 1. What an estimator takes off, and in which units

| Item | Unit | Basis |
|---|---|---|
| Storm drain pipe, by size, material, class | LF | Pipe is measured along the pipe centerline end to end, without deduction for the diameter of manholes [WEB-GUIDE: [UFGS 33 40 00 par. 1.1.1](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2033%2040%2000.pdf)] |
| Sanitary sewer pipe, by size, material | LF | Same convention; UFGS 33 30 00 points to Section 31 00 00 for earthwork and bedding [WEB-GUIDE: [UFGS 33 30 00 par. 3.2.2.2](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2033%2030%2000.pdf)] |
| Water service or main | LF | Measured centerline, center of fitting to center of fitting, center of main to center of hydrant, center of main to end of service; no deduction for valves or fittings [WEB-GUIDE: [UFGS 33 11 00 par. 1.1.1](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2033%2011%2000.pdf)] |
| Gas, power, telecom service routes | LF per route, count of parallel pipes noted | Utility-provider scope often stops at the meter or transformer; read "by utility" notes [PROJECT: `C-5.0` keynotes 1, 3, 4] |
| Drainage structures (inlets, junction boxes, manholes, control structures) | EA by type and size, plus depth | Counted as units complete with frames and gratings or covers; depth measured from top of grating or cover to invert of the outlet pipe; excess over a base depth is paid per vertical foot [WEB-GUIDE: [UFGS 33 40 00 par. 1.1.3](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2033%2040%2000.pdf)] |
| Cleanouts | EA, with riser LF if separate | Spacing and change-of-direction rules in section 3.2 [WEB: [IPC 2018 Georgia, 708](https://up.codes/viewer/georgia/ipc-2018/chapter/7/sanitary-drainage)] |
| Headwalls and walls | CY of concrete or masonry, or EA by standard detail | UFGS measures by cubic yards of concrete or masonry used and pays per wall [WEB-GUIDE: [UFGS 33 40 00 par. 1.1.4](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2033%2040%2000.pdf)] |
| Flared end sections | EA by size | [WEB-GUIDE: UFGS 33 40 00 par. 1.1.5, same link] |
| Trench excavation | CY, with bank/loose/compacted stated | Section 3 |
| Bedding, haunch, initial backfill, final backfill | CY per zone | Section 3 |
| Rock excavation in trench | CY, allowed width capped | UFGS caps rock payment width at 30 in for pipe of 12 in or less, and at pipe OD plus 16 in for pipe over 12 in; 1 ft is allowed outside structure wall lines [WEB-GUIDE: UFGS 33 40 00 par. 1.1.7, same link] |
| Replacement of unstable trench bottom | CY of select granular | [WEB-GUIDE: UFGS 33 40 00 par. 1.1.8, same link] |
| Valves, hydrants, tapping saddles, meters, backflow preventers | EA; valve boxes EA | Water-system units paid each, complete in place [WEB-GUIDE: UFGS 33 11 00 par. 1.1.2, link above] |
| Tracer wire, warning tape | LF over the pipe run | UFGS 33 40 00 par. 3.6 and 31 00 00 par. 2.3 (section 5) |
| Infiltration or detention stone bed, geotextile, underdrain | CY (stone), SF (fabric), LF (pipe) | [PROJECT: `C-4.2`] |

Unit discipline. 1 CY = 27 CF. Label every earth quantity bank (BCY), loose (LCY) or compacted. Aggregate is bought by the ton, so keep CY in place and tons as separate lines [GPT, unverified: ask1.txt section 1].

---

## 2. Sheets and spec sections that drive it (this job)

- **C-4.0 Grading Plan** carries the **STORM STRUCTURES** table (name, type, station, rim, invert in and out) and the **STORM PIPES** table (size, length, slope, invert up and down, material). This is the primary quantity source. [PROJECT: `trades/33-site-utilities/scripts/C-4.0.txt`]
- **C-4.1 Storm Profiles** repeats each run as "70 LF OF 18" HDPE @ 0.50%" with rim and inverts, and shows a 1.91 ft sanitary crossing. [PROJECT: `C-4.1.txt`]
- **C-5.0 Utility Plan** carries the **SANITARY STRUCTURES** and **SANITARY PIPES** tables, the water, gas, power and telephone keynotes, the meter and RPZ, and notes: 10 ft horizontal separation between water and sewer, vertical depth of existing dry and pressurized utilities unknown. [PROJECT: `C-5.0.txt`]
- **C-5.1 Sanitary Profiles**: cleanout S2 to S7, building connection S8, existing manhole S1 whose invert is "based on a utility locate and not verified, contractor to field verify". [PROJECT: `C-5.1.txt`]
- **C-4.2 Infiltration Basin Detail**: bottom of basin 435.00, bottom of gravel 429.5, 6 oz/SY non-woven geotextile, clean open-graded coarse aggregate, 6 in perforated HDPE underdrain, concrete riser with overflow inlet, no compaction of the stone bed. [PROJECT: `C-4.2.txt`]
- **C-0.1 General Notes**: sanitary pipe PVC per ASTM D 3034 or ductile iron per AWWA C150; water PVC C-900 (Class 200 under public roads, otherwise 150) or ductile iron; minimum trench width 2 ft; mechanical joints with thrust blocking; 10 ft parallel and 18 in vertical clearance between utilities; minimum 3 ft cover on waterlines; tops of existing manholes raised flush with new pavement; concrete for encasements 3,000 psi; contractor designs shoring and includes dewatering; stations and elevations refer to the center of drop inlets, manholes and junction boxes. [PROJECT: `C-0.1.txt`]
- **C-6.x Details**: the RCP storm plan note about a 4 in concrete collar where PVC meets RCP (`C-6.x` text) and pavement subgrade compaction to 98% standard Proctor. [PROJECT: `C-6.0.txt`]
- **Specification**: the project manual has no Division 33 section (spec index lists only 313116 Termite Control in this range). Underground trenching rules sit in Div 22 and 23 text: open cut only, no tunneling, bell holes, hand-fill 12 in above the top of pipe with suitable earth compacted to 95% Proctor, no water settling. [PROJECT: `reference/sheets/spec_index.json`, `text/spec-p377.txt`, `spec-p405.txt`]

Consequence for an AI: with no Division 33 spec, bedding type and thickness, structure sizes and frame and cover types are mostly **not stated** here. Those items must be flagged as assumed (the estimate itself writes "NO DETAILS SO ASSUMED" on lines 731 to 733) [PROJECT: `reference/estimate/lines.json` lines 731-733].

---

## 3. Measurement rules

### 3.1 Pipe length

- Take the length from the pipe table where one exists. Here the table lengths are structure-center to structure-center: 18 in HDPE 17.69 + 45.97 + 92.25 + 85.26 + 70.17 + 21.08 = 332.42 LF, 15 in HDPE 25.11 LF, 6 in PVC sanitary 295.96 LF **derived** [PROJECT: `C-4.0.txt`, `C-5.0.txt`]. The estimate carries exactly those totals [PROJECT: `lines.json` lines 721-723]. That is the UFGS rule: centerline, no deduction for manhole diameter [WEB-GUIDE: UFGS 33 40 00 par. 1.1.1].
- Plan length is horizontal. A sloped run is longer by sqrt(L^2 + dz^2); for 0.5% to 1% this is below 0.005% and ignorable, but for steep service risers it is not [GPT, unverified: ask1.txt section 1; **derived** check: 17.69 ft at 0.5% gives dz 0.09 ft].
- Keep installed length (measured) separate from procurement length (installed plus cuts and stock-length rounding) [GPT, unverified].
- Where there is no pipe table (roof-drain header, water, gas, power, telecom), the length is scaled from the plan. The estimate's scaled lengths agree with the two-reader markup values for the 8 in header (168.18 vs 168.2) and the water line (138.27 vs 138.3) but the gas line differs (152.0 in the estimate, 156.4 in the markup legend) [PROJECT: `lines.json` 724-726; `reference/markups/legends.json` pages 74, 77]. Scaled lines carry more uncertainty than table lines.

### 3.2 Structures

- Count by type from the structure table and the legend; separate **EXISTING** rows. C-4.0 lists C1-STJB as "JUNCTION BOX (EXISTING)" and S1-SSMH as "MANHOLE (EXISTING)"; neither is a new structure. The estimate counts 1 junction box (B1) and 1 connection at the existing manhole [PROJECT: `C-4.0.txt`, `C-5.0.txt`, `lines.json` 732, 737].
- Depth = rim minus lowest connecting invert, from the table. Derived for this job: A2-STGI 3.31 ft, A2.1-STYI 4.68, A2.2-STGI 3.11, A3-STGI 4.11, A4-STGI 3.65, B1-STJB 3.38, C2-STGI 3.15, A1 headwall 0.82, B2 outlet control structure 0.67. Sanitary cleanouts S2 to S7: 5.4 to 6.7 ft **derived** [PROJECT: tables above]. Stations, rims and inverts refer to the structure center (C-0.1) [PROJECT: `C-0.1.txt`].
- Rim-to-invert is not the excavation depth. Add base slab, aggregate foundation, bedding and any working space [GPT, unverified: ask1.txt section 2].
- Manhole steps are not required where the manhole is less than 4 ft deep; a steel ladder is called for above 12 ft [WEB-GUIDE: UFGS 33 30 00 par. 2.2.17, 2.2.18, link above].
- Cleanouts: required at not more than 100 ft intervals on building sewers and horizontal drains, at changes of direction over 45 degrees (one cleanout may serve changes within 40 ft of developed length), at or near the building drain to building sewer junction, and within 10 ft of the right of way on building sewers; 6 in and smaller pipe needs 18 in clearance in front of the opening [WEB: [IPC 2018 Georgia, 708.1.1 to 708.1.9](https://up.codes/viewer/georgia/ipc-2018/chapter/7/sanitary-drainage)]. Six cleanouts at S2 to S7 on a 296 LF run are consistent with that, and the estimate carries 6 EA [PROJECT: `lines.json` 729].

### 3.3 Trench geometry

**Width.** The pipe manufacturer's installation manual governs. UFGS 31 00 00 gives the general design range as 12 to 24 in plus pipe OD for smaller pipe and 24 to 36 in plus OD for larger pipe, and a cap of 24 in below the top of pipe plus OD for pipe under 24 in [WEB-GUIDE: [UFGS 31 00 00 par. 3.4.2](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2031%2000%2000.pdf)]. C-0.1 sets a 2 ft minimum trench width on this job [PROJECT: `C-0.1.txt`]. GPT suggests OD + 2 x 6 to 12 in as a preliminary range [GPT, unverified]. The engine's rule, 1.25 x OD + 12 in as an ASTM D2321 minimum, is repeated from the engine's own convention text and I did not open ASTM D2321 [PROJECT: `TakeoffSpeed repo: lib/quantities/trades/site/earthwork.ts` line 405; not verified here, ASTM pages returned HTTP 403].

**Depth.** Ground (or subgrade from which the trench is cut) minus invert, plus pipe wall thickness, plus bedding below the barrel. Invert is the inside bottom, so the trench bottom is lower than the invert [GPT, unverified; same as the engine's `trenchLines` note in `shared.ts`].

**Side slopes and protection (OSHA 29 CFR 1926 Subpart P).**

| Soil type | Maximum slope H:V (excavations 20 ft or less) |
|---|---|
| Stable rock | vertical |
| Type A | 3/4 : 1 |
| Type B | 1 : 1 |
| Type C | 1 1/2 : 1 |

[WEB: [OSHA 1926 Subpart P App. B](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926SubpartPAppB)]. A protective system is required unless the excavation is entirely in stable rock or is under 5 ft deep with no indication of cave-in [WEB: [OSHA 1926.652](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.652)]. Excavations 4 ft or deeper need a ladder, stair or ramp within 25 ft of lateral travel, and excavated material and equipment stay at least 2 ft from the edge [WEB: [OSHA 1926.651](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.651)]. Over 20 ft the system must be engineer-designed [WEB: OSHA App. B note 3, link above]. UFGS also keeps spoil 4 ft from a ditch edge [WEB-GUIDE: UFGS 31 00 00 par. 3.4].

The estimator must decide, and state, whether the quantity is **vertical-sided (shield or box)** or **sloped**. That decision changes the excavation several-fold (section 8).

**Volumes** (feet, divide by 27) [GPT, unverified formulas; they are plain geometry and I re-derived them]:

- vertical trench: V = L x W x H / 27
- sloped trench, slope m : 1: V = L x H x (W + m x H) / 27
- pipe displacement: L x pi x OD^2 / 4 / 27, using the outside diameter
- bedding below the pipe: L x W x b / 27
- backfill = excavation - pipe displacement - structures and other permanent volumes in the trench
- haul-off (bank CY) = excavation - backfill, which equals the displaced volume

The estimate follows this: excavation 456.667 CY, backfill 414.667 CY, haul-off 42.000 CY, and 456.667 - 414.667 = 42.000 exactly **derived** [PROJECT: `lines.json` 740-742]. The engine's `trenchLines` states the same identity [PROJECT: `shared.ts` line 284].

**Pipe zone.** UFGS 31 00 00: bedding and initial backfill compacted with approved tampers to at least 1 ft above the pipe, evenly on both sides, with attention to the haunches; plastic pipe bedded to the spring line; backfill of coated or wrapped sewer pipe free of stones over 1 in up to 2 ft above the pipe and 1 ft above other utilities [WEB-GUIDE: UFGS 31 00 00 par. 3.6.1.3, 3.6.1.4]. UFGS 33 40 00: plastic pipe bedding per ASTM D2321 with Class IB or II material (PVC, PE), compact in 6 in lifts by hand-operated compactors; concrete pipe haunch and bedding of select granular material [WEB-GUIDE: UFGS 33 40 00 par. 3.2.1, 3.2.5]. This job's Div 22 text asks for hand-fill 12 in above top of pipe at 95% Proctor [PROJECT: `spec-p377.txt`].

**Bedding material classes.** Class I angular 1/4 to 1-1/2 in graded stone; Class II coarse sands and gravels, max 1-1/2 in, soil types GW, GP, SW, SP; bedding per AWWA C600 or ASTM D2321 [WEB-GUIDE: UFGS 31 00 00 par. 2.1.6].

---

## 4. Standard coverage, yield and waste factors

Honest summary: very few of these are published as standards. Measure net installed quantity, then add procurement allowances as visible, labeled steps.

| Factor | Value | Basis |
|---|---|---|
| Trench rock cushion under pipe | at least 8 in, or 1/2 in per foot of fill over the pipe, whichever is greater, not more than 3/4 of nominal diameter | [WEB-GUIDE: UFGS 33 40 00 par. 3.1.2] |
| Compaction lift in trench | 6 in loose for hand-operated compactors, 8 in for other machines; final backfill 8 in loose lifts | [WEB-GUIDE: UFGS 33 40 00 par. 3.2.1, 3.8] |
| Density target | 90% (cohesive) and 95% (cohesionless) of maximum density in final backfill; test one per 50 LF per lift | [WEB-GUIDE: UFGS 33 40 00 par. 3.8] |
| Minimum cover, water | 3 ft on this job; a UFGS 33 11 00 design note for steel water pipe recommends 5 ft for ordinary conditions | [PROJECT: `C-0.1.txt`]; [WEB-GUIDE: UFGS 33 11 00, steel pipe earth-cover note] |
| Spacing between parallel pipes in one trench | adjacent sides at least half the nominal diameter or 3 ft, whichever is less | [WEB-GUIDE: UFGS 33 40 00 par. 3.3.7] |
| Utility separation | 10 ft horizontal sanitary to water, edge to edge; 18 in vertical clearance | [WEB-GUIDE: UFGS 33 30 00 par. 3.2.2.1.1]; [PROJECT: `C-0.1.txt`, `C-5.0.txt`] |
| Pipe cut and fit waste | 1 to 3% simple runs, 3 to 5% cut-intensive; no blanket lap on bell-and-spigot if effective laying length is used | [GPT, unverified: ask1.txt section 3] |
| Aggregate density | about 120 lb/ft3 gives 120 x 27 / 2000 = 1.62 short tons per CY; range 1.5 to 1.8 | [GPT, unverified]; arithmetic **derived** |
| Aggregate handling allowance | 2 to 5% | [GPT, unverified] |
| Tracer wire slack | 5 to 10% if risers and test stations are not detailed | [GPT, unverified] |
| Bank to loose swell | none published here; use the geotechnical report or a stated local factor | [GPT, unverified]; the engine defaults to 25% for common earth [PROJECT: `earthwork.ts` line 403, citing a handbook I did not open] |

Note on the stone bed. The estimate's 626.185185 CY underground stone storage equals 3,074 SF x 5.5 ft / 27 **derived**, where 5.5 ft is basin bottom 435.00 minus bottom of gravel 429.5 [PROJECT: `lines.json` 711, `C-4.2.txt`]. It is a net in-place volume with no swell or waste added. The detail forbids compaction of the stone bed [PROJECT: `C-4.2.txt`].

---

## 5. Material breakdown the estimator lists

| Primary item | Follows from it |
|---|---|
| **HDPE or PVC storm and sanitary pipe** | Gaskets or couplers per joint (count joints, not LF), fittings (bends, wyes, tees, reducers), structure boots or flexible connectors at each wall penetration, concrete collar where PVC meets RCP (4 in thick on this job), bedding stone or sand, tracer wire and warning tape if specified, geotextile if the bottom is unstable [WEB-GUIDE: UFGS 33 40 00 par. 3.2.5, 3.6; PROJECT: C-6.x collar note; GPT, unverified: ask1.txt section 4] |
| **Precast manhole, junction box, control structure** | Base, barrel sections, cone or flat top, adjusting rings, frame and cover, section gaskets or sealant, steps (not under 4 ft deep, ladder over 12 ft), pipe boots, channel and bench concrete, drop assemblies, lining or coating [WEB-GUIDE: UFGS 33 30 00 par. 2.2.17-2.2.18; GPT, unverified] |
| **Inlet or catch basin** | Base and risers, top slab, frame and grate (hooded grate, yard inlet), adjusting rings, pipe connectors, foundation aggregate [WEB-GUIDE: UFGS 33 40 00 par. 1.1.3; GPT, unverified] |
| **Cleanout** | Wye or combination fitting, riser to grade, bends, plug (recessed brass on this job), protective box, 18 in x 18 in x 8 in concrete pad (6 pads on this job) [PROJECT: `lines.json` 658, 729] |
| **Headwall, endwall** | Concrete CY and rebar, cutoff wall, apron, riprap by size class, filter stone, geotextile [WEB-GUIDE: UFGS 33 40 00 par. 1.1.4; UFGS 31 00 00 par. 2.4 (riprap); GPT, unverified] |
| **Water service** | Tapping saddle and corporation stop, curb stop, 1 in meter and setter, RPZ backflow assembly, valve boxes, thrust blocks or restrained joints at bends, tees and plugs, tracer wire for non-metallic pipe [PROJECT: `lines.json` 734-736; WEB-GUIDE: UFGS 33 11 00 par. 2.2.1, 2.2.8, 3.2.7] |
| **Gas service** | Utility-furnished pipe and fittings, trench, warning tape, tracer wire; scope boundary at the utility [PROJECT: `C-5.0` keynote 1; GPT, unverified] |
| **Power and telecom routes** | Conduit LF by count of parallel pipes, bends, trench, warning tape; usually priced under Division 26 and 27 [PROJECT: `lines.json` 727-728] |
| **Infiltration bed** | Open-graded stone CY (tons for purchase), non-woven geotextile on bottom, sides and top with laps, perforated underdrain, observation or cleanout ports, riser structure [PROJECT: `C-4.2.txt`, `lines.json` 709-711] |
| **Trench** | Excavation, bedding, haunch and initial backfill, final backfill, select granular for unstable bottom, flowable fill where the specification calls for it, haul-off, shoring or shield (contractor's means), dewatering allowance [WEB-GUIDE: UFGS 31 00 00 par. 2.2; PROJECT: `C-0.1.txt`] |

Warning tape and tracer wire details. UFGS 31 00 00: warning tape polyethylene, minimum 0.003 in thick (0.004 in detectable type), detectable for non-metallic piping when buried up to 3 ft deep; detection wire single-strand solid copper insulated, 12 AWG minimum [WEB-GUIDE: UFGS 31 00 00 par. 2.3.1 to 2.3.3]. UFGS 33 40 00: tracer wire for the full length of each run of non-metallic pipe, attached to the top of the pipe, and warning tape above all storm drain pipe, both as bracketed options [WEB-GUIDE: UFGS 33 40 00 par. 3.6]. On this job no specification section requires either, so they are **not** counted unless the drawings call for them.

---

## 6. Common mistakes, and how to check a takeoff

1. **Mixing length bases**: center-to-center vs inside-face vs procurement. State which; here the table is center-to-center (section 3.1) [GPT, unverified].
2. **Counting existing structures as new** (C1-STJB, S1-SSMH). Check the TYPE column for "(EXISTING)" [PROJECT: `C-4.0.txt`, `C-5.0.txt`].
3. **Rim-to-invert used as excavation depth**, missing wall, bedding and base slab [GPT, unverified].
4. **One average depth for the whole site.** The sanitary run is 5.4 to 7.1 ft deep, the storm runs 2.9 to 4.8 ft **derived**; they cross a 5 ft protective-system threshold [WEB: OSHA 1926.652].
5. **Nominal diameter used for width or displacement** instead of OD. HDPE and PVC ODs differ from nominal; read the product submittal [GPT, unverified].
6. **Omitting displacement** from backfill, so haul-off is wrong (section 3.3).
7. **Bank, loose and compacted CY mixed** (section 1).
8. **Assuming vertical sides without saying so**, or sloping everything. Compare section 8.
9. **Double counting trench vs structure excavation** where a pipe meets a structure [GPT, unverified].
10. **Scaled lengths trusted like table lengths.** The gas line differs by 4.4 LF between the estimate and the markup (section 3.1).
11. **Existing inverts assumed.** C-5.1 says the existing manhole invert is unverified; the trench depth at the tie-in is therefore provisional [PROJECT: `C-5.1.txt`].
12. **Counting a headwall in LF** when the contract measures walls in CY or by unit [WEB-GUIDE: UFGS 33 40 00 par. 1.1.4]. The estimate has the headwall as 9.0 LF (legend 8.8) [PROJECT: `lines.json` 738].
13. **Stone bed volume taken from a minimum-area note.** C-4.2 says "minimum surface area of 950 SF" while the delineated basin is 3,074 SF; use the drawn area and the detail depth [PROJECT: `C-4.2.txt`, `lines.json` 708].
14. **Conflicting drawing data not reconciled.** C-4.0 lists the outlet control structure rim as 435.67 while C-4.2 shows the concrete riser rim elevation 436.5; this changes the structure depth by 0.83 ft **derived** [PROJECT: `C-4.0.txt`, `C-4.2.txt`]. Flag, do not pick silently.

Checks that work on any job: (a) sum the pipe-table lengths per size and compare to plan-scaled lengths; (b) count structures on the plan, the table and the profile and match all three; (c) recompute each structure depth from rim and invert; (d) confirm excavation minus backfill equals displaced pipe and structure volume; (e) confirm a protective system and spoil handling are stated for every run over 5 ft.

---

## 7. What an AI takeoff must read, in order

1. **Structure tables** (name, type, station, rim, invert in and out, EXISTING flags) and **pipe tables** (size, length, slope, up and down inverts, material). Use them as the quantity of record for LF and EA.
2. **Plan keynotes and legend** for items with no table: services, meters, backflow, tapping saddles, cleanouts, headwalls, connection to existing, and the pipe material callouts.
3. **Profiles** for ground line, cover, crossings (the 1.91 ft sanitary crossing on C-4.1) and any deep or special sections.
4. **Details**: structure types and sizes, frame and cover, pipe trench detail (width, bedding thickness, pipe zone), thrust block table, cleanout detail, basin section. If a detail is missing, write "NO DETAILS SO ASSUMED" and cap confidence.
5. **General notes**: material lists, minimum trench width, cover, clearances, who designs shoring, dewatering, tie-in responsibility, utility-furnished scope.
6. **Specifications**: Division 33 sections if present; otherwise the Division 22 and 23 trench clauses. Record compaction, backfill depth over the pipe, no-tunneling and open-cut limits.
7. **Geotechnical report** for groundwater, rock, unsuitable soil, reuse of excavated material, and whether the soil is Type A, B or C if given.
8. **Flag, do not invent**: unknown OD, bedding class, structure wall thickness, protective system, tracer wire, thrust block volumes.

---

## 8. Worked check on this job (reconciliation)

| Item | Drawing/table | Estimate | Note |
|---|---|---|---|
| 18 in HDPE storm | 332.42 LF | 332.42 | exact table sum **derived** |
| 15 in HDPE storm | 25.11 LF | 25.11 | exact |
| 6 in PVC sanitary | 295.96 LF | 295.96 | exact (markup 295.8) |
| 8 in HDPE roof-drain header | no table; markup 168.2 | 168.18 | scaled |
| 1 in PVC water | markup 138.3 | 138.27 | scaled |
| Gas service | markup 156.4 | 152.0 | 4.4 LF apart |
| Hooded grate inlets | 5 (A2, A2.2, A3, A4, C2) | 5 | match |
| Yard inlet, junction box, control structure | 1, 1 new (C1 existing), 1 | 1, 1, 1 | match |
| Sanitary cleanouts | 6 (S2 to S7) | 6 | match |
| Headwall | 8.8 LF (markup) | 9.0 LF | unit questionable |
| Trench excavation / backfill / haul | not on drawings | 456.667 / 414.667 / 42.000 CY | haul = difference |

Sources: [PROJECT: `lines.json` 721-742; `legends.json` pages 74, 77; `C-4.0.txt`; `C-5.0.txt`].

**Trench volume worked example** (**derived**, `worked.py`). Assumptions that are mine, not from the drawings: OD 21.5 in (18 in HDPE), 17.7 in (15 in), 6.275 in (6 in PVC); 12 in clearance each side; 6 in bedding below; ground taken at the structure rim at each end. The ODs are unverified.

- Storm 18 in and 15 in, vertical sides: about 213 CY. Sanitary 6 in, vertical sides: about 184 CY. Together about 397 CY, with about 35 CY of pipe displacement.
- Sanitary alone with sloped sides: 549 CY at 3/4:1, 671 CY at 1:1, 914 CY at 1 1/2:1 (Type C). Storm alone: 396, 457, 579 CY.
- The estimate's 456.667 CY covers the above plus roof-drain header, water and gas. That is only possible with vertical or near-vertical, shielded trenches or shallower grades than the profile table implies; the sloped Type C case would exceed it by a wide margin on the sanitary run alone. The estimate's haul-off of 42 CY is close to my 35 CY displacement for storm plus sanitary, which supports the "haul-off equals displaced volume" reading. I did not reverse-engineer the estimate's exact width and depth; no clean combination of table lengths and round widths and depths reproduced 12,330 CF.

---

## 9. What this means for the app's quantity engine (compare only, not edited)

The engine's `site-utilities` module already follows most of this: pipe LF by run from the pipe table, structures by type with depth from rim and invert, trench excavation/bedding/backfill/haul-off as one identity, warnings at 5 ft depth for a protective system, and "NO DETAILS SO ASSUMED" with a low-confidence cap [PROJECT: `TakeoffSpeed repo: lib/quantities/trades/site/site-utilities.ts`, `shared.ts`]. Gaps worth checking against section 6: existing-structure exclusion, headwall unit, conflicting rim data between sheets, and the vertical vs sloped decision, which the engine fixes at vertical.

---

## 10. Open items I could not source

- Manufacturer installation data (ADS, Uni-Bell, ACPA, NPCA): trench width, bedding, OD tables, manhole section dimensions and weights. ASTM D2321, D3034 and C478 pages returned HTTP 403, so clause text is unverified.
- RSMeans or similar unit conventions for pipe, structures and trench; estimating-handbook coverage and waste factors for pipe, tracer wire and stone.
- A state DOT measurement clause (Georgia DOT section 550 URL returned 404).
- Gas distribution (UFGS 33 11 23 fetched but not read) and utility-owner standards.
- Typical manhole spacing: Wikipedia gives 7 to 20 m for sewers but it is a weak source [WEB: [Wikipedia, Manhole](https://en.wikipedia.org/wiki/Manhole)]; IPC requires manholes at changes of direction and at not more than 400 ft for sewers of 8 in and larger [WEB: IPC 2018 Georgia, 708].
- Swell and shrink factors, and aggregate unit weights for the specified stone.

If more searching is wanted, a follow-up message can continue the search once the web-search budget is raised.
