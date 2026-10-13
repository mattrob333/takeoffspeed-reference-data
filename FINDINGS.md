# How a professional estimator takes off a building, and what an AI takeoff must do to match it

This is the cross-trade synthesis of the 24 folders under `trades/`. Each folder reverse-engineered
how one professional estimator produced every quantity on one real job, a single-storey bank branch
of about 1,900 SF on a 0.96-acre site. The evidence was their PlanSwift markups (92 pages), the
issued drawings (136 sheet files) and the 484-page project manual. A second model then tried to
refute each folder, and the folder was corrected. The scope is **material types and quantities**.
No price, labour or dollar figure is used anywhere.

Line numbers below are estimate line numbers (`reference/estimate/lines.json`). Trade folders are
cited as `01`, `09a` and so on. Each claim comes from that folder's `README.md`, `formulas.md`,
`reconciliation.csv`, `reading-guide.md` or `app-gaps.md`.

---

## 1. The headline numbers, and what they do and do not mean

The estimate has 742 lines. Line 1 is a lump-sum General Conditions line. The other **741 lines**
are split across the 24 trade folders, with no gaps and no overlaps (`reference/estimate/trades.json`).

| Result (computed from the 24 `reconciliation.csv` files) | Lines | Share |
|---|---:|---:|
| Rebuilt within 1% of the estimator's quantity | 702 | 94.7% |
| … of which allowance or copied lines that match by construction (1 LS = 1 LS, or a copy of another line) | 7 | |
| Rebuilt within 1% from a real measurement, count, schedule or formula | 695 | 93.8% |
| Rebuilt within 5% | 724 | 97.7% |
| No recomputed value (allowance with no rule, a fitted factor, or a hand-typed `NAN` row) | 8 | 1.1% |

**What this proves.** The formulas reproduce the estimator, line by line, **from the estimator's own
measured inputs**: the lengths, areas and counts in their PlanSwift legends, plus the schedules and
notes. We now know the rule behind almost every quantity.

**What it does not prove.** It does not show that the TakeoffSpeed app reads the plans that
accurately. Nor does it show that the estimator's measurements match the drawings. Three facts
make the difference plain.

- **The estimator's measurements are not always the drawing.** Where folders measured the drawing
  independently (CAD vectors, dimension strings, unmarked sheets), most measured lines agree to a
  few percent, but some do not:
  - `01`: 8 of 9 CAD checks are within 3%, and the ramp (line 7) is +6.0%.
  - `03`: brick lines 32/35, measured strictly from the drawing, are −3.4%. The estimator's markup
    runs about 3.5 ft past a building corner.
  - `04`: four lines differ from the drawings. Line 40 is 236.34 LF against about 172 LF
    schedule-true (−27%). Lines 70 and 72 (joists) are +9.08 and +12.53 LF. Line 73 (deck) is
    about 8.3% high.
  - `32c`: three lines are not supported by the drawings, at −32% to −69% (section 4).
  - `28`: line 619 is 2 against the drawing's 3.
- **The app does not yet read this well.** `docs/QUANTITY_ENGINE.md` in the app records:
  - 72% of 38 interior material families within 10% in its best run (run 10). In that run the model
    wrote the lines itself, so the quantity engine was not on the path.
  - On the wall system, 8 of 41 lines within 5%, with a median absolute error of 20% (run W8).
  - Runners 26–58% short, because run length is wrong.
- **Vision models cannot measure undimensioned lengths.** In `vision-benchmark/`, every model
  measured partition LF by wall type with 19–55% error. A prototype that measures the same walls from
  the PDF's vector line work gets the six-type total within 1.5% (`vision-benchmark/vector-geometry/`,
  and `APP-ROADMAP.md` §1.3).

So the reconciliation is a **specification of the arithmetic and the conventions**. Turning
drawings into the inputs is a separate problem, and most of the remaining error is there.

---

## 2. What kind of number each line is

Each reconciled line is classed by how the estimator got it. The table uses the first-named class
in each `classification` field (for example, "measured+derived" counts as measured).

