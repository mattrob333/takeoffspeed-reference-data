# 09b Ceilings: reading guide

How to read this job's plans and specs for gypsum ceilings, soffits, ACT and baffles, and how each formula
input was read. Strings in quotes are printed on the sheets exactly as shown.

## 1. Sheets, in reading order

1. **A-130 Reflected ceiling plan** (markup p5). Every ceiling zone carries a tag bubble and a height:
   "ACT-1 / 12' - 0"A.F.F.", "PT-3 / 8' - 6"A.F.F.", "ACT-2 / 11' - 0"A.F.F.". PT-3 is the paint tag of a gypsum
   ceiling (A-170 "GWB-1 PAINTED GYP. / PT-3"). Legend - RCP: "2'X2' - ACOUSTIC CEILING TILE & GRID", "PAINTED GYP.
   CEILING", "EXPOSED CEILING", "EXTERIOR GYP. CEILING", "BAR-1 BEAM BAFFLE SYSTEM". General notes that matter:
   D "MECHANICAL REGISTERS IN FUR DOWN ARE TO ALIGN WITH GRID"; E "ALL GYPSUM BOARD CEILING PAINTED AND SUSPENDED GYPSUM
   BOARD ELEMENTS ARE TO BE PT-1, EXCEPT FOR THE CEILING OVER THE TRANSACTION BAR" (the estimator painted them PT-3 per
   the tags); H "CEILING GRID MAIN TEE MUST BE PERPENDICULAR TO DIRECTION OF LINER GRID LIGHTING".
2. **A-131 Enlarged RCP** (markup p6). Detail 5 "ENLARGED RCP @ TRANSACTION BAFFLES" draws every baffle. Detail 4
   draws the pendants ("PENDANT FIXTURE, 53 TOTAL", 26 electrical). The note reads "BLACK 2'-0" X 4'-0" CEILING TILE AND GRID SYSTEM
   ABOVE BEAM BAFFLES (ACT-2 & ACT-2 GRID). 4'-0" DIMENSION TO RUN PERPENDICULAR TO BAFFLE SYSTEM. PROVIDED BY OWNER
   VENDOR & INSTALLED BY GC." Details 1 and 2: "BAR-1 BEAM BAFFLE @ 8" O.C.", "BEAM BAFFLE HANGER PER MANUFACTURER",
   "5/8" GYP. BD. ON 3 5/8" METAL FRAMING @ 16" O.C. ATTACHED TO STRUCTURE ABOVE, TYP." (the wall face) and, for the box
   around the steel beam at the ACT-2 edge in detail 1 "BAFFLE CEILING AT BULKHEAD", "5/8" GYP. BD. ON 6" MTL FRAMING @
   16" O.C."
3. **A-630 Ceiling details** (no markup). Detail 1 "CLOUD CEILING SECTION" ("3 5/8" ANGLE BRACING @ 48" O.C.",
   "3 5/8" MTL STUD FRAMING @ 16" OC"); detail 3 "CLOUD CEILING SECTION" ("5/8" GYP BD ON MTL FRAMING @ 16" O.C.", no
   stud size, "MTL STUDS TO DECK"); detail 4 "CEILING DETAIL", the 9" × 10" cloud light cove referenced from detail 1,
   which calls "6" METAL STUD FRAMING"; detail 5 "TYPICAL BULKHEAD DETAIL", and detail 2 "CEILING TILE TO GYP. SOFFIT" ("5/8" SAG RESISTANT GYP. BD.", "CONTINUOUS J BEAD, TAPE & SAND
   SMOOTH, TYP.", "EDGE MOLDING, WHITE, TYP."). Section markers on A-130 (1/A-630 to 8/A-630) say which detail applies
   where. Detail 3 is cut through the Gathering Area cloud.
4. **A-170 Schedules › FINISHES SCHEDULE › CEILINGS** (raster table, upper right). Rows ACT-1, ACT-1 GRID, ACT-2, ACT-2
   GRID, BAR-1, GWB-1, MECHO give manufacturer, size, series and colour. Read sizes here, not from the estimate text.
5. **S-002** "SEISMIC DESIGN CRITERIA" block. It prints Risk Category 2, Ie = 1.0, Ss = 0.230 g, S1 = 0.084 g, Site
   Class D, SDS = 0.190 g, SD1 = 0.120 g, Seismic Design Category B. SDC B, so ASTM E580 lateral bracing does not apply
   to the ACT.
