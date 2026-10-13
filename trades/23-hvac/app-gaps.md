# 23 HVAC — TakeoffSpeed engine vs this estimate

Engine: `TakeoffSpeed repo: lib/quantities/trades/mep/hvac.ts` (18 assemblies, conventions at the
bottom of the file), `shared.ts`, `docs/QUANTITY_ENGINE.md`. Every number below was computed in Python
from the same p53 legend values (`trades/23-hvac/scripts/app.py`).

## What it already does right

- **Surface-area geometry** for rectangular (`L × 2(W+H)/12`) and round (`L × πD/12`) duct is the same as
  the estimator's F1. With the gauge read as 26 and both seam allowances set to 0, `hvac.rect-duct` +
  `hvac.round-duct` give **1,200.28 LBS** (estimate 1,200) and a basis SF line of 1,324.81 (estimate 1,325).
- **Sheet weight table**: `hvac.lb-per-sf-galvanized-26ga = 0.906` is the value the estimator used.
- **Spec gauge wins** when given (`gauge` input), with the table as a fallback only.
- **Air devices** keyed by type + face + tag + neck + CFM (`hvac.air-device`). This is the estimator's
  granularity, so all 21 device lines are reproducible as counts.
- **Equipment, fans, split system, sensors, dampers, hood, misc** as tag counts (`countedAssembly`): lines
  474–494 map one-to-one.
- **Refrigerant without sizes** gives one "LINE SET, SIZE NOT GIVEN" LF line, matching line 452.
- **Allowance** (`hvac.allowance`): 1 LS with the area in the description, low confidence. This matches line 445.
- **Flex**: LF per diameter, net, matches 448–451.

## What it computes differently (ranked by quantity impact)

| # | Gap | Engine today | Estimate | Δ |
|---|---|---|---|---:|
| 1 | Duct insulation basis | `wrap`: `L × (2(W+H) + 8t + 2" lap)/12`; round `L × (π(D+2t) + 2)/12`; +10% waste (`hvac-insulation`) | bare rigid surface, all supply + return, no lap, no waste | t=1.5": 1,721 SF net (+29.9%), 1,893 with waste (+42.9%); t=2.2" (spec): 1,877 (+41.7%), 2,065 (+55.9%) |
| 2 | Gauge when the note is missed | gauge-by-size table: rect ≤12" → 26 ga, ≤30" → 24 ga | M-001 "26 GAUGE FOR ALL SIZES" | gauge alone: 468 lb @26 + 934 lb @24 = 1,402 LBS net (+16.9%) in two lines; with the default seam allowances (row 3) it compounds to 523 + 1,074 = 1,598 LBS (+33.1%) |
| 3 | Seam/joint allowance | `hvac.rect-seam-joint-allowance` 15%, `hvac.round-seam-joint-allowance` 10%; +5% waste (`hvac`) | 0%, no waste | 1,365 LBS net (+13.8%); 1,434 with waste (+19.5%) |
| 4 | Remote cable dampers | `air-device.damper` adds 1 damper per device, split by neck | count of keynote 6 + 7 hexagons, one line | per device: 15 LSD + 7 supply diffusers = 22 vs 13 (+69%), in several lines |
| 5 | RTU condensate drain | `rtu.condensateTrap` adds 1 per RTU | 1 (the estimator missed RTU-1's keynote 2) | 2 vs 1 (+100%). **The engine follows the drawings here; the estimate is short** |
| 6 | Liner split | `insulation: liner` per record; `clearInside` grows the sheet metal by 2t | no liner; all wrap | no change at the estimate's convention; a spec-faithful run moves the return SF from wrap to liner and grows lined sheet metal (23 3100 §1.3.B: +2" each way) |
| 7 | Extra lines with no estimate counterpart | `duct-sf` basis per gauge, transverse joint LF (`hvac.rect-section-ft` 5'), round duct LF + spiral couplings (10' sticks), flex draw bands (4/run), spin-in collars (1/run), curb line when `curb` is set | none (allowance 445 covers them) | extra lines, not a quantity error. They must not be scored as misses, and the curb must not double count roofing line 171 |
| 8 | Refrigerant insulation | added when `insulationThickness` is read (spec 1-1/2" AP Armaflex on suction) | none | extra line equal to the refrigerant LF input: 30.9 LF if fed the legend value, which traces both pipes plus an extra leg; the insulated suction pipe alone is ~11.75 LF of route (formulas.md F4) |

## Inputs the engine lacks

- **A job-level gauge rule.** Today `gauge` is per record, so the model must repeat "26" on every size.
  It needs a project input `ductGaugeRule` read once from the notes (e.g. "rect: 26 all sizes;
  round ≤14 26, 15–26 24"), which every rect/round record inherits.
- **An insulation-area basis convention.** There is no way to say "insulation SF = sheet-metal SF". Add
  `hvac.insulation-area-basis` = `outside` (default, current behaviour) | `sheet-surface`.
- **A system-wide insulation scope.** The estimator wrapped every rigid run, and round runs only get an
  insulation line if the record says so. A per-trade "insulate all rigid duct" flag would avoid 12
  per-record settings.
- **Keynote-tag counting for dampers.** `hvac.damper` takes a count, but nothing tells the model to
  count keynote hexagons rather than devices. Add a `countBasis` = `keynote-tags` | `per-device` read
  hint.
- **Rounding.** The estimate rounds LBS and SF to a whole unit (1,200.28 → 1,200; 1,324.81 → 1,325);
  whether the shop rounds LBS to 100 cannot be told from this job. The engine has no per-line purchase rounding
  for these, which is fine for scoring at ±0.5%.

## Concrete changes

1. Add to `QUANTITY_PROFILES['reviewed-commercial']` (`lib/quantities/profiles.ts`):
   `'hvac.rect-seam-joint-allowance': '0'`, `'hvac.round-seam-joint-allowance': '0'`,
   `'hvac.wrap-lap-in': '0'`, and the new `'hvac.insulation-area-basis': 'sheet-surface'`. With
   `mode: 'net'` this reproduces lines 446 and 447 within 0.03% (fixtures in `fixtures.json`).
2. In `insulationOf`/the wrap branch of `rectDuct` and `roundDuct`, when the basis is `sheet-surface`, use
   `sf` (the sheet surface already computed) instead of `L × (outside + lap)/12`. That is a 2-line change.
3. Add the read instruction to the `gauge` input: "Read the duct construction note first (M-001 type
   'RECTANGULAR DUCT: 26 GAUGE FOR ALL SIZES'). When it exists, give that gauge on every record. Use
   the table only when no note or spec table exists." This removes the +17% failure mode (+33% with the default seam allowances).
4. Add a `countBasis` read hint to `hvac.damper` and to `air-device.damper`: when a keynote calls for a
   damper, count the keynote tags and do not attach a damper per device.
5. Keep `rtu.condensateTrap` per RTU (the drawings support 2). Flag the estimate's 1 as an estimator
   miss in the scorecard, not as an engine error.
6. Curb lines: default `curb` to absent for RTUs when a roofing curb line exists on the same job, to avoid
   double counting line 171.
7. Mark the `duct-sf`, joint-sealing, spiral-coupling, flex-strap and collar lines as "inside allowance"
   in the scorecard, so they are not counted as unmatched lines against this estimate.
