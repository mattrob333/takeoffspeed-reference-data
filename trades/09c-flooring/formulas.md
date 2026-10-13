# Formulas: flooring, grout, base, transitions

Units: SF, LF and FT. All arithmetic was done in Python (`trades/09c-flooring/scripts/build.py`, `grout.py`). Every quantity is **net**. The estimator applied no waste, attic stock or stick rounding to any line in this trade, so the engine has to be compared in `mode: 'net'`.

---

## F1. Tag area: `tagArea`

**Lines:** 217 CON-1, 218 CR-1, 219 CR-2, 220 CR-3, 221 CR-4, 222 FT-1, 223 LVT-1.

**Inputs**

- `areas_sf[]`: the polygons of one finish tag, in SF.
- `insets_sf[]`: polygons of other tags that lie inside the field, in SF.
- `door_strips_sf[]`: the strip of each door opening from the jamb face to the door centreline, in SF.

**Rule**

```
Q_tag = Σ areas_sf − Σ insets_sf + Σ door_strips_sf
```

- Measure to the finished wall face.
- At a door, the material that ends there stops at the door centreline. This follows A-150 general note C ("THE SEAM IS TO BE CENTERED UNDER THE DOOR") and spec 09 6519 3.3.E ("Extend floor tiles to center of door openings").
- A field is net of the insets of other tags inside it.
- Do not deduct millwork, counters (SLD-1), toilets or other fixtures. The specs extend tile and carpet "into toe spaces" and "under or behind equipment".
- A mat sitting on another finish **is** deducted from that finish. The CON-1 polygon stops at the MAT-1 outline.

**Conventions**

- One record per tag.
- Tags must be split by pattern polygon, not by room. The meeting-room and relaxed-seating diamonds carry three tags in one room.

**Worked examples**

- CON-1 (line 217), ELEC./I.T. 106, from the A-150 vector layer at 18 pt/ft:
  - room 6.783 × 10.917 = 74.05 SF
  - minus MAT-1 2.0 × 3.0 = 6.00 SF
  - plus half the door strip: 3.00 ft clear opening (between the 2" frame members; = A-600 3'-0") × 0.494/2 ft wall depth = 0.74 SF
  - **68.79 SF**, against 68.78 (+0.02%). The legend reads 68.8.
- LVT-1 (line 223), GATHERING AREA 103: plank hatch 9.739 × 9.622 = **93.71 SF**, against 93.95 (−0.26%). The legend reads 94.0.
- CR-1 (line 218): the field polygons in 105 and 102, net of the CR-2 and CR-3 diamonds. The legend reads 131.4, against 131.36.

**Purchase conversions (not carried; for the engine)**

- carpet tile: SF ÷ tile SF. CR-1 + CR-2 + CR-3 = 594.11 SF ÷ 3.0 = 198.0 tiles; CR-4 82.42 ÷ 4.5 = 18.3 tiles.
- FT-1: 946.11 ÷ 4.0 = 236.5 tiles.
- LVT-1: 93.95 ÷ 2.691 = 34.9 planks. One plank is 0.25 m × 1 m = 0.25 / 0.3048² = 2.691 SF.
- Attic stock at 10% (spec 1.2.E / 1.2.C / 1.2.H) is a separate line:
  - FT-1: 94.61 SF
  - carpet: 67.65 SF
  - LVT: 9.40 SF
  - WB-1: 40.47 LF

---

## F2. Rectangle area: `rectArea`

This is a special case of F1 for one dimensioned rectangle: `Q = L × W`.

**Worked example (line 223):** 9.739 × 9.622 = 93.71 SF. The fixture uses this input with a 0.5% tolerance.

---

## F3. Grout area, rounded up: `groutAreaRoundUp`

**Lines:** 225 GR-1, 226 GR-3.

**Inputs**

- `tile_sf{tag: SF}`: the net SF of each tile tag that this grout serves, taken from the tile lines.
- `allowancePct`: 10.
- `roundUpTo_sf`: 50.

**Rule**

```
Q_grout = ceil( Σ tile_sf × (1 + allowancePct/100) / roundUpTo ) × roundUpTo
```

**Which tiles each grout serves (as the estimator applied it)**

