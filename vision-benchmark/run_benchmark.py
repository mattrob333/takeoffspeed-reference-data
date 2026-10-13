"""Run the plan-reading benchmark against several vision models and score against text-layer answer keys.

usage: DUTYGRAPH_ANTHROPIC_API_KEY=... python3 -I vision-benchmark/run_benchmark.py <image_dir> <run_name> <budget_usd> model:res[,model:res...] [task_id,...]
Appends one JSON line per call to vision-benchmark/results/<run_name>.jsonl and stops before the budget is spent.
"""
import sys, os, json, base64, re, collections, threading, concurrent.futures as cf
import anthropic
from openai import OpenAI

IMG, RUN, BUDGET, SPECS = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4].split(',')
ONLY = set(sys.argv[5].split(',')) if len(sys.argv) > 5 else None
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'results', f'{RUN}.jsonl')
# gpt-6-astra: price not published with the API; booked at an assumed conservative $10/$50 per MTok.
PRICE = {'gpt-6-astra': (10, 50), 'claude-fable-5-1': (10, 50), 'claude-opus-5-5': (4, 20), 'claude-sonnet-5-5': (2, 10), 'claude-haiku-5-5': (0.10, 0.50)}
client = anthropic.Anthropic(api_key=os.environ['DUTYGRAPH_ANTHROPIC_API_KEY'])
oai = OpenAI(api_key=os.environ['OPENAI_API_KEY']) if os.environ.get('OPENAI_API_KEY') else None
lock = threading.Lock()
spent = [sum(json.loads(l)['usd'] for l in open(OUT)) if os.path.exists(OUT) else 0.0]
done = {(j['task'], j['model'], j['res']) for j in map(json.loads, open(OUT))} if os.path.exists(OUT) else set()

PROMPTS = {
    'dimensions': ('This image is a crop of a construction drawing. List every dimension string printed in it: feet-and-inch values such as 12\'-6", 8\'-3 1/4", 2\'-0 1/2" and inch-only values such as 11" or 2". '
                   'Copy each exactly as printed. List every printed occurrence (a value printed three times appears three times), including vertical and rotated text and values inside notes or labels '
                   '(e.g. 6" in "6" ABOVE CEILING", 9\'-0" in a ceiling-height tag). Leave out strings cut off by the image edge, and leave out drawing scales (1/4" = 1\'-0").',
                   {'type': 'object', 'properties': {'dimensions': {'type': 'array', 'items': {'type': 'string'}}}, 'required': ['dimensions'], 'additionalProperties': False}),
    'tag-count': ('This image is a crop of an architectural floor plan. Partition (wall) types are marked with diamond-shaped tags containing a code such as A3A, A3B, A6A, A6B, D3A or D3C. '
                  'Count every wall-type tag in the image, by code. Count each printed tag once; do not count the codes in notes, legends or title blocks.',
                  {'type': 'object', 'properties': {'counts': {'type': 'array', 'items': {'type': 'object', 'properties': {'tag': {'type': 'string'}, 'count': {'type': 'integer'}}, 'required': ['tag', 'count'], 'additionalProperties': False}}}, 'required': ['counts'], 'additionalProperties': False}),
    'schedule': ('This image shows a construction drawing sheet with a DOOR SCHEDULE. Transcribe every row of the door schedule: door mark, door type, width, height, door material, frame material and hardware set number, exactly as printed. '
                 'Use an empty string for a blank cell.',
                 {'type': 'object', 'properties': {'rows': {'type': 'array', 'items': {'type': 'object', 'properties': {k: {'type': 'string'} for k in ('mark', 'type', 'width', 'height', 'material', 'frame', 'hardware')},
                  'required': ['mark', 'type', 'width', 'height', 'material', 'frame', 'hardware'], 'additionalProperties': False}}}, 'required': ['rows'], 'additionalProperties': False}),
    'count': ('', {'type': 'object', 'properties': {'items': {'type': 'array', 'items': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'value': {'type': 'number'}}, 'required': ['name', 'value'], 'additionalProperties': False}}}, 'required': ['items'], 'additionalProperties': False}),
    'measure': ('', {'type': 'object', 'properties': {'items': {'type': 'array', 'items': {'type': 'object', 'properties': {'name': {'type': 'string'}, 'value': {'type': 'number'}}, 'required': ['name', 'value'], 'additionalProperties': False}}}, 'required': ['items'], 'additionalProperties': False}),
}

def norm(s):
    s = s.replace('’', "'").replace('′', "'").replace('”', '"').replace('″', '"').replace("''", '"').strip()
    s = re.sub(r"'\s*-\s*", "'-", s)
    return re.sub(r'\s+', ' ', s)

