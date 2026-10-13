# App gaps: TakeoffSpeed engine vs this estimate

Engine files compared:
- `lib/quantities/trades/fitout/equipment.ts` (`equipment.scheduled-item`)
- `lib/quantities/trades/fitout/furnishings.ts` (`furnishings.window-shade`, `furnishings.furniture`)
- `lib/quantities/trades/fitout/shared.ts` (`countOf`, `responsibilityOf`)
- the playbooks in `lib/trade-playbooks/fitout.ts`

## What it already does right

- **Furniture by tag** (`furnishings.furniture`). It takes the plan count when one exists. When a tag is on the schedule but not placed (`scheduledOnly`), it applies `furnishings.unplaced-scheduled-qty` = 1 EA, marks it V.I.F. and caps confidence at low. This is exactly the estimator's F2 convention. Given the plan counts, all 57 furniture lines reproduce at Δ 0 %, provided the reader attaches the one unsuffixed `SS-03` placement to SS-03B (the drawn 95.5 in three-seat sofa) and marks SS-03A `scheduledOnly`; see row 4.
- **Suffix tags are separate products** ("SS-03A — suffixes are separate tags"). That matches the estimate's 03A/03B, 02L/02R, 04L/04R, 07A/07B, TB-03A…D, TB-04A/B and TB-05A…D lines.
- **Appliance counts by tag** (`equipment.scheduled-item`, `prefer: 'schedule'`, plan count when there is no QTY). This reproduces AE-02/03/04/06/07 and the remote teller terminal at 1 EA each (Δ 0 %).
- **Shade as run LF × drop in SF**, with the run LF kept in the description: `MOTORIZED ROLLER SHADE (n LF)`. This is the estimator's structure. Its read instruction, "head of glazing (or shade pocket) to sill … not room ceiling height", is also the right reading of the drawings.
- The responsibility label is carried, not dropped, which suits the vendor/GC row AE-07.

## What it computes differently (with numbers)

| # | Line(s) | Estimator | Engine as written | Δ |
|---|---|---|---|---|
| 1 | 345 shade | 74.025 LF × **16 ft** = 1184.4 SF | Runs 73.76 LF × drop read from the drawings. At A-311's two storefront heads (10'-0" section 1, 12'-0" section 3), read per run: 737.6–885.1 SF (861.0 SF with 10'-0" at Employee Lounge and Transaction Bar only). At spec 2.4 B head-to-sill: 540.9 SF (10'-0" head) to 688.4 SF (12'-0" head). At each run's ceiling height: 855.1 SF | −37.7 % to −25.3 % / −54.3 % to −41.9 % / −27.8 % |
| 2 | 345 description | "(75 LF)" = ceil of the run | "(73.76 LF)", exact rational | text only |
| 3 | 337 AE-01 | 1 EA (scheduled, not placed) | `countOf` with no count, no `scheduleQty` and no `vif` option **throws "no quantity"**, so no line is produced | −1 EA (−100 %) |
| 4 | 357/358 SS-03A/B | 357 SS-03A 1 EA by the V.I.F. convention (not drawn); 358 SS-03B 1 EA counted (the one `SS-03` placement, a 95.5 in three-seat sofa) | Each record takes its own count. The reader attaches the placement to SS-03B by drawn width and seat count and marks SS-03A `scheduledOnly`, giving 1 + 1. The engine already handles this; it is a reading task, not an engine gap | 0 |
| 5 | not carried: AE-09…AE-15 (7 rows), BE-01…BE-11 (14 rows) | excluded (VENDOR / VENDOR) | The engine and playbook say vendor/vendor rows are "never dropped" and are listed as placeholder lines. That adds up to 21 lines the estimate does not have. AE-09, AE-10 and AE-13 have A-160 placements | +21 lines (quantity 0 impact on carried lines, but the line-match score suffers) |
| 6 | not carried: SS-05 (TBD, unplaced), TB-08 (by millworker) | excluded | `furnishings.furniture` with `scheduledOnly` would carry each at 1 EA V.I.F. | +2 EA |
| 7 | 346–402 responsibility | OFCI from General Note K | The furniture schedule has no PROV. BY / INST. BY columns, so `responsibilityOf` returns UNSTATED with a warning unless the reader passes `furnishedBy: OWNER VENDOR` from note K | label only |
| 8 | 356, 359, 363, 365, 380, 381, 386 item text | SIZE text re-keyed with changes (SS-01 D/W swap, ST-02 `18"7/8"D`, WS-01 feet to inches, CH-09 17.25", SS-02L/R `'` corrected to `"`, SS-07B 16.5" SH) | `SIZE: ${up(size)}` from the schedule string, so it prints A-170 as drawn | text only; quantity Δ 0. Score these as estimator deviations, not engine misses. The engine should also flag the schedule's own typos (SS-02L/R `16.5' SH`, CH-08 `35.4"D`, CH-11 `30"SH`) rather than silently correct them |

## Inputs it lacks

1. **A shade drop convention.** `drop` is a required read with no fallback. A house value (this estimator: 16 ft) cannot be set, and nothing warns when drop × LF gives an area per LF above the storefront head height.
2. **A scheduled-but-unplaced path for equipment.** The `vif` option exists only in `furnishings.furniture`.
3. **An exclusion rule** for rows that are TBD and unplaced, and for rows furnished by another trade (MANUFACTURER = MILLWORKER, "SEE SHEET A-708"). Also a scope policy for VENDOR / VENDOR rows: list them as placeholders, or omit them as this estimator did.
4. **General-note responsibility inheritance.** Note K should be one record-level input applied to every furniture tag, not one per tag.
5. **Run-length rounding for the description.** This is display only: ceil to a whole foot.

## Concrete changes, ranked by quantity impact

1. **Shade drop (299–644 SF on line 345, the only non-count line).** Add the convention `furnishings.shade-drop-ft`. Default it to unset, meaning use the read drop. A company can set it (16 to reproduce this estimator). When both exist, warn if `drop_read` and the convention differ by more than 10 %. Also warn when `drop` exceeds the storefront head **at that run** (A-311 gives 10'-0" in section 1 and 12'-0" in section 3, entry vestibule), not against a single 12'-0" value. Fixture: `shade-sf-run-x-drop`, 74.025 × 16 = 1184.4 SF.
2. **Equipment V.I.F. path (1 EA, line 337).** Give `equipment.scheduled-item` the same `scheduledOnly` flag and the convention `equipment.unplaced-scheduled-qty` = 1 EA (confidence low). Fixture: AE-01 gives 1 EA.
3. **Exclusion and scope filter (2 EA furniture plus 21 vendor lines).** Add `excluded` reasons to the furniture and equipment records: `TBD-unplaced`, `by-other-trade` (MILLWORKER), `vendor-furnished-installed`. Emit no line, and record the exclusion in `steps` and the coverage notes. Make the vendor/vendor policy a setting, `equipment.vendor-rows: 'placeholder' | 'omit'`. This estimator uses `omit`.
4. **Description LF rounding.** `ceil(run_LF)` in the item text ("(75 LF)") while `net` keeps the exact SF.
5. **Inherited responsibility.** Accept `furnishedBy` / `installedBy` from a general note once per schedule (A-110 note K: OWNER VENDOR / GC) so that 57 furniture lines don't each warn UNSTATED.
