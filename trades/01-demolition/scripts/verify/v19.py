import pymupdf, glob, re, json, math
ROOT='/home/user/takeoffspeed-reference-data'
for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
    a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
    if a<=64<=b: pg=pymupdf.open(f)[64-a]
print([ (i[2],i[3]) for i in pg.get_images()])
Z=2592/792
pix=pg.get_pixmap(matrix=pymupdf.Matrix(Z,Z)); W,H,n=pix.width,pix.height,pix.n; S=pix.samples
def isred(x,y):
    if not(0<=x<W and 0<=y<H): return False
    o=(y*W+x)*n; r,g,b=S[o],S[o+1],S[o+2]
    return r>120 and g<100 and b<100 and r-g>60
D=pymupdf.open(ROOT+'/source/drawings/Civil/C-1.0-DEMOLITION-PLAN-Rev.0.pdf')[0].get_drawings()
C=json.load(open('util_chains.json'))[:9]
names=['red TEL loop','green','blue','orange','magenta','cyan','gas','pink','water']
def samples(idx,step=2.0):
    out=[]
    for i in idx:
        for it in D[i]['items']:
            a,b=it[1],it[2]; L=math.dist(a,b); k=max(1,int(L/step))
            for j in range(k): t=j/k; out.append((a.x+(b.x-a.x)*t,a.y+(b.y-a.y)*t))
    return out
def cov(pts,dx,dy,r=3):
    hit=0
    for x,y in pts:
        X=int(round(x+dx)); Y=int(round(y+dy))
        if any(isred(X+u,Y+v) for u in range(-r,r+1,1) for v in range(-r,r+1,1)): hit+=1
    return hit/len(pts)
ref=samples(C[0][1],6)
best=max(((cov(ref,dx,dy,1),dx,dy) for dx in range(-8,9,2) for dy in range(-8,9,2)))
print('registration',best)
_,dx,dy=best
for (ci,idx),nm in zip(C,names):
    print(nm, round(cov(samples(idx),dx,dy,3)*100,1),'%')
json.dump([dx,dy],open('reg.json','w'))
