# 05: Rough carpentry (sheathing, blocking, backing, interior trim)

One real job: a single-storey bank branch. This folder works out how the estimator got each of the 20 rough-carpentry estimate lines (lines 81–97 and 145–147). It uses the PlanSwift markups, the drawings and the project manual. It covers **quantities and material descriptions only**.

| File | Contents |
|---|---|
| `README.md` | This page: scope, sources, materials, what was measured, scorecard |
| `formulas.md` | Every formula, with its inputs, the estimator's conventions and a worked example |
| `reconciliation.csv` | One row per estimate line: source, values, formula, recomputed value, Δ% |
| `fixtures.json` | 16 engine test cases (inputs, expected quantity, tolerance) |
| `reading-guide.md` | How to read the plans and specs for this trade: tags, strings, cross-checks, traps |
| `app-gaps.md` | The TakeoffSpeed quantity engine compared with this estimate, ranked by quantity impact |
| `best-practices.md` | Researched industry practice (already in the folder before this pass) |

## Scope: the 20 lines

| Line | Section | Item | Unit | Qty |
|---|---|---|---|---:|
| 81 | SHEATHING | 1/2" plywood at booth wall | SF | 47.7 |
| 82 | SHEATHING | 1/2" plywood at exterior wall | SF | 3,057.0775 |
| 83 | SHEATHING | 5/8" plywood at exterior wall | SF | 162.9919 |
| 84 | SHEATHING | 5/8" plywood at roof (canopy roofs, RT2) | SF | 285.0 |
| 85 | SHEATHING | 5/8" plywood at canopy ceiling | SF | 568.5 |
| 86 | SHEATHING | 3/4" plywood at booth ceiling | SF | 152.0 |
| 87 | SHEATHING | 3/4" fire-rated plywood backboard, IT room | SF | 215.33 |
| 88 | INTERIOR TRIM | Interior trim at opening, ASSUMED | LF | 910.0 |
| 89 | BLOCKING | 1x4 FRT blocking (A-700 to A-707) | LF | 240.66 |
| 90 | BLOCKING | 2x4 FRT blocking | LF | 10.0 |
| 91–96 | BLOCKING | Treated 2x4, 2x6, 2x16, 2x10, 2x14 and 1x6 blocking at the roof (A-140) | LF | 46 / 46 / 15 / 148 / 40 / 40 |
| 97 | BLOCKING | 2x6 blocking (A-200/A-201) | LF | 8.78 |
| 145–147 | FINISH CARPENTRY › BACKING | 1/2", 3/4" and 5/8" plywood backing | SF | 30 / 135 / 40 |

Related items that other trades carry: glass-mat sheathing at the parapets (09a, line 254), the booth-roof metal framing (09a, line 312), the countertop substrates "over 1"/1-1/2" plywood" and the 3/4" plywood under the backsplash (06 millwork, lines 130, 137–141), and the roof membranes (07).

## Driving sheets and markup pages

