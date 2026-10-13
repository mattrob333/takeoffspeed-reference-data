import { QUANTITY_REGISTRY, expandMeasurements, type MeasurementRecord } from '../../TakeoffSpeed/lib/quantities/index';
type Inp = Record<string, string | string[]>;
const rec = (assembly: string, tag: string, inputs: Inp): MeasurementRecord => ({ assembly, tag, inputs: Object.entries(inputs).flatMap(([name, v]) => (Array.isArray(v) ? v : [v]).map(value => ({ name, value }))) });
const cases: [string, MeasurementRecord[]][] = [
  // Naive per-tag band record: the only way the current schema expresses a band -> every tag gets the full band
  ['restroom band recorded as WT-1 (whole band, both rooms)', [rec('wall-finishes.wall-tile', 'WT-1', { finishTag: 'WT-1', walls: [`7.5083`, `7.675`, `4.0056`, `0.3333`, `7.5083`, `7.675`, `4.0056`, `0.3333`], height: `5'-6"`, tileSize: '3" x 12"' })]],
  ['WT-3 transaction bar', [rec('wall-finishes.wall-tile', 'WT-3', { finishTag: 'WT-3', walls: `10'-4 1/4"`, height: `3'-8 1/2"`, tileSize: '6" x 12"', backerBoard: '1/4" CEMENTITIOUS BACKER BOARD' })]],
  ['A-703 backsplash', [rec('wall-finishes.wall-tile', 'WT-1', { finishTag: 'WT-1', walls: `6'-9"`, height: `2'-8"`, tileSize: '3" x 12"' })]],
  ['A-705 backsplash', [rec('wall-finishes.wall-tile', 'WT-1', { finishTag: 'WT-1', walls: `7'-2"`, height: `1'-6 1/2"`, tileSize: '3" x 12"' })]],
  ['FRP-1', [rec('wall-finishes.frp', 'FRP-1', { finishTag: 'FRP-1', walls: [`2'-0"`, `2'-0"`], height: `4'-0"`, insideCorners: '1' })]],
  ['WC-1', [rec('wall-finishes.wallcovering', 'WC-1', { finishTag: 'WC-1', walls: `10.1`, height: `12'-0"` })]],
  ['WC over PT-7', [rec('wall-finishes.wallcovering', 'WC-PT7', { finishTag: 'WC @ PT-7', walls: `10.3`, height: `10'-0"`, primerTag: 'PT-7', assumed: 'yes' })]],
];
for (const [name, rs] of cases) {
  for (const mode of ['net', 'order'] as const) {
    const r = expandMeasurements(QUANTITY_REGISTRY, rs, { mode } as any);
    console.log(`== ${name} [${mode}]`, r.errors.length ? 'ERR ' + r.errors.join('; ') : '');
    for (const l of r.lines) console.log('  ', l.trade, '|', l.key, '|', l.item.slice(0, 60), '|', l.unit, 'net', l.net, 'gross', l.gross, 'order', (l as any).orderQuantity, (l as any).orderUnit ?? '');
  }
}
