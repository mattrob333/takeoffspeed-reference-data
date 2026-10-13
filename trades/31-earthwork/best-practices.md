# Earthwork (excavation, backfill, haul, grading cut/fill): takeoff best practice

Scope: quantities and material types only.
Written 2026-10-13 for the single-storey bank branch in this repository (Fifth Third Bank - Watson, Warner Robins GA).

## Evidence labels (read this first)

Page numbers for `geotech.txt` and `civil.txt` are PDF page numbers of the extracted text under `trades/31-earthwork/scripts/research/earthwork/`.

The web-search budget for this session was exhausted after the first query batch, so no handbook or trade-association page could be searched for. Every claim below carries one of three labels.

- **[WEB]** fetched and read this session; the link is the source.
- **[PROJECT]** read in this repository's drawings, geotechnical report, specifications or estimate. Paths are relative to `` unless absolute.
- **[GPT, unverified]** a second opinion from GPT-6 Astra (`tools/ask_gpt.py`, transcript `trades/31-earthwork/scripts/research/earthwork/gpt1.txt`). It named publications but nothing it cited was opened here. Treat as a lead to verify, not as a source. Its swell and shrink ranges are explicitly "not confident" in its own words.

Things I could not source (RSMeans, Caterpillar Performance Handbook, FM 5-434 tables, a state DOT measurement clause) are listed in section 12 as open items rather than asserted.

---

## 1. What the estimator takes off, and in what units

| Item | Unit | Basis |
|---|---|---|
| Clearing, grubbing, topsoil strip | SF of area, converted to CY by depth | UFGS strips to a stated depth, 4 in default, within the limits of disturbance [WEB: [UFGS 31 00 00 3.3.2](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2031%2000%2000.pdf)] |
| Mass cut and fill (building pad, drives, parking, swales, basin) | CY, cut and fill kept separate | Estimate lines 639 to 641 [PROJECT: `reference/estimate/lines.json`] |
| Building pad subgrade preparation, proofroll, scarify and recompact | SF | Geotech: scarify at least 10 in, proofroll with a loaded tandem-axle truck [PROJECT: `trades/31-earthwork/scripts/research/earthwork/geotech.txt` p.10] |
| Undercut and replacement of unsuitable soil | CY, as an allowance until directed | UFGS: remove unstable material to the depth directed [WEB: [UFGS 3.4.2.3](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2031%2000%2000.pdf)] |
| Footing, pier and stem-wall excavation | CY | Estimate line 629 [PROJECT] |
| Backfill around footings and stem walls | CY | Estimate line 630 [PROJECT] |
| Utility trench excavation, bedding, initial and final backfill | LF and CY per run | Div 22 and 23 spec text and civil notes [PROJECT: `text/spec-p377.txt`, `civil.txt`] |
| Haul-off of surplus, import of shortfall | CY, stated basis (bank or loose) | Estimate lines 631 and 641 [PROJECT] |
| Under-slab granular capillary break and base courses | SF at stated thickness, then CY or tons | Geotech: at least 4 in free-draining granular [PROJECT: `geotech.txt`, floor slab recommendation 3]. Pavement sections are the paving trade, not this one |
| Topsoil import and spreading | SF at stated thickness | Civil note: 4 in of topsoil on all unsurfaced disturbed areas [PROJECT: C-0.1 general notes, `civil.txt` p.2] |

Unit discipline: 1 CY = 27 CF. Keep **bank (BCY)**, **loose (LCY)** and **compacted (CCY)** labelled on every line. Mixing them is the commonest source of error (section 9).

## 2. Sheets and spec sections that drive it

For this job (indexed in `reference/sheets/index.json`):

