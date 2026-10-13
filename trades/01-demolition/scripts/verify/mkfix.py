import json, copy
P='/home/user/takeoffspeed-reference-data/trades/01-demolition/fixtures.json'
F=json.load(open(P))
by={f['name']:f for f in F}
def s(v):
    if isinstance(v,dict) and 'value' in v:
        u=v['unit']; x=v['value']
        x=int(x) if float(x).is_integer() else x
        if u=='EA': return str(x)
        if u=='FT': return f"{x}'"
        return f"{x} {u}"
    if isinstance(v,list): return '; '.join(s(e) for e in v)
    if isinstance(v,bool): return 'yes' if v else 'no'
    return v
ENGINE_INPUT_SKIP={'rounding'}
out=[]
for f in F:
    n=f['name']
    if n in ('KN11 brick stair steps removal','KN4 storm structures removal'): continue
    g=copy.deepcopy(f)
    if n=='KN11 concrete ramp removal':
        g['name']='KN11 concrete ramp removal + brick stair steps'
        g['formula']='sf = sum(area_i); ea = count(drawn step lines)'
        g['inputs']['stairSteps']={'value':7,'unit':'EA','basis':'7 drawn step lines from the top landing edge (y=953.4 pt) down to the walk edge (y=973.4 pt) on C-1.0'}
        g['source']='lines 7 and 8 / markup p64 (C-1.0)'
        g['expectedLines']=[{'line':7,'key':'remove:CONCRETE RAMP','quantity':442.4,'unit':'SF','tolerancePct':0.5,'estimatorQty':442.37},
                            {'line':8,'key':'remove:stair-steps','quantity':7,'unit':'EA','tolerancePct':0,'estimatorQty':7.0}]
    elif n=='KN4 storm sewer removal (assumed)':
        g['name']='KN4 storm sewer removal (assumed) + storm structures'
        g['formula']='lf = sum(run_i); ea = count(structures at the line ends)'
        g['inputs']['structures']={'value':2,'unit':'EA'}
        g['inputs']['structureType']='STORM STRUCTURE'
        g['source']='lines 14 and 15 / markup p64 (C-1.0)'
        g['expectedLines']=[{'line':14,'key':'utility:remove:15" HDPE STORM SEWER','quantity':107.1,'unit':'LF','tolerancePct':0.5,'estimatorQty':107.11},
                            {'line':15,'key':'structure:STORM STRUCTURE','quantity':2,'unit':'EA','tolerancePct':0,'estimatorQty':2.0}]
    g['engineInputs']={k:s(v) for k,v in g['inputs'].items() if k not in ENGINE_INPUT_SKIP}
    out.append(g)
json.dump(out,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
print(len(out)); print(json.dumps([ (g['assembly'],g['engineInputs']) for g in out],indent=0)[:3000])
