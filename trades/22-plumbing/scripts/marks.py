import glob,re,pymupdf
ROOT='/home/user/takeoffspeed-reference-data'
def mp(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
for n in (59,60):
    pg=mp(n); pix=pg.get_pixmap(matrix=pymupdf.Matrix(1,1)); w,h,s=pix.width,pix.height,pix.samples; nc=pix.n
    cells={}
    for y in range(0,h):
        for x in range(0,w):
            i=(y*w+x)*nc; r,g,b=s[i],s[i+1],s[i+2]
            if max(r,g,b)-min(r,g,b)>80:
                cells.setdefault((x//20,y//20),0); cells[(x//20,y//20)]+=1
    # cluster
    seen=set(); clusters=[]
    for c in cells:
        if c in seen: continue
        st=[c]; seen.add(c); comp=[]
        while st:
            k=st.pop(); comp.append(k)
            for dx in (-1,0,1):
                for dy in (-1,0,1):
                    m=(k[0]+dx,k[1]+dy)
                    if m in cells and m not in seen: seen.add(m); st.append(m)
        xs=[k[0]*20 for k in comp]; ys=[k[1]*20 for k in comp]
        clusters.append((min(xs),min(ys),max(xs)+20,max(ys)+20,sum(cells[k] for k in comp)))
    print(n, sorted(clusters, key=lambda c:-c[4])[:15])
