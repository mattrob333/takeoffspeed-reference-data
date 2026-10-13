import json, math
REF='/home/user/takeoffspeed-reference-data'
L={l['lineNo']:l for l in json.load(open(f'{REF}/reference/estimate/lines.json'))}
G=json.load(open(f'{REF}/reference/markups/legends.json'))
def rows(page):
    for p in G:
        if p['page']==page: return p['items']
def show(n):
    l=L[n]; print(n, {k:l[k] for k in l if k in ('description','unit','quantity','dwgRef')})
for n in (88,148,149,161,162,183,302,311,312): show(n)
print('--- p29'); [print(' ',i['name'],i['quantity'],i.get('unit')) for i in rows(29)]
print('--- p4');  [print(' ',i['name'],i['quantity'],i.get('unit')) for i in rows(4)]
print('--- p7');  [print(' ',i['name'],i['quantity'],i.get('unit')) for i in rows(7)]
# Issue 1
field=1864.3+285.4; laps=43.3*25/12+56.5*1+87.8*3.5; hl=45.3*2; edge4=138.5*4/12; edge30=138.5*2.5
print('field',field,'laps',laps,'hl',hl,'edge4',edge4,'edge30',edge30)
meas=field+laps+hl+edge4; print('measured total',meas,'residual',3042.774-meas,'pct',(meas-3042.774)/3042.774*100)
print('old',field+laps+hl+edge30)
print('crickets+curb fit',meas+262.1+39.9)
# Issue 2
A=28.4+34.2+36.7+49.9; D=3.7+46.0; low=7.7+18.3; ext=89.7+9.2+41.5+13.0
print('A',A,'D',D,'low',low,'ext',ext,'int',A+D+low)
r1=4*(A+D+low)+1*ext; r2=4*A+2*(D+low+ext)
print('4/1 rule',r1,(r1-1053.5)/1053.5*100,' detail rule',r2,(r2-1053.5)/1053.5*100)
# Issue 4
WIN={'A':(12+11.5/12,12,1),'B':(9+11/12,12,1),'C':(7+4/12,12,1),'D':(8,9+4/12,1),'E':(6,7+4/12,2),'F':(6,10,1),'G':(13+4/12,9+4/12,1),'H':(14,9+4/12,1),'J':(7+8.25/12,12,1),'K':(7+7.625/12,10,1)}
GP=sum(2*(w+h)*n for w,h,n in WIN.values()); ext_gl=GP-2*(WIN['J'][0]+WIN['J'][1])-2*(WIN['K'][0]+WIN['K'][1])
print('glazed',GP,'+910',910+GP,'ceil10',math.ceil((910+GP)/10)*10,'exterior glazed',ext_gl,'count units ext', sum(n for k,(w,h,n) in WIN.items() if k not in 'JK'))
print('ext glazed *0.5',ext_gl*0.5)
extdoors=2*(6+8)+2*(3+8); print('ext door perims',extdoors,'ext glazed+doors',ext_gl+extdoors,'x0.5',(ext_gl+extdoors)*0.5, 'jambs+head doors',(2*8+6)+(2*8+3),'->',(ext_gl+(2*8+6)+(2*8+3))*0.5)
# Issue 7 (156)
r=[(46.0,19/12),(38.0,31/12),(13.0,4),(96.6,55/12),(5.9,86/12),(89.7,12.75),(41.5,15.75),(8.7,15.75)]
s=sum(a*b for a,b in r); print('156',s,2652.875-s,(s-2652.875)/2652.875*100)
for i,(a,b) in enumerate(r):
    rest=s-a*b; print('  row',a,'would need',(2652.875-rest)/b)
print('2652.875*8',2652.875*8)
