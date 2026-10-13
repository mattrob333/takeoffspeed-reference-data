import sys, glob, re, pymupdf, collections
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
n=int(sys.argv[1]); x0,y0,x1,y1=map(float,sys.argv[2:6]); zoom=float(sys.argv[6]); target=tuple(int(v) for v in sys.argv[7].split(',')); tol=int(sys.argv[8]); ptperft=float(sys.argv[9]); orient=sys.argv[10] if len(sys.argv)>10 else 'v'
GAP=int(sys.argv[11]) if len(sys.argv)>11 else 20
p=page(n); r=p.rect
clip=pymupdf.Rect(r.width*x0,r.height*y0,r.width*x1,r.height*y1)
pix=p.get_pixmap(matrix=pymupdf.Matrix(zoom,zoom),clip=clip,alpha=False)
W,H,s=pix.width,pix.height,pix.samples
def m(x,y):
    i=(y*W+x)*3; return all(abs(s[i+k]-target[k])<=tol for k in range(3))
runs=[]
if orient=='v':
  for x in range(W):
    ys=[y for y in range(H) if m(x,y)]
    segs=[]
    for y in ys:
        if segs and y-segs[-1][1]<=GAP: segs[-1][1]=y
        else: segs.append([y,y])
    if segs:
        b=max(segs,key=lambda t:t[1]-t[0])
        if b[1]-b[0]>10: runs.append((x,(b[0],b[1]+1)))
else:
  for y in range(H):
    xs=[x for x in range(W) if m(x,y)]
    segs=[]
    for x in xs:
        if segs and x-segs[-1][1]<=GAP: segs[-1][1]=x
        else: segs.append([x,x])
    if segs:
        b=max(segs,key=lambda t:t[1]-t[0])
        if b[1]-b[0]>10: runs.append((y,(b[0],b[1]+1)))
# cluster adjacent
groups=[];
for x,b in runs:
    if groups and x-groups[-1][-1][0]<=3: groups[-1].append((x,b))
    else: groups.append([(x,b)])
tot=0
for g in groups:
    L=max(b[1]-b[0] for _,b in g)
    ft=L/zoom/ptperft
    tot+=ft
    print('pos',g[0][0],'-',g[-1][0],'len_px',L,'ft',round(ft,2), 'from',min(b[0] for _,b in g),'to',max(b[1] for _,b in g))
print('total ft',round(tot,2))
