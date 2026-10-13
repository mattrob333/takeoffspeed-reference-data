# Division 10 specialties: toilet accessories, signage, fire extinguishers and cabinets, panels. Takeoff best practice

Scope: quantities and material types only. No pricing, labor or productivity.

How to read the citations:

- `[ADA]` is the 2010 ADA Standards text at <https://www.access-board.gov/ada/>.
- `[ADA-G6]` is the Access Board guide, <https://www.access-board.gov/ada/guides/chapter-6-toilet-rooms/>.
- `[ADA-G7]` is the Access Board guide, <https://www.access-board.gov/ada/guides/chapter-7-signs/>.
- `[OSHA]` is <https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.157>.
- `[UFGS-1028]` is the federal guide spec UFGS 10 28 13 Toilet Accessories, <https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2010%2028%2013.pdf>.
- `[UFGS-1044]` is UFGS 10 44 16 Fire Extinguishers (Nov 2019), <https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2010%2044%2016.pdf>.
- `[IFC-GA]` is the Georgia amendments to IFC 2018 Chapter 9, <https://up.codes/viewer/georgia/ifc-2018/chapter/9/fire-protection-systems>.
- `[WIKI-FE]` is <https://en.wikipedia.org/wiki/Fire_extinguisher>.
- Paths under `/home/user/...` are project files from this reference repo, not web sources.
- `[UNVERIFIED-GPT]` marks a statement from the GPT-6 Astra second opinion (`tools/ask_gpt.py`) that I could not tie to a fetchable public page. Treat it as a lead to confirm against the standard, not as a citation.

Research limits. The web-search budget ran out after the first attempts, so every web source here came from direct page fetches of known authoritative URLs. I found no fetchable RSMeans, CSI or estimator-blog page. The "what an estimator lists" and "common mistakes" sections therefore rest on the code and guide-spec sources plus this project's own ground truth. Where I could not cite, I say so.

---

## 1. What the estimator takes off, and in what unit

Almost all of Division 10 is counted. The unit is EA, keyed by schedule tag and size, per room. Only a few items are measured.

