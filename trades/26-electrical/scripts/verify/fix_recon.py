import csv, io, sys
p = sys.argv[1] + '/trades/26-electrical/reconciliation.csv'
rows = list(csv.reader(open(p, newline='')))
h = rows[0]; N = h.index('notes'); L = h.index('lineNo')
new = {
 '506': 'Two legend rows, same name (magenta 4.8 = the two short stubs labelled "1"C. FOR AV" at the kiosk and building J-boxes; brown 15.4 = the kiosk J-box to building J-box run). Both rows are now in legends.json p41 (the 4.8 row was restored 2026-10-13). Estimator carried a round 20.0',
 '507': 'Three pages summed (p41 RDT plan, E-010 site plan secondary/data route, E-100 keynote 17). Route LF, not x2. The p41 15.4 has no visible cyan run on the markup and is the same length as the brown 1" 15.4: the (2) 2" bundle and the 1" were measured along the same drawn kiosk-to-building path, one legend row per bundle (same route, two rows)',
 '511': 'fixture tag A. The estimate tag column and the description prefix both read AE, but the body text and model are the E-600 schedule\'s A row (no "WITH EMERGENCY BATTERY BACKUP", model without -EL); quantity = legend A = 8. Line 512 is the real AE (EM backup, -EL) = legend AE = 6',
 '546': 'first legend row on page 44 (magenta), distinct from the 13th row "QUAD RECEPTACLE, 20A, 125V" 3 EA (line 536); restored to legends.json 2026-10-13',
}
seen = set()
for r in rows[1:]:
    if r[L] in new:
        r[N] = new[r[L]]; seen.add(r[L])
assert seen == set(new)
b = io.StringIO(); csv.writer(b, lineterminator='\r\n').writerows(rows)
open(p, 'w', newline='').write(b.getvalue())
print('ok', len(rows) - 1)
