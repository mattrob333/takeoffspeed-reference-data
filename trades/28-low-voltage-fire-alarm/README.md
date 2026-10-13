# 28 — Access control, video, intrusion, fire alarm

Division 28 (Electronic Safety and Security) for the Fifth Third Bank, Watson, a 1,900 SF single-storey branch.
The trade has **26 estimate lines (603–628)**, and every one is a device count or a lump-sum marker.
No line in this trade is a length, area or derived quantity. Cable, conduit and boxes for the low-voltage systems are not taken off as lines here. They sit inside one allowance line (622).

| Block | Lines | Estimator section path | Drawing |
|---|---|---|---|
| Security devices, by schedule number | 603–621 (19 lines) | ELECTRICAL SECURITY DEVICES › LIGHT / ACCESS CONTROL / VIDEO SURVEILLANCE / ELECTRONIC DETECTION AND ALARM / MISC. | E-150 (markup p47) |
| Fire alarm wire / cable / conduit allowance | 622 | ELECTRICAL FIRE ALARM DEVICES › ALLOWANCE | E-160 (markup p48) |
| Fire alarm devices | 623–628 (6 lines) | ELECTRICAL FIRE ALARM DEVICES › DIGITAL, ADDRESSABLE FIRE-ALARM SYSTEM / SMOKE-DETECTORS / MANUAL PULL STATIONS / NOTIFICATION APPLIANCES | E-160 (markup p48) |

## Driving sheets

