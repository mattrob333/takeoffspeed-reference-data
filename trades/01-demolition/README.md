# 01 — Demolition (site demolition, Division 02)

Job: Fifth Third Bank, 2711 Watson Blvd., Warner Robins GA. This is a new single-storey bank branch on a
0.962-acre (41,909 SF) parcel. Before building, the contractor removes everything already on the parcel:
a two-storey building, a one-storey building, the asphalt parking lot with its curbs, walks, ramps and
steps, a monument sign, two trees, and the site utilities. The civil engineer is Gaskins + LeCraw (job 75670007).

## Scope (14 estimate lines, 2–15)

| Line | Item (keynote) | Unit | Estimator qty | Class |
|---|---|---|---:|---|
| 2 | KN1 remove existing curb & gutter | LF | 987.22 | measured |
| 3 | KN2 remove existing TWO STORY building structure & foundation | CFT | 89,780 | derived (SF × 2 × 10 ft) |
| 4 | KN2 remove existing ONE STORY building structure & foundation | CFT | 17,140 | derived (SF × 1 × 10 ft) |
| 5 | KN9 remove existing sidewalk | SF | 390.17 | measured |
| 6 | KN10 remove existing monument sign | EA | 1 | counted |
| 7 | KN11 remove existing concrete ramp | SF | 442.37 | measured |
| 8 | KN11 remove existing brick stair steps | EA | 7 | counted (one per step) |
| 9 | KN7 remove existing pavement w/ pavement striping | SF | 19,363.57 | measured |
| 10 | KN8 remove existing trees/vegetation | EA | 2 | counted |
| 11 | KN6 remove existing water line & associated structures | LF | 55.6 | measured |
| 12 | KN5 remove existing power line & associated structures | LF | 965.36 | measured |
| 13 | Remove existing metal handrail (no keynote) | LF | 76.2 | measured |
| 14 | KN4 remove existing storm sewer line & structures – ASSUMED | LF | 107.11 | measured |
| 15 | KN4 remove existing storm structure | EA | 2 | counted |

**Result: 14 of 14 lines reconcile within 1%, and all 14 within 5%.** Ten lines come straight from the
PlanSwift legend on markup page 64 (C-1.0). The legend prints one decimal and the estimate carries two, so
the largest deviation is −0.009% (line 14). The two building lines are the only derived quantities:
CFT = legend footprint SF × stories × 10 ft, rounded to the nearest 10 CF. That rebuild is exact (0.000%).
The 10 ft per storey is the estimator's own convention. No building height appears anywhere in the
documents.

Each measured line was also checked against the CAD vector layer of C-1.0, independently of PlanSwift
(see `reconciliation.csv` notes). **Against CAD, 8 of the 9 single-value checks fall within 3% (4 of them
within 1%), the handrail sits inside its CAD bracket, and the ramp is the one outlier at +6.0%.** These
are cross-checks of the trace, not the reconciliation itself, which is against the legend above.

| Line | CAD check | CAD value | Estimator vs CAD |
|---|---|---:|---:|
| 2 curb | length along the 10 site curb-linetype polylines (≈ 484 crossing ticks × 2.0 ft = 967 LF) | 975.2 LF | +1.2% |
| 3 2-storey footprint | hatched outline polygon | 4,463.1 SF | +0.58% (on SF) |
| 4 1-storey footprint | hatched outline polygon (≈ 52.1' × 32.9' effective; bounding box 52.4' × 32.9') | 1,716.4 SF | −0.16% (on SF) |
| 5 sidewalk | L-walk closed on the building line 331.3 SF + south apron 49.0 SF | 380.3 SF | +2.6% |
| 7 ramp | sidewalk/ramp outline closed along the 2-storey building (406.4 SF) + west pad (10.8 SF) | 417.2 SF | +6.0% |
| 8 steps | drawn step lines from the top landing to the walk (unequal spaces, 7.7"–18.7") | 7 lines | 0 |
| 9 pavement | 4,556 hatch dots × 4.3397 SF (7.5 pt staggered grid) | 19,771.7 SF | −2.1% |
| 11 water | the ticked W line, x = 696 → 897 pt | 55.83 LF | −0.4% |
| 12 power | length along the 7 dry-utility (OHP/UGP/TEL) polylines (194 `///` ticks × 5.0 ft = 970 LF) | 983.4 LF | −1.8% (−0.48% on ticks) |
| 13 handrail | the "METAL HANDRAIL" lines, with and without the stair sides | 68.5–79.6 LF | inside the bracket |
| 14 storm | JB centre to HW centre | 106.57 LF | +0.51% |

All CAD lengths use the sheet scale 1" = 20' (72 pt = 20 ft). This was verified on the graphic scale bar,
where 0' to 40' spans 144 pt.

## Driving sheets

