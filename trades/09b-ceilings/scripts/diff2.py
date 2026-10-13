import pymupdf, glob, collections, sys
f=glob.glob('/home/user/takeoffspeed-reference-data/source/markups/*_p01-10.pdf')[0]
mp=pymupdf.open(f)[4]
sp=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Architectural/A-130-REFLECTED-CEILING-PLAN-Rev.0.pdf')[0]
K=1190.52001953125/2592.0; OY=24.119873046875
Z=3.0
# sheet region in sheet points
sx0,sy0,sx1,sy1=[float(v) for v in sys.argv[1:5]] if len(sys.argv)>4 else (380,300,1300,1640)
mclip=pymupdf.Rect(sx0*K, OY+sy0*K, sx1*K, OY+sy1*K)
mpix=mp.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=mclip)
spix=sp.get_pixmap(matrix=pymupdf.Matrix(Z*K,Z*K),clip=pymupdf.Rect(sx0,sy0,sx1,sy1))
print(mpix.width,mpix.height,spix.width,spix.height)
W=min(mpix.width,spix.width); H=min(mpix.height,spix.height)
ms,ss,mn,sn=mpix.samples,spix.samples,mpix.n,spix.n
bases={'S36BS':(255,0,255),'S66_4':(0,255,255),'S36_16':(125,0,0),'S46_3':(0,127,0),'S59_26':(125,127,0),'BR5':(0,0,125),'BR8':(127,0,128),'S2H':(0,127,127),'MECHO':(255,0,0),
 'AC1':(0,127,127),'GWB':(0,255,0),'EXP':(255,255,0),'AC2':(255,0,255),'ACM':(0,255,255)}
# fill bases: same colours. Model: m = s*0.4^k + ... ; we test one layer (line over white/sheet) and two layers (line over fill)
fills={'none':None,'AC1':(0,127,127),'GWB':(0,255,0),'AC2':(255,0,255),'ACM':(0,255,255),'EXP':(255,255,0)}
lines=['S36BS','S66_4','S36_16','S46_3','S59_26','BR5','BR8','S2H','MECHO']
out={k:bytearray(b'\xff'*(W*H*3)) for k in lines}
cnt=collections.Counter()
for y in range(H):
  for x in range(W):
    i=(y*mpix.width+x)*mn; j=(y*spix.width+x)*sn
    m=ms[i:i+3]; s=ss[j:j+3]
    if sum(s)<600: continue  # skip sheet linework
    best=None
    for fn,fc in fills.items():
      under = s if fc is None else tuple(0.4*a+0.6*b for a,b in zip(s,fc))
      c=tuple((a-0.4*b)/0.6 for a,b in zip(m,under))
      for ln in lines:
        if fc is not None and bases[ln]==fc: continue
        d=max(abs(a-b) for a,b in zip(c,bases[ln]))
        if best is None or d<best[0]: best=(d,ln,fn)
    if best[0]<22:
      # exclude case 'none' where the line colour equals a fill colour (area fill itself)
      ln=best[1]
      if best[2]=='none' and ln in ('S36BS','S66_4','S2H'): continue
      cnt[(ln,best[2])]+=1
      k=(y*W+x)*3; out[ln][k:k+3]=b'\x00\x00\x00'
for k,v in cnt.most_common(): print(k,v)
for ln in lines:
  pm=pymupdf.Pixmap(pymupdf.csRGB, W, H, bytes(out[ln]), False); pm.save(f'mask_{ln}.png')
# also save the markup crop
mpix.save('mcrop.png')
