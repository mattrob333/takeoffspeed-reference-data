import sys, json, os, pymupdf
ROOT='/home/user/takeoffspeed-reference-data'
s=sys.argv[1]
idx=json.load(open(ROOT+'/reference/sheets/index.json'))
for x in idx:
    if x['sheet']==s and x['pages']==1:
        p=pymupdf.open(os.path.join(ROOT,x['file']))[0]
r=p.rect
print('rect',r)
for b in p.get_text('dict')['blocks']:
    for l in b.get('lines',[]):
        t=' '.join(sp['text'] for sp in l['spans']).strip()
        if not t: continue
        x0,y0,x1,y1=l['bbox']
        print(f"{x0/r.width:.3f} {y0/r.height:.3f} {x1/r.width:.3f} {y1/r.height:.3f} dir={l['dir'][0]:.0f},{l['dir'][1]:.0f} | {t}")
