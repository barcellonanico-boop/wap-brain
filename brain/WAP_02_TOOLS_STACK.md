# WAP_02_TOOLS_STACK.md — Tools Stack

Last updated: April 19, 2026

---

## 1. Content & Website

**WordPress — wearepalermo.com**
The main site. All blog posts and pages live here. 79 posts, 35 pages as of April 2026. Nico manages it directly. No developer.

**YouTube**
~60 videos. Talking head + B-roll + voiceover format. Nico on camera always. Inactive for ~4 months as of April 2026.

**Instagram**
Dormant. Inactive for ~1 year.

**TikTok**
Dormant. Inactive for ~1 year.

---

## 2. Product & Email

**Podia**
Hosts The Sicilian Way premium guide. Handles checkout and delivery. Price: $47 with $31 downsell. Planned migration to Lovable in a future project.

**ConvertKit**
Email marketing platform. Connected to The Sicilian Way funnel. Manages the soap opera sequence and subscriber list. No documented automation system yet for WAP — this is a future project.

---

## 3. Tracking & Analytics

**Google Analytics 4 (GA4)**
Main analytics tool for wearepalermo.com traffic, behavior, and conversions.

**Google Tag Manager (GTM)**
Manages tracking tags on the site. Connected to GA4.

**Switchy**
Link shortener and tracker. Used for affiliate links and campaign tracking.

---

## 4. Affiliate Programs

**Booking.com**
Primary revenue source. Affiliate links embedded throughout the site, primarily on the Where to Stay page and location-specific pages (Cefalu, San Vito Lo Capo, etc.).

**Discover Cars**
Secondary revenue source. Car rental affiliate links.

**GetYourGuide**
Minor revenue source. Experiences and tours affiliate links.

---

## 5. AI Tools

**Claude (Anthropic)**
Primary AI tool for content creation, Brain doc management, and the WAP Content Machine workflow.

**Gemini (Google)**
Secondary AI tool. Used by Nico for research and supplementary tasks.

---

## 6. Project & Brain Management

**GitHub — wap-brain repo**
URL: github.com/barcellonanico-boop/wap-brain
All WAP Brain docs, SOPs, and project docs live here. Cloned locally to ~/wap-brain/. HTTPS authentication (SSH not configured on this machine).

---

## 7. Tool Connections Map

WordPress → GA4 (via GTM) → tracks traffic and behavior
ConvertKit → The Sicilian Way funnel → Podia checkout
Switchy → wraps affiliate links → GA4 tracks clicks
Claude → reads wap-brain repo → executes content SOPs
