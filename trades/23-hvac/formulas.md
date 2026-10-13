# 23 HVAC — formulas

All arithmetic was done in Python (`trades/23-hvac/scripts/duct.py`, `build.py`). Lengths come from
the PlanSwift legend on markup p53 (M-301), which prints one decimal. The estimate keeps PlanSwift's
full precision, so measured LF lines differ from the legend by up to 0.05 LF.

## F1 — Rigid duct surface area (basis of F2 and F3)

- **Inputs**: for each rectangular size W×H (in), measured LF; for each round diameter D (in), measured LF.
  Flex is excluded. Vertical drops are not added (the estimator measured plan length only).
- **Rule**:
  `SF_rect = Σ LF × 2 × (W + H) / 12` and `SF_round = Σ LF × π × D / 12`; `SF_rigid = SF_rect + SF_round`.
  This is the bare sheet-metal surface. There is no seam, joint, fitting or waste factor, and no stretch-out
  for insulation thickness.
- **Convention basis**: the estimator's own. Both derived lines on this job match it to within 0.03%.
- **Worked example (this job)**:

| Size | LF (p53) | SF per LF | SF | LBS at 0.906 |
|---|---:|---|---:|---:|
| 8x10 rect | 31.1 | 2 × (8 + 10) / 12 = 3.0000 | 93.30 | 84.53 |
| 14x12 rect | 7.3 | 2 × (14 + 12) / 12 = 4.3333 | 31.63 | 28.66 |
| 20x12 rect | 94.4 | 2 × (20 + 12) / 12 = 5.3333 | 503.47 | 456.14 |
| 24x12 rect | 13.3 | 2 × (24 + 12) / 12 = 6.0000 | 79.80 | 72.30 |
| 16x12 rect | 41.4 | 2 × (16 + 12) / 12 = 4.6667 | 193.20 | 175.04 |
| 10x10 rect | 7.4 | 2 × (10 + 10) / 12 = 3.3333 | 24.67 | 22.35 |
| 8x8 rect | 10.6 | 2 × (8 + 8) / 12 = 2.6667 | 28.27 | 25.61 |
| 12x12 rect | 9.8 | 2 × (12 + 12) / 12 = 4.0000 | 39.20 | 35.52 |
| 8" round | 113.7 | π × 8 / 12 = 2.0944 | 238.13 | 215.75 |
| 6" round | 18.0 | π × 6 / 12 = 1.5708 | 28.27 | 25.62 |
| 10" round | 10.5 | π × 10 / 12 = 2.6180 | 27.49 | 24.90 |
| 14" round | 10.2 | π × 14 / 12 = 3.6652 | 37.38 | 33.87 |
| **Total** | 215.3 rect + 152.4 round | | **1,324.81** | **1,200.28** |

  The legend's 1-decimal rounding bounds the error at ±0.05 LF × Σ(SF/LF) = ±2.2 SF (±0.16%).

## F2 — Sheet-metal weight (line 446, LBS)

- **Inputs**: `SF_rigid` (F1, SF); gauge per size from the drawing gauge rule (M-001 Part 2 §1.B:
  rectangular 26 ga for all sizes; round ≤14" 26 ga, 15–26" 24 ga); sheet weight by gauge (lb/SF).
- **Rule**: `LBS = Σ_gauge SF_gauge × lb/SF(gauge)`. On this job every run is 26 ga, so
  `LBS = SF_rigid × 0.906`. The result is rounded to a whole lb (1,200.28 → 1,200); whether the shop
  rounds to 10 or 100 lb cannot be told from this job, because 1,200.28 rounds to 1,200 at any of them.
- **Constants**: 26 ga galvanized = 0.906 lb/SF (the usual galvanized gauge weight; 24 ga 1.156,
  22 ga 1.406). The estimate's implied ratio is 1,200 / 1,324.81 = 0.9058 lb/SF.
