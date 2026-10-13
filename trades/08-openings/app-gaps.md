# 08 Openings — TakeoffSpeed engine comparison

Engine files compared (read only):
- `lib/quantities/trades/interiors/doors-hardware.ts`: assemblies `opening`, `hardware-set`, `access-panel`, `overhead-door`, `specialty-frame`
- `lib/quantities/trades/interiors/windows-storefront.ts`: assemblies `storefront`, `window`, `louver`, `glazing`
- `lib/quantities/trades/structure/roofing.ts`: `roofing.counted` with kind `roof hatch`, section ACCESS HATCH
- `docs/QUANTITY_ENGINE.md`

## What it already does right

| Estimate lines | Engine | Result with this job's inputs |
|---|---|---|
| 190–196 doors | `doors-hardware.opening`: one line per group of marks, EA = number of marks; storefront frames get no separate frame line | exact (1, 3, 2, 1, 1, 1, 1) when grouped as in F1 |
| 198–206 hardware | `doors-hardware.hardware-set`: set line EA = marks the door schedule assigns; "a set naming no scheduled opening is not a record"; the door schedule governs | exact (sets 1 … 14, set 11 = 2) |
| 208–213 windows | `windows-storefront.window`: EA per tag with W×H in the item | exact (1, 1, 1, 2, 1, 1) |
| 214–216 storefront | `windows-storefront.storefront`: `(W×H − Σ doors) × instances`, which is the same formula as F4 | 107.000 / 53.021 / 44.250 SF against 107.3 / 53.22 / 44.56 (−0.28 / −0.37 / −0.70%). The doc's first validation reports 0.05% and 0.4–0.7% |
| 197 roof hatch | `roofing.counted` kind `roof hatch` gives section ACCESS HATCH | exact (1 EA) |
| 207 VAT frame | `doors-hardware.specialty-frame` exists, with section SPECIALITY FRAME | see gap 2 |

## Where it computes differently or lacks an input (ranked by quantity impact)

1. **Sealant and sill flashing would be double-counted.** This is the largest impact, and it lands in trade 07. `storefront` and `window` always emit perimeter
   sealant (default `perimeter-sealant-faces` = 2) and, for exterior frames, sill flashing. With this job's frames that comes to:
   - Window sealant: 2 × (W + H) × 2 faces over A, C, D, E×2, G, H = **537.2 LF**.
   - Storefront sealant (B, F, J, K, less door sills): **264.3 LF**.
   - Total **801.5 LF**. The estimator measured **221.9 LF** of "SEALANT W/ BACKER ROD" on A-200/A-201 (65.7 + 156.2), and that belongs to 07.
   - Sill flashing: the engine gives **74.5 LF** (67.6 windows + 6.9 storefront), against 48.3 LF "PRE-FINISHED ALUMINUM SILL" (28.9 + 19.4) measured on the elevations.

   *Change*: emit sealant and sill lines only when `sealedFaces` (and a new `sillFlashing` flag) are given explicitly, and default them to 0.
   Alternatively, suppress them whenever a `sealants.opening` or elevation-measured sealant record exists in the same run, so the joint is counted once.
   The engine's interior storefront (J, K) would also get 2-face sealant. A-600 det. 3 (INT. ALUM. JAMB/HEAD) does show sealant at the partition,
   but the estimator carried no frame sealant in Div 08 for any opening. Whichever trade owns that sealant should own it once.

2. **Specialty frame perimeter is taken at the opening, which gives −7.3%.** The engine computes `Σ 2 × (W + H) × faces` on the opening: 2 × (8.5 + 12.75) / 12 = **3.542 LF**
   against the estimator's **3.82**. Measuring at the frame centreline gives 3.875 LF (+1.44%).
   - *Change*: when `faceWidth` is given, use `2 × ((W + fw) + (H + fw))` and state the convention in the steps.
     `faceWidth` is currently text, so parse it as a length.
   - Add a warning when a keynote says "BOTH SIDES" but the detail says single-sided. With faces = 2 the engine would give 7.08–7.75 LF, about twice the estimate.

