P='/home/user/takeoffspeed-reference-data/trades/01-demolition/README.md'
s=open(P).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a[:70]
    s=s.replace(a,b)
rep("""Each measured line was also checked against the CAD vector layer of C-1.0, independently of PlanSwift
(see `reconciliation.csv` notes):""",
"""Each measured line was also checked against the CAD vector layer of C-1.0, independently of PlanSwift
(see `reconciliation.csv` notes). **Against CAD, 8 of the 9 single-value checks fall within 3% (4 of them
within 1%), the handrail sits inside its CAD bracket, and the ramp is the one outlier at +6.0%.** These
are cross-checks of the trace, not the reconciliation itself, which is against the legend above.""")
rep("| 2 curb | 982 curb-demolition tick halves × 1.0 ft (one tick pair per 2.0 ft) | 982 LF | +0.53% |",
    "| 2 curb | length along the 10 site curb-linetype polylines (≈ 484 crossing ticks × 2.0 ft = 967 LF) | 975.2 LF | +1.2% |")
rep("| 4 1-storey footprint | hatched rectangle 52.4' × 32.9' | 1,716.4 SF | −0.16% (on SF) |",
    "| 4 1-storey footprint | hatched outline polygon (≈ 52.1' × 32.9' effective; bounding box 52.4' × 32.9') | 1,716.4 SF | −0.16% (on SF) |")
rep("| 5 sidewalk | L-shaped walk polygon closed on the building line | 380.8 SF | +2.5% |",
    "| 5 sidewalk | L-walk closed on the building line 331.3 SF + south apron 49.0 SF | 380.3 SF | +2.6% |")
rep("| 7 ramp | sidewalk/ramp polygon north of the 2-storey building | 467.8 SF | −5.4% (the trace stops at the stair and the rail) |",
    "| 7 ramp | sidewalk/ramp outline closed along the 2-storey building (406.4 SF) + west pad (10.8 SF) | 417.2 SF | +6.0% |")
rep("""| 8 steps | tread lines: 5.56 ft run, ≈9.5" treads | 7 treads | 0 |""",
    """| 8 steps | drawn step lines from the top landing to the walk (unequal spaces, 7.7"–18.7") | 7 lines | 0 |""")
rep("| 12 power | (222 − 11 water − 17 gas) utility ticks × 5.0 ft | 970 LF | −0.48% |",
    "| 12 power | length along the 7 dry-utility (OHP/UGP/TEL) polylines (194 `///` ticks × 5.0 ft = 970 LF) | 983.4 LF | −1.8% (−0.48% on ticks) |")
rep("""- **Gas line:** a ticked `///` GAS line about 85 LF long (17 ticks × 5 ft) runs from the west curb to the
  A/C pad""","""- **Gas line:** a ticked `///` GAS line 87.1 LF long (17 ticks; 16 full 5 ft pieces plus two 3.5 ft
  ends) runs from the west curb to the A/C pad""")
open(P,'w').write(s)
