p='/home/user/takeoffspeed-reference-data/trades/09e-painting/reading-guide.md'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1,(a[:70],s.count(a)); s=s.replace(a,b)
rep("""1. **A-170 SCHEDULES**, group "PAINT". This is a raster table with no text layer, so read it as an image (zoom ≥ 3). It is the tag dictionary:""",
    """1. **A-170 SCHEDULES**, group "PAINT" (and the CEILINGS group row `GWB-1 PAINTED GYP. … PT-3`, which ties painted gypsum ceilings to PT-3). This is a raster table with no text layer, so read it as an image (zoom ≥ 3). It is the tag dictionary:""")
rep("""**08 1113** p214 says the frames ship primed.""",
    """**08 1113** p214 says the frames ship primed, while 09 9110 still lists a primer system for HM frames (see trap 6).""")
rep("""| Elevation-traced areas | A-410 elevations A–D above the tile band; A-704 recess | `PT1 WALL PAINT 252.6 SQ FT` (both restrooms); `PT6 37.2 SQ FT` |""",
    """| Elevation-traced areas | A-410 elevation A full height less the door, B–D above the tile band; A-704 recess | `PT1 WALL PAINT 252.6 SQ FT` (both restrooms; the estimator's copy of A keeps the door, about 23 SF); `PT6 37.2 SQ FT` |""")
rep("""1P + 2C on walls and ceilings; PT-7 = primer only; HM frames shop-primed |""",
    """1P + 2C on walls and ceilings; PT-7 = primer only; HM frames shop-primed (field primer carried by convention, flag it) |""")
rep("""A-130 note E says "ALL GYPSUM BOARD CEILING PAINTED … ARE TO BE PT-1", while the same sheet tags the ceilings `PT-3` and A-170 defines PT-3 as FLAT. Note G says all ceilings flat, so take PT-3, as the estimator did, and log an RFI.""",
    """A-130 note E says "ALL GYPSUM BOARD CEILING PAINTED … ARE TO BE PT-1", while the same sheet tags the ceilings `PT-3`, A-170 defines PT-3 as FLAT, and the A-170 FINISHES SCHEDULE CEILINGS group has the row `GWB-1 | PAINTED GYP. | - | - | - | PT-3`, which assigns PT-3 to painted gypsum ceilings outright. Two schedule sources (the RCP tags and the GWB-1 row), plus note G "ALL CEILINGS TO BE FLAT", outweigh the one general note, so take PT-3, as the estimator did. Log an RFI to close note E, but the schedule supports PT-3.""")
rep("""On the tech wall, PT-6 (the recess back) sits inside the PT-4 run, so subtract it from PT-4 or you count it twice. The recess ret""",
    """On the tech wall, PT-6 (the recess back) sits inside the PT-4 run, so subtract it from PT-4 or you count it twice. The recess ret""")
open(p,'w').write(s)
