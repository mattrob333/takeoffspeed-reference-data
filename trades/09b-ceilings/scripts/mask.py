import pymupdf, glob, sys
f=glob.glob('/home/user/takeoffspeed-reference-data/source/markups/*_p01-10.pdf')[0]
pg=pymupdf.open(f)[4]; r=pg.rect
z=3
x0,y0,x1,y1=0.15,0.15,0.58,0.82
clip=pymupdf.Rect(r.width*x0, r.height*y0, r.width*x1, r.height*y1)
pix=pg.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=clip)
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
targets={'S36BS':(255,102,255),'S66_4':(101,255,255),'S36_16':(177,101,101),'S46_3':(101,178,100),'S59_26':(177,178,100),'BR5':(102,101,177),'BR8':(178,101,179),'S2H':(100,178,178),'MECHO':(255,101,101)}
# derive base colour c (alpha .6): c=(sw-0.4*255)/0.6
def base(sw): return tuple(max(0,min(255,(v-102)/0.6)) for v in sw)
out=bytearray(s)
import collections
cnt=collections.Counter()
for y in range(H):
  for x in range(W):
    i=(y*W+x)*n
    p=s[i:i+3]
    hit=None
    for nm,t in targets.items():
      if abs(p[0]-t[0])<8 and abs(p[1]-t[1])<8 and abs(p[2]-t[2])<8: hit=nm;break
    if hit: cnt[hit]+=1
for k,v in cnt.items(): print(k,v)
