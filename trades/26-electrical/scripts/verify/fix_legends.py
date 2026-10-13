import json, sys
root = sys.argv[1]
path = root + '/reference/markups/legends.json'
d = json.load(open(path))
pg = {p['page']: p for p in d}
V = 'added on review: dropped by the reader-merge step (same normalised name); Claude render + GPT-6 Astra agree'

# Page 41: printed order is 1" 4.8 (magenta), (2) 2" 15.4 (cyan), 1" 15.4 (brown)
p41 = pg[41]
assert len(p41['items']) == 2
by = {(i['name'], i['quantity']): i for i in p41['items']}
p41['items'] = [
    {'name': '1"DIA CONDUIT', 'quantity': 4.8, 'unit': 'FT', 'color': 'magenta', 'verified': V},
    by[('(2) 2"DIA CONDUIT', 15.4)],
    by[('1"DIA CONDUIT', 15.4)],
]

# Page 44: restore the printed 39-row order
p44 = pg[44]
items = p44['items']
assert len(items) == 37
quad3 = items[0]; assert quad3['name'] == 'QUAD RECEPTACLE, 20A, 125V' and quad3['quantity'] == 3
trgfci1 = items[12]; assert trgfci1['name'].startswith('TEMPER RESISTANT GFCI') and trgfci1['quantity'] == 1
rest = items[1:12] + items[13:]
names = [i['name'] for i in rest]
new_quad = {'name': 'QUAD RECEPTACLE 20A, 125V', 'quantity': 1, 'unit': 'EA', 'color': 'magenta', 'verified': V}
nan_row = {'name': 'TEMPER RESISTANT GFCI DUPLEX RECEPTACLE, 20A, 125V', 'quantity': 0, 'unit': 'EA',
           'color': 'medium green', 'printed': 'NAN EA',
           'verified': V + '; prints NAN EA, 0 is a placeholder (unknown, not a measured zero)'}
out = [new_quad] + rest[:11] + [quad3, nan_row] + rest[11:]
# move the 1.0 TR GFCI row to its printed place, after the TR duplex engraved row
k = [i['name'] for i in out].index('TEMPER RESISTANT DUPLEX RECEPTACLE, 20A, 125V- PROVIDE FACTORY ENGRAVED...')
out.insert(k + 1, trgfci1)
assert len(out) == 39
p44['items'] = out

# mark the other NAN placeholder (p42) the same way
for it in pg[42]['items']:
    if it['name'] == 'SAFETY SWITCH, 30A, 3 POLE, FUSED@ 20A':
        assert it['quantity'] == 0
        it['printed'] = 'NAN EA'

open(path, 'w').write(json.dumps(d, indent=1, ensure_ascii=True))
for n in (41, 44):
    for i, it in enumerate(pg[n]['items'], 1):
        print(n, i, it['name'], it['quantity'], it['unit'], it['color'])
