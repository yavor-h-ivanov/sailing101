# Sailing 101 — plan and roadmap

A beginner's cheat sheet for getting into sailing on 9–11 m (30–36 ft) GRP cruising
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
| 0 | Start here | `start` | draft, reviewed (safety summary, how to use, trust levels; final scores expert 9.0, beginner 8.8, designer 9.0) |
| 1 | Anatomy and terminology | `anatomy` | complete (7 linked diagrams; reviewed by expert, beginner and designer agents, all ≥ 8.5) |
| 2 | The reference fleet | `fleet` | complete for text (specs sourced and reviewed at 8.7; no CC-licensed photo of any of the five models found on Wikimedia Commons or Openverse, September 2026, so the photo slots stay as placeholders) |
| 3 | Hull, keel and rudder | `hull` | complete for text (6 linked diagrams, sourced; final scores expert 9.0, beginner 8.8, designer 8.7; 1 photo and 3 videos; fault photos still wanted) |
| 4 | Rig and sails | `rig` | complete for text (5 linked diagrams, sourced; final scores expert 9.0, beginner 8.7, designer 8.7; 1 photo and 8 videos; fault photos still wanted) |
| 5 | Deck hardware and steering | `deck` | complete for text (6 linked diagrams, sourced; final scores expert 8.5, beginner 8.8, designer 8.7; 2 photos and 8 videos; fault photos and factory specs still wanted) |
| 6 | Engine and drivetrain | `engine` | complete for text (6 linked diagrams, sourced; final scores expert 8.5, beginner 8.8, designer 8.6; 3 photos and 6 videos; fault photos and some factory specs still wanted) |
| 7 | Boat systems | `systems` | complete for text (5 linked diagrams, sourced; final scores expert 9.0, beginner 8.6, designer 8.7; 7 videos; photos and as-built fits still wanted) |
| 8 | Electronics | `electronics` | complete (4 linked diagrams; reviewed 8.5 / 8.8 / 8.6; facts checked by web search in September 2026 and linked per topic; the pages themselves could not be opened, so sources are search-verified; DSC test call still TBC; 3 photos and 7 videos) |
| 9 | Sailing fundamentals | `sailing` | complete (6 linked diagrams; reviewed 8.5 / 8.8 / 8.7; facts checked by web search in September 2026 and linked; pages search-verified, not opened; 8 videos) |
| 10 | Manoeuvres under engine | `manoeuvres` | complete (7 linked diagrams; reviewed 8.5 / 8.8 / 8.8; facts checked by web search in September 2026 and linked; pages search-verified, not opened; 1 photo and 8 videos) |
| 11 | Navigation and passage planning | `navigation` | complete (9 linked diagrams; reviewed 8.5 / 8.8 / 8.8; facts checked by web search in September 2026 and linked; pages search-verified, not opened; 2 photos and 6 videos) |
| 12 | Seas and cruising grounds | `seas` | complete (4 linked diagrams; reviewed 8.8 / 8.7 / 9.0; facts checked by web search in September 2026 and linked; pages search-verified, not opened; Baltic military areas still TBC; 1 photo and 7 videos) |
| 13 | Licences and qualifications | `licences` | complete (2 linked diagrams; reviewed 9.0 / 8.7 / 8.8; national rules checked by web search in September 2026 and linked; rules change, so the page says to check before going; 6 videos) |
| 14 | Buying and owning | `buying` | complete (2 linked diagrams; reviewed 8.8 / 8.7 / 8.8; facts checked by web search in September 2026 and linked; intervals are rules of thumb; 5 videos) |
| 15 | Glossary, videos, reading | `glossary` | draft (A–Z glossary generated from every section’s term lists, with links to each term; regenerate it when term lists change; final scores expert 8.8, beginner 8.8, designer 8.9) |

## Review process (agreed 2026-09-25)

