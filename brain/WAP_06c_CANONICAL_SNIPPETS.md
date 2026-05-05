# WAP_06c — Canonical HTML Snippets

Last updated: May 5, 2026
Source: /where-to-stay-palermo/ live HTML (Nico hand-finished gold standard)

---

## Purpose

This is the canonical HTML pattern library. The agent uses these snippets verbatim during Fase 7 (HTML conversion). NEVER invent HTML patterns. NEVER modify CSS values without updating this doc first.

When the agent needs to render a TL;DR, callout, hotel card, etc. — it copies the snippet from here, fills the placeholders, done.

---

## 1. TL;DR Blue-Box (Article Opening)

**Purpose:** First decision-helper block. Sits after author intro, before affiliate disclosure.

**Position:** Always after author intro paragraph, before the affiliate disclosure.

**Critical CSS:** `background-color: #e3f2fd` (light blue). 5-row table. Title color `#0d47a1`. Border separators `#bbdefb`.

**HTML template:**

```html
<div style="background-color: #e3f2fd; padding: 20px; border-radius: 8px; margin-bottom: 25px;">
<p style="margin-top: 0; font-weight: bold; color: #0d47a1; font-size: 1.05em; margin-bottom: 15px;">[TLDR_TITLE]</p>
<table style="width: 100%; border-collapse: collapse; color: #333;">
<tbody>
<tr>
<td style="padding: 8px 12px 8px 0; vertical-align: top; width: 110px; font-weight: bold; color: #0d47a1; border-bottom: 1px solid #bbdefb;">[ROW_1_LABEL]</td>
<td style="padding: 8px 0; vertical-align: top; border-bottom: 1px solid #bbdefb;">[ROW_1_CONTENT]</td>
</tr>
<tr>
<td style="padding: 8px 12px 8px 0; vertical-align: top; font-weight: bold; color: #0d47a1; border-bottom: 1px solid #bbdefb;">[ROW_2_LABEL]</td>
<td style="padding: 8px 0; vertical-align: top; border-bottom: 1px solid #bbdefb;">[ROW_2_CONTENT]</td>
</tr>
<tr>
<td style="padding: 8px 12px 8px 0; vertical-align: top; font-weight: bold; color: #0d47a1; border-bottom: 1px solid #bbdefb;">[ROW_3_LABEL]</td>
<td style="padding: 8px 0; vertical-align: top; border-bottom: 1px solid #bbdefb;">[ROW_3_CONTENT]</td>
</tr>
<tr>
<td style="padding: 8px 12px 8px 0; vertical-align: top; font-weight: bold; color: #0d47a1; border-bottom: 1px solid #bbdefb;">[ROW_4_LABEL]</td>
<td style="padding: 8px 0; vertical-align: top; border-bottom: 1px solid #bbdefb;">[ROW_4_CONTENT]</td>
</tr>
<tr>
<td style="padding: 8px 12px 8px 0; vertical-align: top; font-weight: bold; color: #0d47a1;">[ROW_5_LABEL]</td>
<td style="padding: 8px 0; vertical-align: top;">[ROW_5_CONTENT]</td>
</tr>
</tbody>
</table>
</div>
```

**Live example (where-to-stay-palermo):**

