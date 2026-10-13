# TakeoffSpeed reference data

A worked reference for building an AI takeoff that reads plans and specs the way
a professional estimator does and produces **material types and quantities**.
Prices, labor and markups are deliberately out of scope here: the estimator's
workbook carries them, and this repository strips them out. Cost comes later,
from the contractor.

One real commercial job is the ground truth: the full drawing set, the project
manual, the estimator's PlanSwift markups of the drawings (what they measured,
sheet by sheet), and their estimate (what they took off).

> **Confidentiality.** `source/` holds a client's construction documents and a
> bid estimate. Keep this repository private.

## Results

Each of the 24 trade folders rebuilt every estimate line in its trade from the estimator's
markups, the drawings and the specs. A second model then checked the folder adversarially.
The table below is computed from each folder's `reconciliation.csv` and `fixtures.json`.

- **Delta** is (recomputed − estimator) / estimator.
- **No delta** means no recomputed value exists: an allowance with no rule, a fitted factor, or a
  hand-typed `NAN` row.
- **Classes** use the first-named class in the `classification` field.

| Trade | Lines | Within 1% | Within 5% | No delta | Measured | Counted | Derived | Specified | Allowance / judgment | Unresolved | Fixtures |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 01-demolition | 14 | 14 | 14 | 0 | 8 | 4 | 2 | 0 | 0 | 0 | 12 |
| 02-concrete | 15 | 15 | 15 | 0 | 3 | 7 | 4 | 1 | 0 | 0 | 15 |
| 03-masonry | 5 | 5 | 5 | 0 | 3 | 0 | 2 | 0 | 0 | 0 | 6 |
| 04-structural-steel | 45 | 45 | 45 | 0 | 34 | 1 | 7 | 3 | 0 | 0 | 45 |
| 05-rough-carpentry | 20 | 11 | 15 | 4 | 10 | 0 | 6 | 0 | 2 | 2 | 16 |
| 06-millwork-casework | 48 | 33 | 44 | 0 | 16 | 10 | 10 | 11 | 1 | 0 | 48 |
| 07-thermal-moisture | 42 | 40 | 40 | 1 | 29 | 3 | 9 | 0 | 1 | 0 | 40 |
| 08-openings | 27 | 26 | 27 | 0 | 3 | 23 | 1 | 0 | 0 | 0 | 27 |
| 09a-wall-framing-drywall | 50 | 46 | 50 | 0 | 4 | 0 | 46 | 0 | 0 | 0 | 50 |
| 09b-ceilings | 17 | 17 | 17 | 0 | 4 | 0 | 13 | 0 | 0 | 0 | 17 |
| 09c-flooring | 18 | 17 | 17 | 0 | 15 | 0 | 2 | 0 | 1 | 0 | 17 |
| 09d-wall-finishes | 7 | 7 | 7 | 0 | 4 | 0 | 2 | 0 | 1 | 0 | 11 |
| 09e-painting | 13 | 13 | 13 | 0 | 5 | 2 | 5 | 0 | 1 | 0 | 12 |
| 10-specialties | 15 | 15 | 15 | 0 | 1 | 14 | 0 | 0 | 0 | 0 | 15 |
| 11-equipment-furnishings | 65 | 65 | 65 | 0 | 0 | 23 | 1 | 41 | 0 | 0 | 67 |
| 22-plumbing | 42 | 41 | 42 | 0 | 17 | 23 | 0 | 1 | 1 | 0 | 41 |
| 23-hvac | 50 | 50 | 50 | 0 | 5 | 42 | 2 | 0 | 1 | 0 | 49 |
| 26-electrical | 108 | 106 | 106 | 2 | 9 | 96 | 0 | 0 | 3 | 0 | 106 |
| 28-low-voltage-fire-alarm | 26 | 25 | 25 | 0 | 0 | 25 | 0 | 0 | 1 | 0 | 26 |
| 31-earthwork | 6 | 6 | 6 | 0 | 2 | 0 | 4 | 0 | 0 | 0 | 6 |
| 32a-paving-marking | 28 | 28 | 28 | 0 | 10 | 8 | 10 | 0 | 0 | 0 | 28 |
| 32b-site-structures | 31 | 31 | 31 | 0 | 3 | 5 | 23 | 0 | 0 | 0 | 31 |
| 32c-erosion-landscape | 27 | 26 | 26 | 0 | 11 | 1 | 9 | 6 | 0 | 0 | 26 |
| 33-site-utilities | 22 | 20 | 21 | 1 | 6 | 10 | 1 | 3 | 2 | 0 | 20 |
| **Total** | **741** | **702** | **724** | **8** | **202** | **297** | **159** | **66** | **15** | **2** | **731** |

**What this does and does not mean.** The formulas reproduce the estimator from the estimator's
own measured inputs: their PlanSwift legend values, schedules and notes. It does **not** mean the
TakeoffSpeed app reads the plans that accurately today.

- **Seven of the 702 lines match by construction.** They are allowances or copies (1 LS = 1 LS),
  so 695 lines are true rebuilds.
