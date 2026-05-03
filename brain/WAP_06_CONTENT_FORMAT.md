# WAP_06_CONTENT_FORMAT.md — Content Format and Publishing Rules

Last updated: April 29, 2026 (Apr 29 v2.2: cleanup pass — killed duplicate paragraph-length rule, renumbered author intro 1-8 to match WAP_05b. Apr 29 v2.1: author intro 8-step, section architecture, foundation rules, conclusion 4-job, brand rename Sicilian Way → We Are Palermo Premium Guide. Apr 28: P0 patches D1-D6.)

This doc defines HOW a WAP blog post is structured: intro, sections, paragraphs, text boxes, images, affiliate handling, schema, publishing checklist. Voice rules live in WAP_05_VOICE_AND_PERSONA.md. This doc covers everything else.

If a rule here conflicts with WAP_05, WAP_05 wins. Voice is strategy. Format serves voice.

---

## Why This Doc Exists

Two jobs.

Job one: consistency. Every WAP post should look, feel, and read the same way. Readers who land on one post and like it should find the same rhythm when they land on another.

Job two: SEO and AI Overviews. Task 1.8 research established that structure is now a direct ranking factor. 44% of AI Overview citations come from the first 30% of a page. Pages under 540 words of "grounding content" at the top get cited. Pages that bury the answer lose the citation to a competitor.

Structure is not decoration. It's how WAP ranks.

---

## Foundation Rules (Apr 29 — Hard Rules)

Two units, two rules. Different jobs. Don't confuse them.

**Section** = everything inside one H2 (or H3). Full block of content under a heading.

**Text Block** = one chunk of prose between two blank lines. What the reader's eye sees as one unit on mobile.

| Unit | Max | Why |
|---|---|---|
| Text Block (prose only, not bullets/tables) | **180 characters** | Mobile readability. No walls of text. |
| Section | **300-400 words** | Mobile readability. Break with H3 or inline image if longer. |

If a text block exceeds 180 chars, split at sentence boundary.
If a section exceeds 400 words, break with H3 or inline image (or both).

### Alternation Rhythm (Hard Rule)

Vary text block length within a section. Long → short → long → very short.

Don't string 4 long blocks in a row. Don't string 4 short blocks either. Mix them.

Use one-word sentences ("But.") and three-word slams ("Let's be smart.") as rhythm breaks.

Reference: WAP_05b Foundation Rules (annotated example with Section 1 of Tourist Info article).

### Foundation Rule 1.5 — Callout content limit (LOCKED May 3, 2026, tightened evening)

The 180-character text-block limit (Foundation Rule 1) applies inside callouts.

**Specifically:**
- Each `<p>` inside a callout div: ≤180 characters
- Total callout text content (sum of all `<p>` inside the callout div, excluding cite header): ≤250 characters
- Total text blocks per callout: max 4 (excluding the cite header)
- If callout content exceeds these limits: content moves to body prose H3 section, callout becomes punchy summary

Use line breaks to keep visual rhythm. Don't pile sentences into a single block. Don't write paragraphs inside a callout.

**Why:** Callouts are visual emphasis, not overflow holding pens. A 9-paragraph callout reads worse than 9 paragraphs in body prose. Per Finding #79.

**Wrong (May 2 Pass 3 v3 Hotel WiFi callout):** 9 paragraphs of detail in colored box.

**Right:** 3-block callout summary (warning + 1 specific tip + slap closer). Full explainer becomes H3 sub-section in body.

**Pass 3 self-check requirement:** bash audit confirms (a) every `<p>` inside callout ≤180 chars, (b) total callout text ≤250 chars, (c) every callout div has ≤4 `<p>` children.

Locked May 3, 2026 (numbers tightened from initial v0.1 of 180 only).

### Foundation Rule 2 — Section Balance (LOCKED May 3, 2026)

H2 sections: target 300-400 words of body prose.
H3 sub-sections: target ≥80 words OR merge with parent / sibling.

If H3 sub-section <50 words: it's a fragment, not a section. Either merge with sibling H3 or absorb into parent H2 prose. Per Finding #81.

---

## The Content Rule That Overrides Everything

**Specific restaurants, bars, and experience providers are NEVER mentioned by name in free content.**

This rule applies to: blog posts, YouTube videos, social media, newsletters.

Specific recommendations are EXCLUSIVELY for paid products: the We Are Palermo Premium Guide and The Restaurant Guide.

You can reference food categories ("arancini at the markets"), general areas ("seafood in the historic center"), and dish names ("the best pani ca meusa is in the old markets"). You cannot name the specific trattoria, bar, or tour operator.

