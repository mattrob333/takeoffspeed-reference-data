D='/home/user/takeoffspeed-reference-data/trades/28-low-voltage-fire-alarm/'
def sub(fn, pairs):
    t=open(D+fn).read()
    for a,b in pairs:
        assert t.count(a)==1, (fn, a[:70], t.count(a))
        t=t.replace(a,b)
    open(D+fn,'w').write(t)

sub('formulas.md', [
("- **Worked example (line 619, 18: ALARM INTERFACE):** the estimator dotted 2 (night-deposit `AI` + drive-thru `AI`). The drawing has 3 (+ teller-line `AI`). Rule result on the drawing = 3. Estimate = 2. Δ +50 % against the estimate. The fixture keeps the estimator's dotted inputs `[2]`.",
 "- **Worked example (line 619, 18: ALARM INTERFACE):** the inputs are the bubbles printed on the plan, not the estimator's dots. Main plan 2 (the `AI` below `ND` and the teller-line `AI` between the two `HUB` 10s) + drive-thru 1 = **3 EA**. Estimate 2. Δ +50 % (recomputed vs estimate). The estimator dotted only 2 on markup p47 and missed the teller-line `AI`. Fixture L619 carries `count [2, 1]` → expected 3, with `estimatorQty: 2` and a `knownEstimatorDeviation` note."),
("- **Spec check:** smoke detectors ≥ 1 within 5 ft of the FACP (28 7210 §2.2.F). This job has exactly 1, in the IT room next to the FACP.",
 "- **Spec check:** the drawn count (1) governs. The one detector is in ELEC./I.T. 106 beside the FACP, which is consistent with both 28 7210 §2.2.F (a ceiling detector within 5 ft of the FACP) and §2.4.F.4 (detectors in telephone and electrical rooms and adjacent to the FACP). §2.4.F.4 would also put detectors in other rooms that E-160 does not show (E-160 note 1 ties the devices to the base-building system). That is a spec-vs-drawing conflict to flag, not a reason to add devices."),
("- **Worked example (628):** 2 restrooms + 1 shower/locker alcove = **3 EA**. Estimate 3.",
 "- **Worked example (628):** MEN'S 112 + WOMEN'S 111 + the east wall of PHONE ROOM 114 (A-110) = **3 EA**. Estimate 3."),
("  - `roundUpTo`: 1,000 SF (estimator convention)",
 "  - `roundUpTo`: 1,000 SF (estimator convention). This is a **proposed** convention (`low-voltage.allowance-area-roundup-sf`), not an engine input. `low-voltage.allowance` declares only `area` and `source`."),
("- **Worked example:** area 1,900 SF → 1 LS, \"AREA: 2000 SF\". Estimate 1 LS. Δ 0 %.",
 "- **Worked example:** area 1,900 SF → 1 LS, \"AREA: 2000 SF\". Estimate 1 LS. Δ 0 %. The current engine gives the same 1 LS but prints `ALLOWANCE PROVIDED FOR LOW-VOLTAGE WIRE, CABLE & CONDUIT FITTINGS / AREA: 1,900 SF`. Fixture L622 therefore asserts only 1 LS and carries `status: proposed-convention (low-voltage.allowance-area-roundup-sf)`."),
("- **Name:** `security-device-count` (app: `low-voltage.security-device`; cameras 3/14/16/17 may use `low-voltage.camera`)",
 "- **Name:** `security-device-count` (app: `low-voltage.security-device`; the fixtures for cameras 3/14/16/17 use `low-voltage.camera`, which hard-codes the section `VIDEO SURVEILLANCE` and has no `section` input)"),
])

sub('README.md', [
("**§2.2.F: a ceiling smoke detector within 5 ft of the FACP** (this is why there is exactly 1 smoke detector).",
 "**§2.2.F: a ceiling smoke detector within 5 ft of the FACP.** §2.4.F.4 also asks for detectors in telephone and electrical rooms and adjacent to the FACP. The drawn count (1, in ELEC./I.T. 106) governs. It is consistent with both clauses. §2.4.F.4 would also add detectors E-160 does not show (note 1 ties the devices to the base-building system), so flag that as a spec-vs-drawing conflict."),
("| Intelligent photoelectric, ceiling-mounted, within 5 ft of the FACP (§2.2.F) |",
 "| Intelligent photoelectric, ceiling-mounted, in ELEC./I.T. 106 within 5 ft of the FACP (§2.2.F, §2.4.F.4) |"),
("""- **26 of 26 lines reconcile at 0 % to the markup legends.** Cross-checks were the PDF text layer of the tags, a visual symbol count, and a GPT-6 Astra second reading.
- **25 of 26 also match an independent count from the drawings.** Line 619 (18: ALARM INTERFACE) is the exception: E-150 shows **3** tag-18 bubbles (main plan 2, drive-thru 1), and the estimator dotted only 2. The undotted one is the `AI` at the teller line, between the two HUBs under the transaction bar. On the drawing count, that line is 1 EA (−33 %) short.""",
"""- **25 of 26 lines recompute within 5 % (all 25 at 0 %) from the drawings.** The formula inputs are the symbols and tag bubbles printed on the unmarked sheets, not the estimator's dots. Cross-checks were the PDF text layer of the tags, a visual symbol count, and a GPT-6 Astra second reading.
- **Line 619 (18: ALARM INTERFACE) is the one miss: recomputed 3, estimate 2, Δ +50 %.** E-150 shows **3** tag-18 bubbles (main plan 2, drive-thru 1). The estimator dotted only 2 and missed the teller-line `AI`, between the two `HUB` 10s under the transaction bar. The estimate is 1 EA short of the drawing.
- Against the markup legends, all 26 estimate quantities equal the legend rows (p47 row 18 is also 2). That only shows the estimate was copied from the dots. It does not check the dots against the drawing."""),
("- **Reference-data trap:** `reference/markups/legends.json` and `legends.csv` hold only 6 rows for page 48. The row `FIRE ALARM ADA AP... 9.0 EA` (purple, the horn/strobes, line 627) is missing because its truncated name duplicates the yellow 3.0 EA row. The page notes and the image both show 7 rows.",
 "- **Duplicate legend names:** page 48 has two rows called `FIRE ALARM ADA AP...`: purple 9.0 EA (horn/strobes, line 627) and yellow 3.0 EA (visual alarms, line 628). A name-keyed extraction once dropped the purple row. It has been restored in `reference/markups/legends.json` and `legends.csv`, flagged `two readers agree (duplicate name restored)`, and 627 is now sourced from that row. Lesson: key legend rows by page + name + colour + quantity, never by name alone."),
("Files: [`formulas.md`]",
 "Fixtures: lines 603–609 and 614–621 use `low-voltage.security-device` (with `section`). Camera lines 610–613 (tags 3, 14, 16, 17) use `low-voltage.camera`, which fixes the section to VIDEO SURVEILLANCE. Lines 623–624 use `low-voltage.fa-panel`, 625–628 use `low-voltage.fa-device`, and 622 uses `low-voltage.allowance` (quantity only; see F4). Every security fixture gives `count` as [view 1 main, view 2 drive-thru].\n\nFiles: [`formulas.md`]"),
])

