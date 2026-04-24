# EXECUTION BACKLOG: WAP Content Machine

## Phase 1 — Brain Setup

- [x] 1.1 Create WAP Brain GitHub repo and clone locally [Architect] [Est: 20 min | Actual: 24 min ]
- [x] 1.2 Define WAP Brain folder structure and create empty scaffold [PM] [Est: 20 min | Actual: 3 min ]
- [x] 1.3 Write WAP_00_INDEX.md — master directory of all Brain docs and SOPs [PM] [Est: 30 min | Actual: 11 min ]
- [x] 1.4 Write WAP_01_BUSINESS_OVERVIEW.md — what wearepalermo.com is, who Nico is, USP, audience, tone of voice summary, funnel overview [PM] [Est: 45 min | Actual: 2 min ]
- [x] 1.5 Write WAP_02_TOOLS_STACK.md — WordPress, ConvertKit, Podia, YouTube, Switchy, GA4, GTM, Claude, Gemini [PM] [Est: 30 min | Actual: 2 min ]
- [x] 1.6 Write WAP_03_MONETIZATION.md — Booking.com, Discover Cars, GetYourGuide affiliate setup + The Sicilian Way funnel [PM] [Est: 40 min | Actual: 1 min ]
- [x] 1.7 Write WAP_04_CONTENT_INVENTORY.md — catalog of existing 77 posts, 26 pages, 136 YouTube videos with links and view counts [Architect] [Est: 60 min | Actual: 10 min ]
- [x] 1.8 Research SEO + AIO best practices for 2026: Google organic + AI Overviews. Output: pre-digested rules saved to 05_SEO_AIO_Research.md. [Architect] [Est: 60 min | Actual: 11 min]
- [x] 1.9 Write WAP_05_VOICE_AND_PERSONA.md — Nico's persona, the Italian-American comedian style, DOs and DON'Ts, good vs. bad output examples. Written by PM directly (not Copywriting agent) because source material was already in chat context. [PM] [Est: 60 min | Actual: 49 min]
- [x] 1.10 Write WAP_06_CONTENT_FORMAT.md — synthesize SEO/AIO rules from 05_SEO_AIO_Research.md with existing WAP format rules (no wall text, no dashes, text boxes) + WordPress publishing checklist [PM] [Est: 30 min | Actual: 55 min]
- [x] 1.11 Write WAP_08_STORY_BANK.md — tagged library with Master Index, tag taxonomy, 5 full tagged story entries (Italian Romeos, dark alleys, American tipping, 6:30 PM tourist traps, Sicilian gelato origin), Gap List with high-priority stories to capture, voice preservation rules. [PM] [Est: 40 min | Actual: 30 min]
- [x] 1.11b Story Bank refactored: monolithic WAP_08_STORY_BANK.md → WAP_08_STORY_BANK_INDEX.md (rich index) + brain/stories/ folder (one file per story). Migrated S001-S006. Added S007 Pony Race + Battiloro to WAP_09 (R044). Out-of-backlog emergent task. [PM] [Est: — | Actual: ~45 min]
- [x] 1.12 Write WAP_09_PLACES_RESTAURANTS_BARS.md — 43 entries (38 unique venues + Capo/Ballarò markets as catch-all), Master Index, tag taxonomy, Tier A voice treatment for ~11 venues with Nico brain-dump, Tier B baseline for rest, Google Maps URLs auto-generated, TripAdvisor URLs flagged [VERIFY TA URL] for batch population, paid-only content rule enforced at top. [PM] [Est: 30 min | Actual: 110 min]
- [x] 1.13 Write WAP_10_PLACES_EXPERIENCES.md — 26 experiences catalogued across 2 tiers (Tier 1 = affiliate-monetized GetYourGuide experiences, Tier 2 = non-affiliate but recommend-worthy). Covers city tours, day trips, multi-day destinations, cultural shows, festivals, sporting events, markets. Extracted from the best-tours article and things-to-do-in-Palermo article. GetYourGuide affiliate URLs preserved. Master Index + tag taxonomy + Gap List + affiliate disclosure rule at top. Paid-only rule removed (experiences are free-content-eligible when monetized via affiliate). [PM] [Est: 30 min | Actual: 14 min]
- [x] 1.14 All Brain docs committed and pushed. Auto-synced to project knowledge via GitHub integration. [Architect] [Est: 15 min | Actual: 5 min]

## Phase 2 — Content SOPs and Prompts

