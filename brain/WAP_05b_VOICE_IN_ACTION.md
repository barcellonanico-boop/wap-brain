# WAP_05b — Voice in Action

**Last updated:** April 29, 2026
**Status:** Living doc. Patterns added as discovered.
**Pairs with:** WAP_05_VOICE_AND_PERSONA.md (rules) — this doc shows what those rules look like in published work.
**Canonical source article:** https://wearepalermo.com/palermo-tourist-information/ (Palermo Tourist Information)

---

## Why This Doc Exists

WAP_05 has the rules: 21 signature moves, Mode A vs Mode B, banned words, paragraph limits, persona definition. Reading those rules and writing in Nico voice are two different skills. The rules don't compose into voice without examples.

This doc shows the rules in action. Every pattern below is annotated from Nico's published work. Use this side-by-side with WAP_05 every time you write Pass 2 voice.

If a pattern in this doc conflicts with WAP_05, the published work wins. WAP_05 gets patched to match practice.

---

## Voice Memo Rework Discipline (locked May 2, 2026)

**The single highest-leverage voice rule in WAP, learned the hard way.**

When Nico provides a voice memo (transcribed in `05_Brain_Dump.md` or pasted in chat), the memo is NOT raw material to be reworked. It is the voice source. Treat it as canonical.

**Spoken rhythm IS written Maniscalco rhythm when it comes from Nico.**

The agent's job is to:
1. Strip filler (um, uh, "you know," "like," repetitions, false starts)
2. Split text blocks at 180 chars per WAP_06 Foundation Rule 1
3. Apply italic vocal stress where Nico's tone obviously emphasizes (sparingly)
4. Apply 0 em-dashes per WAP_05

The agent's job is NOT to:
- "Improve rhythm" — the rhythm is the source
- "Tighten prose" — Nico's prose IS the voice
- Replace specific images with generic alternatives
- Paraphrase to fit a word count target

### The transcription failure mode

Across 7 Pass 2 voice cycles (Favignana 3, where-to-stay 4), every failure was the same pattern. Agent received voice memo. Agent paraphrased to "make it flow better." Output read as memo-shaped prose with extra italics. Nico rejected.

The instinct to "improve" voice memo prose IS the failure. Resist it.

### Worked example: catcalling callout

**Voice memo source (Nico, raw):**

> "the thing that makes me laugh the most and pisses off the female tourists I see the most is the catcalling — typically not exactly people known for extreme elegance. They're carriage guys, the ones with the carriages; they can be taxi drivers or just neighborhood punks, and the only book they've opened in their whole life is the stickers book, the soccer sticker album. These people here, unfortunately, barely maybe know how to read, let alone talk. It's not clear why, but when they see the shape of a foreign girl they start howling weird shit out of their mouths — 'hey beautiful,' stuff like that."

**Wrong (transcription with cosmetic edits):** keep as 90-word paragraph, italicize "Ciao bella!", call it done. This was v3, v4, v5 of where-to-stay — all rejected.

**Right (assembly from verbatim, filler stripped, blocks split):**

> *Quick word for the women.*
>
> The thing that pisses off female tourists more than anything? The catcalling.
>
> Who? The carriage drivers. The taxi guys at the stand. Neighborhood punks who haven't opened a book since the soccer-sticker-album.
>
> They see the shape of a foreign woman and start howling out the window. *"Ciao bella!"* That kind of stuff.

The "right" version preserves Nico's specific images (carriage drivers, taxi guys at the stand, soccer-sticker-album, howling). It strips spoken filler ("typically not exactly people known for," "unfortunately barely maybe," "weird shit out of their mouths"). It splits at 180-char text blocks. It italicizes one vocal stress. **It does NOT invent new prose.** Every distinctive phrase traces back to Nico's voice memo verbatim.

That is assembly. Anything more is paraphrasing, which is the failure mode.

### Verbatim audit (mandatory in Pass 2 self-check, per Copywriter v2.1)

