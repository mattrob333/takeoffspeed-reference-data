import { QUANTITY_REGISTRY, expandMeasurements } from '/home/user/TakeoffSpeed/lib/quantities/index.ts';

type In = Record<string, string | string[]>;
const rec = (assembly: string, tag: string, inputs: In) => ({
  assembly, tag, pages: [1],
  inputs: Object.entries(inputs).flatMap(([name, v]) => (Array.isArray(v) ? v : [v]).map(value => ({ name, value }))),
});

const records = [
  rec('pavement-marking.sign', 'ADA', { legend: 'RESERVED PARKING', signCode: 'R7-8', count: '1', footingDiameter: '12"', footingDepth: `3'-6"` }),
  rec('pavement-marking.sign', '12', { legend: 'STOP', signCode: 'R1-1', count: '3', footingDiameter: '8"', footingDepth: `3'-0"` }),
  rec('pavement-marking.sign', '13', { legend: 'DO NOT ENTER', signCode: 'R5-1', count: '2', footingDiameter: '8"', footingDepth: `3'-0"` }),
  rec('site-paving.concrete', '14', { use: 'pad', description: 'FOR TRANSFORMER', areas: '16 SF', thickness: '10"', assumed: 'yes' }),
  rec('site-paving.concrete', 'CO', { use: 'pad', description: 'FOR CLEANOUT', rects: Array(6).fill('18" x 18"'), thickness: '6"' }),
  rec('site-paving.concrete', '21', { use: 'enclosure-slab', description: 'HEAVY DUTY - FOR DUMPSTER', areas: '384.3 SF', thickness: '6"' }),
  rec('site-improvements.wall-footing', 'DE', { wall: 'DUMPSTER ENCLOSURE WALL', runs: '36.22', width: `2'-0"`, thickness: `1'-0"`, bottomDepth: `2'-4"`, wallWidth: '8"' }),
  rec('site-improvements.cmu-wall', 'DE', { wall: 'DUMPSTER ENCLOSURE', runs: '36.22', height: `8'-0"`, thickness: '8"', verticalBar: '#5', verticalSpacing: '32"', bondBeams: '1', bondBeamBars: '1', bondBeamBar: '#5', cap: '4" PRECAST CONCRETE STONE CAP ON MORTAR BED', thruWallFlashing: 'yes', drip: 'yes', capSealant: 'yes', finish: '5/8" CEMENTITIOUS COATING EPT-1', finishFaces: '1', finishHeight: `6'-8"` }),
  rec('site-improvements.cmu-wall', 'DE-FULL', { wall: 'DUMPSTER ENCLOSURE FULL', runs: '36.22', height: `8'-0"`, thickness: '8"', grout: 'full' }),
  rec('site-improvements.gate', 'TE', { size: `16'-0" x 6'-8"`, material: 'STEEL', leaves: 'double' }),
  rec('site-improvements.item', 'DUMP', { kind: 'dumpster', description: '2 YARD DUMPSTER', count: '2' }),
  rec('site-improvements.item', 'MON', { kind: 'monument-sign', description: 'PROPOSED MONUMENT SIGN', count: '1', furnishedBy: 'OTHERS' }),
  rec('site-improvements.item', 'ATM', { kind: 'atm', description: 'ATM', count: '1', furnishedBy: 'VENDOR' }),
  rec('site-improvements.canopy', 'CAN', { areas: '61.7 SF', columns: '2' }),
  rec('site-improvements.pier-footing', 'LP', { use: 'light-pole', count: '5', diameter: `1'-6"`, depth: `6'-0"`, exposed: `2'-6"` }),
];

const pick = (tags: string[]) => records.filter(x => tags.includes(x.tag));
for (const [label, tags, conv] of [['cells', ['DE'], {}], ['full', ['DE-FULL'], {}], ['full-profile', ['DE-FULL'], { 'site-improvements.cmu-grout-cf-per-sf-full': '0.3024', 'site-improvements.cmu-mortar-cf-per-100-units': '14.8888889' }]] as const) {
  const rr = expandMeasurements(QUANTITY_REGISTRY, pick([...tags]), { mode: 'net', conventions: conv as Record<string,string> });
  for (const l of rr.lines) if (/grout|mortar|units/.test(l.key)) console.log(label, l.key, l.net);
}
const o = expandMeasurements(QUANTITY_REGISTRY, pick(['LP','ADA','12']), { mode: 'order' });
for (const l of o.lines) console.log('order', l.key, l.net, l.wastePct, l.orderQuantity, l.orderUnit);
const r = expandMeasurements(QUANTITY_REGISTRY, records.filter(x => x.tag !== 'DE-FULL'), { mode: 'net' });
for (const l of r.lines) console.log(JSON.stringify({ key: l.key, item: l.item, unit: l.unit, net: l.net }));
console.log('ERR', JSON.stringify(r.errors));
console.log('WARN', JSON.stringify(r.warnings));