- **Worked example**: 1,324.81 SF × 0.906 = 1,200.28 → **1,200 LBS** (estimate 1,200; +0.02%).
- **Convention**: seam/joint allowance = 0 and waste = 0 (the estimator's own). A shop that adds 15%
  for seams on rectangular duct and 10% on round would get 1,365 lb.

## F3 — Duct insulation area (line 447, SF)

- **Inputs**: `SF_rigid` (F1). Thickness (1.5" on the estimate, 2.2" in the spec) is a description only.
- **Rule**: `SF_insulation = SF_rigid` (all rigid supply and return duct, bare surface, no lap, no
  outside-of-insulation perimeter, no waste). Rounded to the whole number.
- **Worked example**: 1,324.81 → **1,325 SF** (estimate 1,325; −0.01%).
- **Basis and caveat**: this is the estimator's convention. The spec splits the scope: 1" liner in all
  return duct and the first 25 ft downstream of each RTU, and 2.2" R-6 FSK wrap on the unlined supply
  (23 0713 §2.1, §2.2, §3.1.B/F). An outside-of-wrap stretch-out
  (`LF × (2(W+H) + 8t + lap) / 12`; round `LF × (π(D+2t) + lap) / 12`) gives 1,721 SF at t = 1.5" with a
  2" lap and 1,877 SF at t = 2.2". Neither is what the estimator did.

## F4 — Measured LF (lines 448–452)

- **Rule**: `LF = legend LF` for that item, net. There is no waste, no added drops, and no rounding to
  box lengths.
- **Worked**: 6" flex 6.9 (est 6.92), 8" flex 50.1 (50.09), 10" flex 4.8 (4.83), 14" flex 3.1 (3.12),
  refrigerant 30.9 (30.86). Largest delta −0.64% (legend rounding).
- **Refrigerant is not the route counted once.** M-301 draws the line set as two parallel lines
  (keynotes 1 and 2 point at both). The purple PlanSwift trace on p53 runs up from FCU-1, out along one
  drawn line, back along the other, down, and then along the top edge of FCU-1 and on along grey linework
  with no pipe under it. Measured on the p53 raster at zoom 8 (66.1 px/ft):

  | Segment | FT |
  |---|---:|
  | FCU riser leg | 1.22 |
  | Upper drawn pipe | 10.52 |
  | End cap | 0.36 |
  | Lower drawn pipe | 9.89 |
  | Drop | 0.89 |
  | Third leg (no pipe drawn) | 7.97 |
  | **Total** | **30.86** (30.85 from the rounded parts) |

  The total equals the estimate's 30.86 LF. The route counted once (riser leg + one pipe) is 11.75 FT, so
  the legend value is 2.6× the route. Both pipes plus the end cap and drop give 22.89 FT; the remaining
  7.97 FT leg has no drawn pipe and its purpose is unresolved. No vertical rise was added, and the roof
  segment on M-302 (HP-1 to the roof penetration) is not included. A takeoff that measures the route once
  (~11.75 LF) or two pipes (~22.9 LF) will not reproduce line 452.

## F5 — Counts by tag + size + CFM (lines 453–473)

- **Inputs**: device tags printed on M-301 (`LSD (2-48")` with `140 CFM`; `65S`; `220R` + `10"x10"`).
  The neck size comes from the M-101 air distribution schedule's CFM bands (supply: 0–100 → 6"ø,
  101–210 → 8"ø, 211–330 → 10"ø, 331–480 → 12"ø, 481–650 → 14"ø).
- **Face size** comes from the drawn symbol on M-301, not from the CFM. M-101 prints two overlapping
  6"ø bands, `0-90` "FACE SIZE SHALL BE 12X12" and `0-100` (24x24 module), so a CFM ≤90 does not decide
  the face: 60S and 80S are ≤90 CFM and are carried as 24x24. Measure the symbol: the two 65S squares are
  drawn 1'-0" (18 pt at 18 pt/ft on the sheet) → 12x12; 60S, 80S, 160S, 240S and 370S are drawn 2'-0"
  (≈36 pt) → 24x24.
- **Rule**: one estimate line per distinct (device type, face/slots, neck, CFM). `EA = number of tags`.
- **Worked**: LSD (2-48") at 140 CFM appears 6 times in the M-301 text layer, so 6 EA (line 455).
  220R/10"x10" appears 2 times, so 2 EA (line 469). Supply tags 80S, 60S, 160S, 370S, 240S give one
  24x24 line each with necks 6/6/8/12/10"; 65S ×2 gives the 12x12 line. All 21 lines are exact.

## F6 — Counts by schedule tag or symbol (lines 474–488, 492–494)

- **Rule**: `EA = count of the tag (EF-1, RTU-1, HP-1) or the M-002 symbol (T, S, SAT/ST, RAT/RT, C, V,
  PC, TR, OAT)` on the sheet that shows it. Ceiling devices are counted on M-301 and roof devices on M-302.
  A split system is one EA, counted at its outdoor unit (HP-1).
- **Worked**: symbol T ×4 → thermostats 4. SAT + ST → supply-air temperature sensors 2. RAT + RT → return-air
  temperature sensors 2. C ×2 → CO2 2 (grid line "C" excluded). OAT ×2 on M-302 → 2.

## F7 — Counts by keynote tag (lines 489–491, 494)

- **Rule**: `EA = number of keynote hexagons of that number on the plan`. This is not the number of devices
  the keynote describes.
- **Worked**: remote cable operated damper = keynote 6 tags (8, at slot-diffuser plenums) + keynote 7 tags
  (5, at ceiling diffusers) = **13** (line 489, exact). The tallies come from the M-301 text layer: "6"
  appears 10 times and "7" 7 times, less one grid bubble and one keynote-list number each. The
  device-based alternative would be 15 LSD + 7 supply diffusers = 22. Keynote 9 ×1 gives the wax VAV
  damper (490). Keynote 12 ×1 gives the sectorizing baffle (494). Plan text "MD IN VERTICAL" ×1 gives the
  manual damper (491).

## F8 — Area-basis allowance (line 445)

- **Rule**: `1 LS`. The building area is carried in the description ("AREA: 2000 SF"), rounded up from
  1,900 GSF (G-001).
- The quantity cannot be reproduced. It is the company's per-SF allowance convention for fittings, hangers,
  sealant and accessories that were not taken off. The same convention appears in plumbing 403, electrical 510 and
  low-voltage 622.
