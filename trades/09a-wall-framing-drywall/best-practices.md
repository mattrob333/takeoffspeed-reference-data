# Best practice: metal stud framing and gypsum board at walls (quantities and material types only)

Scope: non-load-bearing cold-formed steel stud and track partitions, bulkhead/canopy/booth framing, and gypsum board (plus its accessories and finishing materials) at walls and the ceilings/soffits framed with the same members. Prices, labor and productivity are out of scope.

How to read this file. Every factual claim carries a link. Where a number comes only from an estimating blog or a calculator site it is marked **(blog-level)**; where a page was found by search but not read in full it is marked **(search summary)**. Manufacturer and standards-derived figures are marked **(primary)**. Project-document citations point at files in this repository (`source/specifications.pdf`, `source/drawings/...`). Arithmetic in worked examples is mine (checked in Python) and is labelled **derived**.

Honest summary of the evidence: there is no single published "drywall takeoff standard" for opening deductions or waste. The primary, citable numbers are (1) the manufacturer coverage data (screws, tape, compound per 1,000 SF), (2) the installation standards and master specifications (spacings, heights, anchorage, control joints, finish levels), and (3) stock sizes. Everything else (deduction thresholds, waste %, stud allowances) is estimator convention, and the sources disagree. The right design for an AI takeoff is therefore: measure installed quantities from the drawings, state the convention applied, and keep waste and rounding as separate, visible steps.

---

## 1. What an estimator takes off, and in which units

