import json, csv, os
REF='/home/user/takeoffspeed-reference-data'
OUT=REF+'/trades/10-specialties'
L={l['lineNo']:l for l in json.load(open(REF+'/reference/estimate/lines.json'))}
leg={(p['page'],it['name']):it for p in json.load(open(REF+'/reference/markups/legends.json')) for it in p['items']}
tags=json.load(open('/home/user/work/10-specialties/tagcount.json'))['plan 6/A-410']
def lg(page,name): return leg[(page,name)]['quantity']
# measured geometry (vector reads, inches; 1/2"=1'-0" -> 3 pt per real inch)
bar_c2c={'side_horizontal':44.02-2.0,'rear_horizontal':38.05-2.0,'vertical':20.02-2.0}
mirror=(24.02,36.04)
pnl_raw=[(41.04-9.01,108.0),(111.61-95.59,108.0)]
pnl_faces=[(round(w*8)/8,h) for w,h in pnl_raw]  # CAD vector read rounded to 1/8"  # A-706 elev 6, widths from vector x-positions, height = 9'-0" dimension
pnl_sf=sum(w*h for w,h in pnl_faces)/144
rows=[]; fx=[]
def add(n,short,source,vals,formula,recomp,cls,notes,fixture=None):
    l=L[n]; e=l['quantity']
    d=round((recomp-e)/e*100,2) if e else None
    rows.append(dict(lineNo=n,description=short,unit=l['unit'],estimatorQty=e,source=source,sourceValues=vals,formula=formula,recomputedQty=round(recomp,3),deltaPct=d,classification=cls,notes=notes))
    if fixture:
        f=dict(name=f"L{n} {short}",formula=fixture['formula'],engineAssembly=fixture['assembly'],inputs=fixture['inputs'],
               expected={'quantity':round(recomp,3),'unit':l['unit']},tolerancePct=fixture.get('tol',0.0),
               estimatorQty=e,estimatorUnit=l['unit'],estimatorDeltaPct=d,classification=cls,source=f"line {n} / {source}")
        fx.append(f)
tpl={'TA-3':'TA3','TA-4':'TA4','TA-6':'TA6','TA-8':'TA8','TA-9':'TA9','TA-10':'TA10','TA-1':'TA1','TA-2':'TA2','TA-5':'TA5'}
def ta_fix(tag,men,women,extra=None,per=1):
    inp={'tag':tag,'count':{'value':[men,women] if tag!='TA-10' else [men],'unit':'EA','per':'room ('+('MEN 112; WOMEN 111' if tag!='TA-10' else 'JANITOR 115')+')'}}
    if per!=1: inp['barsPerTag']={'value':per,'unit':'EA/tag'}
    if extra: inp.update(extra)
    return {'formula':'EA = sum(plan tag count per room)'+(' x bars of this size per TA-3 set' if tag=='TA-3' else ''),'assembly':'specialties.toilet-accessory','inputs':inp}
# grab bars
n3=lg(16,'TA3')
add(322,'18" vertical grab bar TA-3, Bradley 1-1/4" SS','markup p16 (A-410) legend TA3 + elev. 7-10/A-410',
    f"legend TA3 = {n3} EA (1 blue dot per restroom: MEN 112, WOMEN 111); plan text TA-3 x {tags['TA-3']}; vertical bar on side wall elev. C = {bar_c2c['vertical']:.2f}\" c-c",
    'EA = TA-3 plan count x 1 vertical 18" bar per set',n3*1,'counted',
    'Size from elevation (vector length 20.02" over the 1" end radii = 18.0" c-c at 1/2"=1\'-0"). Schedule TA-03 gives no length; the estimator split the one tag into sizes.',
    ta_fix('TA-3',1,1,{'size':{'value':'18" VERTICAL','unit':'text'}}))
add(323,'42" horizontal grab bar TA-3, Bradley 1-1/4" SS','markup p16 (A-410) legend TA3 + elev. 8/A-410 (side wall)',
    f"legend TA3 = {n3} EA; side-wall horizontal bar = {bar_c2c['side_horizontal']:.2f}\" c-c",
    'EA = TA-3 plan count x 1 side-wall 42" bar per set',n3*1,'counted',
    'The rear-wall bar on elevation 9 (B) measures 36.05" c-c and is NOT carried by any line: 2 x 36" grab bars omitted (see app-gaps).',
    ta_fix('TA-3',1,1,{'size':{'value':'42" HORIZONTAL','unit':'text'}}))
