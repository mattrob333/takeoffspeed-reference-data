# App gaps — 26 Electrical vs. `lib/quantities/trades/mep/electrical.ts`

The engine module has 15 assemblies (luminaire, device, disconnect, panel,
conduit, feeder, grounding, site-light, generator, branch-allowance,
transformer, meter-junction, room-item, misc, allowance). Compared here
against the 108 estimate lines in `mode: 'net'`.

## Already right

- **Counts by tag / variant, summed by sheet** (`countTotal`, `count` many per sheet):
  matches F1 for the 96 counted lines: fixtures (luminaire), receptacles, switches,
  data, sensors (device), meter, junction boxes, hot box (meter-junction),
  IT room items (room-item), push buttons, power packs, pitch pocket (misc),
  panels (panel).
- **Linear fixtures by run length** (luminaire `lengths`): G 26.78, L 30.36,
  UC 9.13 LF reproduce exactly.
- **Emergency variants as separate items** (`emergency` flag): matches AE/FEM/GEM/JE/TE/X1–X3.
- **Plate notes keep variants apart** (device `plate`, `furnishedBy`): the estimator splits
  black / engraved / furnished-by-others variants the same way.
- **Allowance as 1 LS with the area in the description** (`allowanceAssembly`), capped at low
  confidence. The undrawn branch wiring is not invented.
- **Panels**: one per schedule with voltage, phase, amps, main. Matches 588/589.

## Computed differently (ranked by quantity impact)

| # | Item | Estimator | Engine today | Difference |
|---|---|---|---|---|
| 1 | Conduit bundles (505–508, 601, 602) | 279.62 LF of **route** | `net = Σ runs × conduits` = 617.54 LF | **+120.8%** (+337.92 LF). (2) 4": 203.42 vs 101.71; (4) 3/4" IMC: 78.44 vs 19.61 |
| 2 | Site pole lights (495, 496) | 5 EA (pole assemblies) | site-light luminaire line = poles × headsPerPole = 1×1 + 4×2 = 9 EA heads (pole line 5 EA) | **+80%** on the luminaire line; the pole line matches |
| 3 | Boxes, rings and plates | 16 EA of explicit box lines (575–578, 599, 600) | device adds a box + ring/plate line for each of 118 wall-box devices (receptacles 71, switches/controls 30, data 17) | about 118 boxes + 118 rings + ~101 plates with no estimate counterpart; correct as material but not in this estimator's breakdown |
| 4 | Allowance basis area | 2,000 SF | area "as printed" = 1,900 SF | −5% in the description; quantity 1 LS both |
| 5 | Disconnects without a rating (553 = 6, 559 = 3) | carried by legend name ("DISCONNECT SWITCH") | disconnect requires `amps`, `poles`, `fused`; no rating means no line | 9 EA missing unless every rating is read (E-101 has `30/25 3R`, `100/90 3R`; the E-130/E-704/M-503 ones have none printed) |
| 6 | Attic stock | not carried (C = 53) | not carried | same (good). No input to add it when a contractor wants to; +10 EA C, +10 UC |

## Inputs the engine lacks

1. **Conduit LF basis**: a convention `electrical.conduit-lf-basis` = `route` | `conduit`
   (default `conduit`; the reviewed-commercial profile sets `route`). With `route`, the
   main line is route LF labelled "(n) size …". Couplings, terminations and straps still
   use `× conduits`.
2. **Disconnect without a printed rating**: make `amps`/`poles`/`fused` optional. When
   missing, emit "DISCONNECT SWITCH (RATING PER EQUIPMENT)" with a warning and no fuse
   line. Add `serves` from mechanical sheets (M-503).
3. **Site light count basis**: a convention `electrical.site-light-count` = `heads` |
   `assemblies`. With `assemblies`, the luminaire line is per pole and keeps "2HEAD,
   180°" in the description.
4. **Boxes/plates as separate lines**: a convention `electrical.device-box-lines` = `on` |
   `off`. Off under the reviewed-commercial profile: boxes ride with the device, and only
   called-out boxes (cut-in, 4" square, deep double-gang, 1-gang, 3-gang recessed) are lines.
5. **Allowance basis rounding**: `allowance.basis-round-sf` (default 0 = as printed;
   reviewed profile 500), applied the same way in plumbing, HVAC, electrical, low voltage.
6. **Attic stock**: optional `atticStock` count on luminaire (from schedule notes), off
   by default, labelled when used.
7. **Cross-sheet dedup hint**: a `sameAs` field on count records ("page 87 repeats E-010"),
   so a reprinted sheet doesn't add twice. The model needs it more than the code does.
8. **Hand-entered quantity flag**: when a PlanSwift legend row is `NAN`, the record should
   carry `count: unknown`. That gives a "Measurement not computed" flag, not 0 and
   not 1 (lines 497, 541).

## Concrete changes (ranked by quantity impact)

1. `electrical.conduit`: add `electrical.conduit-lf-basis`; set `route` in the
   `reviewed-commercial` profile. Fixtures 505–508, 601, 602 in `fixtures.json` expect
   route LF. **Fixes 337.92 LF (−55% of the engine's conduit LF).**
2. `electrical.site-light`: add `electrical.site-light-count`. Fixtures 495/496 expect
   assemblies. **Fixes 4 EA (+80%).**
3. `electrical.device`: add `electrical.device-box-lines`, off in the reviewed profile.
   **Removes ~337 box/ring/plate lines** that have no counterpart in this estimate.
4. `electrical.disconnect`: optional rating, as above. **Recovers 9 EA** (553, 559) that
   today fail for a missing required input.
5. `allowanceAssembly`: basis rounding convention. Shared with 22/23/27.
6. Reading prompt (catalog `read` strings): "fixture type = text before the comma on
   E-130 (`C,i` → C)", "count M-503 / mechanical control details for electrical devices",
   "a reduced reprint of a sheet is not a second count", "NAN legend rows are unknown".
