# Masonry (brick veneer, CMU, stone/cast stone) quantity takeoff: best practice

Scope: quantities and material types only.
Written 2026-10-13 for the single-storey bank branch in this repo (Fifth Third Bank - Watson, Warner Robins GA).

## Errata (added 2026-10-13 after review; `formulas.md` is the current record)

This file was written before the reconciliation. Where it disagrees with `formulas.md`, `reconciliation.csv` or `reading-guide.md`, those win. Known disagreements:

- **§9, rowlock sill:** "149.86 has no matching legend row" is wrong. The legend rows `7-5/8"THK. x 3-5/8"H ROWLOCK SILL` are 61.5 FT (p11) + 88.3 FT (p12) = 149.8 LF (formulas F4, −0.04%).
- **§9, CMU:** the back-solve to 157.1 LF (209.475 ÷ 16/12) is superseded. The estimate is `lfUp05(157.4) × 1.33 = 157.5 × 1.33 = 209.475` exactly (formulas F1, C1, C2).
- **§9, brick SF:** the legend sum 395.7 includes a ≈ 9.2 SF overshoot past the NE corner on p12 (reading-guide trap 12). The estimate's 400 is `sfUp5(395.7)` (formulas F2, C3).
- **§6, weeps:** 75 by ceil(L/2) is superseded by formulas F9, `ceil(L × 12 / 24) + 1` = 76 per run, which counts both ends.
- **"Cast stone" for 04 7200 (§2, §4.6, §8 item 11):** the section title is **Architectural Stone Veneer** (spec p78). Its body is a cast-stone section: "Comply with ASTM C 1364" (p79) and "Cast stone units shall be manufactured within 100 miles" (p80). Both names describe the same section. No line or legend on this job uses it.

## 0. Source status (read first)

- The web-search budget was exhausted after the first two queries of this run. Every web source below was therefore fetched directly from the publisher (Brick Industry Association technical notes, CMHA/NCMA TEK notes, CMHA installation guide, Wikipedia). I did not reach RSMeans, CRSI, USG/Sherwin-Williams-type coverage sheets, or flashing/weep manufacturer data sheets. Those are listed as gaps in section 11.
- BIA and CMHA publish the industry's reference quantities. They are strong for brick, CMU, mortar, grout, ties, flashing and weeps. They are thin on stone, cast stone and control-joint spacing for CMU.
- Facts about this project cite local files (drawings, spec text, reference lines). Facts about industry practice cite a link.
- Section 10 holds practitioner conventions from a GPT-6 Astra second opinion. They have no citable source and are marked as such. Treat them as hypotheses to confirm.
- All arithmetic was run in Python (`trades/03-masonry/scripts/research/masonry/calc.py`).

## 1. What an estimator takes off, and in which units