| Class | Lines | Share | What it is | Typical examples |
|---|---:|---:|---|---|
| **Counted** | 297 | 40% | A PlanSwift dot on each symbol, tag or schedule row | 96 electrical devices and fixtures (`26`); 42 HVAC devices (`23`); doors and hardware sets dotted **on the A-600 schedule rows, not the plan** (`08`, lines 190–206); storm structures dotted on the C-4.0 **table rows** (`33`, lines 730–733) |
| **Measured** | 202 | 27% | A legend length or area copied to the line, sometimes rounded | Curb removal 987.22 LF (`01` line 2); 15 of 18 flooring lines (`09c`); 34 steel members (`04`) |
| **Derived** | 159 | 21% | A formula applied to measured or scheduled inputs | 30 gypsum accessory lines from per-SF ratios (`09a`); footing CY from LF × section (`02`); duct LBS from surface SF (`23` line 446) |
| **Specified** | 66 | 9% | A value printed on a schedule, table or plant list, not measured | 41 furniture tags at 1 EA "V.I.F." because they are scheduled but not placed (`11`); storm/sanitary LF summed from the engineer's pipe tables (`33` lines 721–723); base plates from the schedule COUNT column (`04` lines 75–77); the plant list (`32c` lines 701–706) |
| **Allowance / judgment** | 15 | 2% | A number with no reproducible rule | Fittings allowances at 1 LS on an "AREA: 2000 SF" basis (`22` 403, `23` 445, `26` 510, `28` 622); 910 LF of assumed trim (`05` 88, copied to `09e` 304); 1,330 LF of opening sealant (`07` 149); a 10 SF mat (`09c` 224); 42 CY of trench haul (`33` 742); two `NAN` legend rows typed by hand (`26` 497, 541) |
| **Unresolved** | 2 | <1% | A numeric fit on a factor that no drawing prints | Plywood sheathing lines 83 and 85 (`05`) |

**What this means for an AI takeoff.** Two thirds of the estimate is counts and straight
measurements. Counting is solved for strong vision models (about 1% error); measuring undimensioned
lengths from images is not (section 1). The derived fifth is pure arithmetic: once the convention is
known, code can do it exactly. The specified tenth needs reliable schedule reading, and many
schedules here are images with no text layer. The allowance sliver must be carried as labelled
allowances, never as invented measurements.

---

## 3. The measurement conventions the estimator follows everywhere

These habits recur across trades. Each one changes quantities by more than any formula detail.

### 3.1 No opening deductions on framing, board, sheathing, insulation or paint runs

The estimator runs straight through doors and windows.

| Trade | What is not deducted | What deducting would do |
|---|---|---|
| `05` | Exterior plywood sheathing, line 82, measured full height "through the glass" at storefronts | About 888.6 SF of glazing and doors: −29.3% on 3,057 SF |
| `09a` | Gypsum board, line 242 (7 interior doors × 2 faces) | −298.7 SF (−4.97%), carried into its 5 accessory lines |
| `09a` | Studs and runners: stud SF = Σ LF × H; top runner = bottom runner = Σ run LF | Jamb, corner and run-end studs add +1.6% to +8% |
| `09e` | Paint runs on A-150 (339.1 LF of room-face runs at room heights) | The app's partition paint path is recorded at +21% to +25% |
| `07` | Cavity batts (lines 152–156); the fluid-applied barrier (184) gets no returns at openings | Engine returns would add 172 SF (+5.8%) |

The one exception is the restroom paint *elevation* polygon (`09e` line 295). It is cut around the
door, but its copy for the Men's room is not, which leaves about 23 SF of door in the total.

### 3.2 Heights are typed into the item name, not scaled from the plan

The plan gives the run length. The height comes from sections and the RCP, and the estimator types
it into the PlanSwift item name.

- `09a` and `05`: `WALL A3A @ 12'6"H`, `EXT 8" STUD WALL @ 15'9"H NO GWB`, `PARAPET WALL @ 4'7"H`.
  The name suffix `SHTNG 10'3"H` overrides the wall height for sheathing (`05`).
- `09b`: soffits carry **two** heights in one name, `SOFFIT @ 5'9"H, GWB @ 2'6"H`. The framing
  height and the board height differ.
- `03`: `4"THK. CMU STEM WALL W/ GROUT CAVITY SOLID @ 1'4"H`, giving line 31 = LF × 1.33.
- `09d` and `09e`: `WC1 @ 12'H`, `PT1 PAINT @ 9'H`, `FRP-1 @ 4'H`. Every paint height except one
  is a ceiling height printed on A-130.
- `04`: count items with a length in the name. `HSS4x4x1/4 POST @ 1'4"H` × 6 EA is converted to
  LF (lines 36, 37).

Other suffixes in the names act as multipliers:

| Suffix | Meaning | Folder |
|---|---|---|
| `BS` | both sides, so two board faces | `05`, `09b` |
| `NO GWB`, `SHTNG ONLY`, `1 SIDE` | face counts | `09a` |
| a leading `(7)`, `(4)`, `(3)` | rows of blocking. The engine's default of 1–2 rows gives −40% to −70% on line 89 | `05` |
| a trailing `*2` | two pieces per run. Line 65: 121.9 FT × 2 | `04` |

**An AI must parse this name grammar.** The plan alone cannot give these quantities.

### 3.3 Bundles are measured by route length

