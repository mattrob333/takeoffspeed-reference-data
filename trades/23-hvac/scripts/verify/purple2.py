import pymupdf,glob,re,os,sys
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(os.path.join(ROOT,'source/markups/MARKUPS*.pdf'))):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(53); W,H=p.rect.width,p.rect.height
Z=8; box=[0.255,0.315,0.345,0.360]
clip=pymupdf.Rect(W*box[0],H*box[1],W*box[2],H*box[3])
pix=p.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip,alpha=False)
pix.save('refrig_z8.png')
s=pix.samples;PW,PH,n=pix.width,pix.height,pix.n
pxft=18*W/2592*Z
print('px/ft',round(pxft,2),PW,PH)
def purp(x,y):
    i=(y*PW+x)*n; r,g,b=s[i],s[i+1],s[i+2]
    return r-g>40 and b-g>40 and abs(r-b)<30
M=[[purp(x,y) for x in range(PW)] for y in range(PH)]
# rows: count purple px per row
for y in range(PH):
    c=sum(M[y])
    if c>60:
        xs=[x for x in range(PW) if M[y][x]]
        print('row',y,'px',c,'x',xs[0],xs[-1],'ft span %.2f'%((xs[-1]-xs[0])/pxft))
# columns
print('cols')
for x in range(PW):
    c=sum(M[y][x] for y in range(PH))
    if c>40:
        ys=[y for y in range(PH) if M[y][x]]
        print('col',x,'px',c,'y',ys[0],ys[-1])
# polyline estimate (stroke centrelines from the row/col tallies above)
segs={'FCU riser leg (x=82, y 192->111)':(192-111),
 'upper pipe (y=111, x 82->778)':(778-82),
 'end cap (x=778, y 111->135)':(135-111),
 'lower pipe (y=135, x 778->124)':(778-124),
 'drop (x=124, y 135->194)':(194-135),
 'third leg (y=193, x 124->651)':(651-124)}
tot=0
for k,v in segs.items():
    print('%-40s %6.2f ft'%(k,v/pxft)); tot+=v/pxft
print('total %.2f ft vs legend 30.9'%tot)
print('one route (riser + upper pipe) %.2f ft'%((192-111+778-82)/pxft))
print('both drawn pipes + legs, no third leg %.2f ft'%((192-111+778-82+135-111+778-124+194-135)/pxft))