| Item | Unit | Notes / source |
|---|---|---|
| Brick veneer field | SF net of openings, then converted to EA brick (or M) | Wall-area method: net area x units per SF ([BIA TN 10](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf)) |
| Brick special courses (rowlock, soldier, header, sailor, water table, sills, caps) | LF by type, converted to EA | Orientations are defined in [BIA TN 10 Fig. 1](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf). Remove their area from the field SF. |
| Special shapes at corners, jambs, bullnose | EA | [BIA TN 10](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf) says to include partial brick to maintain bond at corners. The CMU equivalent is counted separately ([CMHA TEK 4-2A](https://www.cmha.org/resource/tek-04-02a/)). |
| CMU wall | SF net of openings, converted to EA by size | 8x16 face = 8/9 SF; 119 units per 100 SF including 5% waste ([TEK 4-2A](https://www.cmha.org/resource/tek-04-02a/)) |
| CMU special units (bond beam, lintel, corner, pilaster, KO/sash) | EA, separate from the field count | [TEK 4-2A](https://www.cmha.org/resource/tek-04-02a/): "pilasters, corner units, and bond beam units are counted separately and subtracted from the total" |
| Mortar | cubic ft, or bags/batches by mix | [TEK 4-2A](https://www.cmha.org/resource/tek-04-02a/) Table 2; [BIA TN 10](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf) Table 4 |
| Grout (vertical cells, bond beams, solid-filled walls) | cubic ft / CY, or 80-lb bags | [TEK 4-2A](https://www.cmha.org/resource/tek-04-02a/) Tables 3-5 |
| Reinforcing bars (vertical, bond beam, dowels) | LF and EA by bar size | Cover, bar sizes: [TEK 12-4D](https://www.cmha.org/resource/tek-12-04d/); laps: [TEK 12-6A](https://www.cmha.org/resource/tek-12-06a/) |
| Joint reinforcement (ladder/truss) | LF per reinforced course | [TEK 12-2B](https://www.cmha.org/resource/tek-12-02b/) |
| Veneer ties/anchors | EA | [BIA TN 44B](https://www.gobrick.com/media/file/44b-wall-ties-for-brick-masonry.pdf), [BIA TN 28B](https://www.gobrick.com/media/file/TN%2028B%20FINAL%20PUBLISHED%20VERSION%202025-04.pdf) |
| Through-wall flashing and drip edge | LF, with developed width | [BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf) |
| Weeps / vents | EA | Spacing in [BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf) |
| Cavity drainage / mortar-collection mesh | LF | [BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf) |
| Cavity insulation, WRB | SF | Normally Division 07, but it sits in the veneer assembly ([BIA TN 28B](https://www.gobrick.com/media/file/TN%2028B%20FINAL%20PUBLISHED%20VERSION%202025-04.pdf)) |
| Expansion joints (brick) and control joints (CMU): filler, backer rod, sealant | LF | [BIA TN 18A](https://www.gobrick.com/media/file/18a-tn18a.pdf) |
| Steel lintels, shelf angles | EA / LF | Furnished under Division 05; masonry sets them ([project spec 04 2113 s1.1.B](file://text/spec-p067.txt)) |
| Cast or precast stone (sills, caps, copings) | LF (EA when sized) | Spec 04 7200, cast stone |
| Adhered manufactured stone veneer, if any | SF field, LF corners, SF lath/WRB | [CMHA MSV Installation Guide](https://www.cmha.org/resource/msv-man-001-23/) |
| Cleaning, pointing, protection | SF | Spec 04 2113 s3.10 |

## 2. Sheets and spec sections that drive it

Generic drivers, then the ones on this job.

- Exterior elevations: veneer areas, material keys, rowlock and water table lines, control joint locations.
- Floor plans: wall lengths and openings. Building sections and wall sections: heights, bearing elevations, flashing, weep, shelf-angle and lintel details.
- Finish schedule and keynotes: unit type, color, mortar color, bond.
- Structural drawings: CMU reinforcement, bond beams, lintels.
- Door and window schedules: masonry opening sizes.
- Spec 04 2113 (brick), 04 2200 (CMU, if present), 04 7200 (stone/cast stone), related 05 5000 (lintels, shelf angles), 07 9200 (sealants), 07 6200 (flashing, if present).

On this job:

| Source | What it drives |
|---|---|
| A-200, A-201 (elevations) | Brick veneer "EXT-1" areas, half-rowlock lines. Legend pages 11 and 12 in `reference/markups/legends.csv`: 163.6 + 232.1 SF veneer, 61.4 + 87.9 LF half-rowlock. |
| A-200 detail "BRICK VENEER": "BRICK TIES @ 32" O.C. HORIZ. & 16" O.C. VERT.", air cavity, brick-compatible sealant and backer rod, 3/8" joint | Tie spacing and cavity per the drawings (`text/A-200.txt`) |
| A-110 plan | 4" CMU stem wall "grout cavity solid" at 1'-4" high. Legend: 157.4 FT. |
| A-190 (site/trash enclosure) | 8x8x16 nominal CMU, bond beam with 1 cont. #5, #5 vertical at 32" o.c. max, KO block grouted solid, precast stone cap on mortar bed, continuous through-wall flashing with drip, painted cementitious coating (`text/A-190.txt`) |
| Spec 04 2113 (pp. 67-77 of specifications.pdf) | Face brick ASTM C216, 3-5/8 x 2-1/4 x 7-5/8 (modular), Type N mortar, ASTM A951 joint reinforcement, adjustable slip-in veneer anchors for steel studs, flashing, weeps, cavity drainage mesh, compressible filler, bond-breaker, lintel bearing |
| Spec 04 7200 (pp. 78-82) | "Architectural stone veneer" is cast stone (ASTM C1364), Type N setting and pointing mortar. It is the source of the precast sills and caps. |
| Related: 05 5000 | Steel lintels and shelf angles (not masonry scope) |

Spec 04 2113 details that change quantities (local text, `text/spec-p067.txt` to `spec-p077.txt`):
- Anchors: "not more than 18 inches o.c. vertically and 24 inches o.c. horizontally, with not less than 1 anchor for each 2 sq. ft. of wall area". Additional anchors go "within 12 inches of openings and at intervals, not exceeding 8 inches, around perimeter".
- Flashing at lintels and shelf angles extends at least 6 in. into the masonry each end. At heads and sills it extends 6 in. and turns up at least 2 in. for end dams.
- Weeps in head joints, first course above flashing, 24 in. o.c.
- Weeps use mesh vents. Wicking material goes above flashing under brick sills.
- Cavity drainage: strips full cavity depth, 10 in. high (Mortar Net).
- Lintel bearing: minimum 8 in. each jamb.
- Horizontal pressure-relieving joint under shelf angles. Vertical joints not less than 3/8 in.
- Flashing system: Mortar Net TotalFlash, with termination bar, stainless drip edge and preformed corners.

## 3. Standard measurement rules

### 3.1 Wall-area method (brick and CMU)

- "The most widely used estimating procedure is the 'wall-area' method. It consists simply of multiplying the net wall area (gross areas less areas of openings) by known quantities of material required per square foot" ([BIA TN 10](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf)).
- Net the area first, then apply the per-area factors, then correction factors, then waste last. [BIA TN 10](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf) says to determine net quantities "including all correction factors" before adding waste.
- Deduct windows, doors and other openings from gross wall area ([TEK 4-2A](https://www.cmha.org/resource/tek-04-02a/)).
- Count pilasters, corner units and bond-beam units separately and remove them from the field count ([TEK 4-2A](https://www.cmha.org/resource/tek-04-02a/)).
- The BIA and CMHA notes give no threshold for ignoring small openings. Use one consistent rule and write it down (see section 10).

### 3.2 Openings, corners, jambs

- Masonry opening edges are defined by brick units, not mortar joints. Vertical dimensions are the number of courses plus one extra bed joint. The height is measured to the bottom of the brick above, not to the bottom of the lintel ([BIA TN 10](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf)).
- Masonry openings are typically 4 in. wider than the door or window and 8 in. taller than a window (2 in. each side for framing, 4 in. for sill). Use the masonry opening, not the nominal product size ([CMHA TEK 5-12](https://www.cmha.org/resource/tek-05-12/)).
- Corners and openings are laid out so cutting is limited, using the module relationships in [BIA TN 10](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf). Allow partial brick at corners to hold the bond.
- CMU module: 8 in. vertical and horizontal. Actual units are 3/8 in. under nominal ([TEK 5-12](https://www.cmha.org/resource/tek-05-12/); [Wikipedia CMU](https://en.wikipedia.org/wiki/Concrete_masonry_unit) gives 15-5/8 x 7-5/8 actual for 8x16 nominal).
- Non-modular layouts, many returns and many corners "can significantly increase unit and mortar/grout quantities" ([TEK 4-2A](https://www.cmha.org/resource/tek-04-02a/)).

### 3.3 Heights and where veneer starts and stops

- Base flashing and weeps sit no more than 10 in. above finished grade. Flashing is stepped with significant grade changes. The cavity below base flashing is filled solid with mortar or grout ([BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf), [BIA TN 28B](https://www.gobrick.com/media/file/TN%2028B%20FINAL%20PUBLISHED%20VERSION%202025-04.pdf)).
- Veneer over cold-formed steel: maximum 30 ft above its support to top of wall, 38 ft to top of gable, unless rationally designed ([BIA TN 28B](https://www.gobrick.com/media/file/TN%2028B%20FINAL%20PUBLISHED%20VERSION%202025-04.pdf)). Not a constraint on a single-storey building, but it tells you where shelf angles appear.
- Measure veneer from its support (ledge, shelf angle, or base flashing line) to the top of brickwork, including parapet brick. Coping height is not brick. (Convention, see section 10.)

### 3.4 Slopes, sills, special courses

- Brick sills slope at least 15 degrees from horizontal and project at least 1 in. from the wall face. Ends of sills may need uncored units ([BIA TN 36](https://www.gobrick.com/media/file/36-brick-masonry-details-sills-and-soffits.pdf)).
- Sill flashing extends to the first head joint beyond the jamb and turns up at least 1 in. at each end ([BIA TN 36](https://www.gobrick.com/media/file/36-brick-masonry-details-sills-and-soffits.pdf)). The project spec says 6 in. past the end and a 2 in. upturn. Take the spec's larger figure.
- Brick sills of 4 ft or less need no special anchorage. Longer sills are anchored ([BIA TN 36](https://www.gobrick.com/media/file/36-brick-masonry-details-sills-and-soffits.pdf)).
- Concrete or stone sills longer than 4 ft slope from the ends toward the centre ([BIA TN 36](https://www.gobrick.com/media/file/36-brick-masonry-details-sills-and-soffits.pdf)).
- Convert LF of a special course to EA from the exposed unit dimension plus joint along the run. Derived, not sourced: a rowlock stretcher runs 7-5/8 + 3/8 = 8 in. per brick (1.5 per LF); verify the orientation against [BIA TN 10 Fig. 1](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf).

### 3.5 Laps, overlaps, bearings (installed quantity, not waste)

| Item | Rule | Source |
|---|---|---|
| Flexible flashing laps | at least 6 in., sealed; self-adhered laps typically 3-4 in. | [BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf) |
| Flashing corners | overlap at least 6 in. each way, or use prefabricated corners | [BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf) |
| Flashing up the backing | at least 8 in. above the horizontal leg | [BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf), [TN 28B](https://www.gobrick.com/media/file/TN%2028B%20FINAL%20PUBLISHED%20VERSION%202025-04.pdf) |
| End dams (discontinuous flashing) | turn up at least 1 in. into the head joint | [BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf) |
| Head flashing at openings | extend beyond the jamb lines, then form dams | [BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf) |
| CMU flashing laps | 4 in. minimum | [CMHA TEK 19-4A](https://www.cmha.org/resource/tek-19-04a/) |
| Joint reinforcement splices | at least 6 in. | [TEK 12-2B](https://www.cmha.org/resource/tek-12-02b/) |
| Joint reinforcement at intersections / openings (seismic) | 30 in. each way at intersecting walls; 24 in. past openings | [TEK 12-2B](https://www.cmha.org/resource/tek-12-02b/) |
| Rebar lap (ASD) | not less than 12 in. or 40 bar diameters, whichever is greater | [TEK 12-6A](https://www.cmha.org/resource/tek-12-06a/) |
| Rebar lap with epoxy coating / high stress | plus 50% | [TEK 12-6A](https://www.cmha.org/resource/tek-12-06a/) |
| Loose steel lintel bearing | 4 in. minimum each side (BIA recommendation); this project's spec says 8 in. | [BIA TN 28B](https://www.gobrick.com/media/file/TN%2028B%20FINAL%20PUBLISHED%20VERSION%202025-04.pdf); spec 04 2113 s3.8 |
| Lath laps (adhered stone) | 1 in. at vertical seams, 1/2 in. at horizontal; wrap corners 12 in. | [CMHA MSV guide](https://www.cmha.org/resource/msv-man-001-23/) (the PDF behind that page, 6th ed.) |
| WRB laps (adhered stone) | 2 in. horizontal, 6 in. vertical, 16 in. past corners | [CMHA MSV guide](https://www.cmha.org/resource/msv-man-001-23/) |

## 4. Coverage, yield and waste factors

### 4.1 Brick (from [BIA TN 10 Table 4](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf))

Net quantities with 3/8 in. joint (1/2 in. joint figure in brackets), no waste. Mortar for solid, fully bedded brick.

| Brick (W x H x L nominal, in.) | Brick per 100 SF | Mortar cf per 100 SF | Mortar cf per 1000 brick |
|---|---|---|---|
| Modular 4 x 2-2/3 x 8 | 675 | 5.5 (6.9) | 8.1 (10.3) |
| Engineer modular 4 x 3-1/5 x 8 | 563 | 4.8 (6.1) | 8.5 (10.8) |
| Closure modular 4 x 4 x 8 | 450 | 4.1 (5.2) | 9.1 (11.6) |
| Norman 4 x 2-2/3 x 12 | 450 | 5.1 (6.5) | 11.2 (14.3) |
| Utility 4 x 4 x 12 | 300 | 3.7 (4.7) | 12.3 (15.7) |
| Standard (non-modular, specified 3-5/8 x 2-1/4 x 8, 3/8 joint) | 655 | 9.5 (11.0) | 14.5 (17.8) |

- Hollow brick in a full-bed veneer: use the solid-brick table values. For face-shell bedding, reduce mortar by the void percentage, typically 25-35% ([BIA TN 10](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf)).
- Bond pattern correction (net increase for headers) from [BIA TN 10 Table 6](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf): common bond with full headers every 5th course = +1/5 brick, +1/15 mortar; every 6th = +1/6, +1/18; every 7th = +1/7, +1/21; English = +1/2, +1/6; Flemish = +1/3, +1/9. Running and stack bond need no correction.
- Waste: "at least 5 percent is added to the net brick quantities" and "add 15 to 25 percent to the net mortar quantities" ([BIA TN 10](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf)).
- Rule of thumb: eight bags of masonry cement lay 1000 modular brick, a very rough figure that includes unspecified waste ([BIA TN 10](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf)). One cubic foot of loose damp sand yields about one cubic foot of mortar (same source).
- Collar joint mortar in multi-wythe walls per 100 SF: 2.08 cf (1/4 in.), 3.13 (3/8), 4.17 (1/2), 6.25 (3/4) ([BIA TN 10 Table 5](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf)). Not needed for a drained veneer cavity.

### 4.2 CMU ([CMHA TEK 4-2A](https://www.cmha.org/resource/tek-04-02a/))

- 8x16 face = 8/9 SF per unit, so 112.5 units per 100 SF net (derived). The source gives 119 per 100 SF including about 5% waste. The count does not depend on unit width.
- Mortar, per batch, with face-shell bedding for conventional CMU:
  - Masonry cement, 8 x 70-lb bags + 1 ton sand: 240 conventional units (1,000 brick-sized units).
  - Preblended 80-lb bag: 16 conventional units (50 brick-sized). 3,000-lb bulk bag: 420 (1,550).
  - Site-mixed portland-lime Type S (1 cf cement, 1/2 cf lime, 4-1/2 cf sand): 46 units. Type N (1 : 1 : 6): 62.
  - These values "include nominal amounts for waste". 1 ton damp loose sand = 25 cf.
- Grout, cf per 100 SF of wall, two-core hollow units, 3% waste ([TEK 4-2A Table 3](https://www.cmha.org/resource/tek-04-02a/); I read the table from the published image):

| Grout spacing | 6 in. | 8 in. | 10 in. | 12 in. |
|---|---|---|---|---|
| 8 in. o.c. (solid) | 25.6 | 36.1 | 47.0 | 58.9 |
| 16 in. o.c. | 12.8 | 18.1 | 23.5 | 29.5 |
| 24 in. o.c. | 8.6 | 12.1 | 15.7 | 19.7 |
| 32 in. o.c. | 6.4 | 9.1 | 11.8 | 14.8 |
| 40 in. o.c. | 5.2 | 7.3 | 9.4 | 11.8 |
| 48 in. o.c. | 4.3 | 6.1 | 7.9 | 9.9 |

- Bagged preblended grout, vertical cells: 80-lb bag fills 3.6 cores (6 in.), 2.7 (8 in.), 2.2 (10 in.), 1.8 (12 in.); one 80-lb bag yields about 0.66 cf. Bond beam: 80-lb bag fills 2.7 LF (6 in.), 2.0 LF (8 in.), 1.6 LF (12 in.) ([TEK 4-2A Tables 4-5](https://www.cmha.org/resource/tek-04-02a/)).
- Horizontal bond-beam grout is "additional" to the vertical-cell volumes in Table 3. Small projects tend to have higher grout waste. Lower-density units absorb more water, so more grout ([TEK 4-2A](https://www.cmha.org/resource/tek-04-02a/)).
- Grouting 4 in. conventional units is not recommended (small cells) ([TEK 4-2A](https://www.cmha.org/resource/tek-04-02a/)).
- Grout pour limits: low-lift to 5 ft; high-lift up to 24 ft with cleanouts, placed in 5 ft lifts; cleanouts at least 3 in. wide, at the bottom of every cell with vertical bars, at most 32 in. o.c. in solid-grouted walls ([TEK 3-2A](https://www.cmha.org/resource/tek-03-02a/)). Cleanout units are extra units to count.
- Rebar cover: 1-1/2 in. (No. 5 and smaller) or 2 in. (larger than No. 5) if exposed to weather or earth ([TEK 12-4D](https://www.cmha.org/resource/tek-12-04d/)).
- Joint reinforcement: typically 16 in. o.c. vertically; 8 in. o.c. at intersecting walls (per the TEK); wire W1.7 (9 ga) common ([TEK 12-2B](https://www.cmha.org/resource/tek-12-02b/)).

### 4.3 Ties and anchors

| Wall type | Max area per tie | Max vertical | Max horizontal | Source |
|---|---|---|---|---|
| Brick veneer / steel stud, adjustable ties (older BIA table, 2002 MSJC) | 2.67 SF (2.0 SF recommended) | 18 in. | 32 in. (24 in. recommended) | [BIA TN 44B Table 1](https://www.gobrick.com/media/file/44b-wall-ties-for-brick-masonry.pdf) (table is an image; I read it) |
| Brick veneer / wood stud, non-corrugated | 2.67 SF (W1.7) to 3.50 SF | 18 in. | 32 in. | same |
| Brick veneer / CMU or concrete | 2.67 to 3.50 SF | 18 in. | 32 in. | same |
| Cavity wall, unit ties | 2.67 to 4.50 SF | 24 in. | 36 in. | same |
| Brick veneer / cold-formed steel (2016 TMS 402/602 basis, 2025 note) | 1 tie per 2.67 SF (W1.7, cavity up to 4-5/8 in.) | 25 in. | 32 in. | [BIA TN 28B](https://www.gobrick.com/media/file/TN%2028B%20FINAL%20PUBLISHED%20VERSION%202025-04.pdf) |
| Brick veneer / CMU (2022 basis) | 1 tie per 2.67 SF | spacing 32 in. horizontal | | [BIA TN 28D](https://www.gobrick.com/media/file/28d-tn28d.pdf) |

- Extra ties: around openings with any dimension larger than 16 in., add ties at maximum 3 ft o.c. within 12 in. of the opening ([BIA TN 28B](https://www.gobrick.com/media/file/TN%2028B%20FINAL%20PUBLISHED%20VERSION%202025-04.pdf); [TN 28D](https://www.gobrick.com/media/file/28d-tn28d.pdf)). The older TN 44B recommends extra ties within 8 in. of openings and discontinuities such as shelf angles and vertical expansion joints.
- Corrugated ties are not permitted with cold-formed steel backing ([BIA TN 28B](https://www.gobrick.com/media/file/TN%2028B%20FINAL%20PUBLISHED%20VERSION%202025-04.pdf)).
- Which number to use on a real job: the project spec and the drawing details govern, then the code. Here they disagree (section 9).

### 4.4 Flashing, weeps, cavity

- Weeps: open head joints preferred, recommended at 24 in. o.c. maximum. Codes typically permit up to 33 in. o.c. and no smaller than 3/16 in. diameter. Wick weeps recommended at most 16 in. o.c. Weep tubes not recommended. Open head weeps at least 2 in. high ([BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf)).
- Air space: 1 in. minimum required, 2 in. recommended ([BIA TN 28B](https://www.gobrick.com/media/file/TN%2028B%20FINAL%20PUBLISHED%20VERSION%202025-04.pdf), [TN 28D](https://www.gobrick.com/media/file/28d-tn28d.pdf)).
- Flashing locations: wall base, window sills, heads of openings, shelf angles, tops of walls and roofs, parapets, above projections, grade changes, transitions to other cladding ([BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf)). Under brick sills and over every lintel, turned up at the ends ([TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf)).
- Flashing waste is not stated by BIA. Count the developed width and the laps explicitly (section 3.5), then add a small cutting allowance (section 10).

### 4.5 Movement joints

- Vertical expansion joints in brick veneer: no more than 25 ft o.c. without openings, no more than 20 ft o.c. with multiple openings. Place them at or near corners, offsets, wall intersections, changes in wall height, changes in backing, and where support changes. Extend to the top of the brickwork including parapets ([BIA TN 18A](https://www.gobrick.com/media/file/18a-tn18a.pdf)).
- Corner rule: preferably within 2 ft of the corner; the two distances from a corner to its first joint sum to no more than the straight-wall spacing ([BIA TN 18A](https://www.gobrick.com/media/file/18a-tn18a.pdf)).
- Horizontal expansion joint immediately below each shelf angle, at least 1/4 in. ([BIA TN 18A](https://www.gobrick.com/media/file/18a-tn18a.pdf)).
- Parapets: when vertical joint spacing exceeds 15 ft, widen joints or add joints halfway ([BIA TN 18A](https://www.gobrick.com/media/file/18a-tn18a.pdf)).
- CMU control-joint spacing was not found in the sources I reached. Take it from the drawings, and see the gap in section 11.

### 4.6 Adhered manufactured stone veneer (if a job has it)

From the [CMHA MSV Installation Guide](https://www.cmha.org/resource/msv-man-001-23/) (6th ed. PDF). Not on this job (04 7200 here is cast stone), but included because the trade scope covers stone veneer.
- Unit limits: average thickness at most 2-5/8 in., face dimension at most 36 in., face area at most 5 SF, weight at most 15 psf.
- Lath: self-furring metal lath at 2.5 lb/sq yd or heavier (ASTM C847), welded wire lath (C933) or 18 ga woven wire (C1032). Fastened every 7 in. vertically on each stud, studs at 16 in. o.c. maximum.
- Weep screed: minimum 3.5 in. vertical flange, 26 ga metal.
- Where a WRB is required, two layers. Cement board may replace lath and scratch coat.
- Take off: SF field stone, LF corner units, SF lath + WRB (with laps), LF weep screed and casing bead, LF flashing, SF scratch coat and setting bed mortar. The guide gives no coverage-per-box figure. Use the manufacturer's data sheet for coverage and mortar yield.

## 5. Material breakdown an estimator lists

Brick veneer wall (steel-stud backup, as on this job):

1. Face brick: EA = net SF x units per SF x (1 + waste). Separate lines for each size and color.
2. Special-shape brick: rowlock, soldier, sill, water table, bullnose, return and corner units, by LF converted to EA (field SF reduced accordingly).
3. Mortar: cf or bags by type (here Type N, colored, preblended) from the table in 4.1 plus waste. Separate setting and pointing mortar where stone is set.
4. Veneer ties/anchors: EA, plus perimeter additions at openings. Screws or fasteners: 2 per anchor unless the design uses 1 (spec 3.6.A.1).
5. Joint reinforcement: LF, if specified (not usually required for running-bond veneer, [BIA TN 28B](https://www.gobrick.com/media/file/TN%2028B%20FINAL%20PUBLISHED%20VERSION%202025-04.pdf)).
6. Through-wall flashing: LF x developed width, plus laps, end dams, prefabricated corners, drip edge, termination bar.
7. Weeps/vents: EA per flashing run at the specified spacing.
8. Cavity drainage mesh: LF at the wall base and above lintels (spec: 10 in. high strips).
9. Rigid cavity insulation and WRB: SF (usually Division 07).
10. Expansion joint filler, backer rod, sealant: LF.
11. Compressible filler under shelf angles; bond-breaker strips (spec 2.7).
12. Steel lintels and shelf angles: EA / LF (Division 05, but masonry sets and flashes over them). Length = clear opening + 2 x bearing.
13. Cleaning products, pointing, protection sheeting (spec 1.5, 3.10).

CMU wall:

1. Units by size and special type (standard, half, bond beam, lintel, corner, KO/sash, cap), EA.
2. Mortar (batches, bags or cf).
3. Grout (cf or bags) for vertical cells, bond beams, solid-filled sections, and cleanout sections.
4. Vertical bars, bond-beam bars, dowels (LF by size, with laps and hooks; the drawing note "90 degree std ACI hook").
5. Joint reinforcement where specified.
6. Flashing, weeps and vents, cap or coping (precast cap on mortar bed with dowels), sealant.
7. Control-joint filler and sealant.
8. Surface treatment (here a painted cementitious coating; Division 09 or 04).

Cast stone: sills, caps, copings by LF or EA (per shop-drawing piece count), anchors/dowels, setting mortar, sealant, cleaner.

## 6. Worked example on this job (computed)

Source quantities from `reference/estimate/lines.json` (quantities only) and `reference/markups/legends.csv`. Calculations in `trades/03-masonry/scripts/research/masonry/calc.py`.

Brick veneer, 400 SF (estimate line 32; legends sum to 395.7 SF, ratio 1.011):
- Modular brick (3-5/8 x 2-1/4 x 7-5/8, [BIA TN 10 Table 1/4](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf)): 675/100 SF x 4.00 = 2,700 net. With 5% waste: 2,835.
- Mortar at 5.5 cf/100 SF = 22.0 cf net. With 15% to 25% waste: 25.3 to 27.5 cf.
- Ties by the drawing detail (32 in. horizontal x 16 in. vertical = 3.56 SF each): 112.5 ties before perimeter additions. By the spec (18 in. x 24 in. = 3.0 SF): 133.3. By the spec's "1 per 2 SF": 200. By BIA's 2.67 SF maximum area: 149.8. The first two ignore opening-edge additions, which can only add ties.
- Half-rowlock: 61.4 + 87.9 = 149.3 LF (legend), 149.33 in the estimate. Rowlock sill: 149.86 LF in the estimate (0.53 LF over). Weeps over 149.33 LF of one continuous flashing run at 24 in. o.c.: 75 (ceil(L/2)). The real count needs the flashing runs: base, each head and sill, with ends.

8 in. CMU trash enclosure wall, 289.76 SF (estimate lines 668-670):
- Units: 289.76 / (8/9) = 326 net. With 5% waste: 342. The TEK 4-2A figure of 119/100 SF gives 345.
- Grout by TEK Table 3 at 32 in. o.c. (matching "#5 vertical at 32 in. o.c."): 9.1 cf/100 SF x 2.8976 = 26.4 cf = 0.98 CY. Bond beam and KO-block solid grout come on top.
- Mortar by the sand rule (1 ton = 25 cf per 240 units): 342 / 240 x 25 = 35.7 cf = 1.32 CY.

## 7. Common mistakes and how to check

| Mistake | Check |
|---|---|
| Using gross wall area, or deducting nominal rather than masonry opening sizes | Net area = gross minus masonry openings (opening = product + 4 in. wide, + 8 in. high for windows, [TEK 5-12](https://www.cmha.org/resource/tek-05-12/)) |
| Mixing the brick count tables: modular vs standard vs Norman | Recompute units per SF from nominal face: 100 / (L x H / 144). Modular 8 x 2-2/3 gives 675 ([BIA TN 10](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf)) |
| Waste applied before bond/special-course corrections, or applied twice | BIA: net first, then corrections, then waste ([BIA TN 10](https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf)). Never apply waste to laps, bearings or required overlaps. |
| Counting special courses (rowlock, soldier, sills) and also leaving their area in the field | Subtract their face area from the field SF |
| Counting pilasters, bond beams, lintel and corner units in the field count | Count separately and subtract ([TEK 4-2A](https://www.cmha.org/resource/tek-04-02a/)) |
| Ignoring extra ties near openings | Add ties within 12 in. of openings larger than 16 in., max 3 ft o.c. ([BIA TN 28B](https://www.gobrick.com/media/file/TN%2028B%20FINAL%20PUBLISHED%20VERSION%202025-04.pdf)) |
| Flashing LF taken as wall length only | Include sills, heads, shelf angles, corners, 6 in. laps, upturns and end dams ([BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf)) |
| Weeps counted as total length / 24 in. once | Count per flashing run, with ends. Weeps go immediately above every flashing, including over lintels ([BIA TN 7](https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf)) |
| Mortar/grout taken from brick table for CMU, or the reverse | Brick table (e.g. 5.5 cf/100 SF) is for solid brick; CMU face-shell bedding uses TEK 4-2A |
| Grout taken as full-height solid when only cells with bars are filled | Grout volume depends on cell spacing; use Table 3 for the drawn bar spacing, add bond beams and solid sections |
| Missing movement joints (and their sealant) | Check the drawings first, then 25 ft / 20 ft rule and corners ([BIA TN 18A](https://www.gobrick.com/media/file/18a-tn18a.pdf)) |
| Missing steel lintels or shelf angles because they live in Division 05 | Cross-check the opening schedule and spec 04 2113 s1.1.B |
| Conflicting tie or flashing requirements between spec, detail and BIA | Use the most stringent that is stated in the contract documents and flag the conflict |

Reasonableness checks (derived): brick per SF of veneer should land near 6.75 (modular); CMU near 1.125 per SF net; mortar for modular veneer near 22 cf per 400 SF; tie density near 0.3 to 0.5 per SF.

## 8. What an AI takeoff must read from the drawings and specs

1. Unit identity: brick size and type from the spec (ASTM C216, size 3-5/8 x 2-1/4 x 7-5/8, grade/type), color, bond pattern, joint thickness (3/8 in. on the detail). The size decides the units-per-SF table row. CMU nominal size and weight class, grouted or not, special units from the structural notes.
2. Wall geometry per elevation: lengths, heights from support to top of brick, parapet brick, openings with masonry opening sizes, corners (inside/outside, count), jambs and returns.
3. Assembly: backup (steel stud here), cavity width, insulation, WRB, tie/anchor type and the spacing in the spec and detail.
4. Special courses: rowlock, soldier, water table, sill, cap, coping, with section dimensions from details.
5. Flashing and weeps: every location, developed width, laps, end dams, termination, drip, weep spacing and product. Base flashing elevation vs grade.
6. Movement joints: vertical (CJ marks on the elevation), horizontal at shelf angles, sealant and filler.
7. Lintels, shelf angles, loose steel with bearing lengths (spec 8 in. here).
8. CMU: bar size and spacing, bond beam locations and bars, KO/solid grouted units, dowels and hooks, cap, wall height by section.
9. Spec details that change quantities: mortar type and color, 24 in. weep spacing, anchor additions at openings, flashing extensions, cavity drainage mesh height, compressible filler.
10. Conflicts: where spec text, detail callouts and schedules disagree (section 9), flag instead of choosing silently.
11. Scope boundaries: lintels and shelf angles (Division 05), sealant (07 9200), cast stone (04 7200 here), vapor barrier or fluid-applied WRB (the reference estimate shows a "fluid applied vapor barrier" at 400 SF under the veneer section).

## 9. Observations from this job's reference data (cross-checks, not instructions)

- Brick SF: estimate 400 vs legends 395.7. Half-rowlock LF 149.33 matches legends (149.3). Rowlock sill LF 149.86 has no matching legend row. Treat as an open question for the AI to resolve from the elevations.
- 4 in. CMU stem wall: estimate 209.475 SF vs legend 157.4 FT x 1'-4" = 209.87 SF. The estimate corresponds to a length of 157.1 LF. Small gap, same geometry.
- Tie spacing conflict: drawing detail 32 in. horizontal x 16 in. vertical; spec 04 2113 s3.6 says 18 in. x 24 in. maximum and one per 2 SF; BIA says 2.67 SF maximum. The three give 112, 133, 200 and 150 ties per 400 SF. An AI must report the governing source rather than one number.
- Reference CMU mortar and grout (A-190 wall, 289.76 SF): grout 3.245 CY = 87.6 cf = 30.2 cf/100 SF; mortar 1.798 CY = 48.5 cf = 16.75 cf/100 SF. TEK Table 3 at 32 in. o.c. is 9.1 cf/100 SF, so the estimator's grout is 3.3x that, closer to the 8 in. o.c. (solid) column at 36.1 cf. The mortar is about 1.4x the sand-rule figure. The estimator evidently grouts more cells (or the bond beam and KO courses) or uses a different convention. The data here cannot settle which. A faithful AI takeoff must read the notes on A-190 and state its grout assumption, and the comparison should be made against the estimator's quantity, not against TEK alone.
- The reference estimate lists mortar and grout in CY, the TEK tables work in cf per 100 SF. Convert (27 cf per CY) before comparing.

## 10. Practitioner conventions with no citable source (GPT-6 Astra second opinion, unverified)

Obtained with `ask_gpt.py`. They match common practice but I could not tie them to a document. Use them as defaults only when the contract documents are silent, and label them as conventions.

- No universal small-opening threshold. A stated one (for example ignoring penetrations of 1 SF or less) is acceptable if applied consistently.
- Deduct only from the material the opening actually interrupts. A door opening does not remove the stem wall below the slab.
- Do not count both faces of a single-wythe wall. Measure each wythe once.
- Brick veneer height runs from its support (ledge, angle, base flashing line) to the top of actual brickwork, parapet included. Coping is excluded.
- Corners: special units counted EA by course. Soldier, rowlock and header courses measured in LF by configuration, converted to EA from the exposed unit dimension plus joint, with the field SF reduced.
- Flashing: LF by developed width. Weeps: laid out per flashing run. Movement joints: LF of actual path, with brick expansion and CMU control joints kept separate. Lintel length = clear span + detailed bearings. Rebar: counted from a cutting schedule.
- Ordering waste, as typically used: brick 3-5% (5-10% cut-heavy); CMU 2-5% (5-10% cut-heavy); flashing and joint reinforcement 5-10% after explicit laps; ties, weeps and small accessories 2-5%; rebar 2-5%. BIA's own figure for brick (at least 5%) and mortar (15-25%) is the cited one; the others are unverified.
- The GPT list also claimed a common mistake of measuring masonry to the bottom rather than the top of the footing. I dropped it because it is unclear and not supported.

## 11. Gaps and what to do next

- No RSMeans, CRSI, or manufacturer coverage data (Mortar Net, Hohmann & Barnard, flashing makers) was reachable once search quota ran out. Their published coverage per roll, per box and per bag would sharpen sections 4.3 and 4.4.
- CMU control-joint spacing and CMU opening-deduction conventions beyond TEK 4-2A are not covered. NCMA's TEK 10 series did not appear in the CMHA site listing I fetched.
- Cast stone (sills, caps) takeoff conventions, such as piece length limits and anchor counts, are not sourced. Use the shop drawings.
- A follow-up search pass is the easiest way to close these. If the quota is raised, query: "cast stone sill takeoff linear feet", "CMU control joint spacing NCMA TEK 10-2", "Mortar Net TotalFlash coverage", "Hohmann Barnard adjustable veneer anchor spacing".
- Tables read from images ([BIA TN 44B Table 1](https://www.gobrick.com/media/file/44b-wall-ties-for-brick-masonry.pdf), TEK 4-2A Tables [2](https://www.cmha.org/wp-content/uploads/2018/08/TEK-04-02A-Table-2.png), [3](https://www.cmha.org/wp-content/uploads/2018/08/TEK-04-02A-Table-3.png), [4](https://www.cmha.org/wp-content/uploads/2018/08/TEK-04-02A-Table-4.png), [5](https://www.cmha.org/wp-content/uploads/2018/08/TEK-04-02A-Table-5.png)) were read visually. Re-check transcriptions before hard-coding.

## Source index

- BIA TN 10, Dimensioning and Estimating Brick Masonry (Feb 2009): https://www.gobrick.com/media/file/10-dimensioning-and-estimating-brick-masonry.pdf
- BIA TN 7, Water Penetration Resistance, Design: https://www.gobrick.com/media/file/7-water-penetration-resistance-design.pdf
- BIA TN 18A, Accommodating Expansion of Brickwork (2019): https://www.gobrick.com/media/file/18a-tn18a.pdf
- BIA TN 28B, Brick Veneer/Cold-Formed Steel Framed Walls (Apr 2025): https://www.gobrick.com/media/file/TN%2028B%20FINAL%20PUBLISHED%20VERSION%202025-04.pdf
- BIA TN 28D, Brick Veneer/Concrete Masonry Walls: https://www.gobrick.com/media/file/28d-tn28d.pdf
- BIA TN 36, Brick Masonry Details, Sills and Soffits: https://www.gobrick.com/media/file/36-brick-masonry-details-sills-and-soffits.pdf
- BIA TN 44B, Wall Ties for Brick Masonry: https://www.gobrick.com/media/file/44b-wall-ties-for-brick-masonry.pdf
- BIA technical notes index: https://www.gobrick.com/read-research/technical-notes
- CMHA TEK 4-2A, Estimating Concrete Masonry Materials: https://www.cmha.org/resource/tek-04-02a/
- CMHA TEK 3-2A, Grouting Concrete Masonry Walls: https://www.cmha.org/resource/tek-03-02a/
- CMHA TEK 5-12, Modular Layout of Concrete Masonry: https://www.cmha.org/resource/tek-05-12/
- CMHA TEK 12-2B, Joint Reinforcement for Concrete Masonry: https://www.cmha.org/resource/tek-12-02b/
- CMHA TEK 12-4D, Steel Reinforcement for Concrete Masonry: https://www.cmha.org/resource/tek-12-04d/
- CMHA TEK 12-6A, Splices, Development and Standard Hooks: https://www.cmha.org/resource/tek-12-06a/
- CMHA TEK 19-4A, Flashing Strategies for Concrete Masonry Walls: https://www.cmha.org/resource/tek-19-04a/
- CMHA Manufactured Stone Veneer Installation Guide: https://www.cmha.org/resource/msv-man-001-23/
- Wikipedia, Concrete masonry unit: https://en.wikipedia.org/wiki/Concrete_masonry_unit
- Project files: `reference/estimate/lines.json`, `reference/markups/legends.csv`, `text/A-200.txt`, `A-190.txt`, `spec-p067.txt` to `spec-p082.txt`
