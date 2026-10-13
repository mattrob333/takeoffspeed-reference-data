# Formulas — 32c erosion and sediment control, pond, landscaping

Every quantity here is net, with no waste. All arithmetic was done in
`trades/32c-erosion-landscape/scripts/py/build.py`. "Legend" means the PlanSwift legend row on the
markup page named. The legend prints one decimal place; the estimate sometimes carries the raw
two-decimal value.

F7, F9 and F10 reproduce the estimator, not the drawings. Their fixtures (699, 709, 711) carry
`"estimatorParity": true` and a `perDrawings` block with the drawing-supported value (74.5 LF,
2081.1 SF, 196.04 CY), so an engine test can keep them out of truth assertions.

## Estimator conventions found on this job

| Convention | Rule | Basis on this job |
|---|---|---|
| Hand rounding | Some measured rows go to a whole unit: CO 1569.4 → 1570 and SD1-NS 767.9 → 768 and SD2-F 193.7 → 194 (all up), fuel 25.1 → 25 (nearest). Others keep the raw decimals: 20298.88, 15581.92, 14393.68, 5.14 | The rule is not consistent. Treat it as a ±1-unit display choice, with a 1% tolerance |
| One area, many practices | A zone tagged with several practice codes gets one SF line per practice, each with the zone SF | Ds1 / Ds2 / Du stacked on the C-2.0 tags → lines 689–691 and 694–696. Ss / Ds3 → 697–698 |
| Install once | A barrier is carried on the phase where it is first installed and is not repeated on later phases | SD1-NS is carried on Phase 1 only. C-2.1 still shows Sd1-NS, but no new line was made |
| Carry forward | When the later phase sheet calls a different inlet practice, the earlier quantity is copied | Line 699 copies line 692 (194 LF of SD2-F) |
| Detail accessories ride on the parent line | Stone, fabric, washrack, culvert, liner and stakes are named in the description and get no quantity | Lines 684, 685, 687, 693 |
| Plant list is the count | Trees and shrubs come from the schedule QTY, not from plan symbols | Lines 701–704 |
| Pond reference area drives fabric and stone | geotextile SF = pond SF; stone CY = pond SF × stone depth ÷ 27 | Lines 709 and 711. The drawings do not support this; see F10 |

---

## F1 — Measured area (SF)

`areaSF = Σ areas` (optionally `ceil` or `round` to a whole SF)

