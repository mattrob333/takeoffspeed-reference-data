# TakeoffSpeed engine vs the estimator: wall framing and wall board

Compared against `TakeoffSpeed repo: lib/quantities/`:
`trades/interiors/partitions.ts` (`metal-framing.partition`),
`metal-framing.ts` (`metal-framing.canopy`, conventions), `board.ts`
(`boardFaceLines`, `backerBoardLines`), `gypsum-board.ts` (`wall-board`, `sheathing`,
conventions), `profiles.ts` (`reviewed-commercial`), and `docs/QUANTITY_ENGINE.md`.
All engine-side numbers below were computed in python by applying the engine's own rules
to this job's legend values, with the estimator's two-decimal heights (`trades/09a-wall-framing-drywall/scripts/rebuild3.py`).
The engine was not run or edited.

## What the engine already does right

- **Accessory ratios.** The `reviewed-commercial` profile carries this estimator's house
  ratios: compound 0.53 lb/SF, adhesive 0.031 tubes/SF, tape 0.375 LF/SF on 500 LF rolls,
  screws 0.005357 lb/SF, 32 SF sheets. Routed through `boardFaceLines` with `finish` and
  `adhesive` on, they reproduce lines 243–253 and 261–265. The screw ratio 0.005357 vs
  the exact 3/560 differs by −0.0027% (32.1681 vs 32.168922 lb on line 246).
- **Record = one wall type at one height.** This matches the PlanSwift legend
  (`WALL A3A @ 12'6"H`). Lines aggregate by `stud-wall:size:gauge:spacing` across
  records, the way the estimator sums heights into one line.
- **Stud quantity in SF.** The stud line is framing area (SF), not stick count, and
  the stud count by height appears in the steps, like the estimate's description notes.
- **Faces and layers per record** (`layersA`/`layersB`) can express A-series (2), D-series
  (1), exterior (1) and NO-GWB (0) walls.
- **Top = bottom runner** when no openings are entered and `bottom-track-deduct-doors` = 0.
- **No waste in `net` mode.** The estimator carries no waste (sheets = SF / 32, fractional).

## Where it computes differently (ranked by quantity impact)

