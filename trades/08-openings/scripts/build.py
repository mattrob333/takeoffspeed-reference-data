import json, csv
from fractions import Fraction as F
OUT='/home/user/takeoffspeed-reference-data/trades/08-openings/'
L={l['lineNo']:l for l in json.load(open('/home/user/takeoffspeed-reference-data/reference/estimate/lines.json'))}

# ---- door schedule A-600 (mark, room, type, W in, H in, door mat, frame mat, HW set, comment)
DS=[('100','WEATHER VESTIBULE','D',72,96,'GLASS','ALUM','1','CARD READER AND POWER ASSIST BUTTON'),
    ('101','ENTRY','D',72,96,'GLASS','ALUM','4','AUTO OPERATOR BUTTON'),
    ('105','MEETING ROOM','F',40,84,'GLASS','ALUM','14','32.34" CLEAR OPENING. GC PURCHASE AND COORDINATE WITH FIFTHTHIRDSUPPORT@DIRTT.COM'),
    ('106','ELEC./I.T.','B',36,84,'SCW','HM','7','CARD READER'),
    ('110','EMPLOYEE LOUNGE','E',36,96,'GLASS','ALUM','3','CARD READER'),
    ('111','WORK ROOM','C',36,84,'SCW','HM','6','CARD READER, KNOCK DOWN FRAME'),
    ('112','WOMENS','B',36,84,'SCW','HM','11','1" UNDERCUT'),
    ('113','MENS','B',36,84,'SCW','HM','11','1" UNDERCUT'),
    ('114','PHONE ROOM','B',36,84,'SCW','HM','10',''),
    ('115','JANITOR','B',36,84,'SCW','HM','9','CARD READER, 1" UNDERCUT')]
# 'xxx  H  3'-0" x 1'-0 5/8"' row is an unfilled template row: not a door.
EXTERIOR={'100','110'}   # in the envelope; 101 is the inner vestibule door
def doors(pred): return [d[0] for d in DS if pred(d)]
cr=lambda d:'CARD READER' in d[8]
door_groups={
 190:('F',doors(lambda d:d[2]=='F')),
 191:('B no card reader',doors(lambda d:d[2]=='B' and not cr(d))),
 192:('B card reader',doors(lambda d:d[2]=='B' and cr(d))),
 193:('C (card reader, KD frame)',doors(lambda d:d[2]=='C')),
 194:('D pair interior (auto operator)',doors(lambda d:d[2]=='D' and d[0] not in EXTERIOR)),
 195:('D pair exterior (card reader + power assist)',doors(lambda d:d[2]=='D' and d[0] in EXTERIOR)),
 196:('E exterior',doors(lambda d:d[2]=='E')),
}
hw_lines={198:'1',199:'3',200:'4',201:'6',202:'7',203:'9',204:'10',205:'11',206:'14'}
legend21={190:1,191:3,192:2,193:1,194:1,195:1,196:1,198:1,199:1,200:1,201:1,202:1,203:1,204:1,205:2,206:1}
legend_name21={190:"3'4\"Wx7'H TYPE F ... (yellow)",191:"3'Wx7'H TYPE B ... (blue, 3.0 EA)",192:"3'Wx7'H TYPE B ... (magenta, 2.0 EA)",
 193:"3'Wx7'H TYPE C ... (magenta)",194:"(2) 3'Wx8'H ... AUTO OPERATION BUTTON (periwinkle)",195:"EXT (2) 3'Wx8'H ... (salmon)",196:"EXT 3'Wx8'H TYPE E ... (bright green)"}

