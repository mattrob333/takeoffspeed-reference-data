"""Benchmark variant: the model gets a zoom tool that re-renders any region of the sheet from the PDF.

usage: python3 -I vision-benchmark/run_agentic.py <image_dir> <run_name> <budget_usd> model[,model...] task_id[,task_id...]
Claude models use tool use; GPT-6 Astra uses Responses API function calling. Max 10 zooms per task. Earlier images are re-sent every turn, so Claude calls use prompt caching and the budget is shared across parallel runs via the results file.
"""
import sys, os, json, base64, io, re, collections
import anthropic, pymupdf
from openai import OpenAI
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textlayer import sheet_file
IMG, RUN, BUDGET, MODELS, TASKS = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4].split(','), sys.argv[5].split(',')
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'results', f'{RUN}.jsonl')
src = open(os.path.join(HERE, 'run_benchmark.py')).read()
ns = {'re': re, 'collections': collections, 'json': json}
exec(src[src.index('PRICE = {'):src.index('client = anthropic')], ns)
exec(src[src.index('PROMPTS = {'):src.index('def call(')], ns)
PRICE, PROMPTS, score = ns['PRICE'], ns['PROMPTS'], ns['score']
claude = anthropic.Anthropic(api_key=os.environ['DUTYGRAPH_ANTHROPIC_API_KEY'])
oai = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
spent = sum(json.loads(l)['usd'] for l in open(OUT)) if os.path.exists(OUT) else 0.0
ZOOM = {'name': 'zoom', 'description': 'Re-render a rectangular region of the sheet at high resolution (up to 2576 px on the long edge) and return it as an image. Coordinates are fractions (0..1) of the ORIGINAL overview image you were given, origin top-left. Use it to read small text, check symbols, and measure precisely.',
        'input_schema': {'type': 'object', 'properties': {k: {'type': 'number'} for k in ('x0', 'y0', 'x1', 'y1')}, 'required': ['x0', 'y0', 'x1', 'y1'], 'additionalProperties': False}}

def zoom_png(task, a):
    p = pymupdf.open(sheet_file(task['sheet']))[0]
    r = p.rect; b = task['box']
    fx0, fx1 = sorted((max(0, min(1, a['x0'])), max(0, min(1, a['x1'])))); fy0, fy1 = sorted((max(0, min(1, a['y0'])), max(0, min(1, a['y1']))))
    X0 = b[0] + (b[2] - b[0]) * fx0; X1 = b[0] + (b[2] - b[0]) * max(fx1, fx0 + 0.01)
    Y0 = b[1] + (b[3] - b[1]) * fy0; Y1 = b[1] + (b[3] - b[1]) * max(fy1, fy0 + 0.01)
    clip = pymupdf.Rect(r.width * X0, r.height * Y0, r.width * X1, r.height * Y1)
    z = min(2576 / max(clip.width, clip.height), 12)
    return base64.standard_b64encode(p.get_pixmap(matrix=pymupdf.Matrix(z, z), clip=clip).tobytes('png')).decode()

def run_claude(task, model):
    prompt, schema = PROMPTS[task['kind']]
    prompt = (task.get('prompt') or prompt) + '\n\nYou may call the zoom tool (up to 10 times) to inspect regions at higher resolution. When done, call submit_answer exactly once.'
    submit = {'name': 'submit_answer', 'description': 'Submit the final answer.', 'input_schema': schema, 'strict': True}
    img = base64.standard_b64encode(open(os.path.join(IMG, task['images']['hi']), 'rb').read()).decode()
    msgs = [{'role': 'user', 'content': [{'type': 'image', 'source': {'type': 'base64', 'media_type': 'image/png', 'data': img}}, {'type': 'text', 'text': prompt}]}]
    tin = tout = zooms = 0
    for _ in range(20):
        with claude.messages.stream(model=model, max_tokens=32000, output_config={'effort': 'high'}, tools=[ZOOM, submit], messages=msgs, cache_control={'type': 'ephemeral'}) as st:
            m = st.get_final_message()
        u = m.usage
        # cache writes bill at 1.25x input, cache reads at 0.1x: fold them into input-equivalent tokens
        tin += u.input_tokens + 1.25 * (u.cache_creation_input_tokens or 0) + 0.1 * (u.cache_read_input_tokens or 0); tout += u.output_tokens
        msgs.append({'role': 'assistant', 'content': m.content})
        res = []
        for b in m.content:
            if b.type == 'tool_use' and b.name == 'submit_answer':
                return b.input, tin, tout, zooms
            if b.type == 'tool_use' and b.name == 'zoom':
                zooms += 1
                res.append({'type': 'tool_result', 'tool_use_id': b.id, 'content': [{'type': 'image', 'source': {'type': 'base64', 'media_type': 'image/png', 'data': zoom_png(task, b.input)}}] if zooms <= 10 else 'zoom limit reached; submit your answer'})
        if not res:
            msgs.append({'role': 'user', 'content': 'Call submit_answer with your final answer now.'})
        else:
            msgs.append({'role': 'user', 'content': res})
    return {}, tin, tout, zooms

