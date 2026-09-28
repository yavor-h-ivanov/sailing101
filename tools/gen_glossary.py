# Generates sections/15-glossary.html for Sailing 101: an A-Z glossary built from the term lists of every
# section (anatomy first), plus a few words that have no drawing. Re-run after any section's terms change.
import os
import sys, re, glob, json, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_common import *

SEC = ROOT + 'sections/'
order = json.load(open(SEC + 'sections.json'))
order = order['sections'] if isinstance(order, dict) else order
titles = {s['id']: s['title'] for s in order}
files = [s['file'] for s in order if s['id'] not in ('start', 'glossary')]

# words that only make sense inside one drawing
SKIP = set(x.lower() for x in '''Wind|The danger|Long, low waves|Short, steep waves|Further offshore|Own boat|Another AIS boat|Hidden target|Not on AIS|Sea level now|The new tack|Ease out|Mainsheet in|Repeat the bursts|Room to turn|Burst astern in a turn|Turning on the spot|Depth close in|Stepping ashore|Stepping off|Neutral early|Approach track|Stern out|Bow out|Bow fender|Quarter fender|Engine from cold|Below decks|Sails as wings|Airflow|Drive|Keel force|Total sail force|Heeling force|Buoyancy|Telltales streaming|Windward telltale lifting|Leeward telltale lifting|True wind arrow|Wind of the boat’s motion|Rising warm air|Cold air inland|Bora gusts|Wind with tide|Wind against tide|Crosswind|Stern lines to the posts|Bow lines to the quay|Bow lines to the rock|Line in a clutch|Mooring load|Clutch lever|Clutch cam|Handle socket|Stripper arm|Winch base|Hull below the waterline|Keel joint and bolts|Stern gland or saildrive seal|Seacocks and hoses|Supporting courses|Charter requirements|Engine rebuild|Electronics|Cushions and upholstery|Wind or tide from ahead|Fenders on both sides|Drift when hove to|Helm lashed to leeward|Eased mainsail|I|J|P|E|Sails|Outer skin|Inner skin|Depth|Cycle|Relay|Vaporise|Zero lift|Seize (two meanings)|Tack|Below|Stern lines|Mooring line|Stern kick|Going astern|Sails|Burst ahead, helm hard over|Tiller extension|Sheaves|Engine service|Mast step|Deck core|Antifouling and anodes|Chart table electronics|Instrument displays|Talker|Listeners|Terminator|Power tee|Masthead antenna height|Coastguard aerial|Arc (sector)|Clutter|The smile|Void|Stainless collar|Follower|Carbon ring|Bellows|Seal grease|Packing|Spline|Cone clutch|Sender|Solenoid|Diode|O-ring|Tube stack|Engine bed|Seaway|Duty rating'''.split('|'))

