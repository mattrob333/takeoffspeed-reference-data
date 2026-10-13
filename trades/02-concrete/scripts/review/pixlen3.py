import glob, re, os, pymupdf
ROOT='/home/user/takeoffspeed-reference-data'
def markup_page(n):
    for f in sorted(glob.glob(os.path.join(ROOT,'source/markups/MARKUPS*.pdf'))):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
page=markup_page(33); r=page.rect; Z=3
box=(0.42,0.20,0.84,0.86)
clip=pymupdf.Rect(r.x0+r.width*box[0], r.y0+r.height*box[1], r.x0+r.width*box[2], r.y0+r.height*box[3])
p=page.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip,alpha=False)
W,H,n=p.width,p.height,p.n; s=p.samples
def cls(R,G,B):
    if B>=200 and R<170 and G<170 and abs(R-G)<30: return 'peri'
    if 130<=B<200 and R<90 and G<90: return 'slate'
    if G>=185 and B<130 and R>=140: return 'yellow'
    if R>=140 and G>=140 and abs(R-G)<30 and B<R-40 and R<225: return 'olive'
    return None
lab=[None]*(W*H)
for i in range(W*H):
    j=i*n; lab[i]=cls(s[j],s[j+1],s[j+2])
# run-length filter: keep pixel if its horizontal or vertical run of same class <= 8 px
def runs(axis):
    out=[0]*(W*H)
    if axis=='h':
        for y in range(H):
            x=0
            while x<W:
                c=lab[y*W+x]
                if c is None: x+=1; continue
                x2=x
                while x2<W and lab[y*W+x2]==c: x2+=1
                for k in range(x,x2): out[y*W+k]=x2-x
                x=x2
    else:
        for x in range(W):
            y=0
            while y<H:
                c=lab[y*W+x]
                if c is None: y+=1; continue
                y2=y
                while y2<H and lab[y2*W+x]==c: y2+=1
                for k in range(y,y2): out[k*W+x]=y2-y
                y=y2
    return out
rh=runs('h'); rv=runs('v')
from collections import Counter
tot=Counter(); line=Counter(); widths={k:Counter() for k in ('peri','slate','yellow','olive')}
for i in range(W*H):
    c=lab[i]
    if c is None: continue
    tot[c]+=1
    m=min(rh[i],rv[i])
    if m<=8:
        line[c]+=1; widths[c][m]+=1
print('W,H',W,H,'px per ft', 3*8.27)
print('total px',tot); print('line px',line)
for k in widths: print(k,'run-width hist',sorted(widths[k].items())[:10])
# length estimate = line px / modal width
ptft=410.0/49.6667  # pt per ft from grid 7..1 = 49'-8" (measured ~410 pt) -- refine below