| Item | Unit | Notes / basis |
|---|---|---|
| Gypsum board, by type + thickness + edge, per face, per layer | SF, then sheets (EA) by sheet size | Wall board is SF = wall LF x board height x faces x layers; a partition boarded both sides counts both faces ([Vertigraph](https://www.vertigraph.com/learn/how-to-calculate-drywall-square-footage), [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) (blog-level)). Take each board type separately (Type X, ceiling, moisture/mold resistant, cementitious) ([ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) (blog-level); project types in [09 29 00 s.2.3](#9-project-specific-what-this-set-requires)). |
| Metal studs, by depth, steel thickness (mil), spacing and cut length | EA (grouped by cut length), LF as a check | Count = (wall length / spacing) + 1 per run, then add opening framing and intersections ([NASCLA study guide](https://open-exam-prep.com/study-guides/nascla-contractor/nascla-metals-wood/nascla-9-2-light-gauge-metal-framing) (secondary), [Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step) (blog-level)). |
| Top and bottom runners (track), by depth and thickness | LF | Two runs per wall, 2 x wall length ([NASCLA](https://open-exam-prep.com/study-guides/nascla-contractor/nascla-metals-wood/nascla-9-2-light-gauge-metal-framing), [Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step)). Deflection/slip track is carried as its own line. |
| Door/opening framing: jambs, header track, cripples | EA / LF | See section 3.3. |
| Bridging, bracing, flat strap, backing plates, blocking | LF / EA | Rows set by design; see 3.5. |
| Ceiling/soffit/canopy framing: hangers, carrying channels, furring, studs/joists | EA / LF | Spacings in the specification, see 3.6. |
| Corner bead, edge trim (L, LC, U), control joints | LF | Measured from the plan/elevations, not factored from SF ([ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/), [Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step), [Estimating Edge trim/corner-bead model](https://www.estimatingedge.com/knowledgebase/dw-partition-condition-properties-layer-2-trim-and-count-tabs/)) (blog-level / vendor docs). |
| Screws | lb or count; derived from board SF | Primary factor in section 5. |
| Joint tape | LF, then rolls | Primary factor in section 5; rolls come in 250 ft and 500 ft ([Sheetrock paper tape](https://sherwin-williams.com/painting-contractors/products/sheetrock-paper-joint-tape)). |
| Joint compound | gal (ready-mix) or lb (setting-type), by finish level | Primary factor in section 5. |
| Sound-attenuation insulation in the cavities | SF of cavity area, not board area | [Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step) (blog-level); belongs to the insulation line but is driven by the partition schedule. |
| Acoustical / firestop sealant at perimeters | LF of perimeter, both faces where specified | Project spec 09 29 00 s.3.2 I and A-620 notes J, K (see section 9). |

Reporting rule that avoids most disputes: always output **gross area, openings deducted (with the rule used), net area, waste %, and ordered sheets** as separate numbers ([Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step): add waste after deductions, not before; waste on gross then deducting again is listed as a common error).

---

## 2. Which sheets and spec sections drive it

Generic (any job): floor plans for partition lengths and type tags; the **partition type schedule/details** (stud depth, steel thickness, spacing, board layers/type, insulation, fire/STC rating, head and base conditions); reflected ceiling plans for gypsum ceilings, soffits, bulkheads; building sections and wall sections for heights (slab to deck vs. to ceiling); door/window schedules and elevations for openings; finish plans/schedules for finish level, tile/FRP substrates; Division 09 sections ([Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step) (blog-level); [Civils.ai](https://civils.ai/blog/how-to-use-ai-for-drywall-quantity-takeoffs/) lists plan set, scale, heights, wall-type tags, single/double layer, openings, revisions as the AI's required inputs (vendor blog)).

Spec sections (CSI): 09 22 16 Non-Structural Metal Framing; 09 29 00 Gypsum Board; 05 40 00 Cold-Formed Metal Framing for load-bearing/exterior and heavier studs ([VA 09 22 16](https://www.cfm.va.gov/TIL/spec/092216.docx): "Use this section for wall framing members of 0.75 mm (0.0296 inch) thick bare metal (20 gauge)... See Section 05 40 00 ... for 1.09 mm (0.0428-inch) (18 gauge) or heavier"). Cross-trade: 07 21 00 insulation, 09 91 00 painting (primer/finish level), 09 30 00 tile, 07 84 00 firestopping.

This job's drivers: A-110/A-120 (plans), A-130/A-131 (reflected ceiling), A-140 (roof/canopy framing), A-150 (finish plan), A-300 (building sections), A-410 (restrooms), A-430/A-440 (details), A-600 (doors), **A-620 Interior Partition Schedule & Details**, A-630 (ceiling details), A-704/A-706 (tech wall, booth) in `reference/sheets/index.json`; specs 09 22 16 (spec p.267-272) and 09 29 00 (spec p.273-282).

---

## 3. Standard measurement rules

### 3.1 Partition length and height

- Partition **height is a per-wall input, never a project constant**: partitions to the ceiling grid use the head height in the partition detail; full-height partitions run slab to deck from the building sections; partial-height and shaft walls as noted ([Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step) (blog-level); [Civils.ai](https://civils.ai/blog/how-to-use-ai-for-drywall-quantity-takeoffs/): "each wall segment takes its own height").
- Which walls run to the structure and how far board goes above the ceiling is a **specification** question. A representative master spec: all layers of board go floor to underside of structure on both sides of fire-rated, smoke, sound-rated and full-height partitions and on corridor partitions; on one side of exterior-wall furring; elsewhere board goes not less than 4 in. above suspended acoustical ceilings, and to the ceiling of suspended gypsum ceilings ([VA 09 29 00 s.3.1](https://www.cfm.va.gov/TIL/spec/092900.docx)). The same master spec extends studs to the underside of structure for fire, smoke, shaft and sound-rated partitions, cutting studs 1/4 to 3/8 in. short of the overhead structure ([VA 09 22 16 s.3.1-3.2](https://www.cfm.va.gov/TIL/spec/092216.docx)).
- Wall length from plan lines: centerline vs. face is a convention. Whichever is used, intersections and returns must be reconciled once (second-opinion model, unsourced; the failure mode of double-counting intersection studs also appears in [Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step)).
- Slopes: gable/sloped heads are measured as shapes (trapezoid/triangle) rather than at the maximum height; stud lengths step with the slope, so group studs by cut length (derived; the reference estimate for this job does exactly this, listing counts "@ 12'-6" HT", "@ 18'-8" HT", etc., in `reference/estimate/lines.json` lines 308-311).

### 3.2 Stud count and runners

- **Studs** = ceil(wall length / spacing) + 1 per straight run; 16 in. o.c. is about 0.75 studs per LF and 24 in. o.c. about 0.5 per LF ([NASCLA study guide](https://open-exam-prep.com/study-guides/nascla-contractor/nascla-metals-wood/nascla-9-2-light-gauge-metal-framing), [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/)). Derived check: a 40 ft run gives 41 studs at 12 in., 31 at 16 in., 21 at 24 in. (the NASCLA guide's 40 ft / 16 in. = 31 example agrees).
- Spacing is a drawing/spec input: a master spec limits studs to not more than 24 in. o.c. ([VA 09 22 16 s.3.2 B](https://www.cfm.va.gov/TIL/spec/092216.docx)); the project spec says 16 in. o.c. for single and multilayer unless indicated (spec 09 22 16 s.3.4 A). Spacing and stud depth/thickness must be **checked against the limiting-height table**, not chosen by habit ([ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) lists this as a common mistake). Example of how fast allowable height changes: for ClarkDietrich ProSTUD 400PDS125-15 composite walls at 5 psf and L/240, allowable height is 18'0" at 12 in., 16'4" at 16 in. and 14'4" at 24 in. o.c. ([ClarkDietrich submittal](https://www.buildsite.com/pdf/ram_sales/ProSTUD-ProTRAK-25-Ga-Submittal-Sheet-2970880.pdf)).
- **Track**: 2 x wall length for top and bottom ([NASCLA](https://open-exam-prep.com/study-guides/nascla-contractor/nascla-metals-wood/nascla-9-2-light-gauge-metal-framing)). Installed bottom track is interrupted at door openings (derived; see 3.3). Runners are fastened to floor and overhead at 24 in. o.c. max and near each end: PLU master spec "secure top and bottom runners at 24 inches (600 mm) o.c." ([PLU Div 09 spec](https://www.plu.edu/construction/wp-content/uploads/sites/128/2014/10/div-009.pdf)); a Winnipeg municipal spec says 610 mm (24 in.) max and within 50 mm (2 in.) of each end ([Winnipeg NMS 09 22 16](https://legacy.winnipeg.ca/finance/findata/matmgt/documents/2011/253-2011/253-2011_NMS_092216_Non-Structural_Metal_Framing.pdf)). These drive the **anchor/fastener count** into slab and deck, a line estimators commonly forget.
- Corners and intersections: practice is 2-3 studs per corner/intersection, but sources conflict (2 vs. 3 per corner, 4 per opening in calculator sites) ([calculator roundup (search summary)](https://homebuddy.blog/calculate-studs-for-wall)). Count the actual detail on the drawings and credit studs already counted as run-end studs; do not apply a blanket plus-10% ([ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) uses "about 10%" as a shortcut (blog-level)).
- **Stock lengths drive cut waste**: 3-5/8 in. studs are stocked in 8, 9, 10, 12, 14, 16 ft (25 ga) and up to 18 ft (20 ga); track is 10 ft ([Kuiken Brothers stock table](https://www.kuikenbrothers.com/products/commercial/steel-studs/); ClarkDietrich structural track standard 10 ft per [ClarkDietrich](https://www.clarkdietrich.com/node/402) (search summary)). A 12'-6" wall therefore needs a 14 ft stud (or a spliced pair), not 12'-6" of material. Master specs also require studs 12 ft or shorter to be one piece ([VA 09 22 16 s.2.2 D](https://www.cfm.va.gov/TIL/spec/092216.docx)), so heights above 12 ft are a different (usually structural-stud) item with splice or custom length.

### 3.3 Openings in the framing

- **Doors**: two studs per jamb unless otherwise indicated; header made from a runner (track) section for the cripple studs at the head, secured to the jamb studs; jamb studs extend through suspended ceilings to the structure where indicated; other framed openings (windows, borrowed lites) are framed the same, with framing below the sill matching the head (project spec 09 22 16 s.3.4 D, and [VA 09 22 16 s.3.2 G](https://www.cfm.va.gov/TIL/spec/092216.docx): jambs framed with two studs back to back, screwed together at about 2 ft o.c.).
- Jambs and headers are **structural-type members** even in non-load-bearing walls, and light "EQ" studs (15-27 mil) should not be used as jambs ([Walls & Ceilings, jamb studs](https://www.wconline.com/articles/96115-jamb-studs-why-are-they-so-challenging)). So an AI must read the specified gauge for jambs/headers on the door detail, not assume the field stud.
- Counting method: either count remaining segments plus opening assemblies, or start from a continuous layout and adjust; mixing the two double-counts jambs (second-opinion model, unsourced). For the estimate to tie, remember the framing is **not** reduced by the SF opening deduction: cripples above the head and below the sill remain.
- Door bucks: Estimating Edge's drywall model counts "door buck studs" as a per-door stud drop with gauge/length ([Estimating Edge](https://www.estimatingedge.com/knowledgebase/dw-partition-condition-properties-layer-2-trim-and-count-tabs/)), confirming a per-door count rather than an SF factor.

### 3.4 Head-of-wall conditions

- Where the partition goes to structure, the head is usually a **slip/deflection joint**: studs must not be axially loaded. Two common forms are written into the project spec: single long-leg (2 in.) runner with studs friction-fit and continuous bridging within 12 in. of the stud tops, or a double-runner system with an outer runner sized to friction-fit the inner (spec 09 22 16 s.2.2 D). Manufacturer head-of-wall details set a maximum 7/8 in. gap between track web and stud end, allow 1-1/2 in. of total vertical movement, and prohibit fastening board to the deflection track ([ClarkDietrich head-of-wall composite sheets (search summary)](https://nginx.pr-196.clark-dietrich-drupal.lagoon-prd.acromedia.com/sites/default/files/media/documents/CD_ProSTUD-15mil_HOW_Composite_MaxTRAK.pdf)).
- Takeoff consequence: the slip track **replaces** ordinary top track at that head (derived from the spec: "Slip-Type Head Joints: Where indicated, provide one of the following"); the deeper-leg track is a different, longer-leg item. Count it as its own LF line, with the bridging row and clips/spazzer bars as separate counts.

### 3.5 Bridging, bracing, backing

- Bridging rows are a design/spec item, not a formula. Example: one row at mid-height for partitions up to 3050 mm (about 10 ft) and maximum 1525 mm (5 ft) spacing above ([Winnipeg NMS 09 22 16](https://legacy.winnipeg.ca/finance/findata/matmgt/documents/2011/253-2011/253-2011_NMS_092216_Non-Structural_Metal_Framing.pdf)); in the VA master spec, chase-wall cross braces are studs or runners not less than 2-1/2 in. wide, and furring-stud braces are fastened with two Type S pan head screws at each bearing, with horizontal braces at not more than 3 ft vertical intervals ([VA 09 22 16 s.3.2-3.3](https://www.cfm.va.gov/TIL/spec/092216.docx)). A row is quantified as wall LF per row plus clips.
- **Backing/blocking**: framing must provide additional studs, backing plates or special shapes for fixtures, grab bars, toilet accessories, wall-hung casework, rails, recessed cabinets, door operators ([VA 09 22 16 s.3.3](https://www.cfm.va.gov/TIL/spec/092216.docx); project spec 09 22 16 s.3.3 B; flat strap/backing plate minimum 0.033 in. in project spec s.2.2 E). These come from the accessory schedules and elevations (e.g. A-410 restrooms), not from the partition length.

### 3.6 Ceilings, soffits, bulkheads, canopy and booth framing

- Spacing is given in the specification: master spec frames at 24 in. centers for gypsum board anchorage and 16 in. for metal lath ([VA 09 22 16 s.3.6](https://www.cfm.va.gov/TIL/spec/092216.docx)); the project spec gives hangers 48 in. o.c., carrying channels 48 in. o.c., furring channels 16 in. o.c. (spec 09 22 16 s.3.5 A).
- Derived formulas: a framed panel L x W with members every s feet spanning W has N = ceil(L/s) + 1 members and N x W LF (plus perimeter track); member LF is roughly area / s. For 16 in. (1.333 ft) that is 0.75 LF per SF. Hanger count = suspended area / (hanger spacing x carrying-channel spacing) plus perimeter hangers; read the drawing for obstructions.
- Ceilings and soffits are frequently missed: one source puts gypsum ceilings at 15-25% of board on some jobs ([Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step) (blog-level)).

### 3.7 Gypsum board area: openings, returns, corners

- **Opening deductions have no single standard.** The sources disagree and an AI must carry the rule explicitly:
  - USG/CGC: estimators scale each room; door and window openings are frequently "figured solid" (no deduction), with large picture windows and large door openings as exceptions ([CGC Construction Handbook ch.3 Estimating](https://www.usg.com/content/dam/USG_Marketing_Communications/canada/product_promotional_materials/finished_assets/cgc-construction-handbook-ch03-cladding-can-en.pdf)) (primary, manufacturer).
  - Deduct openings over about 32 SF; ignore standard doors/windows on the theory that cutting waste offsets them; deduct on both sides ([ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/)) (blog-level).
  - Skip openings under about 4 ft x 4 ft by judgment (the "50% rule"); always deduct storefronts and overhead doors ([Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step)) (blog-level).
  - Deduct every opening at rough-opening size; typical 3 x 6'8" door about 20 SF ([Vertigraph](https://www.vertigraph.com/learn/how-to-calculate-drywall-square-footage)) (blog-level).
  - Rule for the AI: compute both gross and net; apply a configurable threshold; never deduct a wall's openings on one face only; never apply waste to gross and then deduct again ([Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step)).
- **Returns**: ignore for jamb depth up to about 4-9/16 in. (2x4 wall); add them for deep walls (2x6 or masonry openings) ([Vertigraph](https://www.vertigraph.com/learn/how-to-calculate-drywall-square-footage)). In steel-stud work with 6 in. and 8 in. studs, returns at windows/storefront are real board; measure width x depth (derived).
- **Corners** add no SF by themselves; they add accessory LF: corner bead at all vertical and horizontal external corners (including column wraps and soffit edges) ([VA 09 29 00 s.3.5](https://www.cfm.va.gov/TIL/spec/092900.docx), [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/)). Inside corners are taped; they are not beaded.
- **Layers**: a two-layer face is 2x the board SF but 1x the finish tape/compound area (finish is taken on the exposed face; screws on each layer) ([RUH calculator note (search summary)](https://www.ruh.ai/industrial/construction/tools/drywall-calculator), [Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step) lists missing a layer as a common error). Double-layer assemblies roughly double fastener count, with longer screws for the face layer ([ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/), [Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step)) (blog-level).
- **Concealed faces**: both faces of framing in concealed spaces above ceilings get board, except chases braced internally (project spec 09 29 00 s.3.2 F). Ceiling-plenum areas are often Level 1 finish (spec s.3.7 D).
- **Sheet orientation and length**: standard sheet sizes 4x8 (32 SF), 4x10 (40), 4x12 (48), 4x14 (56), 4x16 (64) ([Vertigraph](https://www.vertigraph.com/learn/how-to-calculate-drywall-square-footage), [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/)). Specs ask for maximum practical length to minimize end joints and for vertical application over steel framing in single layer, with end joints staggered on opposite sides ([VA 09 29 00 s.3.2](https://www.cfm.va.gov/TIL/spec/092900.docx); project spec 09 29 00 s.3.3 B). So when a wall is 12'-6" high, board is 4x14 (derived: 14 ft sheet cut to 12.5 ft wastes 10.7%) or a 4x12 plus a strip; the SF-based waste factor underestimates that. Wider/longer sheets cut joints and waste: larger sheets "need less waste percentage because there are fewer cuts" ([Vertigraph](https://www.vertigraph.com/learn/how-to-calculate-drywall-square-footage)).
- **Board stopped short of surfaces**: this project holds board 1/2 in. off the floor and stops 1/2 in. below structure (A-620 notes I and O); the effect is a small height deduction (derived: 1 in. on a 12.5 ft wall is under 1% of area), but it matters in the stud-length vs. board-length logic.

---

## 4. Waste factors and their basis

| Material | Factor | Basis |
|---|---|---|
| Gypsum board, simple commercial with 4x12 sheets | 8% | [Vertigraph](https://www.vertigraph.com/learn/how-to-calculate-drywall-square-footage) (blog-level) |
| Board, long open commercial walls using 12 ft sheets | 5-8% | [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) (blog-level) |
| Board, typical rooms | 10% | [Vertigraph](https://www.vertigraph.com/learn/how-to-calculate-drywall-square-footage), [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) (blog-level) |
| Board, cut-up spaces, soffits, curves | 12-15% | [Vertigraph](https://www.vertigraph.com/learn/how-to-calculate-drywall-square-footage), [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) (blog-level) |
| Board, full custom-detail commercial | 15-20% | [Vertigraph](https://www.vertigraph.com/learn/how-to-calculate-drywall-square-footage) (blog-level) |
| Rectangular vs irregular layouts | 5-10% vs 10-15% | [Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step) (blog-level) |
| Measured installation scrap, North America (new construction) | about 12% | [MDPI review (search summary)](https://www.mdpi.com/160668), [Green Building Advisor (search summary)](https://www.greenbuildingadvisor.com/article/job-site-recycling-gypsum-wallboard) |
| Metal framing | 5-10%, about 10% with many openings/headers | [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) (blog-level) |
| Joint compound | 10-15% | [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) (blog-level) |
| Joint tape | 10% | [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) (blog-level) |

Rules that follow from the evidence:

1. **Waste is a separate, single, visible step**, applied once to net area (or to stock-length cut-plans), then rounded to whole sheets/sticks/rolls ([Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step)).
2. If openings are "figured solid" (CGC practice), the unclaimed opening area is already a cutting allowance; do not stack a full waste factor on top without recognizing the overlap ([CGC handbook](https://www.usg.com/content/dam/USG_Marketing_Communications/canada/product_promotional_materials/finished_assets/cgc-construction-handbook-ch03-cladding-can-en.pdf), [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/)).
3. A layout (sheet-length vs. wall-height) calculation beats a flat %; 12'-6" walls on 14 ft sheets waste about 10.7% by geometry alone (derived).
4. The manufacturer coverage figures below (screws, tape, compound) are stated per 1,000 SF of installed board/finished surface with no waste included; add waste to those separately.

---

## 5. Coverage/yield factors per 1,000 SF (primary where noted)

Basis for all rows: 1,000 SF of gypsum board surface, single layer, finished as noted.

| Item | Factor | Source / notes |
|---|---|---|
| Screws, single layer, steel framing 16 in. o.c. | about 1,000 screws (Type S or S-12) | [CGC handbook ch.3](https://www.usg.com/content/dam/USG_Marketing_Communications/canada/product_promotional_materials/finished_assets/cgc-construction-handbook-ch03-cladding-can-en.pdf) (primary) |
| Screws, single layer, framing 24 in. o.c. | about 850 | same (primary) |
| Screw weight, #6 x 1-1/4 in. bugle drywall screw | 0.0050 lb each, so about 200 per lb, so about 5 lb per 1,000 screws (derived) | [L.H. Dottie WR6114 data sheet](https://www.elliottelectric.com/Media/WR6114-DOT) (coarse-thread wood version; fine-thread steel-stud screws weigh similarly but confirm) |
| Screws, rule of thumb | about 1 per SF, or about 1 lb per 100 SF | [Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step), [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) (blog-level); consistent with CGC |
| Screw length | board must penetrate steel at least 3/8 in. (GA-216 preview, search summary); 1-1/4 in. for single layer, 1-5/8 in. for face layer | [Gypsum Association](https://gypsum.org/?p=13903) (search summary), [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) |
| Joint tape | 370 LF (113 m per 100 m2) | [CGC handbook](https://www.usg.com/content/dam/USG_Marketing_Communications/canada/product_promotional_materials/finished_assets/cgc-construction-handbook-ch03-cladding-can-en.pdf), [USG joint compound data](https://www.usg.com/content/dam/USG/pdpmovedocuments/soquete-all-purpose-midweight-joint-compound-submittal-en-J1968.pdf) (primary) |
| Tape, blog figures | about 400 LF (ScopeTakeoff) up to about 1 LF per SF (Aginera) | blog-level, conflicting; prefer the manufacturer's 370 |
| Joint compound, ready-mix all-purpose (vinyl) | about 9.4 gal | [USG data sheet](https://www.usg.com/content/dam/USG/pdpmovedocuments/soquete-all-purpose-midweight-joint-compound-submittal-en-J1968.pdf) (primary) |
| Joint compound, ultralightweight all-purpose | about 9-10 gal; about two 4.5 gal pails | [USG data sheet](https://www.usg.com/content/dam/USG_Marketing_Communications/united_states/product_promotional_materials/finished_assets/sheetrock-ultralightweight-all-purpose-joint-compound-submittal-en-J2051.pdf), [USG FAQ](https://assemblies-tools.usg.com/content/usgcom/en/resource-center/faqs/1977.html) (primary) |
| Joint compound, CGC all-purpose ready-mix | 63 kg (about 138 lb) per 100 m2 (derived conversion); lightweight 36 L (about 9.5 gal) | [CGC handbook](https://www.usg.com/content/dam/USG_Marketing_Communications/canada/product_promotional_materials/finished_assets/cgc-construction-handbook-ch03-cladding-can-en.pdf) (primary) |
| Joint compound, setting-type powder | 72 lb (33 kg); lightweight setting 52 lb (24 kg) | same (primary) |
| Compound by bucket, Level 4 | one 4.5 gal bucket per 400-500 SF | [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) (blog-level; equals 9-11 gal per 1,000 SF, consistent with USG) |
| Level 5 skim coat | adds compound, no extra tape; blog figure about +50% | [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) (blog-level); definition in section 6 |
| Stud adhesive bead (3/8 in.), if specified | 11-19 L (about 2.9-5.0 gal, derived) per 1,000 SF | [CGC handbook](https://www.usg.com/content/dam/USG_Marketing_Communications/canada/product_promotional_materials/finished_assets/cgc-construction-handbook-ch03-cladding-can-en.pdf) (primary) |
| Corner bead, trim, control joints | no per-SF factor; measure LF | [Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step), [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) |

Stock units for converting to orders: sheets 32/40/48/56/64 SF (section 3.7); tape rolls 250 ft or 500 ft ([Sheetrock paper tape](https://sherwin-williams.com/painting-contractors/products/sheetrock-paper-joint-tape)); corner bead 8, 9, 10 ft sticks ([USG paper-faced bead and trim](https://www.usg.com/content/dam/USG_Marketing_Communications/canada/product_promotional_materials/finished_assets/sheetrock-brand-paper-faced-metal-bead-and-trim-brochure-en-can.pdf)), sold in cartons of about 63 (8 ft), 56 (9 ft), 50 (10 ft) ([Phillips klinchSTIK (search summary)](https://amerhart.com/catalog/panels-and-plywood/walls/joint-treatments-and-tapes/phillips-klinchstik-corner-bead)); studs per section 3.2; 4.5 gal and 3.5 gal compound pails/cartons ([USG](https://www.usg.com/content/dam/USG_Marketing_Communications/united_states/product_promotional_materials/finished_assets/sheetrock-ultralightweight-all-purpose-joint-compound-submittal-en-J2051.pdf)).

Installation spacing that underlies the screw counts (read from the spec, not assumed): walls with board parallel to framing, screws 12 in. o.c. in the field and 8 in. at edges; board perpendicular, 12 in. field and edges ([VA 09 29 00 s.3.2 G](https://www.cfm.va.gov/TIL/spec/092900.docx)). Where studs are at 24 in. o.c. and the assembly relies on composite action, sheathing screws at 12 in. o.c. to every framing member including the bottom track ([ClarkDietrich Motion Frame technical note (search summary)](https://www.buildsite.com/pdf/clarkdietrich/Motion-Frame-Connector-Technical-Notes-2975223.pdf)). Derived cross-check: a 4x8 sheet on four stud lines with screws at 16 in. is 28 screws (875 per 1,000 SF), at 12 in. 36 screws (1,125 per 1,000 SF), bracketing CGC's 850-1,000.

Joint-length sanity check (derived): a 4x8 sheet hung vertically has 8 LF of one side joint per 32 SF, i.e. about 250 LF of flat joint per 1,000 SF before end joints and inside corners, so CGC's 370 LF/1,000 SF assumes substantial added joints/corners. Tape for a specific job can be built up from joint LF instead, but the manufacturer factor is the accepted shortcut.

---

## 6. Finish levels (drive compound, tape and primer)

GA-214 levels as summarized by National Gypsum ([Finish levels](https://www.nationalgypsum.com/ngconnects/blog/building-knowledge/gypsum-board-finish-levels)): Level 1 tape embedded, no further coats (plenum, smoke-barrier joints); Level 2 one wipe coat; Level 3 two coats; **Level 4** flat joints three coats (wipe + 2), interior angles two, fasteners three layers, for smooth walls under flat paint or light texture/wallcovering; **Level 5** adds a full-surface skim coat for non-flat/gloss/dark paint or critical lighting. Level 0 has no tape. Level 4 is the usual default; many specs split levels by area (e.g., Level 4 where exposed, Level 1 above ceilings, Level 5 where indicated, project spec 09 29 00 s.3.7 D), so compound and tape must be taken per level-area, not from one global factor ([ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/) lists bidding one finish level when the spec splits levels as a common mistake).

---

## 7. Material breakdown an estimator lists

**Primary materials**
- Studs: each depth / thickness (mil) / flange, grouped by cut length (and joist/furring members for ceilings and canopy framing).
- Runners/track: each depth / thickness; deflection (slip) track separately.
- Gypsum board: each type (regular wall, Type X, ceiling board, moisture/mold-resistant, cementitious backer, glass-mat sheathing, exterior soffit board), thickness, edge, sheet size.

**Components that follow from those**
- Framing: jamb/header members and clips, bridging channel/strap and clips, flat strap and backing plates, blocking (wood or steel) where shown, floor and deck anchors/powder-driven pins (about every 24 in. and near ends), stud-to-track and framing screws (Type S pan head; [VA 09 22 16 s.3.2](https://www.cfm.va.gov/TIL/spec/092216.docx)), isolation strip / foam gasket at exterior walls (project spec 09 22 16 s.2.4 B), hangers, tie wire, carrying channels, furring channels, and ceiling grid for drywall suspension (project spec 09 22 16 s.2.3).
- Board: drywall screws by length (ASTM C1002/C954, [VA 09 29 00](https://www.cfm.va.gov/TIL/spec/092900.docx), project spec s.2.7 B), adhesive if specified, sound-attenuation blankets, acoustical sealant (ASTM C834 type) at perimeters, firestop sealant at rated heads (A-620 note J), security mesh where drawn.
- Finishing: paper joint tape (project spec s.2.6 B), setting-type taping/prefill compound, drying-type all-purpose compound for embed, fill and finish coats, Level 5 skim product, fire tape where specified.
- Trim (ASTM C1047): corner bead, LC-bead, L-bead, U-bead, control (expansion) joints (project spec s.2.5; [VA 09 29 00](https://www.cfm.va.gov/TIL/spec/092900.docx)).
- Gauge/thickness identification: "20 ga" is not one thickness across sources. The project's A-620 table gives 20 ga = 30 mil, 22 ga = 27, 25 ga = 18, 18 ga = 43, 16 ga = 54, 14 ga = 68, 12 ga = 97 and notes 16 and 18 ga are structural framing while 20, 22 and 25 are non-structural. The SFIA convention lists 20 ga structural at 33 mil ([ConstructConnect SFIA codes](https://help.constructconnect.com/takeoff-and-estimating-frequently-asked-questions-244/quick-bid-steel-framing-industry-association-sfia-codes-for-metal-framing-310)). The spec's own phrase is "minimum base-metal thickness as indicated on Drawings", so carry mil.

---

## 8. Common mistakes and how to check a takeoff

Mistakes documented in the sources:
1. One face counted instead of both, or a missed second layer ([Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step), [ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/)).
2. One height applied to every partition, ceiling height used where framing/board run to the deck ([Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step)).
3. All board as one line, ignoring fire-rated / moisture-resistant / abuse-resistant / cementitious types and different ratings ([ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/), [Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step)).
4. Stud spacing or gauge chosen by habit without checking height against limiting-height tables ([ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/)).
5. Compound estimated from sheet count rather than surface and finish level; a single finish level where the spec splits levels ([ScopeTakeoff](https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/)).
6. Missing ceilings, soffits, bulkheads, furring ([Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step)).
7. Inconsistent opening deductions; waste added to gross then openings deducted again ([Aginera](https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step)).
8. Walls from demolition sheets measured as new; unlabelled walls silently skipped ([Civils.ai](https://civils.ai/blog/how-to-use-ai-for-drywall-quantity-takeoffs/)).
9. Jamb/header framing treated as ordinary studs, or not counted (see 3.3, [Walls & Ceilings](https://www.wconline.com/articles/96115-jamb-studs-why-are-they-so-challenging)).
10. Backing and blocking omitted (3.5).

Checks to build in (derived unless linked):
- Net board SF vs. sum of (stud-run LF x height x faces) within the stated deduction rule; sheets x sheet SF >= net x (1 + waste).
- Studs per LF near 0.75 (16 in.) or 0.5 (24 in.) plus visible opening/corner additions; total stud LF vs. wall LF x height x 0.75.
- Track LF about 2 x partition LF minus door widths on bottom track; deflection track LF equals the length of walls flagged as slip heads.
- Screws about 850-1,000 per 1,000 SF of board layer ([CGC](https://www.usg.com/content/dam/USG_Marketing_Communications/canada/product_promotional_materials/finished_assets/cgc-construction-handbook-ch03-cladding-can-en.pdf)); tape about 370 LF and compound about 9-10 gal per 1,000 SF of **finished** surface ([USG](https://www.usg.com/content/dam/USG/pdpmovedocuments/soquete-all-purpose-midweight-joint-compound-submittal-en-J1968.pdf)).
- Control joints: walls longer than 30 ft uninterrupted need them; full-height door frames count as one; ceilings 30 ft (or 50 ft with perimeter relief) ([National Gypsum, GA-216-2021 summary](https://www.nationalgypsum.com/ngconnects/blog/building-knowledge/guidelines-best-practices-installing-drywall-control-joints)); the VA spec says not required for walls under 30 ft and uses edge trim at both sides ([VA 09 29 00](https://www.cfm.va.gov/TIL/spec/092900.docx)). Derived: a 100 ft straight wall needs 3 intermediate joints.
- Sound/rated walls: perimeter sealant LF = partition perimeter on each sealed face.

Worked example (derived, checked in Python): 40 LF partition, 12'-6" high, 16 in. o.c., 5/8 in. board both faces, one 3'x7' door, 4x14 sheets. Gross 1,000 SF; door deduction 42 SF (21 SF x 2 faces); net 958 SF; with 10% waste 1,053.8 SF = 18.8 sheets of 4x14 by area, but by layout 10 sheets per face x 2 = 20 sheets (1,120 SF). Studs ceil(480/16)+1 = 31 before door framing; track 80 LF minus 3 LF door width at the bottom; screws about 958 (about 4.8 lb); tape about 354 LF (0.7 of a 500 ft roll); compound about 9 gal.

---

## 9. Project-specific: what this set requires an AI to read

From the project manual and A-620 (quoted from `source/specifications.pdf` s.09 22 16 pp.267-272, s.09 29 00 pp.273-282 and `A-620 Interior Partition Schedule & Details`):

- Partition **tag** structure on plans = series letter (A-L: layers, stud type, rating), framing depth number (Table B: 2, 3, 4, 6, 8, 10 = 2-1/2, 3-5/8, 4, 6, 8, 10 in.), and a **height designator** (Table D: slab to structure with batt; slab to 6 in. above scheduled ceiling; slab to scheduled ceiling; partial height per details). The AI must resolve each plan tag to depth, mil, spacing, layers, board type, rating, insulation and head/base detail.
- A-620 general notes change quantities: all partitions with plumbing or an exterior face insulated; offices/toilet perimeter partitions get sound-attenuation batts; mechanical/electrical/AV rooms get mineral wool; rated partitions run slab to underside of structure; **tile/FRP partitions use water-resistant core board**; board held 1/2 in. off the floor and stopped 1/2 in. below structure; fire-retardant treated blocking where shown; acoustical sealant on non-rated, firestop on rated partitions; deep-leg slip track shown at some head details (e.g. detail D-T01).
- Steel thickness comes from the A-620 gauge/mil table and the drawings ("as indicated on Drawings"), not the specification; 16 and 18 ga are structural framing and 20/22/25 non-structural.
- Spec 09 22 16: studs ASTM C645, galvanized G60; 16 in. o.c. default; slip-type head joints with long-leg or double runner and bridging within 12 in. of stud top; two studs at each jamb; jamb studs through ceilings where indicated; hangers 48 in. o.c., carrying channels 48 in., furring 16 in.; 0.033 in. flat strap and backing plate; do not bridge building control joints with framing.
- Spec 09 29 00: board types are 5/8 in. Type X (vertical surfaces unless indicated), 1/2 in. ceiling board, 5/8 in. moisture/mold-resistant Type X where indicated, 5/8 in. exterior soffit board; maximum practical sheet length; board vertical on partitions with staggered end joints; multilayer joints offset at least one stud / 16 in. at ceilings; tapered long edges; trim (cornerbead, LC, L, U, control joint); paper tape; Level 1 plenum/concealed, **Level 4 exposed**, Level 5 where indicated; security mesh panels butted, not overlapped.
- Items the plans carry that are easy to miss: stud counts by cut length (heights range from under 2 ft to 18'-8" in the reference estimate), canopy framing at 16 in. o.c., booth ceiling framing at 12 in. o.c., soffit and bulkhead framing on A-130, sheathing and cement-board areas, blocking schedules, tech-wall and booth enlargements (A-704, A-706).
- Revision awareness: the set is a PERMIT SET (Rev 0, 07/02/2026, A-620 title block); re-run when sheets change ([Civils.ai](https://civils.ai/blog/how-to-use-ai-for-drywall-quantity-takeoffs/)).

AI input checklist: (1) every partition segment with length, tag, face-by-face layer/board type; (2) per-wall start and end heights and head condition; (3) every opening with width x height, jamb/head detail and whether it is full-height (control-joint equivalent); (4) outside-corner, column-wrap, soffit-edge and exposed-edge LF; (5) ceiling/soffit/canopy areas with member spacing from the spec; (6) insulation, sealant and blocking flags from the partition notes; (7) finish-level map from the finish plan; (8) specified stud steel thickness per partition and jamb/header; (9) which sheets are demolition, existing or not-in-contract; (10) the deduction rule and waste policy used, echoed in the output.

---

## 10. Calibration against this job's estimator (quantities only, from `reference/estimate/lines.json`)

Derived ratios for the board-related lines (lines 242-291), computed in Python:
- Sheets = board SF / 32 exactly (e.g. 6,004.87 SF / 32 = 187.65 sheets): the estimate carries **no waste** in its sheet counts and no 4x10/4x12 layout.
- Tape = 375 LF per 1,000 SF (500 ft rolls), in line with the manufacturer's 370 LF ([CGC](https://www.usg.com/content/dam/USG_Marketing_Communications/canada/product_promotional_materials/finished_assets/cgc-construction-handbook-ch03-cladding-can-en.pdf)).
- Screws = 5.357 lb per 1,000 SF, which is about 1,070 screws at 200 per lb, in line with the CGC 850-1,000 range.
- Adhesive = 1 tube per 32.26 SF; compound ("mud plaster") = 530 lb per 1,000 SF, which is about 3.8x the CGC all-purpose ready-mix figure of 138 lb (derived: 530 / 138). Flag for the formulas reconciliation: either different product assumptions (e.g. Level 5 or setting-type plus skim) or a unit convention.
- Studs are carried as counts by cut height with the line total in SF (lines 308-311), runners as equal top and bottom LF (lines 314-321), ceiling and canopy framing in LF (lines 284, 291, 312, 313).

---

## 11. Conflicts and open questions

- Opening deductions: CGC "figured solid" vs. blog thresholds (4 SF, 16 SF, 32 SF, all openings). No standard; make it a parameter.
- Tape per 1,000 SF: 370 LF (USG) vs. about 400 LF vs. about 1 LF per SF (blog). Use the manufacturer figure.
- Corner stud allowance: 2 vs. 3 per corner; "+10% for corners/openings" is a shortcut, not a rule.
- Compound: ready-mix by volume (9-10 gal) vs. setting-type by weight (72 lb) ; use the data sheet of the selected product, not calculator-site figures.
- GA-216 ceiling screw spacing and the current ASTM C754/C840 text were not retrievable in full (paywalled or blocked); spacing above comes from master specs and manufacturer notes. Confirm against the current editions before relying on specific tables ([GA-216-2024 page](https://gypsum.org/2019/04/ga-216-2018-application-and-finishing-of-gypsum-panel-products/), [ASTM C754 scope (search summary)](https://bsmd.moic.gov.bh/store/standards/GSO:869433/GSO%20ASTM%20C754:2024)).
- Gauge-to-mil mapping differs by source (30 vs. 33 mil for 20 ga); carry mil from the drawings.
- A second-opinion pass was run with GPT-6 Astra (`tools/ask_gpt.py`). Its answers were used only to prompt cross-checks (framing count methods, header/jamb member counts, control-joint example); wherever a claim is not linked above, treat it as unverified convention.

---

## Sources

Primary / manufacturer / standards-derived
- USG/CGC Construction Handbook, Chapter 3 Cladding (estimating screws, tape, compound, adhesive): https://www.usg.com/content/dam/USG_Marketing_Communications/canada/product_promotional_materials/finished_assets/cgc-construction-handbook-ch03-cladding-can-en.pdf
- USG vinyl ready-mix all-purpose compound data sheet (9.4 gal, 370 LF tape): https://www.usg.com/content/dam/USG/pdpmovedocuments/soquete-all-purpose-midweight-joint-compound-submittal-en-J1968.pdf
- USG Sheetrock UltraLightweight all-purpose compound (9-10 gal): https://www.usg.com/content/dam/USG_Marketing_Communications/united_states/product_promotional_materials/finished_assets/sheetrock-ultralightweight-all-purpose-joint-compound-submittal-en-J2051.pdf
- USG FAQ on ultralightweight coverage: https://assemblies-tools.usg.com/content/usgcom/en/resource-center/faqs/1977.html
- USG paper-faced bead and trim brochure: https://www.usg.com/content/dam/USG_Marketing_Communications/canada/product_promotional_materials/finished_assets/sheetrock-brand-paper-faced-metal-bead-and-trim-brochure-en-can.pdf
- Sheetrock paper joint tape (250/500 ft): https://sherwin-williams.com/painting-contractors/products/sheetrock-paper-joint-tape
- ClarkDietrich ProSTUD composite limiting-heights sheet: https://www.buildsite.com/pdf/ram_sales/ProSTUD-ProTRAK-25-Ga-Submittal-Sheet-2970880.pdf
- ClarkDietrich head-of-wall composite sheet: https://nginx.pr-196.clark-dietrich-drupal.lagoon-prd.acromedia.com/sites/default/files/media/documents/CD_ProSTUD-15mil_HOW_Composite_MaxTRAK.pdf
- ClarkDietrich Motion Frame technical note: https://www.buildsite.com/pdf/clarkdietrich/Motion-Frame-Connector-Technical-Notes-2975223.pdf
- ClarkDietrich structural track page: https://www.clarkdietrich.com/node/402
- L.H. Dottie WR6114 screw data sheet: https://www.elliottelectric.com/Media/WR6114-DOT
- Kuiken Brothers (ClarkDietrich) stud and track stock lengths: https://www.kuikenbrothers.com/products/commercial/steel-studs/
- Phillips klinchSTIK corner bead cartons: https://amerhart.com/catalog/panels-and-plywood/walls/joint-treatments-and-tapes/phillips-klinchstik-corner-bead
- National Gypsum, control joints (GA-216-2021): https://www.nationalgypsum.com/ngconnects/blog/building-knowledge/guidelines-best-practices-installing-drywall-control-joints
- National Gypsum, finish levels (GA-214): https://www.nationalgypsum.com/ngconnects/blog/building-knowledge/gypsum-board-finish-levels
- Gypsum Association GA-216 page and preview: https://gypsum.org/2019/04/ga-216-2018-application-and-finishing-of-gypsum-panel-products/ , https://gypsum.org/?p=13903
- ASTM C754 scope listing: https://bsmd.moic.gov.bh/store/standards/GSO:869433/GSO%20ASTM%20C754:2024

Master specifications
- VA 09 22 16 Non-Structural Metal Framing: https://www.cfm.va.gov/TIL/spec/092216.docx
- VA 09 29 00 Gypsum Board: https://www.cfm.va.gov/TIL/spec/092900.docx
- PLU Division 09 specification: https://www.plu.edu/construction/wp-content/uploads/sites/128/2014/10/div-009.pdf
- Winnipeg NMS 09 22 16: https://legacy.winnipeg.ca/finance/findata/matmgt/documents/2011/253-2011/253-2011_NMS_092216_Non-Structural_Metal_Framing.pdf

Trade press / estimating guides (blog-level or secondary)
- Walls & Ceilings, jamb studs: https://www.wconline.com/articles/96115-jamb-studs-why-are-they-so-challenging
- Vertigraph: https://www.vertigraph.com/learn/how-to-calculate-drywall-square-footage
- ScopeTakeoff: https://scopetakeoff.com/blog/drywall/how-to-estimate-drywall/
- Aginera: https://aginera.ai/blog/drywall-takeoff-from-drawings-step-by-step
- Civils.ai: https://civils.ai/blog/how-to-use-ai-for-drywall-quantity-takeoffs/
- Estimating Edge, drywall partition model: https://www.estimatingedge.com/knowledgebase/dw-partition-condition-properties-layer-2-trim-and-count-tabs/
- NASCLA study guide, light-gauge framing: https://open-exam-prep.com/study-guides/nascla-contractor/nascla-metals-wood/nascla-9-2-light-gauge-metal-framing
- ConstructConnect SFIA codes: https://help.constructconnect.com/takeoff-and-estimating-frequently-asked-questions-244/quick-bid-steel-framing-industry-association-sfia-codes-for-metal-framing-310
- Stud calculator roundup: https://homebuddy.blog/calculate-studs-for-wall
- RUH drywall calculator: https://www.ruh.ai/industrial/construction/tools/drywall-calculator
- MDPI drywall waste review: https://www.mdpi.com/160668
- Green Building Advisor, gypsum jobsite recycling: https://www.greenbuildingadvisor.com/article/job-site-recycling-gypsum-wallboard
