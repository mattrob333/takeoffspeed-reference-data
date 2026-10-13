import pymupdf, json, collections, sys
ROOT='/home/user/takeoffspeed-reference-data/'
d=pymupdf.open(ROOT+'source/drawings/Electrical/E-150-ELECTRICAL-SECURITY-PLAN-Rev.0.pdf')[0]
W,H=d.rect.width,d.rect.height
cnt=collections.defaultdict(lambda: {'main':0,'driveThru':0})
for w in d.get_text('words'):
    t=w[4]; x=w[0]/W; y=w[1]/H; h=w[3]-w[1]
    if not (t.isdigit() and 1<=int(t)<=20): continue
    if h>20: continue                      # PRAXIS3 logo
    if abs(x-0.331)<0.003 and y>0.75: continue   # schedule '#' column
    if y>0.69: continue                    # view titles (1, 2) below plans
    if x<0.25 and y>0.23: continue         # view-2 title '2'
    if x>0.7: continue                     # sheet notes column
    cnt[int(t)]['driveThru' if x<0.25 else 'main']+=1
out={k:{**v,'total':v['main']+v['driveThru']} for k,v in sorted(cnt.items())}
print(json.dumps(out))
# E-160: 'F' glyph text = horn/strobe + pull station
d2=pymupdf.open(ROOT+'source/drawings/Electrical/E-160-ELECTRICAL-FIRE-ALARM-PLAN-Rev.0.pdf')[0]
c2=collections.Counter(w[4] for w in d2.get_text('words') if w[0]/d2.rect.width<0.65 and w[4] in ('F','FD','D','FACP','FAA'))
print(json.dumps(c2))
