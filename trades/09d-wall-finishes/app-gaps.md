# App gaps: TakeoffSpeed engine and this trade

**Compared against:** `TakeoffSpeed repo: lib/quantities/trades/interiors/wall-finishes.ts`, using the assemblies `wall-finishes.wall-tile`, `wall-finishes.frp`, `wall-finishes.wallcovering` and `wall-finishes.panels`. Shared helpers come from `flooring.ts` (setting materials and trims), `board.ts` (backer board) and `painting.ts`.

**How the numbers were produced:** I ran the real engine with `tsx` on this job's inputs (`trades/09d-wall-finishes/scripts/engine-run.ts`), in `mode: 'net'` and in `mode: 'order'`. The restroom walls in that run are the same decimal widths as `fixtures.json` cross-check 8 and formulas F1 (7.5083, 7.675, 4.0056, 0.3333 ft per room, 19.522 ft), and WT-3 uses the printed 10'-4 1/4".

## What the engine already does right

| Line | Engine input (this job) | Engine net | Estimator | Δ |
|---|---|---|---|---|
| 237 WT-3 | wall-tile, walls `10'-4 1/4"` (printed 10'-6 3/4" less two 1 1/4" returns), height `3'-8 1/2"` | 38.40 SF | 38.42 | −0.06% |
| 235 part, A-703 backsplash | wall-tile, `6'-9"` × `2'-8"` | 18.00 SF | 18.0 (legend) | 0 |
| 235 part, A-705 backsplash | wall-tile, `7'-2"` × `1'-6 1/2"` | 11.05 SF | 11.1 (legend) | −0.46% |
| 241 FRP-1 | frp, walls `2'-0"`, `2'-0"`, height `4'-0"` | 16.00 SF, 1 sheet (order) | 16.0 | 0 |
| 239 WC-1 | wallcovering, walls `10.1`, height `12'-0"` | 121.20 SF | 120.0 | +1.0% (the estimator rounded) |
| 240 WC @ PT-7 | wallcovering, `10.3` × `10'-0"`, `primerTag: PT-7`, `assumed: yes` | 103.00 SF, "ASSUMED WALL COVERING, V.I.F.", confidence low, plus a PT-7 primer line in painting | 103.0 | 0 |

Several pieces already match the estimator:
- **Band rule.** `bandArea` computes Σ walls × H − openings, and it does not deduct fixtures. That is the estimator's rule. (The reader prompt is a different matter; see item 6.)
- **Primer-only wall covering.** The `assumed` flag combined with `primerTag` is exactly line 240's convention: a wallcovering assumed from a primer-only tag and marked V.I.F.
- **Tile companions.** The tile setting outputs (thinset, grout to flooring, backer board to gypsum-board, edge and cove trims) cover the companion lines the estimator carried elsewhere, namely 226, 233, 234 and 272.
- **Net mode.** `mode: 'net'` reproduces the estimator's net quantities.

## What it computes differently, ranked by quantity impact

### 1. A blended tile band cannot be split by tag (impact: 100 SF of WT-2 and WT-9 missing, WT-1 +69%)

`wall-tile` takes one tag per record and gives that tag the whole band. The restroom band is a single 5'-6" band laid in a WT-1 / WT-2 / WT-9 random-drop blend, and both backsplashes use the same blend. The engine can only do one of two things:

- **Record the band once.** It then returns WT-1 = 214.74 + 18.00 + 11.05 = **243.79 SF**, against the estimator's 144.19 (+69%), and WT-2 = WT-9 = **0**. The estimator has 46.72 and 53.22 for those.
- **Record each tag with the walls.** Every tag then gets the full band, and the tile total becomes **731.4 SF** against 243.8 (three times too much).

**Change.** Add a `blend` input to `wall-finishes.wall-tile`: `[{tag, areaSF?} | {tag, mixPct?}]`.
- **Traced areas.** When accent areas are given, the field tag gets `bandSF − Σ accents`, which is the estimator's method.
- **Mix fallback.** When only `mixPct` is given, which A-170 prints as "MIX 60% / 20% / 20%", each tag gets `bandSF × mix%`. This keeps the total exact, but on this job WT-1 comes out +1.6%, WT-2 +4.5% and WT-9 −8.3%. Mark those lines as medium confidence.
- **Validation.** Mix percentages must add up to 100. Accent areas must be smaller than the band.
- **Outputs.** Emit one `wall-tile:<tag>` line per blend tag. They all share the same thinset, grout and trim lines.

### 2. No room-repeat multiplier for "similar" rooms (impact: 107.4 SF)

A-410 draws the three tiled elevations once (markers 7/8/9 appear in both rooms on 6/A-410) and adds "MENS INTERIOR ELEVATIONS ARE SIMILAR TO WOMENS". Today the reader has to list every wall twice, as I did in `engine-run.ts`. When the reader forgets, the engine silently halves the restroom tile: 107.37 SF instead of 214.74.

**Change.** Add `roomRepeat` (count, default 1) to `WALL_INPUTS`, and apply it as `net × roomRepeat` with a step line such as "× 2 rooms (MENS SIMILAR TO WOMENS)". Do **not** call it `repeat`: `wall-finishes.wallcovering` already has a `repeat` input (pattern repeat in inches, read with `qOpt(i, 'repeat')` to round the drop), and `WALL_INPUTS` is spread into wall-tile, frp and wallcovering, so a shared `repeat` count would collide with it and silently change the goods LY. Add a prompt rule to `takeoff-adapter.ts`: when a note says "similar", "typical", "mirror" or "opposite hand", set `roomRepeat` instead of re-listing walls, and keep the two meanings apart in the reader text (`roomRepeat` = rooms, `repeat` = pattern inches).

### 3. Order mode adds 10% waste, and spec attic stock is not modelled (impact: about 28 SF of tile)

In `mode: 'order'` the `wall-finishes` class adds 10%: WT-1 is 158.6 SF, WT-2 51.4, WT-9 58.5 and WT-3 42.3. The estimator carried net. That is correct for comparison, so golden comparisons must use `mode: 'net'`. Spec 09 3000 p282 separately requires **"Furnish 10 percent attic stock of tiling materials"**. That is an owner turnover quantity and not waste, and the engine has no input for it.

**Change.** Add an optional `atticStockPct` to `wall-tile`, also usable by flooring tile. It should produce a separate `ATTIC STOCK - <tag>` line, so it is never folded into waste.

### 4. The scope owner of a wall covering is not captured (impact: 223 SF flagged)

The spec responsibility matrix (01 2200 attachment, p15) lists **"Vinyl wall covering: furnished by Owner, installed by Owner"**. A-170 gives an owner vendor contact for WC-1, and PT-7 says "COORDINATE w/ OWNER VENDOR". The estimator still carried 120 + 103 SF. The engine's `wallcovering` assembly has no furnished-by or installed-by input. Only `assumed` lowers confidence.

**Change.** Add `furnishedBy` and `installedBy` (`contractor | owner`) to `wallcovering`, `frp` and `wall-tile`. When the owner installs, emit the SF line at `confidenceCap: 'low'` with "BY OWNER, VERIFY SCOPE", and suppress the goods (LY) line and the trims. When the owner only furnishes, keep the SF line for install and suppress the goods line. Add a reader rule: check the Division 01 responsibility matrix before carrying a finish.

### 5. Rounding on WC-1 (impact: 1.2 SF)

The engine gives 121.2 SF and the estimator 120.0. Do not change the engine. The difference is the estimator's rounding. The fixture tolerance is 1.5%: at 1.0% the +1.00% delta sits exactly on the boundary and passes or fails depending on float evaluation order.

### 6. Inputs the reader lacks today (no quantity impact here, but they cause misses)

- **Tile on the millwork sheets.** The `takeoff-adapter.ts` playbook text covers tile bands on interior elevations. It does not say that **backsplashes and tiled millwork faces on the A-700 series** are wall-tile records. On this job that is 67.5 SF, 24% of the tile, and none of it is tagged on the finish plan. Add the rule "Every WT-n tag on an enlarged millwork elevation is a wall-tile record. Its length is the dimension-chain bays it spans and its height is the backsplash dimension."
- **Raster finish schedule.** A-170's FINISHES SCHEDULE has no text layer. The MIX %, trims, "48" H" and the PT-7 = primer fact all come from reading the image. The pipeline needs a vision pass on schedule tables that return no text, or it will never populate `blend`, `primerTag` or `topEdge`.
- **Height from the RCP for full-height finishes.** The input description says "floor to ceiling" but does not point to the RCP room tag (`12' - 0"A.F.F.`). Add that to the `height` read string.
- **Measuring to finished faces.** Plan dimension strings run to grid or stud lines: the Meeting Room's 10'-9 1/4" against a 10.3 LF finished wall, and the vestibule's 10'-11 1/2" against 10.1 LF. The `walls` read string should say "finished-face length between corners, not the grid dimension".
- **The `openings` read string invites fixture deductions.** `WALL_INPUTS` asks for "Each door / window / fixture opening inside the band". A model will list WCs, lavs, mirrors, the Keurig and the microwave, which the estimator never deducted. Change it to "doors, windows and pass-throughs that cut the band; do NOT list plumbing fixtures, accessories, mirrors or appliances standing in front of the finish".
- **Stacked wall tags.** Add the reader rule already proposed in 09e (`trades/09e-painting/README.md`, line 85): a stacked wall tag means both treatments on that wall. On A-150 the Gathering Area 103 north wall carries `PT-4 / PT-7` and only PT-4 was measured, so the PT-7 primer and the assumed wall covering it implies (about 10.6 × 10 = 106 SF, V.I.F.) were never carried.
- **FRP from the plumbing schedule.** Wet-wall FRP is sized by the fixture: MSK-2424, "BOTH SIDES", giving 2 × 2'-0". Suggest reading the fixture schedule size when the plan shows FRP only at a fixture.

### 7. Trims and companions (cross-trade, for the other folders)

`topEdge` gives Σ walls − full-band openings. For the restrooms that is 2 × 19.52 = 39.04 LF against line 234 "SCHLUTER TRIM" at 39.55 (−1.3%), which is good. The engine names it "METAL TILE EDGE TRIM", whereas the schedule specifies "SCHLUTER JOLLY J AE". Pass the schedule product through as the item text. The cove trim (line 233, 51.87 LF) and grout GR-3 (line 226, 300 SF against 282.55 SF of GR-3 tile) belong to the flooring folder.

## Recommended fixture set

`fixtures.json` in this folder has 7 line fixtures and 4 cross-checks:
- Lines 235, 236 and 238 use the per-tag sum (`tagArea`).
- Line 237 uses `bandArea`.
- Lines 239, 240 and 241 use run × height.
- The cross-checks are the restroom band with `roomRepeat: 2`, the two backsplashes, and the mix fallback.
- Every `runTimesHeight` fixture takes `{run_lf, height_ft}`; every `bandArea` fixture takes `{walls_ft[], height_ft}`.

Wire them into `tests/quantities/interiors-finishes.test.ts` once items 1 and 2 above exist, in `mode: 'net'`.
