# Vision benchmark: which models read construction drawings best

Five models, the same images and prompts, scored automatically against answer
keys that do not come from any model:

- **Printed text** (dimension strings, tags, schedule cells): the PDF text layer of the
  original drawings (`textlayer.py`).
- **Measured and counted quantities**: the estimator's own PlanSwift takeoff of the same
  sheets (`../reference/markups/legends.json`).

Models: Claude Fable 5.1, Claude Opus 5.5, Claude Sonnet 5.5, Claude Haiku 5.5 and
OpenAI GPT-6 Astra, all at high reasoning effort; GPT-6.1 Sol and GPT-6 Sol were added
on 2026-10-13 (all Sol calls are after OpenAI's 2026-09-25 Sol/Luna image-encoding fix).
Images are rendered from the vector PDFs at 2,576 px on the long edge (`hi`, Claude's
maximum) or 1,280 px (`lo`). OpenAI models received `hi` with `detail: "high"`, which
downscales to about 2,500 32-px patches (roughly 1,600x1,600 px; about 3,100 input
tokens per call). `orig` is an OpenAI-only variant: crops rendered by `render_openai.py`
at up to 6,000 px long edge and at most 30,000 patches (the per-image API limit), sent
with `detail: "original"`, so nothing is downscaled (about 20,000–36,000 input tokens per
call). The `zoom-tool` runs give the model a tool that re-renders any region of
the sheet from the PDF at full resolution (up to 10 zooms; OpenAI zooms also used
`detail: "high"`).

## Results by skill

Unless a row says otherwise: `hi` images; Claude sees 2,576 px, OpenAI `detail: "high"`
(about 1,600 px). Rows marked `orig` are OpenAI only: up to 6,000 px, `detail: "original"`.
Rows dated 2026-10-13 are new; where a row has two runs the cell is their mean.

| Skill (tasks) | Answer key | GPT-6 Astra | Fable 5.1 | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 | GPT-6.1 Sol | GPT-6 Sol |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Read every dimension string in a crop (12 crops, 8 sheets) — F1 | text layer | **0.989** | 0.969 | 0.968 | 0.957 | 0.942 | — | — |
| … 5-crop subset (A-130-2, A-420-1, A-610-2, A-700-3, S-201-0), `hi` (Sol 2026-10-13) | text layer | **0.973** | 0.961 | 0.961 | 0.951 | 0.922 | **0.973** | 0.958 |
| … same 5 crops, `orig` (5,629–5,995 px long edge, `detail: "original"`; 2026-10-13) | text layer | 0.971 | n/a | n/a | n/a | n/a | 0.971 | 0.894 |
| Read a door schedule, crop and whole sheet (2) — cell accuracy | text layer | 1.000 | 1.000 | 1.000 | 0.993 | 1.000 | — | — |
| Count wall-type tags by code (3 crops) — tags exact | text layer | 12/12 | 12/12 | 12/12 | 12/12 | 12/12 | — | — |
| Count lighting fixtures by type (E-130) and plumbing fixtures (P-302) — mean abs. error (Sol 2026-10-13) | estimator markup | **0.7%** | 1.1% | 1.2% | 3.0% | 1.8% | 1.2% | 1.6% |
| … with zoom tool (lighting only) | estimator markup | 0.9% | 3.5% | 0.9% | 0.9% | — | — | — |
| … `orig` (5,995x4,702 and 5,342x5,714 px, `detail: "original"`; 2026-10-13) | estimator markup | **0.5%** | n/a | n/a | n/a | n/a | 0.6% | 8.2% |
| Measure ceiling area by type (A-130 RCP) — mean abs. error (Sol 2 runs, 2026-10-13) | estimator markup | 3.8% | 12.6% | **3.8%** | 21.7% | 78.8% | 3.4% | 19.1% |
| … with zoom tool | estimator markup | **2.6%** | **2.6%** | 3.4% | 23.8% | — | — | — |
| … `hi` re-run (1 run, 2026-10-13) | estimator markup | 2.3% | — | — | — | — | — | — |
| … `orig` (5,322x5,725 px, `detail: "original"`; 2 runs, 2026-10-13) | estimator markup | 5.1% | n/a | n/a | n/a | n/a | 17.0% | 40.7% |
| Measure partition LF by wall type (A-120) — mean abs. error (Sol 2 runs, 2026-10-13) | estimator markup | (call failed) | 54.7% | 21.8% | 33.3% | 40.1% | 36.7% | 32.4% |
| … with zoom tool | estimator markup | **19.0%** | 24.6% | 33.2% | 26.4% | — | — | — |
| … `hi` re-run (2 runs, 2026-10-13) | estimator markup | **15.2%** | — | — | — | — | — | — |
| … `orig` (5,835x5,212 px, `detail: "original"`; 2 runs, 2026-10-13) | estimator markup | **15.1%** | n/a | n/a | n/a | n/a | 17.2% | 95.4%¹ |

¹ GPT-6 Sol at `orig` returned one wall type in one run and an empty list in the other
(scored as 0 LF), so this is a failure to answer, not a measurement.

Per-call cost (USD, list prices; GPT-6 Astra booked at an assumed $10/$50 per MTok
because its price is not returned by the API; both Sol models at $2/$10): dimension crop ≈ 0.13 GPT-6 Astra,
0.10 Fable, 0.03 Opus, 0.03 GPT-6.1 Sol, 0.017 Sonnet, 0.0014 Haiku. At `orig` the image
costs about 10x the tokens of `hi`, so a call costs 2–3x as much (dimension crop ≈ 0.40
Astra, 0.08 GPT-6.1 Sol; wall measurement ≈ 1.38 Astra, 0.25 GPT-6.1 Sol). Zoom-tool runs cost 3–20× a
single call. Full table: `RESULTS.md`; raw calls and answers: `results/*.jsonl`.

## Does higher resolution help OpenAI? (`orig`, 2026-10-13)

Test of the finding in `../research/plan-reading-technology.md` that `detail: "high"`
caps GPT-6 Astra near 1,600x1,600 px. Same tasks, prompts and scorers; only the image
changed (`hi`: 2,576 px render downscaled by the API to about 2,500 patches, about 3,100
input tokens; `orig`: 5,600–6,000 px long edge, 16,000–30,000 patches, 20,000–36,000 input
tokens, confirmed not downscaled from the token counts). Wall and ceiling tasks were run
twice per variant. Raw calls: `results/orig1.jsonl`, `results/orig2.jsonl`.

**Wall length (A-120), the key question: higher resolution did not change the error.**
GPT-6 Astra's mean per-type error was 15.2% at `hi` (runs: 14.6%, 15.8%) and 15.1% at
`orig` (14.9%, 15.2%), with 1–3 of 6 wall types within 5% either way. The per-type
pattern is the same at both resolutions, which points to how runs are assigned to wall
types rather than to image detail: A3B is over by
36–42% and D3C by 22–35% in all four runs, and A6A/A6B are within about 5%. GPT-6.1 Sol
went from 36.7% to 17.2%, but most of that is one `hi` run that put 13 LF on the 3.7 LF
D3C type; at `orig` it still overstates A3B by 36–45% and understates D3A by 23–37%.
GPT-6 Sol did not answer at `orig`. Astra's **total** LF across types was within 2.5–4.6%
of the estimator's 198.9 LF in all four runs, but per-type errors offset, and a takeoff
needs each wall type. **No model measures undimensioned walls within about 5% per wall
type at any resolution tested.** That supports the vector-geometry route.

| A-120 wall type (estimator LF) | A3A (49.9) | A3B (34.2) | A6A (36.7) | A6B (28.4) | D3A (46.0) | D3C (3.7) | Total (198.9) |
|---|---:|---:|---:|---:|---:|---:|---:|
| GPT-6 Astra `hi`, run 1 / run 2 | −19% / +3% | +26% / +36% | −5% / −5% | +6% / +4% | −11% / −12% | +22% / +35% | 194.0 / 208.0 |
| GPT-6 Astra `orig`, run 1 / run 2 | −6% / −6% | +42% / +42% | −5% / −4% | +4% / +4% | −8% / −8% | +24% / +27% | 206.9 / 207.3 |
| GPT-6.1 Sol `hi`, run 1 / run 2 | +12% / +6% | +20% / +51% | −5% / −11% | +6% / −23% | −15% / −9% | +251% / −32% | 214.0 / 203.5 |
| GPT-6.1 Sol `orig`, run 1 / run 2 | +1% / −2% | +36% / +45% | +3% / −1% | +6% / +4% | −23% / −37% | +16% / −32% | 204.7 / 196.0 |

**Other skills.** Resolution did not help elsewhere either, beyond noise:
- Dimension strings (5 crops): F1 0.973 → 0.971 for both Astra and GPT-6.1 Sol; GPT-6 Sol
  fell from 0.958 to 0.894.
- Ceiling areas: worse at `orig`. Astra 2.3–3.8% → 4.8–5.3% (GYP +13% in both runs);
  GPT-6.1 Sol 2.6–4.2% → 15.9–18.0% (overstates ACT-1, ACT-2 and GYP); GPT-6 Sol is unstable
  at both (7.7–30.4% `hi`, 2.7–78.7% `orig`).
- Fixture counts: slightly better for Astra (lighting 1.4% → 1.0%) and GPT-6.1 Sol (2.3% →
  1.2%); plumbing was already exact. GPT-6 Sol got worse on lighting (2.2% → 15.3%).
- GPT-6.1 Sol at `hi` is close to Astra on reading and counting (dimension F1 0.973 vs 0.973;
  counts 1.2% vs 0.7%) at about a fifth of the cost per call.

Caveats: the 5 dimension crops were chosen as the densest crop (A-130-2) plus four where
Astra `hi` was below F1 1.0, so subset scores sit below the 12-crop ones. One or two runs per cell; run-to-run spread on the measuring tasks (e.g. GPT-6.1
Sol walls 22–51% at `hi`) is larger than most differences between variants. Five calls were
dropped by the network path before the client switched to background mode and were re-run;
any usage OpenAI billed for the dropped attempts is not in the results files. Logged spend for
this test: $14.81 (Astra $10.59, GPT-6.1 Sol $2.24, GPT-6 Sol $1.99) plus about $0.28 for a
five-call probe that confirmed all three models accept `original` without downscaling.

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
   directions. Sending OpenAI models the full-resolution image (`orig`, up to 6,000 px)
   did not change this: GPT-6 Astra stayed at about 15% per type at both resolutions. This is the dominant source of error in an AI wall takeoff, and it
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
python3 -I vision-benchmark/render_openai.py /tmp/vb [task_ids]  # OpenAI-only <task>-orig.png (<= 6,000 px, <= 30,000 patches)
python3 -I vision-benchmark/run_benchmark.py /tmp/vb orig1 30 gpt-6-astra:orig,gpt-6.1-sol:orig,gpt-6.1-sol:hi [task_ids]
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