If an AI draft names a specific venue, reject and rewrite. No exceptions.

---

## Terminology

Before anything else, vocabulary:

- **Section** = one full H2 block with headline and everything under it until the next H2. A section can be 50 words or 500 words. No rule on section length.
- **Paragraph** = one chunk of text, 1-2 sentences, separated by a blank line from the next chunk.
- **Text box** = styled HTML block with Nico photo + colored background. Three variants: Take, Pick, Warning. Templates at the end of this doc.
- **TL;DR** = the direct-answer block that goes under the H1 before anything else.

---

## Post Types and Word Counts

Different post types get different word count ranges. Based on 2026 data (Ahrefs 174,000-page AI Overview study): longer is NOT winning in AI Overviews, 53% of citations go to pages under 1,000 words.

| Post Type | Target Words | Examples |
|---|---|---|
| Quick-answer / practical | 800-1,500 | ZTL explained, airport transfers, tipping in Sicily |
| Standard guide | 1,500-2,500 | Where to stay in Palermo, best pizzerias, is Palermo safe |
| Comprehensive guide | 2,500-4,000 | Renting a car, how many days in Palermo, first-timer guide |
| Itinerary | 3,000-5,000 | Sicily itinerary, Palermo in 3 days |
| Pillar / hub | 3,000-5,000 | What to eat hub, things to do hub |

**Absolute ceiling: 5,000 words.** Beyond that, AI extractability drops to 12% (Task 1.8 Rule 2.3). If a topic genuinely needs more, split into two posts and link them.

**Absolute floor: 800 words.** Below that, Google treats it as thin content.

---

## The 540-Word Rule (Most Important Rule in This Doc)

**The complete answer to the post's main question must appear in the first 540 words.**

Source: AI engines' content grounding plateaus at ~540 words. If the answer is buried after that, Google grabs a competitor's answer for the AI Overview.

This does NOT mean the post ends at 540 words. It means a reader or an AI crawler reading only the first 540 words should come away with the full answer. Everything after is nuance, detail, stories, specifics.

Test: if you deleted everything after word 540, would the post still answer the headline question? If no, you buried the answer. Rewrite.

---

## Paragraph Length — See Foundation Rules

Paragraph-length rules live in the Foundation Rules section at the top of this doc (text block max 180 characters, section max 300-400 words, alternation rhythm). Single source of truth.

