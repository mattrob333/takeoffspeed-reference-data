# App gaps — 28 low voltage / fire alarm vs TakeoffSpeed engine

The engine code compared is `TakeoffSpeed repo: lib/quantities/trades/mep/low-voltage.ts` together with `trades/mep/shared.ts`. It covers the assemblies `fa-device`, `smoke-coverage`, `fa-cable`, `access-door`, `data-drop`, `camera`, `pathway`, `fa-panel`, `security-device`, `av-device` and `allowance`. I also checked the tests in `tests/quantities/mep-low-voltage.test.ts`.

## What it already does right

- **`low-voltage.security-device`** reproduces lines 603–621 exactly when the reader records one entry per schedule number:
  - The item text comes from `tagged(tag, description)`, for example `"16: 360 IP DOME CAMERA"`. That is the estimator's format character for character.
  - The `section` choices are `ACCESS CONTROL`, `VIDEO SURVEILLANCE`, `ELECTRONIC DETECTION AND ALARM`, `MISC.` and `LIGHT`. These are the estimator's five sections, including `LIGHT` for tag 8 and `MISC.` for tags 18–20.
  - `count` is many-valued, so view 1 and view 2 (the remote drive-thru) are summed: 9 + 1 = 10 for tag 16.
- **`low-voltage.fa-device`** reproduces lines 625–628:
  - The read text says to take the type "from the symbol shape … never from the bare F text". On E-160 a bare `F` belongs to both the horn/strobe and the pull station, so this matters.
  - With `description: "ADA APPROVED HORN/STROBE ALARM"` the item is `FIRE ALARM ADA APPROVED HORN/STROBE ALARM`, which is the estimator's text.
- **`low-voltage.fa-panel`** is a counted pass-through, so the FACP (1) and the FAA (1) match.
- **`low-voltage.allowance`** gives 1 LS with the area printed in the description and confidence capped low. Its quantity matches line 622.
- **`low-voltage.smoke-coverage`** is labelled DESIGN-BUILD and capped at low confidence. It is correctly kept out of jobs with a drawn layout.

All 26 lines can be reproduced with existing assemblies and no new math. Line 619 reproduces the drawing (3), not the estimate (2); see gap 7.

## Where it computes differently, ranked by quantity impact

| # | Gap | This job's numbers | Impact |
|---|---|---|---|
| 1 | **Legend/markup ingestion merges rows with the same truncated name.** On p48 the rows `FIRE ALARM ADA AP...` 9.0 EA (purple) and 3.0 EA (yellow) collapse into one. The reference extraction once dropped the 9 EA row this way. It is restored in `legends.json`/`legends.csv` (flagged `duplicate name restored`). | 9 horn/strobes would be lost from the source set | −9 EA (−100 % on line 627) for any benchmark or adapter that keys on name |
| 2 | **`access-door` expansion** when the reader records the 5 card-reader doors as doors. It emits 5 readers, 5 strikes, 5 REX motion, 5 contacts, 5 lock power supplies (2 purchased) and 5 controllers (3 purchased). The estimator copies the schedule: 5 CR, 4 ES, 2 DC. Tag 7 (MD to shunt the door contact) is already a scheduled device, so the REX line double-counts it. | strikes 5 vs 4 (+25 %), contacts 5 vs 2 (+150 %), REX +5 duplicating line 614, PS +5 net, controllers +5 net | about +19 EA of lines that are not in the estimate |
| 3 | **`fa-device` kit lines.** Every device adds a backbox line, and detectors add a base line. The estimator carries none of these; rough-in is inside the allowance or in the DIV 26 boxes. | 9 + 3 + 2 + 1 = **15 backboxes** + **1 base** | +16 EA of lines with no estimate equivalent |
| 4 | **`smoke-coverage` used on a drawn layout** would replace 1 detector with ceil(1900/900) = 3. | 3 vs 1 | +2 EA (+200 %) on line 625 |
| 5 | **`fa-cable` allowance** with no home runs gives devices × 40 LF + 2 × 1 ft slack per device. The estimator carries no cable LF; it is in the allowance (line 622). | 15 field devices → 630 LF (NAC only: 504 LF) | +630 LF line not in the estimate |
| 6 | **Camera guidance conflicts.** `camera` says "cameras go here, not in low-voltage.security-device", but the test records tag 16 through `security-device`. The keys differ (`camera:16: …` vs `item:VIDEO SURVEILLANCE:16: …`), so a reader that follows both texts emits both lines and nothing deduplicates them. | tags 3/14/16/17 = 20 cameras | up to +20 EA (+100 % on lines 610–613) |
| 7 | **Teller-line alarm interface.** A faithful reading of E-150 gives 18 = 3, but the estimator has 2. The engine is right against the drawings and wrong against the estimate. | 3 vs 2 | +1 EA (+50 % on line 619). Keep the engine result and flag it as an estimator miss, not a defect. |
| 8 | **Cross-trade double counts.** `fa-panel`'s description lists "DACT, NAC POWER SUPPLY". E-702 (DIV 26 line 583) already carries the DACT. E-160 note 4 implies 1 NAC power supply (12 appliances ≤ 20) that the estimator did not carry. Tag 1 ALARM PANEL is DIV 26 SECURITY PANEL (line 581, 7 EA). | DACT +1, NAC PS +1, alarm panel +1 | +1 to +3 EA |
| 9 | **RFI legend row.** p47 `RFI: Per Sheet Notes 1 and 4, se...` 1 EA is a question placeholder. A legend-driven adapter would make a device line from it. | 1 | +1 EA |
| 10 | **Allowance area text.** The engine prints the area as read and with its own covers text: `ALLOWANCE PROVIDED FOR LOW-VOLTAGE WIRE, CABLE & CONDUIT FITTINGS / AREA: 1,900 SF`. The estimator writes `ALLOWANCE PROVIDED FOR WIRE, CABLE & CONDUIT FITTINGS / AREA: 2000 SF`, rounding up as on DIV 22/23/26/28. Fixture L622 asserts quantity only until the convention exists. | 1,900 vs 2000 in the description, plus `LOW-VOLTAGE` | 0 on quantity; the description differs |
| 11 | **Candela.** The engine warns when candela is missing. E-160 general note 6 sets 110 cd unless noted. If it is read, the item becomes `… HORN/STROBE ALARM - 110CD`, but the estimator's text has no candela. | — | 0 on quantity; the item text differs |

