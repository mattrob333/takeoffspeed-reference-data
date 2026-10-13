# App gaps: concrete (`lib/quantities/trades/structure/concrete.ts`)

## Method

I ran the engine itself on this job's measurement records with `expandMeasurements`, in both `mode: 'net'` and
the default `'order'`. The script is `trades/02-concrete/scripts/engine_run.ts`, run with `node_modules/.bin/tsx`.
The inputs are the legend values and schedule strings listed in `reading-guide.md`. I did not edit the engine.

## What it already does right

With correct records in net mode, the engine reproduces all 15 lines within 1%. The formulas are the same as
the estimator's:

| Line | Engine net | Estimator | Δ |
|---|---:|---:|---:|
| 16 SOG SF (`concrete.slab-on-grade`) | 1917.6 | 1917.6 | 0.00% |
| 17 isolation joint (`concrete.joint`) | 39.2 | 39.22 | −0.05% |
| 18 saw-cut joint | 364.1 | 364.11 | 0.00% |
| 19 WF20 (`concrete.continuous-footing`) | 9.2 | 9.196296 | +0.04% |
| 20–26 spread footings (`concrete.isolated-footing`) | 1.0 / 1.4938 / 6.4815 / 1.7778 / 2.4198 / 1.3827 / 2.1605 | 1.0 / 1.4965 / 6.5 / 1.7733 / 2.4137 / 1.3793 / 2.1667 | −0.29 … +0.25% |
| 27, 28 stem walls (`concrete.stem-wall`) | 9.5704 / 0.5185 | 9.6281 / 0.5226 | −0.60 / −0.78% |
| 29 pad (`concrete.pad`) | 0.0417 | 0.041667 | 0.00% |
| 30 formwork, as Σ of the engine's formwork lines | 602.07 + 808.80 + 3.00 = 1413.87 | 1420 | −0.43% |

Several engine conventions already match this estimator:
- footing formed faces = 2
- spread footing formed sides = 4
- wall formed faces = 2
- no slab-edge form unless `formedEdges` is given
- slab area with no blockout deduction
- WF runs net via `deductRuns`

The item labels also match closely, e.g. `5'x5'x1'2"D ISOLATED FOOTING W/ (5) #5 EACHWAY BARS` and
`8"THK. CONCRETE STEM WALL W/ #4 BARS @ 10" O.C & #4 DOWEL BAR @ 18" O.C`.

## What it computes differently, ranked by quantity impact

1. **Order-mode rounding is applied per footing type, not per pour (+15% CY on foundations).**
   - In `'order'` mode each concrete key gets +5% waste and is then rounded up to 0.5 CY. Footings come out at
     1.5 / 2 / 7 / 2 / 3 / 1.5 / 2.5 = 19.5 CY against 16.72 net (+16.7%).
   - Across all foundation concrete (lines 19–29) that is 41.5 CY against 36.05 net (+15.1%).
   - The 0.0417 CY pad becomes 0.5 CY, 12× its volume.
   - Ready-mix is ordered by pour. Pooled, the same waste would order 37.85 CY, so 38.0 CY.
   - The estimator carries net CY with no waste.
   - **Change:** in `finalizeLines`, keep the net lines per mark. Apply concrete waste and half-yard rounding once on a
     pooled `concrete:<fc>:<placement>` total (e.g. all 3000 psi footings, walls and pads in one pour group), or
     report order quantities for concrete only as a summary line.
2. **Saw-cut joints get 5% waste because of a case bug (+18.9 LF, +5.2%).**
   - `joint.compute` sets `wasteClass: type === 'saw-cut' ? null : 'concrete-accessories'`, but `type = up(str(i,'type'))`
     is `'SAW-CUT'`, so the comparison is never true.
   - The engine orders 383 LF against 364.1 net. Saw-cutting is a labour length with no material to waste.
   - **Change:** compare `type === 'SAW-CUT'`, or compare before calling `up()`. Add a test asserting
     `orderQuantity === net` for saw-cut.
3. **Formwork is split into three keys, and none is rounded to the estimator's 10 SF (−6.1 SF, −0.43%, plus line matching).**
   - The engine emits `FORMWORK REQUIRED - FOOTING` (602.07, which pools WF20 and the spread footings), `- STEM WALL`
     (808.8) and `- PAD EDGE` (3.0).
   - The estimator carries one line, `FORMWORK REQUIRED` = ceil10(Σ) = 1420.
   - **Change:**
     - Add a roll-up option, convention `concrete.formwork-rollup` = `by-element` | `single`, that sums all
       `formwork:*` keys into one `formwork:ALL` line.
     - Add purchase rounding `concrete.formwork-round-sf` (default 1, this estimator 10), applied once on the total.
     - The scorer must otherwise sum the three engine lines before comparing.
