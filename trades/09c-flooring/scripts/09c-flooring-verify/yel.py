import pymupdf
pm=pymupdf.Pixmap('p16-elA-base.png'); W,H,n=pm.width,pm.height,pm.n; s=pm.samples
def px(x,y): i=(y*W+x)*n; return s[i],s[i+1],s[i+2]
def isy(c): return c[0]>200 and c[1]>200 and c[2]<140
def isblack(c): return c[0]<80 and c[1]<80 and c[2]<80
# find wall extents along a row at y=255 (base line) black
for y in range(200,270):
    xs=[x for x in range(W) if isy(px(x,y))]
    if len(xs)>50:
        # segments
        segs=[];st=xs[0];pr=xs[0]
        for x in xs[1:]:
            if x-pr>3: segs.append((st,pr)); st=x
            pr=x
        segs.append((st,pr))
        print(y,segs)
