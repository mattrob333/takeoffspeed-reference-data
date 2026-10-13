# 10 — Specialties: TakeoffSpeed engine gaps

Compared with `TakeoffSpeed repo: lib/quantities/trades/fitout/specialties.ts` and `fitout/shared.ts` (`countOf`,
`responsibilityOf`). I ran the engine on this job's inputs with
`npx tsx trades/10-specialties/scripts/run-engine.ts`, which imports the engine directly and edits nothing.

## What it already does right

| Line(s) | Engine assembly | Engine output with this job's inputs | Estimator |
|---|---|---|---|
| 322–331 | `specialties.toilet-accessory` | Counts per room summed, one line per tag × size × responsibility: TA-1/2/5 → `OFCI` from "OWNER VENDOR / GC"; TA-4/6/8/10 → `CFCI`; 18" VERTICAL 2, 42" HORIZONTAL 2 | identical (2, 2, 2, 2, 1, 2, 1, 2, 2, 2) |
| 332–334 | `specialties.signage` | `6"x4" TACTILE SIGNAGE` 3; `6"x9" ADA MEN TOILET SIGNAGE …` 1; `6"x9" ADA WOMAN TOILET SIGNAGE` 1 | identical |
| 335 | `specialties.fire-extinguisher` | `RECESSED FIRE EXTINGUISHER CABINET W/ 10 LB 4A:80B:C` 2; the engine's own step says "extinguisher carried inside the cabinet line" | 2 (line reads only "FIRE EXTINGUISHER CABINET"; see gap 4) |
| 336 | `specialties.panel-system` | faces `32" x 108"` + `16" x 108"` → **36 SF** | 36 SF |

With correct inputs all 15 lines come out exactly. The arithmetic is right. Every gap below is about inputs and
expansion rules, where the model has to read the drawings correctly.

## Gaps, ranked by quantity impact (omissions on this job first, then risks of a wrong read)