for n,tag,short,cls,note,extra in [
 (324,'TA-4','Waste receptacle TA-4, Bobrick B-3644 recessed','counted','Schedule: "(FOR 4\" WALLS)" recessed; one per room at the lav wall (red dots).',{'mounting':{'value':'RECESSED','unit':'text'}}),
 (325,'TA-6','2\'x3\' mirror TA-6, Bobrick B-290 SS angle frame','counted',f'Size from elev. 9: frame {mirror[0]:.2f}" x {mirror[1]:.2f}" = 2\'-0" x 3\'-0" (schedule gives model only). Spec 102800 2.1.F: 6.0 mm clear mirror glass, ASTM C1503.',{'size':{'value':"2'x3'",'unit':'text'}}),
 (326,'TA-8','Sanitary napkin disposal TA-8, Bobrick B-270','counted','WOMEN 111 only (1 cyan dot); MEN 112 has none.',None),
 (327,'TA-9','Coat hook TA-9','counted','Schedule model "REFERENCE DOOR HW SCHEDULE": hardware set 11.0 (doors 112, 113) also lists "2 Coat Hook RM817" per door, carried in Div 08 line 205. Same hooks potentially carried twice (2 here vs 4 in HW set 11).',None),
 (328,'TA-10','Surface mop holder TA-10, Bobrick B-223x24 satin','counted','JANITOR 115 only. The tag also appears on janitor elevation 3; count the plan once.',None),
 (329,'TA-1','Toilet tissue dispenser TA-1','counted','Schedule: OWNER VENDOR PROVIDED, GC TO INSTALL, GC TO ORDER (OFCI).',{'furnishedBy':{'value':'OWNER VENDOR','unit':'text'},'installedBy':{'value':'GC','unit':'text'}}),
 (330,'TA-2','Paper towel dispenser TA-2','counted','Schedule: OWNER VENDOR PROVIDED, GC TO INSTALL (OFCI).',{'furnishedBy':{'value':'OWNER VENDOR','unit':'text'},'installedBy':{'value':'GC','unit':'text'}}),
 (331,'TA-5','Soap dispenser TA-5','counted','Schedule: OWNER VENDOR PROVIDED, GC TO INSTALL (OFCI).',{'furnishedBy':{'value':'OWNER VENDOR','unit':'text'},'installedBy':{'value':'GC','unit':'text'}}),
]:
    q=lg(16,tpl[tag]); 
    men_w={'TA-8':(0,1)}.get(tag,(1,1))
    add(n,short,f'markup p16 (A-410) legend {tpl[tag]}',f"legend {tpl[tag]} = {q} EA; A-410 plan 6 text layer {tag} x {tags[tag]}",
        'EA = sum of plan tag dots (enlarged restroom plan 6/A-410 only)',q,cls,note,
        ta_fix(tag,*men_w,extra) if tag!='TA-10' else ta_fix(tag,1,None,extra))
for n,name,short,note,sz in [
 (332,'6"x4" TACTILE SIGNAGE','6"x4" tactile (exit) signage','3 T.S. tags on G-001 (east exit door beside the K.B. knox box; inner and outer doors of the south entry vestibule). Size from 2/G-002 TACTILE EXIT SIGN 6" x 4".','6" x 4"'),
 (333,'6"x9" ADA MEN TOILET SIGNAGE','6"x9" ADA men toilet sign, 5/8" raised, Gr.2 braille','1 cyan dot at door 112. Size from G-002 GENERAL NOTES - SIGNAGE detail 6" x 9" (6" pictogram + 3" text/braille); lettering from notes 1-2 (5/8" x 1/32", Grade 2 braille).','6" x 9"'),
 (334,'6"x9" ADA WOMAN TOILET SIGNAGE','6"x9" ADA women toilet sign','1 brown dot at door 111. Same G-002 detail.','6" x 9"')]:
    q=lg(2,name)
    add(n,short,f'markup p2 (G-001) legend "{name}"',f"legend = {q} EA",'EA = sum of plan dots on life safety plan',q,'counted',note,
        {'formula':'EA = count','assembly':'specialties.signage','inputs':{'count':{'value':[q],'unit':'EA'},'size':{'value':sz,'unit':'in (W x H)'}}})
add(335,'Fire extinguisher cabinet (recessed, 10 lb 4A:80B:C)','G-001 life safety plan F.E.C. symbols (no legend row on markup p2); A-110 FEC tags',
    'G-001 plan F.E.C. x 2 (one in the corridor by restrooms 112/113, one at the entry / gathering area 102-103); A-110 FEC x 2; code table FIRE EXTINGUISHERS (906.1) PROVIDED 2',
    'EA = count of F.E.C. symbols on G-001 (= code table PROVIDED)',2,'counted',
    'Not marked on the markup: the estimator counted the symbols. Legend: RECESSED FIRE EXTINGUISHER CABINET 10LB UL RATED 4A:80B:C. Spec 104413: J.L. Panorama 1035C70 or Larsen\'s GSS2409R2-C, steel tub, SS flat trim, frameless acrylic door. Spec 104416 says 4-A:60-B:C 10 lb; legend says 4A:80B:C. No separate extinguisher line.',
    {'formula':'EA = count','assembly':'specialties.fire-extinguisher','inputs':{'mount':{'value':'recessed','unit':'choice'},'count':{'value':[1,1],'unit':'EA'},'extinguisherSize':{'value':'10 LB','unit':'text'},'rating':{'value':'4A:80B:C','unit':'text'}}})
add(336,'Booth screen panel system PNL-1, Big Apple Visual Group','markup p29 (A-706) legend "PNL-1 PANEL W/ HARDWOO BLOCKING FILLER BOTH SIDE"',
    f"legend 36 SQ FT (teal); elev. 6/A-706 PNL-1 faces {pnl_faces[0][0]:.2f}\" x {pnl_faces[0][1]:.0f}\" + {pnl_faces[1][0]:.2f}\" x {pnl_faces[1][1]:.0f}\" (9'-0\" panel height dimension)",
    'SF = sum(face W x H)/144 on the interior elevation (one face of the double-sided panel)',pnl_sf,'measured',
    'A-170 FINISHES SCHEDULE "PANEL SYSTEM / PNL-1 BOOTH SCREEN / BIG APPLE VISUAL GROUP / SIZE: SEE PLAN". Double-sided panel is carried once (face area), not x2.',
    {'formula':'SF = sum(W x H)/144','assembly':'specialties.panel-system','inputs':{'faces':{'value':[[32,108],[16,108]],'unit':'in (W x H)'}},'tol':0.5})
with open(OUT+'/reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
json.dump(fx,open(OUT+'/fixtures.json','w'),indent=1)
r1=sum(1 for r in rows if abs(r['deltaPct'])<=1); r5=sum(1 for r in rows if abs(r['deltaPct'])<=5)
print(len(rows),r1,r5,len(fx), 'pnl_sf',pnl_sf, bar_c2c)
