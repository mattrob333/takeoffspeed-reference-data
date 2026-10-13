# 23 HVAC — reading guide

How to read this job's mechanical set the way the estimator did, and where it bites.

## 1. Read order

1. **M-001 Notes and specifications** (Part 2 "Metal ducts" §1.B). Read the **gauge rule before
   measuring anything**: "RECTANGULAR DUCT: 26 GAUGE FOR ALL SIZES." and "14 INCH DIAMETER AND SMALLER:
   26 GAUGE. 15 INCH DIAMETER THRU 26 INCH DIAMETER: 24 GAUGE." This one note sets lb/SF for every run.
   Also note CC: "RUNS OF FLEXIBLE DUCT SHALL NOT EXCEED 5 FEET". The spec (23 3100 §2.5.F) allows 8'
   on low-pressure supply, so the two documents conflict.
2. **M-002 Legend**. Symbol meanings: `T` thermostat control, `RAT` duct return-air temperature, `SAT`
   duct supply-air temperature, `AT` averaging temperature, `HS` humidity, `SD` smoke detector, `C` CO2,
   `V` VOC sensor (in supply duct), `PC` particle counter (in return duct), `TR` temperature/RH display.
   Duct symbols cover the internally lined duct, flex, MVD tee-boot and fire damper. The plan uses `ST`/`RT`
   (at RTU-2) as variants of SAT/RAT, and `S` for a space temperature sensor.
