import pymupdf,sys
doc=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Architectural/A-410-ENLARGED-RESTROOM-PLANS-&-ELEVATIONS-Rev.0.pdf')
pg=doc[0]; W,H=pg.rect.width,pg.rect.height
print(W,H)
def region(fx0,fy0,fx1,fy1,zx0,zy0,zx1,zy1,zoom=4):
    # zx: pixel box within crop
    X0=W*fx0+zx0/zoom; Y0=H*fy0+zy0/zoom; X1=W*fx0+zx1/zoom; Y1=H*fy0+zy1/zoom
    return pymupdf.Rect(X0,Y0,X1,Y1)
for name,r in [('B horiz',region(.19,.13,.36,.38,400,940,880,990)),('B vert',region(.19,.13,.36,.38,340,660,400,930)),
               ('C horiz',region(.36,.13,.53,.38,850,940,1400,990)),('C vert',region(.36,.13,.53,.38,1010,660,1060,930))]:
    xs=[];ys=[]
    for d in pg.get_drawings():
        if r.contains(d['rect']):
            xs+= [d['rect'].x0,d['rect'].x1]; ys+=[d['rect'].y0,d['rect'].y1]
    if xs: print(name, 'width in (3pt=1in):', round((max(xs)-min(xs))/3,2),'height in:',round((max(ys)-min(ys))/3,2))
for name,r in [('B mirror',region(.19,.13,.36,.38,1068,476,1368,920))]:
    xs=[];ys=[]
    for d in pg.get_drawings():
        if r.contains(d['rect']) and d['rect'].width>60:
            xs+= [d['rect'].x0,d['rect'].x1]; ys+=[d['rect'].y0,d['rect'].y1]
    print(name,'W in',round((max(xs)-min(xs))/3,2),'H in',round((max(ys)-min(ys))/3,2))
