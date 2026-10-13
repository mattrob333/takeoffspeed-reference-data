# 31 — Earthwork: excavation, backfill, haul-off, grading (cut/fill)

This folder covers **6 estimate lines**, listed under `31-earthwork` in `reference/estimate/trades.json`:

| lineNo | Section | Description | Unit | Estimator qty | Drawing ref |
|---|---|---|---|---:|---|
| 629 | EXCAVATION | EXCAVATION PROVIDED FOR FOOTING | CY | 119.8 | S201 |
| 630 | BACKFILL | BACKFILL PROVIDED FOR FOOTING | CY | 83.7 | S201 |
| 631 | HAULOFF/IMPORT | HAULING OFF EXTRA MATERIAL | CY | 36.1 | S201 |
| 639 | GRADING | CUT REQUIRED FOR GRADING | CY | 634.41 | C-4.0 |
| 640 | GRADING | FILL REQUIRED FOR GRADING | CY | 786.25 | C-4.0 (carried) |
| 641 | GRADING | NET FILL | CY | 151.84 | C-4.0 (carried) |

It covers quantities and material descriptions only.

**Result:** all 6 lines rebuild from a source, and all 6 land within 0.07% of the estimator's
quantity.

- The grading lines (639–641) match exactly. They are the totals of the PlanSwift
  *Earthwork Pro Summary* (markup page 92).
- The building footing lines (629–631) rebuild from the S-201 schedules, the p33 legend and one
  depth note. The excavation formula is the estimator's own convention, inferred from this job:
  1'-0" working space each side of the wall-footing trench and 6" each side of the spread pads.
  It reproduces 119.7556 CY against the printed 119.8. GPT-6 Astra derived the same split
  independently.

Site-item earthwork is out of scope here. Sign, bollard, light-pole and bike-rack piers, and the
dumpster wall footing, are in `32b-site-structures` (lines 652–656, 661–662, 665–667, 676–677,
715–716, 719–720). Pipe trenching is in `33-site-utilities` (lines 740–742).

| File | Contents |
|---|---|
| `formulas.md` | Every formula: inputs, the rule, the estimator's conventions with their basis, and a worked example |
| `reconciliation.csv` | Line → source → formula → recomputed quantity → delta → classification |
| `fixtures.json` | 6 engine test cases, one per line |
| `reading-guide.md` | Which sheets, legends, tags and notes to read, the exact strings, cross-checks and traps |
| `app-gaps.md` | The TakeoffSpeed engine run on these inputs; what differs, ranked by quantity impact |

## Driving sheets

| Sheet | Markup page | Role |
|---|---|---|
| S-201 Structural Plan – Foundation | p33 (legend) | Footing marks and counts, WF20 run length (124.2 FT), stem walls (8" × 193.8 FT, 10" × 8.4 FT, "@ 2'H"), and the WALL FOOTING / SPREAD FOOTING SCHEDULES. Notes: "TOP OF FOOTINGS AT ALL EXTERIOR [and INTERIOR] FOOTINGS SHALL BE [-2'-0"] BELOW FINISH FLOOR SLAB", "MAXIMUM EARTH DIFFERENTIAL WHEN BACKFILLING SHOULD NOT EXCEED 2'-0"" |
| S-600 Wall Sections – Foundation | p37 (no legend; red band over sections 1–3) | WF20 2'-0" × 1'-0", 8" stem, "4" CMU BELOW GRADE", "FOR SLAB SUBGRADE SEE GEOTECH. REPORT" |
| S-001 General Notes | — | Foundation note 1: bear on original earth or controlled compacted fill, 3,000 psf. Note 2: wall footings 12" thick |
| C-4.0 Grading Plan | p73 (14 area rows), p74 (storm), p91 (cut/fill hatch) | Existing and proposed elevation areas; the red (cut) and blue (fill) Earthwork Pro hatch; FFE 441.00 |
| PlanSwift Earthwork Pro Summary | p92 | Cut / Fill / Qty for each of 14 proposed-contour regions, and the totals 634.41 / 786.25 / 151.84 CU YD |
| C-0.1 General Notes (grading) | — | "ALL CUT OR FILL SLOPES SHALL BE 2:1 OR FLATTER"; "ALL PROPOSED CONTOURS AND SPOT ELEVATIONS REFLECT FINISHED GRADES"; "PROPOSED CONTOURS … IN DRIVES AND PARKING LOTS AND SIDEWALKS ARE FINISHED ELEVATIONS INCLUDING PAVEMENT"; "ALL UNSURFACED AREAS DISTURBED BY GRADING OPERATION SHALL RECEIVE 4 INCHES OF TOPSOIL"; site prep and fill per the geotechnical report |
| C-4.2 Infiltration Basin Detail | — | Bottom of basin 435.00, rim 436.5, top of dam 438.25, slopes 3:1 maximum, bottom of gravel 429.5 |

