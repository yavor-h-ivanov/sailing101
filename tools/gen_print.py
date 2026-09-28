# Writes the printable pages in print/: a passage plan template, and a viewing checklist compiled from the
# buyer's checklists in each section. Re-run after changing any of those checklists.
import os, re, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
OUT = ROOT + 'print/'
os.makedirs(OUT, exist_ok=True)

CSS = '''
  :root { --fg: #15181c; --muted: #4a5560; --line: #9aa7b3; --soft: #eef2f6; }
  * { box-sizing: border-box; }
  body { margin: 0; background: #fff; color: var(--fg); font: 9.5pt/1.3 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }
  main { max-width: 190mm; margin: 0 auto; padding: 12mm 10mm; }
  h1 { font-size: 18pt; margin: 0 0 2mm; }
  h2 { font-size: 12pt; margin: 4.5mm 0 1.5mm; padding-bottom: 1mm; border-bottom: 1.5px solid var(--fg); break-after: avoid; }
  p.note { color: var(--muted); font-size: 9.5pt; margin: 0 0 4mm; }
  table { width: 100%; border-collapse: collapse; margin: 0 0 2mm; break-inside: avoid; }
  th, td { border: 1px solid var(--line); padding: 1.2mm 2mm; text-align: left; vertical-align: top; }
  th { background: var(--soft); font-weight: 600; font-size: 9.5pt; }
  td.fill { height: 6.5mm; }
  table.tall td.fill { height: 9mm; }
  td.box { height: 24mm; }
  .fields { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0 6mm; }
  .fields div { border-bottom: 1px solid var(--line); padding: 2.2mm 0 0.8mm; font-size: 9.5pt; color: var(--muted); }
  ul.check { list-style: none; padding: 0; margin: 0 0 2mm; }
  ul.check li { padding: 1.4mm 0 1.4mm 8mm; position: relative; border-bottom: 1px dotted var(--line); break-inside: avoid; }
  ul.check li.then { padding-left: 0; font-style: italic; color: var(--muted); border-bottom: 0; }
  ul.check li.then::before { display: none; }
  dl.words { columns: 2; column-gap: 6mm; font-size: 8.5pt; margin: 0; }
  dl.words dt { font-weight: 600; break-after: avoid; }
  dl.words dd { margin: 0 0 1.2mm; break-inside: avoid; }
  ul.check li::before { content: ""; position: absolute; left: 0; top: 2mm; width: 4mm; height: 4mm; border: 1.5px solid var(--fg); border-radius: 1mm; }
  .page { break-before: page; }
  .page:first-of-type { break-before: auto; }
  .noprint { margin: 0 0 6mm; padding: 3mm; background: var(--soft); border-radius: 2mm; font-size: 10pt; }
  footer { margin-top: 8mm; font-size: 8.5pt; color: var(--muted); }
  @media print { .noprint { display: none; } main { padding: 0; } @page { size: A4; margin: 12mm; } }
'''

