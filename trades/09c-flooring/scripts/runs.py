# horizontal & vertical colour runs (>= minft) on a markup crop; merges adjacent parallel rows
import pymupdf,glob,re,sys
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
pg=int(sys.argv[1]); sppf=float(sys.argv[2]); col=tuple(map(int,sys.argv[3].split(','))); tol=int(sys.argv[4]); box=tuple(map(float,sys.argv[5:9])); minft=float(sys.argv[9]); gap=int(sys.argv[10]) if len(sys.argv)>10 else 3
p=page(pg); z=float(__import__("os").environ.get("Z","8")); r=p.rect
pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=pymupdf.Rect(r.width*box[0],r.height*box[1],r.width*box[2],r.height*box[3]))
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
pxft=z*sppf*1190.52/2592
M=[[abs(s[(y*W+x)*n]-col[0])<tol and abs(s[(y*W+x)*n+1]-col[1])<tol and abs(s[(y*W+x)*n+2]-col[2])<tol for x in range(W)] for y in range(H)]
def runs(line):
    out=[];st=None;last=None
    for i,v in enumerate(line):
        if v:
            if st is None: st=i
            last=i
        elif st is not None and i-last>gap:
            out.append((st,last)); st=None
    if st is not None: out.append((st,last))
    return out
def fx(px): return round(box[0]+px/W*(box[2]-box[0]),4)
def fy(py): return round(box[1]+py/H*(box[3]-box[1]),4)
H_=[]
for y in range(H):
    for a,b in runs(M[y]):
        if (b-a)/pxft>=minft: H_.append((y,a,b))
V_=[]
for x in range(W):
    for a,b in runs([M[y][x] for y in range(H)]):
        if (b-a)/pxft>=minft: V_.append((x,a,b))
def merge(L):
    L.sort(); g=[]
    for k,a,b in L:
        if g and k-g[-1][1]<=2 and abs(a-g[-1][2])<pxft*0.3 and abs(b-g[-1][3])<pxft*0.3: g[-1][1]=k; g[-1][3]=max(b,g[-1][3])
        else: g.append([k,k,a,b])
    return g
print('pxft',round(pxft,2))
for k0,k1,a,b in merge(H_): print('H at y',fy(k0),'x',fx(a),'-',fx(b),'len ft',round((b-a)/pxft,3),'rows',k1-k0+1)
for k0,k1,a,b in merge(V_): print('V at x',fx(k0),'y',fy(a),'-',fy(b),'len ft',round((b-a)/pxft,3),'cols',k1-k0+1)
