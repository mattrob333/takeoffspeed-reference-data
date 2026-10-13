# Formulas — appliances, equipment, shades, furniture

There are five rules. All arithmetic was done in python (`trades/11-equipment-furnishings/scripts/build.py`).

---

## F1 Tag count (counted)

- **Inputs:** placements of one tag on the plan (EA), one value per sheet or room. Read the PlanSwift count legend, or the tag bubbles where there is no legend.
- **Rule:** `qty_EA = Σ placements(tag)`
- **Scope filter:** apply this only to rows the GC installs (see F5).
- **Worked example (line 354, CH-11 MERANO):** markup p9 legend `CH11 4.0 EA`. The A-160 text layer has four `CH-11` strings around TB-05B in Gathering Area 103. So qty = 4 EA, matching the estimate's 4.
- **Lines:** 338–342 (AE-02/03/04/06/07, 1 EA each); 343 (REMOTE TELLER TERMINAL, p3, 1 EA); 346–356 and 358–363 (17 furniture lines).
- **Unsuffixed plan tag (line 358):** plan tag `SS-03` (legend `SS03 1.0 EA`) has no suffix, but the schedule has SS-03A LUCA 2 SEAT (66.5"W x 33.25"D) and SS-03B LUCA 3 SEAT (95.75"W x 33.25"D). The sofa drawn under the bubble in Relaxed Seating 102 is one three-seat piece, 95.5 in wide x 33.3 in deep on the A-160 vectors, so the placement belongs to **SS-03B**. Rule: attach an unsuffixed placement to the suffixed row whose scheduled size matches the drawn symbol; the other suffixed rows are scheduled-only and go to F2. SS-03A (line 357) is therefore F2, not F1.

## F2 Scheduled but not placed (specified, estimator convention)

