# Best practice: thermal and moisture protection (insulation, roofing, flashing, coping, EIFS, ACM, air/vapor barriers, sealants) - quantities and material types only

Scope: Division 07 on a low-slope commercial building: wall, under-slab and roof insulation; adhered TPO roofing with its tapered insulation, cover board, flashings, curbs and walkway pads; sheet-metal coping, counterflashing, head flashing and sills; through-wall flashing; EIFS; metal composite material (ACM) wall panels and canopy; weather/air/vapor barriers; and joint sealants with backer rod. Prices, labor and productivity are out of scope.

How to read this file. Every factual claim carries a link. Source quality is marked:
- **(primary)**: a manufacturer data sheet, installation detail, standard-derived slide deck or association technical note that I downloaded and read.
- **(project)**: a page of this job's specifications or drawings in this repository.
- **(search summary)**: a page seen only as a search-result summary; the page itself was not read, or returned 403 when fetched.
- **(secondary)**: a retailer or distributor listing, or an estimating blog.
- **(GPT-6 Astra)**: an unverified second opinion from `tools/ask_gpt.py` (saved in `trades/07-thermal-moisture/scripts/gpt/q1.txt`, `q2.txt`, `q3.txt`); it is used only to prompt cross-checks and is marked wherever it is the only support.
- **derived**: arithmetic of mine, checked in Python.

Honest summary of the evidence. There is no published "Division 07 takeoff standard." The citable numbers are (1) manufacturer coverage and sizing data (board sizes, roll sizes, fastener counts per board, base-coat and air-barrier coverage per gallon or pail, sealant yield), (2) installation details and specification text that fix laps, heights, spacings and layer rules (8 in. flashing height, 6 in. stagger of insulation joints, 2-1/2 in. mesh laps, 6 in. flashing laps), and (3) wind-zone geometry for fastening density. Opening-deduction thresholds, waste percentages and "add-on" allowances are estimator convention and the sources disagree or are silent. The right design for an AI takeoff is therefore: measure installed quantities from the drawings with the dimensions the details print, state the convention applied for every allowance, and keep net quantity, waste and package rounding as three visible steps. This job's estimator carries net quantities (no waste, no package rounding) as shown in section 9.

---

## 1. What an estimator takes off, and in which units

