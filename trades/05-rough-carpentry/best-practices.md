# Rough carpentry takeoff: sheathing, blocking, backing, interior trim

Scope: quantities and material types only (no pricing, no labor). Trade = MasterFormat Division 06 as it appears on this bank-branch job: Section 06 10 53 Miscellaneous Rough Carpentry, Section 06 16 00 Sheathing, and the interior trim line the estimator carried under Div 06.

## 0. How to read this document (evidence grading)

Research limits in this run: the shared web-search budget was exhausted before the first query, so every external source below was reached by direct page fetch, not by search. Several authoritative documents could not be retrieved (APA E30 PDF, AWC WCD 1, the IBC 718.2 text, the NRCA and SPRI nailer details, TIA-569, the Woodworking Institute AWS). Each claim is tagged:

- **[V]** read on the cited page in this run.
- **[P]** read in this project's own specification or drawings (local files).
- **[C]** estimating convention that is widely used but that I could not source from a fetched page. Treat as a default to confirm, not as a cited fact.

Where a number is [C], the engine default or the estimator's number is given alongside so the reader can see the spread.

---

## 1. What the estimator takes off, and in which unit

| Item | Unit | Notes |
|---|---|---|
| Wall sheathing (exterior) | SF net, then sheets | Panel type and thickness are separate lines (this job: 1/2" and 5/8" plywood) |
| Roof / canopy / ceiling sheathing | SF net, then sheets | Sloped areas measured on the slope, not the plan |
| Plywood backing / backboards | SF net (panel W x H) | Fire-retardant treated (FRT) when specified; 8'-0" tall at the IT room here |
| Blocking and nailers | LF by nominal size and treatment | Also reported as board feet (BF) for purchasing |
| Roof penetration, curb and parapet nailers | LF by size, plies and treatment | Pressure-treated (PT), not FRT |
| In-wall blocking for casework, equipment, accessories | LF by size and treatment | Count the stacked rows (the "(7) 1x4" tag) |
| Interior trim at openings | LF by profile | Door/window casing, stops; measured per opening |
| Fasteners, flashing separator, field treatment of cuts | allowance / EA / LF | Follow from the spec (see section 6) |

Unit facts used throughout:

