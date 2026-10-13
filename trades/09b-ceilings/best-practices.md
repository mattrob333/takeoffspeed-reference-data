# Ceilings takeoff best practice: gypsum ceilings and soffits, acoustical ceilings, baffles

Scope: quantities and material types only. No pricing, no labor productivity.
Written 2026-10-13 for the 09b-ceilings trade (CSI 09 29 00, 09 22 16, 09 51 13, 09 54 xx).

## 0. How to read this document

Evidence is graded on every number:

- **PUBLISHED** means a manufacturer, standards-derived spec or handbook states it. A link follows.
- **CONVENTION** means estimator practice. No authoritative published figure was found. It is flagged and must be treated as a default that the contractor can override.
- **PROJECT** means it comes from this job's own spec or drawings, so it is not general practice.

Limits of this research (be honest about them):

- The web-search budget ran out part-way through. No RSMeans, Craftsman, AWCI, CISCA handbook, ASTM C636/C754/C840 or GA-216 text was reachable. Where those standards matter, this document cites a manufacturer or federal guide spec that restates the rule (UFGS 09 51 00, 09 22 00, 09 29 00).
- Waste percentages and opening-deduction thresholds have no manufacturer-published value. They are marked CONVENTION. A single GPT-6 Astra second opinion is recorded in section 4 and is not a citable source.
- Carton counts are USG numbers. Armstrong and others differ. Always read the specified manufacturer's packaging data.

---

## 1. What an estimator takes off, and in which units

| System | Primary quantity | Unit | Derived or accessory quantities |
|---|---|---|---|
| Gypsum board ceiling (flat, on framing or drywall grid) | Net finished ceiling area, per board type and thickness | SF | Sheets (EA), framing LF, hanger wire EA, fasteners, tape LF, compound, trim LF, control joints LF |
| Gypsum soffit / bulkhead / fascia | Developed face area (vertical face plus bottom plus return) | SF, with LF of run as the driver | Soffit framing LF, hanger or brace points EA, corner bead and trim LF, board sheets |
| Exposed ceiling / structure (painted) | Area | SF | Paint is a different trade; list only for coordination |
| Lay-in acoustical ceiling (ACT) | Net ceiling area per tile type | SF | Tiles (EA), main tees LF, 4 ft and 2 ft cross tees EA, wall molding LF, hanger wires EA, hold-down clips EA, access panels EA |
| Linear metal / wood baffles | Baffle run length | LF (plus count of runs and lengths) | Carriers or grid for support, hangers EA, end caps EA, perimeter trim LF |
| Ceiling accessories | Fixtures that interrupt the ceiling | EA | Trim rings, light-fixture hangers (4 per fixture), access doors |

Notes:

