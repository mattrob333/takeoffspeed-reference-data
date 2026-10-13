# 23 HVAC: ductwork, devices, units, controls

Single-storey bank branch (Fifth Third Bank, Watson Blvd; 1,900 GSF per G-001 and the title block, 1,892 SF net
on the G-001 code plan). Estimate lines **445–494** (50 lines), DIV 23 HVAC. Quantities and materials only.

**Result: 49 of 50 lines rebuild from a written source within 1%** (42 counts exact, 5 measured LF
within 0.65%, 2 derived duct lines within 0.03%). The one line with no reproducible quantity is the
lump-sum fittings allowance (445), carried as 1 LS on a 2,000 SF area basis. The refrigerant LF (452)
reproduces from the legend and from the trace geometry, but the trace is not the pipe route (see below).

## Scope as the estimator carried it

| Group (estimate section) | Lines | Unit | What it is | Source |
|---|---|---|---|---|
| ALLOWANCE | 445 | LS | Duct fittings allowance, "AREA: 2000 SF" | judgment |
| DUCT WORK | 446 | LBS | 26 ga galvanized sheet metal, all rigid duct | derived from 12 duct LF rows, p53 |
| INSULATION | 447 | SF | "1.5" fiberglass" on all rigid duct | derived, same 12 rows |
| FLEXIBLE DUCTWORK | 448–451 | LF | 6", 8", 10", 14" flex | measured, p53 |
| REFRIGERANT PIPE | 452 | LF | Mini-split line set, size not given | measured, p53 |
| AIR DISTRIBUTION DEVICES | 453–473 | EA | 11 slot-diffuser lines (LSD/LSR by slots × length × CFM), 6 square supply diffusers, 6 eggcrate return grilles (by neck + CFM) | counted, p53 + M-301 tags |
| EXHAUST FAN | 474–476 | EA | EF-1..EF-3 Greenheck ceiling fans | counted, p53 |
| ROOF TOP UNIT | 477–478 | EA | RTU-1, RTU-2 Carrier rooftop heat pumps | counted, p54 |
| AIR CONDITIONER | 479 | EA | FCU-1/HP-1 Mitsubishi mini-split (one system) | counted at HP-1, p54 |
| DRAIN | 480 | EA | 1-1/2" RTU condensate drain assembly | counted, p54 (see the trap below) |
| SENSOR | 481–487 | EA | SAT, RAT, CO2, VOC, space temperature, OAT sensors; thermostats | counted, p53 + p54 |
| EXHAUST HOOD | 488 | EA | 24"x22" gravity hood eq. Greenheck FGR | counted, p54 |
| DAMPER | 489–491 | EA | Remote-cable dampers (keynotes 6+7), wax-actuated VAV damper (keynote 9), manual damper | counted, p53 |
| MISC. | 492–494 | EA | Particle counter, T/RH display, sectorizing baffle | counted, p53 |

Not carried as Div 23 lines: duct fittings, transitions, turning vanes, spin-ins, hangers, sealant,
flexible connections, duct liner, refrigerant insulation, TAB, and duct access doors (all inside the 445
allowance or left out). Handled elsewhere: RTU 18" curbs → roofing line 171 (18"H prefab metal curb,
40 LF); black paint on 4 LSD + 1 LSR (legend "PAINT LSD BLACK" 4, "PAINT BLACK LSR" 1 on p53) → Div 09
line 305 (5 EA); condensate pipe → plumbing line 417; RTU gas shut-offs → plumbing 443; disconnects and
the mini-split wired remote controller (M-503, p55) → Div 26 lines 553/554/593.

## Driving sheets

| Sheet | Markup page | Role |
|---|---|---|
| M-001 Mechanical notes and specifications | — | Duct gauge rule (Part 2 §1.B): rectangular **26 ga for all sizes**; round ≤14" 26 ga, 15–26" 24 ga; G60 galvanized ASTM A653; flex ≤5 ft (note CC) |
| M-002 Notes and legend | — | Symbol legend: T, RAT, SAT, AT, HS, SD, C (CO2), V (VOC), PC, TR; duct symbols (lined duct, flex, MVD) |
| M-101 Schedules | p52 (highlights only, no legend) | RTU, mini-split, exhaust fan schedules; air distribution schedule (neck by CFM; LSD/LSR/LD definitions); duct sizing guide; duct insulation R-value table |
| M-301 Proposed ceiling plan | **p53** (55-row legend) | All duct LF, flex LF, refrigerant LF, devices, sensors, dampers, keynotes 1–12 |
| M-302 Proposed roof plan | **p54** (6-row legend) | RTU-1/2, HP-1, OAT sensors, condensate drain, exhaust hood |
| M-401/M-402 Isometric / duct sections | — (not marked up) | Vertical drops (not added to LF) |
| M-503 Controls details | p55 | Disconnects, wired remote controller (Div 26 lines) |
| G-001 Life safety plan | — | 1,900 GSF building area (allowance basis) |

