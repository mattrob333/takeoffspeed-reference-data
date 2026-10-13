"""Write the PDF text layer of every single-sheet drawing and every spec page to text files.

usage: python3 -I tools/extract_text.py <out_dir>
Produces <out_dir>/<SHEET>.txt (e.g. A-120.txt) and <out_dir>/spec-pNNN.txt (3-digit page).
Trade folders cite these as text/<file>.
"""
import sys, os, json
import pymupdf
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = sys.argv[1]
os.makedirs(out, exist_ok=True)
for x in json.load(open(os.path.join(ROOT, 'reference/sheets/index.json'))):
    if x['sheet'] and x['pages'] == 1:
        open(os.path.join(out, f"{x['sheet']}.txt"), 'w').write(pymupdf.open(os.path.join(ROOT, x['file']))[0].get_text())
for i, p in enumerate(pymupdf.open(os.path.join(ROOT, 'source/specifications.pdf'))):
    open(os.path.join(out, f'spec-p{i + 1:03d}.txt'), 'w').write(p.get_text())
print('done')
