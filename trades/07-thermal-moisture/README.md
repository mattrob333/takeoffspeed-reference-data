# 07 Thermal and moisture protection: insulation, roofing, flashing, coping, EIFS, ACM, barriers, sealants

Ground truth: estimate lines **148–189** (42 lines) of the bank branch job. This folder covers
quantities and material descriptions only; it carries no prices, labour or markups.

**Result:** 40 of the 42 lines rebuild to within 1% of the estimator's quantity (40 within 5%).

- **35 lines** come straight from markup legend rows, schedules or counts with a clear rule.
- **5 lines** reproduce numerically, but the rule behind them was back-solved and is flagged as inferred:
  - 148, which has two acoustic-sealant fits, neither confirmed;
  - the 2'-6" height in 157;
  - the 1 ft strip in 166;
  - the ceil-to-whole-foot transition run behind 154, 157 and 163.
- **2 lines do not reconcile:**
  - 149 (1330 LF opening sealant) is an allowance with no rule.
  - 162 (membrane) rebuilds from the measured rows to 2740.47 SF against 3042.774 (−9.9%). About 302 SF has no drawing-supported basis.

See `reconciliation.csv` for each line.

## Scope (what the 42 lines are)

| Group | Lines | Unit | What |
|---|---|---|---|
| Sealants | 148, 149, 150, 189 | LF | acoustic sealant at partitions; sealant at openings; exterior sealant with backer rod (150 and 189 carry the **same** 221.96 LF twice) |
| Building insulation | 151–157, 160, 161 | SF | under-slab XPS; sound blankets (A3B, A6B); cavity batts 3-1/2", 5-1/2", 8"; 2" rigid at the roof transition wall and behind cladding; booth-ceiling sound batt |
| Roof insulation | 158, 159, 163, 164 | SF | 2" polyiso (RT2), 6" polyiso R-34 (RT1), 1/4" cover board, tapered crickets |
| Roofing | 162, 165, 166, 167 | SF | 60-mil adhered single-ply membrane, roof vapor barrier (assumed), PSA air/vapor barrier at curbs, TPO walkway pads |
| Roof sheet metal and accessories | 168–177 | LF / EA | three copings, RTU curb, roof-hatch curb, drain and vent flashings, head flashing and self-adhered strip at the storefront head under the canopy, curb counterflashing |
| Cladding | 178–183 | SF / LF | EIFS-1 3", EIFS-2 5", EIFS soffit, ACM-1/2 walls, ACM-3 canopy soffit, ACM canopy fascia |
| Wall barriers and flashing | 184–188 | SF / LF | fluid-applied vapor barrier, prefinished aluminium sill, aluminium flashing, thru-wall flashing, integrated sill pan |

## Driving sheets

| Sheet | Markup page | Used for |
|---|---|---|
| A-120 Dimensional floor plan | p4 | wall runs by partition tag and height (A3B, A6B, EXT 8" @ 12'9", EXT 6" @ 12'3", …) → batts, acoustic sealant |
| A-620 Interior partition schedule | – (no markup page) | Table A series (A = GWB both sides, D = one side), Table B stud depth, Table D height letter (**B / D / F = "W/ BATT"**); general notes B, D, K |
| A-140 Roof plan + roof types RT1/RT2 | p7 | RT1/RT2 areas, crickets, walkway, coping runs, parapet laps, high-low wall, curbs, hatch, drain/vent dots, canopy edge, storefront head |
| A-450 Roof details | p20 (no legend) | 1 equipment curb (PSA air/vapor barrier, counterflashing), 4 base tie-in, 6/9 copings, 8 high-low roof, 10 roof transition, 11 hatch |
| A-430 Section details | p18 (no legend) | 1/2 ACM wall (rigid insul. + fluid VB), 3 wing-wall coping, 4/5 masonry base (rigid insul., thru-wall flashing), 6 storefront sill pan, 7/10 canopy edge, 8/9 storefront heads |
| A-200 / A-201 Exterior elevations | p11 / p12 | EIFS-1, EIFS-2, ACM1/2, brick, thru-wall flashing, aluminium flashing, prefinished sill, sealant with backer rod, sill-pan "Linear" run |
| A-130 RCP | p5 | ACM-3 canopy soffit, EIFS soffit |
| A-420 Wing walls | p17 | ACM1/ACM2 at the wing walls |
| A-706 Booth | p29 | booth roof area (6" sound batt) |
| S-201 Foundation plan | p33 | slab area, 8" stem wall LF (XPS) |
| G-003 COMcheck | – | detail 1: XPS under the slab with a 2'-0" turn-down "(where req'd zones > 4)"; envelope R-values |
| A-600 / A-610 | p21 / p22 | door and window sizes (opening sealant) |

