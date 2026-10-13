export const meta = {
  name: 'trade-formula-reverse-engineering',
  description: 'Per trade: research takeoff best practice, reverse-engineer every estimate quantity from the estimator markups, specs and drawings into formulas and fixtures, adversarially verify with a different model, then fix',
  phases: [
    { title: 'Research', detail: 'Sonnet researches industry takeoff practice per trade (web, cited)' },
    { title: 'Reconcile', detail: 'Opus reconciles every estimate line to markup measurements, specs, drawings; writes formulas, fixtures, reading guide, app gaps' },
    { title: 'Verify', detail: 'Fable recomputes and tries to refute; GPT-6 Astra cross-check on the hardest items' },
    { title: 'Fix', detail: 'Opus applies the verified findings' },
  ],
}

const R = '/home/user/takeoffspeed-reference-data'
const APP = '/home/user/TakeoffSpeed'
const COMMON = `Repository: ${R} (a reference for building the most accurate AI quantity takeoff). Ground truth for one real commercial job (a single-storey bank branch):
- ${R}/reference/estimate/lines.json — every estimate line, QUANTITIES AND MATERIAL DESCRIPTIONS ONLY. Prices, labor and markups are out of scope: never read, use, write or mention any cost, price, labor hour or dollar figure, and do not open source/estimate.xlsx.
- ${R}/reference/markups/legends.json — every PlanSwift legend row the estimator measured, per markup page (item name, measured quantity, unit; verified by two independent readers, disputes settled by a third). ${R}/reference/markups/pages.json maps markup page → drawing sheet. The coloured runs/areas/dots on each markup page show WHAT was measured: render any page or crop with  python3 -I ${R}/tools/render.py markup <page> <out.png> [x0 y0 x1 y1] [zoom]  and Read the PNG.
- Drawings: ${R}/source/drawings/<Discipline>/*.pdf, indexed in ${R}/reference/sheets/index.json. Render any sheet/crop:  python3 -I ${R}/tools/render.py sheet <A-120> <out.png> [x0 y0 x1 y1] [zoom]. Text layers of single-sheet drawings: /home/user/work/text/<SHEET>.txt.
- Specifications: ${R}/source/specifications.pdf, sections indexed in ${R}/reference/sheets/spec_index.json; page text at /home/user/work/text/spec-pNNN.txt (NNN = 3-digit page).
- Second opinion from a different provider:  python3 -I ${R}/tools/ask_gpt.py "<question>" [image.png ...]  (GPT-6 Astra).
- The TakeoffSpeed app's quantity engine (to compare against, do not edit): ${APP}/lib/quantities/ (trades/*, engine.ts, profiles.ts) and ${APP}/docs/QUANTITY_ENGINE.md.
Write scratch files under /home/user/work/<trade>/ only. Use python for every calculation; never do arithmetic in your head.`

const lineDigest = (t) => `${t.count} lines: the lineNo list for "${t.trade}" in ${R}/reference/estimate/trades.json; read each line (section, tag, description, unit, quantity, drawing reference) from ${R}/reference/estimate/lines.json.`

const RECON = { type: 'object', properties: {
  linesTotal: { type: 'integer' }, linesReconciled: { type: 'integer', description: 'lines whose quantity was rebuilt from a source within 1%' },
  linesWithin5: { type: 'integer' }, unresolved: { type: 'array', items: { type: 'string' } },
  formulas: { type: 'integer' }, keyFindings: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' },
}, required: ['linesTotal', 'linesReconciled', 'linesWithin5', 'unresolved', 'formulas', 'keyFindings', 'summary'] }
const ISSUES = { type: 'object', properties: {
  issues: { type: 'array', items: { type: 'object', properties: {
    severity: { type: 'string', enum: ['wrong', 'unsupported', 'missing', 'minor'] }, file: { type: 'string' }, lineNo: { type: 'string' },
    problem: { type: 'string' }, evidence: { type: 'string' }, fix: { type: 'string' } }, required: ['severity', 'file', 'problem', 'evidence'] } },
  checked: { type: 'integer', description: 'formulas/lines you independently recomputed' }, verdict: { type: 'string' },
}, required: ['issues', 'checked', 'verdict'] }
const FIXED = { type: 'object', properties: { fixed: { type: 'integer' }, rejected: { type: 'array', items: { type: 'string' } }, summary: { type: 'string' } }, required: ['fixed', 'rejected', 'summary'] }

