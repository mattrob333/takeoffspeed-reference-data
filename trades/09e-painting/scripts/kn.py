import json, pymupdf
idx=json.load(open('/home/user/takeoffspeed-reference-data/reference/sheets/index.json'))
for s in ('M-301','P-303','P-403'):
  x=[i for i in idx if i['sheet']==s][0]
  pg=pymupdf.open('/home/user/takeoffspeed-reference-data/'+x['file'])[0]
  W=pg.rect.width
  words=pg.get_text('words')
  if s=='M-301':
    for k in ('5','8'):
      hits=[(round(w[0]),round(w[1])) for w in words if w[4]==k and w[0]<0.62*W]
      print(s,'keynote',k,len(hits),hits)
  else:
    for w in words:
      if any(t in w[4].upper() for t in ('YELLOW','GAS','PAINT')): print(s,w[4],round(w[0]),round(w[1]))
