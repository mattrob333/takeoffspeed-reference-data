import glob,re,pymupdf,sys
sys.setrecursionlimit(10**7)
for f in sorted(glob.glob('source/markups/MARKUPS*.pdf')):
    a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
    if a<=34<=b: p=pymupdf.open(f)[34-a]
Z=2.0
clip=pymupdf.Rect(380,140,1000,720)
pix=p.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip)
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
PPF=18*1190.52/2592*Z  # px per ft
mask=bytearray(W*H)
for y in range(H):
    for x in range(W):
        i=(y*W+x)*n; r,g,b=s[i],s[i+1],s[i+2]
        if r>190 and g>190 and b<160: mask[y*W+x]=1
# close small gaps (text) by dilation-erosion 3px
def morph(m,k,op):
    out=bytearray(W*H)
    for y in range(H):
        for x in range(W):
            vals=[m[yy*W+xx] for yy in range(max(0,y-k),min(H,y+k+1)) for xx in (max(0,x-k),x,min(W-1,x+k))]
            out[y*W+x]= (1 if any(vals) else 0) if op=='d' else (1 if all(vals) else 0)
    return out
m=morph(morph(mask,3,'d'),3,'e')
seen=bytearray(W*H); comps=[]
for st in range(W*H):
    if m[st] and not seen[st]:
        stack=[st];seen[st]=1;pts=[]
        while stack:
            k=stack.pop();pts.append(k);x,y=k%W,k//W
            for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 0<=nx<W and 0<=ny<H and m[ny*W+nx] and not seen[ny*W+nx]: seen[ny*W+nx]=1;stack.append(ny*W+nx)
        if len(pts)>2000: comps.append(pts)
tot_area=0;tot_per=0
for c in comps:
    cs=set(c); per=0
    for k in c:
        x,y=k%W,k//W
        for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if not (0<=nx<W and 0<=ny<H) or (ny*W+nx) not in cs: per+=1
    xs=[k%W for k in c]; ys=[k//W for k in c]
    area=len(c)/PPF**2; perft=per/PPF
    tot_area+=area; tot_per+=perft
    print('comp bbox pt',round(clip.x0+min(xs)/Z),round(clip.y0+min(ys)/Z),round(clip.x0+max(xs)/Z),round(clip.y0+max(ys)/Z),'area SF',round(area,1),'perimeter ft',round(perft,1))
print('total area',round(tot_area,1),'total perimeter',round(tot_per,1))