```html
<div style="background-color: #e3f2fd; padding: 20px; border-radius: 8px; margin-bottom: 25px;"><p style="margin-top: 0; font-weight: bold; color: #0d47a1; font-size: 1.05em; margin-bottom: 15px;">In a hurry? Here's the whole thing in 90 seconds.</p><table style="width: 100%; border-collapse: collapse; color: #333;"><tbody><tr><td style="padding: 8px 12px 8px 0; vertical-align: top; width: 110px; font-weight: bold; color: #0d47a1; border-bottom: 1px solid #bbdefb;">What it is</td><td style="padding: 8px 0; vertical-align: top; border-bottom: 1px solid #bbdefb;">A Sicilian's pick of the only <strong>three areas</strong> worth sleeping in. Plus when Cefalù beats all three.</td></tr><tr><td style="padding: 8px 12px 8px 0; vertical-align: top; font-weight: bold; color: #0d47a1; border-bottom: 1px solid #bbdefb;">How long to stay</td><td style="padding: 8px 0; vertical-align: top; border-bottom: 1px solid #bbdefb;"><strong>Three nights minimum</strong>. Five is better. Less than three, you're seeing the inside of a taxi.</td></tr><tr><td style="padding: 8px 12px 8px 0; vertical-align: top; font-weight: bold; color: #0d47a1; border-bottom: 1px solid #bbdefb;">What you'll pay</td><td style="padding: 8px 0; vertical-align: top; border-bottom: 1px solid #bbdefb;"><strong>€80-300/night</strong> realistic. €600+ for proper luxury. €2,000 if you want Dua Lipa's wedding venue.</td></tr><tr><td style="padding: 8px 12px 8px 0; vertical-align: top; font-weight: bold; color: #0d47a1; border-bottom: 1px solid #bbdefb;">Best months</td><td style="padding: 8px 0; vertical-align: top; border-bottom: 1px solid #bbdefb;"><strong>April, May, June, September, October.</strong> Skip August. Skip Jan-March if Mondello.</td></tr><tr><td style="padding: 8px 12px 8px 0; vertical-align: top; font-weight: bold; color: #0d47a1;">Where to stay</td><td style="padding: 8px 0; vertical-align: top;"><strong>Walking everywhere?</strong> <a href="https://www.booking.com/hotel/it/exclusive-rooms-palazzo-natoli.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener">Centro Storico (Palazzo Natoli)</a>.<br> <strong>Safety + calm?</strong> <a href="https://www.booking.com/hotel/it/politeama-palace.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener">Politeama (Hotel Politeama)</a>.<br> <strong>Luxury holiday?</strong> <a href="https://www.booking.com/hotel/it/grandhotelvillaigieapalermo.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener">Acquasanta (Villa Igiea)</a>.</td></tr></tbody></table></div>
```

---

## 2. Affiliate Disclosure (Right After TL;DR)

**Purpose:** Single affiliate disclosure per article. Top-only position (locked Apr 28).

**Critical CSS:** `font-size: 0.85em`, `color: #555`, `background-color: #f5f5f5`, `padding: 12px 16px`, `border-radius: 6px`. Tone: casual, "might" not "are" (less definitive).

**HTML template:**

```html
<div style="background-color: #f5f5f5; padding: 12px 16px; border-radius: 6px; margin: 20px 0; font-size: 0.85em; color: #555;">[DISCLOSURE_TEXT]</div>
```

**Live example (where-to-stay-palermo):**

```html
<div style="background-color: #f5f5f5; padding: 12px 16px; border-radius: 6px; margin: 20px 0; font-size: 0.85em; color: #555;">Heads up. Some links here are affiliate. Same price for you. I get a small cut so I can keep doing this and not go work in a bank.</div>
```

---

## 3. Callout — 3 Variants

**Purpose:** Closing punctuation for each H2 section (except FAQ + Bottom Line).

**Variants by content type:**
- Local's Pick → recommendation (green `#e8f5e9`, cite color `#2e7d32`)
- Local's Take → opinion / personal aside (orange `#fff3e0`, cite color `#e65100`)
- Local's Warning → cautionary, scams, traps (red `#ffebee`, cite color `#d32f2f`)

**Critical CSS:** `display: flex` + `align-items: center`. Image `94x94px border-radius: 50%`. Padding `15px`, `border-radius: 8px`.

**Limits (Foundation Rule 1.5):**
- Each `<p>` ≤180 chars
- Total callout text ≤250 chars
- Max 4 `<p>` per callout

**Avatar images (canonical URLs):**
- Take (orange): `https://wearepalermo.com/wp-content/uploads/2025/09/nico-barcellona-portrait-scaled.jpg`
- Pick (green): `https://wearepalermo.com/wp-content/uploads/2025/10/Nico-top-pick.jpg`
- Warning (red): `https://wearepalermo.com/wp-content/uploads/2025/10/Nico-Barcellona-Alert.jpg`

### 3a. Local's Take (Orange)