- **Inputs:** schedule row present (tag), plan placements = 0.
- **Rule:** `qty_EA = 1`, marked V.I.F.
- **Convention basis:** the estimator states it in the FURNITURE section note: "ALL BELOW FURNITURE ARE NOT FOUND ON PLANS BUT GIVEN ON FURNITURE SCHEDULE, SO WE ASSUMED 1 EA, PLEASE V.I.F." It is applied the same way to appliance AE-01. Ratio on this job: 41 of 41 unplaced, included rows carry exactly 1.
- **Exclusions:** a row that is TBD in both description and manufacturer **and** is not placed is dropped (SS-05). So is a row furnished by another trade (TB-08 CHECK WRITING STAND, "MILLWORKER", "SEE SHEET A-708"). CH-06 is TBD but **is** placed (2 on A-160), so it is kept at the plan count and labelled "CHAIR - CH-06".
- **Worked example (line 367, LK-01 LOCKERS, 16"W x 12"D x 72"H):** no LK-01 legend row on p9 and no `LK-01` string on A-160. Plan count is 0, so qty = 1 EA, matching the estimate.
- **Lines:** 337 (AE-01), 357 (SS-03A, not drawn; see F1) and 364–402 (39 lines).
- **Note:** TB-05B (line 396) *is* tagged once on A-160 at the Gathering Area table, but the estimator put no PlanSwift count on it. The convention and the true plan count are both 1, so the line reconciles either way.

## F3 Shade run length (measured)

- **Inputs:** each straight shade run along the interior face of the glazing on the RCP (LF), traced where the RCP legend's MOTORIZED MECHOSHADE symbol, or keynote CP4, sits.
- **Rule:** `run_LF = Σ runs`
- **Worked example (markup p5):** the eight runs measured on the raster (49.99 px/ft) are:

| Run | px | LF | Ceiling at run (RCP) |
|---|---:|---:|---|
| Employee Lounge 109, east storefront | 303 | 6.06 | 10'-0" ACT-1 |
| Transaction Bar 108, east storefront | 301 | 6.02 | 11'-0" ACT-2 |
| Relaxed Seating 102, east storefront | 668 | 13.36 | 12'-0" ACT-1 |
| Relaxed Seating 102, south storefront | 698 | 13.96 | 12'-0" ACT-1 |
| Entry 101, south storefront | 656 | 13.12 | 12'-0" PT-3 |
| Weather Vestibule 100, west storefront | 361 | 7.22 | 12'-0" PT-3 |
| Booth 104, west storefront | 403 | 8.06 | 12'-0" ACT-1 |
| Meeting Room 105, west storefront | 298 | 5.96 | 10'-0" ACT-1 |
| **Σ** | 3688 | **73.76** | |

The legend prints **74.0 FT** (Δ −0.32 %, within the trace accuracy). The estimator's internal value back-solves to 74.025 LF (F4).

- **Description LF:** "(75 LF)" = `ceil(74.025)` = 75. The estimator rounds the LF shown in the description up to a whole foot. The SF quantity uses the unrounded run.

## F4 Shade area (derived; drop is a judgment value)

- **Inputs:** run_LF (ft) from F3; drop (ft).
- **Rule:** `shade_SF = run_LF × drop`
- **Estimator convention:** **drop = 16 ft**, applied flat to every run. Basis: back-solved from this job, 1184.4 / 74.0 = 16.005 and 1184.4 / 16 = 74.025. That fits a PlanSwift linear item with a 16'-0" height, whose area the legend does not display. No 16'-0" dimension exists on A-130, A-131, A-3xx, A-430, A-610 or A-630. A-311 gives **two** storefront head heights: **10'-0"** in section 1, WALL SECTION AT STOREFRONT (SILL 2'-8" + 5'-5" + 1'-11" = 10'-0"; cross-check T.O. LOW PARAPET 17'-4" − 7'-4" = 10'-0"), and **12'-0"** in section 3, WALL SECTION AT ENTRY VESTIBULE ("T.O. STOREFRONT 12' - 0""). A-130 also prints a 10'-0" spot elevation at the exterior face of the Employee Lounge storefront. Ceilings at the runs are 10'–12', and both sections show a 2'-8" knee-wall sill. GPT-6 Astra, asked independently, reached the same reading: a manually set 16' height, with no industry rule that turns a 7'-4"–12' drop into 16'.
- **Worked example:** 74.025 × 16 = **1184.4 SF**, matching the estimate exactly. With the legend's displayed 74.0: 74.0 × 16 = 1184.0 SF (−0.03 %).
- **Drawing-based alternatives (do not reproduce the estimate):**
  - Drop = ceiling height at each run: Σ LF × ceiling = **855.1 SF** (−27.8 % vs the estimate).
  - Drop = storefront head, read per run. The drawings do not say which section governs each run, so the result is a range on the traced runs: 10'-0" everywhere **737.6 SF** (−37.7 %); 12'-0" at Entry 101 and Weather Vestibule 100, 10'-0" elsewhere **778.3 SF** (−34.3 %); 10'-0" at Employee Lounge and Transaction Bar, 12'-0" elsewhere **861.0 SF** (−27.3 %); 12'-0" everywhere **885.1 SF** (−25.3 %). The 12'-0" figure is section 3 only and is an upper bound, not the typical head.
  - Drop = spec 12 2413 2.4 B unit height, head to sill (2'-8" knee wall; the 1/4" deduction is ignored here): 74.025 × 7.333 = **542.9 SF** (−54.2 %) at a 10'-0" head; 74.025 × 9.333 = **690.9 SF** (−41.7 %) at a 12'-0" head. This is the specification's own sizing basis.
  The engine should default to a drawing-based drop read per run, keep `drop = 16 ft` as an overridable house convention that reproduces this estimator, and flag the difference.

## F5 Scope / responsibility filter (which schedule rows become lines)

- **Inputs:** schedule PROV. BY / INST. BY columns; the general notes.
- **Rule (as the estimator applied it):**
  - Appliances: include a row when INST. BY = GC (AE-01…AE-07; AE-07 is VENDOR / GC). Exclude VENDOR / VENDOR (AE-09…AE-15).
  - Bank equipment schedule: exclude all rows (VENDOR / VENDOR, general note D). Carry the remote teller terminal only as a plan keynote count, line 343.
  - Furniture: include every schedule row (General Note K, owner-provided, GC install assumed), except unplaced TBD rows and rows built by another trade (F2).
- **Worked example:** Appliance Schedule rows = 13 (AE-01…AE-04, AE-06, AE-07, AE-09…AE-15). INST. BY GC = 6, giving lines 337–342. Furniture Schedule rows = 59. Excluded SS-05 and TB-08 leaves 57, giving lines 346–402.
