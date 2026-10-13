"""Pixel-area cross-check of PlanSwift overlay colours on a markup page.
usage: colarea.py page x0 y0 x1 y1 sheet_pt_per_ft [zoom]
markup page = issued 36x24 sheet scaled by 1190.52/2592."""
import pymupdf,glob,re,sys
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(ROOT+'/source/markups/MARKUPS*.pdf')):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
n=int(sys.argv[1]); x0,y0,x1,y1=map(float,sys.argv[2:6]); sppf=float(sys.argv[6]); z=float(sys.argv[7]) if len(sys.argv)>7 else 4
p=page(n); r=p.rect
pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=pymupdf.Rect(r.width*x0,r.height*y0,r.width*x1,r.height*y1))
pxft=z*sppf*1190.52/2592; pxsf=pxft*pxft
s=pix.samples; c={'cyan':0,'green':0,'blue':0,'magenta':0,'purple':0}
for i in range(0,len(s),pix.n):
    R,G,B=s[i],s[i+1],s[i+2]
    if R<130 and G>200 and B>200: c['cyan']+=1
    elif R<130 and G>200 and B<130: c['green']+=1
    elif R<130 and G<130 and B>190: c['blue']+=1
    elif R>140 and G<90 and B>140: c['magenta']+=1
    elif R>120 and G<120 and B>200: c['purple']+=1
print({k:round(v/pxsf,2) for k,v in c.items()}, 'px/ft',round(pxft,2))
