# App gaps: 32a paving, marking, signs, bike racks, bollards

**Engine modules compared:**

- `lib/quantities/trades/site/site-paving.ts`: asphalt, concrete, sidewalk, curb-ramp, curb
- `lib/quantities/trades/site/pavement-marking.ts`: stripe, parking-stalls, access-aisle, crosswalk, symbol, sign
- `lib/quantities/trades/site/site-improvements.ts`: bollard, bike-rack
- `lib/quantities/trades/site/shared.ts`: `pierFootingLines`, `circleSF`

**How the comparison was run.** Each line was fed to the engine with this job's measured inputs: `trades/32a-paving-marking/scripts/run-engine.ts` with `npx tsx`, run record by record (`engine-out.txt`) and all together (`engine-out-combined.txt`). Mode `net`, no waste.

## What it already does right

| Line(s) | Engine result | Estimate |
|---|---|---|
| 633 / 632 asphalt SF by duty | 11,367.3 / 2,459.18 SF (`site-paving.asphalt`, `asphalt-pavement:HEAVY` / `:STANDARD`) | exact |
| 634 concrete pavement, two areas in one record | 747.6 SF | 748 (only the ceiling differs, see gap 6) |
| 635 sidewalk SF | 1,834.7 | 1,835 (ceiling) |
| 638 curb LF | 993.9 | 994 (ceiling) |
| 642 SSWL / 646 stop bar with measured runs | 441.31 / 49.58 LF | exact |
| 645, 647, 648, 649, 650 symbols and signs | 1, 2, 1, 3, 2 EA; R7-8P5 plaque line produced | exact |
| 659 bike racks, 660 footing count | 2 EA; `footingsPerRack` 2 → 4 footings | exact |
| 674 / 713 bollard EA, with separate footing keys per diameter × height | 5 / 8 EA | exact |
| Pier excavation and haul-off logic | buried depth only; haul-off = excavation; no backfill | same as estimate |

- The `assumed` flag on asphalt and concrete caps confidence and appends "- ASSUMED DETAILS", the same wording the estimator used.

## What it computes differently, ranked by quantity impact

| # | Gap | Line(s) | Engine | Estimate | Δ |
|---|---|---|---|---|---|
| 1 | **Crosswalk unit.** `crosswalk` reports the crossing length (C × n), not the traced linework. | 643 | 22.5 LF | 79.46 LF | **−71.7%** |
| 2 | **ADA hatch from the default spacing.** `access-aisle` computes W×L/spacing, with a default 36" spacing; there is no way to pass the measured LF. | 644 | 30.0 LF | 97.48 LF | **−69.2%** |
| 3 | **Crosswalk sub-stripes merge into the SSWL and stop-bar lines.** `stripeLine` keys only on width/color/pattern, so the crosswalk's 45 LF of 4" edges joins `stripe:1/3:WHITE` and its 20 LF of 24" bars joins the stop bar `stripe:2:WHITE`. | 642, 646 | 486.31 LF / 69.58 LF | 441.31 / 49.58 | **+10.2% / +40.3%** |
| 4 | **Expansion joints need centerline runs.** An area-only sidewalk gets *no* expansion-joint line (warning "expansion spacing needs walk runs"). With runs it counts ceil(run/25) − 1 per run, which undercounts. | 636 | 0 LF (area only); 70.0 LF with one 366.94' × 5' run | 73.4 LF | **−100% / −4.6%** |
| 5 | **Ramp count comes from the number of area entries.** One measured total (113.3 SF) yields "NO. OF CURB RAMPS 1". C-3.0 tags keynote 6 twice. | 637 | 1 EA (count line) | 2 ramps (description) | −50% on the count |
| 6 | **No ceiling rounding.** The estimator rounds concrete flatwork, ramp and curb up to a whole unit. | 634, 635, 637, 638 | 747.6 / 1,834.7 / 113.3 / 993.9 | 748 / 1,835 / 114 / 994 | −0.05% / −0.02% / **−0.61%** / −0.01% |
| 7 | **Exact π for pier area.** The estimator uses r2(π/4·r2(D)²). | 660–662, 675–677, 714–716 | 0.116355 / 0.775702 / 1.654831 CY | 0.117037 / 0.772222 / 1.647407 | −0.58% / +0.45% / +0.45% |
| 8 | **Bollard excavation and haul-off keys collide across groups.** `bollard:excavation` and `bollard:hauloff` do not include diameter, height or location, so the dumpster and drive-thru groups merge, and both land in section `BOLLARDS`. | 676/677, 715/716 | one line, 2.4305 CY each | 0.772 + 1.647 CY, in separate sections | grouping error (the total matches within 0.45%) |
| 9 | **Extra lines the estimate does not carry.** Bollard concrete fill (0.1858 / 0.2378 CY, from the exposed height only, with a warning); a sign-post EA line; asphalt course SY, subbase CY, tack GAL and geotextile SY lines; concrete CY for walk, curb and ramp. | n/a | extra | n/a | not wrong, but must be kept apart when scoring against this estimate |

