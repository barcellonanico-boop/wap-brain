# SOP_03 — Capture and Store a New Story

**SOP ID:** SOP_03
**Category:** Content — Story Bank
**Owner:** WAP PM
**Last updated:** April 24, 2026
**Status:** v1.0 (untested — first real run validates)

---

## Purpose

Turn a raw story dump from Nico into a well-crafted stand-up-style anecdote, format it to the Story Bank spec, file it into `brain/stories/`, and add a rich index row to `brain/WAP_08_STORY_BANK_INDEX.md`.

Two stages, one agent, one chat.

**Stage 1 — Craft.** The Story Agent takes a chaotic dump (voice-memo transcript, messy brain-dump, copy-paste from a blog, fragment of a YouTube script) and shapes it into a 250-350 word bit in Nico's voice, following Sebastian Maniscalco setup / escalation / payoff structure. Nico iterates with the agent until the story lands.

**Stage 2 — Store.** Same agent, same chat. Once Nico says "ready," the agent runs the storage checklist: dedupe scan, strict-taxonomy tag assignment, named-business check, stats flag, pairs-with check, voice mode confirmation. Drafts the story file and the index row. Surfaces both for Nico's approval. Only then does Claude Code write the files and push.

---

## When To Use

Run SOP_03 whenever any of these happen:

- Nico tells a new story in chat, voice memo, or email
- Nico pastes an existing piece of content (his own or someone else's) that contains a story worth archiving
- A story surfaces during SOP_01 (post rescue) or SOP_02 (new post) that deserves its own Bank entry
- Nico identifies a Gap List item and dictates the raw material

Do NOT run SOP_03 when:

- The raw material is a single observation or one-liner (not a narrative with beats)
- The story is a near-duplicate of an existing entry (Stage 2 dedupe will catch this; resolution is "append a variation to the existing file," not a new S###)
- The content is a restaurant recommendation or experience recommendation only (those go to WAP_09 / WAP_10, not the Story Bank)

---

## Prerequisites

Before starting, confirm the following are accessible:

- **Current Brain docs** (WAP_00 is the index). Key docs for SOP_03:
  - WAP_05 — Voice and Persona (source of truth for Mode A / Mode B and the 21 signature moves)
  - WAP_08_STORY_BANK_INDEX.md (the master index being updated)
  - brain/stories/ folder (the story files)
  - WAP_09 — Restaurants and Bars (cross-reference for named businesses)
  - WAP_10 — Experiences (cross-reference for named experiences)
- **Claude chat or project** with the Story Agent system prompt loaded (see Section: The Story Agent System Prompt)
- **Claude Code** access for final commit and push

---

## Inputs

For every SOP_03 run, gather:

1. Raw story dump from Nico (any form)
2. Source (voice memo / chat transcript / URL if copy-pasted / etc.)
3. Optional: Nico's target goal if he states it ("this is a safety warning," "this is a food tip," "this is a laugh about the cops")

If Nico does not state a goal, the agent asks before Stage 1 begins.

---

## Outputs

Every SOP_03 run produces:

1. New story file at `brain/stories/SXXX_slug.md` with full structured format
2. New index row appended to `brain/WAP_08_STORY_BANK_INDEX.md` Master Index
3. Change Log entry in `projects/PROJECT_WAP_Content_Machine/04_Change_Log.md`
4. Any flagged side-tasks surfaced to PM (new WAP_09 entry needed, stats to verify, new tag proposed, etc.)

---

## The Story Agent System Prompt

The canonical Story Agent system prompt now lives at `agents/STORY_AGENT_SYSTEM_PROMPT.md`.

When running SOP_03, load that file as the system prompt for the Story Agent's Claude Project. Do not duplicate the content here — it would create a versioning trap (two copies that drift apart).

If the Story Agent prompt needs updating, edit `agents/STORY_AGENT_SYSTEM_PROMPT.md` directly. SOP_03 only describes the workflow, not the agent's instructions.

---

## Worked Example

**Raw dump from Nico:** "So I'm sitting at this place having an aperitivo and this British family walks in, mom dad two kids, and they order four Coca-Colas. Four. At aperitivo hour. The waiter just stares at them. In Sicily if you sit down at 7pm you're getting a spritz or a beer, that's just how it works. The waiter brings the Cokes but you can see his soul leaving his body. Then the dad asks for ice. ICE. The waiter actually laughs. Not with them. At them."

**Stage 1 output (crafted):** [Agent would shape this into 250-350 words with setup (the aperitivo scene), escalation (the Coke order, the waiter's face), payoff (the ice request, the laugh)]

**Stage 2 output:**
- Dedupe: no close match
- Tags: palermo-historic-center, food-culture, aperitivo, cultural-clash, funny, british-tourists (NEW TAG PROPOSED in topic category — approve?)
- Named business: none (location genericized)
- Stats: none
- Pairs with: S004 (Tourist Trap Dinner Time — same theme of tourists vs. local dining culture)
- Voice mode: A, free-content eligible

---

## Edge Cases

**1. Near-duplicate detected.** Agent flags at 70%+ overlap. Nico decides: append variation to existing file (add "## Variation B" section) or proceed as new. Never silently create a near-duplicate.

**2. Story mentions a business not in WAP_09/WAP_10.** Agent flags. Nico decides: add to WAP_09/10 now (quick entry), or park for later. If parked, note in change log.

**3. Story exceeds 400 words after 3 revision rounds.** Agent proposes split into two stories (each gets its own S### and SOP_03 run) or a hard cut. Nico decides. Never silently exceed cap.

**4. Nico proposes a new tag not in taxonomy.** Agent proposes placement in the taxonomy (which category, rationale). Nico approves or rejects. If approved, tag is added to WAP_08_STORY_BANK_INDEX.md taxonomy section in the same commit.

**5. Story has no clear payoff.** Agent asks: "This reads more like a scene than a story. Can you give me the ending — what happened next, or what's the point you want to land?" If Nico can't, it may not be a story yet — park in Gap List.

**6. Raw dump is not a story.** SOP_03 does not accept non-stories into the Bank. Options: (a) develop it into a story by adding beats (setup, escalation, payoff), (b) it belongs in WAP_09/10 as a place or experience entry. Which?

---

## Changelog

- v1.0 — April 24, 2026 — Initial draft. Two-stage architecture. Story Agent system prompt embedded. Worked example. 6 edge cases. Three in-flight edits: stats-age ask added (2.4), pairs bidirectional update added (2.5), observations.md option removed from Edge Case 6.