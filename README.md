# Sailing 101

A one-page, scrollable beginner's cheat sheet for getting into sailing on
30–36 ft GRP cruising yachts (Moody 33, Sadler 32, Bavaria 1060,
Gib'Sea 31/33, Finnsailer 35 and similar).

Plain HTML, CSS and JavaScript. No build step.

## Run locally

The page loads its sections with `fetch()`, so it needs an HTTP server:

```sh
python3 -m http.server 8000
# then open http://localhost:8000/
```

## Deploy

Pushes to `main` deploy to GitHub Pages via `.github/workflows/pages.yml`.
One-time setup in the repository settings: **Settings → Pages → Build and
deployment → Source: GitHub Actions**.

## Add or edit a section

1. Create or edit `sections/NN-slug.html`. The file is an HTML fragment
   containing exactly one `<section id="slug" class="topic">` with an `h2`
   and `h3`/`h4` subsections.
2. Register it in `sections/sections.json` (order in the array is page order).
3. Follow the component patterns documented in `docs/PLAN.md`.

## Content rules

* Metric units and knots. English.
* No guessed numbers: mark unverified values `TBC` and add a source when
  filled in.
* Images: only licences that permit reuse (CC BY, CC BY-SA, CC0, public
  domain). Always credit author, licence and source in the caption.
* Videos: thumbnail and link only, always credit the channel, always say why
  the video is recommended.

See `docs/PLAN.md` for the full plan, architecture and roadmap.
