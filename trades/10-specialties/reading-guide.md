# 10 — Specialties: reading guide

## 1. Toilet accessories (A-410)

1. **Start with the schedule.** The TOILET ACCESSORY SCHEDULE is at the top right of A-410 and has three columns: ITEM NO,
   DESCRIPTION, MODEL. The tags are printed with two digits there (`TA-01` … `TA-10`), with one digit on the plan
   (`TA-1`), and with no hyphen in the PlanSwift legend (`TA1`). Normalise them all to `TA-n`. There is **no TA-07**.
   The MODEL column also carries responsibility:
   - `OWNER VENDOR PROVIDED, GC TO INSTALL, GC TO ORDER` on TA-01, TA-02 and TA-05 means OFCI.
   - `REFERENCE DOOR HW SCHEDULE` on TA-09 means the item is carried in Div 08 (A-601 set 11.0). It is not owner-vendor.
   - A Bobrick or Bradley model means CFCI.
2. **Count the placements on ENLARGED RESTROOM PLAN 6 only.** Every tag sits once per room, in a box next to the fixture.
   MEN'S 112 is the left room and WOMEN'S 111 the right one. JANITOR 115 is at the far left and holds only TA-10. The
   markup (p16) puts a coloured dot on each plan tag, so the legend counts equal the plan counts: TA1 2, TA2 2, TA3 2,
   TA4 2, TA5 2, TA6 2, TA8 1, TA9 2, TA10 1.
