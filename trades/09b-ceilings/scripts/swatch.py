import pymupdf, glob, sys
f=glob.glob('/home/user/takeoffspeed-reference-data/source/markups/*_p01-10.pdf')[0]
pg=pymupdf.open(f)[4]; r=pg.rect
z=4
clip=pymupdf.Rect(0, r.height*0.80, r.width*0.30, r.height*0.97)
pix=pg.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=clip)
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
rows=[57,92,128,163,199,234,269,304,340,376,411,446,481,516,551]
names=['AC1','MECHO','GWB','EXPOSED','S36BS','S66_4','S36_16','S46_3','S59_26','BR5','BR8','S2H','ACM3','EIFS','AC2']
for nm,y in zip(names,rows):
    i=(y*W+1355)*n
    print(nm, tuple(s[i:i+3]))
