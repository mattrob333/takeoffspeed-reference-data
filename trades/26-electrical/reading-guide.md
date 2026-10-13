# Reading guide — 26 Electrical

## 1. Sheets to open, in order

1. **E-001 Legend.** Symbol → name. The estimator's line names come from here
   (e.g. `30/20` = "SAFETY SWITCH, 30A, 3POLE, FUSED @ 20A", `30/NF` = non-fused).
2. **E-600 Luminaire schedule** (interior) and the **exterior schedule on E-011**.
   Each row: LABEL, description, mounting, MFG, model, lamps, volts, watts, notes.
   The estimate line description is the schedule row copied (tag: description /
   MFR / MODEL / MOUNTING / LAMP / VOLTS / WATTS).
3. **E-130 Lighting plan.** Fixture tags next to every symbol, written `TAG, switchleg`
   (`C,i`, `T, c`, `TE, NL`, `JE,NL`, `A, j`). The fixture type is the text **before the
   comma**. The letter after it is the switch leg, `NL` = night light.
   Also: LCP schedule (15 relays), keyed notes 1–12, switch bank detail 3/E-130.
4. **E-100 Power & auxiliary plan.** Device symbols with modifiers printed next to
   them: `TR` tamper-resistant, `USB`, `SP` surge-protective, `WP`, `MS` motion sensor,
   `J` junction box, `VC` volume control, mounting heights (`48"`, `40"`, `31"`, `63"`),
   and hexagon keynotes 1–25. Enlarged plan 2/E-100 (transaction bar).
5. **E-101 Roof plan.** Disconnects with rating/enclosure text (`30/25 3R`, `100/90 3R`),
   keynotes 1–2 and the roof disconnect mounting detail (pitch pocket, outlet box hood).
6. **E-010 Site plan** + detail 2 (remote drive-thru) and keynotes 1–13. **E-011** for pole counts.
7. **E-702 / E-703 / E-704 elevations.** IT room enlarged plan 9/E-702 (quad receptacles,
   panels, LCP, relays), backboard elevations 5–8, meeting room / library / janitor elevations.
8. **E-610 panel schedules, E-800 riser.** Panel name, voltage, bus, main; service and feeders.
9. **M-503 Mechanical controls details.** Disconnects and the wired remote controller
   the electrician installs (26 0100 §3.1 C: work shown in another division is in Div 26).

## 2. How each formula input is read

| Input | Where | Actual strings on this job |
|---|---|---|
| Fixture tag + count | E-130 symbols, E-600 LABEL | `A` 8, `AE` 6, `C` 53, `G1` 22, `TE` 9 … (PlanSwift page 46) |
| Linear fixture runs | E-130, schedule "(LENGTH AS SPECIFIED ON PLANS)" | `G` 26.8 FT, `L` 30.4 FT, `UC` 9.1 FT |
| Emergency variant | E-600 description "WITH EMERGENCY BATTERY BACKUP", model suffix `-EL`, `EM-1006`, `-EMH--8`; E-130 sheet note 1: half/fully shaded symbols | AE, FEM, GEM, JE, TE, X1, X2, X3 |
| Site pole + heads | E-011 schedule column "1HEAD" / "2HEAD, 180° CONFIGURATION"; labels on E-010/E-011 | `1P4F` × 1, `2P4DA` × 4 |
| Receptacle variant | E-100 symbol + modifier + keynote | `TR`, `USB`, `SP`, `WP`; keynote 24 "FACTORY ENGRAVED COVER PLATE WITH 'GFCI PROTECTED' LABEL"; transaction-bar note 1 "BLACK COVER PLATES"; keynote 9 "BLACK DEVICES AND COVER PLATES" (booths) |
| Conduit bundle | Callouts and keynotes | E-010 keynote 1 "ROUTE (2)4"C TO MAIN TELEPHONE SERVICE ENTRANCE", keynote 8 "(2)5"C FOR HIGH VOLTAGE SERVICE", detail 2 "1"C. FOR AV"; E-100 keynote 8 "(4) 3/4" IMC FOR POWER AND (4) 2" IMC WITH STRING", keynote 17 "STUB UP (2) 2" CONDUITS", keynote 18 "STUB UP (2) 4" CONDUITS" |
| Conduit route length | Measured along the drawn route at the sheet scale (E-010 1" = 20'-0"; detail 2 3/16" = 1'-0"; E-100 1/4" = 1'-0") | one length per bundle per page |
| Disconnect | Plan text `rating/fuse enclosure` | `30/25 3R`, `100/90 3R` (E-101), `30/2 NF` (E-100 keynote 3), `30/NF 3R` (E-100) |
| Panel | E-610 heading, E-800 | `PNL 'PP'` 400A MCB, `PNL 'RP-A'` 225A MLO |
| Allowance area | Title block, every sheet | `1,900 SF` → basis 2,000 SF |

## 3. Cross-checks that worked

- **Text-layer tag count vs. legend.** Counting the E-130 text layer by the text before
  the comma gives A 8, B 3, F3 1, FEM 2, G1 22, GEM 2, JE 4, PB 1, S 2, T 7, TE 9, U1 2,
  U3 1, X1 4, X2 2, X3 1, all equal to the legend. AE (7 vs 6), C (51 vs 53) and J (11 vs 9)
  are off because the booth inset (2/E-130) and labels without a symbol show up in the
  text layer. When they disagree, use the dot count, and check the inset.
