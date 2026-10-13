import csv, json, io
D='/home/user/takeoffspeed-reference-data/trades/23-hvac/'
rows=list(csv.DictReader(open(D+'reconciliation.csv', newline='')))
fields=list(rows[0].keys())
R={r['lineNo']:r for r in rows}
LJ_ORIG='kept by the original reader merge (last occurrence of the name)'
LJ_REST='restored to legends.json on review, tagged "duplicate name restored"'
# legend row (1-based, of 55), colour, legends.json status
dup={
 '454':(15,'cyan',LJ_REST,'LSD (3-48")'),
 '456':(18,'olive',LJ_ORIG,'LSD (3-48")'),
 '459':(21,'teal',LJ_REST,'LSD (2-24")'),
 '460':(22,'salmon',LJ_ORIG,'LSD (2-24")'),
 '462':(26,'magenta',LJ_REST,'24"x24" SUPPLY AIR DIFFUSER'),
 '464':(28,'brown',LJ_REST+'; legends.json gives it colour "magenta", the image shows brown','24"x24" SUPPLY AIR DIFFUSER'),
 '465':(29,'medium green',LJ_REST+'; legends.json gives it colour "magenta", the image shows medium green','24"x24" SUPPLY AIR DIFFUSER'),
 '466':(31,'indigo',LJ_REST+'; legends.json gives it colour "magenta", the image shows indigo','24"x24" SUPPLY AIR DIFFUSER'),
 '467':(35,'bright green',LJ_ORIG,'24"x24" SUPPLY AIR DIFFUSER'),
 '469':(32,'purple',LJ_REST,'24"x24" RETURN AIR GRILLE'),
 '470':(33,'teal',LJ_REST,'24"x24" RETURN AIR GRILLE'),
 '472':(36,'yellow',LJ_ORIG,'24"x24" RETURN AIR GRILLE'),
}
cfm={'454':'185 CFM','456':'330 CFM','459':'60 CFM','460':'150 CFM','462':'80S','464':'60S','465':'160S','466':'370S','467':'240S','469':'220R 10""x10""','470':'50R 8""x8""','472':'895R 16""x16""'}
def legend_row(ln):
    n,c,_,name=dup[ln]
    q={'459':'2.0','460':'2.0','469':'2.0'}.get(ln,'1.0')
    return f'"{name}" {q} EA ({c}, legend row {n} of 55)'
notes={
 '454':'Two legend rows share the name LSD (3-48""); plan colour separates 185 (cyan, row 15) from 330 (olive, row 18). This row was dropped by the original legends.json merge, which kept the last occurrence; it is now '+LJ_REST+'.',
 '456':'Second of two LSD (3-48"") rows; the one the original legends.json merge kept (last occurrence). Colour on plan: olive = 330 CFM tag.',
 '459':'24"" long = schedule ""LD (X)"" 2\'-0"" slot diffuser. First of two LSD (2-24"") rows (teal = 60 CFM tags); dropped by the original legends.json merge, now '+LJ_REST+'.',
 '460':'Second of two LSD (2-24"") rows (salmon = 150 CFM tags); the one the original legends.json merge kept (last occurrence).',
 '462':'Neck from schedule S(CFM): 0-100 -> 6""ø. Face 24x24: the M-301 symbol is drawn 2\'-0"" square. Five legend rows share this name (one per CFM); the original legends.json merge kept only the last (bright green, 240S); this magenta row is now '+LJ_REST+'.',
 '464':'Neck 0-100 -> 6""ø; face 24x24 (symbol drawn 2\'-0"" square, so the 0-90 ""12X12"" band does not apply). Dropped by the original legends.json merge, now restored; legends.json labels the restored row ""magenta"" but the legend image shows brown.',
 '465':'Schedule 101-210 CFM -> 8""ø. Dropped by the original legends.json merge, now restored; legends.json labels the restored row ""magenta"" but the legend image shows medium green.',
 '466':'Schedule 331-480 -> 12""ø. Dropped by the original legends.json merge, now restored; legends.json labels the restored row ""magenta"" but the legend image shows indigo.',
 '467':'Schedule 211-330 -> 10""ø. Last of the five 24x24 supply rows; the one the original legends.json merge kept.',
 '469':'Dropped by the original legends.json merge (which kept only the yellow 895R row), now '+LJ_REST+'.',
 '470':'Teal dot sits on the 50R tag. Dropped by the original legends.json merge, now '+LJ_REST+'.',
 '472':'Last of the three un-suffixed RAG rows; the one the original legends.json merge kept. Yellow dot sits on 895R.',
}
for ln,(n,c,st,name) in dup.items():
    r=R[ln]
    q={'459':'2.0','460':'2.0','469':'2.0'}.get(ln,'1.0')
    tag=r['sourceValues'].split('; plan text tag',1)[1]
    r['sourceValues']=f'"{name}" {q} EA ({c}, legend row {n} of 55); plan text tag'+tag
    r['notes']=notes[ln].replace('""','"')
