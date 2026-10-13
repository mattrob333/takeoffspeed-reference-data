# 10 — Specialties: formulas

All arithmetic was run in Python (`trades/10-specialties/scripts/build.py`). Printed dimensions are the inputs. Lengths
scaled from the PDF vector geometry (at 1/2" = 1'-0" there are 3 pt per real inch) are cross-checks only, good to about
±0.3".

## F1. Toilet accessory count by tag

- **Inputs:**
  - `count[room]` (EA): the number of times tag TA-n appears on the **enlarged restroom plan 6/A-410**, one value per room.
  - Optional `perRoom` × `rooms` when the room is typical.
- **Rule:** `EA = Σ count[room]`. Count the plan only. Tags on the elevations (7–10, 1, 3) repeat the plan placements and are
  not added.
- **Convention:** one plan tag is one unit, except TA-3 (see F2). The schedule has no QTY column, so there is nothing to
  reconcile against except the plan.
- **Worked example (this job):**

  | Tag | MEN 112 | WOMEN 111 | JANITOR 115 | Total | Legend p16 |
  |---|---|---|---|---|---|
  | TA-1 | 1 | 1 | | 2 | 2 |
  | TA-2 | 1 | 1 | | 2 | 2 |
  | TA-4 | 1 | 1 | | 2 | 2 |
  | TA-5 | 1 | 1 | | 2 | 2 |
  | TA-6 | 1 | 1 | | 2 | 2 |
  | TA-8 | 0 | 1 | | 1 | 1 |
  | TA-9 | 1 | 1 | | 2 | 2 |
  | TA-10 | | | 1 | 1 | 1 |

  Lines 324–331 and 328 reconcile exactly.
- **Trap:** the A-410 text layer has each tag on the plan **and** on the elevations. Counting every text instance gives
  TA-1 = 4, TA-3 = 4 and TA-10 = 2.

## F2. Grab bars: one TA-3 tag expands to a set, sized from the elevations

- **Inputs:**
  - `n_TA3` (EA): TA-3 tags on plan 6, one per accessible water closet.
  - `bars` (in): the nominal length of each bar, printed on **detail 2/A-410 TYPICAL ACCESSIBLE ACCESSORY HEIGHTS**
    (ACCESSIBLE WATER CLOSET diagrams).
