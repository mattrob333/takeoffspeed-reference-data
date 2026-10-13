"""Build the vision benchmark: crops of real sheets with answer keys from the PDF text layer.

usage: python3 -I vision-benchmark/build_tasks.py <image_dir>
Writes vision-benchmark/tasks.json (answer keys) and the crop images (not committed; rebuilt by this script).
The key holds every dimension token printed inside the crop, including values inside notes.
Two renderings per crop: hi (2576 px long edge, the current model maximum) and lo (1280 px).
"""
import sys, os, json, collections
import pymupdf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textlayer import spans, sheet_file, inside, DIM, DIM_TOKEN, TAG

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
HERE = os.path.dirname(os.path.abspath(__file__))
tasks = []

def render(sheet, box, name):
    p = pymupdf.open(sheet_file(sheet))[0]
    r = p.rect
    clip = pymupdf.Rect(r.width * box[0], r.height * box[1], r.width * box[2], r.height * box[3])
    files = {}
    for res, edge in (('hi', 2576), ('lo', 1280)):
        z = edge / max(clip.width, clip.height)
        path = os.path.join(OUT, f'{name}-{res}.png')
        p.get_pixmap(matrix=pymupdf.Matrix(z, z), clip=clip).save(path)
        files[res] = os.path.basename(path)
    return files

# 1. Dimension strings: 2x2 grid over the dimensioned area of each sheet.
for sheet in ['A-120', 'A-130', 'A-131', 'A-420', 'A-600', 'A-610', 'A-700', 'S-201']:
    s = spans(sheet)
    d = [x for x in s if DIM.match(x['text'])]
    x0 = min(x['box'][0] for x in d) - 0.01; x1 = max(x['box'][2] for x in d) + 0.01
    y0 = min(x['box'][1] for x in d) - 0.01; y1 = max(x['box'][3] for x in d) + 0.01
    xm, ym = (x0 + x1) / 2, (y0 + y1) / 2
    for k, box in enumerate([(x0, y0, xm, ym), (xm, y0, x1, ym), (x0, ym, xm, y1), (xm, ym, x1, y1)]):
        # every dimension token in every text span fully inside the crop (notes and labels included)
        inn = [m for x in s if inside(x, box) for m in DIM_TOKEN.findall(x['text'])]
        # tokens in spans cut by the crop edge are excluded from the key and from scoring
        edge = [m for x in s if not inside(x, box) and (box[0] < x['box'][2] and x['box'][0] < box[2] and box[1] < x['box'][3] and x['box'][1] < box[3]) for m in DIM_TOKEN.findall(x['text'])]
        if len(inn) < 10:
            continue
        name = f'dim-{sheet}-{k}'
        tasks.append({'id': name, 'kind': 'dimensions', 'sheet': sheet, 'box': [round(v, 4) for v in box], 'images': render(sheet, box, name),
                      'answer': sorted(inn), 'ignore': sorted(edge)})

# 2. Wall-type tag counts on the dimensional floor plan (whole plan and two halves).
s = spans('A-120')
t = [x for x in s if TAG.match(x['text'])]
x0 = min(x['box'][0] for x in t) - 0.03; x1 = max(x['box'][2] for x in t) + 0.03
y0 = min(x['box'][1] for x in t) - 0.03; y1 = max(x['box'][3] for x in t) + 0.03
for k, box in enumerate([(x0, y0, x1, y1), (x0, y0, x1, (y0 + y1) / 2), (x0, (y0 + y1) / 2, x1, y1)]):
    c = collections.Counter(x['text'] for x in t if inside(x, box))
    name = f'tags-A-120-{k}'
    tasks.append({'id': name, 'kind': 'tag-count', 'sheet': 'A-120', 'box': [round(v, 4) for v in box], 'images': render('A-120', box, name), 'answer': dict(sorted(c.items()))})

# 3. Door schedule: every row's mark, type, size, material, frame and hardware set, read from a crop and from the whole sheet.
COLS = [('mark', 0.316), ('type', 0.391), ('width', 0.406), ('height', 0.424), ('material', 0.467), ('frame', 0.49), ('hardware', 0.51)]
rows = collections.defaultdict(dict)
for x in spans('A-600'):
    if 0.30 < x['cx'] < 0.52 and 0.065 < x['cy'] < 0.16:
        col = min(COLS, key=lambda c: abs(c[1] - x['cx']))
        if abs(col[1] - x['cx']) < 0.006:
            rows[round(x['cy'] * 400)][col[0]] = x['text']
