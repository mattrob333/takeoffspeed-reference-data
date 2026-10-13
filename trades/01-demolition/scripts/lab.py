import pymupdf, json, math, collections
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
T=json.load(open('ticks.json'))
L=[((w[0]+w[2])/2,(w[1]+w[3])/2,w[4]) for w in p.get_text('words') if w[4] in ('GAS','W','UGP','OHP','TEL','FO','SS')]
c=collections.Counter(); out=[]
for t in T:
    if t[0]>1950: continue
    d,lab=min((math.dist(t,(l[0],l[1])),l[2]) for l in L)
    c[lab if d<60 else 'none']+=1; out.append((t,lab,d))
print(c, sum(c.values()))
