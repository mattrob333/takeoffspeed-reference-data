# 22 Plumbing: TakeoffSpeed engine vs this estimate

Engine files: `lib/quantities/trades/mep/plumbing.ts`, `pipe.ts`, `shared.ts`, `engine.ts`.
Numbers were computed with Python from this job's quantities.

## What the engine already does right

- **Every estimate line has an assembly.** `plumbing.pipe` (system + size + material + location)
  covers 404–420. `fixture` covers 422, 424–428. `water-heater` covers 423. `equipment` covers 421.
  `drain` covers 432–435. `hydrant` covers 429–430. `filter` covers 431. `cleanout` covers 436.
  `hose-bib` covers 437. `downspout-nozzle` covers 438. `box` covers 439–440. `valve` covers
  441–443. `gas-service` covers 444. `allowance` covers 403. The 42 lines map to 14 assemblies with
  nothing missing.
- **Primary quantities equal the estimate when given the legend values.** Pipe net LF = Σ runs
  (+ risers). Counts = Σ count. In `mode: 'net'` all 41 measured and counted lines come out exactly
  as in `reconciliation.csv`.
- **Gas splits by location the way the estimator did.** Line 418 (1" roof) and line 419 (1" below
  grade) stay separate because `location` is part of the pipe key.
- **`sizeAssumed` flag** reproduces "1-1/2"DIA CONDENSATE DRAIN PIPE, DIA ASSUMED" (line 417).
- **`materialSpec`** carries "TYPE K" for line 413.
- **Allowance** emits 1 LS with the area in the description, which is the right shape for line 403.
- **Hanger spans** match the project spec §3.10 and P-101: copper ≤1-1/4" 6', CI 5', PVC 4',
  steel gas 3/4"–1" 8'.
- **Cleanout read text** already says to de-duplicate plan versus isometric.

## What it computes differently (ranked by quantity impact)

| # | Difference | This job, in numbers | Change |
|---|---|---|---|
| 1 | **Default `order` mode adds 5% pipe waste and rounds to sticks.** The estimator carries net LF. | 992.90 LF net becomes 1,042.55 LF gross. Example: 1" HW 162.22 → 170.33 LF → 9 × 20' sticks. | Score plumbing against this estimate with `mode: 'net'`. Keep waste as a contractor setting, never in the reference comparison. |
| 2 | **Tag counts summed across sheets.** `fixture.count` is `many: true` and the code sums every value. Only the read text says "the same fixture on two sheets counts once". | WC appears on P-301, P-302 and P-402 (2 each): 2 + 2 + 2 = 6 versus 2. The same 3× applies to LAV, SK-T, SK-U, MS, EDF (6 lines tripled). EWH, CP, HB and RH also repeat on P-402 (4 lines doubled). | Add `countSheet` (designated plan) or de-duplicate in code: take the max per tag over sheets of the same floor and warn when values differ. Mark isometric and riser sheets "no count". |
| 3 | **Pipe lines split by location.** The estimator merges B/G + A/C + roof per size. The engine key includes `location`. | 3" storm: 33.5 / 25.8 / 91.2 on 3 lines vs 150.59 on 1. 4" storm: 12.7 / 103.7 / 56.3 vs 172.7. 3/4" CW: 39.8 + 4.7. 1-1/4" CW: 2.0 + 62.5. That is 4 estimate lines becoming 10 engine lines. | Add an output grouping option `groupPipeBy: 'system+size'` that sums locations into one line, with the location breakdown kept in the steps. Keep gas split, since the estimator split it. |
| 4 | **Risers double counted when the model also reads the iso.** The estimator's plan legend already includes the vertical drops, drawn as off-plan segments. | P-302 has 7 "3" TO CD", 4 "4" DN", 2 "4" UP TO RD" and 2 "4" UP TO OD" points. The 4" points visibly carry vertical segments drawn above the plan, inside the 103.7 FT. Adding risers from P-402 or from the drop notes counts them twice. The size of the overlap cannot be split from the legend total. | When `runs` come from a PlanSwift-style legend total, set `risers` empty. Tell the model in `runs.read` that drawn drop segments are already included. |
| 5 | **Kit lines with no estimate counterpart.** The estimator puts all of these in the line 403 allowance. | Fixtures: LAV 2 → 2 trim + 4 stops + 4 risers + 2 traps + 2 carriers + 2 ADA kits + 2 grid drains. WC 2 → 2 stops + 2 risers + 2 setting kits + 2 seats. EDF 1 → stop, riser, trap, carrier, ADA kit. Drains: FL 3 → 3 traps + 3 trap-primer connections. Pipe: 1" HW → 28 hangers, 28 attachments, 28 shields, 162.22 LF insulation (60 × 3' sections at 10%). CW 1-1/4" + 1" + 3/4" (154.54 LF) → 57 insulation sections. Roof gas → 6 + 2 roof supports. | Correct scope, but score them as "beyond estimate" lines, not misses. Add a `kitLines: 'separate' \| 'in-description'` setting so a contractor who writes trim into the fixture description (as here) gets one line per tag. |
| 6 | **Water-heater kit duplicates the drawn shut-offs.** `water-heater` adds 2 isolation valves (`plumbing.wh-isolation-valves` = 2) and 2 dielectric unions. The estimator counted the same 2 valves from the P-302 legend as line 442. | If the model also records `valve` "SHUT-OFF VALVE" ×2, the result is 4 valves vs 2. | When a `valve` record cites the water-heater keynote, set `wh-isolation-valves` to 0, or have `valve` take `servesTag: EWH` and suppress the kit valves. |
| 7 | **Allowance area as printed vs estimator's rounded basis.** | The engine prints 1,900 SF (G-001). The estimate says 2000 SF. Quantity is 1 LS either way. | Optional `areaBasis` input (rounded) next to `area`, so the description can match. Low impact. |
| 8 | **Condensate owned by two trades.** `plumbing.pipe` (system condensate) and `hvac.condensate` both accept the P-303/M-302 runs. | The estimate puts 34.52 LF in Div 22 (line 417) and the 1 EA trap assembly in Div 23 (line 480). | Have `hvac.condensate` skip LF when a plumbing condensate record cites the same sheet; keep only its `traps`. |

