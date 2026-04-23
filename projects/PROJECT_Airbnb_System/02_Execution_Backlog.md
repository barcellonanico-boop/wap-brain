# EXECUTION BACKLOG: Airbnb System

## Phase 1 — Saturday Fire (Via Ambra 11, deadline Fri April 24 EOD)

- [x] 1.1 Build WAP_11_AIRBNB_PROPERTIES.md master file with full Via Ambra 11 entry — address, specs, wifi, keybox, check-in/out, trash, appliances, heating/AC, water boiler, TV, linens change policy, electrical quirk, shower drain quirk, smoke detector, shutters, noise, house rules, legal, parking, airport transport, groceries, paid services, emergency contacts, maintenance log [PM] [Est: 60 min | Actual: 90 min]
- [x] 1.2 Fix Via Ambra 11 Airbnb listing — Arrival guide (Directions, Check-in method, Wifi, House manual, House rules, Checkout instructions) + Description section (Listing description, Guest access, Interaction with guests, Your property, Other details to note) filled in Nico voice EN + IT. Heating amenity tagged correctly as split ductless. Deferred to Phase 2 polish: title refresh, amenities full audit, host bio, photo captions. Task handled as PM-led working session instead of Copywriting handoff. [PM] [Est: 90 min | Actual: 59 min]
- [x] 1.3 Write Via Ambra 11 pre-arrival messages — 4 messages drafted: (1) welcome + guest-count nudge + expectation, 10 min post-booking; (2) ID request + arrival time + empathetic privacy framing + YouTube explainer video, 3 days before (changed from 5 days); (3) airport transport (Prestia + shared taxi + private taxi + Uber + ZTL warning + icons), 2 days before; (4) self check-in (keybox + LEFT door + wifi), 1 day before. Plus catch-up message drafted for Maximilian (current Saturday guest) and sent manually since M1 and M2 windows had passed. Task handled as PM direct-write (not Copywriting handoff) — iterating in-session was faster. [PM] [Est: 45 min | Actual: 49 min]
- [x] 1.4 Set up Airbnb native scheduled messages for Via Ambra 11 — 4 templates created in Airbnb: "Ambra — 01 Booking Welcome" (booking + 10min, not applied to existing), "Ambra — 02 ID Request (3 days before)" (not applied to existing, to avoid duplicating Maximilian catch-up), "Ambra — 03 Airport Transport (2 days before)" (applied to existing), "Ambra — 04 Self Check-in (1 day before)" (applied to existing). Uses Airbnb variables {{Guest first name}} and {{Check-in date}}. [PM] [Est: 20 min | Actual: 4 min]
- [x] 1.5 Generate guest-facing in-apartment Apartment Handbook (content) — content approved by Nico after multiple revisions. 14 sections: Wi-Fi, Kitchen (with dishwasher/sink + toilet warnings), Climate, Linens & Towels (sheets >7 nights, towels >3 nights, mid-stay €50), TV, Tap Water, Trash, Groceries/Pharmacy, House Rules (no smoking emphasized), Problems (power/shower/smoke detector/wifi), Damages/Loss/Dirt (charging policy), When You Leave the Apartment (shutters/AC/lights every time), Check-out, Contacts (Nico + Marika + Mary, names only). Restaurant/experience picks split out to separate City Guide (future task). Task split into 1.5 (content, done) and 1.5b (HTML/CSS print template, Architect). [PM] [Est: 60 min | Actual: 90 min across multiple revisions]
- [ ] 1.5b Build HTML/CSS A4-print template for Via Ambra 11 Apartment Handbook — Architect builds single standalone HTML file at projects/PROJECT_Airbnb_System/handbook-printable/via-ambra-11.html. Must print to exactly 2 pages A4. Lucide icons, serif/sans pairing (Fraunces + Inter or similar), green/cream palette matching Nico-approved ChatGPT reference. Content is locked (from Task 1.5). Nico print-tests, iterates with Architect. Source of truth: HTML edits are fast, regenerate PDF by printing. [Architect] [Est: 75 min | Actual: __ ]
- [ ] 1.6 Saturday prep checklist — step-by-step list Nico runs Friday/Saturday morning: keybox install (dad), mirror install (dad), cleaning, linen check, amenities check, wifi test, lock test, lightbulb check, trash empty, guidebook printed and placed, itineraries printed and placed [PM] [Est: 30 min | Actual: __ ]
- [ ] 1.7 Execute Saturday prep — physically do everything in 1.6 [Nico + Dad] [Est: 180 min | Actual: __ ]

## Phase 2 — Permanent Airbnb Brain

- [ ] 2.1 Write WAP_12_AIRBNB_GUEST_OPS.md — message library (all Via Ambra messages), FAQ answers in Nico voice (check-in questions, wifi issues, trash, noise, local recs pointer to WAP_09/WAP_10), troubleshooting scripts, guest lifecycle workflow [PM] [Est: 75 min | Actual: __ ]
- [ ] 2.2 Update WAP_00_INDEX.md — register WAP_12 and SOP_06 in Document Map and SOP Map [PM] [Est: 10 min | Actual: __ ]
- [ ] 2.3 Write SOP_06_Reply_To_Guest_Message.md — workflow for pasting guest message, PM checks WAP_11/WAP_12/WAP_09/WAP_10, PM drafts reply in Nico voice, Nico copy-pastes to Airbnb [PM] [Est: 30 min | Actual: __ ]

## Phase 3 — Calendar Integration

- [ ] 3.1 Subscribe Google Calendar to Airbnb .ics export for Via Ambra 11 and Via Divisi 101 — export the .ics URLs from Airbnb host dashboard, add as subscribed calendars in Google Calendar [Architect] [Est: 20 min | Actual: __ ]
- [ ] 3.2 Document calendar integration in WAP_02_TOOLS_STACK.md — add Airbnb + Google Calendar section with the .ics URLs, refresh frequency, limitations [PM] [Est: 15 min | Actual: __ ]
- [ ] 3.3 Connect calendar visibility to PM chat — decide the mechanism (Nico pastes upcoming check-ins at session start, or an MCP connector, or another method) [PM + Architect] [Est: 20 min | Actual: __ ]

## Phase 4 — Via Divisi 101 Back-Documentation

- [ ] 4.1 Back-fill WAP_11 with Via Divisi 101 full entry — same schema as Via Ambra 11 [PM] [Est: 30 min | Actual: __ ]
- [ ] 4.2 Back-fill WAP_12 with Via Divisi 101 message library — preserve existing 3 pre-arrival messages verbatim, add Via Divisi FAQ answers and troubleshooting specific to that apartment (electrical panel location, gas cylinder issue, etc.) [PM] [Est: 45 min | Actual: __ ]
- [ ] 4.3 Final Phase 4 commit — verify repo state clean, both properties fully documented [PM] [Est: 10 min | Actual: __ ]