- **The estimator's measurements sometimes disagree with the drawings:**
  - the column, joist and deck lines in `04`;
  - the pond stone, geotextile and Phase 3 inlet lines in `32c`;
  - the alarm interface in `28`.
- **The app does not read this well yet.** On this job its best interior run had 72% of material
  families within 10%. Its wall system had a median error of 20%.
- **Vision models cannot measure wall runs.** They measured partition LF with 19–55% error.

Turning drawings into those inputs reliably is the work still to do. Read further:

- [`FINDINGS.md`](FINDINGS.md): how the estimator takes off a building across trades. It covers the
  conventions, the deviations and misses, the document conflicts, and the reading traps, with line
  numbers.
- [`APP-ROADMAP.md`](APP-ROADMAP.md): a ranked plan for the app. It covers the architecture, the
  quantity-engine changes from all 24 `app-gaps.md` files, the order to build them, the fixtures as
  a regression suite, and what to validate on a second job.
- [`vision-benchmark/README.md`](vision-benchmark/README.md): which models read drawings best.
  Reading text, schedules and counts is solved; measuring undimensioned lengths from images is not.
  [`vision-benchmark/vector-geometry/`](vision-benchmark/vector-geometry/README.md) measures walls
  from PDF vector line work instead: the six-type total is within 1.5%.

## Layout

| Path | What it is |
|---|---|
| `FINDINGS.md` | Cross-trade findings: what the estimator measured, counted, derived and assumed, and where the documents and the estimate disagree. |
| `APP-ROADMAP.md` | Ranked, actionable plan for the TakeoffSpeed app built from these findings. |
| `source/drawings/` | The issued drawing set by discipline: 136 sheet PDFs (123 numbered sheets in `reference/sheets/index.json`), plus the original `8.11 Drawings.zip`. |
| `source/specifications.pdf` | Project manual, 484 pages, 69 CSI sections (`reference/sheets/spec_index.json`). |
| `source/markups/` | 92 PlanSwift markup pages in 9 PDFs: the estimator's measured runs, areas and counts drawn over the sheets, with a legend of measured quantities. |
| `source/estimate.xlsx` | The estimator's workbook (contains prices; use `reference/estimate/` instead). |
| `reference/estimate/lines.json` · `lines.csv` | All 742 estimate lines, **quantities and material descriptions only**. Line 1 is a General Conditions lump sum; lines 2–742 belong to the trade folders. |
| `reference/estimate/trades.json` | Which estimate lines belong to which trade folder. |
| `reference/markups/pages.json` | Markup page → drawing sheet. |
| `reference/markups/legends.json` · `legends.csv` | Every legend row on every markup page (item, quantity, unit, colour). Two models read them independently and a third settled disagreements. Rows that share a name were later restored and flagged "duplicate name restored". |
| `reference/sheets/` | Sheet index (`index.json`) and spec section index (`spec_index.json`). |
| `trades/<trade>/` | One folder per trade (24): how the estimator took it off, the formulas, line-by-line reconciliation to the markups, test fixtures, a plan-reading guide, researched best practice and the app gaps. |
| `vision-benchmark/` | Which vision models read construction drawings best, scored against answer keys from the PDF text layer and the estimator's markups (`README.md`, full table in `RESULTS.md`, raw calls in `results/`). |
| `vision-benchmark/vector-geometry/` | Prototype that measures wall runs by partition type from the PDF vector line work of A-120, compared with the estimator's markup. |
| `tools/` | Scripts that rebuild everything above from `source/`; `tools/workflows/` holds the multi-model workflows that read the legends and built the trade folders. |

## How each trade folder is organised

| File | Contents |
|---|---|
| `README.md` | Scope, the sheets and spec sections that drive it, material types, what the estimator measured and in which units. |
| `formulas.md` | Every quantity formula: inputs, units, the rule, and a worked example with this job's numbers. |
| `reconciliation.csv` | Each estimate line → its source measurement(s) on the markups → formula → recomputed quantity → difference. |
| `fixtures.json` | Formula test cases (measured inputs → expected quantities) for the TakeoffSpeed quantity engine. |
| `reading-guide.md` | How to read the plans and specs for this trade: symbols, legends, schedules, the sheets to cross-check, and the traps. |
| `best-practices.md` | Researched industry practice for this trade's takeoff, with sources. |
| `app-gaps.md` | Where TakeoffSpeed's current quantity engine differs, and what to change. |

## Rebuilding

```bash
python3 -I tools/extract_estimate.py source/estimate.xlsx /tmp/est      # then strip prices as in reference/estimate
python3 -I tools/render.py markup 4 /tmp/p04.png                       # any markup page or crop
python3 -I tools/render.py sheet A-120 /tmp/a120.png 0.2 0.2 0.6 0.6 3  # any drawing sheet or crop
python3 -I vision-benchmark/build_tasks.py /tmp/vb                      # benchmark crops and answer keys
python3 -I tools/extract_text.py text                                  # sheet and spec text layers cited by trade folders as text/<file>
```

Each trade folder's `scripts/` holds the rebuild and check scripts its agents used.

Needs `pymupdf`, `openpyxl`; the benchmark also needs `anthropic` and `openai`.
