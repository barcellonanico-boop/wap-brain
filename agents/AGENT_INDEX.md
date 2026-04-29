# WAP Agent Index

**Last updated:** April 29, 2026 (v2.1 step numbering update + brand rename)

The master directory of every specialist agent in the WAP system. Use this to find which agent handles which task and where each agent's system prompt lives.

---

## What This Doc Is

Every agent in the WAP system has a system prompt stored in `agents/`. This index lists them all with their role, scope, tools, and where they're used in SOPs. It also documents how to install, update, and version agents.

---

## Active Agents

| Agent | File | Role | Used In | Tools | Status |
|---|---|---|---|---|---|
| WAP PM | [PM_SYSTEM_PROMPT.md](PM_SYSTEM_PROMPT.md) | Project orchestrator. Tracks projects, decides task sequencing, writes handoff prompts, updates docs after every task. | All sessions, every task | project_knowledge_search | v1.0 active |
| WAP Architect | [ARCHITECT_SYSTEM_PROMPT.md](ARCHITECT_SYSTEM_PROMPT.md) | Technical infrastructure: SEO, GA4, GTM, WordPress, ConvertKit, Stripe, Lovable, Make.com, GitHub, scripting. | SOP_01 v2.1 Steps 2, 3, 4, 8 (Live HTML snapshot, Prep, Structural Audit, Pass 3 HTML). SOP_02 (when v2.0 lands). All technical tasks. **NOT used in SOP_01 Step 10 (publish — Nico's job) or Step 12 (post-publish checks — Claude Code's job).** | project_knowledge_search, web_search, web_fetch (varies by task) | v1.0 active |
| WAP Copywriter | [COPYWRITER_SYSTEM_PROMPT.md](COPYWRITER_SYSTEM_PROMPT.md) | Generic SOP-driven copywriter. All writing: blog posts, newsletters, YouTube descriptions, social posts, premium guide copy, sales pages, ads. Reads SOPS_INDEX to find workflow, reads WAP_05 + WAP_05b every session for voice, reads task-specific Brain docs per SOP instructions. No task-specific knowledge baked in — all workflow logic lives in SOPs, all rules in Brain docs. | SOP_01 v2.1 Steps 5, 7 (Pass 1 Information, Pass 2 Voice). SOP_02 Step 3. All content tasks. **Pass 3 (HTML conversion) is Architect's job, not Copywriter's.** | project_knowledge_search, web_search (optional) | v2.0 active |
| WAP Scout | [SCOUT_SYSTEM_PROMPT.md](SCOUT_SYSTEM_PROMPT.md) | Fact verification specialist. Extracts factual claims from drafts, verifies via web sources, returns markdown table with VERIFIED / DISPUTED / UNVERIFIABLE per claim. Surgical extraction (skips personal observations, comedic embellishment, invented dialogue). Tier-ranked sources. | SOP_01 v2.1 Step 6 (Fact Check). SOP_02 Step 4. | web_search, web_fetch | v1.0 active (validated in Favignana run Apr 28) |
| WAP Story Agent | [STORY_AGENT_SYSTEM_PROMPT.md](STORY_AGENT_SYSTEM_PROMPT.md) | Story Bank intake. Two-stage workflow: Stage 1 crafts raw dump into 250-350 word Maniscalco-style bit. Stage 2 runs dedupe, taxonomy tags, named-business check, stats flag, pairs-with, voice mode confirmation. | SOP_03 (the entire workflow). | project_knowledge_search | v1.0 untested (Task 2.13 validates) |

---

## How To Install An Agent

For each agent, the system prompt file in `agents/` is the source of truth. To install an agent into a Claude Project:

1. Open Claude.ai
2. Click "+ Create Project" (left sidebar)
3. Name the project after the agent (e.g., "WAP Scout", "WAP Architect")
4. Open the system prompt file from the wap-brain repo
5. Copy the FULL contents (everything from the title down through the changelog)
6. Paste into the Project's "Custom Instructions" or "Project Knowledge" instructions field
7. Save
8. Verify the right tools are enabled (see Tools column above)

The Project is now ready. Open a chat inside the Project to interact with the agent.

## How To Update An Agent

When an agent's behavior needs changing (new rule, new tool, refined output format):

1. Edit the agent's file in `agents/` directly via Claude Code or your editor
2. Bump the version (v1.0 → v1.1) and add a changelog entry at the bottom
3. Commit and push to the wap-brain repo
4. Open the agent's Claude Project on claude.ai
5. Re-paste the updated system prompt content into the Project instructions
6. Save

Both the file and the live Project must be updated. Editing only the file does not update the live agent. Editing only the Project does not update the file.

## How To Add A New Agent

When the WAP PM identifies a need for a new specialist (e.g., Image Agent, Video Agent, Email Agent):

1. PM drafts the agent's role, tools, scope, and rules in chat
2. Nico approves the draft
3. PM produces the system prompt content
4. Claude Code creates `agents/[NAME]_SYSTEM_PROMPT.md`
5. PM updates this file (`agents/AGENT_INDEX.md`) with a new row
6. PM updates `brain/WAP_00_INDEX.md` Agents section if it has one
7. PM updates relevant SOPs to reference the new agent in their workflows
8. Commit and push
9. Nico installs the agent into a new Claude Project per "How To Install An Agent" above

## Versioning Convention

- v1.0 = initial draft
- v1.1, v1.2... = patch updates (typo fixes, small clarifications, minor rule additions)
- v2.0 = significant architecture change (new stage, new output format, removed/added major capability)

Every version bump requires a changelog entry at the bottom of the agent file. The entry must include: date, what changed, why.

## Parked / Future Agents

These were identified as needed but not yet built:

- **WAP Image Agent (Task 2.8):** Image sourcing, AI generation, editing, alt text, library management. Until built, SOP_01 Step 6.5 is manual (Nico).
- **Scout v2 with Perplexity Sonar API (Task 3.1):** Upgrade Scout's fact-checking with synthesis-style API. Implement only if Scout v1 UNVERIFIABLE rate exceeds 30% in Phase 3 testing.
- **Scout v2 with Firecrawl (Task 3.2):** Add full-page extraction capability when web_fetch isn't enough. Implement only if Scout v1 needs page-reading capability that built-in tools can't provide.

---

## Archived Agents

| Agent | Archived File | Replaced By | Date |
|---|---|---|---|
| WAP Copywriting v1.0 | _archived/COPYWRITING_SYSTEM_PROMPT_v1.0.md | COPYWRITER_SYSTEM_PROMPT.md (v2.0) | April 27, 2026 |

---

## Repo Reference

All agent files live in `agents/` in the wap-brain repo. This index file lives alongside them at `agents/AGENT_INDEX.md`.