```html
<div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img decoding="async" style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/09/nico-barcellona-portrait-scaled.jpg" alt="Nico Barcellona"></figure>
<div>
<p><cite style="font-style: normal; font-weight: bold; color: #e65100;">A Local's Take:</cite></p>
<p style="margin: 0; color: #333;">[CALLOUT_LINE_1]</p>
<p style="margin: 0; color: #333;">[CALLOUT_LINE_2]</p>
<p style="margin: 0; color: #333;">[CALLOUT_LINE_3]</p>
</div>
</div>
```

**Live example:**

```html
<div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;"><figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img decoding="async" style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/09/nico-barcellona-portrait-scaled.jpg" alt="Nico Barcellona"></figure><div><p><cite style="font-style: normal; font-weight: bold; color: #e65100;">A Local's Take:</cite></p><p style="margin: 0; color: #333;">Quick word for the women: the catcalling.</p><p style="margin: 0; color: #333;">Carriage drivers, taxi guys, neighborhood punks. They howl <em>"Ciao bella!"</em> out the window.</p><p style="margin: 0; color: #333;">They're not going to assault you. <em>Howling monkeys. That's the whole bit.</em></p></div></div>
```

### 3b. Local's Pick (Green)

```html
<div style="background-color: #e8f5e9; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img decoding="async" style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/10/Nico-top-pick.jpg" alt="Nico's Top Pick"></figure>
<div>
<p><cite style="font-style: normal; font-weight: bold; color: #2e7d32;">A Local's Pick:</cite></p>
<p style="margin: 0; color: #333;">[CALLOUT_LINE_1]</p>
<p style="margin: 0; color: #333;">[CALLOUT_LINE_2]</p>
<p style="margin: 0; color: #333;">[CALLOUT_LINE_3]</p>
</div>
</div>
```

**Live example:**

```html
<div style="background-color: #e8f5e9; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;"><figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img decoding="async" style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/10/Nico-top-pick.jpg" alt="Nico's Top Pick"></figure><div><p><cite style="font-style: normal; font-weight: bold; color: #2e7d32;">A Local's Pick:</cite></p><p style="margin: 0; color: #333;">Renting a car? <strong>Sleep outside the Z. T. L.</strong></p><p style="margin: 0; color: #333;">Politeama is the move. Park, walk in, walk back.</p><p style="margin: 0; color: #333;"><em>€160 fine avoided.</em></p></div></div>
```

### 3c. Local's Warning (Red)

```html
<div style="background-color: #ffebee; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img decoding="async" style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/10/Nico-Barcellona-Alert.jpg" alt="Nico Barcellona alert"></figure>
<div>
<p><cite style="font-style: normal; font-weight: bold; color: #d32f2f;">A Local's Warning:</cite></p>
<p style="margin: 0; color: #333;">[CALLOUT_LINE_1]</p>
<p style="margin: 0; color: #333;">[CALLOUT_LINE_2]</p>
<p style="margin: 0; color: #333;">[CALLOUT_LINE_3]</p>
</div>
</div>
```

**Live example:**

```html
<div style="background-color: #ffebee; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;"><figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img decoding="async" style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/10/Nico-Barcellona-Alert.jpg" alt="Nico Barcellona alert"></figure><div><p><cite style="font-style: normal; font-weight: bold; color: #d32f2f;">A Local's Warning:</cite></p><p style="margin: 0; color: #333;">Going for a swim? Don't leave your phone on the towel.</p><p style="margin: 0; color: #333;">Find the grandma or the grandpa with the round belly.</p><p style="margin: 0; color: #333;"><em>"Could you watch my stuff for a minute?"</em> Done.</p></div></div>
```

---

## 4. Hotel Card

**Purpose:** Each hotel recommendation in a "Where to stay in [Area]" section.

**Critical CSS:** `background: white`, `box-shadow: 0 1px 3px rgba(0,0,0,0.1)`, `border-radius: 12px`, `padding: 30px`. CTA button: `background: #1E2A39`, `color: white`, `padding: 12px 25px`, `border-radius: 6px`.

**Mandatory attributes per WAP_06 D3:**
- Booking URL with `aid=918822`
- `target="_blank"` on every `<a>`
- `rel="nofollow noopener"` on every affiliate `<a>`
- Image inside the link (clickable)
- Star rating ONLY if Giata-classified hotel (no stars on apartments / B&Bs / R.T.A.)
- Type label in parens after name