For each H2 in Pass 2, compute word-overlap with the source brain-dump block. Below 80% overlap = paraphrasing failure = rebuild required.

---

## Foundation Vocabulary (Locked April 29, 2026)

Two units, two rules. Different jobs. Don't confuse them.

**Section** = everything inside one H2 (or H3). The full block of content under a heading until the next heading.

**Text Block** = one chunk of prose between two blank lines. The thing a reader's eye sees as a single unit on mobile.

**Hard rules:**

| Unit | Max | Why |
|---|---|---|
| Text Block (prose only, not bullets) | 180 characters | Mobile readability. No walls of text. |
| Section | 300-400 words | Mobile readability. Break with H3 sub-section or inline image if longer. |

If a text block exceeds 180 chars, split it at a sentence boundary.
If a section exceeds 400 words, break it with an H3 or an inline image.
If both, use both.

---

## Pattern A — Author Intro Architecture (8 Steps)

**Hard order. No skipping.**

Reference: Tourist Info article, opening sequence (italic lead through TL;DR).

**The 8 steps:**

1. **Italic lead** — promise/USP in <25 words. Must be SPECIFIC and STRONG. Generic framing ("the only guide you need," "everything you need to know") is too weak. The lead has to name the actual unique value.

2. **Featured image** — plain `<img>`, no `[caption]` shortcode (per WAP_06 D8 patch).

3. **Disarming opener block** — "I know, I know" or equivalent. Acknowledges the reader's skepticism or problem BEFORE they voice it. Reader has to feel understood. Mocking imagined dialogue often lives here.

4. **Name + credibility + sales hook** — one paragraph, ~80-100 words. Concrete sensory specifics ("born and raised on pasta, pizza, and seawater" type). Bold on identity, italic on emphasis word.

5. **Three bullet points: "what you'll learn"** — concrete and specific. Not generic. The bullets tell the reader the article delivers on the USP.

6. **One sentence highlighting time-vs-benefit** — "this saves you from doing the painful thing yourself." Frames why reading beats the alternative. Short. Example mode: "less time and more effective results than wasting nights scrolling through Airbnb pictures only to end up in a shitty place anyway." Don't have to use that exact phrasing — that's the rhythm.

7. **TL;DR table** — structured `<table>` with 4-row default (What it is / How to get there / How long / When to go) plus optional 5th row "Where to stay" with affiliate links. NOT a callout. NOT a `<p>` block. See WAP_06 TL;DR Template.

8. **Affiliate disclosure box** — small grey neutral, Nico-voiced. Position: AFTER the TL;DR (per WAP_06 D1 patch).

**Annotated example — Tourist Info opening:**

> *Alright, you're looking for Palermo tourist information? This is the only guide you actually need to read before you land.*

[ITALIC LEAD — note: weak USP. "the only guide you actually need" is plain. Future intros need stronger USP language.]

> I know, I know. Another guide. Today we're talking about "Palermo Tourist Information."

[DISARMING OPENER — acknowledges reader skepticism instantly]

> You know, that pain-in-the-neck stuff you find in the back of travel guides. Yeah, *that* stuff. The essential info that's usually as boring as watching paint dry, but… it's also super useful.

[HYPERBOLIC SPECIFIC + SETUP — "boring as watching paint dry" sets up the "but"]

> But don't click away. We'll kill the boredom, I promise. I'm going to tell you some things that will change your perspective, stuff you won't find in any book.

[SALES HOOK — promises specific value: "stuff you won't find in any book"]

> I know our brains are zombified by Instagram and we've forgotten how to read. But stay with me. Give me five minutes.

[TIME-BOUND CONTRACT — lowers the commitment ask]

> I'm **Nico, a 100% Sicilian** born and raised on pasta, pizza, and sea water, and I *promise* this information will change your vacation.

[NAME + CREDIBILITY + PROMISE — all 3 jobs in one sentence. Bold on identity, italic on emphasis word.]

