import glob,re,pymupdf
for f in sorted(glob.glob('source/markups/MARKUPS*.pdf')):
    a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
    if a<=36<=b: p=pymupdf.open(f)[36-a]
Z=8; PPF=6.2007
def scan(clip,label):
    pix=p.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip)
    W,H,n=pix.width,pix.height,pix.n; s=pix.samples
    best=[]
    for y in range(H):
        xs=[x for x in range(W) if (lambda i:(s[i]>200 and s[i+1]>200 and s[i+2]<120))((y*W+x)*n)]
        if len(xs)>50: best.append((len(xs),min(xs),max(xs),y))
    if not best: print(label,'none');return
    L,x0,x1,y=max(best)
    print(label,'y pt',round(clip.y0+y/Z,2),'x pt',round(clip.x0+x0/Z,2),round(clip.x0+x1/Z,2),'extent ft',round((x1-x0)/Z/PPF,2),'yellow px ft',round(L/Z/PPF,2))
scan(pymupdf.Rect(80,690,220,720),'elev7 lower C7')
scan(pymupdf.Rect(890,690,1030,720),'elev11 lower C7')
scan(pymupdf.Rect(80,605,220,625),'elev7 top C7')