3. **M-101 Schedules**. RTU schedule (RTU-1/RTU-2 Carrier, 1,600 CFM, MERV 13, 208V/3PH, 797 lb; note 1:
   18" factory-insulated curb). Mini-split (FCU-1/HP-1, Mitsubishi PKA-A12LNL/PUZ-A12NL). Exhaust fans
   (EF-1 SP-B90 55 CFM; EF-2/EF-3 SP-B110 80 CFM; note 4: integral backdraft damper and disconnect).
   **Air distribution schedule**: `S (CFM)` neck by CFM band, `LSD (X)` = X one-inch slots, 4'-0" long,
   `LD (X)` = 2'-0" long, `LSR (X)` = return slot, `R (CFM)` eggcrate return. The duct insulation R-value
   table gives NONE in conditioned spaces (it conflicts with 23 0713, which wraps all unlined supply).
4. **M-301 Ceiling plan (markup p53)**: every duct run, flex, device, sensor, damper keynote.
5. **M-302 Roof plan (markup p54)**: RTUs, HP-1, OAT sensors, condensate keynote 2, exhaust hood.
6. **Spec 23 0713 (pp. 414–416), 23 3100 (pp. 423–428), 23 2300 (pp. 417–422)** for insulation,
   liner, flex and refrigerant insulation.

## 2. How each formula input is read (with this job's strings)

| Input | Where | Exact string on this job | Notes |
|---|---|---|---|
| Rect duct size | M-301 run callouts | `20"x12"`, `16"x12"`, `24"x12"`, `8"x10"`, `14"x12"` | Order is W×H; perimeter is unaffected. Sizes are clear inside (23 3100 §1.3.B: lined duct +2" each way), but the estimator used them as drawn |
| Round size | M-301 | `8"ø`, `6"ø`, `10"ø`, `14"ø` | Runouts to round-neck diffusers |
| Duct LF | p53 legend | `20x12 DUCT 94.4 FT`, `8" DUCT 113.7 FT` | Square swatch + blue line icon = linear row |
| Gauge | M-001 Part 2 §1.B | `26 GAUGE FOR ALL SIZES` | Do not use a gauge-by-size table here |
| Flex LF | p53 legend | `8"DIA FLEXIBLE DUCT 50.1 FT`, `6"DIA FLEXIBEL DUCT 6.9 FT` | Misspelling is printed |
| Device type/CFM | M-301 tags | `LSD (2-48")` + `140 CFM`; `370S`; `895R` + `16"x16"` | Tag `nnnS` = supply CFM, `nnnR` = return CFM + neck |
| Neck (supply) | M-101 S(CFM) bands | 0–90 `6"ø` "FACE SIZE SHALL BE 12X12"; 0–100 `6"ø`; 101–210 `8"ø`; 211–330 `10"ø`; 331–480 `12"ø` | 160S → 8", 240S → 10", 370S → 12". The two 6" bands overlap, so they give the neck only |
| Face (supply) | M-301 drawn symbol size | 65S squares drawn 1'-0"; 60S, 80S, 160S, 240S, 370S drawn 2'-0" | 1'-0" → 12x12, 2'-0" → 24x24. 60S and 80S are ≤90 CFM yet 24x24, so do not take the face from the CFM |
| Counts | p53/p54 legend `n.0 EA`, round swatch, red dotted icon | `REMOTE CABLE OPERATED DAMPER 13.0 EA` | Cross-check with the plan text-layer tally |
| Keynote counts | M-301 hexagons | `6` "PROVIDE REMOTE CABLE OPERATED DAMPER IN PLENUM SLOTS…", `7` "…IN CEILING…", `9` wax damper, `12` baffle | Count the hexagons, not the devices |
| Building area | G-001 | `1900 GSF`, `1892 S.F.`; title block `1,900 SF` | The allowance basis is rounded up to 2,000 SF |

## 3. Cross-checks that worked

- **Text-layer tally = legend count** for every device. In `text/M-301.txt`, each
  `LSD (...)` string is preceded by its `nnn CFM` string; counting the pairs gives 140 CFM ×6,
  150 ×2, 60 ×2, 185 ×1 on (2-48"), 185 ×1 and 330 ×1 on (3-48"), 110 and 90 on (1-48"), and LSR 350 ×1.
  `nnnS`/`nnnR` tags give 7 supply and 7 return devices. All 21 device lines match.
- **Keynote tally**: count the keynote number in the text layer, then subtract the grid bubble with the
  same number (grids 1–7) and the keynote-list entry. 6 → 10 − 2 = 8 and 7 → 7 − 2 = 5, so 13 dampers.
- **Weight vs insulation**: LBS / SF = 1,200 / 1,325 = 0.906. This confirms that both lines come from one
  area and one gauge.
- **Second reader**: GPT-6 Astra independently reconstructed 1,324.81 SF × 0.906 = 1,200.28 lb and
  confirmed that the insulation SF is the bare surface (`trades/23-hvac/scripts/gpt1.txt`).

## 4. Traps hit on this job

1. **Repeated legend names (legends.json).** Page 53 has 55 rows (17 FT + 38 EA). The original
   `reference/markups/legends.json` held 47: its reader merge kept only the **last** occurrence of each
   repeated name, so it had `LSD (3-48")` olive 330, `LSD (2-24")` salmon 150, `24"x24" SUPPLY AIR
   DIFFUSER` bright green 240S and `24"x24" RETURN AIR GRILLE` yellow 895R, and dropped 8 rows: cyan 185
   (line 454), teal 60 (459), the 80S/60S/160S/370S supply rows (462, 464, 465, 466), and purple 220 ×2
   and teal 50 returns (469, 470). Those 8 rows have since been restored to legends.json (tagged
   "duplicate name restored"), but the four restored supply rows are all labelled colour "magenta"; only
   the 80S row is magenta (60S brown, 160S medium green, 370S indigo). Read the legend image at zoom 4
   (`render.py markup 53 out.png 0.60 0.35 0.92 0.97 4`), and match each colour swatch to the dot on its
   plan tag.
2. **Same name, different item.** Legend names without CFM need the plan colour to resolve. Here: yellow
   = 895R, teal = 50R, purple = 220R ×2; supply magenta = 80S, brown = 60S, medium green = 160S,
   indigo = 370S, bright green = 240S; LSD (3-48") cyan = 185, olive = 330; LSD (2-24") teal = 60,
   salmon = 150.
3. **Rigid duct LF never appears as an estimate line.** It is collapsed into one LBS line and one SF line.
   A takeoff that emits duct LF by size has nothing to match. Emit the weight (by gauge) and the area instead.
4. **Gauge table vs drawing note.** A SMACNA-style gauge-by-size table puts 14x12, 16x12, 20x12 and 24x12
   at 24 ga, which would add ~17% weight (1,402 vs 1,200 LBS; 33% once the engine's 15%/10% seam
   allowances are also applied). M-001 says 26 ga for every rectangular size.
5. **Insulation thickness is not in the quantity.** The estimate says 1.5". The spec says 2.2" R-6 wrap
   plus 1" liner on returns. The SF is the bare duct surface either way.
6. **Condensate drains: the estimator counted 1, the drawings show 2.** M-302 has keynote 2 ("PROVIDE
   1-1/2" RTU CONDENSATE DRAIN WITH P-TRAP…") at both RTU-1 and RTU-2. Only RTU-2's tag was marked.
7. **Keynotes vs devices for dampers.** M-101 says every LSD has a face-operated damper at the plenum
   inlet, and note 6 asks for remote cable dampers where inaccessible. The estimator counted the keynote
   hexagons (13), not the 22 supply devices.
8. **Refrigerant LF is not the route.** The 30.9 FT purple trace on p53 follows both drawn lines of the
   line set (out along one, back along the other) and then an extra 7.97 FT leg along the top of FCU-1
   and grey linework with no pipe drawn (formulas.md F4). The route counted once is only 11.75 FT. The
   roof segment on M-302 (HP-1 to the penetration, dashed, "REFRIGERANT PIPING DOWN THRU ROOF") was not
   measured, and no vertical rise was added.
9. **Grid letters and numbers collide with symbols and keynotes.** Grid "C" looks like a CO2 symbol, and
   grids 1–7 look like keynotes. Subtract them in any text-layer count.
10. **Model-number slip.** The schedule prints `48FEDA05J3M5-8W4D0`; the estimate reads `48FRDA…`. Copy
    from the schedule.
11. **Split system = 1 EA.** FCU-1 (M-301 keynote 11) and HP-1 (M-302) are one line, counted at HP-1.
12. **Scope that lives elsewhere.** RTU curbs are in roofing (line 171). Black paint at 4 LSD + 1 LSR is
    in Div 09 (line 305; p53 rows `PAINT LSD BLACK 4`, `PAINT BLACK LSR 1`). Condensate pipe is plumbing
    417. Disconnects and the wired remote controller (M-503, p55) are in Div 26. Do not count them twice
    in HVAC.
