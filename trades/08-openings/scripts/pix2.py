import pymupdf, glob
ROOT='/home/user/takeoffspeed-reference-data'
f=glob.glob(ROOT+'/source/markups/MARKUPS*p21-30.pdf')[0]
p=pymupdf.open(f)[1]
z=4
pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z))
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
def fam(r,g,b):
    if r<140 and g>170 and b>170 and abs(g-b)<40: return 'cyan'
    if r<140 and g>170 and b<140: return 'green'
    if 140<r<200 and 60<g<120 and 60<b<120 and abs(g-b)<25: return 'rose'
    return None
regions={}
y0=int(0.35*H)
for y in range(y0,int(0.97*H)):
    row=s[y*W*n:(y+1)*W*n]
    for x in range(0,int(0.88*W)):
        k=fam(row[x*n],row[x*n+1],row[x*n+2])
        if k:
            # split by half-page column
            key=(k, 'top' if y<0.66*H else 'bot', x//(W//8))
            regions.setdefault(key,[0,1e9,1e9,0,0])
            R=regions[key]; R[0]+=1; R[1]=min(R[1],x); R[2]=min(R[2],y); R[3]=max(R[3],x); R[4]=max(R[4],y)
for k,v in sorted(regions.items()):
    if v[0]>200: print(k,v, 'w',v[3]-v[1],'h',v[4]-v[2])
