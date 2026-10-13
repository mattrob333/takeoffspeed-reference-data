"""Ask GPT-6 Astra for an independent second opinion (text, optionally with images).

usage: python3 -I tools/ask_gpt.py "<question>" [image.png ...]
Prints the answer. Use it to cross-check a reading or a formula with a model from a different provider.
"""
import sys, os, base64
from openai import OpenAI
q, *imgs = sys.argv[1:]
content = [{'type': 'input_image', 'image_url': 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode(), 'detail': 'high'} for p in imgs]
content.append({'type': 'input_text', 'text': q})
r = OpenAI(api_key=os.environ['OPENAI_API_KEY']).responses.create(model='gpt-6-astra', reasoning={'effort': 'high'}, input=[{'role': 'user', 'content': content}])
print(r.output_text)
print(f'[gpt-6-astra tokens in {r.usage.input_tokens} out {r.usage.output_tokens}]', file=sys.stderr)
