# 08 — Pass 3 HTML (Architect Final, v3.2)

**STATUS:** ⚠️ SUPERSEDED by 09_Pass4_Nico_Final.md (Nico's manual edits on top of this).
**This file is the Architect's final Pass 3 output, preserved for audit trail.**
**For the actually-published version:** see 09_Pass4_Nico_Final.md.
**For the reconciliation summary (v3.2 vs Pass 4 deltas + brain doc updates):** see 10_PM_Handoff_Pass3_Pass4_Reconciliation.md.

---

**SOP:** SOP_01 v2.0, Step 9 (Pass 3 — Format & HTML)
**Author:** Architect agent
**Date:** April 28, 2026
**Pass:** 3 of 3 (mechanical format application; voice and structure locked upstream)
**Source:** 07_Pass2_Voice.md (v3, locked Apr 28)
**Canonical references at time of writing:** Palermo Tourist Information article (for callout + FAQ patterns); Nico's old Favignana HTML (for 6 hotel image URLs)

## Final state of v3.2

This was the deliverable that went to Nico for review on April 28, 2026 evening. It contains:
- All 4 v3 fixes (Local's Take photo, callout blank-line wpautop fix, FAQ details/summary format, all old-folder image URLs converted to `[NICO: paste URL]` placeholders)
- v3.1 fix (6 hotel image URLs filled from Nico's old HTML reference)
- v3.2 fix (TL;DR table extended with "Where to stay" row containing 3 affiliate-tagged hotel options)

13 image placeholders remained for Nico to fill manually (Pass 4).

**v3 fixes applied (4):**
1. Local's Take photo URL reverted to `nico-barcellona-portrait-scaled.jpg` (canonical from Tourist Info article). v2 used `Nico-Take.png` from the OLD Favignana live HTML, which is the outdated post being replaced. All 8 Local's Take callouts now match Tourist Info canonical.
2. Callout HTML structure fixed: blank lines added inside the inner `<div>` (before `<cite>`, after last `<p>`) on all 13 callouts (8 Take + 3 Warning + 2 Pick). Without these blank lines, WordPress's wpautop filter eats the closing `</div>` and text leaks below the box. Confirmed pattern from Tourist Info article.
3. FAQ section rebuilt from `<h3>` + paragraphs to `<details>/<summary>` format inside `<div class="faq-brutto-ma-funziona">`. H2 changed to "❓ Frequently Asked Questions (The Stuff You're Still Worried About)" matching Tourist Info pattern.
4. ALL old-folder image URLs (7 from `/uploads/2022/06/` and `/uploads/2018/03/`) converted to `[NICO: paste URL]` placeholders. The boat tour image was confirmed broken; the rest from the same folders cannot be verified without site access. Conservative move: every image whose URL came from the stale snapshot is now a placeholder.

**v2 fixes carried through (still valid):**
1. Every paragraph >45 words split at sentence boundaries (mechanical, no voice rewrite)
2. Bold added to skim-keywords throughout intro + TL;DR + body (2-5 word phrases)
3. TL;DR restructured from prose-in-a-box to 4-row What/Where/When/How table
4. Bottom affiliate disclosure removed (top one stays)
5. "PDF" → "guide" in Continue Planning Sicilian Way line
6. New images Nico uploaded to `/uploads/2026/04/` and `/uploads/2025/10|09/` kept in place (those are Nico-uploaded and verifiable by alt-text correlation)

---

## Suggested Meta (carried through from Pass 2)

- **H1:** What You Should Know About Favignana: A Sicilian's Guide *(56 chars)*
- **Meta title:** What You Should Know About Favignana (Local's Guide) *(53 chars)*
- **Meta description:** Favignana from a Sicilian who's been going since childhood. What to do, where to stay, how to get there, what to skip. Real talk, no tourist BS. *(145 chars)*
- **URL slug:** `what-you-should-know-about-favignana` *(keep)*

---

# PUBLISH-READY HTML BODY

> Paste everything below the next divider into the WordPress block editor (Code Editor mode), replacing the current post body. Yoast handles Article schema; FAQPage schema is included as inline JSON-LD at the bottom. Featured image is set in Yoast/post settings, not in body. **6 image placeholders to fill in: marked `[NICO: paste image URL, alt text suggestion]`.**

---

<em>Favignana from a Palermitan who's been going every summer since he was a kid. What to do, what to skip, what it really costs.</em>

[NICO: paste lead/featured image URL, alt text suggestion: "Cala Rossa beach in Favignana, one of the Egadi Islands in Sicily" -- and add the caption "The shore in Cala Rossa, one of the beautiful bays in Favignana, one of the Egadi Islands in Sicily" if you want]

Ciao, your friend <strong>Nico Barcellona</strong> here.

Born in <strong>Palermo</strong>, going to Favignana every summer since I was teething. My grandmother was already swimming there back in <strong>1962</strong>.

So when I tell you about this island, I'm not guessing. I'm reporting from a <strong>family tradition</strong> older than your country's interstate system.

The internet has decided Favignana is a <strong>"hidden gem."</strong> Cute.

Hidden from <em>who</em>? My cousin's neighbor's dog could find this place in his sleep.

The 8 AM hydrofoil in July is packed shoulder-to-shoulder with Italians who've been coming since the eighties. The <strong>"secret"</strong> is only news to tourists.

So instead of pretending it's still some discovery, I'm going to tell you what it actually is. When to go. What to skip. And <strong>where the locals get scammed</strong>. Yes, even me.

Here's what's in this article:

<ul>
<li>Whether Favignana is <strong>worth your trip</strong></li>
<li>What to <strong>do, eat, and skip</strong></li>
<li>Where to <strong>stay near Piazza Madrice</strong></li>
<li>How to <strong>get there</strong></li>
<li>Favignana <strong>vs the other Sicilian islands</strong></li>
</ul>

<div style="background-color: #f5f5f5; padding: 12px 16px; border-radius: 6px; margin: 20px 0; font-size: 0.85em; color: #555;">
Heads up, some links here are affiliate. Price stays the same for you. I get a small cut so I can keep the lights on and avoid begging my cousin for a real job.
</div>

<div style="background-color: #e3f2fd; padding: 20px; border-radius: 8px; margin-bottom: 25px;">
<p style="margin-top: 0; font-weight: bold; color: #0d47a1; font-size: 1.05em; margin-bottom: 15px;">In a hurry? Here's the whole island in 90 seconds.</p>
<table style="width: 100%; border-collapse: collapse; color: #333;">
<tbody>
<tr>
<td style="padding: 8px 12px 8px 0; vertical-align: top; width: 110px; font-weight: bold; color: #0d47a1; border-bottom: 1px solid #bbdefb;">What it is</td>
<td style="padding: 8px 0; vertical-align: top; border-bottom: 1px solid #bbdefb;">Biggest of the <strong>Egadi Islands</strong>, off Trapani, in western Sicily.</td>
</tr>
<tr>
<td style="padding: 8px 12px 8px 0; vertical-align: top; font-weight: bold; color: #0d47a1; border-bottom: 1px solid #bbdefb;">How to get there</td>
<td style="padding: 8px 0; vertical-align: top; border-bottom: 1px solid #bbdefb;">From Palermo: <strong>2-hour bus to Trapani</strong>, then <strong>30-minute hydrofoil</strong>.</td>
</tr>
<tr>
<td style="padding: 8px 12px 8px 0; vertical-align: top; font-weight: bold; color: #0d47a1; border-bottom: 1px solid #bbdefb;">How long</td>
<td style="padding: 8px 0; vertical-align: top; border-bottom: 1px solid #bbdefb;"><strong>2-3 nights</strong> near Piazza Madrice. Bike or scooter, never a car. One day on a small boat.</td>
</tr>
<tr>
<td style="padding: 8px 12px 8px 0; vertical-align: top; font-weight: bold; color: #0d47a1; border-bottom: 1px solid #bbdefb;">When to go</td>
<td style="padding: 8px 0; vertical-align: top; border-bottom: 1px solid #bbdefb;"><strong>Late May to early July</strong>, or <strong>September</strong>. Skip July and August unless you booked months ago.</td>
</tr>
<tr>
<td style="padding: 8px 12px 8px 0; vertical-align: top; font-weight: bold; color: #0d47a1;">Where to stay</td>
<td style="padding: 8px 0; vertical-align: top;"><strong>Couples:</strong> <a href="https://www.booking.com/hotel/it/i-pretti-resort.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener">I Pretti Resort</a> (harbor views).<br /><strong>Families:</strong> <a href="https://www.booking.com/hotel/it/egusa73-favignana.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener">Egusa73</a> (apartments, central).<br /><strong>Budget:</strong> <a href="https://www.booking.com/hotel/it/b-amp-b-il-tufo.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener">B&amp;B Il Tufo</a> (simple, central).</td>
</tr>
</tbody>
</table>
</div>

<h2>Is Favignana actually worth your time?</h2>

<img class="alignnone size-large" src="https://wearepalermo.com/wp-content/uploads/2026/04/Slow-Life-in-favignana.jpg" alt="Slow island life in Favignana, the Sicilian way" loading="lazy" />

Look, I'll level with you.

This is the <strong>closest real island getaway from Palermo</strong>. Two hours from my front door, I'm already in water clearer than my apartment.

But "worth it" depends entirely on who <em>you</em> are.

You picturing a <strong>Mykonos</strong> kind of trip? Beach party, glasses up, music thumping, you drink until you smash your nose on the first rock, DJ at 2 AM?

Stop reading. Book Mykonos. We're saving you the trip.

Still here? Then maybe you're the other kind. The kind who hears <em>"swim, eat, nap, swim again"</em> and feels something unclench in your shoulders.

Because that <em>is</em> Favignana.

Three nouns: <strong>sea, bikes, food</strong>. That's the whole sentence.

A typical day for me. <strong>Eight AM hydrofoil</strong> out of Trapani. <strong>Bike rented by nine</strong>. By ten, I'm in water so clear it makes my bathtub at home look filthy.

I bike between coves. Swim from one to the next. Feeling lazy? I swap the bike for a <strong>small dinghy</strong>. Same coves. Less sweat. Plus you skip the weekend mob.

That's the local move. <strong>Bike or boat</strong>. Both keep you out of the chaos.

Lunch is <strong>tuna so fresh</strong> the fish was making plans this morning. Six plastic chairs. A bill that makes me suspicious it's a typo.

Then nap. Then swim again. <strong>Aperitivo at six</strong>.

You sit down, you order one drink, you blink, it's nine PM and you're asking the guy next to you <em>"wait, what bottle are we on?"</em>

Repeat two, three days. <em>That's</em> Favignana.

Now. The catch.

<strong>Two rays of sun</strong> and Italians come booming over from Palermo and Trapani. Late spring it starts. By August? <em>Insane.</em>

Foreign tourists are still rare here. The Italians? Already a mess.

When the algorithm finds this place, it gets worse. Fast.

<strong>Go now.</strong>

<div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/09/nico-barcellona-portrait-scaled.jpg" alt="Nico Barcellona" /></figure>
<div>

<cite style="font-style: normal; font-weight: bold; color: #e65100;">A Local's Take:</cite>
<p style="margin: 0; color: #333;"><em>Real</em> Sicily, zero influencer brigade.</p>
<p style="margin: 0; color: #333;">For now.</p>

</div>
</div>

<h2>Best Things to Do in Favignana</h2>

[NICO: paste image URL for H2 2 intro , alt text suggestion: "Things to do in Favignana, the Egadi Islands' biggest island"]

This isn't Florence.

There's no headset tour. No megaphone-wielding guide explaining a fresco for forty minutes. No line outside a museum.

The whole charm is <strong>no schedule</strong>. You, the sea, and a cold beer at four PM.

Here's what's actually worth your time.

<h3>Rent a Boat and Circle the Island</h3>

[NICO: paste image URL for boat tour, alt text suggestion: "Boat tour around Favignana coast, Egadi Islands"]

If you do one thing on Favignana, this is it.

Renting a small dinghy is the difference between <em>visiting</em> this island and <em>seeing</em> it.

<strong>No license required.</strong> No Captain Jack Sparrow certification. Six people fit.

The coastline is a maze of coves, sea caves, and water you cannot reach from a beach towel no matter how stubbornly you walk.

<strong>Around €150 a day</strong>, fuel extra. Split four ways: cheaper than dinner.

July and August? Boats disappear faster than the last cannolo at a baptism. Book early or stay on land, jealous, watching everyone else have your day.

<strong>Sea Taxi Favignana</strong> is a solid shop. Friendly, fair, and they don't act like you're bothering them.

Don't want to drive? Captained boat with lunch from the Egadi specialists: <a href="https://gyg.me/uEnbDRCq" target="_blank" rel="nofollow noopener">Egadi Boat Tour with Lunch</a>.

<div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/09/nico-barcellona-portrait-scaled.jpg" alt="Nico Barcellona" /></figure>
<div>

<cite style="font-style: normal; font-weight: bold; color: #e65100;">A Local's Take:</cite>
<p style="margin: 0; color: #333;">If you've ever played <strong>Mario Kart</strong>, you can steer one of these things.</p>
<p style="margin: 0; color: #333;">Captained boats are only worth it if you hate driving or want lunch onboard.</p>

</div>
</div>

<div style="background-color: #ffebee; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/10/Nico-Barcellona-Alert.jpg" alt="Nico Barcellona alert" /></figure>
<div>

<cite style="font-style: normal; font-weight: bold; color: #d32f2f;">A Local's Warning:</cite>
<p style="margin: 0; color: #333;">When you return the dinghy, they "check" how much gas you used. Somehow they always find a couple extra liters you didn't burn.</p>
<p style="margin: 0; color: #333;">It's not because you're foreign. The Favignanese rental guys would <strong>scam their own father</strong>.</p>
<p style="margin: 0; color: #333;">Factor <strong>€10-15 of mystery gas</strong> into your day. The price of doing business here.</p>

</div>
</div>

<h3>Scuba Diving</h3>

<img class="alignnone size-large" src="https://wearepalermo.com/wp-content/uploads/2026/04/scuba-diving-in-favignana.jpg" alt="Scuba diving in Favignana's clear Mediterranean waters" loading="lazy" />

The underwater world here is not a joke.

We're talking <strong>sea caves, rock arches, vibrant marine life</strong>, and dives for every level. Not a sad reef with one fish and a plastic bag.

<strong>Beginners?</strong> Galeotta. Dreamfish, moray eels, and underwater boulders that look prehistoric.

<strong>Intermediate?</strong> Cala Rotonda. A cave dive with mood lighting, umbrine, and the occasional curious octopus making eye contact.

<strong>Advanced?</strong> Secca del Toro for currents and barracuda. Or Scoglio Corrente, the wild west of the chain.

Risky but unforgettable. Tuna, giant grouper, dolphins if the sea gods are feeling generous.

<strong>Egadi Scuba Diving</strong> is the operator. Solid gear, solid guides, solid reputation for not letting idiots drown. Book direct, not on GetYourGuide.

<h3>Try the Local Food</h3>

[NICO: paste red tuna image URL, alt text suggestion: "Red tuna, the signature dish of Favignana" -- and add the caption "Red tuna, Favignana's pride" if you want]

Eating on Favignana means eating like a <strong>Sicilian nonna</strong> is watching you. Because somewhere, she is.

The island is famous for <strong>red tuna</strong>. Grilled, raw, stewed, tartare, you name it.

Start with <strong>tartare</strong>. Then <strong>spaghetti ai ricci</strong> (sea urchins). Then <strong>couscous di pesce</strong> if it's on the menu.

Even if you don't know what it is. <em>Especially</em> if you don't know what it is.

Then there's <strong>pane cunzato</strong>. Bread, tomatoes, olive oil, anchovies, sometimes mozzarella. Hits like a religious experience.

You eat one whole, you order a second, you don't apologize.

The vegetables here? <strong>So fresh they should be illegal</strong> in places where it rains every day. Vegetarians won't suffer.

You don't need a Michelin restaurant. The local trattorie and beach shacks serve the food that matters.

<strong>July and August: book a few days ahead.</strong> Walk in unbooked on a weekend, you'll eat chips on a curb watching everyone else eat tuna.

A note on service.

Don't expect Milan. The Favignanese work three months a year. The other nine? They exist.

That waiter who isn't smiling? Not personal. <strong>Island pace.</strong> The food is worth it.

<h3>Visit Santa Caterina Castle</h3>

[NICO: paste Santa Caterina Castle image URL, alt text suggestion: "Santa Caterina Castle, the highest point on Favignana"]

Want to <em>earn</em> your sunset?

Hike up to <strong>Santa Caterina Castle</strong>, the highest point on the island. <strong>Forty-five minutes uphill</strong>. Uneven terrain. Zero shade.

The view at the top will <strong>blow your sandals off</strong>. All the Egadi Islands, Trapani, Marsala, and your past life decisions if the wind hits right.

The castle itself? Old, crumbling, abandoned. Don't expect Disney. <strong>WWII observation post</strong>. History buffs eat that up.

Bring water. Wear sneakers, not flip-flops. Skip the noon climb unless you enjoy boiling from the inside out. Cut the walk in half by riding a bike to the base.

<h3>Florio Tuna Factory Museum</h3>

[NICO: paste Florio Tuna Factory image URL, alt text suggestion: "Florio Tuna Factory in Favignana, former Mediterranean tuna processing center"]

I know. "Factory tour" doesn't scream vacation.

But this place was once the <strong>largest tuna processing plant</strong> in the Mediterranean. Industrial archaeology with a soul.

Inside? Ancient tools, mattanza history, walls of stories about the <a href="https://en.wikipedia.org/wiki/Florio_family" target="_blank" rel="noopener">Florio family</a>. The family that basically built the island.

The best part? Tours run by <strong>former factory workers</strong>. Real people. Real stories. No scripted nonsense.

They walk you through the rituals, the rise, the fall, and how overfishing ruined it all.

They're <strong>still pissed about it</strong>.

Tours run in Italian. English available on request, more reliable in peak season. Call ahead off-season.

Around <strong>€10 entry</strong>, about an hour. Book ahead in summer.

<div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/09/nico-barcellona-portrait-scaled.jpg" alt="Nico Barcellona" /></figure>
<div>

<cite style="font-style: normal; font-weight: bold; color: #e65100;">A Local's Take:</cite>
<p style="margin: 0; color: #333;"><em>Mattanza?</em> That's the old <strong>tuna slaughter</strong>. The Florio family ran it for centuries.</p>
<p style="margin: 0; color: #333;">Boats forming a ring around the school of tuna, nets closing in, sea turning red. Brutal? Yes. Sustainable? Until we overdid it.</p>
<p style="margin: 0; color: #333;">The factory in front of you was the kitchen.</p>

</div>
</div>

<h3>Tuff Cave Exploration</h3>

[NICO: paste tuff cave image URL, alt text suggestion: "Tuff cave in Favignana, carved limestone landscape"]

Off the tourist radar. Weird, wild, worth your time.

<strong>Tuff</strong> (not "tough") is a soft limestone the locals carved out by hand for centuries. Used to build homes, roads, churches. <strong>Half of Favignana</strong> is made of the stuff.

What's left now? A surreal landscape. Quarry-carved caves. Geometric walls. Abandoned pits the locals turned into gardens, art installations, and shady chill zones for goats.

The best ones are scattered around <strong>Cala Rossa</strong>, <strong>Bue Marino</strong>, <strong>Lido Burrone</strong>, and <strong>Punta Fanfalo</strong>.

No tours. No signs. Camera, sneakers (not flip-flops), early morning or late afternoon for the light.

<div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/09/nico-barcellona-portrait-scaled.jpg" alt="Nico Barcellona" /></figure>
<div>

<cite style="font-style: normal; font-weight: bold; color: #e65100;">A Local's Take:</cite>
<p style="margin: 0; color: #333;">Everyone hits the beaches. Almost nobody walks the tuff quarries.</p>
<p style="margin: 0; color: #333;">That's their loss. They're Favignana's <em>hidden masterpiece</em>.</p>
<p style="margin: 0; color: #333;">And they're <strong>free</strong>.</p>

</div>
</div>

<h2>Where to Stay in Favignana</h2>

<img class="alignnone size-large" src="https://wearepalermo.com/wp-content/uploads/2026/04/Piazza-Madrice-favignana.jpg" alt="Piazza Madrice, the main square in Favignana" loading="lazy" />

Stay near <strong>Piazza Madrice</strong>. The main square in town. Same answer, just louder.

Everything you need is here. Bars, restaurants, bike rentals, boat stands, the port for ferries to Levanzo and Marettimo. <strong>All within a 5-minute walk</strong> of the square.

Sleep too far out and you'll spend half your trip commuting like a local instead of vacationing.

Want quiet? Pick a place 10 minutes out. Not in the middle of nowhere with goats as your neighbors.

<h3>The price reality</h3>

Here's the part nobody warns you about.

Five years ago, this island was a deal. Today? You can stay in <strong>Manhattan for the same money</strong>.

With three to four months' notice for a peak-summer weekend, you won't find anything under <strong>€150 a night</strong> for grandma's house. New York hotel money. For a wobbly fan and a kitchenette.

In peak summer, the grandmas of Favignana are renting <strong>basically holes</strong>. Little dens. They charge for them like they're worth their weight in gold.

<strong>Book early or pay the late tax.</strong>

Six options below. Every budget.

<div style="background-color: #ffebee; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/10/Nico-Barcellona-Alert.jpg" alt="Nico Barcellona alert" /></figure>
<div>

<cite style="font-style: normal; font-weight: bold; color: #d32f2f;">A Local's Warning:</cite>
<p style="margin: 0; color: #333;">In peak season, prices go wild and availability drops. <strong>Book early</strong> or prepare to overpay AND under-sleep.</p>
<p style="margin: 0; color: #333;">Staying more than one night in summer? Only book a place with <strong>air conditioning</strong>.</p>
<p style="margin: 0; color: #333;">The Favignana heat in July and August does not negotiate.</p>

</div>
</div>

<div style="background: white; border-radius: 12px; padding: 30px; margin-bottom: 25px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
<p style="margin-top: 0;"><strong>1. Residence Scirocco e Tramontana – (Apartments)</strong></p>
Simple, central, well-located | <a href="https://www.booking.com/hotel/it/residence-scirocco-e-tramontana.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener"><strong>Mini apartments with kitchenettes</strong></a>

<a href="https://www.booking.com/hotel/it/residence-scirocco-e-tramontana.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener"><img class="alignnone size-large" src="https://wearepalermo.com/wp-content/uploads/2022/06/scirocco-e-tramontana-faviganana.jpg" alt="Residence Scirocco e Tramontana apartments in Favignana" loading="lazy" /></a>

Mini apartments with kitchenettes. Clean, well-located, ideal if you want to keep things simple.

<strong><a style="display: inline-block; background: #1E2A39; color: white; padding: 12px 25px; text-decoration: none; border-radius: 6px;" href="https://www.booking.com/hotel/it/residence-scirocco-e-tramontana.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener">Check it out →</a></strong>

</div>

<div style="background: white; border-radius: 12px; padding: 30px; margin-bottom: 25px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
<p style="margin-top: 0;"><strong>2. B&amp;B Il Tufo – (B&amp;B)</strong></p>
Central, friendly, no fuss | <a href="https://www.booking.com/hotel/it/b-amp-b-il-tufo.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener"><strong>A place to crash after swimming all day</strong></a>

<a href="https://www.booking.com/hotel/it/b-amp-b-il-tufo.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener"><img class="alignnone size-large" src="https://wearepalermo.com/wp-content/uploads/2022/06/il-tufo.jpg" alt="B&B Il Tufo in Favignana" loading="lazy" /></a>

Central and convenient. Clean rooms, friendly hosts, killer location. Nothing fancy. If you just want a place to crash after swimming all day, this is it.

<strong><a style="display: inline-block; background: #1E2A39; color: white; padding: 12px 25px; text-decoration: none; border-radius: 6px;" href="https://www.booking.com/hotel/it/b-amp-b-il-tufo.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener">Check it out →</a></strong>

</div>

<div style="background: white; border-radius: 12px; padding: 30px; margin-bottom: 25px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
<p style="margin-top: 0;"><strong>3. I Pretti – (Residence R.T.A.)</strong></p>
Harbor views, chilled upscale | <a href="https://www.booking.com/hotel/it/i-pretti-resort.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener"><strong>Stylish studios near Piazza Madrice</strong></a>

<a href="https://www.booking.com/hotel/it/i-pretti-resort.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener"><img class="alignnone size-large" src="https://wearepalermo.com/wp-content/uploads/2022/06/i-pretty.jpg" alt="I Pretti residence in Favignana" loading="lazy" /></a>

Harbor views, near Piazza Madrice and a short walk to the port. Stylish studios with outdoor space and a chilled, upscale vibe.

<strong><a style="display: inline-block; background: #1E2A39; color: white; padding: 12px 25px; text-decoration: none; border-radius: 6px;" href="https://www.booking.com/hotel/it/i-pretti-resort.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener">Check it out →</a></strong>

</div>

<div style="background: white; border-radius: 12px; padding: 30px; margin-bottom: 25px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
<p style="margin-top: 0;"><strong>4. Egusa73 Favignana – (Apartments)</strong></p>
Spacious and modern | <a href="https://www.booking.com/hotel/it/egusa73-favignana.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener"><strong>Perfect for families</strong></a>

<a href="https://www.booking.com/hotel/it/egusa73-favignana.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener"><img class="alignnone size-large" src="https://wearepalermo.com/wp-content/uploads/2022/06/egusa-73-favignana-egadi-1024x576.jpg" alt="Egusa73 apartments in Favignana" loading="lazy" /></a>

Big rooms, mix of regular rooms and apartments. Super central but peaceful. Kids and grandparents both happy here.

<strong><a style="display: inline-block; background: #1E2A39; color: white; padding: 12px 25px; text-decoration: none; border-radius: 6px;" href="https://www.booking.com/hotel/it/egusa73-favignana.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener">Check it out →</a></strong>

</div>

<div style="background: white; border-radius: 12px; padding: 30px; margin-bottom: 25px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
<p style="margin-top: 0;"><strong>5. Setteminne – (B&amp;B)</strong></p>
Calm, green, and chic | <a href="https://www.booking.com/hotel/it/setteminne-resort-design.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener"><strong>10-min walk to Piazza Madrice</strong></a>

<a href="https://www.booking.com/hotel/it/setteminne-resort-design.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener"><img class="alignnone size-large" src="https://wearepalermo.com/wp-content/uploads/2022/06/setteminne.jpg" alt="Setteminne B&B in Favignana" loading="lazy" /></a>

Modern rooms, sunny terraces, quiet surroundings. A solid pick if you want some peace while staying close to the action.

<strong><a style="display: inline-block; background: #1E2A39; color: white; padding: 12px 25px; text-decoration: none; border-radius: 6px;" href="https://www.booking.com/hotel/it/setteminne-resort-design.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener">Check it out →</a></strong>

</div>

<div style="background: white; border-radius: 12px; padding: 30px; margin-bottom: 25px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
<p style="margin-top: 0;"><strong>6. Stabilimento Lido Burrone – (B&amp;B)</strong></p>
Beach-lovers paradise | <a href="https://www.booking.com/hotel/it/stabilimento-lido-burrone.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener"><strong>5 mins from Calamoni Beach</strong></a>

<a href="https://www.booking.com/hotel/it/stabilimento-lido-burrone.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener"><img class="alignnone size-large" src="https://wearepalermo.com/wp-content/uploads/2022/06/stabilimento-lido-burrone.jpg" alt="Stabilimento Lido Burrone B&B near Calamoni beach in Favignana" loading="lazy" /></a>

Big bright rooms, modern feel. Five minutes from the beach. For beach bums who roll out of bed and into the sea.

<strong><a style="display: inline-block; background: #1E2A39; color: white; padding: 12px 25px; text-decoration: none; border-radius: 6px;" href="https://www.booking.com/hotel/it/stabilimento-lido-burrone.en.html?aid=918822&amp;no_rooms=1&amp;group_adults=2" target="_blank" rel="nofollow noopener">Check it out →</a></strong>

</div>

<div style="background-color: #e8f5e9; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/10/Nico-top-pick.jpg" alt="Nico's Top Pick" /></figure>
<div>

<cite style="font-style: normal; font-weight: bold; color: #2e7d32;">A Local's Pick:</cite>
<p style="margin: 0; color: #333;">Couple's weekend? <strong>I Pretti</strong> for the harbor views.</p>
<p style="margin: 0; color: #333;">Families? <strong>Egusa73</strong> for the apartment setup.</p>
<p style="margin: 0; color: #333;">Solo or budget? <strong>Il Tufo</strong>: simple, central, done.</p>

</div>
</div>

<h2>How long should you stay?</h2>

Depends what you came for.

You wanna take a selfie and peace out? <strong>One day</strong>. Fine.

You wanna feel the island, swim three coves, eat tuna twice, and slow down enough to forget what your job is?

<strong>You need more.</strong>

I get this question every week. <em>"Can I do Favignana in a day from Palermo?"</em>

Technically? Yes. But it's like going to a wine tasting and only smelling the cork.

The sweet spot is <strong>2 to 3 nights</strong>.

Enough time to rent a boat for a day, hit two or three beaches, eat yourself silly twice, and slow down enough to actually feel the place.

Anything less, you spend half the trip on ferries and buses, watching your vacation through the window like a kid in detention.

If a single day is genuinely all you have? <strong>Sleep in Trapani</strong> the night before. First hydrofoil out, last back. Only way it doesn't drive you insane.

But honestly? This island deserves better than a one-night stand.

<h2>Moving Around the Island</h2>

[NICO: paste bikes/getting around image URL, alt text suggestion: "Bikes parked in Favignana, the best way to get around the island"]

Favignana is small. <strong>Bike-it-in-a-day small</strong>. Two wheels is how you do this place.

Bikes are cheap, quiet, and the electric-assist versions make hills feel flat. <strong>You feel like a hero</strong>.

Scooters get you across the island faster, less sweat, less thigh burn. Pick your cardio level.

Rental shops are everywhere near Piazza Madrice. Walk three minutes, you'll trip over five of them.

No need to book ahead unless it's <strong>July or August</strong>. Then you'd better move. Scooters disappear.

<strong>€5-15/day for bikes. €25-60/day for scooters.</strong> Peaking in August because everything peaks in August.

Helmets and locks usually included.

A car? No. <strong>Streets too narrow.</strong> Parking sucks. You'll waste time, gas, and patience.

Favignana is not built for cars.

<div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/09/nico-barcellona-portrait-scaled.jpg" alt="Nico Barcellona" /></figure>
<div>

<cite style="font-style: normal; font-weight: bold; color: #e65100;">A Local's Take:</cite>
<p style="margin: 0; color: #333;">Renting a car on Favignana is like bringing a <strong>microwave to a picnic</strong>.</p>
<p style="margin: 0; color: #333;">Pointless. Grab a bike or scooter and enjoy the damn island the way it was meant to be seen.</p>

</div>
</div>

<h3>The sun</h3>

Pedaling under the Sicilian sun is no joke.

I'm Sicilian. I turn black on day one. My foreign friends, even loaded with sunscreen, turn red in <strong>48 hours</strong>.

I once brought a <strong>Nordic friend</strong> over. Pale, blonde, blue eyes. The full Scandinavian package.

Two days on a bike with full SPF 50? Full lobster. Red skin, blue eyes. <strong>Tiny patriotic crustacean.</strong>

<strong>Real sunscreen. Hat.</strong> Do not skip the back of your neck.

The Mediterranean sun is brutal in a way most Northern Europeans and Americans aren't ready for.

<div style="background-color: #ffebee; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/10/Nico-Barcellona-Alert.jpg" alt="Nico Barcellona alert" /></figure>
<div>

<cite style="font-style: normal; font-weight: bold; color: #d32f2f;">A Local's Warning:</cite>
<p style="margin: 0; color: #333;">Hours on this island are <strong>vibes-based</strong>. I once had to return a bike at 2 PM to make a 3 PM hydrofoil. Showed up. Closed. 1 to 4 for lunch.</p>
<p style="margin: 0; color: #333;">Bar next door called the guy. He came over in his lunch shirt, pissed. <em>My friend, you work three months a year and you still close two hours mid-afternoon?</em></p>
<p style="margin: 0; color: #333;">That's the island. Plan rentals to return <strong>BEFORE noon or AFTER 4</strong>.</p>

</div>
</div>

<h2>Favignana's Best Beaches</h2>

<img class="alignnone size-large" src="https://wearepalermo.com/wp-content/uploads/2026/04/cala-azzurra-faivgnana.jpg" alt="Cala Azzurra beach in Favignana, Sicily, with turquoise water" loading="lazy" />

This island is <strong>all about the sea</strong>.

If you're not spending half your day in the water, or staring at it like it's your soulmate, you're doing it wrong.

Heads up: most beaches here are <strong>rocky, not sandy</strong>. Bring water shoes or your feet will hate you by day two.

The water clarity, though? <em>Insane.</em> Like swimming inside a glass of Pellegrino.

<h3>By land</h3>

<ul>
<li><strong>Cala Rossa.</strong> Dramatic cliffs, stunning water, no sand. The Instagram favorite.</li>
<li><strong>Cala Azzurra.</strong> Easier access, dreamy turquoise. Quick dip, easy parking.</li>
<li><strong>Bue Marino.</strong> Wild, untouched, cinematic. Bring water shoes.</li>
<li><strong>Calamoni.</strong> Small coves, relaxed, less crowded.</li>
<li><strong>Lido Burrone.</strong> The only sandy beach. Family-friendly, sunbeds, kiosks.</li>
<li><strong>Cala Rotonda.</strong> Fewer people, more peace.</li>
</ul>

<h3>By boat only</h3>

<ul>
<li><strong>Faraglioni.</strong> Huge rocks, dramatic setting.</li>
<li><strong>Relitto allo Scoglio.</strong> Shipwreck nearby, spooky in the best way.</li>
<li><strong>Isolotto del Preveto.</strong> Crystal-clear, calm.</li>
<li><strong>Scoglio Corrente.</strong> Choppy water, worth it.</li>
<li><strong>Secca del Toro.</strong> Divers love it. Snorkelers too.</li>
</ul>

<div style="background-color: #e8f5e9; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/10/Nico-top-pick.jpg" alt="Nico's Top Pick" /></figure>
<div>

<cite style="font-style: normal; font-weight: bold; color: #2e7d32;">A Local's Pick:</cite>
<p style="margin: 0; color: #333;">If I had to pick one beach? <strong>Cala Rossa, by boat.</strong> Hands down.</p>
<p style="margin: 0; color: #333;">The view from the water is on a different planet from the view from the cliff.</p>

</div>
</div>

Want the boat-only beaches without renting your own dinghy? Captained options are in the next section.

<h2>Nightlife Reality Check</h2>

<img class="alignnone size-large" src="https://wearepalermo.com/wp-content/uploads/2026/04/camarillo-brillo-bar-in-favignana.jpg" alt="Camarillo Brillo bar in Favignana, evening aperitivo scene" loading="lazy" />

You looking for Ibiza? <strong>Wrong island.</strong>

The nightlife here is chill. <strong>Aperitivo by the sea</strong>. Slow dinners under the stars. That sweet moment when you're tipsy enough to think your Italian sounds native.

The center has wine bars, beach bars, and cafés with tables spilling onto Piazza Madrice.

No loud DJs. No drunk teens vomiting on sidewalks. No bouncer asking how you knew about it.

Some nights, live music in the square. Locals dancing. Tourists clapping off-beat. Kids running around at 11 PM like it's noon.

<strong>Normal here.</strong>

Private parties happen. You'd need to know someone who knows someone. That's how Sicily works. Nothing official, everything happens.

Dying to dance? Open-air bars just outside the center.

No bottle service. No velvet ropes. <strong>Flip-flops and mojitos.</strong>

<div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/09/nico-barcellona-portrait-scaled.jpg" alt="Nico Barcellona" /></figure>
<div>

<cite style="font-style: normal; font-weight: bold; color: #e65100;">A Local's Take:</cite>
<p style="margin: 0; color: #333;">Favignana's nightlife isn't about going hard. It's about <em>feeling good</em>.</p>
<p style="margin: 0; color: #333;">Beach bars, good wine, conversations that last hours.</p>
<p style="margin: 0; color: #333;">If you want techno at 3 AM, look elsewhere.</p>

</div>
</div>

<h2>Getting to Favignana</h2>

[NICO: paste hydrofoil/ferry image URL, alt text suggestion: "Boat trip from Trapani to Favignana, Egadi Islands"]

There's <strong>no airport</strong> on Favignana. You're coming by ferry.

Two launching points: <strong>Palermo or Trapani</strong>.

<h3>From Palermo</h3>

Easiest move? The <strong>Segesta Autolinee bus</strong> from Palermo center to Trapani port, then a hydrofoil. Segesta is the primary direct line. <strong>FlixBus</strong> also runs the route.

<strong>Almost hourly</strong> in peak season. Just under 2 hours.

Cheap, decent, saves you cursing at Google Maps in a rental.

Want flexibility? Rent a car. Stop for snacks, blast Italian bangers, take the long way.

Use <a href="https://www.discovercars.com/?a_aid=nico0141" target="_blank" rel="nofollow noopener">Discover Cars</a> for a fair price. More in <a href="/news/renting-car-palermo/" rel="noopener">my Palermo car-rental guide</a>. Flying in? <a href="/news/airport-transfers/" rel="noopener">My airport transfers article</a> covers PMO to wherever you're sleeping.

If you drive, you need parking near Trapani port. Don't show up hoping. Use <a href="https://parclick.it/parcheggio/porto-trapani?affiliate=670d25b9" target="_blank" rel="nofollow noopener">Parclick Trapani Port</a> to book ahead.

Once at the port? Hydrofoil to Favignana, around <strong>30 minutes</strong>.

<h3>From Trapani</h3>

Already in Trapani? Walk to the port. Easy.

Hydrofoil tickets through <a href="https://go.wearepalermo.com/ferry" target="_blank" rel="nofollow noopener">Ferryhopper</a>. They sell both Liberty Lines and Siremar tickets, so you're covered either way.

Want something more memorable than a 30-minute hydrofoil? Three captained options:

<ul>
<li><strong>Premium yacht tour with lunch.</strong> <a href="https://gyg.me/38B9HCJk" target="_blank" rel="nofollow noopener">Favignana and Levanzo Yacht Tour</a>. Highly rated, 4.6 stars on GetYourGuide, run by Egadi Lines. The polished captained option done right.</li>
<li><strong>Private group boat.</strong> <a href="https://gyg.me/XRmlMFob" target="_blank" rel="nofollow noopener">Private Tour Egadi Islands</a>. Best for 4-8 people who want their own yacht for the day.</li>
<li><strong>Shared group day cruise.</strong> <a href="https://gyg.me/ztGu5hgx" target="_blank" rel="nofollow noopener">Day Cruise Favignana and Levanzo</a>. Cheaper, social, hits both islands.</li>
</ul>

July and August? <strong>Book online ahead.</strong> Don't show up at the port with 400 panicked tourists trying to pile onto the same boat.

<h3>Hopping to Levanzo or Marettimo</h3>

Side trip from Favignana? Use <a href="https://go.wearepalermo.com/ferry" target="_blank" rel="nofollow noopener">Ferryhopper</a>.

<strong>Levanzo:</strong> about <strong>10 minutes</strong> (~€10-15 RT).

<strong>Marettimo:</strong> about <strong>30-45 minutes</strong> (from ~€20 RT).

<div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/09/nico-barcellona-portrait-scaled.jpg" alt="Nico Barcellona" /></figure>
<div>

<cite style="font-style: normal; font-weight: bold; color: #e65100;">A Local's Take:</cite>
<p style="margin: 0; color: #333;"><strong>Levanzo</strong> feels like a dream from the 1950s.</p>
<p style="margin: 0; color: #333;"><strong>Marettimo</strong> is pure wild beauty.</p>
<p style="margin: 0; color: #333;">More than two nights on Favignana? <strong>Go island-hopping.</strong> You'll thank me later.</p>

</div>
</div>

<h2>Favignana vs the Other Sicilian Islands</h2>

Trip-planning Sicily and not sure which island? Here's the honest comparison.

Most American readers haven't heard of these names. So I'll tell you what each one IS, then I'll rank.

<h3>Favignana vs Levanzo and Marettimo</h3>

[NICO: paste image URL for Levanzo or Marettimo , alt text suggestion: "Levanzo and Marettimo, the smaller Egadi Islands near Favignana"]

The other two <strong>Egadi Islands</strong>. Same chain as Favignana, same ferry network out of Trapani.

<strong>Levanzo</strong> (10 minutes by ferry from Favignana): tiny, postcard-from-1950 quiet. Half a day's worth.

<strong>Marettimo</strong> (30-45 minutes): wild cliffs, sea caves, barely any tourists. A full day.

Both are great side trips. Neither has the food, the hotels, or the buzz to be your main base.

<strong>Favignana wins on logistics.</strong>

<h3>Favignana vs Ustica</h3>

[NICO: paste image URL for Ustica , alt text suggestion: "Ustica island off Palermo, a marine reserve in Sicily"]

<strong>Ustica</strong> is a small volcanic island about <strong>90 minutes by hydrofoil NORTH of Palermo</strong>. No Trapani transfer. Marine reserve. World-class for diving and snorkeling.

The catch? You shoot yourself in the balls with anything else. <strong>Two bars, two restaurants</strong>, a couple climb-and-descents and you're done.

Want only diving? Ustica.

Everything else? Favignana.

<em>(<a href="/news/things-to-do-ustica/" rel="noopener">Read my Ustica article</a> for the full take.)</em>

<h3>Favignana vs the Aeolian Islands</h3>

[NICO: paste image URL for Aeolian Islands , alt text suggestion: "The Aeolian Islands off northern Sicily, including Stromboli and Panarea"]

The <strong>Aeolian Islands</strong> are a different trip entirely. Seven volcanic islands off Sicily's NORTH coast (not west).

<strong>Stromboli</strong> has an active volcano. <strong>Lipari</strong> has the most nightlife. <strong>Salina</strong> is the prettiest (filmed Il Postino). <strong>Panarea</strong> is where Italian celebrities vacation. <strong>Vulcano</strong>? Sulfur-mud spa.

3+ days minimum. Ferry from Palermo: around <strong>5 hours</strong>.

Got a full week and obsessed with volcanoes? Aeolians.

Got 2-3 days and want sea + sleep + tuna without a 5-hour boat ride? <strong>Favignana.</strong>

<em>(Aeolian deep-dive: <a href="/news/panarea-island/" rel="noopener">my Panarea article</a>.)</em>

<div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; align-items: center;">
<figure style="margin: 0; margin-right: 15px; flex-shrink: 0;"><img style="width: 94px; height: 94px; border-radius: 50%; object-fit: cover;" src="https://wearepalermo.com/wp-content/uploads/2025/09/nico-barcellona-portrait-scaled.jpg" alt="Nico Barcellona" /></figure>
<div>

<cite style="font-style: normal; font-weight: bold; color: #e65100;">A Local's Take:</cite>
<p style="margin: 0; color: #333;">Quick rule: <strong>Favignana for sea + ease</strong>. <strong>Aeolians for volcanoes + drama</strong>. <strong>Ustica for diving and nothing else</strong>.</p>
<p style="margin: 0; color: #333;">Short Sicily trip? Favignana. Full week with big-trip-energy? Aeolians.</p>

</div>
</div>

<div class="faq-brutto-ma-funziona">
<h2>❓ Frequently Asked Questions (The Stuff You're Still Worried About)</h2>
<details><summary><strong>Can you visit Favignana as a day trip from Palermo?</strong></summary>Yes, but you'll be exhausted. Early Segesta bus from Palermo to Trapani, last hydrofoil back. Technically doable.

But it's <strong>4-5 hours of transport</strong> for maybe 6 hours on the island.

<strong>Two nights minimum</strong> is way better. If a single day is all you have, sleep in Trapani the night before.

</details><details><summary><strong>Is Favignana expensive?</strong></summary>In peak season? Yes. Hotels start at <strong>€150+/night</strong>, even with three months' notice, for grandma's house with a wobbly fan.

Restaurant prices up <strong>30-50%</strong> over five years ago. Boats and scooters scarce.

May, June, September are reasonable. <strong>Book early or pay the late tax.</strong>

</details><details><summary><strong>What's the best time of year to visit?</strong></summary><strong>Late May to early July, then September.</strong> Great weather, warm water, crowds not yet full zombie mode.

August is the worst combo of heat, prices, and people. October still works for hiking and food, but the sea cools and some operators close.

</details><details><summary><strong>Should I avoid Favignana in August?</strong></summary>If you can swap August for late June or September, do it. <strong>August is peak crowds</strong>, <strong>peak prices</strong>, <strong>bottom availability</strong>.

If August is your only window, it's still beautiful. But book everything in advance: ferry, hotel, restaurants, boat, scooter.

Wing it and you'll hate me.

</details><details><summary><strong>Is it worth visiting the other Egadi Islands?</strong></summary>Yes. <strong>Levanzo:</strong> 10 minutes by hydrofoil, perfect half-day. <strong>Marettimo:</strong> 30-45 minutes, wild and dramatic, perfect full-day.

Use Ferryhopper. Staying 3+ nights on Favignana? Dedicate a day to a side trip.

Levanzo for postcard, Marettimo for nature.

</details><details><summary><strong>Is Favignana the same as Lampedusa?</strong></summary>No. Different parts of Sicily entirely.

<strong>Favignana</strong> is in the Egadi off Trapani in the WEST. <strong>Lampedusa</strong> is in the Pelagie, way SOUTH, closer to Tunisia.

Different ferry, different vibe, different trip. Don't confuse them.

</details><details><summary><strong>Do I need to book restaurants in advance?</strong></summary><strong>June, July, August: yes.</strong> Good places fill up by 7 PM. Walk-ins on weekend nights eat chips on a curb.

Off-peak (May, October), you can usually walk in.

Book the boat and the hotel first; restaurants are the smaller scramble.

</details><details><summary><strong>What should I skip on Favignana?</strong></summary>Renting a car (use bike or scooter). Any place with a giant photo menu in three languages. Doing Favignana as a single day-trip if you have any other option.

The Cala Rossa land approach during peak hours: hike's steep, beach is packed by 10 AM.

</details></div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Can you visit Favignana as a day trip from Palermo?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes, but you'll be exhausted. Early Segesta bus from Palermo to Trapani, last hydrofoil back. Technically doable. But it's 4-5 hours of transport for maybe 6 hours on the island. Two nights minimum is way better. If a single day is all you have, sleep in Trapani the night before."
      }
    },
    {
      "@type": "Question",
      "name": "Is Favignana expensive?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "In peak season, yes. Hotels start at €150+/night, even with three months' notice, for grandma's house with a wobbly fan. Restaurant prices up 30-50% over five years ago. Boats and scooters scarce. May, June, September are reasonable. Book early or pay the late tax."
      }
    },
    {
      "@type": "Question",
      "name": "What's the best time of year to visit Favignana?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Late May to early July, then September. Great weather, warm water, crowds not yet full zombie mode. August is the worst combo of heat, prices, and people. October still works for hiking and food, but the sea cools and some operators close."
      }
    },
    {
      "@type": "Question",
      "name": "Should I avoid Favignana in August?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "If you can swap August for late June or September, do it. August is peak crowds, peak prices, bottom availability. If August is your only window, it's still beautiful, but book everything in advance: ferry, hotel, restaurants, boat, scooter. Wing it and you'll hate me."
      }
    },
    {
      "@type": "Question",
      "name": "Is it worth visiting the other Egadi Islands?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Levanzo: 10 minutes by hydrofoil, perfect half-day. Marettimo: 30-45 minutes, wild and dramatic, perfect full-day. Use Ferryhopper. Staying 3+ nights on Favignana? Dedicate a day to a side trip. Levanzo for postcard, Marettimo for nature."
      }
    },
    {
      "@type": "Question",
      "name": "Is Favignana the same as Lampedusa?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Different parts of Sicily entirely. Favignana is in the Egadi off Trapani in the WEST. Lampedusa is in the Pelagie, way SOUTH, closer to Tunisia. Different ferry, different vibe, different trip. Don't confuse them."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need to book restaurants in advance on Favignana?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "June, July, August: yes. Good places fill up by 7 PM. Walk-ins on weekend nights eat chips on a curb. Off-peak (May, October), you can usually walk in. Book the boat and the hotel first; restaurants are the smaller scramble."
      }
    },
    {
      "@type": "Question",
      "name": "What should I skip on Favignana?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Renting a car (use bike or scooter). Any place with a giant photo menu in three languages. Doing Favignana as a single day-trip if you have any other option. The Cala Rossa land approach during peak hours: hike's steep, beach is packed by 10 AM."
      }
    }
  ]
}
</script>