- `26`: "(2) 4" conduit 101.71 LF" (line 505) is 101.71 LF of trench route carrying two conduits,
  not 203.42 LF of conduit. Across the six conduit lines the route is 279.62 LF. Multiplying by
  the number of conduits gives 617.54 LF (+120.8%).
- `33`: the gas, water, power and telephone services are route LF.
- `01`: line 12 "power line" is one keynote covering overhead power, underground power and
  telephone linework (965.36 LF). The keynote decides the line, not the linetype label.

### 3.4 Counts are summed across sheets, but each object is counted once

The estimator adds the same item name across pages: plan, enlarged plan, elevation, and even a
mechanical controls sheet (`26`: M-503 disconnects). An object drawn on two sheets is still
counted only once:

- `22`: every fixture is counted on P-302 only, although the same tags repeat on P-301 and on the
  P-402 isometric. Summing them would triple WC, LAV, SK-T, SK-U, MS and EDF, and double EWH, CP,
  HB and RH.
- `10`: toilet accessories are counted on enlarged plan 6 only. The elevations repeat the tags:
  27 tags in the text layer against 16 objects (+69%).
- `26`: markup page 87 is a reprint of page 42 and adds nothing. The LCP on page 49 repeats the
  one on page 46.
- **The estimator slipped once.** `33` line 739 (irrigation backflow) is 2 EA because the device
  was dotted on both p42 and its reprint p87. The physical count is 1.
- `04`: each column is meant to be measured once, in one elevation. C-6 and D-6 were measured in
  two elevations (40.86 LF counted twice), which is why line 40 is 27% over schedule-true.

### 3.5 One line per description

A line is one material description. What the estimator splits and merges is consistent within a
trade, but not across trades:

- **Split:**
  - receptacles by plate colour or engraving note (`26`, 19 receptacle lines);
  - air devices by type + face + neck + CFM (`23`, 21 lines);
  - furniture by tag, with suffixes as separate tags (`11`: SS-03A and SS-03B);
  - gas pipe by location (`22` lines 418 and 419: 1" on the roof, 1" below grade);
  - one set of five accessory lines per board type (`09a`, six sets).
