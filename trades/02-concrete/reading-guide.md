# Reading guide: concrete (02-concrete)

## 1. Sheets, in reading order

1. **S-201 Structural Plan – Foundation (1/4" = 1'-0")**. This is the only plan to measure on.
   - Plan symbols: footing marks with the top-of-footing elevation in brackets (`F50` / `[-2' - 0"]`), base-plate
     marks (`BP12`, `BP14`, `BP1518`, which are steel and not concrete), `WF20` / `[-2' - 0"]` along the walls,
     `S.C.J.` saw-cut joints, `R.B.` reinforcing bars at joint intersections, `SOG-4` slab mark, and dashed
     squares around each column for the spread-footing outline.
   - Schedules on the same sheet: **SPREAD FOOTING SCHEDULE** (MARK / LENGTH / WIDTH / THICKNESS / BOTTOM and TOP
     REINFORCEMENT / COUNT), **WALL FOOTING SCHEDULE** (`WF20 2' - 0" 1' - 0" 2 #6`) and **SLAB AND DECK SCHEDULE**
     (`SOG-4 4" CONCRETE SLAB ON A VAPOR RETARDER ON A GRAVEL BED … WELDED WIRE FABRIC 6/6-W2.9xW2.9 IN FLAT SHEETS`).
   - Foundation Plan Notes:
     - "TOP OF FOOTINGS AT ALL EXTERIOR/INTERIOR FOOTINGS SHALL BE [-2'-0"] BELOW FINISH FLOOR SLAB". This gives the stem-wall height.
     - "JOINT SPACING SHALL NOT EXCEED 12'-6" … ASPECT RATIO … 1.5".
     - "FOR ISOLATION JOINT AT COLUMN BASES, SEE 8 / S-680".
     - "S.C.J. … SEE TYPICAL SAW-CUT JOINT DETAIL 3 / S-680".
2. **S-600 Wall Sections – Foundation**. Sections 1–5 show the 8" stem with `#4 CONT. @ 10" o.c. MAX.` and
   `#4 DOWELS AT 18" o.c. MAX.`, the WF20 footing `1' - 0"` thick, and `1/2" JOINT FILLER` at the slab edge.
   Section 6 "At Foundation And Wing Wall" shows the wing-wall stem dimensioned **`10 3/4"`** with #4 @ 10" and #4 @ 18" at each face.
3. **S-680 Typical Details (Foundation)**. Detail 3 is the sawcut at `1/4 "T"`. Detail 8 is the column isolation joint (`ISOLATION JOINT BY
   "NOMAFLEX" OR APPROVED EQUAL`) with diamond blockouts, and `PROVIDE (2) #4 X 4'-0" TOP AT ISOLATION JOINT CORNERS`.
4. **S-001 / S-002 General Notes**. SLAB-ON-GRADE NOTES 6 reads "4" THICK, 3000 PSI … FLAT SHEETS OF WELDED WIRE FABRIC 6x6-W2.9xW2.9 … ON
   A VAPOR BARRIER". The S-002 strength table gives 3000 psi for SOG and for foundations and piers. Concrete note 2 gives 3" cover at footings.
5. **P-302 / P-301 general note 3** gives the cleanout pad size. **C-5.0** shows the 6 site cleanouts. Their pads are site concrete
   (Div 32 line 658), not this trade.
6. **Specs:**
   - 03 3000 p55: #57 stone 4" "where shown on drawings" (none is shown), keyed control joints, plyform.
   - 07 2616 p162: vapor retarder 15 mil.
   - 03 2000 pp46–47: A615-60 bars, WWF lap 6".

## 2. Reading each formula input

