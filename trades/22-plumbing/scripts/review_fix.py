import csv, json, math
D='/home/user/takeoffspeed-reference-data/trades/22-plumbing/'
rows=list(csv.DictReader(open(D+'reconciliation.csv',newline='')))
fields=list(rows[0].keys())
R={r['lineNo']:r for r in rows}
CLIP=(' legends.json flags the P-402 (p59) and P-403 (p60) legend boxes as possibly clipped: every markup page'
      ' is a raster that ends 24 pt above the sheet bottom, and the box has no bottom border. The visible rows are'
      ' taken as complete because each coloured mark on the page (p59: FCO and NFWH; p60: the meter) has a visible'
      ' legend row and no Div 22 line is left without a source.')
R['404']['notes']=('Canopy-drain leaders: the 7 "3\\" CD" on P-303 feed 6 three-inch leaders (the two west CDs at grid C,'
    ' 4.86 GPM/37 SF and 4.68 GPM/36 SF, share one "DN THRU WALL" leader, keynote 2); P-302 has 7 "3\\" TO CD" and'
    ' 6 "3\\" DN", P-301 has 6 "3\\" ST UP" and 6 "3\\" ST B/G REFER TO CIVIL". Legend prints 1 decimal;'
    ' estimate keeps PlanSwift precision.')
R['410']['notes']=('"3\\"o V A/C" run (12.8 FT) joins the VTR. P-302 keynote 1 says it ties into a 3" vent through roof,'
    ' the P-302 plan callout says "4\\" VTR" and P-303 ("VTR W/ BIRDSCREEN") gives no size: document conflict, flag it.'
    ' Quantity unaffected.')
for n in ('429','436','444'):
    base=R[n]['notes'].split(' legends.json flags the P-402')[0].rstrip()
    R[n]['notes']=base+CLIP
r=R['440']
r['source']='P-101 fixture schedule DB row + P-501 detail 8 (condensate drain to rain leader)'
r['sourceValues']=('P-101 "DB DRAIN BOX SIOUX CHIEF MODEL #696-3F" 1 mark; P-501 detail 8 "CONDENSATE DRAIN TO RAIN LEADER'
    ' DETAIL" 1 drain box (secondary funnel, P-trap with trap insert, to rain leader)')
r['formula']=('EA = 1 per scheduled mark (P-101 DB row) = 1 per indoor condensate source piped indirect to a rain leader'
    ' (P-501 detail 8; FCU-1 is the only one); no plan tag')
r['notes']=('No "DB" tag on any plumbing plan. P-101 schedules DB once (#696-3F with #696-LC louvered cover, #696-CF'
    ' secondary drainage funnel, JR Smith trap seal insert; "pipe indirect in wall to drain box", 2" waste). P-501'
    ' detail 8 draws the drain box with secondary funnel and insulated P-trap ("provide w/ trap insert") discharging to'
    ' the rain leader. Estimate line 440 carries dwg ref "P101 - P501". The RTU condensate does not use it: M-302 routes'
    ' it to the primary roof drains and the P-303 purple runs (34.5 FT) end at the two 4" RD on the roof. The one indoor'
    ' condensate source is FCU-1 (M-101 mini-split, wall-mounted, Electrical/IT room), so 1 DB (inference, GPT-6 Astra'
    ' agrees, moderately high confidence). P-302 "DW" (1 EA) is the dishwasher (Div 11 line 340; 1-1/2" SAN to DW on'
    ' P-301), not the drain box. Exact location: coordinate with architect/GC.')
with open(D+'reconciliation.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)

F=json.load(open(D+'fixtures.json'))
for c in F:
    if c['expected']['unit']=='LF':
        n=len(c['inputs']); e=c['expected']['quantity']
        tlf=round(0.05*n,2)
        c['toleranceLF']=tlf
        c['tolerancePct']=max(0.5, math.ceil(round(tlf/e*100,6)*100)/100)
    if c['name'].startswith('22-plumbing line 440'):
        c['formula']=('1 EA per scheduled mark (P-101 DB) = 1 per indoor condensate source piped indirect to a rain leader'
                      ' (P-501 detail 8); no plan tag')
        c['inputs']={'scheduledMarks':c['inputs']['scheduledMarks'],
                     'condensateConnections_P-501-d8':{'value':1,'unit':'EA',
                        'detail':'P-501 detail 8 CONDENSATE DRAIN TO RAIN LEADER DETAIL (drain box, secondary funnel, trap insert, to rain leader)',
                        'basis':'one indoor condensate source: FCU-1 wall-mounted mini-split, M-101 (RTU condensate goes to the roof drains per M-302)'}}
        c['source']='line 440 / P-101 fixture schedule DB row; P-501 detail 8'
# keep key order: put toleranceLF after tolerancePct
out=[]
for c in F:
    d={}
    for k,v in c.items():
        if k=='toleranceLF': continue
        d[k]=v
        if k=='tolerancePct' and 'toleranceLF' in c: d['toleranceLF']=c['toleranceLF']
    out.append(d)
json.dump(out,open(D+'fixtures.json','w'),indent=1)
# checks
for c in out:
    s=sum(v['value'] for v in c['inputs'].values()) if c['expected']['unit']=='LF' else None
    if s is not None:
        e=c['expected']['quantity']
        assert abs(s-e)<=c['toleranceLF']+1e-9, c['name']
        assert abs(s-e)/e*100<=c['tolerancePct']+1e-9, c['name']
        if c['tolerancePct']!=0.5: print(c['name'], c['tolerancePct'], c['toleranceLF'], round(abs(s-e)/e*100,4))
print('fixtures',len(out))
rr=list(csv.DictReader(open(D+'reconciliation.csv')))
na=[r for r in rr if r['classification']!='allowance/judgment']
print('lines',len(rr),'within1',sum(abs(float(r['deltaPct']))<=1 for r in na),'within5',sum(abs(float(r['deltaPct']))<=5 for r in na))
import collections; print(collections.Counter(r['classification'] for r in rr))
