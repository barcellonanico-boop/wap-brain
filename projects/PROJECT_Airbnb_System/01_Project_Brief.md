# PROJECT: Airbnb System

**Started:** April 22, 2026
**Status:** Active
**Owner:** Nico

---

## Goal

Build an AI-assisted system for managing Airbnb operations (guest communication, house documentation, check-in flow, calendar awareness) for Nico's two Palermo apartments: Via Ambra 11 (new, first guest April 26, 2026) and Via Divisi 101 (existing, already running). The system lives inside WAP Brain so guest Q&A reuses WAP_09 (restaurants) and WAP_10 (experiences) for local recommendations. Immediate priority is getting Via Ambra 11 ready for Saturday April 26. Longer-term infrastructure (permanent Airbnb Brain docs, calendar integration, Via Divisi back-documentation) follows after the fire is out.

---

## Scope (What's IN)

### Phase 1 — Saturday Fire (Via Ambra 11, must finish by Fri April 24 EOD)
- Adapt Via Divisi Apartment Guidebook into Via Ambra 11 Apartment Guidebook
- Adapt the 3 Via Divisi pre-arrival messages into Via Ambra 11 versions
- Set up Airbnb native scheduled messages for Via Ambra 11
- Fix the Via Ambra 11 Airbnb listing (title, description, amenities, photos, host bio, smoke/CO alarm installation and reporting)
- Physical Saturday prep checklist (keybox install, mirror install, cleaning, walkthrough)
- Print and place self-guided itineraries + best tours docs in the apartment

### Phase 2 — Permanent Airbnb Brain
- Write `WAP_11_AIRBNB_PROPERTIES.md`: both properties, physical specs, house rules, keybox codes, wifi, quirks, maintenance history
- Write `WAP_12_AIRBNB_GUEST_OPS.md`: standard guest messages library, FAQ answers in Nico voice, troubleshooting scripts, pre-arrival/during-stay/post-checkout workflows
- Update `WAP_00_INDEX.md` to register the two new Brain docs
- Write `SOP_06_Reply_To_Guest_Message.md`: how Nico pastes a guest message, how the PM checks WAP_11, WAP_12, WAP_09, WAP_10 and replies in Nico voice

### Phase 3 — Calendar Integration
- Subscribe Google Calendar to the Airbnb `.ics` export feed for both properties
- Share that Google Calendar with the PM chat context so check-ins/checkouts are visible
- Document the setup in `WAP_02_TOOLS_STACK.md`

### Phase 4 — Via Divisi 101 Back-Documentation
- Back-fill WAP_11 with Via Divisi 101 property data
- Back-fill WAP_12 with Via Divisi 101 message library (preserve existing messages verbatim)

---

## Out of Scope (What's NOT)

- Building a wearepalermo.com direct booking system
- Migrating Via Ambra 11 or Via Divisi 101 off Airbnb
- Promoting the apartments on wearepalermo.com
- Third-party property management tools (Hostaway, Hospitable, Smartbnb, etc.)
- Pricing strategy or dynamic pricing tools
- A maintenance ticketing system (log inside WAP_11 until volume demands more)
- Professional photography or listing photo shoot (flagged for Parking Lot if Nico wants later)
- Cleaning service SOP (later, when volume demands it)

---

## Relevant Brain Docs

- `WAP_00_INDEX.md` — register new docs here
- `WAP_02_TOOLS_STACK.md` — register Airbnb + Google Calendar integration
- `WAP_05_VOICE_AND_PERSONA.md` — all guest messages must sound like Nico
- `WAP_09_PLACES_RESTAURANTS_BARS.md` — answer guest food questions
- `WAP_10_PLACES_EXPERIENCES.md` — answer guest activity questions

---

## Key Decisions

| Date | Decision | Rationale |
|---|---|---|
| Apr 22, 2026 | Keep Airbnb docs inside WAP Brain, not a separate system | Properties will eventually live on wearepalermo.com, so unified brain avoids duplicate infrastructure later |
| Apr 22, 2026 | Calendar integration via Airbnb .ics to Google Calendar | Free, native to Airbnb, no third-party PMS cost |
| Apr 22, 2026 | Phase 1 = Via Ambra 11 fire; Via Divisi 101 back-documentation is Phase 4 | Via Divisi already running fine; no urgency. Via Ambra has a guest in 4 days. |
| Apr 22, 2026 | Airbnb native scheduled messages, not a third-party automation tool | Keep costs zero, scope tight. Revisit if volume grows. |
| Apr 22, 2026 | Reuse WAP_09 and WAP_10 for guest recommendations | No duplicate place lists. Guests benefit from Nico's entire Palermo knowledge bank. |
| Apr 22, 2026 | Project name: Airbnb System | Short, clear, no WAP prefix because it's distinct from the Content Machine project |
