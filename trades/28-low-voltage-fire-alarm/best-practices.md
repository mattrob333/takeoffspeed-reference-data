# Best practice: access control, video, intrusion, fire alarm and supporting structured cabling (quantities and material types only)

Scope: Division 28 electronic safety and security (addressable fire alarm, access control, video surveillance, intrusion detection) and the Division 27 style cabling and pathway items that carry them (horizontal cable, J-hooks, backboxes, conduit stubs, racks). Prices, labor and productivity are out of scope and nothing here uses them.

How to read this file. Every factual claim carries a link. Confidence tags: **(primary)** manufacturer installation data, a code-body or government document, or the project's own drawings/specs; **(secondary)** trade-press, study-guide or vendor-engineering page; **(blog-level)** estimator blog or forum; **(search summary)** the page was found by search and the figure comes from the search result, not a full read (several publishers returned HTTP 403 to the fetch tool); **(derived)** arithmetic I did in Python on cited inputs; **(GPT second opinion)** an answer from GPT-6 Astra via `tools/ask_gpt.py`, with no source of its own (saved at `trades/28-low-voltage-fire-alarm/scripts/research/lowvoltage/gpt_q1.txt` and `gpt_q2.txt`); use it only where a primary source agrees. Project citations point at files in this repository.

Honest summary of the evidence. NFPA 72, NEC, IBC and TIA text is paywalled, so the code figures below come from manufacturer manuals, trade magazines and training sites that quote specific editions, and they disagree in places (the strobe candela table is the clearest case, section 4.3). There is no published "low-voltage takeoff standard"; counts come from the drawings and schedules, and the only conventions that are citable are (1) code spacing rules that bound device counts, (2) manufacturer per-door and per-device component lists, (3) TIA link-length and support-spacing limits, and (4) estimator conventions for cable length, slack and waste that are blog-level. The right design for an AI takeoff is therefore: count symbols and schedule tags exactly, expand each counted device into its fixed kit, measure or explicitly allow cable, and keep slack, waste and package rounding as visible separate steps. Search budget for this pass ran out before three items could be confirmed (NEC Chapter 9 Table 1 fill percentages, TIA slack figures, bank-specific security rules); they are listed in section 11.

---

## 1. What an estimator takes off, and in which units

### 1.1 Fire alarm

