# Reading guide: flooring, grout, base, transitions

## 1. Start from the finish schedule (A-170)

The FINISHES SCHEDULE on A-170 SCHEDULES is a raster table. Its text layer holds only the title, so it has to be read as an image (`render.py sheet A-170 out.png 0.53 0.21 0.86 0.50 4`). It has the columns `ITEM | DESCRIPTION | MANUF. | SIZE | SERIES | COLOR | REMARKS`. These are the rows for this trade:

```
FLOOR FINISHES
CR-1  CARPET          MOHAWK      12" x 36"  LICHEN COLLECTION   STONE COMMUNITY (GT472) 949 STONE         INTALLATION: HALF LAP
CR-2  CARPET          MOHAWK      12" x 36"  LICHEN COLLECTION   MICRO BLOOM II (GT475) 975 FELTED FRINGE STONE FINISH   INTALLATION: HALF LAP
CR-3  CARPET          MOHAWK      12" x 36"  LICHEN COLLECTION   MACRO BLOOM II (GT474) 975 FELTED FRINGE FINISH         INTALLATION: HALF LAP
CR-4  WALK-OFF CARPET MANNINGTON COMMERCIAL 18" x 36" CHARGE    STYLE: CHARGE, COLOR: FLUID (32367)        INSTALLATION: HORIZONTAL BRICK ASHLAR
FT-1  CERAMIC TILE    FLORIDA TILE 24" x 24" AVENTIS            VELVET    UNPOLISHED. GR-1 GROUT. CONTACT: FLORIDA TILE ...
LVT-1 LUXURY VINYL TILE INTERFACE 25cm x 1m  ON GRAIN 4.5mm     EARTHEN FORMS, COLOR: A03305 BESPOKE TIMBER  INSTALL PATTERN: ASHLAR w/ GLUED PERIMETER
LVT-2 LUXURY VINYL TILE MOHAWK    12" x 24"  C0135 MATAYO PLUS STONE  COLOR: 972A SONIC SILVER STONE
CON-1 SEALED CONCRETE BENJAMIN MOORE  -      COROTECH HIGH PERFORMANCE  CLEAR ACRYLIC
MT-1  ANTI-STATIC MAT MATS INC.   36" x 48"  -                    BLACK     ANTI STATIC/ANTI FATIGUE, COLOR: BLACK
TRANSITION STRIP
FTS-1 TRANSITION STRIP SCHLUTER  -  SCHIENE AE100     SATIN ALUMINUM   CARPET TO TILE
FTS-2 TRANSITION STRIP SCHLUTER  -  SCHIENE AE100     SATIN ALUMINUM   VINYL TILE TO CERAMIC TILE
FTS-3 TRANSITION STRIP SCHLUTER  -  RENO U AE100      SATIN ALUMINUM   TILE TO SEALED CONCRETE
FTS-4 TRANSITION STRIP SCHLUTER  -  RENO-RAMP AERP    SATIN ALUMINUM   SEALED CONCRETE TO MAT
GROUT
GR-1  GROUT  CUSTOM BUILDING  EPOXY  335 WINTER GRAY   TRANSACTION BAR & FLOOR TILE
GR-3  GROUT  CUSTOM BUILDING  EPOXY  543 DRIFTWOOD     SERVICE AREA, EMPLOYEE LOUNGE, RESTROOM WALLS
WALL BASE & TRIM
WB-1  RUBBER BASE  JOHNSONITE  4"  TRADITIONAL WALL BASE  #48 GREY   CONTACT: KAREN ROYAL ...
```

From the WALL TILE / COVERING group, also read:

- `WT-8 BULLNOSE ROCA 3" x 12" FLOW TENDER GRAY (FLOTG10-S4312) BULLNOSE AS BASE`
- the trim callouts on the WT-1 row (`TOP TRIM: SCHLUTER JOLLY J AE WITH INSIDE & OUTSIDE CORNER TRIM ACCESSORIES`) and on the WT-9 row (`COVE TRIM: SCHLUTER DILEX-AHK 1S AE WITH INSIDE & OUTSIDE TRIM ACCESSORIES`). Those two trims are flooring lines 233 and 234.

