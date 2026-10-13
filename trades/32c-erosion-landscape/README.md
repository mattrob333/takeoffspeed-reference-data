# 32c — Erosion and sediment control, pond, landscaping

The three-phase ESPC (erosion, sedimentation and pollution control) plan, the stormwater
infiltration basin, and the landscape plan. This covers **27 estimate lines** in Div 32: lineNo
684–706 and 708–711, as listed for `32c-erosion-landscape` in `reference/estimate/trades.json`.
It covers quantities and material descriptions only.

**Result:** 26 of the 27 lines rebuild from a printed source to within 1%, and 26 are within 5%.
Line 693 (RT-P half-round pipe retrofit) is the exception. The legend prints 7.5 FT and the
estimate carries 7.0 LF (+7.1% against the legend), and the 7.0 is unexplained (see *Open items*). Of the 26, 25 match exactly. Line 688 (RT-B) carries the raw PlanSwift
5.14 against the printed 5.1 (−0.78%). Every line reconciles to a source, but three of them
reproduce a quantity that the drawings do not support: 699, 709 and 711. See *What the estimator
got wrong*.

| File | Contents |
|---|---|
| `formulas.md` | Every formula, with inputs, the estimator's conventions and a worked example |
| `reconciliation.csv` | Line → source → formula → recomputed quantity → delta → classification |
| `fixtures.json` | 26 engine test cases, one for each reproducible line (693 is left out). The three for 699, 709 and 711 carry `"estimatorParity": true` and a `perDrawings` block (74.5 LF, 2081.1 SF, 196.04 CY); exclude them from drawing-truth assertions |
| `reading-guide.md` | Which sheets and legends to read, the exact strings, cross-checks and traps |
| `app-gaps.md` | How the TakeoffSpeed engine compares (it was run on these inputs), ranked changes |

## Scope by group (estimate section path)

| Group | Lines | What |
|---|---|---|
| PHASE 1 (C-2.0) | 684–691 | Construction exit (CO), concrete washout, fuel storage, compost filter sock (SD1-NS), slotted board dam retrofit (RT-B), DS1 / DS2 / DU on the first disturbed-area polygon |
| PHASE 2 (C-2.1) | 692–698 | Inlet sediment trap SD2-F, perforated half-round pipe retrofit RT-P, DS1 / DS2 / DU on the second polygon, DS3 + SS on the pond slopes |
| PHASE 3 (C-2.2) | 699–700 | Inlet sediment trap (carried as SD2-F), DS4 final sodding |
| LANDSCAPE (L-1.0) | 701–706 | 2 tree species, 2 shrub species, pine straw, sod. All from the PLANT LIST |
| POND AREA (C-3.0 / C-4.2) | 708–711 | Pond area (reference line), non-woven geotextile, 6" perforated HDPE underdrain, open-graded stone storage |

Line 707 (monument sign) sits between these lines in the estimate but belongs to 32b. The pond
excavation is in the grading quantity (31-earthwork). The estimate note on line 708 says so:
"POND EARTHWORK HAS BEEN ADDEDTO THE GRADING QUANTITY". The irrigation backflow (739) is in
utilities.

## Driving sheets

