import { QUANTITY_REGISTRY, expandMeasurements } from '/home/user/TakeoffSpeed/lib/quantities/index.ts';

type In = Record<string, string | string[]>;
const rec = (assembly: string, tag: string, inputs: In) => ({
  assembly, tag, pages: [1],
  inputs: Object.entries(inputs).flatMap(([name, v]) => (Array.isArray(v) ? v : [v]).map(value => ({ name, value }))),
});
// C-4.0 STORM PIPES / STORM STRUCTURES tables: [name, size, L, upRim, upInv, dnRim, dnInv]
const storm: [string, string, string, string, string, string, string][] = [
  ['A1-A2', '18"', '17.69', '438.40', '435.09', '435.82', '435.00'],
  ['A2-A2.1', '18"', '45.97', '440.00', '435.32', '438.40', '435.09'],
  ['A2-A3', '18"', '92.25', '439.20', '435.55', '438.40', '435.09'],
  ['A2.1-A2.2', '18"', '85.26', '438.85', '435.74', '440.00', '435.32'],
  ['A3-A4', '18"', '70.17', '439.20', '435.90', '439.20', '435.55'],
  ['B1-B2', '15"', '25.11', '435.67', '435.00', '438.25', '434.87'],
  ['C1-C2', '18"', '21.08', '438.01', '434.86', '438.40', '434.75'],
];
// C-5.0 SANITARY PIPES / STRUCTURES tables
const san: [string, string, string, string, string, string][] = [
  ['S1-S2', '49.92', '439.06', '432.35', '438.31', '431.85'],
  ['S2-S3', '92.03', '439.39', '433.27', '439.06', '432.35'],
  ['S3-S4', '14.14', '439.66', '433.41', '439.39', '433.27'],
  ['S4-S5', '90.70', '439.96', '434.32', '439.66', '433.41'],
  ['S5-S6', '14.14', '439.86', '434.46', '439.96', '434.32'],
  ['S6-S7', '23.03', '440.12', '434.69', '439.86', '434.46'],
  ['S7-S8', '12.00', '440.37', '434.81', '440.12', '434.69'],
];
const mode = process.argv[2] ?? 'drawn';
const trench = (r: string[], extra: In = {}): In => mode === 'drawn'
  ? { rimStart: r[0]!, invertStart: r[1]!, rimEnd: r[2]!, invertEnd: r[3]!, bedding: 'stone', beddingBelow: '4"', ...extra }
  : { depthStart: `5'`, depthEnd: `5'`, trenchWidth: `3'`, bedding: 'none' };
const records: any[] = [];
for (const [n, s, L, ur, ui, dr, di] of storm) records.push(rec('site-utilities.pipe-run', n, { system: 'storm', size: s, material: 'HDPE', runs: L, ...(mode === 'drawn' ? {} : { od: s }), ...trench([ur, ui, dr, di]) }));
for (const [n, L, ur, ui, dr, di] of san) records.push(rec('site-utilities.pipe-run', n, { system: 'sanitary', size: '6"', material: 'PVC SDR-35', runs: L, ...(mode === 'drawn' ? {} : { od: '6"' }), ...trench([ur, ui, dr, di]) }));
records.push(rec('site-utilities.pipe-run', 'RD', { system: 'roof-drain', size: '8"', material: 'HDPE', runs: '168.18', ...(mode === 'drawn' ? {} : { od: '8"', depthStart: `5'`, depthEnd: `5'`, trenchWidth: `3'`, bedding: 'none' }) }));
records.push(rec('site-utilities.pipe-run', '8', { system: 'water', size: '1"', material: 'PVC', runs: '138.27', keynote: '8' }));
records.push(rec('site-utilities.pipe-run', '1', { system: 'gas', size: '2"', material: 'PE', runs: '156.4', keynote: '1', coordination: 'COORDINATE WITH UTILITY PROVIDER', furnishedBy: 'UTILITY' }));
records.push(rec('site-utilities.pipe-run', '3', { system: 'power', size: '4"', material: 'PVC CONDUIT', runs: '72.88', keynote: '3', furnishedBy: 'UTILITY' }));
records.push(rec('site-utilities.pipe-run', '4', { system: 'telecom', size: '4"', material: 'PVC CONDUIT', runs: '74.43', keynote: '4', furnishedBy: 'UTILITY' }));
records.push(rec('site-utilities.structure', 'STGI', { type: 'inlet', typeCode: 'A2-2-STGI HOODED GRATE', count: '5', detail: 'standard' }));
records.push(rec('site-utilities.structure', 'STYI', { type: 'yard-inlet', count: '1', detail: 'standard' }));
records.push(rec('site-utilities.structure', 'STJB', { type: 'junction-box', size: `4'-0" DIA`, count: '1', detail: 'none' }));
records.push(rec('site-utilities.structure', 'STOCS', { type: 'control-structure', size: `4'-0" DIA`, count: '1', detail: 'none' }));
records.push(rec('site-utilities.structure', 'SSCO', { type: 'cleanout', size: '4"', plug: 'RECESSED BRASS CLEANOUT PLUG', count: '6', detail: 'detailed' }));
records.push(rec('site-utilities.structure', 'STHW', { type: 'headwall', typeCode: 'A1-STHW', count: '1', wallLength: '8.8', detail: 'standard' }));
records.push(rec('site-utilities.fitting', '5', { kind: 'tapping-saddle', size: '8"x8"x1"', count: '1', keynote: '5' }));
records.push(rec('site-utilities.fitting', '9a', { kind: 'meter', size: '1"', service: 'DOMESTIC WATER', count: '1', keynote: '9' }));
records.push(rec('site-utilities.fitting', '9b', { kind: 'backflow', size: '1"', description: 'RPZ', service: 'DOMESTIC WATER', count: '1', keynote: '9' }));
records.push(rec('site-utilities.fitting', '2', { kind: 'connection', description: 'CORE EXISTING MANHOLE', service: 'SANITARY', count: '1', keynote: '2' }));
records.push(rec('site-utilities.fitting', 'IRR', { kind: 'backflow', description: 'IRRIGATION', service: 'IRRIGATION', count: '1', keynote: '2' }));
const r = expandMeasurements(QUANTITY_REGISTRY, records, { mode: 'net' });
for (const l of r.lines) console.log(JSON.stringify({ key: l.key, item: l.item, unit: l.unit, net: Number(l.net) }));
console.log('ERR', JSON.stringify(r.errors));
console.log('WARN', JSON.stringify(r.warnings).slice(0, 3000));
