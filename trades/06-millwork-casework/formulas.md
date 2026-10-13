# Formulas — millwork, casework and countertops

All arithmetic below was run in Python (`trades/06-millwork-casework/scripts/py/rebuild.py`). Dimensions are feet unless marked.
"Printed" means read from a dimension string on the drawing; "legend" means the PlanSwift legend value on the markup page.

## Rounding convention (estimator's own, this job)

The estimator carries PlanSwift readings either unrounded (cabinet LF: 2.02, 4.66, 5.66) or rounded to a convenient value.
Observed rule on this job: **areas and splash/shelf LF → whole unit, normally rounded up** (17.4→18, 13.6→14, 5.5→6, 12.7→13,
6.6→7, 296.9→300, 89.3→90); **small cabinet runs → nearest half foot, up** (5.3→5.5, 0.875→1.0); exceptions rounded down
(6.2→6, 83.1→83, 64.2→64). Basis: every estimate that differs from its PlanSwift reading does so by 0.2–14% toward a round
number; two lines (142 booth walls, 116 library PL-1) also inherit a defective legend polygon, so they miss the dimension rebuild by
−2.9% and +81%.
The app should carry the exact figure (net) and offer rounding as a display option — not apply waste or whole-unit rounding to
fabricated millwork (see `app-gaps.md`).

---

## F1 Cabinet run (LF)

* **Inputs:** box widths `w_i` (ft) from the elevation dimension string for one cabinet type (category base/upper/tall, depth, height,
  configuration) in one room; fillers between boxes (ft) where dimensioned and in the same run.
* **Rule:** `LF = Σ w_i (+ Σ fillers in the run)`. One line per (room, category, depth, height, configuration, finish). Not countertop
  length. Box count = number of `w_i` (rides in the description, never carried as a second EA line).
* **Convention:** the estimator includes 1" fillers that sit inside the run (work room uppers, base at elev 3) and excludes end panels.
* **Worked examples:**
  * Service counter uppers (A-703 elev 2): 3'-0" + 3'-4" + 3'-4" = **9.667 LF** (estimate 9.66).
  * Back counter 2-drawer bases (A-701 elev 2, section 7): 1'-4" + 1'-4" + 1'-6" + 1'-6" = **5.667 LF** (estimate 5.66, legend "7" 5.7).
  * Work room uppers PL-3 (A-707 elev 4 + 3): (2 × 2'-7½" + 1") + (1¾" + 2 × 2'-8½" + 1¾") = 5.333 + 5.708 = **11.042 LF** (estimate 11.0).
  * Employee lounge 3-drawer bases (A-705 elev 2, section 5): 1'-6" + 1'-3" = **2.75 LF**.
* Totals: 18 cabinet lines, printed-dimension total 72.0 LF vs estimator 72.49 LF (−0.7%).

## F2 Countertop plan area (SF)

* **Inputs:** each leg along the wall `L_i` (ft), depth `D_i` (ft), inside corners `c`, stepped portions as extra rectangles.
* **Rule:** `SF = Σ L_i × D_i − c × D²` (+ Σ stub rectangles). Separate lines by material, finish tag, substrate thickness and support
  (cabinet vs bracket): the estimator splits PL-2 over 1½" plywood **with** support bracket (line 137) from the same top without
  (line 138), and keeps "O/ 1" PLYWOOD" (lounge) and "O/ 3/4"" (library) apart.
* **Worked examples:**
  * Employee lounge PL-2 (A-705 plan 1): 8'-8" × 2'-0" = **17.333 SF** (legend 17.4; estimate 18).
  * Work room top 1 (A-707 plan 1, elev 3 support bracket): (1¾" + 2 × 2'-8½") × 2'-0" + stub (1¾" + 7⅝") × 10¼" = 11.125 + 0.667 = **11.792 SF** (estimate 12).
  * Work room top 2 (A-707 plan 2): 5'-4" × 2'-0" = **10.667 SF** (estimate 11). Tops 1+2 = 22.46 SF vs legend 22.6.
  * Back counter SLD-1 (A-701 plan 1): 8'-8" × 2'-1" = **18.056 SF** (legend 18.1). Service counter SLD-1 (A-703 plan 1): 9'-10" × 2'-0" = **19.667 SF** (legend 19.7).