6. **Spec**: 09 2216 (p.267–272), 09 2900 (p.273–281), 09 5113 (p.289–295), 09 5426 (p.296–303).

## 2. The PlanSwift legend on A-130 (bottom left of markup p5)

Fifteen rows. Area rows have a green polygon icon and read "SQ FT". Linear rows have a blue line icon and read "FT".
The swatch colour is the markup colour at about 60% opacity. Several rows share a hue with an area row:

| Row | Swatch RGB (sampled) | Shares hue with |
|---|---|---|
| AC1 CEILING | 100,178,178 teal | SOFFIT @ 2'H |
| 5/8" GWB CEILING ... (PT3) | 101,254,101 bright green | — |
| AC2 CEILING | 255,102,255 magenta | SOFFIT @ 3'6"H, GWB BS |
| SOFFIT @ 6'6"H, GWB @ 4'H | 101,255,255 light cyan | ACM-3 canopy |
| SOFFIT @ 3'6"H, GWB @ 1'6"H | 177,101,101 rose brown | EIFS SOFFIT |
| SOFFIT @ 4'6"H, GWB @ 3'H | 101,178,100 medium green | — |
| SOFFIT @ 5'9"H, GWB @ 2'6"H | 177,178,100 olive | — |
| BRACING @ 48" O.C @ 5'H | 102,101,177 slate blue | — |
| BRACING @ 48" O.C @ 8'H | 178,101,179 orchid | — |

Do not try to find the soffit runs by colour on a flat render: the linear runs are thin and sit on area fills, so
their pixels blend. What worked was to difference the markup against the clean A-130 sheet (both rendered to the same
scale: the markup page is the 36"x24" sheet scaled by 1190.52/2592 and offset 24.12 pt down), then un-blend each
pixel at 60% opacity. Located that way:

- **SOFFIT @ 4'6"H, GWB @ 3'H (30.5 FT)**: the two long sides of the Gathering Area 103 cloud (PT-3 at 10'-0" between
  ACT-1 at 12'-0", "ALIGN" arrows), about 13.4 + 13.5 ft, plus about 3.2 ft on its south edge. Total about 30.1 ft.
- **BRACING @ 48" O.C @ 8'H (28.1 FT)**: three runs about 9.5 ft each across the Transaction Bar 108 (ACT-2 / baffle
  zone), about 28.5 ft.
- **The other soffit rows** sit where ceiling heights step. These positions are inferred from the height differences
  and were not located by colour, so confirm them on the page:
  - 5'9"H / GWB 2'6": the 8'-6" PT-3 fur-downs on the north and west sides of the transaction bar against the 11'-0"
    ACT-2 (11'-0" − 8'-6" = 2'-6"). About 24.9 + 9.8 ≈ 35 ft against 35.3.
  - 3'6"H / GWB 1'6": the 10'-0" ACT-1 against 8'-6" PT-3 steps.
  - 6'6"H / GWB 4': the 6'-6" PT-3 box at the Employee Lounge.
  - 2'H and 3'6" BS: short fascias.

**How each formula input is read from a soffit condition name.** "SOFFIT @ 5'9"H, GWB @ 2'6"H":
- 5'9" is the **framing height** (studs from the lower ceiling line up to structure). It feeds F5 only.
- 2'6" is the **exposed board height** (the fascia between the two ceiling lines). It feeds F4.
- "GWB BS" means board on both sides at the full soffit height, so faces = 2 and board height = framing height.
- A bare "SOFFIT @ 2'H" means framing and board are both 2 ft, one face.
- The soffit bottom is not in these rows. It is inside the adjacent gypsum ceiling area (516.1 SF).

## 3. Reading the areas

