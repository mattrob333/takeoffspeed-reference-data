import pymupdf,re,collections,json
pg=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Architectural/A-410-ENLARGED-RESTROOM-PLANS-&-ELEVATIONS-Rev.0.pdf')[0]
W,H=pg.rect.width,pg.rect.height
regions={'plan 6/A-410':(0.03,0.43,0.38,0.70),'elevations 7-10':(0.03,0.10,0.72,0.42),'janitor elev 3':(0.72,0.43,0.88,0.70),'janitor elev 1':(0.72,0.70,0.88,0.97)}
out={}
for name,(x0,y0,x1,y1) in regions.items():
    c=collections.Counter()
    for w in pg.get_text('words'):
        if re.fullmatch(r'TA-0?\d+',w[4]) and x0<=w[0]/W<=x1 and y0<=w[1]/H<=y1:
            c['TA-'+str(int(w[4].split('-')[1]))]+=1
    out[name]=dict(sorted(c.items(),key=lambda t:int(t[0][3:])))
    print(name,out[name])
# men/women split on plan by x of room label
for w in pg.get_text('words'):
    if w[4] in ("MEN'S","WOMEN'S"): print(w[4], round(w[0]/W,3), round(w[1]/H,3))
pl=[(w[4],round(w[0]/W,3)) for w in pg.get_text('words') if re.fullmatch(r'TA-0?\d+',w[4]) and 0.03<=w[0]/W<=0.38 and 0.43<=w[1]/H<=0.70]
print(sorted(pl,key=lambda t:t[1]))
json.dump(out,open('tagcount.json','w'),indent=1)
