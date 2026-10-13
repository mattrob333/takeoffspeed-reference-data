# pixel cross-check of A-150 markup (p08) overlay colours: fill areas (SF) and line components (LF)
import pymupdf,glob,re,sys,collections
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(8); z=4; r=p.rect
box=(0.30,0.10,0.62,0.67)
clip=pymupdf.Rect(r.width*box[0],r.height*box[1],r.width*box[2],r.height*box[3])
pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=clip)
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
SPPF=18.0  # sheet pt per ft at 1/4"=1'-0"
pxft=z*SPPF*1190.52/2592
cols={'CON-1':(179,178,96),'CR1':(100,102,255),'CR2':(255,253,106),'CR3':(102,254,96),'CR4/FTS3':(106,253,254),
'FT1':(254,102,255),'FTS-4':(179,100,180),'FTS1':(101,101,101),'FTS2':(255,101,100),'LVT1':(100,179,99),'MAT-1':(100,101,182)}
lab=bytearray(W*H); names=list(cols)
for i in range(W*H):
    R,G,B=s[i*n],s[i*n+1],s[i*n+2]
    for k,(a,b,c) in enumerate(cols.values()):
        if abs(R-a)<10 and abs(G-b)<10 and abs(B-c)<10: lab[i]=k+1;break
cnt=collections.Counter(lab)
print('px/ft',round(pxft,3))
for k,nm in enumerate(names): print(nm,'px',cnt[k+1],'SF',round(cnt[k+1]/pxft/pxft,2))
# components for line colours
import array
seen=bytearray(W*H)
for k,nm in enumerate(names):
    if nm not in ('FTS-4','FTS1','FTS2','CR4/FTS3','MAT-1'): continue
    comps=[]
    for st in range(W*H):
        if lab[st]!=k+1 or seen[st]: continue
        stack=[st]; seen[st]=1; xs=[];ys=[];c=0
        x0=y0=10**9;x1=y1=-1
        while stack:
            q=stack.pop(); x,y=q%W,q//W; c+=1
            x0=min(x0,x);x1=max(x1,x);y0=min(y0,y);y1=max(y1,y)
            for d in (1,-1,W,-W):
                t=q+d
                if 0<=t<W*H and not seen[t] and lab[t]==k+1: seen[t]=1; stack.append(t)
        if c>=30: comps.append((c,(x1-x0+1)/pxft,(y1-y0+1)/pxft,(x0/W*(box[2]-box[0])+box[0],y0/H*(box[3]-box[1])+box[1])))
    comps.sort(reverse=True)
    print('==',nm,len(comps))
    for c in comps[:25]: print('  px',c[0],'w_ft',round(c[1],2),'h_ft',round(c[2],2),'at',tuple(round(v,3) for v in c[3]))
