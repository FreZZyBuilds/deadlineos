# ⚡ DeadlineOS — AI Crisis Command for Serious Productivity

> *The first browser OS for crisis management. AI analyzes your tasks, deadlines and mood — and decides with you. No setup. No account.*

![Hackathon](https://img.shields.io/badge/TestSprite_Hackathon-2026-3ec96a?style=flat-square)
![Made with love](https://img.shields.io/badge/made_with-♥-ff2d55?style=flat-square)
![Powered by Claude](https://img.shields.io/badge/Powered%20by-Claude%20Sonnet-00d4ff?style=flat-square)
![No Setup](https://img.shields.io/badge/Setup-0ms-a8ff3e?style=flat-square)
![Pure HTML](https://img.shields.io/badge/Stack-Pure%20HTML%2FJS-ffc840?style=flat-square)
![License](https://img.shields.io/badge/License-Proprietary-8855ff?style=flat-square)

---

> 🏆 **Made with ♥ for [TestSprite Hackathon 2026](https://testsprite.com)**  
> Built with love, ideas and the drive to be successful and help each other · Started March 2026 · Mighel Wagner

---

## 🚀 Live Demo

> Open `deadlineos-v3.html` directly in your browser — no server required.

---

## What is DeadlineOS?

Most productivity tools show you a list. DeadlineOS **decides with you.**

```
Normal tool:    "You have 7 tasks."

DeadlineOS:     "Task X is blocking your team. Start now, 90 minutes,
                 no multitasking. Deploy can wait until 16:00 — you've got this."
```

One click on **AI Analysis** and Claude reads your tasks, deadlines, mood and energy simultaneously — and delivers a precise action plan. No account. No setup. Everything runs in the browser.

---

## 🏁 How to Use

1. **Open** `index.html` in any modern browser — no server needed
2. **Click** `Open App →` to launch the main app
3. **Add tasks** with deadlines, priorities and assignees
4. **Click** `🎬 Demo` for an instant demo with 6 pre-loaded tasks
5. **Chat** with the AI Commander to get a prioritized action plan
6. **Watch** the Crisis Radar detect and alert on deadline collisions

> 💡 Everything is saved automatically in your browser via LocalStorage — your data survives page reloads.

---

## ✨ Features (V3)

| Feature | Description |
|---------|-------------|
| 🤖 **AI Commander** | Claude Sonnet analyzes tasks + deadlines + mood + energy simultaneously |
| 💬 **AI Chat** | Multi-turn with 8-message context, persistent history |
| 🚨 **Crisis Radar** | Real-time detection of overdue tasks, deadline collisions and team bottlenecks |
| 🏆 **Gamification** | XP system · 10 levels · 12 achievements · streak tracking |
| ⏱ **Focus Timer** | Pomodoro / Deep Work / Break · SVG animation |
| 🌙 **Mood Tracker** | 5 mood levels + 8-point energy scale |
| 🧠 **AI Daily Plan** | Full hourly schedule 8am–6pm |
| 👥 **Team Mode** | PIN profiles · leaderboard · @mentions |
| 📊 **Analytics** | Donut chart · 14-day sparkline · 28-day matrix |
| 📋 **Priority Matrix** | Eisenhower matrix for instant task prioritization |
| 🌐 **i18n DE/EN** | Auto-detect + toggle, all pages translated |
| 🔌 **Integrations** | Google Cal · Slack · Spotify · Discord · Email · Browser notifications |
| 🎬 **Demo Mode** | One-click demo with 6 realistic tasks — perfect for presentations |
| 🌙 **4 Color Themes** | Dark UI with scanlines/grain effect — choose your vibe |

---

## 🤖 AI Commander

DeadlineOS features a **smart AI** powered by Claude Sonnet that understands your full context — tasks, deadlines, mood, energy and team status — all at once.

The AI understands natural language and responds intelligently to:

- 📊 **Task analysis** — *"analyze my tasks"*, *"what should I focus on?"*
- 🚨 **Crisis detection** — *"am I in crisis?"*, *"what's on fire?"*
- ⏰ **Deadline help** — *"which deadlines are critical?"*, *"help me prioritize"*
- 👥 **Team management** — *"who is overloaded?"*, *"team status"*
- ⚡ **Productivity coaching** — *"how can I be more productive?"*, *"I'm overwhelmed"*
- 🍅 **Pomodoro guidance** — *"start a focus session"*, *"I need a break"*

---

## 🛠️ Tech Stack

```
Frontend:   Vanilla HTML + CSS + JavaScript   — zero dependencies
AI:         Claude Sonnet (claude-sonnet-4-20250514) via Anthropic API
Fonts:      JetBrains Mono · Unbounded         — Google Fonts CDN
Storage:    localStorage                        — no cloud needed
Deploy:     Any static host                     — Netlify, Vercel, GitHub Pages
```

**No build tools. No frameworks. No node_modules.** Open the file = done.

---

## 📂 Project Structure

```
deadlineos/
├── index.html                  ← Landing Page
├── deadlineos-v3.html          ← The App (AI + Demo Mode + Crisis Radar)
├── dos-demo.html               ← Interactive demo page
├── dos-features.html           ← Features overview
├── dos-pricing.html            ← Pricing — 3 plans, FAQ
├── dos-roadmap.html            ← V1→V5 timeline + community voting
├── dos-compare.html            ← DeadlineOS vs. Notion / Todoist / Linear / Asana
├── 404.html                    ← Error page with auto-redirect
├── privacy.html                ← Privacy policy
├── robots.txt                  ← SEO
├── sitemap.xml                 ← SEO
├── .nojekyll                   ← GitHub Pages fix (do not delete!)
└── README.md
```

---

## 🚢 Deployment

### Netlify Drop (30 seconds, recommended)
1. Open [app.netlify.com/drop](https://app.netlify.com/drop) → drag folder in
2. Done — Netlify automatically assigns a `*.netlify.app` URL

### GitHub Pages
```bash
git init
git add .
git commit -m "DeadlineOS v3 — TestSprite Hackathon 2026"
git branch -M main
git remote add origin https://github.com/USERNAME/deadlineos.git
git push -u origin main
# → Repo Settings → Pages → Source: main / root → Save
```

### Vercel
```bash
npx vercel --yes
```

---

## 🔑 API Key

For AI features: enter your [Anthropic API Key](https://console.anthropic.com) in the app login.

> ⚠️ **Never commit an API key to a public repository.**

---

## 🗺️ Roadmap

| Version | Status | What |
|---------|--------|------|
| **V1** | ✅ March 10, 2026 | Tasks, timer, AI integration, 4 themes |
| **V2** | ✅ March 10, 2026 | Team mode, analytics, AI daily plan |
| **V3** | 🔵 **Live** | AI chat, gamification, mood tracker, PIN profiles, i18n |
| **V4** | 🟠 Q2 2026 | Cloud sync, PWA, push notifications |
| **V5** | 🔮 Q3–Q4 2026 | AI agents, enterprise, marketplace |

---

## 🧪 Testing

This project uses **TestSprite MCP** for AI-generated automated test coverage.

All test cases are in the `testsprite_tests/` folder and cover:

- ✅ Task creation and management
- ✅ AI Commander responses
- ✅ Crisis Radar detection logic
- ✅ LocalStorage persistence
- ✅ Demo Mode functionality
- ✅ XP and gamification system
- ✅ Mobile responsive UI
- ✅ Theme switching
- ✅ Mood tracking
- ✅ Pomodoro timer

---

## 🔒 Privacy & Data

> DeadlineOS stores **ALL data exclusively on your own device. No exceptions.**

### ✅ What this means:

| Aspect | Details |
|--------|---------|
| 📦 **Data Storage** | Exclusively in your browser's `localStorage` — directly on your device |
| 🚫 **No Cloud** | **Zero data** is ever transmitted to any cloud, server, or external database |
| 🚫 **No Tracking** | No analytics, no monitoring, no telemetry whatsoever |
| 🚫 **No Account** | No registration, no login, no email required |
| 🚫 **No Third-Party Access** | Neither the developer, TestSprite, nor any third party has access to your data — ever |
| 🌐 **Fully Offline** | The app works completely without an internet connection |
| 🗑️ **Data Deletion** | Delete all your data at any time by clearing your browser's `localStorage` |

### 📋 What data is stored locally?

```
- Your tasks & deadlines
- Your XP progress & level
- Your mood & energy settings
- Your personal notes
- Your AI chat history
- Your focus session data
```

> 💡 **Bottom line:** DeadlineOS is 100% private. Your data never leaves your browser.
> No server. No cloud. No access by us. Never.

---

## ⚖️ LICENSE & COPYRIGHT NOTICE — PLEASE READ CAREFULLY

```
DEADLINEOS — PROPRIETARY SOFTWARE LICENSE
════════════════════════════════════════════════════════════════════════

Copyright © 2026 Mighel Wagner. All Rights Reserved.

════════════════════════════════════════════════════════════════════════
OWNERSHIP
════════════════════════════════════════════════════════════════════════

DeadlineOS (the "Software") is the exclusive intellectual property of
Mighel Wagner. All rights to the Software, including all texts,
graphics, source code, concepts, designs, logos and functionality,
remain with the owner.

════════════════════════════════════════════════════════════════════════
WHAT IS PERMITTED ✅
════════════════════════════════════════════════════════════════════════

The following is expressly permitted and encouraged:

  ✅  Use of the Software for private and professional purposes
  ✅  Suggesting extensions, ideas and feature requests
  ✅  Contributing to the project via pull requests and contributions
      (with prior written consent of the owner)
  ✅  Forking the project for collaboration purposes in direct
      agreement with Mighel Wagner
  ✅  Discussion, feedback and public dialogue about the Software
  ✅  Integration of own extensions in agreement with the owner

════════════════════════════════════════════════════════════════════════
WHAT IS PROHIBITED ❌
════════════════════════════════════════════════════════════════════════

Without express written permission from Mighel Wagner, the following
is expressly prohibited:

  ❌  Distribution, sharing or publication of the Software or parts
      thereof in any form (digital or physical)
  ❌  Sale, licensing or commercial use of the Software by third parties
  ❌  Renaming and publishing under a different name
  ❌  Embedding in other products or services without written permission
  ❌  Removal or alteration of this license notice and copyright notices
  ❌  Reverse engineering for the purpose of independent commercial use

════════════════════════════════════════════════════════════════════════
COLLABORATION & CONTRIBUTIONS
════════════════════════════════════════════════════════════════════════

Contributions to the project are warmly welcome. By submitting a
contribution (pull request, patch, idea, code) the contributor declares:

  1. That the contribution is their own intellectual property.
  2. That ownership of the contribution passes irrevocably to
     Mighel Wagner upon acceptance by the owner.
  3. That no compensation claims arise from the contribution,
     unless a separate written compensation agreement exists.

For collaboration requests, partnerships or licensing inquiries:
  📧  mighelwagner@gmail.com

════════════════════════════════════════════════════════════════════════
DISCLAIMER
════════════════════════════════════════════════════════════════════════

The Software is provided "as is", without any express or implied
warranty. The owner assumes no liability for damages arising from
the use of the Software.

════════════════════════════════════════════════════════════════════════

DeadlineOS — "Every app shows you tasks. DeadlineOS decides with you."

Date: March 10, 2026
Owner: Mighel Wagner
```

Full license terms also available as file: [`LICENSE`](./LICENSE) · 📧 mighelwagner@gmail.com

---

## 👨‍💻 Author

- 👤 **Mighel Wagner**
- 🐙 GitHub: [@Mighel881](https://github.com/Mighel881)
- 📧 Contact: [mighelwagner@gmail.com](mailto:mighelwagner@gmail.com)

---

## 🏆 Built For

**TestSprite Hackathon — Season 01 (March 2026)**

> *"Build with AI. Test with TestSprite."*

🗓️ **Started:** March 2026

---

*DeadlineOS — "Every app shows you tasks. DeadlineOS decides with you."*  
*🏆 Made with ♥ for TestSprite Hackathon 2026 · Powered by Claude AI*
