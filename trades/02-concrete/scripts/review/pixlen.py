import sys, glob, re, os, pymupdf
ROOT='/home/user/takeoffspeed-reference-data'
def markup_page(n):
    for f in sorted(glob.glob(os.path.join(ROOT,'source/markups/MARKUPS*.pdf'))):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
page=markup_page(33); r=page.rect; print('page rect',r)
Z=4
def pix(box):
    clip=pymupdf.Rect(r.x0+r.width*box[0], r.y0+r.height*box[1], r.x0+r.width*box[2], r.y0+r.height*box[3])
    p=page.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip,alpha=False)
    return p
def rgb_at(p,x,y):
    i=(y*p.width+x)*p.n; s=p.samples; return (s[i],s[i+1],s[i+2])
# sample legend swatch colours
leg=pix((0,0.78,0.40,1.0))
rows={'F50':57,'F38':92,'F10050':127,'F70':162,'F30':197,'F60':232,'F7040':267,'SCJ':303,'WF20':338,'BP12':373,'BP1518':408,'BP14':443,'ISO':479,'STEM10':514,'STEM8':549,'SLAB':584,'NEW':619}
sw={}
for k,y in rows.items():
    # average a few px around swatch centre x=1810
    cs=[rgb_at(leg,x,yy) for x in range(1800,1821) for yy in range(y-5,y+6)]
    sw[k]=tuple(sum(c[i] for c in cs)//len(cs) for i in range(3))
for k,v in sw.items(): print(k,v)
def close(c,t,tol): return abs(c[0]-t[0])<=tol and abs(c[1]-t[1])<=tol and abs(c[2]-t[2])<=tol
def count(box, targets, tol=18):
    p=pix(box); s=p.samples; n=p.n; W=p.width; H=p.height
    res={k:0 for k in targets}
    for i in range(0,W*H*n,n):
        c=(s[i],s[i+1],s[i+2])
        for k,t in targets.items():
            if close(c,t,tol): res[k]+=1; break
    return res,W,H
# line width: NE corner periwinkle straight run: box (0.70,0.26,0.74,0.30)
res,W,H=count((0.62,0.27,0.70,0.30),{'WF20':sw['WF20'],'STEM8':sw['STEM8']})
print('calib region',res,W,H)
# width via column scan at x middle
p=pix((0.62,0.27,0.70,0.30))
for name in ('WF20','STEM8'):
    widths=[]
    for x in range(0,p.width,25):
        ys=[y for y in range(p.height) if close(rgb_at(p,x,y),sw[name],18)]
        if ys: widths.append(len(ys))
    print(name,'col widths',widths)
