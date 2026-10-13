"""Render a markup page or a drawing sheet (or a crop of it) to PNG for reading.

usage:
  python3 -I tools/render.py markup <page 1-92> <out.png> [x0 y0 x1 y1] [zoom]
  python3 -I tools/render.py sheet <A-120|path.pdf> <out.png> [x0 y0 x1 y1] [zoom]
Crop box is in fractions of the page (0..1, origin top-left). Default zoom 2.
"""
import sys, glob, json, os, re
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def markup_page(n):
    for f in sorted(glob.glob(os.path.join(ROOT, 'source/markups/MARKUPS*.pdf'))):
        a, b = map(int, re.search(r'_p(\d+)-(\d+)', f).groups())
        if a <= n <= b:
            return pymupdf.open(f)[n - a]
    raise SystemExit(f'no markup page {n}')

def sheet_page(s):
    if s.endswith('.pdf'):
        return pymupdf.open(s)[0]
    idx = json.load(open(os.path.join(ROOT, 'reference/sheets/index.json')))
    for x in idx:
        if x['sheet'] == s and x['pages'] == 1:
            return pymupdf.open(os.path.join(ROOT, x['file']))[0]
    raise SystemExit(f'no single-page sheet {s}')

kind, ref, out, *rest = sys.argv[1:]
page = markup_page(int(ref)) if kind == 'markup' else sheet_page(ref)
box = list(map(float, rest[:4])) if len(rest) >= 4 else [0, 0, 1, 1]
zoom = float(rest[4]) if len(rest) >= 5 else 2.0
r = page.rect
clip = pymupdf.Rect(r.x0 + r.width * box[0], r.y0 + r.height * box[1], r.x0 + r.width * box[2], r.y0 + r.height * box[3])
pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), clip=clip)
pix.save(out)
print(f'{out} {pix.width}x{pix.height}')
