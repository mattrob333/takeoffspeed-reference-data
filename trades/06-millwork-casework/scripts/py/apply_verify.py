import json, re
P='/home/user/takeoffspeed-reference-data/trades/06-millwork-casework/fixtures.json'
F=json.load(open(P))
def find(n):
    for f in F:
        if re.match(r'L%d '%n, f['name']): return f
def d(est, q): return round((est-q)/q*100, 2)

# L102 PL-3: 6 1/4" band
f=find(102)
faces=[[115.75/12, 6.25/12],[35.5/12, 6.25/12]]
q=sum(a*b for a,b in faces)
f.update(formula='laminate_face_sf = W x H', inputs={'faces':{'value':[[round(a,4),round(b,4)] for a,b in faces],'unit':'ft x ft'}},
         expected={'quantity':round(q,3),'unit':'SF'}, estimatorDeltaPct=d(7.0,q), classification='derived',
         source='line 102 / A-700 back elev 3 band 9\'-7 3/4" (10\'-6 3/4" - 11") + elev 6 band 35 1/2" (11" + 24 1/2"), band height 6 1/4" (left string 1 1/4" SLD-1 edge / 6 1/4" PL-3 / 1 1/4"); markup p23 legend PL3 FINISH 6.6 SF')
f['notes']='The 7 1/2" string is the 1 1/4" quartz edge plus the 6 1/4" band. Legend 6.6 = printed area; estimate 7 = 6.6 rounded up.'
print('L102',q,f['estimatorDeltaPct'])

# L116 library PL-1: dimension rebuild of the front elevation face net of the cased opening
f=find(116)
faces=[[1.5/12, 8.5],[3.5, 1.5],[5.5, 8.5]]  # left stile, head over cased opening (1'-3" cubby + 2 x 1 1/2"), right of opening
q=sum(a*b for a,b in faces)
assert abs(q-(9.125*8.5-3.5*7.0))<1e-9
f.update(formula='laminate_face_sf = W x H', inputs={'faces':{'value':[[round(a,4),round(b,4)] for a,b in faces],'unit':'ft x ft'}},
         expected={'quantity':round(q,3),'unit':'SF'}, estimatorDeltaPct=d(96.0,q), classification='measured (legend unreliable)',
         source='line 116 / A-702 elev 2: 9\'-1 1/2" x 8\'-6" minus CASED OPENING 3\'-6" x 7\'-0" (faces: 1 1/2" stile x 8\'-6", 3\'-6" x 1\'-6" head, 5\'-6" x 8\'-6"); markup p25 legend PL-1 FINISH 95.6 SF')
f['notes']='Estimate does not reconcile: the p25 salmon polygon fills the cased opening (~19 SF), runs ~4 ft past the millwork over blank sheet/title block (~23 SF), misses the drawer fronts, and adds a plan polygon (~9 SF). tolerancePct stays 1% because it is the engine-vs-expected tolerance; estimatorDeltaPct records the miss.'
print('L116',q,f['estimatorDeltaPct'])

# L139 work-room splash: wall-abutting edges carrying cyan
f=find(139)
edges=[68.5/12, 13.75/12, 7.625/12, 10.25/12, 64/12]
q=sum(edges)
f.update(inputs={'backsplash':{'value':[round(x,4) for x in edges],'unit':'ft'}}, expected={'quantity':round(q,3),'unit':'LF'},
         estimatorDeltaPct=d(14.0,q), classification='derived',
         source='line 139 / A-707 plan 1 back edge 6\'-4 1/8" - 7 5/8" = 5\'-8 1/2", notch 1\'-1 3/4" + 7 5/8", stub end 10 1/4"; plan 2 back edge 5\'-4"; markup p30 legend 4"H PL2 BASE 13.6 FT (cyan)')
f['notes']='Back walls are the bottom edge of plan 1 and the top edge of plan 2. No cyan on the plan-1 left end or plan-2 right end. Cyan on the two front edges belongs to the same-colour (2) 1x4 blocking row.'
print('L139',q,f['estimatorDeltaPct'])

# L142 booth walls: 8'-0" on all four faces
f=find(142)
faces=[[8,9],[8,9],[8,9],[8,9],[0.75,9],[0.75,9],[10.0417,0.75]]
q=sum(a*b for a,b in faces)
f.update(inputs={'faces':{'value':faces,'unit':'ft x ft'}}, expected={'quantity':round(q,3),'unit':'SF'},
         estimatorDeltaPct=d(300.0,q), classification='measured',
         source='line 142 / A-706 plan 1 8\'-0" (outside face) and section 5 1\'-11 1/2" + 1/2" + 4\'-0" + 1/2" + 1\'-11 1/2" = 8\'-0" (inside face), 9\'-0" A.F.F.; jambs 9"; header 9" x 10\'-0 1/2" (9" + 8\'-6 1/2" + 9"); markup p29 legend 296.9 SF')
f['notes']='Estimate 300 = legend 296.9 rounded up. The legend is not a clean measurement: the section-5 polygon runs past the booth over the title block and two polygons sit on the NTS 3D view (det. 10). Inside faces to the PNL-1 pocket (7\'-8") give 303.03 SF.'
print('L142',q,f['estimatorDeltaPct'], 'alt 7-8', 2*8*9+2*(92/12)*9+13.5+10.0417*0.75)

# L109 new fixture
n109={"name":"L109 Base cab 2'D x 2'10\"H, (5) drawer","formula":"cabinet_lf = sum(modules)","engineAssembly":"millwork.cabinet-run",
      "inputs":{"modules":{"value":[0.875],"unit":"ft"}},"expected":{"quantity":0.875,"unit":"LF"},"tolerancePct":1.0,
      "estimatorQty":1.0,"estimatorUnit":"LF","estimatorDeltaPct":d(1.0,0.875),"classification":"allowance/judgment",
      "source":"line 109 / A-701 elev 2 bay 10 1/2\" (section 9); markup p24 legend \"9\" 0.9 FT (brown)",
      "notes":"Estimator carries a 1 LF minimum; no source prints 1'-0\"."}
idx=[i for i,f in enumerate(F) if f['name'].startswith('L108 ')][0]
assert find(109) is None
F.insert(idx+1, n109)
open(P,'w').write(json.dumps(F, indent=1))
print('fixtures', len(F))