| Sheet | Markup page | Use |
|---|---|---|
| **C-1.0 Demolition Plan** | **p64** | Every quantity. The PlanSwift legend (14 rows) sits lower-left over the plan. The engineer's LEGEND (5 symbols: structures ⊠ crosshatch, pavement dot hatch, utilities `///`, curb/gutter `++++`, tree `X`), KEY NOTES 1–11 and GENERAL DEMOLITION NOTES 1–7 are on the right. The survey labels (TWO STORY BUILDING F.F.E.= 442.2', ONE STORY BUILDING F.F.E.=440.3', BRICK STEPS, METAL HANDRAIL, JB, HW 15" HDPE) are base linework. |
| C-0.1 General Notes | p63 (no legend) | DEMOLITION NOTES block. Demolish "EXISTING BUILDINGS, INCLUDING FOUNDATIONS AND ALL APPURTENANCES … BOLLARDS, GAS METERS, AIR CONDITIONING UNITS, SIGNS, CURBS, SIDEWALKS, ELECTRIC METERS, FENCING". "SAWCUT AT INTERFACE OF PAVEMENT OR CURB TO REMAIN. SAWCUT EXISTING PAVEMENT AT THE R/W." Asbestos/hazmat by a licensed contractor. Cut and plug services at the main. |
| C-0.0 Cover | p62 (no legend) | TOTAL DISTURBED AREA = 0.9 ACRES. A context check only. |
| C-3.0 / C-4.0 / C-5.0 | p72–p77 | New work. They confirm that everything inside the curb line is rebuilt, so the whole lot is removed. |

## Specification sections (source/specifications.pdf)

| Section | Pages | What matters for demolition |
|---|---|---|
| Table of contents | p3 | Lists **02 4116 Structure Demolition** and **02 4119 Selective Demolition**. Neither section is bound in the issued manual (they are absent from `spec_index.json` and from pages 1–484). The drawings carry the scope alone. |
| 01 1000 Summary | p10–11 | New single-storey bank of about 1,900 SF with a drive-through. Existing utility interruptions need 2 days' notice. |
| 01 3001 Responsibility chart (bound inside the 01 2200 page range of the index) | p14 | GC provides "a complete scope of work for all incoming utilities". Site preparation is by the contractor. |
| **01 7419 Construction Waste Management and Disposal** | **p26–37** | Divert **75% by weight** of non-hazardous waste (p27). Demolition waste listed: asphalt paving, concrete, rebar, brick, CMU, wood, structural steel. Recycling (p34): asphalt goes to a recycler; concrete is pulverized to 1-1/2" / 4" maximum for fill or subbase; masonry is pulverized to 1" or kept as whole units on pallets. Forms CWM-2, CWM-4 and CWM-8 cover demolition waste. This drives disposal method, not quantity. |
| 31 1000 Site Clearing | — | Referenced by 01 7419 but not bound. |

## Material types and specified properties

The documents specify no removal material properties: no thicknesses, depths, construction type,
pipe sizes (except one) or tree sizes. What is known:

- **Buildings:** a two-storey and a one-storey building, each slab-at-grade by F.F.E. No height, no
  construction type and no basement are noted. "UPPER METAL DECK WITH CONCRETE PATIO BELOW" sits on the
  south side of the two-storey building.
- **Pavement:** asphalt parking lot ("ASPHALT PARKING LOT"), with its striping. Thickness is unknown.
- **Curb:** 24" C&G and 24" roll curb, both carried as one LF line.
- **Walks and ramp:** concrete sidewalk and a concrete sidewalk/ramp. Thickness is unknown.
- **Steps:** brick.
- **Utilities:** water (W); power, overhead and underground (OHP/UGP); telephone (TEL), carried inside the
  "power" line; storm 15" HDPE (from the HW label: TOP 438.00', I.E. IN 434.96'), JB TOP 438.35'.
  General note 7 says the depth of every dry and pressurized utility is unknown.
- **Trees:** two, unsized.

## What the estimator measured and in which units

PlanSwift on C-1.0 only, with three kinds of takeoff:

- **Area (SQ FT):** both building footprints, sidewalk, concrete ramp, pavement.
- **Linear (FT):** curb & gutter, water, power, handrail, storm.
- **Count (EA):** monument sign, brick stair steps (7 stacked dots), trees, storm structures.

The legend item names copy the engineer's keynote text with the keynote number as a prefix. The two
building lines in the estimate change the unit from SQ FT to CFT (× storey height). Every other line is
the legend quantity unchanged. Nothing else is derived: no debris CY, no saw cut and no disposal tonnage.
The estimator's dumpster is a lump-sum General Conditions line (line 1, `DIV 01`), outside this trade.

## Scope the plans show that the estimate does not carry

These are takeoff observations only. Whether to carry them is the estimator's call.

- **Gas line:** a ticked `///` GAS line 87.1 LF long (17 ticks; 16 full 5 ft pieces plus two 3.5 ft
  ends) runs from the west curb to the A/C pad of the one-storey building. It has no keynote and no estimate line.
