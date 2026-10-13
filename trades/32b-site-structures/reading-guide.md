# Reading guide — 32b site concrete and structures

How to read the plans and specs so that every input to `formulas.md` comes from a printed string
or a legend row. Strings in quotes are copied exactly from this job's sheets.

## 1. Where each input lives

| Input | Read it on | Exact string / legend row | Value |
|---|---|---|---|
| Traffic sign count | C-3.0 (markup p72) legend | `12: R1-1:STOP SIGN` 3.0 EA, `13: RF-1: DO NOT ENTER SIGN` 2.0 EA. Keynote 13 reads "DO NOT ENTER SIGN (R5-1)": the sheet designation is R5-1 and the legend's "RF-1" is a label typo, so match the row by keynote 13, not by the R-number | 5 |
| ADA sign count | C-3.0 legend | `ADA PARKING SIGN - C6.0` 1.0 EA | 1 |
| Traffic sign footing | C-6.0 TRAFFIC SIGN MOUNTING DETAIL | "8" DIA. MIN. CONC. FOOTING", depth dimension "3'" (pipe stops 4" above the bottom) | 8" × 3'-0" |
| ADA sign footing | C-6.0 ADA SIGN MOUNTING DETAIL | "8" DIA. STD. STEEL PIPE FILLED W/CONC.", "3'-6" MIN.", "2" X 2" X .188" STEEL TUBE EXTEND 2'-0" INTO CONC. FILLED PIPE" | 3'-6" deep; the hole diameter is not dimensioned (the estimator used 12") |
| Transformer pad | C-3.0 legend + keynote 14 | `14: TRANSFORMER PAD` 16.0 SQ FT. "CONCRETE TRANSFORMER PAD PER UTILITY OWNER'S REQUIREMENTS" | 16 SF; thickness assumed |
| Cleanout count | C-5.0 (p77) legend | `SANITARY CLEANOUTS` 6.0 EA | 6 |
| Cleanout pad size | P-301 / P-302 plumbing note 3, P-501 "DETAIL OF CLEANOUT TO GRADE" | "ALL OUTSIDE CLEANOUTS SHALL BE BROUGHT TO GRADE AND EMBEDDED IN 18"X18"X6" THICK CONCRETE PAD. (J.R. SMITH 4258 OR EQUAL.)" | 18"×18" |
| Enclosure slab and apron | C-3.0 legend, **purple/mauve** row (legends.json/legends.csv page 72) | `21: HEAVY DUTY CONCRETE PAVE...` 384.3 SQ FT | 384.3 SF |
| Slab section | A-190 wall section 3 | "6" CONCRETE SLAB ON GRADE W/#4 AT 12" O.C. EACH WAY BROOM FINISH", "10 MIL VAPOR BARRIER" | description |
| Wall length | C-3.0 legend | `DUMPSTER ENCLOSURE WALL` 36.2 FT (cyan polyline, the U-shaped wall) | 36.22 LF |
| Footing | A-190 section 3 | "2'-0"" width, "1'-0"" thick, "(3) #5 CONT. BOTT. & #5 TRANSV. AT 48" O.C.", "3"CLEAR" | 2'-0" × 1'-0" |
| CMU height | A-190 section 3 dimensions | "6'-8"" grade to underside of the cap, "1'-4"" grade to the top of the footing | 8'-0" |
| Reinforcing | A-190 section 3 | "#5 VERT. AT 32" O.C. MAX.", "BOND BEAM W/ 1 CONT. #5", "K.O. BLOCK W/ (1) #5 CONT., GROUTED SOLID.", "90° STD. ACI HOOK" | The bond-beam leader lands on the top course and the K.O. block leader on the course below it (bar dot in each): possibly two reinforced courses (trap 1) |
| Cap | A-190 wall cap detail 5 | "4" PRECAST STONE CAP", "CONTINUOUS THRU-WALL FLASHING W/ INTEGRAL DRIP", "CONTINUOUS DRIP", "CONTINUOUS SEALANT", "S.S. DOWEL GROUTED SOLID (2) EACH PIECE @ 5TH POINTS", "10 1/4"" cap width | LF items |
| Coating | A-190 section 3, elevations 1/2, finish schedule | "PAINTED 5/8" CEMENTITIOUS COATING ON CMU WALL TO EPT-1" (outside face), "EXPOSED CMU PAINTED TO MATCH EIFS-1" (inside face), "STUCCO WEEP SCREEN". EPT-1 "BENJAMIN MOORE / BALBOA MIST - OC27 / SEMI-GLOSS @ STEEL, SATIN FINISH @ WALLS" | 1 face × 6'-8" |
| Gate | C-3.0 legend + A-190 plan 4 / elevation 1 / keynotes | `DUMPSTER GATE` 1.0 EA; "16'-0"" opening, "6'-8"" height; TE2–TE5 | 1 |
| Dumpsters | A-190 floor plan 4 | label "2 YARD DUMPSTER" with two container rectangles | 2 |
| Monument sign | C-3.0 legend + keynote 22 | `PROPOSED MONUMENT SIGN` 1.0 EA; "PROPOSED MONUMENT SIGN, DESIGNED AND PERMITTED BY OTHERS" | 1 |
| Canopy | A-401 (p89) legend | `PREFABRIFATED CANOPY COORDINATE W/ BANK EQUIPMENT VENDER OR BANK ...` 61.7 SQ FT (indigo rectangle over the drive-thru island); plan notes "PREFABRICATED CANOPY COLUMN & BASEPLATE" (2) | 62 SF |
| ATM | A-401 legend | `ATM BY BANK EQUIPMENT VENDOR COORDINATE W/ VENDOR PRIOR TO INSTALLATI...` 1.0 EA (teal dot) | 1 |
| Light poles | E-011 (p43) legend | `1P4F LIGHT` 1.0 EA (green) + `2P4DA LIGHT` 4.0 EA (yellow) | 5 poles |
| Pole base | E-012 POLE BASE DETAIL 3 | "1'-6"" dia, "6'- 0"" below grade, "2'-6"" above, "3000 PSI CONCRETE BASE WITH SACK FINISH", "8 - #6 BARS VERTICAL", "#4 BAR TIES 12"O.C." | 18" × 8'-6" |

