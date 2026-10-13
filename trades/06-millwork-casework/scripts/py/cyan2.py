import glob, re, pymupdf
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(30); r=p.rect; z=8
for name,box,xr in [('plan1',(0.76,0.78,0.88,0.90),range(95,125)),('plan2',(0.76,0.62,0.88,0.76),list(range(180,200))+list(range(885,905)))]:
    clip=pymupdf.Rect(r.width*box[0],r.height*box[1],r.width*box[2],r.height*box[3])
    pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=clip,alpha=False); s=pix.samples; w,h=pix.width,pix.height
    for x in xr:
        n=sum(1 for y in range(h) if (lambda i: s[i+2]>150 and s[i+1]>150 and s[i]<170 and s[i+1]-s[i]>50)((y*w+x)*3))
        if n: print(name,x,n)
