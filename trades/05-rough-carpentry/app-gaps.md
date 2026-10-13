# App gaps: TakeoffSpeed quantity engine vs this estimate

Engine files compared (read only):
- `lib/quantities/trades/structure/rough-carpentry.ts`: assemblies `sheathing`, `blocking`, `backing`, `stud-wall`
- `lib/quantities/trades/structure/shared.ts`: `wallArea`, `measuredArea`
- `lib/quantities/trades/fitout/millwork.ts`: the `casing` assembly and the in-wall casework blocking that cabinet records emit under `rough-carpentry`
- `lib/quantities/trades/interiors/partitions.ts`: wall faces, where exterior sheathing is "a face with `unfinishedB = yes`"

## What it already does right

- **Blocking.** `blocking` computes `LF = Σ runs × rows` and puts size and treatment in the key (`blocking:2X10 P.T. BLOCKING`). P.T. and FRT lines stay separate, as in the estimate. BF purchase uses nominal t × w / 12, so 148 LF of 2x10 is 246.7 BF.
- **Sheathing.** `sheathing` sums SF areas and W × H panels and applies a slope factor when a pitch is given. Location is part of the key, so roof, canopy ceiling, booth ceiling and IT room stay separate lines, as lines 84–87 are. Sheets default to 32 SF.
- **Backing.** `backing` keys on thickness and treatment only. All 3/4" casework backing merges into one line, which matches line 146 (five legend rows → one line).
- **Casework blocking.** It lands in the `rough-carpentry` trade with the same key form, so it merges with `blocking` records.
- **Fireblocking.** It is generated only for wood stud walls. That is correct here: every wall on this job is cold-formed steel, and the estimate has no fireblocking.
- **Casing.** `millwork.casing` has an `assumed` flag that caps confidence. That is the right treatment for line 88's "ASSUMED".

## Differences and missing inputs, ranked by quantity impact on this job

