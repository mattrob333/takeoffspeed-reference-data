import { QUANTITY_REGISTRY, expandMeasurements, type MeasurementRecord } from '../../TakeoffSpeed/lib/quantities/index';
type Inp = Record<string, string | string[]>;
const rec = (assembly: string, tag: string, inputs: Inp): MeasurementRecord => ({ assembly, tag, inputs: Object.entries(inputs).flatMap(([name, v]) => (Array.isArray(v) ? v : [v]).map(value => ({ name, value }))) });
const coats = { primerCoats: '1', finishCoats: '2' };
const pt1: [string, string][] = [['62.6', `12'-0"`], ['15', `11'-0"`], ['39.7', `8'-6"`], ['4.9', `6'-6"`], ['51.8', `10'-0"`], ['117.1', `9'-0"`], ['48', `12'-6"`]];
const cases: [string, MeasurementRecord[]][] = [
  ['295 PT-1 walls (7 height groups + A-410 elevation area)', [
    ...pt1.map(([lf, h], k) => rec('painting.walls', `PT-1#${k}`, { paintTag: 'PT-1', ...coats, walls: lf, height: h, substrate: 'gypsum' })),
    rec('painting.walls', 'PT-1#A410', { paintTag: 'PT-1', ...coats, areas: '252.6', substrate: 'gypsum' })]],
  ['296 PT-4', [rec('painting.walls', 'PT-4a', { paintTag: 'PT-4', ...coats, walls: '5.3', height: `9'-0"` }), rec('painting.walls', 'PT-4b', { paintTag: 'PT-4', ...coats, walls: '10.6', height: `10'-0"` })]],
  ['297 PT-6', [rec('painting.walls', 'PT-6', { paintTag: 'PT-6', ...coats, areas: '37.2' })]],
  ['298 PT-7', [rec('painting.walls', 'PT-7', { paintTag: 'PT-7', ...coats, walls: '10.3', height: `10'-0"` })]],
  ['299 PT-8', [rec('painting.walls', 'PT-8', { paintTag: 'PT-8', ...coats, walls: '7.4', height: `10'-0"` })]],
  ['300 PT-3 ceiling + soffit', [rec('painting.ceilings', 'PT-3', { paintTag: 'PT-3', ...coats, surface: 'gypsum', areas: ['516.1', '286.2'] })]],
  ['301 PT-3 exposed', [rec('painting.ceilings', 'PT-3X', { paintTag: 'PT-3', ...coats, surface: 'exposed-structure', areas: '98.4' })]],
  ['302 PT-5 booth roof', [rec('painting.ceilings', 'PT-5', { paintTag: 'PT-5', ...coats, surface: 'other', areas: '76.2' })]],
  ['303 HM frames', [rec('painting.doors-frames', 'PT-2', { paintTag: 'PT-2', ...coats, frames: Array(6).fill(`3'-0" x 7'-0"`) })]],
  ['305 diffusers', [rec('painting.mep', 'DIFF', { kind: 'device', color: 'BLACK', device: 'CEILING DIFFUSER', count: '5' })]],
  ['306 gas 3/4', [rec('painting.mep', 'G34', { kind: 'pipe', color: 'SAFETY YELLOW', pipeSize: '3/4"', service: 'GAS', pipeLF: '44.2' })]],
  ['307 gas 1', [rec('painting.mep', 'G1', { kind: 'pipe', color: 'SAFETY YELLOW', pipeSize: '1"', service: 'GAS', pipeLF: '9.7' })]],
];
for (const [name, rs] of cases) {
  for (const mode of ['net', 'order'] as const) {
    const r = expandMeasurements(QUANTITY_REGISTRY, rs, { mode } as any);
    console.log(`== ${name} [${mode}]`, r.errors.length ? 'ERR ' + JSON.stringify(r.errors) : '', (r as any).warnings?.length ? 'WARN ' + JSON.stringify((r as any).warnings) : '');
    for (const l of r.lines) console.log('  ', l.key, '|', l.item.slice(0, 70), '|', l.unit, 'net', l.net, 'order', (l as any).orderQuantity, (l as any).orderUnit ?? '');
  }
}
