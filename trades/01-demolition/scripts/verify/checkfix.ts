import { readFileSync } from 'node:fs';
import { QUANTITY_REGISTRY, expandMeasurements } from '/home/user/TakeoffSpeed/lib/quantities';
const F = JSON.parse(readFileSync('/home/user/takeoffspeed-reference-data/trades/01-demolition/fixtures.json', 'utf8'));
let ok = 0, bad = 0;
for (const f of F) {
  const rec = { assembly: f.assembly, tag: 'D1', pages: [64], inputs: Object.entries(f.engineInputs as Record<string,string>).map(([name, value]) => ({ name, value })) };
  const r = expandMeasurements(QUANTITY_REGISTRY, [rec]);
  if (r.errors.length) { console.log('ERR', f.name, r.errors); bad++; continue; }
  for (const e of f.expectedLines) {
    const l: any = r.lines.find((x: any) => x.key === e.key);
    const net = l ? Number(l.net) : NaN;
    const d = l ? Math.abs(net - e.quantity) / e.quantity * 100 : Infinity;
    const pass = !!l && l.unit === e.unit && d <= e.tolerancePct + 1e-9;
    pass ? ok++ : bad++;
    console.log(pass ? 'PASS' : 'FAIL', `line ${e.line}`, e.key, net, l?.unit, `${d.toFixed(4)}% <= ${e.tolerancePct}%`, '|', l?.item);
  }
}
console.log({ ok, bad });
