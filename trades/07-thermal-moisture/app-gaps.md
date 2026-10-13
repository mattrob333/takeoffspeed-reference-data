# App gaps: TakeoffSpeed quantity engine vs the estimator (07 thermal and moisture protection)

Engine files compared:

- `lib/quantities/trades/structure/roofing.ts` (low-slope, tapered, sheet-metal, curb, walkway, counted)
- `insulation.ts` (batt, rigid, spray-foam, firestop)
- `sealants.ts` (joint, opening, acoustic)
- `exterior-cladding.ts` (finish, air-barrier, flashing, trim)
- `interiors/partitions.ts` (cavity insulation and head/base sealant)
- `interiors/windows-storefront.ts` (perimeter sealant, sill flashing)
- `masonry.ts` (thru-wall flashing)

The numbers below come from this job's inputs, in `mode: 'net'` (no waste or packaging).

## What the engine already does right

| Estimate line | Engine assembly | Result |
|---|---|---|
| 152, 153, 155, 156 cavity batts | `partitions` (insulation over the full framing height; `insulation.cavity-to-ceiling` = 0) | LF × H matches when no openings are given: 427.5 / 355.0 / 112.7 / 2642.4 |
| 165 roof VB | `roofing.low-slope` `vaporBarrier` + `vaporBarrierAssumed` | field area 2149.7, capped at low confidence (matches "ASSUMED") |
| 164 crickets, 167 walkway | `roofing.tapered` areas, `roofing.walkway` areas | 262.1 / 286.8 |
| 168–170 copings, 175–177 flashings, 183 fascia | `roofing.sheet-metal`, `exterior-cladding.trim` | LF = Σ runs, with splice plates as a bonus |
| 172 hatch curb | `roofing.curb` (count 1, 30" × 36") | 11 LF |
| 173, 174 | `roofing.counted` | 11 / 3 EA |
| 178–182 EIFS / ACM | `exterior-cladding.finish` | areas match (only ceil5 presentation differs, ≤ 5 SF) |
| 185–187 sills, aluminium flashing, thru-wall | `exterior-cladding.flashing`, `masonry.veneer` `baseFlashing` | Σ runs |
| 188 sill pan | `windows-storefront.storefront` sill flashing = W − door widths | same rule as the estimator's 24.4 LF "Linear" run |
| 151 XPS, 157 and 160 rigid | `insulation.rigid` (areas + runs × height) | can express 2305.2, 115 and 890 when given the right inputs |
| 150 / 189 duplicate | aggregation by trade + key + unit | the engine reports 221.9 once. **This is correct; the estimator double-counted** |

## Where it computes differently (ranked by quantity impact)