- Inputs: each closed area at the plan scale (1" = 20'), in SF.
- Lines: 684 CO (ceil), 686 fuel storage (round), 689 / 694 DS zones, 697 SS/DS3 ring,
  700 DS4, 708 pond.
- Worked example, 684: legend "CO: CONSTRUCTION EXIT" 1569.4 SQ FT → ceil(1569.4) = **1570 SF** ✓.
- Worked example, 708: "23: PROPOSED STORMWATER PO..." 3074 SQ FT → **3074 SF** ✓. Cross-check:
  the 438 contour on C-4.0 is a closed vector path of 3056.4 SF (−0.6%).

## F2 — Stacked practice (derived SF)

`practiceSF(p) = zoneSF` for each practice code p tagged on the zone.

- Lines 690, 691 = 689 = **20298.88 SF**. Lines 695, 696 = 694 = **15581.92 SF**. Line 698 = 697 =
  **2114 SF**.
- Cross-check for 697: the slope ring is the pond area minus the stone bed. 3074 − 962.4 (ST-1) =
  2111.6 SF, against 2114 (−0.11%).

## F3 — LOD split between phases (allocation)

`phase1 DS SF = polygon A; phase2 DS SF = polygon B`. Both polygons are measured on the
**Phase 1 sheet**.

- Values: teal 20298.88 SF → Phase 1 (689–691). Red 15581.92 SF → Phase 2 (694–696).
- Check: A + B = 35,880.8 SF = 0.824 AC. The printed LIMITS OF DISTURBANCE is 0.9 AC = 39,204 SF,
  so the estimator's trace is 8.5% under the printed figure.
- The split is the estimator's choice. A rule the app can reproduce: take the measured LOD
  polygons and assign each one to a phase. Never sum the two into both phases.

## F4 — Measured run (LF)

`runLF = Σ runs` (optionally `ceil` to a whole LF)

- 687 SD1-NS: ceil(767.9) = **768 LF** ✓.
- 688 RT-B: legend 5.1 (raw 5.14) → **5.14 LF**. From the printed 5.1 the delta is −0.78%.
- 692 SD2-F: ceil(193.7) = **194 LF** ✓. The run is the fabric frame drawn around each of the
  4 Sd2-F inlets: 193.7 / 4 = 48.4 LF per inlet as drawn.
- 693 RT-P: legend 7.5 → estimate **7.0 LF**. This is the one line that does not reproduce
  (+7.1% from the printed value), and **7.0 is unexplained**. The printed 7.5 only bounds the raw
  PlanSwift value to 7.45–7.55, and the raster cannot narrow that: a circle fit to the p66 arc
  gives a semicircle of radius about 2.2–2.3 ft, centreline about 7.3 ft (6.6–7.9 ft across the
  stroke; a second fit gave 7.66 ft). π × 2.25 = 7.07, with 2.25 from the C-2.1 PHASE 2 – SEDIMENT
  STORAGE TABLE "Half Round CMP Diameter 2.25 FT", is the CMP's full circumference, which this item
  never measures. Neither fit is supported. Recommended quantity: **1 EA**, one 2.25' dia
  half-round CMP 2.00' high on the weir, i.e. **2.00 LF** of CMP along its axis. No fixture.
- 710 underdrain (derived, inferred; not an estimator measurement): no legend row on any page.
  The analyst's scaling of the stone bed outline on C-4.0 (vector bbox) is 95.60 ft long
  → ceil = **96 LF** ✓. Equivalent: ST-1 962.4 SF ÷ 10 ft bed width = 96.24 → 96. Which of the
  two the estimator used is inferred.

## F5 — Sock stakes (not carried, available)

`stakes = ceil(LF / spacing) + 1`, with spacing = 2' O.C. ("WOODEN STAKES (2' O.C. FOR TYPE NS)",
C-2.5).

- 768 → ceil(768/2) + 1 = 385 EA. The estimate puts "WOODE STAKES 2' O.C." in the line 687
  description and has no separate line.

## F6 — Counted item (EA)

`EA = count of the practice symbol or area`

- 685 concrete washout: 1 area on C-2.0 → **1 EA** ✓. The size (7'×7') and liner (10 MIL) come
  from the C-2.5 detail text. The legend's 25.1 SF is the area of the drawn symbol (about 5'×5'),
  not the pit.

## F7 — Phase carry-forward (derived)

`phase3 inlet LF = phase2 inlet LF`

- 699 = 692 = **194 LF** ✓ (reproduces the estimator).
- What the drawings support: C-2.2 calls Sd2-P (curb inlet protection) at 4 inlets, and the
  estimator measured it as 74.5 FT on p67. The phase-correct formula is
  `phase3 LF = Σ runs on the Phase 3 sheet = 74.5 LF` (−61.6% against the estimate).

## F8 — Specified from schedule (EA / SF)

`qty = PLANT LIST QUANTITY`

| Line | Plant list row | QTY | Plan callouts |
|---|---|---|---|
| 701 | American Holly, *Ilex opaca* 'Greenleaf', 6' HT., 12' O.C., B&B | **5** | (11) AMERICAN HOLLY; 11 holly symbols — CONFLICT |
| 702 | Eastern Redcedar, *Juniperus virginiana*, 6' HT., 40' O.C., B&B | **11** | (1) + (5) = 6 — CONFLICT |
| 703 | Florida Sunshine Anise, *Illicium parviflorum* 'Florida Sunshine', 3 GAL, 5' O.C. | **17** | (7) + (3) + (7) = 17 ✓ |
| 704 | Don's Dwarf Wax Myrtle, *Myrica cerifera* 'Don's Dwarf', 3 GAL, 5' O.C. | **15** | (6) + (9) = 15 ✓ |
| 705 | Pinestraw (Mulch A) | **2,500 S.F.** | — |
| 706 | Sod | **11,500 S.F.** | — |

