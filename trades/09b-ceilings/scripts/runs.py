import pymupdf, sys
K=1190.52001953125/2592.0; Z=3.0; pxft=18*K*Z  # 1/4"=1' -> 18pt/ft
for ln in sys.argv[1:]:
    m=pymupdf.Pixmap(f'mask_{ln}.png'); W,H=m.width,m.height; s=m.samples
    blk=lambda x,y: s[(y*W+x)*3]==0
    segs=[]
    # vertical runs (allow gaps 4px)
    for x in range(W):
        y=0
        while y<H:
            if blk(x,y):
                y0=y; gap=0
                while y<H and gap<=4:
                    if blk(x,y): gap=0
                    else: gap+=1
                    y+=1
                L=y-gap-y0
                if L>40: segs.append(('V',x,y0,L))
            y+=1
    for y in range(H):
        x=0
        while x<W:
            if blk(x,y):
                x0=x; gap=0
                while x<W and gap<=4:
                    if blk(x,y): gap=0
                    else: gap+=1
                    x+=1
                L=x-gap-x0
                if L>40: segs.append(('H',y,x0,L))
            x+=1
    # merge adjacent parallel duplicates
    segs.sort()
    merged=[]
    for sgm in segs:
        if merged and merged[-1][0]==sgm[0] and abs(merged[-1][1]-sgm[1])<=3 and abs(merged[-1][2]-sgm[2])<=10: 
            if sgm[3]>merged[-1][3]: merged[-1]=sgm
            continue
        merged.append(sgm)
    tot=sum(x[3] for x in merged)/pxft
    print(ln, round(tot,1), [(d,a,b,round(L/pxft,1)) for d,a,b,L in merged])