Reading notes:

- **There is no GR-2.** The numbering skips from GR-1 to GR-3. Two grout tags are not two missing lines.
- **LVT-2 is scheduled but no plan tag carries it.** Do not take it off.
- **The size column is the product module, not the takeoff.** The MT-1 size "36" x 48"" disagrees with the plan, which draws the mat 2'-0" x 3'-0" (see the traps in §6).

## 2. The finish plan (A-150, markup p08)

**Room tags.** Every room carries a stack of hexagon tags in the order wall paint / base / floor: `PT-1 / WB-1 / FT-1`, `PT-1 / WB-1 / CR-2`, `PT-1 / WB-1 / CON-1`, `PT-1 / WB-1 / LVT-1`, `PT-1 / WB-1 / CR-4`. Rooms that have an inset pattern list more than one floor tag:

- MEETING ROOM 105: `CR-1 / CR-2`
- RELAXED SEATING AREA 102: `CR-1 / CR-2 / CR-3`

**Legend hatches** (LEGEND - FINISH PLAN, right column):

| Hatch | Tag |
|---|---|
| plain | CR-1 GROUND COVER |
| diagonal | CR-2 MICROBLOOM |
| cross-hatch | CR-3 MACROBLOOM |
| speckle | sealed concrete |
| 2' grid | FT-1 |
| plank courses | LVT-1 |
| dark brick | CR-4 |

The hatch tells you which tag a polygon belongs to inside a room that carries several tags.

**Transition tags.** These are text call-outs with arrows to the boundary:

- `FTS-1`: nine call-outs
- `FTS-2`: two, on the east and south edges of GATHERING AREA 103
- `FTS-3`: one, at the ELEC./I.T. 106 door
- `FTS-4`: one, pointing to the MAT-1 outline

The key notes also locate transitions:

- F001: FTS-1 at the transaction bar ADA panel
- F002: meeting room DIRTT door, see detail 5
- F003: booth millwork face
- F004: level change at an exterior door, bevel 1:2. It appears at exterior doors 100 and 110.

**Details 1 to 4, bottom of A-150.**

- Each gives the profile and the build-up:
  - FTS-1 "SCHLUTER RENO-TK TRIM 3/8" ... (ATK 100AT) ... FLOAT SLAB 3'-0" FOR FINISHES TO ALIGN"
  - FTS-2 and FTS-4 "1/4" CEMENT BOARD UNDERLAYMENT OVER CONCRETE SLAB ... STAGGER AND FILL SEAMS"
- Every detail carries the note "MITER ALL SCHLUTER METAL STRIPS AT JOINTS AND INTERSECTIONS - TYPICAL".
- The FTS-2 and FTS-4 details call the finishes "VINYL COMPOSITION TILE". That is boilerplate; the schedule's LVT-1 and MT-1 govern.

**General notes that change measurement.**

- C: "WHEN A CHANGE IN FLOOR FINISH OCCURS AT DOORWAY, THE SEAM IS TO BE CENTERED UNDER THE DOOR". This gives the door-strip split.
- D: "THRESHOLDS/TRANSITION STRIPS MUST BE PROVIDED BETWEEN DIFFERING FLOORING MATERIALS". This gives one transition at every material change.
- A and B: field verify; do not scale.

**"TILE START POINT".** This is in ENTRY 101 and sets the FT-1 grid layout. It is not a quantity, but it drives cut waste.

## 3. The PlanSwift markups for this trade

