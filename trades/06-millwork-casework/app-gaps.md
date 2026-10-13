# App gaps — TakeoffSpeed quantity engine vs this job's millwork takeoff

Compared module: `TakeoffSpeed repo: lib/quantities/trades/fitout/millwork.ts` (assemblies `millwork.cabinet-run`,
`countertop`, `shelving`, `laminate-face`, `paneling`, `built-unit`, `accessory`, `backing`; helpers in `fitout/shared.ts`; waste and
rounding in `engine.ts finalizeLines`). The engine was **not edited**. This job's 48 lines were fed to it as 50 measurement records from
the printed dimensions (harness: `trades/06-millwork-casework/scripts/app/run.ts`, output `app/run.out`).

## Score

| Mode | Lines within 1% of the estimate | Within 5% | Failures |
|---|---|---|---|
| `net` (measured quantities) | **31 / 48** | **41 / 48** | line 126 record rejected; 116 −44.7%; 344 −10.1%; 109 −12.5%; 141 −8.3%; 137 −7.3%; 102 −6.2% |
| `order` (default: waste + whole-unit rounding) | 19 / 48 | 23 / 48 | every fractional cabinet/area line rounded up; laminate +15%, panelling +10% |

Lines 102, 109, 139, 141 and 142 differ because the engine computes the printed value and the estimator rounded a PlanSwift reading
(see `formulas.md`); line 116 differs because the estimator's legend polygon is defective (cased opening and title block traced).
Those are estimator conventions or legend defects, not engine errors. (Re-run 2026-10-13 after the verification fixes below.)

## What it already does right

* **Cabinets (F1):** `cabinet-run` with `modules` reproduces all 18 cabinet lines in net mode: 72.0 LF vs the estimator's 72.49 LF
  (−0.7%); the line split (room × category × depth × height × config × finish) matches the estimator's sub-sections one-for-one, and the
  box count stays in the description instead of becoming a second EA line.
* **Shelving (F5):** `runs × shelves` gives 19.375 (library), 15.5625 (night drop), 6.0, 4.0 exactly.
* **Tops (F2):** `runs × depth − corners × depth²` gives 17.333, 10.667, 18.056, 19.667, 5.25, 11.0.
* **Backsplash as LF (F4)**, with the splash face SF kept out of the quantity lines (steps only).
* **Booth panelling (F7):** faces/areas → 309.03 SF walls, 64.06 SF ceiling; **reveal in LF** (89.08) — the estimator's "SF" unit is wrong and
  the engine's LF is right.
* **Built units and accessories (F9):** check desk, locker, table, seats, pencil drawer, both grommet models — all exact counts.
* **Laminate faces by tag (F6):** PL-4 38.397, PL-3 6.565 and library PL-1 53.06 SF from `faces` exactly.

## What it computes differently, ranked by quantity impact

