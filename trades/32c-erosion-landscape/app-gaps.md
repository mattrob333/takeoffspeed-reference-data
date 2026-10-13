# App gaps — 32c erosion control, pond, landscaping vs the TakeoffSpeed quantity engine

**Engine compared:**

- `lib/quantities/trades/site/erosion-control.ts`: sediment-barrier, inlet-protection,
  construction-exit, washout, stabilization, linear-practice, fuel-storage.
- `trades/site/landscaping.ts`: plant, mulch, sod.
- `trades/site/site-utilities.ts`: basin (pond area, storage stone, geotextile, underdrain).

**How it was run:** the engine itself, in `mode: 'net'`, on measurement records that hold this
job's inputs. The script is `trades/32c-erosion-landscape/scripts/run-engine.ts` and its output
is `engine-out.txt`. It was run with `tsx`, and the engine code was not edited.

- Scenario A feeds the engine the estimator's own inputs.
- Scenario B feeds the basin the stone-bed floor area, as the engine's input help asks
  ("Delineated basin floor (bottom) area").

## What it already does right

| Line(s) | Estimator | Engine (net) | Note |
|---|---|---|---|
| 684 construction exit | 1570 SF | 1569.4 SF | ✓ (−0.04%; the estimator rounds up). The item text carries the stone size, the underliner and the accessories, as the estimate does |
| 685 washout | 1 EA | 1 EA "7'x7' CONCRETE WASHOUT AREA W/ 10 MIL PLASTIC SHEETING" | ✓ |
| 686 fuel storage | 25 SF | 25.1 SF "… - NO DETAILS" | ✓ (+0.4%) |
| 687 compost sock | 768 LF | 767.9 LF | ✓. Also gives 385 stakes at 2' O.C., which matches F5 |
| 688 RT-B | 5.14 LF | 5.14 LF | ✓ |
| 689–691, 694–696 DS1/DS2/DU | 20298.88 ×3, 15581.92 ×3 | the same, one SF line per practice per phase, coded DS1:/DS2:/DU: | ✓. The stacked-practice rule (F2) is native |
| 697–698 DS3/SS | 2114 ×2 | 2114 ×2 | ✓ |
| 700 DS4 | 14393.68 | 14393.68 | ✓ |
| 701–704 plants | 5 / 11 / 17 / 15 | 5 / 11 / 17 / 15 | ✓. It also warns "AMERICAN HOLLY: schedule 5 vs plan callouts 11" and "EASTERN REDCEDAR: schedule 11 vs plan callouts 6". This is the RFI the estimator missed |
| 705 pine straw | 2500 SF | 2500 SF "PINESTRAW - MULCH A - 3" DEPTH" | ✓ |
| 706 sod | 11500 SF | 11500 SF | ✓ |
| 708 pond area | 3074 SF | 3074 SF "23: PROPOSED STORMWATER POND / BASIN AREA - EARTHWORK IN GRADING QUANTITY" | ✓ |
| 711 storage stone (scenario A) | 626.185185 CY | 626.1852 CY | ✓ when it is given the pond area. Its depth from elevations (435.00 − 429.5) is the estimator's |

## What it computes differently, ranked by quantity impact

| # | Line | Estimator | Engine | Δ | Cause |
|---|---|---|---|---|---|
| 1 | 711 storage stone (scenario B, per the input help) | 626.19 CY | **196.04 CY** | −68.7% | The engine's `areas` input asks for the basin floor, which is the 962.4 SF stone bed. The engine is right and the estimator is wrong (README *What the estimator got wrong*). This is kept as a gap because a test against the estimate will fail. Keep the engine behaviour |
| 2 | 692 SD2-F | 194 LF | **4 EA only** (no LF line) | −100% of the LF | `inlet-protection` makes LF only from `grateSize` (perimeter × n) or `curbOpening` (+ returns). It has no `runs` input for a measured frame or fabric length. 193.7 / 4 = 48.4 LF per inlet is not a grate perimeter |
| 3 | 699 Phase 3 inlet | 194 LF (copy of Phase 2) | 4 EA Sd2-P, no LF | −100% of the LF | The same gap. Also, nothing in the engine carries a practice forward between phases, which is correct. The phase-correct quantity is 74.5 LF of Sd2-P |
| 4 | 709 geotextile | 3074 SF | scenario A **3381.4 SF** (3074 + 10% laps, bottom only, warning "perimeter not given"); scenario B **2304.94 SF** (962.4 + 206 × 5.5 = 2095.4, + 10%) | +10% / −25% | The engine adds the `site-utilities.geotextile-lap-pct` 10% to net, and wraps the sides when it has a perimeter. The estimator uses pond SF with no laps |
| 5 | 710 underdrain | 96 LF | 95.6 LF | −0.4% | The engine does not round (correct). The estimator rounds up |
| 6 | 693 RT-P | 7.0 LF | 7.5 LF | +7.1% | The engine takes the measured run. The estimator's 7.0 is unexplained. Physically it is 1 EA, a 2.25' dia half-round CMP 2.00' high. `linear-practice` has no EA/size form for the half-round retrofit |

