# Sailing 101 — plan and roadmap

A beginner's cheat sheet for getting into sailing on 30–36 ft GRP cruising
yachts of the 1975–2005 era: Moody 33, Sadler 32, Bavaria 1060, Gib'Sea 31/33,
Finnsailer 35 and the wider class they represent.

## Decisions (agreed 2026-09-25)

| Topic | Decision |
|---|---|
| Hosting | GitHub Pages, deployed by GitHub Actions from `main` |
| Stack | Plain HTML, CSS and vanilla JS. No build step, no framework, no npm |
| Language / units | English. Metric, knots, nautical miles. No imperial |
| Waters covered | Black Sea, Mediterranean, Adriatic, North Sea, Baltic, English Channel |
| Licensing covered | RYA ladder, ICC (UNECE Res. 40), national schemes for the waters above |
| Photos | No own photos. Wikimedia Commons / other CC-licensed images with full attribution, custom SVG diagrams, clearly marked "photo needed" slots |
| Videos | Thumbnail + link + channel credit + one paragraph on why it is worth watching. No embedded players |
| Depth | Cheat-sheet bullets and diagrams on the page, expandable "more detail" blocks per component |
| Boat scope | The five named boats as worked examples, plus the wider class |
| Build order | Thin skeleton of every section first, then deepen section by section |
| Interactivity | Search, dark mode, sticky TOC with scroll-spy, deep links, progress bar, keyboard shortcuts, print stylesheet |

## Architecture

```
index.html                 page shell: header, sidebar TOC, <main>, footer
assets/css/site.css        all styling, CSS variables for light/dark
assets/js/site.js          section loader, TOC, scroll-spy, search, theme
assets/img/                downloaded CC images (with LICENCES.md alongside)
sections/sections.json     ordered manifest: file, id, title, status
sections/NN-slug.html      one <section> per topic, plain HTML fragments
docs/PLAN.md               this file
```

* `index.html` fetches `sections/sections.json`, then every section file, and
  injects them in order. The page therefore needs an HTTP server (GitHub Pages
  or `python3 -m http.server`); it will not work over `file://`.
* Every `<section>` has a stable `id`. Every `h3`/`h4` gets an auto-generated
  `id` of the form `<section-id>--<slug>` so any heading is deep-linkable.
* Diagrams are inline SVG inside the section file. They use the shared CSS
  variables (`--dg-*`) so they follow light/dark mode.
* Search is client-side over the loaded DOM: headings, paragraphs, list items,
  glossary terms. No index file to maintain.

## Content conventions

* **Component card** (`.part-card`) for any physical part: what it is, how it
  works, positives, negatives, common faults, what to check. Optional
  `<details class="more">` for depth.
* **Photo figure** (`figure.photo`): image, caption, then
  `Photo: <author>, <licence>, via <source>` with links. Until an image is
  sourced, use `figure.photo.is-placeholder` with a short description of the
  photo wanted.
* **Video card** (`.video-card`): YouTube thumbnail, title, channel, and a
  "why watch" paragraph. Until a video is verified, use `.is-pending`.
* **Callouts**: `.callout.tip`, `.callout.warn`, `.callout.note`.
* **Spec table** (`table.spec`): metric, knots. Unverified numbers are marked
  `TBC` rather than guessed.
* Facts must be traceable. Numbers, dates and regulations carry a source link
  or a `TBC` marker until verified.

## Section roadmap and status

Status: `skeleton` (headings + intent), `draft` (real content, unreviewed),
`complete` (reviewed, sourced).

| # | Section | id | Status |
|---|---|---|---|
| 0 | Start here | `start` | skeleton |
| 1 | Anatomy and terminology | `anatomy` | complete (7 linked diagrams; reviewed by expert, beginner and designer agents, all ≥ 8.5) |
| 2 | The reference fleet | `fleet` | complete for text (specs sourced and reviewed at 8.7; photos still pending, see below) |
| 3 | Hull, keel and rudder | `hull` | draft (6 linked diagrams, sourced; reviewer round 1 scored 7.0 / 7.5 / 6.5, round 2 in progress) |
| 4 | Rig and sails | `rig` | skeleton |
| 5 | Deck hardware and steering | `deck` | skeleton |
| 6 | Engine and drivetrain | `engine` | skeleton (1 example card) |
| 7 | Boat systems | `systems` | skeleton |
| 8 | Electronics | `electronics` | skeleton |
| 9 | Sailing fundamentals | `sailing` | skeleton (points of sail diagram done) |
| 10 | Manoeuvres under engine | `manoeuvres` | skeleton |
| 11 | Navigation and passage planning | `navigation` | skeleton |
| 12 | Seas and cruising grounds | `seas` | skeleton |
| 13 | Licences and qualifications | `licences` | skeleton |
| 14 | Buying and owning | `buying` | skeleton |
| 15 | Glossary, videos, reading | `glossary` | skeleton |

## Review process (agreed 2026-09-25)

Every section is reviewed in the browser by three sub-agents before it is
called complete: a boat-expert critic, a beginner who knows no terminology,
and a designer who rates the SVGs and UI/UX. Each scores 1–10; only 8.5 or
above is accepted. Rounds so far: Anatomy 4 rounds (final 8.8 / 8.8 / 8.6),
Fleet 3 rounds with the expert (final 8.7), Hull round 1 7.0 / 7.5 / 6.5 then a combined fix pass.

## Blocked: photographs

This environment's network policy blocks page fetches and image downloads
(only web search works). To source licensed photographs the environment
needs outbound access to at least commons.wikimedia.org,
upload.wikimedia.org and en.wikipedia.org. Until then the fleet section
keeps "photo needed" placeholders. The research agent found no Commons
file for any of the five boats by search alone.

## Next steps (proposed order)

1. Review skeleton shape, adjust section list and ordering.
2. Deepen **Anatomy**: full term list, additional diagrams (deck plan from
   above, rig from ahead, below-decks layout, cockpit).
3. Deepen **Fleet**: verified specs and sourced photos for the five boats.
4. Work through **Hull → Rig → Deck → Engine → Systems → Electronics** with
   component cards and fault lists.
5. Sailing, manoeuvres, navigation, seas, licences, buying.
6. Curate the video library with verified links and credits.
