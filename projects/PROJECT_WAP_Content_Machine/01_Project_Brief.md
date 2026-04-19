# PROJECT BRIEF: WAP Content Machine

| Field | Value |
|---|---|
| Started | April 19, 2026 |
| Status | Active |
| Owner | Nico |

## Goal

Build a repeatable, AI-assisted content machine for wearepalermo.com that runs at ~80% autopilot. The machine has two outputs: (1) updated existing blog posts that are losing Google rankings, and (2) new blog posts that maintain and grow organic traffic. Everything gets documented in a dedicated WAP Brain GitHub repository so any AI agent in any future session can pick up where the last one left off without Nico re-explaining context from scratch.

## Scope (What's IN)

- Create a separate GitHub repository for the WAP Brain (wap-brain)
- Define the WAP Brain folder structure: brain docs, SOPs, project folders
- Document the current state of wearepalermo.com in Brain docs: business model, tools stack, content inventory, funnel overview, monetization
- Build SOP for updating existing blog posts with AI (audit, rewrite, republish workflow)
- Build SOP for creating new blog posts with AI (research, outline, draft, publish workflow)
- Build a prompt library embedded inside SOPs for Nico's voice/tone (the Italian-American comedian persona)
- Build WAP_08_STORY_BANK.md: tagged library of Nico's personal anecdotes and jokes with index for fast AI lookup
- Build WAP_09_PLACES_RESTAURANTS_BARS.md: tagged, indexed list of Palermo restaurants and bars
- Build WAP_10_PLACES_EXPERIENCES.md: tagged, indexed list of Palermo experiences and things to do
- Define what Nico must do manually (on-camera, approval, final edit) vs. what AI handles

## Out of Scope (What's NOT)

- Paid advertising (separate project)
- Social media reactivation (Instagram, TikTok)
- YouTube video production workflow
- Migrating The Sicilian Way from Podia to Lovable (separate project, Phase 2)
- Email sequence work in ConvertKit
- Any changes to the existing WordPress site structure or design
- Asset management system (photos and videos)

## Relevant Brain Docs

None yet — this project creates them.

## Key Decisions

| Date | Decision | Reasoning |
|---|---|---|
| Apr 19, 2026 | Brain setup before content workflow | Without a repo to store SOPs and prompts, every AI session starts from zero. Same mistake we avoided with Sheila. |
| Apr 19, 2026 | Separate GitHub repo from eb-brain | WAP is a separate business. No crossover. |
| Apr 19, 2026 | Paid ads out of scope | Different project. Different planning session needed. |
| Apr 19, 2026 | Podia to Lovable migration out of scope | Not urgent. Phase 2 after the machine is running. |
| Apr 19, 2026 | Voice/persona is a Brain doc, not just a prompt | WAP_05_VOICE_AND_PERSONA.md is permanent reference. Prompts live inside SOPs and reference the Brain doc. |
| Apr 19, 2026 | Content format and SEO/AIO rules are a separate Brain doc | WAP_06_CONTENT_FORMAT.md covers structure, WordPress publishing rules, and 2026 SEO+AIO optimization. Research happens before SOPs are written. |
| Apr 19, 2026 | Story Bank needs a summary index at the top | AI reads the index first, jumps to matching entries by tag. Avoids reading the full doc every time. |
| Apr 19, 2026 | Restaurant/bar list and experiences bank are separate Brain docs | WAP_09 and WAP_10. Same tag+index structure as Story Bank. |
| Apr 19, 2026 | Asset management is a separate future project | Too complex for this scope. Parking Lot. |
