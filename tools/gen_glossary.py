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
SKIP = set(x.lower() for x in '''Wind|The danger|Long, low waves|Short, steep waves|Further offshore|Own boat|Another AIS boat|Hidden target|Not on AIS|Sea level now|The new tack|Ease out|Mainsheet in|Repeat the bursts|Room to turn|Burst astern in a turn|Turning on the spot|Depth close in|Stepping ashore|Stepping off|Neutral early|Approach track|Stern out|Bow out|Bow fender|Quarter fender|Engine from cold|Below decks|Sails as wings|Airflow|Drive|Keel force|Total sail force|Heeling force|Buoyancy|Telltales streaming|Windward telltale lifting|Leeward telltale lifting|True wind arrow|Wind of the boat’s motion|Rising warm air|Cold air inland|Bora gusts|Wind with tide|Wind against tide|Crosswind|Stern lines to the posts|Bow lines to the quay|Bow lines to the rock|Line in a clutch|Mooring load|Clutch lever|Clutch cam|Handle socket|Stripper arm|Winch base|Hull below the waterline|Keel joint and bolts|Stern gland or saildrive seal|Seacocks and hoses|Supporting courses|Charter requirements|Engine rebuild|Electronics|Cushions and upholstery|Wind or tide from ahead|Fenders on both sides|Drift when hove to|Helm lashed to leeward|Eased mainsail|I|J|P|E|Sails|Outer skin|Inner skin|Depth|Cycle|Relay|Vaporise|Zero lift|Seize (two meanings)|Tack|Below|Stern lines|Mooring line|Stern kick|Going astern|Sails|Burst ahead, helm hard over|Tiller extension|Sheaves|Engine service|Mast step|Deck core|Antifouling and anodes|Chart table electronics|Instrument displays|Talker|Listeners|Terminator|Power tee|Masthead antenna height|Coastguard aerial|Arc (sector)|Clutter|The smile|Void|Stainless collar|Follower|Carbon ring|Bellows|Seal grease|Packing|Spline|Cone clutch|Sender|Solenoid|Diode|O-ring|Tube stack|Engine bed|Seaway|Duty rating|Person in the water|Shout, throw, point|Engine on, ropes in|Final approach|Approach to a buoy|Pointing at the buoy|Your own line|Neighbour’s circle|Overlapping circles|Fenders in a raft|Springs in a raft|Crossing a raft|Hidden danger|Safe side|Danger side|Ship head on|Ship crossing|Ship from astern|Transit line|Fenders on both sides|Stepping onto a finger|Stopping in the berth|Lines in a finger berth|Midships line to the finger|Person in the water (under sail)|Beam reach away|Tack, jib flapping|Getting downwind|Close-reach approach|Secondary port high water'''.split('|'))

