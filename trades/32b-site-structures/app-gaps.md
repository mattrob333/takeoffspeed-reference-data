# App gaps — 32b site concrete and structures vs the TakeoffSpeed quantity engine

**Engine compared:**

- `lib/quantities/trades/site/site-improvements.ts` (wall-footing, cmu-wall, gate, item,
  canopy, pier-footing)
- `trades/site/pavement-marking.ts` (sign)
- `trades/site/site-paving.ts` (concrete: pad / enclosure-slab)
- `trades/site/shared.ts` (`circleSF`, `pierFootingLines`, `footingEarthworkLines`)

**How it was run:** the engine itself, in `mode: 'net'`, on measurement records holding this
job's inputs. The script is `trades/32b-site-structures/scripts/run-engine.ts` and its output
is `engine-out.txt`; it was run with `tsx` and the code was not edited. Order mode adds waste
(concrete 10%, mortar/grout 15%) and purchase rounding. The estimator's quantities are net, so
compare against net mode.

## What it already does right

| Line(s) | Estimator | Engine (net) | Note |
|---|---|---|---|
| 657 transformer pad | 16 SF | 16 SF (`site-paving.concrete` use=pad, assumed=yes → "ASSUMED DETAILS", low confidence) | ✓ |
| 658 cleanout pads | 13.5 SF | 13.5 SF + NO. OF PADS 6 (rects 6 × 18"×18") | ✓ |
| 663 enclosure slab | 384.31 SF | 384.3 SF | ✓ (legend precision) |
| 664 wall footing | 2.682963 CY | 2.683 CY | ✓ |
| 665 / 666 / 667 footing earthwork | 12.502607 / 8.659644 / 3.842963 | 12.5205 / 8.6451 / 3.8754 | +0.14% / −0.17% / +0.84%. The structure (1' working space, backfill = exc − footing − wall below grade, haul = exc − backfill) is the estimator's |
| 668 CMU SF | 289.76 | 289.76 | ✓ |
| 673 coating (finishFaces 1, finishHeight 6'-8") | 241.5874 | 241.4667 | −0.05% (6.67 against 6⅔) |
| 678 gate | 1 EA | 1 EA | ✓ (plus an extra GATE POST 2 EA line; see below) |
| 679 / 707 / 717 counts | 2 / 1 / 1 | 2 / 1 / 1 (`site-improvements.item`) | ✓ |
| 712 canopy | 62 SF | 61.7 SF | −0.48% (estimator rounds to whole SF) |
| 718 light pole bases | 2.786111 CY | 2.7816 CY | −0.16% (exact π) |
| 719 / 720 | 1.966667 | 1.9635 | −0.16%; the buried-only excavation and haul = excavation already match |
| 654 8" sign footings | 0.194444 | 0.1939 | −0.28%; the STOP and DNE records merge into one 5-footing line, as the estimate does |
| 651 12" ADA footing | 0.102407 | 0.1018 | −0.59% |

## What it computes differently, ranked by quantity impact

| # | Line | Estimator | Engine | Δ | Cause |
|---|---|---|---|---|---|
| 1 | 683 weep screen | 11.88 LF | **no line** | −100% | `cmu-wall` has no weep screen or screed output. Physically it should be 36.22 LF; the estimator's 11.88 = 36 × 0.33 looks like an area slip (see below) |
| 2 | 669 grout | 3.245312 CY | 0.872 CY (default: `grout` inferred as `cells` from the vertical bar) / 2.7903 CY (`grout: full`) | −73% / −14% | Default 0.26 CF/SF and cells at 8"/32". The estimator uses 0.3024 CF/SF solid. Neither the engine's cells mode nor the estimator follows S-001 note 4 (cells + bond beam + **all cells below grade**, about 1.22 CY; 1.40 CY if the K.O. block course below the bond beam is a second reinforced course) |
| 3 | 670 mortar | 1.797585 CY | 1.0262 CY | −42.9% | 1.125 units/SF × 8.5 CF/100 units = 0.0956 CF/SF; the estimator uses 0.1675 CF/SF |
| 4 | 652/653, 655/656 sign excavation and haul | 0.102407 + 0.194444 (two pairs) | 0.2957 (one merged pair) | total −0.39%, wrong line split | `pierFootingLines` keys excavation and haul as `${keyBase}:excavation` / `:hauloff` with no diameter or height, so every sign footing type merges into one pair. Concrete keys do carry `kq(D):kq(H)` |
| 5 | 671/672/680/681/682 | 36 LF | 36.22 LF | +0.61% | The estimator rounds the wall LF to whole feet for per-LF accessories |
| 6 | 667 haul | 3.842963 | 3.8754 | +0.84% | Wall below grade 8" × 1'-4" = 1.1924 CY against the estimator's 1.16 CY |
| 7 | Circle areas (651, 654, 718–720) | 2-dp rounded areas | exact π | −0.16% to −0.59% | `circleSF` uses π exactly; the estimator uses round(π/4·round(D,2)², 2) |
| 8 | 665 excavation | 12.502607 | 12.5205 | +0.14% | Depth 2.33 against 2⅓ |

## Extra lines the engine emits that are not in this estimate

These are not errors, but a reconciliation must map them out:

- `site-paving.concrete` adds a concrete CY line for each pad and slab:
  - transformer 0.4938 CY;
  - cleanouts 0.25 CY at 6" (the estimate text says 8", which would be 0.3333);
  - enclosure slab 7.1167 CY.

  The estimate carries these only in SF.
- `site-improvements.gate` adds `GATE POST` 2 EA. The estimate folds the TE2 posts into the gate
  description.
- `pierFootingLines` adds `NO. OF … FOOTINGS` EA lines. The estimate puts the count in the
  description ("NO OF FOOTINGS: 5").
- `cmu-wall` adds CMU units 325.98 EA, #5 vertical rebar 164.27 lb and bond beam rebar
  40.39 lb. These are not in this estimate.
- `pavement-marking.sign` adds the sign and post lines. Those belong to lines 648–650, another
  trade.

## Inputs the engine lacks

1. **Weep screen / screed for site CMU.** Add a `weepScreed` flag (and `weepFaces`) to
   `site-improvements.cmu-wall`. Output: LF = Σ runs × faces.
2. **Below-grade solid grouting.** Add a `solidBelowGrade` length input (1'-4" here) to
   `cmu-wall` for `grout: cells`. Grout SF = below-grade SF + bond beam SF + remaining SF ×
   cell/spacing. This follows S-001 note 4 ("EXCEPT BELOW GRADE") and gives about 1.22 CY
   (1.40 CY with two reinforced courses; see README open item 5).
3. **Per-type excavation and haul keys** for pier footings (see change 3).
4. **A rounding convention for circle areas and dimensions**, needed to reproduce an estimator
   exactly. Today there is no convention hook.

## Concrete changes (ranked by quantity impact)

1. **Add a weep screed output to `cmu-wall`** (flag `weepScreed`, LF = wall LF × faces with a
   weep). Fixture: 36.22 LF. Note: the estimator carried 11.88; keep the fixture for the
   estimator number marked `inferred-unit-slip` and do not copy it as a rule.
2. **Add the estimator's masonry ratios to the `reviewed-commercial` profile** in
   `lib/quantities/profiles.ts`:
   - `site-improvements.cmu-grout-cf-per-sf-full` = 0.3024, with `grout: full` (verified:
     3.2453 CY);
   - `site-improvements.cmu-mortar-cf-per-100-units` = 14.8889, i.e. 0.1675 CF/SF ÷ 1.125
     units/SF × 100 (verified: 1.7976 CY).

   Keep the defaults. Also add `solidBelowGrade` (above), so that the published-standard default
   follows the structural note: about 1.22 CY in place of the current 0.872.
3. **Key pier excavation and haul-off by type:**
   `${keyBase}:excavation:${kq(D)}:${kq(buried)}` and the same for `:hauloff`, in
   `shared.ts` `pierFootingLines`. This keeps lines 652/653 and 655/656 separate, as the
   estimate does.
4. **Add an optional `site-improvements.accessory-lf-rounding` convention** (none | whole-ft) for
   cap, flashing, drip, sealant and bond beam LF. In the reviewed-commercial profile set it to
   whole-ft (36).
5. **Add an optional `site.circle-area-dp` convention.** When set to 2, `circleSF` rounds
   D(ft) and the area to 2 decimals. Profile only; the default stays exact.
6. **Let `footingEarthworkLines` pass the below-grade wall depth explicitly, and let a record
   pass a measured below-grade wall volume.** Minor: +0.84% on haul.
7. **Add an `emitConcreteCY` flag to `site-paving.concrete` for pads** (default on), so a
   reconciliation can match SF-only estimates without deleting lines. Cosmetic.

## Fixture status

`fixtures.json` (31 cases, all at 0.1% tolerance) uses the estimator's conventions; 666/667
take the estimator's 1.16 CY below-grade wall volume as an input. Against the current engine in net
mode:

- **Pass at 1%:** 651, 654, 657, 658, 663, 664, 665, 666, 667, 668, 671, 672, 673, 678, 679,
  680, 681, 682, 707, 712, 717, 718, 719, 720.
- **Fail:**
  - 652/653 and 655/656: values merge across types (change 3);
  - 669 and 670: default conventions (change 2 fixes them with the profile);
  - 683: no line (change 1).
