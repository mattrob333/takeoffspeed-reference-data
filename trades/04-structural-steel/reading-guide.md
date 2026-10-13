# Reading guide — 04 structural steel, joists, deck, misc. metals

## 1. Sheet order

1. **S-201 Foundation Plan** (read first, even though it is a foundation sheet). It carries the
   **STEEL COLUMN SCHEDULE**, **BASE PLATE SCHEDULE (36 KSI)** and **ANCHOR BOLT SCHEDULE (F1554 GRADE 36)**,
   and the base plate mark at every column (`BP12`, `BP14`, `BP1518`, next to the footing mark `F50` etc.).
2. **S-203 Roof Framing Plan.** Beam size + top of steel at every member (`W14X30` / `t/s 12' - 7 7/8"`),
   joist designations (`16KCS3`, `18KCS2`, `12KCS2`), the deck mark `RD-1.5` with span arrow, and the
   FRAMING KEY symbols: dash-dot line = continuous horizontal rigid bracing; `A.X.`; `H.B.`; `S.J.`; `S.P.`;
   the moment-connection flag. Also frame elevations 2 and 3, the SLAB AND DECK SCHEDULE and the notes
   (4"x3"x1/4" closure angle LLV; framing around openings 10/S-681; mechanical units 3/S-681).
3. **S-301 Elevations – Steel Frames.** Framing elevations 4–11 (3/16" = 1'-0") give column heights,
   diagonal braces (`HSS6X6X1/4` / `AXIAL = 15 K`), knee braces and the parapet channels (`C7X9.8`, `C8X11.5`)
   at the top of the frames.
4. **S-681 / S-682 / S-683 / S-685** typical details: cap plate table (8/S-681), RTU and opening framing
   (3/S-681 and 10/S-681; "A" members = C5x6.7), H.B. and A.X. sizes (1/S-682), bar joist roof
   construction (4/S-682), metal stud to steel (S-683: L3X3X3/16 continuous, L4X3X1/4 LLV).
5. **S-601/602/603** wall sections: the notes that define the small members (2x2x3/16 kicker angles;
   HSS4x4x1/4 posts at each high-roof joist; 2-1/2x2-1/2x3/16 at parapet-channel midspan).
6. **A-200, A-430** (canopy sign tube posts and 5x5 plate), **A-110 + A-450 detail 3** (ladder).

## 2. How each formula input is read

| Input | Where | Actual string on this job |
|---|---|---|
| Column size and count per size | S-201 STEEL COLUMN SCHEDULE (vertical size text, locations row) | `HSS7X7X1/2` – `A-1, A.5-1, B-1, C-2` · `HSS6X6X3/8` – `A-2.6, A-4, A.5-6` · `HSS5X5X3/8` – `A-2.9` · `HSS6X6X3/8` – `A-6, B-2` · `HSS6X6X3/8` – `B-4` (low roof) · `HSS6X6X1/2` – `B-6` · `HSS7X7X1/2` – `C-3` · `HSS6X6X3/8` – `C-6, D-6, E-3` · `HSS5X5X3/8` – `C-7` · `HSS6X6X1/4` – `D-5` |
| Column run length | S-301 / S-203 elevations, base plate to top of parapet channel | HSS7x7 average 19.46 ft; HSS6x6x3/8 runs 18.9–20.3 ft |
| Beam LF | S-203 plan, each member between supports | `HSS10X6X1/4 t/s 13' - 6 5/8"`, `W12X14 t/s 13' - 1 3/4"` … |
| Joist LF and count | S-203 plan, one line per joist | 10 × `16KCS3` (A–B), 4 × `18KCS2` (B–D), 3 × `12KCS2` (B–C) |
| Bridging rows | S-203 dash-dot rigid-bracing lines + legend "*2" | `RIGID JOIST BRACING *2` 121.9 FT; `L2-1/2x2-1/2x1/4 X-TYPE BRIDGING *2` 35.5 FT |
| H.B. | S-203 short magenta lines at `H.B.` tags | 19.1 FT `L3x3x1/4 HORIZONTAL BRACING` |
| Kicker angles | S-602 note + legend dots | `L2x2x3/16 ANGLE @ 4'L` 18 EA; `L2x2x3/16 ANGLE @ 5'8"L` 1 EA |
| Posts on beams | S-603 note + S-203 dots on grid B | `HSS4x4x1/4 POST @ 1'4"H` 6 EA |
| Deck SF | S-203 brown polygons | `1-1/2" WIDE RIB TYPE B 22GA. GALVANIZED (G90) ROOF DECK` 2208.4 SQ FT |
| Base plates | S-201 BASE PLATE SCHEDULE, COUNT column | `BP12 12" 12" 3/4" HEADED ANCHOR BOLT : 3/4" Ø 8" 10`; `BP14 14" 14" 1" … 4`; `BP1518 15" 18" 3/4" … 1" Ø … 4` |
| Cap plates | S-681 det 8 table, rows by column size (9 rows: W8, W10, HSS4X4, HSS5X5, HSS6.00 ROUND, HSS6X6, HSS8X8, HSS12X4, HSS12.75 ROUND) | `HSS5X5 → 3/4"x11"x5-1/2"`, `HSS6X6 → 3/4"x12"x6-1/2"` (no HSS7X7 row; `3/4"x13"x7-1/2"` is the HSS6.00 ROUND row) |
| Tube posts | A-200 legend, A-430 detail | `HSS1-1/2"x1-1/2"x3/16" TUBE POST @ 1'7"H` 6 EA; `1/4" x 5" x 5" STEEL PLATE` |
| Ladder | A-110 legend + A-450 det 3 | `1'9"W ROOF ACCESS LADDER - 1/A312` 1 EA; `13'-4" OVERALL LADDER HEIGHT (VERIFY)` |

The column schedule's text layer is scrambled: the size labels are vertical, and the text order does not
pair sizes with locations. **Render the schedule** and read it column by column; never pair them from
the text dump.

## 3. Grid geometry (for checks)

Horizontal, grid 7 → 1: 3'-6 1/2", 10'-7 7/16", 10'-0 13/16", 4'-6 1/4", 1'-10 5/8", 13'-8 7/8",
5'-3 1/2" = 49'-8". Vertical, A → E: 13'-8 7/8" (A–A.5), 11'-5 1/8" (A.5–B), 14'-11 1/2" (B–C),
9'-0 3/8" (C–D), 3'-5 3/8" (D–E) = 52'-7 1/4". So A–B = 25.17 ft, B–C = 14.96 ft and B–D = 23.99 ft.

## 4. Elevation → grid line map (S-301 and S-203)

| Elevation | Cut along | Columns marked (colour) |
|---|---|---|
| S-301 / 4 | line 6 (A, A.5, B) | A-6, A.5-6 red; B-6 not coloured here |
| S-301 / 5 | line 3 (E, C) | E-3 red; C-3 magenta |
| S-301 / 6 | line A (1 … 6) | A-2.6, A-4 red; A-2.9 dark green; A-1 and A-6 not coloured (taken elsewhere) |
| S-301 / 7 | line C (3, 2) | C-2 magenta |
| S-301 / 8 | line 1 (B, A) | A.5-1, A-1 magenta; two short HSS4X4X1/4 brown |
| S-301 / 9 | line B (2, 1) | B-2 red; B-1 magenta; HSS4X4X1/4 braces blue; W10X12 strut cyan |
| S-301 / 10 | line 6 (B, C, D) | B-6 bright green; C-6, D-6 red |
| S-301 / 11 | line 2 (C, B) | none (C8X11.5 at top) |
| S-203 / 2 | line D (6, 5, 3) | D-6 red (**repeat**), D-5 red (**schedule says HSS6X6X1/4**) |
| S-203 / 3 | line C (7, 6) | C-7 green (HSS5x5x3/8); C-6 red (**repeat**) |

GPT-6 Astra independently read the same cut lines and the same repeats (`trades/04-structural-steel/scripts/gpt_columns.txt`).

## 5. Cross-checks that work on this job

- Base plate COUNT total (10 + 4 + 4 = 18) = column schedule total (18). Anchor rods 56 = 10×4 + 4×4 and
  24 = 4×6.
- Cap plates 2 + 16 = 18 = columns.
- Unique column runs per size = schedule count per size (HSS7x7 5 ✓, HSS5x5 2 ✓, HSS6x6x1/2 1 ✓,
  HSS6x6x3/8: 9 on S-301 (8 + one stray) ✓, but 12 in the estimate ✗, HSS6x6x1/4: 0 ✗).
- Joist count × grid span ≈ joist LF: 16KCS3 10 × 24.86 vs 25.17 ✓; 12KCS2 3 × 17.99 vs 14.96 ✗ (+3.0 ft);
  18KCS2 4 × 27.12 vs 23.99 ✗ (+3.1 ft). Both high- and low-roof joists bear on the grid-B beam on S-203
  (vector strokes: 16KCS3 ends 0.75 ft north of the B beam line, 18KCS2/12KCS2 start 0.66 ft south of it).
- Column schedule bars on S-201 are drawn to scale (9 pt/ft between the 0'-0", 13'-0" and 16'-0" lines), so
  they give each column's height: B-4 runs −1'-0" to ~15.2 ft (16.2 ft), the others −2'-0" to 17.3–18.5 ft.
- Deck SF ≈ union of the plan outline. A darker band on the overlay means two polygons overlap.
- Pixel scale check: on half-size markup pages, 3/16" = 1'-0" is 6.2007 pt/ft and 1/4" = 1'-0" is
  8.2676 pt/ft. The magenta HSS7x7 rebuild came to 97.14 vs 97.3 (−0.16%).

## 6. Traps hit

1. **Duplicate legend names must not be merged.** p34 prints `HSS6x4x3/8 BEAM` twice, 22.2 FT (brown)
   and 9.0 FT (periwinkle). Both rows are in legends.json (items 33 and 6), and the estimator keeps them
   as two lines (45 = 22.24, 46 = 8.98). Keying a lookup by name alone would drop or merge one.
2. **Same column measured twice.** p35 (second S-203 markup copy) has its own legend for frame
   elevations 2 and 3. Summing pages blindly adds C-6 and D-6 a second time (40.86 LF).
3. **Wrong size on a measured column.** D-5 is `HSS6X6X1/4` in the schedule but was traced in the
   HSS6x6x3/8 colour, so there is no HSS6x6x1/4 COLUMN line. Do not confuse it with `HSS6X6X1/4` braces
   on S-301.
4. **A stray run.** One red 19.03 ft line on p36 sits on no elevation (x ≈ 0.56 of the page, beside
   the brace-connection details). It probably stands in for the ninth HSS6x6x3/8 (B-4, an interior
   low-roof column that no elevation shows), but this is not proven. B-4 is shorter than the other
   columns: its S-201 schedule bar runs from 1'-0" below Level 1 to ~15.2 ft (the t/s 15'-2 1/4" of the
   grid-B HSS4X4X1/4 beam), so 16.2 ft (17.2 ft with a 2'-0" base). 19.03 ft over-states it by ~1.8–2.8 ft.
5. **"*2" in item names is a multiplier**, not part of the size. Rigid bracing (×2 chords) and X-bridging
   (×2 diagonals) go into one L2-1/2 line.
6. **Size conflicts between sheets and spec.** A.X. bridging: L2-1/2x2-1/2x1/4 (S-682 det 1, 05 1200)
   vs 2"x2"x1/4" (S-203 key, 05 2100 O); the estimator used L2-1/2. Deck: 22 ga on the drawings vs
   20 ga in 05 3000; the estimator used 22 ga. Ladder: aluminum (A-450) vs galvanized steel (05 5000);
   the estimator used aluminum.
7. **Dead sheet reference.** A-110 says the ladder is at "1/A312"; there is no A-312. The ladder detail
   is 3/A-450.
8. **Count items carry the length in the name** (`@ 4'L`, `@ 1'4"H`, `@ 1'7"H`). A quantity engine that
   reads only the legend unit (EA) loses the LF.
9. **Deck overlap strip.** About 3.6–3.8 ft deep at grid B, its top edge 3.3 ft north of the B beam line,
   drawn twice (≈ 170–190 SF). The low-roof joist
   lines start at the top edge of the same band (3.3 ft north of B; GPT-6 Astra reads the crop the same
   way), although on S-203 they bear on the grid-B beam. That is why lines 70 and 72 run ~3 ft per joist
   longer than B–C / B–D: drawing-true 44.88 and 95.96 LF grid to grid, not 53.96 and 108.49.
10. **Legend counts vs schedule counts.** BP12 legend 9 vs schedule 10; the estimator used the schedule.
11. **Cap plate for a size not in the table** (HSS7X7): the estimator used the HSS6X6 plate.
12. **C7x9.8 on plan and elevation.** 236.7 FT on the plan (S-203) follows the canopy outlines; there is
    no yellow trace on the bare parapets along grid A or grid 7. 177.8 FT on S-301 is the parapet-top
    channels plus two lower C7X9.8 runs in elevations 7 and 11 (15.0 + 14.6 = 29.6 FT, the ones with
    the canopy rain-leader note). Only those two lower runs can repeat the plan canopy outline (along
    line C 3–2 and line 2 B–C): ≈ 30 LF, 7% of line 61. Match them by grid before summing; the overlay
    cannot prove it because the canopy fill is the same yellow.
