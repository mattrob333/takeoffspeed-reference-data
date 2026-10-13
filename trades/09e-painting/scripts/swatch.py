import pymupdf, glob, re, sys
from collections import Counter
f=glob.glob('/home/user/takeoffspeed-reference-data/source/markups/MARKUPS*_p01-10.pdf')[0]
pg=pymupdf.open(f)[7]
z=4
pix=pg.get_pixmap(matrix=pymupdf.Matrix(z,z))
W,H=pix.width,pix.height
print(W,H)
# legend swatches are at x ~ 0.283 of page (swatch col), rows from y ~0.662 to 0.963
s=pix.samples; n=pix.n
def px(x,y):
    i=(y*W+x)*n; return tuple(s[i:i+3])
# sample swatch column: find the x of swatch by scanning row of first legend entry
y0=int(H*0.662)
for fy in [0.662+0.0111*k for k in range(28)]:
    y=int(H*fy)
    c=Counter(px(x,yy) for x in range(int(W*0.279),int(W*0.287)) for yy in range(y-3,y+3))
    print(round(fy,4), c.most_common(3))