key = [r for _, r in sorted(rows.items()) if 'mark' in r]
for name, box in (('sched-A-600-crop', (0.30, 0.02, 0.68, 0.17)), ('sched-A-600-sheet', (0, 0, 1, 1))):
    tasks.append({'id': name, 'kind': 'schedule', 'sheet': 'A-600', 'box': list(box), 'images': render('A-600', box, name), 'answer': key})

# 4. Measuring and counting, scored against the estimator's own PlanSwift quantities (reference/markups/legends.json).
#    These are the hard takeoff skills: undimensioned lengths, areas, and symbol counts.
SKILL = [
    ('count-E-130-lights', 'count', 'E-130', (0.02, 0.02, 0.70, 0.82),
     'This is an electrical lighting plan. Light fixtures are labelled with a fixture type tag (for example A, AE, B, C, F3, G1, J, JE, T, TE, X1, X2, X3, S, U1, U3, GEM, FEM, PB), often with a circuit/switch suffix after a comma (e.g. "C, b" is type C). Count every fixture of each type shown on the plans on this sheet (including enlarged plans/insets). Count fixtures, not tags in notes or schedules. Report counts for these types: A, AE, B, C, F3, G1, J, JE, T, TE, X1, X2, X3, S, U1, U3, GEM, FEM, PB.',
     {'A': 8, 'AE': 6, 'B': 3, 'C': 53, 'F3': 1, 'G1': 22, 'J': 9, 'JE': 4, 'T': 7, 'TE': 9, 'X1': 4, 'X2': 2, 'X3': 1, 'S': 2, 'U1': 2, 'U3': 1, 'GEM': 2, 'FEM': 2, 'PB': 1}),
    ('count-P-302-fixtures', 'count', 'P-302', (0.15, 0.13, 0.58, 0.82),
     'This is a plumbing floor plan. Count every plumbing fixture/fitting of each tag shown on the plan: WC (water closet), LAV (lavatory), SK-U, SK-T (sinks), CP, MS (mop sink), EWH (electric water heater), EDF, HB (hose bibb), VB (valve box), DW (dishwasher), CD (condensate drain), DSN (downspout nozzle).',
     {'WC': 2, 'LAV': 2, 'SK-U': 1, 'SK-T': 1, 'CP': 1, 'MS': 1, 'EWH': 1, 'EDF': 1, 'HB': 2, 'VB': 1, 'DW': 1, 'CD': 7, 'DSN': 2}),
    ('measure-A-130-ceilings', 'measure', 'A-130', (0.12, 0.13, 0.56, 0.84),
     'This is a reflected ceiling plan at 1/4" = 1\'-0" with dimension strings. Measure the floor-plan area in square feet of each ceiling type: ACT-1 (2x2 acoustical tile, legend AC1), ACT-2 (legend AC2), painted gypsum board ceiling (PT-3), and exposed structure (exposed ceiling). Use the printed dimensions and the scale; give one total per type. Names: ACT-1, ACT-2, GYP, EXPOSED.',
     {'ACT-1': 948.7, 'ACT-2': 244.8, 'GYP': 516.1, 'EXPOSED': 98.4}),
    ('measure-A-120-walls', 'measure', 'A-120', (0.13, 0.17, 0.66, 0.88),
     'This is a dimensioned floor plan at 1/4" = 1\'-0". Interior partitions are tagged with wall types in diamond tags (A3A, A3B, A6A, A6B, D3A, D3C). Measure the total linear feet of full-height partition of each type (wall centreline length along each run, using the printed dimensions and the scale; ignore low walls under 4\' tall). Names: A3A, A3B, A6A, A6B, D3A, D3C.',
     {'A3A': 49.9, 'A3B': 34.2, 'A6A': 36.7, 'A6B': 28.4, 'D3A': 46.0, 'D3C': 3.7}),
]
for name, kind, sheet, box, prompt, key in SKILL:
    tasks.append({'id': name, 'kind': kind, 'sheet': sheet, 'box': list(box), 'images': render(sheet, box, name), 'prompt': prompt, 'answer': key,
                  'answerSource': 'estimator PlanSwift legend (reference/markups/legends.json)'})

json.dump(tasks, open(os.path.join(HERE, 'tasks.json'), 'w'), indent=1)
print(len(tasks), 'tasks:', collections.Counter(x['kind'] for x in tasks))
for x in tasks: print(x['id'], len(x['answer']), 'answer items')
