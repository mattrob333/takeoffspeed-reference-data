# Trade 32a - Pavement, sidewalk, ramp, curb, marking, signs, bike racks, bollards: takeoff best practice

Scope: quantities and material types only (no pricing, no labor). Written 2026-10-13 for the single-storey bank branch reference job (Warner Robins, GA).

**Sourcing note.** WebSearch quota was exhausted mid-task, so sources were found by direct fetch of known authoritative pages. Every claim below carries a link to a page that was actually fetched and read. Claims that could not be sourced are tagged **[UNSOURCED]** and are kept only because the TakeoffSpeed engine or the reference estimate uses them; confirm before relying on them. Items the job's own drawings prove are cited to the sheet. A GPT second opinion was used only to suggest candidate URLs (each was then fetched and verified), never as a citation.

---

## 1. What the estimator takes off, and in what unit

| Item | Takeoff unit | Notes |
|---|---|---|
| Demolition of existing pavement, sidewalk, ramp | SF (SY by some DOTs) | Separate line per surface type; striping on pavement is included in the pavement demo line (job: C-1.0 key 7). |
| Demolition of curb and gutter | LF | Job: key 1. |
| Asphalt pavement, by duty (heavy / standard) | SF measured, then SY x inches -> TON for ordering | One line per duty; courses (surface / binder / base) derive from the same area. |
| Aggregate base / subbase | CY compacted (SF x depth) -> TON | Under asphalt and under concrete; separation geotextile in SF/SY. |
| Concrete pavement (heavy-duty, dumpster pad) | SF measured, CY derived | Thickness from detail; reinforcement as separate lines. |
| Concrete sidewalk | SF, CY derived | 4 in per C-6.0; thicken where walk abuts roadway with no curb. |
| Sidewalk joints | LF (expansion) and count/LF (control) | Spacing from detail. |
| ADA / curb ramps with detectable warning | SF (or EA) | Detectable warning is its own line (SF or EA by product). |
| Curb and gutter (and flume, valley) | LF, by type | Cross-section area / 27 gives CY per LF. |
| Pavement marking: lines, stop bar, crosswalk | LF by width | Paint volume converts from area. |
| Pavement marking: symbols, arrows, ADA symbol | EA | |
| Signs | EA, with post, footing, hardware | Footing CY separate. |
| Bike racks | EA, with footings/anchors | |
| Bollards | EA, with pipe, concrete fill, footing, cover/paint | |
| Wheel stops | EA, with pins | |
| Transformer / cleanout / equipment pads | SF, CY | Often hiding in this section (job lines 657-658). |

## 2. The reference job (ground truth, quantities only)

From `reference/estimate/lines.json` and `reference/markups/legends.json` (page 64 = C-1.0, page 72 = C-3.0, page 89 = A-401):

