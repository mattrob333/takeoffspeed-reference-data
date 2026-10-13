import { QUANTITY_REGISTRY, expandMeasurements } from '/home/user/TakeoffSpeed/lib/quantities/index.ts';
type In = Record<string, string | string[]>;
const rec = (assembly: string, tag: string, inputs: In) => ({
  assembly, tag, pages: [1],
  inputs: Object.entries(inputs).flatMap(([name, v]) => (Array.isArray(v) ? v : [v]).map(value => ({ name, value }))),
});
const F: [string, string, string, string][] = [
  ['F30', `3'-0" x 3'-0"`, `1'-0"`, '3'], ['F38', `3'-8" x 3'-8"`, `1'-0"`, '3'], ['F50', `5'-0" x 5'-0"`, `1'-2"`, '6'],
  ['F60', `6'-0" x 6'-0"`, `1'-4"`, '1'], ['F70', `7'-0" x 7'-0"`, `1'-4"`, '1'], ['F7040', `7'-0" x 4'-0"`, `1'-4"`, '1'], ['F10050', `10'-0" x 5'-0"`, `1'-2"`, '1'],
];
const bottom = (t: string) => { const m = /(\d+)'-(\d+)"/.exec(t)!; const inches = 24 + Number(m[1]) * 12 + Number(m[2]); return `${Math.floor(inches / 12)}'-${inches % 12}"`; };
function scenario(label: string, ws: string | null, wallWidth: string | null, spreadWs: string | null) {
  const recs = [
    rec('earthwork.continuous-footing', 'WF20', { mark: 'WF20', runs: '124.2', width: `2'-0"`, thickness: `1'-0"`, bottomDepth: `3'-0"`, ...(wallWidth ? { wallWidth } : {}), ...(ws ? { workingSpace: ws } : {}) }),
    ...F.map(([m, size, t, n]) => rec('earthwork.spread-footing', m, { mark: m, size, thickness: t, bottomDepth: bottom(t), count: n, ...(spreadWs ? { workingSpace: spreadWs } : {}) })),
  ];
  const r = expandMeasurements(QUANTITY_REGISTRY, recs, { mode: 'net' });
  const by: Record<string, number> = {};
  for (const l of r.lines) by[l.key] = (by[l.key] ?? 0) + Number(l.net);
  console.log(label, JSON.stringify(r.lines.map(l => [l.key, l.item, Number(l.net).toFixed(4), l.unit])));
  console.log('  ERR', JSON.stringify(r.errors), 'WARN', JSON.stringify(r.warnings).slice(0, 400));
}
scenario('default(1ft both, wall 8in)', null, '8"', null);
scenario('estimator(1ft wall, 6in spread)', `1'-0"`, '8"', '6"');
const g = expandMeasurements(QUANTITY_REGISTRY, [rec('earthwork.cut-fill', 'EW', {
  cut: ['1.78 CY', '61.2 CY', '15.69 CY', '27.56 CY', '58.96 CY', '47.33 CY', '25.2 CY', '238.52 CY', '158.17 CY'],
  fill: ['51.72 CY', '151.02 CY', '224.56 CY', '199 CY', '2.11 CY', '12.81 CY', '84.11 CY', '37.98 CY', '18.35 CY', '4.59 CY'],
  source: 'Earthwork Pro Summary' })], { mode: 'net' });
for (const l of g.lines) console.log('grading', l.key, l.item, Number(l.net).toFixed(4), l.unit, l.orderQuantity, l.orderUnit);
console.log('  WARN', JSON.stringify(g.warnings));
const g0 = expandMeasurements(QUANTITY_REGISTRY, [rec('earthwork.cut-fill', 'EW', { cut: '634.41 CY', fill: '786.25 CY' })], { mode: 'net', conventions: { 'earthwork.shrink-pct': '0' } });
for (const l of g0.lines) console.log('grading shrink0', l.key, Number(l.net).toFixed(4));
