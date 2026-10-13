# Formulas — 31 earthwork

All volumes are computed in CF and divided by 27 for CY. Dimensions are in feet: 3'-8" = 3.6667,
1'-2" = 1.1667, 1'-4" = 1.3333. The scripts are `trades/31-earthwork/scripts/footing.py` and
`grading.py`.

---

## 1. Footing excavation (line 629)

**Name:** `footingExcavationCY`

**Inputs**

| Input | Unit | This job |
|---|---|---|
| `wf.length` — continuous footing run, measured clear between spread-footing outlines | LF | WF20 124.2 (p33 legend) |
| `wf.width`, `wf.thickness` | ft | 2.0, 1.0 (WALL FOOTING SCHEDULE: WF20 2'-0" × 1'-0") |
| per spread mark: `L`, `W`, `T`, `n` | ft, ft, ft, EA | SPREAD FOOTING SCHEDULE + p33 legend counts (table below) |
| `tof` — top of footing below finish floor | ft | 2.0 (S-201 note "[-2'-0"] BELOW FINISH FLOOR SLAB"; every tag reads [-2' - 0"] except one F38 [-1' - 0"]) |
| `wsWall` — working space each side of the trench | ft | 1.0 (estimator convention) |
| `wsPad` — working space each side of a spread pad | ft | 0.5 (estimator convention) |

**Rule**

```
depth           = T + tof                       (bottom of footing below FINISH FLOOR)
trench CF       = wf.length × (wf.width + 2·wsWall) × (wf.thickness + tof)
pad CF (each)   = (L + 2·wsPad) × (W + 2·wsPad) × (T + tof)
excavation CY   = (trench CF + Σ n·pad CF) / 27        → printed to 0.1 CY
```

- The sides are vertical, with no slope or benching. Every depth is ≤ 3.33 ft, under the 5 ft
  trigger in 03 3000 §3.2.
- The trench and pad volumes are added without removing the small overlap where the trench meets
  a pad.

**Conventions and their basis**

- **1'-0" each side at the continuous trench.** The same estimator used exactly this on the
  dumpster wall footing (line 665: 36.22 × (2 + 2 × 1) × 2.33 / 27), so it is a house
  convention.
- **6" each side (L + 1, W + 1) at spread pads.** This is inferred from this job. A search ran
  over working space {0, ½, 1, 1½, 2} ft and depth {T, T+1, T+2}, separately for pads and trench,
  with and without a separate stem-wall trench. Within that grid (working space 0–2 ft, depth
  T..T+2, trench on the WF20 124.2 LF), only one volume lands within ±0.05 CY of 119.8: pads
  (L+1)(W+1)(T+2) plus a 55.2 CY trench. The 1,490.4 CF trench term has three decompositions:
  124.2 × 4 × 3 (1 ft each side, depth T + 2), 124.2 × 6 × 2 (2 ft each side, depth T + 1) and
  124.2 × 3 × 4 (6" each side, depth T + 3). The dumpster line confirms the 1 ft / T + wall-height
  reading.
- **A wider grid has one other near-match, rejected.** Widening the search (working space 0–3 ft,
  depth T..T+3, trench on 124.2, 193.8 or 202.2 LF) finds one other volume: a trench along the
  202.2 LF stem-wall line, 2 ft wide + 1.5 ft working space each side (5 ft), only 2.0 ft deep
  (2,022 CF, also 202.2 × 2.5 × 4), plus neat pads L × W × (T + 2), gives 119.7778 CY (0.022 CY
  from 119.8). It is physically implausible: a 2 ft
  dig stops at the top of the WF20, leaving the footing's 1 ft thickness unexcavated, and the
  full-depth perimeter pads double count the trench above them. GPT-6 Astra, asked about it
  directly, gave the same verdict. GPT-6 Astra, given only the schedules, notes and legend values,
  derived the same 1'-0" trench / 6" pad split, with 119.7556 CY as the single match in its 3 × 3
  grid (118.949 if the shallow F38 is honoured).
- **Depth from finish floor, not finished grade.** Top of footing −2'-0" is referenced to the
  slab. The estimator dug from FF level everywhere.

**Sensitivity** (exact dimensions)

| Variant | CY | vs 119.8 |
|---|---:|---:|
| Estimator: 1' trench / 6" pads, depth T + 2 | 119.7556 | −0.04% |
| 1' everywhere (TakeoffSpeed default) | 143.1383 | +19.48% |
| 6" everywhere | 105.9556 | −11.56% |
| Neat (no working space) | 72.4889 | −39.49% |
| Same, but the one F38 tagged [-1'-0"] dug 1 ft shallower | 118.9490 | −0.71% |

**Worked example**

| Item | Arithmetic | CF | CY |
|---|---|---:|---:|
| WF20 | 124.2 × (2 + 2) × (1 + 2) | 1,490.400 | 55.2000 |
| F30 ×3 | 3 × (3 + 1) × (3 + 1) × (1 + 2) | 144.000 | 5.3333 |
| F38 ×3 | 3 × 4.6667 × 4.6667 × 3 | 196.000 | 7.2593 |
| F50 ×6 | 6 × 6 × 6 × 3.1667 | 684.000 | 25.3333 |
| F60 ×1 | 7 × 7 × 3.3333 | 163.333 | 6.0494 |
| F70 ×1 | 8 × 8 × 3.3333 | 213.333 | 7.9012 |
| F7040 ×1 | 8 × 5 × 3.3333 | 133.333 | 4.9383 |
| F10050 ×1 | 11 × 6 × 3.1667 | 209.000 | 7.7407 |
| **Total** | | 3,233.400 | **119.7556 → 119.8** |

---

## 2. Footing backfill (line 630)

**Name:** `footingBackfillCY`

**Inputs**

| Input | Unit | This job |
|---|---|---|
| `excavationCY` | CY | 119.7556 (§1) |
| `footingConcreteCY` | CY | 25.925803 = Σ the estimator's printed CY on estimate lines 19–26 (WF20 9.196296; spread footings 1.0 + 1.496544 + 6.5 + 1.773333 + 2.413704 + 1.379259 + 2.166667). Line 19 implies the estimator's own WF20 run of 124.15 LF (124.15 × 2 × 1 / 27); the legend's 124.2 LF would give 9.2 |
| `stemWallConcreteCY` | CY | 10.150741 = the estimator's printed CY on line 27 (8" stem) 9.628148 + line 28 (10" stem) 0.522593. The estimator's own dimensions were 194.0 LF × 2 ft × 0.67 ft and 8.5 LF × 2 ft × 0.83 ft (see `02-concrete`). The legend runs are 193.8 and 8.4 FT; at exact 8" / 10" they give 9.5704 + 0.5185 = 10.0889 CY |

**Rule**

```
backfill CY = excavationCY − footingConcreteCY − stemWallConcreteCY
```

The deduction uses the estimator's printed concrete CY (lines 19–28, 36.076544 CY in total), not
a recomputation from the legend LF. Rebuilding the concrete from the legend LF and exact
thicknesses gives 9.2 CY (WF20) and 10.0889 CY (stems) instead; that variant is the second worked
example below.

All stem walls are deducted, including the runs that sit on spread footings rather than on WF20.
The stem walls are 202.2 FT against 124.2 FT of WF20. This is correct, because the whole 2'-0"
stem sits inside the dug depth.

**Not deducted:**

- the slab and 4" gravel bed in the top 8" of each dig;
- the 4" CMU below grade (line 31).

No compaction or shrink factor is applied. Backfill is the in-place geometric void.

**Worked example**

119.7556 − 25.9258 − 10.1507 = **83.6790 → 83.7** (−0.03%).

The same arithmetic from the printed 119.8 gives 83.7235, which also prints as 83.7.

From the nominal schedule dimensions instead of the estimator's concrete lines:

- footings 25.9160 CY;
- stems 10.0889 CY, using the legend LF (193.8 × 8/12 × 2 + 8.4 × 10/12 × 2) / 27;
- backfill 83.7506 CY (+0.06%).

---

## 3. Footing haul-off (line 631)

**Name:** `footingHaulCY`

**Rule**

```
haul CY = excavationCY − backfillCY  ( = footingConcreteCY + stemWallConcreteCY )
```

The result is in bank CY, with no swell. The soil the concrete displaces is hauled; the rest goes
back in.

**Worked example**

119.7556 − 83.6790 = 36.0765 → **36.1** (−0.07%).

This equals the concrete of lines 19–28: 36.0765 CY.

**Estimator ratios on this job (descriptive, not rules):**

- excavation ÷ concrete = 3.32;
- backfill ÷ excavation = 0.699;
- haul ÷ excavation = 0.301.

---

## 4. Grading cut (line 639) and fill (line 640)

**Name:** `gradingCutCY`, `gradingFillCY`

**Inputs:** one row per Earthwork Pro region: its proposed elevation, Cut Total (CY) and Fill
Total (CY), read from markup p92. A blank cell (printed "CU YD" with no number) is 0.

**Rule**

```
cut  CY = Σ region.cut
fill CY = Σ region.fill
```

How PlanSwift gets the region values: it overlays each proposed flat-elevation region (p73
"P" rows) on the existing flat-elevation areas ("E" rows). For each overlap it takes the area ×
(existing − proposed), as cut where positive and fill where negative. Both surfaces are
**finished grade**. No pavement, slab or topsoil section is subtracted. The overlap geometry
lives in the PlanSwift file, not in the PDF (the markup pages are raster). The app should
therefore either read the report table or compute its own grid (`earthwork.grid-cell`) from
contours.

**Worked example (p92)**

- **Cut:** 1.78 + 61.2 + 15.69 + 27.56 + 58.96 + 47.33 + 25.2 + 238.52 + 158.17 = **634.41**
- **Fill:** 51.72 + 151.02 + 224.56 + 199 + 2.11 + 12.81 + 84.11 + 37.98 + 18.35 + 4.59 = **786.25**

Both match the printed totals exactly. Each row's printed Qty also equals fill − cut, for all 14
rows.

**Cross-check (consistency of the region model):** implied mean existing elevation =
proposed − net CF ÷ region area. The p73 area rows give the region area.

| Proposed | Region SF (p73) | Cut CY | Fill CY | Mean Δ (ft) | Implied existing |
|---|---:|---:|---:|---:|---:|
| 440 | 20,233.7 | 1.78 | 641.22 | +0.853 | 439.15 |
| 439.5 | 4,340.1 (3,841.3 + 498.8) | 76.89 | 84.11 | +0.045 | 439.46 |
| 439 | 4,284.7 | 86.52 | 56.33 | −0.190 | 439.19 |
| 438 | 716.1 | 47.33 | 4.59 | −1.611 | 439.61 |
| 437 | 438.2 | 25.20 | 0 | −1.553 | 438.55 |
| 436.5 (pond side slopes) | 2,167.8 | 238.52 | 0 | −2.971 | 439.47 |
| 435 (pond bottom) | 967.6 | 158.17 | 0 | −4.414 | 439.41 |

Every implied existing elevation falls inside the 437.5–441.0 range of the existing rows, so the
report and the areas agree. The two pond regions total 3,135.4 SF, against 3,074 SF for C-3.0
keynote 23 "PROPOSED STORMWATER POND".

---

## 5. Net fill (line 641)

**Name:** `gradingNetFillCY`

**Rule**

```
net CY = fill − cut      (positive = import, negative = export; no shrink, no swell)
```

**Worked example:** 786.25 − 634.41 = **151.84**. This is the p92 Qty total.

**Convention:** the estimator's net is a plain volumetric balance.

- With a 15% bank-to-compacted shrink (the TakeoffSpeed default), the import would be
  786.25 ÷ 0.85 − 634.41 = 290.59 CY.
- The geotechnical report states no shrink, so 0% is what this estimator carries.

---

## Related checks (other trades, same estimator)

- **Pier footings** (32b lines 652–656, 676–677, 715–716, 719–720): excavation = concrete volume
  of the buried part, haul = excavation, no backfill.
- **Dumpster wall footing** (32b lines 665–667): excavation = LF × (W + 2 × 1') × (T + wall below
  grade); backfill = excavation − footing − wall below grade; haul = the difference. Same
  structure as lines 629–631.
- **Pond stone storage** (32c line 711): 626.185185 CY = 3,074 SF × (435.00 − 429.50) / 27. The
  excavation below the basin bottom for this stone is not in lines 639/631. See the trap in
  `reading-guide.md`.
