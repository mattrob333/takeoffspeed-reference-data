# 33 — Site utilities: TakeoffSpeed engine gaps

**Engine code:**
- `TakeoffSpeed repo: lib/quantities/trades/site/site-utilities.ts`: assemblies
  `pipe-run`, `structure`, `fitting`, `basin`.
- `trades/site/shared.ts`: `trenchLines`, `trenchFromInputs`, the OD tables.
- `trades/site/earthwork.ts`: `earthwork.trench`, and the conventions
  `trench-side-clearance-in` 12, `trench-min-width-in` 24, `swell-pct` 25.

**How it was run:** the engine itself, in `mode: 'net'`, with no code edited. The script is
`trades/33-site-utilities/scripts/run-engine.ts`, run with `tsx`, in two modes:
- **drawn**: one `pipe-run` record per table row with rim and invert elevations, stone bedding,
  4" below. Output in `engine-out-drawn.txt`.
- **est**: the estimator's section forced (3' width, 5' depth, no bedding, OD = nominal).
  Output in `engine-out-est.txt`.

`engine_replica.py` reproduces the drawn-mode trench numbers by system, exact to 4 dp.

## What it already does right

| Line(s) | Estimate | Engine | Match |
|---|---|---|---|
| 721, 722 storm LF by size | 25.11, 332.42 | 25.11, 332.42 (merged by key `pipe:storm:<size>:HDPE` over 7 records) | ✓ |
| 723 sanitary | 295.96 | 295.96 | ✓ |
| 725–728 header / water / power / telephone | 168.18, 138.27, 72.88, 74.43 | same | ✓ |
| 729 cleanouts | 6 | 6, with "W/ RECESSED BRASS CLEANOUT PLUG" | ✓ |
| 730–733 STGI / STYI / JB / OCS | 5 / 1 / 1 / 1 | same. JB and OCS carry "NO DETAILS SO ASSUMED" with confidence cap low (wording matches the estimate) | ✓ |
| 734–737 saddle, meter, RPZ, manhole connection | 1 each | 1 each | ✓ |

Route LF for services, not conduit LF, is the default (`pipes` defaults to 1). That matches.

## What it computes differently, ranked by quantity impact

