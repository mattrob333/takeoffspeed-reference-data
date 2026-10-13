# 32b — Site concrete and structures

Footings, pads, the dumpster enclosure, the monument sign, the drive-thru canopy and the ATM.
This covers **31 estimate lines** (Div 32, lineNo 651–658, 663–673, 678–683, 707, 712, 717–720),
listed in `reference/estimate/trades.json`. It covers quantities and material descriptions only.

**Result:** all 31 lines rebuild from a source, and all 31 land within 1% of the estimator's
quantity. 30 of them match to 4 decimal places. Line 663 is 384.3 against 384.31, because the
legend prints one decimal. Two of the rebuilt formulas rest on an inferred basis rather than a
printed one: line 683 (weep screen = 36 × 0.33) and the 1.16 CY of CMU below grade inside lines
666/667. Line 671 (bond beam, 36 LF) reproduces the estimator with one reinforced course, but
A-190 section 3 may call a second one (72 LF). `reconciliation.csv` has 31 rows and
`fixtures.json` 31 cases, all at 0.1% tolerance. See *Open items*.

| File | Contents |
|---|---|
| `formulas.md` | Every formula, with inputs, the estimator's conventions and a worked example |
| `reconciliation.csv` | Line → source → formula → recomputed quantity → delta → classification |
| `fixtures.json` | 31 engine test cases, one per line |
| `reading-guide.md` | Which sheets and legends to read, the exact strings, cross-checks and traps |
| `app-gaps.md` | How the TakeoffSpeed engine compares (it was run on these inputs), ranked changes |

## Scope by group (estimate section path)

| Group | Lines | What |
|---|---|---|
| SIGN > FOOTINGS | 651–656 | Concrete, excavation and haul-off for the sign post footings: 1 ADA sign (12" × 3'-6"), 5 traffic signs (8" × 3'-0") |
| CONCRETE PAD | 657–658 | Transformer pad (16 SF, 10" assumed) and 6 cleanout pads (18"×18") |
| DUMPSTER ENCLOSURE | 663–673, 678–683 | Slab and apron, footing with its earthwork, 8" CMU wall, grout, mortar, bond beam, precast cap, coating, gate, dumpsters, flashing, drip, sealant, weep screen |
| MONUMENT SIGN | 707 | 1 EA, designed and permitted by others |
| DRIVE THRU ISLAND | 712, 717 | Prefabricated canopy (SF), ATM (EA) |
| SITE LIGHTING FOOTING | 718–720 | 5 light pole bases, 1'-6" dia × 8'-6" H (6'-0" buried) |

These neighbouring lines belong to other trades and are not covered here: the sign panels and
posts (648–650), the bike rack (659–662), the bollards and their footings (674–677, 713–716),
and pavement and walks.

## Driving sheets

