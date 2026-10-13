import { QUANTITY_REGISTRY, expandMeasurements } from '/home/user/TakeoffSpeed/lib/quantities/index.ts';
type Inputs = Record<string, string | string[]>;
const rec = (assembly: string, tag: string, inputs: Inputs) => ({
  assembly, tag, confidence: 'high' as const,
  inputs: Object.entries(inputs).flatMap(([name, v]) => (Array.isArray(v) ? v : [v]).map(value => ({ name, value }))),
});
const iso = (tag: string, n: number, size: string, depth: string, extra: Inputs = {}) => rec('concrete.isolated-footing', tag, { count: String(n), size, depth, ...extra });
const records = [
  rec('concrete.slab-on-grade', 'SOG-4', { areas: '1917.6 SF', thickness: '4"', reinforcing: 'wwf', wwf: '6x6-W2.9xW2.9', vaporRetarder: '15 MIL VAPOR RETARDER', baseThickness: '4"', baseMaterial: '#57 STONE', baseType: 'open-graded' }),
  rec('concrete.joint', 'IJ', { runs: '39.2 FT', type: 'isolation', width: '1/2"' }),
  rec('concrete.joint', 'SCJ', { runs: '364.1 FT', type: 'saw-cut' }),
  rec('concrete.continuous-footing', 'WF20', { runs: '124.2 FT', width: `2'-0"`, depth: `1'-0"`, barCount: '2', barSize: '#6' }),
  iso('F30', 3, `3'-0" x 3'-0"`, `1'-0"`, { barSize: '#4', barsEachWay: '4' }),
  iso('F38', 3, `3'-8" x 3'-8"`, `1'-0"`, { barSize: '#4', barsEachWay: '5' }),
  iso('F50', 6, `5'-0" x 5'-0"`, `1'-2"`, { barSize: '#5', barsEachWay: '5' }),
  iso('F60', 1, `6'-0" x 6'-0"`, `1'-4"`, { barSize: '#5', barsEachWay: '7' }),
  iso('F70', 1, `7'-0" x 7'-0"`, `1'-4"`, { barSize: '#6', barsEachWay: '7' }),
  iso('F7040', 1, `4'-0" x 7'-0"`, `1'-4"`, { barSize: '#6', longBars: '5', shortBars: '7', mats: '2' }),
  iso('F10050', 1, `5'-0" x 10'-0"`, `1'-2"`, { barSize: '#6', longBars: '5', shortBars: '9', mats: '2' }),
  rec('concrete.stem-wall', 'SW8', { runs: '193.8 FT', height: `2'-0"`, thickness: '8"', verticalSize: '#4', verticalSpacing: '10', dowelSize: '#4', dowelSpacing: '18' }),
  rec('concrete.stem-wall', 'SW10', { runs: '8.4 FT', height: `2'-0"`, thickness: '10"', verticalSize: '#4', verticalSpacing: '10' }),
  rec('concrete.pad', 'CO', { count: '1', size: `18" x 18"`, thickness: '6"', purpose: 'CLEAN OUT' }),
];
for (const mode of ['net', 'order'] as const) {
  const r = expandMeasurements(QUANTITY_REGISTRY, records, { mode });
  console.log('=== mode', mode, 'errors', JSON.stringify(r.errors));
  for (const l of r.lines) if (!/^rebar|^wwf|^vapor|^base|^dowel/.test(l.key)) console.log(JSON.stringify({ key: l.key, item: l.item, net: l.net, unit: l.unit, order: l.orderQuantity, orderUnit: l.orderUnit }));
}
