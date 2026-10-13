import { QUANTITY_REGISTRY, expandMeasurements, type MeasurementRecord } from '../../TakeoffSpeed/lib/quantities/index';
type Inp = Record<string, string | string[]>;
const rec = (assembly: string, tag: string, inputs: Inp): MeasurementRecord => ({ assembly, tag, inputs: Object.entries(inputs).flatMap(([name, v]) => (Array.isArray(v) ? v : [v]).map(value => ({ name, value }))) });
const r = expandMeasurements(QUANTITY_REGISTRY, [
  rec('wall-finishes.wallcovering', 'WC-PT7', { finishTag: 'WC @ PT-7', walls: '10.3', height: `10'-0"`, primerTag: 'PT-7', assumed: 'yes' }),
  rec('painting.walls', 'PT-7', { paintTag: 'PT-7', primerCoats: '1', finishCoats: '2', walls: '10.3', height: `10'-0"` }),
], { mode: 'net' } as any);
for (const l of r.lines) if (l.trade === 'painting') console.log(l.key, '|', l.item, '|', l.unit, l.net);
console.log('warnings', JSON.stringify((r as any).warnings));
