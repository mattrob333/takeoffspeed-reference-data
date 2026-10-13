# App gaps: TakeoffSpeed flooring engine vs. this estimator

Code compared:

- `TakeoffSpeed repo: lib/quantities/trades/interiors/flooring.ts`: assemblies carpet-tile, broadloom, resilient, sheet, tile, base, transition, floor-prep, sealer, mat, stair; `settingLines`; `trimLine`.
- the trims and grout that `wall-finishes.ts` routes into flooring.
- `engine.ts` `finalizeLines`, which merges by key and then applies waste and purchase.
- `docs/QUANTITY_ENGINE.md`, including the W7 finishes run.

The engine was not edited.

All comparisons below are in `mode: 'net'`. In `mode: 'order'` the engine adds class waste: tile 10%, carpet tile 5%, resilient 5%, base 5% and trim 10%. The estimator carried none of that on these lines. For example, FT-1 would come out at 1040.72 SF in order mode against the estimator's 946.11.

## What the engine already does right

| Estimator practice (this job) | Engine | Lines |
|---|---|---|
| One SF line per floor finish tag, net polygon area | `flooring.tile`, `flooring.carpet-tile`, `flooring.resilient`, `flooring.sealer` each emit `<kind>:<TAG>` in SF from `measureArea` (rooms, irregular areas, `deduct`) | 217–223 |
| Field net of inset tags (diamond carpets) and of the mat on the concrete | the `deduct` input in `AREA_INPUTS` | 217, 218 |
| Grout carried as **SF of tile served**, keyed by grout tag, with floor and wall tile merged under one tag | `settingLines` emits `grout-area:<GR-n>` with net = tile SF. Records sharing a groutTag merge in `finalizeLines`. | 225, 226 |
| Base LF by tag = traced runs − doors + returns | `flooring.base` (walls / rooms / doorWidths / returns); `material: tile` covers WT-8 (Women's east wall 7.29 + Men's west wall net of door 115, 3.89) | 227, 228 |
| Transition LF by tag = door widths + open boundaries; no waste in net mode | `flooring.transition` (doors, boundaries) and `trimLine` | 229–232 |
| Schluter top trim = band top edge less full-band openings | `wall-finishes` `topEdge` → `tile-edge-trim`: band walls B + C + D net of door from the A-410 plan dimensions, 39.75 against 39.55 (+0.51%) | 234 |
| Waste, attic stock and purchase units kept apart from the net quantity | `mode: 'net'` vs `'order'`; waste classes; `purchase` | all |

## What it computes differently (with this job's numbers)

| # | Line | Estimator | Engine (net) | Δ | Cause |
|---|---|---:|---:|---:|---|
| 1 | 225 GR-1 grout | 1050 SF | 946.11 SF (984.53 if WT-3 is also given groutTag GR-1, as A-170 says) | −9.9% (−6.2%) | `grout-area` has `wasteClass: null` and no round-up. The estimator uses ceil50(1.10 × tile SF). |
| 2 | 226 GR-3 grout | 300 SF | 244.13 SF | −18.6% | same cause |
| 3 | 233 Schluter cove trim | 51.87 LF | 39.75 LF (`tile-cove-trim` = band L − full-band doors) | −23.4% (−12.12 LF) | The engine puts cove only under the tile band. The estimator also ran it along the two WT-8 bullnose-base side walls (Men's west net of door 115, Women's east full): both restroom perimeters net of three doors = 52.10 LF (+0.45%). |
| 4 | 224 MT-1 mat | 10.0 SF | 12.0 SF (`flooring.mat`: 1 × 36"x48") | +20% | The estimator's number is a judgment. The drawn mat is 6 SF. |
| 5 | 232 FTS-4 | 10.02 LF | 14.0 LF if derived from the scheduled mat size; 10.0 if `boundaries: [2, 3, 2, 3]` is traced | +40% / 0% | `flooring.mat` has a perimeter output only as `mat-frame:<tag>` (2 × (W + H) × count, when `recessedFrame` is set), not as `transition:<FTS-n>`, so the ramp edge does not land on the FTS-4 line. With the scheduled size, mat and ramp disagree with the drawing. |
| 6 | 217 CON-1 | 68.78 SF | correct only if the mat footprint is given as `deduct` (6 SF). Otherwise 74.79 SF. | +8.7% if missed | The mat does not deduct itself from the floor beneath it. |
| 7 | Grout material (not an estimate line) | — | 85.6 lb (3.42 × 25 lb bags) with the default 1/8" joint, against 169.8 lb (6.79 bags) with the spec's 1/4" joint (09 3000 3.3.F) | ×2 | The convention `flooring.grout-joint-in` = 1/8" ignores the project spec default. Also, GR-1 and GR-3 are **epoxy**: the 112 lb/CF cementitious density and 25 lb bags do not apply. Epoxy is sold in kits. |
| 8 | 230 FTS-2, 231 FTS-3 | 28.99, 12.24 | match when the boundaries and doors are given | — | FTS-3 at exterior doors (F004) is only caught if the reader follows the estimator's practice, not the schedule definition (see reading-guide §6). |

