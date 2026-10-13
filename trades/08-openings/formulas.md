# 08 Openings — formulas

All arithmetic was done in `trades/08-openings/scripts/build.py`, which writes `reconciliation.csv` and `fixtures.json`.
Dimensions are in inches unless stated.

## F1. Door opening count

- **Inputs**: door schedule rows (mark, type, W×H, door material, frame material, HRDW SET, comments); location (exterior = in the envelope).
- **Rule**: `EA = count(marks)` grouped by **type + size + door/frame material + location + prep that changes the product**.
  For this estimator that prep is a card reader, auto operator, power-assist button, knock-down frame or vendor purchase. An undercut
  does **not** split a group, and neither does a different hardware set.
- **Pairs**: type D is a pair. The schedule prints the pair width (6'-0"), and the estimator writes it as "(2) 3'Wx8'H", so one leaf is the scheduled width ÷ 2.
- **Location**: 101 ENTRY is the inner vestibule door, so it is interior (line 194). 100 and 110 are in the envelope (195, 196).
- **Worked example (lines 191/192)**: Type B marks are 106, 112, 113, 114 and 115. Those with "CARD READER" are 106 and 115, which gives **2** (line 192).
  The others are 112, 113 and 114, which gives **3** (line 191). 112 and 113 carry "1" UNDERCUT" and 114 carries no remark, but all three still sit on one line.
- The row `xxx  H  3'-0" × 1'-0 5/8"` is an unfilled template row with no door type H defined, so it is **not** counted.

## F2. Hardware set count

- **Inputs**: the HRDW SET NO. column of the door schedule (A-600); the set contents (A-601) go in the description only.
- **Rule**: `EA(set n) = count(door-schedule marks with HRDW SET NO. = n)`. The door schedule governs. A set that no scheduled door uses is
  not carried: set 5 "1900 Narrow" lists door 101 as an alternate, but 101 is HW 4, and set 8 is for storage rooms that do not exist here.
- **Worked example (line 205)**: marks with set 11 are 112 and 113, which gives **2**. Every other set (1, 3, 4, 6, 7, 9, 10, 14) has exactly one mark, which gives 1 each.
  Total = 10 sets, matching the 10 openings.

## F3. Window count (glazed frames with no door)

- **Inputs**: A-610 elevation per type (W×H from the overall dimension strings); tag instances on the **A-120** dimensional plan,
  cross-checked on the A-200/A-201 elevations.
- **Rule**: `EA(type) = count(tags of the type)`, but only for elevations with no door bay.
- **Worked example (line 211)**: window E is 6'-0"×7'-4" (72×88). A-120 has two E tags, at the west and east walls (A-200 and A-201 show one each), so **2 EA**.
- Reference areas, which the estimator did not carry: A 155.50, C 88.00, D 74.67, E 44.00, G 124.44, H 130.67 SF each.

## F4. Storefront SF (glazed frames containing a door)

- **Inputs**: overall frame W×H from the A-610 dimension strings; each door opening W×H inside the frame (door width from the
  elevation bay, which matches the door schedule; door height = the frame height below the transom bar).
- **Rule**: `SF = Σ_frames (W × H − Σ_doors w × h) / 144`, summed per system (exterior YES45 TU; interior YES45 FS; DIRTT).
- **Convention**: frame members, mullions and the door's own frame jambs are inside the SF. Only the door leaf bay is deducted.
- **Worked example, line 214 (exterior, B + F)**:
  - B = 119 × 144 − 72 × 96 (door 100 pair) = 17,136 − 6,912 = 10,224 in², which is **71.000 SF**.
  - F = 72 × 120 − 36 × 96 (door 110) = 8,640 − 3,456 = 5,184 in², which is **36.000 SF**.
  - Total **107.000 SF**, against the estimate's 107.3 (−0.28%).
- **Line 215 (DIRTT, K)**: 91.625 × 120 − 40 × 84 (door 105) = 10,995 − 3,360 = 7,635 in², which is **53.021 SF**, against 53.22 (−0.37%).
- **Line 216 (YES45 FS, J)**: 92.25 × 144 − 72 × 96 (door 101) = 13,284 − 6,912 = 6,372 in², which is **44.250 SF**, against 44.56 (−0.70%).
- The estimator's numbers are PlanSwift polygons. All three run 0.2–0.3 SF per door high, which means the door bay was traced slightly
  inside the frame lines. A pixel count of the coloured fills on markup p22, calibrated on frame B (4.126 px/in), confirms that the polygons
  are "whole frame minus the door bay". Use **tolerance 1%**.

## F5. Specialty frame LF (VAT frame)

- **Inputs**: opening W×H and frame face width `fw` from A-701 det. 6; faces = 1 (A-701: "SINGLE SIDED VAT TUBE").
- **Rule (frame centreline)**: `LF = 2 × ((W + fw) + (H + fw)) / 12 × faces`.
- **Worked example (line 207)**: W = 8.5, H = 12.75, fw = 1, so 2 × (9.5 + 13.75) / 12 = **3.875 LF**, against the estimate's 3.82 (+1.44%).
  - The inside opening gives 2 × (8.5 + 12.75) / 12 = 3.542 (−7.3%).
  - The outside gives 2 × (10.5 + 14.75) / 12 = 4.208 (+10.2%).
  - GPT-6 Astra, asked independently, also picked the centreline as the closest convention.
- 3.82 has no exact source and no PlanSwift trace on det. 6. The p24 row `Linear 15.3 FT` was checked: it is the top and back of millwork
  section 5 traced at the page scale (7.4 ft true), not the VAT frame; 15.3 / 4 = 3.825 is coincidental. Classify it as derived, tolerance 2%.

## F6. Roof hatch count

- **Rule**: `EA = count(hatch symbols on the roof plan)`. A-140 legend "30"x36" ROOF ACCESS HATCH - 3/A450" gives **1.0 EA**; spec 07 7200 2.4.B confirms one single-leaf 30×36 lid.

## Ratios and conventions taken from this job

| Convention | Value here | Basis |
|---|---|---|
| Doors with a door bay → storefront SF; frames without → window EA | 4 of 10 elevations → SF; 6 → EA | lines 208–216 against A-610 |
| Pair leaf width = scheduled width / 2 | 72" → 2 × 36" | lines 194/195 "(2) 3'Wx8'H" |
| Door group split by card reader / operator, not by undercut or hardware set | 191 = 3 (HW 10, 11, 11) | lines 191/192 |
| Storefront polygon overrun vs dimension strings | +0.28% to +0.70% | lines 214–216 |
| Sets per opening | 1 | 10 openings → 10 sets |
