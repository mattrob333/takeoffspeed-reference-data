# connected components of one overlay colour on markup p08; prints bbox in feet (1/4" scale) and page fractions
import pymupdf,glob,re,sys
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
col=tuple(map(int,sys.argv[1].split(','))); tol=int(sys.argv[2]); box=tuple(map(float,sys.argv[3:7])) if len(sys.argv)>6 else (0.30,0.10,0.62,0.67)
p=page(8); z=6; r=p.rect
pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=pymupdf.Rect(r.width*box[0],r.height*box[1],r.width*box[2],r.height*box[3]))
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
pxft=z*18.0*1190.52/2592
m=bytearray(W*H)
for i in range(W*H):
    if abs(s[i*n]-col[0])<tol and abs(s[i*n+1]-col[1])<tol and abs(s[i*n+2]-col[2])<tol: m[i]=1
comps=[]
for st in range(W*H):
    if not m[st]: continue
    stack=[st]; m[st]=0; c=0; x0=y0=10**9; x1=y1=-1
    while stack:
        q=stack.pop(); x,y=q%W,q//W; c+=1
        if x<x0:x0=x
        if x>x1:x1=x
        if y<y0:y0=y
        if y>y1:y1=y
        for d in (1,-1,W,-W):
            t=q+d
            if 0<=t<W*H and m[t]: m[t]=0; stack.append(t)
    if c>=40: comps.append((c,round((x1-x0+1)/pxft,2),round((y1-y0+1)/pxft,2),round(box[0]+x0/W*(box[2]-box[0]),3),round(box[1]+y0/H*(box[3]-box[1]),3)))
comps.sort(reverse=True)
print('pxft',round(pxft,2),'n',len(comps))
for c in comps:
    if (min(c[1],c[2])<0.25 and max(c[1],c[2])>0.4) or c[0]>20000: print(c)