EXTRA = [
    ('Beating', 'Sailing upwind in a series of tacks, zigzagging across the wind.', 'sailing'),
    ('Broach', 'An uncontrolled turn up into the wind, usually running in a strong wind with too much sail up.', 'sailing'),
    ('COLREGs', 'The International Regulations for Preventing Collisions at Sea: the rules of the road for every vessel.', 'navigation'),
    ('Dead reckoning', 'A position worked out from course and distance run since the last known position.', 'navigation'),
    ('Fetch', 'The distance of open water the wind has blown across. The longer the fetch, the bigger the waves.', 'seas'),
    ('Heave to', 'Stop the boat under sail by backing the jib and lashing the helm to leeward.', 'sailing'),
    ('In irons', 'Stuck head to wind, sails flapping, with no way on and no steering.', 'sailing'),
    ('Knot', 'One nautical mile an hour. Also a thing you tie.', 'navigation'),
    ('Lee shore', 'A shore the wind is blowing onto. Dangerous: a boat in trouble drifts towards it.', 'sailing'),
    ('Luff up', 'Turn towards the wind; the same as head up.', 'sailing'),
    ('Mayday', 'The spoken distress call on VHF, for a boat or a person in grave and imminent danger; sent after a DSC distress alert.', 'electronics'),
    ('Pan-Pan', 'The urgency call on VHF: a serious problem that needs help but is not yet grave and imminent danger, such as engine failure well clear of danger, or an injured crew member who is not in danger of life. If the boat is being driven onto rocks, it is a Mayday.', 'electronics'),
    ('Man overboard (MOB)', 'Someone in the water from your boat, and the drill for getting them back: shout, throw, point, stop the boat, mark the position, call for help.', 'sailing'),
    ('Dividers', 'A pair of hinged pointers for measuring distances on a chart, against the latitude scale.', 'navigation'),
    ('Bar', 'A bank of sand or shingle across a harbour or river entrance; it may need a certain height of tide to cross.', 'navigation'),
    ('Sill', 'A low wall at a marina entrance that keeps water in at low tide; boats can cross only when the tide is high enough.', 'navigation'),
    ('Withy', 'A small branch or pole on a stake marking the edge of a channel, used in the Wadden Sea and other shallow tidal waters.', 'seas'),
    ('Posidonia', 'A protected Mediterranean seagrass; anchoring on its meadows is banned or restricted in many places.', 'seas'),
    ('Stern buoy', 'A buoy laid off a pontoon in Scandinavian harbours; a boat moors bow-to the pontoon with a stern line to the buoy.', 'seas'),
    ('Tether', 'The short line between a harness and a jackstay or strong point that keeps a person on board.', 'deck'),
    ('Broker', 'A yacht broker: an agent who sells boats for their owners, paid a commission by the seller.', 'buying'),
    ('Turnbuckle, bottlescrew', 'Other names for a rigging screw: see Rigging screws (turnbuckles).', 'rig'),
    ('Lifejacket', 'An inflatable or foam jacket that keeps a person’s head out of the water; worn on deck, with a crotch strap, and serviced every year or as its maker says.', 'sailing'),
    ('GRP', 'Glass-reinforced plastic, or fibreglass: glass fibre set in resin, the material of almost every boat in this class.', 'hull'),
    ('VAT evidence', 'Proof that VAT has been paid on a boat, or that it is exempt; needed to keep a boat in the EU without paying again.', 'buying'),
    ('CEVNI', 'The European code for inland waterways; an endorsement on the ICC after a short test.', 'licences'),
    ('Q flag', 'A plain yellow flag flown on arrival from abroad in countries that still ask for it, meaning “my vessel is healthy and I request free pratique”.', 'licences'),
    ('Box berth', 'A berth between two posts at the outer end and a quay or pontoon at the inner end, common in northern Europe.', 'manoeuvres'),
    ('Slack water', 'The short time around high or low water when the tidal stream is weakest, before it turns.', 'navigation'),
    ('Leading line', 'Two marks or lights kept in line to stay in a safe channel.', 'navigation'),
    ('Clearing bearing', 'A bearing of a landmark that keeps you clear of a danger as long as it stays above or below a set figure.', 'navigation'),
    ('Set and rate', 'The direction a tidal stream or current flows towards, and its speed in knots.', 'navigation'),
    ('Bora', 'A cold, violent north-easterly fall wind of the Adriatic, strongest close under the coastal mountains.', 'seas'),
    ('Mistral', 'A cold, dry north-westerly down the Rhône valley into the Gulf of Lion, often strong for days.', 'seas'),
    ('Meltemi', 'The strong summer north wind of the Aegean, at its height in July and August.', 'seas'),
    ('TSS', 'Traffic separation scheme: one-way lanes for ships, like a dual carriageway at sea.', 'navigation'),
]

KEEP_PAREN = ('crazing (acrylic)',)
def norm(n):
    n = html.unescape(n)
    if n.lower() not in KEEP_PAREN:
        n = re.sub(r'\s*\([^)]*\)', '', n)
    k = re.sub(r'[^a-z0-9]+', ' ', n.lower()).strip()
    k = ' '.join(w[:-1] if len(w) > 4 and w.endswith('s') and not w.endswith('ss') else w for w in k.split())
    return ALIAS.get(k, k)

