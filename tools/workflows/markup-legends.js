export const meta = {
  name: 'markup-legend-extraction',
  description: 'Read every PlanSwift legend on the 92 estimator markup pages with two independent models, then settle disagreements with a third',
  phases: [
    { title: 'Read', detail: 'two independent readers (Sonnet, Opus) per batch of 2 pages' },
    { title: 'Reconcile', detail: 'Fable re-reads only the rows the two readers disagree on' },
  ],
}

const ROW = { type: 'object', properties: {
  name: { type: 'string', description: 'legend row text exactly as printed, e.g. WALL A6B @ 12\'6"H' },
  quantity: { type: 'number' },
  unit: { type: 'string', description: 'unit exactly as printed: FT, SF, EA, CY, LF, etc.' },
  color: { type: 'string', description: 'swatch colour in plain words' },
}, required: ['name', 'quantity', 'unit'] }
const PAGE = { type: 'object', properties: {
  page: { type: 'integer' },
  legendFound: { type: 'boolean' },
  items: { type: 'array', items: ROW },
  notes: { type: 'string', description: 'anything unreadable, cut off, or ambiguous; where the legend sits' },
}, required: ['page', 'legendFound', 'items'] }
const READ = { type: 'object', properties: { pages: { type: 'array', items: PAGE } }, required: ['pages'] }

const W = '/home/user/work/markups'
const R = '/home/user/takeoffspeed-reference-data'
const pages = args.pages
const batches = []
for (let i = 0; i < pages.length; i += 2) batches.push(pages.slice(i, i + 2))

const readPrompt = (b) => `You are transcribing the legend blocks of PlanSwift takeoff markup pages made by a professional estimator. These quantities are ground truth for a quantity-takeoff reference, so exactness matters more than speed. Quantities only — there are no prices on these pages and none are wanted.

Pages in this batch (page number, drawing sheet, title):
${b.map(p => `- page ${p[0]}: ${p[1]} ${p[2] || ''}`).join('\n')}

For each page you have pre-rendered images:
- ${W}/pNN-full.png  (whole page, 1.6x)
- ${W}/pNN-ll.png    (lower-left 40% x 38% of the page at 3.2x — the legend usually sits here)
- ${W}/pNN-lr.png    (lower-right region at 3.2x)
(NN = two-digit page number, e.g. p04-ll.png). Read the full page first to locate the legend block (a list of takeoff items, each with a colour swatch, an item name and a measured quantity with unit, e.g. "WALL A6B @ 12'6"H   28.4 FT"). The legend can be anywhere on the page and can be long. If any row is small, cut off or blurry, render a sharper crop yourself:
  python3 -I ${R}/tools/render.py markup <page> /home/user/work/crop-<page>-<k>.png <x0> <y0> <x1> <y1> <zoom>
(box in page fractions, origin top-left; zoom 4–6 for small text). Do this whenever you are not certain of a digit.

Transcribe EVERY legend row on each page: the name exactly as printed (keep heights, sizes, tags, 'SHTNG', 'NO GWB' etc.), the quantity as a number (no commas), the unit exactly as printed, and the swatch colour. Do not merge, skip, total or infer rows. If a page has no legend (cover sheet, notes), set legendFound false with items []. Say in notes anything you could not read with certainty.`

const norm = s => String(s || '').toUpperCase().replace(/[\s'"’”]+/g, '').replace(/[^A-Z0-9.@&/\-X]/g, '')
const key = it => `${norm(it.name)}|${norm(it.unit)}`

function compare(a, b) {
  // a, b: PAGE objects for the same page from two readers. Rows are matched as a
  // multiset (a page can repeat one item name with different quantities).
  const rest = [...(b?.items || [])]
  const agreed = [], disputed = []
  for (const it of a?.items || []) {
    const k = rest.findIndex(o => key(o) === key(it) && Math.abs(o.quantity - it.quantity) <= Math.max(0.051, Math.abs(it.quantity) * 0.0005))
    if (k >= 0) { agreed.push(it); rest.splice(k, 1) }
    else disputed.push({ readerA: it, readerB: rest.find(o => key(o) === key(it)) || null })
  }
  for (const o of rest) if (!disputed.some(d => d.readerB === o)) disputed.push({ readerA: null, readerB: o })
  return { agreed, disputed }
}

const results = await pipeline(batches,
  (b, _o, i) => parallel([
    () => agent(readPrompt(b), { label: `read-sonnet p${b.map(p => p[0]).join(',')}`, phase: 'Read', schema: READ, model: 'sonnet' }),
    () => agent(readPrompt(b), { label: `read-opus p${b.map(p => p[0]).join(',')}`, phase: 'Read', schema: READ, model: 'opus' }),
  ]),
  async ([s, o], b) => {
    const out = []
    for (const p of b) {
      const ps = s?.pages?.find(x => x.page === p[0])
      const po = o?.pages?.find(x => x.page === p[0])
      const { agreed, disputed } = compare(ps, po)
      let settled = []
      let reconcileNotes = ''
      if (disputed.length) {
        const r = await agent(`Two independent readers transcribed the PlanSwift legend on markup page ${p[0]} (sheet ${p[1]}). They agree on ${agreed.length} rows. They disagree on the rows below (null = that reader did not list the row). Look at the page yourself and give the correct row for every disputed item — name exactly as printed, quantity, unit — and drop rows that do not exist on the page. Render sharp crops of the legend to check digits:
  python3 -I ${R}/tools/render.py markup ${p[0]} /home/user/work/rec-${p[0]}-<k>.png <x0> <y0> <x1> <y1> 5
Pre-rendered: ${W}/p${String(p[0]).padStart(2, '0')}-full.png, -ll.png, -lr.png.
Also list any legend row BOTH readers missed.
Agreed rows (for context, do not repeat them): ${JSON.stringify(agreed.map(x => `${x.name} ${x.quantity} ${x.unit}`))}
Disputed: ${JSON.stringify(disputed)}`, { label: `reconcile-fable p${p[0]}`, phase: 'Reconcile', model: 'fable', schema: PAGE })
        settled = r?.items || []
        reconcileNotes = r?.notes || ''
      }
      out.push({ page: p[0], sheet: p[1], title: p[2], legendFound: !!(ps?.legendFound || po?.legendFound || agreed.length || settled.length),
        items: [...agreed.map(x => ({ ...x, verified: 'two readers agree' })), ...settled.map(x => ({ ...x, verified: 'settled by third reader' }))],
        disputedCount: disputed.length, notes: [ps?.notes, po?.notes, reconcileNotes].filter(Boolean).join(' | ') })
    }
    return out
  })
const flat = results.filter(Boolean).flat()
log(`${flat.length} pages, ${flat.reduce((n, p) => n + p.items.length, 0)} legend rows, ${flat.filter(p => p.disputedCount).length} pages needed a third reader`)
return flat