> Why? Because if you don't know this stuff, you'll get here, you'll get frustrated, and you'll go leave a bad review.
>
> "*It was dirty!*"
> "*The traffic was awful!*"
> "*Everything was closed at 2 PM!*"
>
> And you know the truth? It's not the city's fault. It's *your* fault. Because you showed up unprepared.

[MOCKING IMAGINED DIALOGUE — three quoted italicized lines. Then the slap: "It's *your* fault."]

**Note on Tourist Info gaps:** the Tourist Info article does NOT include the 3-bullet "what you'll learn" overview (step 5) or the time-vs-benefit sentence (step 6). These are NEW rules locked April 29, 2026. Future intros include them. The article is otherwise gold standard.

---

## Pattern B — Section Architecture

**Hard rules per H2 section:**

1. H2 heading
2. **Image immediately after H2** (mandatory, every section)
3. Body prose in text blocks (each ≤180 characters)
4. If section is approaching 300-400 words, break with H3 sub-section
5. If a paragraph block is dense, break with an inline image
6. **Closing callout(s)** — Local's Take / Pick / Warning. Mandatory. Multiple callouts allowed if topic warrants (e.g., a Warning AND a Take).

**Exceptions:** Conclusion section and FAQ section don't follow this — they have their own patterns (see G and I below).

**Why it works:** the section closer (callout) gives every H2 a visual punctuation mark. Reader never gets to the next H2 thinking "where does this section end?" The callout completes the section.

---

## Pattern C — Callout Content Distinction

| Variant | Content type | When to use |
|---|---|---|
| **Local's Pick** | Recommendation | "September is the perfect time" — when you'd give a verdict if asked |
| **Local's Take** | Opinion / personal aside | "A quick tip on ATMs" — Nico note that's not a hard recommendation |
| **Local's Warning** | Cautionary | "Don't be that guy" — scams, traps, dangers, mistakes |

Multiple callouts in one section is fine when topic warrants (Warning + Take, Pick + Warning, etc.).

HTML pattern with wpautop blank-line rule: see WAP_06 D5 patch.

---

## Pattern D — First-Person Stories (Two Valid Modes)

**Mode 1: Long narrative stories**
- "Once I brought a Nordic friend over and she turned full lobster"
- "I had to return a bike at 2 PM, showed up, closed for lunch"
- Specific, time-anchored, narrative event

**Mode 2: Habitual personal practice**
- "I go there once a year, typically in July, for a long weekend"
- "I usually stay at this Airbnb"
- "Whenever we have to give tips, instead of saying 'this is the best place,' say 'this is usually where I go and consider it the best'"
- Pattern of behavior, not single event

**Frequency:** as natural as possible. No hard count. The rule: **the post must not read as detached recommendations.** First-person presence (either mode) is what passes E-E-A-T.

**Why it matters:** AI Overviews and competitor blogs cannot replicate "this is where I usually go." That phrase converts a recommendation into lived experience. Same information. Completely different reader trust.

---

## Pattern E — Mocking Imagined Dialogue (4 Jobs)

The single highest-impact voice move. Quoted, italicized, short.

**4 jobs the move can do:**

1. **Imagining the reader's bad take** — "It was dirty!" / "The traffic was awful!" — confronts reader with their own potential failure mode.

2. **Imagining the reader's stupid alternative** — "I'll come by kayak!" / "I'll ride a horse!" — comic absurdity escalation. Often stacked 2-3 lines for ladder effect.

3. **Imagining the antagonist's lie** — "*Ah, no… the POS is broken. Cash only.*" — exposes scams by quoting the script.

4. **Imagining a Sicilian's reaction** — "*All that milk! He'll be sick!*" — gives cultural perspective in voice.

**Format rules:**
- Always quoted (`"..."` or `'...'`)
- Always italicized
- Default short (3-12 words per line)
- Often stacked 2-3 lines for escalation
- Often followed by a slap line ("And you know the truth? It's *your* fault")
- Longer quoted lines are rare but allowed if rhythm holds
- Don't force where it doesn't fit — some sections (logistics-heavy, emergency, simple facts) don't need this move

---

## Pattern F — Local's Callout 3-Beat Structure

