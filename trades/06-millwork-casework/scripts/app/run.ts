// Feed this job's millwork measurements to the TakeoffSpeed engine (read-only use) and print net + order lines.
import { QUANTITY_REGISTRY, expandMeasurements } from '/home/user/TakeoffSpeed/lib/quantities/index';
type R = { line: string; assembly: string; tag: string; inputs: Record<string, string> };
const recs: R[] = [
  { line: '98', assembly: 'millwork.built-unit', tag: 'CHECK DESK', inputs: { unit: 'CHECK DESK', size: `4'-8 1/2"L x 2'D x 3'-6"H`, finish: 'PL-5, PL-6', count: '1' } },
  { line: '99', assembly: 'millwork.cabinet-run', tag: 'TB UPPER', inputs: { category: 'upper', depth: `1'-4"`, height: `3'-4"`, runs: `3'-10"`, config: 'W/ (2) ADJ. SHELVES', finish: 'PL-1', room: 'TRANSACTION BAR' } },
  { line: '100', assembly: 'millwork.cabinet-run', tag: 'TB BASE', inputs: { category: 'base', depth: `9 1/2"`, height: `3'-9"`, modules: `2'-3"; 2'-3"`, finish: 'PL-4', room: 'TRANSACTION BAR' } },
  { line: '101', assembly: 'millwork.accessory', tag: 'PENCIL DRAWER', inputs: { accessory: 'PENCIL DRAWER', count: '1', room: 'TRANSACTION BAR' } },
  { line: '102', assembly: 'millwork.laminate-face', tag: 'PL-3', inputs: { finish: 'PL-3', faces: `9'-7 3/4" x 6 1/4"; 2'-11 1/2" x 6 1/4"`, room: 'TRANSACTION BAR' } },
  { line: '103', assembly: 'millwork.laminate-face', tag: 'PL-4', inputs: { finish: 'PL-4', faces: `10'-4 1/4" x 3'-8 1/2"`, room: 'TRANSACTION BAR' } },
  { line: '104', assembly: 'millwork.laminate-face', tag: 'PL-5', inputs: { finish: 'PL-5', faces: `3'-10 1/4" x 1'-6"`, room: 'TRANSACTION BAR' } },
  { line: '105', assembly: 'millwork.accessory', tag: 'MAX6-94', inputs: { accessory: 'BRUSH GROMMET', mfr: 'MOCKETT', model: 'MAX6-94', size: '18"', count: '3', room: 'TRANSACTION BAR' } },
  { line: '106', assembly: 'millwork.accessory', tag: 'PC2026Z869 TB', inputs: { accessory: 'SQUARE GROMMET', mfr: 'RICHELIEU', model: 'PC2026Z869', count: '1', room: 'TRANSACTION BAR' } },
  { line: '107', assembly: 'millwork.cabinet-run', tag: 'BC 5', inputs: { category: 'base', depth: `2'-0"`, height: `2'-10"`, modules: `2'-0"`, config: 'W/ (2) SEPARATE DRAWERS', finish: 'PL-1', room: 'BACK COUNTER' } },
  { line: '108', assembly: 'millwork.cabinet-run', tag: 'BC 7', inputs: { category: 'base', depth: `2'-0"`, height: `2'-10"`, modules: `1'-4"; 1'-4"; 1'-6"; 1'-6"`, config: '(2) DRAWER', finish: 'PL-1', room: 'BACK COUNTER' } },
  { line: '109', assembly: 'millwork.cabinet-run', tag: 'BC 9', inputs: { category: 'base', depth: `2'-0"`, height: `2'-10"`, modules: `10 1/2"`, config: '(5) DRAWER', finish: 'PL-1', room: 'BACK COUNTER' } },
  { line: '110', assembly: 'millwork.shelving', tag: 'BC SHELF', inputs: { runs: `1'-0"; 1'-0"`, shelves: '2', depth: '11"', material: 'PLASTIC LAMINATE', support: 'none', finish: 'PL-1', room: 'BACK COUNTER' } },
  { line: '111', assembly: 'millwork.accessory', tag: 'PC2026Z869 BC', inputs: { accessory: 'SQUARE GROMMET', mfr: 'RICHELIEU', model: 'PC2026Z869', count: '1', room: 'BACK COUNTER' } },
  { line: '112', assembly: 'millwork.laminate-face', tag: 'PL-1 BC', inputs: { finish: 'PL-1', areas: '83.1', room: 'BACK COUNTER' } },
  { line: '113', assembly: 'millwork.cabinet-run', tag: 'LIB BASE', inputs: { category: 'base', depth: `1'-0"`, height: `2'-8"`, modules: `1'-3 3/4"; 1'-3 3/4"; 1'-3 3/4"; 1'-3 3/4"`, config: '(2) DRAWER', finish: 'PL-1', room: 'LIBRARY' } },
  { line: '114a', assembly: 'millwork.shelving', tag: 'LIB TOP SHELF', inputs: { runs: `8'-10 1/2"`, shelves: '1', depth: `1'-0"`, material: 'PLASTIC LAMINATE', support: 'none', finish: 'PL-1', room: 'LIBRARY' } },
  { line: '114b', assembly: 'millwork.shelving', tag: 'LIB ADJ SHELF', inputs: { runs: `5'-3"`, shelves: '2', depth: `1'-0"`, material: 'PLASTIC LAMINATE', support: 'none', finish: 'PL-1', room: 'LIBRARY' } },
  { line: '115', assembly: 'millwork.countertop', tag: 'LIB TOP', inputs: { runs: `5'-3"`, depth: `1'-0"`, material: 'PLASTIC LAMINATE', finish: 'PL-1', substrate: '3/4" PLYWOOD', room: 'LIBRARY' } },
  { line: '116', assembly: 'millwork.laminate-face', tag: 'PL-1 LIB', inputs: { finish: 'PL-1', faces: `1 1/2" x 8'-6"; 3'-6" x 1'-6"; 5'-6" x 8'-6"`, room: 'LIBRARY' } },
  { line: '117', assembly: 'millwork.cabinet-run', tag: 'SC SINK', inputs: { category: 'base', depth: `1'-10"`, height: `2'-8"`, modules: `2'-2"`, config: 'SINK BASE', finish: 'PL-1', room: 'SERVICE COUNTER' } },
  { line: '118', assembly: 'millwork.cabinet-run', tag: 'SC DRW', inputs: { category: 'base', depth: `1'-11"`, height: `2'-8"`, modules: `1'-6"; 1'-6"; 1'-6"`, config: '(3) DRAWER', finish: 'PL-1', room: 'SERVICE COUNTER' } },
  { line: '119', assembly: 'millwork.cabinet-run', tag: 'SC TRASH', inputs: { category: 'base', depth: `1'-11"`, height: `2'-8"`, modules: `1'-6"; 1'-6"`, config: 'TRASH', finish: 'PL-1', room: 'SERVICE COUNTER' } },
  { line: '120', assembly: 'millwork.cabinet-run', tag: 'SC UPPER', inputs: { category: 'upper', depth: `1'-0"`, height: `3'-0"`, modules: `3'-0"; 3'-4"; 3'-4"`, config: 'W/ (2) ADJ. SHELF', finish: 'PL-1', room: 'SERVICE COUNTER' } },
  { line: '121', assembly: 'millwork.shelving', tag: 'SC SHELF', inputs: { runs: `3'-0"`, shelves: '2', depth: '11"', material: 'PLASTIC LAMINATE', support: 'none', finish: 'PL-1', room: 'SERVICE COUNTER' } },
  { line: '122', assembly: 'millwork.shelving', tag: 'JAN SHELF', inputs: { runs: `4'-6 3/8"`, shelves: '3', depth: `1'-6"`, material: '3/4" WHITE MELAMINE', support: 'standards', bracket: 'HEAVY DUTY BRACKET', spacing: '24', room: 'JANITOR CLOSET' } },
  { line: '123', assembly: 'millwork.built-unit', tag: 'LOCKER', inputs: { unit: 'EMPLOYEE LOCKER', size: `2'-8"W x 1'-2"D x 6'-8"H`, count: '1', room: 'LOUNGE BOOTH' } },
  { line: '124', assembly: 'millwork.built-unit', tag: 'TABLE', inputs: { unit: 'TABLE', size: `2'-6"W x 3'D x 2'-5"H`, finish: 'PL-5', count: '1', room: 'LOUNGE BOOTH' } },
  { line: '125', assembly: 'millwork.built-unit', tag: 'SEAT', inputs: { unit: 'BOOTH SEATING', size: `3'W x 2'D x 3'-2"H`, finish: 'PL-1', count: '2', room: 'LOUNGE BOOTH' } },
  { line: '126', assembly: 'millwork.paneling', tag: 'MDF APRON', inputs: { surface: 'wall', material: '3/4" MDF', apronRuns: `2'-8 1/2"`, apronHeight: `1'-6"`, room: 'EMPLOYEE LOUNGE' } },
  { line: '127', assembly: 'millwork.cabinet-run', tag: 'EL DRW', inputs: { category: 'base', depth: `2'-0"`, height: `2'-8"`, modules: `1'-6"; 1'-3"`, config: '(3) DRAWER', finish: 'PL-1', room: 'EMPLOYEE LOUNGE' } },
  { line: '128', assembly: 'millwork.cabinet-run', tag: 'EL TRASH', inputs: { category: 'base', depth: `2'-0"`, height: `2'-8"`, modules: `1'-6"`, config: 'TRASH', finish: 'PL-1', room: 'EMPLOYEE LOUNGE' } },
  { line: '129', assembly: 'millwork.cabinet-run', tag: 'EL UPPER', inputs: { category: 'upper', depth: `1'-0"`, height: `2'-6"`, modules: `1'-6"; 2'-4"; 2'-4"; 2'-4"`, config: 'W/ (2) ADJ. SHELF', finish: 'PL-1', room: 'EMPLOYEE LOUNGE' } },
  { line: '130', assembly: 'millwork.countertop', tag: 'EL TOP', inputs: { runs: `8'-8"`, depth: `2'-0"`, material: 'PLASTIC LAMINATE', finish: 'PL-2', substrate: '1" PLYWOOD', room: 'EMPLOYEE LOUNGE' } },
  { line: '131', assembly: 'millwork.cabinet-run', tag: 'WR B1', inputs: { category: 'base', depth: `2'-0"`, height: `2'-8"`, runs: `1'-6"`, config: 'W/ DRAWER, ADJ. SHELF', finish: 'PL-1', room: 'WORK ROOM' } },
  { line: '132', assembly: 'millwork.cabinet-run', tag: 'WR B2', inputs: { category: 'base', depth: `2'-0"`, height: `3'-4"`, modules: `2'-6"`, config: 'W/ (2) ADJ. SHELVES', finish: 'PL-1', room: 'WORK ROOM' } },
  { line: '133', assembly: 'millwork.cabinet-run', tag: 'WR B3', inputs: { category: 'base', depth: `2'-0"`, height: `3'-4"`, modules: `1'-3"`, config: 'DRAWER', finish: 'PL-1', room: 'WORK ROOM' } },
  { line: '134', assembly: 'millwork.cabinet-run', tag: 'WR B4', inputs: { category: 'base', depth: `2'-0"`, height: `3'-4"`, modules: `1'-6"`, config: 'TRASH', finish: 'PL-1', room: 'WORK ROOM' } },
  { line: '135', assembly: 'millwork.cabinet-run', tag: 'WR UPPER', inputs: { category: 'upper', depth: `1'-2"`, height: `3'-0"`, runs: `5'-4"; 5'-8 1/2"`, config: 'W/ (2) ADJ. SHELVES', finish: 'PL-3', room: 'WORK ROOM' } },
  { line: '136', assembly: 'millwork.shelving', tag: 'WR SHELF', inputs: { runs: `7'-9 3/8"`, shelves: '2', depth: `1'-6"`, material: '3/4" WHITE MELAMINE', support: 'brackets', bracket: 'KV 180', room: 'WORK ROOM' } },
  { line: '137+139a', assembly: 'millwork.countertop', tag: 'WR TOP 1', inputs: { runs: `5'-6 3/4"`, depth: `2'-0"`, material: 'PLASTIC LAMINATE', finish: 'PL-2', substrate: '1-1/2" PLYWOOD', support: 'SUPPORT BRACKET', backsplash: `5'-8 1/2"; 1'-1 3/4"; 7 5/8"; 10 1/4"`, splashHeight: '4"', room: 'WORK ROOM' } },
  { line: '138+139b', assembly: 'millwork.countertop', tag: 'WR TOP 2', inputs: { runs: `5'-4"`, depth: `2'-0"`, material: 'PLASTIC LAMINATE', finish: 'PL-2', substrate: '1-1/2" PLYWOOD', backsplash: `5'-4"`, splashHeight: '4"', room: 'WORK ROOM' } },
  { line: '140+141', assembly: 'millwork.countertop', tag: 'PHONE TOP', inputs: { runs: `5'-6"`, depth: `2'-0"`, material: 'PLASTIC LAMINATE', finish: 'PL-2', substrate: '1-1/2" PLYWOOD', support: '21" A&M HYB BRACKET', backsplash: `5'-6"`, splashHeight: '4"', room: 'PHONE ROOM' } },
  { line: '142+144', assembly: 'millwork.paneling', tag: 'BOOTH WALL', inputs: { surface: 'wall', material: '13/16" PLASTIC LAMINATE PANEL', runs: `8'-0"; 8'-0"; 8'-0"; 8'-0"; 9"; 9"`, height: `9'-0"`, areas: '7.53', attachment: 'z-clips', finish: 'PL-1', reveals: `9'-0" x 8; 8'-6 1/2"; 8'-6 1/2"`, revealSpec: '1/2" FRY REGLET U-CHANNEL REVEAL MWU5050', room: 'BOOTH' } },
  { line: '143', assembly: 'millwork.paneling', tag: 'BOOTH CLG', inputs: { surface: 'ceiling', material: '13/16" PLASTIC LAMINATE PANEL', areas: '64.0625', attachment: 'z-clips', finish: 'PL-1', room: 'BOOTH' } },
  { line: '344a', assembly: 'millwork.countertop', tag: 'SLD BC', inputs: { runs: `8'-8"`, depth: `2'-1"`, material: 'QUARTZ', finish: 'SLD-1', room: 'BACK COUNTER' } },
  { line: '344b', assembly: 'millwork.countertop', tag: 'SLD SC', inputs: { runs: `9'-10"`, depth: `2'-0"`, material: 'QUARTZ', finish: 'SLD-1', room: 'SERVICE COUNTER' } },
  { line: '344c', assembly: 'millwork.countertop', tag: 'SLD TB', inputs: { runs: `10'-6 3/4"; 3'-10 1/4"`, depth: `2'-11 1/2"`, insideCorners: '1', material: 'QUARTZ', finish: 'SLD-1', waterfalls: `2'-11 1/2" x 3'-9 3/4"; 2'-0" x 3'-9 3/4"; 2'-11 1/2" x 3'-2 1/4"`, room: 'TRANSACTION BAR' } },
];
const records = recs.map(r => ({ assembly: r.assembly, tag: `L${r.line} ${r.tag}`, inputs: Object.entries(r.inputs).map(([name, value]) => ({ name, value })) }));
for (const mode of ['net', 'order'] as const) {
  const res = expandMeasurements(QUANTITY_REGISTRY, records, { mode });
  console.log(`\n===== mode ${mode}`);
  for (const r of res.records) {
    for (const l of r.lines) console.log(`${r.record.tag} | ${l.trade ?? 'millwork'} | ${l.item} | ${l.unit} | net ${l.net.toNumber(3)}`);
    for (const e of r.errors) console.log(`${r.record.tag} | ERROR ${e}`);
  }
  console.log('--- finalized');
  for (const l of res.lines) console.log(`${l.trade} | ${l.item} | ${l.unit} net ${l.net} waste ${l.wastePct}% order ${l.orderQuantity} ${l.orderUnit}`);
  if (mode === 'net') console.log('warnings:\n' + res.warnings.join('\n'));
}
