# 22 Plumbing: formulas

All numbers below were computed with Python (`trades/22-plumbing/scripts/recon.py`) from
`reference/markups/legends.json` and `reference/estimate/lines.json`. Plumbing has no ratios,
waste factors or derived lines. Every quantity is a measured length or a count, so each formula
is an aggregation rule. The rules that decide whether you reproduce the estimate are the
aggregation conventions: what gets summed, what gets counted once, and what goes to the allowance.

---

## F1. Pipe length by system and size

- **Name:** `plumbing.pipe-lf`
- **Inputs:** `legendLF[sheet]` (FT, one value per markup sheet where the item is drawn),
  for one system (storm / sanitary / vent / CW / HW / condensate / gas) and one nominal size.
- **Rule:** `LF = Σ_sheets legendLF[sheet]`. Net, with **no waste**. **No separate risers**:
  vertical drops are drawn on the plan as segments and are already inside the legend value.
  **No location split**: a size and system that appears below grade, above ceiling and on the
  roof is still one line.
- **Conventions (estimator's own, from this job):**
  1. Vertical drops are drawn as off-plan line segments of the same item (visible on p57
     above the north wall). The legend total is horizontal + vertical.
  2. Sheets are summed across locations. 3" storm: P-301 below grade + P-302 interior leaders +
     P-303 roof. 3/4" CW: P-302 + P-303 (to RH-1). 1-1/4" CW: P-301 B/G stub + P-302.
  3. Gas is the exception: estimator kept "1" NATURAL GAS PIPE" (P-301, below grade / up the
     wall, line 419) separate from "1" GAS PIPE" (P-303, roof, line 418). These are two legend
     names on two sheets, so they are two lines.
  4. Precision: the estimate keeps PlanSwift's internal 2 decimals. The legend shows 1 decimal,
     so tolerance is ±0.05 LF × number of legend rows. `fixtures.json` carries this as
     `toleranceLF` (0.15 for 404/405, 0.10 for 412/415, 0.05 otherwise). Its `tolerancePct`
     (the field the fixture schema requires) is derived from the same rule, as a percentage of the
     expected estimate quantity: `max(0.5, ceil₂(100 × toleranceLF / expected))`, where ceil₂ rounds
     up to 2 decimals. That gives 1.41 for 406 (0.05 / 3.55 = 1.408%) and 0.52 for 418
     (0.05 / 9.71 = 0.515%); every other LF case is 0.5. Counts are exact (0).
- **Worked examples:**

| Line | Inputs (FT) | LF | Estimate | Δ% |
|---|---|---|---|---|
| 404 3" storm | P-301 33.5 + P-302 25.8 + P-303 91.2 | 150.5 | 150.59 | −0.06 |
| 405 4" storm | P-301 12.7 + P-302 103.7 + P-303 56.3 | 172.7 | 172.70 | 0.00 |
| 406 1-1/2" san | P-301 3.6 | 3.6 | 3.55 | +1.41 (display rounding) |
| 407 3" san | P-301 86.7 | 86.7 | 86.73 | −0.03 |
| 408 4" san | P-301 21.9 | 21.9 | 21.94 | −0.18 |
| 409 2" vent | P-302 58.2 | 58.2 | 58.18 | +0.03 |
| 410 3" vent | P-302 12.8 | 12.8 | 12.78 | +0.16 |
| 411 4" vent | P-302 47.3 | 47.3 | 47.29 | +0.02 |
| 412 1-1/4" CW | P-301 2.0 + P-302 62.5 | 64.5 | 64.58 | −0.12 |
| 413 1/2" CW Type K | P-302 15.3 | 15.3 | 15.34 | −0.26 |
| 414 1" CW | P-302 45.5 | 45.5 | 45.52 | −0.04 |
| 415 3/4" CW | P-302 39.8 + P-303 4.7 | 44.5 | 44.44 | +0.14 |
| 416 1" HW | P-302 162.2 | 162.2 | 162.22 | −0.01 |
| 417 1-1/2" condensate | P-303 34.5 | 34.5 | 34.52 | −0.06 |
| 418 1" gas (roof) | P-303 9.7 | 9.7 | 9.71 | −0.10 |
| 419 1" natural gas | P-301 18.6 | 18.6 | 18.60 | 0.00 |
| 420 3/4" gas (roof) | P-303 44.2 | 44.2 | 44.21 | −0.02 |

Total plumbing pipe on this job: 992.90 LF over 17 lines.

## F2. Size assumed

- **Name:** `plumbing.pipe-size-assumed`
- **Inputs:** a drawn run with no size callout (P-303 condensate from RTU-1/RTU-2).
- **Rule:** carry the run under an assumed size and print "DIA ASSUMED" on the line (line 417).
  Basis here: M-302 legend "1-1/2" RTU CONDENSATE DRAIN W/ P-TRAP & REMOVEABLE VENTED CAP".
  The quantity rule is still F1.
- **Example:** 34.5 FT → 34.52 LF "1-1/2"DIA CONDENSATE DRAIN PIPE, DIA ASSUMED".

## F3. Fixture / device count by tag

- **Name:** `plumbing.count-by-tag`
- **Inputs:** `legendEA` for the tag on the one sheet where it was counted.
- **Rule:** `EA = legend count`. The same tag on several sheets is counted **once**: P-302 for
  fixtures, P-402 for FCO and NFWH, P-303 for roof items, P-301 for FL. Faucet and trim sub-rows of
  a schedule mark share the fixture's line and get no count of their own.