# near-duplicates folded into one headword (after plural folding)
ALIAS = {
    'guardrail': 'guardrail and stanchion', 'lift out': 'lift out and on the hard',
    'cog and sog': 'course and speed over the ground', 'nautical mile nm': 'nautical mile',
    'genoa car and track': 'genoa track and car', 'genoa car': 'genoa track and car',
    'traveller': 'mainsheet traveller', 'speed over the ground': 'course and speed over the ground',
    'through hull skin fitting': 'skin fitting', 'guardrail lifeline': 'guardrails and stanchion',
    'reef bundle': 'reef', 'mooring line': 'warp', 'rigging screw turnbuckle': 'rigging screw', 'rope clutch': 'clutch jammer', 'draught draft': 'draught', 'nautical mile nm': 'nautical mile', 'bedding': 'bedding sealant bed', 'propeller shaft': 'propeller and shaft', 'gudgeon': 'pintle and gudgeon', 'crevice corrosion rigging': 'crevice corrosion', 'sealant bed': 'bedding sealant bed', 'tricolour and anchor light': 'tricolour', 'wheel': 'wheel or tiller',
}
# definitions rewritten so they read correctly out of their drawing's context
OVERRIDE = {
    'displacement': "The boat’s weight, equal to the water it pushes aside. About 3.7 to 6.2 tonnes for the five boats of the reference fleet.",
    'transit': "Two fixed, charted objects seen in line, which put you exactly on the line through them: the most accurate position line there is, and the basis of leading lines. At anchor, a transit that stops lining up means the anchor is dragging.",
    'stern anchor': "An anchor laid out astern, often a kedge on a reel of webbing tape at the pushpit: used to hold the boat off a rock or pontoon when moored bow-to, or to hold the stern into the swell.",
    'standing rigging': 'The fixed wires that hold the mast up: the forestay, backstay and shrouds. Replaced by age, since stainless wire fails from inside.',
    'running rigging': 'The ropes that move: halyards, sheets and control lines.',
    'crazing': "A web of fine cracks in the gelcoat only, at a hard spot or an old impact. Usually cosmetic, unlike a deep crack into the laminate; round deck fittings and stanchions it can show movement and leaks.",
}

seen = {}
for name, body, sid in EXTRA:
    seen[norm(name)] = [name, body, sid, [], None]
for f in files:
    s = open(SEC + f).read()
    sid = re.search(r'<section id="([^"]+)"', s).group(1)
    for key, name, body in re.findall(r'<li data-term="([^"]+)"><b>(.*?)</b>\s*(.*?)</li>', s, re.S):
        plain = re.sub('<.*?>', '', name).strip()
        if plain.lower() in SKIP or len(plain) < 2 or key.startswith(('by-', 'cy-')) or plain in ('How sails attach', 'Tanks and batteries'):
            continue
        body = re.sub(r'\s+', ' ', body).strip()
        k = norm(plain)
        if k in seen:
            if sid != seen[k][2] and sid not in [x for x, _ in seen[k][3]]:
                seen[k][3].append((sid, key))
            continue
        body = body.replace('the boats on this page', 'the reference fleet').replace('the five boats on this page', 'the five boats of the reference fleet')
        seen[k] = [plain, OVERRIDE.get(k, body), sid, [], key]

for f in files:
    s2 = open(SEC + f).read()
    sid = re.search(r'<section id="([^"]+)"', s2).group(1)
    for block in re.findall(r'class="first-words"[^>]*>(.*?)</(?:div|details)>', s2, re.S):
        for name, body in re.findall(r'<dt>(.*?)</dt><dd>(.*?)</dd>', block, re.S):
            plain = re.sub('<.*?>', '', name).strip()
            k = norm(plain)
            parts = [norm(x) for x in re.split(r'\s+and\s+|\s*/\s*|,\s*', re.sub(r'\s*\([^)]*\)', '', plain)) if x.strip()]
            if k in seen or (len(parts) > 1 and any(x in seen for x in parts)):
                continue
            seen[k] = [plain, re.sub(r'\s+', ' ', body).strip(), sid, [], None]