3. **Get the grab-bar lengths from detail 2, and confirm them on the elevations.** Detail 2 TYPICAL ACCESSIBLE ACCESSORY
   HEIGHTS (ACCESSIBLE WATER CLOSET diagrams) prints the side bar **42" MIN** (12" MAX from the rear wall, 54" MIN
   extent), the rear bar **36" MIN** (24" MIN + 12" MIN about the WC centreline) and the vertical bar **18" MIN** at
   39"–41" A.F.F. Elevations 7–10 (women's) are at 1/2" = 1'-0"; the note says "MENS INTERIOR ELEVATIONS ARE SIMILAR TO
   WOMENS". The 5'-6" tile dimension is a handy scale bar. Scaling the bars agrees with detail 2 to about ±0.3".
   - **Elevation 9 (B)** looks at the wall behind the WC. It shows the 36" rear bar, the mirror (24" × 36") and TA-02. On
     the left edge, the vertical bar appears in profile and the 42" bar end-on.
   - **Elevation 8 (C)** looks at the side wall. It shows the 42" horizontal bar, the 18" vertical bar, TA-1 and TA-8.
   - Detail 2 gives the bar lengths and mounting heights; elevations 1/3 (janitor) give mounting heights. Neither gives
     counts.
4. **Cross-checks:**
   - Each tag should appear once per room on the plan (TA-8 only in the women's).
   - Every scheduled tag should be placed somewhere.
   - Tags on the elevations should be a subset of the plan tags.

**Traps:**

- **The text layer repeats tags.** Tags appear on the plan and again on the elevations: TA-1 4×, TA-3 4×, TA-10 2×.
  Restrict the count to the plan viewport (x ≈ 0.03–0.38, y ≈ 0.43–0.70 of the sheet).
- **TA-3 is a set, not a bar.** One tag covers three bars. Reading only the plan gives "2 grab bars". The estimator read
  two of the sizes and missed the 36" rear bar.
- **The schedule gives no sizes.** "BRADLEY 1-1/4" STAINLESS STEEL GRAB BAR W/ CONCEALED MOUNTING" has no length, and the
  B-290 mirror has no size. Take the bar lengths from detail 2 (42" / 36" / 18"); scale the mirror from elevation 9.
- **TA-09 points to the door hardware schedule.** A-601 set 11.0 (doors 112, 113) already lists `2 Coat Hook RM817
  US26D RO` per door (4 in all). The hardware set carries the hooks; report the TA-09 plan count only as a cross-reference
  with a duplicate warning.
- **TA-04 B-3644 is recessed "(FOR 4" WALLS)".** It needs a stud-wall opening, which the framing trade has to coordinate.
  It does not change the count.

## 2. Signage (G-001, G-002)

1. **Read the LIFE SAFETY NOTES legend on G-001** (top right). Its symbols:
   - `F.E.` SURFACE MOUNTED FIRE EXTINGUISHER 10LB UL RATED 4A:80B:C
   - `F.E.C.` RECESSED FIRE EXTINGUISHER CABINET 10LB UL RATED 4A:80B:C
   - `M.C.#` MAXIMUM CAPACITY SIGNAGE…
   - `T.S.` TACTILE SIGNAGE PER NFPA 101-7.10.13, REFER TO G-002
   - `K.B.` KNOX BOX
2. **Count the symbols in the plan viewport:**
   - T.S. = 3 (east exit door; inner and outer doors of the south vestibule).
   - F.E.C. = 2.
   - K.B. = 1.
   - F.E. = 0 and M.C.# = 0. Both appear only in the legend.

   Restroom signs are not symbolised. The markup puts the brown dot (legend ADA WOMAN) at door 113, which serves MEN'S
   112, and the cyan dot (legend ADA MEN) at door 112, which serves WOMEN'S 111. The colours are swapped; the counts (1 + 1)
   are right.
3. **Read the sizes from G-002:**
   - The GENERAL NOTES - SIGNAGE detail draws the restroom sign **6" wide × 9" high** (a 6" pictogram field over a 3" text
     and braille band).
   - **2/G-002 TACTILE EXIT SIGN** is **6" × 4"**, drawn in three messages: "EXIT" AT EXIT DISCHARGE, "TO EXIT" AT LOBBY
     AREAS WITH DOOR TO BUILDING EXIT DISCHARGE, and "EXIT ROUTE" AT ROOM/AREA EXITS LEADING TO BUILDING EXITS. On G-001
     the east exit door and the vestibule outer door are exit discharge (EXIT); the vestibule inner door is most likely
     TO EXIT. Record the message per T.S. location.
   - Notes 1–4 give the lettering: "1. 5/8" HIGH BY 1/32" RAISED LETTERING", Grade 2 braille, 1/32" raised pictogram, blue
     background with white letters, eggshell finish. The text layer prints this as "1.5/8"", which is note number 1
     followed by 5/8".

**Traps:**

- **More than one exit-sign size.** G-002 also draws a 5" × 3" "EXIT" plaque inside the restroom sign detail, and detail
  2 draws a 2" × 8" vertical "EXIT" as an ALTERNATE EXIT DISCHARGE sign for egress routes with limited wall surfaces. The
  estimator used the 6" × 4" from detail 2 for all 3.
- **Room numbers and door numbers are crossed at the restrooms.** MEN'S is room 112 behind door 113; WOMEN'S is room 111
  behind door 112 (A-110, A-410 plan 6; A-601 set 11.0 "Doors: 112 (Womens), 113 (Mens)"). There is no door 111 in that
  set (door 111 is the Work Room). Key restroom signs by room name, not by number.
- **Room-ID signs are required but not counted.** Note 25 on G-002 and A-120 requires tactile room-ID signs for permanent
  rooms, but no sheet counts them.
- **Exterior signage is not in this trade.** A-200 and A-201 say "SIGNAGE SHOWN FOR REFERENCE… SEPARATE SIGNAGE PACKAGE",
  so exterior building signage belongs to the sign vendor.

## 3. Fire extinguisher cabinets (G-001, A-110, specs 10 44 13 / 10 44 16)

- **Count:** count the `F.E.C.` symbols on G-001 (2). Cross-check the `FEC` tags on A-110 (2) and the G-001 CODE
  INFORMATION table row `FIRE EXTINGUISHERS (906.1) REQUIRED PER 906.3 / PROVIDED 2`. The markup has **no** legend row for
  them, so the count comes from the drawing.
- **Type:** the legend says recessed. Spec 10 44 13 p. 340 says the cabinet is recessed, flat SS trim, frameless clear
  acrylic door. Basis of design: JL Panorama 1035C70 or Larsen's Gemini GSS2409R2-C. If the wall is too thin, use
  semi-recessed (p. 342).
- **Extinguisher:** spec 10 44 16 p. 345 calls for 10 lb 4-A:60-B:C, JL 10E or Larsen's MP10. The legend says 4A:80B:C.
  Flag the conflict.
- **Mounting:** the A-600 device mounting elevation has a dimension "TO TOP OF F.E.C." (read the value on the render; the
  text layer does not pair it with the label). Spec 10 44 16 3.2.A says brackets at 54" to the top of the extinguisher.
  Mounting height does not change the count.

## 4. Panel system PNL-1 (A-706, A-170)

1. **Get the type from A-170.** The FINISHES SCHEDULE is a raster image with no text layer; render A-170 and read the
   PANEL SYSTEM row: `PNL-1 BOOTH SCREEN | BIG APPLE VISUAL GROUP | SEE PLAN | PANEL SYSTEM`.
2. **Get the area from INTERIOR ELEVATION - BOOTH 6/A-706** (1/2" = 1'-0"). There are two PNL-1 tagged fields between the
   9" PL-1 jambs and the booth opening, both under the 9" PL-1 head, with a 9'-0" dimension. Their widths are printed
   on ENLARGED BOOTH CEILING PLAN 11/A-706 (right-hand string 9", 1'-4", 4'-6 1/2", 2'-8", 9"): **2'-8"** and **1'-4"**.
   (32 × 108 + 16 × 108) / 144 = 36 SF. Details 7 and 8 call out "PNL-1, DOUBLE-SIDED PANEL w/ REPEATING PATTERN";
   details 8 and 4 call out "HARDWOOD BLOCKING FILLER".
3. **Do not attach the PL-1 wall build-up to PNL-1.** The "13/16" PL-1 LAMINATE PANEL ATTACHED TO SUBSTRATE w/ 'Z' CLIPS",
   "PLYWOOD SUBSTRATE" and "16 GAUGE METAL STUD FRAMING @ 16" O.C." callouts on details 7/8/9 are the PL-1 booth walls,
   carried in other trades.

**Trap:** do not double the area for "double-sided" or "BOTH SIDE". The estimator and the legend carry one face area.

## Cross-check list

| Check | Expect |
|---|---|
| Legend TA counts (p16) = plan-6 tag counts | All equal |
| TA-3 count × 3 bars = grab bars on the elevations | 6 (estimator carried 4) |
| G-001 F.E.C. = A-110 FEC = code table PROVIDED | 2 = 2 = 2 |
| G-001 T.S. symbols = legend p2 tactile | 3 = 3 |
| PNL-1 SF from elevation = legend p29 | 36.0 = 36 |
| Coat hooks: TA-09 vs HW set 11 | 2 vs 4: HW set 11 carries them; TA-09 is a cross-reference |