- GR-1 = FT-1 floor tile (946.11).
- GR-3 = WT-1 + WT-2 + WT-9, the 3"x12" Roca Flow blend on the restroom walls and the A-703 / A-705 backsplashes (144.19 + 46.72 + 53.22 = 244.13).
- WT-3 (transaction bar, 38.42 SF) is **not** included. A-170 lists the transaction bar under GR-1.
- The WT-8 bullnose (11.28 LF × 3" = 2.82 SF) makes no difference to the result.

**Worked example**

- GR-1: 946.11 × 1.10 = 1040.72, ceil to 50 → **1050** (exact).
- GR-3: 244.13 × 1.10 = 268.54, ceil to 50 → **300** (exact).

**Basis and confidence**

- The 10% matches the project's attic-stock rate in spec 09 3000 1.2.E ("Furnish 10 percent attic stock of tiling materials").
- The round-up to 50 is the estimator's own habit. Elsewhere in this estimate he rounds up to 0.5 FT, 5 SF, 10 SF and to whole SF.
- `grout.py` tested scopes × waste 0–30% × increments of 10, 25, 50 and 100:
  - Only increment 50 fits both lines.
  - With FT-1 only, any waste of 6–10% fits.
  - With WT-3 added to GR-1, any waste of 3–6% fits. GPT-6 Astra proposed "include the bar, 5%, ceil 50" as an equally good fit.
- Two data points cannot separate these. The 10% / FT-1-only reading is preferred because it uses one clean percentage that also appears in the spec.
- Ratios of line to tile area are 1.110 (GR-1) and 1.229 (GR-3). A single multiplier cannot be the rule.

**What a correct grout takeoff would add (not in the estimate)**

- Grout product quantity from joint geometry: in³/SF = 144 × J × (L + W + J) × D ÷ ((L + J)(W + J)).
- For FT-1 with the spec's 1/4" joint and an assumed 3/8" depth: 1.11 in³/SF, so 946.11 SF ≈ 0.61 CF net, before the manufacturer's coverage factor and the 10% loss.
- The tile thickness is not on the drawings, so this stays a flagged assumption.

---

## F4. Traced run: `tracedRun`

**Lines:** 227 WB-1, 228 WT-8, 229 FTS-1, 231 FTS-3, 233 Schluter cove trim.

**Inputs**

- `runs_lf{location: LF}`: the PlanSwift linear items, as measured.

**Rule:** `Q = Σ runs_lf`.

**How each run is made**

- **Base (WB-1):**
  - finished wall face, net of door openings
  - includes the walls of carpet, tile, LVT and concrete rooms
  - **Base LF = room perimeter − Σ door widths + returns** (the rule spec 09 6513 3.3 describes)
  - The estimator did not split Style A (carpet) from Style B (resilient), and did not exclude the restrooms. WB-1 is tagged there, although elevation A shows WT-8 tile base.
- **WT-8:**
  - RESTROOM ELEVATION - A (10/A-410), 7'-3 1/2" wide. Its marker is only in MEN'S 112, so it is the Men's west wall, and the door drawn in it is JANITOR door 115 (beside the CR card reader, with TA-4/TA-9 on the same wall).
  - The Men's door 113 and the Women's door 112 are both in the south walls, 6" from the side wall. The "similar" Women's wall, the east wall with its own TA-4/TA-9, therefore has no door.
  - Rule: WT-8 = Σ side walls net of the doors in them = Women's east wall (full) + Men's west wall − door 115.
  - The estimator traced both walls on elevation A: run 1 at full width (7.29, the Women's east wall) and run 2 net of door 115 (3.67 + 0.22 = 3.89, the Men's west wall). The total is 11.18 against 11.28 (−0.87%).
  - With the elevation width as printed: (7.292 − 3.0) + 7.292 = 11.58 (+2.7%). With the plan depth 7'-8 1/8": (7.677 − 3.0) + 7.677 = 12.35 (+9.5%). The elevation's 7'-3 1/2" and the plan's 7'-8 1/8" disagree; the estimator followed the elevation.
- **FTS-1:**
  - door openings where carpet meets tile, plus the open edges of the carpet polygons
  - booth 104 east edge (F003)
  - relaxed seating 102 north and west edges
  - transaction bar 108 west edge (F001) and north edge
  - work room 111 east opening
  - phone room 114 door, meeting room 105 DIRTT door (F002), weather vestibule 100 east edge
- **FTS-3:**
  - Σ threshold openings: ELEC./I.T. 106 (3.00, the clear opening between the 2" frame members at x 1024.0–1078.0 pt on A-150; the outside of the frame, 3.33, is not the strip length), exterior storefront opening at EMPLOYEE LOUNGE 110 (3.17) and exterior pair opening at WEATHER VESTIBULE 100 (6.08), both flagged F004.
  - Total 12.25 LF from vector openings, against 12.24 (+0.08%). By door-schedule leaf widths 3 + 3 + 6 = 12.0 (−2.0%).
- **Schluter cove trim:**
  - measured on A-410; on the elevations the runs are hidden under the tile fills, and on the plan the olive runs are visible on the two side walls (Men's west, broken by door 115; Women's east, full).
  - Rule: cove trim runs at the floor on every tiled or tile-based wall = band walls B, C and D + the WT-8 side walls = both restroom perimeters net of the three doors (112, 113, 115). Elevation A's "SCHLUTER COVER TRIM" leader at the WT-8 base puts cove on the A walls too.
  - From the A-410 plan dimensions (Men's 7'-8" × 7'-8 1/8", Women's 7'-6 3/8" × 7'-8 1/8"): 30.688 + 30.417 = 61.10 − 3 × 3.00 = **52.10 LF**, against 51.87 (+0.45%). This equals the top-trim walls 39.75 (F7) + the WT-8 walls by plan (7.677 − 3.0) + 7.677 = 12.35.
  - Net of only the two restroom doors: 55.10 (+6.2%). Band walls plus the measured WT-8 runs, 39.75 + 11.28 = 51.03 (−1.6%).

**Worked example (line 227):** the legend reads `WB-1 404.7 FT` and the estimate 404.72 LF. Purchase is 404.72 ÷ 120 = 3.37 coils (or 102 pieces of 4'). Not carried.

---

## F5. Boundary run: `boundaryRun`

**Line:** 230 FTS-2.

**Inputs**

- `sides_ft[]`: the sides of a material polygon that meet another floor material. Sides that end at a wall are excluded.

**Rule:** `Q = Σ sides_ft`.

**Worked example:** the LVT-1 rectangle is 9.739 wide × 9.622 deep. Its north side is the wall. FTS-2 = 9.622 (west) + 9.739 (south) + 9.622 (east) = **28.98 LF**, against 28.99 (−0.03%).

---

## F6. Perimeter of an inset item: `perimeter`

**Line:** 232 FTS-4.

**Inputs**

- `rect_ft [W, L]`: the drawn mat outline.

**Rule:** `Q = 2 × (W + L)`. The Reno-Ramp runs right round the mat (detail 4: "SECURE ANCHOR LEG IN MORTAR BOND BENEATH MAT-1").

**Worked example:** 2 × (2.0 + 3.0) = **10.00 LF**, against 10.02 (−0.20%).

If the scheduled 36"x48" mat is used, the perimeter is 14.0 LF (+40%). The transition and the mat must use the same size.

---

## F7. Band top edge: `bandTopEdge`

**Line:** 234 Schluter trim (Jolly J AE, the top trim of WT-1).

**Inputs**

- `walls_ft[]`: the tiled wall lengths of elevations B (partition), C (back wall) and D (entrance wall, net of the 3'-0" door), from the A-410 plan dimensions. The two rooms differ in width, so list both:
  - Men's: B 7.677 (7'-8 1/8"), C 7.667 (7'-8"), D 7.667 − 3.0 = 4.667 (includes the 6" nib beside the door)
  - Women's: B 7.677, C 7.531 (7'-6 3/8"), D 7.531 − 3.0 = 4.531
- `rooms`: 1 when the walls of both rooms are listed; 2 when one room is listed and the other is "similar" (A-410 plan note) and the same size.

**Rule:** `Q = rooms × Σ walls_ft`. This is the top edge of the 5'-6" band, less doors that cut the full band.

**Worked example:** (7.667 + 7.677 + 4.667) + (7.531 + 7.677 + 4.531) = **39.75 LF**, against 39.55 (+0.51%). The legend reads 39.6. Scaling elevations B, C and D at 36 pt/ft instead (B 7.508, C 7.675, D 4.006 + 0.333) gives 2 × 19.522 = 39.04 (−1.3%); the elevation scaling reads the 6" nib right of the door as 0.333 ft and the widths short, so the plan dimensions are the better input.

The backsplash tile on A-703 and A-705 carries no trim line.

---

## F8. Mat: `matArea` (judgment line 224)

**Inputs**

- `count`: 1.
- `size`: as scheduled, 36"x48" (A-170 MT-1).
- `drawnSize`: 2'-0"x3'-0" (A-150 vector rectangle).

**Engine rule:** `Q = count × scheduled W × L` = 12.0 SF.

**Estimator:** 10.0 SF. This cannot be reproduced. The drawn area is 6.0 SF (the legend reads `MAT-1 FLOORING 6.0 SQ FT`). The estimate sits 67% above the drawn area and 16.7% below the scheduled one. Two hypotheses fit, and neither is provable:

1. The drawn 6.0 rounded up to the next 5 or 10 SF. This matches the estimator's habit of rounding up.
2. The FTS-4 value of 10.02 was reused in the SF line. GPT-6 Astra rated this "suggestive, low confidence".

Classification: allowance/judgment. Do not tune a formula to it. Carry 12 SF and flag the conflict between the drawn and scheduled sizes.

---

## Conventions used by this estimator (computed from this job)

| Convention | Value | Basis |
|---|---|---|
| Floor areas | net polygon per tag, to the door centreline, insets deducted, mat deducted, no fixture deductions | rebuilt CON-1 +0.02% and LVT-1 −0.26% from the vector layer |
| Waste on flooring and base | 0% | every measured line equals its legend value |
| Attic stock | not carried | spec asks 10% in 09 3000, 09 6513, 09 6519 and 09 6813 |
| Grout | SF, = ceil50(1.10 × served tile SF) | fits both GR lines exactly |
| Transition LF | traced interface length (clear door opening between frames, or polygon edge); no sticks | FTS-2 −0.03%, FTS-4 −0.20%, FTS-3 +0.08% |
| Base | one line for all rooms; no Style A / B split; corners not counted | spec says job-formed corners |
| Restroom tile base and cove | WT-8 on the two side walls (elevation A and its "similar" wall) net of doors; cove trim on all four walls net of doors | WT-8 −0.87%, cove trim +0.45% |
| Precision | estimate carries PlanSwift's full value; the legend shows 1 decimal | deltas ≤ 0.33% |
