import { QUANTITY_REGISTRY, expandMeasurements } from '/home/user/TakeoffSpeed/lib/quantities/index.ts';
type In = Record<string, string | string[]>;
const rec = (assembly: string, tag: string, inputs: In) => ({
  assembly, tag, pages: [1],
  inputs: Object.entries(inputs).flatMap(([name, v]) => (Array.isArray(v) ? v : [v]).map(value => ({ name, value }))),
});
const sets: [string, ReturnType<typeof rec>[]][] = [
 ['A estimator inputs', [
  rec('erosion-control.construction-exit', 'CO', { phase: '1', areas: '1569.4', thickness: '6"', stoneSize: 'N.S.A. R-2 (1.5"-3.5") crushed stone', geotextile: 'geotextile underliner', accessories: 'tire washrack area/tire washer, culvert under entrance - if required' }),
  rec('erosion-control.washout', 'WASH', { phase: '1', count: '1', size: `7'-0" x 7'-0"`, depth: '30"', liner: '10 mil plastic sheeting' }),
  rec('erosion-control.fuel-storage', 'FS', { phase: '1', areas: '25.1' }),
  rec('erosion-control.sediment-barrier', 'SD1-NS', { phase: '1', barrierType: 'compost-sock', description: '18" min dia', runs: `767.9'`, stakeSpacing: `2'` }),
  rec('erosion-control.linear-practice', 'RT-B', { phase: '1', practice: 'slotted-board-retrofit', runs: `5.14'` }),
  rec('erosion-control.stabilization', 'DS1', { phase: '1', practices: ['mulch', 'temporary-seed', 'dust-control'], codes: ['DS1', 'DS2', 'DU'], areas: '20298.88' }),
  rec('erosion-control.inlet-protection', 'SD2-F', { phase: '2', protectionType: 'filter fabric w/ supported frame', inlets: '4' }),
  rec('erosion-control.linear-practice', 'RT-P', { phase: '2', practice: 'half-round-pipe-retrofit', runs: `7.5'`, description: 'fill around barrier with 3"-4" stone' }),
  rec('erosion-control.stabilization', 'DS1b', { phase: '2', practices: ['mulch', 'temporary-seed', 'dust-control'], codes: ['DS1', 'DS2', 'DU'], areas: '15581.92' }),
  rec('erosion-control.stabilization', 'DS3', { phase: '2', practices: ['permanent-seed', 'matting'], codes: ['DS3', 'SS'], areas: '2114' }),
  rec('erosion-control.inlet-protection', 'SD2-P', { phase: '3', protectionType: 'curb inlet protection', inlets: '4' }),
  rec('erosion-control.stabilization', 'DS4', { phase: '3', practices: ['sod'], codes: ['DS4'], areas: '14393.68' }),
  rec('landscaping.plant', 'T1', { category: 'tree', commonName: 'American Holly', botanicalName: "Ilex opaca 'Greenleaf'", size: "6' HT.", root: 'B&B', scheduleQty: '5', planCounts: '11' }),
  rec('landscaping.plant', 'T2', { category: 'tree', commonName: 'Eastern Redcedar', botanicalName: 'Juniperus virginiana', size: "6' HT.", root: 'B&B', scheduleQty: '11', planCounts: ['1', '5'] }),
  rec('landscaping.plant', 'S1', { category: 'shrub', commonName: 'Florida Sunshine Anise', botanicalName: "Illicium parviflorum 'Florida Sunshine'", size: '3 GAL', scheduleQty: '17', planCounts: ['7', '3', '7'] }),
  rec('landscaping.plant', 'S2', { category: 'shrub', commonName: "Don's Dwarf Wax Myrtle", botanicalName: "Myrica cerifera 'Don's Dwarf'", size: '3 GAL', scheduleQty: '15', planCounts: ['6', '9'] }),
  rec('landscaping.mulch', 'M', { mulchType: 'pinestraw', description: 'pinestraw - mulch A', areas: '2500', depth: '3"' }),
  rec('landscaping.sod', 'SOD', { areas: '11500' }),
  rec('site-utilities.basin', 'POND', { keynote: '23', areas: '3074', basinBottom: '435.00', gravelBottom: '429.5', aggregate: 'clean open graded course aggregate', geotextile: '6 oz/sy non-woven geotextile fabric', underdrain: `95.6'`, underdrainPipe: '6" perforated HDPE underdrain' }),
 ]],
 ['B basin on the stone-bed floor (ST-1) with side wrap', [
  rec('site-utilities.basin', 'POND', { keynote: '23', areas: '962.4', basinBottom: '435.00', gravelBottom: '429.5', perimeter: `206'`, geotextile: '6 oz/sy non-woven geotextile fabric', underdrain: `95.6'`, underdrainPipe: '6" perforated HDPE underdrain' }),
 ]],
];
for (const [label, recs] of sets) {
  const r = expandMeasurements(QUANTITY_REGISTRY, recs, { mode: 'net' });
  console.log('##', label);
  for (const l of r.lines) console.log(JSON.stringify({ key: l.key, item: l.item, unit: l.unit, net: Number(Number(l.net).toFixed(4)) }));
  console.log('ERR', JSON.stringify(r.errors));
  console.log('WARN', JSON.stringify(r.warnings));
}
