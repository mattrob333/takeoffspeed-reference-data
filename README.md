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

## Layout

| Path | What it is |
|---|---|
| `source/drawings/` | The issued drawing set by discipline (136 files, 123 numbered sheets). |
| `source/specifications.pdf` | Project manual, 484 pages, 69 CSI sections (`reference/sheets/spec_index.json`). |
| `source/markups/` | 92 PlanSwift markup pages: the estimator's measured runs, areas and counts drawn over the sheets, with a legend of measured quantities. |
| `source/estimate.xlsx` | The estimator's workbook (contains prices; use `reference/estimate/` instead). |
| `reference/estimate/lines.json` · `lines.csv` | All 742 estimate lines, **quantities and material descriptions only**. |
| `reference/estimate/trades.json` | Which estimate lines belong to which trade folder. |
| `reference/markups/pages.json` | Markup page → drawing sheet. |
| `reference/markups/legends.json` | Every legend row on every markup page (item, quantity, unit), read by two models independently and settled by a third. |
| `reference/sheets/` | Sheet index and spec section index. |
| `trades/<trade>/` | One folder per trade: how the estimator took it off, the formulas, line-by-line reconciliation to the markups, test fixtures, a plan-reading guide, and researched best practice. |
| `vision-benchmark/` | Which vision models read construction drawings best, scored against answer keys from the PDF text layer. |
| `tools/` | Scripts that rebuild everything above from `source/`. |

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
```

Needs `pymupdf`, `openpyxl`; the benchmark also needs `anthropic` and `openai`.