| Sheet | Markup page | Used for |
|---|---|---|
| C-3.0 Site Plan | p72 | Legend: wall LF, slab SF, transformer pad, gate, signs, monument sign. Keynotes 10 (ADA sign), 11 (dumpster enclosure), 12 (STOP), 13 (DO NOT ENTER, R5-1), 14 (transformer pad), 20 (drive-thru equipment), 21 (HD concrete), 22 (monument sign) |
| C-5.0 Utility Plan | p77 | `SANITARY CLEANOUTS` 6 EA |
| C-6.0 Construction Details 1 | p79 (highlights only) | TRAFFIC SIGN MOUNTING DETAIL (8" dia min × 3'), ADA SIGN MOUNTING DETAIL (3'-6" min, 8" std pipe) |
| A-190 Trash Enclosure and Details | p90 (highlights only, no legend) | Floor plan 4, wall section 3, wall cap detail 5, elevations 1/2, keynotes TE1–TE5, finish schedule EPT-1 |
| A-401 Bank Equipment Plans & Details | p89 | Legend: canopy 61.7 SF, ATM 1 EA. ATM and canopy stub-up notes |
| E-011 Photometric Site Plan | p43 | Legend: `1P4F LIGHT` 1, `2P4DA LIGHT` 4 (5 poles) |
| E-012 Electrical Site Details | p88 (no legend) | POLE BASE DETAIL 3: 1'-6" dia, 6'-0" buried, 2'-6" exposed, 3000 PSI |
| P-301 / P-302 / P-501 | p56/p57/p61 | Plumbing note 3 and the cleanout-to-grade detail: 18"×18"×6" thick pad |
| S-001 General Notes | — | Concrete masonry notes: mortar ASTM C270 Type S, grout ASTM C476 f'g 2250, cells grouted only where reinforced (and below grade) |

## Specification sections (project manual page numbers)

| Section | Pages | What it fixes for this trade |
|---|---|---|
| 03 2000 Concrete Reinforcement | 45–48 | 3" cover at footings (p47); WWF in slabs on ground |
| 03 3000 Cast-in-Place Concrete | 49–66 | Minimum cement contents: 3,000 psi 498 lb (5.3 bags), 4,000 psi 611 lb (p54). "Pea gravel" (#7 aggregate) concrete for block fill (p54). Grouting of reinforced cells and U-block bond beams (p59). Footing rebar cover 3" (p59) |
| 05 5000 Metal Fabrications | 113–121 | Bollards: Schedule 40 pipe with a 1/4" cap plate (p118), filled solid with concrete (p120). Steel pipe ASTM A53 Std Wt (p115). The bollards themselves are in another trade |
| 07 2616 Below-Grade Vapor Retarders | 162–163 | Basis of design Stego Wrap **15 mil**. A-190 says **10 MIL** (conflict; see the reading guide) |
| 07 6200 Sheet Metal Flashing and Trim | 188–196 | Thru-wall flashing and drip at the cap |
| 07 9200 Joint Sealants | 203–211 | Sealant at the cap |
| 04 2113 Brick Veneer Masonry | 67–77 | Mortar and grout materials (Type S lime, ASTM C144 sand, p71). There is **no 04 2200 CMU section**. Unit masonry is governed by S-001 notes |
| 09 9110 Paint Schedule | 328–329 | Exterior CMU: block filler plus elastomeric (BM 206 / 055 Moorlastic). Pipe bollards: metal primer plus urethane enamel |
| 09 9653 Elastomeric Coatings | 330–334 | Coating on concrete, CMU and stucco |

## Materials and specified properties

| Material | Property (where printed) |
|---|---|
| Sign footings | 8" DIA. MIN. CONC. FOOTING, 3' deep (C-6.0 traffic sign). ADA: 8" DIA. STD. STEEL PIPE FILLED W/CONC., 3'-6" MIN. The estimator used a 12" hole |
| Transformer pad | "CONCRETE TRANSFORMER PAD PER UTILITY OWNER'S REQUIREMENTS" (C-3.0 kn 14). No detail; the estimator assumed 10" |
| Cleanout pad | 18"×18"×6" thick concrete (P-301/P-302 note 3, P-501). The estimate text says 8" |
| Enclosure slab | 6" slab on grade, #4 @ 12" O.C. each way, broom finish, 10 mil vapor barrier, 1/2" premolded filler (A-190 section 3). C-3.0 keynote 21 heavy-duty concrete pavement |
| Wall footing | 2'-0" W × 1'-0" thick, (3) #5 cont. bottom & #5 transverse at 48" O.C., 3" clear (A-190 section 3) |
| CMU wall | 8"×8"×16" NOM. CMU. #5 vert. at 32" O.C. max. Bond beam with 1 cont. #5 under the cap, and a "K.O. BLOCK W/ (1) #5 CONT., GROUTED SOLID." callout on the course below (possibly a second reinforced course; open item 5). 6'-8" above grade, 1'-4" below grade to the footing |
| Cap | 4" precast stone cap on a mortar bed. S.S. dowels grouted solid, (2) per piece at 5th points. 1/2" crown (wall cap detail 5) |
| Cap accessories | Continuous thru-wall flashing with integral drip, continuous drip, continuous sealant (detail 5) |
| Finish | Painted 5/8" cementitious coating on the CMU wall to EPT-1 (Benjamin Moore Balboa Mist OC-27, satin @ walls). Stucco weep screen at the base |
| Gate | 16'-0" W × 6'-8" H steel double leaf. TE2 6" dia gate post with self-closing hinge, TE3 NO PARKING sign, TE4 Stanley #1010 cane bolt, TE5 Grainger #1VJD5 wheel |
| Light pole base | 1'-6" dia, 6'-0" below + 2'-6" above grade, 3000 PSI concrete with sack finish, 8-#6 vertical, #4 ties at 12" O.C. (E-012 detail 3) |
| Canopy / ATM | By the bank equipment vendor (BOD Sterling canopy system). Conduit stub-ups per A-401 |

## What the estimator measured

| Measured (markup legend) | Unit | Page |
|---|---|---|
| DUMPSTER ENCLOSURE WALL 36.2 (36.22) | FT | p72 |
| 21: HEAVY DUTY CONCRETE PAVE... 384.3 (purple/mauve row; legends.json/csv page 72) | SQ FT | p72 |
| 14: TRANSFORMER PAD 16.0 | SQ FT | p72 |
| PREFABRIFATED CANOPY ... 61.7 | SQ FT | p89 |
| Counts: ADA PARKING SIGN 1, R1-1 STOP 3, 13: RF-1 DO NOT ENTER 2 (sheet designation R5-1; "RF-1" is a legend typo), DUMPSTER GATE 1, PROPOSED MONUMENT SIGN 1 (p72); SANITARY CLEANOUTS 6 (p77); ATM 1 (p89); 1P4F 1 + 2P4DA 4 (p43) | EA | |

Everything else is derived from those values. The derivations use dimensions read from the
details (A-190 section 3, C-6.0, E-012, plumbing note 3) and four job-derived conventions:

- Circle areas rounded to 2 decimals.
- The wall LF rounded to whole feet for the cap, flashing, drip, sealant and bond beam.
- Grout 0.0112 CY/SF.
- Mortar 0.1675 CF/SF.

## Classification

| Class | Lines |
|---|---|
| measured | 657, 663, 712 |
| counted | 658 (count × specified size), 678, 679, 707, 717 |
| derived | 651–656, 664–673, 680–683, 718–720 |
| specified | none on its own (the sizes inside the derived lines come from details) |
| allowance / judgment | none as a line. Judgment inputs: the 12" ADA footing diameter, the 10" transformer pad thickness, and the 2-yard dumpster count (an owner/hauler item) |

## Open items

1. **Weep screen 11.88 LF (683)** equals 36 × 0.33 exactly. That points to a 4" strip area
   carried under the LF unit. Physically, a weep screed runs the base of the coated face, about
   36.22 LF. Reproduce it with the flag shown, not as a rule.
2. **CMU below grade 1.16 CY (inside 666/667)** is exactly 31.32 CF. The nominal 8" × 1'-4"
   gives 1.1924 CY. With the 2.33 depth used in 665, the physical formula lands within 0.4%
   (backfill 8.6272, −0.37%) and 0.84% (haul 3.8754). The engine's −0.17% on backfill comes
   from its exact 2⅓ depth. The fixtures carry the estimator's 1.16 CY as an input at 0.1%.
3. **Grout 0.0112 CY/SF (669)** is a solid-grout rate. S-001 note 4 grouts only the reinforced
   cells, the bond beam and the cells below grade. The physical estimate is about 1.22 CY
   (1.40 CY if there are two reinforced courses, item 5) against the estimator's 3.25 CY.
4. **Mortar 0.1675 CF/SF (670)** is about 1.75 times the 8.5 CF / 100 block rule.
5. **Bond beam courses (671).** A-190 section 3 puts the "BOND BEAM W/ 1 CONT. #5" leader on the
   top course under the cap and the "K.O. BLOCK W/ (1) #5 CONT., GROUTED SOLID." leader on the
   course below, where a bar dot is drawn. That may be two reinforced courses: 2 × 36 = 72 LF.
   The estimator carried 36 (one course); the fixture reproduces 36 and notes the alternative.
6. **Spec/drawing conflicts** that affect no quantity here:
   - Vapor barrier: the spec says 15 mil, A-190 says 10 mil.
   - Cleanout pad: the plumbing drawings say 6", the estimate says 8".
7. **Cleanout pads (658).** The estimator carried 6, the C-5.0 count (S2–S7 SSCO). Whether the
   P-302 building-side pad (1 EA) is one of those six is not established.

## Verification

Checked 2026-10-13 against a reviewer's seven findings, by Claude (Opus 5.5), with GPT-6 Astra
(`tools/ask_gpt.py`) as an independent reader of the A-190 section. All arithmetic was redone in
Python.

| Finding | Checked | Result | Changed |
|---|---|---|---|
| 384.3 purple row "missing" from the legends | `legends.json` page 72 (25 items; the last is the purple/mauve 384.3 row) and `legends.csv` line 618 | Reviewer right: the row is present | Removed the data-gap open item, the "MISSING" note in reconciliation row 663 and reading-guide trap 1. The row is now cited directly |
| One bond beam course or two | Markup p90 crops at 7× to 14× of section 3 and wall cap detail 5; GPT-6 Astra asked independently | Both readers see two courses with a horizontal bar, each with its own leader. Ambiguous, not settled | Line 671 flagged (36 with one course, 72 with two): F10, F8 (1.40 CY two-course grout check), reconciliation 671, fixture 671 note, reading-guide trap 1, open item 5 |
| Fixtures 666/667 passed only on widened tolerances | Recomputed: physical 8.627216 (−0.374%) and 3.875391 (+0.844%) | Reviewer right | Both fixtures now take the estimator's `cmuBelowGradeCY` = 1.16 as an input at 0.1%, with the physical results in `note` |
| Backfill delta −0.17% | 12.502607 − 2.682963 − 1.192428 = 8.627216 (−0.37%); −0.17% only with the exact 2⅓ depth | Reviewer right | README item 2, formulas F6 and reconciliation 666/667 now say −0.37% (within 0.4%) and attribute −0.17% to the engine |
| Formula strings mix units | Evaluated every formula string literally on its inputs | Reviewer right (651–656, 658, 664, 718–720). 665 and 673 had the same problem (inches inside `round()`) | Added `/12` conversions; 712 now reads `round(area)`. All 31 strings evaluate to their expected value within 0.1% |
| "RF-1" sign designation | C-3.0 text layer: "DO NOT ENTER SIGN (R5-1), SEE SHEET C-6.0 FOR MOUNTING DETAIL" | Reviewer right | README, reading-guide section 1 and reconciliation 654 note R5-1 and match the row by keynote 13. No quantity changes |
| P-302 pad "inside the 6" | `legends.json` p77 (6 EA) and p57 (1 EA); C-5.0 structure table (S2–S7 SSCO) | Reviewer right: nothing ties them together | Reconciliation 658, the reading-guide cross-check and open item 7 say this is not established |

No estimator quantity or classification changed. All 31 lines still reproduce, and 30 of them
to 4 decimal places.
