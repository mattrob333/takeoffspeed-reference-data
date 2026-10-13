import glob,re,pymupdf,statistics as st
for f in sorted(glob.glob('source/markups/MARKUPS*.pdf')):
    a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
    if a<=34<=b: p=pymupdf.open(f)[34-a]
Z=8
clip=pymupdf.Rect(560,380,960,700)
pix=p.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip)
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
def px(x,y): i=(y*W+x)*n; return s[i],s[i+1],s[i+2]
def ptx(x): return clip.x0+x/Z
def pty(y): return clip.y0+y/Z
# row profile of red channel median over x 600-640pt avoiding lines
print('row profile (y pt, median rgb)')
prev=None
for y in range(0,H):
    vals=[px(x,y) for x in range(int((605-560)*Z),int((625-560)*Z),3)]
    m=tuple(int(st.median(v[i] for v in vals)) for i in range(3))
    lab='dark' if m[1]<45 else ('mid' if m[1]<110 else 'light')
    if lab!=prev: print(round(pty(y),2),m,lab); prev=lab
print('col transitions at y=560pt')
y=int((560-clip.y0)*Z)
xs=[]
for x in range(W):
    r,g,b=px(x,y)
    if g<40 and r<170: xs.append(round(ptx(x),2))
# group
grp=[];cur=[]
for v in xs:
    if cur and v-cur[-1]>0.5: grp.append(cur);cur=[]
    cur.append(v)
if cur: grp.append(cur)
for g_ in grp: print(round((g_[0]+g_[-1])/2,2), len(g_), px(int((g_[0]-clip.x0)*Z),y))
