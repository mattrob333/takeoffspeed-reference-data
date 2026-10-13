# Division 08 Openings: quantity takeoff best practice

Scope: doors, frames, door hardware, windows, aluminum storefront and curtain wall, glazing, roof access hatch.
Quantities and material types only. No pricing or labor is covered.

## Evidence grading and limits of this research

- The WebSearch budget for this run was exhausted before any search ran. Every web source below was reached by fetching a known URL directly. The authoritative standards (ANSI/SDI A250.8, DHI hinge guides, ASTM C1193, GANA/NGA Glazing Manual, AAMA SFM-1, NFPA 80) are paywalled or were not fetchable, so their numbers are second-hand.
- Each factual claim carries one of three tags:
  - **[W]** was read on the linked page.
  - **[J]** is quoted from this job's own specification (`text/spec-pNNN.txt`, from `source/specifications.pdf`). It is binding for this job, not general practice.
  - **[G]** is a second opinion from GPT-6 Astra (`tools/ask_gpt.py`). It has **no link**. Treat it as unverified and check it against the standard before relying on it. The only [G] claims written here are the ones that matter for the takeoff and have no fetched source.
- Rules from standards that I could not fetch are written as "typical" and tagged [G].

## 1. What the estimator takes off, and in what units

| Item | Unit | Notes |
|---|---|---|
| Door opening (the schedule mark) | EA | One per mark. Opening, leaf, frame and hardware set are four different counts. |
| Door leaf | EA | A pair is 2 leaves in 1 opening. Leaves are listed by size, thickness, core/face, type letter, rating, glazing. |
| Frame | EA | Listed by type, gauge/material, throat (wall thickness), width x height, rating, welded or knock-down. |
| Sidelite / transom / borrowed-lite frame | EA, or LF of framing plus SF of glass | Carried with the storefront elevation, not as a hollow-metal frame. |
| Hardware set | EA of openings per set; items expanded per opening | Expand set x openings, then item quantity x leaf count where the set is leaf-based. |
| Hinges, continuous hinge | EA, or LF cut length for continuous | Record the cut length, not just EA. |
| Thresholds, sweeps, gasketing | EA or LF cut length | Per opening. Meeting-stile seals on pairs are separate. |
| Storefront / window framing | SF of system, LF of members by profile, EA of windows by tag | The SF is net of doors when doors are priced as door lines. |
| Glass / glazing | SF by glass type, plus EA of lites | Glass is ordered by lite size. |
| Setting blocks, gaskets, perimeter sealant | EA, LF, LF to cartridges | Follow from the framing and lite count. |
| Access hatch | EA by size, plus curb LF | Roof hatch curb may sit in Division 07. |

