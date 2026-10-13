import pymupdf, sys, collections
doc = pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Electrical/E-150-ELECTRICAL-SECURITY-PLAN-Rev.0.pdf')
p = doc[0]; W,H = p.rect.width, p.rect.height
words = p.get_text('words')
nums=[]
for w in words:
    x0,y0,x1,y1,t = w[:5]
    if t.isdigit() and 1<=int(t)<=20:
        nums.append((t,(x0+x1)/2/W,(y0+y1)/2/H))
# print all '18' and 'AI'
for w in words:
    if w[4] in ('18','AI'):
        print(w[4], round((w[0]+w[2])/2/W,4), round((w[1]+w[3])/2/H,4))