| Sheet | Markup page | Used for |
|---|---|---|
| A-120 Dimensional Floor Plan | p4 | Exterior wall runs by height: `EXT 8" STUD WALL @ 12'9"H` 89.7, `@ 15'9"H` 41.5, `@ 15'9"H NO GWB` 8.7, `@ 4'H` 13.0, `EXT 6" … @ 12'3"H SHTNG 10'3"H` 9.2, `PARAPET WALL @ 7'2"H A310` 5.9, and the wing walls `6" & 3-5/8" METAL STUD @ 18'8"H, BS 1/2" SHTNG ONLY` 8.4 FT |
| A-140 Roof Plan | p7 | Parapets `@ 1'7"H` 46.0, `@ 2'7"H` 38.0, `@ 4'7"H` 96.6; `RT2 ROOFING` 285.4 SF; nailer runs `COPING 6/A450` 148.1, `COPING 9/A450` 38.5, `COPING 3/A430` 13.9, `8/A450 LAP ROOF 2', INCL WALL` 45.3, `CURB - 1/A450` 39.9; general note 4 (P.T. 2x6 at every penetration) |
| A-450 Roof Details | p20 (no legend) | Nailer sizes: det. 6 "2X P.T. WOOD NAILER" (one 2x10), det. 9 a wide 2x plus "BRAKE METAL OVER 1X BLOCKING" (2x14 + 1x6), det. 8/10 "2x P.T. WOOD BLOCKING" (two members, 2x4 + 2x6), det. 1 "2 X 4 P.T. WOOD NAILER" at RTU curbs |
| A-430 Section Details | none | det. 3 wing-wall coping "P.T. WOOD BLOCKING" over the 1'-8" wall (2x16); det. 10/7 canopy edge "PLYWOOD DECK ON METAL FRAMING INFILL" and "EXTERIOR SHEATHING" |
| A-130 RCP | p5 | `ACM-3 … CANOPY - 10/A430` 358.7 SF (canopy soffit) |
| A-200 / A-201 Elevations | p11 / p12 | `5/8" PLYWOOD SHEATHING` 52.1 SF (a separate rectangle on p11); `2x6 BLOCKING` 8.8 FT (outline of the night-depository opening, p12) |
| A-310 / A-311 Wall sections | p14 / p15 (highlights only) | "1/2" EXTERIOR SHEATHING" on the 8" walls; A-311 sec. 1 highlights "5/8" EXTERIOR SHEATHING" on the brick knee wall below the storefront sill (2'-8"), and carries a measured F.F.E.-to-roof-deck wall height of 12'-8 1/4" (not a sheathing height) |
| A-700 to A-707 Casework sheets | p23–p30, p32 | `(n) 1x4 …BLOCKING` and `(n) 2x4 …BLOCKING` rows; plywood backing rows `3/4" PLYWOOD @ h`, `1/2" PLYWOOD @ 3'9"H`, `5/8" PLYWOOD BACKING`; booth (A-706) `WALL 706` 15.9 FT and booth roof 76.2 SF |
| E-702 Electrical Elevations | p49 | `3/4"THK. FIRE RATED PLYWOOD BACKBOARD` 215.3 SF |
| A-110 Floor Plan | p3 | Note F: all blocking FRT. Keynote P15: FRT plywood 8' tall on every IT/ELEC room wall. Legend `PLYWOOD @ 8'H` 32.5 FT (cross-check) |
| A-620 Partition Schedule | p1 highlight only | Note M: FRT blocking in partitions. Series E is "1-LAYER (PLY.WD)", i.e. "PL-1 OVER 1/2" PLYWOOD SHEATHING" |
| A-600 Door Schedule | p21 | Opening counts (the trim line is an assumption, not a measurement) |

## Specification sections (PDF page numbers of `source/specifications.pdf`)

| Section | Pages | What it fixes for quantities |
|---|---|---|
| 06 10 53 Miscellaneous Rough Carpentry | 122–127 | Scope covers blocking, nailers and plywood backing panels (p122). Preservative treatment is AWPA U1: UC2 interior, UC3b exterior, UC4a ground contact. It is required for "wood nailers, blocking, and similar members in connection with roofing, flashing" (p124). FRT means flame-spread ≤ 25 by ASTM E84, Interior Type A, applied to "Concealed blocking" and "Plywood backing panels" (p124–125). Dimension lumber is Construction or No. 2 grade, any species (p125). Equipment backing panels are PS 1 Exterior A-C FRT plywood, ≥ 3/4" unless indicated (p125). Fasteners are hot-dip zinc where treated (p126). Install FRT backing with the label visible (p127) |
| 06 16 00 Sheathing | 128–132 | Wall and parapet sheathing (p128). Plywood is DOC PS 1 Exterior sheathing, span rating ≥ 32/16, "Nominal Thickness: As indicated on Drawings" (p131). Parapet glass-mat (ASTM C1177) defaults to Type X 5/8" (p131; this sheathing is carried by 09a). Screws to metal framing are ASTM C954 (p131) |

The project manual has no finish-carpentry section, so nothing governs the 910 LF trim line.

## Material types and their specified properties

| Material (line) | Properties | Source |
|---|---|---|
| 1/2" plywood wall sheathing (82) | PS 1 Exterior, span rating 32/16, on 8"/6" cold-formed studs. The sections call it "1/2" EXTERIOR SHEATHING" | 06 16 00 p131; A-310/A-311/A-450 |
| 5/8" plywood (83, 84, 85, 147) | The RT2 roof type is "5/8" PLYWOOD" under tapered polyiso. A-311 sec. 1 calls the brick knee wall below the storefront sill (2'-8") "5/8" EXTERIOR SHEATHING". The canopy has a "PLYWOOD DECK ON METAL FRAMING INFILL". A-704 has 5/8" plywood in the tech-wall recess under Type X | A-140 roof types; A-311; A-430 det. 10; A-704 |
| 3/4" plywood (86, 146) | Booth top: "3/4" PLYWOOD FRAMING. PAINTED PT-5". Casework backing: "P-LAM OVER 3/4" PLYWOOD BACKING" | A-706; A-700–A-703 |
| 3/4" fire-rated plywood backboard (87) | 8' tall × length as required, mounted vertically on all NER/IT room walls, UL label visible. Spec: PS 1 A-C FRT ≥ 3/4" | E-702 keynote; A-110 P15; 06 10 53 p125 |
| 1x4 / 2x4 FRT blocking (89, 90) | FRT Interior Type A, Construction/No. 2 grade | A-110 note F; A-620 note M; 06 10 53 p125 |
| P.T. roof blocking (91–96) | AWPA UC3b (exterior, not in ground contact), Construction/No. 2 grade, sized to the wall build-up in each detail | 06 10 53 p124; A-450, A-430 |
| 2x6 blocking at the night depository (97) | Treatment not stated in the description | A-201 markup |
| 1/2" plywood backing (145) | Transaction-bar knee wall: plywood on both faces of the 2x4 framing (tile side under 1/4" cement backer; "PL-4 OVER 1/2" PLYWOOD BACKING @ INTERIOR SIDE") | A-700 |
| Interior trim (88) | Not specified | none |

## What the estimator measured, and in which units

- **Walls (LF × printed height).** The A-120 and A-140 wall runs are linear (FT) with the height in the legend name. Sheathing SF is Σ LF × height, with no deduction for openings. Storefront runs are measured through the glass at full height. The `SHTNG 10'3"H` suffix overrides the wall height, and `BS` (both sides) doubles the face count.
- **Areas (SF).** These are read straight from area legend rows: RT2 roof, E-702 backboard, A-702/A-703 plywood, A-704 backing, the booth roof.
- **Blocking (LF × rows).** A leading `(n)` in the legend name is the number of rows. LF is the traced run. The A-140 nailer runs are the coping, curb and roof-step LF, with the member size read from each detail.
- **Rounding.** The BACKING lines round up to the next 5 SF, which reproduces all three lines exactly (30, 135, 40). The A-140 nailers are rounded inconsistently: 45.3→46, 38.5→40, 13.9→15, 148.1→148. The other lines carry unrounded PlanSwift values (240.66, 215.33, 8.78, 3,057.0775).

