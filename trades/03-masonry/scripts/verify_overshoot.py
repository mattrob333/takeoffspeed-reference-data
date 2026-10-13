import pymupdf
pm=pymupdf.Pixmap('/home/user/work/03-masonry/v-p12-eastleft.png'); W,H=pm.width,pm.height
def P(x,y): return pm.pixel(x,y)[:3]
def purple(c): r,g,b=c; return r>140 and b>140 and g<130
def red(c): r,g,b=c; return r>140 and g<120 and b<120 and r-g>40
def green(c): r,g,b=c; return g>130 and r<140 and b<140 and g-r>30
def cyan(c): r,g,b=c; return g>180 and b>180 and r<120
cols=[x for x in range(W) if sum(purple(P(x,y)) for y in range(H))>20]
rows=[y for y in range(H) if sum(purple(P(x,y)) for x in range(W))>20]
print('purple x',cols[0],cols[-1],' y',rows[0],rows[-1])
for name,f in (('red',red),('green',green),('cyan',cyan)):
    xs=[x for x in range(W) if sum(f(P(x,y)) for y in range(H))>2]
    ys=[y for y in range(H) if sum(f(P(x,y)) for x in range(W))>20]
    print(name,'x0',xs[0] if xs else None,'y',ys[:1],ys[-1:])
# brick hatch: count horizontal dark mortar lines in a column well right (x=600), within purple rows
x=600
dk=[y for y in range(rows[0],rows[-1]+1) if sum(P(x,y))<250]
print('dark ys at x=600',dk)
# left edge of hatch: in row y=300, first x where pixel is dark (vertical edge) after purple start
y=300
print('row300 dark xs',[x for x in range(cols[0],W) if sum(P(x,y))<250][:5])
