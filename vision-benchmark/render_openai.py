"""OpenAI-only high-resolution renders for the vision benchmark (variant `orig`, sent with `detail: "original"`).

usage: python3 -I vision-benchmark/render_openai.py <image_dir> [task_id,...]
Writes <image_dir>/<task_id>-orig.png for each task in tasks.json (tasks.json is not changed).

Why: `detail: "high"` on gpt-6-astra caps an image at 2,500 32-px patches (about 1600x1600 px), so the 2,576 px
`hi` renders built for Claude were downscaled before GPT-6 Astra saw them. `detail: "original"` keeps native size,
but the API rejects (does not resize) any single image over 30,000 32-px patches
(https://developers.openai.com/api/docs/guides/images-vision, read 2026-10-13). Each crop is therefore rendered
from the vector PDF at the largest zoom that keeps the long edge <= 6,000 px and ceil(w/32)*ceil(h/32) <= 30,000.
"""
import sys, os, json, math
import pymupdf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from textlayer import sheet_file

LONG_EDGE, MAX_PATCHES, PATCH = 6000, 30000, 32

def patches(w, h):
    return math.ceil(w / PATCH) * math.ceil(h / PATCH)

def fit(clip):
    """Largest zoom with long edge <= LONG_EDGE px and patch count <= MAX_PATCHES (checked on PyMuPDF's rounded pixel box)."""
    z = LONG_EDGE / max(clip.width, clip.height)
    while True:
        ir = (clip * pymupdf.Matrix(z, z)).irect
        if max(ir.width, ir.height) <= LONG_EDGE and patches(ir.width, ir.height) <= MAX_PATCHES:
            return z
        z *= 0.999

def render(task, out_dir):
    p = pymupdf.open(sheet_file(task['sheet']))[0]
    r, b = p.rect, task['box']
    clip = pymupdf.Rect(r.width * b[0], r.height * b[1], r.width * b[2], r.height * b[3])
    z = fit(clip)
    pix = p.get_pixmap(matrix=pymupdf.Matrix(z, z), clip=clip)
    assert max(pix.width, pix.height) <= LONG_EDGE and patches(pix.width, pix.height) <= MAX_PATCHES, (task['id'], pix.width, pix.height)
    path = os.path.join(out_dir, f"{task['id']}-orig.png")
    pix.save(path)
    # px per inch of paper (PDF points are 1/72 in)
    return pix.width, pix.height, patches(pix.width, pix.height), round(z * 72)

if __name__ == '__main__':
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    only = set(sys.argv[2].split(',')) if len(sys.argv) > 2 else None
    here = os.path.dirname(os.path.abspath(__file__))
    for t in json.load(open(os.path.join(here, 'tasks.json'))):
        if only and t['id'] not in only:
            continue
        w, h, n, ppi = render(t, out)
        print(f"{t['id']:24} {w}x{h} px  {n} patches  {ppi} px/in")