| Item | Unit | Rule / basis |
|---|---|---|
| Control panel (FACP), annunciator, communicator (DACT), remote power supplies (NAC / field charging), batteries | EA | One per symbol/spec requirement. Battery sets are sized by load, not counted from the plan (see 5.4). Project: spec 28 7210 s.2.2 and s.2.5 (`text/spec-p470.txt`, `spec-p471.txt`, `spec-p476.txt`). |
| Smoke / heat detector heads, and one **base** per head | EA + EA | Spec: field wiring terminates on the detector base, not the head (spec 28 7210 s.2.4 E.5, `spec-p473.txt`). Heads and bases are separate order lines on addressable systems ([GPT second opinion](#9-second-opinion-notes-gpt-6-astra)). |
| Duct smoke detector, sampling tube (sized to duct width), remote test/indicator, **control module** for fan shutdown | EA | Tube length follows duct width (manufacturer data: units operate in ducts 6 in. to 10 ft wide, air velocity 100 to 4,000 fpm; [ACI SL-2000 install sheet](https://www.cochranesupply.com/media/assets/product/documents/ACI/SL-2000-P%20Install.pdf) (search summary)). Project: detectors furnished by the fire-alarm scope, installed by the mechanical contractor, wired by the electrical contractor (spec 28 7210 s.2.4 D.4, `spec-p475.txt`). |
| Manual pull stations | EA | Count shown symbols; code placement rules in 4.2. |
| Horns, strobes, horn/strobes, speakers, speaker/strobes | EA by type and candela | A combination horn/strobe is one appliance and one box, not two ([GPT second opinion](#9-second-opinion-notes-gpt-6-astra)). Split by candela, wall vs ceiling, indoor vs weatherproof. |
| Monitor modules, control/relay modules, isolators | EA | One monitor module per supervised dry-contact input (sprinkler flow, tamper); one control module per controlled function (fan shutdown, door release) (spec 28 7210 s.2.4 E, F, `spec-p475.txt`). Count independent points, then modules; do not assume a devices-per-isolator ratio ([GPT second opinion](#9-second-opinion-notes-gpt-6-astra)). |
| Door holders (magnetic, wall or floor) | EA | Quantity from the architectural door schedule (spec 28 7210 s.2.4, `spec-p476.txt`). |
| Backboxes for every wall/ceiling device | EA | 4 in. square box for strobes (spec 28 7210 s.2.3 B.4, `spec-p472.txt`); "devices mounted in proper boxes, not extension rings" (E-160 note 2). |
| Fire alarm cable by circuit type (SLC, NAC, speaker, power) and listing | LF, then reels | See section 6. |
| Conduit (EMT, min 1/2 in.), flex drops, junction boxes (red), supports, bushings | LF / EA | Spec says all fire alarm wiring in conduit, boxes and conduit painted red (spec 28 7210 s.2.1 A, E, `spec-p469.txt`, `spec-p470.txt`); E-160 note 3 repeats min 1/2 in. EMT. |
| EOL resistors, mounting plates, protective covers, labels, test/programming accessories | EA | Per circuit / per device ([GPT second opinion](#9-second-opinion-notes-gpt-6-astra)). |

### 1.2 Access control

| Item | Unit | Rule / basis |
|---|---|---|
| Door count, by lock type and by hardware set | EA | The controlled door is the unit; expand to the kit in 3.2. |
| Readers (one per door; two for read-in/read-out) | EA | [Hanwha controller guide](https://support.hanwhavision.com/hc/en-001/articles/47256876435731) (search summary); [VT door-access details](https://www.facilities.vt.edu/content/dam/facilities_vt_edu/design-and-construction-standards/detail-library/door-access-details.pdf). |
| Electric strike / maglock / electrified lever or exit device | EA | Strike vs maglock vs exit device is a hardware-set decision ([National Lock Supply](https://nationallocksupply.com/blog/how-to-coordinate-a-complete-electrified-opening/)). |
| Request-to-exit (REX): PIR sensor, push button, or integral to the hardware | EA | Same sources; a maglock or sensor-release door also needs the code-required manual release (see 4.6). |
| Door position contact (per monitored leaf) | EA | Same sources; recessed vs surface is a hardware/frame question. |
| Power transfer (electrified hinge / EPT / door loop) | EA | Needed only when the lock or exit device on the leaf is electrified, not for a frame-mounted strike ([National Lock Supply](https://nationallocksupply.com/blog/how-to-coordinate-a-complete-electrified-opening/)). |
| Lock power supplies, door controllers/interface boards, enclosures, batteries | EA | Sized from load and capacity, not 1 per door (see 5.5). |
| Cable per door (reader, lock, REX, contact) | LF per type | See 3.2 and section 6. |

### 1.3 Video surveillance

| Item | Unit | Rule / basis |
|---|---|---|
| Cameras by schedule number (indoor dome, 360 dome, miniature board, exterior) | EA | One per bubble/symbol; schedule number = type. Project: E-150 schedule tags 3, 14, 16, 17. |
| Mount / housing / backbox / junction box per camera | EA | From the schedule installation column (E-150 schedule column "Installation requirements"). |
| Horizontal cable (Cat 6 or as scheduled), one home run per IP camera | LF, then boxes | [Horizontal cabling design](https://open-exam-prep.com/study-guides/bicsi-rcdd/distribution-design/horizontal-cabling-design) (secondary): home-run star, no daisy-chained outlets. |
| PoE switch ports, switches | EA | One port per camera; budget by class maximum (see 5.6). |
| NVR / recorder, licenses, monitors, storage (TB) | EA / TB | Storage formula in 5.7. |

### 1.4 Intrusion

| Item | Unit | Rule / basis |
|---|---|---|
| Alarm panel/control, keypads, expanders, communicator, sounder/alarm lamps | EA | Per schedule. |
| Door/roof/window contacts | EA | One magnetic contact per monitored opening or leaf ([EngineersUniverse intrusion layout](https://engineersuniverse.com/studios/physical-security/intrusion-zone-layout) (secondary): perimeter devices, no counting rule published). |
| Motion detectors (wall PIR, 360 ceiling PIR), glass-break, hold-up/panic buttons, temperature sensor, interfaces | EA | Count schedule tags exactly; coverage figures in 4.7 only bound a design-build count. |
| Zone inputs / points | EA | Hardwired zone = one panel input; addressable device = one address; keep 20 percent spare ([EngineersUniverse intrusion layout](https://engineersuniverse.com/studios/physical-security/intrusion-zone-layout)). |

### 1.5 Pathway and room items that follow from the above

J-hooks and their attachments (EA), conduit stubs/sleeves/pull strings (EA, LF), backboards, ladder rack, cable managers, grounding busbar (EA), data outlets, jacks, faceplates, patch-panel ports (EA). Project examples: E-702 keyed notes (fire-rated plywood backboard 3/4 in., two-post rack, vertical and horizontal cable managers, 18 in. ladder rack, ground bus bar).

Reporting rule that avoids most disputes: output, per device family, **plan count, schedule count, which one governs, the kit expansion, cable measured LF or allowance label, slack, waste and ordered packages** as separate numbers.

---

## 2. Which sheets and spec sections drive it

Generic (any job). Fire alarm: fire alarm plan, electrical legend (symbols are often only on the legend sheet), riser/sequence of operations, mechanical schedules (duct detector and smoke damper locations and airflow), architectural door schedule (door holders, access doors), sprinkler shop drawings (flow and tamper switches). Security: security plan with a **device schedule** that carries tag number, description, wire type and installation requirement; architectural hardware sets; electrical elevations for mounting heights; telecom room details. Division 28 sections 28 31 00 (fire detection and alarm), 28 13 00 (access control), 28 23 00 (video surveillance), 28 16 00 (intrusion detection); Division 27 (communications, structured cabling); Division 26 sections for raceways, boxes and low-voltage wiring methods; Division 08 hardware sets for electrified hardware ([Winnipeg NMS Division 28](https://legacy.winnipeg.ca/finance/findata/matmgt/documents/2017/39-2017/39-2017_NMS_Division_28.pdf) shows a typical Division 28 section list (search summary)). Which trade furnishes, installs and wires each item is a drawing-note and spec question, not a counting question (section 8).

This job's drivers (all found in `reference/sheets/index.json` and `text/`):

| Source | What it gives |
|---|---|
| E-160 Electrical Fire Alarm Plan | Device symbols (F, FACP, FAA annunciator, "D"), notes 1-8: 80 in. min lens height, 14 AWG strobe/horn wire, Belden 8760 shielded for speakers, min 1/2 in. EMT, conduit 12 in. above ceiling at wall penetrations, max 20 devices per power supply, all devices 110 cd unless noted, no splices. No legend on the sheet itself. |
| E-001 Electrical legend | Symbol definitions (security device codes DC, GB, HD, HU, KP, MD, PB, SEC, tele/data outlets; raceway symbols). |
| E-150 Electrical Security Plan | 20-row security device schedule (tag, description, wire, installation requirement), sheet notes 1-12, plan keyed items. |
| E-100 / E-700 / E-701 / E-702 / E-703 / E-704 | Data outlets and power at security equipment; elevations (mounting heights, security panels, data rack, backboard). |
| E-002 Electrical general notes | Free-wiring of low voltage permitted only above accessible ceilings, plenum-rated listed cable, and other wiring-method rules (note 22). |
| E-800 riser diagram | Cross-check for panels and risers (text layer is mostly general notes). |
| Spec 28 7210 Life Safety Systems (spec p.465-477) | Fire alarm products, circuits, batteries, notification and initiating device rules. |
| Spec 28 7250 Security System (spec p.478-480) | **Does not match this building**: lists a warehouse, office, vault, vehicle repair building, a Wells Fargo SMT-4 panel, "12 overhead door contacts", a "Passway 2-card access system" and a second floor. Treat as stale boilerplate; the E-150 schedule governs. |
| Spec 26 1000 (referenced by 28 7210 s.2.1 A for conduit) | Raceway methods. |

---

## 3. Standard measurement and expansion rules

### 3.1 Counting devices

- **Count plan instances, not legend rows.** Count symbols on the plan sheets; legends, typical details and enlarged duplicates are excluded ([GPT second opinion](#9-second-opinion-notes-gpt-6-astra)).
- **Security devices are counted by schedule tag number.** Each plan bubble is a tag; the schedule maps tag to description, wire and installation. In this job 19 of the 20 schedule tags are carried in DIV 28 (tags 2-20). Tag 1, the alarm panel, is the DIV 26 SECURITY PANEL line 581. 18 of those 19 match the drawing. Tag 18 is 3 on the drawing but 2 in the estimate, because the estimator missed the teller-line AI (derived from `reference/markups/legends.json` page 47 and `reference/estimate/lines.json`; e.g. tag 16 "360 IP dome camera" 10 EA, tag 3 "IP dome camera indoor" 8 EA, tag 4 reader 5 EA, tag 6 electric strike with LBM 4 EA).
- **Fire alarm symbols are often unlabelled on the plan** ("F" for pull station or notification appliance, tags like FAA). The legend (E-001), the markup legend and the estimate resolve them: this job has 2 pull stations, 9 ADA horn/strobes, 3 ADA visual appliances, 1 smoke detector, 1 FACP, 1 annunciator (`reference/markups/legends.json` page 48; `reference/estimate/lines.json`).
- **Combination symbols**: a horn/strobe is one device and one box; a speaker/strobe likewise ([GPT second opinion](#9-second-opinion-notes-gpt-6-astra)). Keep wall vs ceiling mounted and the candela as part of the type.
- **Where the drawing and the spec disagree, the drawing's device count governs the count and the spec governs the product and wiring method**, and the disagreement is flagged. This job: spec 28 7210 s.2.4 F.4 lists rooms requiring smoke detectors (elevator lobbies, telephone, electrical and mechanical rooms and so on) but E-160 shows one detector near the FACP and ties devices to the base building system (E-160 note 1).

### 3.2 Per-door kit (access control)

One controlled door expands to a fixed set; do not count the same device twice (once as a door kit and once as a loose device).

| Component | Quantity per door | Cable per component | Source |
|---|---|---|---|
| Card reader | 1 (2 if read-in/read-out) | shielded 22 AWG 6-conductor (Wiegand) | [Hanwha](https://support.hanwhavision.com/hc/en-001/articles/47256876435731) (search summary); VT detail uses 8-conductor 18 AWG shielded or 6-conductor 18 AWG shielded types ([VT door-access details](https://www.facilities.vt.edu/content/dam/facilities_vt_edu/design-and-construction-standards/detail-library/door-access-details.pdf)) |
| Electric strike / lock | 1 | 18/2 or 18/4 | [Hanwha](https://support.hanwhavision.com/hc/en-001/articles/47256876435731) (search summary); VT: 2 conductor 18 AWG unshielded |
| REX (PIR) | 0 or 1 | 22/4 | Hanwha; VT: 4 conductor 22 AWG shielded |
| Door contact | 1 per monitored leaf | 22/2 | [West Penn composite per Hanwha search result](https://support.hanwhavision.com/hc/en-001/articles/47256876435731) (search summary); VT: 2 conductor 18 AWG |
| Power transfer hinge / loop | 1 only if the leaf lock or exit device is electrified | per hardware | [National Lock Supply](https://nationallocksupply.com/blog/how-to-coordinate-a-complete-electrified-opening/) |
| Lock power supply | by load (5.5) | 120 VAC feed + DC out | National Lock Supply |
| Junction box above ceiling | 1 | | VT detail ("J box above ceiling", 3/4 in. EMT to access control cabinet) |

A composite (all-in-one) cable bundles reader, contact, lock and REX runs; it is **one cable run, not several** ([GPT second opinion](#9-second-opinion-notes-gpt-6-astra); composite design noted in the [Hanwha search result](https://support.hanwhavision.com/hc/en-001/articles/47256876435731) (search summary)). The cable table in the security schedule (E-150) gives the project's types: reader 22/3 pair in banana cable; electric strike 18/4 in banana cable; door contact 22/2 in banana cable; motion detector 22/4; hold-up 22/4; alarm interface 22/8; cameras Cat 6; video monitor RG59 coax plus 110 VAC outlet.

### 3.3 Cable length (measured)

- **Measure the routed path, not the straight line**: horizontal route from the panel/TR to the device, plus vertical drops and rises to device height, plus bends. trueCABLE's method: measure each drop, add the ceiling height (or floor-to-plate distance) to every run, 2 ft outlet slack per drop, head-end slack enough to reach the farthest corner of the telecom room plus the floor-to-ceiling height at the entry (their example is 24 ft added per drop), about 1 ft per 90 degree bend, then a 7 to 10 percent waste buffer, then divide by the spool length and round **up** ([trueCABLE](https://www.truecable.com/blogs/cable-academy/cable-waste-math-how-to-estimate-your-box-count) (blog-level)).
- **Daisy-chained fire alarm circuits**: panel-to-first-device home run plus each device-to-device segment, doubled return legs for Class A; do not home-run every addressable device ([GPT second opinion](#9-second-opinion-notes-gpt-6-astra)). The project's circuits are Class B, Survivability Level 1 (spec 28 7210 s.1.2 B, `spec-p466.txt`), so no return leg.
- **Average-run shortcuts** (nearest/farthest average, "150 ft per run for a small place, 225 to 250 ft for a larger one") are installer rules of thumb only ([IPVM thread](https://ipvm.com/forums/video-surveillance/topics/estimating-cable-length) (blog-level, search summary)); they belong in an explicitly labelled allowance, never as a measured quantity.
- **A cable-foot is a cable-foot**: a 100 ft run of 18/2 is 100 ft of cable, not 200 ([GPT second opinion](#9-second-opinion-notes-gpt-6-astra)).
- **Shared raceway counts once** regardless of how many cables ride in it ([GPT second opinion](#9-second-opinion-notes-gpt-6-astra)).
- **Link limits constrain the length**: 90 m (295 ft) permanent link, 100 m (328 ft) channel including at most 10 m of cords; slack consumes the allowance; add a second TR rather than exceed it ([Horizontal cabling design](https://open-exam-prep.com/study-guides/bicsi-rcdd/distribution-design/horizontal-cabling-design) (secondary)).

### 3.4 Heights, slopes and openings (what applies to devices)

- **Mounting heights are drawing inputs and drive vertical cable and conduit LF**: strobe lens 80 to 96 in. AFF ([Potter manual](https://www.pottersignal.com/product/manual/InstallationManual_EH-HS-S-CHS-CS-Series.pdf) (primary)); pull station operable part 42 to 48 in. ([Security Sales](https://www.securitysales.com/contributed/fire-alarm-initiating-devices-can-be-lifesavers/) (search summary), [EngineersUniverse](https://engineersuniverse.com/studios/fire-alarm/how-to-design-fire-alarm-device-layout)); wall horn-only appliances 90 in. AFF minimum and at least 6 in. below the ceiling (Potter manual). Project: security schedule gives per-device heights (e.g. card reader box 44 in., hold-up 74 in., cameras 8'-6" or to ceiling; E-150 schedule) and E-160 note 6 sets 80 in. minimum lens.
- **Ceiling height and slope change detector counts, not the quantity rule**: spot smoke detection above 10 ft and beams or sloped ceilings change spacing (4.1). Take ceiling height from the reflected ceiling plan or sections.
- **Openings** matter for door-device counts only: double doors are two leaves (two contacts if both monitored); a storefront mullion mounts devices on the mullion with a slim metal box (E-150 schedule, "provide slim/mullion metal back box for mounting on mullion"; E-160 label "mounted on mullion").

---

## 4. Code and standards rules that bound device counts

NFPA 72 section numbers move between editions and the figures below come from secondary reproductions of specific editions; the adopted edition and the project's own notes govern. Use these to **check** counts, and to produce a labelled design-build count only when no layout is drawn.

### 4.1 Smoke and heat detector spacing

- Smooth ceiling: **30 ft nominal spacing (900 SF per detector)** is the guideline virtually all manufacturers follow ([Honeywell/System Sensor white paper](https://buildings.honeywell.com/content/dam/hbtbt/en/documents/document-lists/system-sensor/white-papers/SmokeDetectors-SpacingLevelCeilingsWithBeamsJoints%20WhitePaper%20A05-0408.pdf) (primary, 2006)). Two layout tests: detector within half the spacing (15 ft) of walls, or every ceiling point within **0.7 x 30 = 21 ft** of a detector ([ECM article](https://www.ecmag.com/section/integrated-systems/all-spaced-out-how-far-apart-should-you-place-heat-and-smoke-detectors) (search summary)); 0.7 x 30 = 21 is **derived**. The IP Security Depot page prints "21 ft from walls", which conflates the two tests ([IP Security Depot](https://www.ipsecuritydepot.com/guides/nfpa-72-compliance-reference/)); do not use that wording.
- **Corridors**: spacing can stretch to about 41 ft when the 0.7 limit is still met ([ECM article](https://www.ecmag.com/section/integrated-systems/all-spaced-out-how-far-apart-should-you-place-heat-and-smoke-detectors) (search summary); [Honeywell white paper](https://buildings.honeywell.com/content/dam/hbtbt/en/documents/document-lists/system-sensor/white-papers/SmokeDetectors-SpacingLevelCeilingsWithBeamsJoints%20WhitePaper%20A05-0408.pdf) (primary)). Derived: for a 10 ft wide corridor 2 x sqrt(21^2 - 5^2) = 40.8 ft.
- **Beams/joists**: members deeper than 4 in. are beams (spaced over 3 ft) or solid joists (3 ft or less); in the 2002 edition spacing was halved perpendicular to beams up to 12 in. deep on ceilings 12 ft or lower, and a detector was required in every pocket above that, a rule the white paper's CFD study argued against ([Honeywell white paper](https://buildings.honeywell.com/content/dam/hbtbt/en/documents/document-lists/system-sensor/white-papers/SmokeDetectors-SpacingLevelCeilingsWithBeamsJoints%20WhitePaper%20A05-0408.pdf), historical). A current secondary table gives 0.4 x spacing perpendicular to joists for 4 to 12 in. depth and one detector per pocket above 12 in. ([IP Security Depot](https://www.ipsecuritydepot.com/guides/nfpa-72-compliance-reference/) (secondary)). Treat the beam rule as edition-dependent and read the RCP.
- **Heat detectors have a listed spacing** (typically 15 to 50 ft; some listings 70 ft) and the same half-spacing/0.7 logic ([ECM article](https://www.ecmag.com/section/integrated-systems/all-spaced-out-how-far-apart-should-you-place-heat-and-smoke-detectors) (search summary); [EngineersUniverse](https://engineersuniverse.com/studios/fire-alarm/how-to-design-fire-alarm-device-layout) 50 ft with 25 ft to wall).
- **Other placement**: at least 3 ft from supply diffusers ([EngineersUniverse](https://engineersuniverse.com/studios/fire-alarm/how-to-design-fire-alarm-device-layout)); spot detection effectiveness falls above 10 ft and is generally ineffective above 30 ft (same source).
- **Project rule**: provide a ceiling smoke detector within 5 horizontal feet of the FACP (spec 28 7210 s.2.2 F, `spec-p471.txt`); the single smoke detector in E-160 sits beside the FACP (inference from the plan and spec, not a drawn callout).
- Derived design-build check for this building: 1,900 SF / 900 SF = 2.1, so a coverage count would be at least 3 detectors by area. The drawing shows 1 plus base-building coverage; the drawing governs and the difference is flagged, not "corrected".

### 4.2 Manual pull stations

Within 5 ft of each exit doorway on each floor; additional stations so travel to the nearest does not exceed 200 ft measured horizontally; where a grouped opening is over 40 ft wide, stations at both sides; operable part 42 to 48 in. AFF ([Electrical Contractor magazine](https://www.ecmag.com/section/miscellaneous/compliance-requires-proper-placement) (search summary); [Security Sales](https://www.securitysales.com/contributed/fire-alarm-initiating-devices-can-be-lifesavers/) (search summary); [EngineersUniverse](https://engineersuniverse.com/studios/fire-alarm/how-to-design-fire-alarm-device-layout)). Project stations are dual-action, key-reset type (spec 28 7210 s.2.3 C, `spec-p472.txt`).

### 4.3 Visible notification (strobes)

- Mount the **entire lens 80 to 96 in. AFF** (wall) ([Potter manual](https://www.pottersignal.com/product/manual/InstallationManual_EH-HS-S-CHS-CS-Series.pdf) (primary)).
- **Candela by room size, one wall-mounted strobe per room** (2013 edition table as printed by the manufacturer): 20x20 ft 15 cd; 28x28 30 cd; 30x30 34 cd; 40x40 60 cd; 45x45 75 cd; 50x50 94 cd; 54x54 110 cd; 60x60 135 cd; 70x70 184 cd; with four strobes per room (one per wall) 40x40 needs 15 cd and 54x54 needs 30 cd ([Potter manual](https://www.pottersignal.com/product/manual/InstallationManual_EH-HS-S-CHS-CS-Series.pdf) (primary)). A different secondary reproduction prints 30x30 as 30 cd, 50x50 as 95 cd and a ceiling-mount column (20x20 30 cd, 50x50 177 cd) ([IP Security Depot](https://www.ipsecuritydepot.com/guides/nfpa-72-compliance-reference/) (secondary)); another page prints 30x30 as 110 cd ([EngineersUniverse](https://engineersuniverse.com/studios/fire-alarm/how-to-design-fire-alarm-device-layout)). **The sources conflict; do not hard-code a candela table.** Read the candela printed at each appliance on the drawing or schedule; this project sets 110 cd unless noted (E-160 note 6).
- **Non-square rooms** use the smallest table square that encloses the room; large rooms divide into squares each served by a strobe ([Potter manual](https://www.pottersignal.com/product/manual/InstallationManual_EH-HS-S-CHS-CS-Series.pdf); [National Training Center](https://nationaltrainingcenter.com/nfpa-72-visible-notification-requirements-in-special-applications/) (secondary)).
- **Corridors 20 ft wide or less**: strobe within 15 ft of each end, no more than 100 ft apart; corridors wider than 20 ft use room spacing ([National Training Center](https://nationaltrainingcenter.com/nfpa-72-visible-notification-requirements-in-special-applications/) (secondary); [EngineersUniverse](https://engineersuniverse.com/studios/fire-alarm/how-to-design-fire-alarm-device-layout); project spec 28 7210 s.2.3 B.6, `spec-p472.txt`). Derived count for a corridor of length L ft: 1 strobe if L is 30 ft or less, else ceil((L - 30)/100) + 1 (L = 131 ft gives 3).
- **Sleeping areas**: strobe within 16 ft of the pillow; 110 cd if the lens is 24 in. or more below the ceiling, 177 cd if less ([Potter manual](https://www.pottersignal.com/product/manual/InstallationManual_EH-HS-S-CHS-CS-Series.pdf)). Not relevant to a bank, but needed by a general engine.
- Project: strobes in public spaces such as restrooms, kitchens, break rooms and conference rooms, and anywhere six or more people gather (spec 28 7210 s.2.3 B.6 c, `spec-p472.txt`).

### 4.4 Audible notification

Public mode: at least 15 dBA above average ambient, or 5 dBA above the maximum level lasting 60 seconds, whichever is greater, measured 5 ft above the floor; sleeping areas 75 dBA at the pillow ([Electrical Contractor magazine](https://www.ecmag.com/magazine/articles/article-detail/systems-can-you-hear-me-now-audibility-intelligibility-and-visibility-notification) (search summary); [IP Security Depot](https://www.ipsecuritydepot.com/guides/nfpa-72-compliance-reference/)). Counts come from the drawing; audibility only checks whether a horn is in the right space. Project: temporal 3-3 pattern, horns 15 dBA above ambient in public spaces (spec 28 7210 s.2.3 A, `spec-p471.txt`, `spec-p472.txt`).

### 4.5 Duct detectors and equipment interfaces

- IMC requires detectors on systems over 2,000 CFM (return side in the IMC reading), systems under 2,000 CFM are usually exempt unless several serve one area with an aggregate of 2,000 CFM or more, and there is an exception for systems that cannot spread smoke beyond the room ([forum summary of IMC 606.2.1 and NFPA 72](https://forums.mikeholt.com/threads/duct-smoke-detec-location.139685/post-2183163) (blog-level); [NC OSFM interpretation](https://www.ncosfm.gov/mechanical/060622-smoke-detector-common-supply-and-return-air-systems-0/open) (search summary)). Project spec: smoke detectors in each return air path of equipment moving more than 2,000 CFM and in each supply and return path above 15,000 CFM; confirm quantities with Division 23 (spec 28 7210 s.2.4 D.2, `spec-p475.txt`).
- Manufacturer data: install 6 duct widths from obstructions where possible; tube pressure differential 0.01 to 1.2 in. w.c. ([ACI SL-2000 install sheet](https://www.cochranesupply.com/media/assets/product/documents/ACI/SL-2000-P%20Install.pdf) (search summary)).
- Each duct detector comes with an addressable control module as needed for fan shutdown; smoke dampers (Division 23) need a detector at each location; sprinkler flow and tamper switches each need a monitor module (spec 28 7210 s.2.4 D.3, E.6, F, `spec-p473.txt`, `spec-p475.txt`).

### 4.6 Electrified egress hardware

2021 IBC 1010.2.11 (door hardware release of electrically locked egress doors) and 1010.2.12 (sensor release); sensor-release systems unlock on fire alarm or sprinkler activation and need a manual unlock device, typically a push button; delayed egress is typically 15 seconds (30 seconds where the AHJ approves) and needs automatic sprinkler or detection; section numbers shifted in 2024 ([iDigHardware 2021 IBC e-locks](https://idighardware.com/wp-content/uploads/2022/04/2021-IBC-Electromagnetic-Locks.pdf) (primary headings read; body text not extractable), [iDigHardware search summary](https://idighardware.com/2026/02/decoded-fire-protection-system-requirements-for-special-locking-arrangements/) (search summary)). Estimating consequence: a maglock or sensor-release door adds a push-to-exit button and a fire-alarm release interface (relay or control module) to the kit; a strike on a mechanically free-egress door does not.

### 4.7 Intrusion detector coverage (design-build checks only)

PIR wall unit about 35 ft deep at 90 degrees (about 550 SF); ceiling PIR about 20 ft radius; acoustic glass-break about 25 ft radius; interior motion zones cross-zoned under ANSI/SIA CP-01 ([EngineersUniverse intrusion layout](https://engineersuniverse.com/studios/physical-security/intrusion-zone-layout) (secondary, "nominal planning estimates")). A GE acoustic glass-break datasheet gives 15 ft to the farthest glass, a conflict; use the listed range of the specified model ([GE spec sheet](https://manualmachine.com/ge/5885w/6916860-specsheet/) (search summary)). Counts come from the schedule; do not derive them from these ranges when a schedule exists.

### 4.8 Video coverage (design-build checks only)

Pixel density per IEC 62676-4 as published by Axis: detection 25 px/m (8 px/ft), observation 63 px/m (20 px/ft), recognition 125 px/m (40 px/ft), identification 250 px/m (80 px/ft; 76 precise); the model assumes a 16 cm face width, so 40 px across a face gives 250 px/m (derived: 40/0.16) ([Axis white paper](https://whitepapers.axis.com/en-us/pixel-density-based-on-iec-62676-4-2014) (primary)). Newer editions may change terms and thresholds (same Axis page, search summary of the 2024-25 proposals). Required camera count for a given scene width W: horizontal resolution / W must reach the target px/m (derived from the definition). This sizes cameras only when the plan does not show them.

---

## 5. Coverage, yield, capacity and waste factors

### 5.1 Cable packaging and waste

| Factor | Value | Basis |
|---|---|---|
| Box/reel size | 1,000 ft boxes and reels are the standard order unit; the trueCABLE method rounds up to whole 1,000 ft spools | [trueCABLE](https://www.truecable.com/blogs/cable-academy/cable-waste-math-how-to-estimate-your-box-count) (blog-level); fire alarm cable listings sold per 1,000 ft ([Elliott FPLP 18/2 listing](https://static.elliottelectric.com/P/Item/CCI/FPLP182SRR/Alternate) (search summary)) |
| Waste buffer | 7 to 10 percent minimum, more for unfamiliar or complex routing | [trueCABLE](https://www.truecable.com/blogs/cable-academy/cable-waste-math-how-to-estimate-your-box-count) (blog-level); a wire-length calculator page suggests a 10 to 20 percent buffer ([calculator](https://www.ultimatefinancecalculator.com/calculators/wire-length-calculator), blog-level, search summary); GPT suggests 5 percent kept separate (GPT second opinion). No authoritative source sets a figure: carry it as a visible, editable factor. |
| Slack per end | 2 ft outlet end; head-end enough to reach the far corner of the room plus ceiling height | [trueCABLE](https://www.truecable.com/blogs/cable-academy/cable-waste-math-how-to-estimate-your-box-count) (blog-level); a forum poster says 2 to 15 ft per cable in the closet ([search result](https://www.cocoontech.com/goto/post?id=143898), blog-level) |
| Rounding | Round packages up once per job (sum LF, then divide), not per run | [trueCABLE](https://www.truecable.com/blogs/cable-academy/cable-waste-math-how-to-estimate-your-box-count) |

Worked example (derived, illustrative inputs, not project data): 20 Cat 6 drops, route 100 ft + 9 ft vertical + 2 ft outlet slack + 24 ft head-end + 3 ft for bends = 138 ft each; 20 x 138 = 2,760 ft; plus 8 percent = 2,981 ft; 3 boxes of 1,000 ft.

### 5.2 Smoke detector coverage

900 SF per detector on smooth ceilings; 21 ft radius test; about 41 ft in narrow corridors (4.1).

### 5.3 Strobes and horns per power supply

This project: maximum 20 devices per strobe power supply (E-160 note 4); 12 notification appliances therefore need 1 supply (derived: ceil(12/20) = 1). Field charging power supply: 6.0 A (4.0 A continuous), four outputs, never above 70 percent load, one per floor with spare capacity by floor size (spec 28 7210 s.2.2 E, `spec-p471.txt`). SLC loops: each SLC interface communicates with 99 detectors and 99 modules and each circuit stays below 70 percent load or covers at most 5 floors (spec 28 7210 s.2.2 B.1, C, `spec-p470.txt`, `spec-p471.txt`).

### 5.4 Fire alarm batteries

Standby 24 hours plus 5 minutes of alarm for most commercial systems, 15 minutes for voice/emergency communications; Ah = standby A x hours + alarm A x alarm hours, then a 20 percent margin ([EngineersUniverse](https://engineersuniverse.com/studios/fire-alarm/how-to-design-fire-alarm-device-layout) (secondary); [IP Security Depot](https://www.ipsecuritydepot.com/guides/nfpa-72-compliance-reference/) (secondary)). Batteries are 12 V pairs wired in series; a count of sets, one per independently backed power source, and capacity from the load calculation (spec 28 7210 s.2.5 and the shop-drawing battery calculation requirement in s.1.3 B, `spec-p468.txt`, `spec-p476.txt`; [GPT second opinion](#9-second-opinion-notes-gpt-6-astra) for series/Ah). This project's spec asks for 60 hours standby plus 10 minutes alarm on the field charging power supply (s.2.2 E.1). Derived illustration with invented loads (0.5 A standby, 2.0 A alarm): 24 h + 5 min gives 12.2 Ah, 14.6 Ah with a 20 percent margin; 60 h + 10 min gives 30.3 Ah, 36.4 Ah with margin. A takeoff cannot compute this without the load calculation; take battery quantities from the schedule or panel data.

### 5.5 Access control power

Electric strike (12 VDC) about 200 to 300 mA holding with inrush up to 1 A; maglock (24 VDC) 250 to 500 mA continuous; multiply by openings on a supply and add 25 percent headroom; a 4 A supply runs about 6 to 8 strikes ([National Lock Supply](https://nationallocksupply.com/blog/how-to-coordinate-a-complete-electrified-opening/) (secondary)); a trade article derates supplies to 75 to 80 percent and notes maglock inrush of two to three times rating ([Security InfoWatch](https://www.securityinfowatch.com/home/article/10543155/query-the-access-control-expert) (search summary)); one search result also cites about 3.8 A inrush for a panic-bar release, which would favor a dedicated supply (single unattributed source, unverified). Allegion publishes a Von Duprin power-supply selection guide; its URL returned 404 so no figures from it are used here. Derived: 4 strikes x 0.3 A = 1.2 A, 1.5 A with 25 percent headroom. Controllers: ceil(doors / usable doors per controller), checked against reader and I/O capacity ([GPT second opinion](#9-second-opinion-notes-gpt-6-astra)). Access control has no blanket NFPA 72 24-hour battery rule (same source); one practitioner cites 90 minutes for life-safety circuits and 4 hours typical ([National Lock Supply](https://nationallocksupply.com/blog/how-to-coordinate-a-complete-electrified-opening/), unverified against NFPA 101).

### 5.6 PoE and network ports

Port power at the switch: 802.3af 15.4 W, 802.3at 30 W, 802.3bt 60 W and 90 W; device-side 12.95, 25.5, 51 and 71.3 W; the total switch budget is the limit, switches reserve by declared class, practitioners design to 80 percent of nameplate budget; run limit about 100 m ([Omada PoE guide](https://www.omadanetworks.com/ph/blog/2627/poe-switch-guide-standards-power-budget-and-planning-for-business/) (secondary), [IP Security Depot budget post](https://www.ipsecuritydepot.com/blog/how-to-calculate-poe-budget-headroom-for-a-switch-with-heated-ptz-cameras/) (search summary)). Derived: 19 PoE cameras at class maximum 15.4 W = 292.6 W, 366 W at the 80 percent design point; at 30 W each 570 W and 713 W. Ports: one per camera plus uplinks; a 20 percent spare-port allowance is an estimating convention ([GPT second opinion](#9-second-opinion-notes-gpt-6-astra)), giving 23 for 19 cameras (derived) and so one 24-port switch before uplinks.

### 5.7 Video storage

Storage (GB) = bitrate (Mbps) x 10.8 x cameras x days x recording factor (1.0 continuous); divide by 1,000 for TB; raw is not purchasable: RAID 6 efficiency about 0.75 on 8 disks, times about 1.1 for file system and headroom ([Forasoft](https://www.forasoft.com/learn/video-surveillance/articles-vms/surveillance-storage-retention-math) (blog-level)). 10.8 comes from 1 Mbps x 86,400 s / 8 / 1,000 (derived). Derived illustration with invented inputs: 19 IP cameras at 2 Mbps for 30 days is 12.3 TB raw, 18.1 TB after RAID 6 and headroom. Retention days and bitrate come from the spec or the owner; if absent, flag rather than assume.

### 5.8 Pathway supports

- **J-hook spacing**: non-continuous supports no more than 5 ft (1.5 m) per TIA-569 as quoted by the manufacturer; BICSI practice 4 to 5 ft with about 3 in. clearance above ceilings, conduit and pipe ([nVent CADDY Cat HP data sheet](https://tracer.nvent.com/en-ca/data-solutions/products/efscat32hpab/pdf) (search summary), [Vertical Cable summarizing BICSI ITSIMM](https://verticalcable.com/?p=624250) (search summary)).
- **Capacity**: the 2 in. CADDY Cat HP hook is rated 60 Cat 6 (35 Cat 6A, 90 Cat 5e) at 70 percent fill; another CADDY model's listing shows 40 Cat 6 for a 1 5/16 in. hook; Vertical Cable recommends derating the chart by about 25 percent and not loading open-top supports with more than 50 cables (same sources). Derived: 60 x 0.75 = 45 cables.
- Derived count: a 100 ft route at 5 ft spacing is 20 intervals, 21 hooks counting both ends (26 at 4 ft). Project: E-150 note 6 specifies J-hooks at 6 ft on center back to the security panel, which is wider than the 5 ft maximum above; flag, and count to the drawing note while noting the conflict.

---

## 6. Material breakdown an estimator lists (primary materials and what follows from them)

### 6.1 Fire alarm cable and raceway

| Cable | Where | Source |
|---|---|---|
| FPL | general-purpose power-limited fire alarm, not in risers, ducts or plenums unless in conduit | [3Star / NEC 760 summary](https://www.3starinc.com/fire_alarm_cable.html) (search summary) |
| FPLR | riser (vertical between floors), UL 1666 | same; [NEC 760 study guide](https://open-exam-prep.com/study-guides/id-electrician/special-equipment-emergency-renewables/fire-alarm-optical-fiber-low-voltage-power-limited) (secondary) |
| FPLP | plenum and other air-handling space, NFPA 262; may substitute for FPLR and FPL, FPLR for FPL | same |
| CL2 / CL3 (P, R) | Class 2 / Class 3 circuits (30 V AC / 60 V DC and 100 VA limits for Class 2) | [NEC 725 study guide](https://open-exam-prep.com/study-guides/id-electrician/special-equipment-emergency-renewables/fire-alarm-optical-fiber-low-voltage-power-limited) (secondary) |

Rules that change quantities: PLFA conductors cannot share a raceway with light, power, Class 1 or non-power-limited fire alarm conductors, and need 2 in. air separation or a listed barrier in enclosures (NEC 760.136 per the same study guide); 120 VAC cannot share a conduit with low voltage, and shielded wire needs full-length shield continuity ([California HCAI note](https://hcai.ca.gov/document/site-plan-fac22005) (search summary)). Typical gauges: SLC 18/2 shielded or unshielded, NAC 14/2 or 12/2, speaker 18/2 shielded ([GPT second opinion](#9-second-opinion-notes-gpt-6-astra)); the project fixes strobe/horn at 14 AWG thin stranded red/black, speaker Belden 8760 shielded, four-conductor cable prohibited, no solid wire, no splices, wire colors: red reserved for fire, yellow for security (E-160 notes 2-3; E-150 note 3). Conduit stubs: min 1/2 in. EMT for fire alarm (E-160 note 3 and spec 28 7210 s.2.1); plastic insulated bushings and nylon pull string on low-voltage conduits (E-702 elevation note 5).

### 6.2 Security rough-in (what the electrical contractor lists even when the vendor pulls cable)

E-150 sheet notes: the electrical contractor provides all raceways, boxes and pull strings, security cabling is by the security vendor (note 2); 3/4 in. EMT with 3/4 in. bushing stubbed to the accessible ceiling and a **2-gang** backbox for each alarm activating device, exterior ATM/night deposit, CCTV, card readers and all wall-mounted devices (note 7); 3/4 in. conduit to the Knox box (note 8); 3/4 in. conduit from every exterior camera back to the nearest accessible ceiling (note 9); cameras under canopies (note 10); plenum-rated cables (note 5); data/voice cables on J-hooks (note 6). The schedule's per-tag installation text instead specifies **single gang** boxes for most devices (e.g. tags 3, 4, 7, 10, 12). The note and the schedule conflict; carry the note as the governing general rule unless the tag text is more specific, and flag.

### 6.3 Structured cabling and telecom room

Per outlet: jack(s) per port, faceplate, backbox, conduit stub or J-hook route, cable (2 ports typical, scheduled by the legend), patch-panel port per cable, patch cords (two per jack-to-jack link, GPT second opinion); room: rack/cabinet, ladder rack, vertical and horizontal cable managers, backboard, ground bar (E-702 notes). Combination data outlet is the project's main data symbol (E-001 legend line "1 TELE / 1 DATA OUTLET, U.N.O."; 17 in `reference/estimate/lines.json` vs 16 on the E-100 legend markup page, so some outlets are counted from E-701 to E-704 elevations).

### 6.4 Quantities this project's reference estimate carries as allowances

The reference estimate carries a single DIV 28 allowance line, **622 "ALLOWANCE PROVIDED FOR WIRE, CABLE & CONDUIT FITTINGS", AREA 2000 SF, 1 LS**, in the fire alarm section (`reference/estimate/lines.json`, E-160 markup). It covers both the fire alarm and the security wire, cable and conduit. The security section (603-621) carries no allowance or LF line. The ground truth does **not** contain measured LF for these systems, so an AI should emit an area-based allowance line with its basis rather than invent LF.

---

## 7. Common mistakes and how to check a takeoff

Checks marked * come from the GPT second opinion (`gpt_q2.txt`); the rest are from the cited sources or the project documents.

| Mistake | Check |
|---|---|
| Counting legend rows or details as installed devices* | Count only plan instances; reconcile to the schedule and riser. |
| Reading fire alarm "F" symbols as a single type | Resolve each symbol against the legend sheet and the device schedule; split pull stations, horn/strobes, strobes. This job's legend lives on E-001, not E-160. |
| Treating one controlled door as one device* | Build a door-by-door matrix: readers, lock, REX, contact, transfer, power, release interface. Check the schedule counts for consistency: this job has 5 readers but 4 electric strikes (tags 4 and 6) and 2 door contacts (tag 12); reconcile which door has a reader without a strike (e.g. read-only door, a hardware-set exit device) rather than forcing 1:1. |
| Double counting a device once in a door kit and once loose | One owner per device; kits own reader, lock, REX, contact. |
| Assuming "security cabling by vendor" removes electrical scope* | List raceway, boxes, stubs, pull strings, sleeves and supports as electrical scope (E-150 note 2, note 7). |
| Spec and drawing disagree* | Spec 28 7250 is a different building (warehouse, vault, second floor). Use the drawing schedule; log the conflict. Spec 28 7210 also references NFPA 2000 editions and elevators the job does not have. |
| Box count conflicts (note vs schedule) | E-150 note 7 says 2-gang, schedule says single gang; flag. |
| Wrong cable listing | Plenum vs riser from the actual space (E-002 note 22: free wiring only above accessible ceilings, plenum rated); do not use FPL in plenum or risers without conduit. |
| Painting/identification applied too widely* | Red junction boxes and conduit only for fire alarm (spec 28 7210 s.2.1 E); security cable yellow (E-150 note 3). |
| Duct detector scope* | Check furnished-by, installed-by, wired-by: this spec is furnished by fire alarm, installed by mechanical, wired by electrical (spec 28 7210 s.2.4 D.4). |
| Missing module/relay points* | Reconcile FA points with sprinkler flow/tamper, HVAC shutdown, door holders, access release; one module per point. |
| Unrounded or double-rounded packages | Sum LF, add slack and waste, round to boxes once. |
| Ignoring link-length limits | Longest routed drop plus slack against 295 ft; add a TR if exceeded. |
| Missing power supply capacity | NAC and FCPS counts from loading rules (5.3), not device count alone. |
| Mounting heights ignored | Heights drive vertical LF and conduit stubs; read E-150 schedule, elevations and E-160 note 6. |
| Mis-reading candela table from memory | Sources conflict (4.3); read the drawing. |
| Equating outlet symbol with one cable* | Expand by port count from the legend; check dedicated drops (cameras, controllers) are not in two scopes. |
| Missing telecom room items* | Read rack elevation (E-702): backboard, rack, managers, ladder rack, ground bar. |

Cross-checks that catch most errors: (1) device counts on plan = schedule counts = estimate lines; (2) every counted device has its box, base or mount; (3) every FA monitor/control point traces to an interfacing system; (4) every door kit has a power source and a code-compliant release; (5) cable LF is either measured with a route or explicitly an allowance with the basis printed; (6) total ports and PoE budget close; (7) circuit loading (20 devices per supply here) closes.

---

## 8. Reading responsibility (who furnishes, installs, wires)

Build a furnish / install / wire / test matrix per device family. Examples from this job: security cabling by security vendor, raceway and boxes by electrical (E-150 notes 2, 7); duct detectors furnished by fire alarm, installed by mechanical, wired by electrical (spec 28 7210 s.2.4 D.4); sprinkler flow and tamper switches furnished and installed by others, wired by electrical, with monitor modules by fire alarm (s.2.4 E.6); smoke dampers by Division 23 (s.2.3 D); volume control switch "by others, GC to install only" (E-100 legend); fire alarm devices connect to the base building system by a landlord-approved licensed fire alarm contractor (E-160 note 1); mood media: electrical pulls cables, equipment by owner (E-702 keyed notes). A device that is "by owner" or "by vendor" still appears in the quantity list with its responsibility tag, because the raceway, box and power still follow from it.

---

## 9. Second-opinion notes (GPT-6 Astra)

Requested via `tools/ask_gpt.py` with generic, non-project text only. Items where it agreed with cited sources: per-device fire alarm kit (head, base, box), batteries as series pairs and the 24 h plus 5 or 15 minute formula, FPL/FPLR/FPLP selection by space, door kit contents, home-run Cat 6 per camera, storage formula, 90 m / 100 m limits, IBC 1010.2.11 and 1010.2.12 numbering. Items it asserted with no source here and that this file does not rely on: a 2 ft per field termination plus 10 ft per panel slack, a 5 percent waste, 1.20 x port allowance, "2 patch cords per link", "1 Cat 6 per networked controller". It declined to give TIA clause numbers. Treat these as conventions, not citations.

---

## 10. What an AI takeoff must read from the drawings and specs

1. **Sheet set**: security plan and its device schedule (tag, description, wire, installation requirement), fire alarm plan and its notes, electrical legend, electrical elevations, power and auxiliary plan (data outlets, power at security equipment), reflected ceiling plan (ceiling type, height, beams), mechanical schedules (duct airflow), door and hardware schedule, riser diagram.
2. **From each device**: type (by symbol shape against the legend, never from the letter alone), tag/schedule number, candela or rating, mounting (wall, ceiling, weatherproof, mullion), mounting height, backbox type and gang count, who furnishes/installs/wires, wire type from the schedule.
3. **From each door**: leaf count, lock type, reader side(s), REX type, contact, whether the hardware is electrified (power transfer), egress/release requirement, fire-rated or not, the hardware set number.
4. **From notes**: wiring method (conduit, flex, free-wiring above ceilings), listing (plenum), colors, minimum conduit size, support spacing (J-hooks), device-per-supply limits, separation rules, certification and testing requirements.
5. **From the specification**: product names and manufacturers (Notifier, Edwards, Siemens), circuit classes and survivability level, SLC and NAC capacity rules, battery duration, power-supply sizing rules, device accessory requirements (bases, boxes, tubes), submittal calculations; and **whether the spec matches the building** (reject boilerplate).
6. **From geometry**: calibrated plan scale for routed LF, ceiling height and vertical drops, corridor lengths and widths (strobe and detector spacing), room dimensions only when a layout is not drawn.
7. **Outputs**: count by type with plan sheet references; the kit expansion with the rule that produced each line; cable either measured (route listed) or an allowance (basis printed, confidence low); slack, waste and rounding as separate steps; conflicts and unresolved responsibilities listed rather than silently resolved.
8. **Design-build fallback only**: when no layout is drawn, produce a labelled coverage count using 30 ft / 900 SF and the 0.7 test (4.1), and mark it low confidence.

---

## 11. Comparison with the TakeoffSpeed engine and open items

Engine file: `TakeoffSpeed repo: lib/quantities/trades/mep/low-voltage.ts` (read only; not edited). Observations, not instructions:

- Engine design-build smoke count uses `ceil(L/30) x ceil(W/30)` per room, a conservative grid; the 0.7 S test and corridor stretch (4.1) can yield fewer detectors in corridors. It already flags beams and high ceilings.
- Engine slack conventions: 1 ft per termination for fire alarm and access cable, 10 ft TR slack and 1 ft outlet slack for data (attributed to TIA-568.0 "3 m / 30 cm"). I could not verify those TIA figures; the trueCABLE method uses 2 ft at the outlet and a room-dependent head-end allowance (5.1).
- Engine 5 percent cable waste and 1,000 ft boxes fit the sources' lower bound (waste commonly 7 to 10 percent); no authoritative figure exists.
- Engine J-hook spacing 60 in. matches the 5 ft maximum; the project note of 6 ft on center would need an override (5.8). Engine's 50 cables per 2 in. hook is below the manufacturer's 60 at 70 percent fill and equals the cited open-top maximum.
- Engine controller convention (2 readers per controller) and 4 doors per lock power supply are consistent with the 6 to 8 strikes on a 4 A supply once headroom is applied (5.5), but they are conventions, not code.
- Engine has no duct-detector-to-module pairing, no monitor module per sprinkler switch, no door-holder line, no per-circuit power-supply loading rule (20 devices here), and no Class A doubling of home runs beyond a flag; spec 28 7210 requires several of these.
- Engine carries a 75 ft per door allowance and 40 ft per FA device allowance; this reference estimate instead carries a single 2000 SF lump-sum wire and conduit allowance (6.4).

Unverified or not found (search budget exhausted before these could be checked; ask for a follow-up pass): NEC Chapter 9 Table 1 fill percentages (commonly cited as 40 percent for three or more conductors; not confirmed here); TIA-568.0 slack figures; NFPA 72 current-edition section numbers for strobe tables and battery rules; bank-specific security requirements (Bank Protection Act device list, UL 681/UL 2050 intrusion standards); a first-party estimating handbook (NECA, RSMeans) page for fire alarm unit takeoff.
