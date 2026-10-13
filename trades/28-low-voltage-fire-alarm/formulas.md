# Formulas — 28 low voltage / fire alarm

Every line in this trade is a count, so the formulas are counting rules. What makes a count correct is which symbols are counted, in which views, and what is excluded. The numbers below are from this job and were computed in python (`trades/28-low-voltage-fire-alarm/scripts/build.py`, `count_tags.py`).

---

## F1. Security device by schedule number (lines 603–621)

- **Name:** `security-device-count` (app: `low-voltage.security-device`; the fixtures for cameras 3/14/16/17 use `low-voltage.camera`, which hard-codes the section `VIDEO SURVEILLANCE` and has no `section` input)
- **Inputs:**
  - `tag`: schedule number as printed in the hexagon (text, 1–20)
  - `description`: SECURITY DEVICE SCHEDULE description, copied exactly (text)
  - `section`: estimator section (choice; see the table below)
  - `count[]`: bubbles of that number per plan view (EA), one value per view: E-150 view 1 (main) and view 2 (REMOTE DRIVE THRU)
- **Rule:** `Qty (EA) = Σ_views count(tag)`. Item text = `"<tag>: <DESCRIPTION>"`.
- **Exclusions:**
  - The `#` column of the schedule.
  - The view-title numbers (`1`, `2`) and the sheet-note numbers.
  - Tag **1 ALARM PANEL**, which is carried in DIV 26 from E-702 as SECURITY PANEL.
  - Any **RFI** legend row.
- **Section convention** (the estimator's, reproduced exactly by the app's `section` choices):

| Section | Tags |
|---|---|
| LIGHT | 8 |
| ACCESS CONTROL | 4, 6, 12, 15 |
| VIDEO SURVEILLANCE | 2, 5, 3, 14, 16, 17 |
| ELECTRONIC DETECTION AND ALARM | 7, 9, 10, 11, 13 |
| MISC. | 18, 19, 20 |

- **Worked example (line 612, 16: 360 IP DOME CAMERA):** main plan 9 + drive-thru 1 = **10 EA**. Estimate 10. Δ 0 %.
- **Worked example (line 611, 14: ANALOG MINIATURE BOARD CAMERA):** main 0 + drive-thru 1 = **1 EA**. This device appears only in view 2. If view 2 is skipped, the line is lost.
- **Worked example (line 619, 18: ALARM INTERFACE):** the inputs are the bubbles printed on the plan, not the estimator's dots. Main plan 2 (the `AI` below `ND` and the teller-line `AI` between the two `HUB` 10s) + drive-thru 1 = **3 EA**. Estimate 2. Δ +50 % (recomputed vs estimate). The estimator dotted only 2 on markup p47 and missed the teller-line `AI`. Fixture L619 carries `count [2, 1]` → expected 3, with `estimatorQty: 2` and a `knownEstimatorDeviation` note.

Per-tag results (estimate = markup legend p47 = drawing, except tag 18):

| Tag | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | Σ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Estimate | 1 | 8 | 5 | 2 | 4 | 5 | 2 | 5 | 5 | 1 | 2 | 1 | 1 | 1 | 10 | 1 | 2 | 1 | 1 | 58 |
| Drawing | 1 | 8 | 5 | 2 | 4 | 5 | 2 | 5 | 5 | 1 | 2 | 1 | 1 | 1 | 10 | 1 | **3** | 1 | 1 | 59 |

The drawing shows 60 bubbles in all. The difference to the estimate is tag 1 (DIV 26) and the teller-line tag 18.

---

## F2. Fire alarm device by symbol type (lines 625–628)

- **Name:** `fa-device-count` (app: `low-voltage.fa-device`)
- **Inputs:**
  - `deviceType`: from the symbol *shape* against the E-001 FIRE ALARM SYMBOL LEGEND
  - `count[]`: symbols per FA plan sheet (EA)
  - `candela`: E-160 note 6 = 110 cd unless noted
- **Rule:** `Qty (EA) = Σ_sheets count(symbol type)`. The symbol key:

| Symbol | Type | E-160 count | Line |
|---|---|---|---|
| boxed F + triangle | horn/strobe | 9 | 627 |
| triangle with V | visual-only strobe | 3 | 628 |
| boxed F, no triangle | pull station | 2 | 626 |
| circled D | ceiling smoke detector | 1 | 625 |
| boxed D | duct detector | 0 | — |