## F3 Solid-surface top including waterfall faces (SF) — line 344

* **Inputs:** plan area of each SLD-1 top; each waterfall / vertical SLD-1 face W × H on the elevations.
* **Rule (estimator):** `SF_SLD = Σ plan tops + Σ vertical waterfall faces`, summed across sheets into **one** line.
* **Spec basis:** 12 3669 2.2.B.4 "All 90 degree outside edges shall have waterfall finish"; 2.2.C ¾" quartz.
* **Worked example:** legends 73.4 (A-700) + 18.1 (A-701) + 19.7 (A-703) = **111.2 SF** (estimate 111.14, the unrounded sum).
  Transaction bar decomposition by printed dims: bar 10'-6¾" × 2'-11½" = 31.25, right end 1'-2¼" × 1'-9⅝" = 2.14 (plan bottom
  string 10'-6¾" + 1'-2¼" = 11'-9"), return 2'-0" × 3'-10¼" = 7.71 → plan ≈ **41.10 SF**; the remaining ≈ 32.3 SF of the legend are the
  waterfall/vertical faces on elevations 3, 4, 5, 6. Printed: side elevation 5 2'-11½" × 3'-9¾" = 11.28, elevation 6 block 35½" × 38¼"
  = 9.43; the back elevation 3 end block and the front elevation 4 1¼" edges have no closed dimension set, so the face split
  (≈ 32 SF) is legend minus plan — an estimate from the polygon extents, not a printed rebuild.
* **Spec-driven accessory not carried:** grommets `= ceil(top LF / 4)` per 12 3669 2.3.A.1 → transaction bar 15.31 LF (4),
  back counter 8.67 LF (3), service counter 9.83 LF (3) = 10 per top, or ceil(33.81/4) = 9 job-wide.

## F4 Backsplash (LF)

* **Inputs:** each top edge that meets a wall and has a splash in the section (ft); splash height (4").
* **Rule:** `LF = Σ wall edges`. Height rides in the description.
* **Worked examples:** phone room back wall 5'-6" = **5.5 LF** (legend 5.5; estimate 6). Work room (A-707; the back wall is the
  *bottom* edge of plan 1 and the *top* edge of plan 2 — check the elevation-marker direction): plan 1 back edge 6'-4⅛" − 7⅝" = 5'-8½"
  + notch 1'-1¾" + 7⅝" + stub end 10¼" against the side wall = 8.344 LF; plan 2 back edge 5'-4" = 5.333 LF → **13.677 LF** (legend 13.6;
  estimate 14 = rounded up, +2.4%). Pixel trace of the cyan on p30 confirms the same edges (69.8" + 13.8" + 7.5" + 10.2" + 64.4") and no
  2'-0" end return; the cyan on the two front edges is the same-colour (2) 1x4 blocking row.

## F5 Shelving (LF)

* **Inputs:** run length per tier (ft) — wall length, bay width or the dimensioned run; number of shelves (tiers).
* **Rule:** `LF = Σ run × tiers`.
* **Worked examples:**
  * Work room night-drop shelves (A-708 det. 12 "FULL LENGTH OF WALL", 2 shelves; A-120 west wall 7'-9⅜"): 2 × 7.781 = **15.5625 LF** (estimate 15.5).
  * Library (A-702 elev 2): top fixed shelf 3'-6" + 1½" + 2'-6¾" + 1½" + 2'-6¾" = 8.875, plus 2 adjustable × (2 × 2'-6¾" + 1½") = 2 × 5.25 → **19.375 LF** (legend 19.4; estimate 19.5).
  * Service counter open shelves: 2 × 3'-0" = **6.0 LF**. Back counter side bays: 4 shelves × 1'-0" = **4.0 LF**.
  * Janitor (A-410 elev 1): legend 12.7 = 3 shelves × 4.23 ft as drawn → estimate 13; by the plan wall 3 × 4'-6⅜" = 13.594 LF.
* Brackets / standards (not carried as separate lines by this estimator): `per run = ceil(run×12 / spacing) + 1`, × tiers.
  Janitor note: "SPACED EQUALLY (NOT TO EXCEED 2'-0")" → spacing 24".

## F6 Laminate finish face (SF by tag)

