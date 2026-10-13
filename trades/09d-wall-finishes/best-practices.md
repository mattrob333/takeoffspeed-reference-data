# Best practice: wall tile, wall covering, FRP and decorative wall panels (quantities and material types only)

Scope: interior wall finishes applied over a finished substrate: ceramic wall tile (wainscot / full-height) with its setting materials, grout, backer and metal trims; fibre-reinforced plastic (FRP) wall panels with moldings and adhesive; commercial vinyl wall covering with primer and adhesive; and (briefly) prefabricated decorative wall panels. Prices, labor and productivity are out of scope. Floor tile, resilient base and paint are separate trades; they appear here only where they share a material (grout lines, Schluter trims, primer).

How to read this file. Every factual claim carries a link. Source quality is tagged:

- **(primary)**: manufacturer data sheet or installation guide, standard, or master specification that I opened and read in full text.
- **(search summary)**: a figure that a search result summarised from a primary-looking page that I could not open myself (the page blocked the fetch or was a paywalled PDF). Verify before relying on it.
- **(blog-level)**: estimating blog, retailer or calculator page. Useful as a convention, not as a standard.
- **(derived)**: my own arithmetic (done in Python), labelled so; the inputs are cited.
- **(project)**: a file in this repository (`reference/`, `source/`), cited by path.

Honest summary of the evidence. There is no published standard that fixes tile waste, opening-deduction thresholds, or wall-covering overage for commercial takeoff. What can be cited is: (1) manufacturer coverage data (thinset by trowel notch, FRP adhesive per gallon, grout by joint geometry), (2) installation standards and master specs (95 % mortar contact, wainscot layout to the next full tile, expansion gaps, "do not seam within X of a corner"), (3) stock sizes (4x8 FRP, 3'x5' backer, 54" goods, 8'2-1/2" trims), and (4) one real measurement standard for the decorating trades (PCA P10). Everything else is estimator convention and the sources disagree. The right design for an AI takeoff is therefore: measure the installed net quantity from the drawings, apply a stated measurement convention, and keep waste, pack rounding and attic stock as separate, visible steps.

---

## 1. What an estimator takes off, and in which units