<h2>Bottom Line</h2>

Choose Favignana if you want <strong>sea, food, and a 2-3 day reset</strong>. Bike to a cove. Eat tuna in front of the water. Fall asleep early.

<strong>Closest real island getaway from Palermo.</strong>

Skip Favignana if you need nightlife, you only have one day with no flexibility, or you're going in August unprepared.

Go to Mykonos. Go to Cefalù. <em>Spare yourself.</em>

Book the ferry, the hotel, the boat. Pack <strong>water shoes</strong>. <strong>Real sunscreen</strong>. No suitcase the size of a piano. Budget <strong>€10-15 for "mystery gas"</strong> on the dinghy day.

Not a scam, just how it works here.

The island delivers when you treat it right.

Treat it wrong and it'll humble you.

<div style="background-color: #f4f4f4; padding: 20px; border-radius: 8px; margin-top: 30px;">
<h3 style="margin-top: 0; text-align: center;">Continue Planning Your Sicily Trip</h3>
<ul style="list-style-type: none; padding-left: 0; text-align: center;">
     <li style="margin-bottom: 10px;"><strong>Next read:</strong> <a href="/news/things-to-do-ustica/" rel="noopener">Things to Do in Ustica</a>. The other day-trip island, closer to Palermo.</li>
     <li style="margin-bottom: 10px;"><strong>The Palermo half of your Sicily trip:</strong> <a href="https://wearepalermo.com/the-sicilian-way/" target="_blank" rel="noopener noreferrer">The Sicilian Way</a>. My paid guide for the city portion. Pairs with Favignana for the full west-Sicily experience.</li>
     <li style="margin-bottom: 10px;"><strong>Watch the chaos:</strong> <a href="https://www.youtube.com/@wearepalermo" target="_blank" rel="noopener noreferrer">WAP YouTube Channel</a></li>