# ---- windows A-610 (overall W x H inches), tags counted on A-120 dimensional plan
WIN={'A':(155.5,144),'B':(119,144),'C':(88,144),'D':(96,112),'E':(72,88),'F':(72,120),'G':(160,112),'H':(168,112),'J':(92.25,144),'K':(91.625,120)}
TAGS_A120={'A':1,'B':1,'C':1,'D':1,'E':2,'F':1,'G':1,'H':1,'J':1,'K':1}
win_lines={208:'A',209:'C',210:'D',211:'E',212:'G',213:'H'}
legend22={208:1,209:1,210:1,211:2,212:1,213:1}
# frames that contain a door -> storefront SF net of the door opening(s)
SF_FRAMES={'B':[(72,96)],'F':[(36,96)],'J':[(72,96)],'K':[(40,84)]}
def sf_net(tag):
    w,h=WIN[tag]; return (F(w)*F(h)-sum(F(a)*F(b) for a,b in SF_FRAMES[tag]))/144
sf_lines={214:(['B','F'],107.3,'ANODIZED ALUMINUM EXTERIOR STOREFRONT SYSTEM 107.3 SQ FT (cyan, windows B and F)'),
          215:(['K'],53.2,'INTERIOR STOREFRONT 53.2 SQ FT (bright green, window K, DIRTT)'),
          216:(['J'],44.6,'ANODIZED ALUMINUM INTERIOR STOREFRONT SYSTEM BOD YKK YES45 FS 44.6 SQ FT (dusty rose, window J)')}

def short(n):
    d=L[n]['description'].split('\n')[0]
    return d[:110]
rows=[];fx=[]
def pct(r,e): return round((r-e)/e*100,2)
def add(n,source,vals,formula,rq,cls,notes,fixture=None,tol=0.0):
    e=L[n]['quantity']; u=L[n]['unit']
    rows.append([n,short(n),u,e,source,vals,formula,round(float(rq),3),pct(float(rq),e),cls,notes.strip()])
    if fixture is not None:
        fx.append({'name':f'L{n} {short(n).strip()}','formula':fixture[0],'engineAssembly':fixture[2],'inputs':fixture[1],
                   'expected':{'quantity':round(float(rq),3),'unit':u},'tolerancePct':tol,'estimatorQty':e,'estimatorUnit':u,
                   'estimatorDeltaPct':pct(float(rq),e),'classification':cls,'source':f'line {n} / {source}'})

for n,(label,marks) in door_groups.items():
    d=[x for x in DS if x[0]==marks[0]][0]
    leaves='pair' if d[2]=='D' else 'single'
    leafW=d[3]//2 if leaves=='pair' else d[3]
    vals=f"A-600 door schedule marks {', '.join(marks)} (type {d[2]}, {d[3]}\" x {d[4]}\" {'pair' if leaves=='pair' else 'single'}, {d[5]}/{d[6]}, HW {', '.join(sorted({x[7] for x in DS if x[0] in marks}))}); markup p21 legend {legend21[n]}.0 EA {legend_name21[n]}"
    notes={190:'DIRTT thin-profile sliding door inside window K; GC purchase via DIRTT (schedule comment). Spec 08 4113 2.4.B: 1-11/16" sliding glass door, trackless.',
           191:'112 WOMENS, 113 MENS (HW11, 1" undercut) and 114 PHONE ROOM (HW10). Undercut is not a split; card reader is.',
           192:'106 ELEC./I.T. (HW7) and 115 JANITOR (HW9), both CARD READER. Legend lists TYPE B twice (3.0 blue + 2.0 magenta) = 5 Type B in schedule.',
           193:'111 WORK ROOM, comment CARD READER, KNOCK DOWN FRAME (General note 3: HM frames fully welded unless noted).',
           194:'101 ENTRY is the inner vestibule pair inside storefront frame J: estimator files it under INTERIOR DOOR. Type D = pair; schedule width 6\'-0" is the pair, leaf 3\'-0".',
           195:'100 WEATHER VESTIBULE pair in exterior storefront frame B (HW1: card reader, power assist).',
           196:'110 EMPLOYEE LOUNGE single in exterior storefront frame F (HW3).'}[n]
    add(n,'A-600 DOOR SCHEDULE; markup p21',vals,'count(door-schedule marks of this type, size, materials, location and card-reader prep)',len(marks),'counted',notes,
        ('count of door schedule marks',{'marks':{'value':marks,'unit':'door marks'},'location':'exterior' if marks[0] in EXTERIOR else 'interior','leaves':leaves,
          'size':{'value':[leafW,d[4]],'unit':'in (one leaf W x H)'},'doorType':d[2],'doorMaterial':d[5],'frameMaterial':d[6]},'doors-hardware.opening'))

