"""Summarize benchmark results: per model × resolution, per task kind.

usage: python3 -I vision-benchmark/summarize.py results/run1.jsonl [...]  > vision-benchmark/RESULTS.md
"""
import sys, json, collections, statistics
rows = [json.loads(l) for f in sys.argv[1:] for l in open(f)]
by = collections.defaultdict(list)
for r in rows:
    by[(r['kind'], r['model'], r['res'])].append(r)
print('| Task kind | Model | Resolution | Calls | Errors | Precision | Recall | F1 / count or cell accuracy | Exact tag counts | Mean cost per scored call (USD) |')
print('|---|---|---|---:|---:|---:|---:|---:|---:|---:|')
for (kind, model, res), rs in sorted(by.items(), key=lambda kv: (kv[0][0], -statistics.mean([x['score'].get('f1', x['score'].get('countAccuracy', x['score'].get('cellAccuracy', 0))) if 'score' in x else 0 for x in kv[1]]))):
    ok = [x for x in rs if 'score' in x]
    err = len(rs) - len(ok)
    m = lambda k: f"{statistics.mean(x['score'][k] for x in ok):.3f}" if ok and k in ok[0]['score'] else ''
    main = m('f1') or m('countAccuracy') or m('cellAccuracy')
    exact = f"{sum(x['score']['exactTags'] for x in ok)}/{sum(x['score']['tags'] for x in ok)}" if ok and 'exactTags' in ok[0]['score'] else ''
    if ok and 'meanAbsPctError' in ok[0]['score']:
        main = f"MAPE {statistics.mean(x['score']['meanAbsPctError'] for x in ok):.1f}%"
        exact = f"{sum(x['score']['exact'] for x in ok)}/{sum(x['score']['items'] for x in ok)} exact, {sum(x['score']['within5'] for x in ok)} within 5%"
    cost = statistics.mean(x['usd'] for x in (ok or rs))  # errored calls returned no usage
    print(f'| {kind} | {model} | {res} | {len(rs)} | {err} | {m("precision")} | {m("recall")} | {main} | {exact} | {cost:.4f} |')
print()
print('Resolution: `hi` = 2,576 px long edge, `lo` = 1,280 px (Claude: as sent; OpenAI: sent with `detail: "high"`, which '
      'gpt-6-astra and the Sol models downscale to about 2,500 32-px patches, roughly 1,600x1,600 px). `orig` = OpenAI only, '
      'rendered by `render_openai.py` at up to 6,000 px long edge and at most 30,000 patches, sent with `detail: "original"` '
      '(not downscaled). `zoom-tool` = `hi` overview plus up to 10 re-rendered 2,576 px zooms (OpenAI zooms also sent with `detail: "high"`).')