3. **Door grouping splits on raw remarks.** The opening key contains `remark` verbatim. A model passing the schedule comments as they are printed would write:
   - 191 as two lines: 112 + 113 "1" UNDERCUT" (2) and 114 (1).
   - 192 as two lines: 106 "CARD READER" (1) and 115 "CARD READER, 1" UNDERCUT" (1).

   The totals stay the same, but four lines are written where the estimate has two. *Change*: normalise `remark` to product-changing preps (CARD READER,
   AUTO OPERATOR, POWER ASSIST, KNOCK-DOWN FRAME, VENDOR PURCHASE) and drop undercut, clear-opening and similar notes into `spec`.

4. **Pair width.** The input doc says to give ONE leaf's width, but this schedule prints a type-D pair as 6'-0" × 8'-0". If 72" goes in with
   `leaves = pair`, the engine warns, labels the line "(2) 6'Wx8'H", and the opening width doubles to 12'. *Change*: when `leaves = pair`
   and the width is over 48", treat it as the pair width (leaf = W/2), or add `sizeBasis: leaf | pair`. Then the label comes out as the estimator's "(2) 3'Wx8'H".

5. **Storefront vs window rule is not encoded.** The estimator has a convention: a glazed frame with a door bay becomes storefront SF net of the door,
   and a frame without one becomes a window EA. Nothing in the engine enforces that choice, so a model could send A–H to `storefront`.
   That would give 155.5 + 88 + 74.7 + 2×44 + 124.4 + 130.7 = **661.2 SF** of extra exterior storefront instead of 7 EA. *Change*: document
   the rule in the `window` and `storefront` record text, and warn in `storefront` when `doors` is empty and the system is exterior storefront.

6. **Hardware items by others are counted as GC items.** `parseItem` counts every line with a leading quantity. Several lines on A-601 carry a quantity
   but belong to others, and they would appear as counted hardware:
   - "1 Credential Reader By Div 28 … OT"
   - "1 Permanent Medeco Cylinder By Owner … MC"
   - "1 Seals, Sweeps & Astragals By Aluminum Door Mfr. OT"
   - Set 14's DIRTT items (DT)

   The set line EA is still right. *Change*: recognise the trailing manufacturer code OT/MC/DT and "BY OWNER / BY DIV nn / BY … MFR" text, and write those items
   as `furnishedBy` others or move them to the set description without a count.

7. **Opening and frame lines beyond the estimate.** For the HM openings `opening` also writes a leaf line and a frame line (191: 3 leaves + 3 frames). This is useful
   detail for a supplier quote, but it has no matching estimate line. A family-level scorecard that sums EA across lines will show 3× the estimate.
   *Change*: tag the leaf and frame lines as breakdown (`component of opening`) so roll-ups do not add them.

8. **No window tag in the window item.** The item is `${W}Wx${H}H … WINDOW`. Two types of the same size would merge, and the estimator's item carries the tag
   ("… WINDOW - A"). *Change*: add a `tag` input and include it in the key and the item.

9. **Inputs the engine lacks for this trade.**
   - `location` for an inner vestibule door: document that the inner vestibule door is interior.
   - The sliding DIRTT door's "vendor purchase" flag.
   - A hatch spec reference (07 7200), since the hatch lives in roofing while the estimate files it under Div 08 DOORS / ACCESS HATCH.

## Reading problems, not arithmetic

- Tag A exists only on A-120 (A-110 omits it). Grid-letter bubbles (12.5 pt) sit next to the tag letters (9.5 pt) in the text layer.
- Set 5.0 lists door 101 a second time. The door schedule governs, and the engine's rule already handles this when the model passes marks from the schedule.
- The row `xxx / H / 3'-0" × 1'-0 5/8"` must not become a door record.