| Rank | Line | Estimate | Engine (drawn depths, defaults) | Delta | Cause |
|---|---|---|---|---|---|
| 1 | 741 BACKFILL | 414.67 CY | 173.04 CY | **−241.6 CY (−58.3%)** | Engine backfill = excavation − bedding − pipe, and puts 166.74 CY in stone bedding. The estimate has no bedding line; its backfill is the whole hole minus a 42 CY allowance |
| 2 | 742 HAULOFF | 42 CY | 200.30 CY | **+158.3 CY (+377%)** | Engine haul = bedding + pipe (displaced by imported stone). The estimate haul is a 9.2% allowance |
| 3 | 740 EXCAVATION | 456.67 CY | 373.34 CY | **−83.3 CY (−18.2%)** | (a) The header pipe has no rim or invert, so the engine gives no trench for 168.18 LF (warning only). (b) Per-row depths: storm 3.8 ft average vs 5 ft, sanitary 6.5 ft vs 5 ft. (c) Width = OD + 24": 3.75' for 18" N-12 (OD 21") vs the estimator's 3.0', and 2.52' for 6" PVC vs 3.0' |
| — | (no line) bedding stone | none | 166.74 CY | +166.74 CY | Engine emits `PIPE BEDDING STONE (BEDDING, HAUNCH AND INITIAL BACKFILL)` with 12" cover over the crown. C-6.2 says stone to ½ OD above the pipe, not 12" |
| 4 | 724 gas | 152 LF | 156.4 LF | +4.4 LF (+2.9%) | Engine uses the measurement; the estimate's 152 is unexplained. Engine is arguably right |
| 5 | 739 irrigation backflow | 2 EA | 1 EA (if fed once) | −1 EA | No cross-page dedupe hint. If fed the p42 and p87 rows separately, the engine would also sum to 2 |
| 6 | 738 headwall | 9 LF | 1 EA + 8.8 LF "WALL LENGTH" | −0.2 LF, plus an extra EA line | No whole-foot round-up convention. The EA line is not in the estimate |

With the estimator's section forced (est mode: 3' × 5', no bedding, nominal OD):

| Line | Engine | Estimate | Delta |
|---|---|---|---|
| Excavation | 456.48 CY | 456.67 CY | −0.04%: the engine does not round Σ LF to 822 |
| Backfill | 429.26 CY | 414.67 CY | +3.5% |
| Haul | 27.22 CY (= nominal pipe volume) | 42 CY | −35% |

So the engine can reproduce 740 within 0.05% but has no way to carry the 42 CY allowance.

## Inputs the engine lacks

1. **Job-level trench section.** There is no way to give one `trenchWidth` / `trenchDepth` for a
   group of runs. Each record must repeat them, and the `pipe-run` record has no `trenchDepth`
   (only `depthStart` / `depthEnd`, to which it adds wall + bedding).
2. **Haul-off allowance.** There is no `haulAllowanceCY` or `haulPct` input. Haul is always
   bedding + pipe.
3. **Bedding cover from the detail as "½ OD".** `beddingCover` is a length. The C-6.2 detail
   writes cover relative to OD (to ½ OD above the crown), and the convention defaults to 12".
4. **Header and service depth.** The header pipe has keynote "minimum slope of 1%" but no inverts.
   A `minCover` input (C-0.1: 3'-0" for water; C-6.2: 3'-0"/4'-0" sewer) would let the engine
   trench the header and the water service instead of warning.
5. **Cross-page identity.** There is no `sameAs` / sheet+keynote dedupe on fitting and structure
   counts. The same need is recorded in `26-electrical/app-gaps.md` §7.
6. **Rounding conventions.** There is no whole-foot rounding on headwall LF and no `roundLength` on trench length.
   (Ceil and round-to-nearest are indistinguishable on this job: 8.8 → 9 and 821.67 → 822 either way.)
7. **Trench scope selector.** The engine trenches any run with depths. The estimate trenches only
   gravity and drainage pipe and leaves utility-furnished services (`furnishedBy`) and the 1"
   water out. Today that outcome depends on whether depths are supplied.

## Concrete changes, ranked by quantity impact

1. **Make the trench earthwork split a convention** (`site-utilities.trench-bedding-line` =
   `separate | none`). With `none`:
   - backfill = excavation − pipe − haul allowance;
   - no bedding line.

   This closes ranks 1 and 2 (−241.6 / +158.3 CY), and is how this estimator works. Keep
   `separate` as the default, since the C-6.2 detail does require stone, but expose
   `site-utilities.trench-haul-pct` (this job: 9.20%) or a `haulCY` input.
2. **Allow a job-level trench section** (`earthwork.trench` group record: `runsFrom` = the
   pipe-run keys, `width`, `depth`, `roundLength`). On this job: runs = 721 + 722 + 723 + 725,
   width 3', depth 5', round to whole LF → 456.666667 CY exact (rank 3, −83.3 CY).
3. **Read trench width from the detail as a formula.** Accept `O.D. + 18" MAX` → width = OD + 18".
   Do not default to OD + 24" when the detail states a maximum. 18" N-12: 21 + 18 = 39" by OD,
   or 36" by nominal as the estimator used. State which.
4. **Bedding zone from the detail.** Support `beddingCover = 0.5 × OD` (C-6.2) instead of the 12"
   default. That drops the bedding-zone height for 18" pipe from 4" + 21" + 12" = 37" to 4" + 21" +
   10.5" = 35.5".
5. **Dedupe counts across reprinted pages** (`sameAs: p42`). Line 739 would go from 2 to 1 with a
   warning that the estimate shows 2.
6. **Headwall:** offer `unit: LF` only, with a `roundTo: 1 ft` option (direction unverified: this job cannot tell ceil from nearest). The estimator carries 9 LF
   and no EA line.
7. **Flag a legend vs. estimate gap on gas.** No engine change; the engine's 156.4 is right. Put
   the 152 in the review queue.
8. **Warn on an EXISTING structure row.** When a table row says `(EXISTING)`, skip the structure
   count and offer a `connection` fitting (manhole core-and-grout). This job does it for S1-SSMH
   (737) and skips C1-STJB.
