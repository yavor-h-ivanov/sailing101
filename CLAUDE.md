# Working notes for this repository

* Static site, plain HTML/CSS/JS, no build tooling. Do not add npm, bundlers
  or frameworks.
* Page shell is `index.html`; content lives in `sections/*.html` fragments
  registered in `sections/sections.json`. Plan and conventions: `docs/PLAN.md`.
* Test locally with `python3 -m http.server` (fetch needs HTTP, not file://).
* Metric and knots only. English. Never invent specs, dates, regulations or
  YouTube video IDs: use `TBC` / `.is-pending` placeholders until verified.
* Images must be CC-licensed with author, licence and source in the caption.
* Update the status table in `docs/PLAN.md` and `sections/sections.json`
  when a section moves from skeleton to draft to complete.