def score(task, ans):
    if task['kind'] == 'dimensions':
        key = collections.Counter(norm(x) for x in task['answer'])
        ign = collections.Counter(norm(x) for x in task['ignore'])
        pred = collections.Counter(norm(x) for x in ans.get('dimensions', []))
        hit = sum((key & pred).values())
        extra = pred - key
        excused = sum((extra & ign).values())
        n_pred = sum(pred.values()) - excused
        p = hit / n_pred if n_pred else 0.0
        r = hit / sum(key.values())
        return {'precision': round(p, 4), 'recall': round(r, 4), 'f1': round(2 * p * r / (p + r), 4) if p + r else 0.0,
                'missed': sorted((key - pred).elements())[:40], 'wrong': sorted((extra - ign).elements())[:40]}
    if task['kind'] in ('count', 'measure'):
        got = {norm(i['name']).upper(): i['value'] for i in ans.get('items', [])}
        errs, per = [], {}
        for k, v in task['answer'].items():
            g = got.get(norm(k).upper())
            e = abs((g if g is not None else 0) - v) / v
            errs.append(e); per[k] = [g, v]
        exact = sum(1 for k, v in task['answer'].items() if got.get(norm(k).upper()) == v)
        within5 = sum(1 for e in errs if e <= 0.05)
        return {'meanAbsPctError': round(100 * sum(errs) / len(errs), 2), 'within5': within5, 'exact': exact, 'items': len(errs),
                'totalKey': round(sum(task['answer'].values()), 2), 'totalGot': round(sum(v[0] or 0 for v in per.values()), 2), 'per': per}
    if task['kind'] == 'schedule':
        got = {norm(r.get('mark', '')): r for r in ans.get('rows', [])}
        cells = right = 0
        wrong = []
        for k in task['answer']:
            g = got.get(norm(k['mark']), {})
            for f in ('mark', 'type', 'width', 'height', 'material', 'frame', 'hardware'):
                if f not in k:
                    continue
                cells += 1
                if norm(g.get(f, '')).upper() == norm(k[f]).upper():
                    right += 1
                else:
                    wrong.append(f"{k['mark']}.{f}: {g.get(f)} vs {k[f]}")
        extra = len(set(got) - {norm(k['mark']) for k in task['answer']})
        return {'cellAccuracy': round(right / cells, 4), 'cells': cells, 'extraRows': extra, 'wrong': wrong[:30]}
    key = task['answer']
    got = {c['tag'].strip().upper(): c['count'] for c in ans.get('counts', [])}
    tags = set(key) | set(got)
    abs_err = sum(abs(key.get(t, 0) - got.get(t, 0)) for t in tags)
    total = sum(key.values())
    return {'exactTags': sum(1 for t in key if got.get(t, 0) == key[t]), 'tags': len(key), 'absError': abs_err, 'countAccuracy': round(max(0, 1 - abs_err / total), 4), 'got': got}

def call(task, model, res):
    img = base64.standard_b64encode(open(os.path.join(IMG, task['images'][res]), 'rb').read()).decode()
    prompt, schema = PROMPTS[task['kind']]
    prompt = task.get('prompt') or prompt
    if model.startswith('gpt'):
        r = oai.responses.create(model=model, reasoning={'effort': 'high'}, max_output_tokens=32000,
            input=[{'role': 'user', 'content': [{'type': 'input_image', 'image_url': f'data:image/png;base64,{img}', 'detail': 'high'}, {'type': 'input_text', 'text': prompt}]}],
            text={'format': {'type': 'json_schema', 'name': task['kind'].replace('-', '_'), 'strict': True, 'schema': schema}})
        pin, pout = PRICE[model]
        usd = (r.usage.input_tokens * pin + r.usage.output_tokens * pout) / 1e6
        try:
            ans = json.loads(r.output_text)
        except Exception:
            ans = {}
        return {'task': task['id'], 'kind': task['kind'], 'model': model, 'res': res, 'stop': r.status, 'inputTokens': r.usage.input_tokens, 'outputTokens': r.usage.output_tokens,
                'usd': round(usd, 5), 'score': score(task, ans), 'answer': ans}
    with client.messages.stream(model=model, max_tokens=32000, output_config={'effort': 'high', 'format': {'type': 'json_schema', 'schema': schema}},
                                messages=[{'role': 'user', 'content': [{'type': 'image', 'source': {'type': 'base64', 'media_type': 'image/png', 'data': img}}, {'type': 'text', 'text': prompt}]}]) as st:
        msg = st.get_final_message()
    text = ''.join(b.text for b in msg.content if b.type == 'text')
    u = msg.usage
    pin, pout = PRICE[model]
    usd = (u.input_tokens * pin + u.output_tokens * pout) / 1e6
    try:
        ans = json.loads(text)
    except Exception:
        ans = {}
    return {'task': task['id'], 'kind': task['kind'], 'model': model, 'res': res, 'stop': msg.stop_reason, 'inputTokens': u.input_tokens, 'outputTokens': u.output_tokens,
            'usd': round(usd, 5), 'score': score(task, ans), 'answer': ans}

tasks = [t for t in json.load(open(os.path.join(HERE, 'tasks.json'))) if not ONLY or t['id'] in ONLY]
jobs = [(t, m, r) for t in tasks for spec in SPECS for m, r in [spec.split(':')] if (t['id'], m, r) not in done]
print(f'{len(jobs)} calls; ${spent[0]:.2f} already spent in this run; budget ${BUDGET}')

def work(job):
    with lock:
        if spent[0] >= BUDGET:
            return None
    try:
        rec = call(*job)
    except Exception as e:
        rec = {'task': job[0]['id'], 'kind': job[0]['kind'], 'model': job[1], 'res': job[2], 'error': f'{type(e).__name__}: {e}'[:300], 'usd': 0}
    with lock:
        spent[0] += rec['usd']
        open(OUT, 'a').write(json.dumps(rec) + '\n')
        s = rec.get('score', {})
        print(f"{rec['task']:16} {rec['model']:18} {rec['res']} ${rec['usd']:.3f} total ${spent[0]:.2f}  {s.get('f1', s.get('countAccuracy', rec.get('error', '')))}", flush=True)
    return rec

with cf.ThreadPoolExecutor(6) as ex:
    list(ex.map(work, jobs))
print(f'done; ${spent[0]:.2f}')
