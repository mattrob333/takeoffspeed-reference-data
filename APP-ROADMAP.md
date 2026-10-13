# TakeoffSpeed roadmap: toward the most accurate AI quantity takeoff

This plan comes from four sources:

- `FINDINGS.md`;
- the 24 `trades/*/app-gaps.md` files;
- `vision-benchmark/`;
- `vision-benchmark/vector-geometry/`.

It covers material types and quantities only. The app references are
the TakeoffSpeed repository's `lib/quantities/` and `docs/QUANTITY_ENGINE.md`; nothing in the app was
edited.

Every number below comes from **one job and one estimator**. Section 5 lists what must be checked on
a second job before any of it becomes a default.

---

## 0. Where the app stands

**The arithmetic is mostly right.** With correct measurement records in `mode: 'net'`, the engine
already reproduces most trades:

| Folder | Result with correct records |
|---|---|
| `01` | 14 of 14 `expectedLines` pass |
| `02` | 15 of 15 within 1% |
| `04` | every line within 0.4%, except bridging at +1.7% |
| `10` | 15 of 15 exact |
| `22` | 41 of 41 exact |
| `28` | 26 of 26 fixtures pass |
| `09e` | 12 measured lines within 0.05% |
| `06` | 31 of 48 within 1% |

The misses come from conventions, line keys and missing inputs.

**Reading is the bottleneck.** `docs/QUANTITY_ENGINE.md` records:

- Interior run 10 had 72% of 38 families within 10%. In runs 9–10 the model wrote the lines itself,
  so the engine was not on the path.
- Wall run W8 had 8 of 41 lines within 5%, with a median error of 20%. Runners were 26–58% short
  because the run length was wrong.
- Ceiling and finish lines swing 20–70 points between runs.

**What already exists to build on:**

- `lib/plan-text-map.ts`, which feeds the model positioned dimension strings, tags and labels;
- the `PageDimensionIndex` check (`checkRecordAgainstText`);
- the zoom refine pass: `zoom_requests`, up to `MAX_ZOOM_REGIONS` = 12 crops per round, several
  rounds;
- measurement records, behind `TAKEOFF_QUANTITY_ASSEMBLIES` (off);
- the `reviewed-commercial` profile in `lib/quantities/profiles.ts`;
- `mode: 'net'`.

---

## 1. Architecture

### 1.1 Who does what

| Task | Source of truth | Who | Evidence |
|---|---|---|---|
| Printed values: dimensions, tags, schedule cells, notes, keynotes, legend rows | PDF text layer | Code extracts. The model maps values to records. | Models read dimension strings at 94–99% F1. The text layer is exact and free. Model misses were ceiling-height tags in the RCP field. |
| Lengths and areas on vector sheets | PDF vector line work | Code measures. The AI classifies only the pieces code flags. | Wall LF from images: 19–55% error for every model. Vector prototype: six-type total −1.5%; 0–6% per type when types are assigned correctly. |
| Counts | Tag text where tags exist; vector blocks; vision where only symbols exist | Code counts tags. Vision counts symbols. | Lighting/plumbing symbol counts: 0.7–3.0% mean error. |
| Raster schedules, raster details, scanned sheets | The image | Vision, with two readers and a settler (§1.7) | A-170 has 844 characters of text, titles only. The C-6.x details are raster. |
| Heights and assemblies | Sections, elevations, RCP, partition schedule | The AI reads them into records | `09a`, `09b`, vector-geometry README |
| Arithmetic | `lib/quantities/` | Code, with exact rationals | `QUANTITY_ENGINE.md` |
| House conventions | Profile | Contractor setting | `FINDINGS.md` §3 |

### 1.2 Text layer for every printed value

- **Extend the plan text map.** It currently lists dimensions, tags and labels. Add:
  - schedule tables as cells (row × column);
  - legend tables;
  - keynote lists;
  - numbered general notes, keeping the letter tied to its text (`11`: A-110 prints them as two
    separate lists);
  - per-viewport scales with their bounding boxes (`06` A-707: 1/2" plans and 3/4" elevations on
    one sheet);
  - font size, to tell tags from grid bubbles (`08`: 9.51 pt vs 12.51 pt).
