# App gaps — 31 earthwork vs the TakeoffSpeed quantity engine

## How it was compared

**Engine compared:**

- `lib/quantities/trades/site/earthwork.ts`: `earthwork.cut-fill`, `earthwork.balance`,
  `earthwork.continuous-footing`, `earthwork.spread-footing`, and also zone, grid-cell, end-area,
  topsoil-strip, fine-grading, trench and undercut.
- `trades/site/shared.ts` (`footingEarthworkLines`, `loosePurchase`).
- Conventions `earthwork.shrink-pct` 15%, `earthwork.swell-pct` 25% and
  `earthwork.footing-working-space-ft` 1 ft.

**How it was run:** the engine itself, in `mode: 'net'`, on measurement records holding this
job's inputs, with no code edited.

- Script: `trades/31-earthwork/scripts/run-engine.ts`, run with `npx tsx` from the TakeoffSpeed
  root. Output: `engine-out.txt`.
- Records:
  - one `earthwork.continuous-footing` (WF20: runs 124.2, 2'-0" × 1'-0", bottomDepth 3'-0",
    wallWidth 8");
  - seven `earthwork.spread-footing`, one per mark, bottomDepth = 2'-0" + T;
  - one `earthwork.cut-fill` with the 9 non-blank cut and 10 non-blank fill values of p92.

## What it already does right

| Line | Estimator | Engine (net) | Note |
|---|---:|---:|---|
| 639 cut | 634.41 | 634.41 | ✓ exact. The `cut` input takes each printed region value (many) and sums them |
| 640 fill | 786.25 | 786.25 | ✓ exact |
| 641 net fill | 151.84 | 151.84 **only with `earthwork.shrink-pct` = 0** | The plain balance is also printed as a step, "volumetric balance (no shrink)" |
| 629 excavation | 119.8 | 119.7556 **with `workingSpace` 1'-0" on WF20 and 6" on each spread mark** | ✓. The vertical-sided L × (W + 2·ws) × depth structure is the estimator's |
| 629–631 aggregation | 1 line each | 1 line each | Continuous and spread records share the keys `footing:excavation`, `footing:backfill` and `footing:hauloff`, so they sum into one line, as in the estimate |
| 631 haul basis | bank CY | net is bank CY | Swell goes only into the order quantity (`loosePurchase`) |
| backfill rule | exc − concrete | exc − footing − wall below grade | Same structure (`footingEarthworkLines`) |

## What it computes differently, ranked by quantity impact

| # | Line | Estimator | Engine | Δ | Cause |
|---|---|---:|---:|---:|---|
| 1 | 641 NET FILL | 151.84 CY | 290.59 CY `NET FILL (IMPORT)` | **+138.75 CY (+91.4%)** | The default 15% shrink: 786.25 ÷ 0.85 − 634.41. The estimator carries the plain fill − cut, and the geotech gives no factor. The line also lands in section `HAULOFF/IMPORT` under a different item name, so it does not match `GRADING > NET FILL` |
| 2 | 630 BACKFILL | 83.7 CY | 111.09 CY (defaults) | **+27.39 CY (+32.7%)** | The 1 ft working space on spread pads (+23.38 CY of excavation), plus the missing stem deduction (#4) |
| 3 | 629 EXCAVATION | 119.8 CY | 143.14 CY (defaults) | **+23.34 CY (+19.5%)** | `earthwork.footing-working-space-ft` = 1 ft applies to pads as well as trenches. The estimator uses 6" at pads: (L+1)(W+1) |
| 4 | 631 HAUL-OFF | 36.1 CY | 32.05 CY (defaults *and* with working-space overrides) | **−4.05 CY (−11.2%)** | `continuous-footing` deducts the wall only over its own runs: 124.2 × 8" × 2' = 6.13 CY. The estimator deducts all stem walls: 202.2 FT = 10.15 CY. The ≈78 FT of 8" stem over the spread footings and the 10" wing-wall stem (4.02 CY together) have no input. `spread-footing` only takes a square `pier` |
| 4b | 630 BACKFILL (with overrides) | 83.7 | 87.71 | +4.01 CY (+4.8%) | Same cause as #4 |
| 5 | 631 / 641 order quantity | 36.1 / 151.84 (no swell) | 45.1 / 189.8 loose CY in order mode | +25% | `earthwork.swell-pct`. This is correct for trucking, but must not be scored against an estimate that carries bank CY. Compare net mode only |

## Inputs the engine lacks

1. **A separate working space for spread pads and continuous trenches.** There is only one
   convention (`earthwork.footing-working-space-ft`). This job needs 1 ft at the trench and 0.5 ft
   at the pads.
2. **Wall or stem runs independent of the footing runs.** The input `wallRuns` (LF), with
   `wallWidth` and `wallHeight`, would let backfill deduct a stem that sits on spread footings.
   Today the wall deduction is `lengthFt × wallWidth × (bottomDepth − T)` over the footing runs
   only.
3. **The depth datum.** The `bottomDepth` read text says "from finished grade", but S-201 gives
   top of footing below *finish floor* ("[-2'-0"] BELOW FINISH FLOOR SLAB"). Two inputs would
   cover it:
   - `topOfFootingBelow` (with datum FF or grade), plus thickness;
   - a per-tag bracket override (one F38 is `[-1' - 0"]`).
4. **A slab and base deduction at interior digs.** These are optional. They would flag the 8" of
   slab and gravel inside a dig measured from FF: 25.81 CY on this job.
5. **A pavement section on printed tables.** `earthwork.grid-cell` has `sectionDepth`, but
   `earthwork.cut-fill` cannot say whether a printed table is to finished grade or to subgrade.
   Here it is to finished grade, and the box-out is about 881 CY. An input `surface` (finished /
   subgrade) would let the engine warn and add a separate `PAVEMENT SECTION BOX-OUT` judgement
   line from the paving records.
6. **Region rows with a signed Qty.** Earthwork Pro prints Cut, Fill and Qty per region. Taking a
   `region` record (elevation, cut, fill) would keep the 14-row audit trail. The current input is
   two flat lists.
7. **A pond stone-storage excavation cross-check.** The stone of line 711 (626 CY below the 435.00
   basin bottom) has no matching excavation. A check across `site-utilities` / `erosion` and
   `earthwork` should flag stone or aggregate volumes below the grading surface that have no
   excavation.

## Concrete changes, ranked by quantity impact

1. **Net fill as the estimator prints it** (+138.75 CY of error removed).
   - Always emit `GRADING > NET FILL` = fill − cut (signed, no shrink), with key
     `grading:net-fill`.
   - Keep the shrink-adjusted import or export as a second, labelled line
     (`NET FILL (IMPORT) — 15% SHRINK CONVENTION`).
   - Or add `'earthwork.shrink-pct': '0'` to the `reviewed-commercial` profile in
     `lib/quantities/profiles.ts`. The `QUANTITY_ENGINE.md` table already lists "0% (plain
     fill − cut)" as seen in practice.
2. **Spread-footing working space** (−23.38 CY on excavation).
   - Add the convention `earthwork.spread-footing-working-space-ft` (default 1 ft; reviewed
     profile 0.5 ft). Basis: this job's 119.8 CY and the dumpster line 665.
   - Use it in `spreadFooting.compute` in place of `earthwork.footing-working-space-ft`.
3. **Stem walls over pads** (+4.02 CY haul, −4.02 CY backfill).
   - Add `wallRuns` / `wallHeight` to `earthwork.continuous-footing`. Defaults: `runs` and
     `bottomDepth − T`.
   - Or add a `stemWall` pair (length × width) to `earthwork.spread-footing`.
   - With both changes and the legend stem lengths, the engine gives 119.7556 / 83.75 / 36.00
     against 119.8 / 83.7 / 36.1 (−0.04% / +0.06% / −0.26%; nominal schedule concrete 36.00 CY
     against the estimator's lines 19–28 at 36.08 CY).
4. **The datum and bracket overrides** (−0.81 CY if the F38 at [-1'-0"] is honoured). Accept
   top-of-footing brackets and an FF datum, and say which datum each step used.
5. **Scope warnings, not quantities.**
   - `earthwork.cut-fill` should warn when the table is to finished grade and paving records
     exist (box-out of about 881 CY here).
   - It should warn when no topsoil-strip record exists although C-0.1 calls for 4" topsoil.
   - The engine should warn when footing digs are measured from FF and the grading pad sits below
     FF: 38.71 CY above the 440 pad here.
6. **Scoring.** Score earthwork in `mode: 'net'` (bank CY, no swell), and round
   footing-earthwork lines to 0.1 CY only for display. The estimator prints one decimal on
   629–631, and two on 639–641 (the PlanSwift output).