## Specification sections (project manual PDF page numbers)

| Section | Pages | What it fixes |
|---|---|---|
| 23 0500 Common work results for HVAC | 395–409 | General; governs all Div 23 |
| 23 0593 TAB | 410–413 | Independent balancing (no estimate line) |
| 23 0713 Duct insulation | 414–416 | **Wrap: 2.2" thick, ≥0.75 pcf fiberglass, installed R ≥ 6.0, FSKL jacket** (p.414 §2.2.A); **liner: 1", 1.5 pcf** (§2.1.A); liner throughout all return/transfer and 25 ft downstream of each RTU (p.415 §3.1.B); all unlined supply wrapped (§3.1.F); pins on ducts ≥18" wide; 2" SMACNA tape |
| 23 2300 Refrigerant piping | 417–422 | Type L / ACR copper brazed; **suction insulation 1-1/2" AP Armaflex**, condensate 1" (p.420 §2.4.A); hangers 8 ft for ≤2" |
| 23 3100 HVAC ducts and casings | 423–428 | SMACNA 2005; galvanized G90 (§2.1.A, conflicts with M-001 "G60"); **lined duct 2" larger each way** (§1.3.B); low pressure 1" w.g. Seal Class C; flex Class 1 UL 181 R-4.2 min, max 8' low-pressure supply, 2' return (§2.5); spin-in with damper at every flex runout (§2.5.G); access door at each fire/smoke damper (§2.9); remote cable balancing where inaccessible (§3.1.H) |
| 23 3713 Diffusers, registers and grilles | 434–437 | Titus basis; LSD Titus ML-39 aluminum, 2 slots unless noted |
| 23 7400 Packaged outdoor HVAC equipment | 429–433 | Full-perimeter curb by unit manufacturer |

## Material types and specified properties

- **Rigid duct**: galvanized steel, lock-forming, 26 ga for every rectangular size and every round ≤14"
  (M-001). All round on this job is 6"–14", so the whole system is 26 ga = **0.906 lb/SF**.
- **Duct wrap**: spec 2.2" R-6 FSK fiberglass; the estimate line reads "1.5" FIBERGLASS INSULATION" —
  the thickness differs from the spec, but the thickness never entered the quantity.
- **Duct liner**: 1" (spec) — not carried.
- **Flex**: factory-insulated R-4.2 min, UL 181 Class 1; 6/8/10/14" diameters on this job.
- **Refrigerant**: line set to the Mitsubishi PKA-A12LNL / PUZ-A12NL mini-split, size per manufacturer
  (M-301 keynote 2) — carried as "SIZE NOT GIVEN".