- **Merged:**
  - pipe by system + size across below-grade, above-ceiling and roof locations (`22` line 404:
    3" storm = 33.5 + 25.8 + 91.2 = 150.59 LF);
  - two concrete keynotes in one line (`32a` line 634: 241.8 + 505.8 SF);
  - all formwork in one line (`02` line 30);
  - five 3/4" casework backing rows in one line (`05` line 146);
  - STOP and DO NOT ENTER sign footings in one line (`32b` 654);
  - doors by type, ignoring undercut remarks (`08`).
- **Bundled into the description, with no quantity line:**
  - the slab line names its mesh, vapour barrier and gravel (`02` line 16);
  - brick ties, mortar and weeps (`03`);
  - faucets folded into their fixture line (`22`);
  - footing counts as text, "NO OF FOOTINGS: 5" (`32b`);
  - duct fittings, hangers and sealant inside the 1 LS allowance (`23` 445).

The engine must reproduce this keying, or it will score as missing lines and extra lines even when
the quantities are right.

### 3.6 Rounding

Large lines keep full PlanSwift precision (`09e` 3,710.84 SF; `22` 2-decimal LF). Small lines,
and lines the estimator typed by hand, are rounded. The habits:

| Habit | Examples |
|---|---|
| Feet-inches written as 2-decimal feet | 1'-4" = 1.33, 3'-8" = 3.67, 4'-4" = 4.33, 18'-8" = 18.67 (`02`, `03`, `09a`); 16" O.C. = 1.33 ft as a divisor (`09b` line 284: 516.0 / 1.33 = 387.970 LF) |
| Run LF rounded up to the next 0.5 ft before × height | Stem wall 193.8 → 194.0 (`02` line 27); CMU 157.4 → 157.5 (`03` line 31) |
| Finish areas rounded up to the next 5 SF | Brick 395.7 → 400 (`03` 32); specialty board 37.2 → 40, 252.6 → 255, 282.6 → 285 (`09a` 248, 260, 266); 14 cladding and sheet-metal lines (`07`); backing (`05` 145–147); 7 of 11 small paint lines (`09e`) |
| Concrete flatwork rounded up to a whole unit | 747.6 → 748, 1,834.7 → 1,835, 113.3 → 114, 993.9 → 994 (`32a`) |
| Circle areas rounded to 2 decimals after the diameter is | 16" → 1.33 ft → 1.39 SF (`32a`, `32b`) |
| Others | Demolition volume to the nearest 10 CF (`01` line 3: 89,780); grout = ceil to 50 SF of 1.10 × tile SF (`09c` 225, 226: 946.11 → 1,050; 244.13 → 300); allowance area 1,900 → 2,000 SF (`22`, `23`, `26`, `28`); per-LF accessories on whole feet, 36.22 → 36 (`32b`) |

The rounding is not always consistent. The A-140 nailers go 45.3 → 46 but 148.1 → 148 (`05`),
some millwork areas round down (6.2 → 6, `06`), and wall-covering lines built from the same runs do
not round (`09d` 239/240 against `09e` 298). **Rounding is presentation, not measurement.** Keep the
exact net value, and reproduce an estimator's rounding only through an explicit profile.

### 3.7 Per-SF component ratios instead of take-offs

Components are rarely counted. They are ratios applied to a parent line.

| Parent | Ratio | Folder and lines |
|---|---|---|
| Any board SF (gypsum, Type X, MR, glass-mat, 5/8" and 1/4" cement board) | sheets = SF / 32; adhesive 0.031 tubes/SF; tape 0.375 LF/SF on 500 LF rolls (0.00075 rolls/SF); screws 3/560 lb/SF (0.005357); compound 0.53 lb/SF. The same five ratios are used for cement board and glass-mat | `09a` 243–277 (30 lines), `09b` 279–283, 286–290 |
| Wall framing | stud SF = Σ LF × H; runner LF = Σ run LF; stud counts only as notes in the description | `09a` 308–321 |
| Ceiling and soffit framing | joists LF = SF / 1.33; soffit studs = Σ L × H / 1.33 + bracing | `09b` 284, 291 |
| Rectangular and round duct | LBS = bare surface SF × 0.906 (26 ga); insulation SF = the same bare SF, with no seam, lap or waste factor | `23` 446, 447 (1,324.81 SF → 1,200 LBS and 1,325 SF) |
| Site CMU | grout 0.0112 CY/SF (solid); mortar 0.1675 CF/SF | `32b` 669, 670 (about 2.7× and 1.75× the physical rates) |
| Sidewalk | expansion joint LF = SF / 25 | `32a` 636 (1,835 / 25 = 73.4) |
| Buildings removed | CF = footprint SF × stories × 10 ft | `01` 3, 4 |
| Stacked practices | each practice repeats the zone SF (DS1 = DS2 = DU; DS3 = SS) | `32c` 689–698 |
| Finishes that follow other lines | vapour barrier = brick SF (`03` 35); fluid-applied barrier = cladding lines + canopy sheathing (`07` 184); PT-3 ceiling paint = ceiling board + soffit board (`09e` 300 = 278 + 285) | |
| Excavation | 1'-0" working space each side of the wall-footing trench, 6" each side at spread pads (`31` 629); one 3' × 5' section for all site drainage trench (`33` 740) | |

### 3.8 Waste is not carried

Every measured line in all 24 trades is net. Nothing is added for:

- concrete waste (`02`);
- pipe waste or stick rounding (`22`);
- duct seam allowance (`23`);
- shrink or swell (`31`): line 641 is plain fill − cut, 786.25 − 634.41 = 151.84 CY;
- membrane or geotextile laps (`07`, `32c`);
- tile or carpet waste (`09c`, `09d`).

The only uplift is the grout rule in `09c` (×1.10, then round up).

**Spec-required attic stock is also not carried:**

- 10% ACT (`09b`);
- 10% tile, carpet, LVT and base (`09c`, `09d`);
- 10 extra fixtures each of types C and UC (`26`, E-600).

These are scope findings, not waste. Any engine that adds waste or packaging must keep it out of
the scored quantity.

---

## 4. Where the estimator departed from the documents, or missed items

The estimate is ground truth for **conventions**, not for physical truth. These are the places where
the folders found the documents and the estimate disagree. An AI takeoff should reproduce the
convention, flag the deviation, and never tune itself to an error.

### 4.1 Missed or under-counted

| Folder | Line | What | Size |
|---|---|---|---|
| `28` | 619 | Teller-line **alarm interface** (tag 18, `AI`, between the two hold-up buttons under the transaction bar) was not dotted. E-150 shows three tag-18 bubbles. | 2 carried vs 3 drawn (+50%) |
| `10` | 322–323 | 36" rear-wall grab bar, drawn on elevation 9 and printed in detail 2/A-410 (ADA 604.5.2) | 2 EA missing |
| `10` | — | Knox box (G-001), and the fire extinguishers themselves (spec 10 44 16; line 335 is the cabinet only) | 1 EA + 2 EA not carried |
| `23` | 480 | RTU condensate drain: two RTUs, but RTU-1's keynote 2 was missed | 1 vs 2 |
| `04` | — | Column D-5 is HSS6x6x1/4 on the schedule, with no line of its own (it sits inside line 40) | 20.21 LF |
| `01` | — | A ticked `///` GAS line with no keynote; and the full-depth saw cut that general note 3 and C-0.1 require | 87.1 LF and 0 LF carried |
| `09e` / `09d` | 298, 240 | A second PT-7 (wall-covering primer) tag on the Gathering Area 103 north wall. Only PT-4 was measured on that wall. | about 106 SF of primer, and the wall covering it implies |
| `02` | 16 | Vapour barrier written as 10 mil; spec 07 2616 says 15 mil | description only |

### 4.2 Over-measured or counted twice

| Folder | Line | What | Size |
|---|---|---|---|
| `04` | 40 | HSS6x6x3/8 columns: C-6 and D-6 measured in two elevations, D-5 included, and one stray run | 236.34 vs ≈172 LF (−27% to the schedule) |
| `04` | 70, 72, 73 | Low-roof joist lines and the deck polygon snapped 3.3 ft north of grid B, so a strip is double-painted | +9.08 and +12.53 LF; deck about 170–193 SF (≈ −8.3%) |
| `07` | 150, 189 | The same 221.96 LF of exterior sealant carried twice | 221.96 LF |
| `07` | 162 | Roof membrane: 302 SF with no drawing basis | 3,042.77 vs 2,740.47 SF rebuilt (−9.9%) |
| `06` | 116 | Library PL-1 legend polygon fills the cased opening and runs over the title block | 95.6 legend vs 53.06 SF rebuilt (+81%) |
| `09e` | 296, 297 | The PT-6 recess back wall is also inside the PT-4 run | 37.2 SF, 24% of line 296 |
| `09a` | 310 | A 6" stud group at 9'-0" that no drawing shows | 53.1 SF; a drawing-faithful line 310 is −16.5% |
| `23` | 452 | Refrigerant trace follows both drawn pipes plus a 7.97 ft leg with no pipe under it | 30.9 LF vs 11.75 LF of route |
| `32c` | 711 | Storage stone depth applied to the whole pond footprint, not the 962.4 SF stone bed | 626.19 vs 196.04 CY (−68.7%) |
| `32c` | 709 | Geotextile taken as pond SF; per C-4.2 it wraps the stone bed | 3,074 vs ≈2,081 SF (−32%) |
| `32c` | 699 | Phase 3 inlet protection copied from Phase 2. The Phase 3 legend row (Sd2-P, 74.5 FT) was measured but feeds no line | 194 vs 74.5 LF (−61.6%) |
| `32c` | 700, 706 | Landscape sod and ESPC final sodding cover the same lawns | 11,500 + 14,393.68 SF against 20,876 SF of pervious site |
| `33` | 739 | Counted on a page and on its reprint | 2 vs 1 |
| `03` | 32–35 | The p12 markup runs about 3.5 ft past the NE corner | ≈ 9.2 SF; strict −3.4% |

### 4.3 Assumptions with no document basis

These are the estimator's own numbers. They are legitimate as house conventions, but they are not
in the documents:

- `01`: 10 ft per storey for building demolition. No height appears anywhere.
- `11` line 345: a **16 ft shade drop**. The documents support at most a 10'-0" or 12'-0"
  storefront head, which gives 737.6–885.1 SF against 1,184.4 (−25% to −38%).
- `33` 740: a 3' × 5' trench section. C-6.2's `O.D. + 18" MAX` would give 3.25 ft for the 18" pipe.
- `32a`: "ASSUMED DETAILS" pavement sections, heavier than the geotech report that the C-3.0
  Pavement Legend references: 8-1/2" of asphalt against 3" for heavy duty. This changes no SF line.
- `32a` 675–677, 659–662: the dumpster bollard pier depth (3'-0") and the bike-rack footings
  (12" × 12"). Neither is drawn.
- `09a`: every exterior stud flattened to 16 GA. The S-002 schedule calls 43, 54 or 68 mil by
  height band. The wall + parapet rows are one continuous 17'-4" stud, so 800S162-68.
- `05` 88: 910 LF of trim, "ASSUMED". `07` 149: 1,330 LF of sealant. `32b` 683: a weep screen of
  11.88 LF = 36 × 0.33, apparently a unit slip, since the physical length is about 36.22 LF.

### 4.4 Scope carried against the responsibility documents

- `09d` lines 239–240: the spec responsibility matrix (01 2200 attachment, p15) makes vinyl wall
  covering **furnished and installed by the owner**. The estimator carried 223 SF anyway. Line 240
  has no wall covering drawn at all; it is inferred from a primer-only paint tag (PT-7).
- `06`: A-110 General Note K makes all millwork owner-vendor furnished. The estimator carried 48
  lines and noted "INSTALLATION BY THE G.C. IS ASSUMED".
- `10`: TA-09 coat hooks (line 327) are also inside hardware set 11.0 (line 205), so they are
  carried twice.
- `11`: vendor/vendor appliance and bank-equipment rows (AE-09…AE-15, BE-01…BE-11) were omitted.
  That is consistent with the schedule, but it is a choice.

### 4.5 Boilerplate and missing spec sections

The project manual cannot be trusted section by section:

- **Copied from another project:**
  - 28 7250 Security System describes "Office, Warehouse, Fuel and Vehicle Repair", a Wells Fargo
    SMT-4 and 12 overhead door contacts. None of it applies; quantities come only from the E-150
    schedule (`28`).
  - The assumed asphalt section uses NYSDOT terms (F2 / F9 / Type 2) on a Georgia job (`32a`).
- **Listed in the table of contents but not bound:**
  - 02 4116 and 02 4119 demolition (`01`);
  - 31 1000 Site Clearing (`01`);
  - 09 7200 Wall Coverings (`09d`);
  - 32 3913 bollards (`32a`).
- **Missing entirely:** there are no Division 31, 32 or 33 sections (`31`, `32c`, `33`) and no CMU
  section (`03`).
- **Misleading or describing work that is not there:**
  - 04 7200 is titled Architectural Stone Veneer, but its body is cast stone (`03`).
  - 08 4413 specifies a curtain wall that is not drawn (`08`).
  - 09 6519 specifies 12" × 12" VCT; the drawings show LVT plank (`09c`).
- **The reference index itself was wrong** in places. `spec_index.json` omits 07 2413 and 07 5423
  and gives the wrong range for 07 4213 (`07`).

An AI should check that each spec section describes this building before it uses any number from it.

---

## 5. Document conflicts found

In nearly every case the estimator followed the drawing. Most conflicts change a material
description, not a quantity, but each one is an RFI that a reviewer would want flagged.

| Folder | Spec (or one drawing) says | Drawing (or the other drawing) says | Estimator followed |
|---|---|---|---|
| `02` | 15 mil vapour retarder; #57 stone 4" "where shown on drawings" | none shown; joint spacing ≤15 ft (S-001) vs ≤12'-6" (S-201) | 10 mil in the text; 4" gravel assumed |
| `03` | Veneer anchors ≤ 24" × 18" and ≥ 1 per 2 SF (≈198 ties) | 32" × 16" (≈111 ties); S-600 shows a shelf angle that A-430 does not | no tie count carried |
| `04` | Deck 20 ga; A.X. bridging L2-1/2 (05 1200) vs 2x2x1/4 (05 2100); steel ladder | Deck 22 ga; aluminium O'Keefe's ladder | drawings |
| `06` | Countertop core 3/4" plywood; 1 grommet per 4 ft of top | 1" and 1-1/2" cores drawn | drawings; grommet rule not carried |
| `07` | Cover board 1/2" glass-mat | 1/4" cover board | drawings |
| `08` | Kawneer Trifab storefront | YKK YES45 TU / FS | drawings |
| `09a` | 5/8" Type X on all vertical surfaces; parapet glass-mat 5/8" Type X | 1/2" glass-mat at parapets | drawings |
| `09b` | Ceiling board 1/2" | 5/8" board; 6" studs at the cloud cove and beam wrap | 5/8", all studs carried as 3-5/8" |
| `09b` | ACT-2 24" × 48" (A-170, A-131) | estimate text says 24" × 24" | wrong in the text only |
| `09c` | VCT 12" × 12" | LVT 25 cm × 1 m; FTS-1 schedule (Schiene) vs detail 1 (Reno-TK); restroom wall 7'-3 1/2" (elevation) vs 7'-8 1/8" (plan) | drawings; the elevation |
| `09e` | A-130 note E: gypsum ceilings PT-1 | RCP tags and the A-170 GWB-1 row say PT-3; PT-5 semi-gloss vs eggshell; PT-6 eggshell vs "FLAT BLACK" | PT-3 |
| `10` | Extinguisher 4-A:60-B:C | G-001 legend 4A:80B:C | — |
| `22` | Type L copper above ground, Type K below (22 1000) | P-101 materials table: PEX-A primary; PVC vs cast iron above ground; floor-drain grate square vs round; 3" vs 4" VTR | open |
| `23` | G90 galvanizing; 2.2" R-6 duct wrap | M-001 says G60; the estimate text says 1.5" | — |
| `26` | Duplex receptacles 15A (§2.9 A, naming 20A models) | 20A 125V on every plan | 20A |
| `28` | Smoke detectors in telephone and electrical rooms (§2.4.F.4) | one detector drawn | drawing |
| `32a` | Keynotes 3/4/18/21 point to C-6.2 for pavement | C-6.2 is sanitary only; the Pavement Legend points to the geotech report; C-3.0 draws 5 dumpster bollards and A-190 draws 6; civil and architectural bollard details differ | C-3.0 (5 bollards); assumed sections |
| `32b` | 15 mil vapour retarder; cleanout pad 6" (plumbing) | A-190 10 mil; estimate text 8" | — |
| `32c` | Plant list: 5 holly, 11 redcedar | plan callouts: 11 holly, 6 redcedar; sock "AT LEAST 18" DIA" vs the estimate's 30" | the plant list |
| `33` | 22 1000: underground water Type K copper | C-5.0: 1" PVC | civil drawing |

---

## 6. Reading traps

These are the places where a reader, human or AI, goes wrong on this job. Most are general.

### 6.1 Legend and markup data

- **Duplicate and truncated legend names get merged.** A legend extractor that keys rows by name
  loses rows. That happened in this repository's own first extraction (`tools/workflows/markup-legends.js`,
  since fixed):
  - `28` p48: two rows named `FIRE ALARM ADA AP...` (9 horn/strobes, 3 visual alarms). Losing one
    zeroes line 627.
  - `23` p53: 8 of 55 rows dropped, and three restored rows carry the wrong colour.
  - `32c` p65: two `DS1, DS2 & DU` rows (20,298.9 and 15,581.9 SF). Losing one costs 20,298.88 SF on
    each of three lines.
  - `04` p34: HSS6x4x3/8 appears twice (22.2 and 9.0 FT).
  - `31` p73: a duplicate 439.5 row.
  - `32a` p72: `21: HEAVY DUTY CONCRETE PAVE...` names both the 241.8 SF pavement (this trade) and
    the 384.3 SF dumpster slab (`32b`).

  **Key every legend row by page + name + colour + quantity.**
- **`NAN` rows.** PlanSwift prints `NAN EA` where a count was never computed (`26` lines 497 and
  541, where the estimator typed 1; `06` "NO"). Treat these as unknown, never as 0 or 1.
- **Rows that are not items:**
  - unnamed rows: `Linear`, `5`, `7`, `9` (`06`); a `Linear` row that turned out to be the sill pan
    (`07`);
  - a placeholder dot on an RFI note (`28` p47, `RFI: Per Sheet Notes 1 and 4…`);
  - a dot on a sheet note that becomes the allowance line (`28` p48, `ALLOWANCE FOR W...`).
- **Markup geometry errors:**
  - polygons that overshoot onto blank paper (`03` p12) or onto the title block (`06` A-702);
  - polygons drawn on not-to-scale 3D views (`06` A-706 det. 10);
  - a joist line snapped 3.3 ft off grid (`04`);
  - the same colour used for two items on one page (`06` A-707: base splash and blocking).
- **Off-plan segments.** Vertical drops are drawn as off-plan segments in the run's colour, so the
  risers are already inside the legend totals (`22`). Adding risers from the isometric counts them
  twice.
- **Clipped-looking legend boxes.** Every markup page is a raster that stops 24 pt above the sheet
  bottom, so legend boxes look clipped (`22` p59, p60). Completeness was established by checking
  that every coloured mark has a legend row.

### 6.2 Scale

- **Mixed scales on one sheet.** A-707 has 1/2" = 1'-0" plans and 3/4" = 1'-0" elevations. A
  linear item measured at the page scale reads 1.5× long: 16.5 FT against a true 11.04 LF (`06`).
  The same thing happens on A-701, where the page scale is 3/4" and one section is 1-1/2" (`08`).
  Calibrate each viewport separately.
- **Not-to-scale pieces inside dimensioned drawings.** A-702 elevation 2's `3'-6"` bay is drawn
  about 2'-6" wide (`06`). Use the dimension string, not the pixels.
- **Calibrate from the printed dimensions.** The vector prototype paired 83 printed dimension
  strings with their ticks on A-120. Measured span / printed value = 1.00098 to 1.00100, so the PDF
  is uniformly 0.1% larger than nominal. Do not trust the title-block scale alone.

### 6.3 Text and schedules

- **Raster schedules with no text layer.** A-170 SCHEDULES holds the finish, furniture, appliance
  and bank-equipment schedules, but its text layer has only 844 characters, just the titles. Every
  finish tag's product, size, MIX %, trim, "48" H" FRP and "PT-7 = primer" comes from the image
  (`09c`, `09d`, `09e`, `10`, `11`). The C-6.1 to C-6.3 civil details are also raster (`33`).
  Without a vision pass on these, the engine never gets `blend`, `primerTag` or `topEdge`.
- **Text-layer look-alikes:**
  - door and window tags (9.51 pt) sit next to grid bubbles (12.51 pt) in the same font (`08`);
  - tag A appears only on A-120, not on A-110 (`08`);
  - the A-110 notes come out of the text layer as two separate lists, letters and text (`11`);
  - `1.5/8"` in the text layer is note 1 followed by 5/8" (`10`);
  - `///` utility ticks are text glyphs, one every 18 pt (`01`).
- **Strings that look like the item but are not:**
  - `3'-9 7/8"` is the clearance to a pedestal, not the top length (`06` A-708);
  - `7 1/2"` is the quartz edge plus the laminate band; the band is `6 1/4"` (`06`);
  - 12'-0" is the entry-vestibule storefront head only; section 1 shows 10'-0" (`11`).
- **Wrong cross-references:**
  - keynotes point to C-6.2 for the pavement section, which holds only sanitary details (`32a`);
  - the library lines cite A701 for work on A-702 (`06`);
  - the outlet control structure says "see C-6.2", which has no such detail (`33`).
- **Schedule typos.** `16.5' SH`, `35.4"D` and `30"SH` (`11`). Copy the schedule string and flag
  it; do not silently correct it.

### 6.4 Rooms, repeats and tags

- **"Similar" rooms.** A-410 draws the women's restroom elevations once and notes "MENS INTERIOR
  ELEVATIONS ARE SIMILAR TO WOMENS". The estimator copied the polygons to count both rooms (`09d`,
  `09e`). A reader that forgets halves the restroom tile: 107.37 SF instead of 214.74.
