import pymupdf
p=pymupdf.Pixmap('/home/user/work/09e-painting/v-p08-gather.png')
w,h,n=p.width,p.height,p.n; s=p.samples
def px(x,y):
    i=(y*w+x)*n; return s[i],s[i+1],s[i+2]
def blue(c): r,g,b=c; return b>=45 and r<45 and b>g+10
# horizontal extents of blue at rows
for y in (195,198,238,240,242):
    xs=[x for x in range(w) if blue(px(x,y))]
    # segments
    seg=[];st=None;prev=None
    for x in xs:
        if st is None: st=x
        elif x!=prev+1: seg.append((st,prev)); st=x
        prev=x
    if st is not None: seg.append((st,prev))
    print(y,[sg for sg in seg if sg[1]-sg[0]>5])
for x in (268,270,272,1173,1175,1177):
    ys=[y for y in range(150,260) if blue(px(x,y))]
    print('x',x,min(ys) if ys else None,max(ys) if ys else None,len(ys))
# room LVT green fill extents at y=400
row=[x for x in range(w) if (lambda c:c[1]>150 and c[0]<140 and c[2]<140)(px(x,400))]
print('green fill x', min(row), max(row))