const results = await pipeline(args.trades,
  (t) => parallel([
    () => agent(`${COMMON}

You are researching industry best practice for the quantity takeoff of one trade: **${t.title}** (folder ${R}/trades/${t.trade}/).
Use web search (load WebSearch/WebFetch via ToolSearch) to find authoritative, practical sources: estimating handbooks and guides, manufacturer installation and coverage data (e.g. USG, ClarkDietrich, Armstrong, Schluter, Sherwin-Williams, CRSI, ACI, NECA, SMACNA, PHCC as relevant), RSMeans-style takeoff conventions, trade association guides, and experienced estimators' write-ups. Quantities and material types only — skip pricing and labor productivity.
Write ${R}/trades/${t.trade}/best-practices.md: what an estimator takes off for this trade and in which units; which sheets and spec sections drive it; standard measurement rules (what to deduct, what not to, how openings, corners, laps, overlaps, heights, slopes are handled); standard coverage/yield and waste factors with their basis; the material breakdown an estimator lists (primary materials and the accessories/components that follow from them); common mistakes and how to check a takeoff; and what an AI takeoff must read from the drawings and specs to do it right. Cite every factual claim with a link. Be specific and numeric where sources are. Return a 5-line summary.`, { label: `research ${t.trade}`, phase: 'Research', model: 'sonnet' }),
    () => agent(`${COMMON}

Trade: **${t.title}** — folder ${R}/trades/${t.trade}/ (create it). Its estimate lines — ${lineDigest(t)}

Goal: reverse-engineer exactly how the estimator produced every one of these quantities, so the TakeoffSpeed app can reproduce them with written formulas instead of AI guesses. Work like a senior estimator auditing a takeoff:
1. For each line, find its source: the markup legend row(s) (search legends.json by item name, tag, size, height; check the markup page image to see what the colour covers), a schedule or count on a sheet, a spec requirement, or a derivation from other lines. Read the relevant spec sections for material types, sizes, gauges, thicknesses, spacing, coverage and accessories.
2. Rebuild the quantity with python from the source values. Find the formula (e.g. studs SF = Σ(LF × height) or LF × 12/spacing; board SF = wall LF × board height × faces − openings; sheets = SF/32; compound = SF × ratio; derived lines as ratios of their parent). When a ratio is the estimator's own convention, compute it from this job and say so. Classify each line: measured (straight from a markup), derived (formula on measured), counted, specified (from schedule/spec), allowance/judgment (no reproducible source — say why).
3. Write in ${R}/trades/${t.trade}/:
   - README.md — scope; driving sheets and spec sections (with page numbers); material types with their specified properties; what the estimator measured, in which units, and how many lines reconcile.
   - formulas.md — every formula: name, inputs with units, the rule, conventions/ratios with their basis, and a worked example using this job's numbers.
   - reconciliation.csv — columns: lineNo,description,unit,estimatorQty,source,sourceValues,formula,recomputedQty,deltaPct,classification,notes (one row per estimate line; description shortened; no prices).
   - fixtures.json — test cases for the app's quantity engine: [{"name", "formula", "inputs": {...with units}, "expected": {"quantity", "unit"}, "tolerancePct", "source": "lineNo / markup page"}], one per reproducible line.
   - reading-guide.md — how to read the plans and specs for this trade: which sheets, legends, schedules, symbols, tags and notes; how each input to the formulas is read (with the actual strings/tags from this job); cross-checks; and the traps you hit.
   - app-gaps.md — compare with the TakeoffSpeed engine (${APP}/lib/quantities/trades/... for this trade): what it already does right, what it computes differently (with numbers), what inputs it lacks, and concrete changes, ranked by quantity impact.
Be exhaustive: every line accounted for. Return the structured summary.`, { label: `reconcile ${t.trade}`, phase: 'Reconcile', model: 'opus', effort: 'high', schema: RECON }),
  ]),
  ([research, recon], t) => agent(`${COMMON}

You are an adversarial reviewer of the takeoff reverse-engineering for **${t.title}** in ${R}/trades/${t.trade}/ (README.md, formulas.md, reconciliation.csv, fixtures.json, reading-guide.md, app-gaps.md, best-practices.md). The analyst reported: ${JSON.stringify(recon || {}).slice(0, 2500)}
Your job is to find what is wrong. For as many reconciliation rows as you can (all of them if the trade is small; at least 15 otherwise, prioritising the largest quantities and anything marked within 1%): independently look up the source values in legends.json and the markup/drawing images, recompute the formula yourself in python, and check that it really produces the estimator's quantity — a formula fitted backwards to one number with an arbitrary factor is not a finding. Check every fixture computes to its expected value. Check material types and specified properties against the spec text. Check that no price, labor or dollar figure appears anywhere. For the two or three hardest or most suspicious items, also get an independent reading from GPT-6 Astra (tools/ask_gpt.py, with the relevant image crop) and say whether it agrees.
Report each problem with evidence and the correct fix. Write nothing to the trade folder yourself.`, { label: `verify ${t.trade}`, phase: 'Verify', model: 'fable', effort: 'high', schema: ISSUES })
    .then(v => ({ v, recon, research })),
  ({ v, recon }, t) => (v && v.issues && v.issues.length)
    ? agent(`${COMMON}

A reviewer checked the takeoff reverse-engineering for **${t.title}** in ${R}/trades/${t.trade}/ and found these issues:
${JSON.stringify(v.issues).slice(0, 12000)}
For each: verify it yourself (recompute in python, look at the source). Fix the files where the reviewer is right; where they are wrong, leave the file and say why. Keep reconciliation.csv, fixtures.json and formulas.md consistent with each other, and update the README's reconciliation count. Append a short "Verification" section to README.md listing what was checked, by which models, and what changed.`, { label: `fix ${t.trade}`, phase: 'Fix', model: 'opus', effort: 'high', schema: FIXED })
      .then(f => ({ trade: t.trade, recon, verify: v, fix: f }))
    : { trade: t.trade, recon, verify: v, fix: null })

const ok = results.filter(Boolean)
log(`${ok.length}/${args.trades.length} trades done; ${ok.reduce((n, r) => n + (r.recon?.linesReconciled || 0), 0)} lines reconciled within 1%`)
return ok.map(r => ({ trade: r.trade, recon: r.recon, issues: r.verify?.issues?.length ?? null, verdict: r.verify?.verdict, fix: r.fix }))