| Input | Where | Exact string on this job | Value |
|---|---|---|---|
| Slab area | p33 teal polygon, legend row 16 | `4"THK. CONCRETE SLAB ON GRADE W/ 6x6 W2.9xW2.9 WIRE MESH O/ VAPOR BARRIER O/ GRAVEL BED` `1917.6 SQ FT` | 1917.6 SF |
| Slab thickness | S-201 SOG-4; S-001 SOG note 6 | `4" CONCRETE SLAB`, `4" THICK, 3000 PSI` | 4" |
| Base | spec 03 3000 p55; S-201 SOG-4; S-001 note 6 | `Fill for slabs on grade shall be #57 stone, 4" thick where shown on drawings`; `ON A GRAVEL BED OR SAND CUSHION AS RECOMMENDED BY THE GEOTECHNICAL REPORT`; `ON A VAPOR BARRIER ON A NON EXPANSIVE FILL SUBGRADE` | no thickness drawn; the estimate's 4" is a description assumption (SF unaffected) |
| Vapor retarder | spec 07 2616 p162 | `15 mil thickness` | 15 mil (the estimate says 10 MIL) |
| Saw-cut LF | p33 yellow | `SAW-CUT JOINT - 3/S680` `364.1 FT` | 364.1 LF |
| Saw-cut depth | 3/S-680 | `1/4 "T"` | 1" |
| Isolation LF | p33 medium-green diamonds | `ISOLATION JOINT - 8/S680` `39.2 FT` | 39.2 LF |
| Isolation width | S-600 | `1/2" JOINT FILLER` | 1/2" |
| WF20 LF | p33 periwinkle | `WF20` `124.2 FT` | 124.2 LF |
| WF20 section | WALL FOOTING SCHEDULE | `WF20 2' - 0" 1' - 0" 2 #6` | 2' × 1' |
| Spread counts | p33 dots, schedule COUNT | `F30 3`, `F38 3`, `F50 6`, `F60 1`, `F70 1`, `F7040 1`, `F10050 1` | as printed |
| Spread sizes | SPREAD FOOTING SCHEDULE | e.g. `F7040 4' - 0" 7' - 0" 1' - 4" 7 #6 SW, 5 #6 LW` | L × W × T |
| Stem LF | p33 slate blue / olive | `8"THK. CONCRETE STEM WALL … @ 2'H` `193.8 FT`; `10"THK. … @ 2'H` `8.4 FT` | 193.8, 8.4 |
| Stem height | S-201 note [-2'-0"] to FF; legend "@ 2'H" | `[-2' - 0"]` | 2'-0" |
| Stem thickness | S-600 sec 1–5 `8"`; S-201 plan at the 6/S-600 "At Wing Wall" callout and sec 6 `10 3/4"` | `10 3/4"` | 8"; the estimator used 10" for 10 3/4" |
| Pad | P-302 note 3 | `EMBEDDED\ IN 18"X18"X6" THICK CONCRETE PAD. (J.R. SMITH 4258 OR EQUAL.)` | 1 EA × 18 × 18 × 6" |

## 3. What each colour covers on p33

Verified at 5–8× zoom. GPT-6 Astra gave an independent second reading of the WF20 and stem runs and agreed.

- **Teal area**: the whole slab inside the stem walls, one polygon. The diamonds are not cut out.
- **Periwinkle WF20**: perimeter runs that **stop at each dashed spread-footing outline**, so the run is net of overlap.
- **Slate-blue 8" stem wall**: continuous around the whole perimeter, **through** the spread footings, and around the north notch
  (the "NOTCH WALL FOOTING AS REQUIRED FOR VAT TUBE SLEEVE" bump).
- **Olive 10" stem wall**: two short wing-wall stubs. One points west near 3/S-203 at grid C-7. The other points south from the
  south wall to the F50/BP1518 footing "At Wing Wall" (6/S-600).
- **Medium-green diamonds**: isolation-joint blockouts around column base plates:
  - a full diamond at the interior column B-4
  - half or three-quarter diamonds at the perimeter columns (A.5 W/E, B-1, C-3 at R.B., etc.)
- **Yellow**: the saw-cut grid, 5 E-W and 4 N-S lines.
- **Count dots** (one colour per footing mark) sit on each footing tag.
- The **green "New Count"** dots are on the column schedule (A-2.9, C-7). They are not concrete.

