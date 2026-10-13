# 01 — Demolition: how to read the plans and specs

## Sheets in order

1. **C-1.0 DEMOLITION PLAN** (1" = 20', 36×24). It is the only sheet that carries quantities. Read four
   blocks on the right before the plan:
   - **LEGEND** (5 symbols): `⊠ crosshatch` = DEMOLISH EXISTING STRUCTURES; `dot hatch` = DEMOLISH EXISTING
     PAVEMENT; `line with ///` = DEMOLISH EXISTING UTILITIES; `line with ++++` = DEMOLISH EXISTING
     CURB/GUTTER; `X` = DEMOLISH EXISTING TREE.
   - **KEY NOTES 1–11** (hexagon tags): 1 curb & gutter · 2 building/structure and foundation ·
     3 sanitary sewer · 4 storm sewer · 5 power line · 6 water line · 7 pavement · 8 tree/vegetation ·
     9 sidewalk · 10 monument sign · 11 concrete ramp and stairs.
   - **GENERAL DEMOLITION NOTES 1–7**: note 3 requires a full-depth saw cut at the demolition limits;
     note 7 says utility depths are unknown.
   - **CAUTION** box: utilities are shown for convenience only.
2. **C-0.1 GENERAL NOTES → DEMOLITION NOTES**: remove buildings "INCLUDING FOUNDATIONS AND ALL
   APPURTENANCES", saw cut at pavement/curb to remain and at the R/W, cut and plug services, hazmat by a
   licensed contractor.
3. **Spec 01 7419** (p26–37): the 75% diversion target and the recycling methods. 02 4116 / 02 4119 are
   listed in the TOC (p3) but are **not bound**. Don't search for them.

## How each formula input is read (with this job's strings)

| Input | Where | Exactly what to read |
|---|---|---|
| Building footprint SF | C-1.0 ⊠ hatch, tag ② | The hatched outline. Two-storey: an 11-vertex polygon with a north jog and a west bump, 4,463 SF in CAD and 4,489.1 SF traced. One-storey: a slightly skewed 5-vertex outline, 1,716.4 SF in CAD (bounding box 52.4' × 32.9'; about 52.1' × 32.9' effective) and 1,713.7 SF traced. |
| Stories | Survey text inside the outline | `TWO STORY BUILDING  F.F.E.= 442.2'` and `ONE STORY BUILDING  F.F.E.=440.3'` |
| Storey height | Nowhere on the plans | Use the house convention. This estimator uses 10 ft/storey. |
| Pavement SF | Dot hatch, tags ⑦ (10 tags) | Every dotted region inside the curb lines: the whole west lot, the NE lot and the drive between the buildings. "ASPHALT PARKING LOT" labels. |
| Curb LF | `++++` linetype, tags ① (9 tags) | Follow the ticked line around all islands and radii. Mixed `24" C&G` and `24" ROLL CURB` labels go on one line. |
| Sidewalk SF | Tags ⑨ (3 tags), survey "CONCRETE SIDEWALK" | The L-shaped walk north and west of the one-storey building. It is not hatched; its outline is a thin black line. |
| Ramp SF | Tags ⑪ (3 tags), "CONCRETE SIDEWALK/RAMP", "RAMP" | The walk and ramp between the brick steps and the two-storey building, plus the small pad west of the one-storey building. |
| Brick steps EA | "BRICK STEPS" north of the two-storey building, tag ⑪ | Count the drawn step lines (grey horizontal lines) from the top landing down to the walk edge: 7. Their spacing is unequal (7.7" to 18.7"), so count lines; do not divide a run by a tread depth. |
| Monument sign EA | Tag ⑩ on "BRICK SIGN" | 1 |
| Trees EA | `X` symbols with tag ⑧ | 2: one by "CROSSTIE BOARDER ~1' HIGH" and one in "PINESTRAW ISLAND". |
| Water LF | `W` line with `///`, tag ⑥ | The E-W line across the west lot. |
| Power LF | `OHP`, `UGP`, `TEL` lines with `///`, tag ⑤ | The two diagonals from the pole at the north R/W, plus the TEL loop around the east and south of the two-storey building. |
| Handrail LF | Survey "METAL HANDRAIL" (×2 labels) | The rail along the walk edge from the steps to the ramp, plus both ramp sides. There is no keynote. |
| Storm LF / EA | No tag. Read from the "JB TOP ELEV.: 438.35' I.E. IN: 434.73' I.E. OUT: 434.75'" and "HW 15" HDPE TOP ELEV.: 438.00' I.E. IN: 434.96'" labels | The pipe along the south property line, JB to HW, about 107 LF. 2 structures. |

## Cross-checks that work on this sheet

- **Scale:** the graphic scale bar 0'–40' spans 144 pt on the PDF (3.6 pt/ft). Always verify it before
  trusting a PDF measure.
- **Tick counting:** demolition linetypes have a fixed tick pitch. Use LF ≈ ticks × pitch: `///` every
  5.0 ft (the ticks are `///` text glyphs in the text layer, 222 on the plan), and `++++` one full
  crossing tick every 2.0 ft. Power/TEL gives 194 × 5 = 970 LF (vs 965.4) and curb ≈ 484 × 2 = 967 LF
  (vs 987.2).
- **Chain length:** the firmer check is the length of the linetype polylines themselves, chained in
  drawing order (each polyline is a run of 18 pt or 7.2 pt pieces). Power/TEL 983.4 LF (estimator −1.8%),
  curb 975.2 LF (+1.2%), water 55.8 LF, gas 87.1 LF. Do not chain by shared endpoints alone: the
  utility and curb linetypes are both black 0.72 pt and merge where they cross.
- **Dot hatch:** pavement SF ≈ dots × 4.34 SF here, giving 19,772 SF (vs 19,363.6). The pitch depends on
  the hatch scale; measure it on the sheet.
- **Keynote tag counts** from the text layer: ① ×9, ② ×2, ⑦ ×10, ⑧ ×2, ⑨ ×3, ⑩ ×1, ⑪ ×3, ⑤ and ⑥ several.
  **③ and ④: zero tags.** This is why line 14 says "ASSUMED".

## Traps hit on this job

1. **The PlanSwift legend hides takeoff.** The storm line (yellow) and both storm structures (periwinkle
   dots) lie under the legend box in the lower-left of markup page 64. They are visible only as faint
   circles through the semi-transparent legend. Don't conclude "not marked".
2. **No height for a CFT line.** The unit changes from SQ FT on the markup to CFT on the estimate. The
   multiplier (10 ft/storey) is a convention, not a drawing value. An engine default of 12 ft gives
   +20%.
3. **"Power" includes telephone.** The red trace follows the TEL loop too. Splitting by linetype label
   would give a smaller power LF and a TEL LF that the estimate does not have.
4. **One ticked line has no keynote and no estimate line:** the GAS line (87.1 LF, 17 ticks) from
   the west curb to the one-storey building's A/C pad. Flag it for review rather than invent a quantity.
5. **Keynote 11 is split** into ramp SF (line 7) and brick steps EA (line 8). Keynote 2 is split into two
   lines by storey count.
6. **Steps EA = drawn step lines,** not stairs: seven dots are stacked on one stair. A second "BRICK STEPS" label
   on the west of the two-storey building lies inside the building hatch and is not counted separately.
7. **Handrail has no keynote.** It comes from survey labels plus the C-0.1 note ("ALL APPURTENANCES").
   An AI that only reads keynotes misses it.
8. **Hatch boundary ≠ closed polygon in CAD.** The pavement hatch limit on C-1.0 is one open 1,189 ft
   polyline with spurious connectors. Don't shoelace it; trace or count dots.
9. **Survey "~" items** (CROSSTIE BOARDER ~1' HIGH, BRICK PLANTERS ~8" HIGH, 6' WOOD FENCE on the
   property line) were not taken off. Fences on the line belong to the neighbours.
10. **Spec sections 02 4116 / 02 4119 are missing** from the bound manual. The scope comes from the
    drawings only.