- Demo (C-1.0): curb and gutter 987.2 LF; existing pavement with striping 19,363.6 SF; sidewalk 390.2 SF; concrete ramp 442.4 SF; monument sign 1 EA.
- Heavy-duty asphalt 11,367.3 SF (1.5 in surface + 3 in binder + 4 in base + 12 in subbase + separation geotextile, "assumed details"); standard-duty asphalt 2,459.2 SF (1.5 in + 3 in + 12 in subbase + geotextile).
- Heavy-duty concrete pavement 6 in: legend shows two rows, 241.8 SF (key 21) + 505.8 SF (key 18) = 747.6 SF; estimate carries 748.0 SF. The dumpster slab (same key 21, 384.3 SF, purple row on the same page-72 legend; detailed on A-190) is a separate line (663, trade 32b).
- Sidewalk 4 in, 6x6-W2.9xW2.9 WWF, 3000 psi: 1,835 SF. ADA ramp with detectable warning 114 SF. Curb and gutter 6 in x 12 in curb with 18 in gutter on 4 in graded aggregate base: 994 LF.
- Marking: 4 in solid white 441.3 LF; blue 45-degree stall hatching 97.5 LF (two coats); 24 in stop bar 49.6 LF; striped crosswalk 79.5 LF; 3 ft x 3 ft ADA symbol 1 EA; arrows 2 EA.
- Signs: ADA R7-8 + van plaque 1 EA, R1-1 STOP 3 EA, Do Not Enter 2 EA, monument sign 1 EA (by others). Footings: 12 in dia x 3.5 ft x 1; 8 in dia x 3 ft x 5.
- Bike racks 2 EA with four 12 in dia x 1 ft footings. Bollards: 5 at dumpster (C-3.0 count; A-190 plan shows 6) on 16 in dia x 3 ft footings, where the 3 ft depth is an estimator assumption because A-190 gives no pier depth; and 8 at drive-thru (A-401, 16 in dia x 4 ft footings, 4 ft being the nominal 48 in pipe embedment; the detail adds 3 in of fill below the pipe).
- Expansion joint line: 73.4 LF = 1,835 SF / 25. This is the length of the transverse 1/4 in expansion joints at the 25 ft maximum spacing: a walk of width W gets SF/W/25 joints, each W long, so LF = SF/25 and the width cancels (formulas.md F4). The 5 ft contraction/control joints are a separate item that the estimate does not carry; on a 5 ft walk they would be about 1,835 / 5 = 367 LF.

Cross-check: the legend and estimate agree to within rounding (asphalt 11,367.3 / 11,367.3; sidewalk 1,834.7 / 1,835; curb 993.9 / 994; ramp 113.3 / 114). Python check of the tonnage convention in section 5: HD asphalt at 110 lb/SY-in = 104.2 / 208.4 / 277.9 tons for the 1.5 / 3 / 4 in courses; standard duty = 22.5 / 45.1 tons for 1.5 / 3 in.

**There is no Division 32 specification section in this job's spec book.** `spec_index.json` lists 03, 05 and 10 sections and 313116 (termite) only. Pavement requirements live in the civil drawings (C-1.0, C-3.0, C-6.0 details and notes), plus A-190 and A-401 for bollards. An AI that waits for a spec section will find nothing; it must read the detail sheets.

## 3. Sheets that drive it

- **Civil site plan (C-3.0)**: keynoted pavement areas, curb lines, ramps, striping, signs, bike racks, dumpster bollards, monument sign. Legend rows with keynote numbers tie to quantities.
- **Demolition plan (C-1.0)**: what to remove, with its own keynotes.
- **Construction details (C-6.0, 6.1-6.3)**: sidewalk, curb and gutter, ADA parking, ADA symbol, ADA sign, traffic sign, stop bar, pavement-marking arrows, wheel stop, flume, V-notch/taper curb, bollard. Detail notes carry thicknesses, joint spacings, concrete strength, reinforcing and finish.
- **Architectural trash enclosure (A-190) and bank equipment plans (A-401)**: bollard schedules and footing sizes that differ from the civil bollard detail (C-6.0 shows a 6 in pipe in a 24 in dia footing; A-190 and A-401 show 16 in dia fill; A-190 gives no pier depth, and A-401 adds 3 in of fill below the 48 in pipe embedment). Which governs per location is a judgment the AI must surface rather than guess.
- **Pavement section**: the 4 in / 3 in / 1.5 in course stack here is labelled "ASSUMED DETAILS" in the estimate. The keynotes send the reader to C-6.2 (which has no section), but the C-3.0 Pavement Legend says "SEE GEOTECH REPORT BY TERRACON, DATED 05.04.2026" for both pavement types, so the geotech report (`source/drawings/GeoTechnical`) is the referenced design section. Read the legend references as well as the keynotes, and flag any assumed stack that ignores them.
- **Life-safety / floor-plan sheets**: interior signage is not this trade (it lives in Division 10), although it also reads as "sign".

## 4. Standard measurement rules

