import glob,re,pymupdf
for f in sorted(glob.glob('source/markups/MARKUPS*.pdf')):
    a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
    if a<=34<=b: p=pymupdf.open(f)[34-a]
Z=8; PPF=8.2675
for xpt in (570,610,660,700,750,790,830,870,910,930):
    clip=pymupdf.Rect(xpt,415,xpt+1,475)
    pix=p.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip)
    W,H,n=pix.width,pix.height,pix.n; s=pix.samples
    dark=[y for y in range(H) if s[(y*W)*n+1]<50 and s[(y*W)*n]>100]
    if dark: print(xpt,'top',round(415+dark[0]/Z,2),'bottom',round(415+dark[-1]/Z,2),'depth ft',round((dark[-1]-dark[0])/Z/PPF,2))