- **Keynote occurrence count.** Keynote 24 appears 3 times on E-100 (positions
  x≈0.49/0.56/0.63 of the sheet width). Those are the engraved-plate receptacles:
  REF (TR duplex, line 550), EWC (GFCI, 542), DW (TR GFCI, 537).
- **Schedule ↔ plan.** Every E-600 tag shows up on E-130 (22 tags), and every estimate line
  maps to one tag.
- **Riser ↔ panels.** E-800 400A service and 225A feeder match the E-610 PP and RP-A ratings.
- **Spec ↔ callout.** E-100 keynote 8 says IMC, and 26 1000 §3.1 A allows RGS/IMC for
  service and exposed runs. The site conduits have no type in their callouts. By
  §3.1 C / §3.3 A they are Schedule 40 PVC encased in 4" of concrete.

## 4. Traps hit on this job

1. **Conduit LF is route LF.** "(2) 4" CONDUIT 101.71 LF" is the route of the pair, so
   multiplying by 2 doubles it. The same holds for "(4) …" at the transaction bar.
2. **Same-name legend rows can be lost in transcription.** The first `legends.json`
   dropped three rows that are on the page images, because the reader-merge step kept
   one row per normalised name: page 41 "1"DIA CONDUIT 4.8 FT" (magenta, line 506),
   page 44 row 1 "QUAD RECEPTACLE 20A, 125V 1.0 EA" (magenta, line 546; its name
   differs from row 13 "QUAD RECEPTACLE, 20A, 125V" only by a comma) and page 44
   row 14 "TEMPER RESISTANT GFCI DUPLEX RECEPTACLE, 20A, 125V NAN EA". They were
   restored on 2026-10-13 and both pages are now in printed order (p41 3 rows,
   p44 39 rows). Any reader that keys legend rows by name will repeat this; key by
   position and swatch, and re-read the image when the row count is below the notes'.
3. **Same name, different rows.** Page 41 has two "1"DIA CONDUIT" rows and page 44 two
   "TEMPER RESISTANT GFCI DUPLEX RECEPTACLE" rows, each with a different swatch. Sum
   them, and drop a `NAN`.
4. **`NAN EA` is not zero.** It means no dot was placed. The estimator still carried
   1 EA for both NAN rows (497, 541), so a NAN row means "the estimator decided by hand".
5. **Wrong tag in the estimate.** Line 511's tag column and description prefix both
   read `AE`, but the body text and model are the E-600 schedule's type **A** row (no
   "WITH EMERGENCY BATTERY BACKUP", model without `-EL`), and it carries legend A's
   count of 8. Line 512 is the real AE (EM backup, `-EL`, legend AE = 6). Line 520 has
   no tag ("120 J:"). Key on the model number, not the tag column.
6. **Duplicate pages.** Page 87 is a reduced reprint of E-010 with the same 4 junction
   boxes, meter and disconnect. They are not added (503 = 4, not 8). The irrigation
   backflow in trade 33 is the exception: line 739 = 2 is pages 42 + 87, so the same
   device was counted twice there.
7. **Devices hide on non-electrical sheets.** 3 of the 6 disconnects (553) plus 554 and
   593 are on M-503 Mechanical controls details.
8. **Plan text vs. estimator wording.** E-100 keynote 3 reads "30/2 NF DISCONNECT"; the
   legend and estimate say "20/2 NF" (558). The estimate names RTU disconnects only as
   "NEMA 3R FUSIBLE" (559). Ratings are on E-101 (`30/25 3R` × 1, `100/90 3R` × 2).
9. **Attic stock not carried.** E-600 types C and UC say "PROVIDE TEN (10) EXTRA FIXTURES
   FOR ATTIC STOCK". The estimate counts as drawn (C = 53, UC = 9.13 LF). Ask before
   adding it.
10. **Two-head poles.** 2P4DA is 2 heads at 180°, but the estimate counts 4, the pole
    assemblies. A heads-based count gives 8.
11. **Items on the drawings with no estimate line:** lighting relays #2/#3 (E-702), the
    storm switch / manual transfer switch and Power Scout meter (E-800), the kiosk
    canopy-light connection (E-010 keynote 11; page 87 row "11: KIOSK…"), riser feeders and
    grounding electrode system (in the allowance), and two called-out conduits that were
    never measured: the E-100 keynote 13 floor-box feed ("3/4" IMC FOR POWER AND 1-1/4"
    IMC WITH PULL STRING FOR TELE/DATA TO ELEC/IT ROOM") and the E-130 keynote 1 logo-sign
    run ("ROUTE 1" C TO PANEL RPA THRU LIGHTING CONTROL PANEL"). Both are drawn or
    called-out conduit with no measured line; they fall in allowance 510. Only the six
    bundles 505–508, 601 and 602 are measured. Monument sign power (E-010 keynote 13) is
    carried as the bell-box toggle switch, line 498. Flag the rest; don't invent them.
12. **E-150 / E-160 markups** (security, fire alarm) sit in the electrical drawing set
    but belong to trade 28.