## Scorecard

| Result | Lines |
|---|---|
| Reconciled within 1% with a source chain the drawings support | **10**: 82, 84, 86, 87, 89, 94, 97, 145, 146, 147 |
| Within 5% with a drawing-supported chain (measured run, estimator rounding) | 4: 91, 92 (−1.5%), 95, 96 (−3.75%) |
| Numeric match on a fitted factor only (unsourced) | 3: 81 (15.9 LF × 3'-0", a height printed nowhere), 83 (5/8" wall; knee-wall candidate 2'-8" with an implied 61.12 LF run, unresolved, Δ blank), 85 (canopy ceiling; 1.5 ft wrap is fitted, unresolved, Δ blank) |
| Rounding outlier | 1: 93 (13.9 → 15, −7.3% raw; ceil-to-5 reproduces it) |
| No reproducible source (allowance) | 2: 88 (trim, "ASSUMED"), 90 (2x4 FRT, 10 LF) |

So 14 of 20 lines reconcile from drawing-supported chains (within 5%), 3 more match numerically on a fitted factor, 2 are allowances and 1 is a rounding outlier. The open items are listed in `reconciliation.csv` notes and in `app-gaps.md`.

## Verification

A reviewer raised six issues. Each was re-checked against the source and recomputed in Python. Scratch files are in `trades/05-rough-carpentry/scripts/verify/`. The checking was done by Claude Opus 5.5, with GPT-6 Astra (via `tools/ask_gpt.py`) as a second reader of the rendered crops. All six issues were confirmed and fixed.

| Issue | What was checked | Result and change |
|---|---|---|
| Line 83: 5/8" wall chain | Markup p15 (A-311 sec. 1) rendered at 4×. The red arrows of the 12'-8 1/4" markup run from F.F.E. to the underside of the roof deck. The green "5/8" EXTERIOR SHEATHING" highlight sits in the brick knee-wall callout stack beside the 2'-8" SILL dimension. GPT-6 Astra read the crop the same way. 162.9919 / 2.6667 = 61.12 LF | **Confirmed.** The knee-wall chain (2'-8", implied 61.12 LF, nearest rows half rowlock 61.4 / rowlock sill 61.5 FT) is now the primary candidate. 52.1 SF is kept as a separate area of unknown location. The 52.1 + 8.7 × 12'-8 1/4" fit is dropped. recomputedQty and Δ are now blank. Changed in `reconciliation.csv`, `formulas.md` F1, the README material and sheet tables, and `reading-guide.md` §1 and trap 6 |
| Line 85: 1.5 ft canopy wrap | A-430 det. 10 rendered at 5×. 1'-0" = 1" + 10" + 1" is the edge depth, and the 6" is the ACM soffit profile. The only sheathing dimensioned is the two 5/8" decks. (568.5 − 358.7) / 138.5 = 1.515. GPT-6 Astra: the detail does not support a 1'-6" wrap. A brute-force search over A-1xx to A-4xx legend rows found no combination reaching 568.5 | **Confirmed.** The 1.5 ft factor is now described as fitted, not printed. The line is unresolved and Δ is blank. Changed in `reconciliation.csv`, `formulas.md` F2 and `reading-guide.md` §1 |
| Line 82 residual | Rounding bound Σ 0.05 × H × faces = 5.59 SF, below the 6.82 SF residual. The measured heights (4'-7 1/16", 1'-7 1/8", 15'-9 1/16") add 1.24 SF, giving 3,051.50 (−0.18%) | **Confirmed.** The note now says that about 1.2 SF of the residual is unexplained at printed heights, and it gives the measured-height variant. Changed in `reconciliation.csv`, `formulas.md` F1 and the `fixtures.json` note. The fixture's expected value and tolerance are unchanged |
| Lines 91/92: 46 LF source | A-140 legend: `PARAPET WALL @ 1'7"H` = 46.0 FT exactly. Markup p7 rendered at 6×: the olive 8/A450 run follows the high-low step line. A-450 det. 6 shows a single 2x10 nailer | **Confirmed.** The alternative and the reason it is rejected are recorded in the `reconciliation.csv` notes, in `formulas.md` F5 and in the `fixtures.json` notes. The step-wall attribution is kept |
| Line 86: two 3/4" layers | p29 legend rows: PT5 finish 76.2 SF and the metal-stud framing assembly 76.2 SF. The A-706 text prints "PLYWOOD SUBSTRATE" with no thickness | **Confirmed.** The wording is now "2 × 76.2 booth-roof area; second layer read as the ceiling-side substrate, thickness not printed". The line is still classed derived |
| Scorecard headline | Recount after the changes above | **Confirmed.** The headline is now 14 of 20 drawing-supported (within 5%), 3 fitted-factor matches (81, 83, 85), 2 allowances and 1 rounding outlier (93) |