**HTML template:**

```html
<div style="background: white; border-radius: 12px; padding: 30px; margin-bottom: 25px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
<p style="margin-top: 0;"><strong>[NUMBER]. [HOTEL_NAME] – ([TYPE_LABEL])</strong> [STARS_IF_APPLICABLE]</p>
<p><strong>[NICO_ONE_LINER]</strong> | <a href="[BOOKING_URL]" target="_blank" rel="nofollow noopener"><strong>[LINK_TEXT]</strong></a></p>
<p><a href="[BOOKING_URL]" target="_blank" rel="nofollow noopener"><img decoding="async" class="alignnone size-large" src="[IMAGE_URL]" alt="[IMAGE_ALT]"></a></p>
<p>[DESCRIPTION]</p>
<p><strong><a style="display: inline-block; background: #1E2A39; color: white; padding: 12px 25px; text-decoration: none; border-radius: 6px;" href="[BOOKING_URL]" target="_blank" rel="nofollow noopener">Check it out →</a></strong></p>
</div>
```

**Live example (Palazzo Natoli):**

```html
<div style="background: white; border-radius: 12px; padding: 30px; margin-bottom: 25px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);"><p style="margin-top: 0;"><strong>1. Palazzo Natoli Boutique Hotel – (Boutique Hotel)</strong> ★★★★</p><p><strong>The one I send couples to</strong> | <a href="https://www.booking.com/hotel/it/exclusive-rooms-palazzo-natoli.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener"><strong>Quiet alley, real service</strong></a></p><p><a href="https://www.booking.com/hotel/it/exclusive-rooms-palazzo-natoli.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener"><img decoding="async" class="alignnone size-large" src="https://wearepalermo.com/wp-content/uploads/2024/11/natoli-1024x682.jpg" alt="Palazzo Natoli Boutique Hotel in Palermo Centro Storico"></a></p><p>Off Corso Vittorio Emanuele, tucked into a quiet alley. Modern design, real service, walls thick enough to actually sleep behind.</p><p><strong><a style="display: inline-block; background: #1E2A39; color: white; padding: 12px 25px; text-decoration: none; border-radius: 6px;" href="https://www.booking.com/hotel/it/exclusive-rooms-palazzo-natoli.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener">Check it out →</a></strong></p></div>
```

---

## 5. Pros/Cons/Advice Block

**Purpose:** Area introduction sections (Centro Storico, Politeama, Mondello). Three stacked divTable containers.

**Critical CSS:** Class-based layout using `divTable`, `divTableBody`, `divTableRow`, `divTableCell`. Headers use emoji SVGs. Three variants: `TablePro` (pros), `TableCons` (cons), `TableAdvice` (ideal for).

**Emoji SVG URLs:**
- Pros: `https://s.w.org/images/core/emoji/14.0.0/svg/1f601.svg` (grinning face)
- Cons: `https://s.w.org/images/core/emoji/14.0.0/svg/1f641.svg` (slightly frowning)
- Advice: `https://s.w.org/images/core/emoji/14.0.0/svg/1f44d.svg` (thumbs up)

**HTML template (full set of 3):**

```html
<div class="divTable TablePro"><div class="divTableBody"><div class="divTableRow"><div class="divTableCell"><strong><img decoding="async" class="emoji" role="img" draggable="false" src="https://s.w.org/images/core/emoji/14.0.0/svg/1f601.svg" alt=""> PROS</strong></div></div><div class="divTableRow"><div class="divTableCell"><ul>
<li>[PRO_1]</li>
<li>[PRO_2]</li>
<li>[PRO_3]</li>
<li>[PRO_4]</li>
</ul></div></div></div></div>

<div class="divTable TableCons"><div class="divTableBody"><div class="divTableRow"><div class="divTableCell"><strong><img decoding="async" class="emoji" role="img" draggable="false" src="https://s.w.org/images/core/emoji/14.0.0/svg/1f641.svg" alt=""> CONS</strong></div></div><div class="divTableRow"><div class="divTableCell"><ul>
<li>[CON_1]</li>
<li>[CON_2]</li>
<li>[CON_3]</li>
<li>[CON_4]</li>
</ul></div></div></div></div>

<div class="divTable TableAdvice"><div class="divTableBody"><div class="divTableRow"><div class="divTableCell"><strong><img decoding="async" class="emoji" role="img" draggable="false" src="https://s.w.org/images/core/emoji/14.0.0/svg/1f44d.svg" alt=""> AREA IS IDEAL FOR</strong></div></div><div class="divTableRow"><div class="divTableCell"><ul>
<li>[IDEAL_1]</li>
<li>[IDEAL_2]</li>
<li>[IDEAL_3]</li>
<li>[IDEAL_4]</li>
</ul></div></div></div></div>
```