R['463']['notes']='Neck from S(CFM) 0-90/0-100 -> 6"ø. Face 12x12 from the drawn symbol: both 65S squares on M-301 are 1\'-0" (18 pt at 18 pt/ft); 60S and 80S, also <=90 CFM, are drawn 2\'-0" and carried as 24x24. The overlapping 0-90 ("12X12") and 0-100 bands cannot fix the face on their own.'
R['446']['notes']=R['446']['notes'].replace('Estimator rounded to nearest 100 lb (1200.28 -> 1200).','Rounded to a whole lb (1200.28 -> 1200); whether the shop rounds to 10 or 100 lb cannot be told from this job.')
r=R['452']
r['source']='markup legend p53 (M-301); purple PlanSwift trace on the p53 plan'
r['sourceValues']='"REFRIGERANT PIPING, SIZE NOT GIVEN" 30.9 FT; trace segments on p53 (66.1 px/ft at zoom 8): FCU riser leg 1.22 + upper pipe 10.52 + end cap 0.36 + lower pipe 9.89 + drop 0.89 + third leg 7.97 = 30.86 FT'
r['formula']='LF = legend LF = plan length of the whole purple trace (both drawn pipes + an extra leg); not the route counted once (11.75 FT)'
r['notes']='PlanSwift traced both drawn lines of the line set on M-301 (out along one, back along the other) plus a 7.97 FT leg along grey linework above FCU-1 that has no pipe drawn under it; the segments sum to 30.86 FT = the estimate. The route counted once (FCU riser leg + one pipe) is 11.75 FT, so 30.9 is 2.6x the route. Purpose of the extra leg is unresolved. No vertical rise added; the roof run on M-302 (HP-1 to penetration, dashed) was not measured. M-301 keynote 2: size per manufacturer. Spec 23 2300 2.4.A: suction insulated 1-1/2" AP Armaflex - no insulation line carried.'
out=io.StringIO()
w=csv.DictWriter(out, fieldnames=fields, lineterminator='\n'); w.writeheader(); w.writerows(rows)
open(D+'reconciliation.csv','w', newline='').write(out.getvalue())

F=json.load(open(D+'fixtures.json'))
for f in F:
    ln=f['source'].split(' ')[0]
    if ln in dup:
        n,c,st,name=dup[ln]
        ci=f['inputs']['count']
        q={'459':'2.0','460':'2.0','469':'2.0'}.get(ln,'1.0')
        ci['legendRow']=f'"{name}" {q} EA ({c}, legend row {n} of 55)'
        ci['legendsJson']=st
    if ln=='463':
        f['inputs']['count']['face']='12x12 from the drawn 1\'-0" symbol on M-301 (not from the CFM band)'
    if ln=='452':
        old=f['inputs'].pop('route_LF')
        f['formula']='measured LF = legend LF (whole purple trace: both drawn pipes + extra leg)'
        f['inputs']['trace_LF']=old
        f['inputs']['traceSegments_FT']={'FCU riser leg':1.22,'upper pipe':10.52,'end cap':0.36,'lower pipe':9.89,'drop':0.89,'third leg (no pipe drawn)':7.97}
        f['inputs']['routeOnce_LF']={'value':11.75,'unit':'LF','note':'FCU riser leg + one pipe; NOT what the estimator carried'}
json.dump(F, open(D+'fixtures.json','w'), indent=1, ensure_ascii=False)
open(D+'fixtures.json','a').write('\n')
print('ok', sum(f['inputs']['traceSegments_FT'][k] for f in F if 'trace_LF' in f['inputs'] for k in f['inputs']['traceSegments_FT']))
