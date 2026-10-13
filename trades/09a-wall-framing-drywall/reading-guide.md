# Reading the plans and specs for wall framing and wall board

## 1. Sheet order

1. **A-620 Interior Partition Schedule & Details**: learn the tag grammar before
   reading the plan.
2. **A-120 Dimensional Floor Plan** (markup p4): every partition and exterior wall
   run, by tag.
3. **A-310 / A-311 / A-300 wall sections and A-430 / A-440 / A-450 details**: exterior
   stud depth, sheathing, parapet construction, heights.
4. **A-140 Roof Plan** (p7): parapet runs by height and the high-low roof step.
5. **A-130 RCP** (p5): mecho-shade runs (3-5/8" furring) and ceiling heights.
6. **Enlarged plans and elevations**: A-410 restrooms (p16), A-700 transaction bar
   (p23), A-703 service counter (p27), A-704 tech wall (p28), A-705 lounge (p32),
   A-706 booth (p29). Board types other than standard gypsum are measured here as areas.
7. **S-001 / S-002**: cold-formed steel notes and the *Exterior Schedule of Metal Stud
   Sizes* (gauge by wall height). **S-203** (p34): canopy framing area.
8. Specs **09 22 16** (p267–272), **09 29 00** (p273–281), **05 40 00** (p104–112),
   **06 16 00** (p128–132).

## 2. The partition tag (A-620 Partition Legend, Tables A–D)

Tag `A3A` = **series** `A` + **stud depth** `3` + **height designator** `A`.

| Part | Values on this job | Meaning |
|---|---|---|
| Series (Table A) | A, D | A = 1 layer / metal stud / 1 layer (2 faces); D = 1 layer / metal stud / none (1 face). B and C carry cement board but are not used on the plan. |
| Depth (Table B) | 3, 6 | 3 = 3-5/8", 6 = 6" metal stud |
| Height (Table D) | A, B, C | A = slab to structure; B = slab to structure w/ batt; C = slab to 6" above ceiling |
| Fire rating | none shown | |

Gauge is **not** in the tag. Note A says "reference specifications for all stud gauges"
and the spec says "as indicated on drawings". The estimator carried 20 GA (0.0312", per
the A-620 steel-thickness table) for every interior partition. It carried 16 GA (0.0566",
54 mil) for every 6" and 8" exterior stud. S-002 does not support one gauge: it calls 43 to
97 mil by height band, wind zone and deflection limit (trap 11). A-200 sets a floor of
"minimum 16 GA metal stud framing" behind ACM panels.

## 3. How each formula input is read (strings from this job)

| Input | Where | Exact strings |
|---|---|---|
| Run LF per tag and height | p4 legend rows | `WALL A6B @ 12'6"H` 28.4, `WALL A3B @ 12'6"H` 34.2, `WALL A6A @ 12'6"H` 36.7, `WALL A3A @ 12'6"H` 49.9, `WALL D3C @ 12'6"H 1 SIDE` 3.7, `WALL D3A @ 12'6"H 1 SIDE` 46.0, `WALL A3A @ 3'9"H (NO INS)` 7.7 |
| Exterior runs | p4 | `EXT 8" STUD WALL @ 12'9"H` 89.7, `@ 15'9"H` 41.5, `@ 15'9"H NO GWB` 8.7, `@ 4'H` 13.0, `EXT 6" STUD WALL @ 12'3"H SHTNG 10'3"H` 9.2 |
| Special walls | p4 | `6" & 3-5/8" METAL STUD @ 18'8"H, BS 1/2" SHTNG ONLY` 8.4 (high parapet, A-430 "18'-8" T.O. HIGH PARAPET"); `6" METAL STUD WALL @ 4'4" HT, BS GWB` 18.3; `PARAPET WALL @ 7'2"H A310` 5.9 (the 8" upper VAT wall on the canopy beam, A-310 section 1). The 6" VAT recess wall below it is `EXT 6" STUD WALL @ 12'3"H` (9.2 LF, three sides of the recess) |
| Parapets | p7 | `PARAPET WALL @ 1'7"H` 46.0, `@ 2'7"H` 38.0, `@ 4'7"H` 96.6 |
| Roof step wall | p7 | `8/A450 LAP ROOF 2', INCL WALL` 45.3 (A-450 det. 8 HIGH-LOW ROOF DETAIL: "3 5/8" MTL. STUDS & BATT INSULATION") |
| Mecho-shade furring | p5 | `MOTORIZED MECHOSHADE` 74.0 FT (A-310; A-430 det. 8 and 9: "3 5/8" MTL. STUD FURRING AT MECHO-SHADE LOCATIONS"); no height on the row or the details |
| Height | typed in the item name (`@ 12'6"H`) | 12'-6" interior partitions to structure; exterior 12'-9" / 15'-9" to roof (sections) |
| Faces | tag series + name suffixes | `1 SIDE`, `BS` (both sides), `NO GWB`, `SHTNG ONLY` |
| Type X | p28 `TYPE X GWB` 37.2 SF | A-704: "5/8" TYPE 'X' GYP BOARD OVER IN WALL PLYWOOD BLOCKING, PT-6" |
| Moisture board | p16 `PT1 WALL PAINT` 252.6 SF | restroom wall faces that are painted (above/beside tile) |
| Cement board | p16 `WT1 WALL TILE` 120.7, `WT2` 43.8, `WT9` 50.6; p27 15.3/1.4/1.3; p32 8.2/1.6/1.3; p23 `WT3 TILE` 38.4 | all wall tile |
| 1/4" cement board | p23 `1/4" CEMENTITIOUS BACKER BOARD` 38.4 SF | transaction bar |
| Booth roof framing | p29 `6"THK. 16GA. METAL STUD @ 12" O.C W/ 6"THK. SOUND BATT INSULATION W/ 3/4"THK. PL...` 76.2 SF | A-706 det. 11: "6" 16 GAUGE METAL STUD FRAMING AT 12" O.C." |
| Canopy framing | p34 `6" METAL STUD CANOPY FRAMING @ 16" O.C` 416.9 SF | S-203 roof framing plan |

## 4. Cross-checks that hold on this job

- Stud count notes in the estimate ≈ `ceil(LF × 12/16)` per height: 12 of the 17 groups
  are exact, all within ±1 stud (`round(LF / 1.33)`: 13 of 17). Use them to confirm which
  legend rows feed which height, but not as proof: the 2' and 3' groups of line 308 are
  assigned from these notes alone.
  101 studs @ 12'-6" ⇔ 133.8 LF of 3-5/8" partitions.
- Runner LF ≈ Σ stud-row LF (within 2.1%).
- Specialty board SF = elevation-area legend rows, rounded up to 5 SF.
- PT-1 paint area on A-410 (252.6) = moisture board area; tile areas = cement board.
- PT6 = TYPE X GWB = 5/8" PLYWOOD BACKING = 37.2 SF on p28 (three items, one area).
- Booth: line 81 (1/2" plywood at booth wall) 47.7 SF = WALL 706 15.9 LF × 3'. Booth
  roof 76.2 → 77 is reused in framing (312) and paint (302).

## 5. Traps hit on this job

1. **Height is in the item name, not on the plan.** Read `@ 12'6"H` from the legend.
   The plan carries no wall heights, and the A-620 height designator (A/B/C) only says
   "to structure" or "to 6" above ceiling".
2. **One run feeds two stud lines.** The 18'8" double-stud wall (8.4 LF) is 3-5/8"
   (line 308) and 6" 16 GA (line 310). A takeoff that books it once loses 156.8 SF of studs
   and 8.4 LF of each runner. Do **not** copy the estimate's second VAT entry. Line 310 also
   carries a 6" 9'-0" group (~5.9 LF, 53.1 SF) that no drawing shows. On A-310 section 1
   the 6" VAT wall runs F.F.E. to the roof framing (~12'-3", the 9.2 LF `@ 12'3"H` row), and
   the 8" 7'-2" wall sits on the canopy beam. That group is estimator judgment or a double
   count.
3. **Parapets are separate rows at their height above the roof** and get no gypsum
   board. They do get glass-mat sheathing on the roof face (line 254).
4. **Exterior walls get board on one face only**, at full stud height. Rows suffixed
   `NO GWB` or `BS 1/2" SHTNG ONLY` get none.
5. **Spec vs estimate board type.** 09 29 00 §3.3.A (p278) requires 5/8" **Type X on all
   vertical surfaces** unless indicated, yet line 242 is "5/8" THK. GYPSUM BOARD". The spec
   is the governing material; the quantity is unaffected.
6. **Parapet sheathing thickness.** 06 16 00 (p131) says glass-mat "Type X, 5/8 inch
   unless indicated otherwise"; A-310/A-311/A-300 indicate "1/2" GLASS-MAT SHEATHING". The
   drawing governs, so 1/2" is right.
7. **Cement board double count.** WT3 at the transaction bar (38.4 SF) is in both the 5/8"
   cement board (266 = ceil5(244.2 + 38.4)) and the 1/4" backer (272). Walls-only 5/8" would
   be 245 SF.
8. **No backer spec.** 09 30 00 has no backer-board article. The cement board comes from
   A-620 series B/C ("5/8" CEMENT BOARD") and note N ("partitions scheduled to receive tile
   or FRP shall be water-resistant core gypsum"). FRP-1 (16 SF) did not get MR board.
9. **Unstated heights.** The mecho-shade furring (A-430 det. 8 and 9) and the high-low roof
   step wall (A-450 det. 8) are not dimensioned. The estimator's stud-count notes show 3'
   and 2'. Both row assignments are inferred from those notes. The 9' group in line 310 is
   not an unstated height. No drawing shows a 9' 6" wall at all (trap 2).
10. **Booth walls.** A-706 det. 9 shows 6" 16 GA studs @ 16" at 9'-0". The estimator carried
    the booth wall only as 3' of plywood (line 81). No 9' booth studs appear in lines 308–311.
11. **Gauge by height.** S-002's *Exterior Schedule of Metal Stud Sizes* (115 mph, Exp. C,
    Fy 33 ksi) picks the stud from three things: the wall-height band, the wind zone (4 =
    field, 5 = corner end zone, a = 5'-2"), and the deflection limit (L/360 at EIFS or metal
    panel, L/600 at masonry).
    - **Wind Zone 4, L/360, 6":** 600S162-43 up to 12'-6" (both the "Up to 11'-0"" and the
      "11'-0" to 12'-6"" bands), -68 to 15'-6", -97 to 16'-6", 600S200-97 @ 12" to 20'-0".
    - **Wind Zone 4, L/360, 8":** 800S162-43 up to 11'-0", -54 to 16'-6", -68 to 20'-0",
      -97 to 21'-0".
    - **L/600 and Zone 5 are heavier.** For a 6" stud at 11'-0" to 12'-6": -68 at L/600 and
      -54 in Zone 5.

    The gauge table on A-620 maps mils to gauges: 43 mil = 18 GA (0.0451"), 54 = 16 GA,
    68 = 14 GA, 97 = 12 GA. The estimator flattened every 6" and 8" exterior stud to 16 GA.
    Against S-002 (Zone 4, L/360), the legend rows come out like this:
    - **`EXT 6" @ 12'3"H`** (9.2 LF of 310): 600S162-43, 18 GA, lighter than carried. It is
      -68 if L/600 governs at the brick base, and -54 in Zone 5.
    - **`PARAPET WALL @ 7'2"H A310`** (5.9 LF of 311), a separate wall on the canopy beam:
      800S162-43, 18 GA. It is -54 in Zone 5.
    - **The 12'-9" + 4'-7" and 15'-9" + 1'-7" pairs** (89.7 + 96.6 + 41.5 + 8.7 + 46.0 =
      282.5 of 339.4 LF): A-310 draws one continuous 8" stud from F.F.E. to T.O. low parapet
      17'-4" (12'-9" + 4'-7" = 15'-9" + 1'-7" = 17'-4"). The band is therefore 16'-6" to
      20'-0", and the stud is 800S162-68 (14 GA), heavier than carried. These parapet rows
      are the upper part of a full-height stud, not "Up to 11'-0"" studs.
    - **`PARAPET WALL @ 2'7"H`** (38.0 LF) and **`EXT 8" @ 4'H`** (13.0 LF): the stud length
      is not resolved. They are -43 as separate short walls, and heavier if continuous.

    To carry the specified gauge, a takeoff must band each run by its full stud length, not
    by the estimator's wall/parapet split. The split is a quantity device.
12. **Openings are not deducted** from studs, runners or board. Do not net them out when
    reproducing this estimator (7 interior door openings ≈ 299 SF of board).
13. **The markup pages are raster images.** There are no vector lengths to re-measure; the
    legend's one decimal is the finest available precision.
