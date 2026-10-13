import pymupdf, collections
p=pymupdf.Pixmap('/home/user/work/09e-painting/v-p08-gather.png')
w,h,n=p.width,p.height,p.n
s=p.samples
def px(x,y):
    i=(y*w+x)*n; return s[i],s[i+1],s[i+2]
# column profile at x=700 and x=215, rows 150-260
for x in (215,700,1230,270,1175):
    print('x',x,[ (y,px(x,y)) for y in range(180,250,3)])