- **Room numbers differ between sheets.** A-410 numbers the rooms MEN'S 112 and WOMEN'S 111;
  A-150 numbers them 113 and 112 (`09d`). On G-001 the estimator's restroom-sign dot colours are
  swapped (`10`). Match by room name.
- **Stacked wall tags.** `PT-4 / PT-7` means both treatments apply to that wall (`09d`, `09e`).
- **Blended tile.** One 5'-6" band in a WT-1 / WT-2 / WT-9 blend. The estimator traced the accent
  tiles one by one, so the split follows the drawn pattern, not the scheduled MIX %: by the MIX %
  the split would be +1.6% / +4.5% / −8.3% off (`09d`).
- **Multi-tag fields.** Diamond carpet insets put three tags in one room. The field must be measured
  net of the insets (`09c`).
- **What a plan cannot show:**
  - heights, which come from sections (`09a`; vector prototype);
  - walls drawn only in thin "beyond the cut plane" lines, such as the 4'-4" counter knee wall
    (18.3 LF) and the 3'-9" low wall (7.7 LF), which the vector prototype misses by design;
  - wall types where no tag leader reaches the wall.

### 6.5 Cheap completeness checks that worked

- **Impervious area.** The measured areas plus the building sum to 20,810.2 SF against the Site
  Summary's 21,033 SF (−1.06%, `32a`).
