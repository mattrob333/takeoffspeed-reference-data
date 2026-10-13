import { QuantityRegistry, expandMeasurements } from '/home/user/TakeoffSpeed/lib/quantities/engine';
import { fitoutModules } from '/home/user/TakeoffSpeed/lib/quantities/trades/fitout';
const registry = new QuantityRegistry(fitoutModules);
type Inputs = Record<string, string | string[]>;
const rec = (assembly: string, tag: string, inputs: Inputs) => ({
  assembly, tag, inputs: Object.entries(inputs).flatMap(([name, v]) => (Array.isArray(v) ? v : [v]).map(value => ({ name, value }))),
});
const TA = (tag: string, accessory: string, count: string[], extra: Inputs = {}) => rec('specialties.toilet-accessory', tag, { tag, accessory, count, ...extra });
const records = [
  TA('TA-3', 'GRAB BAR', ['1', '1'], { size: '18" VERTICAL', mfr: 'BRADLEY', furnishedBy: 'GC', installedBy: 'GC' }),
  TA('TA-3', 'GRAB BAR', ['1', '1'], { size: '42" HORIZONTAL', mfr: 'BRADLEY', furnishedBy: 'GC', installedBy: 'GC' }),
  TA('TA-3', 'GRAB BAR', ['1', '1'], { size: '36" HORIZONTAL', mfr: 'BRADLEY', furnishedBy: 'GC', installedBy: 'GC' }),
  TA('TA-4', 'WASTE RECEPTACLE', ['1', '1'], { mfr: 'BOBRICK', model: 'B-3644', mounting: 'RECESSED', furnishedBy: 'GC', installedBy: 'GC' }),
  TA('TA-6', 'MIRROR', ['1', '1'], { size: "2'x3'", mfr: 'BOBRICK', model: 'B-290', furnishedBy: 'GC', installedBy: 'GC' }),
  TA('TA-8', 'SANITARY NAPKIN DISPOSAL', ['0', '1'], { mfr: 'BOBRICK', model: 'B-270', furnishedBy: 'GC', installedBy: 'GC' }),
  TA('TA-9', 'COAT HOOK', ['1', '1']),
  TA('TA-10', 'MOP HOLDER', ['1'], { mfr: 'BOBRICK', model: 'B-223x24', furnishedBy: 'GC', installedBy: 'GC' }),
  TA('TA-1', 'TOILET TISSUE DISPENSER', ['1', '1'], { furnishedBy: 'OWNER VENDOR', installedBy: 'GC' }),
  TA('TA-2', 'PAPER TOWEL DISPENSER', ['1', '1'], { furnishedBy: 'OWNER VENDOR', installedBy: 'GC' }),
  TA('TA-5', 'SOAP DISPENSER', ['1', '1'], { furnishedBy: 'OWNER VENDOR', installedBy: 'GC' }),
  rec('specialties.signage', 'T.S.', { signType: 'TACTILE', size: '6" x 4"', count: ['3'], responsibility: 'CFCI' }),
  rec('specialties.signage', 'MEN', { signType: 'ADA MEN TOILET', size: '6" x 9"', count: ['1'], lettering: '5/8"H x 1/32" RAISED LETTERING, GRADE 2 BRAILLE', responsibility: 'CFCI' }),
  rec('specialties.signage', 'WOMEN', { signType: 'ADA WOMAN TOILET', size: '6" x 9"', count: ['1'], responsibility: 'CFCI' }),
  rec('specialties.fire-extinguisher', 'F.E.C.', { mount: 'recessed', extinguisherSize: '10 LB', rating: '4A:80B:C', count: ['2'] }),
  rec('specialties.panel-system', 'PNL-1', { tag: 'PNL-1', system: 'BOOTH SCREEN PANEL SYSTEM', faces: ['32" x 108"', '16" x 108"'], mfr: 'BIG APPLE VISUAL GROUP', filler: 'HARDWOOD BLOCKING FILLER BOTH SIDES' }),
];
const out = expandMeasurements(registry, records as any);
for (const l of out.lines) console.log(JSON.stringify({ key: l.key, item: l.item, net: Number(l.net), unit: l.unit, order: (l as any).orderQuantity }));
console.log('warnings', JSON.stringify(out.warnings));
console.log('errors', JSON.stringify(out.errors));
