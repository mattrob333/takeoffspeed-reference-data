import pymupdf, glob, collections
ROOT='/home/user/takeoffspeed-reference-data'
f=glob.glob(ROOT+'/source/markups/MARKUPS*p21-30.pdf')[0]
p=pymupdf.open(f)[1]
z=3
pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z))
W,H,n=pix.width,pix.height,pix.n
s=pix.samples
print(W,H,n)
# histogram of saturated colors in drawing area
c=collections.Counter()
for y in range(int(0.35*H),int(0.97*H),2):
    row=s[y*W*n:(y+1)*W*n]
    for x in range(0,int(0.88*W),2):
        r,g,b=row[x*n],row[x*n+1],row[x*n+2]
        if max(r,g,b)-min(r,g,b)>60:
            c[(r//16*16,g//16*16,b//16*16)]+=1
for k,v in c.most_common(20): print(k,v)