- AC1 948.7 SQ FT is every ACT-1 zone (vestibule, phone, meeting, work room, employee lounge, relaxed seating, and the
  9'/10'/12' zones), measured inside walls.
- AC2 244.8 SQ FT is the Transaction Bar 108 only (about 24.9 ft × 9'-10").
- The GWB ceiling 516.1 SQ FT is Mens 113, Womens 112, Gathering 103, Weather Vestibule 100, Entry 101 and the 8'-6",
  6'-6" and 10'-0" PT-3 strips.
- Exposed Structure 98.4 SQ FT (Janitor 115, Elec./I.T. 106 "EXPOSED CEILING ALL WALLS TO DECK") is paint only.
- Areas are net plan areas. Light fixtures, diffusers and access panels are not deducted.

## 4. Baffles (A-131 detail 5, markup p6)

One yellow line per baffle: **37 runs**. Count them along any horizontal line through detail 5. Spacing is 8" O.C. (the
dimension string under the plan repeats 8"); field 24'-0" ÷ 8" = 36 spaces + 1 = 37. Runs are about 10.4 ft in the main
field and 8.7 to 9.3 ft where the bulkheads cut in. Σ = 370.8 FT on the legend. Detail 5 is at 1/2" = 1'-0", not the
1/4" of A-130, so the PlanSwift scale must be set per viewport.

## 5. Cross-checks that hold on this job

- PT-3 ceiling paint line 300 = 802 SF = 516 + 286.04 (gypsum ceiling + soffit faces).
- 516 / 1.33 = 387.969925 = line 284, to six decimals. This proves the 1.33 divisor.
- Every gypsum board group in Div 09 uses the same five accessory ratios (sheets /32, adhesive 0.031, tape 0.00075 rolls,
  screws 0.0375/7 lb, mud 0.53 lb per SF).
- Baffle count × spacing = field width (36 × 8" = 24'-0").

## 6. Traps

1. **ACT-2 size.** The estimate line says "SIZE: 24" x 24" x 5/8"". A-170 says "24" x 48" x 5/8"" and the A-131 note says
   "BLACK 2'-0" X 4'-0"". SF is unaffected. A tile count or carton count must use 2x4 (8 SF per tile, not 4).
2. **ACT-2 and BAR-1 are owner-vendor items.** A-131 says the ACT-2 tile and grid are "PROVIDED BY OWNER VENDOR & INSTALLED BY
   GC". BAR-1 is "PURCHASED BY OWNER, INSTALLED BY GC". The estimate flags only BAR-1.
3. **Ceiling board thickness.** Spec 09 2900 lists "Gypsum Ceiling Board: ASTM C 1396" (p.274) with "Thickness: 1/2 inch" (p.275). The drawings
   (A-630 detail 2 "5/8" SAG RESISTANT GYP. BD.", A-131 "5/8" GYP. BD.") and the estimate use 5/8". Follow the drawings and
   raise a question.
4. **Two heights in one soffit name.** Use framing height for studs and GWB height for board. Swapping them makes the
   board +58% (452.1 SF).
5. **"GWB BS" doubles board, not framing.** The estimator counts the framing once.
6. **Bracing rows are framing, not soffits.** They carry no board, are spaced 48" (not 16") and add about 21% to line 291.
   Whether the estimator added them after the 1.33 divisor (braceLF / 4 × height) or inside it (braceLF × height / 3)
   cannot be told from the 0.1-ft legend (430.02 vs 430.24 against 429.60); the first is the adopted convention.
7. **Same-colour rows.** SOFFIT @ 2'H has the AC1 teal; GWB BS has the AC2 magenta; 6'6" soffit has the ACM-3 cyan;
   3'6"/1'6" soffit has the EIFS rose brown. Use the legend icon (line vs polygon) and the unit (FT vs SQ FT) to tell them
   apart, not the colour.
8. **Legend rounding.** The legend prints 0.1 ft or SF. The estimate carries 2 decimals of the same values (948.75 vs 948.7).
   Products of rounded LFs land within about ±1 SF / ±1.5 LF of the estimate.
9. **The estimator rounded the flat ceiling.** 516.0 is carried against 516.1 measured, and every derived line follows 516.0.
10. **Not in the estimate but specified.** 10% ACT attic stock (p.289). ACT grid, wall angle (WA-2 for ACT-2) and 12 ga hangers
    ≤ 48" O.C. (p.291–293). Continuous J-bead at gyp soffit edges (A-630 detail 2). Hangers/track for the gypsum ceiling.
    Raise these as scope questions, not silent additions.
11. **Do not take EXPOSED STRUCTURE, ACM-3 or EIFS SOFFIT rows into this trade.** They are paint, canopy and EIFS scope.
12. **Stud size is not uniform.** The estimate carries all ceiling and soffit studs as 3-5/8". A-630 detail 4 (cloud
    cove) and A-131 detail 1 (beam wrap) call 6" studs. Same LF rule, different size: raise an RFI.