| # | Gap | Engine rule | Estimator rule | Impact on this job |
|---|---|---|---|---|
| 1 | Stud SF from rounded stud positions | `framingSF = Σ_runs (ceil(run × 12/s) + runEnd) × H × s/12` (+ jamb, corner studs) | `SF = Σ LF × H` (gross wall area, no extras) | Reviewed profile, one record per legend row: 308 2218.92 (+1.78%), 309 914.16 (+1.80%), 310 348.59 (+8.00%), 311 2695.41 (+1.60%). The default profile (run-end +1) gives +6.51%, +6.16%, +24.49%, +4.83%. Listing individual runs adds up to one more stud per run. |
| 2 | Openings deducted from board | `bandArea` nets every door/window out of each face | no deduction | 7 interior door openings on A-600/p21 (6 × 3'×7' + 1 × 3'4"×7') = 149.33 SF per face, × 2 faces = **−298.7 SF (−4.97%)** on line 242. The same −4.97% flows to its 5 accessory lines. Windows in exterior walls would deduct more. |
| 3 | Specialty boards modelled as a bottom band | `lowerBoardA` = MR board behind tile, up to a band height | Areas measured on enlarged elevations replace standard board: tile → 5/8" **cement board**; painted wet-room walls → **MR**; tech wall → Type X; standard board = gross − those areas | 580 SF of specialty board (255 MR + 285 cement + 40 Type X) cannot be placed by a band height. The band also inverts this job's rule (MR goes *above* the tile here, cement board behind it). |
| 4 | Cement board accessories | `backerBoardLines`: 15 SF sheets, 1.5 screws/SF (EA), mesh tape 0.53 LF/SF on 150 LF rolls, no adhesive, no compound | same five ratios as gypsum (SF/32, 0.031, 0.00075, 3/560, 0.53) | Line 267: 19.0 sheets vs 8.906 (+113%). Line 269: 1.007 rolls vs 0.214 (+371%). Lines 268/271 (8.835 tubes, 151.05 lb) are not produced. Same pattern on 273–277. |
| 5 | Glass-mat sheathing accessories | `sheathing`: `finish:false, adhesive:false`; screws at 1.25 EA/SF unless screw-lb is set | sheets, adhesive, tape, screws, mud at the gypsum ratios | Lines 256 (20.398 tubes), 257 (0.4935 rolls), 259 (348.74 lb) are not produced. |
| 6 | One run feeding two stud lines | one record = one stud size | The 18'8" double wall feeds 3-5/8" (308) and 6" (310); the drawings support this. Line 310 also carries a 6" 9'-0" group (≈5.9 LF) with **no drawing basis**: estimator judgment or a double count of the 12'3" VAT recess wall. | The double wall: 156.8 SF of studs and 8.4 LF each of top and bottom runner are lost unless the adapter emits two records for the row. The 9' group (53.1 SF, 5.9 LF of runner) should *not* be generated from the drawings; it is estimator-specific. |
| 7 | Framed tops need L × span pairs | `metal-framing.canopy`: joists = (ceil(len × 12/s) + 1) × span, plus perimeter track (and fascia) | `LF = ceil(SF) × 12/s` (booth); `LF = ceil5(SF) / 1.33` (canopy); no track line | An area-only legend row (76.2 SF, 416.9 SF) cannot be entered. Illustration only (8'-0" × 9.525' booth assumed): 9 joists × 9.525 = 85.73 LF vs 77 (+11%), plus a perimeter track line the estimate does not carry. |
| 8 | Estimator rounding | none (exact, then purchase rounding in order mode) | specialty areas ceil to 5 SF; parapet sheathing ceil per row; booth area ceil to whole SF; 16" = 1.33 ft | Without them: 248 −7.0% (37.2 vs 40), 272 −4.0%, 260 −0.94%, 266 −0.84%, 312 −1.04%, 254 −0.39% (per-row ceil is fitted to this one line); 313 −0.99% (312.675 vs 315.789). |
| 9 | Accessory line granularity | `joint-tape`, `joint-compound`, `board-adhesive` keys are global; screws key by thickness and layer | one set of 5 accessory lines per board type | Totals match, but the engine merges 5/8" gypsum, Type X, MR and 5/8" cement board screws into one line, and tape/mud/adhesive for all boards into one line each. The estimate has 6 separate sets. |
| 10 | Sheets line | sheets only as purchase rounding in order mode (ceil) | `NO. OF SHEETS` is its own fractional EA line (SF / 32) | 243: 187.652 (estimate) vs 188 (order mode) or no line (net mode). |
| 11 | Documented runner rule | QUANTITY_ENGINE.md says "the estimator's runner LF is stud count × spacing" | runner = Σ run LF | count × 16/12 = 272.0, 85.33, 22.67, 344.0 → +0.55%, +1.23%, −5.56%, +0.88%. Σ LF gives −0.47% to −2.08%. The code (segment LF = L when there are no openings) is already right; with windows entered, `runners-per-segment` adds cripple-row track the estimator does not carry. |

## Inputs the engine lacks

