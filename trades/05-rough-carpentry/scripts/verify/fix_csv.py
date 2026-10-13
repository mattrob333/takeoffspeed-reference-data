import csv, sys
p='/home/user/takeoffspeed-reference-data/trades/05-rough-carpentry/reconciliation.csv'
rows=list(csv.DictReader(open(p,newline='')))
fields=list(rows[0].keys())
R={r['lineNo']:r for r in rows}
r=R['82']
r['notes']=("Residual -6.82 SF is NOT fully explained by legend rounding: rounding ten LF values to 0.1 ft moves the total by at most "
 "sum(0.05 x H x faces) = 5.59 SF. Using the heights the estimator measured on A-300/A-310 (4'-7 1/16\", 1'-7 1/8\", 15'-9 1/16\" on both 15'-9\" rows) "
 "gives 3,051.50 SF (-0.18%, +1.24 SF); the remaining 5.58 SF then needs every LF rounded down by the maximum, so about 1.2 SF of the residual is unexplained at printed heights. "
 "Excludes the high-low roof step wall (8/A450, 45.3 LF x 2'-0\" = 90.6 SF) although det. 8 shows 1/2\" sheathing on it.")
r=R['83']
r['source']=("markup p15 (A-311 sec. 1) green highlight '5/8\" EXTERIOR SHEATHING' in the brick knee-wall callout stack below the storefront sill (SILL 2'-8\"); "
 "markup p11 (A-200) legend 5/8\" PLYWOOD SHEATHING 52.1 SF (location unknown)")
r['sourceValues']=("knee-wall height 2'-8\" (A-311 sec. 1, F.F.E. to SILL); implied run 162.9919 / 2.6667 = 61.12 LF; nearest legend rows A-200 HALF ROWLOCK BRICK 61.4 FT "
 "(x 2'-8\" = 163.73, +0.45%) and ROWLOCK SILL 61.5 FT (x 2'-8\" = 164.00, +0.62%); separately, 52.1 SF A-200 legend area of unknown location")
r['formula']="SF = knee-wall LF x 2'-8\" (candidate; run not measured as a sheathing row)"
r['recomputedQty']=''; r['deltaPct']=''
r['classification']='unresolved (candidate chain, run not sourced)'
r['notes']=("UNRESOLVED. Primary candidate: 5/8\" sheathing on the brick knee wall below the storefront sill, 2'-8\" high (A-311 sec. 1; GPT-6 Astra ranks this first). "
 "The blue 12'-8 1/4\" markup on A-311 is the measured F.F.E.-to-roof-deck height of the 12'-9\" wall, not a sheathing or storefront-zone height; the earlier chain "
 "52.1 + 8.7 LF (NO GWB, a 15'-9\" wall) x 12'-8 1/4\" = 162.48 was a backward fit (52.1 + 8.7 x 12'-9\" = 163.03 fits as well, so the factor is arbitrary) and is dropped. "
 "Other numeric candidates: 52.1 + ACM1/ACM2 108.7 = 160.8 (-1.34%). The knee wall may overlap the full-height storefront runs already in line 82. "
 "162.9919 has 4 decimals, so it is a product of unrounded PlanSwift values; no chain is confirmed.")
r=R['85']
r['sourceValues']=("358.7 SF + 138.5 LF x 1.5 ft (fitted factor; (568.5 - 358.7) / 138.5 = 1.515 ft). A-430 det. 10 prints no 1'-0\"/6\" sheathing dimension: "
 "1'-0\" = 1\" + 10\" + 1\" is the canopy-edge depth, the bottom 6\" (to a 1/2\" joint) is the ACM soffit profile; the only sheathing it dimensions is two 5/8\" decks "
 "(2 3/4\" | 5/8\" | 6\" | 5/8\" | 2\" = 1'-0\") plus an undimensioned vertical EXTERIOR SHEATHING on 1 5/8\" stud infill")
r['formula']="SF = soffit area + edge LF x fitted wrap (best numeric fit, not drawing-supported)"
r['recomputedQty']=''; r['deltaPct']=''
r['classification']='unresolved (numeric fit on a fitted factor)'
r['notes']=("UNRESOLVED. Best numeric fit is soffit 358.7 SF + canopy edge 138.5 LF x 1.5 ft = 566.45 SF (-0.36% vs 568.5), but the 1.5 ft factor is not a printed sheathing dimension. "
 "A-430 det. 10/7: \"PLYWOOD DECK ON METAL FRAMING INFILL\" (top under RT-2 and bottom above the ACM-3 soffit) and \"EXTERIOR SHEATHING\" at the fascia. "
 "No sum of legend values or LF x printed height reaches 568.5 within 0.05. GPT-6 Astra: the detail does not support 1'-6\" of sheathing wrap per LF.")
r=R['86']
r['sourceValues']=("76.2 SF x 2 layers: top \"3/4\" PLYWOOD FRAMING. PAINTED PT-5\" (A-706) + ceiling-side PLYWOOD SUBSTRATE behind the PL-1 ceiling (A-706 det. 7/8, Z-clips; thickness not printed). "
 "The two 76.2 SF legend rows are the PT5 finish and the 6\" metal-stud booth-roof framing assembly on the same polygon, not two plywood layers")
r['notes']=("Estimator 152 = 152.4 truncated (or 2 x 76). The second layer is read as the ceiling-side substrate (an inference; the 3/4\" thickness for it is not printed). "
 "Underside could also be taken from the PL-1 ceiling area 64.2 SF (76.2 + 64.2 = 140.4, -7.6%); the estimator used 2 x roof area.")
alt=("Alternative: A-140 PARAPET WALL @ 1'7\"H is also 46.0 FT exactly (in which case 46 is unrounded); rejected because its coping detail 6/A450 shows one 2x10 nailer (line 94), "
 "while det. 8/10 at the step wall shows the stacked 2x4 + 2x6, and the olive 8/A450 run on markup p7 follows the high-low step line.")
R['91']['notes']=R['91']['notes'].rstrip()+" "+alt
R['92']['notes']=R['92']['notes'].rstrip()+" "+alt
w=csv.DictWriter(open(p,'w',newline=''),fieldnames=fields,quoting=csv.QUOTE_MINIMAL,lineterminator='\n')
w.writeheader(); w.writerows(rows)