The W7 run (`QUANTITY_ENGINE.md`, "Ceilings and finishes") shows that this trade's misses are mostly **reading** misses, not formula misses:

| Item | W7 result | Absolute |
|---|---:|---:|
| FT-1 | +5% | +47.3 SF |
| CR-1/2/3 | −11% | −65.4 SF |
| CR-4 | +48% | +39.6 SF |
| LVT-1 | +45% | +42.3 SF |
| sealed concrete | +14% | +9.6 SF |
| rubber base | −18% | −72.8 LF |
| transitions | +19% | +19.6 LF |

Each of these items has a formula that matches the estimator once the polygons are read correctly (the 15 measured lines above). The gap is in turning finish-plan polygons into records.

## Inputs the engine lacks

1. **Grout-area allowance and round-up.** Nothing turns 946.11 SF into a grout order area.
2. **Mat drawn size and mat edge transition.** `flooring.mat` takes `size`, `count` and `recessedFrame`. With `recessedFrame` it emits a `mat-frame:<tag>` line of 2 × (W + H) × count LF, but that is a recessed-frame line, not a `transition:<FTS-n>` line, so it cannot carry the surface-mat ramp edge (FTS-4). It also cannot record the drawn outline or deduct itself from the host floor.
3. **Cove trim on base walls.** `wall-finishes` `coveTrim` covers band walls only. `flooring.base` with `material: tile` has no cove-trim output.
4. **Spec joint width.** No input reads "Unless otherwise indicated, install tile with 1/4 inch joint widths". The convention default of 1/8" wins silently.
5. **Grout type.** There is no epoxy/cementitious choice. Epoxy (ANSI A118.3) is bought in kits by coverage.
6. **Attic stock.** No assembly emits the spec's attic-stock line. On this job it is 10% for tile (94.61 SF FT-1), carpet tile (67.65 SF), resilient tile (9.40 SF LVT) and base (40.47 LF WB-1).
7. **Cement-board underlayment tied to a transition detail.** `flooring.floor-prep` has self-leveling, patch, moisture-mitigation, grind and shot-blast, but no 1/4" cement board. FTS-2 and FTS-4 call for it: 93.95 + 6.0 = 99.95 SF (or 105.95 SF with the scheduled mat).
8. **"Float slab 3'-0"" at FTS-1** (detail 1). This is a self-leveling strip of 3'-0" width × FTS-1 LF. It needs a `strip` area input (width × LF).
9. **Base style split.** Spec 09 6513 asks Style A straight at carpet and Style B cove at resilient. `flooring.base` has a single `material`/`height` and no style. The estimator did not split either, so this has no line impact here, but it would matter for purchase.

## Concrete changes, ranked by quantity impact on this job

