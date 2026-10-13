# Formulas — 26 Electrical

Every quantity in this trade is one of four formulas. All arithmetic for the
worked examples was done in Python (`trades/26-electrical/scripts/build.py`).

## F1 `count-sum` — devices, fixtures, boxes, panels, room items (96 lines, EA)

- **Inputs:** for one item name (device variant, fixture tag), the legend count
  on each markup page where the item appears (EA). Optional: the same physical
  item drawn on more than one page.
- **Rule:** `qty = Σ count(page)` over the pages that show **different**
  instances. A page that only re-shows instances already counted is excluded.
- **Item key:** the estimator keys on the full device wording, including
  the plate note. `TAMPER RESISTANT DUPLEX` (549), `… W/ BLACK COVER PLATE` (540)
  and `… PROVIDE FACTORY ENGRAVED …` (550) are three lines.
- **Conventions (this job):**
  - Plan + enlarged plan + elevation are summed when each shows its own devices
    (E-100 + E-702 IT room; E-100 + E-703; E-130 + E-704 + M-503).
  - Page 87 (a reduced reprint of E-010) and the "LCP" row on page 49 repeat
    devices already counted on pages 42 and 46, and are not added.
  - Fixtures are counted **as drawn**, without the schedule's attic stock
    ("PROVIDE TEN (10) EXTRA FIXTURES", types C and UC).
  - Pole lights are counted per pole assembly (2P4DA = 4, with 2 heads each).
- **Worked examples:**
  - Quad receptacle 20A (536): E-100 3 + E-702 14 = **17 EA** (estimate 17).
  - Disconnect switch (553): E-130 3 + E-704 1 + M-503 2 = **6 EA** (estimate 6).
  - Combination data outlet (571): E-100 14 + E-703 1 = **15 EA**.
  - Junction box (574): E-100 9 + E-130 1 = **10 EA**; site boxes are separate (503 = 4).
  - Type C pendant (514): E-130 53 = **53 EA**. With the scheduled attic stock it
    would be 63; the estimator did not carry it.

## F2 `conduit-route-lf` — conduit bundles (6 lines, LF)

- **Inputs:** each measured route length (LF) of one bundle, per markup page;
  conduits in the bundle as printed, e.g. `(2)` in "(2) 4"DIA CONDUIT".
- **Rule:** `LF = Σ route lengths`. The conduit count is **not** multiplied in.
  It stays in the description, so the line reads "(2) 4" conduit, 101.71 LF of route".
- **Basis:** this is how the estimator wrote every bundle line on this job (6/6).
  Material conduit LF, if wanted, is `LF × n`. That is a second line, not this one.
- **Worked examples:**
  - (2) 4" (505): 71.5 (E-010) + 30.2 (E-100) = **101.7 LF** (estimate 101.71; legend
    prints one decimal). As conduit stock: 101.71 × 2 = 203.42 LF.
  - (2) 2" (507): 15.4 (E-010 RDT plan, p41) + 61.8 (E-010 site) + 30.2 (E-100) = **107.4 LF**
    (estimate 107.37). The p41 15.4 is not a separate drawn route: no cyan run is visible on
    the markup, and it equals the brown 1" 15.4 of line 506. Both bundles were evidently measured along
    the same kiosk J-box to building J-box path, one legend row per bundle. Two bundles in one
    trench are two rows of the same route, each carried at the route length.
  - (2) 5" (508): **11.4 LF** (11.39).
  - (4) 3/4" IMC (601): **19.6 LF** (19.61). (4) 2" IMC w/ string (602): **19.5 LF** (19.54).
  - 1" (506): 4.8 + 15.4 = **20.2 LF**. The estimate carries 20.0, rounded to whole feet; the
    recomputed value is 1.0% above it (deltaPct +1.0 = (20.2 − 20.0) / 20.0).

All six conduit lines together: 279.62 LF of route = 617.54 LF of conduit
(ratio 2.208). See app-gaps.md.

## F3 `linear-fixture-lf` — linear LED fixtures (3 lines, LF)

- **Inputs:** each measured run of a fixture whose schedule length reads
  "LENGTH AS SPECIFIED ON PLANS" (types G, L, UC), in LF.
- **Rule:** `LF = Σ runs`. No per-run end caps or feeds are separate lines in
  this estimate.
- **Worked examples:** G (517) 26.8 → 26.78 LF; L (522) 30.4 → 30.36 LF; UC (529)
  9.1 → 9.13 LF. All three are within 0.33% (legend rounding).

## F4 `area-allowance` — branch wiring, conduit and fittings (1 line, LS)

- **Inputs:** building gross area (SF) from the title block: `1,900 SF`.
- **Rule:** `quantity = 1 LS`; `basisArea = ceil(grossArea / 500) × 500`.
- **Convention:** the estimator's own house rule. The same basis, "AREA: 2000 SF",
  appears on plumbing (403), HVAC (445) and low voltage (622). Measured areas on
  this job are 1,917.6 SF slab (S-201) and 1,864.3 SF roofing (A-140). Any of them
  rounds up to 2,000. The rounding step can't be told apart from this job alone:
  ceil to 500 and ceil to 1,000 both give 2,000.
- **Worked example:** ceil(1900 / 500) × 500 = 4 × 500 = **2,000 SF**, 1 LS.
- **Covers:** every conductor and conduit not drawn as a measured run: branch
  circuits, home runs, the riser feeders (E-800: 2 sets 4-#3/0 service, 400A and
  225A feeders), grounding electrode system, fittings, supports.

## Lines without a formula (judgment)

| Line | Item | Why it cannot be reproduced |
|---|---|---|
| 497 | Safety switch 30A 3P fused @ 20A, 1 EA | The legend row prints `NAN EA` (no dot placed). The name is the E-001 symbol `30/20`. The 1 was typed by hand. |
| 541 | TR GFCI duplex w/ engraved plate, 1 EA | The legend row prints `NAN EA`. Keynote 24 (engraved plate) occurs 3 times on E-100, and those three receptacles are already lines 550 (REF), 542 (EWC) and 537 (DW). This is probably a second count of 537. |
