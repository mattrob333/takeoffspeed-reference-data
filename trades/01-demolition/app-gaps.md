# 01 — Demolition: TakeoffSpeed engine gaps

Compared against `TakeoffSpeed repo: lib/quantities/trades/site/demolition.ts` (10 assemblies:
building, pavement, curb, utility, linear, trees, feature, selective, sawcut, abatement), its 3
conventions, and `lib/quantities/profiles.ts`.

## What it already does right

- **The assembly set covers all 14 lines.** Building → lines 3–4. Pavement → 5, 7, 9 (and `stairSteps` →
  line 8). Curb → 2. Utility → 11, 12, 14 (with `structures` → 15). Linear → 13. Trees → 10.
  Feature → 6.
- **Item text** follows the keynote style of this estimate (`${keynote}: REMOVE EXISTING …`), including
  `W/ PAVEMENT STRIPING` via `incidentals`, `- ASSUMED` via `assumed`, and `REMOVE EXISTING STORM
  STRUCTURE` via `structureType`.
- **No waste** on removal lines (`wasteClass: null`), and no debris CY unless `haulDebris`. That matches
  this estimate, which has no haul line in this trade.
- **Measured lines are a plain Σ of runs or areas**, the same rule the estimator used. With the legend
  inputs from `fixtures.json` (its `engineInputs` strings) the engine reproduces lines 2, 5–15 exactly
  and lines 3–4 within 0.02%: all 14 `expectedLines` pass (checked by running `expandMeasurements` on
  the 12 fixtures). Line 8 only comes out of the ramp record (`stairSteps` on `demolition.pavement`,
  which requires `description` and `areas`), and line 15 only out of the storm record (`structures` on
  `demolition.utility`, which requires `utility` and `runs`).

## What it computes differently (ranked by quantity impact)

| # | Item | Engine | Estimator | Impact |
|---|---|---|---|---|
| 1 | Building volume with `stories` only | `demolition.story-height-ft` default **12 ft** → 4,489.1 × 2 × 12 = 107,738.4 CF; 1,713.7 × 12 = 20,564.4 CF | 10 ft/storey → 89,780 / 17,140 | **+20.0%** on both lines, +21,383 CF total. The engine also caps confidence to low and warns, which is correct. |
| 2 | Volume rounding | Exact: 89,782 / 17,137 CF | Nearest 10 CF: 89,780 / 17,140 | +0.002% / −0.018%. Cosmetic. |
| 3 | Handrail without keynote | `linear` appends `(ASSUMED)` and caps confidence at medium | Plain "REMOVE EXISTING METAL HANDRAIL" | Label only. The quantity is identical. |
| 4 | Stair steps label | `REMOVE EXISTING STAIR STEPS` | `REMOVE EXISTING BRICK STAIR STEPS` | Label only. There is no material input. |
| 5 | Trees label | `REMOVE EXISTING TREE (SIZE NOT SHOWN)` | `REMOVE EXISTING TREES/VEGETATION` | Label only. |
| 6 | Building label | `2: REMOVE EXISTING 2 STORY BUILDING STRUCTURE AND FOUNDATION — 4,489.1 SF FOOTPRINT × 20' H` (numeral storey count plus a footprint × height suffix) | `2: REMOVE EXISTING TWO STORY BUILDING STRUCTURE AND FOUNDATION` | Label only. `tests/quantities/site-demolition.test.ts` asserts the `2 STORY` form. |
| 7 | Storm line label | `4: REMOVE EXISTING 15" HDPE STORM SEWER LINE AND ASSOCIATED STRUCTURES - ASSUMED` (size and material from the inputs) | `4: REMOVE EXISTING STORM SEWER LINE AND ASSOCIATED STRUCTURES - ASSUMED` | Label only. |

## Inputs the engine lacks

1. **Storey height per house profile.** The `reviewed-commercial` profile in `profiles.ts` has no
   demolition entry. Add `'demolition.story-height-ft': '10'`, computed from this job (89,780 / 4,489.1 /
   2 = 9.9998 ft; 17,140 / 1,713.7 = 10.0018 ft).
2. **Volume rounding convention.** Add `demolition.building-cf-round` (e.g. `10`) so profiles can round
   to the nearest 10 CF.
3. **Utility grouping.** The estimator lumps OHP, UGP and TEL into the KN5 "POWER" line (965.4 LF ≈ 194
   ticks × 5 ft). The `utility` assembly records one system per keynote, so a linetype-driven reader
   would split TEL out. Add an input `includesLinetypes` (e.g. `["OHP","UGP","TEL"]`) so the line
   documents what it covers, and let the record follow the keynote, not the linetype label.
4. **Stair material.** Add a `stairMaterial` text on `pavement` (or a separate `stair` count assembly) to
   produce "BRICK STAIR STEPS".
5. **CAD-native cross-checks.** The reader has no tick-count or dot-hatch helper. The measurements are
   reproducible from the PDF vectors:
   - `LF ≈ ticks × pitch`: 5.0 ft per `///` glyph, 2.0 ft per `++++` crossing tick at 1" = 20'.
   - `LF = length of the linetype polylines`, chained in drawing order (not by shared endpoints, which
     merges the utility and curb linetypes where they cross).
   - `SF ≈ dots × pitchX × pitchY`: 4.34 SF per dot here.
   - `SF = shoelace of the outline`, closed along the building outline in path order.

   On this job the estimator sits −2.1% to +2.6% from these checks on every measured line except the
   ramp (+6.0% over its CAD outline). They would let the engine flag a traced quantity that is off by
   more than about 3%, which here would correctly flag the ramp for review.
6. **Unkeyed-but-ticked scope.** The `///` GAS line (87.1 LF, 17 ticks) has no keynote and no
   estimate line. The engine should surface ticked linework with no keynote as a review flag (no quantity
   line, per the no-invented-data rule), alongside the existing `(ASSUMED)` mechanism.
7. **Saw cut from the general notes.** C-1.0 GDN 3 and C-0.1 require a full-depth saw cut at the
   limits. The estimate has no LF, and the engine only produces one if `sawcut` runs are given. Add a
   reader prompt: "notes require saw cut → measure the limits where pavement remains."

## Concrete changes, ranked by quantity impact

1. `profiles.ts` → `reviewed-commercial.conventions['demolition.story-height-ft'] = '10'`. This fixes
   +21,383 CF (+20%) on lines 3–4.
2. Add the convention `demolition.building-cf-round` (default `0` = exact; profile `10`). Lines 3–4 then
   match to 0.000%.
3. `utility`: an optional `includesLinetypes` input and a reader rule that the keynote decides the
   record. This protects line 12 (965 LF) from being split or under-read.
4. A review flag for ticked utility linework with no keynote (gas, 87.1 LF), and for notes that
   require a saw cut with no `sawcut` record.
5. Label tweaks: an optional `stairMaterial`; `trees` taking an optional `label` ("TREES/VEGETATION");
   and in `linear`, only append `(ASSUMED)` when the feature is not labelled on the survey.
6. Tests: add `fixtures.json` from this folder to `tests/quantities/site-demolition.test.ts` as a
   golden for this job: 12 records with 14 `expectedLines`, tolerances 0–0.5% (0.1% on the CFT lines).
   The test harness passes inputs as strings, so feed `engineInputs` (`"442.4 SF"`, `"987.2 LF"`,
   `"10'"`, `"7"`, `"yes"`), not the `{value, unit}` objects in `inputs`, and match lines by `key`.
