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

## The Story Agent

### Stage 1 — Craft

The Story Agent receives Nico's raw dump and crafts it into a story.

**Rules:**

1.1. Target word count: 250-350 words. Hard cap: 400. If the raw material pushes past 400, the agent must either cut or propose splitting into two stories. Never silently exceed 400.

1.2. Structure: Sebastian Maniscalco setup / escalation / payoff. Every story needs:
   - **Setup** — scene, context, who's involved
   - **Escalation** — things get weird, funny, frustrating, or surprising
   - **Payoff** — the punchline, the lesson, the reveal, or the "only in Palermo" moment

1.3. Voice: default to Mode A (WAP_05). If Nico says the story is for paid content or a more reflective tone, switch to Mode B. Confirm mode with Nico before finalizing.

1.4. The agent asks clarifying questions if the raw dump is missing beats. "What happened next?" "How did it end?" "Was anyone else there?" Keep questions surgical — no essays.

1.5. Nico iterates. The agent applies surgical feedback exactly. No creative additions beyond what Nico flags. Max 3 revision rounds — if a fourth is needed, the raw material needs a re-dump, not more polishing.

1.6. When Nico says "ready" (or equivalent: "good," "done," "that's it"), Stage 1 ends. The agent confirms: "Story locked. Moving to Stage 2 — storage checklist."

---

### Stage 2 — Store

Once the story is locked, the agent runs this checklist IN ORDER. Each step produces output that Nico sees before proceeding.

**2.1. Dedupe scan**

Scan WAP_08_STORY_BANK_INDEX.md for thematic overlap with existing stories.

- If 70%+ thematic overlap with an existing entry: flag. Options: (a) append as a variation to the existing file, (b) proceed as new entry if Nico confirms it's distinct enough.
- If <70% overlap: proceed.

Report: "Scanned [N] existing stories. Closest match: [SXXX title] at ~[X]% overlap. Proceeding as new entry." OR "Flag: [SXXX title] has ~[X]% overlap. Append variation or new entry?"

**2.2. Tag assignment (strict taxonomy)**

Assign tags from the EXISTING taxonomy in WAP_08_STORY_BANK_INDEX.md ONLY.

- Location tags: pick from existing location tags
- Topic tags: pick from existing topic tags
- Practical tags: pick from existing practical tags
- Vibe/tone tags: pick from existing vibe/tone tags

If a tag does not exist in the taxonomy but is clearly needed:
1. Propose the new tag to Nico with category and rationale
2. If Nico approves, add it to the taxonomy as part of this SOP run
3. If Nico rejects, find the closest existing tag

**Never invent a tag silently.** This is the rule that resolves the Apr 22 process flag.

Report: "Proposed tags: [list]. All from existing taxonomy." OR "Proposed tags: [list]. NEW TAG PROPOSED: [tag] in [category] because [reason]. Approve?"

**2.3. Named-business check**

Scan the story for any named business (restaurant, bar, hotel, tour, shop).

For each named business:
1. Check WAP_09 (restaurants/bars) and WAP_10 (experiences) for an existing entry
2. If found: note the cross-reference in the story file's Named Business Flags field
3. If NOT found: flag for Nico — "Does [business] need a WAP_09/WAP_10 entry?"
4. Confirm the Named Business Flag: FREE (can name in free content), PAID_ONLY (genericize in free content), or GENERICIZE_ALWAYS

Report: "Named businesses found: [list with WAP_09/10 cross-refs and flag status]." OR "No named businesses in this story."

**2.4. Stats flag**

Scan the story for any statistical claim, historical fact, or specific number.

For each:
1. Note the claim
2. Flag as [VERIFY BEFORE PUBLISHING]
3. If the claim is over 3 years old or you have any doubt, note in the change log entry for PM to re-verify before publishing
4. Ask Nico the approximate age of any specific statistical or historical claim. The agent cannot infer claim age without asking.

Report: "Stats/claims found: [list with VERIFY flags]." OR "No statistical claims in this story."

**2.5. Pairs-with check**

Scan WAP_08_STORY_BANK_INDEX.md for stories that pair thematically with this one (sister stories, contrasting takes, same-location different-angle).

List any pairs found. Populate the Pairs with field.

Pairs are bidirectional. If a pair is identified, the existing story's index row in WAP_08_STORY_BANK_INDEX.md must also be updated to reference the new story. The agent drafts both index-row updates and surfaces both to Nico for approval before Claude Code execution.

Report: "Pairs with: [SXXX] ([reason])." OR "No strong pairs found."

**2.6. Voice mode confirmation**

Confirm with Nico:
- Mode A (comedian, conversational, free content) or Mode B (reflective, longer sentences, paid content)?
- Free-content eligible, paid-only, or both?

---

### Stage 2 Output — Draft for Approval

After completing 2.1-2.6, the agent drafts:

**A. Story file** (`brain/stories/SXXX_slug.md`):

```markdown
# SXXX — [Title]

**Goal:** [What this story achieves when deployed]
**Source:** [Where the raw material came from]
**Date captured:** [Today's date]
**Voice mode:** [A / B]
**Content eligibility:** [Free / Paid only / Both]
**Word count:** [N]

## Tags

- **Location:** [tags]
- **Topic:** [tags]
- **Practical:** [tags]
- **Vibe/tone:** [tags]

## Named Business Flags

[Business name] — [FREE / PAID_ONLY / GENERICIZE_ALWAYS] — [WAP_09/10 ref if exists]

## The Story

[Full crafted story text from Stage 1]

## Pullable Hooks

- [2-4 hooks: specific lines or moments that can be extracted for use in posts]

## Core Observations

- [1-3 observations: the deeper point the story makes about Palermo, travel, or life]

## Pairs With

- [SXXX] — [reason for pairing]

## Use Cases

- [2-4 specific post topics or contexts where this story fits]

## Stats to Verify

- [Any flagged claims with VERIFY status, or "None"]
```

**B. Index row** for WAP_08_STORY_BANK_INDEX.md:

The agent drafts a rich index row matching the existing format in the Master Index (title, tags summary, pullable hooks preview, core observations preview, pairs with, named business flags, use cases).

**C. Change log entry** for `projects/PROJECT_WAP_Content_Machine/04_Change_Log.md`:

Single row with date, what changed, details (story ID, title, tags, any flags surfaced, any new WAP_09/10 entries needed, any stats to verify).

The agent presents A, B, and C to Nico for approval. Nico approves or requests changes. Once approved, Claude Code writes the files and pushes.

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