| Sheet | Markup page | Used for |
|---|---|---|
| C-2.0 ESPC – Phase 1 | p65 (legend, 7 rows) | CO 1569.4 SF, CONCRETE WASHOUT 25.1 SF, FUEL STORAGE 25.1 SF, SD1-NS 767.9 FT, RT-B 5.1 FT, "DS1, DS2 & DU" teal 20298.9 SF and red 15581.9 SF. General note: TOTAL DISTURBED AREA = 0.9 ACRES; LIMITS OF DISTURBANCE: 0.9 AC |
| C-2.1 ESPC – Phase 2 | p66 (legend, 4 rows) | SD2-F 193.7 FT, RT-P 7.5 FT, "SS, DS3: AREA" 2114 SF, "ST-1:" 962.4 SF (this traces the stone bed; no line uses it). PHASE 2 – SEDIMENT STORAGE TABLE (Rt-P: Half Round CMP Diameter 2.25 FT, Height 2.00 FT) |
| C-2.2 ESPC – Phase 3 | p67 (legend, 2 rows) | Sd2-P "TEMPORARY INLET SEDIMENT  TRAP (CURB INLET PROTEC..." 74.5 FT (no line uses it), DS4 14393.7 SF |
| C-2.3 / C-2.4 ESPC Notes | p68 / p69 (no legend) | Schedule of activities (Sd2-F in Phase 2, Sd2-P allowed once structure tops are in place), seeding table, mulch and lime rates, secondary containment liner for fuel tanks |
| C-2.5 ESPC Details 1 | p70 (title highlights only) | Compost filter sock (Sd1-NS) "AT LEAST 18" DIA", stakes "2' O.C. FOR TYPE NS"; crushed stone construction exit; concrete washdown "PROVIDE 7'x7' CONCRETE WASHOUT AREA"; Ds1, Du, Ss, Sd2-P details |
| C-2.6 ESPC Details 2 | p71 (no legend) | Sd2-F fabric and supporting frame; Rt-P perforated half-round pipe with stone filter; Ds2, Ds3, Ds4 tables |
| C-3.0 Site Plan | p72 | "23: PROPOSED STORMWATER PO..." 3074 SF (magenta, the pond to its top of bank) |
| C-4.0 Grading Plan | p74 (storm legend) | Pond contours 435–438. Keynote 7 marks the stone bed, which scales to 95.6 ft × 10.27 ft from the CAD vectors |
| C-4.2 Infiltration Basin Detail | p76 (no markup) | BOTTOM OF INFILTRATION BASIN: 435.00, BOTTOM OF GRAVEL: 429.5, 6 OZ/SY NON-WOVEN GEOTEXTILE FABRIC, 6" PERFORATED HDPE UNDERDRAIN, "INFILTRATION TRENCH SHALL HAVE A MINIMUM SURFACE AREA OF 950 SF" |
| L-1.0 Landscape Plan | p83 (purple highlights on the PLANT LIST), p85 | Plant list quantities, sizes and spacing; plan callouts (n) NAME; hatch legend SOD / GRASS, MULCH |
| L-1.1 Landscape Details | p84 / p86 (no markup) | General landscape note 6: 3" of mulch on all beds; planting, sod placement and bed details |

**Specifications:** the project manual (`source/specifications.pdf`, 69 sections) has **no
Division 31/32 section for erosion control, turf or planting**. The only site section is 313116
TERMITE CONTROL (spec p481), which is not this trade. The responsibility chart bound at spec pp. 14–17
lists "Landscaping" as designed by CE (the civil engineer) and furnished and installed by the
contractor, and "Landscaping Irrigation System" as LS (landscape supplier). The material
properties therefore come from the drawings. The GSWCC *Manual for Erosion and Sediment Control
in Georgia* is cited in C-2.0 general note 1.

## Material types and specified properties

| Item | Code | Specified properties (source) |
|---|---|---|
| Construction exit | Co | N.S.A. R-2 (1.5"–3.5") coarse aggregate, 6" MIN, 20' MIN × 50' MIN, geotextile underliner, tire washrack / washers, culvert under entrance if needed (C-2.5) |
| Concrete washout | — | Approximately 7'×7', approximately 30" storage depth, 12" MIN freeboard, MAX. SLOPE 2:1, lined with plastic sheeting (10 MIL, MIN). An approved prefabricated container may be substituted (C-2.5) |
| Fuel storage | — | No detail. C-2.3: "TEMPORARY FUELING TANKS SHALL HAVE A SECONDARY CONTAINMENT LINER" |
| Sediment barrier, non-sensitive | Sd1-NS | Compost filter sock, "AT LEAST 18" DIA", wooden stakes "2' O.C. FOR TYPE NS", 30" MIN above grade, 18" MIN embed (C-2.5). The estimate says 30" DIA (see traps) |
| Slotted board dam retrofit | Rt-B | At the sediment storage outlet (C-2.0 legend) |
| Perforated half-round pipe retrofit | Rt-P | One-half round CMP attached to the weir box, 1" holes 8"–10" apart, fill around it with 3"–4" stone, 1' MIN graded stone (C-2.6). The C-2.1 table gives diameter 2.25 FT and height 2.00 FT |
| Inlet sediment trap | Sd2-F | Fabric and supporting frame, steel frame and Type C silt fence (C-2.6) |
| Inlet sediment trap | Sd2-P | Curb inlet filter, "pigs in blanket" (C-2.5). Phase 3 only |
| Disturbed area stabilization | Ds1 / Ds2 / Du | Ds1: mulch only (dry straw 2 TONS/AC, hay 2½ TONS/AC). Ds2: temporary seeding (C-2.4 table, e.g. annual ryegrass 40 LBS/AC). Du: dust control. Lime 1–2 TONS/AC (C-2.5 / C-2.4) |
| Permanent vegetation, slope stabilization | Ds3 / Ss | Permanent seeding (C-2.6 table). Rolled erosion control products on the slopes (C-2.5 Ss). Slopes steeper than 3:1 get DOT matting and hydroseeding (C-2.4) |
| Sodding | Ds4 | C-2.6 sod tables. Final stabilization on all pervious areas (C-2.2) |
| Pond geotextile | — | 6 OZ/SY non-woven geotextile fabric at the bottom and sides of the stone bed (C-4.2) |
| Underdrain | — | 6" perforated HDPE, upturned (C-4.2) |
| Storage stone | — | "UNDERGROUND STONE STORAGE CLEAN OPEN GRADED COURSE AGGREGATE", 429.5 to 435.00 = 5.5' deep (66" on the trench section), not compacted (C-4.2) |
| Trees | — | American Holly *Ilex opaca* 'Greenleaf' 6' HT, 12' O.C., B&B. Eastern Redcedar *Juniperus virginiana* 6' HT, 40' O.C., B&B (L-1.0) |
| Shrubs | — | Florida Sunshine Anise *Illicium parviflorum* 'Florida Sunshine' 3 GAL, 5' O.C. Don's Dwarf Wax Myrtle *Myrica cerifera* 'Don's Dwarf' 3 GAL, 5' O.C. (L-1.0) |
| Mulch | Mulch A | Pinestraw. "ALL PLANTS & PLANT BEDS MUST BE COMPLETELY MULCHED WITH 3" OF CLEAN, ORGANIC MULCH" (L-1.1 note 6) |
| Sod | — | The plant list gives no species. Sod is rolled with no gaps over 1/4" (L-1.1 sod placement detail) |