| # | Gap | This job (numbers) | Impact |
|---|---|---|---|
| 1 | **Order mode adds waste to fabricated finish faces and panels.** `laminate-face` carries waste class `millwork-laminate` 15%, `paneling` and its reveals/Z-clips `millwork-paneling` 10%. The estimator carries these as net fabricated surfaces. | PL faces 186.9 → **218 SF** (+31 SF, +17%); booth walls 309.03 → **340 SF**; ceiling 64.06 → **71 SF**; reveal 89.08 → **98 LF** (estimate 300 / 64 / 90) | ≈ +69 SF, +9 LF |
| 2 | **Order mode rounds every LF/SF line up to a whole unit** (`WHOLE_UNITS` includes LF and SF), including fabricated cabinets with `wasteClass: null`. | cabinet LF 72.0 → **80 LF** (+11%): 2.167 → 3, 1.25 → 2, 1.5 → 2, 3.833 → 4, 0.875 → 1, 5.25 → 6… | +8 LF over 18 lines |
| 3 | **Solid-surface tops cannot be entered the way they are drawn or carried.** `countertop` has one `depth` per record (the transaction bar is a 2'-11½"-deep bar with a 2'-0"-wide return), no `areas` input for irregular tops, and waterfalls always go to a separate `WATERFALL END PANEL` line. The estimator carries tops + waterfall faces as one SF line (111.14). | app 18.06 + 19.67 + 33.90 top + 28.33 waterfall = **99.95 SF** (−10.1%; −11.2 SF), on two lines | −11 SF and a split line |
| 4 | **Z-clip extrusion and shelf hardware lines the estimator does not carry.** `paneling` with `attachment = z-clips` emits `ALUMINUM Z-CLIP EXTRUSION` = rows × runs × 2 (applied to 9" jamb faces too); `shelving` emits brackets/standards at the 32" convention when no spacing is given. | +402 LF Z-clip (443 order); +12 brackets + 4 standards (janitor, 24" from note), +8 KV 180 brackets (work room, 32" convention warning) | extra lines (not wrong; label as derived accessories) |
| 5 | **Spec-driven grommet count missing.** 12 3669 2.3.A.1: "1 grommet per every 4 feet of countertop". | per top ceil(15.31/4)+ceil(8.67/4)+ceil(9.83/4) = **10 EA** (9 job-wide); not in the estimate either | +9–10 EA |
| 6 | **Stepped top in one record.** Work-room top 1 has a 9⅜" × 10¼" stub at a shallower depth. | app 11.125 vs 11.792 SF (−5.7%) unless a second record is made | −0.67 SF |
| 7 | **Apron-only record is rejected.** The removable MDF knee panel (`apronRuns`/`apronHeight`) only exists inside `paneling`, which throws "give runs × height or areas" when there is no panel area. | line 126 (2.708 LF) produces **no line** | −2.7 LF (a whole line lost) |
| 8 | **No responsibility on millwork assemblies.** General Note K makes all millwork owner-vendor furnished, GC-installed; `cabinet-run`, `countertop`, `built-unit`, `accessory` have no `RESPONSIBILITY_INPUTS` (the furnishings modules do). | all 48 lines carry no OFCI flag | scope, not quantity |
| 9 | **Locker double count not flagged.** Millwork line 123 (employee locker) and furnishings line 367 (LK-01 lockers, by furniture vendor) are the same item. | 1 EA twice | 1 EA |

## Inputs the engine lacks

* `countertop.areas` (printed/traced SF for irregular tops) and per-leg `depth` (or `legs = L x D` pairs).
* `countertop.mergeWaterfalls` (flag) — carry waterfall faces in the top line, as this estimator (and the SLD-1 legend) did.
* `countertop.grommetsPerLF` / spec rule `12 3669 2.3.A.1` → `ceil(top LF / 4)` EA, black 2" OD.
* A standalone `millwork.apron` (or allow `paneling` with only `apronRuns`).
* Responsibility inputs (`responsibility`, `furnishedBy`, `installedBy`) on all millwork assemblies.
* `laminate-face.sameAs` (re-use another face — the PL-4 staff face = WT-3 tile face) is optional; `faces` already covers it.
* Rounding display option: `round = none | half-up | whole-up` per line to mirror an estimator's convention without changing net.

## Concrete changes (in order)

1. In `finalizeLines`, do not apply whole-unit rounding to lines whose `wasteClass` is `null` (fabricated millwork) — round to 1/100
   instead. Removes the +8 LF cabinet inflation (gap 2) and the over-rounding on tops (17.333 → 18 is fine as display, not as order).
2. Make `millwork-laminate` waste apply only when a `sheet` size is given (raw HPL purchase); otherwise `wasteClass: null` for a
   finish-face SF. Same for booth panels when no `panel` module is given. Removes ≈ +69 SF (gap 1).
3. Add `areas`, per-leg depth and `mergeWaterfalls` to `millwork.countertop`; default `mergeWaterfalls = true` for solid surface /
   quartz with waterfalls so the SLD-1 line reads 111 SF, as the estimator and the legend carry it (gap 3, −11 SF).
4. Add the spec grommet rule to `countertop` (input `grommetSpacingFt`, from 12 3669: 4) (gap 5).
5. Let `paneling` compute with only `apronRuns`, or add `millwork.apron` (gap 7).
6. Skip Z-clip rows on faces narrower than one panel module (jambs/headers) and label Z-clip and bracket lines "derived accessory —
   verify if carried in the panel/shelf description" (gap 4).
7. Add `RESPONSIBILITY_INPUTS` to millwork assemblies and a cross-trade check that a millwork `built-unit` named LOCKER does not
   duplicate a furnishings LK tag (gaps 8, 9).
8. Measurement QA (takeoff side, not the engine): warn when a sheet carries viewports at different scales (A-707 ½" plans, ¾" elevations)
   and a linear measurement is ≥1.4× the dimension string it crosses; warn when a polygon is drawn on an NTS view.