Every section is reviewed in the browser by three sub-agents before it is
called complete: a boat-expert critic, a beginner who knows no terminology,
and a designer who rates the SVGs and UI/UX. Each scores 1–10; only 8.5 or
above is accepted. Rounds so far: Anatomy 4 rounds (final 8.8 / 8.8 / 8.6),
Fleet 3 rounds with the expert (final 8.7), Hull 4 rounds (7.0 / 7.5 / 6.5 → final 9.0 / 8.8 / 8.7), Rig 3 rounds (7.5 / 7.8 / 7.7 → final 9.0 / 8.7 / 8.7), Deck 2 rounds (7.0 / 8.2 / 7.9 → final 8.5 / 8.8 / 8.7), Engine 3 rounds (7.5 / 7.6 / 8.2 → final 8.5 / 8.8 / 8.6), Systems 3 rounds (7.0 / 7.4 / 8.4 → final 9.0 / 8.6 / 8.7), Electronics 3 rounds (7.5 / 7.8 / 8.1 → final 8.5 / 8.8 / 8.6), Sailing 2 rounds (7.5 / 8.0 / 8.2 → final 8.5 / 8.8 / 8.7), Manoeuvres 3 rounds (8.0 / 8.2 / 8.2 → final 8.5 / 8.8 / 8.8), Navigation 2 rounds (8.0 / 8.3 / 8.3 → final 8.5 / 8.8 / 8.8), Seas 2 rounds (8.0 / 7.9 / 8.4 → final 8.8 / 8.7 / 9.0), Licences 2 rounds (8.0 / 8.3 / 8.0 → final 9.0 / 8.7 / 8.8), Buying 3 rounds (8.0 / 8.2 / 7.8 → final 8.8 / 8.7 / 8.8), Glossary 3 rounds (8.0 / 7.6 / 7.6 → final 8.8 / 8.8 / 8.9), Start 2 rounds (8.0 / 8.2 / 8.3 → final 9.0 / 8.8 / 9.0). The reviews are AI passes written from three points of view (experienced skipper, beginner, designer), not checks by people. From Engine on, at most three review rounds per section.

## Photographs: network access (resolved 2026-09-28)

The environment's network policy was opened on 2026-09-28, so Commons and
YouTube are reachable. Wikimedia still rate-limits this environment heavily:
fetch one file at a time, with long pauses, from upload.wikimedia.org
without query strings. No Commons or Openverse photo exists for any of the
five fleet boats, so their slots stay as placeholders.

## Next steps (proposed order)

1. Review skeleton shape, adjust section list and ordering.
2. Deepen **Anatomy**: full term list, additional diagrams (deck plan from
   above, rig from ahead, below-decks layout, cockpit).
3. Deepen **Fleet**: verified specs and sourced photos for the five boats.
4. Work through **Hull → Rig → Deck → Engine → Systems → Electronics** with
   component cards and fault lists.
5. Sailing, manoeuvres, navigation, seas, licences, buying.
6. Curate the video library with verified links and credits.

## Photos and videos (2026-09-28)

* **Videos:** every section from Hull to Buying has a "Worth watching" block
  built by `videos()` in `tools/gen_common.py`. Each video's title and channel
  were confirmed through YouTube's oEmbed endpoint; videos were chosen by
  title, channel and description and not watched in full, and the shared note
  on every block says so. Upload dates could not be checked (YouTube pages
  were rate-limited), so credits carry no years.
* **Photos:** images come from Wikimedia Commons, are stored as 1280 px
  copies in `assets/img/`, and are placed by `photo()` / `photos()` with the
  author, licence and a link to the Commons file page. Commons rate-limits
  this environment heavily, so fetch slowly and one file at a time.
* Nothing CC-licensed was found for the five fleet models; the fleet
  placeholders say so and invite an owner's CC BY or CC BY-SA photo.


## Decision: which Gib'Sea 33 (2026-09-26)

The site uses the 2001–04 Dufour-built J&J Gib'Sea 33 as "the" Gib'Sea 33,
because it is the boat adverts and charter fleets mean. The 1970s Harlé
boat is more numerous by documented count but rare on the market; the
1990s "33" appears to be the Gib'Sea 334. Research: scratchpad rig-research.md, Part A.

## Constraint: web-search budget (2026-09-28)

This environment allows 200 web searches per session, and they ran out
during the Engine and Systems research. Sections written after that point
(Electronics onwards) rest on standard references named in each section
and on the reviewers' knowledge; figures that were not checked against a
source are marked TBC. A later session with search available should
source them.
