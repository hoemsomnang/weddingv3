---
title: "Web Invitation — Sonton & Santini"
date: "2026-02-14"
description: "A beautiful digital wedding e-invitation for Sonton & Santini, created by SAMBOT online. Featuring couple photos, ceremony details, and personalized guest messages."
tags: ["wedding", "e-invitation", "Cambodia", "SAMBOT online"]
coverImage: "/images/sonton-santini-cover.jpg"
author: "SAMBOT online"
---

# 💍 Web Invitation — Sonton & Santini

A romantic digital wedding e-invitation showcasing the love story of **Sonton & Santini**, beautifully crafted by [SAMBOT online](https://sambot.online).

---

## 📅 Event Details

| Detail        | Info                              |
| ------------- | --------------------------------- |
| **Couple**    | Sonton & Santini                  |
| **Date**      | February 14, 2026 💝              |
| **Platform**  | [e.sambot.co](https://e.sambot.co) |
| **Partner**   | Marriage Store                    |
| **Language**  | Khmer (Cambodian) & English       |

---

## 🎬 Video Preview

> **Duration:** 0:43 seconds  
> **Format:** Vertical (mobile-first) MP4 — 720p

The video demonstrates the full guest experience of opening the e-invitation on a smartphone, scrolling through couple photos, ceremony details, and heartfelt guest messages.

---

## 📸 Scene Breakdown

### 0:00 — Opening / Branding

The invitation opens with a stunning title screen set against a deep crimson floral background:

- 🏷️ Title: **"Web Invitation — Sonton & Santini"** in elegant gold script
- 📱 Displayed on a smartphone showing the SAMBOT online branding page
- 🤝 *"In Partnership with Marriage Store"*
- 🔗 Website: `e.sambot.co`

---

### 0:10–0:24 — Couple Photo Gallery (Traditional)

The invitation scrolls to a **photo gallery section** showing 4 romantic couple photos taken at **Angkor Wat, Cambodia**:

- 👘 Traditional Khmer wedding attire — **orange & purple outfits**
- 🏛️ Iconic Angkor Wat temple backdrop
- Warm, golden-hour tones celebrating Cambodian culture and heritage

---

### 0:25–0:35 — Couple Photo Gallery (Modern)

Continued photo gallery in **Western/modern attire**:

- 🤵 Groom in a light grey suit
- 👒 Bride in a white hat and elegant dress
- 🌿 Lush green outdoor garden venue
- Casual, romantic, and contemporary style

---

### 0:36 — Ceremony Details Section

The invitation transitions to the **ceremony information page**:

- 📜 Text in **Khmer script** with event specifics
- 📆 Dates stamped: **14-02-2026**
- RSVP and wish/greeting sections for guests
- Elegant floral border design in red and gold

---

### 0:39 — Guest Message / Wish Card

The final section showcases a **personalized guest message** card:

- 👤 Addressed to: *"Mr. Toa Sothearith"*
- 💬 A heartfelt message in English about friendship, love, and the wedding day:

> *"My beautiful childhood bestie, From playground days to your wedding day — what a journey it has been! I'm so happy to see you marrying the love of your life. May your home be filled with laughter, peace, and unconditional love. You deserve a happiest life. Love you forever. ❤️"*

---

## 🏢 About SAMBOT Online

**SAMBOT online** is a digital e-invitation service that creates stunning, interactive web-based wedding invitations.

| Info       | Details                    |
| ---------- | -------------------------- |
| 🌐 Website | [sambot.online](https://sambot.online) |
| 📱 Social  | `@sambotonline`            |
| 📞 Telegram | `081 711 611`             |
| 🤝 Partner | Marriage Store             |

> *"Make Invitation Comes Alive"*

---

## 🛠️ Usage in Next.js

This markdown file can be used with the following Next.js setups:

### With `next-mdx-remote` or `@next/mdx`

```tsx
// app/invitations/[slug]/page.tsx
import { getMDXContent } from "@/lib/mdx";

export default async function InvitationPage({ params }) {
  const { content, frontmatter } = await getMDXContent(params.slug);
  return (
    <article>
      <h1>{frontmatter.title}</h1>
      <p>{frontmatter.description}</p>
      {content}
    </article>
  );
}
```

### With `gray-matter` for Frontmatter Parsing

```ts
import matter from "gray-matter";
import fs from "fs";

export function getInvitationData(filename: string) {
  const raw = fs.readFileSync(`content/${filename}`, "utf-8");
  const { data, content } = matter(raw);
  return { frontmatter: data, content };
}
```

---

## 📂 Suggested File Structure

```
/content
  └── invitations
        └── sonton-santini-invitation.md
/public
  └── images
        └── sonton-santini-cover.jpg
/app
  └── invitations
        └── [slug]
              └── page.tsx
```

---

*Generated from video analysis of `65c46990bcc792eef9430e5798e42295_720w.mp4`*  
*E-Invitation by [SAMBOT online](https://sambot.online) — Make Invitation Comes Alive*
