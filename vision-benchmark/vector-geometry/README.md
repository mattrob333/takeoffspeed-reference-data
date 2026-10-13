# Wall lengths by partition type from PDF vector geometry (prototype)

Sheet: A-120 DIMENSIONAL FLOOR PLAN (one page, 36"x24", 1/4" = 1'-0").
Ground truth: the estimator's PlanSwift takeoff of this sheet (`reference/markups/legends.json`, page 4) and
their colored markup (markup PDF page 4, a 200 dpi raster of the whole sheet).
Quantities only. This prototype has no prices.

```
python3 -I extract_walls.py          # -> results.json, overlay.png   (~2 s, pymupdf only)
python3 -I compare_to_markup.py      # -> markup_comparison.json      (evaluation only)
```

## Summary

In the benchmark, vision models measured these per-type lengths with 19-55% error. This prototype gets
the length from the PDF's own line work. The thickness family (A3 / A6 / D3 / 8" exterior) comes from the
geometry. The type letter (A vs B, A vs C) comes from the tag symbols on the sheet.

* **Detection and classification are right where the drawing has cut wall lines.** I sampled the
  estimator's markup colour under every run that got its type from a tag on the sheet. All of them
  (A3A, A3B, A6A, A6B, D3A, D3C) sit under the estimator's colour for that same type: 0 LF of tag-typed
  run is under a different type's colour.
* **As assigned with no human or AI help**, four of the six partition types are within about 12%
  (A6A +5.4%, A6B +3.2%, D3A -11.7%, D3C +1.0 ft). A3A (-21%) and A3B (+27%) are off because of **one
  7.6 ft wall piece**. The code flags that piece as ambiguous: the drawing does not say which type it is,
  and the estimator chose the other one. The six-type total is 195.9 vs 198.9 LF (-1.5%).
* **When the assignment is taken from the estimator** (an oracle, to separate measuring error from
  assigning error), the measured lengths are A3A -6.0%, A3B +4.7%, A6A +5.4%, A6B +3.2%, D3A 0.0%,
  and D3C +1.0 ft on 3.7 ft.
* **What it cannot do from the plan:**
  * walls drawn only in thin "beyond the cut plane" lines: the 4'-4" counter knee wall, the 3'-9" low
    wall, and the exterior wall with no gypsum board (NO GWB);
  * heights. The estimator's EXT rows differ only by height (12'9" / 15'9" / 4'), and those come from
    sections, not the plan;
  * A-vs-B where no tag reaches the wall.

## Scale calibration

* Nominal scale: 1/4" = 1'-0", so 1 ft = 18 pt.
* The code paired all **83** printed dimension strings of 2 ft or more with the two dimension ticks
  that bracket each one. Each tick is a 0.86 pt slash; the code takes the point where its two halves
  meet.
* Measured span / printed value = **1.00098 to 1.00100**. The PDF is uniformly about 0.1% larger than
  nominal, so the code uses 18.018 pt/ft.
