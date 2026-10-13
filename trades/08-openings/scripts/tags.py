import pymupdf, json, sys
ROOT='/home/user/takeoffspeed-reference-data'
idx=json.load(open(ROOT+'/reference/sheets/index.json'))
for s in sys.argv[1:]:
    f=[x for x in idx if x['sheet']==s][0]['file']
    p=pymupdf.open(ROOT+'/'+f)[0]
    W,H=p.rect.width,p.rect.height
    out=[]
    for w in p.get_text('words'):
        if w[4] in list('ABCDEFGHJK') and (w[2]-w[0])<12:
            out.append((w[4],round(w[0]/W,3),round(w[1]/H,3),round(w[3]-w[1],1)))
    out.sort()
    print(s,out)
