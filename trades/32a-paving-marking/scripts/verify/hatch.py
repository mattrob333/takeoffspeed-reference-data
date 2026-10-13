import pymupdf, math
p = pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Civil/C-3.0-SITE-PLAN-Rev.0.pdf')[0]
F=20/72.0; W,H=p.rect.width,p.rect.height
# find the aisle outline: axis-aligned lines near the hatch
X0,X1,Y0,Y1=0.325,0.375,0.498,0.516
allseg=[]
for d in p.get_drawings():
  for it in d['items']:
    if it[0]=='re':
      r=it[1]
      if X0<=r.x0/W<=X1 and Y0<=r.y0/H<=Y1: print('rect',r, r.width*F, r.height*F)
    if it[0]!='l': continue
    a,b=it[1],it[2]
    if X0<=a.x/W<=X1 and Y0<=a.y/H<=Y1 and X0<=b.x/W<=X1 and Y0<=b.y/H<=Y1:
      dx,dy=abs(b.x-a.x),abs(b.y-a.y); L=math.hypot(dx,dy)*F
      allseg.append((a.x/W,a.y/H,b.x/W,b.y/H,dx,dy,L,d.get('color'),d.get('width')))
for s in sorted(allseg,key=lambda s:(s[4]==0 or s[5]==0, s[0])):
  print(' '.join('%.4f'%v for v in s[:4]),'L=%.2f'%s[6],'ratio=%s'%(round(s[4]/s[5],2) if s[5] else 'inf'),s[7],round(s[8] or 0,2))