| Item family | Unit | Basis |
|---|---|---|
| Toilet accessories (dispensers, grab bars, mirrors, waste receptacles, napkin disposal, hooks, mop holder) | EA by tag and size | The specs require a product schedule "indicating types, quantities, sizes, and installation locations by room" ([project spec 10 2800 §1.2.B, text/spec-p335.txt](file://text/spec-p335.txt); same wording in [UFGS-1028](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2010%2028%2013.pdf)). |
| Grab bars | EA by length | Each bar has its own length (18 in vertical, 42 in horizontal, 36 in rear). Never lump them as "grab bars". |
| Tactile/ADA signs | EA by sign type, size and message | Designation signs for permanent rooms and spaces, and exit-door signs, need tactile characters ([ADA §216.2, §216.4.1](https://www.access-board.gov/ada/); [ADA-G7](https://www.access-board.gov/ada/guides/chapter-7-signs/)). |
| Fire extinguisher cabinets (FEC) | EA by type: recessed, semi-recessed or surface; trim style; door style | Project spec 10 4413 §2.2 (spec-p340). |
| Fire extinguishers | EA by rating and size | Project spec 10 4416 §2.2.B: 10-lb 4-A:60-B:C multipurpose dry chemical (spec-p345). |
| Extinguisher mounting brackets | EA | Spec 10 4416 §2.3, for extinguishers not in cabinets. |
| Panel systems (decorative or screen) | SF of face area, per tag | This project: PNL-1, 36 SF on A-706. |

Items that look like specialties but belong to other trades or lines:

- **Coat hook TA-09** is scheduled on the toilet-accessory schedule but says "REFERENCE DOOR HW SCHEDULE" (text/A-410.txt). The hooks are carried in the hardware set that schedule points to (A-601 set 11.0: "2 COAT HOOK RM817 US26D RO" per door, doors 112 and 113 = 4). Keep the TA-09 plan count (2) only as a cross-reference and flag it as a likely duplicate of the hardware set; do not carry it as a second Div 10 quantity. On this job the estimator carried both (line 327 = 2 and line 205 hardware set 11 × 2 doors).
- **Exit signs and the building identification sign** are electrical or site items. Do not count them as Div 10 tactile signs.
- **Occupant-load, Knox box and other life-safety plaques** are small counts keyed by symbols on G-001 (M.C.#, K.B.).

## 2. Sheets and spec sections that drive the trade

Project-specific, from the drawings and specs in this repo:

- **A-410 Enlarged restroom plans and elevations.** Holds the Toilet Accessory Schedule (TA-01 to TA-10, with TA-07 absent from the schedule), the typical accessible-accessory heights, restroom elevations A to D, and the janitor closet elevation. The schedule also says which items are "OWNER VENDOR PROVIDED, GC TO INSTALL, GC TO ORDER".
- **G-001 Life safety plan.** Holds the symbol legend (F.E., F.E.C., T.S. tactile signage, M.C.# maximum-capacity sign, K.B. Knox box). Its table reads "FIRE EXTINGUISHERS (906.1) … PER 906.3 / PROVIDED 2". It gives the building area (1,892 SF) and the occupant-load basis (1,900 GSF at 1 per 150 GSF).
- **G-002** has the tactile-sign details and mounting rules. Detail 2 draws three 6" × 4" messages (EXIT, TO EXIT, EXIT ROUTE) and a 2" × 8" vertical alternate.
- **A-110 floor plan** carries the 2 FEC placements; **A-120** has the FEC legend entry only.
- **A-706 Booth enlarged plan and details** is the source for PNL-1, the Big Apple Visual Group double-sided panel with a repeating pattern and hardwood blocking filler on both sides. The 13/16" PL-1 laminate on Z-clips, plywood substrate and 16-gauge studs on details 7/8/9 are the PL-1 booth walls, carried in other trades.
- **Specs.** 10 2800 Toilet Accessories (pages 335–337; 338 is blank), 10 4413 Fire Extinguisher Cabinets (339–343) and 10 4416 Fire Extinguishers (344–346), indexed in reference/sheets/spec_index.json. There is no signage section in the spec index. Signage scope therefore comes only from the drawings (G-001, G-002, finish and door schedules).

General rule behind this list: the schedule is the contract. Plan and elevation dots locate the items; the spec supplies the product, material and mounting requirements.

## 3. Standard measurement rules

### 3.1 Counting rules

1. **Count tag dots, then expand by the elevation.** One tag symbol can stand for several physical pieces. On this job the markup shows TA3 at 2 locations, but the estimate carries 2 vertical 18 in bars plus 2 horizontal 42 in bars, which is 4 pieces. The expansion comes from the elevations, not from the plan dot.
2. **Reconcile plan, elevation and schedule. Do not sum them.** The same item appears on the plan, on elevation views and in the schedule. Pick one primary source (plan dots, with the schedule for descriptions) and use the others as a check. [UNVERIFIED-GPT]
3. **Do not assume a fixed number of grab bars per stall.** ADA §604.5 requires a side-wall bar and a rear-wall bar at a water closet, but a third bar, or a vertical bar, comes from the project detail ([ADA-G6](https://www.access-board.gov/ada/guides/chapter-6-toilet-rooms/)).
4. **Count combination units as one assembly** unless components are scheduled separately. [UNVERIFIED-GPT]
5. **Carry the furnish/install split on the line.** Quantity does not change when the owner supplies the item. The line must say who furnishes and who installs, and A-410 states it per item.
6. **Count cabinets and extinguishers separately.** A cabinet does not include its extinguisher, and an exposed bracket replaces a cabinet rather than adding to it (spec 10 4416 §2.3, §3.2; [UFGS-1044](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2010%2044%2016.pdf)). On this job spec 10 4413 refers the extinguishers to 10 4416 (spec-p339). Cabinets = 2 F.E.C.; the 2 × 10 lb extinguishers are a separate record that the estimate does not carry (line 335 reads only "FIRE EXTINGUISHER CABINET"). Treat that as unresolved scope, not as "inside the cabinet line".

### 3.2 Panel systems

- Measure the face area from the elevation, as SF per tag. On this job the markup is 36 SF and the estimate line is 36 SF for PNL-1, described as a double-sided panel with blocking filler on both sides.
- Inference, not a stated rule: because the markup and estimate quantities match, the two faces are not doubled into 72 SF. The "both sides" wording describes construction, not a second measured quantity.
- Fabricated panel systems are ordered to size, so no field-cut waste is added unless the line is carried per sheet.

### 3.3 Deduct / don't deduct

There are no deductions in this trade. Items are counted, not netted. The one exception is panels measured by area: a deduction is needed only for an opening shown in the panel elevation.

## 4. Heights, clearances and placement rules that gate a count

These are not quantity multipliers, but a takeoff that ignores them miscounts or mis-specifies items.

**Grab bars ([ADA §604.5, §609](https://www.access-board.gov/ada/); [ADA-G6](https://www.access-board.gov/ada/guides/chapter-6-toilet-rooms/)):**

- Side-wall bar: at least 42 in long, at most 12 in from the rear wall, extending at least 54 in from the rear wall (§604.5.1).
- Rear-wall bar: at least 36 in long, extending at least 12 in on one side of the water closet centerline and 24 in on the other (§604.5.2). It may be 24 in minimum where a recessed fixture limits wall space.
- Height: 33 to 36 in above the floor, measured to the top of the gripping surface (§609.4).
- Wall clearance: 1½ in between wall and bar (§609.3).
- Round bar diameter: 1¼ to 2 in (§609.2.1).
- Strength: must withstand 250 lbf (§609.8). The project spec repeats this: 250 lbf per ASTM F 446 (spec 10 2800 §3.1.B).

**Dispensers and operable parts ([ADA §604.7, §308](https://www.access-board.gov/ada/)):**

- Toilet-paper dispenser centerline: 7 to 9 in in front of the water closet; outlet 15 to 48 in above the floor; not behind grab bars.
- Reach range: 15 in minimum low, 48 in maximum high for unobstructed forward or side reach (§308.2.1, §308.3.1).

**Mirrors, hooks and shelves ([ADA-G6](https://www.access-board.gov/ada/guides/chapter-6-toilet-rooms/); [ADA §603.3, §604.8.3](https://www.access-board.gov/ada/)):**

- Mirror above a lavatory or counter: bottom edge at most 40 in above the floor. Other mirrors: at most 35 in.
- Only one mirror in a toilet room must comply.
- Coat hooks: within a §308 reach range. Shelves: 40 to 48 in above the floor.
- Accessible compartment: at least 60 in wide measured perpendicular to the side wall (§604.8.1.1).

**Protrusion ([ADA §307.2](https://www.access-board.gov/ada/)):** a wall-mounted object with its leading edge between 27 in and 80 in above the floor may project at most 4 in into a circulation path. This applies to surface-mounted extinguishers, cabinets and dispensers in corridors.

**Tactile signs ([ADA §703.4](https://www.access-board.gov/ada/); [ADA-G7](https://www.access-board.gov/ada/guides/chapter-7-signs/)):**

- Mount at 48 in minimum to the baseline of the lowest tactile character and 60 in maximum to the baseline of the highest.
- Single door: on the latch side. Double doors with one active leaf: on the inactive leaf. Two active leaves: to the right of the door.
- Keep an 18 in by 18 in clear floor space centred on the sign, beyond the door swing.
- Raised characters: 5/8 in to 2 in high, 1/32 in minimum raised. Grade 2 braille below the text. The project line "5/8 in H × 1/32 in raised lettering, Grade 2 braille" matches this.
- Which signs: permanent room and space designations, and exit-passageway, exit-discharge and exit-stair doors (§216.2, §216.4.1). Directional and informational signs need not be tactile (§216.3).

**Fire extinguishers:**

- Federal workplace rule: Class A extinguishers within 75 ft travel distance, Class B within 50 ft ([OSHA 1910.157(d)](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.157)).
- Mounting height: top of extinguisher at most 60 in AFF for units 40 lb or less, and at most 42 in for heavier units ([UFGS-1044](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2010%2044%2016.pdf), quoting NFPA 10). The ADA operable-part limit of 48 in to the handle is a separate check ([UFGS-1044](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2010%2044%2016.pdf); [WIKI-FE](https://en.wikipedia.org/wiki/Fire_extinguisher)).
- This project's spec sets the bracket at 54 in AFF to the top of the extinguisher (spec 10 4416 §3.2.A, spec-p346).
- Georgia deletes IFC 906.3 to 906.10 and defers to NFPA 10 for selection, distribution and installation ([IFC-GA](https://up.codes/viewer/georgia/ifc-2018/chapter/9/fire-protection-systems)). The drawings still show the result: G-001 states 2 provided.

## 5. Coverage, yield and waste factors

### 5.1 Extinguisher quantity from area

Two sources disagree, and the difference matters when you check a designer's count.

- The federal guide spec note (UFGS 10 44 16, Nov 2019) gives the older rule: light hazard, one 1-A unit per 3,000 sq ft within 75 ft travel; ordinary hazard, one 2-A unit per 3,000 sq ft within 75 ft; extra hazard, one 3-A unit per 3,000 sq ft within 75 ft ([UFGS-1044](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2010%2044%2016.pdf)).
- Second opinion for current NFPA 10 Table 6.2.1.1 `[UNVERIFIED-GPT]`:

| Hazard | Min single rating | Max sq ft per unit of A | Max sq ft per extinguisher | Max travel |
|---|---|---|---|---|
| Light | 2-A | 3,000 | 11,250 | 75 ft |
| Ordinary | 2-A | 1,500 | 11,250 | 75 ft |
| Extra | 4-A | 1,000 | 11,250 | 75 ft |

Verify this table against the NFPA 10 edition adopted in Georgia before relying on it. I could not fetch the NFPA text.

**Worked check for this job** (calculated in Python): the building is 1,892 SF (G-001). Under either table, one extinguisher covers the area by floor area alone (6,000 / 3,000 / 4,000 SF for light, ordinary and extra using the unverified table). The 75 ft walking-distance rule and the code review are what drive the design count of 2. Area division alone would give 1, so area is a floor, not the answer.

### 5.2 Waste and overage

- Countable items (accessories, signs, extinguishers, cabinets): 0% waste. Spare quantities are added only when the spec requires them, as a stated number, not a percentage. `[UNVERIFIED-GPT]` Neither project spec section (10 2800, 10 4413, 10 4416) calls for attic stock or spares.
- Panels cut from sheet stock: layout waste is the estimator's judgment. The 5 to 10% preliminary allowance in the second opinion has no source I could verify. Fabricated panels (PNL-1) carry none.
- Do not carry a general "waste" line on Div 10 counts. Waste exists only as a spec-required spare or a sheet-cut allowance.

## 6. Material breakdown an estimator lists

**Toilet accessories (per tag):**

- The accessory unit itself, with model and finish from the schedule. Here: Bradley 1¼ in stainless grab bars, Bobrick B-3644 recessed waste receptacle, B-290 mirror with stainless angle frame, B-270 surface sanitary-napkin disposal, B-223×24 mop holder.
- Owner-vendor-provided items (TA-01 tissue, TA-02 towel and TA-05 soap dispensers): count them, but mark them furnished by owner, installed by GC. TA-09 coat hook is not owner-vendor: the schedule defers it to the door hardware schedule (A-601 set 11.0, RM817 US26D).
- Fasteners and anchors. Spec 10 2800 §2.1.E requires tamper- and theft-resistant fasteners where exposed and galvanized where concealed.
- Blocking or backing in stud walls. The guide spec requires fastening to studs, blocking or rough frame in wood; to metal studs with sheet-metal screws; and, for surface-mounted units on gypsum board without solid backing, into the studs or to backplates secured to metal studs ([UFGS-1028 §3.1](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2010%2028%2013.pdf)). Recessed units need a rough opening and wall depth. B-3644 is "FOR 4" WALLS" on A-410.
- Mirrors: ASTM C 1503, 6.0 mm clear glass (spec 10 2800 §2.1.F).
- Stainless steel: ASTM A 666 Type 304, 0.031 in minimum (spec 10 2800 §2.1.A).
- Each accessory item typically includes its universal key (spec 10 2800 §2.3.B). Keys are not a separate takeoff line.

**Signage:**

- The sign by type, size and message (6×4 tactile, 6×9 ADA men and women restroom signs).
- Mounting hardware or adhesive per the sign detail. This is not itemized unless the sign schedule does so.

**Fire protection specialties:**

- FEC: steel box, stainless trim and door, clear acrylic glazing, recessed, with "FIRE EXTINGUISHER" lettering applied to the door glazing (spec 10 4413 §2.2).
- Extinguisher: 10-lb multipurpose dry chemical, 4-A:60-B:C (spec 10 4416 §2.2.B). Rating notation: the number before A times 1.25 gives gallons of water equivalent, and the number before B is the Class B fire area in sq ft ([WIKI-FE](https://en.wikipedia.org/wiki/Fire_extinguisher)).
- Mounting bracket: only for bracket-mounted extinguishers, with red "FIRE EXTINGUISHER" decals (spec 10 4416 §2.3.B).
- A cabinet and a bracket for the same extinguisher is a double count. [UNVERIFIED-GPT]

**PNL-1 panel system:** Big Apple Visual Group booth screen panel system (A-170), double-sided with a repeating pattern, with hardwood blocking filler on both sides (A-706 details 4 and 8; estimate line 336). The 13/16 in PL-1 laminate panels on Z-clips, the plywood substrate and the 16-gauge studs at 16 in o.c. called out on details 7/8/9 are the PL-1 booth walls, not PNL-1; they are carried in other trades.

## 7. Cross-check against this job's ground truth

All quantities below come from `reference/estimate/lines.json` (lines 322–336) and `reference/markups/legends.json`. No prices are used.

| Item | Markup (dots) | Estimate | Note |
|---|---|---|---|
| TA1 tissue dispenser | 2 | 2 EA | match |
| TA2 paper towel dispenser | 2 | 2 EA | match |
| TA3 grab bars | 2 dots | 2 × 18 in vertical + 2 × 42 in horizontal | 2 locations expand to 4 pieces |
| TA4 recessed waste receptacle | 2 | 2 EA | match |
| TA5 soap dispenser | 2 | 2 EA | match |
| TA6 mirror 2×3 ft | 2 | 2 EA | match |
| TA8 sanitary napkin disposal | 1 | 1 EA | match |
| TA9 coat hook | 2 | 2 EA | match, but hardware set 11.0 (line 205) also carries 4 RM817 hooks: likely duplicate |
| TA10 mop holder | 1 | 1 EA | match |
| Tactile signs (6×4) | 3 | 3 EA | G-001 |
| ADA men / women restroom signs (6×9) | 1 / 1 | 1 / 1 EA | G-001 |
| Fire extinguisher cabinet | not a dot-count page | 2 EA | matches the "2 provided" in G-001 |
| PNL-1 panel | 36 SF | 36 SF | A-706 |

Totals, calculated in Python: 16 tag dots on the TA markup page against 18 estimate pieces. The 2-piece difference is the TA3 expansion (2 dots to 4 bars).

Two observations for the engine:

1. The estimate has a FEC line (2 EA) but no extinguisher line, although spec 10 4416 §2.2 requires a 10-lb 4-A:60-B:C unit per cabinet. This could be an estimate omission or an item bought elsewhere. A takeoff should list both and flag it.
2. TA-07 is missing from the schedule (it jumps from TA-06 to TA-08). Flag the gap; do not invent an item.

## 8. Common mistakes and how to check a takeoff

1. **Counting tag dots without expanding the tag.** TA3 is the clearest example here (2 dots, 4 bars). Check every tag against its elevation.
2. **Adding plan, elevation and schedule counts together.** They describe the same items. Cross-check, do not sum. `[UNVERIFIED-GPT]`
3. **Dropping owner-furnished items.** The installation scope is still the GC's. Carry the quantity with the furnish/install note.
4. **Missing items that live outside the toilet-accessory sheet:** coat hook (hardware schedule), tactile signs (G-001 symbols), FECs (G-001 and A-110 floor plan symbols; A-120 legend only).
5. **Cabinet without extinguisher, or both cabinet and bracket.** See section 6.
6. **Treating signs as one lump.** Size, message and tactile/braille content are separate lines.
7. **Ignoring backing.** Grab bars need 250 lbf support (spec 10 2800 §3.1.B; [ADA §609.8](https://www.access-board.gov/ada/)). Confirm the framing takeoff carries blocking at every bar and recessed-unit location.
8. **Over-applying waste.** Countable specialties carry none unless the spec requires spares.
9. **Wrong sign scope.** Only permanent room and exit-door signs need tactile characters; directional signs do not ([ADA §216](https://www.access-board.gov/ada/)).
10. **Trusting a single extinguisher-area rule.** Check travel distance (75 ft) as well as floor area, and check which NFPA 10 edition the jurisdiction adopted.

Checks to run, each reproducible in a script:

- Sum of dots per tag equals the sum of pieces per tag divided by pieces-per-tag from the elevation.
- Every schedule tag has at least one plan dot, and every plan dot has a schedule entry. Report gaps (TA-07 here).
- FEC count equals the "provided" count in the G-001 extinguisher table, and an extinguisher or bracket exists for each.
- Sign count by type equals the T.S./room-sign symbols on the plans.

## 9. What an AI takeoff must read from the drawings and specs

1. **A-410 schedule and elevations:** every tag, its product, size, mounting type (recessed, surface), finish, and the furnish/install note. Read the elevations to find how many pieces each tag expands to, and the mounting heights.
2. **Plan symbols across all floor plans:** tag circles (TA-n), FEC and F.E. symbols, T.S. symbols. Count by symbol, then deduplicate against enlarged plans, because the same restroom appears on a floor plan and an enlarged plan.
3. **G-001 legend and life-safety table:** the number of extinguishers provided, the extinguisher rating (legend 10 lb 4A:80B:C; flag the conflict with spec 10 4416, 4-A:60-B:C), and the sign symbols.
4. **G-002:** sign mounting height and location rules (48 to 60 in, latch side, 18 × 18 clear floor space).
5. **Door hardware schedule:** items such as coat hooks that are scheduled outside Div 10.
6. **Spec sections 10 2800, 10 4413, 10 4416:** products and materials, mounting requirements (54 in bracket height, 250 lbf grab bars), keys, and whether spares or attic stock are required.
7. **Detail sheets for panels (A-706):** face dimensions, single- or double-sided, substrate, framing.
8. **What not to invent:** if a tag is missing from the schedule (TA-07), a spec section does not exist (no signage section), or an extinguisher count is not stated, report the gap. Do not fill in a number.

---

## Source-quality notes

- ADA 2010 Standards text and Access Board guides: primary, authoritative.
- OSHA 29 CFR 1910.157: primary, but it states only travel distances, not unit counts.
- UFGS guide specs: authoritative federal guide specifications. They are not the building code. The extinguisher-sizing note is older than the current NFPA 10 table.
- Georgia IFC amendments (up.codes viewer): confirms that Georgia defers to NFPA 10, but the NFPA 10 table itself was not retrievable.
- Wikipedia: secondary, used only for rating notation and the 48 in handle limit.
- Not found: RSMeans or other published estimating conventions for Div 10, manufacturer coverage data (Bobrick/Bradley installation sheets), and an NFPA 10 primary-text excerpt. A follow-up with more web-search budget should close these three.