def run_gpt(task, model):
    prompt, schema = PROMPTS[task['kind']]
    prompt = (task.get('prompt') or prompt) + '\n\nYou may call the zoom tool (up to 10 times) to inspect regions at higher resolution. When done, call submit_answer exactly once.'
    tools = [{'type': 'function', 'name': 'zoom', 'description': ZOOM['description'], 'parameters': ZOOM['input_schema'], 'strict': True},
             {'type': 'function', 'name': 'submit_answer', 'description': 'Submit the final answer.', 'parameters': schema, 'strict': True}]
    img = base64.standard_b64encode(open(os.path.join(IMG, task['images']['hi']), 'rb').read()).decode()
    items = [{'role': 'user', 'content': [{'type': 'input_image', 'image_url': f'data:image/png;base64,{img}', 'detail': 'high'}, {'type': 'input_text', 'text': prompt}]}]
    tin = tout = zooms = 0
    for _ in range(20):
        r = oai.responses.create(model=model, reasoning={'effort': 'high'}, tools=tools, input=items, max_output_tokens=32000)
        cached = getattr(r.usage.input_tokens_details, 'cached_tokens', 0) or 0
        # cached input assumed billed at 0.5x (conservative)
        tin += r.usage.input_tokens - 0.5 * cached; tout += r.usage.output_tokens
        items += [o.model_dump(exclude_none=True) for o in r.output]
        calls = [o for o in r.output if o.type == 'function_call']
        if not calls:
            items.append({'role': 'user', 'content': 'Call submit_answer with your final answer now.'}); continue
        for c in calls:
            a = json.loads(c.arguments)
            if c.name == 'submit_answer':
                return a, tin, tout, zooms
            zooms += 1
            items.append({'type': 'function_call_output', 'call_id': c.call_id, 'output': 'image follows' if zooms <= 10 else 'zoom limit reached; submit your answer'})
            if zooms <= 10:
                items.append({'role': 'user', 'content': [{'type': 'input_image', 'image_url': f'data:image/png;base64,{zoom_png(task, a)}', 'detail': 'high'}, {'type': 'input_text', 'text': f'zoom result for ({a["x0"]:.3f},{a["y0"]:.3f})-({a["x1"]:.3f},{a["y1"]:.3f})'}]})
    return {}, tin, tout, zooms

tasks = {t['id']: t for t in json.load(open(os.path.join(HERE, 'tasks.json')))}
for tid in TASKS:
    for model in MODELS:
        spent = sum(json.loads(l)['usd'] for l in open(OUT)) if os.path.exists(OUT) else 0.0
        if spent >= BUDGET:
            print('budget reached'); sys.exit()
        t = tasks[tid]
        try:
            ans, tin, tout, zooms = (run_gpt if model.startswith('gpt') else run_claude)(t, model)
            pin, pout = PRICE[model]; usd = (tin * pin + tout * pout) / 1e6
            rec = {'task': tid, 'kind': t['kind'], 'model': model, 'res': 'zoom-tool', 'zooms': zooms, 'inputTokens': tin, 'outputTokens': tout, 'usd': round(usd, 5), 'score': score(t, ans), 'answer': ans}
        except Exception as e:
            rec = {'task': tid, 'kind': t['kind'], 'model': model, 'res': 'zoom-tool', 'error': f'{type(e).__name__}: {e}'[:400], 'usd': 0}
        spent += rec['usd']
        open(OUT, 'a').write(json.dumps(rec) + '\n')
        s = rec.get('score', {})
        print(f"{tid:24} {model:18} zooms {rec.get('zooms')} ${rec['usd']:.3f} total ${spent:.2f}  {s.get('meanAbsPctError', s.get('f1', rec.get('error', '')))}", flush=True)
