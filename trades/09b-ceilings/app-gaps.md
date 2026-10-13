# 09b Ceilings: TakeoffSpeed engine gaps

Compared against `TakeoffSpeed/lib/quantities/trades/interiors/ceilings.ts`, `gypsum-board.ts`, `board.ts`,
`framing.ts`, `profiles.ts` and `docs/QUANTITY_ENGINE.md` (ceilings runs W6–W8: soffit board −84% / −72%,
ceiling framing +22% / −59%, ACT-2 −74% / +4%, baffles −39% / −33%). Numbers below are this job's legend inputs
run through the engine's formulas in Python (`trades/09b-ceilings/scripts/engine_cmp.py`), not an engine run.

## What it already does right

| Line(s) | Engine | Estimator | Delta |
|---|---|---|---|
| 278 board SF | `gypsum-board.ceiling` net area × layers = 516.1 | 516.0 | +0.02% |
| 279 sheets | SF ÷ `default-sheet-sf` 32 | SF / 32 | 0 |
| 280–283 with `reviewed-commercial` profile | adhesive 0.031 tubes/SF; tape 0.375 LF/SF ÷ 500 LF roll; compound 0.53 lb/SF; screws 0.005357 lb/SF | 0.031; 0.00075 rolls/SF; 0.53; 0.0375/7 = 0.00535714 | 0 (screws −0.003%) |
| 292, 293 ACT SF | `ceilings.act` SF line, `wasteClass: null` (net) | net SF | 0 |
| 294 baffles | `ceilings.baffles` Σ rows; field fallback floor(24'×12/8") + 1 = 37 rows | 37 runs, 370.76 LF | 0 when rows are read |
| ACT-2 module | `module: 2x4` produces a "24"x48"" item label | estimate text wrongly says 24"x24" | engine is right |

## What it computes differently (with this job's numbers)

1. **Soffit board needs a width and adds a bottom (line 285).** `gypsum-board.soffit` makes `width` required. Board =
   L × faces × drop + L × width. The estimator carries only the fascia: Σ LF × GWB height × faces = 286.2 SF, and the
   soffit bottom sits inside the gypsum ceiling area. Any reader-supplied width double-counts. At 1'-0" it adds
   107.5 SF (+38%). The engine also has one `drop` per record, but each legend condition names **two** heights
   (framing 5'9", board 2'6"). Readers who put the framing height in `drop` get 452.1 SF (+58%). Both effects fit the
   documented −72% to −84% swings.
2. **Soffit framing is count-based, double on two-faced soffits, and has no bracing (line 291).** Engine:
   Σ(ceil(run×12/16)+1) × faces × (drop + toStructure) + bottom joists. With one run per condition (the true run split
   is not known) that gives 400.5 LF of soffit studs. The estimator's area rule gives 452.125/1.33 = 339.9 LF (engine
   +17.8%) and adds 90.1 LF of bracing that the engine cannot produce. The net is −6.8%, but only because two errors
   offset. "GWB BS" (faces 2) doubles the engine's verticals (35.0 vs 11.1 LF here). The estimator frames once.
3. **Divisor 1.33 vs 16/12 (lines 284, 291).** The reviewed-commercial profile turns on assumed stud joists, and
   irregular areas use SF × 12/16 = 387.0 LF on 516.0 SF. The estimator uses SF / 1.33 = 387.970 (−0.25%). Rectangle
   inputs use ceil(long × 12/16) joists × short span, which differs again depending on how rooms are split.
4. **Lines the estimator does not carry.** These are noise when scoring against this estimate. They are useful scope,
   but they belong behind a flag:
   - soffit track L × (faces + 2) = 326.7 LF
   - soffit corner bead L × faces = 111.7 LF
   - ceiling perimeter track
   - ACT tiles 237.2 / 30.6 EA
   - ACT mains 237.2 / 61.2 LF, 4' tees 118.6 / 30.6 EA, hangers 59.3 / 15.3 EA
   - wall angle
   - 5% `ceilings` waste on tiles
5. **Default profile ratios (no `reviewed-commercial`).** Compound 0.138 lb/SF gives 71.2 lb against 273.48 (−74%).
   Screws come out as 619 EA, not lb. There is no adhesive line. Tape is 0.37 LF/SF, so 0.382 rolls against 0.387
   (−1.3%).

## Inputs it lacks

- `framingHeight` and `boardHeight` as separate soffit inputs, read straight from a "SOFFIT @ x'H, GWB @ y'H" condition name,
  plus "BS" = 2 board faces on one framing line.
- A **stud-bracing** record: LF of run, brace height, spacing (48"). Source: A-630 detail 1 "3 5/8" ANGLE BRACING @ 48" O.C."
  and A-130 rows "@ 48" O.C @ 5'H / 8'H".
- An optional soffit `width` (0 or absent = no bottom board, when the bottom is inside the ceiling area).
- An ACT `atticStockPct` from the spec (09 5113 §1.2.D: 10%) as its own line, separate from waste.
- A furnish/install responsibility on ACT (ACT-2 is owner-vendor per A-131), as `ceilings.baffles` already has.
- A **stud size per soffit** (and per bracing run). The estimate carries every soffit stud as 3-5/8", but A-630 detail 4
  (cloud light cove, on the 30.5 FT Gathering Area cloud run) and A-131 detail 1 (transaction-bar beam wrap) call 6"
  metal studs. To follow the details the engine needs a size input on each soffit record and should emit one stud line
  per size; scored against this estimate, the default stays 3-5/8".

## Concrete changes, ranked by quantity impact on this job

| # | Change | Lines | Impact here |
|---|---|---|---|
| 1 | Soffit: add `framingHeight`, `boardHeight`, `faces` (board) and `framingLines` (default 1); make `width` optional with default 0; board = Σ L × boardHeight × faces | 285–290 | removes +38% to +58% reader-dependent error; 286.2 vs 286.04 (+0.06%) |
| 2 | New `metal-framing.stud-bracing` assembly: LF = Σ run / (spacing/12) × height; route into the same stud line as the soffit framing (bracing after the divisor is a convention: braceLF × height / 3 inside it fits the legend equally, 430.24 vs 430.02) | 291 | +90.1 LF (21% of the line) |
| 3 | Soffit framing area rule under a convention `metal-framing.soffit-framing-rule = area` (Σ L × framingHeight / divisor), counted once per run; on in `reviewed-commercial` | 291 | 400.5 → 339.9 LF soffit part; with #2, 430.0 vs 429.6 (+0.10%) |
| 4 | Convention `metal-framing.area-rule-divisor-ft` (default 16/12; 1.33 in `reviewed-commercial`) used by joists and soffit area rules | 284, 291 | 387.0 → 387.970 (−0.25% → 0) |
| 5 | Profile switch to omit unestimated by-products (soffit track/bead, ceiling track, ACT components, tile waste) or score them as "extra scope" | scoring | removes 9+ unmatched lines |
| 6 | ACT attic stock line from spec % (separate from waste); take tile size from the schedule and warn when estimate text disagrees | 292–293 | +94.9 / +24.5 SF as a separate line (not in this estimate) |
| 7 | Screws ratio as the exact rational 0.0375/7 in the profile, not the rounded 0.005357 | 282, 289 | −0.003% → 0 |

Fixtures for all 17 lines are in `fixtures.json`. Formula ids: `gypsum-board.ceiling.board-sf`, `gypsum-board.sheets`,
`gypsum-board.adhesive-tubes`, `gypsum-board.tape-rolls`, `gypsum-board.screws-lb`, `gypsum-board.compound-lb`,
`metal-framing.ceiling-joists-area-rule`, `gypsum-board.soffit.board-sf-by-legend-height`,
`metal-framing.soffit-studs-area-rule`, `ceilings.act.area`, `ceilings.baffles.rows`.
