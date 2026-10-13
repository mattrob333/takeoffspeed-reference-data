# Formulas: wall tile, wall covering, FRP

Units: lengths are in feet (decimal feet after you convert the printed feet-inches), areas are in SF. All quantities are **net**, with no waste and no attic stock, because that is how the estimator carried them. Numbers come from this job and were computed in python (`trades/09d-wall-finishes/scripts/*.py`).

---

## F1. Tile band area (gross band on an elevation)

**Inputs**
- `walls[]` (ft): the tiled length of each elevation inside the band, measured between finished faces. Leave out door widths that pass through the band.
- `H` (ft): the band height from the elevation dimension.
- `openings[]` (W × H, ft): only true openings inside the band, such as a door or a pass-through. **Do not deduct** plumbing fixtures, accessories, mirrors or appliances standing in front of the tile.
- `roomRepeat` (count): how many identical rooms the drawn elevations represent.

**Rule**

`bandSF = roomRepeat × (Σ walls × H − Σ openings_in_band)`

**Basis.** This matches what the estimator traced. On A-410 the cyan, magenta and blue polygons together equal Σ walls × 5'-6" for two rooms, within 0.2%.

**Worked example (A-410 restrooms).** The elevation widths, scaled from the PDF vectors at 1/2" = 1'-0" (36 pt/ft), are B = 7.508, C = 7.675 and D = 4.006 + 0.333. D is the wall left of the door plus a 4" strip right of the door frame, with the door taken out of the list. H = 5'-6" = 5.5. roomRepeat = 2, from the note "MENS INTERIOR ELEVATIONS ARE SIMILAR TO WOMENS".

`2 × (19.522 × 5.5) = 214.74 SF`

The legend total WT1 + WT2 + WT9 on p16 is 120.7 + 43.8 + 50.6 = **215.1 SF** (−0.17%). Using the exact vector height of 5.506 ft gives 214.96 SF (−0.06%).