## Spec sections (project manual page numbers)

`reference/sheets/spec_index.json` omits 07 2413 and 07 5423 and gives the wrong range for 07 4213.
The page ranges below come from the page headers.

| Section | Pages | Properties that matter for quantity / material |
|---|---|---|
| 07 2100 Thermal insulation | 146–150 | XPS ASTM C578 **Type IV, 25 psi** (p147); unfaced glass-fiber blanket ASTM C665 Type I (p148); below-grade horizontal insulation "extend a minimum of 24 in. in from exterior walls" (p149, 3.3.A.1); blankets in metal-stud walls over 96" must be mechanically supported (p149) |
| 07 2413 EIFS (Class PB) | 151–158 | basis of design Dryvit (p153); EPS board ASTM E2430, max **24 × 48 in.**, thickness per drawings (p154); glass-fiber reinforcing mesh ≥ 120 lbf/in, plus strip, detail and corner mesh (p154); adhesive notched-trowel ≥ 1/4" (p156) |
| 07 2500 Weather barriers | 159–161 | building wrap ASTM E1677 Type I (Tyvek basis); self-adhered butyl flexible flashing (p160) |
| 07 2616 Below-grade vapor retarders | 162–163 | 15 mil, < 0.012 perm; 6" laps taped (slab VB is in the concrete trade) |
| 07 2726 Fluid-applied membrane air barriers | 164–170 | dry film ≥ 35 mil (p166); vapor-retarding ≤ 0.08 perm (Grace Perm-A-Barrier basis) or permeable ≥ 15 perm (p167); transition strips at roofing and thru-wall flashing (6" wide, p168–169) |
| 07 4213 Metal composite material panels | 171–178 | Alcoa Reynobond FR, 0.020" skins, **0.157 in. (4 mm)** panel, FR core (p174); subgirts, extrusions and clips (p177) |
| 07 5423 TPO roofing | 179–187 | **60 mil** fabric-reinforced TPO, white, adhered (p179, p182); sheet flashing 55 mil (p183); polyiso ASTM C1289 Type II Class 1 Grade 2 (p183); tapered 1/4"/ft, crickets and saddles (p183); **cover board 1/2" glass-mat gypsum (p184), but the drawings say 1/4"**; two or more layers where total ≥ 2.7" (p185); walkways heat-welded (p186) |
| 07 6200 Sheet metal flashing and trim | 188–196 | aluminium ASTM B209; copings **0.040 in.**, 96 in.–12 ft sections, continuous cleats, joint plates (p193); cleats ≤ 12" o.c. (p194) |
| 07 7200 Roof accessories | 197–202 | curbs with 1-1/2" glass-fiber insulation and factory wood nailer (p199); roof hatch **30 × 36 in.**, single leaf, 14 ga (p200) |
| 07 9200 Joint sealants | 203–211 | silicone ASTM C920 (exterior), urethane (traffic), latex (interior, door frame perimeters), acoustical latex; "install acoustical sealant at both faces of partitions at perimeters" (p209, 3.3.G) |

## Material types as drawn

- **RT1** (main roof, 1864.3 SF): metal deck, then 3 × 2" polyiso (R-34.2, R-5.7/in, first layer mechanically fastened, the rest adhered), then 1/4" cover board, then single-ply membrane fully adhered.
- **RT2** (canopies, 285.4 SF): 5/8" plywood over steel and stud infill, then polyiso tapered to the drain (2" shown, 1" min), then single-ply membrane. RT2 has no cover board.
- **Walls:** 8" studs with batt (R-13 per COMcheck), sheathing and fluid-applied VB, finished with EIFS-1 3" (R-11.55), EIFS-2 5" (R-19.25), ACM on Z-girts over 2" rigid, or brick over 2" rigid (R-10).
- **Partitions:** A3B (3-5/8") and A6B (6") carry sound-attenuation blanket to structure.
- **Copings:** prefinished 0.040 aluminium with cleats and splice plates: 6/A450 (2'), 9/A450 (2'4"), 3/A430 (2'7").

## What the estimator measured, and how many lines reconcile

- **Areas (SF):** RT1, RT2, crickets, walkway, EIFS-1/-2 per elevation, ACM per elevation, ACM-3 canopy and EIFS soffit (RCP), booth roof, slab.
- **Lengths (LF):** wall runs by tag and height (A-120), parapet laps (with heights in the row name), copings, curbs, canopy edge, storefront head, high-low wall, and on the elevations thru-wall flashing, aluminium flashing, sills, sealant and the sill-pan "Linear" run.
- **Counts (EA):** drain flashings 11, vent flashings 3, hatch 1.
- **Rounding:** the estimator rounds most cladding and sheet-metal values **up to the next 5** (14 lines). Insulation SF is **rounded to the whole SF** (lines 158, 159, 161; 169 also rounds 148.1 down to 148). Measured sums are carried **unrounded** in lines 150, 164, 165, 167 and 185–189 (162's 3042.774 is also unrounded, but it is not a measured sum).

| Classification | Lines |
|---|---|
| measured (legend row(s), ± rounding) | 150, 158, 159, 161, 164, 165, 167–171, 175–183, 185–189 |
| measured + derived (LF × height) | 152, 153, 155, 156 |
| derived (formula on measured / other lines) | 151, 154, 160, 163, 184 |
| derived, estimator convention back-solved | 157, 166 |
| derived, convention inferred (two fits, neither confirmed) | 148 |
| derived, not reconciled (residual +302 SF) | 162 |
| counted / specified | 172, 173, 174 |
| allowance / judgment (no rule) | 149 |

Files: `formulas.md` (every rule with a worked example), `reconciliation.csv` (line by line),
`fixtures.json` (40 engine test cases; 149 and 162 are left out because neither can be reproduced), `reading-guide.md` (how to read the inputs, plus traps),
`app-gaps.md` (TakeoffSpeed engine comparison). The rebuild script is in
`trades/07-thermal-moisture/scripts/rebuild.py`.

## Verification

A reviewer pass, followed by this fix pass, checked seven findings against the sources. Every number was recomputed in Python
(`trades/07-thermal-moisture/scripts/verify.py` and `apply_fixes.py`, plus the reviewer's `recheck.py` and `search.py`
in `trades/07-thermal-moisture/scripts/07-thermal-moisture-review/`). Every fixture was re-run through an independent evaluator: all 40 pass, and
each `recomputed` equals the formula's output.

- **Models.** Claude Opus (review and fix) read the drawings and the JSON. GPT-6 Astra (`tools/ask_gpt.py`) gave second opinions:
  - The reviewer showed it the 10/A430 crop. It read a 4" wrap, giving 46.17 SF, with no basis for the full girth.
  - The reviewer showed it the A-620 base and head crops. It counted A = 2 + 2, D = 1 (+1), low walls = 2, which totals 1055.0 conditionally.
  - This pass showed it the zoomed 7/A430 and 10/A430 crops (`gpt-canopy-d7.txt`). It read the drawn turn-down as about 3-1/2" on both, with the 4" note governing and no full fascia wrap.
- **162 membrane (changed).** Detail 10/A430 says "WRAP MEMBRANE 4" MIN. OVER EDGE OF CANOPY". Detail 7/A430, which the original
  GPT consult believed was missing, is on the sheet and draws the same short turn-down. So the 2.5 ft fascia-girth term was removed.
  The line is now "derived, not reconciled": 2740.47 SF from the measured rows, with a +302.3 SF residual. 515 alternative splits
  land within 0.1%, so none was adopted. The L162 fixture was dropped.
- **148 acoustic sealant (changed).** A-B01 and A-T01 draw 2 + 2 beads, and D-B01 draws one bead on the gypsum side only.
  The stated rule is now 4 × A (149.2) + 2 × (D 49.7 + low 26.0 + exterior 153.4) = 1055.0 (+0.14%). The 4/1 fit (1053.0) is kept as an
  equally unconfirmed alternative. The fixture now uses four groups with beads 4/2/2/2. "GPT-6 Astra agreed" was deleted: the earlier
  consult had called the 4/1 rule "not a verified detail-based formula". The reading guide's "both sides" claim for D-B01, and its
  claim that A-T02 shows head sealant, were corrected.
- **161 booth batt (changed).** Line 312 is 77 LF of studs and line 302 is 77 SF of paint, so the "same area" note was rewritten.
  The cross-check in F2 was removed. Reading-guide §5 never carried that cross-check, so it needed no change.
- **149 opening sealant (changed).** This is now an allowance with no formula. The 910 + 419.06 = 1329.06 match is labelled a coincidence check.
  The L149 fixture was dropped, and L169 gained `round: 1` so that `recomputed` (148) equals its formula's output (reconciliation.csv row 169 now also shows 148).
- **156 8" batt (changed).** The note now says the line is carried from line 311, and that the legend rebuild is 10.52 SF short
  (−0.40%) with an unexplained residual that is not display rounding.
- **app-gaps (changed).**
  - Item 8 now names the 9 exterior glazed frames (344.4 LF). The two exterior doors sit inside frames B and F, so adding their perimeters would double count.
  - Item 7 is narrowed to `roofing.curb`, because `roofing.low-slope` already takes curb perimeters as LF.
  - Items 2 and 3 and the impact table were restated against the corrected 162 and 148 rules.
