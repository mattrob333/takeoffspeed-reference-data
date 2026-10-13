# Plan-reading technology for TakeoffSpeed: models, OCR, takeoff products, and measurement techniques

Research date: 2026-10-13. Scope: getting **material quantities** from construction drawings and specs as
accurately as possible. Cost of the stack is not a constraint. Pricing and estimating features are out of scope.

How to read this report:

- Every factual claim links to its source. **Vendor-reported** marks numbers a vendor published about its own
  product that nobody else has reproduced. Treat those as marketing until tested.
- Our own benchmark (`vision-benchmark/RESULTS.md` in this repository) is the baseline. One real 36x24 vector set:
  frontier models read dimension strings at 0.94–0.99 F1, transcribe door schedules at about 1.00, and count
  tagged symbols within about 1% MAPE. The best model measured areas within about 4%. Undimensioned lengths
  measured from images missed by 13–59% MAPE on Claude models without a zoom tool, and the best was still 10.8%
  with one. GPT-6 Astra's 3.8% covered only 4 of 10 items, because one call errored. Measuring
  the same walls from the PDF vector paths in code got within 1.5% (`vision-benchmark/vector-geometry/`).
- The recommendation is in **section 6**, marked clearly. Sections 1–5 are the evidence behind it.

---

## 0. Executive summary