| Sheet | What it gives |
|---|---|
| **E-150 ELECTRICAL SECURITY PLAN** | View 1 is the main building plan and view 2 is SECURITY PLAN REMOTE DRIVE THRU (top-left). Devices are shown as hexagon tags numbered 1–20. The SECURITY DEVICE SCHEDULE (# / DESCRIPTION / WIRE / INSTALLATION REQUIREMENTS) maps each number to a device. Twelve SHEET NOTES apply. |
| **E-160 ELECTRICAL FIRE ALARM PLAN** | Fire alarm symbols on the floor plan, plus eight sheet notes: 110 cd unless noted, lens at least 80" AFF, minimum 1/2" EMT, 14 AWG strobe/horn wiring, and a power supply for every 20 devices or fewer. |
| **E-001 ELECTRICAL LEGEND AND ABBREVIATION** | The FIRE ALARM SYMBOL LEGEND, plus the SECURITY DEVICES and ACCESS CONTROL DEVICE abbreviation lists (CR, ES, DC, MD, KP, HU …). |
| E-702 ELECTRICAL ELEVATIONS (IT room) | Shows the FACP, the DACT and 7 SECURITY PANELs on the plywood backboard. Those items are carried in DIV 26, lines 581 (SECURITY PANEL, 7 EA) and 583 (DACT, 1 EA), and not in this trade. |
| E-703 / E-704 | Mounting heights of card readers and security devices. They are not used for any quantity. |
| E-002 note 22, E-100 auxiliary notes 1–2 | Low-voltage cable may be free-wired and plenum rated above accessible ceilings. It must be in conduit in walls and hard ceilings. J-hooks at no more than 5 ft. |

## Spec sections

| Section | Pages | What it says that matters for quantities |
|---|---|---|
| **28 7210 LIFE SAFETY SYSTEMS** | 465–477 | §1.1.F: Notifier, Edwards or Siemens, intelligent addressable. §1.1.E: 20 % spare transponder capacity. §2.1: all FA wiring in conduit per 26 1000, red J-boxes and conduit. §2.2.E: field charging power supply, 6 A, 60 h standby. **§2.2.F: a ceiling smoke detector within 5 ft of the FACP.** §2.4.F.4 also asks for detectors in telephone and electrical rooms and adjacent to the FACP. The drawn count (1, in ELEC./I.T. 106) governs. It is consistent with both clauses. §2.4.F.4 would also add detectors E-160 does not show (note 1 ties the devices to the base-building system), so flag that as a spec-vs-drawing conflict. §2.3.B: strobes UL 1971, selectable 15–110 cd, mounted on a 4" square box, white lens with red FIRE. Strobes are required in restrooms, break rooms, conference rooms and similar spaces. §2.3.C: dual-action, key-reset pull stations. §2.3.E: 80-character LCD remote annunciator. §2.4.F: photoelectric detector, max 1.875" deep. §2.4.G: duct detectors, none on this job. §2.5: two 12 V batteries. |
| 28 7250 SECURITY SYSTEM | 478–480 | **Boilerplate from another project** ("Office, Warehouse, Fuel and Vehicle Repair", Wells Fargo SMT-4, 12 overhead door contacts …). None of its quantities applies to this bank, and the estimator used none of them. Quantities come only from the E-150 schedule. |
| 26 1000 ELECTRICAL BASIC MATERIALS & METHODS | 452–464 (p457) | Use EMT for fire alarm and telephone raceway. |

## Material types and specified properties

| Item (estimate text) | Symbol / tag | Properties from drawings / spec |
|---|---|---|
| FIRE ALARM CONTROL PANEL | `FACP` box | Microprocessor, addressable, 80-character LCD, dedicated 20 A circuit, top of cabinet ≤ 72" AFF (E-702), Notifier/Edwards/Siemens |
| FIRE ALARM ANNUCIATOR [sic] | `FAA` box | LCD alphanumeric, 80 characters, at main entry |
| FIRE ALARM SMOKE DETECTOR | circled `D` | Intelligent photoelectric, ceiling-mounted, in ELEC./I.T. 106 within 5 ft of the FACP (§2.2.F, §2.4.F.4) |
| FIRE ALARM PULL STATION | boxed `F` alone | Dual-action, non-coded, key reset; one is MOUNTED ON MULLION |
| FIRE ALARM ADA APPROVED HORN/STROBE ALARM | boxed `F` + triangle | Wall-mounted, 110 cd (E-160 note 6), lens 80"–96" AFF, temporal-3, 4" square box |
| FIRE ALARM ADA APPROVED VISUAL ALARM | triangle with `V` | Strobe only, wall-mounted, 110 cd, lens 80"–96" AFF |
| 1 ALARM PANEL *(not in DIV 28)* | hex 1 | (4) 110 VAC duplex. Carried as DIV 26 SECURITY PANEL |
| 2 NETWORK VIDEO RECORDER | hex 2 | (1) 110 VAC quad |
| 3 IP DOME CAMERA – INDOOR | hex 3 | CAT6; single gang box with 2-3/4" round mud ring |
| 4 CARD READER | hex 4 / `CR` | 22/3 pair in banana cable; single gang box 44" AFF, slim mullion box where on a mullion |
| 5 VIDEO MONITOR | hex 5 / `VM` | 110 VAC outlet, RG59 coax; single gang box 86" AFF, serially piped with HUB and IL |
| 6 ELECTRIC STRIKE WITH LBM | hex 6 / `ES` | 18/4 in banana cable; wiring from the card reader |
| 7 MOTION DETECTOR (TO SHUNT DOOR CONTACT) | hex 7 / `MD` | 22/4 banana cable |
| 8 ALARM LAMP/INDICATOR LIGHT | hex 8 / `IL` | 18/2; single gang box 60" AFF |
| 9 360 MOTION DETECTOR | hex 9 / `MD` | 22/4; ceiling box with round mud ring |
| 10 HOLD UP BUTTON | hex 10 / `HUB` | 22/4; teller line has a conduit stub at 18" AFF under the counter |
| 11 TEMPERATURE SENSOR | hex 11 / `TS` | 22/4; 60" AFF (ATM room) |
| 12 DOOR CONTACT | hex 12 / `DC` | 22/2 in banana cable; 1/2" pipe laid into both door frames |
| 13 ALARM KEYPAD | hex 13 / `KP` | 22/4; 44" AFF |
| 14 ANALOG MINIATURE BOARD CAMERA | hex 14 | CAT6 (remote drive-thru) |
| 15 ROOF CONTACT | hex 15 / `RC` | 22/4 |
| 16 360 IP DOME CAMERA | hex 16 | CAT6; box 8'-6" AFF or to the ceiling/canopy; exterior J-boxes at the building corners (note 12) |
| 17 IP MINIATURE BOARD CAMERA | hex 17 | CAT6; 74" AFF |
| 18 ALARM INTERFACE | hex 18 / `AI` | 22/8 |
| 19 NIGHT DEPOSIT | hex 19 / `ND` | 110 VAC, 74" AFF |
| 20 VENUS ROUTER | hex 20 / `V` | No provisions required |

## What the estimator measured

The estimator measured counts only, in EA, in PlanSwift:

- **Markup p47 (E-150):** 21 legend rows. Each row is named with the bare schedule number ("16", "4" …) and gives a count. Row "1" (alarm panel, 1 EA) is not carried in DIV 28; it is the DIV 26 SECURITY PANEL. Row "RFI: Per Sheet Notes 1 and 4, se..." (1 EA) is a placeholder dot on sheet note 1 and is not an estimate line. The 19 remaining rows map one-to-one onto lines 603–621. The estimator wrote each line as `<#>: <schedule description>`.
- **Markup p48 (E-160):** 7 legend rows, and every name is truncated (`FIRE ALARM PULL S...` …). Six are devices (lines 623–628). The seventh, `ALLOWANCE FOR W...` 1 EA, is a dot placed on sheet notes 3/4 and becomes the 1 LS allowance (line 622).
- The estimator measured no lengths, so there is no cable or conduit LF in this trade. The allowance description carries an "AREA: 2000 SF" basis. The same convention appears on the DIV 22, 23 and 26 allowance lines.

## Reconciliation result

- **25 of 26 lines recompute within 5 % (all 25 at 0 %) from the drawings.** The formula inputs are the symbols and tag bubbles printed on the unmarked sheets, not the estimator's dots. Cross-checks were the PDF text layer of the tags, a visual symbol count, and a GPT-6 Astra second reading.
- **Line 619 (18: ALARM INTERFACE) is the one miss: recomputed 3, estimate 2, Δ +50 %.** E-150 shows **3** tag-18 bubbles (main plan 2, drive-thru 1). The estimator dotted only 2 and missed the teller-line `AI`, between the two `HUB` 10s under the transaction bar. The estimate is 1 EA short of the drawing.
- Against the markup legends, all 26 estimate quantities equal the legend rows (p47 row 18 is also 2). That only shows the estimate was copied from the dots. It does not check the dots against the drawing.
- Classifications: 25 counted and 1 allowance (622). The allowance quantity is a 1 LS marker. Its area basis of 2000 SF is the estimator's convention: the 1,900 SF on the title block rounded up to the next 1,000 SF.
- **Duplicate legend names:** page 48 has two rows called `FIRE ALARM ADA AP...`: purple 9.0 EA (horn/strobes, line 627) and yellow 3.0 EA (visual alarms, line 628). A name-keyed extraction once dropped the purple row. It has been restored in `reference/markups/legends.json` and `legends.csv`, flagged `two readers agree (duplicate name restored)`, and 627 is now sourced from that row. Lesson: key legend rows by page + name + colour + quantity, never by name alone.

Fixtures: lines 603–609 and 614–621 use `low-voltage.security-device` (with `section`). Camera lines 610–613 (tags 3, 14, 16, 17) use `low-voltage.camera`, which fixes the section to VIDEO SURVEILLANCE. Lines 623–624 use `low-voltage.fa-panel`, 625–628 use `low-voltage.fa-device`, and 622 uses `low-voltage.allowance` (quantity only; see F4). Every security fixture gives `count` as [view 1 main, view 2 drive-thru].

Files: [`formulas.md`](formulas.md), [`reconciliation.csv`](reconciliation.csv), [`fixtures.json`](fixtures.json), [`reading-guide.md`](reading-guide.md), [`app-gaps.md`](app-gaps.md).

## Verification

An adversarial reviewer (Claude Fable, which also used GPT-6 Astra) raised 8 findings. Each one was re-checked by Claude Opus 5.5, with GPT-6 Astra (`tools/ask_gpt.py`) as an independent second reader on unmarked crops. All 8 were confirmed and fixed. Scratch files are in `trades/28-low-voltage-fire-alarm/scripts/verify/`.

**What was checked**

| Finding | How it was checked | Result |
|---|---|---|
| Tag 18 count (line 619) | E-150 text layer via PyMuPDF: tag `18` sits in the plan at (0.566, 0.361) teller line, (0.492, 0.149) below ND, and (0.169, 0.147) in the drive-thru. The fourth hit, at x 0.333, is the schedule `#` column. On the p47 crops, two are dotted and the teller-line one is not. GPT-6 Astra on unmarked E-150 crops also returned 3. | 3 vs estimate 2. Line 619 is recomputed to 3, Δ +50 %. |
| p48 legend rows | `legends.json` page 48 read in python: 7 items, the 7th purple 9 EA, flagged `duplicate name restored`. `legends.csv` has the same row. GPT-6 Astra on the p48 legend crop listed the same 7 rows. | The "missing row" claim was removed everywhere. The lesson about keying rows is kept. |
| DIV 28 allowance lines | python scan of `lines.json`: the only DIV 28 line containing ALLOWANCE is 622 (FA section, E160). | best-practices §6.4 corrected. |
| Third visual-only strobe room | A-110 text layer has no SHOWER or LOCKER. A-110 and E-160 crops show the V on the east wall of PHONE ROOM 114, plus one in each of MEN'S 112 and WOMEN'S 111. GPT-6 Astra placed it in Phone Room 114. | Room name corrected. The count of 3 is unchanged. |
| L622 fixture | Read `allowanceAssembly` in `lib/quantities/trades/mep/shared.ts`: its only inputs are `area` and `source`. | `areaRoundUpTo` was removed from the fixture, which now asserts 1 LS only, marked `status: proposed-convention`. |
| Camera fixtures | Read `low-voltage.camera` in `low-voltage.ts`: it has no `section` input, and the section is hard-coded to VIDEO SURVEILLANCE. | `section` was dropped from L610–L613, and the README now names the assembly each fixture uses. |
| E-150 notes and tag claims | The E-150 text layer runs SHEET NOTES 1.–12. | best-practices table and §3.1 corrected (19 of 20 tags in DIV 28, 18 of 19 match the drawing). |
| Smoke detector attribution | spec-p471 has §2.2.F (within 5 ft of FACP). spec-p474 has §2.4.F.4 (telephone and electrical rooms, adjacent to FACP). E-160 note 1 ties the devices to the base building. | Reworded: the drawn count governs, both clauses are cited, and the conflict is flagged. |

**Engine run.** All 26 fixtures were run through `expandMeasurements(QUANTITY_REGISTRY, …)` from `TakeoffSpeed repo: lib/quantities` with `tsx`. 26 of 26 produce the expected quantity, unit and item, where an item is asserted. No fixture passes an input its assembly does not declare.

**What changed**

- `reconciliation.csv`:
  - Lines 603–621: the formula input is now the plan bubbles, not the dots.
  - Line 619: recomputed 3, Δ +50.0, note "estimator missed the teller-line AI/18".
  - Line 622: description now matches the estimate text (`ALLOWANCE PROVIDED FOR …`).
  - Line 627: sourced from `legends.json`.
  - Line 628: room set to PHONE ROOM 114.
- `fixtures.json`:
  - Security and camera counts are now given as [view 1, view 2].
  - L619 has `[2, 1]` → 3, with `estimatorQty: 2` and `knownEstimatorDeviation`.
  - `section` removed from the camera fixtures.
  - L622 asserts quantity only.
- `formulas.md`: F1 worked example for 619, the F1 note on the camera assembly, F2 spec check and 628 room, and F4 marked as a proposed convention with the engine's real text.
- `README.md`, `reading-guide.md` and `app-gaps.md`: reconciliation count, legend-row claim, room name, smoke-detector clauses, and the allowance text the engine prints.
- `best-practices.md`: §2 table, §3.1 and §6.4.
- **Reconciliation count: 25 of 26 within 5 %.** Line 619 is the one miss, at +50 %.