Source for the unit and grouping logic: the SDI "Technical Data Series" includes a recommended door, frame and hardware schedule form (111D-24) and a "Hinge and Strike Spacing" sheet (129) [W: https://steeldoor.org/tech_data/]. DHI publishes the "Sequence and Format for the Hardware Schedule" [W: https://www.dhi.org/Resources/Technical-Literature]. Full text was not read for either.

## 2. Which sheets and spec sections drive it

For the Fifth Third Bank, Warner Robins job (single-storey bank branch):

- **Sheets** (index `reference/sheets/index.json`): A-600 Door Schedule and Details (door types A to F, frame types, jamb and head details), A-601 Hardware Schedules, A-610 Window Elevations (window tags, storefront elevations), A-620 Interior Partition Schedule (wall thickness, which sets frame throat), A-140 Roof Plan (roof hatch and curb), A-200/A-201 Exterior Elevations, A-110 floor plan for door tags. Electrical and security plans (E-150) matter only for hardware that Division 28 supplies (readers, power supplies, motion sensors).
- **Spec sections** (`reference/sheets/spec_index.json`): 081113 Hollow Metal Doors and Frames (p.212), 081416 Flush Wood Doors (p.221), 083113 Access Doors and Frames (p.226), 084113 Aluminum-Framed Entrances and Storefronts (p.229), 084413 Glazed Aluminum Curtain Walls (p.240), 087100 Door Hardware (p.248), 088000 Glazing (p.258).
- MasterFormat Division 08 groups these sections. The SDI sample guide spec is also numbered 081113 [W: https://steeldoor.org/specifications/].

## 3. Measurement rules

### 3.1 Doors, frames
- Count from the door schedule, then confirm every tag on the plans. A tag that appears on a plan and not in the schedule (or the reverse) is a flag, not a guess. [G]
- Pair doors: the schedule size is **one leaf**. The frame opening is two leaves wide. Count 1 opening, 2 leaves, 1 frame. [G] The in-repo engine encodes this the same way (`TakeoffSpeed repo: lib/quantities/trades/interiors/doors-hardware.ts`).
- Split lines by anything that changes the material list: leaf type, frame type (welded vs knock-down vs slip-on drywall), rating, card reader, auto operator, vendor-supplied. In the reference estimate, identical 3'x7' Type B doors appear on separate lines with and without "CARD READER" (`reference/estimate/lines.json`, lines 191 and 192).
- Frame types matter to the material list. SDI's glossary defines knock-down (KD, assembled on site), welded (continuous or face weld) and drywall/slip-on frames (installed after the wall is erected) [W: https://steeldoor.org/glossary/].
- Frame throat comes from the finished wall thickness (stud plus board both faces) from the partition schedule, not from the door schedule. Wall type is on the partition sheet. [G] The in-repo convention is jamb depth = wall thickness + 7/8" (`doors-hardware.frame-depth-allowance-in`).
- Storefront entrance doors sit inside the storefront frame. Do not also take off a hollow-metal frame for them. This matches the reference estimate, where "(2) 3'Wx8'H ... STOREFRONT GLASS DOOR W/ ALUMINUM STOREFRONT FRAME" is a door line and the storefront system is a separate SF line (`lines.json`, lines 194 to 196 and 214).

### 3.2 Hinges and frame anchors
- **Hinges:** this job's spec requires the quantity in the hardware schedule "but not fewer than the number recommended by manufacturer ... or one hinge for every 30 inches of door height, whichever is more stringent" [J: spec 087100, p.257]. By that rule, a computed count is: 80" and 84" doors need 3 hinges, 90" needs 3, 96" needs 4, 120" needs 4 (computed in Python).
- The customary DHI/manufacturer table is 2 hinges up to 60", 3 up to 90", 4 up to 120", plus one per added 30" [G]. It agrees with the job rule for every height above, apart from the 60" and under case, which no door on this job reaches.
- Hinge count is per leaf, so a 7' pair has 6 hinges and a 7' single has 3. Frame hinge reinforcements match the hinges, not an extra set. [G]
- Continuous hinges replace the butt-hinge calculation and are measured in length. [G] On this job, hardware sets 1, 3 and 4 use a continuous hinge on the storefront doors (`lines.json`, lines 198 to 200).
- **Jamb anchors** (this job's spec): masonry type, anchors not more than 16" from top and bottom and not more than 32" o.c., three per jamb for 60" to 90" high frames. Stud-wall type, not more than 18" from top and bottom and not more than 32" o.c., four per jamb for 60" to 90" high [J: spec 081113, p.217]. A 7' stud-wall frame therefore takes 4 x 2 = 8 jamb anchors.
- **Floor anchors:** one welded to the bottom of each jamb, with four spot welds each. Slip-on drywall frames get anchor clips or countersunk holes instead [J: spec 081113, p.217]. SDI defines the adjustable floor anchor (for depressed or uneven slabs) and the fixed floor/base anchor [W: https://steeldoor.org/glossary/].
- **Spreader bars:** welded frames ship with two removable spreader bars across the bottom [J: spec 081113, p.213]. SDI defines the spreader as temporary [W: https://steeldoor.org/glossary/]. They are removed and not a purchase item.
- **Silencers:** drill the strike-jamb stop for three silencers on single frames, except on weather-stripped frames [J: spec 081113, p.217]. Pair frames typically take two, in the head [G]. SDI defines the silencer as a resilient mute on the frame stop [W: https://steeldoor.org/glossary/].
- Do not count hinge or strike reinforcement as a separate purchase when the frame and door come prepared. SDI defines both as plates attached inside the door or frame [W: https://steeldoor.org/glossary/]. The governing preparation standards are ANSI/SDI A250.6 (reinforcing and field hardware prep) and A250.14 (hardware mounting dimensions) [W: https://steeldoor.org/ansi/].

### 3.3 Hardware sets
- Take the set from the hardware schedule; the door schedule only names the set number. Multiply each item's per-opening quantity by the number of openings using that set.
- Read the quantity next to each item. A set item is quantified per opening, not per leaf, unless the schedule says "EA leaf" or the set heading says pair. A pair does not mean doubling everything. [G]
- Items that come from other divisions appear in the set but are not Division 08 supply: credential readers, power supplies, motion sensors ("BY DIV 28" in sets 1, 3, 6, 7 and 9 of the reference estimate, `lines.json`). Count them once, in the right division, to avoid double counting. This is a recurring failure when the same item shows in both the hardware set and the electrical sheets.
- Hinge counts left "as required" in a set are computed from leaf height (rule in 3.2).
- Thresholds, weather sweeps and astragals: the aluminum storefront spec requires a manufacturer's bottom sweep with concealed fasteners and a BHMA A156.21 threshold, beveled 1:2 or less, at most 1/2" high [J: spec 084113, p.235]. The BHMA standard list covers thresholds (A156.21), gasketing (A156.22), exit devices (A156.3), closers (A156.4), overhead stops (A156.8), butts and hinges (A156.1), mortise locks (A156.13), auxiliary hardware (A156.16) and finishes (A156.18) [W: https://buildershardware.com/ANSI-BHMA-Standards/Hardware-Highlights].
- Finish codes (US26D, US32D, 626, 630 and similar) are carried on the line but do not change the count. The BHMA code lookup is a spreadsheet and was not read [W: https://buildershardware.com/ANSI-BHMA-Standards/BHMA-Finish-Code-Lookup].

### 3.4 Accessibility and egress items that add hardware
- Accessible routes need 32" minimum clear door width, thresholds at most 1/2" high, operable parts 34" to 48" above floor, 5 lbf maximum opening force for interior hinged doors, and closer sweep of at least 5 seconds from 90 degrees to 12 degrees [W: https://www.access-board.gov/ada/ sections 404.2.3, 404.2.5, 404.2.7, 404.2.9, 404.2.8.1].
- Power-assisted and automatic doors follow ANSI/BHMA A156.19 and A156.10, with a 32" clear opening in both power-on and power-off modes (404.3, 404.3.1) [W: https://www.access-board.gov/ada/]. This is why the reference estimate carries "AUTOMATIC OPENER", "ADA SWITCH" and "POSITION SWITCH" items in the entrance sets (`lines.json`, lines 198 and 200).
- Panic hardware (exit devices) is required by code on doors serving assembly or high-occupancy areas, under IBC and ANSI/BHMA A156.3 [W: https://en.wikipedia.org/wiki/Panic_bar].
- Fire-rated openings carry listed labels on leaf and frame, and the self-closing device must fully close the door. NFPA 80 limits undercut to 3/4" and clearances to 1/8" (wood) or 3/16" (metal) at top and edges [W: https://en.wikipedia.org/wiki/Fire_door].

### 3.5 Storefront, windows, curtain wall
- Measure framing from the elevation: width x height of each elevation type, net of door openings, times the number of instances. The reference quantities for this job are 107.3 SF exterior storefront, 53.22 SF demountable-vendor interior system, and 44.56 SF interior storefront (`lines.json`, lines 214 to 216). The markup legend for A-610 reports the same 107.3 SF (`reference/markups/legends.json`).
- Windows are counted by tag with their size: tags A, C, D, E, G and H on A-610 (`lines.json`, lines 208 to 213).
- Framing LF = perimeter plus verticals plus horizontals, less door sill widths, by profile (the extrusion size, e.g. 2" x 4-1/2" mullion for the thermally broken system and 1-3/4" x 4-1/2" for the interior). Shared members count once. [G]
- Mullion terminology: horizontal members are cut slightly short for thermal expansion; aluminum mullions deflect about 3 times more than steel under the same load, which is why steel reinforcement appears in some mullions [W: https://en.wikipedia.org/wiki/Curtain_wall_(architecture)]. If the spec calls for reinforced mullions, list the reinforcement separately.
- Stick systems are field-glazed, unitized systems are factory-glazed [W: https://en.wikipedia.org/wiki/Curtain_wall_(architecture)]. Storefront is not curtain wall; curtain wall spans floors and handles building movement. The job spec has separate sections for each (084113 and 084413).
- Glass: typical commercial IGU is 1" overall (two 1/4" lites and a 1/2" airspace), with 1/4" monolithic used for spandrels and interior lites [W: https://en.wikipedia.org/wiki/Curtain_wall_(architecture)]. The reference estimate lists "1" THK. VITRO SOLARBAN 90 (2) ACUITY" for the exterior system and "1/4" THK. CLEAR FLOAT GLASS, FULLY TEMPERED" for the interior system (`lines.json`, lines 214 and 216).
- **Ordered glass size is not the visible size.** Glass is cut to daylight opening plus bite on each edge, or to pocket size less edge clearance; do not subtract bite from daylight size [G]. The in-repo engine assumes 1/2" bite on each edge for these 2"-sightline frames (`windows-storefront.glass-bite-in`); that figure is the engine's own assumption and was not confirmed by a fetched source.
- Setting blocks: typically 2 per glazed unit, sized and positioned by the manufacturer [G]. The job spec lists setting blocks, gaskets and shims as part of the manufacturer's standard glazing system [J: spec 084113, p.235], so they may be furnished with the framing and not be a separate buy.
- Perimeter sealant: both faces where the details show both. The A-600 details show "CONTINUOUS SEALANT BOTH SIDES, TYP." at hollow-metal frames and a sealant joint at the storefront (`text/A-600.txt`). Continuous sill members and flashing are set in a full sealant bed per Section 079200 [J: spec 084113, p.238].
- Perimeter firestopping at a curtain wall's floor-slab gap is separate from the wall system [W: https://en.wikipedia.org/wiki/Curtain_wall_(architecture)]. This one-storey job has no slab-edge gap.

### 3.6 Sealant yield
A 10.1 US fl oz cartridge holds about 18.2 in^3, so linear feet per cartridge = 1.519 / (joint width x depth in inches), before loss (computed in Python):

| Joint | LF per cartridge |
|---|---|
| 1/4" x 1/4" | 24.3 |
| 3/8" x 1/4" | 16.2 |
| 1/2" x 1/4" | 12.2 |
| 3/8" x 3/8" | 10.8 |
| 1/2" x 1/2" | 6.1 |

This is a volume calculation, not a coverage figure published by a standard [G]. The in-repo engine uses 24 LF (1/4 x 1/4) for door frames and 12 LF (1/2 x 1/4) for storefront perimeter, which match the table. Joint width and depth must come from the detail. ASTM C1193 is the guide for joint sealant use [G]; the ASTM page was not accessible.

### 3.7 Access hatch
- Count each by size and type: the reference job has one 30" x 36" roof access hatch (`lines.json`, line 197), listed with its components (gasket, slam latch, thermally broken cover, liner, hold-open arm, spring lift, stainless hinge pin, cover insulation). A separate LF line carries the prefabricated metal curb at the roof hatch (`lines.json`, line 172).
- Packaged hatches include hinges, latches, and frame/curb. Do not apply a door-hinge multiplier to them. [G]
- The job's Section 083113 covers access doors and frames (spec p.226). Roof hatch sizing and code minimums (IBC 1011.12) were not verified from a fetched source.

## 4. Waste and overage

| Item | Typical allowance | Basis |
|---|---|---|
| Doors, frames, complete hardware sets, hatches | 0% dimensional waste. List specified spares as separate lines. | [G] Factory-fabricated to size. |
| Aluminum storefront extrusions | Often 5 to 10% of net cut LF, until stock-length optimization replaces it. | [G] Cut loss on stock lengths. |
| Factory-cut glass | Take exact lite sizes; no blanket sheet waste. | [G] |
| Gaskets and backer rod | Often 5 to 10% of measured LF. | [G] |
| Sealant | Often 10 to 20% extra volume, then round up to whole cartridges. | [G] |
| Loose anchors, blocks, silencers, screws | Often 5 to 10%, then package rounding. | [G] |

None of these percentages is mandated by a standard (the GPT answer says the same). State the basis (cutting loss, stock lengths, breakage, package size or contractual spares) on every line. The in-repo engine carries a 10% waste class for specialty frame trim cut from stock lengths.

## 5. The material breakdown an estimator lists

For each hollow-metal opening: door leaf(s), frame (with anchors, floor anchors, spreader, hinge and strike reinforcement prepared at the factory), hardware set items, silencers, perimeter sealant at the frame where detailed, and any door/frame finish carried in Division 09. Per hardware set: hinges (or continuous hinge by cut length), lock/latch/exit device, cylinders, closer plus mounting plate and stop spacer, stops/holders, kick/push/pull trim, threshold and seals, silencers, electric strike/transfer/wiring harness, and the Div 28 items flagged by others.

For each storefront or window: framing by profile and LF, door framing, glass by type and SF, glazing gaskets, setting blocks, sill flashing, perimeter sealant, anchors, plus entrance door hardware (continuous hinge, exit device, pull, closer, threshold, sweep, auto operator).

## 6. Common mistakes and checks

| Mistake | Check |
|---|---|
| Opening, leaf, frame and hardware-set counts confused. | Reconcile: leaves = openings + pairs; frames = openings less storefront doors. |
| Doubling every pair item, or missing the inactive-leaf items (flush bolts, coordinator, astragal). | Read each hardware-set line's own quantity; add pair items only where the set lists them. |
| Counting frame hinge preps as extra hinges. | Hinges = leaves x rule; frame preps follow. |
| One anchor-count rule for every frame type. | Use wall type (masonry, stud, slip-on) and frame height. Spec says 3 per jamb masonry, 4 per jamb stud for 60 to 90 in [J: spec 081113, p.217]. |
| Storefront door frame also taken as a hollow-metal frame. | Entrance frame is part of the storefront elevation. |
| Door area left in storefront SF (double count) or door sill left in framing LF. | Subtract door openings from SF and door widths from perimeter LF. |
| Glass sized from visible daylight, not from cut size. | Add bite to D.L.O. per the manufacturer's detail. [G] |
| Div 28 hardware counted in Div 08 and again in electrical. | Mark "BY DIV 28" items and count them once. |
| Items copied from a generic set that this set does not list. | Take items only from the hardware schedule and spec. |
| Mixing rough opening, frame opening, daylight opening and glass size. | Label which one each dimension is. [G] |
| Ignoring addenda that change type letters or hardware set numbers. | Re-read the schedule revision block. |

Check totals by type against the markup legend counts and by sheet; flag any door tag with no set, any set with no door, and any type letter not in the schedule.

## 7. What an AI takeoff must read from drawings and specs

1. **Door schedule** (A-600): mark, location (interior/exterior), leaves (single/pair), size of one leaf, thickness, type letter, door material, frame material and type, rating, hardware set number, remarks (card reader, auto operator, vendor supplied).
2. **Frame type and door type elevations/details** on A-600: frame depth, anchors to studs, silencers, sealant both sides, threshold, sidelite.
3. **Partition schedule** (A-620): wall thickness at each door, which sets jamb depth.
4. **Hardware schedule** (A-601): every set's items and per-opening quantities; "as required" quantities; items by others.
5. **Window and storefront elevations** (A-610): tags, sizes, system type, mullion size, glazing type, lite grid, door positions inside the system, sill and head details.
6. **Roof plan and details** (A-140): hatch size, curb height, insulation.
7. **Specs**: 081113 (anchors, silencers, gauge, prep), 087100 (hinge rule, hardware quantities, keying), 084113/084413 (system, gaskets, thresholds, sweeps), 088000 (glass types), 083113 (access doors).
8. **Cross-sheet reconciliation**: every plan tag appears in the schedule, every set number in the door schedule appears in the hardware schedule, every storefront door appears in both the door schedule and the storefront elevation.
9. **Flag, do not invent**: a missing wall thickness, an unscheduled door material, a set with no items, an elevation with no lite sizes, or a tag found only on one sheet.

## 8. Reference-job calibration (quantities only)

The reference estimate's Division 08 has: 7 door lines (sliding glass, solid-core wood with welded frame, solid-core with knock-down frame, three storefront entrance lines), 1 roof hatch, 9 hardware-set lines (sets 1, 3, 4, 6, 7, 9, 10, 11, 14), 1 specialty frame (3.82 LF), 6 window tags, and 3 storefront SF lines (`reference/estimate/lines.json`, lines 190 to 216). The in-repo engine's own notes state that it reproduces door openings, leaves, frames and hardware sets exactly by type, and exterior storefront within 0.05% (`TakeoffSpeed repo: docs/QUANTITY_ENGINE.md`). I did not re-test that claim.

## Sources

Web pages read (each was fetched and read; only the facts tagged [W] come from them):
- Steel Door Institute glossary: https://steeldoor.org/glossary/
- SDI ANSI/SDI standards list: https://steeldoor.org/ansi/
- SDI Technical Data Series list: https://steeldoor.org/tech_data/
- SDI specification resources: https://steeldoor.org/specifications/
- DHI technical literature list: https://www.dhi.org/Resources/Technical-Literature
- BHMA A156 list: https://buildershardware.com/ANSI-BHMA-Standards/Hardware-Highlights
- BHMA finish lookup page: https://buildershardware.com/ANSI-BHMA-Standards/BHMA-Finish-Code-Lookup
- ADA Standards (Access Board), section 404: https://www.access-board.gov/ada/
- Wikipedia, curtain wall: https://en.wikipedia.org/wiki/Curtain_wall_(architecture)
- Wikipedia, fire door: https://en.wikipedia.org/wiki/Fire_door
- Wikipedia, panic bar: https://en.wikipedia.org/wiki/Panic_bar

Job documents: `source/specifications.pdf` (text at `text/spec-p212.txt` to `spec-p262.txt`), `text/A-600.txt`, `reference/estimate/lines.json`, `reference/markups/legends.json`, `reference/sheets/spec_index.json`.

Not found or not usable: manufacturer storefront installation data (Kawneer, YKK), GANA/NGA Glazing Manual, AAMA SFM-1, ASTM C1193, DHI hinge-quantity text, SDI A250.8 and A250.11 text, RSMeans conventions, access hatch manufacturer data, IBC chapter 10 (403/404 responses or empty pages). These gaps are where the [G] claims sit and where the next research pass should start.