- **Text-layer check:** count of `F` glyphs = horn/strobes + pull stations. On this job that is 11 = 9 + 2 (verified).
- **Spec check:** the drawn count (1) governs. The one detector is in ELEC./I.T. 106 beside the FACP, which is consistent with both 28 7210 §2.2.F (a ceiling detector within 5 ft of the FACP) and §2.4.F.4 (detectors in telephone and electrical rooms and adjacent to the FACP). §2.4.F.4 would also put detectors in other rooms that E-160 does not show (E-160 note 1 ties the devices to the base-building system). That is a spec-vs-drawing conflict to flag, not a reason to add devices.
- **Worked example (627):** the 9 horn/strobes are at:
  - the top-centre recess
  - the NE room (beside a pull station)
  - the corridor under the restrooms
  - the IT room
  - the conference room
  - the wall east of the IT room
  - two at the lobby/kiosk wall
  - the entry vestibule beside the FAA

  That gives **9 EA**. Estimate 9. Δ 0 %.
- **Worked example (628):** MEN'S 112 + WOMEN'S 111 + the east wall of PHONE ROOM 114 (A-110) = **3 EA**. Estimate 3.

---

## F3. Fire alarm panel items (lines 623–624)

- **Name:** `fa-panel-count` (app: `low-voltage.fa-panel`)
- **Inputs:**
  - `description`: FIRE ALARM CONTROL PANEL / FIRE ALARM ANNUCIATOR
  - `count[]`: the boxed `FACP` / `FAA` on E-160 (EA)
- **Rule:** `Qty (EA) = count`. Count each panel once across sheets. The FACP is drawn again on the E-702 IT-room elevation. Do not add that one.
- **Worked example:** FACP 1 → **1 EA** (623). FAA 1 → **1 EA** (624). The DACT (E-702) is a fire alarm panel accessory but is carried in DIV 26 line 583, so it is not repeated here.

---

## F4. Low-voltage wire / cable / conduit allowance (line 622)

- **Name:** `lv-allowance` (app: `low-voltage.allowance`)
- **Inputs:**
  - `area`: building gross SF (title block `1,900 SF`; slab legend p33 = 1917.6 SF)
  - `roundUpTo`: 1,000 SF (estimator convention). This is a **proposed** convention (`low-voltage.allowance-area-roundup-sf`), not an engine input. `low-voltage.allowance` declares only `area` and `source`.
- **Rule:** `Qty = 1 LS`. Description: `ALLOWANCE PROVIDED FOR WIRE, CABLE & CONDUIT FITTINGS / AREA: <ceil(area / roundUpTo) × roundUpTo> SF`.
- **Convention basis:** all four MEP/LV allowance lines carry `2000 SF`: 403 (DIV 22), 445 (DIV 23), 510 (DIV 26) and 622 (DIV 28). ceil(1900/1000) × 1000 = **2000**. ceil(1917.6/1000) × 1000 = 2000 as well. A 500 SF step also gives 2000, so the step size cannot be pinned from this one job. 1,000 is the simplest rule that fits.
- **Scope covered:** no FA or security cable, conduit, J-box or J-hook line exists in DIV 28. Sheet notes E-150 #2 / #6 / #7 and E-160 #2 / #3 describe that work (3/4" EMT stubs with 2-gang backboxes, J-hooks at 6 ft, 1/2" EMT for FA, 14 AWG). All of it is covered by this single allowance.
- **Worked example:** area 1,900 SF → 1 LS, "AREA: 2000 SF". Estimate 1 LS. Δ 0 %. The current engine gives the same 1 LS but prints `ALLOWANCE PROVIDED FOR LOW-VOLTAGE WIRE, CABLE & CONDUIT FITTINGS / AREA: 1,900 SF`. Fixture L622 therefore asserts only 1 LS and carries `status: proposed-convention (low-voltage.allowance-area-roundup-sf)`.
- **Classification:** allowance. The quantity is reproducible (1). Its value is a judgment and is not on any drawing.

---

## What is *not* a formula on this job

| Item | Why it has no estimate line |
|---|---|
| Smoke detectors from coverage (900 SF per detector) | The design is drawn. Coverage would give ceil(1900/900) = 3, against 1 actually drawn. |
| FA cable LF and security cable LF | Covered by the allowance. Cable is "by security vendor" (E-150 note 2). |
| Backboxes, bases, mud rings, FA power supply (E-160 note 4) | Not taken off as lines. Rough-in is in the allowance or the DIV 26 boxes. |
| Access-control door kits (REX, power supply, controller) | The estimator copies the numbered schedule devices only. |
