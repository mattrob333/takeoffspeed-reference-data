# 33 — Site utilities: reading guide

How to read this job's plans for storm, sanitary, services, structures and trenching. Every input
to `formulas.md` is listed with the exact string it is read from.

## 1. Sheets to open, in order

1. **C-4.0 Grading Plan** (markup p74). Lower right of the sheet holds two engineer tables:
   - **STORM PIPES**: columns NAME / SIZE / LENGTH / SLOPE / INV UP / INV DOWN / MATERIAL.
     Rows: `A1-A2 18" 17.69 0.50% … HDPE`, `A2-A2.1 18" 45.97`, `A2-A3 18" 92.25`,
     `A2.1-A2.2 18" 85.26`, `A3-A4 18" 70.17`, `B1-B2 15" 25.11`, `C1-C2 18" 21.08`.
   - **STORM STRUCTURES**: NAME / TYPE / STATION / RIM / INV IN / INV OUT. Rows:
     - `A1-STHW HEADWALL`;
     - `A2-STGI HOODED GRATE INLET`;
     - `A2.1-STYI YARD INLET`;
     - `A2.2-STGI`, `A3-STGI`, `A4-STGI` (hooded grate inlets);
     - `B1-STJB JUNCTION BOX`;
     - `B2-STOCS OUTLET CONTROL STRUCTURE`;
     - `C1-STJB JUNCTION BOX (EXISTING)`;
     - `C2-STGI HOODED GRATE INLET`.
   - **STRUCTURE TYPES** box: `STGI: GDOT STD 1019A TYPE E`, `STYI: NYOPLAST INLET W/DOME`,
     `STHW: GDOT STD 1001B HEADWALL`, `STOCS: SEE DETAILS SHEET C-6.2`.
   - Keynote 5: `8" HDPE HEADER PIPE FOR ROOF DRAIN CONNECTION, MINIMUM SLOPE OF 1%`.
2. **C-5.0 Utility Plan** (p77): **SANITARY PIPES** (`S1-S2 6" 49.92 1.00% … PVC` … `S7-S8 6"
   12.00`), **SANITARY STRUCTURES** (`S1-SSMH MANHOLE (EXISTING)`, `S2..S7-SSCO CLEANOUT`,
   `S8-SSBC BLDG CONNECTION`), and KEY NOTES 1–12:

   | Keynote | Text | Line |
   |---|---|---|
   | 1 | Gas service | 724 |
   | 2 | Existing-manhole connection | 737 |
   | 3 | Power | 727 |
   | 4 | Telephone | 728 |
   | 5 | 8"×8"×1" tapping saddle and corporation stop | 734 |
   | 6 | Bend water line for clearance | — |
   | 7 | Horizontal bends, 2 × 45° | — |
   | 8 | 1" PVC domestic water line | 726 |
   | 9 | 1" meter and RPZ | 735, 736 |
   | 10 | Irrigation meter reuse / replace | — |
   | 11 | Transformer pad | — |
   | 12 | Refer to arch plans | — |
3. **C-4.1 Storm Profiles** and **C-5.1 Sanitary Profiles**: rims and inverts again, plus
   whole-foot callouts (`70 LF OF 18" HDPE @ 0.50%`). Use them for depth only, never for length.
4. **C-6.2 / C-6.3** (raster details, no text layer; render them). City of Warner Robins
   standard details:
   - `SECTION - SANITARY SEWER BEDDING PVC PIPE`: width `O.D. + 18" MAX`, `4" MIN` crushed stone
     under the pipe, stone to `1/2 O.D.` above the crown, `MINIMUM PIPE COVER 3'-0" MINIMUM / 4'-0"`,
     `DETECTABLE MYLAR TAPE` 18" below finished grade, `12 GAUGE COPPER WIRE`.
   - `SECTION - DROP TIE-IN TO EXIST. MANHOLE`.
   - `DETAIL - CLEANOUT TO GRADE`: `RECESSED BRASS CLEANOUT PLUG`, `18"x18"x 8" CONCRETE PAD OR 18" SQUARE CONCRETE COLLAR IN ALL PAVED AREAS`,
     `4" DIA. MIN PIPE`.
   - Water bedding, tapping sleeve, meter, valve and tracer-wire details.
5. **C-0.1 General Notes**, utility and drainage notes:
   - `SANITARY SEWER PIPE … PVC PER ASTM D 3034`;
   - `MINIMUM TRENCH WIDTH SHALL BE 2 FEET`;
   - `MINIMUM OF 3'-0" COVER ON ALL WATERLINES`;
   - `HIGH DENSITY POLYETHYLENE, ADS N-12 ST IB PIPE (PER AASHTO M294)`;
   - `A MINIMUM GRADE OF 0.50% SHALL BE MAINTAINED ON ALL PIPES`;
   - `NO MORE THAN 500 LF OF TRENCH MAY BE OPENED AT ONE TIME`.
6. **E-010** (p42 and p87): keynote 2 `IRRIGATION BACKFLOW`.

## 2. How each input is read

