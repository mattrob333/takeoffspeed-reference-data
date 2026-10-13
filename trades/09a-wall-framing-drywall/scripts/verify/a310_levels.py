import pymupdf, json, sys
ROOT='/home/user/takeoffspeed-reference-data'
idx=json.load(open(f'{ROOT}/reference/sheets/index.json'))
f=[x for x in idx if x['sheet']=='A-310'][0]['file']
pg=pymupdf.open(f'{ROOT}/{f}')[0]
print(pg.rect)
for b in pg.get_text('words'):
    w=b[4]
    if w in ('F.F.E.','LOW','SILL','VAT','8"','6"','17\'','0\'','2\'') or 'PARAPET' in w:
        print(round(b[0],1),round(b[1],1),w)
