import glob,re,pymupdf
for f in sorted(glob.glob('source/markups/MARKUPS*.pdf')):
    a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
    if a<=34<=b: p=pymupdf.open(f)[34-a]
Z=8
clip=pymupdf.Rect(560,200,960,700)
pix=p.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip)
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
def px(x,y): i=(y*W+x)*n; return s[i],s[i+1],s[i+2]
def colprofile(xpt,label):
    x=int(round((xpt-clip.x0)*Z))
    # compare pixel at line vs pixel 2pt to the side
    prev=None;out=[]
    for y in range(H):
        c=px(x,y); side=px(x+16,y)
        online = (side[0]-c[0])>25 or (side[1]-c[1])>25
        if online!=prev: out.append((round(clip.y0+y/Z,2),online,c,side)); prev=online
    print(label,xpt); [print('  ',o) for o in out if True]
for xpt,l in [(595.75,'18KCS2'),(763.0,'12KCS2'),(805.0,'12KCS2')]:
    colprofile(xpt,l)