1. **No grab-bar set expansion: 2 EA missed (36" rear bars).** The assembly treats each size as its own record ("each
   size is its own record"), so the result depends on the model finding every bar in the elevations. On this job the
   estimator found 2 of the 3 sizes.

   *Change:* add `specialties.grab-bar-set`.
   - **Inputs:** `accessibleWC` count, `side` (default 42"), `rear` (default 36"), `vertical` (default 18", may be 0).
     Optional `ambulatoryWC` adds 2 × 42" side bars per ambulatory stall (ADA 604.8.2).
   - **Output:** one EA line per size: `count × 1`.
   - **Warn** when the plan has a TA grab-bar tag but no rear bar was read.
   - **Expected on this job:** 42" 2, 36" 2, 18" 2. Tests: ADA 2010 §604.5.1/604.5.2.

2. **No cross-trade dedupe for coat hooks: 2–4 EA risk.** TA-09 says "REFERENCE DOOR HW SCHEDULE". The
   `doors-hardware` hardware-set line (line 205, set 11.0 × 2 doors) already contains "2 Coat Hook RM817". The engine
   emits `ta:TA-9` (2 EA, `UNSTATED` responsibility) and the hardware set independently.

   *Convention (same as `best-practices.md` §1 and `formulas.md`):* the hardware set carries the hooks (set 11.0: 2 RM817
   per door × 2 doors = 4); the TA-09 plan count (2) is a cross-reference, not a second quantity. The estimator carried
   both, so `fixtures.json` L327 still expects 2 to reproduce the estimate, with a note.

   *Change:*
   - In `toiletAccessory`, accept `carriedIn: 'door-hardware'`. If the schedule MODEL column matches `/door h\.?w|hardware
     schedule/i`, keep the record with its plan count but warn "TA-9 also listed in hardware set 11.0 (2 per door): carried
     in Div 08, do not price twice", and name the hardware set.

3. **Accessory counting overcounts by about 69 % if the model counts text instances: +11 EA.** If the model counts
   every TA tag in the A-410 text layer, the elevations add 11 tags to the 16 on the plan:

   | Tag | Plan | Text layer |
   |---|---|---|
   | TA-1 | 2 | 4 |
   | TA-3 | 2 | 4 |
   | TA-10 | 1 | 2 |
   | TA-2, TA-4, TA-5, TA-6, TA-9 | 2 each | 3 each |
   | TA-8 | 1 | 2 |

   That is 27 against 16.

   *Change:* the `count` input's `read` text should say "count on the ENLARGED PLAN only; elevations repeat the plan
   tags". Add a check that warns when `count` exceeds the number of rooms that carry the tag × 1.

4. **Fire extinguisher: the cabinet line silently absorbs the extinguishers, and there is no rating check.** Spec 10 44 13
   refers the extinguishers to a separate section, 10 44 16 (2 × 10 lb here), and estimate line 335 is the cabinet only.
   The engine's "W/ 10 LB …" description and "carried inside the cabinet line" step assert a scope the estimate does not
   show. *Change:* emit the extinguishers as their own record (or a warning "extinguishers not carried") unless
   `extinguisherByOthers` is set. The engine also takes one `rating` string. On this job the
   legend says 4A:80B:C and spec 10 44 16 says 4-A:60-B:C. That has no quantity impact, but it does affect the
   description.

   *Change:* add an optional `specRating` input and warn when it differs from `rating`. Add `codeTableProvided` (the
   G-001 "FIRE EXTINGUISHERS PROVIDED 2") as a second count source, reconciled the same way `scheduleQty` is.

5. **No Knox box from the life-safety legend: 1 EA.** `specialties.misc-item` can carry a KNOX BOX, but nothing prompts
   for it. On this job the K.B. symbol (1) is in no estimate line.

   *Change:* in the profile or prompt for life-safety plans, enumerate every legend symbol (F.E., F.E.C., T.S., M.C.#,
   K.B., EXIT) and require a record or an explicit "not placed" for each. M.C.# is legend-only here, so it would give 0
   with a note rather than an invented count.

6. **Panel system: the "double-sided" description invites ×2: up to +36 SF.** `panel-system` sums `faces`. It is right
   with one face per field, but the read text does not say what to do with a DOUBLE-SIDED / BOTH SIDES note.

   *Change:* add `doubleSided` (flag), which goes into the description only. Its `read` text should say: "area = one face
   of each panel field from the elevation; do not double for double-sided panels".

7. **Signage: sizes come from detail sheets, not the plan.** The engine's `size` pair is optional. With no size, the
   description loses 6"x4" / 6"x9" and the 3 tactile and 2 restroom signs could merge differently by key. There is no
   quantity impact (the keys include `signType`).

   *Change:* warn when `size` is missing and the accessibility sheet (G-002) has a sign detail. Note that G-002 also
   draws a 5"x3" EXIT plaque and a 2"x8" vertical alternate exit sign; the 6"x4" in 2/G-002 TACTILE EXIT SIGN governs on
   this job, in three messages (EXIT / TO EXIT / EXIT ROUTE) that the description should carry per location.

8. **Test fixture realism (`tests/quantities/fitout-specialties.test.ts`).** The panel-system test uses `3'-0" x 6'-0" x 2
   = 36 SF`, which is not the geometry on this job. Use `fixtures.json` L336 (`32" x 108"` + `16" x 108"`) instead. Do the
   same for the accessory tests (per-room counts MEN/WOMEN, TA-8 women only).

## Inputs the engine lacks

- `carriedIn` / cross-trade reference for accessories that the schedule assigns to door hardware.
- Grab-bar set parameters: accessible and ambulatory WC count, and bar lengths per wall.
- A life-safety code-table count (`codeTableProvided`) for extinguishers.
- `specRating` for extinguishers.
- `doubleSided` flag for panel systems (description only).