**Live example (Centro Storico):**

```html
<div class="divTable TablePro"><div class="divTableBody"><div class="divTableRow"><div class="divTableCell"><strong><img decoding="async" class="emoji" role="img" draggable="false" src="https://s.w.org/images/core/emoji/14.0.0/svg/1f601.svg" alt=""> PROS</strong></div></div><div class="divTableRow"><div class="divTableCell"><ul><li>You walk to everything. Quattro Canti, the Cathedral, Teatro Massimo, the markets.</li><li>The food. <strong>Either you wear a muzzle, or you pack on two pounds a day.</strong></li><li>The chaos <em>is</em> the experience.</li><li>Cheapest of the three areas for what you get.</li></ul></div></div></div></div>

<div class="divTable TableCons"><div class="divTableBody"><div class="divTableRow"><div class="divTableCell"><strong><img decoding="async" class="emoji" role="img" draggable="false" src="https://s.w.org/images/core/emoji/14.0.0/svg/1f641.svg" alt=""> CONS</strong></div></div><div class="divTableRow"><div class="divTableCell"><ul><li>It's loud. Not <em>city loud.</em> More <em>Italian wedding next door at 2 AM</em> loud.</li><li>Drift from the main streets and the edges get rougher. Albergheria and behind Vucciria can feel sketchy at night.</li><li><strong>You walk a hundred meters and go from paradise to a complete shithole.</strong> That's Palermo.</li><li>Real grocery stores: scarce. <strong>Salita Partanna</strong> off Via Maqueda is one of the few that stays open late.</li></ul></div></div></div></div>

<div class="divTable TableAdvice"><div class="divTableBody"><div class="divTableRow"><div class="divTableCell"><strong><img decoding="async" class="emoji" role="img" draggable="false" src="https://s.w.org/images/core/emoji/14.0.0/svg/1f44d.svg" alt=""> AREA IS IDEAL FOR</strong></div></div><div class="divTableRow"><div class="divTableCell"><ul><li>First-timers who want raw, real Palermo</li><li>Sightseers and history lovers</li><li>Nightlife people</li><li>Couples who like chaos with their charm</li></ul></div></div></div></div>
```

---

## 6. FAQ Section (details/summary)

**Purpose:** End-of-article FAQ. 4-8 questions per article. Each answer 15-150 words.

**Critical CSS:** Wrapper class `faq-brutto-ma-funziona`. Native HTML `<details>/<summary>` (no JS, no plugin).

**Companion required:** FAQPage JSON-LD schema in `<script type="application/ld+json">`. Without schema, no Google rich results.

### 6a. HTML template:

```html
<div class="faq-brutto-ma-funziona">

<details>
<summary><strong>[QUESTION_1]</strong></summary>
<p>[ANSWER_1_PARAGRAPH_1]</p>
<p>[ANSWER_1_PARAGRAPH_2]</p>
</details>

<details>
<summary><strong>[QUESTION_2]</strong></summary>
<p>[ANSWER_2_PARAGRAPH_1]</p>
<p>[ANSWER_2_PARAGRAPH_2]</p>
</details>

</div>
```

**Live example (first 2 questions):**

