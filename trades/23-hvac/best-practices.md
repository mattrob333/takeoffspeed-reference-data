# HVAC (Div 23): ductwork, devices, units, controls. Quantity-takeoff best practice

Scope: quantities and material types only. No pricing, labor or productivity.
Project evidence is from the reference job (single-storey bank branch, 1,900 SF) and is cited by file path, not URL.

## How to read the citations (read this first)

The web-search budget for this session was exhausted after zero searches ran (limit: 200 per turn, shared by all agents). I did not work around it. All web evidence below comes from direct page fetches of URLs I already knew, and most of those pages were thin on estimating detail. Every claim carries one of four tags:

- **[web]** a link I actually opened that supports the claim.
- **[job]** read from this job's drawings, specs, markups or estimate lines (file path given).
- **[GPT]** recalled by GPT-6 Astra (`tools/ask_gpt.py`, transcript `trades/23-hvac/scripts/research/hvac/gpt1.txt`) and **not verified by me**. It names a standard or table, but I could not open it. Treat as a lead, not a fact. Percent allowances tagged [GPT] were described by the model itself as estimating assumptions, not published figures.
- **UNSOURCED** no source found.

Pages that failed to give usable data: zzTakeoff has no HVAC trade page yet (https://www.zztakeoff.com/trades/hvac-takeoff-software returned "not available yet"). Procore's HVAC estimating page has no ductwork measurement rules (https://www.procore.com/library/hvac-estimating). ICC code pages returned 403/404. The ADC flexible-duct standard is a paid document, and its public page gives no support spacing, sag or bend radius (https://airductcouncil.org/technical-papers-standards/). SMACNA, Owens Corning, Johns Manville, Ruskin and CustomPartNet pages returned 404, 403, redirects or 429. **A follow-up session with search access should replace every [GPT] row with a linked primary source.**

---

## 1. What the estimator takes off, and in which units

| Item class | Unit | Notes |
|---|---|---|
| Rectangular sheet-metal duct, by size, gauge, pressure class | LF by size, then converted to SF of surface, then to LB by gauge weight | Surface SF = 2(W+H)/12 x L. Weight = SF x lb/SF of the gauge. Sections 3.1 and 4. |
| Round / spiral duct, by diameter and gauge | LF, then SF = pi x D/12 x L, then LB | Rectangular and round are separate items because the spec sets different gauges (job: 26 ga rectangular, 26 ga up to 14" round, 24 ga for 15"-26" round; M-001 notes, `text/M-001.txt` lines 280-288). |
| Fittings (elbows, transitions, taps, offsets) | Either individually developed SF/LB, or a percentage on straight-duct weight, or an allowance (LS) | See 3.3. The reference estimate carries fittings as one allowance line, not counted pieces [job] (`reference/estimate/lines.json` line 445). |
| Flexible duct, by diameter | LF | Spec limits the installed length per run (8'-0" on low-pressure supply runouts, job spec p426-427). |
| Duct insulation (external wrap) or duct liner (internal) | SF of duct surface, by thickness | Job: wrap 2.2" thick, installed R >= 6.0, FSK-L jacket; liner 1" thick, 1.5 lb density (job spec p414). Duct insulation is also a separate takeoff item in the reference estimate (line 447). |
| Air devices (diffusers, grilles, registers, linear slot) | EA by tag/type, size, neck size, CFM | Count by schedule row and verify against the plan symbols. Linear slot diffusers are counted per run and carry slot length in the tag, for example `LSD (2-48")` [job, M-301]. |
| Dampers: manual volume, control, remote-cable, fire, smoke, combination, backdraft | EA by type and size | Fire and smoke dampers get access doors and sleeves (section 7). |
| Rooftop units, split systems, exhaust fans, hoods | EA by tag | Each tag is one count, with its scheduled model, CFM, capacity, voltage and weight [job, M-101/M-302]. |
| Refrigerant piping | LF, by size and type if given | Reference job has 30.86 LF "size not given" [job, line 452]; that is the whole PlanSwift trace (both drawn pipes plus an extra 8 ft leg), not the 11.75 ft route. |
| Condensate drains, traps | EA | 1-1/2" RTU condensate drain with P-trap and removable vented cap [job, line 480]. |
| Controls: thermostats, temperature / CO2 / VOC / OA sensors | EA | 17 sensor/thermostat items in this job [job, lines 481-487]. |
| Test and balance | LS or per-device | Spec requires AABC-style total system balance [job, M-001.txt line 486]. |

A takeoff records every product and supply the job needs, and the estimator checks whether ducts, fittings and electrical supply are standard items or must be ordered or fabricated [web: Procore](https://www.procore.com/library/hvac-estimating).

Typical duct stock lengths that drive joint, hanger and cleat counts [web]:
- Rectangular galvanized duct comes in 4 ft sections.
- Round spiral duct stock is usually 10 ft joints. Non-spiral residential joints are 5 ft.
- Flexible duct ships in boxes of 25 ft compressed to 5 ft, in 4-18 inch diameters, with 6-12 inch most common.
- Source: [Wikipedia, Duct (HVAC)](https://en.wikipedia.org/wiki/Duct_(HVAC)).

## 2. Sheets and spec sections that drive it

**Generic:** mechanical notes and legend, equipment schedules (RTU, split system, fans, diffusers/grilles), ventilation schedule, ceiling-level duct plan, roof plan with units, duct sections/isometrics, details, and control diagrams. The architectural reflected ceiling plan and the structural roof framing govern clearances and curb locations. Plumbing owns the condensate drain beyond the unit. Electrical owns power to the units; the HVAC trade counts the units and controls only.

**This job** [job, `reference/sheets/index.json`]:

| Need | Sheet |
|---|---|
| General notes, abbreviations, embedded specification text (duct gauges, hangers, sealing, controls, balancing) | M-001, M-002 |
| Equipment and diffuser/grille schedules (tag, model, CFM, neck size, electrical, weight) | M-101 |
| Ventilation schedule | M-102 |
| Ductwork, devices, dampers, sensors (proposed ceiling plan) | M-301 |
| Rooftop units, exhaust hood, condensate drain | M-302 |
| Isometric and duct sections | M-401, M-402 |
| Details and controls | M-501, M-502, M-503 |
| Full specs | Spec pages 395-440: 23 05 00 (p395), 23 05 93 test/adjust/balance (p410), 23 07 13 duct insulation (p414), 23 23 00 (p417), 23 31 00 ductwork (p423), 23 74 00 packaged RTUs (p429), 23 37 13 diffusers/grilles (p434) (`reference/sheets/spec_index.json`) |

Spec sections that set material types in this job's specs [job]:
- Ducts follow the SMACNA 2005 (3rd ed.) HVAC Duct Construction Standards, and where SMACNA offers a choice of gauge or support the heavier one governs (spec p423).
- Low-pressure ductwork is the "standard 1 inch WC at 2500 FPM, Class C seals" class; medium-pressure is 3 inch WC at 4000 FPM, Class A seals (spec p424).
- The mechanical notes require SMACNA seal Class A (M-001.txt line 420), which conflicts with the Class C low-pressure definition in the spec. An AI should carry the stricter one and flag the conflict.

## 3. Measurement rules

### 3.1 Straight duct

- Rectangular: perimeter x length. Round: circumference x length. Length is measured on the duct centerline along the plan route, from the plan scale or the drawn run, not by counting the number of pieces. The formulas are plain geometry [GPT, not a published rule].
- Take off by size and by gauge change. A single run that crosses a gauge threshold (job: round duct changes from 26 ga to 24 ga above 14 inch diameter, M-001.txt lines 287-288) is split into two items.
- Flexible duct is measured in LF per diameter, and the spec length limit applies per connection: 8'-0" low-pressure, 4'-0" medium/high-pressure supply runouts (job spec p426-427). A flexible run drawn longer than the limit is a drawing error to flag, not to quantity silently.
- ADC FAQ: flexible connectors are limited to "installation lengths not over 14 feet", and 14-foot sections may not be spliced to exceed it; UL-listed air ducts have no length limit [web: ADC FAQ](https://airductcouncil.org/frequently-asked-technical-questions/). Spec limits are tighter and win.
- ADC FAQ: flexible duct is generally sized one inch larger in diameter than the equivalent round sheet-metal duct [web: ADC FAQ](https://airductcouncil.org/frequently-asked-technical-questions/). This matters when converting a sized rigid run to a flex diameter.

### 3.2 What to deduct and what not to

No source I could open states a deduction rule for ducts. These are practices the reference estimate shows:
- **Do not deduct** the length occupied by dampers, fittings or devices from straight duct [job: the reference LF totals are the raw marked run lengths, and the weight is computed on them].
- **Do not double count** flex duct: it is its own line with its own diameter [job, lines 448-451], and it is not in the sheet-metal weight (see section 9).
- Round and rectangular runs under the same plan symbol are different items.

### 3.3 Fittings

Three conventions exist; the estimate must say which one it used:
1. **Individually developed:** every elbow, transition and tap is measured and its surface is developed. Transitions use the developed slant surface, not perimeter x axial length [GPT].
2. **Percentage allowance on straight duct:** a preliminary-estimate allowance of 10-25% of straight-duct sheet area is the figure [GPT, described by the model as an estimating assumption with no published basis]. The TakeoffSpeed engine uses 15% ("estimator practice") and notes the reviewed human estimate used 0% [job: `TakeoffSpeed repo: docs/QUANTITY_ENGINE.md` line 104].
3. **Lump-sum allowance** with no piece count. This is what the reference estimate does (line 445, "ALLOWANCE PROVIDED FOR FITTINGS", 2,000 SF area).

Spec: "install factory fabricated fittings for changes in direction, size, and shape and for branch connections" (M-001.txt line 421); medium-pressure branches use radiused or 45-degree take-offs, and straight taps are not accepted (job spec p426). A takeoff that lists spin-in fittings, splitter dampers and radius taps follows from that.

### 3.4 Openings, corners, laps, heights, slopes

- **Heights:** ceiling-level duct is measured on plan; a duct that rises ("DUCT UP" notes on M-301) needs the rise from the section or isometric, not the plan scale. Penetrations through walls and roof carry their own sleeves, curb or flashing and firestopping (M-001.txt lines 405-409).
- **Insulation laps:** the spec says insulation is "cut slightly longer than circumference of duct to ensure full thickness at corners" and all joints are sealed with 2-inch-wide SMACNA tape (job spec p415). The TakeoffSpeed engine exposes `hvac.wrap-lap-in` for this [job: `lib/quantities/trades/mep/hvac.ts` line 40]. The reference estimate applies no lap (section 9).
- **Liner:** liner is not installed within 6 inches of a damper, and lined straight runs are counted separately from lined elbows (job spec p415). A liner takeoff must therefore remove 6 inches at each damper.
- **Clear-air dimensions:** lined ducts are drawn to the clear air dimension, so sheet-metal dimensions are the clear size plus twice the liner thickness [GPT; unverified]. Check whether the drawn size is clear or sheet-metal.
- **Slope:** condensate and exhaust ducts may be pitched; slope does not change the takeoff length by a meaningful amount at HVAC pitches, but the drain location and trap depth do change fitting counts [UNSOURCED].

## 4. Coverage, yield and weight factors

| Factor | Value | Basis |
|---|---|---|
| Galvanized sheet weight, lb/SF: 28 ga 0.781; 26 ga 0.906; 24 ga 1.156; 22 ga 1.406; 20 ga 1.656; 18 ga 2.156; 16 ga 2.656 | as listed | **[GPT]**, attributed to the CustomPartNet sheet-metal gauge chart, which I could not open (HTTP 429). Not checked against SMACNA or ASHRAE. |
| 26 ga check against this job | 1,200 lb / 1,324.81 SF = 0.9058 lb/SF | [job, reconstruction in section 9]. The reference estimate uses 0.906 lb/SF, which independently matches the GPT table value. |
| Galvanized sheet thickness, in: 28 ga 0.0187; 26 ga 0.0217; 24 ga 0.0276; 22 ga 0.0336; 20 ga 0.0396; 18 ga 0.0516 | as listed | [web: Wikipedia, Sheet metal](https://en.wikipedia.org/wiki/Sheet_metal). This page gives thickness only, no weight. |
| Manufacturers' Standard Gauge steel density | 41.82 lb per SF per inch thick | [web: Wikipedia, Sheet metal](https://en.wikipedia.org/wiki/Sheet_metal). Weight = 41.82 x thickness is the check, but it applies to the plain steel gauge, not galvanized thickness, so it will not match the table exactly. |
| Rectangular duct stock length | 4 ft | [web: Wikipedia, Duct (HVAC)](https://en.wikipedia.org/wiki/Duct_(HVAC)) |
| Round spiral duct stock length | 10 ft | [web: same](https://en.wikipedia.org/wiki/Duct_(HVAC)) |
| Flexible duct package | 25 ft compressed to 5 ft | [web: same](https://en.wikipedia.org/wiki/Duct_(HVAC)) |
| Sheet-metal scrap/waste | 5-10% on net developed sheet | [GPT, described as an assumption; no published figure] |
| Duct liner waste | 10-15% | [GPT, assumption] |
| External wrap waste | 5-10% | [GPT, assumption] |
| Insulation compression | 25% compression applies to installed R-value, not to SF | [GPT]. Do not add 25% to SF. |
| Duct hanger max spacing, rigid duct | 10 ft (IMC 603.10 prescriptive) | **[GPT]**, unverified (ICC pages blocked). SMACNA Chapter 5 and Tables 5-1 / 5-2 select the strap and rod size; the job spec cites those tables (M-001.txt lines 310-313) and also requires "hangers and supports within 24" of each elbow and within 48" of each branch intersection" (M-001.txt line 425) [job]. |
| Flex duct support spacing | 5 ft max horizontal, 1.5 in minimum strap width, 0.5 in max sag per foot, 6 ft vertical | **[GPT]**. Only the 1.5-inch strap width is confirmed: "In no case will the material contacting the duct or connector be less than 1-1/2 inches wide" [web: ADC FAQ](https://airductcouncil.org/frequently-asked-technical-questions/). The 5 ft, sag and 6 ft values are unverified. |
| Mastic gallons | coated SF x wet-film mils / 1,604 | [GPT]. Arithmetic identity for theoretical coverage (1 gal = 1,604 SF at 1 mil). Use the manufacturer's coverage in practice. |

**Where waste belongs.** Do not add a percentage to a quantity that is already a net measured surface and call it the purchase quantity unless the estimate lists purchase and installed quantities separately. The reference estimate carries net quantities with zero waste on sheet metal and insulation (section 9).

## 5. Material breakdown an estimator lists

For each system, primary items and the components that follow from them:

1. **Rectangular duct:** galvanized sheet (LB by gauge), plus joints/connectors (TDC/TDF or slip and drive cleats by section length), reinforcement as required by pressure class, sealant per the seal class, turning vanes in radius-less elbows (spec: mitered with double-thickness vanes in low pressure, no vanes in lined returns, job spec p423), hangers (strap or rod and trapeze; cadmium-plated rod, M-001.txt line 309), access doors where required.
2. **Round/spiral duct:** coupling/slip joint per section, tap and fittings, hangers (strap, M-001 line 310 refers to SMACNA round-duct hanger Table 5-2).
3. **Flexible duct:** duct by diameter, collars or spin-in fittings with integral scoop and volume damper (low-pressure only; job spec p427), draw bands/clamps at both ends, support straps, mastic at collars. The TakeoffSpeed engine derives straps and collars per connection [job: `hvac.ts` lines 281-282].
4. **Insulation and liner:** wrap by thickness and density, with pins and speed clips on ducts 18 in wide or more (job spec p415), tape (2 in wide SMACNA tape on all joints), adhesive; liner with adhesive, weld pins, speed washers and metal nosings (job spec p415).
5. **Dampers and fire protection:** volume dampers (single-blade up to 12 in round or 12x12; multi-blade larger), fire dampers (UL, 1-1/2 or 3 hour, 160 F links), smoke dampers (Class 1 low leakage), combination fire/smoke dampers, backdraft dampers, an access door at each fire and smoke damper (job spec p425-427). Fire damper function: the fusible link melts at a temperature above ambient; an annular clearance outside the listing is a deficiency [web: Wikipedia, Fire damper](https://en.wikipedia.org/wiki/Fire_damper). Combination dampers are one assembly, not two [GPT].
6. **Terminal devices:** diffusers, grilles, linear slot diffusers by length and number of slots, with neck sizes. Boots or plenum boxes are part of the device only if the schedule says so.
7. **Rooftop units:** each tag is one unit. Components that follow from a unit: roof curb, disconnect, economizer, condensate trap and drain, thermostat or space sensor, filters (the job schedule specifies MERV 13) [job, lines 477-478; accessory list is GPT-recalled and unverified]. Rooftop units are also called packaged units and need a weatherproof lid and sealing around joints [web: Wikipedia, Rooftop unit](https://en.wikipedia.org/wiki/Rooftop_unit). That page does not cover curbs, economizers or disconnects, so rely on the job schedule for accessories.
8. **Split systems:** one indoor unit plus one outdoor unit per tag, refrigerant line set (LF), condensate drain, condenser pad or stand, controller [job, line 479].
9. **Exhaust fans:** fan by tag, with curb or roof cap, backdraft damper, duct run, and wall or roof termination. This job lists three fans (EF-1 to EF-3, 55-80 CFM) and an exhaust hood.
10. **Controls:** thermostat, supply-air, return-air, OA and space temperature sensors, CO2 and VOC sensors, remote-cable-operated dampers, low-voltage wiring in the spec's wire type (22-14 AWG stranded, M-001.txt lines 369-377). Control points are typed as analog or digital, input or output [web: Wikipedia, Building automation](https://en.wikipedia.org/wiki/Building_automation). One AI per analog measurement, one AO per modulating command, one DI per status and one DO per binary command is the counting convention [GPT; the source it names, ANSI/ASHRAE 135 Clause 12, defines BACnet objects, not mandatory point counts].
11. **Testing, balancing, startup:** the spec requires a balance agency [job, M-001.txt lines 481-486]. Treat it as an LS or per-system item.

VAV-box jobs would add a box per zone, reheat coil if scheduled, airflow sensor and actuator [web: Wikipedia, Variable air volume](https://en.wikipedia.org/wiki/Variable_air_volume). This job has no VAV boxes.

## 6. Insulation, liner and sealing: what the specs here say

All from the job's spec (pages 414-415, 423-424), because I found no linked estimating guide:
- Duct liner is required throughout return air, transfer ducts and plenums, and on some supply runs for a specified distance.
- All unlined supply duct is insulated. All outside air duct is insulated. Conditioned ducts in ventilated-only spaces (penthouses) are insulated.
- Insulation is 2.2 in thick, installed R >= 6.0.
- Seams: Class C for low pressure, Class A for medium pressure and for exhaust (M-001 line 420).
- Test pressure and leakage classes are not defined in the sources I could open [web: Wikipedia, Duct leakage testing](https://en.wikipedia.org/wiki/Duct_leakage_testing) says only that commercial ductwork is tested to SMACNA standards and rated).

## 7. Counting rules for devices, dampers and equipment

- **Devices:** count by schedule row, not by plan symbol alone, because identical symbols can have different CFM and neck sizes. In this job, 24x24 diffusers with 6", 8", 10" and 12" necks are separate lines at different CFM [job, lines 462-467].
- **Dampers:** the reference job counts 13 remote-cable-operated dampers, 1 wax-controlled and 1 manual damper [job, lines 489-491]. The legend names them; the keynote hexagons 6 and 7 on M-301 mark where remote-cable dampers are required (8 + 5 = 13). Count the hexagons, not the 22 supply devices; M-301 has no per-branch damper symbol.
- **Fire and smoke dampers:** one per protected opening, access door at each (job spec p427); a combination fire/smoke damper is one assembly [GPT].
- **Units:** count the tag once per unit, and take the model from the schedule, not the plan label.
- **Sensors:** the reference estimate carries 17 sensor and thermostat items across M-301/M-302: 2 supply-air, 2 return-air, 2 CO2, 1 VOC, 4 temperature, 2 outdoor-air, 4 thermostats [job, lines 481-487].

## 8. Common mistakes and how to check a takeoff

| Mistake | Check |
|---|---|
| Counting duct by plan length when the duct rises or drops | Cross-check against M-401 / M-402 section and isometric views. |
| Using one gauge for all duct | Read the spec gauge table; round duct changes gauge at 14/15 inch in this job. |
| Mixing rectangular and round in the same weight line | Separate line per shape and size. |
| Counting flex duct in sheet-metal weight | Flex has its own LF line. |
| Applying a fitting percentage on top of individually measured fittings | One convention per job; state it. |
| Double-applying a waste factor on both duct and insulation | Insulation SF is net duct surface; apply waste once, at purchase. |
| Missing items the spec requires but the plan does not draw (access doors at fire dampers, hangers, sealant, test and balance, condensate trap, pins and clips) | Walk the spec "Products" and "Execution" lists against the takeoff. |
| Class A vs Class C conflict between notes and spec | Flag it; carry the stricter. |
| Counting devices by symbol without reading the schedule | Match every device tag to a schedule row and its neck size. |
| Skipping equipment accessories (curb, disconnect) because the electrical or roofing trade may own them | Decide ownership once per job and list it in the exclusions. |

Checks that are numeric and can be run in code:
- Sum of LF by size from the marked runs should equal the total on the plan.
- Duct SF = sum of perimeter x LF; LB = SF x gauge weight; insulation SF should be >= duct SF when external wrap is specified on every duct.
- Device count on the plan = device count on the schedule.
- Schedule CFM at each diffuser should add up to roughly the RTU CFM (job: RTU-1 and RTU-2 are 1,600 CFM each [job, lines 477-478]).

## 9. Reverse-engineering the reference estimate [job]

The reference estimate's Division 23 section has 50 lines. Verified by recomputation (`trades/23-hvac/scripts/research/hvac/` scratch, python):

| Item | Reference value | Reconstruction |
|---|---|---|
| Sheet-metal duct | 1,200 LB, one line, 26 gauge | Rectangular runs from M-301 markups (8x10 31.1 ft, 14x12 7.3, 20x12 94.4, 24x12 13.3, 16x12 41.4, 10x10 7.4, 8x8 10.6, 12x12 9.8 = 215.3 LF) give 993.53 SF; round runs (6" 18.0, 8" 113.7, 10" 10.5, 14" 10.2 = 152.4 LF) give 331.28 SF. Total 1,324.81 SF x 0.906 lb/SF = **1,200.28 LB**, which rounds to the 1,200 on the estimate. |
| Duct insulation | 1,325 SF, 1.5" fiberglass | Equals the 1,324.81 SF duct surface, rounded. So **insulation = bare duct surface, with no lap, no waste, no fittings, and covering every duct including round**. Note the thickness differs from the spec's 2.2 in wrap. |
| Fittings | 1 LS allowance | No fitting pieces counted. |
| Round duct gauge | same 0.906 lb/SF as rectangular | The estimate priced all duct at 26 ga, although the spec calls 24 ga for 15-26 inch round. No round duct on this job exceeds 14 inch, so there is no conflict. |
| Flexible duct | 6" 6.92 LF, 8" 50.09, 10" 4.83, 14" 3.12 = 64.96 LF | Taken straight from the markups, outside the 1,200 LB. |
| Air devices | 30 EA across 21 lines | One line per tag/CFM/neck combination. |
| Dampers, sensors, hoods, units, fans | counted per legend | See section 7. |

Not in the estimate at all: hangers, rod, strap, sealant, tape, mastic, flex collars/straps, turning vanes, access doors, curb, disconnect, balance. The TakeoffSpeed engine's seam/joint allowances (15% on rectangular, 10% on round) would give 1,365 LB against the estimate's 1,200 LB, so the engine and the reference differ by 13.8% on the duct line unless both conventions are set to 0 [job: engine doc line 104].

## 10. What an AI takeoff must read from the drawings and specs

1. **Schedules (M-101, M-102):** tag, model, CFM, neck size, electrical, weight, filter, capacity. Never infer these from plan symbols.
2. **Plan (M-301, M-302):** every duct run with its size label (`20"x12"`, `8"ø`), every flex run, every device with its CFM label, every damper symbol, every sensor and thermostat, every unit tag, rise notes ("DUCT UP"), and wall or roof penetrations.
3. **Legend (M-002):** what each damper, sensor and duct symbol means. Different symbols for remote-cable, wax-controlled and manual dampers decide the line item.
4. **Notes and spec (M-001, spec 23 05 00-23 74 00):** duct gauge by shape and diameter, pressure class and seal class, which ducts are lined or wrapped and the thickness, hanger rules, flex length limit, fire damper access, balance requirement.
5. **Details (M-501 to M-503):** curb, hood, condensate trap, damper, controls wiring, sensor mounting.
6. **Conflicts and gaps:** record every place where notes and spec disagree (seal class), where a size is missing (refrigerant pipe "size not given"), or where a drawn flex run exceeds the spec's limit.
7. **Output discipline:** quantities stay `unknown` rather than `0` where the drawings do not give a value (CLAUDE.md rule 1). Report the convention used for fittings, waste and insulation laps next to every duct line.

## 11. Open gaps for a follow-up pass

- Replace every [GPT] row with a linked primary source: SMACNA HVAC Duct Construction Standards (hanger Tables 5-1 and 5-2, Table 1-2 seal classes), IMC 603.10 and 607, ADC installation standard support spacing, ASHRAE gauge-weight table, Owens Corning / Johns Manville duct wrap and liner installation data, a damper manufacturer's installation guide.
- Find a linked estimating text that gives a fitting-to-straight-duct ratio and sheet-metal scrap allowance (RSMeans or SMACNA/MCAA estimating references). I have none.
- A published controls points-list convention for packaged RTUs.
- Compare what the engine's `hvac.ts` computes for this job against section 9 once flags and conventions are set to match (do not edit the engine).
