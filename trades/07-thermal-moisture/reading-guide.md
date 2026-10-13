# Reading guide: 07 thermal and moisture protection

How to read each input that the formulas need, using the actual strings on this job.

## 1. Order of reading

1. **A-140 roof plan.** Read the roof types first (RT1 and RT2 sections in the right column), then the key notes R1–R16, then the plan.
2. **A-450 and A-430 details.** For every callout bubble on the roof plan, read what the detail
   wraps: membrane, insulation, cover board, coping, barrier.
3. **A-620 partition schedule.** Use Tables A, B and D and the general notes to decide which wall tags get batt and sealant.
4. **A-120 plan.** Read the wall tags and heights.
5. **A-200 / A-201 elevations.** Read the exterior finish schedule (ACM-1/2/3, EIFS-1/2, EXT-1, M-1).
6. **A-610 window elevations** and the **A-600 door schedule** for opening sizes.
7. **G-003 COMcheck** (envelope R-values, climate zone) and **S-201** (slab, stem walls).
8. Spec sections 07 2100 / 2413 / 2726 / 4213 / 5423 / 6200 / 7200 / 9200 (pages in `README.md`).

## 2. Partition tags → which walls get batt and acoustic sealant

A tag reads **series + stud depth + height letter**: `A3B` = series A (GWB both sides), 3-5/8" studs, height B.
These come from A-620 Tables A, B and D, and the partition legend reads them in that order
(`1 A2A`, with the fire rating first when there is one).

| Table D letter | Meaning | Batt? |
|---|---|---|
| A | slab to structure above | no |
| **B** | slab to structure above **w/ batt** | yes |
| C | slab to 6" above the scheduled ceiling | no |
| **D** | slab to 6" above the ceiling **w/ batt** | yes |
| E | slab to the scheduled ceiling | no |
| **F** | slab to the ceiling **w/ batt** | yes |
| G | partial height, see details | per detail |

On this job only **A3B** (34.2 LF) and **A6B** (28.4 LF) carry sound blankets. A3A, A6A, D3A and D3C do not,
even though general note D ("offices and toilet rooms … insulated with sound attenuation batts")
could be read more widely. The estimator followed the tag letter. Batt thickness follows the
stud depth: 3-5/8" → 3-1/2", 6" → 5-1/2".

Exterior walls (general note B: "partitions having an ext. face shall be insulated") get batt equal to the
stud depth over the full framing height. A-310 and A-311 call out "8" MTL. STUD & BATT INSULATION" and
"6" MTL. STUD & BATT INSULATION".

**Acoustic sealant.** Count the beads drawn in each A-620 detail.

- The two-sided base details (A-B01, B-B01, C-B01) draw "CONTINUOUS ACOUSTICAL SEALANT" at both runner flanges.
- The one-sided D-B01 draws a single bead, on the gypsum-board side only.
- At the head, A-T01 (and B-T01, C-T01) draw two beads at structure. D-T01 draws one "CONTINUOUS SEALANT" bead.
  A-T02, A-T03 and D-T02 (boards stopping above or at the ceiling) draw none.
- There is no head detail for the 3'9" and 4'4" low walls, and no sealant detail for the exterior walls.

Note K says non-rated partitions use acoustical sealant. Counting head + base per finished face gives 4 × A-series + 2 × (D-series,
low walls, exterior GWB walls) = 1055.0 LF against the estimator's 1053.5. A second fit, 4 × all interior + 1 × exterior = 1053.0,
contradicts D-B01. Neither is confirmed (`formulas.md` F16).

## 3. Roof plan legend rows (markup p7) and what they cover