</ul>
</div>

<p style="margin-top: 30px;"><em>A hug is always,</em><br />
<em>Nico Barcellona</em></p>

---

# ARCHITECT NOTES (NOT FOR PUBLICATION)

## v2 Changes vs v1

| # | Issue (Nico's complaint) | v2 fix |
|---|---|---|
| 1 | Wall-of-text paragraphs throughout | All paragraphs >45 words split at sentence boundaries. Author intro now 7 short paragraphs. |
| 2 | Zero bold in intro / many paragraphs | Bold added to skim-keywords throughout: 2-5 word phrases on every long-ish paragraph. |
| 3 | TL;DR is a word dump, mobile users skip it | Restructured from `<p>` block to `<table>` with 4 labeled rows: What it is / How to get there / How long / When to go. Skim-friendly. |
| 4 | H2 1 fragmented style ≠ paragraphs below | All paragraphs across all H2s now have the same fragmented short rhythm. |
| 5 | Wrong Nico photo on Local's Take callouts | All 8 Local's Take callouts now use `Nico-Take.png` (the correct existing site URL), matching the live post. |
| 6 | No photo under H2 2 "Best Things to Do" intro | Added `[NICO: paste image URL]` placeholder. Also added image to H3 "Rent a Boat" using `Favignana-tour-boat-scaled.jpg` (the unused new image from v1). |
| 7 | Missing hotel images for some cards | 4 hotel image URLs verified from live HTML. 2 inferred URLs (Residence Scirocco, B&B Il Tufo) replaced with `[NICO: paste image URL]` placeholders. I Pretti URL kept as inferred — if it 404s, treat as a 7th placeholder. |
| 8 | Bottom affiliate disclosure redundant | REMOVED. Top one stays. |
| 9 | "PDF" not "guide" for The Sicilian Way | Fixed: "My paid PDF" → "My paid guide" in Continue Planning. |
| 10 | Need image placeholders for Marettimo / Ustica / Aeolian | 3 placeholders added in H2 9 sub-sections. |