- **Sanitary sewer:** keynote 3 exists in KEY NOTES but has no tag on the plan. The 8" sewer is in
  Westgate Dr. ("SCALED ONLY"). No line, which is correct.
- **Saw cut:** general demolition note 3 and C-0.1 require a full-depth saw cut at the demolition limits
  and the R/W. No LF line.
- **Appurtenances** named in the C-0.1 note (A/C units, gas meter, electric meters, fencing, crosstie
  border, brick planters about 8" high): these are presumably inside the building or pavement lines.
  None is listed on its own.

## Verification

A reviewer raised 11 issues on this folder. Each was re-checked by Claude (Opus 5.5) against the C-1.0
vector layer (PyMuPDF, every figure computed in Python), the markup page 64 renders, the spec text and the
TakeoffSpeed engine source. GPT-6 Astra (OpenAI) gave independent readings of rendered crops. Scratch
scripts are in `trades/01-demolition/scripts/verify/`.

| # | Issue | Verdict | What changed |
|---|---|---|---|
| 1 | Power CAD check (222/194 ticks, 970 LF) | **Reviewer partly wrong.** The 222 ticks exist: they are `///` text glyphs in the text layer (223 with the legend), one every 18 pt, clustered 141 + 53 dry, 17 gas, 11 water. The reviewer counted 18 pt pieces with a tolerance too tight (they print as 17.9–18.1 pt) and chained by shared endpoints, which merges the utility and curb linetypes. Chaining in drawing order gives 7 dry polylines = 983.4 LF, so the estimator is −1.8% (not +3.5%). GPT-6 Astra matched the three north traces to the three CAD runs. | Kept the tick count and said what the ticks are. Added the chain-length measure (983.4 LF, −1.8%) as the main check in the CSV, formulas, README, reading guide and app-gaps. |
| 2 | Stair and storm-structure fixtures cannot run | **Right.** `description`/`areas` and `utility`/`runs` are required, and the assembly strings were not registry ids. | Folded line 8 into the ramp fixture and line 15 into the storm fixture. Added `engineInputs` (engine strings) and `expectedLines` (engine keys). All 14 expected lines pass when the 12 fixtures are run through `expandMeasurements`. |
| 3 | Ramp CAD polygon 467.8 SF | **Right that 467.8 is wrong; the bracket proposed is not the fix.** 467.8 came from appending the closing vertices in reverse, which makes a self-intersecting polygon. Closed in path order along the building outline, the polygon is 406.4 SF, + 10.8 SF pad = 417.2 SF. The reviewer's upper value (454.3, to the x = 1342 line) takes in ground east of the rail that the markup does not trace (GPT-6 Astra agrees). | The estimator is now +6.0% over CAD (it had been reported as −5.4%). The "trace stops at the stair and the rail" wording is removed. |
| 4 | 52.4' × 32.9' ≠ 1,716.4 SF | **Right.** The outline is a skewed 5-vertex polygon: shoelace 1,716.4 SF, bounding box 1,724.7 SF. | Quoted the polygon area with its effective and bounding dimensions. |
| 5 | Sidewalk 380.8 / 67.3 SF apron | **Right.** 380.3 = 331.3 L-walk + 49.0 apron. The 67.3 SF piece is dotted pavement south of the gas line. | Rewrote the note. The estimator is +2.6%. |
| 6 | Uniform 9.5" tread | **Right.** The step-line spaces are 7.7"–18.7". GPT-6 Astra counts 7 lines. | Rule is now "count the drawn step lines = 7". |
| 7 | Gas "17 ticks" back-derived | **Reviewer wrong on the count.** There are 17 glyphs: the text layer has 17, a visual count finds 17, and GPT-6 Astra also counts 17. The reviewer's 13 segments and 84.5 LF are wrong. | Gas length is now the measured 87.1 LF (16 full 5 ft pieces plus two 3.5 ft ends). |
| 8 | Curb 982 tick halves | **Right that 982 cannot be reproduced.** The linetype is 7.2 pt pieces with a full crossing tick at each joint (≈ 484 ticks × 2.0 ft = 967 LF). Measured along the 10 site curb polylines it is 975.2 LF. | The estimator is +1.2% (it had been reported as +0.53%). The check is now described as crossing ticks × 2.0 ft plus the chain length. |
| 9 | 01 7419 pages 26-29 | **Right.** The section runs p26–37 (01 9113 starts p38). | Fixed. |
| 10 | Pricing vocabulary | **Right.** | Reworded to measurement terms in best-practices.md, plus one README sentence. Dropped the unit-price lookup. |
| 11 | Building label gap missing | **Right.** The engine emits `… 2 STORY … — 4,489.1 SF FOOTPRINT × 20' H`. | Added label-gap rows for the building and the storm label (the engine adds `15" HDPE`). |

Reconciliation count after verification: against the legend, still **14 of 14 within 1%**. Against CAD, 8
of the 9 single-value checks fall within 3%, the handrail sits inside its bracket, and the ramp is +6.0%.
No estimate quantity or classification changed.