Every callout (regardless of variant) follows hook → body → slap.

**Beat 1 — Hook (1 line):** disarming opener, direct address, or rhetorical question
- "You want the honest truth?"
- "Look, I'm not trying to give you style lessons."
- "About those parking guys (*posteggiatori abusivi*)."

**Beat 2 — Body (2-3 lines):** the specific advice with ONE signature voice move
- Italic stress
- Mocking dialogue
- Hyperbolic specific
- Parallel rhythm

**Beat 3 — Slap closer (3-7 words):** one-line verdict, no hedging
- "It's the ideal."
- "That's it."
- "Don't give them 5 euros."

**Word count:** 30-50 words typical. If a callout reads as continuous prose at 80+ words, it's failing the 3-beat structure.

---

## Pattern G — Italic Vocal Stress vs Bold for Topics

Two different jobs. Both valid. Don't conflate.

| Use | When | Example |
|---|---|---|
| **Italic** | Vocal stress (you'd say it that way out loud) | "the *perfect* time is September" |
| **Bold** | Skim-keyword for scanners (≤12 word phrase) | "**minimum of three full days**" |

A long paragraph should have at least one bolded skim-keyword (per WAP_06 D7 patch, pending). Italic is sprinkled for rhythm, not skim-scanning.

Never conflate them: a sentence with everything bolded is a sentence saying nothing.

---

## Pattern H — FAQ Pattern (3-Beat + One Move)

**Structure of every FAQ answer:**

**Beat 1 — Framing opener (1 sentence):** does NOT answer the question. Positions Nico against the reader.
- "I know, you're in a hurry."
- "Smart. You can't just stay in the city."
- "Ah, the million-dollar question."

**Beat 2 — Answer with ONE signature move (2-3 sentences):** exactly one move per answer. Not three. Not none.
- Negative-then-positive ("It's madness" → "minimum three full days")
- Mocking expectation ("Don't try to do Agrigento and back unless you enjoy sitting on a bus for 5 hours")
- Insider-vs-tourist framing ("TripAdvisor top 10... tourist spots. The **real** places... I've spent years collecting them")

**Beat 3 — Slap closer + optional CTA (1 sentence):** if there's a CTA, the closer EARNS it
- Pure slap: "Anything less, and you're just ticking boxes for Instagram and you'll leave frustrated."
- Slap + CTA: "I've got a full guide on the [places nearby that are actually worth your time](LINK)."

**Format rules:**
- 60-100 words per answer (tighter than body prose)
- 6-8 FAQs per article (hard range, never less than 6, never more than 8)
- Bold for skim-keywords inside answers (same rule as body)
- One link per answer maximum, always soft close
- NO callouts inside FAQ section
- Conversational question wording ("How many days do I actually need to 'see' Palermo?") not formal
- ONE FAQ per post does the paid-product pitch (not all of them)

**The paid-pitch FAQ pattern:**

Structured as: question every reader is asking → honest answer that proves Nico knows → "but for the full thing, the paid guide."

Example: FAQ #6 in Tourist Info ("Where are the best restaurants?"). The answer mocks TripAdvisor first ("if you follow the TripAdvisor top 10, you are going to eat at tourist spots"), then positions the paid product as the real answer.

The pitch lands because the answer above already gave value. Reader paid with attention. The pitch is the natural close.

---

## Pattern I — Conclusion Architecture (4 Jobs)

**Length: 100-180 words total.**

**Job 1 — Disarming opener with reward framing**

Reward the reader for finishing. They did the work. Make them feel like they're better than the tourists who didn't.

- "I know, I know. That was a lot. But look how much you know now compared to those shitty tourists out there."
- "Good job, you're a traveler now, not one of those tourists who feeds pigeons and sits where the waiter reels them in."

This is a callback to the intro's "I know, I know" — intro and conclusion form a matching pair. Reader feels closure.

**Job 2 — 3-5 numbered takeaways**

NOT a recap of the article. The 5 things the reader will REGRET not knowing.

Format:
- Each bullet bolded skim-keyword
- Most bullets hyperlink to related WAP content (internal link funnel)
- One short sentence per point — no walls of text

**Job 3 — Ironic channel menu CTA**

The conclusion converts via the channel menu. Each channel framed in voice with self-deprecating irony.

The 4 channels:

| Channel | Voice frame | URL |
|---|---|---|
| Instagram | "for people with attention problems who can't focus more than 10 seconds" | https://www.instagram.com/wearepalermo_sicily/ |
| TikTok | "for people with attention problems who can't focus more than 10 seconds" | https://www.tiktok.com/@wearepalermo |
| YouTube | "Palermo Netflix — binge these long-ass videos and literally turn into a Sicilian" | https://www.youtube.com/@WeArePalermo |
| We Are Palermo Premium Guide | "everything you're desperately looking for and that I'll never tell you for free because I've gotta pay for this whole circus" | https://wearepalermo.podia.com/the-sicilian-way |

**The TripAdvisor joke (use when relevant, not always):**

When the article touches restaurants, recommendations, or "where do I go" topics, the conclusion can drop:

"TripAdvisor is fantastic because Sicilians don't use it, so it's tourists recommending stuff to other tourists. Amazing!"

The joke earns its place when it lands in context. Don't force it on a transport-only or logistics-only post.

**Job 4 — Signature.** Every post ends with:

> Un grande abbraccio,
> *Nico Barcellona*

Italian, untranslated. The English literal "A hug is always" doesn't make sense in English and was deprecated April 29, 2026. Pairs with the bilingual identity (Italian-American comedian persona). Same logic as keeping "*capito?*" or "*scimunito*" untranslated mid-article.

Brand consistency. Every post.

---

## Three Foundation Rules (Reinforced)

These three rules underpin every pattern above. Violating them breaks voice.

### Rule 1 — Text Block max 180 characters

Every prose text block under 180 chars. Bullets and tables don't count (they're already visually broken).

