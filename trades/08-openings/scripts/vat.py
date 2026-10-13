import pymupdf, json
ROOT='/home/user/takeoffspeed-reference-data'
idx=json.load(open(ROOT+'/reference/sheets/index.json'))
f=[x for x in idx if x['sheet']=='A-701'][0]['file']
p=pymupdf.open(ROOT+'/'+f)[0]
R=p.rect; print(R)
clip=pymupdf.Rect(R.width*0.23,R.height*0.6,R.width*0.42,R.height*0.95)
# find text positions for dims
for b in p.get_text('words',clip=clip):
    if b[4] in ('8','1/2"','1"','1\'-0','3/4"','1','1/2"'): print([round(v,1) for v in b[:4]],b[4])
segs=[]
for d in p.get_drawings():
    if not clip.intersects(d['rect']): continue
    for it in d['items']:
        if it[0]=='l':
            a,b=it[1],it[2]
            L=((a.x-b.x)**2+(a.y-b.y)**2)**.5
            if L>20: segs.append((round(a.x,1),round(a.y,1),round(b.x,1),round(b.y,1),round(L,1)))
        if it[0]=='re':
            r=it[1]; print('rect',r, r.width,r.height)
segs.sort(key=lambda s:-s[4])
for s in segs[:40]: print(s)
