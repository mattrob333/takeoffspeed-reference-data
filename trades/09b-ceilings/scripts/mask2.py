import pymupdf, glob, collections
f=glob.glob('/home/user/takeoffspeed-reference-data/source/markups/*_p01-10.pdf')[0]
pg=pymupdf.open(f)[4]; r=pg.rect
z=3
x0,y0,x1,y1=0.15,0.15,0.58,0.82
clip=pymupdf.Rect(r.width*x0, r.height*y0, r.width*x1, r.height*y1)
pix=pg.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=clip)
W,H,n=pix.width,pix.height,pix.n; s=pix.samples
sw={'S36BS':(255,102,255),'S66_4':(101,255,255),'S36_16':(177,101,101),'S46_3':(101,178,100),'S59_26':(177,178,100),'BR5':(102,101,177),'BR8':(178,101,179),'S2H':(100,178,178),'MECHO':(255,101,101)}
base={k:tuple((v-102)/0.6 for v in c) for k,c in sw.items()}
fills={'white':(255,255,255),'AC1':(100,178,178),'GWB':(101,254,101),'AC2':(255,102,255),'ACM':(101,255,255),'EXP':(254,253,100)}
exp={}
for k,c in base.items():
  for fn,fc in fills.items():
    e=tuple(round(0.4*fv+0.6*cv) for fv,cv in zip(fc,c))
    if max(abs(a-b) for a,b in zip(e,fc))>25: exp[(k,fn)]=e
cells=collections.defaultdict(collections.Counter)
for y in range(H):
  for x in range(W):
    i=(y*W+x)*n; p=s[i:i+3]
    for key,e in exp.items():
      if abs(p[0]-e[0])<7 and abs(p[1]-e[1])<7 and abs(p[2]-e[2])<7:
        cells[key][(x//40,y//40)]+=1; break
for key,c in sorted(cells.items()):
  tot=sum(c.values())
  big=[(cx,cy,v) for (cx,cy),v in c.items() if v>=15]
  print(key, exp[key], tot, sorted(big)[:40])