EXTRA = [
    ('Beating', 'Sailing upwind in a series of tacks, zigzagging across the wind.', 'sailing'),
    ('Broach', 'An uncontrolled turn up into the wind, usually running in a strong wind with too much sail up.', 'sailing'),
    ('COLREGs', 'The International Regulations for Preventing Collisions at Sea: the rules of the road for every vessel.', 'navigation'),
    ('Dead reckoning', 'A position worked out from course and distance run since the last known position.', 'navigation'),
    ('Fetch', 'The distance of open water the wind has blown across. The longer the fetch, the bigger the waves.', 'seas'),
    ('Heave to', 'Stop the boat under sail by backing the jib and lashing the tiller to leeward (on a wheel, turn it to windward and lock it).', 'sailing'),
    ('In irons', 'Stuck head to wind, sails flapping, with no way on and no steering.', 'sailing'),
    ('Knot', 'One nautical mile an hour. Also a thing you tie.', 'navigation'),
    ('Lee shore', 'A shore the wind is blowing onto. Dangerous: a boat in trouble drifts towards it.', 'sailing'),
    ('Luff up', 'Turn towards the wind; the same as head up.', 'sailing'),
    ('Mayday', 'The spoken distress call on VHF, for a boat or a person in grave and imminent danger; sent after a DSC distress alert.', 'electronics'),
    ('Pan-Pan', 'The urgency call on VHF: a serious problem that needs help but is not yet grave and imminent danger, such as engine failure in a shipping lane or while drifting slowly towards danger, or an injured crew member who is not in danger of life. If the boat is being driven onto rocks, it is a Mayday.', 'electronics'),
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
    ('Abaft', 'Behind: further towards the stern than something. “Abaft the beam” means behind straight out to the side.', 'anatomy'),
    ('ABYC', 'American Boat and Yacht Council: a US body whose standards for boat wiring and systems are often quoted.', 'systems'),
    ('Beaufort scale', 'Wind strength in forces 0 to 12, from calm to hurricane. Each force covers a range of wind speeds in knots, and forecasts for sailors give the wind in forces.', 'sailing'),
    ('Estimated position (EP)', 'A position worked out from the course steered, the speed through the water and the tidal stream, when no fix is available.', 'navigation'),
    ('Fire blanket', 'A fireproof sheet in a quick-release pouch by the cooker, pulled out and laid over a pan fire to smother it.', 'start'),
    ('Fire extinguisher', 'A portable bottle of powder, foam or gas for putting out a small fire. Every crew member should know where they are and how to use one.', 'start'),
    ('Fluke', 'The flat blade of an anchor that digs into the seabed.', 'deck'),
    ('Give-way vessel', 'The vessel the collision rules require to keep out of the way of another. It acts early and obviously; the other vessel, the stand-on vessel, keeps its course and speed.', 'navigation'),
    ('Harness', 'Straps worn round the chest, often built into the lifejacket, with a tether (a short line with a clip at each end) that you clip to a jackstay or a strong point so that you cannot go over the side.', 'deck'),
    ('Isophase', 'A light with equal periods of light and dark, such as Iso 4s: two seconds on, two seconds off.', 'navigation'),
    ('Lifebuoy', 'A floating ring or horseshoe kept at the stern, ready to throw to a person in the water; often with a light and a danbuoy attached.', 'sailing'),
    ('Liferaft', 'An inflatable raft packed in a canister or valise that inflates when its line is pulled, for abandoning a boat that is sinking or on fire. It needs servicing at the maker’s intervals.', 'electronics'),
    ('Motorsailer', 'A boat built to motor as well as it sails, usually with a wheelhouse and a bigger engine, such as the Finnsailer 35.', 'fleet'),
    ('Occulting', 'A light that is on for longer than it is off: the opposite of flashing.', 'navigation'),
    ('RYA', 'Royal Yachting Association: the UK national body for sailing and motor boating, which runs the courses and certificates described in Licences.', 'licences'),
    ('Sea-kindly', 'Moving gently in waves, without slamming or jerking.', 'fleet'),
    ('Sécurité', 'The safety call on VHF, said three times, before a navigation or weather warning.', 'electronics'),
    ('Stand-on vessel', 'The vessel that the collision rules require to keep its course and speed while the give-way vessel keeps clear; it must still act if a collision cannot be avoided by the other alone.', 'navigation'),
    ('Standard port', 'A port for which the tide tables give full daily times and heights of high and low water. Secondary ports are worked out from a standard port with published corrections.', 'navigation'),
    ('Stiff', 'Resisting heeling: a stiff boat stands up well to a strong wind. The opposite is tender: a tender boat heels easily. (A tender is also a boat’s dinghy.)', 'fleet'),
    ('Tidal diamond', 'A letter in a diamond printed on a chart, with a table giving the direction and rate of the tidal stream there, at springs and at neaps, for each hour before and after high water at a standard port.', 'navigation'),
    ('WOBBLE', 'The daily engine check taught at RYA training centres: Water filter, Oil, Belt, Bilges, Levels, Engine and exhaust. Some schools use Leaks and Electrics for the L and E.', 'engine'),
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
    'transit': "Two fixed, charted objects seen in line, which put you exactly on the line through them: the most accurate position line there is, and the basis of leading lines. At anchor, take a transit on the beam and check it often: a steady shift one way, not a swing back and forth, means the anchor is dragging.",
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
        out.append(f'  <h4 class="glossary__letter" id="glossary--{first.lower() if first != "#" else "num"}">{first}</h4>')
        out.append('  <dl class="glossary">')
    links = [f'<a href="#{"term-" + key if key else sid}">{titles.get(sid, sid)}</a>'] + [f'<a href="#term-{k2}">{titles.get(x, x)}</a>' for x, k2 in also]
    if name == 'Course and speed over the ground':
        name = 'Course and speed over the ground (COG, SOG)'
    gid = 'gl-' + re.sub(r'[^a-z0-9]+', '-', html.unescape(name).lower()).strip('-')
    out.append(f'    <dt id="{gid}">{name}</dt><dd>{body} <span class="glossary__where">In: {", ".join(links)}.</span></dd>')
out.append('  </dl>')
jump = ' '.join(f'<a href="#glossary--{l.lower() if l != "#" else "num"}">{l}</a>' for l in letters)

def build_video_library():
    blocks = []
    for sct in order:
        f = SEC + sct['file']
        if sct['id'] in ('start', 'glossary') or not os.path.exists(f): continue
        src = open(f).read()
        cards = re.findall(r'<p class="video-card__title"><a href="([^"]+)"[^>]*>(.*?)</a></p>\s*<p class="video-card__channel">(.*?)</p>', src, re.S)
        if not cards: continue
        lis = '\n'.join(f'        <li><a href="{u}" rel="noopener">{t}</a> <span class="video-list__channel">{c}</span></li>' for u, t, c in cards)
        blocks.append(f'''  <details class="more">
    <summary>{sct['title']} ({len(cards)})</summary>
    <div class="more__body">
      <p><a href="#{sct['id']}--worth-watching">Thumbnails and notes in {sct['title']}</a></p>
      <ul class="video-list">
{lis}
      </ul>
    </div>
  </details>''')
    total = sum(b.count('<li>') for b in blocks)
    return f'  <p>{total} videos in {len(blocks)} sections.</p>\n' + '\n'.join(blocks)
video_library = build_video_library()

FIRST = ['QkcCC5GHN8k', 'agWYQ2YGiGg', 'xlexzR3yPKA', '6ubt7BqAmdM', '1TMB4-EPMAI', 'maX1ZkfUNbU', '5hArHpw1gxE', 'F1gUxS1IR4g']
def first_videos_list():
    allcards = {}
    for sct in order:
        f = SEC + sct['file']
        if not os.path.exists(f) or sct['id'] == 'glossary': continue
        for u, t, c in re.findall(r'<p class="video-card__title"><a href="([^"]+)"[^>]*>(.*?)</a></p>\s*<p class="video-card__channel">(.*?)</p>', open(f).read(), re.S):
            allcards[u.split('v=')[1]] = (u, t, c, sct['title'])
    missing = [v for v in FIRST if v not in allcards]
    assert not missing, missing
    return '\n'.join(f'    <li><a href="{allcards[v][0]}" rel="noopener">{allcards[v][1]}</a> <span class="video-list__channel">{allcards[v][2]}</span> <span class="video-list__channel">{allcards[v][3]}</span></li>' for v in FIRST)
first_videos = first_videos_list()

page = f'''<section id="glossary">
  <h2>Glossary, videos and reading</h2>
  <p class="lead">The words defined on this site, in one alphabetical list, with a link to the section where it is explained and drawn. Then every video on the site, the books worth owning, and where to find other owners.</p>

  <h3 id="glossary--words">Glossary</h3>
  <p>{len(entries)} words, gathered from the word boxes at the start of each section, the term lists at the end, and a few more. Press <kbd>/</kbd> to search the whole page. A word in several sections links to each of them.</p>
  <div class="glossary__words">
  <p class="glossary__jump" aria-label="Jump to a letter">{jump}</p>
{chr(10).join(out)}
  </div>

  <h3 id="glossary--videos">Video library</h3>
  <p>Every video linked from this site, by section; open a section for thumbnails and a note on each.</p>
  <div class="callout note"><p>{VIDEO_NOTE}</p></div>
  <h4>Watch these first</h4>
  <p>Eight to start with; each is also listed under its section below.</p>
  <ul class="video-list">
{first_videos}
  </ul>
{video_library}

  <h3 id="glossary--reading">Reading</h3>
  <p>A short shelf, in the order a new owner is likely to need it. Editions are the latest found in September 2026; older editions are cheap second-hand and still useful, except for rules, radio procedure and anything electronic.</p>
  <h4>Learning to sail and navigate</h4>
  <ul>
    <li><em>RYA Competent Crew Skills</em> (RYA, code CCPCN; the 2014 edition, reprinted in 2024). For your first course, or before you crew for someone else: the words, the ropes and the jobs on deck.</li>
    <li><em>RYA Day Skipper Handbook – Sail</em>, Sara Hopkinson (RYA, code G71; the 2012 edition, reprinted in 2025). The book for the next course, Day Skipper: seamanship, pilotage, tides and the collision rules.</li>
    <li><em>RYA Navigation Handbook</em> (G6) and <em>RYA VHF Handbook</em> (G31). The next step on navigation, and the radio procedure behind the SRC exam.</li>
    <li><em>The Complete Yachtmaster</em>, Tom Cunliffe (Adlard Coles, 11th edition, 2025). Seamanship, boat handling, navigation and weather in one volume; the book to keep on board once the course is over.</li>
  </ul>
  <h4>On board, every season</h4>
  <ul>
    <li><strong>An almanac:</strong> the annual <em>Reeds Nautical Almanac</em> (Bloomsbury) covers the UK, Ireland and the Atlantic coast of Europe from Denmark to Gibraltar: tides, lights, harbour plans, radio and weather. For the Baltic, the Mediterranean and the Black Sea you need the pilot books and national publications instead.</li>
    <li><strong>Pilot books</strong> for each area, such as the Imray <em>Adriatic Pilot</em> by Trevor and Dinah Thompson, and <em>The Baltic Sea and Approaches</em> by the Royal Cruising Club (RCC) Pilotage Foundation (Imray, 5th edition, 2025).</li>
    <li><strong>Charts:</strong> official paper or electronic charts, or a chart folio, for the area and the current year.</li>
  </ul>
  <h4>Keeping an old boat going</h4>
  <ul>
    <li><em>RYA Diesel Engine Handbook</em>, Andrew Simpson (RYA, code G25; the 2006 edition, reprinted in 2024). A short, clear first book on the engine, before Calder.</li>
    <li><em>Boatowner’s Mechanical and Electrical Manual</em>, Nigel Calder (4th edition, 2015). Batteries, wiring, pumps, toilets, steering and nearly everything else that breaks.</li>
    <li><em>Marine Diesel Engines</em>, Nigel Calder (3rd edition). How a small diesel works, how to service it, and fault-finding charts.</li>
    <li><em>This Old Boat</em>, Don Casey (2nd edition). Surveying, repairing and improving an older GRP yacht, job by job.</li>
    <li><em>Heavy Weather Sailing</em>, Peter Bruce and Martin Thomas (Adlard Coles, 8th edition, 2022). Preparing the boat and crew for bad weather, and what happened to yachts caught out.</li>
  </ul>

  <h3 id="glossary--online">Online</h3>
  <h4>Safety and the law, for a British boat</h4>
  <ul>
    <li>{a('https://weather.metoffice.gov.uk/specialist-forecasts/coast-and-sea/inshore-waters-forecast', 'The Met Office inshore waters forecast')}: for a boat of this size within 12 miles of the coast, more useful than the shipping forecast.</li>
    <li>{a('https://www.gov.uk/register-406-beacons', 'The UK Beacon Registry')}: register an EPIRB or PLB here, free; rescuers use the details when it goes off.</li>
    <li>{a('https://www.ofcom.org.uk/spectrum/radio-equipment/ships-radio', 'Ofcom ship radio licence')}: the licence for the boat’s VHF, AIS and EPIRB, which issues the MMSI and call sign.</li>
    <li>{a('https://assets.publishing.service.gov.uk/media/5a7ca25340f0b65b3de0a2bc/msn1781.pdf', 'MSN 1781')}: the collision regulations as they apply to UK boats.</li>
    <li>{a('https://rnli.org/safety', 'RNLI sea safety')}: free advice, and lifejacket and safety checks.</li>
  </ul>
  <h4>Rules, weather and formalities everywhere</h4>
  <ul>
    <li>{a('https://www.rya.org.uk/', 'Royal Yachting Association')}: courses, the ICC, and advice on boating abroad.</li>
    <li>The collision regulations: {a('https://www.imo.org/en/about/conventions/pages/colreg.aspx', 'the IMO’s COLREG page')}, and the {a('https://www.navcen.uscg.gov/navigation-rules-amalgamated', 'full text of the rules')} as published by the US Coast Guard (the international rules are the same).</li>
    <li>{a('https://weather.metoffice.gov.uk/specialist-forecasts/coast-and-sea/shipping-forecast', 'The Met Office shipping forecast')} for British waters; the forecast services for the other seas are in <a href="#seas--forecasts">Seas</a>.</li>
    <li>{a('https://www.noonsite.com/', 'Noonsite')}: formalities, ports and practical notes for cruising yachts, country by country.</li>
  </ul>
  <h4>Clubs and pilotage</h4>
  <ul>
    <li>{a('https://www.theca.org.uk/home', 'The Cruising Association')}: a club for cruising sailors, with harbour reports from members.</li>
    <li>{a('https://rccpf.org.uk/', 'The RCC Pilotage Foundation')}: the pilot books above, and free online pilotage notes.</li>
  </ul>
  <h4>Owners of the reference fleet</h4>
  <ul>
    <li><strong>Moody 33:</strong> {a('https://www.moodyowners.org/', 'Moody Owners Association')}, and the {a('https://www.moodyowners.info/', 'Moody Owners Information Exchange')} forum.</li>
    <li><strong>Sadler 32:</strong> {a('https://sadlerandstarlight.co.uk/', 'Sadler and Starlight Owners Association')}.</li>
    <li><strong>Bavaria 1060:</strong> {a('https://www.bavariaowners.co.uk/', 'Bavaria Owners Association')}, which covers the whole range.</li>
    <li><strong>Gib’Sea 31/33:</strong> the Gib’Sea Association (gibsea.org.uk, according to search results). The site did not respond when checked in September 2026, so it is not linked yet (<span class="tbc">TBC</span>).</li>
    <li><strong>Finnsailer 35:</strong> no owners’ association was found; one owner keeps an {a('https://finnsailer35.wordpress.com/finnsailer-35-information/', 'information page on the Finnsailer 35')}.</li>
    <li>For all of them, the {a('https://forums.ybw.com/', 'YBW forum')} is a large British sailing forum where many of the owner reports in <a href="#fleet">the fleet section</a> come from. Treat forum posts as one owner’s experience, not fact.</li>
  </ul>
{sources('the reading list and links', [
  'Editions: ' + a('https://www.rya.org.uk/shop/p/rya-day-skipper-handbook-sail', 'RYA shop, Day Skipper Handbook') + ', ' + a('https://openlibrary.org/isbn/9781399422154', 'Open Library, Complete Yachtmaster 11th edition') + ', ' + a('https://openlibrary.org/isbn/9781472992604', 'Open Library, Heavy Weather Sailing 8th edition') + ', ' + a('https://store.imray.com/products/the-baltic-sea-and-approaches', 'Imray, The Baltic Sea and Approaches') + ', ' + a('https://openlibrary.org/isbn/9780071790338', 'Open Library, Boatowner’s Mechanical and Electrical Manual 4th edition') + ', ' + a('https://www.bookharbour.com/reeds-nautical-almanac-2026', 'Reeds Nautical Almanac 2026 coverage') + '.',
  'RYA books: ' + a('https://www.rya.org.uk/products/rya-competent-crew-skills/', 'RYA shop, Competent Crew Skills') + ', ' + a('https://www.rya.org.uk/products/rya-diesel-engine-handbook/', 'RYA shop, Diesel Engine Handbook') + '.',
  'Checked in September 2026: the publisher and catalogue pages were opened directly, and the links above were opened and responded, except the Ofcom and RNLI pages (confirmed by web search; their sites block automated checks) and the Gib’Sea Association site (did not respond).',
])}
</section>
'''
page = page.replace('{TBC}', TBC)
open(SEC + '15-glossary.html', 'w').write(page)
ids = re.findall(r'id="([^"]+)"', page)
print(len(entries), 'entries;', len(letters), 'letters; dup ids:', len(ids) - len(set(ids)))