## Specifications

The project manual has **no Division 31 earthwork section**. The table of contents (spec p. 9)
lists only `31 3116 Termite Control` and "Geotechnical Report — N/A". Earthwork requirements come
from the drawings' notes and the Terracon report.

| Source | Page | Requirement |
|---|---|---|
| 03 3000 Cast-in-Place Concrete §3.2 Site Preparation | spec p. 58 | Excavations deeper than 5 ft need a back slope no steeper than 1V:1.5H, or sheeting and bracing. All footings here are 3.0–3.33 ft deep from FF, so they are cut vertical. |
| 31 3116 Termite Control | spec pp. 481–484 | Coordinate soil treatment with excavating, filling and grading. Re-treat soil disturbed by later excavation. No quantity. |
| Terracon Geotechnical Report 49265099 (`source/drawings/GeoTechnical/`) | PDF pp. 13–17 | Strip topsoil in building and parking areas. Proofroll. Scarify fill areas 10". Existing fill to about 3 ft in 5 of 8 borings. Structural fill: max lift 8" loose (4–6" hand equipment), 98% of standard Proctor (ASTM D698) within 1 ft of slab or pavement subgrade, 95% deeper, general fill 92%. Moisture −2% to +3% of optimum. On-site soils CL/SC are reusable (LL < 45, PI < 25). |
| Terracon (Shallow Foundations) | PDF pp. 20–21 | 3,000 psf. Minimum embedment: exterior footings 18", interior 12". Minimum widths: columns 24", continuous 16". For passive resistance, concrete is placed **neat** against vertical sides, or the forms are removed and compacted structural fill is placed. |

The report gives **no shrink or swell factor**, and the estimator applied none.

## Material types and properties

| Material | Where | Property |
|---|---|---|
| Excavated soil (bank) | Footing excavation, grading cut | Existing fill (≈3 ft) over coastal-plain soils. Conventional equipment, no rock expected (Terracon). |
| Footing backfill | Around footings and stem walls | On-site soil or structural fill, compacted to 95% std. Proctor (98% within 1 ft of slab subgrade). Max differential 2'-0" while backfilling (S-201 note). |
| Grading fill | Proposed regions below existing | Structural fill within 10 ft of structures and pavements, otherwise general fill. 8" loose lifts. |
| Haul-off | Displaced footing and stem volume | Bank CY. No swell is carried. |

## What the estimator measured, and in which units

- **Footings (S-201, p33):** counts in EA for each spread-footing mark, the WF20 run in FT
  (124.2, measured clear between the spread-footing outlines), and stem walls in FT. No
  excavation was measured. Lines 629–631 are formulas on these measurements plus the schedule
  sizes and the −2'-0" top-of-footing note. They are rounded to 0.1 CY.
- **Grading (C-4.0, p73 → p92):** six "Existing" flat elevation areas (437.5, 438.5, 439, 439.5,
  440 and 441; 41,063.9 SF) and fourteen "Proposed" flat-elevation regions (435, 436.5, 437, 438,
  439, 439.5 and 440; 33,148.2 SF), all in SQ FT. PlanSwift Earthwork Pro overlaid them and
  reported cut and fill in CU YD for each proposed region. Lines 639 and 640 are its column
  totals, and 641 = fill − cut. The pond (435 and 436.5 regions) is inside these totals, as
  estimate line 708 says: "POND EARTHWORK HAS BEEN ADDED TO THE GRADING QUANTITY".

| Classification | Lines |
|---|---|
| measured (straight from a PlanSwift report) | 639, 640 |
| derived (formula on measured or scheduled values) | 629, 630, 631, 641 |
| counted / specified / allowance | — |

## Open items

1. The 6"-per-side working space at spread footings is inferred. Only the total reproduces it
   (see `formulas.md` §1 for the sensitivity). The 1'-0" at the wall trench agrees with the
   dumpster footing (line 665).
2. The grading is to **finished** grade, with no pavement-section, slab or topsoil adjustment,
   and the footing excavation is measured from finish floor. Both are the estimator's choice. See
   the traps in `reading-guide.md` for the size of each.

## Verification

Reviewed 2026-10-13 after an independent review of this folder. Each finding was rechecked in
python (`trades/31-earthwork/scripts/verify_grid.py`, `footing.py`) and against the sources.
Models: Claude Opus 5.5 (recomputation, source checks, edits) and GPT-6 Astra via
`tools/ask_gpt.py` (two independent questions).

| Finding | Checked | Result | Change |
|---|---|---|---|
| p73 row `439.500 - Proposed 3841.3 SQ FT` said to be missing from `legends.json` / `legends.csv` | Both files now hold all 14 p73 rows (item 14, "duplicate name restored"); 6 existing rows sum to 41,063.9 SF and 8 proposed rows to 33,148.2 SF | Reviewer right (the claim went stale when the legend files were updated) | Removed the open item and reading-guide trap 8 (traps renumbered); reworded the reconciliation 639 note; noted the duplicate 439.5 row in the reading-guide input table |
| Stem-wall / WF20 concrete dimensions in `formulas.md` §2 and fixtures 630/631 | 193.8 × 8/12 × 2 / 27 = 9.5704 ≠ 9.628148; 8.4 × 10/12 × 2 / 27 = 0.5185 ≠ 0.522593; 9.196296 × 27 / 2 = 124.15 LF. The estimator's 194.0 × 2 × 0.67 and 8.5 × 2 × 0.83 reproduce lines 27–28 exactly | Reviewer right; backfill and haul results unchanged | Inputs now described as the estimator's printed CY (lines 19–28, 36.076544 CY) with the estimator's own LF 124.15 / 194.0 / 8.5; the legend-LF variant (stems 10.0889, backfill 83.7506 CY) is kept as the second example |
| "Only one result lands within ±0.05 CY of 119.8" | Wider grid (working space 0–3 ft, depth T..T+3, trench on 124.2 / 193.8 / 202.2 LF): the 55.2 CY trench term has three decompositions, and a 202.2 LF stem-line trench (5 ft wide, 2.0 ft deep) plus neat pads gives 119.7778 CY | Reviewer right; the claim holds only inside the original grid | Sentence qualified and the alternative stated and rejected. GPT-6 Astra judged it physically implausible (a 2 ft dig stops at the top of the WF20; the pads double count) and, given only the schedules and notes, again derived 1'-0" trench / 6" pads = 119.756 CY as the single 3 × 3 match (118.949 with the shallow F38) |
| Out-of-scope wording in `best-practices.md` (generic, no figures) | grep found lines 66 and 126, plus the scope line 3 | Reviewer right | Reworded to "haul effort follows quantity x distance" and "only for sequencing and testing"; scope line now reads "quantities and material types only" |

Reconciliation count after this pass: still **6 of 6** lines rebuilt, all within 0.07% (no
recomputed quantity changed). `reconciliation.csv`, `fixtures.json` and `formulas.md` carry the
same inputs: excavation 119.7556 CY, footing concrete 25.925803 CY, stem concrete 10.150741 CY,
backfill 83.6790 CY, haul 36.0765 CY, grading 634.41 / 786.25 / 151.84 CY.