| Page | Sheet | Legend rows used | Colour |
|---|---|---|---|
| p08 | A-150 | `CON-1 FLOORING 68.8 SQ FT` | olive/khaki |
| p08 | A-150 | `CR1 FLOORING 131.4 SQ FT` | periwinkle blue |
| p08 | A-150 | `CR2 FLOORING 435.7 SQ FT` | yellow |
| p08 | A-150 | `CR3 FLOORING 27.1 SQ FT` | bright green |
| p08 | A-150 | `CR4 FLOORING 82.4 SQ FT` | cyan |
| p08 | A-150 | `FT1 FLOORING 946.1 SQ FT` | magenta |
| p08 | A-150 | `LVT1 FLOORING 94.0 SQ FT` | medium green |
| p08 | A-150 | `MAT-1 FLOORING 6.0 SQ FT` | slate/indigo |
| p08 | A-150 | `WB-1 404.7 FT` | light green |
| p08 | A-150 | `FTS1 TRANSITION 51.6 FT` | dark grey |
| p08 | A-150 | `FTS2 TRANSITION 29.0 FT` | red/coral |
| p08 | A-150 | `FTS3 TRANSITION 12.2 FT` | cyan |
| p08 | A-150 | `FTS-4 TRANSITION 10.0 FT` | purple/orchid |
| p16 | A-410 | `WT-8 BASE 11.3 FT` | yellow |
| p16 | A-410 | `SCHLUTER COVE TRIM 51.9 FT` | olive/khaki |
| p16 | A-410 | `SCHLUTER TRIM 39.6 FT` | slate |

Reading the markup pages:

- **Hyphens differ.** Legend names drop the hyphen (`CR1`, `FT1`, `FTS1`) while the drawing tags keep it (`CR-1`, `FTS-1`), and two items keep it (`CON-1`, `MAT-1`, `FTS-4`). Match on the normalised tag.
- **Colours repeat.** `CR4 FLOORING` and `FTS3 TRANSITION` are both cyan (106, 253, 254), and `CON-1` and `PT8` are both olive. Identify an item by its legend name, not by its colour.
- **Rows that are not flooring.** `FINISH 1.0 EA` (magenta dot over general note G) and all the PT, WC, FRP and PT4/7/8 rows on p08 belong to other trades.
- **What each colour covers on p08.**
  - Magenta FT-1 fills the corridors, ENTRY, LIBRARY, SERVICE COUNTER, EMPLOYEE LOUNGE, restrooms and JANITOR.
  - Yellow CR-2 fills PHONE 114, WORK 111, TRANSACTION BAR 108 and BOOTH 104, and forms the outer diamond ring in 105 and 102.
  - Blue CR-1 is the field round the diamonds.
  - Green CR-3 is the inner diamond in 102.
  - Olive CON-1 fills 106, with the indigo MAT-1 rectangle inside it.
  - The FTS lines sit on the boundaries.

## 4. How each formula input is read

- **Floor area per tag (F1).**
  - Trace each tag's polygon on A-150 to the finished wall face. Stop at the door centreline (note C).
  - Split rooms by hatch. Measure an inset once, in its own tag, and deduct it from the field.
  - The A-150 vector layer prints no room dimensions. Scale at 1/4" = 1'-0", which is 18 pt/ft on the 2592 × 1728 pt sheet. Take wall faces from the 1.59-pt wall lines.
  - Checks: ELEC./I.T. 106 is 6'-9 3/8" × 10'-11" (6.783 × 10.917 ft). The LVT plank hatch in GATHERING AREA 103 is 9.739 × 9.622 ft.
  - A-120 dimension strings are to stud and grid lines. Use them only as a cross-check.
- **Mat (F8).** Take the count from the plan (one `MAT-1` tag in 106) and the size from A-170 (`36" x 48"`). Then compare with the drawn outline: the A-150 rectangle is (1044.6, 554.6)-(1080.6, 608.6) pt = 2'-0" × 3'-0". Report the conflict.
- **Grout (F3).**
  - Each grout tag lists in its REMARKS the tiles it serves. The tile rows say which grout they take (`FT-1 ... GR-1 GROUT`).
  - GR-3's "RESTROOM WALLS / SERVICE AREA / EMPLOYEE LOUNGE" means the WT-1, WT-2 and WT-9 restroom band plus the A-703 (service counter) and A-705 (employee lounge) backsplashes.
  - The joint width is spec 09 3000 3.3.F, 1/4" unless otherwise indicated. Nothing on the drawings indicates otherwise.
  - Tile thickness is not given anywhere.