hwnotes={'1':'Set 1.0 doors: 100. 2 continuous hinges, 2 electric CVR exit devices, auto opener, ADA switches, threshold. Reader, seals by others.',
 '3':'Set 3.0 doors: 110.','4':'Set 4.0 doors: 101. Set 5.0 (1900 Narrow) also lists 101 but the door schedule assigns 101 HW 4: set 5 not carried.',
 '6':'Set 6.0 doors: 111.','7':'Set 7.0 doors: 106.','9':'Set 9.0 doors: 115.','10':'Set 10.0 doors: 114.','11':'Set 11.0 doors: 112 (Womens), 113 (Mens).',
 '14':'Set 14.0 doors: 105 (DIRTT concealed overhead slider + back-to-back pull by DIRTT).'}
for n,s in hw_lines.items():
    marks=[d[0] for d in DS if d[7]==s]
    add(n,'A-600 HRDW SET NO. column; A-601 hardware sets; markup p21',f"door schedule marks with HW set {s}: {', '.join(marks)}; markup p21 legend HARDWARE {s} = {legend21[n]}.0 EA",
        'count(door-schedule marks whose HRDW SET NO. = n)',len(marks),'counted',hwnotes[s]+' Estimate dwg ref "A0.0" does not exist; hardware is on A-601.',
        ('hardware set count = openings assigned the set',{'setNo':s,'marks':{'value':marks,'unit':'door marks'},'leaves':'pair' if any(d[2]=='D' for d in DS if d[0] in marks) else 'single'},'doors-hardware.hardware-set'))

# access hatch
add(197,'A-140 roof plan; markup p7 legend','markup p7 legend 30"x36" ROOF ACCESS HATCH - 3/A450 = 1.0 EA (cyan dot); spec 07 7200 2.4.B single-leaf lid 30 by 36 inches','count(hatch symbols on roof plan)',1,'counted',
    'Spec 07 7200 (p.200): Bilco S-20 basis, 14 ga stainless, curb 12" min, ladder-assist post. The estimate description (11 ga thermally broken cover, 18 ga liner, 3" polyiso, SS 316 pintle hinge, spring lift) reads like a product data sheet, not the spec.',
    ('count',{'kind':'roof hatch','count':{'value':1,'unit':'EA'},'description':'30"x36" ROOF ACCESS HATCH'},'roofing.counted'))

# VAT frame
W_,H_,fw=F(17,2),F(51,4),F(1)
inner=2*(W_+H_)/12; cl=2*(W_+fw+H_+fw)/12; outer=2*(W_+2*fw+H_+2*fw)/12
add(207,'A-701 det.6 VAT ACCESS ELEVATION (3"=1\'-0") + note; A-110 keynote P3',f'opening 8 1/2" W x 1\'-0 3/4" H, frame face 1" each side; inside perimeter {float(inner):.3f} LF, centerline {float(cl):.3f} LF, outside {float(outer):.3f} LF; no markup trace on det. 6; the p24 row Linear 15.3 FT is the top and back of millwork section 5, not the frame',
    'LF = 2 x ((W + fw) + (H + fw)) / 12 (frame centerline, one face)',cl,'derived',
    'Closest convention is the frame centerline (+1.44%); inside opening is -7.3%, outside +10.2%. 3.82 has no exact source. The p24 row Linear 15.3 FT was checked: it is the top and back of millwork section 5 traced at the page scale (7.4 ft true), not the VAT frame; 15.3/4 = 3.825 is coincidental. A-110 P3 says frame BOTH SIDES; A-701 says SINGLE SIDED VAT TUBE and the estimator took one face.',
    ('specialty frame LF = 2((W+fw)+(H+fw))/12 x faces',{'openings':{'value':[[8.5,12.75]],'unit':'in (W x H)'},'faceWidth':{'value':1,'unit':'in'},'faces':{'value':1,'unit':'faces'}},'doors-hardware.specialty-frame'),tol=2.0)