entries = sorted(seen.values(), key=lambda e: re.sub(r'[^a-z0-9]+', ' ', html.unescape(re.sub(r'^[“"]', '', e[0])).lower()).strip())
letters = []
out = []
cur = None
for name, body, sid, also, key in entries:
    first = re.sub(r'[^a-z0-9]', '', html.unescape(re.sub(r'^[“"]', '', name)).lower())[:1].upper()
    if not first.isalpha():
        first = '#'
    if first != cur:
        if cur is not None:
            out.append('  </dl>')
        cur = first
        letters.append(first)
        out.append(f'  <h4 class="glossary__letter" id="glossary--{first.lower() if first != "#" else "num"}">{first} <a class="glossary__top" href="#glossary--words">back to letters</a></h4>')
        out.append('  <dl class="glossary">')
    links = [f'<a href="#{"term-" + key if key else sid}">{titles.get(sid, sid)}</a>'] + [f'<a href="#term-{k2}">{titles.get(x, x)}</a>' for x, k2 in also]
    if name == 'Course and speed over the ground':
        name = 'Course and speed over the ground (COG, SOG)'
    gid = 'gl-' + re.sub(r'[^a-z0-9]+', '-', html.unescape(name).lower()).strip('-')
    out.append(f'    <dt id="{gid}">{name}</dt><dd>{body} <span class="glossary__where">In: {", ".join(links)}.</span></dd>')
out.append('  </dl>')
jump = ' '.join(f'<a href="#glossary--{l.lower() if l != "#" else "num"}">{l}</a>' for l in letters)

page = f'''<section id="glossary">
  <h2>Glossary, videos and reading</h2>
  <p class="lead">The words defined on this site, in one alphabetical list, with a link to the section where it is explained and drawn. Then the videos and books worth your time.</p>

  <h3 id="glossary--words">Glossary</h3>
  <p>{len(entries)} words, gathered from the word boxes at the start of each section, the term lists at the end, and a few more. Press <kbd>/</kbd> to search the whole page. A word in several sections links to each of them.</p>
  <p class="glossary__jump" aria-label="Jump to a letter">{jump}</p>
{chr(10).join(out)}

  <h3 id="glossary--videos">Video library</h3>
  <p>Each video on this site will show a thumbnail and link to its creator’s own YouTube page, with a note on why it is worth your time. None has been checked yet, so none is listed: a video is only added once it has been watched and its facts checked against the section it illustrates. The planned subjects are listed at the end of each section.</p>

  <h3 id="glossary--reading">Reading</h3>
  <p>Books that have been in print for many editions and are widely recommended on sail-training courses. Check for the current edition {TBC}.</p>
  <ul>
    <li><strong>A course handbook:</strong> the <em>RYA Day Skipper Handbook – Sail</em>, and <em>The Complete Yachtmaster</em> by Tom Cunliffe, for seamanship and navigation in one place.</li>
    <li><strong>An almanac</strong> for the waters you sail, such as the annual <em>Reeds Nautical Almanac</em>: tides, lights, harbours and radio.</li>
    <li><strong>Pilot books</strong> for each area, from publishers such as Imray, and the national charts or chart folios.</li>
    <li><strong>The boat:</strong> Nigel Calder’s <em>Boatowner’s Mechanical and Electrical Manual</em> and <em>Marine Diesel Engines</em>, for everything that breaks; Don Casey’s <em>This Old Boat</em>, for restoring an older GRP yacht.</li>
    <li><strong>Heavy weather:</strong> <em>Adlard Coles’ Heavy Weather Sailing</em>, for when it goes wrong at sea.</li>
  </ul>

  <div class="planned">
    <p>Planned for this section</p>
    <ul>
      <li>A checked video library, grouped by section, with channel credits</li>
      <li>The reading list with editions and what each book is best for</li>
      <li>Owners’ associations and forums for each boat in the reference fleet</li>
    </ul>
  </div>
</section>
'''
page = page.replace('{TBC}', TBC)
open(SEC + '15-glossary.html', 'w').write(page)
ids = re.findall(r'id="([^"]+)"', page)
print(len(entries), 'entries;', len(letters), 'letters; dup ids:', len(ids) - len(set(ids)))
