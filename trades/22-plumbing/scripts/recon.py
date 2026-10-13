import json, csv, math
R='/home/user/takeoffspeed-reference-data'
L={l['lineNo']:l for l in json.load(open(R+'/reference/estimate/lines.json'))}
T=[t for t in json.load(open(R+'/reference/estimate/trades.json')) if t['trade']=='22-plumbing'][0]['lines']
G={g['page']:g for g in json.load(open(R+'/reference/markups/legends.json'))}
def leg(page,name):
    rows=[i for i in G[page]['items'] if i['name']==name]
    assert len(rows)==1,(page,name,rows)
    return rows[0]['quantity'],rows[0]['unit']
SH={56:'P-301',57:'P-302',58:'P-303',59:'P-402',60:'P-403',61:'P-501'}
# lineNo -> (source rows [(page,name)], classification, formula, short desc, notes)
M={
403:([],'allowance/judgment','1 LS (area basis 2000 SF carried in description)','Allowance for fittings & valves (2000 SF)','No markup. Building is 1,900 GSF (G-001 / title block "1,900 SF"); estimator rounded the area basis up to 2,000 SF. Covers fittings, hangers, small valves, insulation and trap/stop trim not taken off as lines.'),
404:([(56,'3"DIA STORM PIPE'),(57,'3"DIA STORM PIPE'),(58,'3"DIA STORM PIPE')],'measured','LF = sum of legend LF for the size+system over P-301 + P-302 + P-303','3" storm pipe','Canopy-drain leaders: 7 x 3" CD on P-303 drop through wall to 3" ST B/G on P-301. Legend prints 1 decimal; estimate keeps PlanSwift precision.'),
405:([(56,'4"DIA STORM PIPE'),(57,'4"DIA STORM PIPE'),(58,'4"DIA STORM PIPE')],'measured','LF = sum of legend LF over P-301 + P-302 + P-303','4" storm pipe','Roof drain (2 RD) and overflow (2 OD) leaders; P-302 includes off-plan vertical segments drawn up from each "4\\" DN"/"UP TO RD/OD" point.'),
406:([(56,'1-1/2"DIA SANITARY PIPE')],'measured','LF = legend LF (P-301)','1-1/2" sanitary pipe','Short 1-1/2" SAN branch to DW (dishwasher) at SK-T, P-301.'),
407:([(56,'3"DIA SANITARY PIPE')],'measured','LF = legend LF (P-301)','3" sanitary pipe','Below-grade sanitary main/branches ("3\\"o SAN B/G"); keynote 3: underground sanitary no less than 3".'),
408:([(56,'4"DIA SANITARY PIPE')],'measured','LF = legend LF (P-301)','4" sanitary pipe','4" SAN B/G building drain to civil (I.E. -4\'-0").'),
409:([(57,'2"DIA VENT PIPE')],'measured','LF = legend LF (P-302)','2" vent pipe','Vent A/C, P-302 ("2\\"o V A/C").'),
410:([(57,'3"DIA VENT PIPE')],'measured','LF = legend LF (P-302)','3" vent pipe','"3\\"o V A/C" to 3" VTR (keynote 1).'),
411:([(57,'4"DIA VENT PIPE')],'measured','LF = legend LF (P-302)','4" vent pipe','Red run on P-302 to "4\\" VTR". P-303 shows "VTR W/ BIRDSCREEN".'),
412:([(56,'1-1/4"DIA CW'),(57,'1-1/4"DIA CW')],'measured','LF = P-301 B/G service stub + P-302 above-ceiling main','1-1/4" cold water pipe','P-301 "1-1/4\\" CW B/G" (2.0) + P-302 "1 1/4\\"o CW A/C" (62.5). Material not stated on the line; spec 22 1000 2.2: Type L hard copper above ground, Type K below.'),
413:([(57,'1/2"DIA CW PIPE TYPE K COPPER')],'measured','LF = legend LF (P-302)','1/2" CW Type K copper (trap primer)','P-302 keynote 4 "1/2\\" SOFT COPPER BELOW SLAB TO PRIME FLOOR DRAIN (TYPICAL)"; spec 22 1000 2.2.C soft Type K, no joints underground. Cyan diagonal runs to the 3 FL.'),
414:([(57,'1"DIA CW')],'measured','LF = legend LF (P-302)','1" cold water pipe','"1\\"o CW A/C".'),
415:([(57,'3/4"DIA CW'),(58,'3/4"DIA CW')],'measured','LF = P-302 + P-303 legend LF','3/4" cold water pipe','P-302 "3/4\\"o CW A/C" (39.8) + P-303 "3/4\\" CW DN" to RH-1 (4.7).'),
416:([(57,'1"DIA HW')],'measured','LF = legend LF (P-302)','1" hot water pipe','"1\\"o HW A/C"; includes the recirculation return (no separate HWR size on plan).'),
417:([(58,'1-1/2"DIA CONDENSATE DRAIN PIPE, DIA ASSUMED')],'measured','LF = legend LF (P-303)','1-1/2" condensate drain pipe (size assumed)','Purple runs from RTU-1/RTU-2 on P-303; size not given on drawings, 1-1/2" assumed from M-302 legend "1-1/2\\" RTU CONDENSATE DRAIN W/ P-TRAP" (line 480, Div 23).'),
418:([(58,'1"DIA GAS PIPE')],'measured','LF = legend LF (P-303)','1" gas pipe (roof)','"1\\" GAS UP" on P-303; roof-level gas, painted safety yellow (P-403 note).'),
419:([(56,'1"DIA NATURAL GAS PIPE')],'measured','LF = legend LF (P-301)','1" natural gas pipe (below grade / up wall)','"NG B/G REFER TO CIVIL" and "1\\" NG UP TO A/C" on P-301 (cyan).'),
420:([(58,'3/4"DIA GAS PIPE')],'measured','LF = legend LF (P-303)','3/4" gas pipe (roof)','"3/4\\" GAS" branches to RTU-1 and RTU-2 on P-303.'),
421:([(57,'CP')],'counted','EA = legend count of tag','CP circulation pump','P-101 circulation pump schedule CP TACO 006-ST4; 1 on P-302 (keynote 3) and P-402.'),
422:([(57,'EDF')],'counted','EA = legend count of tag','EDF water cooler hi-lo','P-101 fixture schedule EDF ELKAY EZSTL8C.'),
423:([(57,'EWH')],'counted','EA = legend count of tag','EWH electric water heater 10 gal','P-101 water heater schedule EWH LOCHINVAR LDJ-10-JE.'),
424:([(57,'LAV')],'counted','EA = legend count of tag','LAV lavatory + battery faucet','LAV + LAVATORY (BATTERY) FAUCET are one estimate line (faucet is a sub-row of the LAV schedule mark).'),
425:([(57,'MS')],'counted','EA = legend count of tag','MS mop sink + wall faucet','MS + WALL FAUCET sub-row merged into one line.'),
426:([(57,'SK-T')],'counted','EA = legend count of tag','SK-T lounge sink + faucet','SK-T + LOUNGE FAUCET merged.'),
427:([(57,'SK-U')],'counted','EA = legend count of tag','SK-U library sink + faucet','SK-U + LIBRARY FAUCET merged.'),
428:([(57,'WC')],'counted','EA = legend count of tag','WC water closet ADA','Seat and supply in the description, not separate lines.'),
429:([(59,'NON FREEZE GROUND HYDRANT')],'counted','EA = legend count (P-402 NFWH)','WH wall hydrant','Plan tag on P-402 is "NFWH"; legend row says "NON FREEZE GROUND HYDRANT" (NFGH is a different abbreviation on P-001). Estimate uses schedule mark WH (J.R. SMITH 5509-QT).'),
430:([(58,'RH-1')],'counted','EA = legend count (P-303 RH-1)','RH roof hydrant','Plan tag "RH-1" on P-303; schedule mark "RH".'),
431:([(57,'STANDARD FILTER SIMILAR TO "WHIRLPOOL L...')],'counted','EA = legend count (P-302 keynote 5)','Whole-building sediment filter','From P-302 keynote 5; legend name truncated by PlanSwift.'),
432:([(57,'CD')],'counted','EA = legend count of tag','CD canopy drain','7 "3\\" CD" callouts on P-303; counted on P-302 where the leaders drop.'),
433:([(56,'FL')],'counted','EA = legend count of tag','FL floor drain','3 "3\\" FL" on P-301; P-402 iso labels them "FD".'),
434:([(58,'OD')],'counted','EA = legend count of tag','OD overflow drain','2 "4\\" OD" on P-303.'),
435:([(58,'RD')],'counted','EA = legend count of tag','RD roof drain','2 "4\\" RD" on P-303.'),
436:([(59,'FCO')],'counted','EA = legend count (P-402 SAN/VENT riser)','FCO floor cleanout','1 FCO on P-301 plan and on the P-402 riser; counted once (on P-402). Exterior cleanouts are civil (line 729).'),
437:([(57,'HB')],'counted','EA = legend count of tag','HB hose bib','2 HB on P-302.'),
438:([(57,'DSN')],'counted','EA = legend count of tag','DSN downspout nozzle','2 "4\\" DSN" on P-301; counted on P-302.'),
439:([(57,'VB')],'counted','EA = legend count of tag','VB wall valve box','1 VB on P-302 (keynote 6, Quench/Keurig feed).'),
440:([(57,'DW')],'specified','EA = 1 per scheduled mark with no plan placement (P-101 DB row); only matching plan count is P-302 "DW" 1 EA','DB drain box','No "DB" tag on any plumbing plan. P-101 schedules DB once; the only Div 22 legend count without its own estimate line is P-302 "DW" (1 EA), which on the plan is the dishwasher drain point (the appliance itself is Div 11 line 340). Quantity 1 either way; source mapping unverified.'),
441:([(61,'ISOLATION & BALANCING VALVE')],'counted','EA = legend count (P-501 detail)','Isolation & balancing valve (HWR)','P-501 detail "HWR ISOLATION VALVE AND BALANCING VALVE"; P-101 pump note 2 balancing valve in recirc line. Counted as one assembly.'),
442:([(57,'SHUT-OFF VALVE')],'counted','EA = legend count (P-302)','Shut-off valve (water heater in/out)','P-302 keynote 3: shutoff valves on input and output of water heater = 2 per EWH.'),
443:([(58,'MANUAL SHUT-OFF VALVE')],'counted','EA = legend count (P-303)','Manual gas shut-off valve at RTU','P-303 keynote 3: manual shutoff at each RTU; 2 RTUs (M-302).'),
444:([(60,'NATURAL GAS METER BY GAS COMPANY')],'counted','EA = legend count (P-403)','Natural gas meter by gas company','P-403 "NATURAL GAS METER"; service by gas company.'),
}
assert sorted(M)==sorted(T), set(T)^set(M)
rows=[];fx=[]
for n in T:
    l=L[n]; src,cls,form,desc,notes=M[n]
    if src:
        vals=[(SH[p],nm,)+leg(p,nm) for p,nm in src]
        rq=round(sum(v[2] for v in vals),4)
        sv='; '.join(f'{s} "{nm}" {q} {u}' for s,nm,q,u in vals)
        source='markup legend '+' + '.join(f'p{p} ({SH[p]})' for p,_ in src)
        if n==440: source='P-101 fixture schedule DB row; cross-check markup p57 (P-302) "DW"'
    else:
        rq=1.0; sv='G-001 "1,900 GSF"; estimate text "ALLOWANCE: 2000 SF"'; source='judgment (no markup)'
    eq=l['quantity']
    d=round((rq-eq)/eq*100,3)
    rows.append(dict(lineNo=n,description=desc,unit=l['unit'],estimatorQty=eq,source=source,sourceValues=sv,formula=form,recomputedQty=rq,deltaPct=d,classification=cls,notes=notes))
    if n!=403:
        unit=l['unit']
        if src:
            inp={}
            for k,(s,nm,q,u) in enumerate(vals):
                key=f'{s}' if len(vals)>1 else 'legend'
                inp[(key+'_LF') if unit=='LF' else (key+'_count')]={'value':q,'unit':'LF' if unit=='LF' else 'EA','legendItem':nm,'markupPage':src[k][0]}
            tol = 0.5 if unit=='LF' else 0
            # tolerance: legend shows 1 decimal -> up to 0.05 LF per row
            if unit=='LF': tol=max(0.5, round(0.05*len(vals)/eq*100+0.01,2))
            fx.append({'name':f'22-plumbing line {n}: {desc}','formula':'pipe LF = Σ legend LF over sheets (net, no waste, no added risers)' if unit=='LF' else 'count = legend EA (same tag counted once across plan/iso)','inputs':inp,'expected':{'quantity':eq,'unit':unit},'tolerancePct':tol,'source':f'line {n} / '+', '.join(f'markup p{p} ({SH[p]})' for p,_ in src)})
with open(R+'/trades/22-plumbing/reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
json.dump(fx,open(R+'/trades/22-plumbing/fixtures.json','w'),indent=1)
within1=sum(1 for r in rows if abs(r['deltaPct'])<=1 and r['classification']!='allowance/judgment')
within5=sum(1 for r in rows if abs(r['deltaPct'])<=5 and r['classification']!='allowance/judgment')
print('lines',len(rows),'within1',within1,'within5',within5,'fixtures',len(fx))
for r in rows: print(r['lineNo'],r['unit'],r['estimatorQty'],r['recomputedQty'],r['deltaPct'],r['classification'])