- **Base (F4).**
  - WB-1 is tagged in every room's stack. Trace every wall face that has a floor finish against it, and break at each door (A-600 widths: 3'-0" leaves, 6'-0" pairs at 100 and 101, and 3'-4" at DIRTT 105).
  - The spec style rule is Style A straight at carpet and Style B cove at resilient flooring. Record which floor the base meets.
  - In the restrooms, A-410 elevation A shows `WT-8` bullnose base and a "SCHLUTER COVER TRIM" leader. Elevations B, C and D show the tile band coming down to a Schluter cove at the floor. So the cove trim runs on all four walls of each restroom, net of the doors: 52.10 LF from the plan dimensions against 51.87.
- **WT-8 (F4).** Find the wall first. The elevation-A marker (10) is only in MEN'S 112, so RESTROOM ELEVATION - A is the Men's west wall, 7'-3 1/2" overall, and the door in it is JANITOR door 115 (next to the CR card reader). The restroom doors 113 and 112 are in the south walls, 6" from the side wall. The "similar" Women's wall is the east wall, with its own TA-4/TA-9 and no door. Base on the Men's wall runs either side of door 115: 3.67 ft on the left and a 0.22 ft jamb pier on the right (3.89). The Women's east wall takes the full width (7.29). WT-8 = 7.29 + 3.89 = 11.18 against 11.28. Do not double the net-of-door run for the Women's room.
- **Transitions (F4 to F6).**
  - For each `FTS-n` call-out, measure the boundary the arrow points to.
  - At doors use the clear opening between the frame members, read from the vector layer: 106 is 3.00 ft (x 1024.0 to 1078.0 pt; the 2" frame members sit outside that, and frame-outside to frame-outside is 3.33 ft), 110 is 3.17 ft and the 100 pair is 6.08 ft (the storefront wall openings). The 106 value equals the A-600 3'-0" leaf, and the cyan FTS3 run on p08 scales 2.92 ft there.
  - At open edges use the polygon side. For the LVT these are the west, south and east sides of 103; the north side is wall.
  - FTS-4 is the mat perimeter.
- **Schluter top trim (F7).** The band (5'-6") is on elevations B, C and D. The elevations carry no width dimension, so take the wall lengths from the A-410 plan dimensions: Men's B 7'-8 1/8", C 7'-8", D 7'-8" less the 3'-0" door; Women's B 7'-8 1/8", C 7'-6 3/8", D 7'-6 3/8" less the door. Sum both rooms: 39.75 LF. Scaling the elevations at 1/2" = 1'-0" (36 pt/ft: B 7.508, C 7.675, D 4.006 + 0.333) reads short (39.04), partly because the plan's 6" nib beside the door scales 0.333 ft.
- **Schluter cove trim (F4).** Every wall of both restrooms net of the doors 112, 113 and 115: the band walls above plus the two WT-8 side walls. 61.10 − 9.00 = 52.10 LF.

## 5. Cross-checks

1. **Areas add up per room.** In 102 and 105, CR-1 + CR-2 + CR-3 must equal the room area. If the field was not netted, the carpet comes out at room area plus the insets.
2. **Concrete plus mat.** CON-1 + MAT-1 drawn = 68.8 + 6.0 = 74.8 SF. The 106 room, including the half door strip (3.00 × 0.247), is 74.05 + 0.74 = 74.79 SF.
3. **LVT and its transition.** FTS-2 should be the LVT perimeter minus the wall side: 28.98 against 29.0.
4. **Mat and its transition.** FTS-4 equals the mat perimeter. A 10 SF mat line next to a 10 LF ramp line means one of them is wrong. If the mat really is 36"x48", both change: 12 SF and 14 LF.
5. **Grout against tile.** Each GR line should be at least the SF of the tiles it serves: 1050 ≥ 946.11 and 300 ≥ 244.13. An increase of more than one round-up step plus about 10% means a tile tag is in the wrong grout.
6. **Top trim against the band.** Plan dimensions B + C + D net of door, both rooms: 39.75 against 39.55 LF. Cove trim = top-trim walls + the two WT-8 side walls (12.35 by plan) = 52.10 against 51.87 LF.
7. **Base below perimeter.** WB-1 404.7 LF must be less than Σ room perimeters minus doors.
8. **One transition per material change at each door.** Every door in A-600 between two different floor tags should map to an FTS. Doors between the same tag (FT-1 to FT-1) get none.
   - 112 and 113 (restrooms) are FT-1 to FT-1, so no transition.
   - 106 is FT-1 to CON-1, so FTS-3.
   - 105 is FT-1 to CR-1, so FTS-1 (F002).
   - 114 and 111 are FT-1 to CR-2, so FTS-1.
   - The exterior doors 100 and 110 carry FTS-3 under F004.

## 6. Traps hit on this job

- **The finish schedule is an image.** A text-only reader misses the tile sizes, the grout assignment ("GR-1 GROUT" on the FT-1 row), the Schluter trims on the wall-tile rows and the MT-1 size.
- **Three mat sizes.** Schedule 36"x48" (12 SF), drawn 2'x3' (6 SF), estimate 10 SF. The FTS-4 line follows the drawn mat (10 LF).
- **The schedule and the detail disagree on the FTS-1 product.** A-170 says Schiene AE100. A-150 detail 1 says Reno-TK (ATK 100AT) over a 3'-0" floated slab. The estimator used the schedule.
- **The spec describes the wrong resilient product.** 09 6519 specifies 12x12 VCT (Armstrong Excelon), and the details call the LVT and the mat "VINYL COMPOSITION TILE". The plan and schedule carry LVT-1 25 cm x 1 m Interface plank. Plank SF per piece is metric: 2.691 SF.
- **Inset patterns.** The two diamond carpets put three tags in one room. Treating the room as one tag, or measuring the field without netting the insets, double-counts every inset SF.
- **Grout is carried as SF.** Both GR lines are areas, rounded up. A takeoff that produces grout in lb or kits will not line up with the estimate unless it also emits the SF line.
- **Grout scope.** Per the schedule, GR-1 includes the transaction bar (WT-3). The estimator's numbers fit only if WT-3 is left out at 10%, or put in at 3–6%. Keep the tile list per grout explicit.
- **Base type in the restrooms.** WB-1 appears in the restroom tag stacks, but the A-410 elevations show WT-8 tile bullnose and Schluter cove trim at the floor. The estimator carried both WB-1 (inside 404.7) and WT-8. Check that the restroom walls are not in both.
- **One elevation, two walls.** WT-8 is traced twice on elevation A, once across the drawn door and once net of it. That is not a run across a doorway: the drawn door is the Janitor door 115 in the Men's west wall, and the full-width run is the "similar" Women's east wall, which has no door. Reading "similar" as "identical, door included" gives 2 × 3.89 = 7.78 LF and loses 3.4 LF. Locate each elevation on the plan before applying a "similar" note.
- **FTS-3 is used at exterior doors.** The schedule defines it as tile to sealed concrete, but the estimator also used it at the two F004 exterior thresholds, one of which is CR-4 carpet. An AI following the schedule definition alone would carry 3.00 LF (door 106 only), not 12.2.
- **Same colour, different items.** CR4 and FTS3 are both cyan, and CON-1 and PT8 are both olive. Pixel-colour readers must key on the legend name.
- **Hidden trims.** The Schluter trim runs on p16 are drawn under the wall-tile fills on the elevations and can barely be seen; only the cove-trim runs on the plan side walls show. Take the legend value, and check it against the plan dimensions (top trim 39.75, cove trim 52.10) rather than re-tracing the elevations.
- **Attic stock.** All four flooring spec sections ask for 10% attic stock, and the estimator carries none. Report it separately; never fold it into waste.
