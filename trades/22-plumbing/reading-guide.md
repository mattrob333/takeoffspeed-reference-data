# 22 Plumbing: how to read the plans and specs

## 1. Sheet order

1. **P-101 Tables and schedules** first. It is the dictionary: every tag (WC, LAV, EDF, MS, SK-T,
   SK-U, FL, DB, WH, RH, RD, OD, CD, DSN, VB), the water heater (EWH), the circulation pump (CP), the
   cleanouts (FCO, WCO), the piping schedule (material, joints, hanger spacing by size), the
   pipe-materials table, and the insulation thickness table. Faucets are **sub-rows** under their
   fixture mark ("LAVATORY - (BATTERY) FAUCET", "WALL FAUCET", "LOUNGE FAUCET", "LIBRARY FAUCET").
   They are part of the fixture line, not separate counts.
2. **P-001** for abbreviations: B/G below grade, A/C above ceiling, VTR, FCO, NFWH, NFGH, ST storm,
   SAN, V, CW, HW, NG. Also general notes F (shut-offs on branches serving 2+ fixtures),
   G (undersized water lines are 1/2"), U (cleanout locations).
3. **P-301 sanitary foundation plan.** Below-grade sanitary ("3"ø SAN B/G", "4"ø SAN B/G"), storm
   leaders out of the building ("3" ST B/G REFER TO CIVIL…", "4" ST B/G…"), "3" ST UP"/"4" ST UP"
   risers, the 1-1/4" CW service stub ("1-1/4" CW B/G REFER TO CIVIL"), natural gas ("NG B/G REFER
   TO CIVIL", "1" NG UP TO A/C"), floor drains "3" FL", "4" DSN", "FCO", and "1 1/2" SAN" to "DW".
