import { QUANTITY_REGISTRY, expandMeasurements } from '/home/user/TakeoffSpeed/lib/quantities/index.ts';
type Inputs = Record<string, string | string[]>;
const rec = (assembly: string, tag: string, inputs: Inputs) => ({
  assembly, tag, confidence: 'high' as const,
  inputs: Object.entries(inputs).flatMap(([name, v]) => (Array.isArray(v) ? v : [v]).map(value => ({ name, value }))),
});
const m = (shape: string, role: string, lengths: string[], extra: Inputs = {}) => rec('structural-steel.member', shape, { shape, role, lengths, ...extra });
const records = [
  m('HSS1-1/2x1-1/2x3/16', 'column', [`1'-7" x 6`], { location: 'CANOPY SIGN TUBE' }),
  m('HSS4x4x1/4', 'column', ['5.6 FT', `1'-4" x 6`]),
  m('HSS5x5x3/8', 'column', ['20.3 FT', '18.9 FT']),
  m('HSS6x6x1/2', 'column', ['19.7 FT']),
  m('HSS6x6x3/8', 'column', ['61.4 FT', '175 FT']),
  m('HSS7x7x1/2', 'column', ['97.3 FT']),
  m('HSS4x4x1/4', 'beam', ['40.2 FT']), m('HSS5x5x1/4', 'beam', ['21.5 FT']), m('HSS6x2x1/4', 'beam', ['3 FT']),
  m('HSS6x4x3/8', 'beam', ['22.2 FT'], { location: 'T/S 12-8 5/8' }), m('HSS6x4x3/8', 'beam', ['9 FT'], { location: 'T/S 10-8 5/8' }),
  m('HSS6x6x3/8', 'beam', ['3.1 FT']), m('HSS8x2x1/4', 'beam', ['76.7 FT']), m('HSS8x3x1/4', 'beam', ['36.9 FT']), m('HSS8x6x1/4', 'beam', ['33.6 FT']), m('HSS10x6x1/4', 'beam', ['65.2 FT']),
  m('W8x10', 'beam', ['13.5 FT']), m('W10x12', 'beam', ['51.5 FT', '4.8 FT']), m('W10x22', 'beam', ['11.9 FT']), m('W12x14', 'beam', ['74.7 FT']), m('W12x22', 'beam', ['15 FT']), m('W14x26', 'beam', ['19.5 FT']), m('W14x30', 'beam', ['20.1 FT']), m('W16x26', 'beam', ['20.1 FT']),
  m('C5x6.7', 'channel', ['53.4 FT']), m('C7x9.8', 'channel', ['236.7 FT', '14 FT', '177.8 FT']), m('C8x11.5', 'channel', ['10.1 FT', '14.5 FT']),
  m('HSS4x4x1/4', 'brace', ['28.6 FT']), m('HSS6x6x1/4', 'brace', ['59.6 FT']), m('L3x3x1/4', 'brace', ['19.1 FT'], { location: 'HORIZONTAL BRACING' }),
  m('L2x2x3/16', 'angle', [`4'-0" x 18`, `5'-8"`]), m('L3x3x3/16', 'angle', ['99.4 FT']), m('L4x3x1/4', 'angle', ['179.9 FT'], { orientation: 'LLV' }),
  rec('structural-steel.joist', '12KCS2', { designation: '12KCS2', spans: ['54 FT'] }),
  rec('structural-steel.joist', '16KCS3', { designation: '16KCS3', spans: ['248.6 FT'] }),
  rec('structural-steel.joist', '18KCS2', { designation: '18KCS2', spans: ['108.5 FT'] }),
  rec('structural-steel.bridging', 'RJB', { shape: 'L2-1/2x2-1/2x1/4', type: 'horizontal', rows: ['121.9 FT'] }),
  rec('structural-steel.bridging', 'AX', { shape: 'L2-1/2x2-1/2x1/4', type: 'x', rows: ['35.5 FT'], joistSpacing: '55', joistDepth: '16"' }),
  rec('structural-steel.deck', 'RD-1.5', { areas: ['2208.4 SF'], ribDepth: '1-1/2" WIDE RIB TYPE B', gauge: '22', coating: 'GALVANIZED (G90)', use: 'roof' }),
  rec('structural-steel.plate', 'PL5', { kind: 'base plate', count: '6', size: '5" x 5"', thickness: '1/4"' }),
  rec('structural-steel.plate', 'BP12', { kind: 'base plate', count: '10', size: '12" x 12"', thickness: '3/4"' }),
  rec('structural-steel.plate', 'BP14', { kind: 'base plate', count: '4', size: '14" x 14"', thickness: '1"' }),
  rec('structural-steel.plate', 'BP1518', { kind: 'base plate', count: '4', size: '15" x 18"', thickness: '3/4"' }),
  rec('structural-steel.plate', 'CP5', { kind: 'cap plate', count: '2', size: '11" x 5-1/2"', thickness: '3/4"' }),
  rec('structural-steel.plate', 'CP6', { kind: 'cap plate', count: '16', size: '12" x 6-1/2"', thickness: '3/4"' }),
  rec('structural-steel.misc', 'LADDER', { kind: 'ladder', item: `1'9"Wx13'4"H ALUMINUM ROOF ACCESS LADDER`, count: '1' }),
];
const r = expandMeasurements(QUANTITY_REGISTRY, records, { mode: 'net' });
console.log('errors', JSON.stringify(r.errors), 'warnings', JSON.stringify((r as any).warnings ?? []).slice(0, 2000));
for (const l of r.lines) console.log(JSON.stringify({ key: l.key, item: l.item, net: Number(l.net), unit: l.unit }));