* **Inputs:** each exposed face W × H on the elevations for one finish tag in one assembly, or the traced area.
* **Rule:** `SF = Σ W × H` (no waste in the estimate).
* **Convention:** the staff-side face of a knee wall is taken equal to the customer-side face (same polygon re-used).
* **Worked examples:**
  * PL-4 (A-700 front elev 4 / det. 9): (10'-6¾" − 2 × 1¼") × 3'-8½" = 10.354 × 3.708 = **38.397 SF** (legend 38.4 = WT-3 tile = ¼" backer; estimate 38.5).
  * PL-3 (A-700): bands (10'-6¾" − 11" = 9'-7¾") + (11" + 24½" = 2'-11½") = 151.25" long × **6¼"** high = **6.565 SF** (legend 6.6;
    estimate 7 = rounded up, +6.6%). Back elevation 3 prints 1¼" (SLD-1 edge) / 6¼" (PL-3) / 1¼"; the separate 7½" string is the quartz
    edge plus the band — do not use it as the band height.
  * PL-1 back counter (A-701): legend 83.1 = elevation face ≈ 12.06 × 5.36 (64.6) + plan footprint 8'-8" × 2'-1" (18.06) = 82.7 by pixel check.
  * PL-1 library (A-702 elev 2): 9'-1½" × 8'-6" − cased opening 3'-6" × 7'-0" = 77.5625 − 24.5 = **53.06 SF** (front face, drawer fronts
    included). Legend 95.6 / estimate 96 do **not** reconcile (+81%): the salmon polygon fills the cased opening (~19 SF), runs ~4 ft
    past the millwork over the title block (~23 SF), misses the drawer fronts and adds a plan polygon (~9 SF).

## F7 Wall / ceiling panelling (SF) and reveals (LF) — booth A-706

* **Inputs:** each laminate face W × H; ceiling inside W × L; reveal runs.
* **Rule:** `SF_wall = Σ faces`; `SF_ceiling = W × L` inside the walls; `LF_reveal = faces × verticals per face × H + ceiling runs`.
* **Worked example (walls):** 2 outside faces 8'-0" × 9'-0" (plan 1, 144) + 2 inside faces 8'-0" × 9'-0" (section 5: 1'-11½" + ½" +
  4'-0" + ½" + 1'-11½" = 8'-0", 144) + 2 jamb/ends 9" × 9'-0" (13.5) + header 10'-0½" × 9" (9" + 8'-6½" + 9"; 7.531) = **309.03 SF**
  (estimate 300 = legend 296.9 rounded up, −2.9% vs the rebuild). Stopping the inside faces at the PNL-1 pocket (plan 1 string
  1'-11½" + ½" + 4'-0" + ½" + 1'-7½" = 7'-8") gives 303.03 SF. No wall face prints 7'-6" — that is the ceiling length (RCP 11 8'-0" less
  the 6" Mechoshade pocket). The legend is not a clean reading: the section-5 polygon runs past the booth over the title block and two
  polygons sit on the NTS 3D view (det. 10), so the legend landing within 4% of the rebuild is partly coincidence.
* **Ceiling:** 7'-6" × (1'-4" + 4'-6½" + 2'-8") = 7.5 × 8.542 = **64.06 SF** (legend 64.2; estimate 64).
* **Reveal:** 4 faces × 2 vertical reveals × 9'-0" = 72 + 2 ceiling reveals × 8'-6½" = 17.083 → **89.083 LF** (legend 89.3 FT; estimate
  90 with unit "SF" — the unit is LF). The two 4'-0" cross lines on RCP 11 are recessed linear lights, not reveals.

## F8 Removable panel / apron (LF)

* **Inputs:** knee-space width (ft); panel height.
* **Rule:** `LF = Σ opening widths`. Worked: A-705 sink knee space 2'-8½" = 2.708 LF (legend "7" 2.7; estimate 2.75).

## F9 Counted items (EA)

* **Rule:** `EA = Σ count of the unit/symbol on the plan, section or plan note`. Prefer a printed total ("MOCKETT MAX6-94 … (3 TOTAL)").
* Check desk 1, transaction-bar pencil drawer 1, Mockett grommets 3, Richelieu grommets 1 + 1, locker 1, table 1, booth seats 2.

## F10 Allowance / judgment

* Line 109 (5-drawer base): printed 10½" = 0.875 LF; estimate 1.0 LF — a 1 LF minimum, no source.
