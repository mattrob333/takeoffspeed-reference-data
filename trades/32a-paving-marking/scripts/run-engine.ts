import { QUANTITY_REGISTRY, expandMeasurements } from '/home/user/TakeoffSpeed/lib/quantities/index.ts';
type In = Record<string, string | string[]>;
const rec = (assembly: string, tag: string, inputs: In) => ({
  assembly, tag, pages: [72],
  inputs: Object.entries(inputs).flatMap(([name, v]) => (Array.isArray(v) ? v : [v]).map(value => ({ name, value }))),
});
const records = [
  rec('site-paving.asphalt', '3', { keynote: '3', duty: 'HEAVY', areas: '11367.3 SF', surface: '1-1/2"', surfaceMix: '9.5 MM', binder: '3"', binderMix: '19 MM', base: '4"', baseMix: '37.5 MM', subbase: '12"', geotextile: 'SEPARATION GEOTEXTILE', assumed: 'yes' }),
  rec('site-paving.asphalt', '4', { keynote: '4', duty: 'STANDARD', areas: '2459.18 SF', surface: '1-1/2"', surfaceMix: '9.5 MM', base: '3"', baseMix: '19 MM', subbase: '12"', geotextile: 'SEPARATION GEOTEXTILE', assumed: 'yes' }),
  rec('site-paving.concrete', '21', { keynote: '21', use: 'pavement', description: 'HEAVY DUTY - FOR PARKING', areas: ['241.8 SF', '505.8 SF'], thickness: '6"' }),
  rec('site-paving.sidewalk', '5', { areas: '1834.7 SF', thickness: '4"', psi: '3000 PSI', wwf: '6x6-W2.9xW2.9', expansionSpacing: `25'-0"`, jointMaterial: '1/4" EXPANSION JOINT' }),
  rec('site-paving.sidewalk', '5-RUNS', { runs: ['366.94'], width: `5'-0"`, thickness: '4"', expansionSpacing: `25'-0"`, jointMaterial: '1/4" EXPANSION JOINT (RUNS TEST)' }),
  rec('site-paving.curb-ramp', '6', { keynote: '6', standard: 'GDOT STANDARD', rampAreas: ['113.3 SF'], thickness: '6"' }),
  rec('site-paving.curb', '1', { curbType: '24" CURB & GUTTER', runs: ['993.9'], curbWidth: '6"', curbHeight: '12"', gutterWidth: '18"', gutterThickness: '6"', baseThickness: '4"' }),
  rec('pavement-marking.stripe', '16', { runs: ['441.31'], width: '4"', color: 'WHITE', coats: '2' }),
  rec('pavement-marking.stripe', '2', { runs: ['49.58'], width: '24"', color: 'WHITE' }),
  rec('pavement-marking.crosswalk', '17', { style: 'ladder', crossing: `22'-6"`, walkWidth: `5'-0"`, barWidth: '24"', barSpacing: `6'-0"`, lineWidth: '4"' }),
  rec('pavement-marking.access-aisle', 'AA', { aisles: '1', size: `5'-0" x 18'-0"`, width: '4"', color: 'BLUE', coats: '2' }),
  rec('pavement-marking.symbol', 'ADA', { symbol: 'ACCESSIBLE SYMBOL', count: '1', size: `3'-0" x 3'-0"`, color: 'WHITE', background: 'BLUE FIELD' }),
  rec('pavement-marking.symbol', '15', { symbol: 'ARROW', count: '2', size: `3'-8" x 9'-4"` }),
  rec('pavement-marking.sign', 'ADA', { legend: 'PERMIT PARKING ONLY TOW-AWAY ZONE', signCode: 'R7-8', count: '1', panelSize: '12" x 18"', panel: '.080 ALUMINUM', post: '2" X 2" X .188" STEEL TUBE IN 8" STD PIPE', plaques: '1', plaque: 'VAN ACCESSIBLE R7-8P5' }),
  rec('pavement-marking.sign', '12', { keynote: '12', legend: 'STOP', signCode: 'R1-1', count: '3', panelSize: '30" x 30"', post: '2" GALV. STL. CHANNEL' }),
  rec('pavement-marking.sign', '13', { keynote: '13', legend: 'DO NOT ENTER', signCode: 'R5-1', count: '2', post: '2" GALV. STL. CHANNEL' }),
  rec('site-improvements.bike-rack', '19', { count: '2', description: '1.25" DIA SCH 40 PIPE', footingsPerRack: '2', footingDiameter: `1'-0"`, footingDepth: `1'-0"` }),
  rec('site-improvements.bollard', 'TE1', { count: '5', diameter: '6"', height: `5'-0"`, material: 'GALVANIZED STEEL', finish: 'PAINTED YELLOW', footingDiameter: '16"', footingDepth: `3'-0"` }),
  rec('site-improvements.bollard', 'DT', { count: '8', diameter: '6"', height: `4'-0"`, material: 'STEEL', cover: 'INNOPLAST BOLLARD COVER', footingDiameter: '16"', footingDepth: `4'-0"` }),
];
for (const r0 of records) {
  const r = expandMeasurements(QUANTITY_REGISTRY, [r0], { mode: 'net' });
  console.log('##', r0.assembly, r0.tag);
  for (const l of r.lines) console.log('  ', JSON.stringify({ key: l.key, item: l.item, unit: l.unit, net: Number(l.net) }));
  if (r.errors.length) console.log('   ERR', JSON.stringify(r.errors));
  if (r.warnings.length) console.log('   WARN', JSON.stringify(r.warnings));
}
