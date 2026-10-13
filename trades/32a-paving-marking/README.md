# 32a: Pavement, sidewalk, ramp, curb, marking, signs, bike racks, bollards

The site paving and marking package for the Fifth Third Bank branch on Watson Blvd, Warner Robins GA (0.96 ac site, a 1,900 SF building, 11 parking spaces per the Site Summary though the plan's circled counts add to 12, and a drive-thru). This folder covers **28 estimate lines**: 632–638, 642–650, 659–662, 674–677 and 713–716.

**All 28 lines reconcile within 1%**. Twenty-three match their source exactly, and the other five (632, 642, 643, 644, 646) differ only because the legend prints one decimal (largest gap 0.05%). Every quantity comes from the PlanSwift legend on markup **page 72 (C-3.0 Site Plan)** or **page 89 (A-401)**. Some lines use the measured value as is, some round it up to a whole unit, some count symbols, and some apply one formula to a count (pier footings) or to an area (expansion joint). No line is an unexplained allowance. Three inputs are the estimator's own judgment:

- **Pavement sections.** These are written "ASSUMED DETAILS", although the C-3.0 Pavement Legend points to the Terracon geotech report for both pavement types.
- **Bike-rack hardware and footing size.** No detail exists for either.
- **Dumpster bollard pier depth (3'-0").** A-190 gives the 16" pier diameter only.

There is also one count conflict between the drawings: **C-3.0 draws 5 dumpster bollards and A-190 draws 6; the estimate carries 5**.

## Scope

| Group | Lines | Unit | What it is |
|---|---|---|---|
| Asphalt pavement | 632 standard duty, 633 heavy duty | SF | Area by duty. The layer stack sits in the description only. |
| Concrete pavement | 634 | SF | 6" heavy-duty concrete paving. Keynotes 18 (drive-thru slab) and 21 (ADA stall and aisle) are merged into this one line. |
| Sidewalk | 635 SF, 636 LF | SF / LF | 4" walk with WWF, plus 1/4" expansion joint. |
| Curb ramp | 637 | SF | GDOT standard ADA ramp with detectable warning (2 ramps). |
| Curb and gutter | 638 | LF | 24" C&G: 6" x 12" curb with 18" gutter on 4" GAB. |
| Pavement marking | 642–647 | LF / EA | 4" SSWL, striped crosswalk, ADA aisle hatch, ADA symbol, 24" stop bar, arrows. |
| Signs | 648–650 | EA | ADA R7-8 sign with R7-8P5 plaque; R1-1 STOP; R5-1 DO NOT ENTER. The sign footings are lines 651–656 in trade 32b. |
| Bike racks | 659–662 | EA / CY | 2 racks, 4 pier footings, excavation, haul-off. |
| Bollards | 674–677 (dumpster), 713–716 (drive-thru) | EA / CY | 6" concrete-filled pipe bollards with 16" pier footings, excavation, haul-off. |

Outside this trade: the dumpster slab (line 663, the purple "21" row at 384.3 SF, which shares its truncated name with the teal 241.8 row used here), the transformer and cleanout pads (657–658), the sign footings (651–656) and the monument sign (707) are all in **32b-site-structures**. Grading is in **31-earthwork**. Demolition of the existing pavement and curb is in **01-demolition**.

## Driving sheets

| Sheet | Markup page | Role |
|---|---|---|
| **C-3.0 Site Plan** | **72** | All measured areas, runs and counts. Keynotes 1–23, the Pavement Legend, the Site Summary (11 spaces, impervious 21,033 SF), and note 5 (1 HC space, van accessible). |
| C-6.0 Construction Details 1 | 79 (highlights only) | Sidewalk detail (4", 6x6-W2.9xW2.9, 3000 PSI, expansion joints at 25' max, contraction joints at 5'). Curb and gutter detail. Stop bar detail. Pavement marking (arrow) detail. ADA parking, ADA symbol, ADA sign and sign mounting details. Traffic sign mounting detail. Civil bollard detail. |
| C-6.1 Construction Details 2 | 80 | GDOT standard ADA ramp and detectable warning. Referenced by keynote 6. |
| C-6.2 Construction Details 3 | 81 | Keynotes 3, 4, 18 and 21 say "SEE SHEET C-6.2 FOR PAVEMENT SPECIFICATIONS", but **C-6.2 holds only sanitary details**. The C-3.0 Pavement Legend (and General Site Note 9) instead point to the Terracon report, which is therefore the design section. |
| A-190 Trash Enclosure | 90 | TE1 bollard: 6" concrete-filled galvanized, painted yellow, 5'-0" high, 16" concrete pier (wall section 3; diameter only, the pier is drawn with break lines and has **no depth**). Floor plan 4 shows the bollard locations (6). General note: all painted steel pipe bollards receive a bollard cover. |
| A-401 Bank Equipment | **89** | 8 drive-thru bollards (legend). Typical Bollard detail 8 (16" dia concrete fill; pipe "48" BELOW GRADE" from top of paving, plus 3" of fill below the pipe = 51"; 4'-0" exposed height). Bollard cover note (Innoplast, 24" and 48" heights, 3M blue tape). |
| Terracon geotechnical report (dated 05.04.2026) | n/a | PDF pages 31–32 (report pp. 27–28) give the AC and PCC pavement section tables. The C-3.0 Pavement Legend ("CONCRETE PAVEMENT (SEE GEOTECH REPORT BY TERRACON, DATED 05.04.2026)", "HEAVY DUTY PAVEMENT (SEE GEOTECH REPORT ...)") and General Site Note 9 reference it, so it is the design pavement section for the job, not an outside source. |

## Specification sections

The project manual has **no Division 32 section**. The table of contents (spec p. 9) lists "32 3913 Surface Mount Metal Bollards", but the section is not bound into the manual. What does apply:

| Section | Page(s) | What it says for this trade |
|---|---|---|
| 05 5000 Metal Fabrications, 2.9 Metal Bollards | p. 118 | Fabricate from **Schedule 40 steel pipe**. Cap with a 1/4" steel plate. |
| 05 5000, 3.3 Installing Metal Bollards | p. 120 | Fill solidly with concrete. Anchor in holes at least 8" deep and 3/4" larger than the pipe OD (this sentence is for slab-mounted bollards; the drawings detail piers instead). |
| 09 9110 Paint Schedule, Pipe Bollards | p. 329 | Steel: Benjamin Moore V131 primer with P-22 alkyd urethane enamel, high gloss (or PPG equivalent). |
| 03 3000 Cast-in-Place Concrete | p. 50 (ASTM D1751 preformed expansion joint filler), p. 64 (curing) | Exterior slabs, sidewalks and curbs are cured with a clear, non-yellowing cure-and-seal compound. |
| Responsibility matrix bound after 01 2200 | p. 14 | "Sidewalks other than above": designed and installed by CE (contractor). |
| 01 7419 Construction Waste | p. 27 | Asphalt paving is listed as recyclable demolition waste. |

## Material types and specified properties

- **Heavy-duty asphalt (keynote 3), as the estimator assumed:**
  - 1-1/2" 9.5 mm top course
  - 3" 19 mm binder course
  - 4" 37.5 mm base course
  - 12" Type 2 subbase
  - separation geotextile on compacted subgrade

  The "F2 / F9 / Type 2" wording is NYSDOT terminology, which suggests boilerplate from another job. **Geotech heavy duty:** 1-1/4" SP9.5, 1-3/4" SP19, 8" GAB (GDOT 815/310), subgrade at 98% Standard Proctor.
- **Standard-duty asphalt (keynote 4), as the estimator assumed:** 1-1/2" 9.5 mm, 3" 19 mm, 12" subbase, geotextile. **Geotech light duty:** 2" SP9.5 and 6" GAB.
- **Concrete pavement (keynotes 18 and 21):** 6" in the estimate, assumed. **Geotech PCC (referenced by the C-3.0 Pavement Legend):** heavy duty 6-1/2" on 4" GAB, light duty 5" on 4" GAB, with a 4,000 psi basis (550 psi modulus of rupture); subgrade upper 12" at 98% Standard Proctor. The legend also says "CONTRACTOR TO SUBMIT JOINT PLAN TO GEOTECH FOR REVIEW/APPROVAL PRIOR TO PAVING".
- **Sidewalk (keynote 5):** 4" thick, 6x6-W2.9xW2.9 WWF, 3000 psi, 2" slump, broom finish, subgrade at 98% Standard Proctor. 1/4" expansion joints at 25' maximum and at all structures (1/2" at the building pad). Contraction joints at 5' (1" deep). 15# felt between the walk and parallel curb. Thicken to 6" where the walk abuts a roadway with no curb.
  - The A-190 dumpster detail shows a different walk: 6x6-W1.4xW1.4 WWF with control joints at 10'. That walk is outside this trade's lines.
- **Curb and gutter (keynote 1):**
  - Profile: 6" top, 1'-0" curb, 1'-6" gutter, 1"/ft gutter slope, on graded aggregate base.
  - Concrete: 3000 psi high early strength, smooth finish.
  - Joints: expansion joints at structures and curb returns, control joints at 25' maximum.
- **Marking:** C-6.0 calls for 4" blue lines (two coats) for HC delineation and 4" white lines (two coats) for regular stalls. The HC symbol is a 3'-0" x 3'-0" blue field with a 3" white border. Stop bars are 24" white per DOT. Arrows: 3'-8" x 9'-4" at road size, reduced 50% for parking lots. The crosswalk is 5' wide and white striped (keynote 17).
- **Signs:**
  - ADA: 1'-0" x 1'-6" .080 aluminum R7-8 plus a 1'-0" x 0'-6" R7-8P5 VAN ACCESSIBLE plaque, on a 2" x 2" x .188" steel tube set 2' into an 8" STD pipe filled with concrete (3'-6" min embed).
  - STOP: R1-1, 30" x 30", on a 2" galvanized steel channel with an 8" dia min concrete footing 3' deep.
  - DO NOT ENTER: R5-1 (the estimate says "RF-1").
- **Bollards:**
  - Dumpster (A-190 TE1): 6" Sch 40 pipe, concrete filled, galvanized, painted yellow, 5'-0" above slab, on a 16" dia concrete pier. **No pier depth is drawn**; the estimate's 3'-0" is an assumption. Cover required by the A-190 general note ("ALL PAINTED STEEL PIPE BOLLARDS ARE TO RECEIVE A BOLLARD COVER"), product per the A-401 note (Innoplast light gray #7D-42612-G2). Estimate line 674 carries no cover for this group (quantity unaffected, material note only).
  - Drive-thru (A-401): 6" concrete-filled pipe with an Innoplast light gray cover (24" and 48" heights) and 3M 5100R-75 blue reflective tape, 4'-0" exposed, pipe 48" below grade (top of paving) with 3" of 16" dia concrete fill below the pipe (51" of fill). The estimate uses 4'-0" and ignores the 3" extension and the paving thickness.
- **Bike rack:** no detail. The estimator assumed 1.25" Sch 40 pipe and two 12" x 12" footings per rack.

## What the estimator measured (page 72, C-3.0; page 89, A-401)

| Legend row | Qty | Unit | Estimate line |
|---|---|---|---|
| 3: HEAVY DUTY ASPHALT (cyan) | 11,367.3 | SQ FT | 633 |
| 4: STANDARD DUTY ASPHALT (brown) | 2,459.2 | SQ FT | 632 (2,459.18) |
| 21: HEAVY DUTY CONCRETE (teal) + 18: HEAVY DUTY CONCRETE (bright green) | 241.8 + 505.8 | SQ FT | 634 (748) |
| 5: CONCRETE SIDEWALK (green) | 1,834.7 | SQ FT | 635 (1,835) and 636 (1,835 / 25 = 73.4 LF) |
| 6: GDOT ADA RAMP (olive) | 113.3 | SQ FT | 637 (114) |
| 1: 24" CURB & GUTTER (slate blue) | 993.9 | FT | 638 (994) |
| 16: 4" SSWL (red) | 441.3 | FT | 642 (441.31) |
| 17: STRIPED CROSSWALK (bright green) | 79.5 | FT | 643 (79.46) |
| 4" W DA 45 DEGREE (yellow) | 97.5 | FT | 644 (97.48) |
| 24" WHITE STOP BAR (purple) | 49.6 | FT | 646 (49.58) |
| ADA PAINTED PARKING SIGN / ADA PARKING SIGN | 1 / 1 | EA | 645 / 648 |
| 12: R1-1 STOP / 13: DO NOT ENTER | 3 / 2 | EA | 649 / 650 |
| ARROW MARKING / 19: BIKE RACK / DUMPSTER BOLLARDS | 2 / 2 / 5 | EA | 647 / 659 / 674 |
| A-401: 6" DIA STEEL BOLLARD & WRAP (p89) | 8 | EA | 713 |

The rounding conventions differ by line type. The estimator wrote them down as follows:

- **Asphalt and marking lines** keep the PlanSwift value to 2 decimals.
- **Concrete flatwork, ramp and curb lines** are **rounded up to the next whole unit**: 747.6 → 748, 1,834.7 → 1,835, 113.3 → **114**, 993.9 → 994.
- **Pier footings** carry the circle area rounded to 2 dp after rounding the diameter to 2 dp (16" → 1.33 ft → 1.39 SF; 12" → 0.79 SF). This is the same convention as the sign and light-pole footings in 32b.
- **Excavation and haul-off** for piers equal the pier concrete.

## Reconciliation summary

| Classification | Lines | Count |
|---|---|---|
| measured | 632, 633, 634, 635, 637, 638, 642, 643, 644, 646 | 10 |
| counted | 645, 647, 648, 649, 650, 659, 674, 713 | 8 |
| derived | 636, 660–662, 675–677, 714–716 | 10 |
| specified / allowance | none | 0 |

- **28 of 28 within 1%**, and 28 of 28 within 5% (23 exact). The five non-zero deltas, all ≤ 0.05%, are the legend's 1-decimal printing against the estimate's PlanSwift precision. The verification pass below changed sources and notes only; no estimator or recomputed quantity moved, so the count is unchanged.

**Cross-check against the site summary.** The site summary gives 21,033 SF of impervious area. The measured areas add up to 20,810.2 SF (−1.06%):

| Component | SF |
|---|---|
| Building | 1,900 |
| Heavy-duty asphalt | 11,367.3 |
| Standard-duty asphalt | 2,459.2 |
| Sidewalk | 1,834.7 |
| Ramps | 113.3 |
| Concrete pavement | 747.6 |
| Dumpster slab | 384.3 |
| Transformer pad | 16 |
| 994 LF of 2'-wide curb and gutter | 1,987.8 |
| **Total** | **20,810.2** |

This is a cheap check that the areas are complete and use the right scale.

**Open issues to raise in a bid review:**

1. **Dumpster bollards.** C-3.0 draws 5 (3 back wall + 2 gate jamb) and A-190 floor plan 4 draws 6 (4 back wall + 2 gate jamb). The estimator followed the civil sheet; keynote 11 ("REFER TO ARCHITECTURAL PLANS") makes A-190 govern, so 6 is likely pending RFI. The 6th bollard adds 0.154444 CY each to footing, excavation and haul-off (0.926667 CY per line).
2. **Pavement section not followed.** Keynotes 3/4/18/21 point to C-6.2 (sanitary only), but the C-3.0 Pavement Legend points to the Terracon report, and the estimator's "ASSUMED DETAILS" stack ignores that reference (RFI/clarification). The estimate's assumed sections are much heavier than the geotech's: asphalt totals 8-1/2" against 3" for heavy duty and 4-1/2" against 2" for standard duty, and the aggregate is 12" against 8" and 6" of GAB. This matters for any course or tonnage line, though not for the SF lines here.
3. **Arrow size.** The arrows are written at road size; the detail says halve them for parking lots.
4. **Two bollard details.** The civil C-6.0 BOLLARD DETAIL uses a 24" dia footing, 4'-0" minimum embedment below the pavement plus 3" of concrete below the pipe, 3'-0" minimum exposed and a 6" x 7' pipe, which conflicts with the architectural 16" piers. The estimator used the architectural details (5 dumpster bollards on the civil detail would be 2.327 CY at 4'-0" or 2.473 CY at 4'-3", against 0.772 CY).
5. **Dumpster pier depth.** A-190 section 3 gives no depth for the 16" pier; the 3'-0" behind lines 675–677 is an estimator assumption (RFI), like the bike-rack footing.
6. **Drive-thru pier depth.** A-401 detail 8 carries 3" of fill below the 48" pipe embedment (51" total). At 4'-3" lines 714–716 would be 1.750370 CY each (+6.25%) instead of 1.647407.
7. **Bike-rack footing.** No detail; the 4 footings of 12" x 12" are assumed (RFI).

## Verification

A reviewer pass (2026-10-13) raised ten issues on this folder; nine arrived complete and were each re-checked from the source files. The tenth was cut off in the hand-off and could not be checked. Claude Opus 5.5 did the checks: pymupdf text and vector extraction from C-3.0, C-6.0, A-190 and A-401, renders of every crop involved, the Terracon report PDF pp. 31–32, legends.json/csv, and Python for every number (`trades/32a-paving-marking/scripts/verify/`). GPT-6 Astra (`tools/ask_gpt.py`) gave an independent read of four crops: the A-190 wall section, the C-6.0 bollard detail, A-401 detail 8 and the C-3.0 dumpster enclosure. On each crop it agreed with the conclusions below. All nine issues were confirmed, and these changes were made:

1. **Duplicate "21" legend row.** The purple 384.3 SF row **is** in legends.json (page 72) and legends.csv. The "missing from legends.json" claim was removed from README, reconciliation 634 and reading-guide (section 2, trap 3). The warning about the shared truncated name stays.
2. **Pavement section.** The C-3.0 PAVEMENT LEGEND ("SEE GEOTECH REPORT BY TERRACON, DATED 05.04.2026" for both hatches, plus the joint-plan note) and General Site Note 9 both reference the geotech report, so that report is the design section, not an outside source. Only the keynotes point to C-6.2. This is now classed as "estimator did not follow the legend reference (RFI)". PCC light duty 5" on 4" GAB was added. Files changed: README, reconciliation 632–634, reading-guide items 1, 4, 5 and trap 2, best-practices, app-gaps input 7.
3. **Dumpster pier depth.** A-190 section 3 gives the 16" diameter only, and the pier is drawn with break lines. The only "3'-0"" on the sheet sits in the floor-plan dimension string, and the 1'-4" and 1'-0" dimensions belong to the CMU wall footing. The source for H on lines 675–677 is now "estimator assumption (RFI)" in reconciliation, fixtures (`depth.assumed: true`), formulas F11, README (material types and open issue 5) and best-practices.
4. **Civil bollard detail.** On C-6.0, "3' MINIMUM" is the exposed height, "4' MINIMUM" is the embedment from the pavement to the pipe bottom, and there are 3" more of concrete below the pipe. The old 1.744 CY figure (24" x 3'-0" x 5) was replaced with 2.327 CY (4'-0") and 2.473 CY (4'-3"), computed with π × 1² × H × 5 / 27.
5. **ADA hatch.** The 58.18 LF figure does not reproduce. The 0.72-pt hatch pen inside the 5' x 18' aisle gives 12 diagonal segments totalling 66.06 LF. The reviewer's 68.96 LF also counts four 0.12-pt annotation strokes. Neither total plus the sides or perimeter gives the crosswalk's 0.935 ratio. The "same short-trace factor" claim was dropped from F9, reconciliation 644 and reading-guide trap 6.
6. **A-401 depth.** "48" BELOW GRADE" runs from the top of paving to the pipe bottom, with 3" more of fill below the pipe (51"). The 4'-0" on the detail is the **exposed height**, not a depth; the old "48" / 4'-0" below grade" wording was wrong on that point too. The 4'-3" alternative (1.750370 CY, +6.25%) is now recorded in reconciliation 714, F11, README and the reading guide.
7. **Expansion joint.** best-practices now agrees with F4: 73.4 LF is the transverse 1/4" expansion-joint length at 25' (SF/25, width cancels). The 5' control joints are listed as a separate item.
8. **Bollard covers.** The A-190 general note requires a cover on all painted steel pipe bollards. This was added for the dumpster group (README, reconciliation 674, reading guide, best-practices) as a material note only.
9. **5 vs 6 bollards.** C-3.0 draws 5 (3 back wall + 2 jamb) and A-190 draws 6 (4 back wall + 2 jamb). Keynote 11 refers to the architectural plans. The rewording is in README, reconciliation 674, fixtures 674, F10 and reading-guide trap 1.

Also corrected: the README's exact-match count (now 23 exact and 5 legend-rounding deltas; it had said 19 and 9).

**Not changed:** all estimator and recomputed quantities and all classifications (28 of 28 within 1%).
