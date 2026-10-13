import glob,re,pymupdf
for f in sorted(glob.glob('source/markups/MARKUPS*.pdf')):
    a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
    if a<=34<=b: p=pymupdf.open(f)[34-a]
Z=4; PPF=8.2675
clip=pymupdf.Rect(540,420,960,470)
pix=p.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip)
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
cnt=0; xs=[];ys=[]
for y in range(H):
    for x in range(W):
        i=(y*W+x)*n; r,g,b=s[i],s[i+1],s[i+2]
        if 120<=r<=165 and g<=50 and 20<=b<=90: cnt+=1; xs.append(x); ys.append(y)
print('dark px area SF',round(cnt/(Z*PPF)**2,1),'x',round(clip.x0+min(xs)/Z,1),round(clip.x0+max(xs)/Z,1),'y',round(clip.y0+min(ys)/Z,1),round(clip.y0+max(ys)/Z,1))
w=(max(xs)-min(xs))/Z/PPF; h=(max(ys)-min(ys))/Z/PPF
print('bbox ft',round(w,2),round(h,2),'SF',round(w*h,1))