- **Rule:** `EA(size) = n_TA3 × bars of that size per set`.
- **What the drawings show:**

  | Bar | Detail 2/A-410 (input) | Where drawn | Elevation scale check (±0.3") |
  |---|---|---|---|
  | Side wall, horizontal | **42" MIN** (12" MAX from rear wall, 54" MIN extent) | elev. 8 (C) | ~42" |
  | Vertical | **18" MIN** at 39"–41" A.F.F. | elev. 8 (C) in full; elev. 9 (B) in profile only | ~18" |
  | Rear wall, horizontal | **36" MIN** (24" MIN + 12" MIN about the WC CL) | elev. 9 (B) | ~36" |

  So each set is 1 × 42" + 1 × 36" + 1 × 18". The elevation check subtracts a flange of about 1.8"–2" from the drawn
  extent, so it confirms the nominal length but cannot resolve it finer than about ±0.3".
- **Estimator convention:** the estimator carried 1 × 18" vertical and 1 × 42" horizontal per TA-3, with no 36" bar. From
  this job: `estimator bars per TA-3 = (2 + 2) / 2 = 2`, against 3 drawn.
- **Worked example:**
  - Line 322 (18" vertical) = 2 × 1 = **2 EA**.
  - Line 323 (42" horizontal) = 2 × 1 = **2 EA**.
  - The 36" rear bar would be 2 × 1 = 2 EA. It is not carried.
- **Basis:** ADA 2010 §604.5.1 requires a 42" min side-wall bar and §604.5.2 a 36" min rear-wall bar. The 18" vertical bar is
  an ICC A117.1 (2017) requirement, which ADA 2010 does not have; the drawings show it, so it is carried.

## F3. Mirror size (description input, not a quantity)

- **Rule:** the size is the frame W × H on the elevation.
- **Worked example:** TA-06 on elevation 9 scales to about 24" × 36", so the line description reads 2'x3'. The schedule gives
  only the model, B-290; B-290 2436 is that size.

## F4. Signage count by type and size

- **Inputs:** `count` (EA) of each sign symbol on G-001: T.S. for tactile exit signs; the restroom signs are at the restroom
  doors. Size `W × H` (in) and message from the G-002 details.
- **Rule:** `EA = Σ symbols`. The size is part of the description.
- **Worked example:**
  - T.S. = 3: east exit door, and the inner and outer doors of the south vestibule. That gives **3 EA 6"x4"**. Detail
    2/G-002 draws three 6" × 4" messages: "EXIT" AT EXIT DISCHARGE, "TO EXIT" AT LOBBY AREAS WITH DOOR TO BUILDING EXIT
    DISCHARGE, and "EXIT ROUTE" AT ROOM/AREA EXITS LEADING TO BUILDING EXITS. Here the east exit door and the vestibule
    outer door are exit discharge (EXIT, 2); the vestibule inner door is most likely TO EXIT (1), or EXIT ROUTE — the
    plan does not label the message, so the takeoff should record the message per door as a read, not a given. The detail also draws a 2" × 8"
    vertical "EXIT" as an ALTERNATE for egress routes with limited wall surface; it is not used here.
  - Men 1 and women 1 give **6"x9"** each: the G-002 restroom sign detail is 6" wide by 6" + 3" = 9" high. On the markup
    the estimator's dots are colour-swapped (brown ADA WOMAN at door 113 = MEN'S 112; cyan ADA MEN at door 112 = WOMEN'S
    111). The counts are unaffected.
  - Lines 332–334 reconcile exactly.

## F5. Fire extinguisher cabinets

- **Inputs:** `count` (EA) of **F.E.C.** symbols on G-001. Cross-checks: the FEC tags on A-110, and the G-001 code table
  row "FIRE EXTINGUISHERS (906.1) … PROVIDED 2".
- **Rule:** `EA cabinets = Σ F.E.C.`. Bracket units would be `EA = Σ F.E.` (0 on this job).
- **Worked example:** G-001 F.E.C. 1 + 1 = **2 EA**, which matches A-110 FEC (2) and the code table (2). Line 335 reconciles.
- **Extinguishers are a separate record, not a convention.** Spec 10 44 13 covers the cabinets and refers the
  extinguishers to Section 10 44 16 (spec p. 339), which specifies a 10 lb 4-A:60-B:C unit (p. 345). The extinguisher
  record would be `EA = Σ F.E.C. + Σ F.E.` = 2 × 10 lb. Line 335 reads only "FIRE EXTINGUISHER CABINET" and the estimate
  has no extinguisher line, so the 2 extinguishers are **unresolved scope** (omitted, owner-furnished, or bought
  elsewhere — the estimate does not say). The rating is a legend (4A:80B:C) vs spec (4-A:60-B:C) conflict to flag.

## F6. Panel system face area (PNL-1)

- **Inputs:** each PNL-1 field `W × H` (in). The widths are the printed **2'-8"** and **1'-4"** dimensions on enlarged
  booth ceiling plan 11/A-706 (right-hand string 9", 1'-4", 4'-6 1/2", 2'-8", 9"). The height is the **9'-0"** dimension on
  interior elevation 6/A-706, from the floor to the underside of the 9" PL-1 head.
- **Rule:** `SF = Σ (W × H) / 144`. The panel is **one** face area even though it is "DOUBLE-SIDED": the panel is a single
  element seen from both sides, so it is not × 2.
- **Worked example:**

  | Field | Width (plan 11) | Height (elev. 6) | Area |
  |---|---|---|---|
  | Left | 2'-8" = 32" | 9'-0" = 108" | 24.0 SF |
  | Right | 1'-4" = 16" | 9'-0" = 108" | 12.0 SF |

  Total = (32 × 108 + 16 × 108) / 144 = **36.0 SF**. That equals the legend (36 SQ FT, teal) and line 336, at 0.0 %.
  Cross-checks: the vector edges on elevation 6 give about 32" and 16"; the teal markup area on p29 scales to about
  35.5 SF (edge loss), so the estimator measured the same two fields at the full 9'-0".
- **Related (not this trade):** the hardwood blocking filler is a component of the panel, named in the description. The
  13/16" PL-1 laminate wall panels on Z-clips, their plywood substrate and the 16-ga stud framing on details 7/8/9 belong
  to the PL-1 booth walls, not to PNL-1. Plywood backing and blocking are carried in `05-rough-carpentry` (lines 89–90,
  145–147).

## Conventions table

| Convention | Value | Basis |
|---|---|---|
| Accessory count source | Enlarged plan only, one tag per unit | A-410: every legend count equals the plan-6 tag count |
| Grab bar set per accessible WC | 42" side + 36" rear + 18" vertical; estimator carried 42" + 18" | Detail 2/A-410 (lengths); elevations 8 and 9, A-410 (cross-check); ADA 604.5 |
| Coat hooks TA-09 | Carried in door hardware set 11.0 (2 per door × 2 doors = 4); TA-09 plan count (2) is a cross-reference with a duplicate warning | A-410 schedule "REFERENCE DOOR HW SCHEDULE"; A-601 set 11.0 |
| Cabinets vs extinguishers | Cabinets = Σ F.E.C. (2); extinguishers are a separate 10 44 16 record (2 × 10 lb) that this estimate does not carry: unresolved scope | Spec 10 44 13 p. 339 → 10 44 16; line 335 wording |
| Double-sided panel area | 1 × face area | Line 336 = legend 36 SF = one face of elevation 6 |
