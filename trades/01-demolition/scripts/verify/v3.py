import pymupdf, math
p=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0]
print(p.rotation, p.rect, p.mediabox)
ws=[w for w in p.get_text('words') if w[4]=='///']
print(sorted([(round((w[0]+w[2])/2,1),round((w[1]+w[3])/2,1)) for w in ws if 690<w[0]<1000 and 760<w[1]<820]))
# legend
print([ (round(w[0]),round(w[1])) for w in ws if w[0]>1950])