| Item | Unit | Basis / notes |
|---|---|---|
| Wall tile, by finish tag (WT-1, WT-2 ...) and by band height | SF net (installed face area) | Estimating software treats wall tile as SF of material placed on a wall, with LF and EA as alternates for trims and pieces ([Estimating Edge, wall ceramic tile take-off](https://www.estimatingedge.com/knowledgebase/wall-ceramic-tile/), blog-level). Tile is bought by the carton (published SF per carton), so keep net SF and cartons as two lines. |
| Tile count (check figure) | EA | 3"x12" nominal = 144 / (3 x 12) = 4.0 tiles per SF (derived). |
| Thinset (setting mortar) | 50 lb bags | Coverage depends on trowel notch (section 5). |
| Grout | lb or units per manufacturer chart | Depends on tile size, thickness and joint width (section 5). |
| Backer board behind tile | SF net, then boards | Cement backer units are sold as 3'x5' x 7/16" boards (15 SF) in one common product ([Custom Building Products WonderBoard Lite TDS-266](https://cdn.shopify.com/s/files/1/0049/0995/7154/files/TDS-266.pdf), primary). |
| Tile edge, cove, corner metal trims | LF, then sticks | Schluter JOLLY is a 90-degree profile for outside corners and tile edges, set in the mortar bed under the tile ([Schluter JOLLY](https://www.schluter.com/schluter-us/en_US/Profiles/For-Walls/Edging-&-Outside-Wall-Corners/Schluter-JOLLY/p/JOLLY), primary). Stock length is 8'2-1/2" (2.5 m) in retailer listings ([Ceramed JOLLY 8'2-1/2"](https://www.ceramed.ca/en/products/schluter-jolly-wall-edge-molding-aluminium-white-glossy-1-2-12-5-mm-x-8-2-1-2), blog-level), with select finishes also in 10' lengths ([Schluter JOLLY](https://www.schluter.com/schluter-us/en_US/Profiles/For-Walls/Edging-&-Outside-Wall-Corners/Schluter-JOLLY/p/JOLLY), primary). |
| Ceramic trim shapes (bullnose, cove base, internal / external corner pieces) | LF or EA by piece length | A master spec lists the standard wall-tile trim types: base cove, base cap, wainscot cap, external corners, internal corners ([Daltile 09 30 13 guide spec](https://digitalassets.daltile.com/content/dam/Daltile/website/resources/trade-professionals/architects-designers/AD_fillableform.pdf), primary). |
| Movement / sealant joints | LF | Provided "where indicated" and formed during installation, never saw-cut afterwards ([Daltile 09 30 13](https://digitalassets.daltile.com/content/dam/Daltile/website/resources/trade-professionals/architects-designers/AD_fillableform.pdf), primary). Backer-board data sheet: tiled surfaces over 36 ft continuous, or abutting dissimilar structure, should carry perimeter and movement joints per TCNA EJ171 ([TDS-266](https://cdn.shopify.com/s/files/1/0049/0995/7154/files/TDS-266.pdf), primary). |
| FRP panels, by tag and height | SF net, then sheets | Common sheet sizes 4x8, 4x9, 4x10 (and 4x12 for some lines): 4x8 = 32 SF (derived). Distributor listing of Marlite pebbled white P100 in 4x8 and 4x9 and 4x10 colours ([FBM Marlite P100 4x8](https://myfbm.com/all-products/wall-%26-ceiling-panels/fiberglass-reinforced-plastic---frp/frp-panels/4-ft-x-8-ft-class-c-frp-panel%2c-pebbled-white-p100/p/frpwh-8-mar), search summary). |
| FRP moldings: division bar, inside corner, outside corner, top/bottom cap | LF, then sticks | 8' and 10' sticks are common ([Crane Sequentia 10' outside corner](https://hemlockhardware.com/products/100195-crane-sequentia-10-ft-white-frp-outside-corner-molding), search summary). Crane describes one-piece moldings with expansion guides and two-piece moldings ([Crane FRP Installation Guide](https://pdf.lowes.com/productdocuments/c8b0c4ed-f527-420b-8cca-7bb080d2f995/49012583.pdf), primary). |
| FRP adhesive | gallons | About 50 SF per gallon with a 3/16" W x 1/4" D x 1/2" c-c V-notch trowel ([Titebond FRP guide](https://static.richelieu.com/documents/docsGr/104/999/8/1049998/3285886.pdf), primary). |
| FRP sealant (silicone) | cartridges / LF of joint | Crane: where moisture resistance is required, silicone goes in all moldings and around all panel edges, fasteners and fixtures ([Crane guide](https://pdf.lowes.com/productdocuments/c8b0c4ed-f527-420b-8cca-7bb080d2f995/49012583.pdf), primary). |
| Vinyl wall covering | SF net for the area line; linear yards (LY) of goods for the buy line | Commercial estimators run takeoffs assuming 54"-wide goods in linear yards; 54" x 36" / 144 = 13.5 SF per LY ([Astek square-footage conversions](https://tothesource.com/s/Astek-Square-Footage-Conversions.pdf), primary). |
| Wall covering primer / liner / adhesive | SF (primer, liner), gal (adhesive) | Spec sections call for a primer and a manufacturer-approved adhesive, applied to the back of the wall covering; an optional liner is a non-woven polyester-cellulose sheet ([VA 09 72 16](https://www.wbdg.org/FFC/VA/VAASC/VA%2009%2072%2016.pdf), primary). |
| Wall covering edge guards / wainscot cap | LF | "J"-shape with a groove to receive the wall covering ([VA 09 72 16](https://www.wbdg.org/FFC/VA/VAASC/VA%2009%2072%2016.pdf), primary). |
| Decorative wall panels (acoustic, laminated, "PNL-n") | EA by size and SF, plus trim LF | Counted from elevations; not area-formula items. |
| Attic stock | EA / cartons / rolls | Spec-driven and separate from waste (section 7). |

---

## 2. Which sheets and spec sections drive this trade

Drawings (generic):

- **Finish plan and finish legend** give the tag, product (size, manufacturer, model, colour), and which rooms/walls get which finish. Tile, FRP and wall covering are tagged finishes, so the legend is the key.
- **Interior elevations and enlarged room plans** (restrooms, break rooms, back-of-house) give band heights (a wainscot "5'-6\"" line, FRP "4'-0\"" line), trim callouts (metal edge strip at the top, cove trim at the bottom), and wall extents.
- **Partition schedule / wall types** give the substrate that tile or FRP lands on. Tile and FRP walls need water-resistant gypsum or cement board; this changes the framing/board takeoff, not just the finish.
- **Millwork elevations** give feature tile panels and decorative wall panels.
- **Door and window schedules and openings** govern what is deducted inside a band.

Specifications (MasterFormat): tile is 09 30 00 (or 09 30 13 Ceramic Tiling); wall coverings are 09 72 00 (federal guide spec UFGS 09 72 00 exists: [WBDG UFGS 09 72 00](https://stg.wbdg.org/dod/ufgs/ufgs-09-72-00), search summary); FRP panels and special wall surfaces fall in 09 77 00. I found no UFGS guide spec for 09 77 00 or 09 77 23 (search summary), so FRP is often specified only by a finish-legend entry plus a short spec paragraph or a section from the architect's own master.

**This project (project):**

- Finish plan `source/drawings/Architectural/A-150-FINISH-PLAN-Rev.0.pdf` (text at `text/A-150.txt`) carries the tags WT-1, WT-2, WT-9, WC-1, FRP-1 and the Schluter transition notes.
- `A-410` (enlarged restroom plans and elevations) shows the wainscot elevations: tags WT-1 / WT-2 / WT-9 with a 5'-6" dimension line, "SCHLUTER STRIP" at the top edge, "SCHLUTER COVE TRIM" at the base, and "FRP PANEL @ MOP SINK, BOTH SIDES" (`text/A-410.txt`).
- Wall tile also appears on enlarged millwork sheets A-700 to A-705 (the estimate's drawing reference for the WALL FINISH section is "A410, A700 - A705", `reference/estimate/lines.json` lines 235-241).
- Partition schedule A-620 has general note N: "ALL PARTITIONS SCHEDULED TO RECEIVE TILE OR FRP, SHALL BE CONSTRUCTED OF WATER-RESISTANT CORE GYPSUM WALL BOARD" and lists 5/8" and plain "cement board" layers in some types (`text/A-620.txt`).
- Specification `source/specifications.pdf` section 09 30 00 pp. 282-288 covers only "ceramic floor tile and base" in its summary, with ANSI A118.4 thinset, ANSI A118.7 polymer-modified grout or A118.3 epoxy grout, a 10 percent attic-stock requirement, and "lay out tile work and center tile fields ... minimize the use of pieces that are less than half of a tile" (`text/spec-p282.txt` to `spec-p286.txt`). The spec index has no section for wall covering or FRP (`reference/sheets/spec_index.json`: the only 09 sections are 092216, 092900, 093000, 095113, 095426, 096513, 096519, 096813, 099100, 099110, 099653). Lesson for an AI: the drawings' finish legend, not the specification, is the only source of wall covering and FRP products here, and the tile section's scope sentence does not exclude wall tile that the drawings schedule.

---

## 3. Measurement rules

### 3.1 Net installed area

Measure each finish band as wall length x band height, per tag, then subtract the part of each opening that lies inside the band. A door through a 4'-0" FRP band deducts door width x 4'-0", not the full door area. A window that sits entirely above the band deducts nothing. This is the rule implemented in the app engine ([wall-finishes.ts `bandArea`](file://TakeoffSpeed repo: lib/quantities/trades/interiors/wall-finishes.ts), project) and matches generic wall-tile calculators, which measure the wall, subtract openings, then add waste ([DG Floors wall tile calculator](https://dgfloors.com/wall-tile-calculator/), search summary / blog-level).

### 3.2 Opening deductions: what the sources actually say

- **Decorating trades (PCA P10, primary):** "When a small opening interrupts a continuous surface, the opening is disregarded and considered part of the continuous surface. Any openings extending from floor to ceiling and exceeding five feet in width shall be deducted. All openings 100 square feet or larger are deducted." Cabinets, tubs, showers and other items that restrict access are not deducted ([PCA P10, Measurement of Surface Area for Estimating Painting and Decorating Work](https://www.pcapainted.org/wp-content/uploads/2023/10/PCA-Industry-Standards_20230918-P10.pdf)). P10 is a painting and decorating standard; it is the closest published rule for wall covering, but it is a labor-and-spread-rate measurement convention, not a material-yield rule.
- **Tile (blog-level):** do not subtract small fixtures (outlets, faucet holes); the cutouts are absorbed by the waste allowance ([DG Floors](https://dgfloors.com/wall-tile-calculator/), search summary). No published standard sets a tile deduction threshold.
- **Federal wall covering spec (primary):** install wall covering "continuous behind non-built-in casework" and fill the spaces above and below windows and doors with consecutive strips from the roll ([VA 09 72 16](https://www.wbdg.org/FFC/VA/VAASC/VA%2009%2072%2016.pdf)). The goods for those fill-ins are real material even though the area is "an opening".
- **Tile spec language that matters for coverage (primary):** extend tile into recesses and behind equipment "to form complete covering without interruptions unless otherwise indicated" ([Spec 09 30 00, project, `spec-p285.txt`](file://text/spec-p285.txt); same wording in the [Daltile 09 30 13 guide spec](https://digitalassets.daltile.com/content/dam/Daltile/website/resources/trade-professionals/architects-designers/AD_fillableform.pdf)). So do not deduct tile behind a fixture that is not built in.

Practical rule for an AI: report two numbers per tag, (a) net installed SF with openings inside the band deducted at their real overlap, and (b) the purchase quantity, where small penetrations save nothing. Say which convention each number follows.

### 3.3 Heights, layout and rounding

- **Wainscot height.** A master spec says to "lay out tile wainscots to dimensions indicated or to next full tile beyond dimensions indicated" ([Daltile 09 30 13](https://digitalassets.daltile.com/content/dam/Daltile/website/resources/trade-professionals/architects-designers/AD_fillableform.pdf), primary). The installed height can therefore exceed the drawn height. Example (derived): a 5'-6" (66") wainscot in 3" x 12" tile laid with the 3" side vertical is 22 whole courses, no rounding; laid with the 12" side vertical it is 5.5 tiles, so the "next full tile" height is 72".
- **Centre the field.** Specs say to centre the tile field in each direction and minimise cut pieces smaller than half a tile ([Spec 09 30 00, project, `spec-p285.txt`](file://text/spec-p285.txt)). Layout drives cuts, so it drives waste.
- **Tile movement joints.** Tiled surfaces beyond 36 ft continuous need movement joints ([TDS-266](https://cdn.shopify.com/s/files/1/0049/0995/7154/files/TDS-266.pdf), primary); a small bank restroom rarely reaches that length, but corners and changes of plane still carry detailed sealant joints.
- **FRP height limits.** Crane recommends panels not exceed 48" in width and 12' in length ([Crane guide](https://pdf.lowes.com/productdocuments/c8b0c4ed-f527-420b-8cca-7bb080d2f995/49012583.pdf), primary). Above 12' use stacked panels with a division molding.
- **FRP end gaps.** A minimum 1/4" gap at the top and bottom of each panel, minimum 1/8" (recommended 1/4") between panels, and cut panels 1/4" short where a base molding will extend ([Crane guide](https://pdf.lowes.com/productdocuments/c8b0c4ed-f527-420b-8cca-7bb080d2f995/49012583.pdf), primary). These are installed-gap rules; they change cut lengths by fractions of an inch and do not change takeoff SF, but they are why a nominal 8'-0" sheet is not a clean 8'-0" panel.

### 3.4 Corners, returns, laps

- **Tile corners.** An outside corner needs a trim: a bullnose / surface-bullnose ceramic piece or a metal profile such as JOLLY (master spec external-corner options: [Daltile 09 30 13](https://digitalassets.daltile.com/content/dam/Daltile/website/resources/trade-professionals/architects-designers/AD_fillableform.pdf), primary; Schluter JOLLY: [Schluter](https://www.schluter.com/schluter-us/en_US/Profiles/For-Walls/Edging-&-Outside-Wall-Corners/Schluter-JOLLY/p/JOLLY), primary). Count outside corners and exposed vertical ends as LF of band height; count the exposed top edge as LF; count inside corners as a sealant joint, not an extra area. A corner adds no square footage; a tiled return, jamb or sill adds its developed area.
- **FRP corners.** Division bars at panel-to-panel joints and a corner molding at each inside/outside corner; Crane's moldings sequence starts "in an inside corner" with a plumb line 48-1/8" from the corner, inserts a division bar after the first panel, and puts a corner molding on the first panel of the next wall ([Crane guide](https://pdf.lowes.com/productdocuments/c8b0c4ed-f527-420b-8cca-7bb080d2f995/49012583.pdf), primary). A corner molding replaces, rather than adds to, a division bar at the same location.
- **Wall covering corners.** The federal spec says to wrap wall covering around inside and outside corners, not to seam within 2" of an inside corner or within 6" of an outside corner, and to install no horizontal seams ([VA 09 72 16](https://www.wbdg.org/FFC/VA/VAASC/VA%2009%2072%2016.pdf), primary). These rules force strip splits at corners and so add goods; there is no "corner SF".
- **Wall covering and base.** Install wall covering before resilient base and run it not more than 1/4" below the top of the base ([VA 09 72 16](https://www.wbdg.org/FFC/VA/VAASC/VA%2009%2072%2016.pdf), primary), so the covered height normally stops at the top of base, not the floor, when a base is scheduled. Note that the height stated on a plan (for example "wall covering at 10'-0\" H") should be checked against the base height.

### 3.5 Substrate and underlay

Tile and FRP substrates change the board quantity. Crane lists standard unpainted gypsum as its preferred substrate and notes that painted surfaces do not allow solvent-free or solvent-based adhesives to dry ([Crane guide](https://pdf.lowes.com/productdocuments/c8b0c4ed-f527-420b-8cca-7bb080d2f995/49012583.pdf), primary). Painted walls behind FRP are therefore a coordination flag between the paint and FRP takeoffs (no paint behind FRP unless the adhesive is rated for it). For tile on studs, cement backer units are fastened to framing at 16" o.c. maximum, with screw spacing around 6" along framing and a 1/8"-3/16" gap at joints filled with polymer-modified mortar and 2" mesh tape ([TDS-266](https://cdn.shopify.com/s/files/1/0049/0995/7154/files/TDS-266.pdf), primary). Backer boards are bought as sheets; round up per wall, do not divide total SF by 15.

---

## 4. Material breakdown an estimator lists (primary materials and what follows from them)

### 4.1 Wall tile

1. Field tile by tag (size, manufacturer, model, colour), in cartons.
2. Trim tile (bullnose, cove, corners) if the detail shows ceramic trim, otherwise metal profiles (section 1).
3. Thinset: polymer-modified mortar to ANSI A118.4 (as called for by the project spec; the [VA 09 30 13](https://www.wbdg.org/FFC/VA/VANCAS/VANCA093013.pdf) master spec lists ANSI A108.5 / A118.1 dry-set and A118.4 latex-portland options, primary).
4. Grout: cement-based (A118.6 / A118.7) or epoxy (A118.3) per spec; one grout tag may serve several tile tags, so track by tag. Unsanded grout for joints 1/8" and narrower, sanded for 1/8" and wider ([VA 09 30 13](https://www.wbdg.org/FFC/VA/VANCAS/VANCA093013.pdf), primary).
5. Backer: cement backer unit or glass-mat water-resistant gypsum backer behind tile in wet areas; backer joint tape and screws ([VA 09 30 13](https://www.wbdg.org/FFC/VA/VANCAS/VANCA093013.pdf), primary; [TDS-266](https://cdn.shopify.com/s/files/1/0049/0995/7154/files/TDS-266.pdf), primary).
6. Waterproofing / crack-isolation membrane where the spec calls for it (fabric-reinforced fluid-applied, ANSI A118.10 / A118.12 per the master spec: [VA 09 30 13](https://www.wbdg.org/FFC/VA/VANCAS/VANCA093013.pdf), primary).
7. Metal trims: edge, cove, outside corner, in sticks (section 1).
8. Sealant at movement joints and at changes of plane; grout sealer if specified; tile cleaner.
9. Attic stock per spec (section 7).

### 4.2 FRP

Panels; division bars; inside corners; outside corners; top cap / edge molding; base or bottom cap only where the detail shows one; FRP-rated adhesive (applied to the panel back, not the wall: Crane, [Titebond](https://static.richelieu.com/documents/docsGr/104/999/8/1049998/3285886.pdf)); silicone sealant; fasteners or nylon drive rivets only if specified (Crane recommends 16" o.c. both ways and pre-drilled oversize holes; [Crane guide](https://pdf.lowes.com/productdocuments/c8b0c4ed-f527-420b-8cca-7bb080d2f995/49012583.pdf), primary). Tools (trowel, roller) are not material.

### 4.3 Wall covering

Goods (LY), primer (the wall covering primer is usually a distinct painted-primer line under the paint trade), adhesive, optional wall liner, edge guards / wainscot cap where shown, attic stock. The spec requires a full-height sample wall of at least 8' length before work proceeds ([VA 09 72 16](https://www.wbdg.org/FFC/VA/VAASC/VA%2009%2072%2016.pdf), primary), which is a submittal item, not a quantity.

---

## 5. Coverage, yield and waste factors, with their basis

### 5.1 Thinset (per 50 lb bag, manufacturer estimating chart)

| Trowel notch | SF per 50 lb bag |
|---|---|
| 1/4" x 1/4" x 1/4" square | 90-100 |
| 1/4" x 3/8" x 1/4" square | 60-67 |
| 1/2" x 1/2" x 1/2" square (not recommended by the maker) | 42-47 |
| 3/4" x 9/16" x 3/8" U-notch at 45 degrees / at 30 degrees | 34-38 / 42-47 |

Source: [Custom Building Products VersaBond HP](https://www.custombuildingproducts.com/products/versabond-hp-high-performance-large-and-heavy-tile-mortar) (primary). The same page requires at least 80 % mortar contact in dry areas and at least 95 % in wet areas and exteriors, and calls the chart an estimating chart; coverage varies with technique and conditions. A master spec requires 95 % mortar coverage for exterior tile floors and tile floors in wet areas ([Daltile 09 30 13](https://digitalassets.daltile.com/content/dam/Daltile/website/resources/trade-professionals/architects-designers/AD_fillableform.pdf), primary). Bags for a net area (derived): 100 SF at the 1/4" x 3/8" notch = 100/67 to 100/60 = 1.49 to 1.67 bags. Small-format wall tile like 3"x12" is typically set with the smaller notches; pick the notch from the tile maker or spec, not from a default. Mapei recommends adding 5-10 % overage to mortar ([Mapei mortar calculator](https://www.mapei.com/us/en-us/product-calculator/tile-mortars-and-adhesives), search summary).

### 5.2 Grout

Grout use is a geometric function of tile length L, width W, thickness T and joint width J. The volume per tile "cell" is (L + W) x J x T; dividing by L x W gives volume per unit face area ([BuildingClub grout calculator](https://pro.buildingclub.info/en/finishing/tile-grout-calculator-ft-sqft-cost/), blog-level, search summary). Manufacturers publish coverage charts instead: Laticrete refers to its coverage chart (DS 254.3) and calculator, says actual coverage varies with job-site conditions, tile size and joint size, and says to "add 10% for waste, spillage and clean-up", plus another 10-15 % for unglazed quarry tile ([Laticrete SPECTRALOCK PRO data sheet](https://cdnmdm.laticrete.com/ProductAssets/Product%20Documents/lds6850_spectralock-pro-grout-la-en.pdf), primary; the "10% rule" is repeated in a [Laticrete article](https://www.laticrete.com/blog/2023/october/the-power-of-the-grout-calculator), primary).

Worked example, inputs illustrative (derived): 3" x 12" tile, 1/8" joint, 5/16" thickness gives (12 + 3) / (12 x 3) x 0.125 x 0.3125 x 144 = 2.34 cubic inches of joint per SF; at the 1/16" joint it is 1.17 cu in per SF. The thickness and the joint width must come from the product data and the spec, so an AI that has neither should flag grout as "not computable" rather than assume. A blog-level figure of about 230 cubic inches per 25 lb of sanded grout exists ([BuildingClub](https://pro.buildingclub.info/en/finishing/tile-grout-calculator-ft-sqft-cost/), blog-level), which would give about 98 SF per 25 lb at the 1/8" example; use the manufacturer chart instead for a real number.

### 5.3 Tile overage

There is no standard. Reported values: 5 % to 7 % for simple layouts and 10-15 % for diagonal or complex cuts ([Flooring Clarity](https://www.flooringclarity.com/how-much-extra-tile-project/), blog-level); a wall-specific row of 10-15 % for backsplash / feature wall ([Flooring Clarity](https://www.flooringclarity.com/how-much-extra-tile-project/), blog-level, search summary); 10 % simple, 15 % diagonal, 20 % herringbone / mosaic / large format ([DG Floors](https://dgfloors.com/wall-tile-calculator/), blog-level, search summary); one retailer asks for 20 % on a straight grid and a minimum 30 % on tile 18"x36" and larger ([Artistic Tile](https://www.artistictile.com/advice), blog-level, search summary). The spread is wide, so state the percentage and the reason. For small 3"x12" subway tile on straight-stacked or running-bond walls, 10 % is the usual starting value in the sources above. Separate from waste, the specification may require a quantity of full-size attic stock (section 7).

### 5.4 FRP

- Sheet area: 4x8 = 32 SF (derived). A 4'-0"-high band is cut from the 8'-0" length, so one 4x8 sheet covers 8 LF of wall at 4' high (derived). Purchase sheets by layout per wall, not by total SF / 32: a 4 LF run of 4'-high wainscot is 16 SF but still needs one sheet (derived).
- Adhesive: about 50 SF per gallon with a 3/16" W x 1/4" D x 1/2" c-c V-notch ([Titebond FRP guide](https://static.richelieu.com/documents/docsGr/104/999/8/1049998/3285886.pdf), primary). For comparison, Marlite's decorative Plank & Panels line quotes 210 SF per 3.5 gallons, which is 60 SF per gallon, using the same trowel ([Marlite Plank & Panels installation instructions](https://www.buildsite.com/pdf/marlite/Planks-Panels-Installation-Instructions-2958856.pdf), primary; the 60 is derived). Crane specifies 100 % adhesive coverage over the whole panel back with a crosshatch pattern, using a trowel recommended by the adhesive maker ([Crane guide](https://pdf.lowes.com/productdocuments/c8b0c4ed-f527-420b-8cca-7bb080d2f995/49012583.pdf), primary). So use the net adhesive area equal to the net panel area, not the wall area.
- Moldings: 8' and 10' sticks are common, verify per product ([Crane Sequentia trim listing](https://hemlockhardware.com/products/100195-crane-sequentia-10-ft-white-frp-outside-corner-molding), search summary). Division bars are needed at each panel joint if moldings are the seam treatment; if the detail instead specifies colour-matched caulk or urethane seam sealant, there are no division bars and sealant is the line (Crane lists moldings, colour-coordinating caulk and seam sealant as the three seam treatments: [Crane guide](https://pdf.lowes.com/productdocuments/c8b0c4ed-f527-420b-8cca-7bb080d2f995/49012583.pdf), primary).
- Panel waste: no published figure. The sources only say to pre-fit panels and do cutting before adhesive. Use a layout-based sheet count; if a percentage is needed, state it as an estimator allowance.

### 5.5 Wall covering

- Goods width and usable yield: 54"-wide goods give 13.5 SF per linear yard; 36" gives 9 SF; 44" gives 11 SF ([Astek](https://tothesource.com/s/Astek-Square-Footage-Conversions.pdf), primary). Some digitally printed goods are 54" wide on the roll with a maximum printable width of 52" (same source), so the usable width can be less than the nominal width; confirm.
- Type: Type II is "medium duty" under WA W-101, with minimum total weight of 13.0 oz/yd2 for PVC-coated goods (Type I 7.0, Type III 22.0) ([Wallcoverings Association W-101](https://cdn.ymaws.com/www.wallcoverings.org/resource/resmgr/WA_W-101_2025_Final_.pdf), primary). Commercial product listings show 54" width and a vertical repeat, for example "Type II, 54 inch, 25-1/4 inch repeat" ([Momentum Editorial listing](https://momentumco.com/products/09239932), primary).
- Minimum piece length: W-101 sets 9' as the minimum length piece unless otherwise specified ([W-101](https://cdn.ymaws.com/www.wallcoverings.org/resource/resmgr/WA_W-101_2025_Final_.pdf), primary), which matters for short-run fill pieces over doors.
- Method: manufacturer calculators ask for perimeter, height, vertical repeat, roll width and waste percentage, and label the output "an estimate only" ([Momentum listing](https://momentumco.com/products/09239932), primary). The method that produces a defensible number is strip-based: strips = ceil(wall length / goods width); drop length = wall height + trim allowance, rounded up to the next full vertical repeat for matched patterns; LY = strips x drop / 36. Worked example (derived), using this project's 10.3 LF at 10'-0" high, 54" goods, 25.25" repeat and 4" trim allowance: net area 103 SF equals 7.63 LY by area / 13.5; strips = ceil(10.3 x 12 / 54) = 3; drop = 124" rounds to 126.25" (5 repeats); LY = 3 x 126.25 / 36 = 10.52. The area-only figure understates the buy by about 38 % because the strip count rounds up and the drop rounds to the repeat. The app engine's formula (net SF / width x drop / height / 3) gives 8.03 LY for the same inputs (derived from [wall-finishes.ts](file://TakeoffSpeed repo: lib/quantities/trades/interiors/wall-finishes.ts), project), which is a scaled area rather than a strip count, so it also understates when the wall is not an exact multiple of the goods width.
- Waste: sources agree on direction but not on numbers. A larger vertical repeat means more waste per drop; random match wastes least; half-drop and multi-drop matches waste more ([blog-level wall covering calculators, search summary](https://production.matthewmarks.com/?p=24436)). A common budget number is 10-15 % on area-derived yardage; once a drop-by-drop cutting plan exists, only a small extra for damage and dye lot is justified. I found no standard that sets either number.

### 5.6 Primer and adhesive for wall covering

Spec paragraphs require a manufacturer-approved primer and adhesive and say to apply adhesive to the wall covering back ([VA 09 72 16](https://www.wbdg.org/FFC/VA/VAASC/VA%2009%2072%2016.pdf), primary). Adhesive coverage varies by product; there is no neutral number to cite, so the AI should read it from the product data or leave the quantity open.

---

## 6. Common mistakes and how to check a takeoff

1. **Dividing total SF by sheet or board area.** FRP sheets and backer boards are bought by the piece; a 16-SF wainscot still needs one 32-SF sheet. Check: sheets from a per-wall layout, with offcut re-use only where size and orientation allow.
2. **Treating wall covering as area.** Strips round up and drops round to the pattern repeat (section 5.5). Check: compute both the area figure and the strip figure and explain the difference.
3. **Wrong band height.** Using the wall height for a wainscot, or ignoring "next full tile" rounding (section 3.3). Check: the elevation dimension line against the tile module.
4. **Deducting small penetrations from the purchase quantity.** Outlets and faucet holes save no tile or sheet (blog-level, [DG Floors](https://dgfloors.com/wall-tile-calculator/)). Check: report net installed SF and purchase quantity separately.
5. **Missing trim LF.** Top edge, base cove, outside corners, exposed ends, jambs and window returns each need a trim; missing any silently shorts the job. Check: for every tiled band, list top edge, bottom edge, each vertical end and each outside corner (the Schluter strips on A-410 are the example).
6. **Missing the substrate change.** Tile and FRP walls need water-resistant gypsum or cement board (A-620 note N, project). Check: cross-reference the partition takeoff for the same walls.
7. **Painting behind FRP or tile.** Crane warns paint prevents adhesive cure ([Crane guide](https://pdf.lowes.com/productdocuments/c8b0c4ed-f527-420b-8cca-7bb080d2f995/49012583.pdf), primary). Check: remove those walls from the paint area.
8. **Mixing units.** Trim SF vs LF; wall covering SF vs LY; thinset in bags vs SF per bag. Check: write the unit on every intermediate number.
9. **Applying waste twice.** Applying a blanket percentage on top of a layout-based sheet count or a repeat-rounded drop duplicates overage. Check: waste is applied once, to the net quantity, with a stated basis.
10. **Forgetting attic stock or counting it as waste.** Specs set attic stock as a separate full-unit quantity (section 7).
11. **Ignoring unit-count checks on tile.** Cross-check tiles: net SF x tiles per SF vs cartons x pieces per carton.
12. **Using one grout joint or thickness for everything.** Joint width and tile thickness change grout use by multiples (section 5.2).

Reasonableness checks (derived): tiles per SF for the module; 4x8 sheet = 32 SF and 8 LF at 4' high; 54" goods = 13.5 SF/LY; 2.5 m trim = 8.20 ft; tile bags 100/60 to 100/100 per 100 SF depending on notch.

---

## 7. Attic stock and submittal quantities (kept separate from waste)

- Tile: a master spec asks for full-size units equal to 3 percent of the amount installed for each type, composition, colour, pattern and size ([Daltile 09 30 13](https://digitalassets.daltile.com/content/dam/Daltile/website/resources/trade-professionals/architects-designers/AD_fillableform.pdf), primary). The project spec asks for 10 percent attic stock of tiling materials ([Spec 09 30 00, project, `spec-p282.txt`](file://text/spec-p282.txt)). Read the number from the project, not from a default.
- Wall covering: one university master spec asks for full-size units equal to 5 percent of the amount installed, all from the same print run or dye lot ([University of Houston 09 72 00](https://www.uh.edu/facilities-services/departments/fpc/master-specs/09-72-00-wall-coverings.pdf), primary).
- Dye-lot rule for wall covering: use wall covering of the same batch or run in each area and rolls in consecutive numerical sequence ([VA 09 72 16](https://www.wbdg.org/FFC/VA/VAASC/VA%2009%2072%2016.pdf), primary). The buy quantity should be made in one order.

---

## 8. What an AI takeoff must read from the drawings and specs

From the finish legend / schedule: tag, product (size, manufacturer, model, colour), grout tag, transition / trim product and finish, and for wall covering the width, repeat and match (often "varies by market" or not stated, which must be flagged rather than guessed). From interior elevations: band heights, wall extents and any "next full tile" dimension, top-edge and base trims, corner and end conditions, opening dimensions inside the band, movement joints. From partition schedule: the substrate behind each tile or FRP wall. From the spec: setting-mortar standard, grout type, trowel notch if stated, backer, membrane, attic stock percentage, whether FRP or wall covering sections exist at all. From product data (if provided): tile thickness and SF per carton, FRP sheet size and moldings, wall covering width / repeat / roll size.

Rules for the model:
- Return a net installed quantity per tag, then a purchase quantity with the pack size and rounding rule used, then the waste or attic-stock percentage and where it came from.
- If tile thickness, joint width, or trowel notch is not stated, return grout and thinset as "not computable" or as a range with the assumption stated.
- Do not invent a wall covering as a finish just because a primer-only paint tag exists. In this project the estimate does list an assumed wall covering at the PT-7 primer-only paint area, marked "ASSUMED WALL COVERING, V.I.F" (`reference/estimate/lines.json` line 240, project); an AI should carry such an item at low confidence and flag it.

---

## 9. This project as a calibration case (project, quantities only)

Measured in the markups (`reference/markups/legends.json`) versus the estimate lines (`reference/estimate/lines.json`), computed in Python (derived):

| Tag | Markup pages summed | Markup SF | Estimate SF | Difference |
|---|---|---|---|---|
| WT-1 (3"x12") | A-410 120.7 + A-703 15.3 + A-705 8.2 | 144.20 | 144.19 | 0.01 |
| WT-2 (3"x12") | 43.8 + 1.4 + 1.6 | 46.80 | 46.72 | 0.08 |
| WT-9 (3"x12") | 50.6 + 1.3 + 1.3 | 53.20 | 53.22 | -0.02 |
| WT-3 (6"x12") | A-700 38.4 | 38.40 | 38.42 | -0.02 |
| FRP-1 (48" H) | 4 LF at 4'H | 16.0 | 16.0 | 0.0 |
| Wall covering at PT-7 | 10.3 LF at 10'H | 103.0 | 103.0 | 0.0 |
| Schluter cove trim | | 51.9 LF | 51.87 LF | |
| Schluter trim | | 39.6 LF | 39.55 LF | |

Findings: (1) the estimator's wall-finish quantities equal the measured markup totals, so they are net installed quantities with no waste, no attic stock, and no pack rounding; (2) the estimate carries one tile line per tag, one bullnose tile base line (WT-8, 11.28 LF, in the BASE section, 3"x12" Roca Flow), one line per Schluter profile (TRANSITION section), and cement backer in the WALLS section (5/8" cementitious backer board 285 SF and 1/4" backer board 40 SF, lines 266 and 272), which is within 2.5 SF of the 282.55 SF of wall tile (WT-1, -2, -3, -9) (derived), so backer area follows the tile area; (3) the estimate has no separate thinset, wall-tile grout, FRP molding, FRP adhesive or wall covering adhesive lines (the two grout lines, GR-1 1,050 SF and GR-3 300 SF, sit in the FLOORING section; whether they include wall tile is not stated in the line text), and WC-1 (120 SF) has no markup measurement, so its basis is unknown; (4) a check against the best-practice material breakdown shows what an AI should additionally derive: tile cartons, thinset bags, trim sticks, FRP sheet(s), FRP moldings and adhesive, and wall covering LY. These gaps are reported for calibration, not as errors in the estimate. Derived purchase-side numbers for orientation, not as targets: all four wall-tile tags total 282.55 net SF; trims 51.87 LF and 39.55 LF need 7 and 5 sticks of 8'2-1/2" (derived, ignoring splice and miter loss); one 4x8 FRP sheet covers the 16 SF of FRP-1 (derived).

---

## 10. Second-opinion check

I asked a second model provider (`tools/ask_gpt.py`, GPT-6 Astra) the same question as a cross-check only; it is not cited as a source. It agreed on: separate net, purchase and attic-stock quantities; deduct only the overlap of an opening with the band; sheets from layout not total SF; strip-and-repeat method for wall covering; corner moldings replace divider bars at that location; about 50 SF per gallon for FRP adhesive; 10 % as a starting tile allowance; and that TCNA and PCA P10 are not waste-factor sources. It explicitly refused to state a PCA P10 deduction threshold, whereas I read P10 directly (section 3.2).

## 11. Gaps (what I could not source)

- A published tile waste or opening-deduction standard (none found).
- Crane / Marlite FRP division-bar and trim stick lengths from the manufacturer's own catalogue (only distributor listings found).
- Marlite Standard FRP thickness and installation sheet (the Marlite document I read covers its decorative Plank and Panels line, not Standard FRP).
- Manufacturer coverage tables for grout by tile size and joint (Laticrete and Mapei point to charts or calculators I could not open).
- Wall covering waste percentage from a manufacturer or the Wallcovering Installers Association (not found).
- The web-search budget for this session ran out before a final pass on FRP takeoff conventions and on WIA / PDCA wall covering estimating guides.