for n,t in win_lines.items():
    w,h=WIN[t]
    add(n,'A-610 window elevations; window tags on A-120; markup p22 legend',f'A-610 WINDOW {t} {w}" x {h}" ({float(F(w)*F(h)/144):.2f} SF each); A-120 tag count {TAGS_A120[t]}; markup p22 legend {legend22[n]}.0 EA',
        'count(window tags of this type on the dimensional plan) for frames with no door',TAGS_A120[t],'counted',
        {'A':'Tag A appears only on A-120 (entry, 12\'-11 1/2" bay); A-110 has no A tag.','E':'Two E tags: west wall (A-200) and east wall (A-201).'}.get(t,'')+' YKK YES45 TU 2"x4-1/2", 1" Solarban 90 IGU (A-610 notes).',
        ('window count by tag',{'size':{'value':[w,h],'unit':'in'},'instances':{'value':TAGS_A120[t],'unit':'EA'},'exterior':True,'frameMaterial':'ALUMINUM'},'windows-storefront.window'))

for n,(tags,leg,legname) in sf_lines.items():
    parts=[]; tot=F(0)
    for t in tags:
        w,h=WIN[t]; s=sf_net(t); tot+=s
        parts.append(f"{t}: {w}\"x{h}\" = {float(F(w)*F(h)/144):.3f} SF - door(s) {' + '.join(f'{a}x{b}' for a,b in SF_FRAMES[t])} = {float(s):.3f} SF")
    add(n,'A-610 window elevations; markup p22 legend','; '.join(parts)+f'; legend {legname}',
        'SF = sum over frames with doors (W x H - sum door openings W x H) / 144',tot,'measured',
        {214:'Shaded area = whole frame less the door bay below the transom bar. Estimator +0.28% (PlanSwift polygon).',
         215:'Window K, DIRTT Inspire (spec 08 4113 2.2.A.3); door 105 (3\'-4" x 7\'-0") excluded. Estimate 53.22 is the unrounded legend 53.2.',
         216:'Window J around door 101 (6\'-0" x 8\'-0"); 1/4" tempered, YKK YES45 FS 1-3/4"x4-1/2". Estimate 44.56 = unrounded legend 44.6.'}[n],
        ('storefront SF net of doors',{'frames':[{'tag':t,'size':{'value':list(WIN[t]),'unit':'in'},'doors':{'value':[list(x) for x in SF_FRAMES[t]],'unit':'in'},'instances':{'value':1,'unit':'EA'}} for t in tags],
          'system':'exterior-storefront' if n==214 else ('demountable' if n==215 else 'interior-storefront')},'windows-storefront.storefront'),tol=1.0)

rows.sort(key=lambda r:r[0])
with open(OUT+'reconciliation.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow('lineNo,description,unit,estimatorQty,source,sourceValues,formula,recomputedQty,deltaPct,classification,notes'.split(','))
    w.writerows(rows)
fx.sort(key=lambda x:int(x['name'].split()[0][1:]))
json.dump(fx,open(OUT+'fixtures.json','w'),indent=1)
print(len(rows),len(fx))
for r in rows: print(r[0],r[2],r[3],r[7],r[8],r[9])
print('within1',sum(abs(r[8])<=1 for r in rows),'within5',sum(abs(r[8])<=5 for r in rows))
print('B',float(sf_net('B')),'F',float(sf_net('F')),'J',float(sf_net('J')),'K',float(sf_net('K')))
print('window SF', {t:round(WIN[t][0]*WIN[t][1]/144,2) for t in WIN})