- **Air devices** (M-101): LSD(X) = Titus MLTI-39 slot diffuser, X one-inch slots, 4'-0" long with
  insulated plenum and face-operated damper; "LD"/(2-24") = 2'-0" version; LSR = return slot; square
  supply = Titus OMNI 24x24 or 12x12 face (face from the drawn symbol size: 65S drawn 1'-0", the rest
  2'-0"; the overlapping 0–90/0–100 CFM bands cannot decide it), neck 6"/8"/10"/12"/14" by CFM band; return = Titus
  50F eggcrate.

## What the estimator measured

- On **M-301 (p53)**: 55 legend rows — 17 in FT (12 rigid duct sizes: 8 rectangular + 4 round; 4 flex;
  1 refrigerant) and 38 in EA (21 air-device rows by size + CFM, 3 fans, 14 sensor/damper/misc/paint rows).
  The original `reference/markups/legends.json` held 47: its merge kept the last occurrence of each repeated
  name and dropped 8 rows. Those 8 are now restored (tagged "duplicate name restored"), but three restored
  supply rows carry the wrong colour; see reading-guide trap 1.
- **Refrigerant (452)**: the 30.9 FT purple trace follows both drawn lines of the line set and then an
  extra 7.97 FT leg with no pipe under it (1.22 + 10.52 + 0.36 + 9.89 + 0.89 + 7.97 = 30.86 FT unrounded = the
  estimate). The route counted once is 11.75 FT. No vertical rise; the M-302 roof run is not included.
- On **M-302 (p54)**: 6 count rows (HP-1, RTU-1, RTU-2, OAT ×2, condensate drain, hood).
- Rigid duct LF were never carried as lines; they became **one weight line and one insulation line**,
  both from the same bare surface area: **1,324.81 SF = 993.53 SF rectangular + 331.28 SF round**.
  Weight = 1,324.81 × 0.906 = 1,200.28 → 1,200 LBS. Insulation = 1,324.81 → 1,325 SF.
  No seam, joint, fitting or waste factor; flex excluded from both.

## Unresolved

- **Refrigerant third leg (452).** 7.97 of the 30.86 LF lies on a trace along the top of FCU-1 and grey
  linework with no pipe drawn under it. The quantity reproduces, but why the estimator traced it is not
  known, so a drawing-faithful takeoff (route once ≈11.75 LF, or two pipes ≈22.9 LF) will not match it.

## Files

- `formulas.md` — every formula with this job's worked numbers.
- `reconciliation.csv` — all 50 lines.
- `fixtures.json` — 49 engine test cases (every line but the allowance).
- `reading-guide.md` — how to read M-001/M-101/M-301/M-302 for this trade, and the traps.
- `best-practices.md` — researched trade practice (separate pass).
- `app-gaps.md` — TakeoffSpeed `lib/quantities/trades/mep/hvac.ts` versus this estimate, ranked.

## Verification

A reviewer pass (with GPT-6 Astra as its second reader) raised 9 issues. Each one was re-checked by
Claude Opus 5.5 against the sources, with every number recomputed in Python
(`trades/23-hvac/scripts/verify/`: `purple2.py`, `gauge.py`, `tagcol.py`, `fix_data.py`). GPT-6 Astra
independently traced the refrigerant markup (`verify/gpt_refrig_trace.txt`).

| # | Issue | Verdict | What changed |
|---|---|---|---|
| 1 | Refrigerant 30.9 FT is not the route counted once | **Right on the problem, wrong on the cause.** The route is 11.75 FT, but the plan geometry does regenerate 30.9: the purple trace covers both drawn pipes plus a 7.97 FT extra leg, 30.86 FT in all (Claude pixel trace). GPT-6 Astra got 30.92 FT and agreed it counts "more than both pipes". The reviewer's "no other purple linear markup" and "must include vertical legs" do not hold | F4 rewritten with the segment table; 452 row and fixture (`trace_LF`, segments, route-once reference); reading-guide trap 8; app-gaps row 8; best-practices §1; new Unresolved entry for the extra leg. 452 stays `measured` |
| 2 | p53 legend is 55 rows, not 56 | Right: 27 + 28 rows on the zoom-4 renders = 55 (17 FT + 38 EA, 21 air-device rows; 8 dropped) | 56→55, 39→38, 22→21, 9→8 in README and reading-guide trap 1 |
| 3 | Duplicate rows attributed the wrong way round | Right for the original 47-row legends.json (its merge kept the last occurrence: olive 330, salmon 150, bright green 240S, yellow 895R). Since then legends.json has been re-merged to 55 rows with the 8 restored, so "missing" no longer applies. The four restored supply rows are all labelled "magenta"; plan sampling shows brown 60S, medium green 160S, indigo 370S (legends.json was not edited here) | 15 reconciliation rows and their fixtures now cite the legend row number (of 55) and whether the row was the merge's kept or restored row. Quantities unchanged |
| 4 | +33.1% gauge gap includes the seam allowances | Right: gauge table alone 468.1 + 934.2 = 1,402.3 LBS (+16.9%); with 15%/10% seams 1,597.6 (+33.1%) | app-gaps row 2 and change 3; reading-guide trap 4 |
| 5 | "≤90 CFM → 12x12 face" contradicts 60S/80S | Right: M-301 vectors give 18 pt (1'-0") squares at both 65S, 36 pt (2'-0") at 80S, 160S, 240S, 370S; 60S measures ≈2'-0" on the render | F5, reading-guide §2 (new Face row), 463/464 notes, fixture 463, README material line |
| 6 | "35 counts exact" | Right: 42 counted rows (453–494) | Result line |
| 7 | "Nearest 100 lb" cannot be inferred | Right: 1,200.28 → 1,200 at 1, 10 or 100 lb | F2, 446 note, app-gaps rounding bullet |
| 8 | best-practices 1,380 LB and per-branch damper symbol | Right: (993.53 × 1.15 + 331.28 × 1.10) × 0.906 = 1,365.3; M-301 has 10 × "6" and 7 × "7" (13 hexagons after the grid bubble and keynote list) and no damper tag at the 22 supply devices | §9 → 1,365 (13.8%), §7 damper wording |
| 9 | "per-SF rate" wording | Right | F8 → "per-SF allowance convention" |

Line count after the fixes: 50 lines, 49 within 1% (42 counted, 5 measured, 2 derived), 1 allowance.
All 49 fixtures re-checked against their expected quantities.