4. **P-302 domestic floor plan.** Water ("1 1/4"ø CW A/C", "1"ø CW A/C", "3/4"ø CW A/C",
   "1"ø HW A/C"), vents ("2"ø V A/C", "3"ø V A/C", "4" VTR"), storm leaders inside
   ("3" TO CD / 3" DN", "4" UP TO RD", "4" UP TO OD", "4" DN"), and every fixture tag. Keynotes 1–6
   drive the valves, filter, trap primer and valve box.
5. **P-303 roof plan.** "4" RD", "4" OD", seven "3" CD" with GPM and SQ FT tags, "4" ST" leaders,
   "1" GAS UP", "3/4" GAS", "3/4" CW DN" to "RH-1", and the condensate runs from the RTUs. Keynote 3
   sets the gas assembly at each RTU.
6. **P-402 isometric riser.** Counts FCO on the SAN/VENT riser and "NFWH" on the domestic riser.
   The fixture tags repeat here; do not count them again.
7. **P-403 gas iso.** Meter "BY GAS COMPANY", the per-RTU assembly (shut-off, drip leg, 2 test
   ports, regulator, union, flex connector), and the painting note (roof gas = safety yellow).
8. **P-501 details.** Detail 2: HWR isolation and balancing valve. Detail 8: condensate drain to
   rain leader, which is where the scheduled DB drain box goes (line 440). Also the water-heater
   piping (expansion tank, mixing valve, P&T relief, safety pan), the cleanout-to-grade pad
   (18"x18"x6"), the trap primer, and the valve box (Quench/Keurig).
9. **M-302** for the RTU count (2), which sets the gas shut-off count. The RTU condensate trap
   assembly belongs to Div 23.

## 2. How each formula input is read

| Input | Where | Actual strings on this job |
|---|---|---|
| Pipe size + system | Callout next to the run, holds until the next callout | `3"ø SAN B/G`, `4" ST B/G`, `1 1/4"ø CW A/C`, `1"ø HW A/C`, `2"ø V A/C`, `1" GAS UP`, `3/4" GAS`, `1" NG UP TO A/C` |
| Location | Sheet + suffix | P-301 = below grade (`B/G`), P-302 = above ceiling (`A/C`), P-303 = roof |
| Pipe length | Measured along the run at 1/4" = 1'-0" (all P-30x plans) | Legend FT per sheet |
| Vertical drops | `DN`, `UP`, `UP TO RD/OD`, `DN THRU WALL` points | Estimator drew them as off-plan segments of the same colour |
| Material | Spec 22 1000 + P-101 piping schedule (the plan never says) | Copper Type L above ground; Type K soft for 1/2" below slab; PVC Sch 40 below grade; hubless CI above; Sch 40 black steel gas |
| Fixture count | Tag text on P-302 | `WC` ×2, `LAV` ×2, `EWH`, `CP`, `SK-T`, `SK-U`, `MS`, `EDF`, `HB` ×2, `VB` |
| Drain count | P-303 roof, P-301 floor | `4" RD` ×2, `4" OD` ×2, `3" CD` ×7, `3" FL` ×3, `4" DSN` ×2 |
| Hydrants | P-402 `NFWH`, P-303 `RH-1`, P-302 keynote 2 "3/4" CW UP TO ROOF HYDRANT" | WH 1, RH 1 |
| Valves | Keynotes | P-302 keynote 3 (2 at EWH); P-303 keynote 3 (1 per RTU); P-501 detail 2 (1 HWR assembly) |
| Filter | P-302 keynote 5 | "WHIRLPOOL LARGE CAPACITY 10" X 4.5" … WHKF-DWHBB", 10-micron |
| Allowance area | G-001 / title block | "1,900 GSF" (estimator wrote 2000 SF) |

## 3. Cross-checks that hold on this job

- Text-layer tag counts on the counting sheet equal the legend counts for every tag: WC 2, LAV 2,
  CD 7, FL 3, RD 2, OD 2, DSN 2, HB 2 and the single items.
- Storm leaders: the 7 CD on P-303 feed **6** three-inch leaders. The two west CDs at grid C
  (4.86 GPM/37 SF and 4.68 GPM/36 SF) share one "DN THRU WALL" leader (keynote 2, canopy drainage
  to civil). Text counts agree: P-302 has 7 `3" TO CD` and 6 `3" DN`; P-301 has 6 `3" ST UP` and
  6 `3" ST B/G REFER TO CIVIL`. The 2 RD and 2 OD use 4" leaders (`4" RD`, `4" OD`; P-301 has 4
  `4" ST UP`): two continue as `4" ST B/G` to civil and two end as `4" DSN` emergency downspouts
  (P-301 keynote 1, "terminate emergency downspout 12" above finish curb"). So drains are not
  one-to-one with leaders; count drains from the drain tags, not from the leaders.
- Gas shut-offs = RTUs = 2 (M-302 legend RTU-1, RTU-2).
- Water-heater shut-offs = 2 × EWH (keynote 3).
- Roof gas paint (P-303 legend 53.9 FT) = 3/4" gas 44.2 + 1" gas 9.7.
- 1/2" Type K (15.3 FT) is the trap-primer tubing to the 3 FL (keynote 4). The cyan diagonals on
  p57 run from the CW main to each floor drain.
- P-101 schedules 2" waste connections (LAV, SK-T, SK-U, EDF), but there is no 2" sanitary line.
  P-301 keynote 3 ("ALL UNDERGROUND SANITARY LINES ARE TO BE NO LESS THAN 3" IN SIZE") explains it:
  those fixtures drop straight into the 3" B/G runs. The only sub-3" sanitary is the 1-1/2" to DW.

## 4. Traps hit on this job

1. **Same tag on three sheets.** WC, LAV, SK-T, SK-U, MS, EDF appear on P-301, P-302 and P-402.
   Summing per sheet triples the count (WC 6 instead of 2). Count on P-302 only. FCO is on P-301
   and P-402; count it once.
2. **Legend name differs from schedule mark.** "NON FREEZE GROUND HYDRANT" in the P-402 legend is
   the scheduled **WH** wall hydrant: the plan tag is NFWH, while NFGH is a different abbreviation.
   "RH-1" on the plan is schedule mark "RH". "FL" in the schedule is "FD" in the P-402 iso.
3. **DW is not DB.** P-302 "DW" is the dishwasher (Div 11 line 340, next to SK-T, fed by the
   1-1/2" SAN on P-301). The scheduled DB drain box has no plan tag. P-501 detail 8 shows what it is for
   (condensate drain to rain leader: drain box, secondary funnel, trap insert). The RTU condensate
   goes to the roof drains (M-302, P-303), so the one indoor source, FCU-1 (M-101 wall-mounted
   mini-split, IT room), is what discharges to it: 1 DB. Exact placement is still "coordinate with
   architect/GC".
4. **Vertical pipe is inside the plan legend.** The estimator drew the drops as extra segments. An
   app that measures plan runs and then adds risers from P-402 double counts the verticals.
5. **Locations are merged.** One estimate line per system and size, summed over B/G, A/C and roof
   (3" storm over 3 sheets). Roof gas versus below-grade gas is the only split.
6. **Material conflicts.** The P-101 "PIPE MATERIALS" table is primary/fallback: PEX-A for water
   above and below ground, Sch 40 PVC for waste, vent and condensate, cast iron for vent over 2";
   its note says that where those are not permitted by local code use Type L copper (above-ground
   water), Type K (below-ground water), Type M (waste/vent under 2"), cast iron (waste 2" and
   larger) and Sch 40 wrought iron (condensate). The P-101 piping schedule lists Type L hard copper
   for water and, for sanitary, hubless cast iron, DWV hard copper and "ALL / PVC SHED 40 DWV (sic) /
   solvent weld" (note 3: "pipe material may be used where permitted by AHJ"; general note K: no
   PVC in a return-air plenum). The spec says Type L/K copper water, PVC below grade, hubless CI
   above. So the open items are PEX-A vs copper for water and PVC vs cast iron for above-ground
   waste/vent. The estimate lines name a material only where the plan does ("TYPE K COPPER", from
   keynote 4). Flag the conflict; do not pick one silently.
7. **Size assumed.** Condensate size is not drawn; the estimator wrote "DIA ASSUMED".
8. **Truncated legend names.** PlanSwift cuts long names ("STANDARD FILTER SIMILAR TO "WHIRLPOOL
   L...", "18"x18"x6"THK. CONCRETE PAD FOR CLEAN O..."). Use the keynote text for the line.
9. **Items on Div 22 sheets that belong to other trades.** The cleanout pad (Div 03 line 29), the
   gas safety paint (Div 09 lines 306/307), the dishwasher (Div 11) and the RTU condensate assembly
   (Div 23 line 480).
10. **Scope the estimator absorbed in the allowance.** Expansion tank (P-101 WH note 2; P-501
    "AMTROL ST-5"), FloodStop leak detector (note 1), heat traps, drain pan, mixing valves under
    the LAVs, trap primer valves, the gas drip leg, test ports and regulators at each RTU (P-403),
    insulation, hangers. An app that emits these as lines will not match this estimate line for
    line. Report them as add-ons, not misses.
