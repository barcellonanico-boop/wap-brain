# PARKING LOT: WAP Content Machine

## Out-of-Scope Ideas

| Date | Idea | Notes |
|---|---|---|
| Apr 19, 2026 | Asset management system (photos + videos) | Need organized storage, easy retrieval for blog and video content. Complex enough to be its own project. Revisit after content machine is running. |
| Apr 19, 2026 | Podia to Lovable migration (The Sicilian Way) | Move product + checkout off Podia to save costs and gain flexibility. Not urgent. Phase 2 after this project completes. |
| Apr 19, 2026 | Paid advertising project | Meta or Google ads to accelerate traffic. Needs separate planning session. Budget ~$100-200 to test. |
| Apr 19, 2026 | Social media reactivation (Instagram, TikTok) | Dead for ~1 year. AI-assisted short-form content possible. Not the bottleneck right now. |
| Apr 19, 2026 | YouTube video production workflow | Nico on camera + B-roll + voiceover format. AI can help with scripts and structure. Later. |
| Apr 19, 2026 | Author page rebuild for Nico | Task 1.8 Rule 4.2. High E-E-A-T leverage. Needs: photo, bio (Palermo-born + resident), YouTube list, social profiles, press mentions. Own mini-project. |
| Apr 19, 2026 | Site-wide schema audit | Verify every post has Article + FAQPage + Author schema. Unknown current state. Possibly an Architect one-shot task. |
| Apr 19, 2026 | Core Web Vitals check on SiteGround hosting | Relevant for AI citation (ChatGPT bot HTML reading mode). Not urgent. |
| Apr 19, 2026 | robots.txt check for AI crawlers | Verify GPTBot, Google-Extended, PerplexityBot not blocked. 5-minute Architect task. |
| Apr 19, 2026 | WordPress schema plugin verification | Rule 3.5 requires it. Nico must confirm if RankMath or Yoast is installed. |
| Apr 21, 2026 | Batch populate TripAdvisor URLs in WAP_09 | All Tier B entries (~32) and some Tier A flagged [VERIFY TA URL]. Needs ~30 min batched Architect session: web search each restaurant on TripAdvisor, paste URL, commit. Pre-requisite before WAP_09 can be used for paid products. |
| Apr 24, 2026 | Retroactive audit of S001-S007 against new SOP_03 story file template | Existing stories were created before SOP_03 existed. May have missing metadata fields (Goal, Source, Date captured, full tag categories, Pairs with). One-time sweep to bring into line. Low priority but worth doing before Story Bank scales beyond ~15 entries. |
| Apr 24, 2026 | S006 Fiat Panda trim pass | Flagged as too long during Story Bank refactor. SOP_03 word-count discipline (250-350, 400 cap) doesn't apply retroactively, but S006 specifically deserves a trim pass to match the bank's new standard. |
| Apr 24, 2026 | Multi-story voice memo handling | If Nico records a single memo containing 3 distinct stories, does each go through SOP_03 independently? Implied yes, not explicitly specced. Address in v1.1 after first test run if it comes up. |

## Future Optimizations

| Date | Idea | Notes |
|---|---|---|
| Apr 19, 2026 | Story Bank auto-search during content drafts | Build a smarter lookup: agent searches Story Bank by tag before every draft and flags matches automatically. Needs the bank to have enough entries first. |
| Apr 19, 2026 | ConvertKit integration for WAP | Currently using CK but no documented automation system for WAP. Could mirror the Sheila approach eventually. |

## Questions for Nico

| Date | Question | Status |
|---|---|---|
| Apr 19, 2026 | What keyword tool are you currently using for SEO research, if any? | Open |
| Apr 19, 2026 | Where do your photos currently live? Google Drive, hard drive, something else? | Open — needed before asset project starts |
| Apr 19, 2026 | Is the "free itinerary" lead magnet a PDF? Where does it live and what does it contain? | Open — needed before any funnel work |
| Apr 19, 2026 | Which WordPress schema plugin is installed on wearepalermo.com? RankMath, Yoast, something else, or none? | Open — blocks proper implementation of Task 1.10 Rule 3.5 |
| Apr 24, 2026 | Where does the Story Agent live long-term? Claude chat (re-paste prompt each time), dedicated Claude project (persistent), or Claude Code setup? Doesn't block first test run but worth deciding before Story Bank scales. | Open |

## Process Flags

- **Apr 22, 2026 — SOP_03 gap exposed.** Copywriting agent produced a Story Bank prompt with 10 invented tags that don't exist in the WAP_08 taxonomy (e.g., palermo-chaos, via-maqueda, rules-and-enforcement, comic-anecdote). PM caught and corrected before Claude Code ran. This will keep happening on every new story intake until SOP_03_Add_Story_To_Bank.md is written (Task 2.3 in Phase 2). SOP must explicitly require the agent to reference the existing tag taxonomy in WAP_08 and only propose new tags via the Parking Lot, never invent them inline. Priority: elevate 2.3 when Phase 2 starts.

| Apr 24, 2026 | Task 2.4 (cadence) sequence reversal | Originally planned BEFORE SOPs. Nico correctly argued cadence depends on SOP execution speed, which is unknown until SOP_01 runs. Task 2.4 now happens AFTER Phase 3 test run, not before. |
