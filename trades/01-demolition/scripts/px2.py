import pymupdf, collections
pix=pymupdf.Pixmap('p64-z4.png')
w,h,n=pix.width,pix.height,pix.n
s=pix.samples
c=collections.Counter()
for y in range(0,int(h*0.72)):   # above legend
    row=y*w*n
    for x in range(0,int(w*0.74),1):
        i=row+x*n
        c[(s[i]//8*8,s[i+1]//8*8,s[i+2]//8*8)]+=1
for k,v in c.most_common(25): print(k,v)