- **Cross-check rule:** placements of the tag text on the counting sheet should equal the count
  (computed from the text layers: WC 2, LAV 2, EWH 1, CP 1, SK-T 1, SK-U 1, MS 1, EDF 1, HB 2, VB 1 on
  P-302; "3" CD" 7 and RD 2 / OD 2 on P-303; "3" FL" 3 and "4" DSN" 2 on P-301).
- **Examples:** 424 LAV = 2; 428 WC = 2; 432 CD = 7; 433 FL = 3; 434 OD = 2; 435 RD = 2;
  421/422/423/425/426/427 = 1 each; 436 FCO = 1 (P-402); 437 HB = 2; 438 DSN = 2; 439 VB = 1;
  429 WH = 1 (P-402 "NFWH", legend "NON FREEZE GROUND HYDRANT"); 430 RH = 1 (P-303 "RH-1");
  431 filter = 1 (P-302 keynote 5); 444 gas meter = 1 (P-403).

## F4. Valves counted from keynotes and details

- **Name:** `plumbing.valve-by-keynote`
- **Inputs:** the keynote's rule and the count of the item it applies to.
- **Rule:** `EA = Σ (items the keynote applies to × valves per item)`. The estimator placed one
  count mark per valve on the plan, and the legend count equals this product.
- **Examples:**
  - 442 shut-off valve = 1 EWH × 2 (P-302 keynote 3: "on input and output of water heater") = **2**.
  - 443 manual gas shut-off = 2 RTU (M-302: RTU-1, RTU-2) × 1 (P-303 keynote 3 / P-403 note 1:
    "at each RTU") = **2**.
  - 441 isolation & balancing valve = 1 HW recirculation line × 1 assembly (P-501 detail 2
    "HWR ISOLATION VALVE AND BALANCING VALVE"; P-101 pump note 2) = **1**.

## F5. Scheduled item with no plan tag, placed by a detail

- **Name:** `plumbing.scheduled-by-detail`
- **Inputs:** a schedule mark (P-101 "DB DRAIN BOX, SIOUX CHIEF MODEL #696-3F", with #696-LC louvered
  cover, #696-CF secondary drainage funnel and JR Smith trap seal insert, "pipe indirect in wall to
  drain box", 2" waste) that has no tag on any plan, and the detail that shows where it is used:
  P-501 detail 8 "CONDENSATE DRAIN TO RAIN LEADER DETAIL" (drain box with secondary funnel, insulated
  P-trap "provide w/ trap insert", discharging to the rain leader).
- **Rule:** `EA = 1 per scheduled mark = 1 per indoor condensate source piped indirect to a rain
  leader`. On this job that is FCU-1 alone (M-101 mini-split, wall-mounted Mitsubishi PKA-A12LNL in
  the Electrical/IT room). This is an inference, not a drawn connection. Estimate line 440
  carries the drawing reference "P101 - P501". Exact placement is "coordinate exact location with architect and GC" (P-101), so flag the location,
  not the count.
- **Not the source:** P-302 "DW" (1 EA) is the dishwasher (Div 11 line 340, "DISHWASHER - AE-04",
  next to SK-T; P-301 runs a 1-1/2" SAN branch to it). It is not the drain box. GPT-6 Astra, given
  detail 8 and the P-302 crop, read it the same way.
- **Cross-check:** the rooftop units do not use the drain box. M-302 routes the RTU condensate "to
  primary roof drain", and on P-303 (p58) the two purple runs (34.5 FT, line 417) end at the two
  4" RD on the roof. That leaves one indoor condensate source (FCU-1), which matches the one
  scheduled DB. GPT-6 Astra, given detail 8, the p58 crop and these notes, agreed (FCU-1, 1 DB,
  moderately high confidence).
- **Example:** 440 DB = **1**.

## F6. Allowance line

- **Name:** `plumbing.allowance`
- **Inputs:** building gross area (G-001: 1,900 GSF), area basis printed by the estimator (2,000 SF).
- **Rule:** `1 LS`, with the area in the description. The area basis is the gross area rounded up
  to the next 1,000 SF here: 1,900 → 2,000. This is a judgment. The HVAC allowance (line 445,
  "AREA: 2000 SF") uses the same rounding.
- **Covers:** fittings, valves not drawn, hangers and supports, insulation, traps, stops, carriers,
  test/disinfection. None of these has a quantity line.
- **Example:** 403 = 1 LS, "ALLOWANCE: 2000 SF".

## Derived quantities outside Div 22 (cross-check only)

| Line | Rule | Numbers |
|---|---|---|
| 306 3/4" gas safety yellow paint (Div 09) | = line 420 LF rounded up to whole LF | ceil(44.21) = 45 LF |
| 307 1" gas safety yellow paint (Div 09) | = line 418 LF rounded up | ceil(9.71) = 10 LF |
| P-303 legend "SAFETY YELLOW PAINT AT ROOD GAS PIPE" | = 3/4" + 1" roof gas | 44.2 + 9.7 = 53.9 FT |
| 29 cleanout pad (Div 03) | 1 EA × 18"×18"×6" | 1.5 × 1.5 × 0.5 / 27 = 0.041667 CY |
