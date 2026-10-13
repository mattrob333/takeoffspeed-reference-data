import pymupdf, collections
pix=pymupdf.Pixmap('p64-z4.png')
w,h,n=pix.width,pix.height,pix.n
s=pix.samples
# sample colors of known features
def at(x,y):
    i=(y*w+x)*n; return tuple(s[i:i+3])
# zoom4: markup pt *4. one-story centre approx markup (300,295) ; pavement (230,380); two-story (380,420)
for nm,(x,y) in {'one':(300,290),'pav':(215,400),'two':(370,440),'side':(255,262),'ramp':(400,355)}.items():
    print(nm, at(x*4,y*4))