- A 4 x 8 ft panel is 32 SF [V: [Omni Calculator plywood](https://www.omnicalculator.com/construction/plywood), [Inch Calculator plywood](https://www.inchcalculator.com/plywood-calculator/)]; plywood is most commonly made in 4 x 8 ft sheets [V: [Wikipedia, Plywood](https://en.wikipedia.org/wiki/Plywood)].
- Board foot = thickness (in) x width (in) x length (ft) / 12 [V: [Wikipedia, Board foot](https://en.wikipedia.org/wiki/Board_foot), [Inch Calculator board foot](https://www.inchcalculator.com/board-footage-calculator/), [Omni Calculator board foot](https://www.omnicalculator.com/construction/board-foot)]. For surfaced softwood, board feet are computed from the nominal width and thickness and the actual length [V: Wikipedia, Board foot]. So 1 LF of 2x4 = 2 x 4 / 12 = 0.667 BF, and 1 LF of 1x4 = 0.333 BF.
- Actual sizes are smaller than nominal: 2x4 is 1-1/2 x 3-1/2 in, 2x6 is 1-1/2 x 5-1/2 in, 2x8 is 1-1/2 x 7-1/4 in, 2x10 is 1-1/2 x 9-1/4 in, 2x12 is 1-1/2 x 11-1/4 in [V: [Wikipedia, Lumber](https://en.wikipedia.org/wiki/Lumber)]. Use actual sizes when a detail depends on real thickness (nailer height against insulation); use nominal when buying and when computing BF.
- Stock lengths in the US and Canada: 6, 8, 10, 12, 14, 16, 18, 20, 22, 24 ft; precut studs for 8, 9 and 10 ft ceilings are 92-5/8, 104-5/8 and 116-5/8 in [V: Wikipedia, Lumber].

---

## 2. Which sheets and spec sections drive it

### Specification (this job) [P]

All from `source/specifications.pdf` (index: `reference/sheets/spec_index.json`; page text `text/spec-pNNN.txt`).

- **06 10 53 Miscellaneous Rough Carpentry (spec pp. 122-127).** Includes wood blocking and nailers and plywood backing panels (1.1 A). Treatment rules:
  - Preservative treatment is by pressure process to AWPA U1: UC2 for interior not in ground contact, UC3b for exterior not in ground contact, UC4a for ground contact (2.2 A). Treat items indicated on the drawings, "and wood nailers, blocking, and similar members in connection with roofing, flashing, and vapor barriers" (2.2 D).
  - Fire-retardant treatment: flame spread index 25 or less under ASTM E84, Interior Type A unless exterior type is indicated (2.3 B). Apply to items indicated on the drawings "and concealed blocking" and "plywood backing panels" (2.3 E).
  - Dimension lumber: Construction or No. 2 grade, any species (2.4 B).
  - Equipment backing panels: plywood to DOC PS 1, Exterior, A-C, fire-retardant treated, thickness as indicated or not less than 3/4 in (2.5 A).
  - Fasteners: hot-dip zinc (ASTM A153) where carpentry is exposed, in ground contact, preservative treated, or in high humidity (2.6 A.1). A flexible flashing separator is required between PT wood and metal decking (3.1 G, 2.7 A).
  - Install FRT backing with the testing-agency classification marking exposed to view (3.1 C).
- **06 16 00 Sheathing (spec pp. 128-131).** Includes wall sheathing and parapet sheathing. Plywood sheathing is DOC PS 1 Exterior sheathing, span rating not less than 32/16, nominal thickness as indicated on the drawings (2.4 A). Preservative-treated and FRT plywood are available "where indicated on Drawings" (2.2, 2.3). It points to 07 25 00 Weather Barriers for the water-resistive barrier over the sheathing, and to 06 10 53 for backing panels (1.1 B).

### Drawings (this job) [P]

- **A-110 General notes:** the contractor provides blocking for all wall-mounted equipment and accessories; all wood blocking, bridging, bracing and framing shall be fire-retardant treated as called for by the governing code; the IT/electrical room gets FRT plywood on all walls, 8 ft tall, painted to match, with the label kept visible.
- **E-702 Electrical elevations:** "PLYWOOD BACKBOARD: PROVIDE 8' x (LENGTH AS REQUIRED) x 3/4" FIRE-RATED PLYWOOD" mounted vertically along all the room walls, UL label visible. Net area comes from the elevation widths, not from the plan.
- **A-140 Roof plan + A-450 Roof details:** 5/8" plywood under the single-ply membrane; "ALL ROOF PENETRATIONS REQUIRE PRESSURE TREATED 2x6 BLOCKING AT INSULATION AROUND ENTIRE PERIMETER"; detail callouts for P.T. wood nailers at coping (2x P.T.), at prefabricated metal curbs (2x4 P.T. nailer, fasteners at 6" o.c.), and at the wall top.
- **A-120 / A-140 / A-440 wall sections:** exterior sheathing thickness by wall type (1/2" at the metal-stud walls); 2x P.T. blocking at brick closure and at brake-metal conditions.
- **A-700 to A-707 enlarged plans and details:** the bulk of the in-wall blocking and plywood backing for casework. Tags like "(7) 1x4 FIRE RETARDANT TREATED BLOCKING" mean seven stacked or repeated rows.
- **A-600 door schedule and details:** drives interior trim at openings.
- **S-601, S-603:** "see architectural drawings for blocking" (structural sheets defer blocking to A-sheets, so do not look for it there).

---

## 3. Standard measurement rules

### 3.1 Sheathing and backing panels (SF)

1. Measure net installed area, then convert to sheets. The common method is total SF, plus a waste allowance, divided by the sheet area (32 SF), rounded up [V: Inch Calculator plywood; Omni Calculator plywood].
2. **Walls:** length x height, per wall type and per sheathing thickness. Deduct openings (windows, doors, louvers) at their rough-opening size. This is the convention the TakeoffSpeed engine applies [C]; the estimator's exterior wall line on this job (1/2" x 3,057.08 SF) must be read the same way, with the estimator's actual deduction threshold unknown.
3. **Height:** use the height the section shows the sheathing stops at, which may be the top of the metal stud, the underside of the roof deck, or the top of the parapet. Parapet sheathing is a separate scope item in 06 16 00 (1.1 A.2) [P].
4. **Roofs and canopies:** measure the sloped surface. The slope factor is sqrt(1 + (rise/12)^2) [C: geometry]; the engine applies it [P: `lib/quantities/trades/structure/rough-carpentry.ts`]. On this job the roof is nearly flat (tapered insulation), so the factor is close to 1.
5. **Backing / backboards:** take panels as W x H from the elevation (E-702: 8'-0" tall, full-length along the room walls). Do not take them as a plan area.
6. **Panel edge gap:** APA says leave a 1/8" gap between sheathing panels for expansion, and a 10d box nail (0.128" x 3") can serve as the spacer [V: [APA Roof Systems](https://www.apawood.org/applications-systems/roof-systems/); [APA Builder Tip N335](https://www.apawood.org/guides-tools-training/technical-document-library/builder-tips/proper-installation-of-apa-rated-sheathing-for-roof-applications/)]. A 4 x 8 panel then covers about 31.9 SF, not 32 SF (computed: 47.875 x 95.875 / 144). That 0.4% is far below the waste allowance, so takeoff on 32 SF per sheet is correct; the gap matters for framing layout (panel ends land on framing), not for quantity.

### 3.2 Blocking and nailers (LF, BF)

- Take LF along the run the detail shows, times the number of rows or plies. Report by nominal size and by treatment (PT, FRT, untreated) as separate lines, because they are bought separately [P: the estimate keeps them separate].
- Blocking provides "grounds (backing or back blocking)" to hold fixtures such as cabinets, shelving, handrails and vanity tops, and spreads the load across structural members [V: [Wikipedia, Blocking](https://en.wikipedia.org/wiki/Blocking_(construction))]. Spacing intervals come from the code or the engineer, not from a rule of thumb [V: same page].
- Convert to BF only for purchasing: LF x thickness x width / 12 using nominal sizes [V: Wikipedia, Board foot].
- Stock length: blocking is cut from stock lengths (8-24 ft [V: Wikipedia, Lumber]). Short in-wall pieces (1.6 ft, 8.6 ft runs) cut from the same stock, so waste is driven by the number of cuts as well as the pieces.

### 3.3 Interior trim at openings (LF)

- Take each opening's perimeter on the sides and head (casing); sill and apron where a window has them. This job's estimate carries "INTERIOR TRIM AT OPENING, ASSUMED" at 910 LF from sheet A-600 [P]. "Assumed" means the estimator did not measure it from a drawing; an AI must either measure each opening from the door and window schedules or flag the number as an assumption.
- Baseboard is a different item (finish, Div 09 or 06 20 00): the lowest part of an interior wall, typically under about 8 in high [V: [Wikipedia, Baseboard](https://en.wikipedia.org/wiki/Baseboard)]. Do not double count base with opening trim.
- Door openings are deducted from base length but not from casing; this is a convention [C].

### 3.4 Treatment decides the line

- **FRT** (interior Type A unless "Exterior" is indicated): flame spread index of 25 or less under ASTM E84, dried to 19% moisture content or less for lumber and 15% or less for wood structural panels [V: [Hoover Treated Wood Design & Construction Guide](https://frtw.com/wp-content/uploads/2026/01/FRTW-Design-And-Construction-Guide.pdf), quoting 2024 IBC 2303.2.8-2303.2.9; [UpCodes CBC 2022 ch. 23](https://up.codes/viewer/california/ca-building-code-2022/chapter/23/wood)]. The label must show the agency mark, treater, treatment name, species, flame spread and smoke-developed index, drying method [V: Hoover guide, 2024 IBC 2303.2.5].
- Paints and coatings are not FRT [V: Hoover guide, 2018/2021 IBC 2303.2.2].
- **Preservative-treated (PT)** is a different product and not a substitute for FRT [V: UpCodes 2303.2 and 2304.12 summaries; Hoover guide states FRT "cannot be substituted for preservative treated wood"]. Required by the IBC for wood in contact with earth, sleepers and sills on a slab in contact with earth, framing against below-grade walls, and similar [V: UpCodes CBC 2022 ch. 23, 2304.12]. Roofing nailers are PT by this job's spec (06 10 53 2.2 D) [P].
- When both could apply (a roof nailer that is also in a rated assembly), the drawing or spec wins; if silent, flag it.

---

## 4. Coverage, yield, waste

| Item | Factor | Basis |
|---|---|---|
| 4 x 8 panel | 32 SF per sheet | [V] Inch Calculator, Omni Calculator, Wikipedia Plywood |
| Sheathing sheet waste | 10% minimum, round up to whole sheets | [V] [Omni Calculator plywood](https://www.omnicalculator.com/construction/plywood), [Inch Calculator plywood](https://www.inchcalculator.com/plywood-calculator/). These are calculator-site rules of thumb, not a manufacturer or code figure |
| Engine default | 10% (class `rough-carpentry`: dimension lumber, blocking and sheathing) | [P] `lib/quantities/trades/structure/rough-carpentry.ts` |
| Stud count | ceil(length / spacing) + 1, plus extra studs at corners and openings | [V] [Inch Calculator framing](https://www.inchcalculator.com/framing-calculator/); typical spacing 16 in o.c., sometimes 12 or 24 [V] [Wikipedia, Framing](https://en.wikipedia.org/wiki/Framing_(construction)) |
| Plates | 3 per wall (one bottom, two top) | [V] Inch Calculator framing says multiply by three or four; Wikipedia Framing: two top plates are common |
| Blocking waste | No authoritative source found. Industry practice is 10% or more, higher for short pieces; **[C]** | Do not present this as a sourced number |

Worked sheet counts for this job (Python, net SF from `lines.json` descriptions, 10% waste, 32 SF per sheet):

| Line | Net SF | Net sheets | Sheets at +10% |
|---|---|---|---|
| 1/2" plywood, exterior wall | 3,057.08 | 95.5 | 106 |
| 5/8" plywood, exterior wall | 162.99 | 5.1 | 6 |
| 5/8" plywood, roof | 285.00 | 8.9 | 10 |
| 5/8" plywood, canopy ceiling | 568.50 | 17.8 | 20 |
| 3/4" plywood, booth ceiling | 152.00 | 4.8 | 6 |
| 3/4" FR plywood backboard, IT room | 215.33 | 6.7 | 8 |
| 1/2" plywood, booth wall | 47.70 | 1.5 | 2 |

Two consequences: (1) keep thicknesses separate, since waste is applied per line; (2) a backboard bought as 8-ft-long full-height sheets (E-702 says 8 ft tall) wastes little, so the sheet count for it is closer to net / 32 rounded up than to +10%.

Nail and gap facts that follow from the panel, useful for a fastener allowance:

- Roof sheathing nails: 8d common or ring-shank, 6 in at edges and 6 in at intermediate supports for 3/8"-3/4" panels; 10d common, 6 in edge and 12 in field for 7/8"-1-1/4" panels; tighter spacing near roof edges in high wind [V: [UpCodes CBC 2022 ch. 23, Table 2304.10.2 rows 30-32](https://up.codes/viewer/california/ca-building-code-2022/chapter/23/wood); the page warns the table layout was garbled, so verify against the code]. APA Builder Tip N335: at least 8d common nails [V].
- Local wind uplift or diaphragm design can override these, so a takeoff should read the structural notes before assuming a nailing pattern.

---

## 5. Material breakdown the estimator lists

**Sheathing**
1. Plywood panels by thickness, grade/exposure (DOC PS 1 Exterior, span rating 32/16 here [P]) and size.
2. Treatment where indicated (PT or FRT plywood).
3. Fasteners, per the spec and the nailing schedule; hot-dip galvanized where treated or exposed [P: 06 10 53 2.6 A.1].
4. Water-resistive barrier is a separate section (07 25 00) [P]; joints and flashing at sheathing are not in this trade.

**Backing panels / backboards**
1. Plywood, DOC PS 1 Exterior A-C, FRT, 3/4" minimum [P: 06 10 53 2.5 A].
2. Fasteners to studs; the classification mark must stay exposed [P].
3. Paint is Div 09; it does not belong in this line.

**Blocking and nailers**
1. Lumber by nominal size, grade (Construction or No. 2 [P]) and treatment (PT or FRT).
2. Anchors, bolts or screws to the substrate: recess bolts and nuts flush unless indicated (06 10 53 3.2 B) [P]; screws for metal framing to ASTM C954 (2.6 C) [P]; power-driven fasteners and post-installed anchors with ICC-ES reports (2.6 D, E) [P].
3. Flexible flashing separator where PT wood sits on metal decking (2.7 A, 3.1 G) [P].
4. Field treatment of cut PT surfaces to AWPA M4 (3.1 F) [P]. FRT lumber may be cut to length in the field without end treatment, but not ripped or milled after treatment; FRT plywood may be cut in any direction [V: Hoover guide, CSI-format specification 3.03 D]. A designer should note this: ripped FRT is a rejection risk.

**Interior trim**
1. Trim stock by profile and species (wood, MDF) [V: Wikipedia Baseboard lists wood and MDF].
2. Fasteners and adhesive; finish is Div 09.

---

## 6. Common mistakes and checks

1. **Missing the multiplier in a legend tag.** In the PlanSwift legends here, "(7) 1x4 FIRE RETARDANT TREATED BLOCKING 8.6 FT" is a measured length of 8.6 ft taken seven times, which is 60.2 LF. A takeoff that reports 8.6 LF understates by 7x. Across the pages A-700 to A-707 the 1x4 legend rows give 206.6 LF (computed: 7 x 8.6 + 2 x 14.6 + 4 x 9.8 + 2 x 23.3 + 2 x 15.7), against 240.66 LF on the estimate line, so about 34 LF came from somewhere other than those legend rows (unlisted pages or other items). Treat the legend as a floor, not the full count.
2. **Mixing FRT and PT.** Casework blocking is FRT (A-110 note, A-701 tag). Roof penetration and parapet blocking is PT (A-140, A-450). The estimate keeps these on separate lines (lines 89-97), and an AI must too.
3. **Counting from the wrong sheet.** Structural sheets point to the architectural drawings for blocking (S-601, S-603). The count lives on A-sheets.
4. **Plan area for sloped decks, or elevations for backing.** Use the slope factor for roofs, and the elevation for backboards (E-702).
5. **Forgetting the second layer.** Sheathing may appear on both sides of a wall type (the booth wall), or two plywood layers behind a countertop. Read the wall type or detail.
6. **Treating "assumed" lines as measured.** The 910 LF of opening trim is an estimator assumption; do not claim it as a drawing quantity.
7. **Deducting everything.** Deduct openings from wall sheathing, but not control joints, corners, or small penetrations; ignoring the deduction threshold in the estimator's practice leads to systematic overstatement [C]. The estimator's actual threshold is unknown.
8. **Dimension lumber sizes.** 2x16 and 2x14 stock is not common in the yard; check whether the detail means built-up members (2 x 8 plus 2 x 8) or a typo. In this estimate, A-140 lists 2x16 (15 LF), 2x14 (40 LF) and 2x10 (148 LF) treated blocking; these read like roof-edge and curb nailers built up to match insulation height, so cross-check against A-450 before trusting them [C].

Check methods:
- **Reasonableness by ratio:** sheathing SF / wall area, and blocking LF / casework LF, should be stable across similar buildings; a 3x swing signals a miss.
- **Cross-sheet reconciliation:** every elevation or detail that names blocking should land on a plan, and vice versa.
- **BF cross-check:** the BF sum of all lumber lines should match the lumber order; a mismatch usually means a missed treatment class or a nominal/actual mix-up.
- **Sheet-count check:** net SF / 32 should be at or just below the sheet count; if sheets fall under net / 32 the count is wrong.

---

## 7. What an AI takeoff must read from the drawings and specs

1. **Spec 06 10 53 and 06 16 00 first.** Extract per item: material (plywood grade, lumber grade), thickness, treatment class (PT use category, FRT interior/exterior), and the "treat items indicated on drawings and the following" lists (nailers and blocking at roofing; concealed blocking and backing panels for FRT). These tell the AI which untagged blocking inherits a treatment.
2. **General notes (A-110):** blanket rules (all blocking FRT; equipment blocking by contractor; the IT room plywood 8 ft tall). These generate quantities with no tag on the plan.
3. **Wall types and sections (A-4xx, A-3xx):** sheathing thickness per wall type, where it stops, nailer and blocking callouts (2x P.T. blocking at brick closure and brake metal).
4. **Roof plan and details (A-140, A-450):** deck sheathing, nailer sizes and locations, the "all roof penetrations" blocking rule (perimeter of each curb, each pipe), and the roof schedule that gives penetration sizes.
5. **Enlarged plans and elevations (A-700 series, E-702):** each blocking tag with its row count and size, backing panel extents, countertop substrates. Read the height callouts ("PLYWOOD @ 3'-9"H", "@ 8"H") because they give panel heights and so SF.
6. **Door and window schedules (A-600):** opening count and sizes for trim.
7. **Equipment lists (bank equipment, TV, grab bars, toilet accessories):** each wall-mounted item needs blocking; the drawings often say only "provide blocking" (A-110). An AI must generate it from the item list and flag that the extents are an inference.
8. **Do not invent:** if the drawing does not give a height, treatment or thickness, return the gap, not a default (this repository's rule 1). An unread treatment on a blocking line should block the line, not default to untreated.

---

## 8. How the TakeoffSpeed engine compares (read only)

`TakeoffSpeed repo: lib/quantities/trades/structure/rough-carpentry.ts` defines `sheathing`, `blocking` and `backing` assemblies with the following behaviour [P]:

- Sheathing: SF net, sheets of 32 SF by default (4x8) or by stated size, waste class `rough-carpentry` at 10%, slope factor when a pitch is given.
- Blocking: LF = runs x rows, purchased in board feet (1 BF = 1/(t x w/12) LF); treatment is part of the line key, so PT and FRT stay separate.
- Backing: SF from W x H panels, thickness and treatment in the key.
- Gaps against the practice above: no trim assembly in this module (the 910 LF "assumed" trim line has no producer); the engine sets no distinct waste for short blocking pieces or for backboards; its 10-ft fireblocking interval (`rough-carpentry.fireblock-max-ft`, basis IBC 718.2.2) is stated in the engine but I could not retrieve the IBC 718.2 text in this run to confirm it, so treat it as unverified here. The A-450 text layer shows an 18'-8" wall dimension, so confirm that wall is metal stud (no wood fireblocking) before assuming no fireblocking applies.

---

## 9. Sources not retrieved (so not cited as fact)

- APA E30 / E30X-WC wall and roof construction guides: the pages describe the contents (wall sheathing, nail base for siding, shear walls) but the PDF links were not reachable, so the 6-in edge and 12-in field spacing is from the IBC table (section 4), not from APA.
- AWC WCD 1, ICC IBC 718.2 and 603.1 text, NRCA nailer details, ANSI/SPRI/FM 4435/ES-1 nailer dimensions (the [SPRI standards page](https://www.spri.org/standards/) lists ES-1 and RP-04 but gives no nailer height; [NRCA](https://nrca.net/roofing-guidelines/guidelines-resources/shop-fabricated-edge-metal-testing) only mentions ES-1 for edge-metal testing).
- TIA-569 plywood backboard (3/4 in, 8 ft): not retrievable. For this job the requirement is in the drawings (E-702, A-110) and spec 06 10 53 2.5 A.
- USDA Wood Handbook FPL-GTR-282 ([PDF](https://research.fs.usda.gov/download/treesearch/62200.pdf), 104 MB) was identified but not read.
- Woodworking Institute AWS (trim and casework blocking standards) and RSMeans trim conventions: not reachable.
- A waste percentage specific to blocking and to trim: no authoritative source found.

A follow-up run with search quota would target: APA E30X-WC PDF (nailing, orientation), IBC 718.2 and 603.1, the NRCA Roofing Manual nailer rules, FM Global DS 1-49 on perimeter and nailer attachment, and Gordian/RSMeans waste conventions.