The schedule's subtotals check: trees 5 + 11 = 16, shrubs 17 + 15 = 32. The plan shows 17 trees.
Available but not carried: pine straw at 3" depth (L-1.1 note 6) is 2500 × 0.25 / 27 = 23.1 CY,
or 50 bales at 50 SF per bale.

## F9 — Pond geotextile (derived, estimator convention)

`geotextileSF = pondAreaSF`

- 709 = 708 = **3074 SF** ✓.
- What the drawings support: the C-4.2 INFILTRATION TRENCH CROSS SECTION shows 6 OZ/SY fabric on
  the **bottom and sides** of the stone bed, with no top wrap.
  `geotextileSF = bedSF + bedPerimeter × depth = 948.1 + 206.0 × 5.5 = 2081.1 SF` (−32%), before
  laps. Bed SF and perimeter come from the C-4.0 435-contour vector path.
- Trap: a full wrap (bottom + sides + top) would be 962.4 × 2 + 206 × 5.5 = 3057.8 SF, within
  0.5% of 3074. That is a coincidence. The section does not show fabric on top.

## F10 — Storage stone (derived, estimator convention)

`stoneCY = area × (basinBottom − gravelBottom) / 27`

- Inputs: area = 3074 SF (line 708), basinBottom = 435.00 ("BOTTOM OF INFILTRATION BASIN:
  435.00"), gravelBottom = 429.5 ("BOTTOM OF GRAVEL: 429.5"), both from C-4.2. Depth = 5.5 ft,
  which matches the 66" dimension on the trench section.
- 711: 3074 × 5.5 / 27 = **626.185185 CY** ✓ (exact to 6 dp).
- What the drawings support: area = the stone bed only, 962.4 SF (ST-1 legend on p66; the C-4.0
  vector path gives 948.1). "INFILTRATION TRENCH SHALL HAVE A MINIMUM SURFACE AREA OF 950 SF".
  So 962.4 × 5.5 / 27 = **196.04 CY** (−68.7%), or 193.1 CY on the vector area.
- Corroboration from the water-quality volume (assumes about 40% voids in open-graded stone,
  which the set does not print): 962.4 SF × 5.5 ft × 0.40 = 2,117 CF, against C-4.2 "PROVIDED WQv =
  2,225 CF" (−4.8%; it implies 0.42 voids). The estimator's footprint gives 626.185 CY × 27 × 0.40
  = 6,763 CF, three times the provided WQv (it would imply 0.13 voids).

## Not carried by the estimator (the app may add them; quantities shown for reference)

| Item | Formula | This job |
|---|---|---|
| Construction exit stone | SF × 6" / 12 / 27 | 1570 × 0.5 / 27 = 29.07 CY |
| Exit geotextile | = exit SF | 1570 SF |
| Washout liner | (7 + 2 × 2.5 + 2 × 1) × same | 14 × 14 = 196 SF (engine, with a 1' anchor) |
| Straw mulch, Ds1 | AC × 2 TON/AC (C-2.5 dry straw rate) | Phase 1 0.932 TON, Phase 2 0.715 TON |
| Sock stakes | F5 | 385 EA |
| Rip rap / St-1 outlet | C-2.5 St-1: La 9.0', W1 4.5', W2 10.5', d50 0.3', dmax 0.9' | apron 9 × (4.5 + 10.5) / 2 = 67.5 SF. The estimator's "ST-1:" 962.4 SF row traces the stone bed instead |