- The CGC/USG handbook frames the gypsum estimate as "scaling a plan": length, width and ceiling height of each room, converted to square feet, summed, then divided into board lengths ([CGC handbook ch.3, Estimating][cgc3]).
- Soffits are length-driven on the plans (LF at a stated height). The material is area. SF equals LF times total developed face width ([GPT-6 second opinion, CONVENTION](#4-measurement-rules)). Measure each face (vertical, horizontal underside, return) separately.
- Baffles are bought in LF and counted by run. Footprint SF is not the baffle quantity (see section 6).

## 2. Which sheets and spec sections drive the takeoff

General practice:

- **Reflected ceiling plans (A-13x)** show ceiling type tags, heights, soffit and bulkhead locations, grid direction, fixtures and baffle layout. Federal and manufacturer guides both say the layout starts from the project plans and architect starting points ([Armstrong install §3.2][arm-inst]).
- **Floor plans / dimensioned plans** give wall perimeters for wall molding LF and the room boundaries that bound each ceiling zone.
- **Sections, wall sections and ceiling details** give heights, soffit profiles, and the substrate (suspended vs furred vs direct).
- **MEP drawings** locate diffusers, troffers, sprinklers, access panels. They matter for tile deductions and extra hangers (see section 4).
- **Structural drawings** show where hangers can attach (deck, joists, beams). Hangers cannot attach to steel deck tabs or roof deck in the project spec ([Spec 09 51 13, p.293](#project-sources)).
- **Specification sections**: 09 29 00 Gypsum Board (board type, thickness, finish level, control joints), 09 22 16 Non-Structural Metal Framing (framing and suspension), 09 51 13 Acoustical Panel Ceilings (tile, grid, hangers, molding, attic stock), 09 54 26 Linear Wood Ceilings (this job's index lists it; check whether it applies).

This project (PROJECT):

- Sheet A-130 Reflected Ceiling Plan: legend shows AC1 ceiling, AC2 ceiling, 5/8" GWB ceiling over 3-5/8" metal studs, exposed structure, six soffit types by LF, and an EIFS soffit. Sheet A-131 shows the BAR-1 baffle system.
- Spec index: 092216 Non-Structural Metal Framing (p.267), 092900 Gypsum Board (p.273), 095113 Acoustical Panel Ceilings (p.289), 095426 Linear Wood Ceilings (p.296) in `reference/sheets/spec_index.json`.
- A-130 notes: mechanical registers in fur-down align to grid; ceiling grid main tee must be perpendicular to linear lighting; gypsum ceilings painted PT-1 except over the transaction bar.

## 3. Standard product and layout facts that fix the quantities

### 3.1 Acoustical lay-in grid layouts (PUBLISHED)

- Standard 2x4: main beams 48 in. o.c., 4 ft cross tees at 90 degrees every 24 in. ([Armstrong install §3.1.1.1][arm-inst]).
- Standard 2x2: same layout, plus 2 ft cross tees at the midpoints of the 4 ft cross tees ([Armstrong install §3.1.1.2][arm-inst]).
- USG gives the same components: 4 ft cross tees serve both 2x4 and 2x2 patterns, 2 ft cross tees are for 2x2 only, and hanger wire is typically 12 gauge every 4 ft o.c. along each main runner ([CGC handbook ch.9][cgc9]).
- Hanger wire: minimum 12 gauge galvanized, spaced no more than 4 ft o.c. along the main beams unless the AHJ and load capacity permit more ([Armstrong install §5.3, 5.5][arm-inst]).
- Wire wraps and plumb: three full turns within 3 in., not more than 1 in 6 out of plumb, otherwise add a counter-splay wire ([Armstrong install §5.6, 5.7][arm-inst]).
- Wall molding attaches every 16 to 24 in. o.c. ([Armstrong install §4.1][arm-inst]). The federal guide spec says not more than 3 in. from ends and not more than 16 in. o.c. ([UFGS 09 51 00 §3.1.2][ufgs095100]).
- Main runners: at least two per ceiling span, and kept clear of abutting walls ([UFGS 09 51 00 §3.1][ufgs095100]).
- Lighting fixtures supported from the grid get at least four hangers per fixture, each within 6 in. of a fixture corner ([UFGS 09 51 00 §3.1.1.1][ufgs095100]).
- Border panels: aim for borders of at least 10 in. wide and equal on opposite walls ([Armstrong install §3.2.1][arm-inst]). USG describes the same equal-border layout from the room centerline ([CGC handbook ch.9][cgc9]).
- Minimum plenum drop for hangers: 4 in. from grid bulb to structure ([Armstrong install §5.4][arm-inst]).

### 3.2 Gypsum ceiling framing and suspension (PUBLISHED)

- Drywall suspension grid (USG flat ceilings): main tees at a maximum 48 in. o.c., hanger wires at a maximum 48 in. o.c., cross tees per manufacturer or UL listing ([CGC handbook ch.2, Drywall Suspension System][cgc2]).
- Armstrong FrameAll: cross tees 16 or 24 in. o.c. for 5/8 in. drywall and 16 in. o.c. for 1/2 in. drywall; hanger wires on mains 48 in. o.c. ([Armstrong FrameAll guide][arm-frame]).
- Federal guide spec: drywall grid cross tees at 16 in. o.c. with 1/2 or 5/8 in. board, 24 in. o.c. with 5/8 in. board only ([UFGS 09 22 00 §3.1.2.10][ufgs092200]). Suspended and furred ceilings follow ASTM C754 except framing is 16 in. o.c. unless indicated otherwise ([UFGS 09 22 00 §3.1.2.1][ufgs092200]).
- Maximum frame spacing by board: 1/2 in. single-layer ceiling 24 in. perpendicular (16 in. if water-based texture); 5/8 in. single-layer ceiling 24 in. perpendicular; double-layer 1/2 and 5/8 in. 24 in., but 16 in. if a fire rating is required ([CGC handbook ch.2, frame spacing table][cgc2]).
- USG drywall suspension components for flat ceilings are DGLW heavy-duty main tees (12 ft), 2, 4 and 6 ft cross tees and DGWM24 wall molding (12 ft), installed to ASTM C636, E580, C754 and CISCA ([USG AC3117][usg-flat]).
- Conventional grillage: 8 gauge hanger wires 48 in. o.c. along 1-1/2 in. carrying channels, carrying channels 48 in. o.c. and within 6 in. of walls, furring channels at right angles within 6 in. of walls ([CGC handbook ch.2, Suspended Ceiling Grillage][cgc2]).
- Furring channels 24 in. o.c. at right angles to bar joists, nested at least 8 in. at splices ([CGC handbook ch.2][cgc2]).
- Soffits: maximum vertical soffit height 48 in. with a maximum unsupported drywall area of 48 x 24 in.; intermediate cross tees are not needed when bulkhead dimensions do not exceed 24 in.; cross tee spacing in a horizontal soffit plane not more than 24 in. ([CGC handbook ch.2, Soffit and Fascia][cgc2]).
- Armstrong SimpleSoffit: standard main spacing 48 in. o.c., up to 72 in. depending on load; brace to structure as needed or at 96 in. o.c. ([Armstrong SimpleSoffit guide][arm-soffit]).
- Hanger wire is also required within 12 in. on both sides of a pivoted splice clip, and within 12 in. of a transition clip ([CGC handbook ch.2][cgc2]).
- Board fasteners to grid: No. 6 Type S Hi-Lo screws at 8 in. o.c. at the panel periphery and 12 in. o.c. in the field ([CGC handbook ch.2][cgc2]).

### 3.3 Control joints and relief (PUBLISHED, a takeoff item)

- Ceiling dimensions should not exceed 50 ft (2,500 SF) with perimeter relief and 30 ft (900 SF) without it ([CGC handbook ch.2][cgc2]).
- The federal spec says the same for interiors: 50 ft with perimeter relief, 30 ft without, and 30 ft for exterior ceilings and soffits ([UFGS 09 29 00 §3.2.13][ufgs092900]). Also put control joints where ceiling framing changes direction, or intermediate blocking ([same][ufgs092900]).
- Takeoff consequence: LF of control joint is a countable item whenever a ceiling zone exceeds these limits and the drawings do not show it. Flag it as a question rather than inventing it.

### 3.4 Seismic additions (PUBLISHED, spec and SDC driven)

- Armstrong: in Seismic Design Category D to F use minimum 2 in. wall molding, perimeter support wires within 8 in., horizontal restraint wire or rigid bracing over 1,000 SF, and seismic separation joints or full-height partitions over 2,500 SF ([Armstrong seismic brochure][arm-seis]).
- Category C uses minimum 7/8 in. molding with minimum 3/8 in. clearance ([Armstrong seismic brochure][arm-seis]).
- Drywall grid: hanger wire spacing 48 in. o.c., verticals at the perimeter wall no more than 24 in. from the wall, 12 gauge wire, terminal ends screwed to wall angle ([Armstrong FrameAll, seismic table][arm-frame]).
- Takeoff consequence: read the seismic design category on the structural general notes. It changes molding size, adds perimeter wires, bracing and trim rings (Armstrong notes 2 in. oversized trim rings for sprinklers in unbraced D-F ceilings, [same][arm-seis]).

### 3.5 Baffle systems (PUBLISHED)

- Armstrong MetalWorks Linear planks: hanger wires within 24 in. of the perimeter wall then 48 in. o.c.; main beam carriers 48 in. o.c. perpendicular to plank length; first and last carrier within 24 in. of the wall; carrier molding fastened to the wall every 16 to 24 in. ([Armstrong MetalWorks Linear guide][arm-linear]).
- Border plank rule: cut perimeter planks should be over 50% of their width, and equal on opposite sides ([Armstrong MetalWorks Linear guide][arm-linear]).
- Rockfon Intaline open-plenum baffles hang from 15/16 in. grid or a 4x4 module Cubegrid with hanger wire at 48 in. o.c.; baffle sizes 4 in. (V-base) and 6, 8, 10 in. (round base) ([Rockfon Intaline guide][rockfon]).
- Long baffle runs need alignment clips (top clip plus bottom sleeve or clip), and splices cannot sit directly under a carrier or main runner ([Rockfon Intaline guide][rockfon]).
- Baffles longer than 4 ft are handled by two installers ([Rockfon Intaline guide][rockfon]). Treat that as a lift note, not a takeoff rule.
- Practical takeoff: baffle LF drives the count of stock lengths. Pieces per run depend on the manufacturer's available lengths, so confirm them from the specified product. This job's BAR-1 is owner-furnished, so the estimate carries installation scope only.

## 4. Measurement rules

### 4.1 Openings and deductions

| Topic | Rule used in practice | Grade and source |
|---|---|---|
| Gypsum board, wall and ceiling openings | Many estimators "figure solid" and ignore door and window openings. Exceptions are large picture windows and large door openings | PUBLISHED, [CGC handbook ch.3][cgc3] |
| Calculator convention | CertainTeed's drywall calculator measures height floor to ceiling and width corner to corner, does not subtract openings, tells the user to round up, and states its estimates exclude waste | PUBLISHED, [CertainTeed calculator][ct-calc] |
| Deduction threshold | There is no universal threshold. Companies set their own (a 10 to 16 SF house rule was suggested by one model). Declare the cutoff in the estimate | CONVENTION, no authoritative source found |
| Lay-in tile | Deduct full ceiling modules that are replaced by fixtures or diffusers (a 2x2 troffer replaces one tile). Do not reduce grid, wall molding or hangers by the same amount | CONVENTION; supported by grid being continuous around fixtures ([UFGS 09 51 00 §3.1.1.1][ufgs095100]) |
| Large voids, shafts, areas covered by other ceiling types | Deduct from the gross zone | CONVENTION |
| Estimating software | Software conditions measure area, linear feet and counts and let the user deduct ceiling lights | PUBLISHED, [Estimating Edge][ee] |

### 4.2 Heights, slopes, corners, laps, overlaps

- Flat ceilings measure in plan. A ceiling height matters for hanger drop and for wall-hung soffit faces, not for the ceiling area. Armstrong's note of "minimum 4 in. drop, no maximum with 12 gauge wire unless local code limits it" ([Armstrong install §5.4][arm-inst]) means hanger length is a function of the plenum depth read from sections.
- Sloped or faceted ceilings need their own condition. Armstrong publishes a separate sloped-ceiling guide ([Armstrong sloped ceilings guide][arm-slope]). Measure true developed area, not plan area, for gypsum on a slope. This is CONVENTION; the guide was not opened in full.
- Wall molding: measure the perimeter of each ceiling zone, add nothing for corners except mitre and cut loss. Armstrong mitres inside corners and overlaps outside corners ([Armstrong install §4.2][arm-inst]).
- Gypsum board laps: boards run in whole sheets. Maximum practical length minimises butt joints, and ends and edges are located over framing ([CGC handbook ch.2][cgc2], [UFGS 09 29 00][ufgs092900]). Double-layer ceilings put the base layer perpendicular to framing and the face layer parallel with joints offset ([CGC handbook ch.3][cgc3]). Material area for multi-layer systems is face area times layers.
- Corners: trim at all internal and external angles, corner bead on external corners ([CGC handbook ch.2][cgc2]). Corner bead and trim are LF items, so each soffit return and bulkhead edge adds LF.
- Soffits: measure LF of soffit run, and for each run the vertical face height, the underside depth and the return. A single flat LF number understates board unless the profile is applied. Do not count the ceiling area under a soffit twice.
- Cross-check against the seismic and control-joint triggers in section 3.

### 4.3 Second opinion (not a source)

A GPT-6 Astra answer on measurement agreed with the above: measure actual finished face SF, separate ceilings from soffit faces, state the deduction cutoff, take off baffles as blade count and LF rather than footprint SF, and do not mix waste with separately specified attic stock. Its specific percentages (waste and thresholds) are used below only as flagged CONVENTION ranges.

## 5. Coverage, yield and waste factors

### 5.1 Gypsum board (PUBLISHED unless flagged)

| Item | Factor | Basis |
|---|---|---|
| Joint tape | About 370 LF per 1,000 SF of panels | [CGC handbook ch.3][cgc3] |
| Joint compound, conventional setting powder | 72 lb per 1,000 SF; lightweight setting powder 52 lb | [CGC handbook ch.3][cgc3] |
| Joint compound, all-purpose ready-mixed | 138 lb per 1,000 SF (CGC product) | [CGC handbook ch.3][cgc3] |
| Joint compound, USG ultralightweight ready-mixed | Approximately 9 to 10 gal per 1,000 SF of panels | [USG submittal J2051][usg-jc] |
| Screws, single layer to 16 in. o.c. framing | About 1,000 per 1,000 SF; about 850 at 24 in. o.c. | [CGC handbook ch.3][cgc3] |
| Screws, other cases | Appendix charts give counts per 1,000 SF by framing spacing, screw spacing and board size, with an allowance for loss | [CGC handbook appendix][cgc-app] |
| Adhesive (lamination only) | Tables per 1,000 SF by notch size and strip vs sheet lamination | [CGC handbook ch.3][cgc3] |
| Sheets per 1,000 SF net (computed) | 4x8: 31.25; 4x10: 25.0; 4x12: 20.8 | computed from 32, 40, 48 SF per sheet |
| Waste on board | 5 to 10% simple, 10 to 15% intricate or soffit heavy | CONVENTION (second opinion; no published figure found). The federal spec only says to select panel sizes to minimise waste and reuse cutoffs ([UFGS 09 29 00][ufgs092900]) |

CertainTeed states its calculator estimates do not include allowances for waste ([CertainTeed calculator][ct-calc]). The CGC handbook table is likewise a net-area quantity per 1,000 SF with a separate note to allow for loss on screws ([CGC handbook appendix][cgc-app]).

### 5.2 Acoustical lay-in ceilings

Computed per 100 SF of net ceiling (python, assuming mains 48 in. o.c., cross tees per the layouts in 3.1):

| Component | 2x4 layout | 2x2 layout | Basis |
|---|---|---|---|
| Tiles | 12.5 EA | 25.0 EA | area / module area |
| Main tee | 25.0 LF (2.08 pieces of 12 ft) | 25.0 LF | one main per 4 ft |
| 4 ft cross tees | 12.5 EA (50 LF) | 12.5 EA (50 LF) | one per 4 x 2 ft cell |
| 2 ft cross tees | 0 | 12.5 EA (25 LF) | one at the midpoint of each 4 ft tee |
| Total tee length | 75 LF | 100 LF | sum |
| Hanger wires (48 in. x 48 in.) | 6.25 EA | 6.25 EA | one per 16 SF; real count is higher (perimeter, fixtures, obstructions) |
| Wall molding | perimeter LF / piece length | same | 12 ft pieces: 40 per carton, 480 LF ([USG catalog][usg-cat]) |

Packaging (USG, PUBLISHED): 12 ft main tees come 20 per carton (240 LF); 4 ft cross tees 60 per carton (240 LF); 2 ft cross tees 60 per carton (120 LF) ([USG catalog packaging data][usg-cat]). A typical 2x2 USG panel carton holds 16 pieces for 64 SF, and 2x4 holds 8 pieces for 64 SF ([USG catalog][usg-cat]).

Waste and extras:

- Tile cutting allowance of about 10% is a common example for perimeter, fixture and obstruction cuts, but no authoritative source gives a standard percentage. Tile 3 to 10% and grid 5 to 10% are second-opinion ranges only (CONVENTION).
- Attic stock is a separate spec item, not waste. This project requires 10 percent attic stock of acoustical panel ceiling materials ([Spec 09 51 13, p.289](#project-sources)).
- Hold-down clips are required when panels weigh under 1.0 lb/SF or when a fire rating applies ([UFGS 09 51 00 §3.1.3][ufgs095100]).

### 5.3 Baffles (PUBLISHED structure, CONVENTION waste)

- Count runs and LF per run, then convert to stock lengths. Rockfon Sequence baffles are up to 8 ft (10 ft on the grid-clip version) and Armstrong Classics planks are 96 in. ([Rockfon Intaline guide][rockfon], [Armstrong MetalWorks Linear guide][arm-linear]).
- Supports follow the layout: carriers 48 in. o.c. with hangers at 48 in. o.c. ([Armstrong MetalWorks Linear guide][arm-linear]) or a 4x4 grid with 48 in. hangers ([Rockfon Intaline guide][rockfon]).
- Waste for field-cut stock: 5 to 10% (CONVENTION). Factory-sized pieces: 2 to 5% (CONVENTION).

## 6. Material breakdown lists

### 6.1 Gypsum ceiling (suspended or furred)

Primary: gypsum board by type (regular, ceiling/sag-resistant, Type X, moisture-resistant) and thickness; for exterior or humid areas, soffit board ([UFGS 09 29 00][ufgs092900]).

Follows from primary:
- Suspension: hanger wire, drywall main and cross tees or carrying channel plus furring channel, wall angle or channel molding ([CGC handbook ch.2][cgc2], [Armstrong FrameAll][arm-frame]).
- Fasteners: Type S screws to metal, with field and perimeter spacing above.
- Finishing: tape, compound, trim (corner bead, J-bead, control joint), per finish level specified. The project spec calls for Level 1 in plenum areas, Level 4 and Level 5 where indicated ([Spec 09 29 00, p.280](#project-sources)). Level 5 skim is extra compound.
- Insulation weight limit on sag: unsupported insulation over 1/2 in. board on 24 in. framing must not exceed 1.3 psf ([CGC handbook ch.2][cgc2]).
- Paint is handled in the paint trade.

### 6.2 Soffit / bulkhead

Primary: board face SF. Follows: framing LF (studs, track, or soffit grid), hangers or bracing points EA, corner bead LF, extra compound at returns. Armstrong SimpleSoffit mains at 48 in. o.c. with bracing at 96 in. o.c. ([Armstrong SimpleSoffit guide][arm-soffit]). The CGC soffit limits (48 in. vertical, 48 x 24 in. unsupported area) tell you when an intermediate member is needed ([CGC handbook ch.2][cgc2]).

### 6.3 Acoustical ceiling

Primary: tile by type and size. Follows: mains, 4 ft and 2 ft cross tees, wall molding, hanger wire, hanger fasteners/anchors, hold-down clips if required, access panels, acoustical sealant if specified at molding, and attic stock ([UFGS 09 51 00 §3.1][ufgs095100], [Spec 09 51 13](#project-sources)). Molding can be a different type at each edge condition. Include trim rings or edge moldings for round penetrations when the spec requires them ([Spec 09 51 13, p.292](#project-sources)).

### 6.4 Baffles

Primary: baffle blades (LF and count). Follows: carriers or grid, hangers, alignment clips and sleeves, end caps, perimeter or floating trim, and clips per manufacturer ([Rockfon Intaline guide][rockfon], [Armstrong MetalWorks Linear guide][arm-linear]).

## 7. Common mistakes and how to check a takeoff

Mistakes:

1. Treating baffle footprint SF as baffle quantity. Take off LF and count.
2. Counting the ceiling area under a soffit twice, or missing the vertical face and return.
3. Deducting tile modules but also reducing grid. Grid runs continuously around fixtures ([UFGS 09 51 00][ufgs095100]).
4. Using one waste percent for all materials; board, tile, grid and trim have different offcut behavior.
5. Mixing waste with the specified attic stock (10% on this job).
6. Missing the second or third ceiling type (here AC1 and AC2 are different tile and grid products: USG vs Armstrong tile, USG vs Gordon grid, per the reference estimate descriptions).
7. Ignoring control joints and seismic bracing triggers (section 3.3, 3.4).
8. Ignoring heights above the standard when hanger wire, soffit framing and lifts depend on them.
9. Taking off owner-furnished items as material (here BAR-1 baffles are furnished by owner).
10. Forgetting hold-down clips, access panels and extra hangers at fixtures.

Checks you can compute:

- Sum of ceiling zones by type should equal the plan areas of the rooms that carry that type, within the unmeasured gaps. Show the delta.
- Tile count times module area should be within the net area (add the fixture deductions back). Use the module of each tag: on this job ACT-1 948.75 SF / 4 SF (2x2) = 237.2 tiles and ACT-2 244.81 SF / 8 SF (2x4, A-170) = 30.6 tiles, 267.8 before waste. Dividing the 1,193.56 SF total by 4 gives 298 and overstates the count by 30.
- Main tee LF should land near area / 4. Cross tee length near area / 8 times 4 (2x4) or plus the 2 ft tees (2x2).
- Hanger count should not be below area / 16.
- Wall molding LF should equal the measured ceiling perimeter. Compare with the room perimeters on the floor plan.
- For gypsum: sheets = area / sheet SF; board SF = ceiling area plus soffit faces; ratio of tape LF to board SF near 0.37 ([CGC handbook ch.3][cgc3]).
- A material per-SF ratio far outside the published ones (section 5) usually signals a wrong unit or a missed layer.

## 8. What an AI takeoff must read from the drawings and specs

From drawings:

1. Ceiling zone boundaries and type tag per room (RCP legend and schedule), including exposed structure and soffit symbols.
2. Ceiling heights and soffit heights per tag (A-130 legend carries them in the label text).
3. Grid direction and layout notes (module 2x2 vs 2x4, main tee direction constraints, fixture alignment notes).
4. Soffit run lengths by type and the vertical dimensions given in the type name, plus soffit detail sections for the underside depth. Without the depth, board SF cannot be finished.
5. Baffle plan: runs, spacing, lengths, orientation, any gaps around MEP.
6. Fixtures, diffusers, sprinklers, access panels: counts per ceiling type.
7. Control joint and expansion joint locations, and fire-rated or sound-rated ceiling assemblies.
8. Perimeter conditions: molding types, shadowline or reveal, wall-to-ceiling transitions.

From specifications:

1. Tile: manufacturer, model, size, edge, NRC and CAC limits, color, attic stock.
2. Grid: duty class, face width, color, seismic and hanger rules (48 in. o.c., within 8 in. of ends, 3 turns on hangers, 4 turns on bracing in this spec).
3. Molding: type, fastening interval (not more than 16 in. o.c., 3 in. from ends here), sealant, no exposed pop rivets.
4. Gypsum: board type per location, thickness, layers, finish level, moisture-resistant locations, soffit board.
5. Framing: gauge, spacing, hanger attachment, deflection limits.
6. Who furnishes what (owner-furnished baffles) and who installs.

The reading must also record where a value is printed vs inferred, so a missing soffit depth is flagged rather than guessed. That follows the TakeoffSpeed rule of no invented data (see CLAUDE.md rule 1).

## 9. Observations from this job's reference estimate (quantities only)

These are what the estimator carried, not best practice. All ratios computed in python.

- ACT1 948.75 SF and ACT2 244.81 SF match the A-130 legend (948.7 and 244.8 SF) with no waste added. As tiles, ACT-1 is 948.75 / 4 = 237.2 (2x2) and ACT-2 is 244.81 / 8 = 30.6 (2x4 per A-170, not the 24x24 in the estimate text): 267.8 tiles before attic stock.
- Gypsum ceiling 516.0 SF against legend 516.1 SF (+0.02%). Sheets are exactly SF / 32 (4x8 board, no waste). Ceiling joists are SF / 1.33 = 387.969925 LF (0.7519 LF per SF, the 16" O.C. divisor 16/12 written as 1.33; the exact 16/12 rule gives 387.0).
- Soffit board 286.04 SF = Σ legend LF x GWB height x faces over the six A-130 soffit rows (4.2, 2.7, 6.7, 30.5, 35.3, 28.1 LF at 3.5, 4, 1.5, 3, 2.5, 2 ft), with "GWB BS" counted on 2 faces: 286.2 SF (+0.06%). No underside or return is in the line; the soffit bottom sits inside the gypsum ceiling area. Soffit studs are not a per-SF ratio of board: they are framing area (LF x framing height, 452.125 SF) / 1.33 = 339.9 LF plus 90.1 LF of 48" O.C. bracing, 430.0 LF against 429.6 (+0.10%). The 1.50 LF per board SF that this happens to give is a coincidence of two different formulas.
- Per 1,000 SF of board the estimate carries 31 tubes of adhesive, 0.75 rolls of tape, 5.36 lb of screws and 530 lb of compound ("mud plaster"), identically for ceiling and soffit. The compound figure is 3.8 times the CGC all-purpose figure of 138 lb ([CGC handbook ch.3][cgc3]); the unit definition probably differs. Treat as a template ratio, not a standard.
- BAR-1 baffles 370.76 LF (legend 370.8 FT), owner-furnished, installed by the GC.
- The reference carries each ACT type as one SF line with tile and grid named in the description (lines 292 and 293). Mains, cross tees, wall molding and hangers are not separate quantity lines, so a component-level takeoff is more detailed than the reference and cannot be scored against it.

## 10. Open items and gaps

- Opening deduction threshold, waste percentages and drywall grid carton counts: no authoritative published values found. Use project settings.
- Armstrong and USG tile carton counts vary by item; the USG 64 SF/carton figures are from their packaging table only.
- ASTM C636, C754, C840, GA-216 and CISCA texts were not read directly.
- Sloped and curved ceiling rules were not read in detail.
- RSMeans unit-of-measure conventions could not be verified.

## Sources

<a id="project-sources"></a>
Project sources (local files, PROJECT grade):
- `text/spec-p289.txt` to `spec-p295.txt` (Section 09 51 13 Acoustical Panel Ceilings: attic stock p.289, products p.291 to 292, installation p.293 to 294).
- `text/spec-p273.txt` to `spec-p281.txt` (Section 09 29 00 Gypsum Board; finish levels p.280).
- `text/A-130.txt` (reflected ceiling plan notes).
- `reference/markups/legends.json` (pages 5 and 6) and `reference/estimate/lines.json` lines 278 to 294 (quantities only).

External sources (all opened and read for the figures used):

[arm-inst]: https://www.armstrongceilings.com/content/dam/armstrongceilings/commercial/north-america/installation-and-maintenance/suspended-ceilings-installation-instructions.pdf
[arm-frame]: https://www.armstrongceilings.com/content/dam/armstrongceilings/commercial/north-america/technical-guides/hanging-framing-flat-ceilings-technical-guide.pdf
[arm-seis]: https://www.armstrongceilings.com/content/dam/armstrongceilings/commercial/north-america/brochures/seismic-design-what-you-need-to-know-brochure.pdf
[arm-linear]: https://www.armstrongceilings.com/content/dam/armstrongceilings/commercial/north-america/installation-and-maintenance/metalworks-linear-installation-guide.pdf
[arm-soffit]: https://www.armstrongceilings.com/content/dam/armstrongceilings/commercial/north-america/installation-and-maintenance/simplesoffit-installation-guide.pdf
[arm-slope]: https://www.armstrongceilings.com/content/dam/armstrongceilings/commercial/north-america/technical-guides/sloped-ceilings-technical-guide.pdf
[cgc2]: https://www.usg.com/content/dam/USG_Marketing_Communications/canada/product_promotional_materials/finished_assets/cgc-construction-handbook-ch02-framing-can-en.pdf
[cgc3]: https://www.usg.com/content/dam/USG_Marketing_Communications/canada/product_promotional_materials/finished_assets/cgc-construction-handbook-ch03-cladding-can-en.pdf
[cgc9]: https://www.usg.com/content/dam/USG_Marketing_Communications/canada/product_promotional_materials/finished_assets/cgc-construction-handbook-ch09-acoustical-ceiling-design-and-applicationcan-en.pdf
[cgc-app]: https://www.usg.com/content/dam/USG_Marketing_Communications/canada/product_promotional_materials/finished_assets/cgc-construction-handbook-appendix-can-en.pdf
[usg-flat]: https://www.usg.com/content/dam/USG_Marketing_Communications/united_states/product_promotional_materials/finished_assets/usg-drywall-suspension-system-flat-data-ac3117.pdf
[usg-cat]: https://s7d9.scene7.com/is/content/usg/USG/shared/assets/documents/catalog/usg-ceiling-solutions-catalog-pro-edition-wl294911.pdf
[usg-jc]: https://www.usg.com/content/dam/USG/pdpmovedocuments/sheetrock-ultralightweight-all-purpose-joint-compound-submittal-en-J2051.pdf
[ufgs095100]: https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2051%2000.pdf
[ufgs092200]: https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2022%2000.pdf
[ufgs092900]: https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2009%2029%2000.pdf
[rockfon]: https://www.rockfon.com/syssiteassets/rockfon-na/installation/install-guide/rockfon_intaline_metal_baffles_installation_guide.pdf
[ct-calc]: https://certainteed.com/drywall-calculator?area=138
[ee]: https://www.estimatingedge.com/knowledgebase/acoustic-area-condition-properties-general-tab/

Note on [usg-flat]: AC3117 is cited only for the drywall suspension component list (DGLW mains, 2/4/6 ft cross tees, wall molding) and for the standards it says to install to (ASTM C636, E580, C754 and CISCA).
