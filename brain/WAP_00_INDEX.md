# WAP_00_INDEX.md — WAP Brain Master Index

Last updated: April 19, 2026

This is the master directory of all Brain docs and SOPs in the WAP Brain.
Read this first in every session to understand what exists and where to find it.

---

## Document Map

| File | What It Contains | When to Read | When to Update |
|---|---|---|---|
| WAP_00_INDEX.md | This file. Master directory of all docs and SOPs. | Every session, read first. | When any new doc or SOP is added, or an existing one changes scope. |
| WAP_01_BUSINESS_OVERVIEW.md | What wearepalermo.com is, Nico's USP, target audience, brand positioning, current state of the business. | When starting any content, copywriting, or strategy task. | When the business model, audience, or positioning changes. |
| WAP_02_TOOLS_STACK.md | Every tool in the WAP stack: WordPress, ConvertKit, Podia, YouTube, Switchy, GA4, GTM, Claude, Gemini. Includes what each tool does and how they connect. | When setting up automations, integrations, or new workflows. | When a tool is added, removed, or its role changes. |
| WAP_03_MONETIZATION.md | All revenue streams: Booking.com, Discover Cars, GetYourGuide affiliate setup. The Sicilian Way funnel: free itinerary optin, soap opera sequence, $47 offer with $31 downsell on Podia. | When working on any funnel, affiliate, or revenue task. | When affiliate programs change, funnel is updated, or product moves platform. |
| WAP_04_CONTENT_INVENTORY.md | Full catalog of existing content: 79 blog posts, 35 pages, ~60 YouTube videos. Each item tagged with status: ranking, losing, outdated, evergreen. | Before any content update or creation task. Pick targets from here. | After every post updated or published. Keep status current. |
| WAP_05_VOICE_AND_PERSONA.md | Nico's persona in full. The Italian-American comedian style. DOs and DON'Ts. Good vs. bad output examples. Rules for sounding like Nico, not like a travel blog. | Before any writing task. Non-negotiable. | When new examples of good/bad output are identified during test runs. |
| WAP_06_CONTENT_FORMAT.md | Article structure rules: no wall text, no dashes, text boxes, bullet points, formatting conventions. WordPress publishing checklist. SEO and AIO optimization rules for 2026. | Before any writing or publishing task. | When SEO/AIO best practices change or new formatting rules are established. |
| WAP_07_CONTENT_CADENCE.md | Weekly content cadence: how many posts updated per week, how many new posts, what Nico must touch vs. what runs without him. | When planning the week's content work. | When cadence changes. |
| WAP_08_STORY_BANK.md | Tagged library of Nico's personal anecdotes, jokes, and observations. Summary index at top for fast lookup by tag. Use before every content draft to check for matching stories. | Before every writing task. Search index by tag first. | Every time Nico adds a new story. Follow SOP_03. |
| WAP_09_PLACES_RESTAURANTS_BARS.md | Indexed, tagged list of Palermo restaurants and bars Nico recommends. Includes notes, category tags, last updated date. | When writing content that references where to eat or drink. | When Nico visits somewhere new or a place closes/changes. |
| WAP_10_PLACES_EXPERIENCES.md | Indexed, tagged list of Palermo experiences and things to do. Same structure as WAP_09. | When writing content about activities, tours, or what to do in Palermo. | When Nico discovers something new or an experience changes. |
| WAP_11_AIRBNB_PROPERTIES.md | Master source of truth for Nico's Airbnb properties (Via Ambra 11, Via Divisi 101). All property facts, quirks, rules, procedures, and internal contacts. Guest-facing materials are derived from this doc. | Before replying to any guest message, before generating any guest-facing material (Guidebook, listing copy, pre-arrival message). | When any property fact changes — new wifi, new quirk, new cleaner, new maintenance event. |
| WAP_12_AFFILIATE_LINKS.md | Canonical source for all affiliate URLs (Booking.com, GetYourGuide, Discover Cars, Parclick). Used by SOP_01/SOP_02/Copywriting when inserting monetization links. Also contains Direct Bookings section for Nico's own property. | When adding a new hotel/tour/rental partner, when verifying a link (monthly via SOP_05), when a link breaks. |

---

## SOP Map

| File | What It Does | When to Use |
|---|---|---|
| SOP_01_Update_Existing_Post.md | Full workflow for updating an existing blog post with AI: pull from WordPress, rewrite prompt, SEO/AIO check, Nico review, republish, update inventory. | Every time an existing post needs updating. |
| SOP_02_Create_New_Post.md | Full workflow for creating a new blog post with AI: keyword/topic input, draft prompt, Nico review, images, publish, update inventory. | Every time a new post is created. |
| SOP_03_Add_Story_To_Bank.md | Two-stage workflow: Stage 1 the Story Agent crafts a raw dump into a 250-350 word bit in Nico's voice; Stage 2 same agent runs dedupe scan, strict-taxonomy tag assignment, named-business check, stats flag, bidirectional pairs-with check, voice mode confirmation. Drafts story file + index row, surfaces for Nico approval, Claude Code writes and pushes. | Every time Nico wants to add a story to the Bank. See SOP for when NOT to use (one-liners, near-duplicates, recommendation-only content). |

---

## Repo Structure

```
wap-brain/
├── brain/          — permanent reference docs (this folder)
├── sops/           — standard operating procedures
├── projects/       — active project folders
└── archive/
    └── projects/   — completed project folders (read-only reference)
```

---

## Active Projects

| Project | Status | Folder |
|---|---|---|
| WAP Content Machine | Active | projects/PROJECT_WAP_Content_Machine/ |
| Airbnb System | Active | projects/PROJECT_Airbnb_System/ |

---

## Agents

See `agents/AGENT_INDEX.md` for the full registry including installation instructions, update protocol, and versioning convention.

| Agent | What It Does | When to Update |
|---|---|---|
| WAP PM | Project orchestrator. Tracks projects, decides task sequencing, writes handoff prompts, updates docs after every task. | When changing orchestration rules, adding new specialist agents, or changing the Claude Code update protocol. |
| WAP Architect | Technical infrastructure: SEO, GA4, GTM, WordPress, ConvertKit, Stripe, Lovable, Make.com, GitHub, scripting. | When adding platform access, changing tool configs, or updating technical workflows. |
| WAP Copywriting | All writing: blog posts, rewrites, email sequences, opt-in pages, ad copy, microcopy. Voice lock to Nico's Italian-American comedian style. | When voice rules change (WAP_05), content format changes (WAP_06), or new content types are added. |
| SCOUT | Fact verification specialist. Receives content drafts, extracts factual claims, verifies via web_search + web_fetch, returns markdown table report with VERIFIED/DISPUTED/UNVERIFIABLE per claim. Handles surgical extraction (skips personal observations, comedic embellishment, invented dialogue). Tier-ranked sources. Used in SOP_01 Step 4 and SOP_02 Step 4. | When updating Scout's rules, when adding a tier source, when extending tool integration. |
| WAP Story Agent | Story Bank intake. Two-stage workflow: Stage 1 crafts raw dump into 250-350 word Maniscalco-style bit. Stage 2 runs dedupe, taxonomy tags, named-business check, stats flag, pairs-with, voice mode confirmation. Used in SOP_03. | When Story Bank format changes, when taxonomy rules change, when word count discipline changes. |
