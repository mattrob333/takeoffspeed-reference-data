"""Text-layer answer keys for the vision benchmark: dimension strings and tags with positions."""
import re, json, os
import pymupdf
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIM = re.compile(r"""^(\d+'-\d+(?: \d+/\d+)?"|\d+(?: \d+/\d+)?"|\d+'-\d+")$""")
# Every dimension token inside any text (notes and labels included): 12'-6", 9' - 0", 8'-3 1/4", 2 3/8", 1/2", 11"
DIM_TOKEN = re.compile(r"""\d+' ?- ?\d+(?: \d+/\d+)?"|(?<![\d/'])\d+ \d+/\d+"|(?<![\d/' ])\d+/\d+"|(?<![\d/'])\d+"(?!\d)""")
TAG = re.compile(r'^[A-D]\d[A-C]$')

def sheet_file(sheet):
    for x in json.load(open(os.path.join(ROOT, 'reference/sheets/index.json'))):
        if x['sheet'] == sheet and x['pages'] == 1:
            return os.path.join(ROOT, x['file'])
    raise KeyError(sheet)

def spans(sheet):
    p = pymupdf.open(sheet_file(sheet))[0]
    W, H = p.rect.width, p.rect.height
    out = []
    for b in p.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            t = ' '.join(s['text'] for s in l['spans']).strip()
            if not t:
                continue
            x0, y0, x1, y1 = l['bbox']
            out.append({'text': t, 'cx': (x0 + x1) / 2 / W, 'cy': (y0 + y1) / 2 / H, 'box': [x0 / W, y0 / H, x1 / W, y1 / H]})
    return out

def inside(s, box, margin=0.0):
    x0, y0, x1, y1 = s['box']
    return x0 >= box[0] - margin and y0 >= box[1] - margin and x1 <= box[2] + margin and y1 <= box[3] + margin
