import { readFileSync } from 'node:fs';
import { QUANTITY_REGISTRY, expandMeasurements } from '/home/user/TakeoffSpeed/lib/quantities';
const F = JSON.parse(readFileSync('/home/user/takeoffspeed-reference-data/trades/01-demolition/fixtures.json', 'utf8'));
for (const f of F) {
  const rec = { assembly: f.assembly, tag: 'D1', pages: [64], inputs: Object.entries(f.engineInputs as Record<string,string>).map(([name, value]) => ({ name, value })) };
  const r = expandMeasurements(QUANTITY_REGISTRY, [rec]);
  console.log(JSON.stringify({ name: f.name, errors: r.errors, lines: r.lines.map((l: any) => ({ key: l.key, net: Number(l.net), unit: l.unit, item: l.item })) }));
}