## Inputs the engine lacks

- **Count-sheet designation** per tag (gap #2).
- **Gas appliance connection kit per RTU** from P-403 and P-303 keynote 3: shut-off, drip leg,
  2 test ports, regulator, union, flex connector, × 2 RTUs. Only `water-heater` (fuel gas) has a
  shut-off and drip leg. The estimator carried only the shut-off (line 443), so this is low impact
  for matching but real scope.
- **Hose bib and hydrant drain tubing.** RH and HB need copper drain tube to the nearest drain
  (schedule notes). There is no input for it. The estimator also left it unmeasured.
- **Material conflict flag.** There is no way to record "documents disagree" (P-101 PEX-A table, with its
  copper fallback note, vs Type L copper schedule and spec; PVC vs cast iron above ground). `material` is a single required choice. Add a
  `materialConflict` text input that caps confidence.
- **Faucet sub-row.** `fixture.trim` exists, but there is no rule saying a schedule sub-row
  ("LAVATORY - (BATTERY) FAUCET") belongs to its parent tag. Add that to the `trim.read` text.

## Concrete changes, in order

1. Score Div 22 in `mode: 'net'` (removes 49.65 LF of waste from the comparison).
2. Count-once logic for tags across sheets (prevents 3× on 6 fixture lines and 2× on 4 more).
3. `groupPipeBy: 'system+size'` output option (10 lines collapse to 4, matching 404, 405, 412, 415).
4. Note in the pipe `runs`/`risers` read text that PlanSwift-style drop segments are already in
   the runs.
5. `kitLines` setting plus a "beyond estimate" class for kit lines in scoring.
6. Water-heater kit / valve de-duplication.
7. RTU gas connection kit assembly; `materialConflict`; allowance `areaBasis`; condensate ownership.

`fixtures.json` in this folder has one test per reproducible line. Inputs are legend values with
units. The expected value is the estimate quantity. Tolerance is the legend's display rounding
for LF: `toleranceLF` = 0.05 FT × legend rows, and `tolerancePct` = that as a percentage of the
expected quantity, rounded up to 2 decimals, minimum 0.5% (formulas.md F1 convention 4). Counts
are exact.
