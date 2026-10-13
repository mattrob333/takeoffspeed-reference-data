import pymupdf, json, sys, collections
ROOT='/home/user/takeoffspeed-reference-data'
idx=json.load(open(ROOT+'/reference/sheets/index.json'))
for s in ['A-120','A-110','A-200','A-201']:
    f=[x for x in idx if x['sheet']==s][0]['file']
    p=pymupdf.open(ROOT+'/'+f)[0]
    c=collections.defaultdict(list)
    for b in p.get_text('dict')['blocks']:
        for l in b.get('lines',[]):
            for sp in l['spans']:
                t=sp['text'].strip()
                if len(t)==1 and t in 'ABCDEFGHJK':
                    c[(round(sp['size'],2),sp['font'])].append(t)
    print(s,{k:sorted(v) for k,v in c.items()})
