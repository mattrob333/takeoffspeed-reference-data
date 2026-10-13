import pymupdf
d=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Architectural/A-410-ENLARGED-RESTROOM-PLANS-&-ELEVATIONS-Rev.0.pdf'); p=d[0]
FT=36.0; z=4
regions={'B':[(580.5,850.8)],'C':[(1037.0,1313.3)],'D':[(1518.0,1662.2),(1782.3,1794.3)]}
y0,y1=372.7,570.9
tot={'dark':0,'grey':0,'other':0}
for k,spans in regions.items():
    res={'dark':0,'grey':0,'other':0}
    for a,b in spans:
        pix=p.get_pixmap(matrix=pymupdf.Matrix(z,z),clip=pymupdf.Rect(a,y0,b,y1),colorspace=pymupdf.csGRAY)
        s=pix.samples
        for v in s:
            if v<120: res['dark']+=1
            elif v<215: res['grey']+=1
            else: res['other']+=1
    px_per_sf=(FT*z)**2
    out={kk:round(vv/px_per_sf,2) for kk,vv in res.items()}
    print(k,out,'sum',round(sum(out.values()),2))
    for kk in tot: tot[kk]+=out[kk]
print('per room',{k:round(v,2) for k,v in tot.items()})
print('x2',{k:round(2*v,2) for k,v in tot.items()})