## What the estimator measured, and in which units

- **Areas (SF):** the construction exit, the two disturbed-area polygons (traced on the Phase 1
  sheet and split between Phase 1 and Phase 2), the pond-slope ring (DS3/SS), the Phase 3 sodding,
  the pond (on the site plan) and the stone bed ("ST-1", which no line uses).
- **Runs (LF):** the sock along the LOD, the RT-B and RT-P retrofits, the Sd2-F frames around 4
  inlets (Phase 2) and the Sd2-P curb inlet protection (Phase 3, which no line uses).
- **Counts (EA):** the washout (1, from the detail) and the plants (from the plant list, not
  counted on the plan).
- **Specified quantities taken verbatim:** the PLANT LIST rows, including Pinestraw 2,500 S.F.
  and Sod 11,500 S.F.
- **Derived:** each stacked practice repeats its zone's SF (DS1 = DS2 = DU; DS3 = SS). The pond
  geotextile equals the pond SF. Stone CY = pond SF × 5.5' / 27. The Phase 3 inlet trap repeats
  Phase 2.

The estimator rounds by hand to whole units on some lines (CO up to 1570, SD1-NS up to 768,
SD2-F up to 194, fuel storage to 25) and carries raw PlanSwift decimals on others (20298.88,
15581.92, 14393.68, 5.14).

Classification count: measured 11 (684, 686–689, 692–694, 697, 700, 708), derived 9 (690, 691,
695, 696, 698, 699, 709, 710, 711; 710 is "derived (inferred)", the analyst's scaling of the design
bed with no estimator measurement behind it), counted 1 (685), specified 6 (701–706).

## What the estimator got wrong (quantities the drawings do not support)

