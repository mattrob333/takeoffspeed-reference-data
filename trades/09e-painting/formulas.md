# Formulas: painting

Units: lengths are decimal feet (convert the printed feet-inches first: 8'-6" = 8.5, 12'-6" = 12.5), areas are SF, counts are EA. Every quantity is **net**: no waste, no gallons, no surface factors, because that is how the estimator carried them. All numbers were computed in python (`trades/09e-painting/scripts/build.py`).

---

## F1. Wall paint from finish-plan runs (painted height per run)

**Inputs**
- `runs[]`: each painted wall-face run traced on the finish plan, in LF, one face per room. Group the runs by painted height.
- `H` per group (ft): the ceiling height of the room the face bounds, read from the RCP tag (`9' - 0"A.F.F.`). Where the ceiling is exposed ("EXPOSED CEILING / ALL WALLS TO DECK"), use the partition height to structure (12'-6" on this job).
- `areas[]` (SF): wall faces traced on elevations instead of the plan, such as restrooms above a tile band. They are added as is.

**Rule**

`SF_tag = Σ_groups (Σ runs × H) + Σ areas`

Openings are **not** deducted from the finish-plan runs (the A-150 LF × H rows). Traced elevation areas can deduct them: on A-410 the elevation A polygon is cut around the door and the D polygons are notched at the door head, although the estimator's duplicate of A for the Men's room is a full rectangle that leaves about 23 SF of door in. Tile, FRP and wallcovering zones are excluded because they are never traced as paint runs: the restrooms are carried as elevation areas (A full height, B/C/D above the tile band), and the WC-1 and FRP-1 walls have their own runs.

**Worked example (line 295, PT-1).**

| Legend row (p08) | LF | H | SF |
|---|---|---|---|
| PT1 PAINT @ 12'H | 62.6 | 12.0 | 751.20 |
| PT1 PAINT @ 11'H | 15.0 | 11.0 | 165.00 |
| PT1 PAINT @ 8'6"H | 39.7 | 8.5 | 337.45 |
| PT1 PAINT @ 6'6"H | 4.9 | 6.5 | 31.85 |
| PT1 PAINT @ 10'H | 51.8 | 10.0 | 518.00 |
| PT1 PAINT @ 9'H | 117.1 | 9.0 | 1,053.90 |
| PT1 PAINT @ 12'6"H | 48.0 | 12.5 | 600.00 |
| **runs** | **339.1** | | **3,457.40** |
| PT1 WALL PAINT (p16, A-410, both restrooms; A full height less door, B/C/D above tile, copy of A without door cut) | | | 252.60 |
| **total** | | | **3,710.00** |

The estimator has 3,710.84 (−0.02%). The legend shows one decimal. A ±0.05 LF display rounding on seven rows, times their heights, allows ±3.5 SF, so the 0.84 SF difference is display precision and nothing else.

**Line 296 (PT-4).** 5.3 × 9 + 10.6 × 10 = 47.7 + 106.0 = **153.70** SF, against 153.62 (+0.05%; the display bound is ±0.95). The 10.6 FT tech-wall run steps around the A-704 recess (front, both side returns at the depth drawn on A-150, recess back), so it already holds the side returns and also the 37.2 SF PT-6 back wall.
**Line 298 (PT-7).** 10.3 × 10 = 103.0, then F9 rounding gives **105**.
**Line 299 (PT-8).** 7.4 × 10 = 74.0, then F9 gives **75**.

---

## F2. Wall paint from a traced elevation area

**Inputs:** `area` (SF) traced on an interior elevation.
**Rule:** `SF = area`, then F9 rounding when the line is small.
**Worked example (line 297, PT-6).** The A-704 recess back wall is 37.2 SF on the legend. The vector check is 7'-9 3/4" × 4'-9 1/4" = 7.8125 × 4.7708 = 37.27 SF. F9 rounds up to 5: **40** (raw −7.0%).

---

## F3. Gypsum ceiling paint = ceiling board + soffit faces

**Inputs**
- `ceilingSF`: the painted gypsum ceiling area (the RCP area item that carries the paint tag), in SF.
- `soffits[]`: each soffit run (LF) with the height of its gypsum face (ft), from item names like `SOFFIT @ 5'9"H, GWB @ 2'6"H`. "GWB BS" (both sides) means 2 × the soffit height. A row with no GWB height (`SOFFIT @ 2'H`) uses its own height.

**Rule**

`SF = ceilingSF + Σ (soffit LF × GWB face height)`

This equals the sum of the two gypsum-board parent lines, ceiling board and soffit board. The estimator painted every gypsum board SF that faces the room. ACT is never painted.

**Worked example (line 300, PT-3).**
soffit faces = 4.2 × 7.0 + 2.7 × 4 + 6.7 × 1.5 + 30.5 × 3 + 35.3 × 2.5 + 28.1 × 2 = 29.4 + 10.8 + 10.05 + 91.5 + 88.25 + 56.2 = **286.20** SF (estimate line 285: 286.04).
SF = 516.1 + 286.2 = **802.30**. The parent lines give 516.0 + 286.04 = 802.04, carried as **802** (+0.04%).

---

## F4. Exposed structure paint = plan area

**Inputs:** `planSF` of the rooms marked "EXPOSED CEILING" on the RCP; `surfaceFactor` (default 1.0; the estimator used none).
**Rule:** `SF = planSF × surfaceFactor`, then F9.
**Worked example (line 301).** 98.4 × 1.0 = 98.4, and F9 gives **100**.
**Convention basis.** The 1.0 factor is the estimator's own choice. The real painted girth of 1-1/2" Type B deck plus K-series joists is larger. The spec states no factor, so a factor is a contractor convention and has to be flagged.

---

## F5. Painted top of a plywood booth roof = plan area

**Inputs:** `planSF` of the booth roof framing plan (A-706 detail 2).
**Rule:** `SF = ceil1(planSF)`. Edges are not added, although A-706 says "ALL EDGES TO BE PAINTED GREEN".
**Worked example (line 302).** 76.2 → **77**. This is the same area and the same rounding as booth ceiling framing line 312 (77 LF).

---

## F6. Painted hollow metal frames = count by size

**Inputs:** the door schedule / legend rows whose frame is hollow metal, with their counts and sizes.
**Rule:** `EA(size) = Σ count of doors with an HM frame of that size`. Leaves count only when they are HM or paint-grade. Aluminium storefront, aluminium sliders and factory-finished wood leaves are excluded.
**Worked example (line 303).** On p21, TYPE B "W/ WELDED HOLLOW METAL FRAME" has 3 + 2 and TYPE C "W/ KNOCK-DOWN HOLLOW METAL FRAME" has 1, so **6** EA at 3'-0" × 7'-0". These equal estimate lines 191 + 192 + 193.

---

## F7. Opening trim (allowance; back-fit only)

**Inputs:** the carpentry line "INTERIOR TRIM AT OPENING, ASSUMED" (line 88).
**Rule (as carried):** `LF_paint = LF_trim(line 88) = 910`. `reconciliation.csv` therefore carries `recomputedQty` 910, `deltaPct` 0, classification `copied/allowance`; the back-fit below lives in the notes only.
**Back-fit hypothesis (not proven):** `LF = ceil10(2 × (Σ doors (2H + W) + Σ EA-counted window perimeters 2(W + H)))`
- doors, one face: 6 × (3 + 2 × 7) + (3.333 + 14) + (6 + 16) + (6 + 16) + (3 + 16) = 182.33
- windows A, C, D, E ×2, G, H: 49.92 + 38.67 + 34.67 + 53.33 + 45.33 + 46.67 = 268.58
- 2 × 450.92 = 901.83, and ceil10 gives **910** (−0.9% before rounding).

**Why it is still an allowance.** The rule counts the exterior face of exterior openings and leaves out the SF-carried storefront windows B, F, J and K (150.48 LF of perimeter). No sheet details paint-grade trim. Treat it as a scope allowance that has to be confirmed.

---

## F8. MEP paint: devices and pipe

**Devices.** `EA = count of devices tagged by a paint keynote`. On M-301 these are keynote 5 "IN UPPER CEILING. PAINT BLACK." (4 LSD) and keynote 8 "LSR(3) … INSIDE TO BE PAINTED FLAT BLACK" (1), so **5** EA (line 305).

**Pipe.** `LF(size) = Σ runs of exposed pipe whose note requires paint`, followed by F9. P-403 limits safety-yellow paint to "EXTERIOR ROOF-LEVEL NATURAL GAS PIPING".
- Line 306: the 3/4" run is 44.2, and F9 gives **45**.
- Line 307: the 1" run is 9.7, and F9 gives **10**.

**Cross-check.** The paint row `SAFETY YELLOW PAINT AT ROOD GAS PIPE` reads 53.9 = 44.2 + 9.7.

---

## F9. The estimator's rounding of small hand-entered lines

**Rule (observed on most small painting lines, not a job-wide habit):**
- A quantity that the estimator copies by hand from a single small legend row is usually rounded **up to the next multiple of 5**: `ceil5(x) = 5 × ⌈x / 5⌉`.
- Large multi-row sums keep PlanSwift precision (lines 295 and 296).
- Exceptions: the booth (76.2 → 77, rounded up to 1) and PT-3 (802.04 → 802, rounded to the nearest unit).

**Basis.** Every small hand-entered example found on this job, including two wallcovering lines (folder 09d) built from the same A-150 runs:

| Raw | Carried | ceil5 | Fits |
|---|---|---|---|
| 37.2 (297) | 40 | 40 | yes |
| 103.0 (298) | 105 | 105 | yes |
| 74.0 (299) | 75 | 75 | yes |
| 98.4 (301) | 100 | 100 | yes |
| 44.2 (306) | 45 | 45 | yes |
| 9.7 (307) | 10 | 10 | yes |
| 38.4 (272, 09a) | 40 | 40 | yes |
| 76.2 (302) | 77 | 80 | no, ceil1 |
| 802.04 (300) | 802 | 805 | no, nearest |
| 121.2 (239, WC-1: `WC1 @ 12'H` 10.1 FT × 12) | 120 | 125 | no, rounded down / nearest 5 |
| 103.0 (240, `WALL COVERING @ 10'H ABOVE PT7` 10.3 FT × 10) | 103 | 105 | no, unrounded |

The rule fits **7 of 11**. The same raw 103 SF (10.3 FT × 10) is carried as 105 on line 298 and as 103 on line 240, so the rounding is a per-line hand choice rather than a rule. GPT-6 Astra independently read this as "line-specific upward adjustments, not a uniform rule". The app should model it as an optional, per-contractor convention (`round-small-lines-up-to: 5`) and leave it off by default.

---

## F10 (cross-check, not an estimate line). Paint area of HM frames

The engine adds `frame SF = Σ (2H + W) × girth`. With the 12" default girth, 6 × 17 LF × 1 ft gives 102 SF. The estimator carries frames as EA only. If the app adds this SF, it has to be a separate line and must not replace the EA line.
