import sys, glob, re, pymupdf
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(33); Z=4
clip=pymupdf.Rect(p.rect.width*0.42,p.rect.height*0.26,p.rect.width*0.82,p.rect.height*0.86)
pix=p.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip)
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
def px(x,y):
    i=(y*W+x)*n; return s[i],s[i+1],s[i+2]
def is_yellow(c): r,g,b=c; return r>145 and g>190 and b<125 and g-b>70
mask=[[is_yellow(px(x,y)) for x in range(W)] for y in range(H)]
def runs(lines):
    out=[]
    for k,row in enumerate(lines):
        st=None
        for i,v in enumerate(row+[False]):
            if v and st is None: st=i
            if not v and st is not None:
                if i-st>40: out.append((k,st,i))
                st=None
    return out
hr=runs(mask); cols=[[mask[y][x] for y in range(H)] for x in range(W)]; vr=runs(cols)
def cluster(rs):
    rs=sorted(rs); groups=[]
    for k,a,b in rs:
        for g in groups:
            if abs(g['k']-k)<=4 and not (b<g['a']-5 or a>g['b']+5):
                g['a']=min(g['a'],a); g['b']=max(g['b'],b); g['k']=k; break
        else: groups.append({'k':k,'a':a,'b':b})
    return groups
hg=cluster(hr); vg=cluster(vr)
ptft=1191/36*0.25  # pt per ft if sheet scaled by width
pxft=ptft*Z
print('pt/ft',ptft)
tot=0
for name,g in (('H',hg),('V',vg)):
    for x in g:
        L=(x['b']-x['a'])/pxft; tot+=L; print(name,x['k'],round(L,2))
print('total ft',round(tot,2))
from collections import Counter
c=Counter()
for y in range(0,H,3):
    for x in range(0,W,3):
        r,g,b=px(x,y); c[(r//20*20,g//20*20,b//20*20)]+=1
print(c.most_common(25))