```html
<div class="faq-brutto-ma-funziona"> <details> <summary><strong>Should I stay in Kalsa, Vucciria, Capo, or Albergheria specifically?</strong></summary><p>These are sub-neighborhoods inside Centro Storico. To us, it's all <em>Centro Storico.</em> Pick a hotel anywhere inside Centro Storico, you're fine.</p><p>Just <strong>avoid sleeping inside Capo or Ballarò markets.</strong> That's the 7 AM fish-truck alarm clock.</p><p>Vucciria is loud at night (it's the main nightlife area now). Kalsa is fine. Albergheria can feel sketchy after dark.</p> </details> <details> <summary><strong>Is Palermo safe?</strong></summary><p>Safer than your American friend who watched <em>The Godfather</em> thinks.</p><p>Per Il Sole 24 Ore's 2025 crime index (2024 data), Palermo records <strong>3,936 reported crimes per 100,000 inhabitants.</strong> That's <strong>below Milan, Rome, Florence, AND Naples.</strong></p><p>Pickpockets exist in markets and on Via Maqueda. Violent crime against tourists is rare.</p><p>Solo women: stick to Politeama if it's your first time in Italy. See <a href="https://wearepalermo.com/news/palermo-safe-place-visit/">my detailed safety guide</a>.</p> </details> </div>
```

### 6b. FAQPage JSON-LD schema template:

```html
<script type="application/ld+json"> {
 "@context": "https://schema.org",
 "@type": "FAQPage",
 "mainEntity": [
 {
 "@type": "Question",
 "name": "[QUESTION_1_TEXT]",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "[ANSWER_1_PLAIN_TEXT_NO_HTML]"
 }
 },
 {
 "@type": "Question",
 "name": "[QUESTION_2_TEXT]",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "[ANSWER_2_PLAIN_TEXT_NO_HTML]"
 }
 }
 ]
} </script>
```

**Live example (full 8 questions from where-to-stay-palermo):**

```html
<script type="application/ld+json"> {
 "@context": "https://schema.org",
 "@type": "FAQPage",
 "mainEntity": [
 {
 "@type": "Question",
 "name": "Should I stay in Kalsa, Vucciria, Capo, or Albergheria specifically?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "These are sub-neighborhoods inside Centro Storico. To us, it's all Centro Storico. Pick a hotel anywhere inside Centro Storico, you're fine. Just avoid sleeping inside Capo or Ballaro markets. That's the 7 AM fish-truck alarm clock. Vucciria is loud at night (it's the main nightlife area now). Kalsa is fine. Albergheria can feel sketchy after dark."
 }
 },
 {
 "@type": "Question",
 "name": "Is Palermo safe?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "Safer than your American friend who watched The Godfather thinks. Per Il Sole 24 Ore's 2025 crime index (2024 data), Palermo records 3,936 reported crimes per 100,000 inhabitants. That's below Milan, Rome, Florence, AND Naples. Pickpockets exist in markets and on Via Maqueda. Violent crime against tourists is rare. Solo women: stick to Politeama if it's your first time in Italy."
 }
 },
 {
 "@type": "Question",
 "name": "Is the tap water in Palermo drinkable?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "Technically yes, the city water is treated and safe. In practice, locals drink bottled. Slight chlorine taste in some buildings. Staying more than two nights? Buy a 6-pack of 1.5L bottles at any supermarket for under 5 euros."
 }
 },
 {
 "@type": "Question",
 "name": "What's the closest beach to the center of Palermo?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "Mondello at 11 km north. Bus 806 from Politeama, 30 to 40 minutes. Foro Italico at the edge of the historic center has small public access but isn't a swimming beach. Locals don't swim there. Beach is the goal? Base in Mondello. Or stay in Politeama and day-trip."
 }
 },
 {
 "@type": "Question",
 "name": "Do I need a rental car in Palermo?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "For Palermo itself, no. The historic center is walkable, the Z. T. L. means you can't drive in anyway, parking is a nightmare. For Sicily beyond Palermo, yes. If you rent a car for the Sicily portion, stay outside the Z. T. L.: Politeama, NOT Centro Storico. Otherwise that 160 euro fine is waiting on day one."
 }
 },
 {
 "@type": "Question",
 "name": "How do I get from the airport to my hotel?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "Falcone-Borsellino airport is 30 to 40 minutes from the historic center. Options: shuttle bus (Prestia e Comande, around 7 euros), train (around 6 euros, slower), taxi (around 45 euros fixed), or a private transfer."
 }
 },
 {
 "@type": "Question",
 "name": "Is Mondello worth booking in winter?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "No. Town goes dead. Buzz is gone. You'll feel it. Atmospheric for a 2-hour walk. Not a base for sleeping. Winter trip? Stay in Politeama or Centro Storico."
 }
 },
 {
 "@type": "Question",
 "name": "How early should I book my Palermo accommodation?",
 "acceptedAnswer": {
 "@type": "Answer",
 "text": "Peak summer (June through August): 3 to 4 months ahead for the good Booking.com listings. October-November has La Via dei Tesori running on weekends, which packs the city. Book 2 to 3 months ahead. Christmas and New Year: 2 months. Winter (November through February except Christmas) has the best supply and lowest prices. 2 to 4 weeks is fine."
 }
 }
 ]
} </script>
```

