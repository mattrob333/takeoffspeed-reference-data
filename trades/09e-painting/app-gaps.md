# App gaps: TakeoffSpeed engine and this trade

**Compared against:** `TakeoffSpeed repo: lib/quantities/trades/interiors/painting.ts`, which provides the assemblies `painting.walls`, `painting.ceilings`, `painting.exterior`, `painting.doors-frames` and `painting.mep`. Also compared: the paint output of `partitions.ts` (`paintA`/`paintB` per wall face, stopped at `ceiling`), the PT-7 primer path in `wall-finishes.ts` (`primerTag`), `millwork.ts` `paintLine` (painted trim from millwork LF), and `engine.ts` order rounding.

**How the numbers were produced:** I ran the real engine with `tsx` on this job's inputs (`trades/09e-painting/scripts/engine-run.ts`), in `mode: 'net'` and in `mode: 'order'`.

## What the engine already does right

| Line | Engine record (this job's inputs) | Engine net | Engine order | Estimator |
|---|---|---|---|---|
| 295 PT-1 | 7 × `painting.walls` (one per height group: `walls` LF, `height`) + 1 × `areas 252.6` | 3,710.00 SF | 3,710 | 3,710.84 (−0.02%) |
| 296 PT-4 | 2 × `painting.walls` (5.3 @ 9'-0", 10.6 @ 10'-0") | 153.70 | 154 | 153.62 |
| 297 PT-6 | `painting.walls areas 37.2` | 37.20 | 38 | 40 |
| 298 PT-7 | `painting.walls` 10.3 @ 10'-0" | 103.00 | 103 | 105 |
| 299 PT-8 | `painting.walls` 7.4 @ 10'-0" | 74.00 | 74 | 75 |
| 300 PT-3 | `painting.ceilings surface gypsum, areas 516.1 + 286.2` | 802.30 | 803 | 802 |
| 301 PT-3 exposed | `painting.ceilings surface exposed-structure, areas 98.4` (warns: no surface factor) | 98.40 | 99 | 100 |
| 302 PT-5 | `painting.ceilings surface other, areas 76.2` | 76.20 | 77 | 77 |
| 303 HM frames | `painting.doors-frames frames 3'-0" x 7'-0" × 6` → `3'Wx7'H HOLLOW METAL FRAME` | 6 EA | 6 | 6 |
| 305 diffusers | `painting.mep kind device, count 5, color BLACK` | 5 EA | 5 | 5 |
| 306 3/4" gas | `painting.mep kind pipe, 3/4", 44.2` | 44.20 LF | 45 | 45 |
| 307 1" gas | `painting.mep kind pipe, 1", 9.7` | 9.70 LF | 10 | 10 |

What already matches:
- **Formulas.** Σ LF × H per height group, plus areas carried as is, ceiling SF from areas, frames counted by size, devices EA, and pipe LF. These are exactly the estimator's rules. Given the estimator's readings, **all 12 measured lines land within 0.05% in `net` mode** before rounding, and 7 of them match exactly in `order` mode.
- **Item wording.** The frame item label `3'Wx7'H HOLLOW METAL FRAME - PT-2` matches the estimate's text.
- **Exposed structure.** It is taken at plan area with a warning, which is the right default; the estimator used no factor either.
- **Paint height.** The partition path stops paint at the ceiling height (`ceiling` per wall record), which is the estimator's height rule.

## What it computes differently, ranked by quantity impact

### 1. The partition path paints per partition face, not per room face (largest: about ±20% on 3,711 SF)

When the model reads walls through `metal-framing.partition` records, paint comes from `paintA`/`paintB` on each face, net of openings (`bandArea(..., placed)`), to `ceiling`. The estimator's PT-1 is 339.1 LF of room-face runs at room heights, with **no opening deduction on those runs** (only the A-410 elevation polygons are cut around doors). The engine's own scorecard (`docs/QUANTITY_ENGINE.md`) records **wall paint +21% to +25%** against this estimate on that path. The gap comes from three places:
- faces being double counted where `paintA`/`paintB` are both set on walls whose other face is tile, wallcovering, an exposed room or exterior;
- one `ceiling` per wall record, when a partition between a 9' room and a 12' room needs a different height on each face (`ceiling` is not per face);
- opening deductions the estimator does not take.

**Change.**
- Add `ceilingA`/`ceilingB` (paint height per face).
- Add a `painting.opening-deduct` convention, default `1` (deduct) and `0` under the `reviewed-commercial` profile.
- Steer the prompt to record finish-plan paint runs as `painting.walls` per room face when the finish plan is the source. That is how this estimator measured.

### 2. The tech wall double count and the recess returns (PT-4/PT-6, 37.2 SF, 24% of line 296)

The estimator's PT-4 run includes the PT-6 recess back. It also steps around the recess (10.6 FT against the 9'-9 3/4" wall), so the side returns are already in it at the depth drawn on A-150; only the head and sill returns (about 12.4 SF) are absent. `painting.walls` has `exclude`, but nothing links a PT-6 area to the PT-4 record that contains it.

**Change.** Add an input `insetOf: <tag>` on an area record (or an `exclude` that references another record's tag), so the PT-6 area is deducted from PT-4 automatically. Add `returns` (LF × depth) for recess and reveal returns, with a warning when the wall run already traces the returns in plan. A-704 "PAINT RECESS RETURNS ALL SIDES, PT-4" calls for them.

### 3. Primer-only tags get finish coats (PT-7, 103 SF, plus 106 SF possibly missing)

`painting.walls` takes coats from the reader. If the model copies note G ("ONE COAT PRIMER, TWO COATS PAINT"), PT-7 gets 2 finish coats, when A-170 TYPE = PRIMER and 09 9110 says finish "N/A". Separately, `wall-finishes.wallcovering` with `primerTag: PT-7` already emits a PT-7 primer line (103 SF). If the model also records `painting.walls` for PT-7, the engine sums the two keys separately (`paint-area:PT-7:walls` and `paint-area:PT-7:WALLS`, which differ in case), so **PT-7 is counted twice** (206 SF). This was verified with `trades/09e-painting/scripts/engine-pt7.ts`: the run returns `paint-area:PT-7:walls` 103 SF and `paint-area:PT-7:WALLS` 103 SF, and the shared `primer:PT-7:smooth` key merges to 0.687 gal, twice the single-record 0.343 gal.

**Changes.**
- Make the key case-consistent.
- When a schedule TYPE is PRIMER, force `finishCoats = 0`.
- Warn when a tag appears in both a wallcovering `primerTag` and a `painting.walls` record.
- The Gathering Area `PT-4 / PT-7` double tag (about 106 SF) should become a reading-prompt rule: "a stacked wall tag means both treatments on that wall".

### 4. Rounding differs on small lines (6 lines, 1 to 3 SF each; 2.8 SF on PT-6)

Engine `order` mode rounds SF and LF up to whole units (`WHOLE_UNITS`). The estimator rounds most small hand-entered painting lines up to 5 (F9, 7 of 11 small lines; wallcovering lines 239/240 do not follow it): 37.2→40 where the engine gives 38, 103→105 (engine 103), 74→75 (74), 98.4→100 (99). It keeps raw precision on 3,710.84 and 153.62 (engine 3,710 and 154).

**Change.** Add an optional per-unit convention `rounding.small-line-step` (for example `5` below 150 SF/LF) to a contractor profile. Do not make it the default. The total impact is under 10 SF across the trade.

### 5. Soffit faces are not linked to ceiling paint (286 SF of line 300)

`painting.ceilings` needs the soffit SF typed in as an `area`. The gypsum-board soffit record already computes Σ LF × face height (line 285, 286.04).

**Change.** Have the ceiling and soffit board records emit a `paint-area:<ceilingTag>:CEILING` line when a ceiling `paintTag` is given, the same way the partitions emit wall paint. This prevents the −40% / −14% ceiling-paint misses recorded in `docs/QUANTITY_ENGINE.md` (979.0 SF expected, which is 802 + 100 + 77).

### 6. Opening trim has no painting source (line 304, 910 LF)

The engine paints trim only from `millwork` trim/casing records with `fieldFinished`, under section `TRIM`, item `PAINTED WOOD TRIM (FROM MILLWORK TRIM LF)`. The estimator's 910 LF is an assumed carpentry line (88). This job has no casing drawn, so the engine will rightly produce nothing.

**Change.** None to the formula. Add an `allowance` record kind (LF, `assumed: yes`, confidence low) so a contractor's "assumed trim at openings" can be carried and labelled. Never infer it from openings. If a contractor does want the back-fit rule (2 × Σ opening perimeters, ceil10 = 910 here), it belongs in a profile.

### 7. Substrate and system choices that don't fit this job (gallons only)

- `painting.ceilings` has `surface: gypsum | exposed-structure | other`, and `other` falls back to gypsum rates. PT-5 is on 3/4" plywood, and 09 9110 groups it with steel (semi-gloss enamel).
- `doors-frames` primes frames that 08 1113 ships primed. That matches this estimator's 1P + 2C and 09 9110's HM primer row; 09 9100 3.3.B.2 would allow touch-up priming only, so it is a convention choice.

**Changes.**
- Add `wood` and `metal` to the ceiling surface choices.
- Add an optional `shopPrimed: yes` on `doors-frames` (default off, matching this estimate) to set `primerCoats = 0` or a touch-up fraction.

Neither changes a SF/EA/LF line, only the gallons, which the estimate does not carry.

### 8. Extra lines the estimate does not have (no quantity conflict)

Every area record emits primer and finish **GAL** lines, and `doors-frames` emits a 102 SF paint-area line (6 × 17 LF × 12" girth). These are additive. The comparison scorecard should leave them out of line matching.

## Inputs the engine lacks

| Input | Needed for | Evidence on this job |
|---|---|---|
| Paint height per wall face (`ceilingA` / `ceilingB`) | partitions between rooms of different heights | Work Room 111 (9'-0") shares a wall with Employee Lounge 110 (10'-0") |
| `opening-deduct` convention | estimator does not deduct openings from paint | PT-8 window wall carried at full 7.4 × 10 |
| `insetOf` / linked exclude | PT-6 inside PT-4 | A-704 |
| Recess / reveal `returns` (LF × depth) | PT-4 head/sill returns (side returns already in the run here) | A-704 "PAINT RECESS RETURNS ALL SIDES, PT-4" |
| `finishCoats = 0` forced by schedule TYPE PRIMER | PT-7 | A-170 |
| Ceiling `paintTag` on gypsum ceiling / soffit records | PT-3 = board SF | lines 278 + 285 = 300 |
| `shopPrimed` on frames | primer omission | 08 1113 p214, 09 9100 3.3.B.2 |
| Allowance record | assumed trim | line 88 / 304 |
| Optional small-line rounding step | estimator's ceil5 | F9 |

## Concrete changes, ranked

1. Per-face paint height plus an opening-deduction convention in `partitions.ts` (the recorded +21% to +25% is about 780 to 930 SF on PT-1).
2. Ceiling and soffit board records emit ceiling paint by tag (286 SF of soffit paint, and the ceiling paint misses).
3. Fix the PT-7 key case and the primer-only coat handling, and warn on a duplicate tag between wallcovering and painting (103 SF duplicate risk).
4. `insetOf` and `returns` for recess walls (37 SF of double count).
5. An allowance record for assumed scope (910 LF, labelled rather than invented).
6. Optional `rounding.small-line-step` in a contractor profile (under 10 SF).
7. `wood`/`metal` ceiling surfaces and `shopPrimed` frames (gallons only).
