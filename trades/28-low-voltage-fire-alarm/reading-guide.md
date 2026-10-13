# Reading guide: 28 low voltage, security and fire alarm

## Which sheets, in what order

1. **E-001 legend.** Read it first.
   - The FIRE ALARM SYMBOL LEGEND (about x 0.55–0.78, y 0.30–0.50 of the sheet) defines the symbols:
     - `F` box plus a triangle is the ADA horn/strobe.
     - A triangle with `V` on a stem is the ADA visual alarm.
     - A boxed `FACP` or `FAA` is the panel or the annunciator.
     - A circled `D` is the smoke detector. With a tick it is wall-mounted; without one it is ceiling-mounted.
     - A boxed `F` alone is the pull station.
     - A boxed `D` is the duct smoke detector.
   - The SECURITY DEVICES and ACCESS CONTROL DEVICE lists give the abbreviations `CR`, `ES`, `DC`, `MD`, `KP`, `HU` and so on.
2. **E-150 ELECTRICAL SECURITY PLAN.** Two views:
   - View 1, ELECTRICAL SECURITY PLAN, at 1/4" = 1'-0".
   - View 2, SECURITY PLAN REMOTE DRIVE THRU, a small view at the top-left (x < 0.25).

   The SECURITY DEVICE SCHEDULE sits at the bottom centre. Its columns are `#`, `DESCRIPTION`, `WIRE (FOR REFERENCE SEE NOTE A)` and `INSTALLATION REQUIREMENTS`. The 12 SHEET NOTES are on the right.
3. **E-160 ELECTRICAL FIRE ALARM PLAN.** One plan view with 8 sheet notes on the right.
4. **E-702 IT-room elevation.** Use it only to see what DIV 26 already carries: 7 SECURITY PANELs, the DACT, the FACP on the backboard and the data rack.
5. **Spec 28 7210** (pp. 465–477) covers system type and placement rules. **Ignore spec 28 7250** (pp. 478–480). Its quantity tables are boilerplate for a warehouse and vehicle-repair campus.

## How each input is read

### Security device tag counts (F1)

- Each device is a **hexagon with a number**. Most hexagons also have a two-letter box beside them, for example `CR` with `4`, `ES` with `6`, `MD` with `7` or `9`, `HUB` with `10`, `AI` with `18`, `ND` with `19`, `KP` with `13`, `RC` with `15`, `TS` with `11`, `V` with `20`, `VM` with `5`, `IL` with `8` and `DC` with `12`.
  - **Count the numbers, not the letter boxes.** `MD` serves both tag 7 (shunt motion) and tag 9 (360 motion). There are 9 `MD` labels on the sheet but 10 motion detectors. `HUB` also appears as a word inside the schedule text.
- The schedule number is the item. The estimator writes the line as `"<#>: <DESCRIPTION>"`, with the description copied verbatim from the schedule: `"7: MOTION DETECTOR (TO SHUNT DOOR CONTACT)"`, `"6: ELECTRIC STRIKE WITH LBM"`, `"16: 360 IP DOME CAMERA"`.
- **Read both views.** View 2 holds 14 (ANALOG MINIATURE BOARD CAMERA), one 16, and one 18 with its `AI` box.
- Text-layer check: tag numbers in the plan area, excluding the schedule `#` column at x ≈ 0.331 and the view titles. The counts are 1:1, 2:1, 3:8, 4:5, 5:2, 6:4, 7:5, 8:2, 9:5, 10:5, 11:1, 12:2, 13:1, 14:1, 15:1, 16:10, 17:1, **18:3**, 19:1, 20:1, for 60 in all.
- Exclude tag 1 ALARM PANEL. It is carried in DIV 26 as SECURITY PANEL (E-702).

### Fire alarm counts (F2, F3)

- On E-160 every horn/strobe has a text `F` beside a triangle. Pull stations have a text `F` and no triangle. There are 11 `F` glyphs, which is 9 horn/strobes plus 2 pull stations.
  - At the NE exit the horn/strobe and the pull station sit side by side and read as a double `F F` box. That is one of each.
  - The second pull station is the boxed `F` at the entry storefront, labelled `MOUNTED ON MULLION`.
- Visual-only strobes (`V` in a triangle) are vector graphics, not text. Count them on the image: one in each restroom (MEN'S 112, WOMEN'S 111) and one on the east wall of PHONE ROOM 114 (A-110; on E-160 it is the hatched room with a single chair, below the JAN. mop sink), 3 in all.
- `FD` in the two restrooms is the architectural **floor drain** underlay. It is not a fire device.
- The circled `D` in ELEC./I.T. 106 is the only smoke detector. The drawn count governs. It is consistent with spec 28 7210 §2.2.F (within 5 ft of the FACP) and §2.4.F.4 (electrical and telephone rooms, adjacent to the FACP). §2.4.F.4 also lists rooms that E-160 does not cover, so flag that conflict. No duct detectors are drawn.
- FACP: the boxed text with a leader, in the IT room. FAA: at the entry vestibule.