- [x] 2.1 SOP_01 Update Existing Post drafted (v1.1). 8-step workflow (Intake → Prep → Rewrite → Fact Check → Nico Review → Revision → Images → Publish). School C revision philosophy locked. Reference-by-pointer to WAP_05/06/08/10/12/13 instead of duplicating content. Named business rule enforced via WAP_08 flag system. Monitoring at 6-week mark. Phase 3 validation: test on /where-to-stay-palermo/. 6 follow-on tasks identified (2.7 Scout, 2.8 Image Agent, 2.9 Affiliate Verification SOP, WAP_12 build, WAP_13 build, WAP_10 expansion). [PM] [Est: 75 min | Actual: 115 min]
- [ ] 2.2 Write SOP_02_Create_New_Post.md — step by step: keyword/topic input, run AI draft prompt (embedded here), Nico review, images, WordPress publish, update inventory [PM + Copywriting] [Est: 75 min | Actual: __ ]
- [ ] 2.3 Write SOP_03_Add_Story_To_Bank.md — how Nico brain-dumps a story, how agent formats and tags it, how it gets added to WAP_08 [PM] [Est: 30 min | Actual: __ ]
- [x] 2.0 Google Search Console audit: export performance data for all 77 posts, assign LOSING / RANKING / OUTDATED / EVERGREEN status, update WAP_04_CONTENT_INVENTORY.md [Architect] [Est: 60 min | Actual: 35 min] — DONE. Full GSC export analyzed: 109 pages classified. 12 P1 urgent (high decline + revenue-critical), 6 P2, 18 P3, 30 P4, 43 healthy. Site-wide: +16% QoQ (misleading) but -17% YoY (real trend). Key finding: 10 of 12 P1 posts still rank top 10 — decline is CTR collapse from AI Overview cannibalization, not ranking demotion. Results saved to 06_GSC_Audit_Results.md. SOP_01 test sequence recommended: where-to-stay → parking → taormina.
- [ ] 2.4 Define the weekly content cadence — posts updated per week, new posts per week, what Nico must touch vs. what runs without him [PM + Nico] [Est: 30 min | Actual: __ ]
- [ ] 2.5 Document cadence in WAP_07_CONTENT_CADENCE.md [PM] [Est: 20 min | Actual: __ ]
- [ ] 2.6 Commit and push. Update project knowledge. [Architect] [Est: 10 min | Actual: __ ]
- [ ] 2.7 Build WAP Scout agent — fact verification specialist (web search + web fetch tools, VERIFIED/DISPUTED/UNVERIFIABLE output format, source citations). Required before Phase 3 SOP_01 test run. [PM + Architect] [Est: 45 min | Actual: __ ]
- [ ] 2.8 Build WAP Image Agent — image sourcing, AI generation, editing, alt text, library management. Until this exists, SOP_01 Step 6.5 is manual (Nico). [PM + Architect] [Est: 60 min | Actual: __ ]
- [ ] 2.9 Write SOP_05_Verify_Affiliate_Links.md — monthly verification of all links in WAP_12. [PM] [Est: 30 min | Actual: __ ]
- [ ] 2.10 Create WAP_12_AFFILIATE_LINKS.md — registry of canonical affiliate URLs (Booking.com hotels, GetYourGuide tours, Discover Cars pickup points, Parclick). Each entry: name, area, short description, affiliate link, last-verified date. Required before Phase 3. [PM + Nico] [Est: 45 min | Actual: __ ]
- [ ] 2.11 Create WAP_13_GSC_AUDIT_LATEST.md — living Brain doc for latest GSC audit data. Migrate April 21 findings from projects/06_GSC_Audit_Results.md into evergreen Brain doc. Original project file stays as frozen snapshot. Required before Phase 3. [PM + Architect] [Est: 30 min | Actual: __ ]
- [ ] 2.12 Expand WAP_10 scope to cover experiences, monuments, rituals, and combo moves. Add sections for: (Tier 1) affiliate-monetized experiences [current content], (Tier 2) monuments and places to see, (Tier 3) free cultural experiences and rituals, (Tier 4) Nico combo moves (e.g., Santa Caterina cannolo + cloister). Rename doc if scope change warrants. [PM + Nico] [Est: 45 min | Actual: __ ]

## Phase 3 — Test Run

- [ ] 3.1 Test SOP_01: pick 3 posts actively losing rankings, run full update workflow [Nico + Copywriting] [Est: 90 min | Actual: __ ]
- [ ] 3.2 Test SOP_02: pick 1 keyword, run full new post workflow, publish [Nico + Copywriting] [Est: 90 min | Actual: __ ]
- [ ] 3.3 Post-run debrief: what broke, what was slow, what needs fixing [PM + Nico] [Est: 30 min | Actual: __ ]
- [ ] 3.4 Update SOPs based on debrief [PM] [Est: 30 min | Actual: __ ]
- [ ] 3.5 Final commit and push. Mark project complete. Move to archive. [Architect] [Est: 15 min | Actual: __ ]