- **Raster gate.** When a sheet's text layer is near-empty compared with its drawn content (A-170:
  844 characters), mark it raster and send it to vision. Never let "no text" become 0.
- **Extend `checkRecordAgainstText` to schedule cells.** Every quoted string in a record must exist
  on the cited page.

### 1.3 Vector geometry measured by code

Build a deterministic `lib/geometry/` stage. The prototype is
`vision-benchmark/vector-geometry/extract_walls.py` (pymupdf only, about 2 s per sheet).

- **Scale gate.**
  - Pair printed dimension strings with their ticks. On A-120 that gave 83 samples, with
    measured/printed = 1.00098–1.00100.
  - Require at least 5 samples and a spread of 0.5% or less per viewport. Otherwise ask the user to
    calibrate.
  - Never trust the title-block scale alone.
- **Style profile per sheet.** The stroke classes are cut wall, board layer, door frame and tag
  tick. The AI proposes the classes; code verifies that stud-depth spacings actually occur.
- **Walls.** Each piece carries:
  - endpoints;
  - thickness family;
  - board faces;
  - openings;
  - junction graph;
  - gross and net LF.

  Store lengths in integer units (1/16" or millipoints) until display.
- **Wall types.**
  - Follow tag → leader → wall.
  - Propagate a type only within the same thickness family.
  - Flag ambiguous pieces; leave untagged pieces untyped.
- **Then extend the stage to:**
  - hatch and fill polygons by shoelace, for areas (`01` CAD checks, `09c` vector checks);
  - linetype polylines and tick counts for curbs and utilities (`01`: 5.0 ft per `///` tick and
    2.0 ft per curb tick at 1" = 20');
  - vector symbol blocks for counts.
- **The AI resolves only flagged pieces.** It gets a crop of the piece, the candidate types with
  their path costs, and the room names on either side, and returns a type or `unknown`. On A-120
  that is 1 ambiguous piece (7.6 LF) and 7 untagged pieces (17.5 LF), instead of the model measuring
  about 200 LF.
- **Untyped or unmeasured LF blocks a final quantity.** Show `—`, never `0`.
- **Known gaps.** List them for the user rather than guess:
  - thin "below the cut plane" walls (knee wall 18.3 LF, low wall 7.7 LF);
  - heights, which come from sections;
  - angled and curved walls;
  - other CAD templates.

### 1.4 Vision only for scanned sheets, raster schedules and symbol counting

- **Counting:** about 1% error on the strong models.
- **Areas:** 2.6–3.8% on the strong models. Use vision areas only when there is no vector polygon,
  and label them "estimated from image".
- **Lengths:** never from vision.

### 1.5 The zoom/crop tool

**What the app has today** is a batch refine pass:

- the model files `zoom_requests`;
- the pipeline re-renders vector crops at the full per-page raster budget;
- up to 12 regions per round, over several rounds.

**What the benchmark tested** is an interactive tool that re-renders any region at full resolution,
up to 10 zooms per task.

- It helps counting for weaker models: Sonnet went from 3.0% to 0.9%.
- It helps areas: Fable went from 12.6% to 2.6%, and GPT-6 Astra from 3.8% to 2.6%.
- It does not fix lengths. Wall LF stayed at 19–33% error, and Opus got worse (21.8% → 33.2%).
- It costs 3–20× a single call.

**Recommendation.**

- Expose the interactive crop tool inside reading, counting and flagged-piece tasks: raster
  schedules, symbol counts, dense RCP tags.
- Never use it for measuring.
- Keep the batch pass for coverage.
- Log every zoom region, so a reviewer can see what was looked at.

### 1.6 Which model for which job

| Job | Model | Why (benchmark) |
|---|---|---|
| Sheet classification, text-layer checks, bulk passes | Haiku 5.5 | Strong at reading (F1 0.942) and counting (tags 12/12, symbols 1.8%) at 1–2% of the cost of the strongest models. Not for measuring: areas 78.8%. |
| Reading schedules, counting symbols, assigning wall types, resolving flagged pieces | Opus 5.5 | Equal to Fable on reading (0.968) and counting (1.2%), better on one-shot areas (3.8% vs 12.6%), at about a third of Fable's cost |
| Hardest items, second-provider check | GPT-6 Astra | The most accurate reader (0.989 F1, 0.7% counts, 2.6% areas with zoom), but the slowest and costliest. One wall call failed. |
| Settler when two readers disagree | Fable 5.1 | Settled the legend disagreements here |
| Measuring lengths | none: code | Every model was at 19–55% |

Sonnet 5.5 suits cost-bound counting only if it has the zoom tool (3.0% → 0.9%); its areas were
21.7%. Each skill had only 2–12 tasks, so treat differences under about 1 point as noise.

### 1.7 Two readers and a settler

**Evidence that it works:**

- **Markup legends.** Sonnet and Opus agreed on 647 of the 656 rows in the first settled
  extraction, and Fable settled the rest.
- **Trade folders.** The adversarial second pass caught real errors, for example:
  - the dropped 9 EA legend row and the line-619 miss (`28`);
  - door 106 measured at 3.00 ft, not 3.33 (`09c`);
  - the ramp CAD check, which moved from −5.4% to +6.0% (`01`);
  - two defective legend polygons (`06`);
  - the refrigerant trace (`23`).

**In the app,** run two independent readers on:

- raster schedules;
- every count by tag;
- flagged geometry pieces;
- imported contractor legends.

**Settle disagreements in this order:**

1. a code check: text layer, schedule COUNT column, or a sum check;
2. a third model, preferably from a different provider for the hardest items;
3. the user.

Store each value's agreement state ("two readers agree", "settled", "disputed"), as
`legends.json` does.

### 1.8 Model reads, code computes: keep the engine on the path

Make measurement records mandatory for every scope the engine covers. Allow a model-written line
only as a labelled fallback, when the record's required inputs are missing.

---

## 2. Quantity-engine changes, ranked by quantity impact

Each change is ranked by the size of the error it removes on this job. The units differ, so the
order within a tier is judgment.

- "Fixtures" refers to `trades/<folder>/fixtures.json`, by estimate line or fixture name.
- "Profile" means a setting in `reviewed-commercial`; the default stays unchanged unless stated.

### Tier 1: over 20% on a line, or a line lost, invented or put in the wrong trade

| # | Change | Folders | On this job | Fixtures |
|---|---|---|---|---|
| 1 | Conduit LF is route length. Multiply by the number of conduits only for couplings and straps (`electrical.conduit-lf-basis`; profile `route`). | 26 | 617.54 vs 279.62 LF (+120.8%, +337.92 LF); (2) 4" is 203.42 vs 101.71 | `26` lines 505–508, 601, 602 |
| 2 | Net fill = fill − cut with no shrink. Emit a shrink-adjusted import only as a separate labelled line (or profile `earthwork.shrink-pct` = 0). | 31 | 290.59 vs 151.84 CY (+91.4%) | `31` line 641 |
| 3 | Make opening sealant and sill flashing opt-in on storefront and window records, or suppress them when a 07 sealant record exists | 08, 07 | Engine sealant 801.5 LF vs 221.9 LF measured in 07; sill 74.5 vs 48.3 LF | `08` lines 208–216; `07` lines 150, 185 |
| 4 | Route plywood and OSB exterior sheathing to `rough-carpentry.sheathing`, and reject `PLYWOOD|OSB` as a partition board face | 05 | Up to 3,057 SF in the wrong trade, with invented screws, tape and mud | `05` line 82 |
| 5 | Opening-deduction convention per family (sheathing, board, paint, insulation, air-barrier returns); profile `none` | 05, 09a, 09e, 07 | Sheathing −29.3% (−889 SF); board −4.97% (−298.7 SF) plus its 5 accessory lines; paint +21–25% on the partition path; barrier returns +172 SF | `05` L82; `09a` 242–247; `09e` 295; `07` 184 |
| 6 | Count each object once across sheets: a designated count sheet per tag; `sameAs` for reprints; max per tag per floor; elevations and isometrics "no count"; column runs de-duplicated by grid ID against the column schedule | 22, 10, 26, 33, 04 | Plumbing fixtures 3× on 6 lines and 2× on 4; accessories +69% (27 vs 16); backflow 2 vs 1; HSS6x6x3/8 −27% (−64.5 LF) | `22` 421–438; `10` 322–331; `33` 739; `04` 40 |
| 7 | Legend ingestion keys rows by page + name + colour + quantity. `NAN` becomes unknown ("Measurement not computed", no line). RFI placeholder rows are dropped. Same-name rows with different swatches are never merged. | 28, 32c, 23, 26, 04, 31 | 9 horn/strobes lost (−100% on 627); 20,298.88 SF lost on each of 3 lines; 8 of 55 HVAC rows | `28` L627; `32c` 689–691; `26` 497, 541 |
| 8 | Report roof insulation per stack; boards per layer only in purchase | 07 | 5,592.9 vs 1,864 SF (3×) | `07` L159 |
| 9 | Duct insulation basis = sheet surface; seam and joint allowances 0 and wrap lap 0 (profile); one job-level gauge rule read from M-001 | 23 | Insulation +29.9% to +55.9%. Weight +16.9% from gauge alone, +33.1% with the seam allowances (seams alone +13.8%) | `23` L446, L447 |
| 10 | Site trench: a `trench-bedding-line = none` option; a job-level trench section; a haul allowance input; width read from the detail formula `O.D. + 18" MAX` | 33 | Backfill −58.3% (−241.6 CY); haul +377% (+158.3 CY); excavation −18.2% (−83.3 CY) | `33` L740, L741 |
| 11 | Shade drop convention `furnishings.shade-drop-ft` (unset by default); warn when the drop exceeds that run's storefront head | 11 | 1,184.4 SF estimated vs 737.6–885.1 per the drawings (−25% to −38%) | `11` `shade-sf-run-x-drop` |
| 12 | Specialty-board replacement areas (Type X, MR, cement board) subtracted from standard board; cement board and glass-mat use the gypsum accessory set (profile) | 09a | 580 SF of specialty board cannot be placed today; cement-board sheets +113%, tape +371%; 6 accessory lines missing | `09a` 248–277 |
| 13 | Soffit records get separate `framingHeight` and `boardHeight`, board `faces`, and an optional width (0); add a stud-bracing assembly; area-rule framing with the 1.33 divisor (profile) | 09b | Board +38% to +58% depending on the reader; bracing 90.1 LF (21% of line 291) | `09b` 285–291 |
| 14 | Wall tile `blend` by tag (traced accent areas, with MIX % as a fallback); `roomRepeat` for "similar" rooms. Do not call it `repeat`: that name is already the wallcovering pattern repeat. | 09d | WT-1 +69% with WT-2 and WT-9 at 0 (100 SF missing); restroom tile halved (107.4 SF) | `09d` 235, 236, 238 and the roomRepeat cross-check |
| 15 | Marking: `measuredRuns` on crosswalk and access-aisle; a purpose in the stripe key; sidewalk expansion joint = SF / spacing; `rampCount` | 32a | Crosswalk −71.7%; aisle hatch −69.2%; SSWL +10.2%; stop bar +40.3%; expansion joint −100% (no line); ramps −50% | `32a` 636, 637, 642–644, 646 |
| 16 | Inlet protection `runs` (measured LF), keyed by phase and code; warn when a phase's practice code differs from its legend | 32c | 388 LF on two lines produces no LF line (−100%) | `32c` 692 |
| 17 | Demolition storey height 10 ft and volume rounding to 10 CF (profile) | 01 | +20% (+21,383 CF) on lines 3–4 | `01` building fixtures |
| 18 | Weep screed output on site CMU; site CMU grout and mortar ratios (profile); `solidBelowGrade` grout per S-001 | 32b | Weep screen has no line (−100%); grout −73%; mortar −42.9% | `32b` 669, 670, 683 |
| 19 | Rough carpentry: a leading `(n)` means rows on blocking and backing; `faces` and per-run heights on sheathing; `layers` on areas | 05 | Blocking −40% to −70% (72–144 vs 240.66 LF); wing walls −5.1% (−156.8 SF); booth ceiling −50% | `05` 81–97, 145–147 |
| 20 | Cove trim on tile-base walls; grout area +10% then ceil to 50 SF (order mode only, profile) | 09c | Cove −23.4% (−12.12 LF); grout −9.9% / −18.6% (+159.8 SF) | `09c` 225, 226, 233 |
| 21 | A `scheduledOnly` path for equipment, as furniture already has (1 EA V.I.F., low confidence) | 11 | AE-01 throws "no quantity" (−1 EA; a lost line) | `11` AE-01 (line 337) |
| 22 | Millwork apron-only record; countertop `areas`, per-leg depth and `mergeWaterfalls` | 06 | Line 126 lost; SLD-1 −10.1% (−11.2 SF) and split in two | `06` L126, L344 |
| 23 | Count site lights by pole assembly (`electrical.site-light-count`) | 26 | Luminaire line 9 vs 5 (+80%) | `26` 495, 496 |
| 24 | A disconnect with no printed rating still emits a line, rated "per equipment" | 26 | 9 EA lost (553, 559) | `26` 553, 559 |
| 25 | Painting: paint height per face; ceiling and soffit board records emit ceiling paint by tag; fix the PT-7 key-case bug; primer-only tags get 0 finish coats; `insetOf` | 09e | Soffit paint (286 SF) is not linked; PT-7 counted twice (206 SF); PT-6 sits inside PT-4 (37.2 SF) | `09e` 296–300 |

### Tier 2: 5–20%, or extra lines that break line matching

| # | Change | Folders | On this job | Fixtures |
|---|---|---|---|---|
| 26 | Stud area rule `wall-area` (SF = Σ LF × H, no run-end, jamb or corner studs; profile). Emit two records for dual-use rows (`6" & 3-5/8"`). Correct `QUANTITY_ENGINE.md`: runner LF = Σ run LF on this job, not stud count × spacing. | 09a | +1.6% to +8.0% with the profile, +4.8% to +24.5% default; 156.8 SF and 8.4 LF of runners lost on the double wall | `09a` 308–321 |
| 27 | Concrete: pool order rounding per pour group, not per mark. Fix the saw-cut waste bug: `concrete.ts` upper-cases `type` before comparing it to `'saw-cut'`, so the test never matches. Add a formwork roll-up and its rounding. | 02 | Order CY +15.1% (41.5 vs 36.05 net; the pad is 12× its volume); saw-cut +18.9 LF (+5.2%) | `02` L18, L19–29, L30 |
| 28 | Earthwork: footing working space per type (pads 0.5 ft, trench 1 ft); `wallRuns` for stems over pads; FF datum and per-tag brackets | 31 | Excavation +19.5% (+23.34 CY); backfill +32.7%; haul −11.2% | `31` 629–631 |
| 29 | Structural steel: deck polygon union or overlap warning; joist length checked against the bearing grid; `totalLF` + `count` inputs; parse `*N` and `@ L/H` in legend names; X-bridging at plan length as an option; plates from schedules | 04 | Deck −8.3% (−183.8 SF); joists −16.8% / −11.5%; joist EA 1/1/1 → 3/10/4; about 415 LF made reproducible; bridging +1.7% | `04` 36, 37, 65, 67, 70–79 |
| 30 | Roofing: developed-height flashing runs with no extra 12" lap; edge wraps by girth; a `roofing.transition-wall` assembly; curb perimeter LF and `barrierHeight`; no head bead on partial-height walls | 07 | Engine is 115 SF over the measured rebuild; transition wall 299 SF across 4 lines; curb barrier +50% (+20 SF); acoustic sealant +5.1% (+52 LF) | `07` 148, 154, 157, 163, 166, 171 |
| 31 | Millwork: no whole-unit rounding on fabricated lines; laminate and panel waste only when a sheet size is given | 06 | In order mode: cabinets +11% (+8 LF); faces +17% (+31 SF); booth +10%; reveal +9 LF | `06` (all 48, order mode) |
| 32 | Masonry: barrier with no waste class; spec tie minimum (`tieMaxSF`); `cutFraction` for the half rowlock; `courses` for CMU height; cavity grout | 03 | Barrier +4% (+16 SF); ties +78% (+87); half rowlock −336 brick | `03` L31–35 |
| 33 | Toggles for lines the estimator does not carry: electrical box/ring/plate; fire-alarm backboxes and bases; an access-door guard when a security schedule exists; one camera path; plumbing kits; HVAC duct-sf, joint and coupling lines; ACT components; pad concrete CY | 26, 28, 22, 23, 09b, 32b | About 337 electrical box lines; +16 fire-alarm EA; +19 access-door EA; up to +20 cameras | `26` 534–580; `28` 603–628 |
| 34 | `groupPipeBy: system+size`, keeping gas split by location; no risers added when runs come from a legend total | 22 | 10 engine lines collapse to 4; riser double-count risk removed | `22` 404, 405, 412, 415 |
| 35 | Key pier excavation and haul by diameter and depth; put the bollard location in the key and section | 32a, 32b | Sign footing pairs and the two bollard groups' earthwork merge today | `32b` 652, 653, 655, 656; `32a` 676, 677, 715, 716 |
| 36 | A grab-bar set (side, rear and vertical per accessible WC); enumerate every life-safety legend symbol | 10 | +2 EA rear bars; +1 Knox box | `10` 322, 323 |
| 37 | Basin `stoneBedAreas` separate from the pond reference area; geotextile wraps the bed and sides; move geotextile and blanket laps from net to order | 32c | Here the engine is right per the drawings (196.04 vs 626.19 CY; ≈2,095 vs 3,074 SF). The laps add +307 SF and +211 SF to net. | `32c` 709 and 711 (`perDrawings`), 698 |

### Tier 3: under 5%, labels, and scope flags

| # | Change | Folders | Notes |
|---|---|---|---|
| 38 | An estimator presentation-rounding profile, off by default: 2-decimal feet, LF up to 0.5, finish SF ceil 5, flatwork ceil to a whole unit, circle areas to 2 dp, whole-foot accessory LF, allowance area ceil to 1,000 SF | 02, 03, 05, 07, 09a, 09e, 32a, 32b, 22/23/26/28 | At most 5 units per line, and it makes dozens of lines exact. Never applied to net. |
| 39 | An allowance record kind (assumed scope in LF, SF or LS, low confidence) and allowance-basis rounding | 05, 09e, 07, 22, 23, 26, 28, 33 | 910 LF trim; 1,330 LF sealant; 42 CY haul; "AREA: 2000 SF" |
| 40 | Responsibility inputs (furnished-by / installed-by) on millwork, wall finishes, ACT and equipment; inherited once from a general note; hardware items marked OT, MC or DT | 06, 09d, 09b, 11, 08 | 223 SF of owner wall covering; 48 millwork lines; 57 furniture lines that warn UNSTATED today |
| 41 | Cross-trade ownership and duplicate checks | 02↔32b, 03↔07, 22↔23, 23↔07, 06↔11, 10↔08, 28↔26, 09d↔09e, 32c | Cleanout pads; thru-wall flashing (213 LF); condensate; RTU curbs (line 171); lockers; coat hooks; DACT and security panels; PT-7; sod (5,018 SF over the pervious area) |
| 42 | A spec-vs-drawing conflict flag (`materialConflict`) and a `conditional` / `alternate` flag | 22, 07, and all | The XPS "where req'd" zone note puts 2,298 SF at stake |
| 43 | Attic stock as separate lines from the spec %, never folded into waste | 09b, 09c, 09d, 26 | ACT +94.9 / +24.5 SF; tile 94.61 SF; carpet 67.65 SF; LVT 9.40 SF; base 40.47 LF; 10 C + 10 UC fixtures |
| 44 | Item text and keys taken from schedule strings: product names, the window tag in the key, door remarks normalised, pair width, footing dimension set, saw-cut depth, stair material | 01, 02, 08, 09c, 11 | Affects line matching only |
| 45 | Store the screw ratio as the exact 3/560 instead of 0.005357 | 09a, 09b | −0.003% |

---

## 3. Order of implementation

Measure before you change anything. Do the cheap, high-impact work first, and build the geometry
stage in parallel. Per the app's `CLAUDE.md`: no automatic merge, migration, flag flip or
deployment, and golden assertions are never edited to make a build pass.

1. **Harness, about 1–2 days.**
   - Build the fixture runner and scorer (§4) in `mode: 'net'`, with a per-trade scorecard.
   - List the fixtures that fail today.
   - Fix the two code bugs: the saw-cut waste case (#27) and the PT-7 key case (#25).
   - Correct the runner rule in `QUANTITY_ENGINE.md`.
2. **Profile and convention changes.** Most are existing conventions or one-line additions:
   #2, #9, #17, #1, #23, #5, #26, #8, #3, #31, #32. Each flips a known set of fixtures from fail to
   pass.
3. **Ingestion and reading rules,** in the takeoff adapter and the legend import:
   - #7: row keying, `NAN`, RFI rows;
   - one parser for the name grammar (heights, `BS`, `(n)`, `*N`, `@ L`, `SHTNG h`, `NO GWB`),
     reused by #13, #19 and #29;
   - #6: count once, `sameAs`, count sheet;
   - §1.8: make measurement records mandatory;
   - #4: plywood routing.
4. **New inputs and assemblies, by impact:** #10, #12, #13, #14, #15, #16, #11, #18, #20, #21, #22,
   #24, #25, then #28–#30 and #34–#37.
5. **Geometry stage,** started in parallel with step 2:
   - walls from the prototype, the scale gate, and flagged-piece resolution;
   - then site polygons and linetypes (C-1.0, C-3.0), and the A-150 finish areas;
   - then vector symbol counts.

   Regression-test each step on the A-120 fixture first.
6. **Scope integrity:** #33 and #39–#43.
7. **Cosmetic last:** the presentation profile (#38) and labels (#44, #45).
8. **Held-out validation (§5)** before any default changes or any assembly flag is turned on.

---

## 4. Using the `fixtures.json` files as a regression suite

### What exists

There are **731 cases in 24 files**, one or more per reproducible estimate line. A few folders add
extra cases:

- exact-geometry variants (`03`);
- cross-checks (`09d`: 7 lines and 4 cross-checks);
- display-precision cases (`11`: 67 cases for 65 lines).

Lines that cannot be reproduced are left out, for example `07` 149 and 162, `09c` 224, `32c` 693,
and `33` 724 and 742.

**Fields every case has:** `name`, `formula` (prose or an expression), `inputs` (values with units,
often with the legend item and page), `expected {quantity, unit}`, `tolerancePct` and `source`.

**The schema is not uniform:**

- Only `01` carries engine-ready `engineInputs` and `expectedLines` with engine keys.
- `06`, `08` and `10` name an `engineAssembly`.
- Status fields vary by folder:
  - `knownResidual` (`09a`: 14 cases, 5 of which fail by design);
  - `estimatorParity` and `perDrawings` (`32c`);
  - `knownEstimatorDeviation` (`28` L619);
  - `status: proposed-convention` (`28` L622);
  - `toleranceLF` (`22`);
  - `toleranceBasis` (`09a`);
  - `estimatorDeltaPct` and `classification`.

### Plan

1. **Normalise every case into one schema.** Proposed fields:

   ```text
   id            "<trade>:<line>[:variant]"
   lineNo, trade, assembly
   record        engine input strings exactly as a model would print them (like 01's engineInputs)
   profile       default | reviewed-commercial | estimator-rounding
   mode          net
   expect        [{ key, quantity, unit, tolerancePct, basis }]
   truth         estimator | drawings | both
   perDrawings?
   knownGap?     "<roadmap #>"
   ```

   Write one converter per folder. Before trusting a converted case, check that an independent
   evaluator reproduces its own expected value; the folders did this already (for example `09a`
   and `06` `check_fixtures.py`).
2. **Run three tiers.**
   - **Formula tier:** records → `expandMeasurements` → lines, in net mode. Fast; one case per
     estimate line.
   - **Reading tier:** `reference/markups/legends.json` → records through the adapter. This tests
     legend keying, the name grammar, `NAN` handling and count-once, against the same expected
     values.
   - **Geometry tier:** the A-120 vector fixture, using `results.json` and
     `compare_to_markup.py`. Tag-typed runs must stay 100% under the estimator's colour. With the
     estimator's assignments, each type must be within 6%, except D3C, which must be within 1 ft.
     Add sheets as the stage grows.
3. **Treat known gaps as expected failures.** Tag each case with the roadmap item that should fix it
   (`knownGap: #n`) and run it as expected-fail (vitest `it.fails`). The suite is green today; a
   fix flips its cases and forces the marker to be removed. A case that flips the other way is a
   regression.
4. **Keep two answer keys where they differ.** That covers `32c` 699/709/711, `28` 619, `04`
   40/70/72/73, `03` strict, and the `11` shade line. The default profile asserts the drawings; the
   estimator profile asserts the estimator. Never tune a default toward a documented estimator
   error.
5. **Set tolerances by class, never per line.** 0 for counts; 0.01% for exact formulas; 0.5% for
   Σ LF and LF × H; 1% for legend display rounding; `toleranceLF` = 0.05 per legend row (`22`).
   Never widen a tolerance to make a case pass, the same rule as the app's golden assertions.
6. **Scoring.** Map engine keys to estimate lines; several engine lines may sum to one estimate
   line, as with formwork. Class unmatched engine lines as "beyond estimate", "inside allowance" or
   "breakdown component", not as misses.
7. **Report** the per-trade scorecard (within 1% / 5%, failures by roadmap item) on every engine
   change, and keep the history.
8. **Confidentiality.** The fixtures carry quantities and descriptions from a client's bid. Keep
   them private, and never copy `source/` into the app repository.

---

## 5. What must be validated on a second, held-out job

All of this rests on one job, one estimator and one CAD template, and many conventions were fitted
on a single line. Before a convention becomes an engine **default** rather than an opt-in profile,
run a job that was **not** used to tune any rule. Ideally it has a different architect and CAD
template, a different estimator, and a different building type.

### 5.1 How strong each convention's evidence is

| Strength | Conventions |
|---|---|
| Fitted to one line or one total (hypotheses) | Formwork ceil to 10 SF (`02` 30); parapet per-row ceil (`09a` 254); 6" pad working space (`31` 629, total only); 3' × 5' trench (`33` 740; 2.5 × 6 and 2 × 7.5 fit equally); weep screen = LF × 0.33 (`32b` 683); bracing placement (`09b` 291); 16 ft shade drop (`11`); 10 ft per storey (`01`); grout ×1.10 then ceil 50 (two lines, `09c`) |
| Several lines, one trade or one house | Finish SF ceil 5 (`03`, `09a`, `07`, `05`; only 7 of 11 small lines in `09e`); LF up to 0.5 (`02`, `03`); 2-decimal feet (`02`, `03`, `09a`); the per-SF board ratios (`09a`, `09b`); duct bare-surface basis (`23`, two lines); 2,000 SF allowance basis (four lines) |
| Seen across many trades and common in published practice | Net quantities without waste; route LF for bundles; each object counted once; one line per description; gross through openings for framing and board. Practice for paint and sheathing varies between estimators. |

**Rule.** A convention becomes a default only if (a) the held-out job's estimator does the same, or
(b) a published standard supports it. Otherwise it stays in a named profile, and every score states
which profile it used.

### 5.2 Reading and geometry to re-check

- **Vector stage on another CAD template:**
  - style-profile detection;
  - scale-gate pass rate;
  - per-type error with automatic assignment;
  - LF flagged for the AI or the user;
  - how many walls are drawn only in thin lines.
- **Text layer:** the share of sheets that have one, and whether raster schedules are found and read
  correctly by two readers.
- **Vision:** counts near 1% and areas at 2.6–3.8% on a different symbol set and drafting style.
- **Model choices:** whether Haiku, Opus and GPT-6 Astra keep their roles on the new set.

### 5.3 End-to-end acceptance

- **Run** with measurement records on the path and a frozen engine and profile, in `mode: 'net'`.
- **Score** per line against the second estimator's takeoff. Separately, score a sample against
  independent drawing-truth checks, as the trade folders did.
- **Report** per trade:
  - lines within 1% and within 5%;
  - flagged, untyped and unknown quantities;
  - conventions where the two estimators differ.
- **Suggested gates** before record-driven assemblies become the default. These are judgment;
  adjust after the run.
  - Counted lines are at least 98% exact.
  - Measured LF/SF lines where vector geometry exists are at least 90% within 5%.
  - No Tier 1 failures.
  - Every unknown quantity shows `—` and blocks a final number.

### 5.4 What would change this plan

- **If the second estimator deducts openings or carries waste,** those stay contractor profile
  choices, not defaults.
- **If the second CAD template breaks the stroke-style profile,** the geometry stage needs AI style
  detection, verified by code, before rollout.
- **If counts or schedules regress on another drafting style,** the two-reader + settle pattern
  moves from "hardest items" to "every value".
