# 33 — Site utilities: storm and sanitary, inlets, structures, trenching

This folder covers storm and sanitary pipe, the roof-drain header, the dry and pressure service routes
(gas, water, power, telephone), structures and inlets, cleanouts, water appurtenances, and pipe
trench earthwork. It covers **22 estimate lines** (Div 33, lineNo 721–742), listed in
`reference/estimate/trades.json`. It covers quantities and material descriptions only.

**Result:** 17 of the 22 lines rebuild exactly from a drawing or legend value. 3 more reproduce
exactly only by construction. A 21st grounded line (724) is within 5%.

- Grounded (17):
  - 3 pipe lines are sums of the engineer's pipe tables (721–723).
  - 5 lines are PlanSwift legend lengths (725–728, 738). The headwall (738) is the legend length
    rounded to whole feet (ceil and nearest are indistinguishable on this job).
  - 9 lines are counts (729–737).
- Reproduced by construction (3):
  - 739 replicates a double count the folder itself calls wrong (physical count 1).
  - 740 uses an inferred section. The data fix only the area, 15 SF/LF; the estimator's
    3'-0" × 5'-0" fits, but so do 2.5' × 6' and 2' × 7.5'. The 3' width is an estimator
    convention, not a detail value.
  - 741 is excavation − the unexplained 42 CY haul allowance (742).

Two lines do not reconcile:

| Line | Item | Estimate | Best source | Why it does not reconcile |
|---|---|---|---|---|
| 724 | Gas service | 152 LF | p77 legend 156.4 FT | The legend is +2.89% over the estimate (csv basis: (recomputed − estimate) / estimate; 2.81% of the legend). 152 appears on no sheet, so it was probably trimmed or re-measured by hand. |
| 742 | Trench haul-off | 42 CY | none | A whole-CY allowance. Pipe displacement alone is 27.22 CY. See `formulas.md` §6. |

Line 739 (irrigation backflow, 2 EA) does reproduce, but only because the same device was
counted on two markup pages of E-010 (p42 and p87). The physical count is 1.

| File | Contents |
|---|---|
| `formulas.md` | Every formula, with inputs, the estimator's conventions and a worked example |
| `reconciliation.csv` | Line → source → formula → recomputed quantity → delta → classification |
| `fixtures.json` | 20 engine test cases, one per exactly reproducible line: 17 grounded + 3 by construction (739, 740, 741). 724 and 742 are left out |
| `reading-guide.md` | Which sheets, tables, legends and details to read, the exact strings, cross-checks and traps |
| `app-gaps.md` | TakeoffSpeed engine run on these inputs: what matches, what differs, ranked changes |
| `best-practices.md` | Researched industry practice (written separately; not part of this reconciliation) |

## Scope by group (estimate section path)

| Group | Lines | What |
|---|---|---|
| UNDERGROUND PIPING | 721–728 | 15" and 18" HDPE storm, 6" PVC sanitary, gas service, 8" HDPE roof-drain header, 1" PVC water, power and telephone service routes |
| CLEANOUTS | 729 | 6 × 4" sanitary cleanouts with recessed brass plug |
| INLETS | 730–731 | 5 hooded grate inlets (STGI), 1 yard inlet (STYI) |
| JUNCTION BOX / CONTROL STRUCTURE | 732–733 | 1 junction box and 1 outlet control structure; 4'-0" dia precast is assumed (no detail) |
| MISC. | 734–739 | Tapping saddle, water meter, RPZ, manhole connection, headwall (LF), irrigation backflow |
| PIPE TRENCHING | 740–742 | Excavation, backfill and haul-off for the trench |

Neighbouring lines that belong to other trades:

| Item | Lines / trade |
|---|---|
| Pond geotextile, 6" perforated underdrain (96 LF), storage stone | 708–711, 32c / 31 |
| Cleanout concrete pads | 658, 32b |
| Building-side plumbing below slab (P-301) | 22 |
| Site conduit and electrical devices (E-010) | 26 |
| Demolition of the existing storm and water lines (C-1.0) | 02 |

## Driving sheets