- **Height from the legend item name.** `@ 12'6"H`, `@ 4'4" HT`, `@ 1'7"H` should be parsed
  from the PlanSwift row name; the plan carries no heights. To mimic this estimator, round
  parsed heights to 0.01 ft (4'-4" = 4.33, 18'-8" = 18.67; see formulas.md).
- **Faces from the tag grammar and name suffixes.** A-620 Table A series (A = 2 faces,
  D = 1) plus `1 SIDE`, `BS` / `BS GWB`, `NO GWB`, `SHTNG ONLY`, `EXT` (interior face only).
- **Specialty-area replacement.** An input listing elevation-measured areas by board type
  (`TYPE X GWB 37.2`, `PT1 WALL PAINT 252.6 → MR`, `WT* WALL TILE → cement board`). Each
  is deducted from the standard board of the same wall group.
- **Dual-use rows.** A way to say one run carries two stud sizes, each with its own line
  (the double-stud wall `6" & 3-5/8" METAL STUD @ 18'8"H`).
- **Area-only framed tops.** Booth and canopy framing as SF with spacing, in addition to
  L × span pairs.
- **Gauge by height.** S-002's exterior stud schedule picks gauge and spacing by wall-height
  band, wind zone and deflection limit (L/360 at EIFS, L/600 at masonry). The band uses the
  full stud length: wall + parapet rows that are one continuous 17'-4" stud fall in the
  16'-6" to 20'-0" band (800S162-68). The estimator flattened every exterior stud to 16 GA,
  and the engine takes gauge as free text. See reading-guide trap 11.

## Concrete changes (in order of quantity impact)

1. **Add a stud-area convention** (e.g. `metal-framing.stud-area-rule`: `positions` |
   `wall-area`). Set `wall-area` (`SF = Σ LF × H`, no run-end, jamb or corner studs) in
   `reviewed-commercial`. Keep the per-height stud count as a step only. Fixes lines
   308–311: +1.6…+8% becomes −0.04…−0.56%.
2. **Add `gypsum-board.deduct-openings`** (default 1, set 0 in `reviewed-commercial`). The
   same flag should govern `wall-board` and `sheathing` openings. Fixes the −4.97% on 242
   and its accessories.
3. **Add a specialty-area input on `metal-framing.partition` / `gypsum-board.wall-board`**:
   `replaceAreas = "TYPE X 37.2; MR 252.6; CEMENT BOARD 282.6"`. Emit each as its own board
   line and subtract the total from the standard board (formula F3). Add a profile rounding
   `gypsum-board.specialty-area-round-sf = 5` (ceil) for those lines (F4).
4. **Let the profile choose the accessory set for cement board and glass-mat**: a convention
   `gypsum-board.accessories-for-all-boards = 1` routes backer and sheathing through
   `boardFaceLines` with `finish` and `adhesive` on, at the gypsum ratios (F6). Fixes
   +113% / +371% on 267/269 and the six missing lines.
5. **Adapter: emit two records for dual-use rows**, meaning names that contain `&` between
   two stud sizes. This recovers 156.8 SF of studs and 8.4 LF each of top and bottom runner.
   Do not add a "parapet-over-wall" rule that turns `PARAPET WALL @ 7'2"H A310` into a lower
   6" 9' wall. The drawings show no such wall: the 6" VAT wall is the separate 12'3" row.
   The estimate's 9' group (53.1 SF) is estimator judgment, not a drawing-derived quantity,
   so a drawing-faithful engine will be −16.5% on line 310.
6. **`metal-framing.canopy`: accept `areaSF`** with `LF = ceil(SF) × 12/s`, and the profile
   options `canopy-area-round-sf = 5` and `spacing-ft-1.33 = 1`. Make the perimeter track
   optional (`metal-framing.framed-top-track = 0` in the profile). Fixes 312/313 exactly.
7. **Per-board accessory keys** (`joint-tape:${board}`, `joint-compound:${board}`,
   `board-adhesive:${board}`, screws keyed by board name), so the output matches the
   estimate's line granularity.
8. **Emit a fractional `NO. OF SHEETS` line** (SF / sheet SF) in `net` mode when the
   profile asks for it.
9. **Correct QUANTITY_ENGINE.md**: runner LF = Σ run LF on this job, not stud count × spacing.
10. **Screw ratio exactly `3/560`** in the profile (Q.of accepts fraction strings): a
    cosmetic −0.0027%.
11. **Parapet sheathing rounding**: `gypsum-board.sheathing-round-per-run = 1` (ceil each
    row to whole SF) gives 658, but it is fitted to this one line and nothing else in the
    job corroborates it. Leave it off by default; the unrounded sum is −0.39%.
