"""Re-score saved benchmark answers against the current tasks.json (no API calls).

usage: python3 -I vision-benchmark/rescore.py results/run1.jsonl
"""
import sys, json, os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('rb', os.path.join(HERE, 'run_benchmark.py'))
src = open(os.path.join(HERE, 'run_benchmark.py')).read()
ns = {}
exec(src.split('def call(')[0].split("IMG, RUN, BUDGET")[0] + src[src.index('PROMPTS = {'):src.index('def call(')], ns)
tasks = {t['id']: t for t in json.load(open(os.path.join(HERE, 'tasks.json')))}
f = sys.argv[1]
rows = [json.loads(l) for l in open(f)]
for r in rows:
    if 'answer' in r and r['task'] in tasks:
        r['score'] = ns['score'](tasks[r['task']], r['answer'])
open(f, 'w').write(''.join(json.dumps(r) + '\n' for r in rows))
print(f'rescored {len(rows)} rows')
