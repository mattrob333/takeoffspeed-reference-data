import pymupdf, json
ROOT='/home/user/takeoffspeed-reference-data'
idx=json.load(open(f'{ROOT}/reference/sheets/index.json'))
f=[x for x in idx if x['sheet']=='A-430'][0]['file']
pg=pymupdf.open(f'{ROOT}/{f}')[0]
for b in pg.get_text('blocks'):
    t=b[4].replace('\n',' ')
    if 'MECHO-SHADE' in t or 'DETAIL' in t or 'HEAD' in t or 'SILL' in t:
        print(round(b[0]),round(b[1]),round(b[2]),round(b[3]),t[:80])