* Spot checks. The dimension ticks land exactly on the stud faces the detector finds:
  * "8'-1 5/8"" (women's 111): ticks at x = 865.91 and 1012.49. These are the A6B stud faces at the
    measured A6B centerlines 861.40 and 1007.99, plus 4.5 pt (half of a 6" stud).
  * "5'-11 1/4"" (jan. 115): ticks at 609.90, which is the inside stud face of the 8" exterior cavity
    597.9-609.9, and 716.89, which is the far face of the A6B wall.

## Method (details in the `extract_walls.py` docstring)

1. **Line work.** The code keeps axis-aligned black 0.5 pt strokes; on this sheet these are the cut wall
   lines. A 5/8" board layer shows up as a second line 0.94 pt outside a face. 18 oblique 0.5 pt
   segments (door leaves) are ignored.
2. **Wall bodies (stud cavities).** A wall body is a pair of parallel lines spaced at a stud depth at
   scale, with no cut line between them:
   * 3-5/8" stud = 5.44 pt; 6" = 9.00 pt; 8" = 12.0 pt.
   * The code then looks for board lines outside each face, stretch by stretch:
     * 3-5/8" with board on both sides: A3 family.
     * 3-5/8" with board on one side: D3. On this sheet the bare face of a D3 wall is a thin 0.24 pt
       line, so a second pass allows that.
     * 6" with board on both sides: A6.
     * 8": exterior.
     * 6" with board on one side: reported separately.
     * Cavities with no board on either side are "bare cavity", not walls. On this sheet that is the
       booth bench back.
   * Patterns are matched most-specific first, and each accepted body claims its lines. Without this,
     a D3 board line plus an unrelated booth line 12 pt away read as an 8" exterior wall.
   * A short stretch inside one cavity that has lost a board on one side keeps its neighbour's class.
3. **Runs.**
   * Collinear bodies are merged across junction gaps of 14 pt or less, where a crossing wall breaks a face.
   * A gap of 90 pt (5 ft) or less that contains door-frame strokes (0.79 pt) is an opening. **Gross**
     runs through openings, which is the estimator's convention. **Net** removes them.
   * A run end is extended to the centerline of the partition it butts into. Against an exterior wall,
     the run stops at the exterior wall's inside face.
   * Runs are cut into pieces at every T-junction.
4. **Types.**
   * Every tag (27 text spans matching `[AD]\d[A-Z]`) has a leader ending in a heavy 2.52 pt tick
     drawn across the wall it marks.
   * The code follows tick → leader → diamond, which bound all 28 ticks, then gives the tag to the
     piece the tick crosses.
   * An untagged piece takes the type of the nearest tagged piece **of the same thickness family**
     through the junction graph. The cost is feet travelled plus 0.5 ft per corner, so a straight
     continuation wins a tie. If the runner-up type is within 1 ft, the piece is flagged
     `propagated-ambiguous`.
   * Pieces with no tagged neighbour stay `untagged <family>`. The code does not guess them.
5. **Exterior.**
   * 8" cavities are measured as solid wall.
   * As a separate figure, the exterior wall line is carried across storefront and window gaps between
     two solid runs, where parallel frame lines cover at least 70% of the gap.

Output coordinates are PDF points, with the origin at the top-left of the page. `results.json` holds the
following:
* per-type gross and net LF;
* every piece with its endpoints, thickness, type, `type_source` (tag / propagated /
  propagated-ambiguous / geometry-only), the candidate types with their path costs, and the tags that
  bound it;
* the scale samples.

The overlay (`overlay.png`) draws the measured runs in each type's colour:
* openings as white dashes;
* ambiguous pieces with a black dotted line;
* the exterior line through glazing as a brown dashed line.

## Comparison with the estimator (partition types, LF, all at 12'6"H)

The "Vector, as assigned" column is fully automatic: tags, then propagation, with flagged and untagged
pieces left as the code assigned them. The last two columns take each of our runs and give it the type
the estimator coloured over it (`compare_to_markup.py`). That isolates measuring error from assigning
error, but it uses the answer key, so it is not something the system can do by itself.

| Type | Estimator | Vector, as assigned (gross) | Error | Vector net (doors removed) | Our LF under estimator's colour | Error |
|---|---:|---:|---:|---:|---:|---:|
| A3A | 49.9 | 39.2 | -21.4% | 39.2 | 46.9 | -6.0% |
| A3B | 34.2 | 43.4 | +26.9% | 30.9 | 35.8 | +4.7% |
| A6A | 36.7 | 38.7 | +5.4% | 35.6 | 38.7 | +5.4% |
| A6B | 28.4 | 29.3 | +3.2% | 26.2 | 29.3 | +3.2% |
| D3A | 46.0 | 40.6 | -11.7% | 40.6 | 46.0 | 0.0% |
| D3C | 3.7 | 4.7 | +27.0% (+1.0 ft) | 4.7 | 4.7 | +27.0% |
| **Six types** | **198.9** | **195.9** | **-1.5%** | 177.2 | 201.4 | +1.3% |

Also produced and not included in the six types above:
* `untagged D3` 15.4 LF and `untagged A3` 2.1 LF: pieces no tag reaches.
* `6in stud, board one side` 11.2 LF.
* `bare 6in cavity` 7.7 LF (not a wall).

Gross is the comparable column, because the estimator runs through doors.

### Other estimator rows

| Estimator row | Estimator LF | Vector | Notes |
|---|---:|---:|---|
| EXT 8" @12'9" + @15'9" + @4'H + @15'9" NO GWB | 89.7+41.5+13.0+8.7 = 152.9 | 87.3 solid + 39.0 through glazing = 126.3 (-17%) | Of the solid 8" runs, 75.2 LF are under the estimator's 12'9" colour and 10.3 under 15'9". The split by height is not in the plan. The south "A" storefront line, 12.96 LF, matches "EXT 8" @4'H" (13.0). Misses: the G and H storefront lines (the bridge needs a solid 8" run at both ends of the gap) and the thin-line NO GWB wall. |
| EXT 6" @12'3" | 9.2 | 11.2 (`6in stud, board one side`) | 8.6 LF of it is under the estimator's EXT 6" colour. The remaining 2.67 LF is a stretch of the north wall behind the ATM, x 1025-1073. Our geometry finds a 6" cavity there (lines 486.17/495.18 with board 496.11); the estimator ran their 8" line through it. |
| PARAPET @7'2" | 5.9 | 5.94 | This is the gap span across the ATM bump-out opening (x 1092-1199). The code reports it inside "through glazing", so its label is wrong: it is an open parapet. |
| 6" & 3-5/8" BS 1/2" SHTNG @18'8" | 8.4 | ~6.7 as `untagged D3` (west pier 3.4 + SE pier 3.25) | Found, but untyped. |
| 6" METAL STUD @4'4" BS GWB | 18.3 | 0 | Counter knee wall along y ≈ 944 pt, x 1009-1330. It is drawn only in thin grey lines (below the cut plane), so it is missed by design. |
| A3A @3'9"H (NO INS) | 7.7 | 0 | Along x ≈ 794 pt, y 1229-1358, the line of door pair 101 between the weather vestibule and the entry. There are no cut wall lines there. |

## Where and why it disagrees (checked against the estimator's markup image)

Each item below was checked by cropping the markup raster in sheet coordinates (7199/2592 px per pt)
next to our overlay. Most of them are also listed automatically in
`markup_comparison.json`.

1. **A3B → A3A, 7.6 LF: the only assignment error among the partition types.**
   * Where: the wall above the ELEC./I.T. room 106, piece id 9, (801.25, 738.51)-(937.98, 738.51).
   * It is the straight continuation of the tagged A3B meeting-room/vestibule wall, across door 106.
   * It also meets, end to end, the tagged A3A wall on the west side of the electrical room. That wall
     butts into it at x = 801.
   * No tag touches the piece. The costs are A3B 7.6 and A3A 8.1, so the code picks continuation and
     flags the piece as ambiguous.
   * The estimator coloured it A3A, so the whole electrical room is enclosed in A3A. That is room-level
     reasoning ("this room is an A3A enclosure"), and the tags alone do not determine it. Assigning it
     the other way would make A3A 46.8 and A3B 35.8.
2. **D3A -5.3 LF: the box at the top of the service counter.**
   * Pieces 12, 22 and 64 are a small box at x 932-971, y 738-758.
   * It is made of one-sided and two-sided 3-5/8" framing, and no tag or tagged neighbour reaches it.
     The code leaves it untagged; the estimator coloured it magenta (D3A).
   * One of its sides (piece 12) has board on both faces, so by geometry it is "A3", not D3. This is a
     correct "needs a human or AI decision".
3. **A3A, 2.8 LF: across the 105 opening in the south wall of the meeting room.**
   * The estimator ran yellow across the sliding-door opening (x 714-764).
   * The opening is wider than the 5 ft bridge limit, so the code ends the run. This is a convention
     difference.
4. **Where the run ends: a few tenths of a foot per junction.**
   * The code runs partition centerlines to the centerline of the partition they meet.
   * Where a piece stands alone, its length matches the extent of the estimator's colour closely
     (ours / estimator, ft):
     * D3A: 7.90 / 7.91, and 10.76 / 10.74 (twice);
     * A6B toilet walls: 7.88 / 7.83 and 7.88 / 7.63; A6B phone-room wall: 5.64 / 5.69;
     * A6A: 5.41 / 5.22, and 10.83 / 10.32. On that last one the estimator stops at the wall faces.
   * D3C (+1.0 ft): the estimator starts each column-wrap leg at the face of the A6A wall (y ≈ 950.6).
     We start it at the A6A centerline (944.1). That is +0.36 ft on each of four legs that are only
     0.6-0.9 ft long.
   * There is no single right convention, but the app must fix one and document it.
5. **A6A +2.0 LF.**
   * The estimator's green on the south wall of the electrical room continues without a break past the
     end of the cut wall (x 1000.7) and becomes the 4'-4" knee wall. The knee wall row has the same
     green swatch.
   * So the markup cannot show where the estimator split A6A from the knee wall. The remainder is
     junction convention (item 4).
6. **Untagged D3 not in the estimator's takeoff, 5.5 LF.**
   * A one-sided furring box behind the transaction bar at grid B (pieces 23 and 70, x 1335-1428,
     y 931). It is real framing with board on one side, but the estimator did not count it.
   * It is either an omission by the estimator or something they count with millwork.
7. **Exterior.** The solid 8" stud runs and the window gaps between them are reliable. Corner storefront
   runs (G, H) and the thin-line exterior wall east of the entry are missed. Heights, which are what
   separate four of the estimator's rows, are never in the plan.

## What fails, or would fail on other sheets

* **Stroke conventions are drawing-set specific.** Each sheet needs its own style profile:
  * this sheet uses 0.5 pt cut lines, 0.94 pt board layers, 0.24 pt bare faces, 0.79 pt door frames,
    2.52 pt tag ticks and 0.86 pt dimension slashes;
  * a different CAD template, or a PDF flattened from a scan, breaks the patterns. A raster-only PDF
    has no geometry at all.
* **Orthogonal only.** Angled and curved walls are ignored. On this sheet there are none.
* **Below-cut-plane walls** (knee walls, low walls, walls with no board) are drawn as thin
  "beyond" lines, like millwork. They are deliberately not measured, because pairing thin lines
  produces many false walls from casework.
* **A vs B, and A3A vs A3A@3'9".** These share geometry, so only tags, schedules or room context can
  decide them. Heights never come from the plan.
* **Untagged islands** stay untyped (17.5 LF here). That is correct behaviour, but it leaves work
  for someone.
* **Tolerances.**
  * The thresholds are physical sizes converted at scale: stud depths, a 5/8" board, a 9" junction gap
    and a 5 ft opening.
  * They are not fitted to the answer. One convention choice was made after looking: partitions stop
    at the inside face of an exterior wall. That changed A6B from 30.8 to 29.3 and D3A from 42.2 to
    40.6. D3A moved away from the estimator's total, not toward it.
* **Bridging doors.**
  * Door evidence is "0.79 pt strokes in the gap". A collinear wall continuing across a corridor with
    no door would correctly not bridge. A door frame drawn with another stroke weight would not bridge
    either: net is right, gross is low.
  * The 5 ft cap misses wide openings (item 3).

## Recommendations for TakeoffSpeed: the AI classifies and assigns, the code measures

1. **Code measures every length.** Never let the model emit a length. Build a deterministic
   `lib/geometry/walls` stage that does what `extract_walls.py` does and writes candidate wall pieces:
   * endpoints in PDF points;
   * thickness family;
   * board faces;
   * opening spans;
   * junction graph;
   * net and gross length.

   Lengths should stay in integer units (for example 1/16 in, or millipoints) until display, the same
   discipline as integer cents. Show `—`, not `0`, when geometry was not found.
2. **Calibrate scale automatically and gate on it.** Pair the printed dimension strings with their
   ticks, as here (83 samples, spread 0.002%).
   * If the spread is above about 0.5%, or there are fewer than 5 samples, stop and ask the user to
     calibrate.
   * Never trust the title-block scale alone.
3. **Use the AI for what it was good at in the benchmark: reading and classifying.** Its calls are
   cheap and bounded.
   1. **Style profile.** Show the model a crop with candidate strokes highlighted, plus a histogram of
      parallel spacings, and have it say which stroke class is cut walls, boards, door frames and tag
      leaders. The code then tests the claim: stud-depth spacings must appear.
   2. **Tag legend and schedule.** Read the partition schedule (A-620) into
      `{tag → stud depth, board each side, height}`, and check it against the measured thickness
      family. A tag that disagrees with the geometry is a warning: wrong leader binding, or a wall
      that changes type at a junction.
   3. **Resolve only what the code flags.** For each `propagated-ambiguous` or `untagged` piece, send a
      small crop with the piece highlighted, its candidate types and path costs, and the room names on
      either side. Ask for a choice, `unknown` allowed, and a one-line reason. Here that is 1 ambiguous
      piece (7.6 LF) and 7 untagged pieces in 4 groups (17.5 LF), instead of the model measuring 200 LF.
   4. **Heights and exterior assemblies come from sections and elevations.** Do not take them from the
      plan. Exterior pieces get a height class from sections A-300 and A-310 through the AI; the code
      keeps the length.
4. **Expose the uncertainty in the takeoff.** Each line item should carry:
   * LF by `type_source`: tag / propagated / AI-assigned / user;
   * the ambiguous LF;
   * LF measured but untyped;
   * LF the user added by hand.

   An estimator reviews about 25 LF of flagged pieces on an overlay like `overlay.png`, not the whole
   sheet. Untyped LF must block a "final" quantity, the same way unknown labor blocks a final bid.
5. **Make conventions explicit settings, and record them on the takeoff.** Gross vs net at openings;
   bridge limit; partition ends at centerline or at face. Item 4 of the disagreements is worth about
   1-3% per type on its own.
6. **Fallbacks.** If the sheet has no usable vector walls (raster PDF, or style profile check failed),
   fall back to the vision path, and label the result clearly as an estimate. Walls drawn only in thin
   lines are a known gap: list them as "possible low walls / not measured" for the user, instead of
   pairing thin lines automatically.
7. **Regression test.** Keep this sheet as a fixture. With the estimator's assignments, measured
   lengths must stay within 6% per type, except D3C, which is under 1 ft of absolute error. Compare
   tagged runs against the markup's colours: tag-typed runs must stay 100% in agreement.
   `compare_to_markup.py` already computes both.

## Files

* `extract_walls.py`: the extractor (python3 -I, pymupdf only, deterministic, about 2 s).
* `results.json`: scale samples, counts, per-type LF (gross/net), and every piece with endpoints,
  type, source and candidates.
* `overlay.png`: the measured runs coloured by type over the plan.
* `compare_to_markup.py` and `markup_comparison.json`: evaluation against the estimator's colour
  markup. It produces a per-run colour reading, a confusion table in LF, and clusters the estimator
  marked that we did not measure.
