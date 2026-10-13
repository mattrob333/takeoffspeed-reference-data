P='/home/user/takeoffspeed-reference-data/trades/01-demolition/app-gaps.md'
s=open(P).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a[:70]
    s=s.replace(a,b)
rep("""- **Measured lines are a plain Σ of runs or areas**, the same rule the estimator used. With the legend
  inputs from `fixtures.json` the engine reproduces lines 2, 5–15 exactly.""",
"""- **Measured lines are a plain Σ of runs or areas**, the same rule the estimator used. With the legend
  inputs from `fixtures.json` (its `engineInputs` strings) the engine reproduces lines 2, 5–15 exactly
  and lines 3–4 within 0.02%: all 14 `expectedLines` pass (checked by running `expandMeasurements` on
  the 12 fixtures). Line 8 only comes out of the ramp record (`stairSteps` on `demolition.pavement`,
  which requires `description` and `areas`), and line 15 only out of the storm record (`structures` on
  `demolition.utility`, which requires `utility` and `runs`).""")
rep("""| 5 | Trees label | `REMOVE EXISTING TREE (SIZE NOT SHOWN)` | `REMOVE EXISTING TREES/VEGETATION` | Label only. |""",
"""| 5 | Trees label | `REMOVE EXISTING TREE (SIZE NOT SHOWN)` | `REMOVE EXISTING TREES/VEGETATION` | Label only. |
| 6 | Building label | `2: REMOVE EXISTING 2 STORY BUILDING STRUCTURE AND FOUNDATION — 4,489.1 SF FOOTPRINT × 20' H` (numeral storey count plus a footprint × height suffix) | `2: REMOVE EXISTING TWO STORY BUILDING STRUCTURE AND FOUNDATION` | Label only. `tests/quantities/site-demolition.test.ts` asserts the `2 STORY` form. |
| 7 | Storm line label | `4: REMOVE EXISTING 15" HDPE STORM SEWER LINE AND ASSOCIATED STRUCTURES - ASSUMED` (size and material from the inputs) | `4: REMOVE EXISTING STORM SEWER LINE AND ASSOCIATED STRUCTURES - ASSUMED` | Label only. |""")
rep("""   - `LF ≈ ticks × pitch`: 5.0 ft for `///`, 2.0 ft per `++++` pair at 1" = 20'.
   - `SF ≈ dots × pitchX × pitchY`: 4.34 SF per dot here.

   These checks hit −0.5% to +2.1% on this job. They would let the engine flag a traced quantity that is
   off by more than about 3%.""",
"""   - `LF ≈ ticks × pitch`: 5.0 ft per `///` glyph, 2.0 ft per `++++` crossing tick at 1" = 20'.
   - `LF = length of the linetype polylines`, chained in drawing order (not by shared endpoints, which
     merges the utility and curb linetypes where they cross).
   - `SF ≈ dots × pitchX × pitchY`: 4.34 SF per dot here.
   - `SF = shoelace of the outline`, closed along the building outline in path order.

   On this job the estimator sits −2.1% to +2.6% from these checks on every measured line except the
   ramp (+6.0% over its CAD outline). They would let the engine flag a traced quantity that is off by
   more than about 3%, which here would correctly flag the ramp for review.""")
rep("The `///` GAS line (about 85 LF, 17 ticks) has no keynote", "The `///` GAS line (87.1 LF, 17 ticks) has no keynote")
rep("(gas, about 85 LF)", "(gas, 87.1 LF)")
rep("""6. Tests: add `fixtures.json` from this folder to `tests/quantities/site-demolition.test.ts` as a
   golden for this job (14 cases, tolerances 0–0.5%).""",
"""6. Tests: add `fixtures.json` from this folder to `tests/quantities/site-demolition.test.ts` as a
   golden for this job: 12 records with 14 `expectedLines`, tolerances 0–0.5% (0.1% on the CFT lines).
   The test harness passes inputs as strings, so feed `engineInputs` (`"442.4 SF"`, `"987.2 LF"`,
   `"10'"`, `"7"`, `"yes"`), not the `{value, unit}` objects in `inputs`, and match lines by `key`.""")
open(P,'w').write(s)
