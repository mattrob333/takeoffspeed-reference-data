# Reading guide — 32c erosion and sediment control, pond, landscaping

How to read this job's plans for the 27 lines, with the exact strings as they are printed.
Markup pages are rendered with `tools/render.py markup <page>` and sheets with
`tools/render.py sheet <SHEET>`.

## 1. Order of reading

1. **C-2.0 / C-2.1 / C-2.2 (ESPC Phase 1/2/3).** Start with each sheet's EROSION CONTROL LEGEND
   (lower right, columns CODE / PRACTICE / MAP SYMBOL). It lists the practices that phase uses,
   and those are the only codes that phase's lines may carry:
   - Phase 1: Co, Sd1-NS, Rt-B, Ds1, Ds2, Du, LOD.
   - Phase 2 adds Rt-P, Sd2-F, St, Ds3, Ss.
   - Phase 3: Ds3, Ds4, Ss, Sd2-P, St.
2. **The general notes block on each phase sheet.** It gives "TOTAL SITE AREA = 0.96 ACRES",
   "TOTAL DISTURBED AREA = 0.9 ACRES" and "PHASE n DISTURBED AREA = …" (0.9 for Phase 1, 1.0 for
   Phase 2 and Phase 3). The plan also prints "LIMITS OF DISTURBANCE: 0.9 AC". Use these to check
   the measured stabilization areas.
3. **C-2.5 / C-2.6 details.** These give the material and the size for each code. The estimator
   highlighted the detail titles on p70.
4. **C-2.3 / C-2.4 notes.** The schedule of activities says which practice is installed in which
   phase. The seeding table and the lime and mulch rates are here too.
5. **C-3.0 site plan (p72).** Keynote 23 is the pond reference area.
6. **C-4.0 grading (p74) and C-4.2 basin detail.** Use the pond contours, the stone-bed outline
   (keynote 7) and the elevations.
7. **L-1.0 (p83).** Read the PLANT LIST (lower right), then check it against the plan callouts
   `(n) NAME` along the south buffer.
8. **L-1.1 details.** Mulch depth, sod placement, planting pits.

There is **no spec section** for this trade in the project manual. Do not look for a 31 25 00 or a
32 90 00; the drawings are the specification.

## 2. Legend rows and the line each one feeds

| Markup page | Legend row (exact, as printed) | Qty | Feeds |
|---|---|---|---|
| p65 C-2.0 | `CO: CONSTRUCTION EXIT` | 1569.4 SQ FT | 684 (ceil → 1570) |
| p65 | `CONCRETE WASHOUT` | 25.1 SQ FT | 685 as **1 EA** (the area is ignored) |
| p65 | `FUEL STORAGE` | 25.1 SQ FT | 686 (→ 25) |
| p65 | `SD1-NS: SEDIMENT BARRIER - NON SENSITIVE` | 767.9 FT | 687 (→ 768) |
| p65 | `RT-B: SLOTTED BOARD DAM RETROFIT` | 5.1 FT | 688 (raw 5.14) |
| p65 | `DS1, DS2 & DU` (teal swatch) | 20298.9 SQ FT | 689, 690, 691 (Phase 1) |
| p65 | `DS1, DS2 & DU` (red swatch) | 15581.9 SQ FT | 694, 695, 696 (Phase 2) |
| p66 C-2.1 | `SD2-F: TRMPORARY INLETE SEDIMENT TRAP( FILTER FABRI...` | 193.7 FT | 692 (→ 194) and, copied, 699 |
| p66 | `RT-P: PERFORATED HALF-ROUND PIPE RETROFIT` | 7.5 FT | 693 (carried as 7.0; unresolved) |
| p66 | `SS, DS3: AREA` | 2114 SQ FT | 697, 698 |
| p66 | `ST-1:` | 962.4 SQ FT | **no line**. It traces the stone bed; use it for 710/711 |
| p67 C-2.2 | `TEMPORARY INLET SEDIMENT  TRAP (CURB INLET PROTEC...` | 74.5 FT | **no line** (line 699 should use it) |
| p67 | `DS4` | 14393.7 SQ FT | 700 |
| p72 C-3.0 | `23: PROPOSED STORMWATER PO...` | 3074 SQ FT | 708, 709, 711 |
| p83 L-1.0 | PLANT LIST rows, highlighted in purple | 5 / 11 / 17 / 15 / 2,500 S.F. / 11,500 S.F. | 701–706 |