| # | Gap | Engine behaviour | Estimator | Impact here |
|---|---|---|---|---|
| 1 | **Opening deduction on wall sheathing** | `wallArea` (sheathing `runs` mode) and `stud-wall` subtract every opening W × H given | No deduction; storefront runs are taken full height through the glass | Exterior glazing + doors on A-610/A-600 total ≈ 888.6 SF, so line 82 would come out ≈ 2,161.7 SF (−29.3% vs the estimate) if the model supplies openings |
| 2 | **Exterior plywood routed as a partition face** | The adapter tells the model that exterior sheathing is a partition face with `unfinishedB = yes`. That emits the board under `gypsum-board`, with screws, tape and mud ratios | Plywood sheathing is a Div 06 line in SF, with no accessories | Up to 3,057 SF lands in the wrong trade, with invented gypsum accessories. Glass-mat parapet sheathing (09a) does belong there; plywood does not |
| 3 | **Waste in default mode** | Waste class `rough-carpentry` is 10% on every sheathing, backing and blocking line | All lines are net | +305.7 SF on line 82, +56.9 SF on line 85, +24.1 LF on line 89 unless `mode: 'net'` is used |
| 4 | **Casework blocking rows** | `millwork.blocking-rows-base` = 1 and `-upper` = 2 rows per cabinet LF | The drawings print the rows: (7), (4), (3), (2) | The runs total 72.0 LF. The engine gives 72–144 LF against 240.66 (−40% to −70%; −30% to −65% against the 1x4-only 206.6). The `(n)` legend prefix must override the convention |
| 5 | **No `faces` on sheathing runs** | One height and one face per record | `BS 1/2" SHTNG ONLY` wing walls count twice | −156.8 SF on line 82 (−5.1%) unless the model enters the runs twice |
| 6 | **No per-run height in one sheathing record** | `height` is a single value, so each height group needs its own record. The keys merge, so the total survives, but ten records are needed for line 82 | Ten height rows on one line | No quantity loss, but a high chance of the model collapsing heights (one 12'-9" for every A-120 run gives 2,249.1 SF before parapets) |
| 7 | **No `layers` input** | — | Booth ceiling = 2 × roof area | −76.2 SF on line 86 (−50%) unless the area is entered twice |
| 8 | **Penetration perimeter blocking** | No input converts curb/penetration counts or sizes into a perimeter. The model must trace LF | A-140 note 4: P.T. 2x6 around every penetration (curbs 39.9 LF + hatch + vents) | The estimate itself omits it. The engine cannot generate it from the note. Flag it as missing scope |
| 9 | **Multi-member nailer stacks** | One `size` per record | One run gives two lines (2x14 + 1x6 at 9/A450; 2x4 + 2x6 at 8/A450) | No loss if the model writes two records. The catalog should say so: −40 LF and −46 LF if one member is dropped |
| 10 | **Estimator rounding conventions** | None. Purchase rounding happens only in sheets/BF | BACKING is rounded up to 5 SF (lines 145–147). A-140 nailers are rounded by hand | Engine is lower by 3.2 SF (146), 2.8 SF (147), 0.7–1.5 LF per nailer line: −2.4% / −7.0% / −1.5% to −7.3% |
| 11 | **Trim at openings** | `millwork.casing` = 2H + W + 2 × casing per side; 7 interior doors × 2 sides + exterior doors + windows ≈ 570 LF (before the casing-width add) | 910 LF "ASSUMED" | Not reproducible (−37%). Keep as an allowance line; do not fit a formula to it |
| 12 | **Treatment on sheathing** | `sheathing` has no `treatment` input; FRT must be put in `material` text | "FIRE RATED PLYWOOD BACKBOARD" | Naming only. Make `treatment` a first-class key so an FRT backboard can never merge with an untreated panel |

## Concrete changes (in order)

1. **Opening deduction default.** Add the convention `rough-carpentry.sheathing-deduct-openings` (default `none`; options `all` and `over-N-SF`), and pass it to `wallArea` from `sheathing` and `stud-wall`. This estimator deducts none, which is worth 889 SF here.
2. **Route plywood to Div 06.** In `takeoff-adapter.ts`, route plywood/OSB exterior sheathing to `rough-carpentry.sheathing`. Keep `unfinishedB` for gypsum and glass-mat only. Reject a partition face whose board text matches `PLYWOOD|OSB`.
3. **Read `(n)` as rows.** Parse a leading `(n)` in a legend or record name into `rows` on `blocking` and `backing`. Make casework blocking take printed rows when present, and fall back to `millwork.blocking-rows-*` only when no row count is drawn.
4. **Faces and runs.** Add `faces` (default 1) to `sheathing` runs. Allow per-run heights, the way `fixtures.json` encodes them as `{lf, height, faces}`.
5. **Layers.** Add `layers` (default 1) to `sheathing` areas.
6. **Optional output rounding.** Add a convention `rough-carpentry.round-up-sf` / `round-up-lf` (default 0, i.e. off), so that a contractor whose estimator rounds BACKING up to 5 SF can match. Never round below the measured value.
7. **Penetrations.** Add an input `penetrations` (pairs W × H, or counts with a perimeter) to `blocking`, so that a general note such as A-140 note 4 can yield LF. Add a flag when roof curbs are counted but no penetration blocking record exists.
8. **Catalog read hints.**
   - For `blocking`: "one record per member in a stacked detail; read the drawn width when only 2X/1X is printed".
   - For `sheathing`: "sheathing height may differ from wall height (`SHTNG h`); parapet face above the deck is a separate run".

## Engine output for this job's inputs (net mode, with the changes above)

`fixtures.json` encodes the inputs. With items 3–6 implemented, the 16 fixtures reproduce the estimate within their tolerances: 8 within 0.3% of the estimator's figure, and 8 exactly where a rounding convention applies (lines 91–93, 95, 96, 145–147). Without them, lines 82, 86, 89 and 146/147 miss by 5.1%, 50%, 40–70% and 2.4–7.0% respectively.