## Image Placeholders for Nico to Fill (6 total)

| # | Location | Suggested alt text |
|---|---|---|
| 1 | H2 2 "Best Things to Do" intro (just below H2) | "Things to do in Favignana, the Egadi Islands' biggest island" |
| 2 | H2 3 hotel card #1 (Residence Scirocco e Tramontana) | "Residence Scirocco e Tramontana apartments in Favignana" |
| 3 | H2 3 hotel card #2 (B&B Il Tufo) | "B&B Il Tufo in Favignana" |
| 4 | H2 9 H3 "Favignana vs Levanzo and Marettimo" | "Levanzo and Marettimo, the smaller Egadi Islands near Favignana" |
| 5 | H2 9 H3 "Favignana vs Ustica" | "Ustica island off Palermo, a marine reserve in Sicily" |
| 6 | H2 9 H3 "Favignana vs the Aeolian Islands" | "The Aeolian Islands off northern Sicily, including Stromboli and Panarea" |

Note on hotel card #3 (I Pretti Resort): I had inferred the URL `https://wearepalermo.com/wp-content/uploads/2022/06/i-pretti-favignana-1024x683.jpg` in v1. v2 keeps that URL. If it 404s in preview, treat as a 7th placeholder.

## Brain Doc Updates Triggered (PM action)