`reference/markups/legends.json` and `legends.csv` carry both p65 `DS1, DS2 & DU` rows (coral-red
15581.9 and teal 20298.9, told apart only by the swatch colour). An app that merges legend rows by
name will lose one of the two areas; see `app-gaps.md` (legend adapter).

## 3. How each formula input is read

| Input | Where | String / value |
|---|---|---|
| Exit pad area | p65 maroon area at the Westgate Drive entrance, tag `Co` | 1569.4 SF. Detail minimum 20' × 50' = 1000 SF |
| Exit stone and fabric | C-2.5 CRUSHED STONE CONSTRUCTION EXIT | "N.S.A. R-2 (1.5"–3.5") COARSE AGGREGATE", "6" MIN.", "GEOTEXTILE UNDERLINER", "TIRE WASHRACK AREA/ TIRE WASHERS", "CULVERT UNDER ENTRANCE (IF NEEDED)" |
| Washout | C-2.5 CONCRETE WASHDOWN | "PROVIDE 7'x7' CONCRETE WASHOUT AREA", "APPROX. 30" STORAGE DEPTH", "PLASTIC SHEETING (10 MIL, MIN)" |
| Sock length | p65 slate-blue line, following the LOD/SF line on the west, south and east | 767.9 FT |
| Sock size, stakes | C-2.5 COMPOST FILTER SOCK (Sd1-NS) | "FILTER SOCK SIZED TO SUIT CONDITIONS AND AT LEAST 18" DIA", "WOODEN STAKES (2' O.C. FOR TYPE NS)" |
| DS zones | p65 red and teal polygons inside the LOD. Red is two lobes, north-centre and south-east, each over an existing building outline on the Phase 1 base; teal is the rest of the LOD around and between them (west strip, south-west, the north-east corner, and the existing striped parking). They do not overlap | teal 20298.88 / red 15581.92 SF |
| Inlet frames | p66 green squares around the 4 `Sd2-F` inlets | 193.7 FT total |
| Rt-P | p66, a small arc at the outlet riser of the pond, tag `Rt-P` | 7.5 FT. C-2.1 table "Half Round CMP Diameter 2.25 FT", "Half Round CMP Height 2.00 FT" |
| Pond slopes | p66 periwinkle ring between the 435 and 438 contours, tags `Ss` `Ds3` | 2114 SF |
| DS4 | p67 maroon: every pervious area except the pond | 14393.7 SF |
| Pond area | p72 magenta stadium shape, keynote 23, the pond at top of bank (438) | 3074 SF |
| Stone bed | C-4.0 keynote 7 hatch inside the 435 contour; p66 `ST-1:` magenta | 95.6 × 10.27 ft bbox, 948 SF vector area, 962.4 SF traced |
| Stone depth | C-4.2 | "BOTTOM OF INFILTRATION BASIN: 435.00", "BOTTOM OF GRAVEL: 429.5" → 5.5'. Trench section "66"" |
| Geotextile extent | C-4.2 INFILTRATION TRENCH CROSS SECTION | fabric drawn on the bottom and both sides only |
| Underdrain | C-4.2 "6" PERFORATED HDPE UNDERDRAIN", "UPTURNED UNDER DRAIN" | 1 run along the bed, 95.6 → 96 LF |
| Plants | L-1.0 PLANT LIST, columns COMMON NAME / BOTANICAL NAME / QUANTITY / MIN. SIZE / MIN. SPACING / NOTES | see formulas F8 |

## 4. Cross-checks that work on this job

- **Pond = slopes + bed.** 3074 (pond) − 962.4 (ST-1 bed) = 2111.6, against 2114 for SS/DS3
  (−0.1%). If the stone bed area is in doubt, use this.
- **Stone bed against the design minimum.** 962.4 SF ≥ "MINIMUM SURFACE AREA OF 950 SF". Any
  stone area much larger than about 1000 SF is the wrong polygon.
- **Underdrain against the bed.** The underdrain length should be about the bed length:
  962.4 / 10.27 ≈ 94, and the bbox length is 95.6.
- **Stabilization against the LOD.** Phase 1 + Phase 2 polygons = 35,880.8 SF, against 0.9 AC =
  39,204 SF (−8.5%). The estimator's trace runs inside the LOD line.
- **Final cover against the site summary.** L-1.0 SITE SUMMARY gives PERVIOUS AREA 20,876 S.F.
  DS4 14,393.68 + DS3 2,114 = 16,507.68 SF, which fits. Sod 11,500 + DS4 14,393.68 = 25,893.68
  SF is more than the whole pervious area, so the two sod lines overlap.
- **Plant list against the plan.** Shrubs agree (17 = 7+3+7, 15 = 6+9). Trees do not.

## 5. Traps hit on this job

1. **Two legend rows with the same name.** p65 has `DS1, DS2 & DU` twice, with different swatches
   and areas. They are two polygons, not a duplicate. The phase split is teal → Phase 1 and
   red → Phase 2. The Phase 2 area is measured on the **Phase 1 sheet**, because C-2.1 has Ds tags
   but no area row.
2. **The Phase 3 inlet line is a copy.** Line 699 says SD2-F at 194 LF. C-2.2 calls **Sd2-P**
   (curb inlet protection, C-2.5 "CURB INLET FILTER "PIGS IN BLANKET"") and the p67 legend
   measured 74.5 FT. C-2.3 note: "SD2-P MAY BE INSTALLED ON INLET STRUCTURES WITH STRUCTURE TOPS IN
   PLACE". Read each phase's own legend; do not carry the previous phase forward.
3. **Stone over the wrong footprint.** The keynote 23 pond area (3074 SF, top of bank) is a
   reference line for earthwork. The stone is only the 435 bottom bed. The estimator's 626 CY is
   3.2 times what the detail supports (196 CY).
4. **Geotextile wrap.** Bottom + sides ≈ 2081 SF. Bottom + sides + top would be 3058 SF, which is
   close to the pond area by coincidence. The section shows no top fabric.
5. **Sock diameter.** The estimate says "30" DIA COMPOST FILTER SOCK". The detail's 30" is "30"
   MIN." (stake height above ground). The sock is "AT LEAST 18" DIA". Do not order 30" sock from
   this line.
6. **Washout as an area.** The legend measured the drawn symbol (25.1 SF). The line is 1 EA of the
   7'×7' pit.
7. **The ESPC sheets and the landscape plan both carry sod.** DS4 (ESPC, 14,393.68 SF) and SOD
   (L-1.0 plant list, 11,500 SF) are the same lawns. L-1.0 also says "SOD SHALL BE USED IF UNABLE
   TO ACHIEVE STABILIZATION WITH EROSION CONTROL SPECIFICATIONS" for the pond slopes and bottom.
8. **Designer quantities.** The PLANT LIST says "ALL QUANTITIES ARE FOR A GENERAL GUIDE ONLY.
   CONTRACTOR SHALL CONFIRM ALL QUANTITIES". The pine straw and sod SF were not measured. Measure
   the MULCH and SOD / GRASS hatches when the app reproduces this trade.
9. **Tree species swap.** The schedule says Holly 5 and Redcedar 11. The plan has 11 scalloped
   holly symbols with the callout "(11) AMERICAN HOLLY", and 6 starburst redcedars ((1) + (5)).
   Raise an RFI; do not silently pick one.
10. **Typos to tolerate when matching names:** `TRMPORARY`, `INLETE`, `DRIVE TRRU`,
    `PINESTRAWV-MULCH A`, `LLEX OPACA`, `LLICIUM`, `DON'S DW ARF WAX MYRTILE`, `GAL: 3'` (it is
    3 GAL). Legend names are cut off with `...` (FILTER FABRI..., CURB INLET PROTEC...,
    STORMWATER PO...).
11. **Sheet ID drift.** `pages.json` lists p65 as C-2.0 with `correctedFromVisualMatch: "C-2.2"`.
    The title block, the "PHASE 1 DISTURBED AREA" note and the legend content all show it is
    C-2.0 (Phase 1).
12. **ST-1 label.** On C-2.1 the `St-1` tag sits in the pond. St-1 is the 18" pipe outlet apron
    (C-2.5 table: La 9.0', W1 4.5', W2 10.5', d50 0.3'), but the estimator's `ST-1:` area traces
    the whole stone bed. That area is useful for the bed; it is not a rip rap quantity.