## 2. Legend reading notes

- C-3.0 prints its legend at the lower left, over the plan (25 rows). Names are truncated with
  `...` by PlanSwift, so match rows by the leading **keynote number**:

  | Keynote | Meaning |
  |---|---|
  | `21:` | heavy-duty concrete pavement (two rows) |
  | `14:` | transformer pad |
  | `12:` | STOP |
  | `13:` | DO NOT ENTER |

- **Two rows are both `21: HEAVY DUTY CONCRETE PAVE...`.** The purple 384.3 SQ FT row is the
  dumpster slab and apron: it covers the enclosure floor plus the apron in front of the gate.
  The teal 241.8 SQ FT row is pavement elsewhere. Both rows are in `legends.json` and
  `legends.csv` (page 72), listed separately. Tell them apart by the swatch colour against
  the area drawn at the dumpster, east of the parking lot.
- On p72 the cyan wall polyline is hard to see under the cyan asphalt hatch, and the gate (green
  dot) sits over the opening. The five brown circles are the dumpster bollards (another trade).
- A-190 (p90) has **no legend**. Its purple highlights (TE1–TE3, the cap and coating callouts,
  the wall section title) only show what the estimator read. Every enclosure dimension comes
  from the section and the plan.
- E-011 counts fixtures by label. Both fixture types are pole mounted (schedule: "POLE MOUNT,
  SEE DETAIL FOR POLE HEIGHT"), so the pole base count equals the fixture-label count, 5.
  `2P4DA` is a two-head fixture on **one** pole.

## 3. How each formula input is read

- **Wall LF:** use the legend value with the estimate's precision (36.22). Draw the centerline
  of the U: back wall plus two side walls, stopping at the gate posts. A plan check from the
  A-190 dimensions:
  - outside dimensions "16'-0"" wide × "11'-4"" deep;
  - centerline (16 − 0.667) + 2 × (11.333 − 0.333) = 37.33 LF.

  The civil-scale measurement is 36.22, 3% short of that. Use the legend value, since it is
  what the estimate carries.
- **CMU height:** add the two section dimensions, 6'-8" + 1'-4". Do not use the 5'-0" bollard
  dimension or the 6'-3" elevation dimension.
- **Footing earthwork depth:** footing thickness plus the CMU below grade, 1'-0" + 1'-4" =
  2'-4" (2.33). The slab and its vapor barrier are not part of the trench.
- **Exposed height for coating:** "6'-8"" (6.67). One face only: the inside face is "EXPOSED CMU
  PAINTED TO MATCH EIFS-1", which is painting, not coating.
- **Pier footings:** count × diameter × depth from the mounting detail. For light poles, split
  buried (6'-0") from exposed (2'-6"): concrete takes both, excavation and haul-off take the
  buried part only.

## 4. Cross-checks

| Check | Result |
|---|---|
| Sign footing count = sign panel count (lines 649 STOP 3 + 650 DNE 2) | 5 = 5 |
| Light pole bases = E-011 fixtures (1 + 4) | 5. E-010 shows the pole circuits |
| Haul-off = excavation − backfill (estimate) | 12.502607 − 8.659644 = 3.842963 ✓ |
| Haul-off ≥ footing CY | 3.842963 ≥ 2.682963 ✓. The difference is the CMU below grade |
| CMU SF ÷ wall LF = 8.00 | ✓ |
| Coating SF ÷ wall LF = 6.67 | ✓ |
| Grout ÷ CMU SF = 0.0112 CY/SF; mortar CF ÷ CMU SF = 0.1675 | ✓ (job conventions) |
| Cleanout count: C-5.0 (6) against the P-302 building-side pad (1 EA) | The estimator carried 6 (the C-5.0 count; six SSCO structures, S2–S7). Whether the P-302 building-side pad is one of them is not established |
| Canopy SF against the A-401 plan | The legend area (61.7) is the canopy roof footprint; the drawn indigo rectangle matches |

## 5. Traps

1. **One bond beam course or two.** A-190 section 3 labels the top course under the cap
   "BOND BEAM W/ 1 CONT. #5" and the next course down "K.O. BLOCK W/ (1) #5 CONT., GROUTED
   SOLID.", with a bar dot drawn in each. That may be two reinforced horizontal courses
   (line 671 = 72 LF; grout cross-check 1.40 CY rather than 1.22 CY). The estimator carried one
   course (36 LF). Reproduce 36 and flag the alternative.
2. **Circle-area rounding.** The estimator rounds D to 2 decimals and the area to 2 decimals.
   16" becomes 1.33 ft → 1.39 SF, not 1.396 SF. Exact π misses by 0.2–0.6%.
3. **Pier excavation is the buried part only**, with no backfill and no over-dig. A
   wall-footing trench, by contrast, gets 1' working space each side plus backfill.
4. **Excavation and haul-off are per footing type.** Do not merge the 12" ADA pair with the 8"
   traffic-sign pair.
5. **Per-LF accessories use the rounded wall LF (36), but the area lines use 36.22.**
6. **Weep screen 11.88 LF** is 36 × 0.33, which looks like an area slip. Physically it is about
   36.22 LF.
7. **Grout is not what the drawings ask for.** S-001 note 4 says "DO NOT FILL CELLS NOT CONTAINING
   REINFORCING BARS, EXCEPT BELOW GRADE". That is about 1.22 CY (1.40 CY if the K.O. block
   course is a second reinforced course, trap 1), but the estimator carried a solid-grout rate
   (3.25 CY).
8. **The cleanout pad thickness** reads 8" in the estimate and 6" on the plumbing drawings.
   Quote the drawing.
9. **The vapor barrier** reads 10 mil on A-190 and 15 mil in spec 07 2616 (Stego Wrap 15). The
   spec governs material selection; this trade does not carry it as its own line.
10. **The ADA sign hole diameter** is not dimensioned (only the 8" pipe is). The estimator chose
    12". Flag it as an assumption.
11. **The transformer pad thickness (10")** is assumed; the pad is "PER UTILITY OWNER'S
    REQUIREMENTS". Keep the "ASSUMED DETAILS" label.
12. **Gate posts (TE2)** are not a separate line. They ride in the gate description, and so do
    the TE3 sign, the TE4 cane bolt and the TE5 wheel.
13. **The canopy and ATM are vendor items.** The line quantity is footprint SF and EA, with the
    coordination text carried. The stub-up conduits are electrical.
14. **The monument sign has no footing line** ("DESIGNED AND PERMITTED BY OTHERS"). Its power
    (`13: MONUMENT SIGN POWER`, p87) is electrical.