| Legend row (exact) | Colour | Covers | Feeds |
|---|---|---|---|
| `RT1 ROOFING` 1864.3 SQ FT | yellow | the main roof field | 159, 163, 165, 162 |
| `RT2 ROOFING` 285.4 SQ FT | very light cyan | the canopy roofs at the building edges | 158, 165, 162 |
| `TAPERED POLYISOCYANURATE INSULATION ROOF CRICKET` 262.1 | magenta (shows orange over RT1) | crickets along the north drains (key note R10) | 164 |
| `TPO WALKWAY PAD MEMBRANE` 286.8 | periwinkle hatch | the R11 path between the RTUs and the hatch | 167 |
| `PARAPET LAP @ 2'1"H / @ 1'H / @ 3'6"H - 4,6/A450` | teal / red / green | membrane flashing up the roof-side face of the parapets (4/A450 base tie-in, 6/A450 to the coping) | 162 |
| `PARAPET WALL @ 2'7"H / 1'7"H / 4'7"H` | olive / indigo / orchid | parapet framing heights (studs, sheathing; 09a trade) | 156 (8" batt) |
| `8/A450 LAP ROOF 2', INCL WALL` 45.3 FT | olive | the **high-low wall** between roof planes (3-5/8" studs, batt, 2" rigid, 1/4" cover board, membrane up and over) | 154, 157, 163, 162 |
| `COPING 6/A450` 148.1, `COPING 9/A450` 38.5, `COPING 3/A430` 13.9 | red / teal / green | three coping profiles | 169, 170, 168 |
| `CURB - 1/A450` 39.9 FT | indigo | RTU curb perimeters (equipment curb detail) | 171, 166, 177 |
| `30"x36" ROOF ACCESS HATCH - 3/A450` 1 EA | cyan dot | hatch | 172 (curb 11 LF) |
| `FLASHING @ ROOF DRAIN` 11 EA / `@ VENT PIPE` 3 EA | brown / green dots | penetration flashings | 173, 174 |
| `CANOPY EDGE 7/A430` 138.5 FT | periwinkle line | the free edge of the RT2 canopies | 183, 162 |
| `9/A430` 119.4 FT | magenta line | the building side of the canopies: storefront head @ canopy | 175, 176 |

The roof-type sections carry these strings: RT1 "1/4" COVER BOARD / POLYISO BOARD w/ STAGGERED JOINTS. Rvalue =34.2 (R-5.7/INCH)
/ MECHANICALLY FASTENED FIRST LAYER … FULLY ADHERED ADDITIONAL LAYERS / (6" MIN INSULATION THICKNESS) R-VALUE = 34".
RT2 "POLYISO BOARD … TAPERED TO DRAIN / 5/8" PLYWOOD / NOTE: TAPER INSULATION TO ROOF DRAIN, 1" MIN."

## 4. Elevations (markup p11 / p12)

- `EIFS-1` (yellow) and `EIFS-2` (cyan) are areas per elevation. EIFS-2 is the vestibule parapet ("5" EIFS SYSTEM
  @ VESTIBULE PARAPET" in the exterior finish schedule).
- `ACM1, ACM2 FINISH - 1/A440` (teal) is on A-200. The wing walls are on A-420 (p17, 379.6 SF).
- `THRU WALL FLASHING`, `ALUMINUM FLASHING`, `PRE-FINISHED ALUMINUM SILL`, `SEALANT W/ BACKER ROD` are runs on each elevation. Add A-200 and A-201 together.
- **`Linear` 24.4 FT (bright green)** is an unnamed row. It is the line along the storefront glazing sill at the slab on the west elevation, with doors excluded. It feeds **integrated sill pan flashing** (line 188, detail 6/A430). Always render a row named "Linear" to find out what it is.

## 5. Cross-checks that worked

- **Batt = stud SF:** line 156 (8" batt) = line 311 (8" studs), 2652.875 SF. Line 155 = the 12'3" row of line 310.
  The legend rows themselves rebuild 156 to 2642.36 (−0.40%), and that residual is unexplained.
- **High-low wall = 46 LF:** it appears as 2x4 and 2x6 treated blocking (lines 91, 92), 35 studs @ 2' (line 308),
  92 SF batt, 115 SF rigid and +92 SF cover board.
- **Coping LF matches the treated-blocking LF** (A-140 carpentry lines; the pairing is by length, not stated): 2x10 148 = 6/A450, 2x14 40 = 9/A450, 2x16 15 = 3/A430, 1x6 40 = curb.
- **Rigid behind cladding = ACM line + brick line** (490 + 400 = 890).
- **Fluid-applied VB = EIFS + ACM lines + canopy-ceiling sheathing (line 85).** Brick VB is a separate masonry line (35).
- **RT2 = 5/8" plywood at roof (line 84, 285) = 2" polyiso (line 158, 285).**

## 6. Traps hit on this job

1. **Duplicate line.** Lines 150 and 189 are both "SEALANT W/ BACKER ROD 221.96 LF", the same A-200 + A-201 runs. An app that aggregates by material key will (correctly) report it once. Do not "fix" the app to match.
2. **Misleading description.** Line 154, "3-1/2" BATT INSULATION AT EXTERIOR WALLS", is the 3-5/8"-stud high-low roof wall (8/A450), not an exterior wall on A-120.
3. **Spec vs drawing conflict.** The cover board is 1/4" on A-140 and A-450 but 1/2" glass-mat gypsum in 07 5423 (p184). The estimator followed the drawings. Flag it as an RFI.
4. **Spec index gaps.** `spec_index.json` does not list 07 2413 EIFS (p151–158) or 07 5423 TPO (p179–187), and its 07 4213 range swallows them. Read the page headers.
5. **Roof insulation by layer vs by stack.** RT1 is 3 × 2". The estimator carries 1864 SF of "6" polyiso", not 5592.9 SF of 2" boards.
6. **"Assumed" vapor barrier.** Line 165 has no basis in the drawings or the TPO spec. Keep it as an assumption, at low confidence.
7. **XPS "where req'd zones > 4".** G-003 makes under-slab XPS conditional, and the job is in zone 3a. The estimator carried it anyway (2298 SF). Treat it as an alternate.
8. **Parapets inside the 8" batt.** The 656 SF of parapet above the roof deck is included in line 156 because the estimator copied the stud SF.
9. **Two 9/A430 meanings.** "9/A430" on the roof plan is a run label (the storefront head under the canopy). It is not a coping or an edge. Both the head flashing and the self-adhered strip take it.
10. **Cricket overlap.** The cricket area sits over RT1 and is not added to the membrane or the vapor barrier.
11. **Legend display rounding.** 153 and 155 imply 28.5 and 9.25 LF where the legend shows 28.4 and 9.2. Deltas of 0.3–0.6% are expected.
12. **Drawing reference "A1.1"** on line 148 does not exist in this set. The line looks carried from a template, and its LF matches an inferred rule, not a legend row.
13. **Opening sealant 1330 LF** is a round number with no takeoff on A-600. Treat it as an allowance. That 910 (line 88) + 419.06 (glazed perimeters) comes to 1329.06 is a coincidence, not a rule.
14. **Canopy-edge membrane is a 4" wrap, not the fascia girth.** Detail 10/A430 says "WRAP MEMBRANE 4" MIN. OVER EDGE OF CANOPY", and detail 7 draws about 3-1/2". The 12" + 12" + 6" girth on line 183 is the ACM. With the measured rows, membrane line 162 rebuilds to 2740.47 SF, and about 302 SF of the estimator's 3042.774 has no measured basis.