---

## 7. Continue Planning Grey-Box (Pre-Signature)

**Purpose:** End-of-article navigation block. 3 internal links (next read + dedicated guide + premium product).

**Position:** After Bottom Line section, before signature.

**Critical CSS:** `background-color: #f4f4f4`, `padding: 20px`, `border-radius: 8px`, `margin-top: 30px`. Centered alignment. UL with `list-style-type: none`.

**HTML template:**

```html
<div style="background-color: #f4f4f4; padding: 20px; border-radius: 8px; margin-top: 30px;">
<h3 style="margin-top: 0; text-align: center;"><span id="[SPAN_ID]">[SECTION_TITLE]</span></h3>
<ul style="list-style-type: none; padding-left: 0; text-align: center;">
<li style="margin-bottom: 10px;"><strong>Next read:</strong> <a href="[NEXT_READ_URL]" rel="noopener">[NEXT_READ_TITLE]</a>. [NEXT_READ_DESCRIPTION]</li>
<li style="margin-bottom: 10px;"><strong>[DEDICATED_GUIDE_LABEL]:</strong> <a href="[GUIDE_URL]" rel="noopener">[GUIDE_TITLE]</a>. [GUIDE_DESCRIPTION]</li>
<li style="margin-bottom: 10px;"><strong>The deeper insider stuff:</strong> <a href="[PREMIUM_URL]" target="_blank" rel="noopener noreferrer">[PREMIUM_TITLE]</a>. [PREMIUM_DESCRIPTION]</li>
</ul>
</div>
```

**Live example (where-to-stay-palermo):**

```html
<div style="background-color: #f4f4f4; padding: 20px; border-radius: 8px; margin-top: 30px;"><h3 style="margin-top: 0; text-align: center;"><span id="Continue_Planning_Your_Palermo_Trip">Continue Planning Your Palermo Trip</span></h3><ul style="list-style-type: none; padding-left: 0; text-align: center;"><li style="margin-bottom: 10px;"><strong>Next read:</strong> <a href="https://wearepalermo.com/news/airport-transfers/" rel="noopener">Palermo Airport Transfers</a>. How to actually get from PMO to your hotel without getting fleeced.</li><li style="margin-bottom: 10px;"><strong>If Cefalù sounds right:</strong> <a href="https://wearepalermo.com/news/where-to-stay-cefalu/" rel="noopener">Where to Stay in Cefalù</a>. The dedicated guide with deeper picks.</li><li style="margin-bottom: 10px;"><strong>The deeper insider stuff:</strong> <a href="https://wearepalermo.podia.com/the-sicilian-way" target="_blank" rel="noopener noreferrer">The Sicilian Way</a>. My paid guide with 50+ curated restaurants and the scams I won't put in a public post.</li></ul></div>
```

---

## Usage Rules

1. **NEVER invent HTML patterns.** Only use snippets from this doc.
2. **NEVER modify CSS values** in a snippet without first updating this doc and noting the change in WAP_06.
3. **ALWAYS preserve** `target="_blank"`, `rel="nofollow noopener"` on affiliate links.
4. **ALWAYS include** the Booking `aid=918822` query param.
5. If a new pattern is needed (e.g., comparison table, image gallery), draft it once, get Nico approval, then add to this doc as snippet 8/9/etc.

---

## Source Article

Gold-standard source: https://wearepalermo.com/where-to-stay-palermo/
Local fixture: tools/test_articles/where-to-stay-palermo.html
Last validated: May 5, 2026 (audit_post.sh v0.8 → 32 PASS / 2 FAIL legitimate)
