"""Count pixels near a target colour inside a crop of a markup page.
usage: pxcount.py page x0 y0 x1 y1 zoom R G B tol
Coordinates are page fractions. Prints count and the bounding box (fractions) of matches."""
import sys, glob, re, os
import pymupdf
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
n=int(sys.argv[1]); x0,y0,x1,y1,z=map(float,sys.argv[2:7]); R,G,B,tol=map(int,sys.argv[7:11])
p=page(n); r=p.rect
clip=pymupdf.Rect(r.width*x0,r.height*y0,r.width*x1,r.height*y1)
pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=clip,alpha=False)
s=pix.samples; w,h=pix.width,pix.height; nc=pix.n
cnt=0; minx=miny=10**9; maxx=maxy=-1
for y in range(h):
    row=y*w*nc
    for x in range(w):
        i=row+x*nc
        if abs(s[i]-R)<=tol and abs(s[i+1]-G)<=tol and abs(s[i+2]-B)<=tol:
            cnt+=1
            if x<minx:minx=x
            if x>maxx:maxx=x
            if y<miny:miny=y
            if y>maxy:maxy=y
# pts per pixel = 1/z ; report in page points
print('pixels',cnt,'pt2',cnt/(z*z),'bbox_pt',(clip.x0+minx/z,clip.y0+miny/z,clip.x0+maxx/z,clip.y0+maxy/z))
