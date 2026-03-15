# ⚡ DeadlineOS — AI Crisis Command for Serious Productivity

 "Every app shows you tasks. DeadlineOS decides with you."

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

## 🚀 What is DeadlineOS?

**DeadlineOS** is a fully browser-based productivity OS that combines AI-powered task management, crisis detection, mood tracking, and gamification — all without requiring a single login or installation.

Built for people who don't just want *another* to-do app. Built for people who are **in the middle of it**.

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

> Structure follows the **TestSprite Hackathon submission requirements**.

```
deadlineos/
├── src/                        ← All source code
│   ├── index.html              ← Landing Page
│   ├── deadlineos-v3.html      ← The App (AI + Demo Mode + Crisis Radar)
│   ├── dos-demo.html           ← Interactive demo page
│   ├── dos-features.html       ← Features overview
│   ├── dos-pricing.html        ← Pricing — 3 plans, FAQ
│   ├── dos-roadmap.html        ← V1→V5 timeline + community voting
│   ├── dos-compare.html        ← DeadlineOS vs. Notion / Todoist / Linear / Asana
│   ├── pitch.html              ← Pitch deck (browser-based, keyboard navigation)
│   ├── privacy.html            ← Privacy policy
│   ├── 404.html                ← Error page with auto-redirect
│   ├── _preview.html           ← Internal preview navigation
│   ├── banner.png              ← Project banner
│   ├── mcp.json                ← MCP server config
│   ├── package.json            ← Node config (for test runner)
│   └── LICENSE                 ← Source-Available Collaboration License
│
├── testsprite_tests/           ← AI-generated test cases (TestSprite)
│   └── core-functions.test.js  ← 42 tests across 2 suites — all passing ✅
│
├── README.md                   ← Project documentation (this file)
└── demo.mp4                    ← 1:21 min live demo video 🎬
```

---


## 🔑 API Key

