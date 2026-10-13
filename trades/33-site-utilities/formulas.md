# 33 — Site utilities: formulas

Every number below was computed with python. The scripts are in `trades/33-site-utilities/scripts/`:
`build.py` writes the reconciliation and fixtures, `depths.py` holds the depth basis, and
`trench_search.py` / `haul_search.py` hold the hypothesis searches. Units: LF, EA and CY (bank,
no swell).

---

## 1. Pipe LF from the engineer's pipe table (lines 721, 722, 723)

**Name:** `pipeLFFromTable`

**Inputs:**
- One row per pipe-table row: `size` (in), `material`, `length` (ft, the table LENGTH column, 2 dp).

**Rule:** `LF(size, material) = Σ length` over the rows of that size. Use no plan scaling and no
fitting or waste allowance. The table length is the station difference between structure
centres (centre-to-centre).

**Convention:** the estimator used the table, not a polyline. Storm pipe has no PlanSwift row at all.
Sanitary has one (295.8 FT), but the estimate carries the table total of 295.96.

**Worked example:**
- 18" HDPE: 17.69 + 45.97 + 92.25 + 85.26 + 70.17 + 21.08 = **332.42 LF** (line 722).
- 15" HDPE: B1-B2 = **25.11 LF** (line 721).
- 6" PVC: 49.92 + 92.03 + 14.14 + 90.70 + 14.14 + 23.03 + 12.00 = **295.96 LF** (line 723).
  This equals the S8-SSBC station 2+95.96.

**Cross-check:** the C-4.1 / C-5.1 profile callouts round each run to whole feet: 18, 46, 92, 85,
70, 21, 25 / 50, 92, 14, 91, 14, 23, 12. Do not use them; they lose up to 0.5 ft per run.

---

## 2. Pipe and route LF from a PlanSwift polyline (lines 724–728)

**Name:** `pipeLFMeasured`

**Inputs:**
- `legendLF` (ft) from the markup legend: the 2-dp PlanSwift value where it is available; the legend prints 1 dp.

**Rule:** `LF = Σ legendLF` for the item, with one route = one line. Service conduits are route LF,
not conduit LF (no "× number of conduits").

**Worked example:**

| Line | Item | Legend | Estimate |
|---|---|---|---|
| 725 | Header | 168.2 FT | 168.18 |
| 726 | Water | 138.3 | 138.27 |
| 727 | Power | 72.9 | 72.88 |
| 728 | Telephone | 74.4 | 74.43 |

All four agree to the printed decimal.

**Exception (line 724, gas):** the legend reads 156.4 FT and the estimate carries 152. On the
`reconciliation.csv` basis, (recomputed − estimate) / estimate, the legend is **+2.89%** over the
estimate (the same 4.4 LF gap is 2.81% of the legend). Unresolved. No sheet prints 152. Treat it as a manual override: the app should output
156.4 and flag the line.

---

## 3. Headwall LF (line 738)

**Name:** `headwallLF`

**Inputs:**
- `legendLF` (ft): the A1-STHW polyline, 8.8 FT.

**Rule:** `LF = legendLF` rounded to whole feet. **Convention:** the estimator carries this small
concrete item in whole feet. Ceil and round-to-nearest are indistinguishable on this job
(ceil(8.8) = round(8.8) = 9; a sample such as 8.2 would separate them), so the direction is
unverified. The fixture input is `roundTo`, not `roundUpTo`.

**Worked example:** 8.8 → **9 LF**. That is +2.27% over the raw polyline, and exact to the estimate.

Only one headwall exists (A1-STHW, GDOT STD 1001B). The estimate carries it in LF, not EA.

---

## 4. Structure and appurtenance counts (lines 729–737)

**Name:** `structureCount`

**Inputs:**
- Structure-table rows with `name`, `type`, and an EXISTING flag; or legend dot counts per keynote.

**Rule:**
- `EA(type) = count(rows where TYPE = type and not EXISTING)`.
- An EXISTING manhole that receives the new pipe becomes **one connection line** (737), not a structure.
- A keynote that names two devices (keynote 9: meter AND RPZ) becomes **two lines** of 1 EA each (735, 736).

**Worked example:**

| Type | Rows | Count | Line |
|---|---|---|---|
| STGI hooded grate inlet | A2, A2.2, A3, A4, C2 | 5 | 730 |
| STYI yard inlet | A2.1 | 1 | 731 |
| STJB junction box | B1 (C1 is EXISTING, excluded) | 1 | 732 |
| STOCS outlet control structure | B2 | 1 | 733 |
| SSCO cleanout | S2, S3, S4, S5, S6, S7 | 6 | 729 |
| S1-SSMH (EXISTING) | — | 1 connection | 737 |
| SSBC (S8) building connection | — | none | not a line |

Keynote counts: keynote 5 → 1 tapping saddle (734); keynote 9 → 1 meter (735) + 1 RPZ (736).

The structure **size** is not counted. The estimator writes "4'-0" DIA … NO DETAILS SO ASSUMED"
for the JB and OCS; that is a description, not a quantity.

---

## 5. Cross-page count (line 739)

**Name:** `countAcrossPages`

**Inputs:**
- `pageCounts` (EA): one value per markup page that shows the item.

