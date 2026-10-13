import csv, io, sys
p = sys.argv[1]
rows = list(csv.DictReader(open(p, newline='')))
fields = list(rows[0].keys())
SIZE = {
 '356': 'A-170 prints SS-01 26.25"D x 26.25"W x 20.25"-29"H; the estimate text reads 26.25"W X 26.25"W (estimator swapped D to W)',
 '359': 'A-170 prints ST-02 12"W x 18 7/8"D x 21"H; the estimate text reads 18"7/8"D (re-keying error)',
 '363': 'A-170 prints WS-01 OVAL TOP: 42"D x 9\'W OR 10\'W (VARIES) in feet; the estimate text reads 9"W OR 10"W (feet turned into inches)',
 '365': 'A-170 prints CH-09 18"W x 21"D x 35.4" x 17.5"-21.5"SH; the estimate text reads 17.25"-21.5"SH',
 '380': 'A-170 prints SS-02L 86.25" x 44.5"D x 29.5"H x 16.5\' SH (foot-mark typo); the estimate corrected it to 16.5"SH',
 '381': 'A-170 prints SS-02R 86.25" x 44.5"D x 29.5"H x 16.5\' SH (foot-mark typo); the estimate corrected it to 16.5"SH',
 '386': 'A-170 prints SS-07B 26.25"D x 52.75"W x 29"H x 18"SH; the estimate text reads 16.5" SH',
}
for r in rows:
    n = r['lineNo']
    if n == '357':
        r.update({
          'source': 'A-170 Furniture Schedule row SS-03A; not drawn on A-160 (the one SS-03 placement is the 3-seat SS-03B)',
          'sourceValues': 'schedule row present, plan placements 0 (A-160 sofa under the SS-03 bubble measures 95.5 in wide x 33.3 in deep = SS-03B 95.75 x 33.25; SS-03A is 66.5 in)',
          'formula': 'scheduled furniture tag not placed -> 1 EA (V.I.F.)',
          'recomputedQty': '1.0',
          'classification': 'specified',
          'notes': 'Estimator convention stated in section note: NOT FOUND ON PLANS ... ASSUMED 1 EA, PLEASE V.I.F. The p9 legend SS03 1.0 EA belongs to SS-03B (line 358), not to this row'})
    elif n == '358':
        r['sourceValues'] = 'SS03 = 1 EA; the drawn sofa is one 3-seat piece 95.5 in wide (A-160 vectors) = SS-03B 95.75 in'
        r['notes'] = 'OFCI per A-110 General Note K. Plan tag SS-03 carries no suffix; the reader assigns the placement to SS-03B by drawn width and seat count'
    elif n == '345':
        r['notes'] = ('1184.4/74.0 = 16.0054; exact if hidden LF = 74.025. 16 ft is not on any drawing. A-311 gives two storefront heads: '
                      '10\'-0" (section 1, WALL SECTION AT STOREFRONT: 2\'-8" + 5\'-5" + 1\'-11") and 12\'-0" (section 3, ENTRY VESTIBULE); ceilings at the runs are 10\'-12\'. '
                      'Ceiling-height drop gives 855.1 SF; spec 12 2413 2.4 B head-to-sill (2\'-8") gives 542.9 SF at a 10\'-0" head and 690.9 SF at 12\'-0". Description (75 LF) = ceil(74.025)')
    if n in SIZE:
        r['notes'] = r['notes'] + '. Quantity matches; SIZE text deviates from A-170: ' + SIZE[n] + '. Engine: copy the schedule string and flag the deviation, do not reproduce it'
b = io.StringIO(); w = csv.DictWriter(b, fieldnames=fields); w.writeheader(); w.writerows(rows)
open(p, 'w', newline='').write(b.getvalue())
import collections
print(len(rows), collections.Counter(r['classification'] for r in rows))
print(sum(1 for r in rows if abs(float(r['deltaPct']))<=1), sum(1 for r in rows if float(r['deltaPct'])==0))
