import json, csv, re, sys, math
R = sys.argv[1]; T = R + '/trades/26-electrical/'
leg = json.load(open(R + '/reference/markups/legends.json'))
legrows = {}
for p in leg:
    for it in p['items']:
        legrows.setdefault((p['page'], it['name']), []).append(it['quantity'])
lines = {x['lineNo']: x for x in json.load(open(R + '/reference/estimate/lines.json'))}
fx = json.load(open(T + 'fixtures.json'))
rec = {int(r['lineNo']): r for r in csv.DictReader(open(T + 'reconciliation.csv'))}
bad = 0
fxlines = set()
for f in fx:
    ln = int(re.search(r'line (\d+)', f['name']).group(1)); fxlines.add(ln)
    vals = []
    for k, arr in f['inputs'].items():
        if not isinstance(arr, list): continue
        for i in arr:
            if 'page' not in i: continue
            q = legrows.get((i['page'], i['legendItem']))
            if q is None or not any(abs(v - i['value']) < 1e-9 for v in q):
                bad += 1; print('legend miss', ln, i['page'], i['legendItem'], i['value'], q)
            vals.append(i['value'])
    exp = f['expected']['quantity']
    if abs(exp - lines[ln]['quantity']) > 1e-9: bad += 1; print('expected != estimate', ln, exp, lines[ln]['quantity'])
    r = rec[ln]
    if r['recomputedQty'] and vals and f['inputs'].get('counts') or f['inputs'].get('routeLengths') or f['inputs'].get('runs'):
        s = round(sum(vals), 2)
        if r['recomputedQty'] and abs(s - float(r['recomputedQty'])) > 0.051: bad += 1; print('sum != recomputed', ln, s, r['recomputedQty'])
        tol = f['tolerancePct']
        if abs(s - exp) / exp * 100 > tol + 1e-9: bad += 1; print('outside tolerance', ln, s, exp, tol)
# reconciliation sources exist in legends
for ln, r in rec.items():
    if abs(float(r['estimatorQty']) - lines[ln]['quantity']) > 1e-9: bad += 1; print('rec estimatorQty', ln)
    for m in re.finditer(r"p(\d+) '((?:[^']|'(?! \+|$))*)'", r['source']):
        pg, nm = int(m.group(1)), m.group(2)
        if (pg, nm) not in legrows: bad += 1; print('rec source not in legends', ln, pg, nm)
print('fixtures', len(fx), 'rec rows', len(rec), 'lines without fixture', sorted(set(rec) - fxlines), 'problems', bad)
