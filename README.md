# DeadlineOS 🔴

> **Das erste Browser-Betriebssystem für Krisenmanagement.**  
> KI analysiert deine Lage — in Echtzeit, ohne Setup, ohne Bullshit.

![Hackathon](https://img.shields.io/badge/TestSprite_Hackathon-2026-3ec96a?style=flat-square)
![Made with love](https://img.shields.io/badge/made_with-♥-ff2d55?style=flat-square)
![Powered by Claude](https://img.shields.io/badge/Powered%20by-Claude%20Sonnet-00d4ff?style=flat-square)
![No Setup](https://img.shields.io/badge/Setup-0ms-a8ff3e?style=flat-square)
![Pure HTML](https://img.shields.io/badge/Stack-Pure%20HTML%2FJS-ffc840?style=flat-square)
![License](https://img.shields.io/badge/License-Proprietary-8855ff?style=flat-square)

---

> 🏆 **Made with ♥ for [TestSprite Hackathon 2026](https://testsprite.com)**  
> Gebaut an einem Tag · 10. März 2026 · Mighel Wagner

---

## 🚀 Live Demo

> Ordner auf [app.netlify.com/drop](https://app.netlify.com/drop) ziehen → fertig.  
> Oder direkt `deadlineos-v3.html` im Browser öffnen — kein Server nötig.

---

## Was ist DeadlineOS?

Die meisten Produktivitäts-Tools zeigen dir eine Liste. DeadlineOS **entscheidet mit dir.**

```
Normales Tool:    "Du hast 7 Tasks."

DeadlineOS:       "Task X blockiert dein Team. Starte jetzt, 90 Minuten,
                   kein Multitasking. Deploy kann um 16:00 — du schaffst das."
```

Ein Klick auf **KI-Analyse** und Claude liest Tasks, Deadlines, Stimmung und Energie gleichzeitig — und gibt einen präzisen Aktionsplan. Kein Account. Kein Setup. Alles im Browser.

---

## Dateien

| Datei | Was | Größe |
|-------|-----|-------|
| `index.html` | **Landing Page** (= deadlineos-landing-v2.html umbenannt) | ~95 KB |
| `deadlineos-v3.html` | **Die App** — vollständiges Browser-OS mit allen 8 Features | ~137 KB |
| `dos-demo.html` | 10-Sekunden Auto-Demo + interaktiv | ~56 KB |
| `dos-features.html` | Feature Deep-Dive | ~48 KB |
| `dos-pricing.html` | Preise — 3 Pläne, FAQ | ~34 KB |
| `dos-roadmap.html` | V1→V5 Timeline + Community Voting | ~31 KB |
| `dos-compare.html` | DeadlineOS vs. Notion / Todoist / Linear / Asana | ~30 KB |
| `404.html` | Fehlerseite mit Auto-Redirect | ~9 KB |
| `privacy.html` | Datenschutzerklärung | ~11 KB |
| `robots.txt` + `sitemap.xml` | SEO | — |
| `.nojekyll` | GitHub Pages Fix | — |

---

## Features (V3)

| Feature | Was |
|---------|-----|
| 🤖 KI-Kommandant | Claude Sonnet analysiert Tasks + Deadlines + Stimmung + Energie gleichzeitig |
| 💬 KI-Chat | Multi-Turn mit 8 Nachrichten Kontext, persistente Historie |
| 🏆 Gamification | XP-System · 10 Level · 12 Achievements · Streak-Tracking |
| ⏱ Fokus-Timer | Pomodoro / Deep Work / Pause · SVG-Animation |
| 🌙 Moodtracker | 5 Stimmungsstufen + 8-Punkt Energie-Skala |
| 🧠 KI-Tagesplan | Vollständiger Stundenplan 8–18 Uhr |
| 👥 Team-Modus | PIN-Profile · Leaderboard · @Mentions |
| 📊 Analytics | Donut-Chart · 14-Tage Sparkline · 28-Tage Matrix |
| 🌐 i18n DE/EN | Auto-detect + Toggle, alle Seiten übersetzt |
| 🔌 Integrationen | Google Cal · Slack · Spotify · Discord · E-Mail · Browser-Notifications |

---

## Tech Stack

```
Frontend:   Vanilla HTML + CSS + JavaScript   — keine Dependencies
KI:         Claude Sonnet (claude-sonnet-4-20250514) via Anthropic API
Fonts:      JetBrains Mono · Unbounded         — Google Fonts CDN
Storage:    localStorage                        — keine Cloud nötig
Deploy:     Jeder statische Host                — Netlify, Vercel, GitHub Pages
```

**Keine Build-Tools. Keine Frameworks. Keine node_modules.** Datei öffnen = fertig.

---

## Projektstruktur

```
deadlineos/
├── index.html                  ← Landing Page (deadlineos-landing-v2.html umbenennen!)
├── deadlineos-v3.html          ← Die App
├── dos-demo.html
├── dos-features.html
├── dos-pricing.html
├── dos-roadmap.html
├── dos-compare.html
├── 404.html
├── privacy.html
├── robots.txt
├── sitemap.xml
├── .nojekyll                   ← GitHub Pages Fix (nicht löschen!)
└── README.md
```

---

## Deployment

### Netlify Drop (30 Sekunden, empfohlen)
1. `deadlineos-landing-v2.html` → `index.html` umbenennen
2. [app.netlify.com/drop](https://app.netlify.com/drop) öffnen → Ordner reinziehen
3. Fertig — Netlify vergibt automatisch `*.netlify.app` URL

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

## API Key

Für KI-Features: [Anthropic API Key](https://console.anthropic.com) im App-Login eingeben.

> ⚠️ **Niemals einen API Key in ein öffentliches Repository committen.**

---

## Roadmap

| Version | Status | Was |
|---------|--------|-----|
| **V1** | ✅ 10. März 2026 | Tasks, Timer, KI-Integration, 4 Themes |
| **V2** | ✅ 10. März 2026 | Team-Modus, Analytics, KI-Tagesplan |
| **V3** | 🔵 **Live** | KI-Chat, Gamification, Moodtracker, PIN-Profile, i18n |
| **V4** | 🟠 Q2 2026 | Cloud-Sync, PWA, Push-Notifications |
| **V5** | 🔮 Q3–Q4 2026 | KI-Agenten, Enterprise, Marketplace |

---

## ⚖️ Lizenz

**© 2026 Mighel Wagner — Alle Rechte vorbehalten.**  
Vollständige Lizenzbedingungen: [`LICENSE`](./LICENSE) · 📧 hallo@deadlineos.app

---

*DeadlineOS — "Jede App zeigt dir Tasks. DeadlineOS entscheidet mit dir."*  
*🏆 Made with ♥ for TestSprite Hackathon 2026 · Powered by Claude AI*