**Rule as the estimator applied it:** `EA = Σ pageCounts`. That gives 1 (p42, E-010) + 1 (p87,
E-010 reprint) = **2 EA**.

**Correct rule:** dedupe by sheet and location. Both dots sit on the single keynote-2 device, so the
physical count is **1**. The electrical trade (26) dedupes the same page pair for every other
device; only this line was doubled. The fixture keeps 2 so it reproduces the estimate, and the
app should warn.

---

## 6. Pipe trench excavation (line 740)

**Name:** `trenchExcavationCY`

**Inputs:**

| Input | Value | Basis |
|---|---|---|
| `runs` (ft) | 25.11 (15" storm), 332.42 (18" storm), 295.96 (6" sanitary), 168.18 (8" header) | Lines 721, 722, 723, 725 |
| `W` (ft) | 3.0 | Trench width |
| `D` (ft) | 5.0 | Trench depth |

**Rule:** `CY = round(Σ runs, 0) × W × D / 27`.

**Conventions and their basis:**
- **Which runs:** only the four drainage pipes this contractor installs. Gas, water, power and
  telephone are not trenched in this line: they are utility-coordinated services, and water is a
  shallow 1" line.
- **W = 3'-0"**: an estimator convention, not a detail value. The estimator used one 3' × 5'
  section for all four pipes. The only bedding detail, C-6.2 `SECTION - SANITARY SEWER BEDDING PVC
  PIPE`, is a City sanitary-PVC standard and states a maximum (`O.D. + 18" MAX`). By O.D. it would
  give 21" + 18" = 39" = 3.25 ft for the 18" N-12 HDPE run (ADS N-12 18" O.D. 21", engine
  `OD_TABLES.hdpe`; reading nominal 18" as the O.D. is what makes 36" = 3.0 ft) and about 2.0 ft
  for the 6" PVC sanitary (6.275" + 18"). The storm runs have no bedding detail at all (C-0.1
  drainage type 3 only says install per ASTM D2321).
- **D = 5'-0"**: one average depth for the whole job. From the C-4.0 and C-5.0 structure
  tables, (rim − invert) averaged at both ends of each of the 14 storm and sanitary rows, plus 4"
  bedding, length-weighted, gives **5.01 ft**:
  - storm alone: 3.80 ft;
  - sanitary alone: 6.46 ft.
- **Rounding:** Σ runs = 821.67 LF, rounded to 822 LF (ceil and nearest both give 822). Without
  rounding the result is 456.48 CY (−0.04%).

**Worked example:** 822 × 3 × 5 = 12,330 CF ÷ 27 = **456.666667 CY**, exact to the estimate.

**Uniqueness:** a brute-force search over all subsets of the run lengths and rectangular sections
(`trench_search.py`) found other exact fits, for example 1,233 LF × 10 SF. On the natural run set
(the four gravity and drainage pipes) the data fix only the section **area**, 15 SF/LF:
3' × 5', 2.5' × 6' and 2' × 7.5' all give 456.666667 CY. 3' × 5' is preferred because 5.0 ft
matches the measured 5.01 ft average depth, but the width is assumed, so this line is
**reproduced by construction (section inferred)**, not grounded. `reconciliation.csv` classifies
it `derived (section inferred)`.

---

## 7. Pipe trench backfill (line 741)

**Name:** `trenchBackfillCY`

**Inputs:**
- `excavationCY` (line 740).
- `haulCY` (line 742).

**Rule:** `backfill CY = excavation CY − haul CY`. This is the same convention as the footing
earthwork (trade 31, lines 629–631): backfill is the hole minus what goes into it. No compaction
or shrink factor is applied.

**Worked example:** 456.666667 − 42 = **414.666667 CY**, exact. It is exact **by construction**:
it subtracts the unexplained 42 CY allowance (§8) from the inferred §6 section, so it is not
independently grounded. `reconciliation.csv` classifies it `derived from allowance`.

---

## 8. Pipe trench haul-off (line 742): allowance

**Name:** `trenchHaulCY` (allowance)

**Observed:** 42 CY = 1,134 CF. It is a whole number of CY, while 740 and 741 are thirds of a CY.
That means it was typed, not computed from the same section. Ratio to excavation = 42 /
456.67 = **9.20%**.

**What it should represent** (the estimator's convention elsewhere): the volume of what goes into
the trench, i.e. pipe plus imported bedding.

| Candidate (four drainage runs) | CY | Matches 42? |
|---|---|---|
| Nominal pipe volume π/4·D²·L | 27.22 | no |
| Outside-diameter pipe volume (N-12 / D3034 ODs) | 36.6 | no |
| Pipe + 4" bedding × 3' wide (C-6.2 minimum bedding) | 57.66 | no |
| Pipe + 2" × 3' (or 3" × 2') bedding, rounded | 42.44 → 42 | fits, but no drawing basis |
| GPT-6 Astra second opinion | — | Agreed no grounded formula gives 1,134 CF uniquely |

**App rule:** keep a `trenchHaulCY` input or allowance. Default it to pipe + bedding displacement
from the bedding detail. Do not fit to 42.

---

## Formula count

Eight formulas, numbered 1–8 above. The C-4.0 and C-5.0 tables, read as data, supply every input
except the markup legend lengths and E-010 counts.