1. **Roof insulation SF per layer (line 159, +3729 SF).** `roofing.low-slope` emits `field × layers` per thickness. RT1 (3 × 2")
   gives 3 × 1864.3 = **5592.9 SF of 2" polyiso**. The estimator carries **1864 SF** of "MIN. 6"THK. POLYISO R-34". Both are valid
   units, but scoring and display break.
   *Change:* add `insulationReport: 'per-layer' | 'per-stack'` (default per-stack for scoring). Keep the per-layer boards in `purchase`.

2. **Membrane (line 162, −187 SF, −6.2%).** The engine computes field + parapets × (one `parapetHeight` + 12" top lap) + walls × 8"
   + curbs × 8". It takes a **single** parapet height per record, and it adds a 12" lap on top of measured lap heights. With this
   job's runs: 2149.7 + (43.3 × 3.083 + 56.5 × 2 + 87.8 × 4.5 = 641.6) + 45.3 × 0.667 + 50.9 × 0.667 = **2855.4**, against **3042.8**.
   It also has no input for the canopy-edge wrap. Detail 10/A430 calls for 4" min. over the edge: 138.5 LF × 4/12 = 46.2 SF.
   The estimator's own total cannot be rebuilt either. The measured rows (field + laps + high-low × 2' + edge × 4") give 2740.5,
   which leaves about 302 SF of line 162 unexplained (`formulas.md` F8). With developed heights and the 4" wrap, the engine would
   land near 2740.5, not 3042.8. Score this line against the measured rebuild and report the residual; do not tune the engine to it.
   *Change:* accept `flashings: [{ runs, developedHeight }]` (the PlanSwift "PARAPET LAP @ h" rows), with no extra lap when the
   height is a developed height. Add `edgeWraps: [{ runs, girth }]` for canopy and roof edges, with the girth taken from the membrane
   note in the detail, not from the fascia. Let the high-low wall take "lap roof 2' incl. wall" as a developed height.

3. **Acoustic sealant (line 148, +53.5 LF, +5.1%).** `partitions` emits (head + base) × finished faces. That gives
   4 × 149.2 (A walls) + 2 × 49.7 (D) + 4 × 26.0 (low walls) + 2 × 153.4 (exterior) = **1107.0** before door deductions
   (about 1064.3 after the base beads across 7 doors), against **1053.5**. Counting the beads drawn on the A-620 details
   (head + base per finished face, no head bead on partial-height walls) gives 4 × 149.2 + 2 × (49.7 + 26.0 + 153.4) = **1055.0**
   (+0.14%). The whole engine excess (52 LF) is the head bead it puts on the 26.0 LF of low walls. The estimator also takes no door deduction.
   The other fit (4 × interior + 1 × exterior = 1053.0) contradicts D-B01. Neither rule is confirmed.
   *Change:* do not put a head bead on walls that stop below structure or the ceiling (a `partialHeight` flag or the height letter),
   and make the door-base deduction a convention. Keep faces × (head + base) for full-height walls.

4. **Opening sealant (line 149, about 1330 LF, allowance).** `windows-storefront` emits 2 faces × perimeter less door sills, and
   `doors-hardware` adds door frames when `sealantFaces` is given. Glazed units here come to 2 × (419.1 − door widths), and
   7 interior doors × 2 faces = 238.7. The estimator instead carried a round 1330 LF, which fits 910 trim LF (assumed) + 419.1.
   Do not chase this number. Expose it as `allowance` with low confidence, and score the measured parts separately.

5. **Cover board (line 163, −92 SF, −4.7%).** The engine emits cover board on the field only (1864.3). The estimator also covers the
   high-low wall face: 46 × 2 = 92.
   *Change:* let `walls` / `flashings` runs carry `coverBoard: true`, or add `coverBoardWallRuns` (LF × height).

6. **High-low (transition) wall as one assembly (lines 154, 157, 163, part of 162, about 299 SF across lines).** The engine has no
   record for a roof step wall that emits batt (LF × 2'), rigid (LF × 2'6"), cover board (LF × 2') and membrane (LF × 2')
   together. Today each needs a separate record.
   *Change:* add `roofing.transition-wall` with inputs runs, wall height and over-top extension. It emits the four lines plus
   blocking (2x4 and 2x6 LF = run, lines 91/92).

7. **Curb barrier (line 166, +20 SF, +50%).** `roofing.curb` emits `barrier` = LF × curb height = 39.9 × 1.5 = **59.85**. The
   estimator used a 1 ft strip (40).
   *Change:* add `barrierHeight` (default the curb height) and note the estimator convention.
   Also: `roofing.curb` **requires count + L × W** (`count`, `size`, `height`), but the estimator measured curb perimeter LF (39.9) on the plan.
   Let `roofing.curb`, and its `barrier` emission, take a measured perimeter (`perimeters`, LF, many). `roofing.low-slope` already
   accepts curb perimeters as LF (`curbs`, many) for the membrane flashing and so already uses the 39.9 LF row. Only `roofing.curb` has this gap.

8. **Fluid-applied barrier returns (line 184).** `exterior-cladding.air-barrier` adds a 6" return around every opening by default
   (`exterior-cladding.opening-return-in`). The estimator adds no returns and uses the **rounded** cladding lines plus the canopy
   ceiling sheathing (568.5). If the 9 exterior glazed frames are passed (A, B, C, D, E × 2, F, G, H; 344.4 LF), the engine adds 344.4 LF × 0.5 = 172 SF (+5.8%).
   The two exterior doors (100 in frame B, 110 in frame F) sit inside those frames, so their perimeters are not added again.
   *Change:* make returns opt-in (they are carried in the self-adhered flashing lines on this job).

9. **XPS conditional (line 151).** `insulation.rigid` computes it correctly, but there is no way to mark "where required, zone > 4"
   as an alternate.
   *Change:* support a `conditional` or `alternate` flag on records, with low confidence.

10. **8" batt in parapets (line 156, 656 SF).** The engine gives batt on whatever partition record carries `insulation`. If the reader
    attaches batt to parapet records (as the estimator did), the result matches. If it omits it, the result is −24.7%.
    *Change:* add a reading rule: parapet framing above the roof deck carries the wall's batt only when the section shows it.
    Score both ways.

## Inputs the engine lacks

- **Rounding conventions.** `ceil5` on cladding and sheet-metal LF/SF, `round1` on insulation SF, `ceilFt` on short runs. These cause
  deltas of up to 5 SF / 1.5 LF per line (13.9 → 15 is +7.9% on line 168).
  *Change:* add a `presentationRounding` per waste class in `mode: 'estimator'`, kept separate from purchase rounding.
- **Developed-height flashing runs** (see 2) and **edge wraps by girth** (girth from the membrane note, e.g. 4" at 10/A430).
- **Curb perimeter LF** (see 7).
- **The unnamed "Linear" row.** It needs a reading-time classification (this one was the sill pan).
- **Cross-line derivations.** Line 160 is line 181 + line 32, and line 184 is lines 178–181 + line 85. The engine computes these from
  areas, which is better. It needs no link to other lines, but the fixture expected values depend on rounding before summing.

## Concrete changes, ranked by quantity impact on this job

| # | Change | Lines | Approx. impact |
|---|---|---|---|
| 1 | Per-stack roof insulation reporting | 159 | 3729 SF (unit mismatch) |
| 2 | Developed-height flashings + edge wraps in `roofing.low-slope` | 162 | engine 2855.4 is 115 SF over the measured rebuild 2740.5 (extra 12" laps on measured heights); 187 SF under the estimator, whose 302 SF residual is unexplained |
| 3 | `roofing.transition-wall` assembly | 154, 157, 163, 162 | 299 SF |
| 4 | Opt-in air-barrier opening returns | 184 | up to 172 SF |
| 5 | No head bead on partial-height walls (+ door-base deduction convention) | 148 | 52 LF |
| 6 | `roofing.curb` `perimeters` + `barrierHeight` | 166, 171, 177 | 20 SF |
| 7 | Presentation rounding (ceil5 / round1) in estimator mode | 14 lines | ≤ 5 per line |
| 8 | Alternate/conditional flag (XPS zone note) | 151 | 2298 SF at stake |
| 9 | Allowance marking for opening sealant | 149 | 1330 LF (no measurable basis) |
