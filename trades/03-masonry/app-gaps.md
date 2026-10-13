# 03 — Masonry: TakeoffSpeed engine vs the estimator

Engine module: `TakeoffSpeed repo: lib/quantities/trades/structure/masonry.ts`
(assemblies `masonry.cmu-wall`, `masonry.veneer`, `masonry.special-course`, `masonry.lintel`).
I ran the engine with `expandMeasurements(QUANTITY_REGISTRY, …)` on this job's inputs, using a
throwaway vitest file that was deleted afterwards. The repo was not edited. Records used:

```
masonry.cmu-wall        runs 157.4', height 1'-4", thickness 4, grout solid, use STEM WALL
masonry.veneer          areas 163.6, 232.1; modular; EXT-1; ADJUSTABLE BRICK TIES 32 x 16; airBarrier FLUID APPLIED VAPOR; weepSpacing 24
masonry.special-course  runs 61.4', 87.9'; rowlock; modular; label 3-1/4"THK. x 3-5/8"H HALF ROWLOCK BRICK
masonry.special-course  runs 61.5', 88.3'; rowlock; modular; label 7-5/8"THK. x 3-5/8"H ROWLOCK SILL
```

## Line-by-line result

| Line | Estimator | Engine net | Engine order qty | Δ net | Engine line key |
|---|---|---|---|---|---|
| 31 CMU stem wall | 209.475 SF | 209.867 | 210 | +0.19% | `cmu:4:solid:-:STEM WALL` |
| 32 Brick veneer | 400 SF | 395.7 | 396 | −1.08% | `veneer:EXT-1:modular` |
| 33 Half rowlock | 149.33 LF | 149.3 | 150 | −0.02% | `course:rowlock:3-1/4"THK. X 3-5/8"H HALF ROWLOCK BRICK:EXT-1` |
| 34 Rowlock sill | 149.86 LF | 149.8 | 150 | −0.04% | `course:rowlock:7-5/8"THK. X 3-5/8"H ROWLOCK SILL:EXT-1` |
| 35 Vapor barrier | 400 SF | 395.7 | **416** | −1.08% net / **+4.0% order** | `barrier:FLUID APPLIED VAPOR` |

**The 395.7 baseline inherits a markup overshoot.** The engine was fed the estimator's legend areas and runs, and the p12 area and both rowlock lines run ≈ 3.5 ft past the NE corner of the East elevation onto blank paper (reading-guide trap 12). An engine that measures strictly from the drawing would produce ≈ 386.5 SF for lines 32/35 (**−3.4% vs 400**, not −1.08%) and ≈ 145.8 / 146.3 LF for lines 33/34 (−2.4% / −2.4%). That is still inside a 5% band, but outside 1%. Scoring a strict engine against this estimate should allow for it rather than tune toward the overshoot.

There was one warning: `EXT1: tie spacing 32" x 16" exceeds 2.67 SF per tie (TMS 402); confirm.` That is correct and useful.

## What it already does right

- **All five estimate lines exist as engine lines** with matching units (SF, SF, LF, LF, SF) and the estimator's section names (`CMU`, `EXTERIOR FINISH`, `ROWLOCK`, `VAPOR BARRIER`). The CMU item text, `4"THK. FULLY GROUTED CMU STEM WALL`, reads like line 31.
- **Physical geometry is right:** CMU SF = Σ runs × height; veneer SF = Σ zone areas − openings; special courses = Σ runs. The veneer input's `read` text says to exclude special courses from the areas, which avoids trap 2.
- **The barrier behind the veneer is the net veneer SF.** This is the estimator's own convention for line 35. The engine also warns not to repeat it in `exterior-cladding.air-barrier`.
- **Tie warning:** it flags the 32" × 16" spacing as over the TMS 2.67 SF limit.
- **Companion lines** the estimator does not carry as quantities: CMU units (236.1 EA), 4" solid grout (0.855 CY), brick units, ties (111.3 EA), mortar cement (35.2 bags) and sand (3.9 CY). These are useful for purchasing, and they don't interfere with the five lines.

## What it computes differently (ranked by quantity impact)

