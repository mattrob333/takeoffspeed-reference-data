import pymupdf, collections
d=pymupdf.open('source/drawings/Structural/S-203-Structural-Plan---Roof-Rev.0.pdf');p=d[0]
segs=[]
for dr in p.get_drawings():
    for it in dr['items']:
        if it[0]=='l':
            a,b=it[1],it[2]
            if abs(a.x-b.x)<0.5 and abs(a.y-b.y)>60:
                y0,y1=sorted([a.y,b.y])
                segs.append((round(a.x,1),round(y0,1),round(y1,1),dr.get('width'),dr.get('dashes')))
            if abs(a.y-b.y)<0.5 and abs(a.x-b.x)>300:
                x0,x1=sorted([a.x,b.x])
                print('H',round(a.y,1),round(x0,1),round(x1,1),dr.get('width'),dr.get('dashes'))
segs=sorted(set(segs))
for s in segs:
    if 1200<s[0]<2100 and s[2]>800: print('V',s, 'len_ft',round((s[2]-s[1])/18,2))
