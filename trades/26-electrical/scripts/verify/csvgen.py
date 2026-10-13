import json, csv, io, sys
root = sys.argv[1]
d = json.load(open(root + '/reference/markups/legends.json'))
buf = io.StringIO()
w = csv.writer(buf, lineterminator='\r\n')
w.writerow(['page', 'sheet', 'item', 'quantity', 'unit', 'verified'])
for p in d:
    for it in p['items']:
        w.writerow([p['page'], p['sheet'], it['name'], it['quantity'], it['unit'], it['verified']])
out = buf.getvalue()
if len(sys.argv) > 2 and sys.argv[2] == 'write':
    open(root + '/reference/markups/legends.csv', 'w', newline='').write(out)
else:
    cur = open(root + '/reference/markups/legends.csv', newline='').read()
    print('identical' if cur == out else 'differs', len(cur), len(out))
    if cur != out:
        a, b = cur.splitlines(), out.splitlines()
        for i, (x, y) in enumerate(zip(a, b)):
            if x != y: print(i, repr(x), repr(y)); break
