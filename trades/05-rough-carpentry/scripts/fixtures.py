import json
F=lambda f,i=0: round(f+i/12,6)
fx=[]
def add(name,formula,inputs,q,u,tol,src,note=None):
    d=dict(name=name,formula=formula,inputs=inputs,expected=dict(quantity=q,unit=u),tolerancePct=tol,source=src)
    if note: d['note']=note
    fx.append(d)
add('booth wall 1/2" plywood (LF x height)','sheathing.wall: SF = sum(LF x height x faces)',{'runs':[{'lf':15.9,'unit':'FT','height':{'value':3.0,'unit':'FT'},'faces':1}]},47.7,'SF',0.5,'line 81 / markup p29 (A-706) WALL 706','height 3.0 ft is the estimator\'s and is not printed on any sheet; keep as a regression of the arithmetic only')
ext=[(89.7,F(12,9),1,'EXT 8" STUD WALL @ 12\'9"H'),(9.2,F(10,3),1,'EXT 6" STUD WALL @ 12\'3"H SHTNG 10\'3"H (sheathing height overrides wall height)'),(5.9,F(7,2),1,'PARAPET WALL @ 7\'2"H A310'),(41.5,F(15,9),1,'EXT 8" STUD WALL @ 15\'9"H'),(13.0,4.0,1,'EXT 8" STUD WALL @ 4\'H'),(8.7,F(15,9),1,'EXT 8" STUD WALL @ 15\'9"H NO GWB'),(8.4,F(18,8),2,'6" & 3-5/8" METAL STUD @ 18\'8"H, BS 1/2" SHTNG ONLY'),(46.0,F(1,7),1,'A-140 PARAPET WALL @ 1\'7"H'),(38.0,F(2,7),1,'A-140 PARAPET WALL @ 2\'7"H'),(96.6,F(4,7),1,'A-140 PARAPET WALL @ 4\'7"H')]
add('exterior wall 1/2" plywood sheathing','sheathing.wall: SF = sum(LF x sheathing height x faces), no opening deduction',{'runs':[{'lf':a,'unit':'FT','height':{'value':h,'unit':'FT'},'faces':f,'legend':t} for a,h,f,t in ext],'openings':[]},3057.0775,'SF',0.5,'line 82 / markups p4 (A-120) + p7 (A-140)','recomputes 3050.26 (-0.22%)')
add('canopy roof 5/8" plywood (RT2 area)','sheathing.area: SF = sum(areas) x slope factor (1.0, flat)',{'areas':[{'value':285.4,'unit':'SF','legend':'RT2 ROOFING'}],'pitch':{'value':0,'unit':'in/12'}},285.0,'SF',0.2,'line 84 / markup p7 (A-140)')
add('booth ceiling 3/4" plywood, two layers','sheathing.area: SF = area x layers',{'areas':[{'value':76.2,'unit':'SF','legend':'PT5 FINISH @ BOOTH ROOF'}],'layers':2},152.0,'SF',0.3,'line 86 / markup p29 (A-706)')
add('IT room FR plywood backboard','backing.area: SF = measured elevation area (8 ft tall panels)',{'areas':[{'value':215.3,'unit':'SF','legend':'3/4"THK. FIRE RATED PLYWOOD BACKBOARD'}],'thickness':'3/4"','treatment':'FRT'},215.33,'SF',0.1,'line 87 / markup p49 (E-702)')
blk=[(7,8.6,'A-701 (7) 1x4 FIRE RETARDANT TREATED BLOCKING'),(2,14.6,'A-702 (2) 1x4 WOOD BLOCKING FRAMING'),(4,9.8,'A-703 (4) 1x4 WOOD BLOCKING FRAMING'),(2,23.3,'A-707 (2) 1x4 WOOD BLOCKING FRAMING'),(2,15.7,'A-705 (2) 1x4 BLOCKING'),(5,1.6,'A-700 (5) 2x4 WOOD BLOCKING FRAMING'),(3,8.7,'A-705 (3) 2x4 BLOCKING')]
add('casework in-wall blocking, rows from the "(n)" prefix','blocking: LF = sum(rows x run LF)',{'runs':[{'lf':l,'unit':'FT','rows':n,'legend':t} for n,l,t in blk],'size':'1x4','treatment':'FRT'},240.66,'LF',0.1,'line 89 / markups p23-p32','estimator folded the two 2x4 rows into the 1x4 line; 1x4 rows alone = 206.6 LF')
add('high-low roof step wall 2x4 P.T. blocking','blocking: LF = run LF, rounded up to whole LF',{'runs':[{'lf':45.3,'unit':'FT','legend':'8/A450 LAP ROOF 2\', INCL WALL'}],'size':'2x4','treatment':'P.T.','roundUpTo':{'value':1,'unit':'LF'}},46.0,'LF',0.0,'line 91 / markup p7 (A-140), A-450 det. 8/10')
add('high-low roof step wall 2x6 P.T. blocking','blocking: LF = run LF, rounded up to whole LF',{'runs':[{'lf':45.3,'unit':'FT','legend':'8/A450 LAP ROOF 2\', INCL WALL'}],'size':'2x6','treatment':'P.T.','roundUpTo':{'value':1,'unit':'LF'}},46.0,'LF',0.0,'line 92 / markup p7 (A-140), A-450 det. 10')
add('wing-wall coping 2x16 P.T. blocking','blocking: LF = coping LF, rounded up to 5 LF',{'runs':[{'lf':13.9,'unit':'FT','legend':'COPING 3/A430'}],'size':'2x16','treatment':'P.T.','roundUpTo':{'value':5,'unit':'LF'}},15.0,'LF',0.0,'line 93 / markup p7 (A-140), A-430 det. 3')
add('roof coping 2x10 P.T. nailer','blocking: LF = coping LF',{'runs':[{'lf':148.1,'unit':'FT','legend':'COPING 6/A450'}],'size':'2x10','treatment':'P.T.'},148.0,'LF',0.1,'line 94 / markup p7 (A-140), A-450 det. 6')
add('high-parapet coping 2x14 P.T. nailer','blocking: LF = coping LF, rounded up to 5 LF',{'runs':[{'lf':38.5,'unit':'FT','legend':'COPING 9/A450'}],'size':'2x14','treatment':'P.T.','roundUpTo':{'value':5,'unit':'LF'}},40.0,'LF',0.0,'line 95 / markup p7 (A-140), A-450 det. 9')
add('high-parapet 1x6 blocking under brake metal','blocking: LF = coping LF, rounded up to 5 LF',{'runs':[{'lf':38.5,'unit':'FT','legend':'COPING 9/A450'}],'size':'1x6','treatment':'P.T.','roundUpTo':{'value':5,'unit':'LF'}},40.0,'LF',0.0,'line 96 / markup p7 (A-140), A-450 det. 9')
add('night depository opening 2x6 blocking','blocking: LF = traced opening perimeter',{'runs':[{'lf':8.8,'unit':'FT','legend':'2x6 BLOCKING'}],'size':'2x6'},8.78,'LF',0.3,'line 97 / markup p12 (A-201)')
add('transaction bar knee wall 1/2" plywood, both faces','backing.wall: SF = ceil5(LF x height x faces)',{'runs':[{'lf':4.0,'unit':'FT','height':{'value':3.75,'unit':'FT'},'faces':2,'legend':'1/2" PLYWOOD @ 3\'9"H'}],'roundUpTo':{'value':5,'unit':'SF'}},30.0,'SF',0.0,'line 145 / markup p23 (A-700)')
add('casework 3/4" plywood backing','backing: SF = ceil5(sum(n x LF x H) + sum(areas))',{'runs':[{'lf':3.7,'unit':'FT','height':{'value':F(1,4),'unit':'FT'},'rows':2,'legend':'A-700 (2) 3/4" PLYWOOD @ 1\'4"H'},{'lf':1.6,'unit':'FT','height':{'value':F(0,8),'unit':'FT'},'rows':1,'legend':'A-700 3/4" PLYWOOD @ 8"H'},{'lf':8.6,'unit':'FT','height':{'value':7.67,'unit':'FT'},'rows':1,'legend':'A-701 3/4" PLYWOOD @ 7.67H'}],'areas':[{'value':46.9,'unit':'SF','legend':'A-702 3/4" PLYWOOD'},{'value':8.0,'unit':'SF','legend':'A-703 3/4" PLYWOOD'}],'roundUpTo':{'value':5,'unit':'SF'}},135.0,'SF',0.0,'line 146 / markups p23, p24, p25, p27','raw 131.80 SF before the ceil-to-5 rule')
add('tech wall 5/8" plywood backing','backing.area: SF = ceil5(area)',{'areas':[{'value':37.2,'unit':'SF','legend':'5/8" PLYWOOD BACKING'}],'roundUpTo':{'value':5,'unit':'SF'}},40.0,'SF',0.0,'line 147 / markup p28 (A-704)')
json.dump(fx,open('/home/user/takeoffspeed-reference-data/trades/05-rough-carpentry/fixtures.json','w'),indent=1)
# self-check
import math
def ev(f):
    i=f['inputs']; s=0
    for r in i.get('runs',[]):
        s+=r['lf']*r.get('height',{'value':1})['value']*r.get('faces',1)*r.get('rows',1)
    for a in i.get('areas',[]): s+=a['value']
    s*=i.get('layers',1)
    if 'roundUpTo' in i: st=i['roundUpTo']['value']; s=math.ceil(round(s,6)/st)*st
    e=f['expected']['quantity']; return s,(s-e)/e*100
for f in fx: s,d=ev(f); print(f['source'][:8],round(s,4),round(d,3),'OK' if abs(d)<=f['tolerancePct']+1e-9 else 'FAIL')
print(len(fx))
