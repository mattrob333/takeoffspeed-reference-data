import pymupdf
lines={'S36BS':(255,0,255),'S66_4':(0,200,255),'S36_16':(150,0,0),'S46_3':(0,160,0),'S59_26':(160,160,0),'BR5':(0,0,255),'BR8':(255,120,0),'S2H':(0,0,0),'MECHO':(255,0,0)}
base=pymupdf.Pixmap("mcrop.png"); mm=pymupdf.Pixmap("mask_BR5.png"); W,H=mm.width,mm.height; BW=base.width
out=bytearray(b'')
bs=base.samples; n=base.n
img=bytearray(W*H*3)
for i in range(W*H):
    yy0,xx0=divmod(i,W); p=bs[(yy0*BW+xx0)*n:(yy0*BW+xx0)*n+3]; g=sum(p)//3; v=200+g//5
    img[i*3:i*3+3]=bytes((v,v,v))
for ln,col in lines.items():
    if ln in ('S36BS','S66_4','S2H','MECHO'): continue
    m=pymupdf.Pixmap(f'mask_{ln}.png').samples
    for y in range(H):
        for x in range(W):
            if m[(y*W+x)*3]==0:
                for dy in (-1,0,1):
                    for dx in (-1,0,1):
                        yy,xx=y+dy,x+dx
                        if 0<=yy<H and 0<=xx<W: img[(yy*W+xx)*3:(yy*W+xx)*3+3]=bytes(col)
pm=pymupdf.Pixmap(pymupdf.csRGB,W,H,bytes(img),False); pm.save('compose.png')