## Inputs the engine lacks

- A **"schedule present" switch** for security and access control. When a numbered SECURITY DEVICE SCHEDULE exists, `access-door` should refuse or warn, and every device goes through `security-device`.
- An **`excludeToTrade` / `carriedBy`** input, or a cross-trade rule, for items on IT-room elevations: SECURITY PANEL, DACT, FACP drawing repeats.
- A **view tag** on each count (`E-150/1`, `E-150/2`) so a missing remote view shows up as a coverage gap. Line 611 lives only in view 2.
- An **allowance area rounding** convention (see change 5).
- A **kit-lines toggle** (`low-voltage.fa-kit-lines`) for estimators who do not take off FA backboxes and bases.

## Concrete changes, in priority order

1. **Adapter or benchmark:** key PlanSwift legend rows by `(page, name, colour, quantity)`. Never key on the truncated name alone. The reference data already carries both page-48 rows (the purple 9 EA row restored). Use this page as the regression case.
2. **`access-door`:** add a guard. If any `security-device` record on the same sheet has a CR/ES/DC/REX-like description, emit an error instead of the expansion, or have the prompt pick exactly one path. Also add a test that 5 doors plus schedule tags 4/6/7/12 do not double-count.
3. **`fa-device`:** add the convention `low-voltage.fa-kit-lines` (default `on`, house style `off`). With it off, only the device line is emitted. That matches lines 625–628 exactly and removes 16 phantom EA.
4. **Camera path:** choose one. Either `camera` handles tags 3/14/16/17 and `security-device` rejects descriptions matching `/CAMERA/`, or the reverse. Fix the `security-device` test that records `16: 360 IP DOME CAMERA` through it.
5. **`allowance`:** add the convention `low-voltage.allowance-area-roundup-sf = 1000`, which prints `ceil(area / 1000) × 1000`. It is observed on 4 MEP/LV allowance lines in this job (403, 445, 510, 622).
6. **`fa-panel`:** remove DACT from the description, or warn "DACT / security panels on IT elevations may be carried in DIV 26 room-item". Add a per-job dedupe for the same tag across E-160 and E-702.
7. **Legend adapter:** drop rows whose name starts with `RFI` and rows for schedule numbers that map to another trade (tag 1 ALARM PANEL → DIV 26).
8. Keep the faithful reading for tag 18 (3), but emit a reviewer note when a markup-legend count disagrees with the plan count. This job is the regression case: line 619, estimate 2, drawing 3.
