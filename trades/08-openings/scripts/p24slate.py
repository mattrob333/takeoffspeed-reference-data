import pymupdf, glob, re, collections
ROOT='/home/user/takeoffspeed-reference-data'
for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
    a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
    if a<=24<=b: p=pymupdf.open(f)[24-a]
z=4
pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z)); W,H,n=pix.width,pix.height,pix.n; s=pix.samples
def px(x,y): i=(y*W+x)*n; return s[i],s[i+1],s[i+2]
# legend swatch for 'Linear' row: find colour near legend right column at y of 'Linear' (~0.957)
print('swatch', [px(int(0.349*W)+dx,int(0.957*H)) for dx in (-4,0,4)])
T=(102,101,177)
hits=[]
for y in range(0,H,1):
    for x in range(0,W,2):
        i=(y*W+x)*n; r,g,b=s[i],s[i+1],s[i+2]
        if abs(r-T[0])+abs(g-T[1])+abs(b-T[2])<45: hits.append((x,y))
leg=lambda x,y: x<0.36*W and y>0.815*H
out=[(x,y) for x,y in hits if not leg(x,y)]
print('hits',len(hits),'outside legend',len(out))
c=collections.Counter((x*40//W,y*40//H) for x,y in out)
print(sorted(c.items()))
xs=[x for x,y in out]; ys=[y for x,y in out]
print('bbox frac', min(xs)/W, max(xs)/W, min(ys)/H, max(ys)/H)
# det 6 region: VAT ACCESS elevation approx x 0.235-0.40 y 0.60-0.94 ; count saturated pixels excluding legend
sat=0
for y in range(int(0.60*H),int(0.94*H),2):
    for x in range(int(0.235*W),int(0.40*W),2):
        if leg(x,y): continue
        i=(y*W+x)*n; r,g,b=s[i],s[i+1],s[i+2]
        if max(r,g,b)-min(r,g,b)>60: sat+=1
print('det6 saturated px (sampled every 2, outside legend)',sat)
import json; json.dump(out,open('/home/user/work/08-openings/p24slate-hits.json','w'))