- **C-4.0 Grading Plan**: 1 ft contour interval, FFE 441.00, spot grades, storm structures, no printed earthwork table. The cut and fill therefore have to be computed from contours or spot grades [PROJECT: rendered `trades/31-earthwork/scripts/research/earthwork/c40.png`; text search of `civil.txt` found no table]. Note 2 on the sheet: no slopes steeper than 2:1.
- **C-0.1 General Notes** and civil grading notes: cut and fill slopes 2:1 or flatter, 4 in topsoil on disturbed unsurfaced areas, stabilization fabric on slopes 3H:1V or steeper, all fill in place and compacted before utilities, fill and unsuitable-soil removal per the geotechnical report [PROJECT: `civil.txt` p.2].
- **C-1.0 Demolition** (existing pavement and slabs that come out before grading), **C-4.1 Storm Profiles**, **C-4.2 Infiltration Basin Detail** (stone bed, no compaction of the subsurface stone storage bed, hand tools or light equipment only [PROJECT: `civil.txt` p.14]), **C-5.0/C-5.1 Utility and Sanitary Profiles** (trench depth from rim and invert), **C-6.x Details** (compact subgrade to 98% standard Proctor under sidewalk and curb [PROJECT: `civil.txt` p.17]).
- **S-001 Foundation Notes**: bearing 3,000 psf verified at excavation, footing elevations adjustable to soil conditions, wall footings 12 in thick with 6 in spread each side of the masonry wall [PROJECT: `text/S-001.txt` lines 108-121].
- **S-201 Foundation Plan**: top of interior and exterior footing 2'-0" below finish floor unless noted, footing marks and elevations, maximum earth differential when backfilling 2'-0" [PROJECT: `text/S-201.txt`]. **S-600 and S-680** give the footing, stem-wall and step details.
- **Terracon geotechnical report** (63 pp.): the earthwork rules for this site. It governs excavation, fill material classes, lifts, compaction, reuse of existing fill, groundwater [PROJECT: `geotech.txt` pp.13-18].
- **Specification**: the project manual has **no** Division 31 earthwork section; only 313116 Termite Control [PROJECT: `reference/sheets/spec_index.json`]. Earthwork criteria are carried by the civil notes, the geotechnical report, and trade sections: 22 and 23 trench and backfill text (hand-fill 12 in above pipe, 95% Proctor, no water settling [PROJECT: `spec-p377.txt`]); a general clause that excavations deeper than 5 ft have back slopes no steeper than 1V:1.5H unless sheeted and braced [PROJECT: `spec-p058.txt` lines 86-89]; 017419 Construction Waste Management for disposal. An AI must therefore not wait for a 31 23 00 section to appear.
- **Geotechnical-report reference in the drawings**: S-001 note 1 and the civil notes both send the reader to Terracon Project 49265099, dated May 4, 2026. Treat the report as a contract-governing document for this trade.

Industry equivalent: the reference federal guide specification for Division 31 earthwork is [UFGS 31 00 00](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2031%2000%2000.pdf) [WEB]. It shows what a conforming section defines: structural fill, embankment fill, porous fill, topsoil, bedding, satisfactory and unsatisfactory material, rock, overhaul, borrow and subgrade (section 1.2).

## 3. Volume states and conversions