1. **Geometry should come from vectors, and models should make the judgments.** No published result, and
   nothing in our own data, shows any VLM measuring undimensioned lengths from pixels to estimator accuracy. The
   field's own benchmarks agree. DrawingVQA (CVPR 2026) finds models "fail at visual perception... most pronounced
   on quantity takeoff tasks" ([arXiv 2607.15418](https://arxiv.org/html/2607.15418)). AECV-Bench finds
   symbol-centric understanding "remains unsolved" ([arXiv 2601.04819](https://arxiv.org/pdf/2601.04819)). The
   strongest published takeoff system, Handoff-H1, uses purpose-built CV models and tools under its agents rather
   than raw VLM perception ([arXiv 2608.15032](https://arxiv.org/html/2608.15032)).
2. **Our image benchmark under-tested OpenAI's resolution.** `run_benchmark.py` sends `detail: "high"`. On
   `gpt-6-astra`, `high` caps the image at 2,500 patches (about 1600x1600 px). The `original` detail level
   preserves dimensions up to the 30,000-patch request limit, roughly 6,800x4,500 px for a 36x24 sheet, or about
   188 px/in ([OpenAI images & vision guide](https://developers.openai.com/api/docs/guides/images-vision)). Claude's
   ceiling is 2576 px on the long edge and 4,784 visual tokens, about 65 px/in across a full 36x24 sheet
   ([Claude vision docs](https://platform.claude.com/docs/en/build-with-claude/vision)). Re-run the benchmark at
   `original`.
3. **Gemini is the main untested family, and it needs a new key.** Earlier Gemini versions led both
   construction-drawing benchmarks: AECV-Bench counting ([arXiv 2601.04819](https://arxiv.org/pdf/2601.04819)) and
   DrawingVQA overall and on dimensional recognition ([arXiv 2607.15418](https://arxiv.org/html/2607.15418)). The
   current lineup is Gemini 3.8 Flash (stable) and Gemini 4 Argon (flagship, limited rollout)
   ([Gemini models](https://ai.google.dev/gemini-api/docs/models)). Gemini also offers "agentic vision": Python
   code execution that crops and zooms images
   ([Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/agentic-vision-gemini-3-flash/)).
4. **For scanned (vector-less) plans, the best-documented OCR is Azure Document Intelligence.** Its Layout model
   has an `ocrHighResolution` add-on aimed at "engineering drawings" and A1/A2/A3 sheets
   ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/concept/add-on-capabilities)).
   Run it as primary OCR, with VLM crops as reader and verifier. The open-weights fallback is PaddleOCR (Apache-2.0),
   whose PaddleOCR-VL-1.6 is near the top of OmniDocBench ([GitHub](https://github.com/PaddlePaddle/PaddleOCR),
   [OmniDocBench](https://github.com/opendatalab/OmniDocBench)).
5. **No commercial takeoff product publishes independently verified accuracy.** Some do expose APIs: Kreo (Pro and
   Enterprise plans), Exayard (REST/MCP), and Autodesk Takeoff (read access to takeoff data). None is a better
   geometry engine than our own vector pipeline. Togal's 98%, Kreo's 94%, and Trimble's 97% scale detection are all
   vendor-reported. Trimble's figure is still a useful signal: scale reading from sheet text is a solved-enough
   problem at scale ([Trimble](https://www.trimble.com/en/blog/construction/article/actual-results-mep-estimators-ai-assisted-takeoff)).

---

## 1. Vision-language models available via API (October 2026)

### 1.1 Lineup, resolution and coordinate behavior

| Provider / model | Access today | Max image fidelity per call | Coordinates and pointing | Region/zoom tooling | List price (in / out per 1M tokens) |
|---|---|---|---|---|---|
| Anthropic `claude-fable-5-1`, `claude-opus-5-5`, `claude-sonnet-5-5`, `claude-haiku-5-5` | **Have key** | High-resolution tier (Claude 4.7 and later): 2576 px long edge, 4,784 visual tokens, 28x28-px patches; hard cap 8000x8000; up to 600 images per request ([vision](https://platform.claude.com/docs/en/build-with-claude/vision)) | Returns **absolute pixel** coordinates in the resized image. Docs say it "does not work well" with normalized 0–1000 coordinates. Set `transformations.oversized_image: "error"` to forbid silent resizing ([coordinates](https://platform.claude.com/docs/en/build-with-claude/vision-coordinates)) | Client-side tools (our zoom tool); code execution server tool ([models overview](https://platform.claude.com/docs/en/about-claude/models/overview)) | Fable 5.1 $10/$50; Opus 5.5 $4/$20; Sonnet 5.5 $2/$10; Haiku 5.5 from $0.10/$0.50 ([models overview](https://platform.claude.com/docs/en/about-claude/models/overview)) |
| OpenAI `gpt-6-astra` | **Have key** | `original` detail keeps native dimensions up to 65,535 px per side. Requests over 30,000 32-px patches are rejected. `high` = 2,500 patches ([images & vision](https://developers.openai.com/api/docs/guides/images-vision)) | Not documented in the guide. Roboflow measures 75.5–76.8% on its "text localization" OCR subtask ([Roboflow](https://playground.roboflow.com/models/compare/gpt-6-astra-vs-grok-4-6)) | code_interpreter and computer use in the Responses API | $10/$50 ([DeepLearning.AI](https://www.deeplearning.ai/the-batch/sol-nearly-eclipses-astra)) |
| OpenAI `gpt-6.1-sol` (released 2026-09-29) | **Have key** | Takes image input. The model page does not state its detail levels, so verify that `original` is accepted ([model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol)) | Roboflow text localization 74.4–76.7%; object detection 80.8–81.6% ([Roboflow](https://playground.roboflow.com/models/compare/gpt-6-1-sol-vs-claude-fable-5-1)) | code_interpreter, computer_use, hosted_shell ([model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol)) | $2/$10; prompts over 272K tokens cost more ([model page](https://developers.openai.com/api/docs/models/gpt-6.1-sol)) |
| OpenAI `gpt-6-sol`, `gpt-6-luna` (2026-09-22) | **Have key** | An image-encoding bug that "degraded image understanding" was fixed on **2026-09-25**. OpenAI recommends re-running evals ([changelog](https://developers.openai.com/api/docs/changelog)) | n/a | Same tools as above | Sol $2/$10, Luna $0.10/$0.50 ([TechJack summary of OpenAI post](https://techjacksolutions.com/ai-tools/chatgpt/what-is-gpt-6-sol-and-luna/)) |
| Google `gemini-3.8-flash` (stable) | **New key** (AI Studio or Vertex) | `media_resolution` per item: low 280 / medium 560 / high 1120 / ultra_high 2240 tokens per image ([media resolution](https://ai.google.dev/gemini-api/docs/media-resolution)). PDF pages are scaled to at most 3072x3072 ([document processing](https://ai.google.dev/gemini-api/docs/document-processing)) | Native `box_2d` boxes, normalized 0–1000, plus segmentation masks ([image understanding](https://ai.google.dev/gemini-api/docs/image-understanding)) | **Agentic vision**: the model writes Python to crop, zoom and annotate images; Google claims a 5–10% boost on vision benchmarks ([blog](https://blog.google/innovation-and-ai/technology/developers-tools/agentic-vision-gemini-3-flash/), [code execution](https://ai.google.dev/gemini-api/docs/code-execution)) | $0.75/$3.75 through 2026-12-31, then $1.50/$7.50 ([pricing](https://ai.google.dev/gemini-api/docs/pricing)) |
| Google `gemini-4-argon` (announced 2026-09-30) | Listed on the model page ([models](https://ai.google.dev/gemini-api/docs/models)), but launch coverage describes a limited rollout that starts with paid API customers ([VentureBeat](https://venturebeat.com/technology/google-unveils-gemini-4-argon-retaking-benchmark-lead-over-openai-and-anthropic-but-in-limited-release)). Confirm access with a key | Not documented separately | — | — | Introductory $2/$10, later $4/$20 ([Google blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)) |
| Google `gemini-3.1-pro-preview` | New key | Same media_resolution scheme | Same | Same | $2/$12 under 200K tokens ([pricing](https://ai.google.dev/gemini-api/docs/pricing)) |
| Alibaba Qwen3.5-397B-A17B (open weights, Apache-2.0); Qwen3.6 Plus (closed API) | Self-host, or a new Alibaba Cloud account | Qwen3-VL uses relative 0–1000 coordinates; Qwen2.5-VL used absolute ([Qwen3-VL report](https://arxiv.org/pdf/2511.21631), secondary: [Ollama](https://registry.ollama.ai/library/qwen3-vl)) | Grounding evaluated on RefCOCO and CountBench ([report](https://arxiv.org/pdf/2511.21631)) | Self-built | Qwen3.6 Plus $0.325/$1.95 ([Roboflow](https://playground.roboflow.com/models/compare/qwen3-6-plus-vs-claude-opus-5-5)) |
| xAI Grok 4.6 | New key | — | Roboflow object detection about 24%, text localization about 10% ([Roboflow](https://playground.roboflow.com/models/compare/gpt-6-astra-vs-grok-4-6)) | — | — |
| Mistral (Large 3), Meta, DeepSeek | New keys | — | Mistral Large 3 was mid-to-low on AECV-Bench counting ([arXiv 2601.04819](https://arxiv.org/pdf/2601.04819)). DeepSeek-OCR-2 is an OCR model, see 2.3 | — | — |

**What resolution means on a 36x24 sheet.** This is our arithmetic from the limits above. Plotted note text on
drawings is commonly 3/32" ([SourceCAD](https://sourcecad.com/standard-text-sizes-in-technical-drawing/)).

- **Claude, full sheet:** about 2350x1567 px, or 65 px/in. 3/32" text is about 6 px tall, which is unreadable.
  Claude therefore *must* work from crops, which is what our zoom tool does. A 6"-wide crop at 2576 px gives about
  430 px/in.
- **GPT-6 Astra, `original`, full sheet:** about 6,780x4,520 px under the 30,000-patch cap (188 px/in), so 3/32"
  text is about 18 px. That costs about 36,000 image tokens, roughly $0.36 per sheet on Astra or $0.07 on 6.1 Sol
  at list price.
- **Gemini, PDF input:** pages are capped at 3072 px, about 85 px/in on a 36" sheet. Send image crops instead.

### 1.2 Published evidence on technical and construction drawings

| Benchmark | What it tests | Key result | Caveat |
|---|---|---|---|
| **AECV-Bench** (Jan 2026; [paper](https://arxiv.org/pdf/2601.04819), [code](https://github.com/AECFoundry/AECV-Bench)) | 120 floor plans (CubiCasa5K, CVC-FP, web), counting doors, windows, bedrooms and toilets; 192 drawing QA pairs | Best counting: Gemini 3 Pro at 0.51 mean exact-match accuracy and 16.0% MAPE; GPT-5.2 at 0.49 and 19.4%. Door and window exact match only 0.39 / 0.34. OCR QA up to 0.95. "Symbol-centric drawing understanding... remains unsolved" | Raster residential plans with **untagged** symbols and older models. Our tagged-symbol counts with 2026 models are far better, so the two results are consistent: tags plus text are easy, while graphic symbols without tags are hard |
| **DrawingVQA** (CVPR 2026; [paper](https://arxiv.org/html/2607.15418)) | 33 Issued-for-Construction drawings, 92 QA pairs | Overall: Gemini-3-pro-preview 77.2; experienced professionals 94.9. Quantity takeoff is the weakest category: best model 41.7 versus professionals 96.6. Dimensional recognition: Gemini-3-pro 77.4 | Small set, older models (Claude 4.5, o3, GPT-4o) |
| **Handoff-H1** ([paper](https://arxiv.org/html/2608.15032)) | 10 residential blueprint sets, 2,009 expert-verified line items; coverage and quantity Precision@25% | Raw frontier models score 35–61 composite (claude-fable-5 61.4, gpt-5.6 58.6). The Handoff-H1 agent system with purpose-built CV primitives scores **81.6**; professional estimators 77.6 (P@25% 87.9 versus 78.8 for H1) | Data available on request. Methods withheld. Area and linear trades (framing, siding, roofing) are worse than count trades |
| **AEC-Bench** ([arXiv 2603.29199](https://arxiv.org/abs/2603.29199), [Nomic](https://www.nomic.ai/news/aec-bench)) | 196 agentic tasks in 9 families (cross-sheet reasoning) | Adding domain tools to Claude Code or Codex harnesses consistently improves results | Scores not legible in the indexed text |
| **Roboflow Vision Evals** (updated 2026-10-13) | General vision across 62 models | GPT-6 Astra 83.4 overall (#1); Claude Opus 5.5 82.0 (#2); GPT-6.1 Sol 81.7 (#4); Gemini 3.8 Flash 79.8 (#6); Fable 5.1 74.7 (#13). Text localization: Astra 77%, 6.1 Sol 77%, Opus 5.5 61%, Fable 5.1 43–47%, Gemini 3.8 Flash 26–59% ([Astra](https://playground.roboflow.com/models/compare/gpt-6-astra-vs-grok-4-6), [Opus vs 3.8 Flash](https://playground.roboflow.com/models/compare/claude-opus-5-5-vs-gemini-3-8-flash), [6.1 Sol vs Fable](https://playground.roboflow.com/models/compare/gpt-6-1-sol-vs-claude-fable-5-1)) | Not drawing-specific. Gemini 4 Argon not evaluated |
| **MechVQA** (ICML 2026; [GitHub](https://github.com/xiaofengShi/MechVQA)) | Mechanical drawings | A 4B fine-tuned MechVL (84.85) beats GPT-5 (75.44) and Gemini-3-Pro-Preview (77.28) | Domain fine-tuning beats general frontier models on narrow drawing tasks |
| **OmniDocBench v1.6** ([GitHub](https://github.com/opendatalab/OmniDocBench)) | Document parsing, not drawings | Gemini 3 Pro 92.91; GPT-5.2 86.59. Specialised OCR VLMs lead (TeleOCR 96.91, PaddleOCR-VL-1.6 96.34). No Claude entry | Page documents, not sheets |

**Hype versus evidence for VLMs:**

- **Proven (ours and the literature):** reading printed text, dimension strings, schedules and tags; sheet and title
  block understanding.
- **Promising but unproven on our data:** Gemini's native boxes and masks, and agentic zoom.
- **Not supported by any evidence:** pixel-measuring lengths to under 5% error without a dimension.

---

## 2. OCR and document AI for rotated, tiny, dense drawing text and tables

On **vector PDFs**, OCR should not be the first source of text at all. The text layer (pdf.js `getTextContent`, or
PyMuPDF) gives exact strings, fonts, positions and rotation matrices. Our benchmark's dimension F1 is a VLM
reading score, not a ceiling. OCR matters for scanned sets, raster images pasted into PDFs, and SHX text that CAD
exports as stroked line work rather than real text.

### 2.1 Cloud services

| Service | Drawing-relevant capability | Hard limits | Notes |
|---|---|---|---|
| **Azure AI Document Intelligence v4.0 (2024-11-30 GA), Layout** | `ocrHighResolution` add-on, written for "small text from large-size documents, like engineering drawings... varying fonts, sizes, and orientations", A1/A2/A3 ([add-ons](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/concept/add-on-capabilities)). Extracts **rotated tables** with cell polygons ([layout](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout)) | Images 50 to 10,000 px per side; 500 MB; 2,000 pages; minimum text height about 12 px, or about 8 pt at 150 DPI ([layout](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/prebuilt/layout)) | **Best documented fit for scanned sheets.** A 36" side allows up to about 277 DPI |
| **AWS Textract** | Handles any in-plane rotation of the document, including 45° ([limits](https://docs.aws.amazon.com/textract/latest/dg/limits-document.html)) | 10,000 px per side; PDFs up to 40 in / 9000 pt per side; minimum text 15 px; "does not support vertical text" ([limits](https://docs.aws.amazon.com/textract/latest/dg/limits-document.html)) | Mixed-orientation text on one sheet (vertical dimension strings) needs testing. Six Latin languages only |
| **Google Document AI** (Enterprise OCR v2.1; Gemini-backed Layout Parser) | Rotation correction and deskew; native PDF text merged with OCR; image-quality defect scores including "small text" ([OCR](https://docs.cloud.google.com/document-ai/docs/enterprise-document-ocr)). The Layout Parser runs on Gemini 3 Pro/Flash previews ([layout parser](https://docs.cloud.google.com/document-ai/docs/layout-parse-chunk)) | Images up to 40 MP per page (not applied to PDFs); 40 MB online; 15 pages online, 500 batch ([limits](https://docs.cloud.google.com/document-ai/limits)) | No drawing-specific guidance |
| **Mistral OCR 4 / 4.1** (`mistral-ocr-latest`) | Markdown or HTML tables; block-level boxes and types; page, block and word confidence ([docs](https://docs.mistral.ai/capabilities/document_ai/basic_ocr/)) | Secondary sources report $4 per 1,000 pages, or $2 batch; OmniDocBench 93.07 claimed for OCR 4 ([RuntimeWire](https://runtimewire.com/article/mistral-ocr-4-1-block-confidence-document-ai)) | Built for documents. Good for **scanned project manuals and specs**, unproven on sheets |

### 2.2 Open models

| Model | Status | Evidence | Fit |
|---|---|---|---|
| **PaddleOCR 3.7** (PP-OCRv6, PP-StructureV3, PaddleOCR-VL-1.6) | Apache-2.0, released 2026-06-11 ([GitHub](https://github.com/PaddlePaddle/PaddleOCR)) | PaddleOCR-VL-1.6 scores 96.34 on OmniDocBench v1.6 ([leaderboard](https://github.com/opendatalab/OmniDocBench)). PP-OCRv6 is a 1.5M–34.5M-parameter detector plus recognizer | Detector and recognizer suit **tiled drawing OCR** with rotated boxes. The VL model suits schedules and specs |
| **docTR 1.1** (Mindee) | Apache-2.0; returns rotated boxes when `assume_straight_pages=False` ([GitHub](https://github.com/mindee/doctr)) | — | Solid, self-hostable word-level OCR for rotated text |
| **Surya 2 / Chandra OCR 2** (Datalab) | Code Apache-2.0. Weights under modified OpenRAIL-M, free only under $5M funding or revenue ([GitHub](https://github.com/datalab-to/surya)) | olmOCR-bench: Surya 2 83.3, Chandra 2 85.9 | Docs suggest at most 2048 px wide, so not built for whole sheets. Check the license |
| **GOT-OCR** | — | 48.3 on olmOCR-bench ([Surya README](https://github.com/datalab-to/surya)) | Behind newer models |
| **DeepSeek-OCR-2** (2026-01-27) | Open, 3B | 91.09 on OmniDocBench v1.5 ([TechNode](https://technode.com/2026/01/28/deepseek-releases-ocr-2-with-new-visual-encoding-architecture-targeting-more-human-like-machine-vision/)) | Document-oriented, no drawing evidence |
| **eDOCr2** (mechanical drawings) | Code at [github.com/javvi51/edocr2](https://github.com/javvi51/edocr2) | 93.75% text recall and under 1% CER on its benchmark. VLMs added after segmentation helped interpret results ([MDPI Machines 13(3):254](https://www.mdpi.com/2075-1702/13/3/254)) | The pattern carries over: **segment, then OCR, then VLM-verify** dimension text |

Roboflow's general guidance agrees: for small text, "detect the region, crop it, then run OCR"
([Roboflow](https://roboflow.com/blog/best-computer-vision-models)).

**Assessment for scanned plans.** No public benchmark compares these services on construction sheets. We would
have to measure this ourselves (see 6.4, B5). On documentation alone, Azure Layout with `ocrHighResolution` comes
first, Google Enterprise OCR and Textract follow, and PaddleOCR is the self-hosted fallback.

**Schedules.** On vector PDFs, rebuild table cells from the ruling lines, the way pdfplumber does: find lines,
intersect them, form cells ([pdfplumber](https://github.com/jsvine/pdfplumber)). Fill the cells from the text
layer, and keep the VLM transcription as an independent second read. Our VLMs already reach about 1.00 here. On
scans, use Azure Layout tables with cell polygons.

---

## 3. Construction-specific AI takeoff products

| Product | What the AI does | Scale | Accuracy claim (all **vendor-reported** unless noted) | API |
|---|---|---|---|---|
| **Togal.AI** | One button detects rooms (areas) and walls, "trained to recognize the parallel lines that represent walls". Outputs footprint, net, gross, wall centerline and perimeter. Users clean up gaps and wrong lines ([help](https://help.togal.ai/en/articles/15602901-ai-powered-area-and-wall-detection)) | Listings describe auto scale ([FitGap](https://us.fitgap.com/products/021642/togal-ai)) | "Up to 98% accuracy on floor plans" ([togal.ai](https://www.togal.ai/)); "humans were 97%" ([ForConstructionPros](https://www.forconstructionpros.com/equipment/worksite/electric-tools-and-accessories/article/22908091/togal-ai-leverages-first-in-market-status-in-ai-takeoff-software)). No methodology | None public |
| **Kreo** | Auto Measure 3.0 (rooms, walls, doors, windows; a second pass "re-fits every outline"), One-Click Area, Auto Count, AI Scale Detection, Caddie agent ([kreo.net](https://www.kreo.net/)) | AI scale detection | Outline accuracy 72%→94%; area captured 92.6%→99.3%; precision 81%→90%; recall 81%→87% ([kreo.net](https://www.kreo.net/)). A user found auto-measure cleanup "as long as manual"; it works best on vector plans ([Capterra/GetApp reviews](https://www.getapp.co.uk/software/2058370/kreo-2d-takeoff)) | **Yes**: Pro (via sales) and Enterprise ("Full API") ([kreo.net](https://www.kreo.net/)) |
| **Beam AI** (Attentive.ai) | AI takeoff followed by an expert estimator QA pass; 24–72 h turnaround ([Capterra](https://capterra.com/p/10017154/Beam-AI)) | — | "±1% of in-house takeoff" via human review (Capterra) versus "98%" (GetApp). The two conflict ([GetApp](https://www.getapp.com/construction-software/a/beam-ai/)) | Not found. Essentially a service with human labor |
| **STACK** | "Symbol Counting AI" ([support](https://support.stackct.com/hc/en-us/articles/47345171478163)); page blocked our fetch | — | — | — |
| **Bluebeam Max** (2026 premium tier) | Natural-language analysis of **existing markups** and document text: counting, grouping, room/area tables, spec conflicts ([IMAGINiT](https://resources.imaginit.com/how-tos/how-estimators-can-use-bluebeam-max-to-support-faster-takeoffs)). Symbol finding remains VisualSearch, an example-based match with rotation and scale options ([Novedge](https://novedge.com/blogs/design-news/bluebeam-tip-automate-symbol-counts-with-visualsearch-and-a-saved-count-tool)) | Reads **embedded viewport scales** from AutoCAD PDFs ("Use Embedded Scale"); Revit exports lack them ([Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/embedded-scale-units-in-pdf-exports-missing-feature/td-p/13644739)) | Results "should not be treated as final bid quantities without review" | No takeoff API found |
| **PlanSwift / On-Screen Takeoff (ConstructConnect "Takeoff Boost")** | Auto Takeoff gives a page of linears, areas and counts; net area with walls subtracted; GWB and ACT ceilings from hatch patterns; untagged windows as wall openings; Auto Count from one picked symbol ([release notes](https://help.constructconnect.com/planswift-historical-release-notes-52/planswift-with-takeoff-boost-ai-powered-tools-release-notes-2026-05-06-2752)) | **Auto Scale reads the scale from the plans** (same source) | "Up to 95% faster". The article names failure modes: low-res scans, unusual symbols, irregular geometry, crowded pages, missing sheets ([ConstructConnect](https://www.constructconnect.com/blog/are-ai-takeoffs-accurate-in-2026)) | No public API |
| **Trimble MEP estimating** (2026) | Auto scale and sheet naming across a set; symbol recognition with confidence-ranked review; auto conduit routing ([press](https://news.trimble.com/New-Trimble-AI-Takeoff-Capabilities-Cut-MEP-Estimating-Time-and-Increase-Accuracy)) | **About 300,000 scales set per month; 97% needed no manual change** across more than 4,000 US contractors ([Trimble blog](https://www.trimble.com/en/blog/construction/article/actual-results-mep-estimators-ai-assisted-takeoff)) | No count accuracy or false-positive rates published. Its time-savings arithmetic is internally inconsistent (60% claimed versus 40% computed) | — |
| **Autodesk Takeoff (ACC / "Forma Takeoff")** | Symbol Detection: box one sample, review matches. Only 90°-increment rotations; clutter degrades it; excludes text ([help](https://help.autodesk.com/cloudhelp/ENU/Takeoff-Takeoff/files/Symbol_Detect.html)) | — | — | **Yes**: APS Takeoff API reads packages, types and takeoff items (3-legged OAuth) ([APS](https://aps.autodesk.com/en/docs/acc/v1/reference/http/takeoff-projects-project_id-packages-package_id-takeoff-items-GET)). This is a data API, not a detection API |
| **Countfire** (electrical) | Auto counts symbols across a set ([countfire.com](https://www.countfire.com/)) | — | 41.9M items auto-counted in 2025, a usage figure rather than accuracy ([blog](https://www.countfire.com/blog/year-in-review-2025)) | — |
| **Exayard** | Natural-language takeoff, Auto Count, Auto Measurements, "automatic scale detection"; 32 trades ([exayard.com](https://www.exayard.com/)) | Claimed | The accuracy FAQ answer was blank | **Yes**: MCP, REST, webhooks, CLI on paid plans (same source) |
| **Downtobid** | Bid package detection, sheet renaming, scope review. **No takeoff** ([HuntScreens](https://huntscreens.com/products/downtobid)) | — | — | — |
| **ProEst** (Autodesk) | Estimating database. No AI takeoff evidence found | — | — | — |

**What these products have in common:**

- Every vendor does scale detection by reading the plan. PlanSwift says so explicitly, and Trimble's 97% supports
  it. Bluebeam honors embedded PDF viewport scale.
- Walls are found by parallel-line detection (Togal). Areas come from closed-boundary filling (Kreo's bucket fill,
  Togal).
- Symbols are found by example-based visual search, with review UIs ranked by confidence (Bluebeam, Autodesk,
  Trimble, PlanSwift).
- Every product requires human review.
- No vendor publishes an accuracy methodology. The only independent comparison is Handoff-H1, where the best
  system beats professionals on coverage but **not on quantity precision** (78.8% versus 87.9% at P@25%)
  ([arXiv 2608.15032](https://arxiv.org/html/2608.15032)).
- **Gap TakeoffSpeed can own:** quantities that come with an audit trail and a stated tolerance.

---

## 4. Techniques and open-source tools for measuring from drawings

### 4.1 PDF vector extraction

| Tool | What it gives | Production-grade? | License |
|---|---|---|---|
| **pdf.js `getOperatorList`** (already used in `lib/multipass/ingest/vector-paths.ts`, `pdfjs-dist ^6.3`) | Raw operator stream. You walk the CTM, line width, dash and marked-content (OCG) state yourself ([API](https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib-PDFPageProxy.html)). OPS numbering changes between versions, so don't hard-code it ([source history](https://lists.alioth.debian.org/pipermail/pkg-javascript-commits/2014-June/008235.html)) | Yes. Mozilla's renderer; runs in Node | Apache-2.0 |
| **PyMuPDF `Page.get_drawings()`** (MuPDF 1.28) | Paths as dicts with items `l`, `re`, `qu`, `c` plus color, width, dashes, fill. "Always returns all paths": it ignores show/hide instructions, so filter OCG layers yourself ([recipes](https://pymupdf.readthedocs.io/en/latest/recipes-drawing-and-graphics.html)). Fastest Python PDF library in its own benchmark ([about](https://pymupdf.readthedocs.io/en/latest/about.html)) | Yes | **AGPL or commercial** from Artifex. The commercial license matters for a SaaS backend |
| **pdfplumber** (pdfminer.six) | `chars`, `lines`, `rects`, `curves` with attributes; line-intersection table extraction. "Works best on machine-generated PDFs"; slower than PyMuPDF ([GitHub](https://github.com/jsvine/pdfplumber)) | Yes for tables | MIT |
| **PDFium** (pypdfium2) | Path objects and segments through `FPDFPath_*` | Yes, Chrome's engine | BSD/Apache |

Recommendation: keep pdf.js as the production producer. Add PyMuPDF only as an **offline second oracle** for
regression tests, so the AGPL code never ships. If the two disagree on path totals for a sheet, that's a parser
bug signal.

### 4.2 Scale calibration

Ranked by reliability:

1. **Embedded PDF measurement dictionaries.** A viewport (`/VP`) with a `/Measure` rectilinear dictionary maps
   page units to real units. Its `R` entry holds the scale string and `CYX` covers unequal axes (ISO 32000-1
   Tables 260 and 262, per [ABCpdf docs](https://www.websupergoo.com/helppdfnet/source/9-abcpdf.elements/12-interactive/1487-viewportelement/default.htm)).
   AutoCAD writes these per viewport and Revit does not
   ([Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/embedded-scale-units-in-pdf-exports-missing-feature/td-p/13644739)).
   When present, this is exact.
2. **Printed scale text per view** ("1/4" = 1'-0"" under each view title or in the title block), read from the text
   layer or by a VLM. This is what PlanSwift and Trimble automate. Trimble's 97% no-correction rate
   ([Trimble](https://www.trimble.com/en/blog/construction/article/actual-results-mep-estimators-ai-assisted-takeoff))
   suggests it works on most sheets. The risk is several views at different scales on one sheet, so assign each
   view region its own scale.
3. **Dimension-string regression.** Pair each parsed dimension value with the vector length between its extension
   lines or arrowheads, then fit page-units-per-foot as a robust median over many pairs. This checks (1) and (2),
   and catches "NTS" views and sheets reduced in print. Monaverse refuses pixel-only scaling for this reason
   ([Monaverse](https://monaverse.com/help/floor-plan-dimensions-and-scale)). Research on learned scale inference:
   [ASCE 2024](https://ascelibrary.com/doi/10.1061/9780784485248.087).
4. **Graphic scale bar.** Detect it and measure it in vectors. This is the last resort, and the only one that
   survives a sheet printed at the wrong size.

Rule: a quantity is final only when two independent scale sources agree within tolerance. Otherwise it shows `—`
and needs review, per the CLAUDE.md rule "no invented data".

### 4.3 Floor-plan parsing and symbol spotting research

**Vector CAD panoptic symbol spotting (FloorPlanCAD):**

- CADSpotting reports 87.4 PQ versus 83.3 for SymPoint and 68.9 for CADTransformer
  ([arXiv 2412.07377](https://arxiv.org/pdf/2412.07377)).
- SymPoint-V2 and DPSS (with ArchCAD-400K) claim a few points more
  ([ArchCAD-400K](https://www.researchgate.net/publication/390321835_ArchCAD-400K_An_Open_Large-Scale_Architectural_CAD_Dataset_and_New_Baseline_for_Panoptic_Symbol_Spotting)).
- 2026 papers: PolarSym (+1.73 PQ over a reproduced SymPoint-V2; [arXiv 2608.11793](https://arxiv.org/abs/2608.11793))
  and TextCAD, which fuses primitives with text annotations ([arXiv 2607.12678](https://arxiv.org/abs/2607.12678)).
- These models consume **vector primitives**, the same representation our PDFs give us. They are research-grade:
  trained on Chinese residential and commercial CAD, with uncertain code and license status.
- Use them as the long-term path for untagged symbols (doors, windows, fixtures) in our vector paths.

**Raster floor-plan reconstruction:**

- Raster2Seq (SIGGRAPH '26) reports RoomF1 of 88.7 on CubiCasa5K and 97.0 on Raster2Graph
  ([arXiv 2602.09016](https://arxiv.org/pdf/2602.09016), [weights](https://huggingface.co/haopt/Raster2Seq)).
- The older Raster-to-Vector baseline is about 90% precision and recall
  ([PapersWithCode](https://cs.paperswithcode.com/paper/raster-to-vector-revisiting-floorplan)).
- All of these target residential plan images, not commercial CDs.

**YOLO-family symbol detection on construction drawings:**

- YOLOv8 reaches 82.5% mAP@50 on 34 electrical service-key classes from 45 scanned plans
  ([SkeySpot](https://arxiv.org/html/2508.10449v1)).
- On industry drawings: YOLO 79% mAP versus Faster R-CNN 83%
  ([Jamieson et al.](https://rgu-repository.worktribe.com/output/2418851)).
- Current detectors: **RF-DETR**, Apache-2.0 up to Large, for accuracy; YOLO26, under AGPL or enterprise license,
  for edge use ([Roboflow](https://roboflow.com/blog/best-computer-vision-models)).
- Roboflow says a specialized detector beats a VLM call for pixel-accurate boxes
  ([Roboflow on Gemini 3.5 Flash](https://blog.roboflow.com/use-gemini-3-5-flash-vision/)).

### 4.4 Raster-to-vector for scanned sheets

- **LSD line detector:** OpenCV `createLineSegmentDetector` was removed in 4.1.0–4.5.3 over a license conflict and
  later restored ([OpenCV docs](https://docs.opencv.org/4.12.0/javadoc/org/opencv/imgproc/LineSegmentDetector.html)).
  Hough transforms and morphology are always available.
- **Deep vectorization of technical drawings** (ECCV 2020): cleanup, then primitive estimation; trained on synthetic
  data plus vectorized scans
  ([paper](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123580579.pdf)).
- **Potrace** traces outlines rather than centerlines, so it is a poor fit for wall lengths.
- **Production reality:** raster wall extraction plus OCR'd-dimension calibration can produce *reviewable* geometry.
  Kreo and the ConstructConnect article both say AI is weakest on scans
  ([ConstructConnect](https://www.constructconnect.com/blog/are-ai-takeoffs-accurate-in-2026)).

### 4.5 CAD and BIM ingestion

| Format | Tool | Status |
|---|---|---|
| DXF | **ezdxf** (MIT; R12–R2018 read and write) ([docs](https://ezdxf.readthedocs.io/en/stable/introduction.html)) | Production-grade for DXF. Blocks, INSERTs and DIMENSION entities give exact counts and lengths. Cannot read DWG directly |
| DWG | **ODA Drawings SDK** (reads R12–2025 "100% of the data"; writes; PDF import and export) ([ODA](https://www.opendesign.com/products/drawings)); free ODA File Converter for DWG→DXF (recommended by [ezdxf](https://ezdxf.readthedocs.io/en/stable/introduction.html)) | Production-grade. The commercial SDK needs ODA membership; pricing is not public. Check the converter's terms before server use |
| DWG | **LibreDWG** (GPLv3, "beta"; some R2010+ entities skipped; writes only R1.1–R2000) ([GNU](https://www.gnu.org/software/libredwg/)) | **Not production-grade** for commercial ingestion |
| IFC | **IfcOpenShell 0.9.1** with OpenCASCADE, CGAL and Manifold kernels and shape and volume utilities ([docs](https://docs.ifcopenshell.org/ifcopenshell-python/geometry_processing.html), [util.shape](https://docs.ifcopenshell.org/autoapi/ifcopenshell/util/shape/index.html)) | Production-grade. When a model exists, read quantities straight from it |

---

## 5. Hype versus evidence

| Claim | Evidence | Verdict |
|---|---|---|
| "VLMs can do takeoff" | Raw frontier models score 35–61 composite (Handoff-H1); DrawingVQA QTO scores 25–42 versus 96.6 for professionals | **Not on their own.** They read well and measure poorly |
| "98% accurate AI takeoff" (Togal; Beam via GetApp) | No methodology. Beam's figure depends on human QA | Marketing |
| Kreo Auto Measure 3.0 at 94% outline accuracy | Vendor A/B numbers, no dataset | Plausible for vector plans. Unverified |
| Auto scale detection works | Trimble: 97% no-change over about 300k scales per month (vendor data, large n) | **Believable** and matches our design |
| VLM symbol counting is unreliable | AECV-Bench (untagged, raster, older models) versus ours (tagged, vector, 2026 models, about 1% MAPE) | Depends on the task. Counting tags and text is good; counting graphic symbols needs a detector or vector matching |
| Higher image resolution fixes measurement | In our runs the zoom tool did not consistently improve measurement MAPE. Opus 5.5 got worse (12.8% hi to 18.3% zoom). Fable 5.1 (33.6% to 13.6%) and Sonnet 5.5 (27.5% to 25.1%) improved but stayed far above 5% | **No.** Resolution helps reading, not metric estimation |
| Gemini leads drawing benchmarks | Leads AECV-Bench counting and DrawingVQA (2025–26 versions); trails Claude and GPT on Roboflow text localization | **Worth benchmarking.** Not proven on our set |

---

## 6. RECOMMENDATION

### 6.1 Principle

- Use **code for numbers and models for judgment.** Every length, area and count that reaches a bid is computed
  from PDF vectors (or CAD/IFC entities) with `computeBidTotals`-style integer arithmetic.
- VLMs classify what was drawn (this path is a wall of type A3B; this hatch is ACT ceiling), read text and
  schedules, choose scales per view, and act as adversarial verifiers.
- When a vector quantity and a model reading disagree beyond tolerance, the result is `—` and goes to review, never
  a blend of the two.

### 6.2 Task-by-task stack

| Task | Primary | Independent cross-check | Scanned-plan fallback |
|---|---|---|---|
| **Sheet classification** (discipline, sheet type, title block fields, view regions) | Text layer and title block regex, plus **Claude Haiku 5.5** on a low-res render. Haiku already scored 1.00 on schedules and 0.94 on dimension F1 at $0.001–0.002 per call (our results) | Sonnet 5.5 on disagreements | Same, after OCR |
| **Text / dimension strings** | **PDF text layer** (exact). VLM only where text is outlined or SHX strokes | Opus 5.5 or GPT-6.1 Sol reading crops at 2576 px (Claude) or `original` (GPT) | **Azure DI Layout with `ocrHighResolution`** at about 200–250 DPI (under 10k px); PaddleOCR PP-OCRv6 self-hosted second read |
| **Schedules** (door, window, finish, fixture) | Vector ruling-line cell reconstruction plus text-layer fill | VLM transcription (Opus 5.5 / Astra / Haiku all at about 1.00 here); require cell-level agreement | Azure Layout tables (rotated tables supported) plus VLM |
| **Specs / project manual** | Native PDF text, section parsing | VLM extraction of materials and requirements per section | **Mistral OCR 4** (cheap, block-level confidence) or Azure Layout |
| **Symbol counting** | Tagged items: text-layer tag matching, exact. Untagged: **vector signature matching** (repeated identical path groups / XObjects) seeded by one VLM-identified example | VLM count per crop (our ~1% MAPE result) | Fine-tuned **RF-DETR** on our own labeled sheets (Apache-2.0); Gemini `box_2d` as zero-shot candidate generator; VLM verify |
| **Wall / linear geometry** | **Vector paths** (current pipeline, 1.5% on our set). Parallel-pair centerlines, layer, OCG and line-weight filtering | VLM labels numbered candidate paths on a rendered overlay. It **classifies, never measures** | Raster line extraction (LSD/Hough/morphology), then the same classifier, flagged low-confidence and human-verified |
| **Areas** (rooms, floors, ceilings, roofs) | Closed polygons from vector boundaries; room-name text-in-polygon association; hatch-pattern classification for ceilings | Printed room areas (when present) and VLM area estimate as sanity bound (our best ~3–4%) | Raster2Seq-style polygonization (research-grade) plus mandatory review |
| **Scale calibration** | 1) PDF `/VP` `/Measure` dictionaries; 2) per-view printed scale text | 3) dimension-string regression on vector dimension lines; must agree within tolerance | Dimension-string regression on OCR'd dims plus scale bar |
| **DWG / DXF / IFC uploads** | ezdxf (DXF), ODA converter or SDK (DWG), IfcOpenShell (IFC). Exact counts and lengths from entities | Compare to the PDF-derived quantities | — |

**Model choice for reading and judgment, given today's evidence:**

- **Primary:** Opus 5.5. It matched or beat Fable 5.1 on every task in our set at about a third of the cost, and
  ranks #2 on Roboflow.
- **Second opinion from another vendor:** GPT-6.1 Sol. It costs half as much as Opus 5.5 at list price, is
  near-Astra quality, and has the best text localization measured (74–77%). Use GPT-6 Astra where `original`-detail
  full-sheet reading pays off.
- **Fable 5.1:** not needed in the reading loop; keep it for adversarial review.
- **Haiku 5.5:** for bulk classification.
- **Gemini 3.8 Flash and Gemini 4 Argon:** candidates pending benchmarks B1 and B2.

### 6.3 Accounts and keys to request

| Account | Why | Priority |
|---|---|---|
| **Google AI Studio / Vertex AI (Gemini API) key**; request Gemini 4 Argon access | The only frontier family not yet benchmarked. Leads both construction-drawing benchmarks; native boxes and masks; agentic vision zoom | **High** |
| **Azure AI Document Intelligence (Foundry) resource, S0 tier** | `ocrHighResolution` for scanned sheets; rotated table extraction | **High** (needed for scanned fallback) |
| **Artifex commercial license for PyMuPDF** (only if PyMuPDF ever runs in production) | AGPL otherwise | Medium (offline oracle use needs no license if never distributed or served; confirm with counsel) |
| **AWS (Textract)** and **Google Cloud Document AI** | Only for a one-time OCR bake-off against Azure | Low–medium |
| **Mistral API key** | OCR 4 for scanned spec books; cheap | Low–medium |
| **GPU host** (e.g., an existing cloud account) | Self-host PaddleOCR / RF-DETR training for symbol detection on scans | Medium (when scanned volume justifies it) |
| **ODA membership** | Only if DWG uploads become a product requirement | Low |
| Request **Handoff-H1 benchmark data** (research use, on request; [arXiv 2608.15032](https://arxiv.org/html/2608.15032)); download **AECV-Bench** ([GitHub](https://github.com/AECFoundry/AECV-Bench)) | More ground truth beyond our single job | **High** (no account cost) |

No new keys are needed for the vector-first changes. They use the Anthropic and OpenAI keys we already have.

### 6.4 What to benchmark next on our own test set

Ordered by expected value.

- **B1. OpenAI at `original` detail.**
  - Re-run `dimensions`, `count`, `measure` and `schedule` with `detail: "original"` on `gpt-6-astra` and
    `gpt-6.1-sol`. Size full-sheet renders to at most 30,000 patches (about 6,780x4,520 for 36x24).
  - Also re-test `gpt-6-sol` / `gpt-6-luna` now that the Sep 25 encoding bug is fixed. Any earlier Sol/Luna runs are
    invalid.
  - Expect gains on reading, not on measurement.
- **B2. Gemini.** `gemini-3.8-flash` (and `gemini-4-argon` if accessible) with `media_resolution: ultra_high` on our
  crops, with and without code execution (agentic zoom). Same tasks and scorer. Add a `box_2d` symbol-localization
  task scored by IoU against the estimator's PlanSwift count marks.
- **B3. VLM classifies, code measures. This is the decisive test.**
  - Render each plan crop with candidate vector paths numbered and color-coded.
  - Ask Opus 5.5, GPT-6.1 Sol and Gemini which IDs are walls and which wall type each is.
  - Compute lengths from the chosen vectors and score total and per-type wall length against the estimator's
    markups.
  - Target: per-type wall length within 2%, versus 1.5% today for untyped totals.
- **B4. Scale calibration audit.**
  - On every sheet and view in the set, compare the auto-chosen scale (VP/Measure, then printed text, then
    dimension regression) against the estimator's PlanSwift scale.
  - Report agreement rate and every disagreement. Target: 100% agreement, or a correct refusal.
- **B5. Scanned-plan OCR bake-off.**
  - Rasterize our vector sheets at 150, 200 and 300 DPI. Add scan noise, ±2° skew, and a print-and-scan of a few
    sheets.
  - Run Azure Layout (with and without `ocrHighResolution`), Textract, Google Enterprise OCR, PaddleOCR PP-OCRv6,
    and VLM crops.
  - Score dimension-string F1, including vertical and rotated strings, and schedule cell accuracy against the text
    layer as ground truth. This is free ground truth.
- **B6. Untagged symbol counting** (doors by swing, plumbing fixtures, receptacles): vector-signature matching versus
  VLM-per-crop versus Gemini boxes. Score MAPE and position-level precision and recall against PlanSwift count
  marks.
- **B7. Areas.** Closed-polygon room areas from vectors versus estimator areas, and versus printed room areas.
  Target within 1%.
- **B8. Generalization.** Our benchmark is n=1 job. Add at least 3–5 more sets: one AutoCAD export (with VP scales),
  one Revit export (no VP scales), one scanned set, one MEP-heavy set, plus Handoff-H1's residential sets if granted.
  Report per-set, not pooled.

### 6.5 What not to do

- Don't buy a commercial takeoff product as the engine. None publishes verifiable accuracy. Their methods match
  what our vector pipeline already does, and their APIs (Kreo, Exayard, Autodesk) don't expose better geometry.
- Don't spend more effort on prompting VLMs to measure undimensioned lengths or areas from pixels. Our data (10.8%
  MAPE at best) and every published benchmark say this is the wrong tool.
- Don't treat LibreDWG, research symbol-spotting checkpoints, or Raster2Seq as production components without our
  own validation.