## Extra lines the engine makes that the estimate does not carry

The estimator rolls these into the parent line's description. They are correct, but a test
comparing against this estimate should allow them.

| Engine line | Net | Parent line |
|---|---|---|
| CONSTRUCTION EXIT STONE (CY) | 29.063 CY (1569.4 × 0.5 / 27) | 684 |
| GEOTEXTILE UNDERLINER UNDER CONSTRUCTION EXIT | 1569.4 SF | 684 |
| 10 MIL PLASTIC SHEETING WASHOUT LINER | 196 SF ((7 + 2×2.5 + 2×1)²) | 685 |
| WOOD STAKES @ 2' O.C. | 385 EA | 687 |
| STRAW / HAY MULCH, Phase 1 / Phase 2 | 0.932 / 0.7154 TON at an assumed 2 TON/AC, with a warning | 689 / 694. C-2.5 does print "DRY STRAW … 2 TONS PER ACRE", so feed `mulchTonsPerAcre: 2` |
| EROSION CONTROL BLANKET INCL. LAPS | 2325.4 SF (2114 × 1.10) | 698 |
| PINE STRAW (bale purchase) | 2500 SF → bales at 50 SF | 705 |
| Seeding warnings | no seed line without a rate | 690 / 695 / 697. The C-2.4 SEEDING REQUIREMENTS table gives rates (e.g. annual ryegrass 40 LBS/AC) |

## Inputs the engine lacks

1. **A measured `runs` input on `erosion-control.inlet-protection`.** This is needed whenever the
   plan draws the protection rather than dimensioning the grate (lines 692 and 699, 388 LF in
   the estimate).
2. **Phase allocation of shared LOD polygons.** `stabilization` takes areas per record, which is
   enough. The adapter that turns the legend into records must keep both p65
   `DS1, DS2 & DU` rows. Two legend rows with the same name and different swatches are two
   records. Merging them would lose 20,298.88 SF on each of 3 Phase 1 lines.
3. **A half-round pipe retrofit size.** Diameter and height from the sediment storage table, as
   `linear-practice` practice `half-round-pipe-retrofit` with `count`, `diameter` and `height`.
   The output would be EA, plus the CMP LF = height × count.
4. **A stone-bed area that is separate from the pond reference area on `site-utilities.basin`.**
   Today one `areas` input feeds both the reference line and the stone. Line 708 (3074, the pond
   at top of bank) and the stone footprint (962.4) are different polygons. A new
   `stoneBedAreas` input (stone and fabric) is needed, with `areas` kept for the reference line.
5. **A geotextile lap toggle in net mode.** The 10% lap is added to `net`. Other trades keep
   laps and waste out of net. Move the lap into the purchase/order step so that net matches a
   plan quantity.
6. **A cross-trade check for duplicate sod.** `landscaping.sod` and `erosion-control.stabilization`
   (practice sod) can both cover the same lawns: 11,500 + 14,393.68 SF against a site pervious
   area of 20,876 SF. Warn when Σ sod > the site pervious area, which L-1.0 SITE SUMMARY prints.
7. **A sock diameter check.** The record description is free text. The estimate's "30" DIA" came
   from the detail's "30" MIN." stake dimension, while the detail says "AT LEAST 18" DIA". A
   `diameter` input checked against the detail minimum would catch this.

## Concrete changes, ranked by quantity impact on this job

1. **`site-utilities.basin`: add `stoneBedAreas`** (default = `areas`). Stone CY = stoneBed ×
   depth / 27, and geotextile = stoneBed + perimeter × depth. With 962.4 SF this gives 196.04 CY
   instead of 626.19 CY (430 CY of stone), and about 2095 SF of fabric instead of 3074. Keep the
   reference SF line on `areas`. Add a warning when the stone footprint is more than 1.5 times a
   printed "MINIMUM SURFACE AREA" note.
2. **`erosion-control.inlet-protection`: add `runs` (length, many).** Emit an LF line =
   Σ runs, keyed by phase and code, so that 692 = 193.7 LF. For 699, add a warning when a phase
   record's practice code differs from the code on that phase's legend (Sd2-F against Sd2-P).
3. **Legend adapter: never merge same-name rows with different swatches** (p65 DS rows). This
   affects 6 lines × about 15.6k–20.3k SF.
4. **Net-mode laps:** move `site-utilities.geotextile-lap-pct` and `erosion-control.blanket-lap-pct`
   from net to the order quantity. That is +307 SF on 709 and +211 SF on the 698 blanket.
5. **`linear-practice` half-round retrofit as EA + CMP LF** (line 693, 7.0 LF against a physical
   1 EA / 2.00 LF).
6. **Sod overlap warning** across `landscaping.sod` and `stabilization` sod (5,018 SF over the site
   pervious area on this job).
7. **Optional estimator-parity flag** for whole-unit rounding (ceil) on ESPC SF/LF lines. It only
   changes results by ±1 unit (684, 687, 692, 710). This is cosmetic, and the engine's unrounded
   values are better.