| Input | Read from | This job |
|---|---|---|
| Storm LF by size | STORM PIPES LENGTH, grouped by SIZE | 18" = 332.42, 15" = 25.11 |
| Sanitary LF | SANITARY PIPES LENGTH | 295.96 (= last station 2+95.96) |
| Header, water, power, telephone, gas LF | Markup legend polyline on p74 / p77 | 168.2, 138.3, 72.9, 74.4, 156.4 FT |
| Headwall LF | p74 legend `A1-STHW: HEADWALL 8.8 FT` | whole feet → 9 (ceil and nearest agree) |
| Inlet / JB / OCS counts | STORM STRUCTURES TYPE column, skipping `(EXISTING)` | 5 / 1 yard / 1 / 1 |
| Cleanouts | SANITARY STRUCTURES TYPE = CLEANOUT | 6 |
| Appurtenances | C-5.0 keynote symbols 2, 5, 9 | 1 each; keynote 9 → 2 lines |
| Trench width | Estimator convention (no storm bedding detail; C-6.2 `O.D. + 18" MAX` is a sanitary-PVC maximum) | 3'-0" used; the detail by O.D. would give 21" + 18" = 3.25 ft for 18" N-12 |
| Trench depth | (RIM − INV) at both ends of every table row + 4" bedding, length-weighted | 5.01 ft → 5'-0" |
| Trench length | Σ drainage pipe lines (721+722+723+725), rounded | 822 LF |

## 3. Cross-checks

- **Station check.** The last structure's STATION equals the sum of the pipe lengths on that
  line: S8 at 2+95.96 = 295.96, and B2 at 0+25.11 = B1-B2.
  - Storm stations restart per branch (A, B, C), so check each branch separately.
  - Branch A is a tree, not a chain: A2-A2.1-A2.2 and A2-A3-A4 both start at A2.
- **Table vs. polyline.** Sanitary table 295.96 vs. polyline 295.8 (−0.05%). A difference over 1%
  means the polyline missed or added a run.
- **Structure count vs. table.** The legend says 5 STGI. The table has five rows typed HOODED GRATE
  INLET (A2, A2.2, A3, A4, C2). Do not count A1 (headwall) or C1 (existing JB) as inlets.
- **Profiles vs. table.** Every C-4.1 / C-5.1 callout rounds the table length to whole feet.
  Use the profiles only for rims and inverts.
- **Depth sanity.** Sanitary runs average 5.8–6.9 ft deep (rim-to-invert 5.4–6.7 ft at the
  cleanouts; above 5 ft: OSHA protective system). Storm runs average 2.4–4.3 ft deep. Both on the
  `formulas.md` §6 basis: (rim − invert) averaged at both ends of the run, plus 4" bedding. A single 5 ft section over-digs storm and under-digs sanitary, but nets out.
- **C-5.0 keynote 9** names two devices and becomes two estimate lines.

## 4. Traps hit on this job

1. **No storm pipe in the PlanSwift legend.** p74 has only the header, headwall and structure
   counts. Storm LF must come from the STORM PIPES table; an AI reading only legends will miss
   357.53 LF.
2. **Count dots sit on the tables.** The p74 dots for inlets, JB and OCS sit on the STORM
   STRUCTURES rows, not on the plan symbols. Use the table as the counting source.
3. **EXISTING rows.**
   - `C1-STJB JUNCTION BOX (EXISTING)` is not a new JB.
   - `S1-SSMH MANHOLE (EXISTING)` is not a new manhole; it is the core-and-grout connection (737).
   - C1-C2 is new 18" pipe into an existing structure, with invert out 424.75 (EX).
4. **Duplicate page.** p87 is a reduced reprint of E-010 (p42). The irrigation backflow was
   counted on both pages, giving 2 EA for one device. Dedupe by sheet and keynote.
5. **Gas 152 vs. 156.4.** The estimate is shorter than the only measurement. Flag it; do not copy it.
6. **"NO DETAILS" on the inlet line.** The estimate says the STGI has no details. C-4.0 names
   GDOT STD 1019A TYPE E and C-6.1 shows the GDOT inlet detail. The OCS points to C-6.2, but
   C-6.2 has no OCS; C-4.2 shows the riser. The JB/OCS 4'-0" diameter is an assumption.
7. **Water pipe material conflict.** C-5.0 says 1" PVC. Spec 22 1000 2.2A (p386) says Type K copper
   for service entrance piping 3" and smaller. The estimate follows the civil drawing. Raise an
   RFI (p14: the GC owns "a complete scope of work for all incoming utilities").
8. **Trench scope.** The trench lines cover only the four drainage pipes. The 1" water (3'-0" cover
   required) has no trench in this estimate. Check whether that was intended (utility-installed
   gas, power and telephone are reasonably excluded).
9. **No bedding stone line.** The C-6.2 detail requires crushed stone bedding (4" under, to ½ OD
   over). The estimate carries no bedding material; only the haul-off implies it.
10. **Spec index.** There is no Division 33 section. Do not wait for 33 30 00 / 33 40 00; the
    files `ufgs333000.txt` and `ufgs333400.txt` in the work folder are generic UFGS references,
    not this project.
11. **Legend spellings.** `WATERINE`, `DOMESTICRPZ`, and `A2-2-STGI` (for A2 / A2.2) are carried
    verbatim into estimate descriptions. Match on keynote number and size, not spelling.
