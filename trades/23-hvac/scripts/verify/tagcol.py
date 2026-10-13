import pymupdf,glob,re,os,collections
ROOT='/home/user/takeoffspeed-reference-data'
def page(n):
    for f in sorted(glob.glob(os.path.join(ROOT,'source/markups/MARKUPS*.pdf'))):
        a,b=map(int,re.search(r'_p(\d+)-(\d+)',f).groups())
        if a<=n<=b: return pymupdf.open(f)[n-a]
p=page(53); W,H=p.rect.width,p.rect.height
pix=p.get_pixmap(matrix=pymupdf.Matrix(3,3),alpha=False); s=pix.samples;PW=pix.width;n=pix.n
sh=pymupdf.open(ROOT+'/source/drawings/Mechanical/M-301-MECHANICAL-PROPOSED-CEILING-PLAN-Rev.0.pdf')[0]
SW,SH=sh.rect.width,sh.rect.height
ws=sh.get_text('words')
named={'magenta':(255,102,255),'cyan':(101,255,255),'olive':(177,178,100),'brown':(177,101,101),'mgreen':(101,178,101),'indigo':(101,102,177),'bgreen':(101,255,101),'yellow':(255,254,101),'purple':(178,101,179),'teal':(101,178,178),'salmon':(255,101,101),'periw':(101,102,255)}
def dom(fx,fy,r=25):
    cx,cy=int(fx*W*3),int(fy*H*3); c=collections.Counter()
    for y in range(cy-r,cy+r,2):
        for x in range(cx-r,cx+r,2):
            i=(y*PW+x)*n; px=s[i:i+3]
            for k,v in named.items():
                if max(abs(a-b) for a,b in zip(px,v))<=20: c[k]+=1
    return c.most_common(2)
for i,w in enumerate(ws):
    t=w[4]
    if (t.endswith('S') and t[:-1].isdigit()) or t in ('895R','220R','50R') :
        fx=(w[0]+w[2])/2/SW; fy=(w[1]+w[3])/2/SH; print(t, round(fx,3),round(fy,3), dom(fx,fy))
    if t=='LSD' and i+1<len(ws) and ws[i+1][4] in ('(3-48")','(2-24")'):
        cfm=[x[4] for x in ws if abs(x[0]-w[0])<15 and 0<x[1]-w[1]<12 and x[4].isdigit()]
        fx=(w[0]+w[2])/2/SW; fy=(w[1]+w[3])/2/SH; print('LSD',ws[i+1][4],cfm, dom(fx,fy,35))