- Cut is measured in the ground (bank). Fill is measured as placed and compacted. Trucks carry loose material.
- Conversions, with s as swell and h as shrink in decimals [GPT, unverified; the algebra is exact, the percentages are not sourced]: LCY = BCY x (1 + s); CCY = BCY x (1 - h); BCY = CCY / (1 - h). Example: 100 BCY at 25% swell is 125 LCY, and at 10% shrink is 90 CCY.
- **Compaction percentage is not volumetric shrinkage.** "95% of maximum dry density" is a density ratio from the laboratory test [GPT, unverified]. The Proctor tests themselves: standard effort ASTM D698 (3 lifts, 5.5 lb hammer, 12 in drop, about 12,375 ft-lbf/ft3) and modified effort ASTM D1557 (5 lifts, 10 lb hammer, 18 in drop, about 56,250 ft-lbf/ft3) [WEB: [Proctor compaction test](https://en.wikipedia.org/wiki/Proctor_compaction_test)]. UFGS defines degree of compaction as a percentage of the maximum dry density from the named test (section 1.2.16) [WEB].
- Shrink and swell numbers must come from the geotechnical report when it gives them. Terracon gives none: only compaction percentages (see section 6). So any shrink figure on this job is an estimator convention and must be labelled as one. Planning ranges quoted by GPT-6 for orientation only [GPT, unverified, "not confident enough to attribute to a verified table"]: swell sand 10-15%, common earth 20-30%, clay 30-50%; shrink sand 0-10%, common earth and clay 10-20%.

## 4. Measurement methods for mass cut and fill

- **Grid or borrow-pit method**: divide the area into cells, take existing and proposed elevations at corners, volume per cell is average depth x cell area. Good for wide, regular sites. Misses features smaller than the cell [GPT, unverified].
- **Average end area**: V = L x (A1 + A2) / 54 CY with L in ft and A in SF [GPT, unverified; the 54 is 2 x 27]. Suited to linear work (roads, trenches, swales).
- **Prismoidal**: V = h (A1 + 4 Am + A2) / 6 where Am is the true mid-section area, not the mean of the ends [WEB: [Prismatoid](https://en.wikipedia.org/wiki/Prismatoid)]. Convert to CY by dividing by 27.
- **TIN or surface-to-surface model** (what CAD packages do): triangular-prism volumes between surfaces; the Wikipedia overview notes grid, cross-section and TIN methods can give different results from the same data [WEB: [Earthworks (engineering)](https://en.wikipedia.org/wiki/Earthworks_(engineering))].
- No method has a universal accuracy ranking; it depends on survey quality, spacing and terrain [GPT, unverified]. Practical rule: use two methods or two grid spacings and reconcile; if they disagree by more than the net balance, the balance is not trustworthy.
- Excavation and fill must balance with haul in mind: haul effort follows quantity x distance, and balance points matter [WEB: [Earthworks (engineering)](https://en.wikipedia.org/wiki/Earthworks_(engineering))]. UFGS defines overhaul as quantity hauled beyond the free-haul limit times the distance beyond it (section 1.2.18) [WEB].

### 4.1 Cut and fill slope limits as they affect the model

Civil notes cap cut and fill slopes at 2:1 or flatter [PROJECT]. The grading model must carry the daylight lines (the 2:1 slopes from pad edge to existing grade) or the volumes at the perimeter are wrong. Stabilization fabric applies to slopes 3H:1V or steeper [PROJECT].

## 5. Footing, pier and trench excavation

### 5.1 Geometry

Excavation volume per footing = (footing length + 2w) x (footing width + 2w) x depth / 27, where w is the working space each side. For a continuous footing, L x (W + 2w) x D / 27, with sloped ends handled separately. For symmetric side slopes of mH:1V, CY = L x D x (b + mD) / 27 where b is the bottom width [GPT, unverified, algebra standard].

- **Depth** for this job: top of footing is 2'-0" below finish floor and the wall footing is 12 in thick (S-001 note 2, S-201 note) so footing bottom is 3'-0" below FFE 441.00 before steps and before the 4 in slab and gravel are considered [PROJECT: `S-001.txt`, `S-201.txt`, `c40.png`]. Footing steps (maximum 2'-0" vertical, not closer than 4'-0" o.c.) change the depth along the run [PROJECT: `S-001.txt` line 121].
- **Working space**: there is no universal dimension. 1 ft each side is a common stated assumption and must be labelled as one; earth-formed footings need none, formed footings, waterproofing and shoring need more [GPT, unverified]. The TakeoffSpeed engine uses 1 ft [PROJECT: `TakeoffSpeed repo: lib/quantities/trades/site/earthwork.ts` convention `earthwork.footing-working-space-ft`].
- **Over-excavation**: measure the specified limits and list any contingency separately; there is no standard percentage [GPT, unverified]. UFGS forbids excavating below indicated depths except to remove unstable material, and requires excessive excavation to be backfilled with compacted satisfactory material (3.4, 3.4.1) [WEB].

### 5.2 Side slopes and protective systems (OSHA)

Protection is required unless the excavation is in stable rock or is under 5 ft deep with no sign of cave-in potential [WEB: [1926.652](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.652)]. The default option is a slope no steeper than 1.5H:1V (34 degrees); other options use Appendix A and B or an engineer's design (same source).

Maximum allowable slopes for excavations under 20 ft deep [WEB: [Appendix B](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926SubpartPAppB)]:

| Soil or rock | Max slope (H:V) | Angle |
|---|---|---|
| Stable rock | vertical | 90 deg |
| Type A | 3/4:1 | 53 deg |
| Type A, short term (open 24 h or less, 12 ft or less deep) | 1/2:1 | 63 deg |
| Type B | 1:1 | 45 deg |
| Type C | 1 1/2:1 | 34 deg |

Soil classes: Type A is cohesive soil at 1.5 tsf or more; Type B is 0.5 to 1.5 tsf, angular gravel, silt, silt loam, sandy loam, and previously disturbed soil unless Type C; Type C is cohesive soil at 0.5 tsf or less, gravel, sand, loamy sand, submerged or freely seeping soil [WEB: [Appendix A](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926SubpartPAppA)]. Previously disturbed soil is Type B at best, which matters here because the Terracon borings found existing fill to about 3 ft [PROJECT: `geotech.txt` p.14].

Other layout facts from [1926.651](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.651) [WEB]: spoil and equipment kept at least 2 ft from the excavation edge; trenches 4 ft or deeper need a means of exit within 25 ft of lateral travel; utility owners are contacted before digging.

These slopes are safety limits and should not be added automatically to a takeoff. They matter when the excavation is deeper than 5 ft (the 1V:1.5H clause in the spec at p.58 [PROJECT]) or when the soil is Type C. On this job the footing excavations are shallow (about 3 ft) so they will normally be cut vertical or near vertical; the quantity that drives the estimate is the working space, not slope.

The geotechnical report also bars trench excavation below a downward 1:1 projection from existing foundations without engineering review [PROJECT: `geotech.txt` p.17].

### 5.3 Utility trenches

- Width: UFGS limits trench width to pipe OD plus 24 in for pipe under 24 in diameter, and OD plus 36 in for larger pipe, with 12 to 24 in plus OD typical for small pipe (3.4.2 and its note) [WEB: [UFGS](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2031%2000%2000.pdf)].
- Excavation for manholes, catch basins and inlets leaves at least 12 in clear between structure and excavation face, or whatever forming requires (3.4.2.4) [WEB].
- Depth: pipe invert from the profile sheets (C-4.1, C-5.1) plus bedding thickness plus pipe wall, down from existing or finished grade, whichever is lower for cover (3.4.2.6) [WEB].
- Backfill zones: bedding, initial backfill to 1 ft above the pipe (hand-operated tampers for the first lifts), then final backfill [WEB: UFGS section 3.6.1 initial backfill paragraph; PROJECT: Terracon p.17 allows on-site soil from 1 ft above the pipe to the surface].
- Subtract the pipe volume from backfill (pi x (OD/2)^2 x L); the pipe is a permanent displacement [GPT, unverified, standard practice].

## 6. Fill, backfill and compaction requirements (drives lift count and material class)

From the Terracon report for this site [PROJECT: `geotech.txt` pp.15-17]:

- Structural fill is used below or within 10 ft of structures, pavements or constructed slopes; general fill elsewhere.
- Acceptable structural fill: CL and ML with LL under 45 and PI under 25; or SP, SM, SC, SW with under 50% passing the No. 200 sieve; maximum dry density at least 95 pcf by standard Proctor ASTM D698. Off-site fill sources must be tested before delivery.
- Lifts: 8 in or less loose with heavy self-propelled equipment; 4 to 6 in loose with hand-guided equipment.
- Compaction: 98% of maximum dry density within 1 ft of slab or pavement subgrade; 95% below foundations and more than 1 ft below slab or pavement subgrade; general fill 92%. Moisture -2% to +3% of optimum.
- Scarify exposed areas that will receive fill to at least 10 in; strip all topsoil in building and parking/drive areas; existing fill (about 3 ft deep at five of eight borings) may be reused if it is free of organics and debris and Terracon approves; undercut soft areas found by proofrolling.
- Under-slab capillary break: at least 4 in of free-draining, compacted granular material.
- Groundwater was not encountered; dewatering is not expected.

UFGS parallels, for orientation [WEB: [UFGS 3.6.2](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2031%2000%2000.pdf)]: structural fill in 8 in loose layers (4 in with hand-operated equipment), compacted to 90% (cohesive) or 95% (cohesionless) of laboratory maximum dry density; do not place backfill against foundation walls within 7 days of wall completion; heavy compaction equipment kept back from walls by a distance equal to the backfill height above the footing; granular maximum particle size not more than half the lift thickness (1.2.7 note).

Lift thickness converts to **number of lifts** only for sequencing and testing. For material quantity it does not matter. Do not use lift count as a quantity driver.

## 7. Coverage, yield and waste factors

| Factor | Value | Basis |
|---|---|---|
| CY per 1,000 SF at depth d | d(in) x 1000 / 12 / 27 | arithmetic. 4 in topsoil gives 12.35 CY per 1,000 SF (computed in Python) |
| Topsoil strip depth | 4 in default; the geotechnical report and drawings state the site value | [WEB: UFGS 3.3.2](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2031%2000%2000.pdf); [PROJECT] 4 in respread note |
| Swell | from soil or geotechnical data; sand 10-15%, common earth 20-30%, clay 30-50% as planning ranges only | [GPT, unverified] |
| Shrink, bank to compacted | not in Terracon report; convention only | [PROJECT] absence; ranges [GPT, unverified] |
| Waste on imported select fill | an estimator choice; the engine applies 0 waste because compaction is shrink, not waste | [PROJECT: `earthwork.ts` wasteClasses] |
| Truck capacity | loose CY, so haul quantity is bank x (1 + swell) | [GPT, unverified] |

Physical waste and allowance are different things. Spillage and trim on imported stone or select fill is waste; shrink and swell are volume-state conversions and must not be double-counted with waste.

## 8. Material breakdown the estimator lists

Primary items:

1. Cut (excavation) in BCY, split by purpose: mass grading, footings and piers, trenches, basin, topsoil strip.
2. Fill in CCY, split by structural fill versus general fill (different compaction and test frequency), then structural fill under slab and pavement.
3. Imported fill or borrow in BCY or LCY as ordered, when fill exceeds reusable cut.
4. Surplus haul-off, stated as bank or loose.
5. Topsoil: stripped and stockpiled, then respread at stated thickness; imported topsoil if short.
6. Free-draining granular capillary break under slab, 4 in minimum on this job [PROJECT: Terracon].

Accessories and components that follow:

- Subgrade proofrolling and scarify-and-recompact area (SF).
- Undercut and replacement allowance (CY), pending Terracon direction.
- Bedding stone and initial backfill for utility runs (CY per run).
- Geotextile or stabilization fabric: separation geotextile under subbase [PROJECT: estimate lines 632-633], stabilization fabric on slopes 3H:1V or steeper [PROJECT: civil note], 6 oz/SY non-woven geotextile and clean open-graded stone in the infiltration basin [PROJECT: `civil.txt` p.14].
- Compaction and density testing (counts) and Terracon observation, since S-003 lists special inspections for fill [PROJECT: `S-003.txt` lines 273-278].
- Dewatering, shoring and trench boxes: allowances only if conditions call for them. None are indicated here.
- Utility locating before digging [WEB: [1926.651](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.651)].

## 9. Common mistakes and how to check a takeoff

1. **Mixing volume states.** Cut in BCY, fill in CCY, trucks in LCY. Check that every line carries a state label and that import is computed as fill / (1 - shrink) - cut when shrink applies (the engine does this and also prints the plain balance) [PROJECT: `earthwork.ts` balanceLines].
2. **Netting cut against fill before converting**, which hides the shrink effect [GPT, unverified].
3. **Treating density percentage as shrinkage.** 95% compaction is not 5% shrink [GPT, unverified].
4. **Forgetting permanent displacement.** Backfill = excavation minus the footing, pier and stem-wall concrete (and pipes) below grade. Verified on this job (section 10).
5. **Omitting working space** around formed footings, or adding it twice (once in the excavation and again as extra backfill).
6. **Double counting** topsoil stripping inside the cut volume, and the footing excavation inside the mass cut.
7. **Ignoring slab and pavement buildup.** Contours on C-4.0 for drives, lots and sidewalks are finished elevations including pavement [PROJECT: `civil.txt` p.2]. Subgrade is lower by the pavement section thickness. Cut and fill computed straight from finished contours understates cut and overstates fill in paved areas unless the section is deducted.
8. **Missing existing fill and unsuitable soil** reported by borings (about 3 ft at five of eight borings here) [PROJECT: `geotech.txt` p.14].
9. **Reading ranges the wrong way**: footing elevations "may be adjusted at time of excavation" (S-001 note 1), so footing depth is a design value to be confirmed [PROJECT].
10. **Ignoring the 5 ft rule**: any excavation deeper than 5 ft requires either 1V:1.5H back slope or sheeting and bracing [PROJECT: `spec-p058.txt`; WEB: [1926.652](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.652)].

Checks:

- Two methods (grid at two spacings, or grid plus section) agree within the net balance.
- Excavation minus backfill equals permanent below-grade volume (footing and stem concrete from the concrete trade).
- Plain balance (fill - cut) is shown beside any shrink-adjusted import.
- Strip volume equals area x depth and appears once.
- Footing excavation depth ties to S-201 elevations and the S-600 and S-680 details.
- Trench quantities tie to profile sheets and utility lengths.

## 10. Reference job: what the estimator actually did, and how it compares

Ground truth (estimate lines 629-631 and 639-641, `reference/estimate/lines.json`; quantities only):

| Line | Description | Qty | Sheet |
|---|---|---|---|
| 629 | Excavation provided for footing | 119.8 CY | S201 |
| 630 | Backfill provided for footing | 83.7 CY | S201 |
| 631 | Hauling off extra material | 36.1 CY | S201 |
| 639 | Cut required for grading | 634.41 CY | C-4.0 |
| 640 | Fill required for grading | 786.25 CY | (C-4.0) |
| 641 | Net fill | 151.84 CY | (C-4.0) |

Python-checked relationships (recomputed this session):

- Haul-off 36.1 = excavation 119.8 - backfill 83.7 (36.1 exactly).
- That 36.1 also equals the footing and stem-wall concrete in the concrete lines 19-28: footings 25.93 CY + stem walls 10.15 CY = 36.08 CY. So the estimator hauled off exactly the volume the concrete displaces, in bank measure, with **no swell applied** to the haul quantity.
- Net fill 151.84 = 786.25 - 634.41 exactly: a **plain volumetric balance with no shrink factor**. With 10% shrink the import would be 239.2 CY and with 15% it would be 290.6 CY; the estimator carried neither. The Terracon report gives no shrink value, which is consistent with that choice.
- The footing excavation volume 119.8 CY is not reconstructable from the legend alone. The depth (3 ft to the bottom of a 12 in footing 2 ft below FFE), the 1 ft working-space convention and footing counts are the inputs; I did not reverse-engineer them and make no claim.
- C-4.0 prints no cut and fill table, so 634.41 and 786.25 were produced by the estimator's own surface comparison; the method is not recorded in the files.

Compared with the TakeoffSpeed engine (read-only, `lib/quantities/trades/site/earthwork.ts`):

- The engine defaults to 15% shrink when no geotechnical value is given and 25% swell for haul order, both capped at medium confidence with a warning, and always prints the plain balance as a step. The ground truth shows the estimator's printed quantities use the plain balance and bank volume for haul-off. The two figures should both appear and be labelled; the plain figure matches the ground truth.
- The engine's footing working-space default is 1 ft per side, labelled a convention.
- The engine's published basis for shrink and swell cites the Caterpillar Performance Handbook and NAVFAC DM-7. I could not open either source here, so those citations remain unverified by this research pass.

## 11. What an AI takeoff must read from the drawings and specs

1. **Existing and proposed contours** (C-4.0 and the survey): contour interval 1 ft; finished versus subgrade elevations; the pavement section depth to convert finished contours to subgrade.
2. **Limits of disturbance and limits of clearing** (C-2.x, C-4.0): stripping area, daylight lines, slope ratio notes (2:1 or flatter, 3:1 key note).
3. **Finish floor and slab buildup** (S-201, S-001, A-sheets): FFE 441.00, 4 in slab, 4 in gravel, vapor barrier. The building pad subgrade elevation is FFE minus slab and base.
4. **Footing schedule and details** (S-201, S-600, S-680): sizes, counts, top-of-footing elevations, steps, stem-wall heights. Also whether footings are earth-formed.
5. **Geotechnical report**: existing fill depth, strip requirements, fill classes, lifts, compaction, reuse of on-site soil, groundwater, bearing stratum, slope and trench restrictions, any shrink figure (none here).
6. **Civil notes**: topsoil depth, slope limits, utilities in place after fill, who removes unsuitable soil.
7. **Utility profiles and details** (C-4.1, C-5.1, C-6.x): pipe lengths, inverts, OD, bedding detail, structure sizes.
8. **Basin and BMP details** (C-4.2): excavation to the stone bottom elevation, stone bed volume, no-compaction rule.
9. **Specification sections 22 and 23 trench text and 01 74 19 waste**: backfill zones and compaction percentages, disposal.
10. **Missing-data flags**: no Division 31 section, no earthwork table on C-4.0, no shrink or swell factor, no stated working space. An AI should report each as an open assumption with the convention it used, never as a document value.

Rules from the repository's own instructions that apply: no invented data, and a missing value is shown as unknown instead of zero [PROJECT: `TakeoffSpeed repo: CLAUDE.md`, rule 1].

## 12. Open items (not verified this session)

- RSMeans earthwork takeoff conventions, Caterpillar Performance Handbook swell and load-factor tables, US Army FM 5-434 (the one GPT named), NAVFAC DM-7, a state DOT measurement-and-payment clause (for bank versus compacted measurement and overbreak), NRCS Engineering Field Handbook quantity chapter. Guessed URLs for several of these returned 403, 404 or unreadable content; a follow-up session with search budget should pull the actual tables.
- Typical estimator working-space allowances beyond the single "1 ft each side" convention.
- Any published accuracy comparison between grid, end-area and TIN methods.

## Source list

- [UFGS 31 00 00 Earthwork (USACE/NAVFAC/AFCEC, Aug 2023)](https://www.wbdg.org/FFC/DOD/UFGS/UFGS%2031%2000%2000.pdf), read in full text this session.
- [29 CFR 1926.651](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.651), [1926.652](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.652), [Appendix A](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926SubpartPAppA), [Appendix B](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926SubpartPAppB), [Subpart P index](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926SubpartP).
- [Prismatoid (prismoidal formula)](https://en.wikipedia.org/wiki/Prismatoid), [Proctor compaction test](https://en.wikipedia.org/wiki/Proctor_compaction_test), [Earthworks (engineering)](https://en.wikipedia.org/wiki/Earthworks_(engineering)).
- Project documents: Terracon Geotechnical Engineering Report 49265099 (May 4, 2026), civil sheets C-0.1, C-4.0, C-4.2, C-6.x, structural S-001, S-003, S-201, specification pages 58, 377, 405, and `reference/estimate/lines.json`.
- Second opinion, unverified: GPT-6 Astra transcript at `trades/31-earthwork/scripts/research/earthwork/gpt1.txt`.