sub('reading-guide.md', [
("one in each restroom and one in the shower/locker alcove, 3 in all.",
 "one in each restroom (MEN'S 112, WOMEN'S 111) and one on the east wall of PHONE ROOM 114 (A-110; on E-160 it is the hatched room with a single chair, below the JAN. mop sink), 3 in all."),
("- The circled `D` in the IT room is the only smoke detector. Spec 28 7210 §2.2.F requires one within 5 ft of the FACP. No duct detectors are drawn.",
 "- The circled `D` in ELEC./I.T. 106 is the only smoke detector. The drawn count governs. It is consistent with spec 28 7210 §2.2.F (within 5 ft of the FACP) and §2.4.F.4 (electrical and telephone rooms, adjacent to the FACP). §2.4.F.4 also lists rooms that E-160 does not cover, so flag that conflict. No duct detectors are drawn."),
("Here 25/25 device lines agree except tag 18.",
 "Here every device line agrees except tag 18 (plan 3, legend and estimate 2)."),
("`legends.json` / `legends.csv` keep only the yellow row, so the 9 EA horn/strobe source is missing from the reference data. Key legend rows by name + colour + quantity, never by name alone.",
 "A name-keyed extraction once dropped the purple row. It is now restored in `legends.json` / `legends.csv`, flagged `duplicate name restored`. Key legend rows by page + name + colour + quantity, never by name alone."),
])

sub('app-gaps.md', [
("The reference `legends.json` already lost the 9 EA row this way. | 9 horn/strobes are lost from the source set |",
 "The reference extraction once dropped the 9 EA row this way. It is restored in `legends.json`/`legends.csv` (flagged `duplicate name restored`). | 9 horn/strobes would be lost from the source set |"),
("Never key on the truncated name alone. Also fix `reference/markups/legends.json` page 48 by adding `{\"name\": \"FIRE ALARM ADA AP...\", \"quantity\": 9, \"unit\": \"EA\", \"color\": \"purple/orchid\"}`.",
 "Never key on the truncated name alone. The reference data already carries both page-48 rows (the purple 9 EA row restored). Use this page as the regression case."),
("The engine prints the area as read (`AREA: 1900 SF`). The estimator rounds up to `AREA: 2000 SF`, the same on DIV 22/23/26/28. | 1900 vs 2000 in the description |",
 "The engine prints the area as read and with its own covers text: `ALLOWANCE PROVIDED FOR LOW-VOLTAGE WIRE, CABLE & CONDUIT FITTINGS / AREA: 1,900 SF`. The estimator writes `ALLOWANCE PROVIDED FOR WIRE, CABLE & CONDUIT FITTINGS / AREA: 2000 SF`, rounding up as on DIV 22/23/26/28. Fixture L622 asserts quantity only until the convention exists. | 1,900 vs 2000 in the description, plus `LOW-VOLTAGE` |"),
("All 26 lines can be reproduced with existing assemblies and no new math.",
 "All 26 lines can be reproduced with existing assemblies and no new math. Line 619 reproduces the drawing (3), not the estimate (2); see gap 7."),
])

sub('best-practices.md', [
("sheet notes 1-10, plan keyed items.", "sheet notes 1-12, plan keyed items."),
("In this job the 20 schedule tags reproduce exactly in the reference estimate (derived from",
 "In this job 19 of the 20 schedule tags are carried in DIV 28 (tags 2-20). Tag 1, the alarm panel, is the DIV 26 SECURITY PANEL line 581. 18 of those 19 match the drawing. Tag 18 is 3 on the drawing but 2 in the estimate, because the estimator missed the teller-line AI (derived from"),
("Both the fire alarm and the security sections of the reference estimate carry **\"ALLOWANCE PROVIDED FOR WIRE, CABLE & CONDUIT FITTINGS\", AREA 2000 SF, 1 LS** (`reference/estimate/lines.json`, E-160 and E-150 lines).",
 "The reference estimate carries a single DIV 28 allowance line, **622 \"ALLOWANCE PROVIDED FOR WIRE, CABLE & CONDUIT FITTINGS\", AREA 2000 SF, 1 LS**, in the fire alarm section (`reference/estimate/lines.json`, E-160 markup). It covers both the fire alarm and the security wire, cable and conduit. The security section (603-621) carries no allowance or LF line."),
])
print('done')