### Allowance (F4)

- There is one dot on the markup, on E-160 notes 3/4, in the legend row `ALLOWANCE FOR W...`. The line text is `ALLOWANCE PROVIDED FOR WIRE, CABLE & CONDUIT FITTINGS / AREA: 2000 SF`.
- The area basis comes from the title block `1,900 SF`, rounded up to 2000. DIV 22, 23 and 26 use the same 2000.

## Notes that set properties (not quantities)

| Note | Text, summarised | Effect |
|---|---|---|
| E-150 note 1 / 4 | "SECURITY DEVICES SHOWING ON THIS SHEET IS FOR COORDINATION PURPOSES ONLY…", "NOT ALL DEVICES MAY BE USED" | Raised as the RFI legend row on p47. The estimator still counted every device. |
| E-150 note 2 | EC provides raceways, boxes and pullstrings; security cabling is by the security vendor | No security cable LF |
| E-150 note 5 / 6 | All cables plenum rated; J-hooks 6' o.c. | Covered by the allowance |
| E-150 note 7 | 3/4" EMT with bushing plus a 2-gang backbox at every alarm-activating device, ATM, night deposit, CCTV, card reader and wall device | Rough-in, covered by the allowance |
| E-150 note 12 | Exterior J-box for each 360 camera at the building corners | No separate line |
| E-160 note 2 | Strobes ≥ 80" AFF; proper boxes, no extension rings; flex to a J-box labelled "F/A" | — |
| E-160 note 3 | 14 AWG stranded for strobes and horns; Belden 8760 for speakers; minimum 1/2" EMT | Covered by the allowance |
| E-160 note 4 | Power supply at no more than 20 devices each | 12 notification appliances → 1 supply. Not carried as a line. |
| E-160 note 6 | **110 candela unless otherwise noted** | Candela for lines 627 and 628 |

## Cross-checks

- **Legend vs plan:** compare every p47 and p48 legend quantity with the tag or symbol count on the unmarked sheet. Here every device line agrees except tag 18 (plan 3, legend and estimate 2).
- **Text layer vs image:** `F` glyphs = horn/strobes + pull stations. Hexagon numbers per view = security tags.
- **Code sanity:** each restroom has a visual strobe (spec §2.3.B.6.c). There is a smoke detector at the FACP. Pull stations are at the exits: 2 here, at the NE exit and the main entry.
- **Doors vs card readers:** 5 `CR` tags against DIV 08 card-reader doors (lines 192: 2, 193: 1, 195: 1 pair). Only 4 `ES` because one reader door has no strike. Do not expand doors into strikes, contacts and REX devices. Count the schedule tags.
- **Cross-trade:** the 7 SECURITY PANELs, the DACT and the data rack are on E-702, which DIV 26 counted (lines 581, 583, 586). Do not count them again in 28.
- Second opinion: GPT-6 Astra read the unmarked E-160 and E-150 crops independently. It got HS 9, V 3, PS 2, SD 1, FACP 1, FAA 1, and the same 20 tag counts, including 18 = 3 (main 2 + drive-thru 1).

## Traps hit on this job

1. **Truncated duplicate legend names.** The p48 legend has two rows called `FIRE ALARM ADA AP...`: purple 9.0 EA (horn/strobe) and yellow 3.0 EA (visual). A name-keyed extraction once dropped the purple row. It is now restored in `legends.json` / `legends.csv`, flagged `duplicate name restored`. Key legend rows by page + name + colour + quantity, never by name alone.
2. **Bare-number legend names.** On p47 the rows are named only `16`, `4`, `3` and so on. Map them to the schedule on the same sheet before matching estimate text.
3. **Missed device in the markup.** The teller-line `AI` (18), between two `HUB` 10s under the transaction bar, was not dotted. The estimate has 2 alarm interfaces and the drawing has 3.
4. **Remote drive-thru view.** It holds 14 (the only analog board camera), a 16 and an 18. It is easy to skip because it is drawn small at the top-left.
5. **Boilerplate security spec.** Section 28 7250 lists quantities (12 overhead door contacts, 100 cards, Securitron mag locks) for a different facility. Using it would invent devices.
6. **Repeated letter boxes.** `MD` ≠ one device type, and `HUB`, `CR` and `ES` also occur in notes or the schedule. Count hexagon numbers inside the plan views only.
7. **Floor drains `FD`** on E-160 come from the architectural background.
8. **Tag 1 and the RFI row** are on the p47 legend but have no DIV 28 lines. Tag 1 belongs to DIV 26. The RFI row is a question, not a device.