1. **WAP_06.md hotel card template** — still missing literal HTML in project knowledge. PM should ship a canonical hotel card HTML block in WAP_06 v2 with placeholder markers.

2. **WAP_06.md TL;DR template** — v1 used a `<p>` block in a colored div (the spec wording suggested that format). v2 uses a `<table>` layout that mobile-skims better. PM decision: which is the canonical TL;DR format going forward?

3. **WAP_06.md bold logic** — current spec rule: "bold = 2-4 word phrases only." Missing rule: "every long paragraph should have at least one bolded skim-keyword." That implicit rule was the v1 bold-failure root cause. Make it explicit.

4. **WAP_06.md Local's Take photo URL** — spec lists `nico-barcellona-portrait-scaled.jpg`. Live post and v2 use `Nico-Take.png`. PM canonical decision needed.

5. **WAP_06.md affiliate disclosure** — spec says both top and bottom. Nico's call: top only. PM update spec.

6. **SOP_01 v2.0 Pass 2 self-check rigor** — Pass 2 v3 self-claimed paragraph-length compliance and the claim was false. Add to SOP_01 Step 8 a "run actual word-count grep on every paragraph" mandate.

7. **SOP_01 v2.0 Pass 3 scope** — original spec said "Do NOT rewrite content — voice locked in Pass 2." Nico's call confirms Pass 3 CAN break wall-of-text paragraphs at sentence boundaries (mechanical, no voice change). PM clarify in SOP_01 Step 9.

## Discrepancies Found

- Pass 2 v3 self-check claim re paragraph length was inaccurate
- Two em-dashes leaked through Pass 2 in Continue Planning (both fixed in v1, kept clean in v2)
- WAP_06 v2 hotel card template HTML not retrievable
- Sicilian Way URL: wearepalermo.com vs Podia (kept wearepalermo.com)
- `cala-azzurra-faivgnana.jpg` filename has typo "faivgnana" (kept as-provided)

## Time Spent (v2)

~40 minutes on top of the v1 ~85 min. Total Pass 3 time: ~125 min, well over the 45-60 budget.

---

## Status

✅ Pass 3 v2 complete. All 10 issues from Nico's review addressed. 6 image placeholders flagged for Nico to fill. 7 brain-doc updates flagged for PM.

→ Next: Nico drops in the 6 image URLs, PM/Nico final review, publish.