## 4. Cross-checks

- Footing counts appear three ways, and all three agree: the legend EA, the schedule COUNT column, and plan tags
  in the S-201 text layer. Each tag appears count + 1 times in the text because the schedule row repeats it,
  e.g. `F50` appears 7 times for 6 footings.
- Slab 1917.6 SF against G-001 `ACTUAL AREA … 1892 S.F.`: +1.35%. That is reasonable for the slab traced to the outside line.
- Stem 193.8 LF − WF20 124.2 LF = 69.6 LF. That should equal the stem length that crosses perimeter spread footings
  (about 14 perimeter footings, roughly 5' each).
- Saw-cut layout: about 45' of slab with spacing ≤ 12'-6" needs at least 3 interior lines each way. Nine lines are drawn,
  and a pixel trace measures ~352 LF against the 364.1 legend.
- Formwork: compare against Σ contact area (F7). A value outside 1% of Σ means a face convention changed.

## 5. Traps hit on this job

1. **Legend rounding.** The legend prints 124.2 / 39.2 / 364.1. The estimate carries 124.15 / 39.22 / 364.11. Use a 0.1% tolerance.
2. **Ft-in rounding.** The estimator multiplies 2-decimal feet: 3'-8" → 3.67 and 1'-4" → 1.33. This gives ±0.3% per footing line,
   −0.50% on the 8" stem (0.67) and +0.40% on the 10" stem (0.83).
   Do not copy it. Use exact fractions.
3. **Stem LF differs from the legend.** The estimate uses 194.0 and 8.5 LF where the legend shows 193.8 and 8.4. These look
   rounded up to 0.5 FT. Treat the difference as rounding: the LF alone is −0.10% and −1.18%, and with the ft-in rounding
   the lines total −0.60% and −0.78%.
4. **Wing wall is 10 3/4", not 10".** S-201 prints `10 3/4"` at the south stub beside the 6/S-600 "At Wing Wall" callout, and 6/S-600
   dimensions it the same. The estimate line says 10" and 0.83 ft. Reading the drawing literally gives 0.557 CY, +6.7%.
   The app should read the section, and the reconciliation should note this deviation.
5. **WF20 is net, stem wall is gross.** Do not deduct spread-footing widths from the stem wall. Do not add them back to WF20.
6. **Isolation joint is column blockouts only.** S-600 also calls a 1/2" joint filler at the slab edge against the stem wall,
   about 200 LF. The estimator did not take it. Do not merge the two.
7. **Joint-spacing conflict.** S-001 allows 15 ft and S-201 allows 12'-6". The drawn grid governs. Only lay out joints from the note when no layout is drawn.
8. **Vapor retarder thickness.** The estimate text says 10 MIL. Spec 07 2616 requires 15 mil, Class A. The SF does not change.
9. **Cleanout pads: don't double count across trades.** The only marker for line 29 is on the P-302 note text, and line 29 is the one
   plumbing-sheet exterior cleanout. The six C-5.0 cleanout pads are carried in Div 32 line 658 (18"x18"x8", 6 EA, 13.5 SF).
   Do not add the civil cleanouts here.
10. **Base plates and "New Count" on the same page.** BP12, BP14 and BP1518 are steel, and the BP12 legend shows 9 against a schedule
    count of 10. Do not read them as concrete piers. S-680 shows piers only where footings are more than 2'-0" below the floor,
    and every footing here is at [-2'-0"] except one F38 at [-1'-0"], so there are no piers.
11. **Formwork is one rolled-up line.** It is not split by element, and the 1420 fits a round-up to 10 SF. That rounding is a hypothesis
    from this one line. Score the raw contact area (1413.87 SF) at 1%. The slab edge is not formed.
12. **No rebar, WWF, stone or vapor lines.** They exist only in the descriptions. Do not score engine lines for them against this estimate.