- **Disturbed area.** The disturbed-area polygons are 91.5% of the printed 0.9 AC limits of
  disturbance (`32c`).
- **Three count sources agree.** Footing counts from the legend, the schedule COUNT column and the
  plan tags all match (`02`).
- **Stall count.** The Site Summary says 11 stalls, but the circled counts on the plan add to 12
  (`32a`). The drawing contradicts itself.

---

## 7. What an AI takeoff must do to match the estimator

1. **Read every printed value from the PDF text layer.** That covers dimensions, tags, schedules
   and notes. Use vision only where the text layer is empty: raster schedules, raster details and
   scanned sheets.
2. **Measure lengths and areas in code from vector geometry, never in the model.** The model
   classifies and resolves the pieces the code flags.
3. **Count once per object.** Designate a count sheet per tag, de-duplicate across reprints,
   isometrics and elevations, and count where the estimator counts: schedule rows, table rows or
   keynote tags.
4. **Parse the PlanSwift name grammar.** That means heights, `BS`, `(n)`, `*N`, `NO GWB` and
   `SHTNG h`. Key legend rows by page + name + colour + quantity.
5. **Apply the measurement conventions explicitly**, as named settings. Section 3 lists them:
   gross through openings, route LF for bundles, net with no waste, per-SF ratios, and the
   one-line-per-description keying.
6. **Keep exact net quantities.** Put estimator rounding in a profile, never in the measurement.
7. **Carry allowances and assumptions as labelled lines with low confidence.** Never back-fit a
   formula to them.
8. **Flag document conflicts, boilerplate spec sections, responsibility (owner-furnished) scope and
   cross-trade duplicates.** Do not resolve them silently.
9. **Score against two answer keys where they differ:** what the estimator carried, and what the
   drawings support. The engine should be right against the drawings; a profile can reproduce the
   estimator.

`APP-ROADMAP.md` turns this into a ranked plan for the app.