Mobile reading examples (from Nico's rental article) showing correct text block rhythm:

> "Ready to give you the insider scoop on renting a car during your vacation in Palermo." ✅

> "If you put the legends aside and follow the tips I am about to give you, having your own set of wheels opens up a world of possibilities." ✅ (at 173 chars, near the 180 ceiling)

> "Don't. Be. That. Guy." ✅ (one-sentence text block for rhythm — see Alternation Rhythm)

The Apr 29 v2.1 cleanup deleted the older "30 words / 140 chars / 45 words" rule because it conflicted with the 180-char text block standard. If you find any reference to "45 words" or "30 words" as a paragraph limit elsewhere, it's stale — flag it.

---

## The WAP Post Structure (in order)

Every blog post follows this structure. No exceptions.

### 1. Italic Lead

One italic sentence, max 25 words, directly above the main image. Contains the primary keyword or a close variation. States the USP of the article.

Example: *"This article is your absolute bible for renting a car in Palermo without losing your mind, your deposit, or your dignity."*

Not: *"In this article, we'll explore everything you need to know about car rentals in Palermo."* (Generic, dead, Fireable Offense #1 territory.)

### 2. Featured Image

Plain `<img>` element. No `[caption]` shortcode. 800x530 pixels minimum. Descriptive alt text with primary keyword. Not keyword-stuffed.

### Author Intro Architecture (8 Steps — canonical Apr 29)

The author intro is NOT 3 jobs in one paragraph. It's an 8-step opening sequence. Hard order. No skipping. Same numbering as WAP_05b Pattern A.

1. **Italic lead** — promise/USP in <25 words. SPECIFIC and STRONG. Generic framing ("the only guide you need") is too weak. The lead names the unique value.

2. **Featured image** — plain `<img>`, no `[caption]` shortcode. See Featured Image Pattern below.

3. **Disarming opener block** — "I know, I know" or equivalent. Acknowledges reader skepticism BEFORE they voice it. Reader feels understood. Mocking imagined dialogue often lives here.

4. **Name + credibility + sales hook** — one paragraph, ~80-100 words. Concrete sensory specifics ("born and raised on pasta, pizza, and seawater"). Bold on identity, italic on emphasis word.

5. **Three bullet points: "what you'll learn"** — concrete and specific. Not generic. The bullets prove the article delivers on the USP.

6. **One sentence: time-vs-benefit framing** — "this saves you from doing the painful thing yourself." Short. Frames why reading beats the alternative.

7. **TL;DR table** — structured `<table>` with rows. See TL;DR Template below. NOT a callout. NOT a `<p>` block.

8. **Affiliate disclosure box** — small grey neutral, Nico-voiced. Position: AFTER the TL;DR (per D1).

Reference: WAP_05b Pattern A (annotated example with Tourist Info opening).

Note: steps 1 and 2 (italic lead, featured image) may also appear in the "Post Structure" section above as separate items 1-2 of the post skeleton. They appear once in the rendered post but are listed in both places for clarity (skeleton order + author intro architecture). Same elements, different framings.

Reference: WAP_05b Pattern A (annotated example with Tourist Info opening).

### 8 (expanded). Affiliate Disclosure (AFTER TL;DR — Apr 28 canonical)

**UPDATED Apr 28:** Affiliate disclosure position is AFTER TL;DR, not before. ONE affiliate disclosure per post. The previously-spec'd bottom disclosure is removed entirely.

New canonical order: Italic lead → Featured image → Author intro → TL;DR → **Affiliate disclosure** → H2 1.

Reasoning per Nico Apr 28 publish session: "the text box with the warning for links where there's an affiliation is in the new position. I did it on purpose, you have to leave it there. And you can absolutely put it as a rule." Top-only is non-redundant; reader hits the disclosure at the moment they're about to consume affiliate-loaded content (TL;DR has affiliate links in the "Where to stay" row).

In Nico voice. Short. Honest. Unobtrusive. Does not generic-blog it.

**Canonical HTML (May 3 evening):**

```html
<div style="background-color: #f5f5f5; padding: 10px 14px; border-radius: 6px; margin: 15px 0; font-size: 0.75em; color: #888; line-height: 1.4;">
<em>Heads up. Some links here might be affiliate links. Same price for you. I get a small cut so I can keep doing this and not go work in a bank.</em>
</div>
```

**Key specs:** `font-size: 0.75em` (smallest legible), `color: #888` (light grey), "might be" not "are" (less definitive), padding `10px 14px` (smaller box). Present but unobtrusive.

Never use generic "this post may contain affiliate links." Always Maniscalco-flavored.

---

## Affiliate Opportunity Check (LOCKED May 3, 2026)

**Principle: "We don't do things for free."**

For every article (new or rewrite), the writer must check WAP_12 for affiliate opportunities relevant to the article's topic. If a relevant affiliate option exists in WAP_12 and the article naturally discusses that topic without linking, that's a missed revenue opportunity.

**Check applies to:** Booking.com (hotels), GetYourGuide (tours), Discover Cars (rentals).

**When to add:** Article mentions a category that has affiliate inventory in WAP_12. Mention is natural, not forced. Link doesn't disrupt reader flow.

**When NOT to add:** Forcing a link where it doesn't fit. Linking to a competitor's hotel to fill a slot. Mentioning specific restaurants by name (paid-only rule, WAP_03).

**Workflow:**
1. Phase 1 (tech recon): Architect surfaces affiliate opportunities. Question for Nico: "These WAP_12 options are relevant. Add any?"
2. Phase 3 (brain dump): Nico answers — which to add, which to skip.
3. Phase 5 (first draft): writer keeps existing affiliate links + adds new ones from Phase 3.
4. Phase 8 (auditor): mechanical check that decided affiliate links are present.

Per Nico May 3, 2026: revenue is the goal. Articles must monetize where natural.

---

### Section Architecture (Hard Rules — Apr 29)

Every H2 section follows this structure. Hard rules.

1. H2 heading
2. **Image immediately after H2** — mandatory, every section
3. Body prose in text blocks (each ≤180 characters per Foundation Rule 1)
4. If section approaches 300-400 words, break with H3 sub-section (Foundation Rule 2)
5. If a paragraph block is dense, break with an inline image
6. **Closing callout(s) — MANDATORY for every H2 section, except FAQ + Conclusion sections.** Variants: Local's Take, Local's Pick, Local's Warning. Multiple callouts allowed if topic warrants. Intro section's TL;DR table substitutes for the closing callout requirement (TL;DR serves the summary job).

**Why mandatory:** callouts give the reader a visual anchor at the end of every section. Without one, the section ends in a flat paragraph with no rhythm break before the next H2.

**Exception list (callout NOT required):**
- Intro section (TL;DR substitutes)
- FAQ section (own format)
- Conclusion section (4-job pattern substitutes)

Per WAP_05b Pattern B and Nico clarification May 3, 2026.

### 6. Main Content — H2 Sections

Every H2 is a natural-language question. Not "Best Time" — "When is the best time to visit Palermo?"

Under each H2:
- First paragraph = direct answer to the H2 question (self-contained, makes sense alone)
- Following paragraphs = detail, examples, nuance, stories
- At least one text box per H2 (or one every ~300 words in long sections)
- One image per H2 section if visual content helps
- Internal links to 2-3 related WAP posts where natural

### 7. FAQ Section

Mandatory at the bottom of every post. 4-6 questions. Each answer 40-75 words. Each answer self-contained.

Uses FAQPage schema (template below). Questions phrased EXACTLY as a searcher would type them.

### 8. Conclusion Architecture (4 Jobs — Apr 29)

Length: 100-180 words total.

**Job 1 — Disarming opener with reward framing.** Reward the reader for finishing. Make them feel they're better than the tourists who didn't.
- "I know, I know. That was a lot. But look how much you know now compared to those shitty tourists out there."
- Callback to intro's "I know, I know" — frames closure.

**Job 2 — 3-5 numbered takeaways.** NOT a recap of the article. The 3-5 things the reader will REGRET not knowing.
- Each bullet bolded skim-keyword
- Most bullets hyperlink to related WAP content
- One short sentence per point

**Job 3 — Ironic channel menu CTA.** Each channel framed in voice with self-deprecating irony.

| Channel | Voice frame | URL |
|---|---|---|
| Instagram | "for people with attention problems who can't focus more than 10 seconds" | https://www.instagram.com/wearepalermo_sicily/ |
| TikTok | (same goldfish-attention frame) | https://www.tiktok.com/@wearepalermo |
| YouTube | "Palermo Netflix — binge these long-ass videos and literally turn into a Sicilian" | https://www.youtube.com/@WeArePalermo |
| We Are Palermo Premium Guide | "everything you're desperately looking for and that I'll never tell you for free because I've gotta pay for this whole circus" | https://wearepalermo.podia.com/the-sicilian-way |

**TripAdvisor joke** (use when relevant, not always): "TripAdvisor is fantastic because Sicilians don't use it, so it's tourists recommending stuff to other tourists. Amazing!"

**Job 4 — Signature.** Every post: "Un grande abbraccio, *Nico Barcellona*" (Italian canonical Apr 29 — English version deprecated as nonsensical literal translation)

Reference: WAP_05b Pattern I.

### 9. Continue Your Palermo Planning Block

Gray-background HTML block with 3 internal links:
- Next recommended post
- We Are Palermo Premium Guide
- WAP YouTube channel

Template below.

### 10. Signature

*Un grande abbraccio,*
*Nico Barcellona*

---

## Mandatory Elements on Every Post (Pulled From WAP_05)

These come from the voice doc. Re-stated here because they're structural requirements, not just style.

- **One Reader Interrogation** (Variant A or B) somewhere in the post. Non-negotiable. See WAP_05 Move #21.
- **At least one first-person specific observation** proving Nico was physically there. Time-anchored, physical, specific. Non-negotiable (E-E-A-T ranking signal).
- **Zero em-dashes.** Fireable Offense #1.
- **Every factual claim verified** or flagged [VERIFY: X] for Nico. Fireable Offense #2.
- **At least 3 of the 21 signature moves** from WAP_05.
- **Correct voice mode** (Mode A default, Mode B for Mafia/tragedy, religion sub-mode).

---

## SEO Rules (Pulled From Task 1.8 Research)

### On-Page

- **H1:** contains primary keyword, phrased as a searcher would type it, max 60 characters.
- **Meta title:** 55-60 characters, same pattern as H1 but can vary for click-through.
- **Meta description:** 140-155 characters, answers the question in one sentence.
- **URL slug:** short, keyword-only. Dashes between words. No stop words.
- **H2 and H3:** natural-language questions. Mirror how searchers actually phrase things.
- **Internal links:** 3-5 per post to related WAP posts, plus 1-2 to hub pages.
- **External links:** only to reliable sources (UNESCO, official tourism boards, Google Maps).
- **Image alt text:** descriptive, include keyword only if it fits naturally, never stuffed.
- **Publish date + "last updated" date** visible on every post.

### Keyword Strategy

No density targeting. Cover the topic semantically. Primary keyword appears in:
- H1
- Meta title and description
- URL slug
- First 100 words (intro + italic lead)
- At least one H2
- Conclusion

Related keywords appear naturally throughout H2s, H3s, and body text. If you have to force them, stop forcing.

### Topic Clusters

Every post links to its related hub page. Every hub page links down to its spokes. This is how Google detects topical authority in 2026 (Task 1.8 Rule 1.5).

Example: "Where to stay in Palermo" (hub) links to specific neighborhood posts. Neighborhood posts link back up to the hub and sideways to 2-3 sibling neighborhood posts.

---

## Schema Markup

WAP uses Yoast free. Yoast free handles Article schema automatically. Two schemas need manual addition.

### Author Schema

Add to author page (Nico's bio page). Template:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Nico Barcellona",
  "url": "https://wearepalermo.com/about-us/",
  "image": "https://wearepalermo.com/wp-content/uploads/2025/09/nico-barcellona-portrait-scaled.jpg",
  "jobTitle": "Founder and Writer",
  "worksFor": {
    "@type": "Organization",
    "name": "We Are Palermo",
    "url": "https://wearepalermo.com"
  },
  "sameAs": [
    "https://www.youtube.com/@WeArePalermo",
    "[INSTAGRAM URL IF REACTIVATED]",
    "[TIKTOK URL IF REACTIVATED]"
  ],
  "description": "Born-and-raised Sicilian from Palermo. Writes wearepalermo.com, an English-language travel guide to Palermo and Sicily."
}
</script>
```

### FAQPage Schema

Add inside every blog post's FAQ section. Template:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "QUESTION 1 HERE",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ANSWER 1 HERE, 40-75 words, self-contained."
      }
    },
    {
      "@type": "Question",
      "name": "QUESTION 2 HERE",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ANSWER 2 HERE."
      }
    },
    {
      "@type": "Question",
      "name": "QUESTION 3 HERE",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ANSWER 3 HERE."
      }
    },
    {
      "@type": "Question",
      "name": "QUESTION 4 HERE",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "ANSWER 4 HERE."
      }
    }
  ]
}
</script>
```

Add this block in WordPress using a Custom HTML block, placed directly below the visible FAQ section.

---

## Text Box Templates (Copy and Paste)

Three variants. Each has its own color and its own Nico photo. Use consistently.

### Variant 1: Local's Take (Orange, Neutral Advice)

Use for: general insider perspective, context, "here's how locals think about this."

```html
<div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/09/nico-barcellona-portrait-scaled.jpg" alt="Nico Barcellona" /></figure>
<div>
<cite style="font-style: normal; font-weight: bold; color: #e65100;">A Local's Take:</cite>
<p style="margin: 0; color: #333;">LINE 1 OF NICO'S ADVICE.</p>
<p style="margin: 0; color: #333;">LINE 2 OF NICO'S ADVICE.</p>
<p style="margin: 0; color: #333;">LINE 3 (OPTIONAL).</p>
</div>
</div>
```

### Variant 2: Local's Pick (Green, Positive Recommendation)

Use for: specific recommendation of an area, a car type, a strategy, a move Nico endorses.

```html
<div style="background-color: #e8f5e9; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/10/Nico-top-pick.jpg" alt="Nico's Top Pick" /></figure>
<div>
<cite style="font-style: normal; font-weight: bold; color: #2e7d32;">A Local's Pick:</cite>
<p style="margin: 0; color: #333;">LINE 1 OF RECOMMENDATION.</p>
<p style="margin: 0; color: #333;">LINE 2 OF RECOMMENDATION.</p>
<p style="margin: 0; color: #333;">LINE 3 (OPTIONAL).</p>
</div>
</div>
```

### Variant 3: Local's Warning (Red, Alert / Avoid)

Use for: scam warnings, traps, things to avoid, risks.

```html
<div style="background-color: #ffebee; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/10/Nico-Barcellona-Alert.jpg" alt="Nico Barcellona alert" /></figure>
<div>
<cite style="font-style: normal; font-weight: bold; color: #d32f2f;">A Local's Warning:</cite>
<p style="margin: 0; color: #333;">LINE 1 OF WARNING.</p>
<p style="margin: 0; color: #333;">LINE 2 OF WARNING.</p>
<p style="margin: 0; color: #333;">LINE 3 (OPTIONAL).</p>
</div>
</div>
```

### Callout HTML Pattern (Canonical — Apr 28, wpautop rule)

All 3 callout variants (Local's Take orange, Local's Pick green, Local's Warning red) MUST include **blank lines inside the inner `<div>`** for WordPress's wpautop filter. Without blank lines (before `<cite>` and after the last `<p>`), wpautop eats the closing `</div>` and the callout text leaks below the box.

**Canonical pattern (Local's Take orange variant):**

```html
<div class="locals-take">
<div>

<img src="https://wearepalermo.com/wp-content/uploads/2025/09/nico-barcellona-portrait-scaled.jpg" alt="Nico Barcellona" />

<cite>Local's Take</cite>

<p>[Callout body content here.]</p>

</div>
</div>
```

**Critical:** the blank line BEFORE `<cite>` and AFTER the last `<p>` are not optional. They are required for wpautop to render correctly.

Same pattern applies to Local's Pick (green class) and Local's Warning (red class). Reference implementation: see `09_Pass4_Nico_Final.md`.

### Local's Take Photo URL (Canonical — Apr 28)

`https://wearepalermo.com/wp-content/uploads/2025/09/nico-barcellona-portrait-scaled.jpg`

This is the canonical URL used in the Tourist Info article (the gold-standard reference). The OLD `Nico-Take.png` URL from pre-2025 live posts is OUTDATED. Do not use the old URL even if it appears in legacy snapshots — those snapshots are from posts being replaced.

### Rules for Using Text Boxes

- **Frequency:** at least one per H2 section, or roughly one every 300 words of body text.
- **Length:** 2-3 short lines per box. Never more than 4.
- **Placement:** ideally at the end of a section to reinforce the point. Middle of section also works for breaking up dense content.
- **Mixing:** use all three variants across a post. If every box is a Warning, the post feels negative. If every box is a Pick, the post feels like a pitch. Balance.
- **Voice:** inside text boxes, same Nico voice rules apply (WAP_05). No generic bullet-point summaries.

---

## TL;DR Template (Canonical HTML — Apr 28)

The TL;DR is a `<table>` with rows. NOT a `<p>` block in a colored div. Reasoning: mobile skim requires structure; prose-in-a-box reads as a robot summary.

**Default 4-row pattern:**

```html
<table class="tldr-box">
<tbody>
<tr><td><strong>What it is</strong></td><td>[1-line definition with primary keyword]</td></tr>
<tr><td><strong>How to get there</strong></td><td>[1-line transit answer with affiliate link if natural]</td></tr>
<tr><td><strong>How long</strong></td><td>[1-line duration verdict]</td></tr>
<tr><td><strong>When to go</strong></td><td>[1-line season verdict]</td></tr>
</tbody>
</table>
```

**Optional 5th row — "Where to stay" (use when post has hotel cards):**

The 5th row provides 3 stay options inline with affiliate links, formatted on separate physical lines (NO `<br />` tags — WordPress's wpautop handles line breaks).

```html
<tr><td><strong>Where to stay</strong></td><td>
<strong>Couples:</strong> <a href="[booking-aid-918822-url]" target="_blank" rel="nofollow noopener">[Hotel Name]</a>

<strong>Families:</strong> <a href="[booking-aid-918822-url]" target="_blank" rel="nofollow noopener">[Hotel Name]</a>

<strong>Budget:</strong> <a href="[booking-aid-918822-url]" target="_blank" rel="nofollow noopener">[Hotel Name]</a>
</td></tr>
```

Reference implementation: see `09_Pass4_Nico_Final.md` (Favignana, Apr 28, 2026).

---

## Hotel Card Template (Canonical HTML — Apr 28)

```html
<div class="hotel-card">
<a href="https://www.booking.com/hotel/it/[slug].en.html?aid=918822&no_rooms=1&group_adults=2" target="_blank" rel="nofollow noopener"><img src="https://wearepalermo.com/wp-content/uploads/[year]/[month]/[hotel-image-slug].jpg" alt="[Hotel Name]" class="alignnone size-large" /></a>

<h3>[Hotel Name] — ([Type Label])[ ★★★/★★★★ if Giata-classified]</h3>

<p><strong>[Tagline]</strong></p>

<p>[Description, 30-60 words]</p>

<p><a href="https://www.booking.com/hotel/it/[slug].en.html?aid=918822&no_rooms=1&group_adults=2" target="_blank" rel="nofollow noopener" class="check-it-out-button">Check it out →</a></p>

</div>
```

**Critical attributes (every hotel card):**
- Booking URL with `aid=918822` query param (preserved through both image link and CTA button)
- `target="_blank"` on every `<a>` (opens new tab)
- `rel="nofollow noopener"` on every affiliate `<a>` (SEO + security)
- Image inside the link (clickable image as well as button)
- Star rating ONLY if hotel is Giata-classified per WAP_06b (no stars on apartments, B&Bs, R.T.A. residences)
- Type label in parens after hotel name: (Apartments) / (B&B) / (Resort) / (Residence (R.T.A.)) — match hotel's own self-classification

**Image URL inference is BANNED.** If you don't have the verified image URL, use `[NICO: paste image URL]` placeholder and let Nico fill in Pass 4. Inferring from naming conventions produces broken images (real examples Apr 28: `b-amp-b-il-tufo.jpg` was actually `il-tufo.jpg`; `i-pretti-favignana.jpg` was actually `i-pretty.jpg` — typo preserved across years).

Reference implementation: see `09_Pass4_Nico_Final.md` (6-hotel section).

---

## Continue Planning Block (End of Post)

Gray box with 3 internal links. Template:

```html
<div style="background-color: #f4f4f4; padding: 20px; border-radius: 8px; margin-top: 20px;">
<h3 style="margin-top: 0; text-align: center;">Continue Your Palermo Planning</h3>
<ul style="list-style-type: none; padding-left: 0; text-align: center;">
     <li style="margin-bottom: 10px;"><strong>[RELATED POST NAME]:</strong> <a href="[URL]" target="_blank" rel="noopener noreferrer">[CALL TO ACTION TEXT]</a></li>
     <li style="margin-bottom: 10px;"><strong>Premium Guide:</strong> <a href="https://wearepalermo.podia.com/the-sicilian-way" target="_blank" rel="noopener noreferrer">Get the We Are Palermo Premium Guide</a></li>
     <li style="margin-bottom: 10px;"><strong>Watch the Chaos:</strong> <a href="https://www.youtube.com/@WeArePalermo" target="_blank" rel="noopener noreferrer">Check our YouTube Channel</a></li>
</ul>
</div>
```

Always include: one related WAP blog post, We Are Palermo Premium Guide link, YouTube channel link.

---

## Images

### Requirements

- **One image every 300-400 words** of body text (excluding text boxes).
- **Original photos** taken by Nico wherever possible. Stock images only as last resort.
- **Dimensions:** 800x530 pixels for body images. 1024x572 for infographics or wide visuals.
- **Alt text:** descriptive, natural language, includes keyword only when it fits. Not "palermo-car-rental-best-guide-2026."
- **File names:** lowercase, dashes, descriptive. "nico-barcellona-fiat-500.jpg" not "IMG_4829.JPG."
- **Compression:** use a plugin (Smush, ShortPixel, or similar) to keep file sizes under 200KB where possible.

### YouTube Embeds

Embed Nico's YouTube videos when the topic genuinely overlaps. Not for the sake of it. Direct paste of the YouTube URL on its own line in WordPress triggers automatic embed.

Purpose: entity consistency across platforms (Task 1.8 Rule 4.6). Same Nico, same voice, same face.

---

## Pre-Publish Checklist

Before hitting publish on any new or updated post, verify every item.

### Structure
- [ ] Italic lead (TL;DR) present, under 25 words, includes primary keyword
- [ ] Main image present, 800x530 min, descriptive alt text
- [ ] Nico self-introduction ("Ciao, it's Nico") in first paragraphs
- [ ] Benefit promise paragraphs present
- [ ] TL;DR callout as `<table>` with rows (not `<p>` in a colored div)
- [ ] Affiliate disclosure (italic, Nico voice) AFTER TL;DR, BEFORE H2 1
- [ ] NO bottom affiliate disclosure (removed Apr 28 — top-only is canonical)
- [ ] Main answer complete in first 540 words
- [ ] FAQ section at bottom, 4-6 questions
- [ ] Continue Planning block at end
- [ ] Signature ("Un grande abbraccio, *Nico Barcellona*" — Italian canonical, deprecated English version)

### Voice (Pulled From WAP_05 Self-Check)
- [ ] Opening does NOT sound like a travel-blog intro
- [ ] At least ONE Reader Interrogation (Variant A or B) in the post
- [ ] At least ONE first-person specific observation proving Nico was there
- [ ] ZERO em-dashes
- [ ] Paragraphs max 2 sentences or 45 words
- [ ] At least THREE of the 21 signature moves from WAP_05
- [ ] Correct voice mode used
- [ ] Ending is a verdict, not a pleasantry
- [ ] If swearing appears, it's elegant and specific
- [ ] No paragraph is boring

### Paid Content Rule
- [ ] NO specific restaurants, bars, or experience providers named by name

### SEO
- [ ] H1 contains primary keyword, max 60 characters
- [ ] Meta title 55-60 chars, Meta description 140-155 chars
- [ ] URL slug short, keyword-only
- [ ] Primary keyword in: H1, intro first 100 words, at least one H2, conclusion
- [ ] H2s and H3s phrased as natural-language questions
- [ ] 3-5 internal links to related WAP posts, 1-2 to hub pages
- [ ] External links only to reliable sources
- [ ] All images have descriptive alt text
- [ ] Visible publish date + "last updated" date

### Schema
- [ ] Article schema auto-generated by Yoast (verify in Yoast sidebar)
- [ ] FAQPage schema manually added as Custom HTML block below FAQ section
- [ ] Author schema added (one-time, on Nico's author page)

### Facts
- [ ] Every price, date, opening hour, name verified
- [ ] Any unverified claim flagged [VERIFY: X]

### Mobile
- [ ] Preview checked on mobile
- [ ] No paragraph runs longer than 4 lines on iPhone
- [ ] Text boxes render properly
- [ ] Images load, not broken

### Affiliate Links
- [ ] All affiliate links open in new tab (target="_blank" rel="noopener noreferrer")
- [ ] ONE disclosure present AFTER TL;DR, BEFORE H2 1 (in Nico voice)
- [ ] NO bottom disclosure (removed Apr 28)

### Categories and Tags
- [ ] Assigned to correct WordPress category
- [ ] Tags relevant, not keyword-stuffed (3-5 tags max)

---

## Audit Checklist for Existing Posts (Applies to SOP_01)

When SOP_01 updates an existing post, it must ALSO run this audit and fix any failures before republishing.

- [ ] All em-dashes purged, replaced with three-dot pauses, commas, or full stops
- [ ] At least one Reader Interrogation added if missing
- [ ] At least one first-person specific observation added if missing
- [ ] TL;DR / direct-answer block in first 540 words — add if missing
- [ ] Affiliate disclosure text box and italic line added if missing
- [ ] Wikipedia-voice paragraphs rewritten in Nico voice
- [ ] FAQPage schema added if missing
- [ ] "Last updated" date updated to republish date
- [ ] All facts re-verified (prices, hours, dates — things go stale fast)
- [ ] Internal links audited (broken links fixed, new relevant links added)
- [ ] Paragraph length checked against 2-sentence / 45-word rule
- [ ] No specific restaurant/bar/experience-provider names (paid content rule)

---

## What NOT to Do (Pulled From Task 1.8)

- Do NOT chase keyword density. Dead.
- Do NOT publish thin content under 800 words.
- Do NOT publish over 5,000 words. Split into two posts.
- Do NOT bury the answer past the first 540 words.
- Do NOT use generic travel-blog openers.
- Do NOT disguise affiliate links without clear disclosure.
- Do NOT add nosnippet/noindex thinking you're "protecting" content from AI Overviews. You only remove yourself from SERPs entirely.
- Do NOT let a post sit untouched for 18+ months without a refresh. Freshness is a ranking factor.
- Do NOT let low-quality blog comments accumulate. Moderate or disable.
- Do NOT copy this format blindly onto YouTube scripts or social posts — those have different rules (TBD in future docs).

---

---

## D15 — Pros/Cons/Advice Block Pattern (CANONICAL, LOCKED May 3, 2026)

For destination guides and where-to-stay posts. WordPress legacy `divTable` pattern. Verified against `/where-to-stay-palermo/` live HTML May 2.

Three blocks ALWAYS together: `TablePro` → `TableCons` → `TableAdvice`. Emoji codes: 1f601 (grinning), 1f641 (frowning), 1f44d (thumbs up). Per Finding #77.

---

## D16 — Continue Planning Block (CANONICAL, LOCKED May 3, 2026)

Every guide-tier post ends with grey-box Continue Planning block BEFORE signature. Always 3 items: next-logical-read + conditional-relevant link + Sicilian Way paid pitch. Per Finding #77.

---

## D14 amendment — Image placeholder format (LOCKED May 3, 2026)

Image placeholders are ALWAYS HTML comments: `<!-- NICO: paste body image #5 here -->`. NEVER bracketed text inside `<img src>` tags (renders as broken HTML in WordPress).

PLUS: before using ANY placeholder, search the live site for existing URLs. web_fetch the target article + any internally-linked WAP articles that contribute images. Only after live-search returns no hit: use HTML comment placeholder. Per Findings #82 and original Apr 28 Finding #41.

---

## Working Document Note

This doc evolves. When Nico identifies new format patterns that work, new publishing tricks, new tool integrations, or new SEO/AIO rules from future research, they get added here with a date stamp.

When Yoast gets replaced, when WordPress theme changes, when new schema requirements emerge — update this doc, commit, push.

Format is not fixed. It's a living system that serves the voice and the ranking strategy.