### Rule 2 — Section max 300-400 words

Break with H3 sub-section or inline image if longer.

### Rule 3 — Alternation rhythm (HARD)

Vary text block length within a section. Long → short → long → very short.

Don't string 4 long blocks in a row. Don't string 4 short blocks either. Mix them.

Use one-word sentences ("But.") and three-word slams ("Let's be smart.") as rhythm breaks.

**Example from Tourist Info Section 1 (annotated):**

> So when should you come? Ask any Sicilian, and they'll scream, "ALWAYS! Palermo is always beautiful, *capito*!?"

[LONG TEXT BLOCK — ~25 words, mocking dialogue]

> …and yeah, it's true. But. There's always a 'but'.

[SHORT TEXT BLOCK — 11 words, with a one-word "But." breaking rhythm]

> You wanna come in August? Go ahead. But it's 40 degrees in the shade (104°F). Your internal organs will start to slow-cook. Not exactly the best vibe for sightseeing, is it?

[LONG TEXT BLOCK — ~30 words, hyperbolic specific "internal organs slow-cook"]

> Let's be smart.

[THREE-WORD SLAM — rhythm reset before the bullet list]

This is deliberate. The reader's eye never gets tired. Every section needs this rhythm.

---

## Patterns Pending (Future Annotation)

When patterns surface from future posts that aren't covered here, log them as new entries. WAP_05b is a living doc.

Currently uncovered:
- Hotel card voice patterns (formal copy vs Nico copy in tagline + description)
- Pricing reality block voice (Favignana "grandmas renting basically holes" pattern — could become Pattern J)
- Comparison section voice (Favignana H2 9 "Favignana vs Other Sicilian Islands" pattern)
- Image alt text voice rules (currently minimal per Nico preference, document if standardized)

Add as needed.

---

## Versioning

- **v1.0 — April 29, 2026** — Initial doc. Patterns A-I locked from collaborative annotation session with Nico (Pass 2 voice failure on Favignana triggered creation). Source article: Tourist Info. 3 foundation rules established (text block, section, alternation).