1. **Grout-area order rule (+159.8 SF across lines 225 and 226).**
   - Give `grout-area:<tag>` a waste class `flooring.grout-area`, default 10% (basis: spec 09 3000 1.2.E and the estimator's fit).
   - Add a line-level `roundUpTo` of 50 SF, applied after merging, in `finalizeLines`.
   - Order mode then gives exactly 1050 and 300.
   - Keep net mode at the tile SF.
   - Document it as an estimator convention fitted from two lines, not a published rule.
2. **Cove trim along tile-base walls (+12.35 LF, line 233).**
   - Add `coveTrim: yes` to `flooring.base` when `material: tile`, emitting `tile-cove-trim` = base LF (it merges with the wall-finishes cove line by key).
   - With the WT-8 walls by plan dimensions (Men's west 7.677 − 3.0 door 115, Women's east 7.677, = 12.35) the engine gets 39.75 + 12.35 = 52.10 LF (+0.45%). Feeding the measured WT-8 runs (11.28) instead gives 51.03 LF (−1.6%).
3. **Mat assembly links (CON-1 ±6 SF, FTS-4 ±4 LF, MT-1 ±2 to 6 SF).**
   - Add `drawnSize` and warn when it differs from `size`.
   - Add `hostTag` to emit a negative area onto the host floor tag (`sealer:CON-1`).
   - Add `edgeTransitionTag` to emit `transition:<FTS-n>` = 2 × (W + L) × count (the same perimeter the `recessedFrame` option already computes for `mat-frame:<tag>`, keyed to the transition tag instead).
   - Default to the scheduled size, but print both sizes. On this job that is 12 SF / 14 LF against the drawn 6 SF / 10 LF and the estimator's 10 SF / 10.02 LF.
4. **Spec joint width and epoxy grout (grout material ×2).**
   - Add a `specJointIn` override that the project spec sets once (1/4" here). The warning should then cite the spec, not the convention.
   - Add `groutType: epoxy | cementitious`. For epoxy, output kits = ceil(net SF × (1 + loss) ÷ kit coverage), with kit coverage taken from product data. Without it, leave the quantity in SF and flag.
5. **Cement-board underlayment prep type (+99.95 SF of new scope).**
   - Add `prepType: cement-board` with thickness. Bind it to transition details that call for it (FTS-2, FTS-4).
6. **Attic stock lines (+94.61 SF tile, +67.65 SF carpet, +9.40 SF LVT, +40.47 LF base).**
   - Add `atticStockPct` per assembly from the spec, emitted as a separate `attic-stock:<tag>` line with no waste.
   - The estimator omitted these, so they must not count against the reconciliation. They are scope the spec requires.
7. **Float-slab strip at FTS-1** (51.63 LF × 3'-0" ≈ 154.9 SF of leveling, new scope). Add a `strips` input to `floor-prep`: width × LF.
8. **Names.** Pass the schedule product through to item text:
   - `SCHLUTER JOLLY J AE` instead of `METAL TILE EDGE TRIM`
   - `SCHLUTER DILEX-AHK 1S AE` instead of `METAL COVE PROFILE`
   - `SCHLUTER RENO-RAMP AERP` on FTS-4
   - LVT-1 as metric plank 2.691 SF/pc
   This has no quantity impact but makes the lines match the estimate.

## Fixture coverage

`fixtures.json` has 17 cases, one per reproducible line. MAT-1 is excluded as judgment. They use these formula ids: `tagArea`, `rectArea`, `groutAreaRoundUp`, `tracedRun`, `boundaryRun`, `perimeter`, `bandTopEdge`.

- `tagArea` and `tracedRun` map to existing engine inputs: `areas` and `walls` / `boundaries`.
- `groutAreaRoundUp` needs change 1.
- `perimeter` needs change 3, or the user tracing `boundaries`.
- `bandTopEdge` maps to the wall-finishes `topEdge`.
