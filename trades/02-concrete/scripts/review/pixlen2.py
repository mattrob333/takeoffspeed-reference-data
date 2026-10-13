import glob, re, os, pymupdf
from collections import Counter
ROOT='/home/user/takeoffspeed-reference-data'
def markup_page(n):
    for f in sorted(glob.glob(os.path.join(ROOT,'source/markups/MARKUPS*.pdf'))):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
page=markup_page(33); r=page.rect; Z=4
def pix(box):
    clip=pymupdf.Rect(r.x0+r.width*box[0], r.y0+r.height*box[1], r.x0+r.width*box[2], r.y0+r.height*box[3])
    return page.get_pixmap(matrix=pymupdf.Matrix(Z,Z),clip=clip,alpha=False)
def hist(box):
    p=pix(box); s=p.samples; n=p.n; c=Counter()
    for i in range(0,len(s),n):
        col=(s[i]//8*8,s[i+1]//8*8,s[i+2]//8*8)
        if max(col)-min(col)>40: c[col]+=1   # colourful only
    return c
# NE corner straight run region: periwinkle + slate over white
h=hist((0.62,0.27,0.70,0.30))
print('NE run colours', h.most_common(12))
# south wing stub region (olive over white)
h=hist((0.63,0.76,0.66,0.84))
print('wing stub colours', h.most_common(8))
# saw-cut yellow over teal: region inside slab
h=hist((0.50,0.40,0.58,0.48))
print('slab interior colours', h.most_common(8))