### Areas and lengths
- Measure paving to the face of curb or edge of pavement as drawn, per keynote, by surface type and by duty. Do not merge heavy and standard duty, or asphalt and concrete, because courses, bases and reinforcing differ. Evidence: job legend splits C-3.0 into keyed rows and the estimate carries them as separate lines.
- Measure curb and gutter in LF along the face of curb. Cross-section area (SF) / 27 gives CY per LF; use the type-specific section from the detail. FDOT standard sections show multiple types (A, B, D, E, F, valley, shoulder, drop curb) with different widths and lips, so confirm the type before applying a section. Source: [FDOT Index 520-001](https://www.fdot.gov/docs/default-source/design/standardplans/2024/idx/520-001.pdf).
- Concrete volume = length x width x thickness (ft) / 27. [Concrete Network](https://www.concretenetwork.com/concrete/howmuch/). The same page gives a 4 in shortcut (SF / 81) and advises adding 1/4 in to the slab thickness "assuming a well graded, compacted subgrade". Check on this job: 1,835 SF x 4 in = 22.65 CY; at 4.25 in = 24.07 CY.

### Joints (these produce LF quantities and drive panel layout)
- General slab rule: contraction joint spacing 24 to 36 times slab thickness, never over 15 ft; panels square or nearly so, length no more than 1.5 times width; groove at least 1/4 thickness (and at least 1 in); wire mesh should be discontinued at contraction joints; use preformed isolation filler where slabs meet walls or footings. [NRMCA CIP 6](https://www.nrmca.org/wp-content/uploads/2021/01/06pr.pdf).
- Sidewalk (FDOT standard): dummy/tooled or saw joints at 5 ft maximum centers, an expansion joint when a run exceeds 120 ft, expansion joint (preformed filler) between the sidewalk and driveways, drainage inlets and other fixed objects; 6 in concrete at driveways, 4 in elsewhere. [FDOT Index 522-001](https://www.fdot.gov/docs/default-source/design/standardplans/2024/idx/522-001.pdf).
- Curb and gutter (FDOT standard): contraction joints at 10 ft maximum centers; expansion joint with preformed filler between curb and concrete pavement; avoid sawcuts in valley gutters and at curb endings. [FDOT Index 520-001](https://www.fdot.gov/docs/default-source/design/standardplans/2024/idx/520-001.pdf).
- **Job-specific, from sheet C-6.0 (read from the rendered sheet; verify before use)**: sidewalks 4 in thick; control joints every 5 ft for 5 ft walks; for 10 ft walks, 5 ft intervals plus a longitudinal joint at the centerline; control joints 1 in deep, edged 1/8 in radius; 1/4 in expansion joints at structures with a maximum 25 ft spacing; 1/2 in expansion material where the walk meets concrete structure; a layer of 15# felt between walk and adjacent curb; thicken to 6 in within 3 ft where the walk abuts a roadway with no curb; 6x6-W2.9xW2.9 WWF on subgrade compacted to 98 percent standard Proctor; 3000 psi, 2 in slump, broom finish. Curb and gutter detail: 3000 psi high-early concrete, expansion joints at all structures and curb returns, control joints at 25 ft maximum, 4 in graded aggregate base (also on the estimate line).

### Reinforcement
- Welded wire reinforcement is bought in sheets (stock widths 5 to 10 ft, lengths 10 to 20 ft) or rolls (5 to 7 ft wide, 150 to 200 ft long). 6x6-W2.9xW2.9 weighs 0.42 lb/SF (42 lb per 100 SF). [WRI TF 202](https://wirereinforcementinstitute.org/download_file/571).
- Laps: the WRI detail for plain welded wire in slab-on-ground calls for a 2 in minimum lap splice, measured between wire centerlines, and defers to the licensed designer. [WRI WWR.2](https://wirereinforcementinstitute.org/download_file/view/354). The engine's "one mesh spacing plus 2 in" lap is consistent with this but the one-mesh part is **[UNSOURCED]** here. Check on this job: 1,835 SF in 5 ft x 10 ft sheets with 2 in laps each way gives about 38.6 sheets at 47.5 net SF each, about 771 lb of mesh (1,835 x 0.42).

### Asphalt
- Estimating paving tonnage from width, length and compacted thickness is the NAPA-endorsed method (see the NAPA [Mix Quantity calculator](https://www.asphaltpavement.org/resources/calculators/mix-quantity-economic-impact/); the page describes the inputs but the density constant sits in a spreadsheet that could not be read here).
- Compaction context: rollers finish at about 92 to 95 percent of theoretical maximum density; a lift should be at least twice the maximum aggregate size and a rule of thumb is three times nominal maximum aggregate size. [Pavement Interactive - Compaction](https://pavementinteractive.org/reference-desk/construction/compaction/), [Placement](https://pavementinteractive.org/reference-desk/construction/placement/). This is why lift thickness (1.5 in for 9.5 mm, 3 in for 19 mm, 4 in for 37.5 mm) must be taken from the course-by-course section, never from a total depth divided evenly. Python check: 1.5 / 3 / 4 in lifts on 9.5 / 19 / 37.5 mm mixes are about 4.0x, 4.0x and 2.7x the nominal maximum aggregate size, so each is at least twice NMAS as the source requires.

### Marking
- Longitudinal lines: normal line is 4 to 6 in wide; wide line is at least twice normal width; double line is two parallel lines. [MUTCD 11th Ed. Part 3, Section 3B.](https://mutcd.fhwa.dot.gov/pdfs/11th_Edition/part3.pdf) A double line is two LF per LF of roadway.
- Stop line: solid white, 12 to 24 in wide (Section 3B.19). Crosswalk lines: white, transverse lines 6 to 24 in wide; marked crosswalk at least 6 ft wide (8 ft at non-intersection locations with 40 mph or more) (Sections 3C.03). Parking space markings: white; blue lines may supplement for accessible spaces (Section 3B.27). Same MUTCD Part 3 link.
- Convert LF of line to area by width (24 in stop bar: 49.58 LF x 2 ft = 99.2 SF) before computing paint.
- The job's own notes (C-6.0) say stall lines are "two coats" (blue 45-degree lines and white stall lines) and that the stop-bar detail is "for private on-site use". Two coats doubles the paint volume for those lines.
- **No DOT measurement-and-payment page was retrievable** (TxDOT hosts returned 503). Standard practice, **[UNSOURCED]**: lines by LF (double line counts both lines), broken lines by LF of stripe (not of gap), symbols/arrows/legends by EA, crosswalk and stop bar by LF at stated width or SF.

### Signs
- Mounting height: 7 ft minimum from bottom of sign to top of curb in business and residential areas (5 ft in rural areas); 7 ft over a sidewalk. [MUTCD 11th Ed. Chapter 2A, Section 2A.15](https://mutcd.fhwa.dot.gov/pdfs/11th_Edition/Chapter2a.pdf).
- Sizes: R1-1 STOP 30 x 30 in (single lane) and 36 x 36 in (multi-lane); R5-1 DO NOT ENTER 30 x 30 in; R7-8 Reserved Parking 12 x 18 in; R7-8aP VAN ACCESSIBLE plaque 12 x 6 in. [MUTCD Chapter 2B, Table 2B-1](https://mutcd.fhwa.dot.gov/pdfs/11th_Edition/Chapter2b.pdf). The R7-8 sign is required with the International Symbol of Accessibility; a van plaque goes below it where the space is van-accessible (same chapter, Section 2B.52).
- Accessibility sign height: bottom of the sign at least 60 in above the ground. [US Access Board ADA Standards 502.6](https://www.access-board.gov/ada/). The MUTCD 7 ft and the ADA 60 in are different tests; the more demanding one in the detail governs. Job detail C-6.0: 7 ft to sign bottom, 2 x 2 x 0.188 in steel tube extended 2 ft into a concrete-filled pipe, 8 in dia pipe, 3 ft 6 in minimum embedment; STOP sign on a 2 in galvanized channel with an 8 in dia minimum footing.

### Accessible parking, ramps and routes (drive quantities of striping, signs, ramps)
- Required accessible spaces by total spaces (1-25: 1; 26-50: 2; 51-75: 3; 76-100: 4; 101-150: 5; 151-200: 6; 201-300: 7; 301-400: 8; 401-500: 9; 501-1000: 2 percent; over 1000: 20 plus 1 per 100); at least one in every six accessible spaces must be van-accessible (208.2, 208.2.4). [ADA Standards](https://www.access-board.gov/ada/).
- Car space at least 96 in wide; van space at least 132 in (or 96 in with a 96 in aisle); access aisle at least 60 in wide and the full length of the space; slope no steeper than 1:48 in spaces and aisles (502.2 to 502.4). [ADA Standards](https://www.access-board.gov/ada/). See also the [Access Board parking guide](https://www.access-board.gov/ada/guides/chapter-5-parking/): one aisle may serve two spaces; 98 in vertical clearance at van spaces; no sign needed where the site has four or fewer spaces.
- Ramps and curb ramps: running slope not steeper than 1:12, clear width at least 36 in, rise per run not over 30 in (405.2, 405.5, 405.6); curb ramp flares not steeper than 1:10; top landing at least 36 in; ramps may not project into parking spaces or access aisles (406.3 to 406.5); detectable warning across the full ramp width, full depth or at least 24 in from the curb (406.8). [ADA Standards](https://www.access-board.gov/ada/).
- Detectable warning domes: base diameter 0.9 to 1.4 in; spacing 1.6 to 2.4 in center to center (705.1). [ADA Standards](https://www.access-board.gov/ada/). Takeoff consequence: count the full ramp width (excluding flares) x the greater of 24 in or the ramp depth; take the product's tile size from the submittal, not from the plan.
- Walking surfaces: running slope not steeper than 1:20, cross slope not steeper than 1:48, clear width at least 36 in (403.3, 403.5.1); changes in level up to 1/4 in vertical, 1/4 to 1/2 in beveled at no steeper than 1:2 (303). [ADA Standards](https://www.access-board.gov/ada/). Bollard layouts that leave less than 36 in clear on an accessible route fail this.

### Bike racks
- A typical bicycle footprint is about 6 ft x 2 ft; inverted-U and post-and-ring racks park one bicycle on each side. Holes drilled into existing concrete should be at least 3 in from edges or joints; asphalt is too soft for wedge or spike anchors so a freestanding or asphalt-specific anchor is needed; for new pads, embedded racks must be placed before pouring because they are hard to relocate. [APBP Essentials of Bike Parking](https://www.apbp.org/assets/docs/EssentialsofBikeParking_FINA.pdf).
- Takeoff consequence: count racks as EA and also take off the anchor type (surface flange with anchors vs embedded with footing). The job estimate carries two racks and four 12 in dia x 1 ft footings, so it assumed embedded posts.

### Bollards
- No authoritative embedment/spacing page could be fetched (the manufacturer pages returned 403). Use the job details: C-6.0 civil bollard detail (6 in dia x 0.28 in x 7 ft steel pipe filled with 3000 psi concrete, 24 in dia footing, 3 ft minimum exposed above the pavement, 4 ft minimum embedment from the pavement surface to the pipe bottom plus 3 in of concrete below the pipe, 1/2 in rebar through pipe, smooth concrete cap, 2 in sand cushion); A-190 (16 in dia concrete pier with no depth given, painted yellow; its general note requires a bollard cover on all painted steel pipe bollards, so the dumpster group takes a cover too); A-401 (6 in dia filled galvanized bollard with cover, 16 in dia concrete fill, pipe 48 in below grade plus 3 in of fill below the pipe, 4 ft exposed; bollard placement "drawn for reference, coordinate with ATM vendor").
- Footing volume = pi x (d/2)^2 x h / 27. Checks: 16 in dia x 4 ft x 8 = 1.65 CY (1.76 CY at the detailed 4 ft 3 in); 16 in dia x 3 ft x 5 = 0.78 CY (3 ft assumed); 12 in dia x 1 ft x 4 = 0.116 CY. Civil detail, 24 in dia x 4 ft x 5 = 2.33 CY (2.47 CY at 4 ft 3 in).

## 5. Coverage, yield and waste (with basis)

| Item | Factor | Basis / source |
|---|---|---|
| Traffic paint, 4 in line | 320 LF per gallon per coat at 15 mils wet (107 SF/gal; 9.1 mils dry) | [Sherwin-Williams Hotline TM2152](https://www.paintdocs.com/docs/webPDF.jsp?SITEID=STORECAT&lang=E&doctype=PDS&prodno=TM2152). Spreading rate is theoretical and includes no application-loss factor. |
| Traffic paint on new asphalt | not over 8 mils wet, about 200 SF/gal | Same data sheet: heavy films can lift or crack new asphalt. |
| Glass beads | dropped on wet paint to make reflective markings | Same data sheet confirms the method. Rate (engine uses 6 lb/gal) is **[UNSOURCED]**; take it from the spec. |
| Job paint check (python) | SSWL 441.3 LF = 1.38 gal (1 coat); blue/white stall lines 97.5 LF x 2 coats = 0.61 gal; stop bar 99.2 SF = 0.93 gal | Computed from the figures above. |
| HMA tonnage | tons = SY x inches x 110 lb/SY-in / 2000 (110 lb/SY-in = 146.7 lb/CF) | **[UNSOURCED]**; the 110 lb/SY-in constant is the engine's convention. NAPA publishes a calculator but its constant could not be read. Prefer the mix design's actual density. |
| Concrete volume | L x W x t / 27; add 1/4 in to thickness; never order exact | [Concrete Network](https://www.concretenetwork.com/concrete/howmuch/). A numeric waste percent (commonly 5 to 10) is **[UNSOURCED]**. |
| WWF | 0.42 lb/SF for 6x6-W2.9xW2.9; sheets 5-10 x 10-20 ft; 2 in minimum lap | WRI TF 202 and WWR.2 above. |
| Joint spacing | 24 to 36 x thickness, max 15 ft; sidewalk 5 ft; C&G 10 ft (FDOT) or per detail | NRMCA CIP 6 and FDOT 520/522 above. |
| Aggregate base | 1.9 ton/CY compacted (engine) | **[UNSOURCED]**. |
| Tack coat, prime, geotextile overlap | engine values 0.06 gal/SY tack, 0.25 gal/SY prime, 18 in overlap | **[UNSOURCED]** here (the engine cites FHWA and AASHTO documents that could not be opened). |

Waste guidance in one line: only the concrete thickness allowance, the WWF lap and the paint application-loss caveat are sourced. Percentages for asphalt, aggregate and sign hardware are not.

## 6. Material breakdown an estimator lists

**Asphalt pavement (per duty)**: surface, binder and base courses (TON, each from SY x course inches); tack coat between lifts; prime coat on aggregate base if the spec calls for it; aggregate subbase (CY or TON); separation geotextile (SF, with side laps); fine grade and compact subgrade (SF). Take the course thicknesses from the section.

**Concrete pavement / pads**: concrete CY, mesh or bars (SF or LB; laps and chairs), vapor barrier where specified (dumpster slab line shows 10 mil), joint filler/sealant (LF), curing compound, subbase.

**Sidewalk**: concrete CY at the detail thickness (plus thickened edges), WWF (sheets with laps), 1/4 in or 1/2 in expansion filler (LF), saw/tooled control joints (LF), aggregate bed if shown, broom finish.

**Curb and gutter**: concrete CY from the section, graded aggregate base (CY/TON), expansion filler at structures and returns, reinforcing dowels, forming for curved reaches, flume, V-notch and taper as separate items.

**ADA ramp**: concrete, WWF, detectable warning plates (SF or EA), flares, 15# felt or filler at curb, painted/handrail items if the ramp is a run rather than a curb ramp.

**Marking**: paint (gal, per coat), glass beads (lb), stencils/templates for symbols, thermoplastic or tape only if the spec says so, layout and surface preparation. Colors tracked separately: white, blue (accessible), yellow.

**Signs**: sign panel (by MUTCD code and size), van plaque, post (steel tube, galvanized channel, or U-channel), hardware (bolts, nuts, washers), concrete footing, excavation and haul-off of spoil (the estimate carries these as separate CY lines).

**Bike racks and bollards**: unit, footing concrete and rebar, excavation and haul-off, bollard cover/wrap, paint, sand cushion where detailed.

## 7. Common mistakes and how to check

1. **Missing the "hidden" items in other sections.** Pads, bollards, bike racks and signs appear in Div 32 lines but are drawn on A-190, A-401 and civil details. Check every sheet's keynote legend for unit and EA items, not just the area keynotes.
2. **Wrong duty or double counting.** Heavy-duty asphalt and heavy-duty concrete share a keynote word; the legend splits C-3.0 into keys 21 and 18 for concrete (241.8 + 505.8 SF). Sum keyed rows, then tie to the keyed polygon total.
3. **Using total depth for lifts.** Use the stated course thickness per course.
4. **Mixing units.** SF vs SY for paving; LF of line vs SF of stripe (24 in stop bar); expansion joint LF from area is SF / spacing (73.4 LF here), which is a length, not a count of panels; keep it apart from the 5 ft control joints.
5. **Forgetting coats.** C-6.0 requires two coats at stall lines; paint volume doubles for those lines.
6. **Conflicting details.** Civil bollard detail (24 in dia footing) vs A-190/A-401 (16 in dia). Pick by location (dumpster enclosure and drive-thru follow the architectural sheets) and record the choice.
7. **Assumed section.** The 4 in / 3 in / 1.5 in asphalt stack is labelled "assumed"; check the geotech before ordering.
8. **Ramp and aisle conflicts.** A curb ramp or flare projecting into a space or aisle is a design error to flag (ADA 406.5).
9. **Counting interior ADA signs here.** Restroom tactile signs (G-001) are Division 10.
10. **Demo vs new.** Demo curb 987.22 LF vs new curb 994 LF are close but not equal; do not copy one to the other.

Checks to run before releasing the takeoff (use Python):
- Legend total vs estimate total, per surface.
- Concrete CY = SF x t / 12 / 27, for each thickness; reconcile to the CY on the pour list.
- Tonnage = SF / 9 x inches x 110 / 2000 per course; compare to the mix schedule if one exists.
- Footing CY = pi x r^2 x h / 27 x count; compare each to the estimate (the estimate's 12 in dia x 3.5 ft footing reads 0.1024 CY vs 0.1018 CY by pi; it is within 0.6 percent).
- Paint gallons = (LF x width in / 12) / 107 x coats, using the product's own spread rate.
- Sidewalk joints: LF = (walk length / 5 ft) x walk width, plus expansion joints per structure.
- Counts: accessible spaces, STOP signs, bollards, bike racks against the plan symbols.

## 8. What an AI takeoff must read from drawings and specs

1. **Keynote legend on C-3.0 and C-1.0**: keynote number, description, unit, and the polygon/length it points to. Parse the text layer and the colored markup areas.
2. **Detail sheets C-6.x**: thickness, strength, reinforcement, joint spacing, finish, base. These appear as notes beside the cross sections, not in tables.
3. **Section callouts with "assumed details"**: record as assumed and request geotech.
4. **Architectural A-190 / A-401 / A-110**: bollard type, count, footing size, covers, paint color; trash enclosure slab.
5. **Product submittals / spec text** for: detectable warning product, traffic paint spec and bead rate, sign panel legend and sheeting, bike rack model and anchor type. This job has no Division 32 spec, so the AI must say so rather than fabricate a spec section.
6. **Stripe widths and coats from notes**, not from plan graphics. Convert LF to SF or gallons only after reading the width and coats.
7. **Jurisdiction references**: GDOT standard for the ramp ("GDOT STANDARD ADA RAMP WITH DETECTABLE WARNING"), the local H.C. code for the ADA sign text, and the solid-waste ordinance for dumpster signage.
8. **Slopes and ADA geometry** on grading sheets to confirm ramp runs and landings exist at the dimensions in section 4.
9. **Units**: output LF, SF, SY, CY, TON, EA, GAL, LB consistently and keep both measured and ordered quantity.

## 9. Engine comparison (reference only, not edited)

`TakeoffSpeed repo: lib/quantities/trades/site/site-paving.ts` and `pavement-marking.ts` already implement: asphalt by course at 110 lb/SY-in, aggregate at 1.9 ton/CY, tack and prime, WWF sheet 8 ft x 20 ft with 2 in extra lap, paint at 15 mils (1,604 / mils SF per gal), beads at 6 lb/gal, broken lines at 10 ft dash and 30 ft gap, 5 gal pails. Points to examine against the sources above: the WWF default sheet is 8 x 20 ft whereas the WRI document describes stock sheets as 5 to 10 ft wide and 10 to 20 ft long (8 x 20 is inside that range); the paint spread rate 1,604 / 15 = 106.9 SF/gal matches the Sherwin-Williams 107 SF/gal; the engine's 10 ft / 30 ft broken-line pattern and its asphalt, aggregate, tack, prime and bead constants are **[UNSOURCED]** from this pass and should be verified against the cited agency documents.

## 10. Source list

Fetched and read:
- US Access Board, ADA Standards for Accessible Design: https://www.access-board.gov/ada/
- US Access Board, Chapter 5 Parking guide: https://www.access-board.gov/ada/guides/chapter-5-parking/
- FHWA MUTCD 11th Edition, Part 3 Markings: https://mutcd.fhwa.dot.gov/pdfs/11th_Edition/part3.pdf
- FHWA MUTCD 11th Edition, Chapter 2A: https://mutcd.fhwa.dot.gov/pdfs/11th_Edition/Chapter2a.pdf
- FHWA MUTCD 11th Edition, Chapter 2B: https://mutcd.fhwa.dot.gov/pdfs/11th_Edition/Chapter2b.pdf
- NRMCA CIP 6, Joints in Concrete Slabs on Grade: https://www.nrmca.org/wp-content/uploads/2021/01/06pr.pdf
- FDOT Standard Plans Index 520-001 Curb and Gutter: https://www.fdot.gov/docs/default-source/design/standardplans/2024/idx/520-001.pdf
- FDOT Standard Plans Index 522-001 Concrete Sidewalk: https://www.fdot.gov/docs/default-source/design/standardplans/2024/idx/522-001.pdf
- Wire Reinforcement Institute TF 202: https://wirereinforcementinstitute.org/download_file/571
- Wire Reinforcement Institute detail WWR.2: https://wirereinforcementinstitute.org/download_file/view/354
- Sherwin-Williams Hotline TM2152 data sheet: https://www.paintdocs.com/docs/webPDF.jsp?SITEID=STORECAT&lang=E&doctype=PDS&prodno=TM2152
- APBP Essentials of Bike Parking: https://www.apbp.org/assets/docs/EssentialsofBikeParking_FINA.pdf
- Concrete Network, how much concrete: https://www.concretenetwork.com/concrete/howmuch/
- Pavement Interactive, Compaction and Placement: https://pavementinteractive.org/reference-desk/construction/compaction/ and https://pavementinteractive.org/reference-desk/construction/placement/
- NAPA Mix Quantity calculator page: https://www.asphaltpavement.org/resources/calculators/mix-quantity-economic-impact/

Not reachable in this pass (re-try when search quota resets): TxDOT Items 340/529/531/666 (503), Reliance Foundry bollard pages (403), FHWA FP-14 and FHWA tack coat guide (404 / unreadable), state DOT HMA tonnage conversion pages, thermoplastic thickness and bead-rate documents.
