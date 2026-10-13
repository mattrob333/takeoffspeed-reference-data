import sys, glob, re, pymupdf
ROOT='/home/user/takeoffspeed-reference-data'
def mp(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
for n in (59,60):
    pg=mp(n); r=pg.rect
    print('page',n,'rect',r,'mediabox',pg.mediabox,'cropbox',pg.cropbox)
    for a in pg.annots() or []:
        if a.rect.y0>r.height*0.8: print('  annot',a.type,a.rect, (a.info.get('content') or '')[:60])
    for d in pg.get_drawings():
        rr=d['rect']
        if rr.y0>r.height*0.6 and rr.x0<r.width*0.7 and (rr.width>200 or rr.height>20):
            print('  draw',rr, [it[0] for it in d['items']][:6])
    for b in pg.get_text('dict')['blocks']:
        if b['bbox'][1]>r.height*0.6:
            t=' '.join(s['text'] for l in b.get('lines',[]) for s in l['spans'])
            if b['bbox'][0]<r.width*0.7: print('  text',[round(x) for x in b['bbox']],t[:60])