For AI features: enter your [Anthropic API Key](https://console.anthropic.com) in the app login.
This is just for the Beginning others will coming in the future Updates

> ⚠️ **Never commit an API key to a public repository.**

---

## 🗺️ Roadmap

| Version | Status | What |
|---------|--------|------|
| **V1** | ✅ March 10, 2026 | Tasks, timer, AI integration, 4 themes |
| **V2** | ✅ March 11, 2026 | Team mode, analytics, AI daily plan |
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

### Running Tests

```bash
npm install
npx jest test/__tests__/core-functions.test.js
```

> **Result: 42/42 tests passing** across 2 test suites.

---

## 📋 Changelog

### v3.3.0 — March 14, 2026 (Full English Translation)

#### 🌐 Complete German → English Translation Pass (All Files)

All remaining German text across every HTML file has been translated to English.

**`index.html`**

| German | English |
|--------|---------|
| `Von 0 zu Kontrolle. In 4 Stepen.` | `From 0 to Control. In 4 Steps.` |
| `Planung` (card tag) | `Planning` |
| `Sicherheit · Team` (card tag) | `Security · Team` |
| `AI-Kommandant` | `AI Commander` |
| `PIN-Prole` / `PIN-Prole & Team Mode` | `PIN-Profiles` / `PIN-Profiles & Team Mode` |
| `Tasks eingeben` | `Enter Tasks` |
| `Taskn mit Priority und Deadline anlegen. Drag & Drop…` | `Add tasks with priority and deadline. Drag & Drop…` |
| `AI analysieren lassen` | `Let AI Analyze` |
| `Eine HTML-Datei. Open, get started. Zero Friction.` | `One HTML file. Open, get started. Zero Friction.` |
| `PIN-protectede Prole` | `PIN-protected Profiles` |
| `PWA — auf Homescreen` | `PWA — Add to Home Screen` |
| `Tasks erfassen` | `Capture Tasks` |
| `Schnell eingeben, AI priorisiert automatisch.` | `Enter quickly, AI prioritizes automatically.` |
| `Drag & Drop Sortierung` | `Drag & Drop Sorting` |
| `Predictive Warnungen` | `Predictive Warnings` |
| `AI aktivieren` | `Activate AI` |
| `Voller context-Zugriff` | `Full context access` |
| `Flow halten` | `Stay in the Flow` |
| `der Rest.` | `the Rest.` |
| `Integrierter Focus Timer` | `Integrated Focus Timer` |
| `Zero Setup (sofort im Browser)` | `Zero Setup (instantly in browser)` |
| `Mood Tracker & Energy im AI context` | `Mood Tracker & Energy in AI context` |
| `Tool-Chaos` | `Tool Chaos` |
| `Notion, Trello, … und trotzdem vergisst du die wichtigste Deadline. Der kognitive Overhead…` | Full English translation |
| `Kein Crisis Radar` | `No Crisis Radar` |
| `None echte AI` | `No Real AI` |
| `Die gamification really motivates. In 3 Weeks… davor mit Notion.` | `The gamification really motivates. In 3 weeks… before with Notion.` |
| `Der AI Chat ist das Killer-Feature. Antworten die meinen echten context kennen — nichts Comparebares.` | `The AI Chat is the killer feature. Answers that know my real context — nothing comparable.` |
| `Als Hackathon-Veteran kenne ich viele Tool-Projekte. DeadlineOS ist das erste, das ich danach weiter benutzt habe.` | `As a hackathon veteran I've seen many tool projects. DeadlineOS is the first one I kept using afterwards.` |
| `Du hast Asked Questions, wir haben Antworten. Nicht dabei? Schreib uns…` | `You have questions, we have answers. Not covered? Write us…` |
| `Brauche ich eine Internetverbindung?` | `Do I need an internet connection?` |
| `Wie sicher sind meine Daten?` | `How secure is my data?` |
| `Welche AI steckt hinter DeadlineOS?` | `What AI powers DeadlineOS?` |
| `Funktioniert es auf dem Handy?` | `Does it work on mobile?` |
| `Was unterscheidet DeadlineOS wirklich?` | `What really sets DeadlineOS apart?` |
| `Andere Tools zeigen dir was du hast…` | `Other tools show you what you have…` |
| `Kann ich meine Daten exportieren?` | `Can I export my data?` |
| `▶ Aktuell — 10. March 2026` | `▶ Current — March 10, 2026` |
| `V1 — Kern-Foundation` | `V1 — Core Foundation` |
| `Team Mode, Analytics-Dashboard, Integrationen…` | `Team Mode, Analytics Dashboard, Integrations…` |
| `V3 — AI Chat, Gamification & Prole` | `V3 — AI Chat, Gamification & Profiles` |
| `Account-Sync, Cloud-Backup, Real-time-Kollaboration…` | `Account sync, cloud backup, real-time collaboration…` |
| `V5 — Enterprise & AI-Agenten` | `V5 — Enterprise & AI Agents` |
| `AI-Agenten` (chip) | `AI Agents` |
| `↗ Nur 8% der PM-Tools nutzen kontextbewusstes AI-Reasoning` | `↗ Only 8% of PM tools use context-aware AI reasoning` |
| `Free starten →` | `Start Free →` |
| `offen` (JS open count) | `open` |
| `Tasks neu priorisiert` (JS toast) | `Tasks re-prioritized` |

**`deadlineos-v3.html`**

| German | English |
|--------|---------|
| `✓ Save & starten` | `✓ Save & Start` |
| `Prole "${name}" created!` | `Profile "${name}" created!` |
| `lang==='xx'?'offen':'open'` | `'open':'open'` |
| `i18n — Deutsch / English` (comment) | `i18n — German / English` |
| Email report strings: `Tagesbericht`, `Dein DeadlineOS Tagesbericht`, `Offen insgesamt`, `None kritischen Tasks`, etc. | All translated to English |

**`dos-demo.html`**

| German | English |
|--------|---------|
| `10-Sekunden Walkthrough` | `10-Second Walkthrough` |
| `oder drück Play` | `or press Play` |
| `2. Task hinzufügen` | `2. Add Task` |
| `3. AI analysiert` | `3. AI Analyzes` |
| `6. XP steigt` | `6. XP Rises` |
| `alles live hier.` | `all live here.` |
| `Task hinzufügen: +10/15/25 XP je nach Priorität` | `Add task: +10/15/25 XP depending on priority` |
| `Timer abschließen: +20 XP pro Session` | `Complete timer: +20 XP per session` |
| `Daten bleiben lokal — no account nötig` | `Data stays local — no account needed` |
| `Auto-Demo starten` | `Auto-Demo Start` |
| `Dashboard — Dein Überblick` | `Dashboard — Your Overview` |
| `Tasks hinzufügen, erledigen, Timer starten —` | `Add tasks, complete them, start timer —` |

**`privacy.html`**

| German | English |
|--------|---------|
| `Deine Mood` | `Your mood` |
| `Oder in der App: Profile → Settings → Delete all data` | `Or in the app: Profile → Settings → Delete all data` |
| `Prole → Settings` (JS) | `Profile → Settings` |
| `Prole names and PINs` | `Profile names and PINs` |

**`pitch.html`**
- `TestSprite Hackathon 2025` → `TestSprite Hackathon 2026` (3× — from v3.2.0)

**`dos-pricing.html`**
- `5 AI Analysiss / Day` → `5 AI Analyses / Day`
- `Unlimited AI Analysiss` → `Unlimited AI Analyses`

**`index.html` (JS variable)**
- `aiAnalysiss` → `aiAnalyses` (internal variable rename for consistency)

---

### v3.2.0 — March 14, 2026 (Translation & Localization Fix)

#### 🌐 Landing Page — "Try It Now" Demo Section Fully Translated to English

| Location | Before (German) | After (English) |
|----------|-----------------|-----------------|
| Demo section heading | `Teste es jetzt. / Direkt hier.` | `Try it now. / Right here.` |
| Task input label | `Neue Task` | `New Task` |
| AI actions label | `AI-Aktionen` | `AI Actions` |
| AI analyze button | `⚡ AI analysieren` | `⚡ AI Analyze` |
| Auto-prioritize button | `🎯 Auto-priorisieren` | `🎯 Auto-prioritize` |
| Tasks list header | `Taskn (0)` | `Tasks (0)` |
| Empty state message | `Noch keine Taskn.` | `No tasks yet.` |
| Stats label | `Taskn` | `Tasks` |
| Stats label | `XP gesamt` | `Total XP` |
| Stats label | `Prioritysverteilung` | `Priority Distribution` |
| Stress warning badge | `⚠ KRITISCH` | `⚠ CRITICAL` |
| CTA above buttons | `Volle App mit AI Chat, Daily plan, Analytics & mehr` | `Full App with AI Chat, Daily Plan, Analytics & more` |
| JS empty state (dynamic) | `Noch keine Taskn.` | `No tasks yet.` |

#### 🗓️ Pitch Deck Year Update

| File | Before | After |
|------|--------|-------|
| `pitch.html` (×3) | `TestSprite Hackathon 2025` | `TestSprite Hackathon 2026` |

---

### v3.1.0 — March 14, 2026 (Bugfix Release)

#### 🐛 Bug Fixes

**XP System — Exploit Prevention**

| Issue | Fix |
|-------|-----|
| **Create/Delete XP Spam** — Repeatedly creating and deleting tasks gave unlimited XP (+10 per create) | Deleting an uncompleted task now **claws back** the +10 XP that was granted on creation |
| **Complete-Toggle XP Spam** — Toggling a task done/undone repeatedly gave +25 XP each time | Added `completeXpGranted` flag per task — completion XP is awarded **only once** per task, regardless of how many times it is toggled |

**404 Page Fixes**

| Issue | Fix |
|-------|-----|
| Auto-redirect pointed to `deadlineos-landing-v2.html` (non-existent file) | Fixed to redirect to `index.html` |
| Logo and back-link also pointed to `deadlineos-landing-v2.html` | Fixed to `index.html` |
| Mixed German/English text (`"Nextleitung in"`, `"Error aufgetreten"`, `"← Back zur Home"`) | All text corrected to proper English |

**Footer Link Fixes** (`dos-compare.html`, `dos-features.html`, `dos-pricing.html`, `dos-roadmap.html`, `privacy.html`)

| Issue | Fix |
|-------|-----|
| Home/Logo links pointed to `deadlineos-landing-v2.html` | Fixed to `index.html` across all pages |

**Test Suite Fixes** (`jest.setup.js`, `test/__tests__/core-functions.test.js`)

| Test | Issue | Fix |
|------|-------|-----|
| TC-012 | Level-Cap formula: `Math.floor(1500/100)+1 = 16` instead of max `10` | Added `Math.min(..., 10)` cap |
| TC-013 | `localStorage.setItem` was not mocked in jsdom environment | Replaced with `Object.defineProperty` override in `jest.setup.js` |
| TC-014 | `localStorage.getItem.mockReturnValue` not recognized | Fixed via jest.setup.js + `DB.get()` now falls back to `localStorage.getItem()` |
| TC-015 | Same localStorage mock issue | Resolved through jest.setup.js fix |

**Profile PIN Fix**

| Issue | Fix |
|-------|-----|
| Profile "Myself" used PIN `0000`, Profile "Anna K." used `1234` | Both profiles now use PIN `1234` for consistency |

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

## 🎤 Pitch Deck

The project includes a fully interactive pitch deck (`pitch.html`) that can be navigated with keyboard arrows or scroll — no presentation software needed, it runs directly in the browser.

### Slide Overview

**Slide 1 — Title**
Opens with the core tagline: *"The AI-powered operating system for people who refuse to miss deadlines."* Key stats upfront: 10 features, AI-powered, 0 dependencies.

**Slide 2 — The Problem**
*83% of teams miss deadlines. Every single quarter.*
Three root causes are broken down visually:
- **Silent Stress** — teams don't realize they're overloaded until burnout hits
- **Task Chaos** — 50+ tasks, no real priorities, everything feels urgent
- **No Intelligence** — current tools are dumb checklists that don't learn or predict failures

**Slide 3 — The Solution**
DeadlineOS is framed not as another task manager, but as an intelligent operating system that analyzes, predicts, and coaches teams in real-time. The three-step flow: add tasks → AI analyzes urgency & priorities → get coached in real-time.

**Slide 4 — Core Features**
All 10 features shown side by side with icons:
AI Commander · Crisis Radar · Auto-Prioritize · Pomodoro Engine · XP & Levels · Team Profiles · Mood Tracker · Analytics Hub · Smart Notes · AI Integration

**Slide 5 — AI Integration**
Deep dive into what Claude Sonnet actually does inside the app: deadline risk analysis, personalized daily plans, burnout pattern detection, mood-adaptive recommendations, natural language coaching, and real-time crisis scoring. Also highlights the Smart Mock System — a fully local fallback with 11 response categories and 20+ templates, so the app works even without an API key.

**Slide 6 — Tech Stack**
*Pure. Fast. Zero Dependencies.*
HTML5 · CSS3 · Vanilla JavaScript · Claude Sonnet API · LocalStorage · Web Animations API
9 HTML files · 0 npm packages · sub-1s load time · 100% client-side

**Slide 7 — Roadmap**
Four phases from MVP to enterprise:
- ✅ Foundation — tasks, timer, mood, local storage
- ✅ AI Integration — Claude commander, crisis radar, auto-prioritization
- 🔵 Team & Gamification ← current: XP/levels, achievements, team profiles, analytics
- 🟠 Cloud & Collaboration — real-time sync, shared dashboards, mobile app
- 🔮 Enterprise & Integrations — Jira, GitHub, Slack, Google Calendar, SSO

**Slide 8 — Live Demo**
One-click demo mode: open `deadlineos-v3.html`, click 🎬 DEMO, watch the AI come alive. No API key needed, no server, works fully offline.

**Slide 9 — Closing**
*"Deadlines don't kill projects. Silence does. DeadlineOS breaks the silence with AI."*

### How to present it
Open `pitch.html` in any modern browser. Use **↑ ↓ arrow keys** or **scroll** to advance slides. Each slide is self-contained and visually animated — no setup, no projector software, no PowerPoint.

---

## 👨‍💻 Author

- 👤 **Mighel Wagner**
- 🐙 GitHub: [@FreZZyBuilds](https://github.com/FreZZyBuilds)
- 📧 Contact: [mighelwagner@gmail.com](mailto:mighelwagner@gmail.com)

---

## 🏆 Built For

**TestSprite Hackathon — Season 01 (March 2026)**

> *"Build with AI. Test with TestSprite."*

🗓️ **Started:** March 2026

---

*DeadlineOS — "Every app shows you tasks. DeadlineOS decides with you."*  
*🏆 Made with ♥ for TestSprite Hackathon 2026 · Powered by Claude AI*

---
TestSprite Account
TestSprite email used for this project: mighelwagner@gmail.com