def page(title, body, back):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Sailing 101</title>
<style>{CSS}</style>
</head>
<body>
<main>
<p class="noprint">A printable page from <a href="../index.html#{back}">Sailing 101</a>. Print it (Ctrl+P or ⌘P), or save it as a PDF, and fill it in by hand. <a href="../index.html#{back}">Back to the site</a>.</p>
{body}
<footer>Sailing 101 · a cheat sheet for learning, not a substitute for training, a current chart, the pilot book or the boat’s own manuals.</footer>
</main>
</body>
</html>
'''

def rows(n, cols):
    return '\n'.join('<tr>' + ''.join('<td class="fill"></td>' for _ in range(cols)) + '</tr>' for _ in range(n))

def table(head, n, cls=''):
    return f'<table{cls}><thead><tr>{"".join(f"<th>{h}</th>" for h in head)}</tr></thead><tbody>\n{rows(n, len(head))}\n</tbody></table>'

def fields(names):
    return '<div class="fields">' + ''.join(f'<div>{n}</div>' for n in names) + '</div>'

# ---------------------------------------------------------------- passage plan
pp = f'''<h1>Passage plan</h1>
<p class="note">Two pages for a day passage, in the order of the plan in the Navigation section. Times: say whether UT or local.</p>
{fields(['Boat', 'Skipper', 'Date', 'Crew on board (number)'])}
<h2>1 Where and when</h2>
{fields(['From', 'To', 'Distance (nm)', 'Planned departure', 'Expected arrival', 'Tidal gates (place and time)', 'Depth over bar or sill on leaving', 'Depth over bar or sill on arriving'])}
<h2>2 The route</h2>
{table(['No.', 'Waypoint', 'Latitude, longitude', 'Course (°T)', 'Course (°M), to steer', 'Distance (nm)', 'Dangers, and how to clear them'], 6)}
<h2>3 Tides</h2>
{table(['Place', 'HW time', 'HW height', 'LW time', 'LW height', 'Range, springs or neaps'], 3)}
{table(['Time', 'Tidal stream: direction', 'Rate (kn)', 'Time', 'Tidal stream: direction', 'Rate (kn)'], 3)}
<h2>4 Weather</h2>
{fields(['Forecast: source and time issued', 'Wind: direction and force', 'Sea state', 'Visibility', 'Outlook for the next day', 'My limit: I will not go out in'])}
<h2>5 Bolt holes (harbours to run to if plans change)</h2>
{table(['Port of refuge', 'Distance from route', 'State of tide to enter', 'VHF channel', 'Notes'], 3)}
<h2>6 Pilotage plan for the arrival</h2>
<p class="note">Write it large enough to read in the cockpit.</p>
{table(['Mark or landmark, in order', 'Bearing or leading line', 'Depth', 'Notes (clearing bearings, lights)'], 5, ' class="tall"')}
<table><tbody><tr><td class="box">Berth, and a sketch of the entrance:</td></tr></tbody></table>
<h2>7 Boat and crew</h2>
<ul class="check">
<li>Fuel (litres) and water on board: ________ / ________</li>
<li>Engine checks done (WOBBLE: water filter, oil, belt, bilges, levels, engine and exhaust)</li>
<li>Safety kit checked: lifejackets, harnesses, liferaft, flares, grab bag, fire extinguishers</li>
<li>Crew briefed: lifejackets, man overboard, the radio, the gas, the engine</li>
<li>Seasickness plan; food and drink for the day</li>
<li>Watch plan, if it is a long day</li>
</ul>
{table(['Crew member', 'Experience', 'Notes'], 4)}
<h2>8 Someone ashore knows</h2>
{fields(['Name', 'Phone', 'Told: route and ETA', 'Call the coastguard if no news by'])}
'''
open(OUT + 'passage-plan.html', 'w').write(page('Passage plan', pp, 'navigation--passage-plan'))

# ---------------------------------------------------------------- viewing checklist, compiled from the sections
SEC = ROOT + 'sections/'
parts = [('14-buying.html', 'buying--viewing', 'First look round the boat'),
         ('03-hull.html', 'hull--checklist', 'Hull, keel and rudder'),
         ('04-rig.html', 'rig--checklist', 'Rig and sails'),
         ('05-deck.html', 'deck--checklist', 'Deck hardware and steering'),
         ('06-engine.html', 'engine--checklist', 'Engine and drivetrain'),
         ('07-systems.html', 'systems--checklist', 'Boat systems'),
         ('08-electronics.html', 'electronics--checklist', 'Electronics')]
def plain(fragment):
    t = re.sub(r'<(?!/?(strong|em)\b)[^>]+>', '', fragment)
    t = re.sub(r'<(/?)(strong|em)\b[^>]*>', r'<\1\2>', t)
    for tok in ('¹', '²'):
        t = t.replace(tok, '')
    t = re.sub(r'\s+', ' ', t).strip()
    return re.sub(r'\s+([),.;:])', r'\1', t)
# the Buying section's first look repeats the section checklists; keep only what they do not cover
FIRST_LOOK_DROP = ('Hull below the waterline', 'Keel joint', 'Rudder', 'Stern gland or saildrive', 'Seacocks and hoses', 'Deck',
                   'Chainplates', 'Mast step', 'Standing rigging', 'Sails', 'Engine')
WORDS = [('Bubble test', 'with the burners off, bubbles in the leak detector fitted in the gas line (or in soapy water brushed on the joints) mean a leak.'),
         ('Bucket test', 'a bucket of water poured into a drain: it should run away at once.'),
         ('Cutless bearing', 'the water-lubricated rubber bearing that carries the propeller shaft where it leaves the hull.'),
         ('Flame-failure device', 'a valve on each gas burner that shuts off the gas if the flame goes out.'),
         ('Gypsy stamp', 'the chain size cast or stamped on the windlass’s chain wheel (the gypsy); the chain must match it.'),
         ('Partners', 'where a keel-stepped mast passes through the deck.'),
         ('Rag test', 'on steering wires, a rag run along the wire snags on broken strands; on toilet hoses, a damp rag wiped on the hose that smells afterwards means the hose needs replacing.'),
         ('T-terminals', 'fittings at the top of a shroud that hook into slots in the mast.'),
         ('Vented loop', 'a loop of toilet hose above the waterline with a small valve at the top that stops sea water siphoning back into the boat.')]
body = ['<h1>Viewing a used yacht: the checklist</h1>',
        '<p class="note">Compiled from the buyer’s checklists in each section of Sailing 101; the reasons behind every item are there, and the words in <em>italics</em> are explained at the end. Tick as you go, note what you find, and take photographs. A checklist does not replace a surveyor.</p>',
        fields(['Boat and year', 'Where viewed', 'Date', 'Asking price'])]
seen = set()
for i, (f, hid, name) in enumerate(parts):
    src = open(SEC + f).read()
    start = src.index(f'id="{hid}"')
    ol = re.search(r'<ol[^>]*>(.*?)</ol>', src[start:], re.S)
    items = [plain(x) for x in re.findall(r'<li>(.*?)</li>', ol.group(1), re.S)]
    out = []
    for x in items:
        head = re.sub(r'<[^>]+>', '', re.match(r'(<strong>.*?</strong>)?', x).group(0) or '').strip(' .:')
        if (i == 0 and head.startswith(FIRST_LOOK_DROP)) or (head and head in seen): continue
        seen.add(head)
        for w, _ in WORDS:
            x = re.sub(r'\b(' + re.escape(w.lower()) + r's?)\b', r'<em>\1</em>', x, count=1, flags=re.I)
        out.append(f'<li class="then">{x}</li>' if head.startswith('Then') else f'<li>{x}</li>')
    body.append(f"<h2>{'Below decks: first impressions' if i == 0 else name}</h2>")
    body.append('<ul class="check">\n' + '\n'.join(out) + '\n</ul>')
body.append('<h2>Words on this list</h2><dl class="words">' + ''.join(f'<dt>{w}</dt><dd>{d}</dd>' for w, d in WORDS) + '</dl>')
body.append('<h2>Notes</h2><table><tbody><tr><td class="box"></td></tr></tbody></table>')
open(OUT + 'viewing-checklist.html', 'w').write(page('Viewing checklist', '\n'.join(body), 'buying--viewing'))
print('print/passage-plan.html, print/viewing-checklist.html')