Other bands:
- A-703 backsplash: (3'-4" + 3'-4" + 1") × 32" = 6.75 × 2.6667 = **18.00 SF** (legend 15.3 + 1.4 + 1.3 = 18.0).
- A-705 backsplash: (2'-4" × 3 + 2") × 1'-6 1/2" = 7.1667 × 1.5417 = **11.05 SF** (legend 11.1, −0.46%). The microwave is not deducted.
- A-700 front: 10'-4 1/4" × 3'-8 1/2" = 10.3542 × 3.7083 = **38.40 SF** (legend 38.4, line 38.42, −0.06%). The front elevation (4/A-700) carries no width, but the back elevation (3/A-700) prints the bar as 11'-9" overall, **10'-6 3/4" from FACE OF WALL** to the outside of the waterfall edge. The front elevation draws a 1 1/4" SLD-1 return at both ends of the tile field (the right one against the wall), so the field is 10'-6 3/4" − 2 × 1 1/4" = 10'-4 1/4". **Vector check:** at 3/4" = 1'-0" (54 pt/ft) the tile field runs from 814.51 to 1374.19 pt = 10'-4 3/8" (38.44 SF, +0.05%), and both returns measure 1 1/4". The drawn overall is about 1/8" longer than the printed 10'-6 3/4", so use the printed figure.

---

## F2. Splitting a blended band by tag

A band laid in a mix of tags, such as WT-1, WT-2 and WT-9 in a random-drop pattern, has to be split before each tag gets a line.

**Rule (estimator's method, preferred).** Use the area traced per tag on the elevation:

`tagSF = Σ (traced polygons of that tag)`, where the field tag is the band minus the accents.

`fieldSF = bandSF − Σ accentSF`

**Fallback (when the pattern is not drawn).** Use the finish schedule MIX %:

`tagSF = bandSF × mix%`

Here A-170 gives WT-1 60%, WT-2 20% and WT-9 20%.

**Worked example.** The whole blend is 244.13 SF (lines 235 + 236 + 238).

| Tag | MIX % | Mix-derived | Estimator | Δ |
|---|---|---|---|---|
| WT-1 | 60% | 146.48 | 144.19 | +1.6% |
| WT-2 | 20% | 48.83 | 46.72 | +4.5% |
| WT-9 | 20% | 48.83 | 53.22 | −8.3% |

The actual share differs by location:
- Restrooms: 56.1 / 20.4 / 23.5%.
- A-703: 85.0 / 7.8 / 7.2%.
- A-705: 73.9 / 14.4 / 11.7%.

The MIX % is the product-blend ratio for the whole order and does not hold for each wall. So the fallback keeps the total exact (244.13 SF) but can miss a single tag by up to 8%. This is the estimator's convention: trace the drawn pattern. The mix % is a design intent and not the takeoff.

Independent pixel check on the A-410 vectors: dark tiles (WT-2) 44.9 SF (+2.5%), grey tiles (WT-9) 44.7 SF (−11.7%, because the WCs and lavs hide part of the grey band in the drawing), and white (WT-1) 126.0 SF (+4.4%, because it includes linework).

---

## F3. Tile line quantity (per tag, whole job)

**Rule**

`lineSF(tag) = Σ over sheets of tagSF(sheet)`

This sums F2 results, or the PlanSwift legend rows of the same tag across sheets.

**Worked examples**
- **235, WT-1:** 120.7 (A-410) + 15.3 (A-703) + 8.2 (A-705) = **144.20**. Estimate 144.19 (+0.01%).
- **236, WT-2:** 43.8 + 1.4 + 1.6 = **46.80**. Estimate 46.72 (+0.17%).
- **238, WT-9:** 50.6 + 1.3 + 1.3 = **53.20**. Estimate 53.22 (−0.04%).
- **237, WT-3:** 38.4 (A-700 only) = **38.40**. Estimate 38.42 (−0.05%).

The remaining differences come from the legend's 1-decimal display. The estimate carries PlanSwift's unrounded values.

---

## F4. Run × height (wall covering, FRP, any full-height or wainscot finish measured on plan)

**Inputs**
- `runLF` (ft): the finish-plan run along the finished wall face.
- `H` (ft): the finish height. Full height uses the RCP ceiling height. A wainscot uses the elevation or schedule height.

**Rule**

`SF = runLF × H − openings_in_band`

No opening fell inside these runs on this job.

**Worked examples**
- **239, WC-1:** 10.1 LF × 12'-0". The ceiling height of WEATHER VESTIBULE 100 is "12' - 0" A.F.F." on A-130. That gives **121.2 SF** against the estimate of 120.0 (+1.0%). The estimator's figure equals 10.0 × 12, so the run was rounded down or the quantity was overridden. It cannot be proven.
- **240, wall covering over PT-7:** 10.3 LF × 10'-0" (MEETING ROOM 105 ceiling "10' - 0" A.F.F.") = **103.0 SF**, an exact match.
- **241, FRP-1:** 4.0 LF × 4'-0" = **16.0 SF**, an exact match.

---

## F5. FRP run at a corner mop sink

**Inputs**
- Mop-sink basin size from the plumbing fixture schedule (P-101 "MOP SINK BASIN FIAT MSK-2424 24"X24"").
- The number of wet walls it touches. A-410 says "FRP PANEL @ MOP SINK, BOTH SIDES".

**Rule**

`runLF = walls_touched × basin_side`

`FRP SF = runLF × FRP height`

**Worked example**

2 × 2'-0" = 4.0 LF, and 4.0 × 4'-0" = **16.0 SF** (line 241).

Sheets, if you need them: one 4' × 8' panel (32 SF) covers both 2' × 4' pieces. Specification accessories for the order are 1 inside-corner molding (4 LF), a 4 LF cap, and division bars where panels join (0 here).

---

## F6. Assumed wall covering from a primer-only paint tag (judgment)

**Rule.** When the finish schedule defines a paint tag as a *wallcovering primer* and no WC tag is shown on that wall, carry `SF = runLF × H` of the paint tag's run as an "ASSUMED WALL COVERING, V.I.F." line at low confidence. The A-170 entry is PT-7 "PRIMER / SHIELDZ / UNIVERSAL WALLCOVERING / ROMAN PRO-999 ULTRA PRIME / COORDINATE w/ OWNER VENDOR".

**Basis.** This is the estimator's own convention, seen in line 240. The quantity is reproducible (103.0 SF). The scope is not, because it is inferred.

**A second PT-7 tag on this job.** A-150 also tags the Gathering Area 103 north wall with a stacked `PT-4 / PT-7` pair whose leaders run to both ends of the wall. The estimator measured that wall only as `PT4 @ 10'H` 10.6 FT, with no PT-7 run and no wall-covering run. Under this rule it implies a second assumed wall covering of up to 10.6 LF × 10'-0" (A-130 GATHERING AREA `10' - 0"A.F.F.`) = **106.0 SF, V.I.F.**, which the estimator did not carry. The extent is uncertain: the A-704 tech wall plan and details show only PT-4 and PT-6 on that wall. So flag it and do not carry it as a firm quantity. Line 240 is left at 103.0 SF.

---

## Conventions and ratios used

| Convention | Value | Basis |
|---|---|---|
| Fixtures, accessories and appliances in front of tile | not deducted | Every band on A-410, A-703 and A-705 rebuilds gross |
| Repeated room "similar to" | × count of rooms | A-410 note; legend = 2 × drawn elevations |
| Wall-finish height | in the legend item name ("@ 12'H", "@ 4'H") | This equals the RCP ceiling height or the elevation/schedule height |
| Waste | 0% in the estimate line | All 7 lines rebuild net |
| Attic stock | 10% required by spec 09 3000 p282, **not carried** | An extra quantity to add as its own line if the app models it |