## Inputs the engine lacks

1. **`measuredRuns` on `crosswalk` and `access-aisle`.** This would accept the PlanSwift traced LF as the reported line, with the geometry-derived bars and hatch used only for paint SF. Without it, gaps 1 and 2 cannot close.
2. **`expansionSpacing` that works from area.** Rule: `LF = SF / spacing`, plus abutments × width plus along-joints. This is exact for transverse joints across a constant-width walk, and it is what the estimator did (1,835 / 25 = 73.4).
3. **`rampCount` on `curb-ramp`,** independent of how many area entries are given. Alternatively, count the keynote tags.
4. **`rounding` per line:** `'none' | 'ceil-unit' | 'nearest'`. Default `ceil-unit` for concrete flatwork, ramp and curb, and `none` for asphalt and marking, to match this estimator's profile (`profiles.ts`).
5. **`circleAreaRounding`** convention (`exact` | `2dp`) in `pierFootingLines`. It belongs in the profile, because it is the estimator's habit and not a physical rule (see 32b, which has the same pattern).
6. **Location / served group on bollard records** (DUMPSTER ENCLOSURE vs DRIVE THRU ISLAND). It should go into both the keys and the sections, so that the excavation and haul-off stay per group, as in the estimate.
7. **`geotechSection` on asphalt and concrete.** This would let the engine warn when the assumed stack differs from the geotechnical recommendation. On this job the geotech report is not an outside source: the C-3.0 Pavement Legend references it for both pavement types ("SEE GEOTECH REPORT BY TERRACON, DATED 05.04.2026"), while the keynotes point to C-6.2, which has no section. Here the assumed asphalt totals 8-1/2" against 3" heavy duty and 4-1/2" against 2" standard duty, and the aggregate is 12" against 8"/6" GAB. That would swing any tonnage line by more than 100%.
8. **A `parkingLot` flag on `symbol` (arrows),** so the size can be halved where the detail says "REDUCE DIMENSIONS SHOWN BY 50% FOR PARKING LOTS AND DRIVES". This affects paint SF only.

## Concrete changes, ranked by quantity impact

1. **crosswalk / access-aisle:** add a `measuredRuns` input. When it is present, report `LF = Σ measuredRuns` as the item line. Fixtures: 643 expects 79.46, 644 expects 97.48. *(Gaps 1 and 2: −72% and −69%.)*
2. **stripeLine key:** include the source assembly or purpose (`stop-bar`, `crosswalk-bar`, `crosswalk-edge`, `lane`) in the key and the item text, so crosswalk bars and edges stop merging into the SSWL and stop-bar lines. Also add a `purpose: stop-bar` choice to `stripe` that yields the item "24" WHITE STOP BAR". *(Gap 3: +10% / +40%.)*
3. **sidewalk:** when `expansionSpacing` is given without `runs`, compute `LF = SF / spacing` and record the rule in `steps`. When runs are given, use `run / spacing` (not ceil − 1) for parity with the estimator, or expose both. Fixture: 636 expects 73.4. *(Gap 4.)*
4. **curb-ramp:** add a `rampCount` input that overrides the count of areas; warn when the keynote tag count differs from the area entries. *(Gap 5.)*
5. **profiles.ts:** add an estimator profile with `rounding: ceil-unit` for `site-paving.concrete`, `site-paving.sidewalk`, `site-paving.curb-ramp` and `site-paving.curb`, and `circleAreaRounding: 2dp` for `pierFootingLines`. Fixtures 634/635/637/638/660/675/714 then reproduce exactly. *(Gaps 6 and 7: ≤ 0.6%.)*
6. **bollard:** add `location` to the record, and fold it into `keyBase` (`bollard:${location}`) and into the section (`${location} > BOLLARDS`). *(Gap 8.)*
7. **Cross-sheet count check:** when a bollard (or any counted item) is recorded from a site plan *and* an enlarged plan exists, warn if the counts differ. This job: C-3.0 has 5 and A-190 floor plan 4 has 6. One more 16" × 3'-0" pier adds 0.154 CY of concrete, excavation and haul-off each, and the EA rises 20%.
8. **Asphalt:** add a `geotechSection` cross-check warning (see input 7).
9. **Symbol:** add the `parkingLot` halving and the ft-in size formatting (3'-8" x 9'-4" instead of 3.667'x9.333'). This is cosmetic, plus paint SF.

Fixtures for each of these are in `fixtures.json` (28 cases, one per estimate line), with the estimator's rounding stated as explicit inputs.
