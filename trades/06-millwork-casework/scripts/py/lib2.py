import glob, re, pymupdf
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(25); r=p.rect; z=3
def grab(box):
    clip=pymupdf.Rect(r.width*box[0],r.height*box[1],r.width*box[2],r.height*box[3])
    pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=clip,alpha=False)
    return pix
def stats(pix):
    s=pix.samples;w,h=pix.width,pix.height
    pts=[(x,y) for y in range(h) for x in range(w) if (lambda i: s[i]>150 and s[i]-s[i+1]>60 and s[i]-s[i+2]>60)((y*w+x)*3)]
    xs=[a for a,b in pts]; ys=[b for a,b in pts]
    return len(pts),min(xs),max(xs),min(ys),max(ys)
# elevation: find the vertical extent of coloured in cased bay column x=420 (crop coords)
pix=grab((0.58,0.38,0.99,0.72)); s=pix.samples; w=pix.width
col=[y for y in range(pix.height) if (lambda i: s[i]>150 and s[i]-s[i+1]>60)((y*w+420)*3)]
print('cased col y',col[0],col[-1])
row=[x for x in range(w) if (lambda i: s[i]>150 and s[i]-s[i+1]>60)((150*w+x)*3)]
print('top row x',row[0],row[-1])
pl=grab((0.62,0.76,0.88,0.86)); print('plan',stats(pl))
