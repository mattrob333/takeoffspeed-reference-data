# Vision benchmark: which models read construction drawings best

Five models, the same images and prompts, scored automatically against answer
keys that do not come from any model:

- **Printed text** (dimension strings, tags, schedule cells): the PDF text layer of the
  original drawings (`textlayer.py`).
- **Measured and counted quantities**: the estimator's own PlanSwift takeoff of the same
  sheets (`../reference/markups/legends.json`).

Models: Claude Fable 5.1, Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5 and
OpenAI GPT-6 Astra, all at high reasoning effort. Images are rendered from the
vector PDFs at 2,576 px on the long edge (`hi`, the current maximum) or 1,280 px
(`lo`). The `zoom-tool` runs give the model a tool that re-renders any region of
the sheet from the PDF at full resolution (up to 10 zooms).

## Results by skill

| Skill (tasks) | Answer key | GPT-6 Astra | Fable 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 |
|---|---|---:|---:|---:|---:|---:|
| Read every dimension string in a crop (12 crops, 8 sheets) — F1 | text layer | **0.989** | 0.969 | 0.968 | 0.957 | 0.942 |
| Read a door schedule, crop and whole sheet (2) — cell accuracy | text layer | 1.000 | 1.000 | 1.000 | 0.993 | 1.000 |
| Count wall-type tags by code (3 crops) — tags exact | text layer | 12/12 | 12/12 | 12/12 | 12/12 | 12/12 |
| Count lighting fixtures by type (E-130) and plumbing fixtures (P-302) — mean abs. error | estimator markup | **0.7%** | 1.1% | 1.2% | 3.0% | 1.8% |
| … with zoom tool (lighting only) | estimator markup | 0.9% | 3.5% | 0.9% | 0.9% | — |
| Measure ceiling area by type (A-130 RCP) — mean abs. error | estimator markup | 3.8% | 12.6% | **3.8%** | 21.7% | 78.8% |
| … with zoom tool | estimator markup | **2.6%** | **2.6%** | 3.4% | 23.8% | — |
| Measure partition LF by wall type (A-120) — mean abs. error | estimator markup | (call failed) | 54.7% | 21.8% | 33.3% | 40.1% |
| … with zoom tool | estimator markup | **19.0%** | 24.6% | 33.2% | 26.4% | — |

Per-call cost (USD, list prices; GPT-6 Astra booked at an assumed $10/$50 per MTok
because its price is not returned by the API): dimension crop ≈ 0.13 GPT-6 Astra,
0.10 Fable, 0.03 Opus, 0.017 Sonnet, 0.0014 Haiku. Zoom-tool runs cost 3–20× a
single call. Full table: `RESULTS.md`; raw calls and answers: `results/*.jsonl`.

## What this means for TakeoffSpeed

1. **Reading printed information is solved.** Dimension strings, tags and
   schedules are read at 96–99% F1 by every current model, and resolution barely
   matters (Opus 0.968 at 2,576 px vs 0.964 at 1,280 px). The remaining misses are
   ceiling-height tags inside the RCP field (e.g. `9'-0" A.F.F.`). The PDF text
   layer gives these strings exactly, for free, so the app should use the text
   layer for every printed value and use vision only for scanned sheets.
2. **Counting symbols is reliable** at about 1% error on the strong models, and the
   zoom tool helps weaker ones (Sonnet 3.0% → 0.9%).
3. **Areas are good from the strong models** (2.6–3.8%), and the zoom tool closes
   most of Fable's gap (12.6% → 2.6%).
4. **Measuring undimensioned wall runs from an image is not reliable for any model**,
   even zooming freely: 19–55% error per wall type, with totals off in both
   directions. This is the dominant source of error in an AI wall takeoff, and it
   matches the app's own results on the same job (runner LF 21–62% short).
   Geometry should come from the PDF's vector line work (26,341 line segments on
   A-120 alone), measured by code, with the AI assigning wall types and checking
   the result — see `vector-geometry/`.
5. **Model choice:** GPT-6 Astra is the most accurate reader overall but the
   slowest and costliest here. Opus 5.5 is the best Claude value: equal to Fable
   on reading and counting, better on one-shot areas, at about a third of the
   cost. Haiku 5.5 is surprisingly strong at reading and counting for 1–2% of the
   cost and suits bulk passes (sheet classification, text checks), not
   measurement. Two independent readers plus a third to settle disagreements worked well
   for the markup legends (Sonnet and Opus agreed on 647 of the 656 final rows;
   Fable settled the rest). A second provider (GPT-6 Astra) adds independence
   for the hardest items.

## Reproduce

```bash
pip install pymupdf anthropic openai
python3 -I vision-benchmark/build_tasks.py /tmp/vb          # crops + answer keys -> tasks.json
python3 -I vision-benchmark/run_benchmark.py /tmp/vb run1 20 claude-opus-5-5:hi,gpt-6-astra:hi [task_ids]
python3 -I vision-benchmark/run_agentic.py /tmp/vb zoom1 14 claude-opus-5-5 measure-A-120-walls
python3 -I vision-benchmark/rescore.py results/run1.jsonl   # re-score saved answers after a key change
python3 -I vision-benchmark/summarize.py results/*.jsonl > vision-benchmark/RESULTS.md
```

Needs `DUTYGRAPH_ANTHROPIC_API_KEY` and `OPENAI_API_KEY`.

## Caveats

- One job, one estimator. The measuring keys are the estimator's quantities, so
  they include the estimator's conventions (e.g. which short wall segments count).
- Two to twelve tasks per skill; treat differences under ~1 point as noise.
- The tag-count crops include one tag the text layer places at the crop edge, which
  every model scored identically, so tag counting is effectively perfect.
- The first dimension answer key missed values inside notes and spaced ceiling
  heights (`9' - 0"`); the key was widened and every saved answer re-scored with
  `rescore.py` (no model was re-run).