| # | Gap | Impact on this job | Change |
|---|---|---|---|
| G1 | **Waste is applied to the barrier.** `airBarrier` uses waste class `masonry-accessories` (5%), so the order quantity is 416 SF against the estimator's 400 (+4%). The estimator adds no waste to SF finish lines. Line 32 has `wasteClass: null`. | +16 SF on line 35 | Give the barrier line `wasteClass: null` (or a barrier class at 0%, matching `exterior-cladding-barrier` once laps are explicit), so net = order = veneer SF. |
| G2 | **No estimator rounding profile.** The engine gives exact values (209.867, 395.7). The estimator rounds a run LF up to 0.5 FT before × height, writes heights at 2 decimals (1.33), and rounds finish areas up to 5 SF. | line 32 −4.3 SF (−1.08%); line 31 +0.39 SF (+0.19%) | Add masonry conventions `masonry.lf-round-step` (default 0), `masonry.height-decimals` (default exact) and `masonry.finish-area-step-sf` (default 0). Set them to 0.5 / 2 / 5 in the existing `reviewed-commercial` profile in `profiles.ts`, which today holds only framing and board ratios, and apply them to the CMU LF × H product and the veneer SF. The exact value stays the default. Fixtures for both modes are in `fixtures.json`. |
| G3 | **Ties: the spec minimum is not applied.** The engine counts 395.7 × 144 / 512 = 111.3 ties from the drawing spacing and only warns. Spec 04 2113 §3.6.A.5 requires ≤ 24" × 18" **and** ≥ 1 per 2 SF, which gives 197.9 ties: 86.6 more (+78%). | +87 ties (no estimate line) | Add `tieMaxSF` (spec "1 anchor per x SF") and `tieMaxHorizontal` / `tieMaxVertical` inputs. Compute `max(area / spacing area, area / tieMaxSF)` and say which rule governs. |
| G4 | **Half rowlock counted as full brick.** The `special-course` assembly gives 149.3 × 4.5 = 671.9 brick for the half rowlock. It is a 3-1/4"-deep cut piece, so two come from one brick: about 335.9 brick plus cuts. | −336 brick (−8% of the merged 4,017 brick line) | Add `cutFraction` (e.g. 1/2 for half units) or `piecesPerUnit`, and emit a `CUT BRICK` count line. |
| G5 | **Module height.** Modular H = 8/3" (BIA 3 courses = 8"). With the spec's actual 2-1/4" + 3/8" joint, the module is 2.625", giving 6.857 brick/SF and 4.571 rowlocks/LF (+1.6%). This is a convention choice, not an error. | ±1.6% of brick EA | Document it. Allow `jointIn` to override 3/8" vs the BIA module. |
| G6 | **Grout cavity below grade is not modelled.** The `cmu-wall` grout covers the CMU cells only (0.855 CY). "GROUT CAVITY SOLID UP TO GRADE" (S-600, A-430) fills the gap between the CMU/brick and the concrete stem wall over the CMU height. | Unquantified in both | Add a `cavityGroutWidth` input (from the detail) to `cmu-wall` or `veneer`: `CY = runLF × height × width / 27`. |
| G7 | **Flashing and weeps would double-count Div 07.** If the AI fills `baseFlashing` on the veneer record, the engine emits a thru-wall flashing line that the estimator carries in Div 07 (line 187, 213.07 LF). | Up to 213 LF duplicated | Make the `read` text say: leave `baseFlashing` empty when an `exterior-cladding.flashing` record (or Div 07 legend row) already carries thru-wall flashing. Or route the masonry flashing to the 07 section key so the two dedupe. |
| G8 | **Brick EA merges veneer and special courses.** All three records share the key `brick:modular:EXT-1`, so they merge into one 4,016.9 EA line (2,671 + 674 + 672). That is fine for purchasing, but the audit trail per course is lost and G4 is hidden. | presentation | Keep a per-course sub-line, or carry `steps` per source record. |
| G9 | **No CMU-height derivation.** The engine needs `height` typed in. Here it is not dimensioned (2 courses on a detail). | input | Accept `courses` (count × 8") as an alternative to `height`, and add a reading hint: stem-wall depth − brick below grade. |

## Inputs the engine lacks for this trade

- `courses` for CMU height (G9); `cavityGroutWidth` (G6).
- `tieMaxSF`, `tieMaxHorizontal`, `tieMaxVertical` from the spec (G3).
- `cutFraction` / `piecesPerUnit` for half and cut special courses (G4).
- Rounding profile keys (G2).
- A flag that flashing is carried by Div 07 (G7).

## Concrete changes, in priority order

1. Set the veneer barrier line `wasteClass: null` (G1). This is a one-line change and makes line 35 exact once G2 is in.
2. Add an estimator rounding profile (LF up to 0.5 FT, heights at 2 decimals, finish SF up to 5). This makes lines 31, 32 and 35 match exactly.
3. Add spec tie limits and a governing-rule max (G3).
4. Add `cutFraction` on `special-course` (G4).
5. Add cavity grout and a `courses` height (G6, G9).
6. Add a flashing ownership rule between masonry and exterior-cladding (G7).