4. **The wing-wall thickness reads as printed (+6.7% on line 28 if read literally).**
   - S-201 (at the 6/S-600 "At Wing Wall" callout) and S-600 detail 6 both print `10 3/4"`. The engine would compute 8.4 × 2 × 10.75/12 ÷ 27 = 0.557 CY against the estimator's 0.5226.
   - The engine is right to the drawing, and the estimator simplified.
   - **Change:** none to the math. Add a reconciliation note in the read instruction for `thickness`, along the lines of
     "use the section dimension; estimates often round to the nominal 10" or 12" wall".
5. **Cleanout pads can be double counted across trades (+0.25 CY in Div 03 if the 6 civil pads are pulled in).**
   - `concrete.pad.count` reads "Number of pads of this type on the MEP or architectural plans". On this job line 29 carries
     the 1 plumbing-scope pad from P-302 note 3 ("ALL OUTSIDE CLEANOUTS ... 18"X18"X6"").
   - The 6 C-5.0 sanitary cleanouts already have their pads in site concrete: Div 32 line 658, `18"x18"x8" THK CONCRETE PAD
     FOR CLEANOUT / NO OF PADS: 6`, 13.5 SF (6 × 1.5 × 1.5). Div 33 line 729 carries the 6 cleanouts themselves.
   - **Change:** a cross-trade de-duplication warning. When a note-driven pad count would draw on civil sheets, check
     whether the site-concrete trade already takes pads for the same items, and warn instead of adding them to Div 03.
6. **Spread-footing labels put L ≥ W first (labels only).**
   - The engine prints `10'x5'x1'2"D` and `(5) & (9) #6 BARS TOP & BOTTOM`.
   - The schedule order is LENGTH × WIDTH: `F7040 4'-0" 7'-0"` and `F10050 5'-0" 10'-0"`.
   - The estimator's order is not consistent. Line 25 prints `7'x4'x1'4"D` (W × L, opposite to the schedule) and line 26 prints
     `5'x10'x1'2"D` (L × W, schedule order). Both put the short-way bars first.
   - The quantities are identical.
   - **Change:** no fixed label order can reproduce both lines. The line matcher should compare the dimension set
     ({L, W} plus D) rather than the printed order.
7. **The slab line bundles its ancillaries in this estimate (scoring only).**
   - The engine emits separate lines for concrete CY (23.67), WWF SF, vapor SF, #57 stone CY (23.67) and curing.
   - The estimator carries one SF line whose description names all of them.
   - **Change:** none to the math. The scoring adapter should map `sog:*` to line 16 and not count the ancillary lines
     as extras for this estimator.
8. **Saw-cut label has no depth.** The engine item is `SAW-CUT JOINT`. The estimate says `1" SAW-CUT JOINT`, where depth = T/4 per 3/S-680.
   - **Change:** add an optional `depth` input, or derive it from slab thickness ÷ 4 when the detail says `1/4 "T"`.
     The `width` input should stay for filler width.
9. **Estimator rounding conventions are not modelled (≤ 0.6%).**
   - The estimator rounds ft-in to 2-decimal feet (3'-8" → 3.67) and the stem LF up to 0.5 FT. Together these explain
     every residual from −0.78% to +0.25%. The formwork 10 SF round-up is fitted from one line and is a hypothesis
     (round-to-nearest-10 on the estimator's own 1415.26 SF also gives 1420).
   - **Change:** none. Exact rationals are correct. Keep the scoring tolerance at 1% for this estimator.

## Inputs the engine lacks for this job

- A way to say an **isolation joint is column-blockout only, as distinct from the slab-edge joint filler**. Both are
  `type: 'isolation'` with width 1/2" and would merge into one key. The slab-edge filler is in S-600 and is about 200 LF.
  The estimator carried only the 39.2 LF of blockouts. Add `location: 'column-blockout' | 'slab-perimeter'` to the key.
- **A pour-group or placement input** (footings, walls and slab in separate pours) for item 1.
- **A formwork roll-up and its rounding convention** (item 3).
- **A cross-trade check for pads already taken in site concrete** (item 5).

## Concrete changes, in order of impact

1. Pool concrete order rounding per pour group, not per mark. On this job's foundations the order falls from 41.5 CY (per mark) to 38.0 CY (pooled), a 3.5 CY reduction. Net is 36.05 CY.
2. Fix the saw-cut `wasteClass` case comparison (−18.9 LF), and add a unit test.
3. Add a formwork roll-up with `concrete.formwork-round-sf` (1413.87 → 1420 SF, one line).
4. Add a cross-trade de-duplication warning for cleanout pads already taken in site concrete (Div 32 line 658).
5. Add the wing-wall thickness read note and the isolation-joint `location` key.
6. Match spread-footing labels on the dimension set, not the printed order, and add the saw-cut depth to the label.