| System | Items listed | Unit | Notes / basis |
|---|---|---|---|
| Roof field membrane | TPO sheet by roof-type tag, thickness and attachment | SF (field plan area), rolls only at purchase | Fully adhered per [07 54 23 s.3.5](../../source/specifications.pdf) (project, pp.185-186); 60 mil nominal per s.2.3 (project, p.182). Rolls are 10 ft x 100 ft or 12 ft 4 in x 100 ft, 45 or 60 mil ([Elevate UltraPly product data](https://www.buildsite.com/pdf/firestone/UltraPly-TPO-Membrane-Product-Data-2979480.pdf), primary). |
| Base flashing, parapet membrane, curb flashing | Membrane or separate 55 mil sheet flashing up walls, over parapet tops and around curbs | LF by detail and height, then developed SF | Spec calls for 55 mil minimum unreinforced TPO sheet flashing ([07 54 23 s.2.4.B](../../source/specifications.pdf), project, p.183). Minimum flashing termination 8 in. above the roof surface is printed on [A-450](../../source/drawings/Architectural/A-450-ROOF-DETAILS-Rev.0.pdf) (project). |
| Roof insulation | Polyiso by thickness and layer; tapered panels; crickets/saddles; wall-transition rigid board | SF per layer, boards EA (SF / board area), tapered by panel designation | 4x4 and 4x8 boards ([Mule-Hide Poly ISO 2](https://images.greenbuildingadvisor.com/app/uploads/2020/09/24230905/Mule-Hide-Poly-ISO-2-Roof-Insulation-Flat-Tapered-Product-Data-1326252.pdf), primary; [JM listing via search](https://www.bimobject.com/sv/johns-manville/product/r-panel-roof-insulation), search summary). |
| Cover board | Gypsum or HD polyiso cover board by thickness | SF, boards EA | DensDeck Prime is 4x4 and 4x8, 1/4, 1/2 or 5/8 in. ([Kingspan data sheet](https://a-us.storyblok.com/f/572366803407467/x/727046ea6d/kingspan-densdeck-prime-roof-board-data-sheet-en-us-issue-1.pdf), primary). |
| Insulation and cover-board fasteners and plates | By FM/wind zone (field, perimeter, corner) | EA | Counts per board are in section 3.4. |
| Membrane accessories | Bonding adhesive; seam cover strip; termination bar; pipe boots; drain flashings; walkway pad; pourable sealer; corners | gal; LF; LF; EA; EA; SF; EA; EA | Accessory list in [07 54 23 s.2.4.F](../../source/specifications.pdf) (project, p.183). |
| Roof curbs, hatches, nailers | Prefabricated curbs (L x W x H), hatch, curb insulation, wood nailers | EA and perimeter LF | Curbs min. 12 in. high, factory 1-1/2 in. glass-fiber insulation and factory nailer; hatch 30 x 36 in. ([07 72 00 s.2.3-2.4](../../source/specifications.pdf), project, pp.199-200). Nailer LF is rough carpentry (spec cross-reference in 07 54 23 s.1.1.B, project, p.179). |
| Coping | Prefinished aluminum coping by girth/width, cleats, splice plates, corners, end caps | LF (by profile), EA for corners/plates/caps | Sections 96 in. minimum to 12 ft maximum, 6 in. concealed back-up plate, 0.040 in. aluminum ([07 62 00 s.2.6](../../source/specifications.pdf), project, p.193). |
| Counterflashing, head flashing, sills, drip/edge metal | By material, thickness, girth | LF | Detail-driven (project drawings below). |
| Through-wall flashing and sill pans | Flexible or metal flashing, end dams, weeps | LF (continuous runs), EA (end dams, weeps) | Laps, end dams and rise rules in section 3.6. |
| EIFS | Insulation board by thickness, adhesive, base coat, mesh and strip mesh, primer, finish; trim (drip screed, casing bead, expansion joint) | SF (system), LF (trim and reinforcing strips), EA (diagonal mesh pieces) | [07 24 13](../../source/specifications.pdf) (project, pp.151-158). |
| ACM wall and canopy panels | Panels (face SF), fabricated returns, sub-girts/furring, clips, flashings and trim, joint sealant | SF face area; LF sub-girt and trim; EA panels | [07 42 13](../../source/specifications.pdf) (project, pp.171-178). |
| Water-resistive and air/vapor barriers | Building wrap, fluid-applied membrane, self-adhered strips, transition strips, primer, termination mastic | SF, LF (strips at openings and transitions), gal or pail (at purchase) | [07 25 00](../../source/specifications.pdf) (project, pp.159-161), [07 27 26](../../source/specifications.pdf) (project, pp.164-170). |
| Below-grade vapor retarder | 15 mil sheet, tape, mastic | SF, LF tape | [07 26 16](../../source/specifications.pdf) (project, pp.162-163). |
| Wall, ceiling and under-slab insulation | Batts, sound-attenuation blankets, rigid XPS/EPS/polyiso by thickness | SF by thickness and type | XPS Type IV 25 psi ([07 21 00 s.2.1](../../source/specifications.pdf), project, p.147). |
| Joint sealants | Sealant by type/color, backer rod by diameter, bond-breaker tape, primer, cartridges or sausages | LF per joint size and sealant type; EA at purchase | Schedule in [07 92 00 s.3.5](../../source/specifications.pdf) (project, p.209); backing per ASTM C 1330 Type C (project, p.206). |

---

## 2. Which sheets and spec sections drive it

Specification sections in this set (all `source/specifications.pdf`): 07 21 00 Thermal Insulation (pp.146-150), 07 24 13 Polymer-Based EIFS (pp.151-158, not in `spec_index.json`'s section list but present in the text), 07 25 00 Weather Barriers (pp.159-161), 07 26 16 Below-Grade Vapor Retarders (pp.162-163), 07 27 26 Fluid-Applied Membrane Air Barriers (pp.164-170), 07 42 13 Metal Composite Material Wall Panels (pp.171-178), 07 54 23 TPO Roofing (pp.179-187, also not in the index), 07 62 00 Sheet Metal Flashing and Trim (pp.188-196), 07 72 00 Roof Accessories (pp.197-202), 07 92 00 Joint Sealants (pp.203-211) (project; `reference/sheets/spec_index.json` lists only 07 21 00, 07 25 00, 07 26 16, 07 27 26, 07 42 13, 07 62 00, 07 72 00 and 07 92 00, so an AI that relies on the index alone will miss the roofing and EIFS sections).

Drawings that drive quantities (project, `source/drawings/`):
- [A-140 Roof Plan](../../source/drawings/Architectural/A-140-ROOF-PLAN-Rev.0.pdf): roof types RT1 and RT2 with build-ups, tapered insulation and crickets, walkway pad hatch, drains, vent stacks, hatch, coping keynote R2, general notes (crickets 1/4 in. per foot minimum; all roof penetrations need pressure-treated 2x6 blocking).
- [A-450 Roof Details](../../source/drawings/Architectural/A-450-ROOF-DETAILS-Rev.0.pdf): coping and splice details, parapet membrane wrap, base flashing, curb, counterflashing, 8 in. minimum termination note.
- [A-200/A-201 Exterior Elevations](../../source/drawings/Architectural/A-200-EXTERIOR-ELEVATIONS-Rev.0.pdf): EIFS-1, EIFS-2, ACM1/ACM2, thru-wall flashing, sill, aluminum flashing and sealant keynotes.
- [A-310 Exterior Wall Sections](../../source/drawings/Architectural/A-310-EXTERIOR-WALL-SECTIONS-Rev.0.pdf) and [A-430 Section Details](../../source/drawings/Architectural/A-430-SECTION-DETAILS-Rev.0.pdf): wall build-ups (stud depth, batt, vapor barrier, fluid-applied barrier, EIFS thickness and R-value, rigid insulation, thru-wall flashing and weeps at 24 in. o.c.).
- [G-003 ComCheck](../../source/drawings/General/G-003-COMCHECK-Rev.0.pdf): R-value per inch used by the designer (polyiso 5.7, EPS 3.85, XPS 5) and the conditional under-slab XPS note.
- [S-201 Foundation Plan](../../source/drawings/Structural/S-201-Structural-Plan---Foundation-Rev.0.pdf): slab extent for under-slab insulation and vapor retarder.
- [A-706 Booth](../../source/drawings/Architectural/A-706-BOOTH---ENLARGED-PLAN-&-DETAILS-Rev.0.pdf): booth ceiling sound batt.
- Door/window schedules and storefront sheets for opening perimeters (sealant, flashing, air-barrier transition).

---

## 3. Standard measurement rules

### 3.1 General basis (applies to every system)

- There is no universal opening-deduction threshold for EIFS, ACM, air barrier or insulation. A senior-estimator second opinion recommends measuring actual-net coverage (deduct every opening where the material is absent), then keeping any "do not deduct openings under N SF" rule as a separate, labeled reporting convention; if one is used the example offered is 10 SF per opening, explicitly marked convention ([GPT-6 Astra q1](file://trades/07-thermal-moisture/scripts/gpt/q1.txt)). The sibling wall-framing study found the same absence of a standard for gypsum board ([09a best practices](../09a-wall-framing-drywall/best-practices.md)).
- Three quantities should never be confused: net installed coverage, conventional measured area, and purchase quantity (net plus returns, laps, waste) ([GPT-6 Astra q1](file://trades/07-thermal-moisture/scripts/gpt/q1.txt)). This matches the app's "aggregation before rounding" rule in `docs/QUANTITY_ENGINE.md`.
- Sealant calculators and all coverage tables assume a rectangular joint; Tremco states its calculators "are not suitable for detailing or flashing applications" because the product is often tooled flat ([Tremco](https://www.tremcosealants.com/blog/how-to-use-sealant-calculators-to-estimate-product-needs), primary).

### 3.2 Roof field area, parapets, base flashing

- No authoritative standard for the roofing takeoff method was found; the search results were trade articles and scraped guides. The practice below is convention: field membrane is measured as plan area of each roof type (RT1, RT2) from the roof plan; flashing is measured in LF where the roof meets a wall, parapet, curb or edge and then converted to developed SF ([GPT-6 Astra q1](file://trades/07-thermal-moisture/scripts/gpt/q1.txt)). For a parapet the developed width is height + top width + any downward leg; only the details tell which legs are membrane versus metal.
- Parapet membrane formula: area = sum of L x (H + T + D), where H is measured from the finished roof surface (not the deck) to the start of the top turn, T the horizontal coverage across the top, and D the downward leg if the detail shows one ([GPT-6 Astra q1](file://trades/07-thermal-moisture/scripts/gpt/q1.txt)). This job's A-450 detail has "install membrane down outside face of" the parapet under the coping and states that flashing must terminate at least 8 in. above the roof surface and that intermediate adhered-membrane fastening is required at 5 ft maximum intervals (project, [A-450](../../source/drawings/Architectural/A-450-ROOF-DETAILS-Rev.0.pdf)).
- Minimum base flashing height is 8 in. in several authoritative documents: the VA master spec ("minimum of 200 mm (8 inches) above the roof surface") ([VA 07 54 23](https://www.wbdg.org/FFC/VA/VAASC/VA%2007%2054%2023.pdf), search summary) and BIA for masonry through-wall flashing turned up 8 in. ([BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf), primary). GAF's older parapet details also show 8 in. minimum base flashing, with 24 in. as the threshold for a separate high-parapet detail ([GAF search](https://www.gaf.com/en-us/blog/commercial-roofing/roof-to-wall-flashing-why-details-matter-for-single-ply-roofing-systems-04873b23-f26d-4119-b9c7-1d56c2da7484), search summary).
- Heat-welded TPO laps need a 1-1/2 in. weld with an automatic welder or 2 in. with a hand welder, per GAF's hybrid base-of-wall detail ([GAF detail](https://www.gaf.com/en-us/document-library/documents/details/tpo-hybrid-flashing-at-base-of-wall-or-curb-detail-075423-931.pdf), search summary). The project spec only says "minimum dimensions required by manufacturer" ([07 54 23 s.3.5.C](../../source/specifications.pdf), project, p.186), so lap width comes from the selected manufacturer's detail.
- Penetrations (drains, vent pipes, curbs, hatches) are counted in EA separately from the field area on the plans and reconciled against detail sheets and the Division 07 spec ([GPT-6 Astra q2](file://trades/07-thermal-moisture/scripts/gpt/q2.txt), convention). Small penetrations are usually not deducted from field area (same source, convention). A generic take-off guide says to subtract skylights, chimneys and other openings from total roof area with no size threshold ([scraped take-off guide](https://wiki.uep.edu.py/Download_PDFS/taking/705655/Off%20Quantities%20For%20Roof.pdf), secondary, low quality), which is why the hatch and RTU curb footprints should be deducted from field area explicitly and their flashing taken separately.
- Slope: for low-slope roofs plan area is used; actual area for a pitched plane = plan area x sqrt(1 + (rise/12)^2) (standard geometry, derived).
- If the field sheet itself turns up the wall, assign it to one line (field or flashing), never both ([GPT-6 Astra q2](file://trades/07-thermal-moisture/scripts/gpt/q2.txt)).

### 3.3 Roof insulation layers, boards, cover board, tapered

- Layers: where total insulation thickness is 2.7 in. or more, two or more layers with joints of each layer staggered at least 6 in. in each direction ([07 54 23 s.3.4.D](../../source/specifications.pdf), project, p.185). Mule-Hide also suggests multi-layer application above 2.7 in. ([Mule-Hide Poly ISO 2](https://images.greenbuildingadvisor.com/app/uploads/2020/09/24230905/Mule-Hide-Poly-ISO-2-Roof-Insulation-Flat-Tapered-Product-Data-1326252.pdf), primary) and PIMA recommends a multi-layered, staggered-joint continuous system ([PIMA TB 118](https://www.polyiso.org/page/TB118), search summary).
- Take off each layer separately: boards per layer = SF x (1 + waste) / board area (32 SF for 4x8, 16 SF for 4x4) ([GPT-6 Astra q2](file://trades/07-thermal-moisture/scripts/gpt/q2.txt) for the formula; board sizes from [Mule-Hide](https://images.greenbuildingadvisor.com/app/uploads/2020/09/24230905/Mule-Hide-Poly-ISO-2-Roof-Insulation-Flat-Tapered-Product-Data-1326252.pdf) and [Kingspan](https://a-us.storyblok.com/f/572366803407467/x/727046ea6d/kingspan-densdeck-prime-roof-board-data-sheet-en-us-issue-1.pdf), primary). The R-value target fixes thickness: LTTR is 5.7 per inch for 1 in. polyiso, 11.4 at 2 in., 23.6 at 4 in. ([Mule-Hide](https://images.greenbuildingadvisor.com/app/uploads/2020/09/24230905/Mule-Hide-Poly-ISO-2-Roof-Insulation-Flat-Tapered-Product-Data-1326252.pdf), primary); 6 in. x 5.7 = R-34.2 (derived), which matches RT1's "R-value = 34.2 (R-5.7/inch)" note on [A-140](../../source/drawings/Architectural/A-140-ROOF-PLAN-Rev.0.pdf) (project).
- Tapered insulation: Mule-Hide tapered panels are 1/8 in. per ft (panels AA, A, B, C), 1/4 in. per ft (X, Y) and 1/2 in. per ft (Q), each with a stated thickness range ([Mule-Hide](https://images.greenbuildingadvisor.com/app/uploads/2020/09/24230905/Mule-Hide-Poly-ISO-2-Roof-Insulation-Flat-Tapered-Product-Data-1326252.pdf), primary). This job calls for factory-tapered boards at 1/4 in. per 12 in. unless indicated, plus saddles, crickets and edge strips ([07 54 23 s.2.5.C-D](../../source/specifications.pdf), project, p.183). Cricket SF is the footprint (triangle = b x h / 2); volume or board-feet uses average thickness per facet: for a triangular facet with one high vertex and two at t0, average = t0 + rise/3, and for a rectangular wedge t0 + rise/2 ([GPT-6 Astra q2](file://trades/07-thermal-moisture/scripts/gpt/q2.txt), unverified but standard geometry). Final panel counts follow the manufacturer's tapered layout, not volume.
- Cover board: counted as a separate SF layer with its own fasteners; the spec requires cover board joints offset at least 6 in. from the insulation joints below and long joints in continuous lines ([07 54 23 s.3.4.H](../../source/specifications.pdf), project, p.185). Note the conflict in section 11 on its thickness.
- Wood nailers at drains, curbs and terminations must match insulation thickness ([07 54 23 s.3.1.A](../../source/specifications.pdf), project, p.184).
- Insulation at drains is trimmed flush ([07 54 23 s.3.4.E](../../source/specifications.pdf), project, p.185); gaps over 1/4 in. are filled with insulation (s.3.4.F).

### 3.4 Fastening zones and counts

- Zone geometry: Tremco's perimeter and corner layout states "dimension A equals 10% of roof width or 40% of building height, whichever is less, with a minimum of 4 ft" ([Tremco detail 14](https://tremcoroofing.com/media/Roofing/Detail%20Drawings/TremPly%20Single%20Ply%20Roofing%20Systems/Application/TremPly%20KEE%20Single%20Ply%20Roofing%20Systems/PDFs/Class-1-90-or-more,-General-Perimeter-and-Corner-Layout.pdf), primary). The ASCE 7 roof-zone width in the SPRI wind-design deck is a = 0.4 x height or 0.1 x width, whichever is less, but not less than 0.04 x width or 3 ft ([SPRI WDS slides](https://www.spri.org/wp-content/uploads/2023/10/2-2023-WDS-ASCE-7_Chamberlain.pdf), primary). The two differ (4 ft versus 3 ft minimum), so take the number from the project's uplift diagram or the manufacturer's approval.
- Fastener counts per board with FM 1-29 prescriptive enhancements for perimeter and corners (JM, 2 ft x 4 ft = 8 SF boards, "< Class 1-75 systems") ([JM RS-7388](https://JM.COM/content/dam/jm/global/en/commercial-roofing/Fastening-Patterns/RS-7388_2x4-Roof-Insulation-Fastening-Placement.pdf), primary):

| Field density | Field | Perimeter | Corner | Per 4x8 (field/perim/corner) | Per SF (derived) |
|---|---:|---:|---:|---|---|
| 1 per 2 SF | 4 | 6 | 8 | 16 / 24 / 32 | 0.50 / 0.75 / 1.00 |
| 1 per 2.67 SF | 3 | 5 | 8 | 12 / 20 / 32 | 0.375 / 0.625 / 1.00 |
| 1 per 4 SF | 2 | 4 | 8 | 8 / 16 / 32 | 0.25 / 0.50 / 1.00 |

- Manufacturer minimums by attachment: mechanically attached membrane over insulation, at least 4 fasteners per 4x4 board and 6 per 4x8; fully adhered membrane, if the top insulation layer is under 2 in. thick at least 16 per 4x8 (and 8 per 4x4), and if 2 in. or thicker 8 per 4x8 (4 per 4x4) ([Mule-Hide Poly ISO 2](https://images.greenbuildingadvisor.com/app/uploads/2020/09/24230905/Mule-Hide-Poly-ISO-2-Roof-Insulation-Flat-Tapered-Product-Data-1326252.pdf), primary). DensDeck cover board: 8 fasteners per 4x8 for 2 in. or thicker insulation attachment, with FM patterns of 12, 16 and 17 ([Mule-Hide DensDeck page](https://www.mulehide.com/Products/p/DensDeckPrimeRoofBoard), search summary).
- Count rule: count fasteners and plates on installed boards per pattern (not on boards bought with waste); one plate per fastener; do not multiply by the number of layers when one fastening pass secures the stack ([GPT-6 Astra q2](file://trades/07-thermal-moisture/scripts/gpt/q2.txt)). The wind design pressure that sets the pattern is "as indicated on Drawings" ([07 54 23 s.2.2.C](../../source/specifications.pdf), project, p.182), so the AI must read it from the roof plan or code sheet.
- Intermediate adhered-membrane fastening at 5 ft maximum intervals is printed on [A-450](../../source/drawings/Architectural/A-450-ROOF-DETAILS-Rev.0.pdf) (project); the spec also requires mechanical fastening at terminations, penetrations and perimeter ([07 54 23 s.3.5.E](../../source/specifications.pdf), project, p.186).

### 3.5 Sheet metal: coping, counterflashing, head flashing, sills

- Coping is taken off in LF along a declared reference line, grouped by profile/girth, with corners, end caps, intersections and splice plates counted separately in EA ([GPT-6 Astra q3](file://trades/07-thermal-moisture/scripts/gpt/q3.txt)). Girth (developed flat-sheet width, including front and back drops, upstands, hems and returns) governs metal area: SF = LF x girth(in.) / 12 (derived from [GPT-6 Astra q3](file://trades/07-thermal-moisture/scripts/gpt/q3.txt)). Do not equate coping top width with girth.
- Piece lengths: this spec fabricates coping in sections of 96 in. minimum to 12 ft maximum with 6 in. wide concealed back-up plates, butted with expansion space ([07 62 00 s.2.6.A](../../source/specifications.pdf), project, p.193). Englert's snap-on coping comes in 10 ft increments with a 6 in. splice plate and a 1/8 in. gap between 10 ft sections ([Englert instructions](https://www.englertinc.com/sites/default/files/coping-2-installation.pdf), primary); ATAS shows 12 ft continuous-cleat coping with a 6 in. splice and sealant by others ([ATAS spec sheet](https://www.atas.com/wp-content/uploads/2018/06/Continuous-Cleat-Coping-Spec-Sheet.pdf), search summary). The project spec also requires movement joints at maximum 10 ft spacing and none within 24 in. of a corner or intersection ([07 62 00 s.3.3.C](../../source/specifications.pdf), project, p.194), so with this spec 10 ft is the controlling piece length for splice counts.
- Splices are counted by connection, not by piece: an open run of n sections has n - 1 internal connections, a closed loop n ([GPT-6 Astra q3](file://trades/07-thermal-moisture/scripts/gpt/q3.txt)). Each miter corner is one corner assembly; each open end needing a cap is one end cap (same source).
- Cleats: continuous cleat anchored at 24 in. centers per [07 62 00 s.3.4.B](../../source/specifications.pdf) (project, p.195) but "space cleats not more than 12 inches apart" per s.3.3.A.3 (project, p.194); Englert fastens cleats at 12 in. o.c. ([Englert](https://www.englertinc.com/sites/default/files/coping-2-installation.pdf), primary). Cleat LF equals coping LF; fasteners need the stricter 12 in. unless the detail says otherwise.
- Underlayment: where sheet metal sits directly on cementitious or wood substrates the spec requires No. 30 felt (2 in. laps) and a slip sheet, and a bituminous coating on the concealed side of uncoated aluminum ([07 62 00 s.2.3, 3.2, 3.3.B](../../source/specifications.pdf), project, pp.191, 193-194).
- Counterflashing: the project detail prints "counter flashing 12 in. o.c." ([A-450](../../source/drawings/Architectural/A-450-ROOF-DETAILS-Rev.0.pdf), project; the text layer does not say what is spaced, most likely the attachment, so confirm on the rendered detail). BIA says counter flashing overlaps the roof flashing a minimum of 3 in. ([BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf), primary).
- Head flashing and sills are LF per opening plus EA end dams; the head flashing must extend beyond both jambs before the end dams are formed ([BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf), primary). Use the opening schedule for ID, quantity, finished length and profile ([GPT-6 Astra q3](file://trades/07-thermal-moisture/scripts/gpt/q3.txt)).

### 3.6 Through-wall flashing

- Lap continuous flashing at least 6 in. and seal; turn up the ends of discontinuous flashing at least 1 in. for end dams; extend flashing to the exterior wall face; self-adhesive flashing laps are typically 3 to 4 in. ([BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf), primary).
- Weeps are required at the flashing level; open head-joint weeps are at least 2 in. high and recommended at no more than 24 in. o.c.; wick or tube weeps are recommended at no more than 16 in. o.c.; most building codes permit up to 33 in. o.c. ([BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf), primary). Copper Development Association guidance also gives weeps at a maximum of 24 in. o.c. and a minimum 8 in. rise ([Copper.org](https://copper.org/applications/architecture/arch_dhb/arch-details/flashings_copings/wall_flashing.php), search summary). This job prints "thru-wall flashing & weeps @ 24 in. o.c." on [A-310](../../source/drawings/Architectural/A-310-EXTERIOR-WALL-SECTIONS-Rev.0.pdf) and "weep tubes 24 in. o.c." on [A-430](../../source/drawings/Architectural/A-430-SECTION-DETAILS-Rev.0.pdf) (project); that tube spacing is wider than the 16 in. BIA recommends for tube weeps, so the weep count follows the drawing (EA = ceil(LF x 12 / 24) + 1 per run, derived) and the difference is worth flagging. Which weep type applies at which location must be read from the detail.
- At a roof-to-wall junction on a brick-veneer drainage wall, the through-wall flashing extends through the veneer, across the air space and turns up a minimum of 8 in. ([BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf), primary). Material area is LF x developed width (back leg, horizontal run, drip, hem) ([GPT-6 Astra q3](file://trades/07-thermal-moisture/scripts/gpt/q3.txt)).
- Corners: complete corner coverage must be credited against the straight runs; do not count full straight length through a corner and then add a complete corner fitting over the same coverage ([GPT-6 Astra q3](file://trades/07-thermal-moisture/scripts/gpt/q3.txt)).

### 3.7 EIFS

- Measure wall area per system (EIFS-1, EIFS-2, soffit) from elevations; deduct openings to the EIFS termination, not necessarily to the rough opening; add jamb/head/sill returns separately where EIFS wraps them ([GPT-6 Astra q1](file://trades/07-thermal-moisture/scripts/gpt/q1.txt), convention). Treat shallow aesthetic reveals as LF by profile, not as extra area (same source, convention).
- Board: this spec allows boards of not more than 24 x 48 in. (8 SF), oriented with long edges horizontal in running bond, no piece narrower than 12 in. or shorter than 6 in., board joints offset 6 in. from horizontal and 4 in. from vertical sheathing joints ([07 24 13 s.2.3, 3.5](../../source/specifications.pdf), project, pp.154, 156-157). Sto's EPS board is 2 x 4 ft, offset 6 in. from sheathing joints, with L-shaped boards around openings ([Sto EPS bulletin](https://www.buildsite.com/pdf/stocorp/Sto-Expanded-Polystyrene-EPS-Insulation-Board-Product-Data-2970965.pdf), primary). Boards = SF x (1 + waste) / 8 for 2 x 4 ft (derived).
- Adhesive: applied not less than 1/4 in. thick for factory-mixed (3/8 in. field-mixed) over the entire board face ([07 24 13 s.3.5.A.1](../../source/specifications.pdf), project, p.156). One manufacturer's coverage per 60 lb, 5-gal pail of base coat: adhesive by notched trowel 160 SF, mesh embedment 280 SF (standard mesh), adhesive plus standard mesh 120 SF ([Sika LaHabra A/BC](https://usa.sika.com/dam/dms/us01/y/us-lahabra-pds-abc-base-coat.pdf), primary). Use the product data of the selected system (Dryvit Outsulation Plus MD on this job); no Dryvit coverage figure was retrievable.
- Base coat: the project spec requires not less than 1/16 in. dry thickness ([07 24 13 s.3.6.A](../../source/specifications.pdf), project, p.158); Dryvit's listing for its systems requires the mesh fully embedded with final base-coat thickness of at least 2 mm (1/12 in.) ([Dryvit Category 1 listing](https://www.dryvit.com/media/Dryvit/Resources/Model%20Building%20Codes/dryvit-category-1.pdf), primary), so the manufacturer's figure is the thicker. Dead-load weights for the Dryvit layers are in the manufacturer's bulletin ([Dryvit D.26.02](https://www.dryvit.com/resource/download/bulletin_s-25-01_deadload-calculation-eifs-bulletin.pdf), primary).
- Mesh: field mesh overlapped not less than 2-1/2 in., no laps within 8 in. of corners; strip mesh around openings extending 4 in. beyond the perimeter; a 9 x 12 in. diagonal strip at each re-entrant opening corner (so 4 per rectangular opening, derived); an 8 in. wide strip at inside and outside corners unless the base mesh is lapped at least 4 in. each side; board edges wrapped with mesh 2-1/2 in. onto front and back faces ([07 24 13 s.3.5.A.14, 3.6](../../source/specifications.pdf), project, pp.157-158). Dryvit's listing names Standard, Standard Plus and Intermediate meshes at 150-372 g/m2 (0.49-1.22 oz/sq ft) with edges overlapped 3 in. minimum (the project spec says 2-1/2 in.), and Panzer heavier meshes (1.6-2.2 oz/sq ft) added for impact zones ([Dryvit Category 1 listing](https://www.dryvit.com/media/Dryvit/Resources/Model%20Building%20Codes/dryvit-category-1.pdf), primary). Mesh SF = wall SF x (1 + lap allowance) plus the strip LF x strip width (derived); the more stringent of the 2-1/2 in. and 3 in. laps applies.
- Trim: PVC drip screed/track at bottom edges, casing bead elsewhere, expansion joints where drawn ([07 24 13 s.3.4](../../source/specifications.pdf), project, p.156); sealant joints formed with back-to-back casing beads ([s.3.5.A.13](../../source/specifications.pdf), project, p.157). Take trim in LF; add 10 ft stock length at purchase (the app engine uses 10 ft accessories, `exterior-cladding.accessory-piece-ft`).
- EIFS must not bridge expansion joints in the substrate, and gaps between boards are filled with insulation slivers, never with base coat or adhesive ([Construction Specifier](https://www.constructionspecifier.com/tips-for-success-with-exterior-insulation-and-finish-systems/2/), secondary).
- EPS thickness limits: Dryvit lists EPS up to 6 in. maximum in its tested assemblies ([Dryvit Category 1 listing](https://www.dryvit.com/media/Dryvit/Resources/Model%20Building%20Codes/dryvit-category-1.pdf), primary); this job's 3 in. and 5 in. EIFS thicknesses are inside that.

### 3.8 ACM (metal composite material) wall panels and canopy

- Take off in SF of panel face per color/finish and panel type, plus LF of sub-girts, trim, flashings and sealed joints. The senior-estimator view is to keep three labels distinct: projected facade area, actual exposed face area, and fabrication blank area ([GPT-6 Astra q1](file://trades/07-thermal-moisture/scripts/gpt/q1.txt)).
- Panel: this spec calls 0.157 in. (4 mm) panel thickness, fire-retardant core, 0.020 in. aluminum facings, two-coat fluoropolymer ([07 42 13 s.2.2](../../source/specifications.pdf), project, pp.173-174); Reynobond FR 4 mm weighs about 1.55 lb/sq ft ([Arconic fabrication guide](https://arconic.com/documents/d/aap-northamerica/fabricationguidelines_reynobond), primary).
- Sheet limits: widths 34 to 62 in. and lengths up to 20 ft 3 in. for Reynobond FR ([ICC-ES ESR-3435](https://www.icc-es.org/wp-content/uploads/report-directory/ESR-3435.pdf), search summary), so a typical layout is one panel face per sheet, not 4x8.
- Rout-and-return fabrication routes a groove at a constant 1 in. from the edge, folds a 1 in. deep return, and clip angles are attached about 12 in. o.c.; recommended minimum joint width 5/8 in. ([Arconic fabrication guide](https://arconic.com/documents/d/aap-northamerica/fabricationguidelines_reynobond), primary). Blank area with 1 in. returns all around = (W + 2)(H + 2) / 144 SF (derived): 48 x 96 in. face is 32.0 SF, blank 34.0 SF (+6.3%); 24 x 48 in. is 8.0 SF, blank 9.0 SF (+12.8%). The spec only says "Attachment Assembly: Manufacturer's standard" ([07 42 13 s.2.2.C](../../source/specifications.pdf), project, p.174) and the drawings key "ACM extrusion & clips" ([A-430](../../source/drawings/Architectural/A-430-SECTION-DETAILS-Rev.0.pdf), project), so whether returns apply (and how deep) must be read from the details; the returns above are Arconic's rout-and-return values, not a project requirement.
- Sub-girt/furring is LF by member from the layout; panel area alone is not a sub-girt quantity ([GPT-6 Astra q1](file://trades/07-thermal-moisture/scripts/gpt/q1.txt)). Canopy fascia is carried in LF with its developed profile (this job: 12 in. top x 12 in. front x 6 in. base, [lines.json](../../reference/estimate/lines.json) line 183).

### 3.9 Water-resistive, air and vapor barriers

- Sheet WRB (building wrap): seams lapped and taped; barrier laps vertical flashing at least 4 in.; flexible flashing laps at least 4 in.; cut back 1/2 in. each side of control joints ([07 25 00 s.3.1-3.2](../../source/specifications.pdf), project, pp.160-161).
- Fluid-applied air barrier: total dry film not less than 35 mils applied in one or more coats ([07 27 26 s.2.3-2.4, 3.4](../../source/specifications.pdf), project, pp.166-169). Coverage rate must be taken from the product: Tremco ExoAir 230 on exterior sheathing is minimum 48 wet mils (25 dry) at 33 SF/gal, and on porous substrates minimum 70 wet mils (35 dry) at 23 SF/gal; solids 0.53 ([Tremco ExoAir 230 data sheet](https://tremcosealants.com/resource/download/ExoAir_230_230LT_DS.pdf), primary). The spec's basis-of-design is GCP Perm-A-Barrier, so that product's data sheet governs. Gallons = SF / (SF per gal at the specified dry mils) x (1 + waste) (derived).
- Accessories that follow from the barrier: primer; transition strips with at least 3 in. coverage over each substrate; an additional 6 in. wide transition strip sealing the top of through-wall flashing to the barrier; termination mastic at the top edge; foam sealant at frame gaps; 6 in. patches beyond repairs ([07 27 26 s.3.3](../../source/specifications.pdf), project, pp.168-169). Take transition strips in LF by width: opening perimeters, roof-to-wall transitions and through-wall flashing tops.
- Below-grade (under-slab) vapor retarder: 15 mil Class A sheet (ASTM E 1745), joints overlapped 6 in. and taped, 6 in. patches taped on all four sides, penetration seals ([07 26 16 s.2.2, 3.2](../../source/specifications.pdf), project, p.163). SF = slab area + lap-over-footing allowance; tape LF = seam length (roll width). A 14 ft x 100 ft roll is a common size for this class of product but was not verified against the Stego sheet ([StegoCrawl listing](https://www.idi-insulation.com/poly-stegocrawl-15mil-14-x100-wht-25-p.html), secondary).

### 3.10 Wall, ceiling and under-slab insulation

- Cavity insulation: SF of wall between framing and above-ceiling zones by thickness and type; the quantity is gross wall area with the openings that the sound/thermal detail omits deducted; whether framing area is also deducted is a convention that must be labeled ([GPT-6 Astra q1](file://trades/07-thermal-moisture/scripts/gpt/q1.txt), convention). The project spec extends sound-attenuation blankets over the entire ceiling and 48 in. up either side of partitions where indicated, and requires mechanical support when metal-stud cavities exceed 96 in. ([07 21 00 s.3.5-3.6](../../source/specifications.pdf), project, pp.149-150).
- Batt sizes and bags: Owens Corning R-13, 3-1/2 in. x 15 in. x 93 in. unfaced is 11 batts and 106.56 SF per bag; the 3-1/2 in. x 23 in. x 93 in. pack is 178.25 SF ([Home Depot listing](https://homedepot.com/p/Owens-Corning-R-13-Unfaced-Fiberglass-Insulation-Batt-15-in-x-93-in-10-Bags-E51/315133945) and [Luvo Home table](https://luvohome.com/products/owens-corning-r-13-un-faced-fiberglass-insulation-batts-all-sizes), secondary / search summary); coverage per bag varies by R-value and product line, so take it from the product code.
- Mineral wool sound blankets: Thermafiber SAFB is 16 x 48 in. or 24 x 48 in., thickness in 1/2 in. increments from 1.5 to 7 in. at 2.5 pcf ([Thermafiber SAFB data sheet](https://www.owenscorning.com/en/documents/uploads/thermafiber-safb-data-sheet), primary); distributor bag coverage is 96 SF for 2 in. and 64 SF for 3 in. in 24 x 48 ([Service Partners 2 in.](https://shop.service-partners.com/item/thermafiber-919692-tfsafb224) and [3 in.](https://shop.service-partners.com/item/thermafiber-919380-tfsafb324), search summary); these imply 12 and 8 pieces per bag (derived).
- Under-slab XPS: ASTM C 578 Type IV, 25 psi (project, [07 21 00 s.2.1](../../source/specifications.pdf), p.147), R-5 per inch long-term ([Owens Corning FOAMULAR 250 NGX listing](https://www.idi-insulation.com/xps-oc-f-250-ngx-1x48x96-se-48-u.html), search summary); 48 x 96 in. boards (same listing). Loose-laid on horizontal surfaces with staggered end joints and, if not otherwise indicated, extended a minimum of 24 in. in from exterior walls ([07 21 00 s.3.3](../../source/specifications.pdf), project, p.149). Boards = SF x (1 + waste) / 32.
- Foam board in cavity walls is adhered with adhesive pads about 24 in. o.c. both ways ([07 21 00 s.3.4](../../source/specifications.pdf), project, p.149).
- Rigid insulation behind exterior finishes, R-value per inch: designer's ComCheck uses polyiso 5.7, EPS 3.85 and XPS 5 per inch, so "R-12 EIFS" implies about 3 in. and "R-10 rigid" 2 in. XPS ([G-003](../../source/drawings/General/G-003-COMCHECK-Rev.0.pdf), project).

### 3.11 Joint sealants and backer rod

- Measure the actual LF of each required bead, grouped by joint width x depth and sealant type; interior and exterior perimeters are separate beads; do not count a shared joint twice ([GPT-6 Astra q3](file://trades/07-thermal-moisture/scripts/gpt/q3.txt)).
- Yield formula: package volume (in^3) / (joint width x depth x 12) = LF per package; 1 US fl oz = 231/128 = 1.8047 in^3 (derived). Checks: 20 fl oz sausage at 1/4 x 1/4 in. = 48.1 LF; at 1/4 x 1/2 in. = 24.1 LF; at 1/2 x 1/2 in. = 12.0 LF (derived), matching a distributor chart of 48, 24 and 12 LF for the same joints, and 25, 12 and 6.2 LF for a 10.3 oz cartridge ([PK Supplies chart](https://www.pksupplies.com/guides/sealant-estimator-chart.html), secondary).
- Joint design: sealant depth is measured from the top of the joint to the top of the backer rod; the recommended width-to-depth ratio is 2:1, bead tooled to an hourglass; if joint depth exceeds 1/2 in., backer rod is required ([Tremco](https://www.tremcosealants.com/blog/how-to-use-sealant-calculators-to-estimate-product-needs), primary; [PK Supplies](https://www.pksupplies.com/guides/sealant-estimator-chart.html), secondary). NIH's joint-design guidance gives a 2:1 width to rod-setback ratio and a maximum setback of 3/8 in. ([NIH sealant joints part 2](https://orf.od.nih.gov/TechnicalResources/Documents/News%20to%20Use%20PDF%20Files/2021%20NTU/Sealant%20Joints%20%e2%80%93%20Part%202%20Joint%20Design-March%202021%20News%20to%20Use_508.pdf), search summary). Backer rod is typically sized about 25% larger than the joint width ([backer rod glossary](https://projul.com/terms/backer-rod/), search summary, vendor-level).
- Backing is ASTM C 1330 Type C closed-cell, with no gaps between rod ends ([07 92 00 s.2.6, 3.3.C](../../source/specifications.pdf), project, p.206 and the installation page that follows).
- Acoustical sealant goes in continuous beads at both faces of partitions at perimeters and through penetrations ([07 92 00 s.3.3.G](../../source/specifications.pdf), project, p.209); distributor data list about 85 LF of bead per 29 oz tube for USG Sheetrock acoustical sealant ([Service Partners](https://shop.service-partners.com/item/sheetrock-030250-usgacoseal-29oz), search summary).
- Sealant schedule: traffic-grade urethane for exterior horizontal traffic joints (concrete slab isolation and contraction joints), neutral-cure silicone Class 50 for exterior vertical joints (masonry control joints, perimeters of doors/windows), latex for interior vertical joints, mildew-resistant silicone at plumbing fixtures, acoustical sealant where indicated ([07 92 00 s.3.5](../../source/specifications.pdf), project, p.209).

---

## 4. Waste factors and their basis

| Material | Allowance seen | Basis |
|---|---|---|
| Sealant (field application) | 10-15% unknown applicator; 20-25% new; 10-15% average; 0-5% highly experienced | [Tremco](https://www.tremcosealants.com/blog/how-to-use-sealant-calculators-to-estimate-product-needs) (primary). App default 10% (`sealants`). |
| Roofing membrane after explicit laps and flashing | 5-10% simple; 10-15% cut-up | Estimator convention ([GPT-6 Astra q2](file://trades/07-thermal-moisture/scripts/gpt/q2.txt)); generic take-off guide gives 5-10% for covering materials ([take-off guide via search](https://wiki.uep.edu.py/Download_PDFS/taking/705655/Off%20Quantities%20For%20Roof.pdf), secondary, low quality); GAF says its suggested waste "is based on the roof complexity" and excludes extra material for ridges, hips and valleys ([GAF sample report](https://www.gaf.com/en-us/document-library/documents/brochures-&-literature/quick_measure_sample_roof_report-commercial.pdf), search summary). App default 5% (`roofing`). |
| Roof insulation boards | 3-5% simple; 5-10% cut-up (each layer) | Convention ([GPT-6 Astra q2](file://trades/07-thermal-moisture/scripts/gpt/q2.txt)). App default 5% (`roofing-insulation`). |
| Cover board | 3-5% simple; 5-10% cut-up | Convention ([GPT-6 Astra q2](file://trades/07-thermal-moisture/scripts/gpt/q2.txt)). |
| Tapered insulation | 5-10% simple; 10-15% complex; reconcile with the manufacturer's layout | Convention ([GPT-6 Astra q2](file://trades/07-thermal-moisture/scripts/gpt/q2.txt)). |
| Fasteners and plates | 3-5% | Convention ([GPT-6 Astra q2](file://trades/07-thermal-moisture/scripts/gpt/q2.txt)). |
| Bonding adhesive | 5-10% beyond the stated coverage | Convention ([GPT-6 Astra q2](file://trades/07-thermal-moisture/scripts/gpt/q2.txt)); coverage itself is manufacturer data (section 5). |
| EIFS components | 5-10% | One calculator recommends 5-10% for cuts and errors ([Search summary of an EIFS calculator](https://www.ultimatefinancecalculator.com/calculators/eifs-coverage-calculator), secondary, low quality); app default 10% (`exterior-cladding`). |
| ACM panels | Layout-driven; use panel blank area, not a flat %; returns add 5-13% to face area for 1 in. returns | [Arconic](https://arconic.com/documents/d/aap-northamerica/fabricationguidelines_reynobond) (primary), derived in 3.8. |
| Metal flashing/coping | Laps are explicit in piece lengths; do not add a lap percentage on top | [GPT-6 Astra q3](file://trades/07-thermal-moisture/scripts/gpt/q3.txt). App default 5% (`roofing-sheet-metal`). |
| Batts and rigid insulation | 5% | App default (`insulation`); no independent source retrieved. |
| Backer rod | cut and end waste explicit | [GPT-6 Astra q3](file://trades/07-thermal-moisture/scripts/gpt/q3.txt). |

Rule shared with the app: apply waste once, after aggregating the same material across all records, then round to packages once.

---

## 5. Coverage and yield factors (primary where noted)

| Item | Figure | Source |
|---|---|---|
| TPO rolls | 10 x 100 ft (1,000 SF), 10 x 200 ft, 12 ft 4 in x 100 ft (1,233.3 SF, derived), 12 ft 4 in x 200 ft; 45 mil = 0.23 lb/SF, 60 mil = 0.31 lb/SF | [Elevate UltraPly data](https://www.buildsite.com/pdf/firestone/UltraPly-TPO-Membrane-Product-Data-2979480.pdf) (primary) |
| Bonding adhesive | 45-60 SF/gal on roller application to both mating surfaces; less on porous or uneven substrates | [Elevate adhesive sheet via search](https://lfportal.everettwa.gov/WebLink/0/doc/1542452/Page35.aspx) (search summary) |
| Polyiso boards | 4x4 and 4x8; LTTR 5.7 at 1 in., 8.6 at 1.5, 11.4 at 2, 14.4 at 2.5, 17.4 at 3, 20.5 at 3.5, 23.6 at 4 in. | [Mule-Hide](https://images.greenbuildingadvisor.com/app/uploads/2020/09/24230905/Mule-Hide-Poly-ISO-2-Roof-Insulation-Flat-Tapered-Product-Data-1326252.pdf) (primary) |
| Tapered polyiso | 1/8, 1/4, 1/2 in. per ft panels with listed average thickness | same |
| Cover board | 4x4, 4x8; 1/4, 1/2, 5/8 in.; 1.2 / 2.0 / 2.5 lb/SF | [Kingspan DensDeck Prime](https://a-us.storyblok.com/f/572366803407467/x/727046ea6d/kingspan-densdeck-prime-roof-board-data-sheet-en-us-issue-1.pdf) (primary) |
| Roof insulation fasteners | Table in 3.4 | [JM RS-7388](https://JM.COM/content/dam/jm/global/en/commercial-roofing/Fastening-Patterns/RS-7388_2x4-Roof-Insulation-Fastening-Placement.pdf), [Mule-Hide](https://images.greenbuildingadvisor.com/app/uploads/2020/09/24230905/Mule-Hide-Poly-ISO-2-Roof-Insulation-Flat-Tapered-Product-Data-1326252.pdf) (primary) |
| Fluid-applied air barrier | 33 SF/gal at 48 wet mils (sheathing); 23 SF/gal at 70 wet mils (porous); solids 0.53 | [Tremco ExoAir 230](https://tremcosealants.com/resource/download/ExoAir_230_230LT_DS.pdf) (primary) |
| EIFS base coat/adhesive | 160 SF/pail adhesive (notched trowel); 280 SF/pail standard mesh embedment; 120 SF/pail adhesive plus standard mesh (60 lb, 5-gal pail) | [Sika LaHabra A/BC](https://usa.sika.com/dam/dms/us01/y/us-lahabra-pds-abc-base-coat.pdf) (primary; another manufacturer than the job's Dryvit, use as a sanity check) |
| EIFS board | 2 x 4 ft; thickness in 1/2 in. increments; R-3.6 per inch | [Sto EPS bulletin](https://www.buildsite.com/pdf/stocorp/Sto-Expanded-Polystyrene-EPS-Insulation-Board-Product-Data-2970965.pdf) (primary) |
| EIFS dead load (system weight, sanity check) | Dryvit adhesive 0.5 psf, base coat plus mesh 1.1 psf, EPS 0.083 psf per inch | [Dryvit D.26.02](https://www.dryvit.com/resource/download/bulletin_s-25-01_deadload-calculation-eifs-bulletin.pdf) (primary) |
| ACM | 4 mm FR = 1.55 lb/SF; rout-and-return 1 in. returns; clips 12 in. o.c.; joint min 5/8 in. | [Arconic](https://arconic.com/documents/d/aap-northamerica/fabricationguidelines_reynobond) (primary) |
| Sealant | 20 fl oz sausage: 48 / 24 / 12 LF at 1/4x1/4, 1/4x1/2, 1/2x1/2; 10.3 fl oz cartridge 25 / 12 / 6.2 LF | [PK chart](https://www.pksupplies.com/guides/sealant-estimator-chart.html) (secondary); formula derived in 3.11 |
| Batts | R-13 15x93 in.: 106.56 SF/bag (11 batts) | [Home Depot](https://homedepot.com/p/Owens-Corning-R-13-Unfaced-Fiberglass-Insulation-Batt-15-in-x-93-in-10-Bags-E51/315133945) (secondary) |
| SAFB mineral wool | 16 x 48 or 24 x 48 in.; 2 in. bag 96 SF, 3 in. bag 64 SF | [OC data sheet](https://www.owenscorning.com/en/documents/uploads/thermafiber-safb-data-sheet) (primary); [distributor](https://shop.service-partners.com/item/thermafiber-919692-tfsafb224) (search summary) |
| XPS | R-5 per inch; 48 x 96 in. boards | [IDI/Owens Corning listing](https://www.idi-insulation.com/xps-oc-f-250-ngx-1x48x96-se-48-u.html) (search summary) |

---

## 6. Material breakdown an estimator lists

Primary material, then the components that follow from it:

- **TPO roof (fully adhered, mechanically fastened first insulation layer)**: field membrane; base flashing sheet (55 mil); bonding adhesive (field and flashing); walkway pad; pipe boots/cone-and-vent flashings; preformed inside and outside corners; T-joint covers; lap sealant; pourable sealer; termination bar/reglet and fasteners; drain flashing and clamping ring seal; intermediate fastening at 5 ft; polyiso layers (flat, tapered, crickets); cover board; insulation fasteners and plates; vapor barrier or air/vapor barrier where drawn; curbs, curb insulation, wood nailers (carpentry), hatch ([07 54 23 s.2.3-2.6](../../source/specifications.pdf), project, pp.182-184; [07 72 00](../../source/specifications.pdf), project, pp.197-199).
- **Sheet metal at roof**: coping, cleats (continuous), splice/back-up plates (6 in.), corners (shop mitered), end caps, expansion joints, sealant at splices, fasteners, felt and slip sheet, bituminous coating at dissimilar contact, counterflashing and reglet ([07 62 00](../../source/specifications.pdf), project, pp.191-194).
- **Through-wall flashing**: membrane or metal flashing, end dams, termination bar/sealant, weep tubes or open head joints, transition strip where it ties to the air barrier ([BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf), primary; [07 27 26 s.3.3.G](../../source/specifications.pdf), project, p.169).
- **EIFS**: EPS board, adhesive, base coat, field mesh, strip mesh (4 in. beyond openings, 9 x 12 in. diagonals, 8 in. corner strips, edge wrap), primer, finish coat (color and texture from drawings), drip screed, casing bead, expansion joint, back-to-back bead joints, sealant and rod at joints, flashing ([07 24 13](../../source/specifications.pdf), project, pp.154-158).
- **ACM**: panels with rout-and-return, extrusions or clips, sub-girts, fasteners, EPDM or PVC washers, gaskets/separators, closure strips, joint sealant, ACM flashing and trim, canopy fascia and soffit ([07 42 13 s.2.3-2.4](../../source/specifications.pdf), project, pp.172-174).
- **Fluid-applied barrier**: primary membrane, primer, transition strips, joint-reinforcing fabric, termination mastic, foam sealant, metal termination bars, substrate patching ([07 27 26 s.2.5](../../source/specifications.pdf), project, p.167).
- **Wall insulation**: batts or blankets by thickness and facing, tape for faced vapor retarders, mechanical support above 96 in. cavities ([07 21 00 s.3.5](../../source/specifications.pdf), project, p.149); rigid board, adhesive pads.
- **Under-slab**: XPS boards, 15 mil vapor retarder, seam tape, mastic, penetration seals ([07 21 00](../../source/specifications.pdf), [07 26 16](../../source/specifications.pdf), project).
- **Sealants**: sealant by type per schedule, backer rod by diameter, bond-breaker tape, primer, cleaners, masking tape ([07 92 00 s.2.1-2.7](../../source/specifications.pdf), project, pp.204-206).

---

## 7. Common mistakes and how to check a takeoff

- Adding laps twice: once in piece lengths or roll coverage, once as a blanket percentage ([GPT-6 Astra q3](file://trades/07-thermal-moisture/scripts/gpt/q3.txt)).
- Counting the same flashing as both field membrane and base flashing ([GPT-6 Astra q2](file://trades/07-thermal-moisture/scripts/gpt/q2.txt)).
- Measuring base flashing from the deck instead of the finished roof surface; ignoring that tapered insulation and cover board change the height ([GPT-6 Astra q1](file://trades/07-thermal-moisture/scripts/gpt/q1.txt)).
- Treating coping top width as girth; omitting return legs, hems and concealed upstands ([GPT-6 Astra q3](file://trades/07-thermal-moisture/scripts/gpt/q3.txt)).
- One splice plate per piece instead of per connection; treating every endpoint as an end cap ([GPT-6 Astra q3](file://trades/07-thermal-moisture/scripts/gpt/q3.txt)).
- Using the full cavity depth for sealant depth; ignoring that backer rod sets depth ([Tremco](https://www.tremcosealants.com/blog/how-to-use-sealant-calculators-to-estimate-product-needs), primary; [GPT-6 Astra q3](file://trades/07-thermal-moisture/scripts/gpt/q3.txt)).
- Missing the second sealant face (interior and exterior) or doubling it where only one is specified ([GPT-6 Astra q3](file://trades/07-thermal-moisture/scripts/gpt/q3.txt)).
- Reading only the spec index: here the TPO roofing and EIFS sections are absent from `spec_index.json` ([section 2](#2-which-sheets-and-spec-sections-drive-it)).
- Duplicated estimate lines: in this job's estimate the "sealant with backer rod" line appears twice with an identical 221.96 LF (lines 150 and 189), while the legend sums to 221.9 LF once (derived in section 9).
- Taking the cover board thickness from the drawing and ignoring the spec, or the reverse; the two disagree here (section 11).
- Using one fastener density for the whole roof; the zone widths and per-board counts change at perimeter and corners (3.4).
- Forgetting the sound-attenuation blanket above ceilings (48 in. up either side of partitions) and the booth ceiling ([07 21 00 s.3.6](../../source/specifications.pdf), project, p.150).

Self-checks (cross-reconciliations that catch most errors):
1. Roof SF by type on the plan equals insulation SF on layer 1 within plan-rounding; the cover-board SF equals the membrane field SF.
2. Insulation thickness x R-per-inch equals the printed R-value (6 in. x 5.7 = 34.2).
3. Coping LF equals parapet top LF measured on the roof plan; cleat LF equals coping LF; splice plates equal pieces minus runs (open runs).
4. Wall system SF (EIFS + ACM + other claddings) reconciles with the air-barrier SF plus reveals/returns, minus openings.
5. Sealant LF by joint size multiplied by joint volume reconciles with sausages or cartridges purchased.
6. Thru-wall flashing LF reconciles with the opening and wall-base schedule; weep count equals LF x 12 / 24 + 1 per run.

---

## 8. What an AI takeoff must read from drawings and specs

1. From A-140 and the roof legend: every roof type (RT1, RT2) and its build-up top to bottom (membrane, cover board, each insulation layer thickness, decking/plywood), the R-value, attachment per layer ("mechanically fastened first layer, fully adhered additional layers"), tapered/cricket areas and slope, walkway pad hatch, drain and vent counts, hatch size, RTU curbs, and parapet LF by height.
2. From A-450 and A-310/A-430 details: parapet wrap path (membrane down the outside face), coping profile and girth, cleat spacing, counterflashing detail, curb height, 8 in. termination note, 5 ft intermediate fastening note, thru-wall flashing rise and weep spacing, EIFS termination, ACM joint and clip details, sill pan details.
3. From the elevations: EIFS and ACM areas by tag, opening sizes (to deduct and to size flashing/sealant/mesh strips), reveals, canopy/fascia.
4. From wall sections: stud depth, batt thickness and facing, vapor barrier and fluid-applied barrier sheets, rigid thickness and R-value, EIFS thickness.
5. From G-003 and S-201: R-values per inch and the slab extent for under-slab insulation (and whether it applies; the G-003 note is conditional on climate zone, "where required zones > 4").
6. From the specifications: product types and thicknesses (60 mil TPO; 55 mil sheet flashing; polyiso ASTM C 1289 Type II Class 1 Grade 2; cover board; 0.040 in. aluminum coping; 4 mm ACM; 35 mil air barrier; 15 mil vapor retarder), board sizes, layer rules (2.7 in. rule), laps and offsets, spacing (cleats, hangers, movement joints), and the sealant schedule.
7. Wind uplift pressures ("as indicated on Drawings") and building dimensions to size perimeter and corner zones.
8. Revision awareness: this is a Rev 0 permit set dated 07/02/2026 (title block of A-140 and the spec headers); re-run if sheets change.

AI input checklist: (1) roof areas by type and layer thickness; (2) parapet/wall LF by height and detail; (3) coping, counterflashing, head and sill LF by profile and corner/end counts; (4) EIFS, ACM, barrier SF by tag with each opening's size and return depth; (5) sealant LF by joint width and depth and by sealant type; (6) curb/hatch/drain/vent counts and sizes; (7) tapered/cricket footprints and slope; (8) the convention used for each allowance; (9) the source (sheet or spec page) for every number.

---

## 9. Calibration against this job's estimator (quantities only, from `reference/estimate/lines.json` and `reference/markups/legends.json`)

Derived in Python:
- The estimator carries net quantities that equal the legend measurements: roof types RT1 1,864.3 SF and RT2 285.4 SF (sum 2,149.7 SF) against estimate polyiso lines 1,864 and 285 SF and "vapor barrier at roof, assumed" 2,149.28 SF; walkway pad 286.79 versus 286.8 SF; thru-wall flashing 213.07 versus 213.1 LF (101.6 + 111.5); aluminum flashing 101.18 versus 101.2; pre-finished sill 48.27 versus 48.3 LF; EIFS-1 1,640 versus 1,638.9 SF, EIFS-2 275 versus 274.4 SF; ACM 490 versus 488.3 SF and canopy 360 versus 358.7 SF. No waste, no roll or board rounding.
- Membrane: line 162 is 3,042.774 SF, which is 893.5 SF (41.6%) more than the 2,149.28 SF field. Parapet laps on the legend (43.3 LF x 2'-1", 56.5 x 1'-0", 87.8 x 3'-6", 45.3 x 2'-0") total 544.6 SF and parapet walls on the legend (38 x 2'-7", 46 x 1'-7", 96.6 x 4'-7") total 613.8 SF; curb 39.9 LF x 18 in. is 59.9 SF. These components were not reconciled to the 893.5 SF with certainty, so the flashing developed-width rule used by the estimator ("with additional layer") needs an owner's decision.
- Insulation: 6 in. polyiso on RT1 is two layers or more (spec 2.7 in. rule); the estimate carries one SF line, so board counts per layer = SF / 32 per layer (RT1: 58.26 boards per layer, derived). R-34 = 6 x 5.7 = 34.2.
- Cover board: 1,956 SF, which is 91.7 SF (4.9%) above RT1's 1,864.3 SF; the estimate line is 1/4 in. while the spec requires 1/2 in. (section 11).
- Crickets: 262.06 SF of tapered polyiso as a separate line.
- Coping: 203 LF in three girths (15 + 148 + 40) versus legend 200.5 LF (38.5 + 148.1 + 13.9).
- Under-slab XPS: 2,298 SF versus slab on grade 1,917.6 SF on the legend (ratio 1.198); the note says the insulation detail was "taken from Section 1/G003," so the extra 380 SF is unexplained (perimeter and thickened edges are a possible reading, not verified).
- Fluid-applied barrier: 2,983.5 SF versus EIFS (1,925) + wall ACM (490) + canopy ACM (360) = 2,775 SF; difference 208.5 SF (barrier at returns or other walls; not verified).
- "2 in. rigid insulation behind exterior finish": 890 SF, much less than the EIFS area (1,925 SF), so it is a different wall (probably the ACM and masonry walls with XPS R-10 on G-003).
- Sealant with backer rod: legend 65.7 + 156.2 = 221.9 LF; estimate lines 150 and 189 both 221.96 LF (a likely duplicate). "Continuous sealant at opening" 1,330 LF and "continuous acoustic sealant at walls" 1,053.5 LF are carried in LF only (no joint size).
- Wall batts: 8 in. batt 2,652.9 SF, 5-1/2 in. 113.3 SF, 3-1/2 in. 92 SF; sound blankets 3-1/2 in. 427.5 SF and 5-1/2 in. 356.25 SF; booth ceiling 6 in. 76 SF (matches the A-706 legend 76.2 SF).
- Counts: 11 roof-drain flashings, 3 vent-pipe flashings, 1 roof hatch (30 x 36 in.), curbs 40 LF (18 in.) and 11 LF (hatch).

Relation to the app engine (`lib/quantities/trades/structure`; not edited): the engine's roofing assemblies take `parapetLap` 12 in., base flashing height 8 in., side lap 3 in., 10 x 100 ft roll, 0.25 / 0.375 / 0.5 fasteners per SF for field/perimeter/corner insulation (8/12/16 per 4x8), cover board 4x8, coping piece 10 ft, and 5% waste classes. Of these, the 8 in. height, 10 ft coping piece and roll size agree with the sources above; the perimeter and corner fastener densities (0.375 and 0.5 per SF) are lower than the JM prescriptive enhancement rows (0.5 to 0.75 per SF perimeter and 1.0 per SF corner), and the adhered-system rule in Mule-Hide (16 per 4x8 under a top layer thinner than 2 in., 8 per 4x8 at 2 in. or thicker) is not in the engine's conventions. These are suggestions for the formulas reconciliation, not edits.

---

## 10. Conflicts and open questions

- Cover board thickness: [A-140](../../source/drawings/Architectural/A-140-ROOF-PLAN-Rev.0.pdf) RT1 shows 1/4 in. cover board and the estimate carries 1/4 in. (line 163), but [07 54 23 s.2.6.C](../../source/specifications.pdf) calls for 1/2 in. glass-mat gypsum (DensDeck) (project, p.184). Per the precedence rule in the repo's CLAUDE.md the drawing and spec conflict is for the estimator to settle; the AI must flag it, not choose.
- Roofing manufacturer: spec basis-of-design is Firestone UltraPly (now Elevate) with Carlisle, GAF and JM as equals ([07 54 23 s.2.1](../../source/specifications.pdf), project, p.182); lap widths, adhesive rates and fastening patterns differ by manufacturer.
- Perimeter-zone width: 4 ft minimum (Tremco) versus 3 ft minimum (ASCE 7 per SPRI) ([sources in 3.4](#34-fastening-zones-and-counts)); and the corner-zone width was not confirmed from a primary source.
- Cleat spacing: 24 in. (07 62 00 s.3.4.B) versus 12 in. (s.3.3.A.3) versus Englert's 12 in. (section 3.5).
- Coping piece length: spec allows up to 12 ft but requires movement joints at maximum 10 ft (section 3.5).
- Weep spacing: 24 in. is printed on the details for both through-wall flashing and weep tubes; BIA TN 7 recommends no more than 24 in. for open head-joint weeps but 16 in. for wick or tube weeps, and notes codes permit up to 33 in. (section 3.6).
- EIFS mesh lap: 2-1/2 in. in the project spec versus 3 in. minimum in Dryvit's listing (section 3.7).
- Roof curbs: spec calls for aluminum curbs with factory insulation and nailer (07 72 00) while the estimate carries "prefabricated metal curb" with a separate 2x4 pressure-treated nailer and "insulated substrate" (lines 171-172); who furnishes the curb (roofing, HVAC) must be settled before counting.
- Opening-deduction rule: no standard; the AI should apply actual-net deductions and label any threshold (section 3.1).
- EIFS and ACM coverage per pail/panel for the job's own products (Dryvit Outsulation Plus MD, Reynobond) were not retrievable; Sika LaHabra figures are a cross-check only.
- Several pages were seen only as search summaries (marked) because fetches returned 403 or the web-search budget for this run was exhausted. Items to re-verify when the budget allows: ASCE 7 corner-zone width, ASTM C 1193 backer-rod sizing and 1/4 in. minimum depth, BIA TN 7 numeric weep spacing, SMACNA lap widths and coping girth conventions, FM 1-29 zone widths, ACM standard sheet sizes for the specified products, Stego roll sizes and tape/mastic coverage.
- The GPT-6 Astra pass was used for conventions and cross-checks only; any claim cited only to it is unverified convention.

---

## Sources

Project documents (this repository):
- Specifications: [`source/specifications.pdf`](../../source/specifications.pdf), sections 07 21 00 to 07 92 00 (pages as cited).
- Drawings: [A-140](../../source/drawings/Architectural/A-140-ROOF-PLAN-Rev.0.pdf), [A-450](../../source/drawings/Architectural/A-450-ROOF-DETAILS-Rev.0.pdf), [A-310](../../source/drawings/Architectural/A-310-EXTERIOR-WALL-SECTIONS-Rev.0.pdf), [A-430](../../source/drawings/Architectural/A-430-SECTION-DETAILS-Rev.0.pdf), [A-200](../../source/drawings/Architectural/A-200-EXTERIOR-ELEVATIONS-Rev.0.pdf), [A-201](../../source/drawings/Architectural/A-201-EXTERIOR-ELEVATIONS-Rev.0.pdf), [A-706](../../source/drawings/Architectural/A-706-BOOTH---ENLARGED-PLAN-&-DETAILS-Rev.0.pdf), [G-003](../../source/drawings/General/G-003-COMCHECK-Rev.0.pdf), [S-201](../../source/drawings/Structural/S-201-Structural-Plan---Foundation-Rev.0.pdf).
- Ground truth: [`reference/estimate/lines.json`](../../reference/estimate/lines.json) (lines 148-189, quantities and descriptions only), [`reference/markups/legends.json`](../../reference/markups/legends.json).
- App engine for comparison: `TakeoffSpeed repo: lib/quantities/trades/structure/{roofing,insulation,sealants,exterior-cladding}.ts`, `docs/QUANTITY_ENGINE.md`.

External sources read (primary):
- [Tremco, How to use sealant calculators](https://www.tremcosealants.com/blog/how-to-use-sealant-calculators-to-estimate-product-needs)
- [Tremco ExoAir 230/230LT data sheet](https://tremcosealants.com/resource/download/ExoAir_230_230LT_DS.pdf)
- [Tremco detail 14, perimeter and corner layout](https://tremcoroofing.com/media/Roofing/Detail%20Drawings/TremPly%20Single%20Ply%20Roofing%20Systems/Application/TremPly%20KEE%20Single%20Ply%20Roofing%20Systems/PDFs/Class-1-90-or-more,-General-Perimeter-and-Corner-Layout.pdf)
- [Johns Manville RS-7388 fastener placement, 2 x 4 ft boards](https://JM.COM/content/dam/jm/global/en/commercial-roofing/Fastening-Patterns/RS-7388_2x4-Roof-Insulation-Fastening-Placement.pdf)
- [Mule-Hide Poly ISO 2 product data](https://images.greenbuildingadvisor.com/app/uploads/2020/09/24230905/Mule-Hide-Poly-ISO-2-Roof-Insulation-Flat-Tapered-Product-Data-1326252.pdf)
- [Kingspan DensDeck Prime data sheet](https://a-us.storyblok.com/f/572366803407467/x/727046ea6d/kingspan-densdeck-prime-roof-board-data-sheet-en-us-issue-1.pdf)
- [Elevate (Firestone) UltraPly TPO product data](https://www.buildsite.com/pdf/firestone/UltraPly-TPO-Membrane-Product-Data-2979480.pdf)
- [SPRI wind design slides, ASCE 7](https://www.spri.org/wp-content/uploads/2023/10/2-2023-WDS-ASCE-7_Chamberlain.pdf)
- [Englert coping installation](https://www.englertinc.com/sites/default/files/coping-2-installation.pdf)
- [BIA Technical Note 7, water penetration resistance](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf)
- [Arconic Reynobond fabrication guidelines](https://arconic.com/documents/d/aap-northamerica/fabricationguidelines_reynobond)
- [Sika LaHabra A/BC base coat](https://usa.sika.com/dam/dms/us01/y/us-lahabra-pds-abc-base-coat.pdf)
- [Dryvit Category 1 listing](https://www.dryvit.com/media/Dryvit/Resources/Model%20Building%20Codes/dryvit-category-1.pdf)
- [Dryvit dead load estimation D.26.02](https://www.dryvit.com/resource/download/bulletin_s-25-01_deadload-calculation-eifs-bulletin.pdf)
- [Sto EPS insulation board bulletin](https://www.buildsite.com/pdf/stocorp/Sto-Expanded-Polystyrene-EPS-Insulation-Board-Product-Data-2970965.pdf)
- [Owens Corning Thermafiber SAFB data sheet](https://www.owenscorning.com/en/documents/uploads/thermafiber-safb-data-sheet)

External sources, secondary or search-summary only (not read in full):
- [PK Supplies sealant estimator chart](https://www.pksupplies.com/guides/sealant-estimator-chart.html) (read; distributor)
- [Construction Specifier, EIFS tips](https://www.constructionspecifier.com/tips-for-success-with-exterior-insulation-and-finish-systems/2/) (read; trade magazine)
- [PIMA TB 118](https://www.polyiso.org/page/TB118) (403)
- [GAF roof-to-wall flashing blog](https://www.gaf.com/en-us/blog/commercial-roofing/roof-to-wall-flashing-why-details-matter-for-single-ply-roofing-systems-04873b23-f26d-4119-b9c7-1d56c2da7484) (403)
- [GAF TPO hybrid flashing detail](https://www.gaf.com/en-us/document-library/documents/details/tpo-hybrid-flashing-at-base-of-wall-or-curb-detail-075423-931.pdf)
- [VA 07 54 23 master spec](https://www.wbdg.org/FFC/VA/VAASC/VA%2007%2054%2023.pdf)
- [GAF commercial sample roof report](https://www.gaf.com/en-us/document-library/documents/brochures-&-literature/quick_measure_sample_roof_report-commercial.pdf)
- [Roofing Contractor, flashing methods](https://roofingcontractor.com/articles/86566-proper-flashing-methods-for-low-slope-roofs) (appeared in search results only; no claim above rests on it)
- [Take-off guide (scraped copy)](https://wiki.uep.edu.py/Download_PDFS/taking/705655/Off%20Quantities%20For%20Roof.pdf)
- [Mule-Hide DensDeck Prime page](https://www.mulehide.com/Products/p/DensDeckPrimeRoofBoard)
- [Elevate bonding adhesive sheet (City of Everett copy)](https://lfportal.everettwa.gov/WebLink/0/doc/1542452/Page35.aspx)
- [ATAS continuous cleat coping spec sheet](https://www.atas.com/wp-content/uploads/2018/06/Continuous-Cleat-Coping-Spec-Sheet.pdf)
- [Copper.org through-wall flashing](https://copper.org/applications/architecture/arch_dhb/arch-details/flashings_copings/wall_flashing.php) (403)
- [ICC-ES ESR-3435, Reynobond FR](https://www.icc-es.org/wp-content/uploads/report-directory/ESR-3435.pdf)
- [NIH, sealant joints part 2](https://orf.od.nih.gov/TechnicalResources/Documents/News%20to%20Use%20PDF%20Files/2021%20NTU/Sealant%20Joints%20%e2%80%93%20Part%202%20Joint%20Design-March%202021%20News%20to%20Use_508.pdf)
- [Projul, backer rod glossary](https://projul.com/terms/backer-rod/)
- [Home Depot, Owens Corning R-13 15 x 93 in. batt](https://homedepot.com/p/Owens-Corning-R-13-Unfaced-Fiberglass-Insulation-Batt-15-in-x-93-in-10-Bags-E51/315133945)
- [Luvo Home, Owens Corning R-13 batts](https://luvohome.com/products/owens-corning-r-13-un-faced-fiberglass-insulation-batts-all-sizes)
- [Service Partners, Thermafiber SAFB 2 in.](https://shop.service-partners.com/item/thermafiber-919692-tfsafb224) and [3 in.](https://shop.service-partners.com/item/thermafiber-919380-tfsafb324); [USG Sheetrock acoustical sealant](https://shop.service-partners.com/item/sheetrock-030250-usgacoseal-29oz)
- [IDI, Owens Corning FOAMULAR NGX 250](https://www.idi-insulation.com/xps-oc-f-250-ngx-1x48x96-se-48-u.html)
- [IDI, StegoCrawl 15 mil](https://www.idi-insulation.com/poly-stegocrawl-15mil-14-x100-wht-25-p.html)
- [JM R-Panel listing](https://www.bimobject.com/sv/johns-manville/product/r-panel-roof-insulation)
- [EIFS coverage calculator page](https://www.ultimatefinancecalculator.com/calculators/eifs-coverage-calculator)

Second opinion (unverified): GPT-6 Astra via `tools/ask_gpt.py`, answers saved at `trades/07-thermal-moisture/scripts/gpt/q1.txt`, `q2.txt`, `q3.txt`.