| Line | Carried | Per the drawings | Δ | Why |
|---|---|---|---|---|
| 711 storage stone | 626.19 CY | 196.04 CY (962.4 SF stone bed × 5.5' / 27) | −68.7% | The depth was applied to the whole pond footprint at top of bank. Stone fills only the 435 bottom bed, and C-4.2 asks for a 950 SF minimum |
| 709 geotextile | 3074 SF | ≈2081 SF (948 SF bed bottom + 206' perimeter × 5.5' sides), before laps | −32% | The fabric wraps the stone bed, not the pond surface. The C-4.2 trench section shows fabric on the bottom and sides only. A full wrap including the top would come to 3058 SF, close to 3074, but that is a coincidence |
| 699 Phase 3 inlet trap | 194 LF of SD2-F | 74.5 LF of Sd2-P (C-2.2 legend) | −61.6% | The Phase 2 line was copied. The Phase 3 row the estimator measured feeds no line |
| 706 + 700 sod | 11,500 SF + 14,393.68 SF | the same lawns | overlap | The landscape plan sod and the ESPC DS4 sodding both cover the final pervious areas. The site pervious area is 20,876 SF |
| 701 / 702 trees | 5 holly, 11 redcedar | plan shows 11 holly, 6 redcedar | species swap, 16 vs 17 trees | The plant list and the plan callouts disagree. The schedule was carried without an RFI |

## Open items

1. **Line 693, RT-P 7.0 LF.** The legend prints 7.5, and the 7.0 is unexplained. The printed
   value only bounds the raw PlanSwift length to 7.45–7.55. The raster cannot narrow that: a circle
   fit to the p66 arc gives a semicircle of radius about 2.2–2.3 ft with a centreline of about
   7.3 ft (6.6–7.9 ft across the stroke; a second fit gave 7.66 ft). π × 2.25 FT (the table
   diameter) = 7.07 is the CMP's full circumference, which this item never measures. No fixture
   was written. The recommended quantity is the physical one: **1 EA**, one 2.25' dia half-round
   CMP, 2.00' high, fixed to the weir, i.e. **2.00 LF** of CMP. GPT-6 Astra agrees: pipe LF runs
   along the pipe axis, and neither 7.0 nor 7.5 is that length.
2. **The LOD split.** The two "DS1, DS2 & DU" polygons add up to 35,880.8 SF (0.824 AC), 91.5% of
   the printed limits of disturbance, 0.9 AC (39,204 SF). Red (15,581.92 SF) is two lobes,
   north-centre and south-east, each over an existing building outline on the Phase 1 base; teal
   (20,298.88 SF) is the rest of the LOD around and between them. They do not overlap. The
   estimator gave the teal polygon to Phase 1 and the red one to Phase 2. Each ESPC phase sheet has a printed disturbed area (0.9 AC
   for Phase 1, 1.0 AC for Phase 2 and Phase 3), so this allocation is the estimator's own choice.
3. **Line 710, underdrain 96 LF.** No legend row exists, so the line is classified "derived
   (inferred)". The value equals the analyst's scaled stone-bed length (95.6 ft, rounded up) and
   also ST-1 962.4 SF ÷ 10 ft. Either reading gives 96; which one the estimator used is inferred.

## Verification

A review of this folder (2026-10-13) raised eight issues. Each was rechecked against the sources,
with all arithmetic in python (scripts and outputs in `trades/32c-erosion-landscape/scripts/verify/`),
by Claude Opus 5.5, with GPT-6 Astra (`tools/ask_gpt.py`) as a second opinion on the two visual
questions.

| # | Checked | Result | Change |
|---|---|---|---|
| 1 | `reference/markups/legends.json` p65 and `legends.csv` lines 586–587 | Both `DS1, DS2 & DU` rows are present (coral-red 15581.9, teal 20298.9) | reading-guide §2: the "known gap" paragraph replaced with the adapter warning only |
| 2 | 35,880.8 / 39,204 | 91.52%, 8.5% under (not 82%) | best-practices §3.4 and §7 corrected |
| 3 | `lib/quantities/trades/site/site-utilities.ts` `site-utilities.basin` | The basin assembly exists and `app-gaps.md` ran it | best-practices §8: the gap sentence rewritten to the real gaps (no `stoneBedAreas`, no `runs` on inlet protection, laps in net, no blanket slope factor) |
| 4 | Circle fit to the p66 Rt-P arc at 16x (`arcfit2.py`; scale checked against the 95.6 ft bed, 0.909 ft/pt) | Semicircle, radius 2.32 ft by this fit (2.22 ft by the reviewer's), centreline 7.28 ft (6.6–7.9 across the stroke); the reviewer's fit gave 7.66 ft. GPT-6 Astra: the raster cannot separate 7.45–7.49 from 7.50–7.55, and the reviewer's "7.5–7.7, so below 7.5 is unlikely" is not supported either | Reviewer partly right. The 7.45–7.49 and π × 2.25 explanations are no longer offered as fits; 693 now says 7.0 is unexplained and recommends 1 EA / 2.00 LF CMP (reconciliation.csv, formulas F4, Open item 1). The reviewer's 7.5–7.7 ft claim was not adopted |
| 5 | Fixtures 699, 709, 711; C-4.2 "PROVIDED WQv = 2,225 CF" | 962.4 × 5.5 × 0.40 = 2,117 CF (−4.8%); 3074-SF footprint gives 6,763 CF | `estimatorParity: true` and `perDrawings` (74.5 LF, 2081.1 SF, 196.044444 CY) added; all other fixtures `estimatorParity: false`; WQv check added to F10 |
| 6 | p65 render (and GPT-6 Astra on the same crops) | Red is two lobes, north-centre and south-east, over existing building outlines; teal surrounds them, including the north-east corner and the striped parking; no overlap. The reviewer's "building pad and parking lot" label was not adopted: the Phase 1 base shows existing buildings, and the south-east lobe is a building, not a lot | reconciliation 689, reading-guide §3, Open item 2 |
| 7 | p66 render and C-2.1 text layer (4 plan `Sd2-F` tags + 1 in the sheet legend) | 4 inlets; 193.7 / 4 = 48.4 LF | best-practices §3.2 job check rewritten |
| 8 | Line 710 provenance | No estimator measurement; two derivations give 96 | Classified "derived (inferred)"; count now measured 11, derived 9 |