| Sheet | Markup page | Used for |
|---|---|---|
| C-4.0 Grading Plan | p74 | Legend: header pipe 168.2 FT, A1-STHW headwall 8.8 FT, 5 STGI, 1 yard inlet, 1 JB, 1 OCS. The **STORM PIPES** table (7 rows: name, size, length, slope, inverts, material) and the **STORM STRUCTURES** table (10 rows: name, type, station, rim, inverts). Structure Types box. Keynote 5 (8" HDPE header, min slope 1%) |
| C-4.1 Storm Profiles | p75 (no legend) | Profile callouts ("70 LF OF 18" HDPE @ 0.50%"), used to cross-check the table lengths and depths |
| C-4.2 Infiltration Basin Detail | p76 (no legend) | 18" HDPE inflow at invert 435.00, concrete riser (the OCS) rim 436.5, underdrain (other trade) |
| C-5.0 Utility Plan | p77 | Legend: 6" sanitary 295.8 FT, 6 cleanouts, gas 156.4, manhole connection, power 72.9, telephone 74.4, tapping saddle, water 138.3, meter, RPZ. The **SANITARY PIPES** and **SANITARY STRUCTURES** tables. Keynotes 1–12, General Utility Notes |
| C-5.1 Sanitary Profiles | p78 (no legend) | "50 LF OF 6" PVC @ 1.00%" callouts, rims and inverts S1–S8 |
| C-6.1 Construction Details 2 | p80 | GDOT inlet detail, GDOT manhole detail (raster images) |
| C-6.2 Construction Details 3 | p81 | City of Warner Robins standard details: SANITARY SEWER BEDDING (PVC), DROP TIE-IN TO EXIST. MANHOLE, TRACER WIRE (SEWER), CLEANOUT TO GRADE, Nyloplast 1899CGD 18" dome grate |
| C-6.3 Construction Details 4 | p82 | WATER LINE BEDDING, THRUST BLOCKS, WATER LINE CONFLICT, CUTTING-IN SLEEVE, TAPPING SLEEVE, WATER VALVE SETTING, TRACER WIRE (WATER), STANDARD WATER METER |
| C-0.1 General Notes | p63 | Utility and drainage notes: pipe materials, minimum 2 ft trench width, 3'-0" cover on water, 0.50% minimum storm grade, 10' / 18" separations |
| E-010 Electrical Site Plan | p42, p87 | Keynote 2 IRRIGATION BACKFLOW, counted on both pages (line 739) |

## Specification sections

The project manual has **no Division 33 (or 31) section**. `reference/sheets/spec_index.json`
lists 69 sections and the last one is 31 3116 Termite Control (p481). The utility "spec" is
therefore the civil notes on C-0.1 and the City of Warner Robins standard details on C-6.2 and
C-6.3. Two project-manual pages still matter:

| Section | Page | What it says |
|---|---|---|
| 01 2200 Unit Prices (responsibility matrix) | p14 | "It is the responsibility of the General Contractor to provide a complete scope of work for all incoming utilities." Civil/MEP discrepancies must be raised by RFI during the bid |
| 22 1000 Plumbing Piping 2.2A | p386 | "Underground domestic water service entrance piping 3" and smaller in size shall be Type K hard drawn copper tubing … brazed." This **conflicts** with C-5.0 keynote 8 "1" PVC DOMESTIC WATER LINE". The estimate follows the civil drawing |
| 22 1000 2.1A | p385 | Underground sanitary piping (building side) PVC DWV Schedule 40. Applies inside the 5 ft line, not to the site sewer |

## Material types and specified properties

| Material | Where specified | Properties |
|---|---|---|
| Storm pipe 15" and 18" | C-4.0 STORM PIPES table: MATERIAL HDPE. C-0.1 drainage notes, type 3 | HDPE ADS N-12 ST IB per AASHTO M294, smooth interior, annular exterior corrugations, bell-and-spigot soil-tight joint, gaskets ASTM F477, fittings ASTM F2306. Slope 0.50% (all rows) and 0.50% minimum per C-0.1. RCP CL III is required only in the public ROW (none here) |
| Roof-drain header 8" | C-4.0 keynote 5 | HDPE, minimum slope 1%. No inverts given |
| Sanitary 6" | C-5.0 SANITARY PIPES: MATERIAL PVC. C-0.1 utility notes | PVC per ASTM D3034 (or DIP AWWA C150), slope 1.00% (all rows). Bedding per C-6.2: crushed stone (D.O.T. std) or coarse sand, 4" minimum under the pipe and up to ½ O.D. over the pipe; trench width O.D. + 18" max; minimum pipe cover 3'-0" to 4'-0"; detectable mylar tape 18" below finished grade; 12 gauge copper tracer wire |
| Water 1" | C-5.0 keynote 8; C-0.1 | 1" PVC (C-0.1 allows C-900, Class 150 outside roads, 200 psi PVC D2241, or Type L copper). Minimum 3'-0" cover, minimum trench width 2 ft. The spec page p386 wants Type K copper (conflict) |
| Tapping saddle | C-5.0 keynote 5; C-6.3 TAPPING SLEEVE | 8" × 8" × 1" saddle and corporation stop on the existing 8" CI main (C-4.0/C-5.0 "8" CI") |
| Meter, RPZ | C-5.0 keynote 9; C-6.3 STANDARD WATER METER DETAIL | 1" domestic meter and RPZ backflow preventer per the utility provider. The meter box has a reader door (DFW D1200-DIRB) |
| Irrigation | C-5.0 keynote 10; E-010 keynote 2 | Reuse the existing 1" irrigation meter, or replace it with a new meter and RPZ if required |
| Gas, power, telephone | C-5.0 keynotes 1, 3, 4 | Service routes; "contractor to coordinate with utility provider for exact location and continuation". No size or depth |
| Hooded grate inlet (STGI) | C-4.0 Structure Types | GDOT STD 1019A TYPE E (C-6.1 GDOT inlet detail) |
| Yard inlet (STYI) | C-4.0 Structure Types | Nyloplast inlet with dome. C-6.2: 1899CGD 18" ductile-iron dome grate, ASTM A536 70-50-05 |
| Headwall (STHW) | C-4.0 Structure Types | GDOT STD 1001B headwall. The estimator describes it as a 6" concrete headwall |
| Outlet control structure (STOCS) | C-4.0 "SEE DETAILS SHEET C-6.2"; C-4.2 | No OCS detail on C-6.2. C-4.2 shows a concrete riser with overflow inlet, rim 436.5, and a 24" × 24" trash rack with anti-vortex. The estimate assumes 4'-0" dia precast |
| Junction box (STJB) | C-4.0 table | B1 is new; C1 is existing. No detail; 4'-0" dia precast is assumed |
| Cleanout | C-6.2 CLEANOUT TO GRADE | 4" minimum pipe, 45° bend and lateral Y branch, recessed brass cleanout plug, 18" × 18" × 8" concrete pad or 18" square concrete collar in all paved areas (pad in trade 32b, line 658 "18"X18"X8" THK") |
| Manhole connection | C-5.0 keynote 2; C-6.2 DROP TIE-IN | Core the existing manhole from inside at the invert shown (431.63) and grout watertight. The existing invert is not verified |

## What the estimator measured, and in which units

- **Pipe from the engineer's table, LF.** Storm 15"/18" and sanitary 6" are table LENGTH sums,
  exact to 2 dp. The p74 table LENGTH column is highlighted, and there is no PlanSwift
  polyline for storm pipe at all. The sanitary polyline (295.8) agrees within 0.05% but was not
  what the estimator used.
- **Pipe from PlanSwift polylines, LF.** Header, water, power and telephone carry the 2-dp
  PlanSwift value; the legend prints 1 dp. Gas is the exception: 152 against 156.4.
- **Headwall, LF.** Polyline 8.8 FT, rounded to 9 LF (whole feet; up or nearest cannot be told apart here).
- **Structures, EA.** Count dots were placed on the **structure table rows**, not on the plan
  symbols. Rows marked EXISTING (C1-STJB, S1-SSMH) are not counted as structures; S1 becomes the
  "connection at existing manhole" line.
- **Appurtenances, EA.** One dot per keynote symbol on C-5.0 (5, 9, 9, 2) and on E-010 (2,
  counted on both pages).
- **Trenching, CY.** Not measured. It is derived from the four drainage-pipe lines with one
  uniform 3' × 5' section. The estimator chose that section: C-6.2's `O.D. + 18" MAX` is a
  sanitary-PVC bedding maximum and by O.D. gives 3.25 ft for the 18" N-12 run, and the storm
  runs have no bedding detail (C-0.1 type 3: install per ASTM D2321); the services are not trenched in this trade. Backfill = excavation −
  haul; haul is a 42 CY allowance.

## Reconciliation summary

| Class | Lines | Count |
|---|---|---|
| specified (engineer's table) | 721, 722, 723 | 3 |
| measured (legend) | 724*, 725, 726, 727, 728, 738 | 6 |
| counted | 729–737, 739 | 10 |
| derived (section inferred) | 740 | 1 |
| derived from allowance | 741 | 1 |
| allowance/judgment | 742 | 1 |

\* 724: the legend is +2.89% over the estimate (within 5%, not within 1%).

- Exact (0.0%) and grounded in a drawing or legend value: 17 (721–723, 725–738).
- Exact only by construction: 3 (739 double count, 740 inferred section, 741 depends on 742).
- Within 5%: 1 (724). Exact or within 5%, all bases: 21.
- Not reproducible: 1 (742).

## Verification

A review of this folder (2026-10-13) raised 8 issues. Each was re-checked against the source
(rendered C-6.2, spec page text, C-5.0 tables recomputed in python, engine `OD_TABLES`), with
GPT-6 Astra (`tools/ask_gpt.py`) as a second-provider reader. All 8 were upheld and fixed.
`build.py` was patched and re-run, so `reconciliation.csv` and `fixtures.json` were regenerated
together; all 20 fixtures recompute to their expected quantity.

| # | Issue | Checked | Change |
|---|---|---|---|
| 1 | Cleanout pad 6" | C-6.2 CLEANOUT TO GRADE read at 2x by Claude and by GPT-6 Astra: `18"x18"x 8" CONCRETE PAD OR 18" SQUARE CONCRETE COLLAR IN ALL PAVED AREAS`; estimate line 658 description `18"X18"X8" THK` | 6" → 8" plus the paved-area collar in the README material table, reading-guide §1(4) and the 729 note |
| 2 | Sanitary depth 6.3–6.9 ft | python, §6 basis: runs 5.75–6.92 ft (weighted 6.464); rim-to-invert 5.40 (S6) to 6.71 (S2) at the cleanouts; storm 2.36–4.33 ft | reading-guide §3 now says 5.8–6.9 ft (5.4–6.7 ft at the cleanouts) |
| 3 | Spec cite 22 1000 1.3 | `spec-p385.txt`: PART 2, 2.1 A is the PVC DWV Sch 40 underground sanitary paragraph | README cites 22 1000 2.1A (p385) |
| 4 | Headwall "ceil" | python: ceil(8.8) = round(8.8) = 9; ceil(821.67) = round(821.67) = 822. GPT-6 Astra agreed one sample cannot separate them (8.2 would) | Rule worded as "rounded to whole feet, direction unverified" in formulas §3, csv 738, reading guide, README, app-gaps; fixture input renamed `roundUpTo` → `roundTo` |
| 5 | "20 exact" overcounts | 739 replicates a double count; 740 fixes only W × D = 15 SF (3×5, 2.5×6, 2×7.5 all give 456.666667 CY); 741 = 740 − the 42 CY allowance. GPT-6 Astra: the section is not uniquely determined | Count is now 17 grounded + 3 by construction; csv classes 740 `derived (section inferred)`, 741 `derived from allowance`; notes on 739–741 say "reproduced by construction" |
| 6 | 3.0 ft width "from the detail" | C-6.2 rendered: title `SECTION - SANITARY SEWER BEDDING PVC PIPE`, `O.D. + 18" MAX`; engine `OD_TABLES.hdpe` 18" = 21" → 39" = 3.25 ft; C-0.1 type 3 says only "install per ASTM D2321". GPT-6 Astra: 3.0 ft is an estimator convention (it quoted 21.5" O.D., i.e. 3.29 ft, and noted 3.0 ft exceeds the detail maximum for 6" PVC, about 2.0 ft) | formulas §6, reading-guide §2, README and the csv 740 source/notes now call 3' × 5' the estimator's section, not detail-backed |
| 7 | Fixture input 295.9599999999999 | `sum()` float artifact in build.py | 740 fixture runs passed through `round(…, 2)`; now 295.96 |
| 8 | Gas gap 2.89% vs −2.81% | python: 4.4/152 = 2.895%; 4.4/156.4 = 2.813% | README and formulas quote +2.89% on the csv basis, (recomputed − estimate)/estimate, and label 2.81% as "of the legend" |

Models: Claude Opus 5.5 (re-checks, python recomputation, edits) and GPT-6 Astra (second reading of
the C-6.2 cleanout callout; second opinion on the N-12 O.D., the trench width basis, the rounding
direction and section uniqueness). No issue was rejected. No estimate quantity changed; only the
explanations, classifications and one fixture input value did.
