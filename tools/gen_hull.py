# Generates sections/03-hull.html for Sailing 101.
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
import sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_hull_diagrams as g
from gen_common import video, videos, photo, photos

ONE = '<span class="conf conf--one" title="Single source: found in only one place and not independently confirmed">¹</span>'
TWO = '<span class="conf conf--conflict" title="Sources disagree, or the figure is anecdotal (forum, owner report)">²</span>'
TBC = '<span class="tbc" title="To be confirmed: not yet verified against a reliable source">TBC</span>'
HINT = '<span class="diagram__hint">Every labelled part is a link: hover it (or tap it on a phone) to read its definition under the drawing; click it, tap it again or use “Full entry” to jump to the full entry. In the term lists, a name with a small circle after it is on a drawing; click it to see where.</span>'

def figure(fid, short, viewbox, title, desc, body, caption, note='', wide=True, start=0):
    cls = 'diagram diagram--wide' if wide else 'diagram'
    return f'''  <figure class="{cls}" id="{fid}" data-short="{short}">
    <div class="diagram__scroll" data-start="{start}"><svg viewBox="{viewbox}" role="group" aria-labelledby="{fid}-title {fid}-desc">
      <title id="{fid}-title">{title}</title>
      <desc id="{fid}-desc">{desc}</desc>
{body}
    </svg></div>
    <figcaption><span class="caption">{caption}</span>{note}</figcaption>
  </figure>'''

HEADS = {
  'part':  ('How it works', 'Positives', 'Negatives', 'Common faults', 'What to check'),
  'fault': ('What happens', 'The good news', 'The bad news', 'Signs', 'What to do'),
}
def card(cid, name, aka, intro, how, pros, cons, faults, check, kind='part', fold=False):
    def ul(items): return '\n'.join(f'          <li>{i}</li>' for i in items)
    h = HEADS[kind]
    aka_html = f'\n      <span class="part-card__aka">{aka}</span>' if aka else ''
    extra = ' part-card--fault' if kind == 'fault' else ''
    if fold:
        tag, head_open, head_close, top = 'details', '<summary class="part-card__head">', '</summary>', f'<details class="part-card part-card--fold{extra}" id="{cid}" open>'
    else:
        tag, head_open, head_close, top = 'article', '<div class="part-card__head">', '</div>', f'<article class="part-card{extra}" id="{cid}">'
    return f'''  {top}
    {head_open}
      <h4>{name}</h4>{aka_html}
    {head_close}
    <div class="part-card__body">
      <p>{intro}</p>
    </div>
    <div class="part-grid">
      <div class="how"><h5>{h[0]}</h5><ul>
{ul(how)}
      </ul></div>
      <div class="pros"><h5>{h[1]}</h5><ul>
{ul(pros)}
      </ul></div>
      <div class="cons"><h5>{h[2]}</h5><ul>
{ul(cons)}
      </ul></div>
      <div class="faults"><h5>{h[3]}</h5><ul>
{ul(faults)}
      </ul></div>
      <div class="check"><h5>{h[4]}</h5><ul>
{ul(check)}
      </ul></div>
    </div>
  </{tag}>'''

def terms(rows):
    out = ['  <ul class="terms">']
    for key, name, body in rows:
        out.append(f'    <li data-term="{key}"><b>{name}</b> {body}</li>')
    out.append('  </ul>')
    return '\n'.join(out)

def sources(title, items):
    lis = '\n'.join(f'        <li>{i}</li>' for i in items)
    return f'''  <details class="more">
    <summary>Sources and confidence: {title}</summary>
    <div class="more__body">
      <ul>
{lis}
      </ul>
    </div>
  </details>'''

def a(url, text=None):
    return f'<a href="{url}" rel="noopener">{text or url.split("/")[2]}</a>'

def compare(caption, head, rows):
    th = ''.join(f'<th scope="col">{h or "<span class=sr-only>Feature</span>"}</th>' for h in head)
    body = '\n'.join('        <tr><th scope="row">' + r[0] + '</th>' + ''.join(f'<td>{c}</td>' for c in r[1:]) + '</tr>' for r in rows)
    return f'''  <div class="table-wrap">
    <table class="spec compare">
      <caption>{caption}</caption>
      <thead><tr>{th}</tr></thead>
      <tbody>
{body}
      </tbody>
    </table>
  </div>'''

# ------------------------------------------------------------------ content
page = f'''<section id="hull">
  <h2>Hull, keel and rudder</h2>
  <p class="lead">The hull keeps the water out, the keel keeps the boat upright and stops it sliding sideways, and the rudder points it where you want. On a thirty- to fifty-year-old glass-fibre boat this is also where the expensive surprises live, so this section is written for the day you stand under a boat with a torch. In a hurry? <a href="#hull--checklist">Jump to the one-afternoon checklist</a>.</p>

  <div class="first-words">
    <p>Ten words before anything else</p>
    <dl>
      <dt>GRP</dt><dd>Glass-reinforced plastic, or “fibreglass”: layers of glass fibre soaked in liquid plastic (resin) that sets hard. Every boat on this page is built of it.</dd>
      <dt>Gelcoat</dt><dd>The smooth, coloured outer skin of the plastic, a fraction of a millimetre thick. It is what you polish, and what osmosis lifts.</dd>
      <dt>Laminate</dt><dd>The stack of glass-and-resin layers behind the gelcoat. That is the actual structure.</dd>
      <dt>Ballast</dt><dd>The heavy metal, iron or lead, in or under the keel that keeps the boat upright.</dd>
      <dt>Draught</dt><dd>How deep the boat reaches below the waterline, keel included. Deep draught sails better; shallow draught goes more places.</dd>
      <dt>Grounding</dt><dd>Touching the bottom. “Going aground” or “touching” is the same thing. Every keel on this page is designed to survive a gentle one.</dd>
      <dt>Drying out</dt><dd>Sitting on the seabed when the tide goes out. Bilge keels do it standing up; a fin keel needs support.</dd>
      <dt>Lift-out</dt><dd>Craning the boat out of the water. A boat “on the hard” is standing ashore on wooden or steel props (supports), in a cradle or on a trailer, which is when you can inspect the keel and rudder.</dd>
      <dt>Bedding</dt><dd>The flexible sealant under any fitting bolted through the hull or deck. When it fails, water gets in.</dd>
      <dt>Seacock</dt><dd>A tap on a hole in the bottom of the boat. A cruising boat of this size has several. Each one can sink you.</dd>
    </dl>
  </div>
  <p class="conf-key"><b>Marks used below:</b> {ONE} means the fact comes from a single source; {TWO} means sources disagree or the figure is anecdotal (a forum or owner report); {TBC} means not yet verified. Everything unmarked is supported by at least two sources listed under “Sources and confidence” at the end of each topic.</p>

  <h3>How a GRP boat is built</h3>
  <p>A hull is made in a female mould (a hollow shape the size of the boat, like a jelly mould), outside first: gelcoat is sprayed in, then layer after layer of glass is laid in by hand and “wetted out”, that is soaked with resin. The hull and the deck are separate mouldings that are joined later. Decks are usually a sandwich, two thin skins with a light core between them, because a flat panel needs thickness to be stiff. The drawing shows both, magnified.</p>

{figure('fig-laminate', 'laminate section', '0 0 940 360', 'Magnified sections through a solid GRP hull and a cored deck', 'Left: a solid hull laminate with gelcoat on the outside and alternating layers of chopped-strand mat and woven roving. Right: a cored deck with gelcoat, an outer skin, a balsa or plywood core and an inner skin; a deck fitting is bolted through with a backing plate, and water past a failed sealant bed has soaked a patch of the core.', g.laminate(), 'A solid hull is heavy, tough and easy to repair, and on this class it is the norm. A cored deck is stiff and light, but every fitting bolted through it is a way in for water, and a wet core goes soft.', note=HINT)}

  <ul>
    <li><strong>Mat and cloth.</strong> Chopped-strand mat (CSM) is a felt of short fibres that soaks up resin and fills the shape; woven roving is a heavy cloth that gives strength. Builders alternate them. Early hand-laid hulls often have uneven resin, dry patches and air voids in the mat {TWO}.</li>
    <li><strong>Resins.</strong> Boats of the 1970s and early 1980s were built with the cheapest general-purpose polyester (orthophthalic), which absorbs water most readily. Builders moved to isophthalic resin and gelcoat during the 1980s, which resists water far better, and vinylester is used today as a barrier skin. This is widely cited as the main reason older boats blister and newer ones mostly do not {TWO}.</li>
    <li><strong>Thickness.</strong> A hull of this size is thickest along the keel and at the bow and thinnest in the topsides (the part of the hull above the waterline). Stiffness comes as much from the bulkheads, the stringers (lengthwise ribs bonded inside the hull) and the internal grid as from the skin. Figures quoted on forums vary too much to publish {TWO}.</li>
    <li><strong>Print-through</strong> is the weave of the cloth showing faintly through the gelcoat, worst on dark hulls. Cosmetic.</li>
    <li><strong>Crazing</strong> is a web of fine cracks in the brittle gelcoat only, usually at a hard spot (a place where a bulkhead or fitting stops the hull flexing) or an old knock. A single deep crack that runs through the gelcoat into the laminate is a different thing and needs a surveyor’s opinion.</li>
    <li><strong>The hull-to-deck joint</strong> is where the two mouldings meet. Most sailing boats of this class have an inward flange (a lip) on the hull with the deck sitting on it, bedded in sealant and bolted or screwed; the cheaper “shoebox” joint, where the deck drops over the hull like a lid, relies on its fasteners. Leaks here are the hardest on the boat to trace, because the water travels a long way inside before it shows.</li>
  </ul>
{sources('construction', [
  a('https://www.pbo.co.uk/expert-advice/essential-boat-construction-guide-grp-wood-and-metal-106586','Practical Boat Owner, boat construction guide') + ' and ' + a('https://www.boatoutfitters.com/fiberglass-101-learn-content','Fiberglass 101') + ' on layup; an ' + a('https://forums.ybw.com/threads/old-grp-layup-spec.60530/','owners’ forum thread') + ' on early hand layup (anecdotal).',
  'Resins: ' + a('http://lnvtblog.blogspot.com/2018/05/resins-isophthalic-vs-orthphophthalic.html','ortho vs isophthalic') + ', ' + a('https://stevedmarineconsulting.com/wp-content/uploads/2014/03/Blisters-and-Osmosis.pdf','Steve D’Antonio on blisters and osmosis') + ', ' + a('https://www.boatdesign.net/threads/isophthalic-resin-vs-vinyl-ester.17904/','boatdesign.net on vinylester') + '.',
  'Print-through and crazing: ' + a('https://medusamarine.co.uk/index.php/pattern-starting-gel-coat/','Medusa Marine on print-through') + ', ' + a('https://www.safe-skipper.com/stress-cracks-on-grp-boats/','Safe Skipper on stress cracks') + ', ' + a('https://dreamsandsails.com/en/sailboat-survey-guide-chapter-1-grp-fiberglass-hull-structure-and-fundamental-defects/','a survey guide to GRP defects') + '.',
  'Hull-to-deck joints: ' + a('https://goodoldboat.com/the-hull-to-deck-joint/','Good Old Boat') + ', ' + a('https://wavetrain.net/2012/01/31/fiberglass-boatbuilding-hull-deck-joints/','WaveTrain') + ', ' + a('https://www.safe-skipper.com/repairing-a-leaking-hull-to-deck-joint/','Safe Skipper on repairing leaks') + '.',
  'Hull thickness figures come only from forum threads and range from a few millimetres in the topsides to over 20 mm at the keel; none is published here.'
])}

  <h3>Keel types</h3>
  <p>The keel does two jobs at once: its weight rights the boat, and its area stops the boat being pushed sideways by the wind. How the designer shaped it decides how the boat sails, where it can float and what happens when it touches the bottom.</p>

{figure('fig-keels', 'keel types', '0 0 900 300', 'Four keel arrangements found on the reference fleet', 'Fin keel with a spade rudder in profile; long keel with a keel-hung rudder in profile; twin bilge keels seen from astern sitting upright on the ground; a centreboard that lifts into a ballast stub.', g.keels(), 'Side views have the bow to the right. Fin keels sail closest to the wind and fastest; long keels hold a straight course and take the ground gracefully; bilge keels dry out upright, which matters on tidal coasts; a centreboard gives the shallowest draught of all at the cost of a case in the cabin and more to maintain.')}

{compare('Keel types at a glance', ['', 'Fin', 'Bilge (twin)', 'Long', 'Centreboard'], [
  ['Draught', 'deepest', 'shallower', 'shallow to moderate', 'shallowest, board up'],
  ['Sailing to windward', 'best', 'good to fair', 'fair', 'good, board down'],
  ['Handling in a marina', 'turns in its own length', 'good', 'wide turns, poor astern', 'good'],
  ['Dries out', 'only on legs or a cradle', 'standing on its keels', 'leaning against a harbour wall', 'flat, if the stub allows'],
  ['Grounding', 'a hard stop; check the joint', 'two feet, usually gentle', 'slides on', 'board swings up'],
  ['On the reference fleet', 'Bavaria 1060, Gib’Sea 31, Sadler 32', 'Moody 33, Sadler 32 (options)', 'Finnsailer 35', 'Sadler 32, Gib’Sea 31 DL (options)'],
])}

{card('hull--fin-keel', 'Fin keel', 'bolted fin, deep or shoal (shallow) fin', 'A single blade of cast iron or lead, bolted to a stub moulded into the hull. The standard arrangement on the Bavaria 1060, the Gib’Sea 31 and the fin-keel Sadler 32, and on almost every production boat since.',
  ['The ballast hangs low on a short keel, so the boat is stiff (resists heeling) for its weight, and the keel behaves like a wing: it makes sideways lift efficiently when the boat moves.', 'A short keel means the boat turns in its own length under engine and steers well going astern (in reverse).'],
  ['Sails closest to the wind and fastest of the four.', 'Most agile in a marina.', 'The keel can be inspected, re-bedded (taken off, cleaned and refitted on fresh sealant) or replaced because it is a separate casting.'],
  ['Deepest draught, so the most places you cannot go and the hardest touch when you do.', 'Less directional stability: the helm needs more attention on a long passage.', 'Cannot dry out without legs (poles clamped to the sides) or a cradle.'],
  ['The “smile”: a crack opening along the front of the keel joint after a grounding (see below).', 'Rust weeping from the joint or the bolt heads.', 'Cracked or debonded floors and grid inside the hull above the keel.'],
  ['Sight along the joint from ahead and astern: it should be a hairline, not a gap.', 'Look inside the bilge over the keel for cracked filler, rust runs and moisture around the nuts.', 'Ask when the keel was last taken off or the bolts inspected, and whether the boat has ever been aground hard.'], fold=True)}

{card('hull--bilge-keels', 'Bilge (twin) keels', 'twin keels', 'Two shorter keels, one each side, angled slightly outwards. Offered on the Moody 33 and the Sadler 32 because so many British boats live in tidal harbours that dry out twice a day.',
  ['Two keels share the ballast and area, so each is shallower. Because they are angled, the leeward keel (the one on the side away from the wind) stands more upright as the boat heels and does more of the work.', 'Standing on both keels with the rudder or a skeg as a third leg, the boat sits level on the mud or sand when the tide goes out.'],
  ['Shallower draught than the same boat with a fin.', 'Dries out upright without legs, so drying moorings (berths that are dry at low water) and half-tide harbours (usable only around high water) are open to you.', 'Grounding is usually a gentle stop on two feet rather than a blow on one.'],
  ['More wetted surface (hull area in the water, which means drag), so slower in light air, and older designs sail noticeably less close to the wind than a fin. Modern twin keels close the gap.', 'When heeled, waves slap under the windward keel and draught actually increases.', 'If one keel finds a hole when drying out the boat can lean over hard.'],
  ['Two keel joints and two sets of bolts to corrode instead of one.', 'Damage to a keel root (where it meets the hull) from taking the ground unevenly.'],
  ['Everything under Fin keel, twice.', 'From astern, check that the two keels are mirror images; one standing at a different angle from the other has had a hard landing.'], fold=True)}

{card('hull--long-keel', 'Long keel', 'full keel', 'The keel runs along most of the underwater length and the rudder hangs at its back end, as on the Finnsailer 35 and most motorsailers. The oldest arrangement and still the most protective.',
  ['Ballast is spread along a long, shallow keel, often moulded into the hull with the metal sealed inside rather than bolted on.', 'The long straight edge resists turning, so the boat holds a course by itself.'],
  ['Tracks like a train: the best for long passages and self-steering.', 'Rudder and propeller are protected behind the keel; it takes the ground and lobster-pot lines gracefully.', 'Shallow draught for its length.'],
  ['Slow to tack (turn the bow through the wind) and poor to windward compared with a fin.', 'Hard to steer in reverse: marina manoeuvres need planning and use of prop walk (the sideways push of the propeller, see the Engine section).', 'Heavy and slow in light air.'],
  ['If the ballast is encapsulated, a grounding can crack the GRP skin and let water reach the metal, which then rusts and swells (see Encapsulated keel).'],
  ['Look for cracks and repairs along the bottom and leading edge of the keel.', 'On the Finnsailer 35 the published data lists the rudder as skeg-hung {ONE}; whether its 1,800 kg of iron ballast is encapsulated or bolted is {TBC}. Check the heel bearing at the bottom of the rudder for play.'], fold=True)}

{card('hull--centreboard', 'Centreboard and lifting keel', 'swing keel, dériveur lesté (French: “ballasted dinghy”)', 'A pivoting board or a lifting fin that retracts into a stub or a case in the cabin. Uncommon in production cruisers of this size because the engineering gets expensive, but the Sadler 32 and the Gib’Sea 31 “DL” were both offered this way.',
  ['A ballasted stub keeps the boat upright; the board adds area for going to windward and is winched or pumped up for shallow water.'],
  ['The shallowest draught of any type: creeks, sills (a step across a harbour entrance that holds water in at low tide) and drying berths that no fin can use.', 'Board up, the boat floats off a beach before a bilge-keeler.'],
  ['The case takes room out of the saloon.', 'A pivot pin, lifting wire, winch or hydraulic ram and seals, all under water, all needing attention.', 'Some designs do not retract fully and still cannot dry out flat.'],
  ['Worn pivot pin and play (loose movement) in the board.', 'Corroded lifting wire.', 'Grounding loads bending the board or cracking the case.'],
  ['Lift and lower the board with the boat out of the water and watch for play, noise or a bent board.', 'Ask when the lifting wire and pivot were last replaced.'], fold=True)}

  <h3>How the keel is attached</h3>
  <p>Almost every fin and bilge keel on this class is a casting bolted to the hull. The joint is the most heavily loaded part of the boat, and the one place where a fault can be fatal. It is worth understanding exactly what is holding the keel on.</p>

{figure('fig-keel-joint', 'keel joint', '0 0 940 330', 'Section through a bolted keel joint, and an encapsulated keel', 'Left, a section along the length of the boat with the bow to the right: the hull laminate with internal floors and a moulded keel stub, a sealant joint, a cast keel below, and keel bolts with nuts and backing plates inside the hull; a crack at the forward end of the joint is marked as the smile, with arrows showing how a grounding levers the keel. Right: an encapsulated keel with the ballast sealed inside the GRP moulding.', g.keel_joint(), 'Bow to the right. Bolted keels can be inspected, re-bedded and replaced; the price is bolts that corrode where you cannot see them. Encapsulated keels have no bolts, but a cracked skin lets water in to the metal.')}

{card('hull--keel-bolts', 'Keel bolts', 'keel studs', 'Threaded rods cast into the keel or bolted through it, passing up through the stub, with nuts and large washers or backing plates inside the bilge. A boat of this size usually has somewhere between six and twelve {TWO}, and they are hidden under filler and bilge paint.',
  ['The bolts clamp the keel to the stub; the sealant between the two keeps water out. Sideways loads from sailing are carried by the joint faces and the floors, and the bolts hold it all together in tension.', 'With an iron keel the bolts are usually galvanised mild steel (ordinary steel with a zinc coating) or stainless; with a lead keel, bronze or Monel (a nickel-copper alloy). Mixing metals badly makes a battery: silicon-bronze bolts in an iron keel corrode the iron around them.'],
  ['A bolted keel can be taken off, inspected and re-bedded by any competent yard.', 'Mild steel corrodes from the outside in: rust on the nuts or weeping at the joint is usually the first sign. But a stud can be necked (thinned) inside the joint while its nut looks clean, so the fifteen-year check still applies.'],
  ['Stainless steel suffers crevice corrosion (a form of rust that starts in tight, wet, airless gaps) in the keel sump, the low point of the bilge where water collects, and can look perfect until it breaks; rust stains around a stainless bolt are a warning, not a cosmetic issue.', 'You cannot see the bolt where it matters, inside the keel and the stub.'],
  ['Corroded or wasted (thinned) bolts; rust runs from the nuts; weeping at the joint.', 'On the Moody 33 the studs are mild steel by design, because the builder distrusted stainless; surface rust on the nuts is common and usually superficial {ONE}. On the Sadler 32 the backing plates are plain or galvanised steel and rust, and owners replace them with stainless {TWO}.'],
  ['Galvanised bolts more than about fifteen years old are due for inspection {TWO}. Where the bolts are removable (bolted through the keel), the simplest check is to withdraw one at a time, look at it and refit it; J-shaped studs cast into a lead keel cannot be withdrawn and need the tests below.', 'Ultrasound from the bolt head finds a corroded or cracked bolt without dismantling anything and works with both iron and lead; X-ray works on iron keels but lead blocks it.', 'A surveyor should sight the joint, tap around the stub and inspect the floors inside.'])}

{card('hull--grounding', 'Grounding damage and the “smile”', 'keel smile, matrix damage', 'When a fin keel hits the bottom at speed the keel is thrown backwards: its aft end drives up into the hull while the front pries down and away. The visible sign is the smile, a crack opening along the forward end of the joint; the invisible sign is cracked or debonded floors and grid inside.',
  ['The keel acts as a lever with the joint as its pivot. Loads that the bolts and floors were never designed for go straight into the hull structure.', 'On boats built from the mid-1980s with a bonded internal grid (a “matrix”, a moulded lattice of ribs glued into the hull instead of laminated in), the grid can crack or tear away from the hull, and a wooden core in the stub can lose its strength if water gets in. Of the reference boats, the 2002 Gib’Sea 33 has a grid bonded in under the cabin sole, with ten keel bolts, according to a magazine test {ONE}; the Moody 33’s builder’s lay-up drawing shows a solid laminate and no grid {ONE}; the others are {TBC}.'],
  ['A smile is easy to see on the hard and is the trigger for a proper inspection.', 'Keel loss is rare: Yachting World counted 72 keel failures worldwide over the thirty years to 2013 {ONE}, against hundreds of thousands of boats.'],
  ['The damage that matters is inside, behind furniture and under the engine, and a boat can look fine from outside.'],
  ['Cracks in the filler at the keel joint, especially forward.', 'Cracked bilge paint, cracked or lifted grid, movement between grid and hull, water in a cored stub.'],
  ['After any grounding, however gentle it felt, look inside over the keel for fresh cracks; after a hard one, lift the boat and have the joint and the structure inspected. The UK Maritime and Coastguard Agency’s guidance note MGN 613 says exactly this for fin-keel GRP yachts, and also recommends an inspection of the keel and its attachment at every annual lift-out.', 'When buying, ask directly whether the boat has been aground and look for repairs around the keel root.'], kind='fault')}

  <div class="callout danger">
    <span class="callout__title">Why this matters</span>
    <p>In May 2014 the yacht <em>Cheeki Rafiki</em>, a 12 m Beneteau First 40.7, lost her keel in the Atlantic and four crew died. The UK Marine Accident Investigation Branch found that the boat had grounded and been repaired more than once and that the internal matrix had detached; it inspected four sister ships that had also grounded and found matrix detachment aft of the keel in each of them. Keel losses on other production yachts have followed the same pattern of hidden structural damage or bolts corroded out of sight. Every grounding is worth an hour with a torch.</p>
  </div>

{card('hull--encapsulated', 'Encapsulated keel', 'moulded-in ballast', 'The hull moulding continues down to form a hollow keel and the ballast, iron or lead, is lowered in and glassed over (sealed under layers of glass and resin) from above. There are no bolts and no joint. Used on the Contessa 32, most Nauticats and many long-keel boats; whether the Finnsailer 35’s iron ballast is encapsulated has not been confirmed {TBC}.',
  ['The ballast sits inside a GRP box that is part of the hull. Loads spread over the whole keel area instead of through a few bolts.'],
  ['Nothing to corrode and nothing to drop off; often described as the strongest way to carry ballast.', 'Takes the ground and lobster-pot lines gently because the keel is part of the hull shape.'],
  ['A grounding that cracks the outer skin lets water reach the ballast. Iron then rusts and swells, and a wet keel is heavy and hard to dry.', 'Cannot be replaced or re-bedded; repairs are laminate repairs.', 'Usually paired with a long or fat keel, so less agile in a marina.'],
  ['Cracks or bulges in the skin along the bottom of the keel.', 'Rust staining bleeding through the antifouling (the paint on the underwater hull, explained below) low on the keel.', 'Damp or free water inside the keel cavity, felt as a cold, wet bilge that never dries.'],
  ['Tap along the keel skin listening for a dull, dead sound and look for repairs at the front and bottom edges.', 'Ask whether the keel has ever been opened.'])}
{sources('keels and keel attachment', [
  'Keel bolt materials: ' + a('https://fairwindfasteners.com/blogs/news/what-kind-of-metal-should-you-use-for-keel-bolts','Fair Wind Fasteners') + ', ' + a('https://www.practical-sailor.com/blog/keel-bolt-inspection-and-repair/','Practical Sailor on inspection and repair') + ', ' + a('https://www.morganscloud.com/2020/06/05/planning-and-budgeting-a-refit-keels-part-2-non-destructive-testing-of-bolts/','Attainable Adventure Cruising on non-destructive testing') + '. The bolt count and the fifteen-year figure are owner and yard rules of thumb, not published specifications.',
  'Moody 33 studs of mild steel: ' + a('https://www.moodyowners.info/threads/moody-keel.20500/','Moody owners’ forum') + ' and ' + a('https://groups.google.com/g/moody-owners-association---americas-chapter/c/XXb2aczhpns','the MOA Americas chapter') + '. Sadler 32 backing plates: ' + a('https://forums.ybw.com/threads/keel-bolt-backing-plate-rust.604178/','YBW forum thread') + ' (anecdotal).',
  'Finnsailer 35 long keel, skeg-hung rudder and iron ballast: ' + a('https://www.listingsport.com/sailboats/finnsailer/35','Listings Port') + ' and ' + a('https://goodoldboat.com/saildata/boat/finnsailer-35/','Good Old Boat sail data') + '; neither says whether the ballast is encapsulated.',
  'The smile and matrix damage: ' + a('https://www.yachtingmonthly.com/gear/7-checks-after-grounding-a-yacht-30650','Yachting Monthly, seven checks after grounding') + ', ' + a('https://sailmagazine.com/diy/how-secure-is-your-keel/','SAIL, how secure is your keel') + '.',
  'Cheeki Rafiki: ' + a('https://www.yachtingmonthly.com/news/cheeki-rafiki-maib-accident-report-published-30655','Yachting Monthly on the MAIB report') + ', ' + a('https://en.wikipedia.org/wiki/Cheeki_Rafiki','Wikipedia') + '. Official guidance: ' + a('https://www.gov.uk/government/publications/mgn-613-m-yacht-and-powerboat-safety-at-sea-grounding-of-fixed-fin-keel-grp-yachts-good-practice','MCA MGN 613 (M)') + '. Keel-failure count and other losses: ' + a('https://www.yachtingworld.com/news/keel-failure-shocking-facts-60006','Yachting World') + ', ' + a('https://www.iims.org.uk/keel-failure-and-capsize-of-charter-yacht-tyger-of-london-maib-report-published/','IIMS on Tyger of London') + '.',
  'Keel types: ' + a('https://www.yachtingmonthly.com/sailing-skills/keel-type-affects-performance-54322','Yachting Monthly on how keel type affects performance') + ', ' + a('https://uk.boats.com/boat-buyers-guide/choosing-a-yacht-bilge-keels-vs-fin-keels/','boats.com on bilge vs fin') + ', ' + a('https://www.rustleryachts.com/keel-design-explained/','Rustler Yachts on keel design') + ', ' + a('https://www.sirius-yachts.com/choosing-the-best-keel/','Sirius Yachts on lifting keels') + '.',
  'Encapsulated keels: ' + a('https://www.jeremyrogers.co.uk/contessa32-specification/','Contessa 32 specification') + ', ' + a('https://www.grabauinternational.com/news/choosing-a-blue-water-yacht-keel-type/','Grabau International') + '. No numerical pointing-angle differences between keel types were found in any source, so none are given.'
])}

  <h3>Rudders</h3>
  <p>The rudder is a foil (a wing-shaped blade) hung under the stern on a shaft called the stock. How it is supported decides how well the boat steers, how it survives a lobster-pot line, and what a surveyor will want to look at. Two words first: a <em>bearing</em> is the bush or ring the stock turns in, and the <em>heel bearing</em> is the one at the very bottom, on a skeg or a keel.</p>

{figure('fig-rudders', 'rudder types', '0 0 900 300', 'Four ways of hanging a rudder', 'Spade rudder on its stock alone with an upper bearing, a lower bearing in the hull skin and a quadrant; skeg-hung rudder supported by a fixed skeg with a heel bearing; keel-hung rudder on the back edge of a long keel with a stock in a tube and a heel bearing; transom-hung rudder on the outside of the stern with pintles, gudgeons and a tiller.', g.rudders(), 'Bow to the right; the dashed line is the waterline. Spade rudders steer best and are the most exposed; skegs protect the blade at some cost in feel; a keel-hung rudder is the most protected and the least nimble; a transom-hung rudder can be lifted off without a lift-out.')}

{compare('Rudder types at a glance', ['', 'Spade', 'Skeg-hung', 'Keel-hung', 'Transom-hung'], [
  ['Steering feel', 'lightest, best astern', 'steady, heavier', 'heavy', 'heavy, direct'],
  ['Protection', 'none', 'skeg takes the knock', 'best', 'exposed at the stern'],
  ['What wears', 'two bearings, the stock', 'heel bearing, skeg root', 'heel bearing, stock tube', 'pintles and gudgeons'],
  ['On the reference fleet', 'Bavaria 1060', 'Moody 33, Sadler 32, Finnsailer 35', 'traditional long-keel boats', 'smaller and older boats'],
])}

{card('hull--spade-rudder', 'Spade rudder', 'balanced rudder', 'A blade held only by its stock, which passes up through the hull in a tube with a bearing at each end. Found on the Bavaria 1060 and on most volume-production boats built since about 1990.',
  ['Part of the blade sits ahead of the stock, so water pressure helps turn it: the rudder is “balanced” and light on the helm.', 'All the load goes into the stock and the two bearings; there is nothing else holding it. On a wheel-steered boat the quadrant, a fan-shaped fitting on top of the stock, is what the steering cables pull on.'],
  ['The most efficient rudder for sailing and manoeuvring; steers well astern.', 'Simple to build and to replace.'],
  ['Everything depends on the stock. A bent stock after hitting something means a new rudder, and the leading edge (the front of the blade) is unprotected against ropes and debris.', 'Bearings wear and the blade develops play.'],
  ['Play at the bearings; a stiff or notchy (catching, uneven) helm from swollen plastic bearings; water inside the blade.', 'Bent stock after a grounding or a collision.'],
  ['With the boat out of the water, push the bottom of the blade sideways: about a millimetre of movement at the bearing is acceptable, more needs investigation {ONE}.', 'Turn the rudder from one stop to the other by hand and feel for tight spots.'], fold=True)}

{card('hull--skeg-rudder', 'Skeg-hung rudder', '', 'The blade hangs behind a fixed fin (the skeg) that is part of the hull moulding, with a bearing at the bottom as well as at the top. The Moody 33, the Sadler 32 and the Finnsailer 35 are built this way.',
  ['The skeg carries the heel bearing, so the stock is supported at both ends and the blade cannot be levered sideways.', 'The skeg also protects the leading edge and gives the boat directional stability.'],
  ['Robust: a knock is taken by the skeg first.', 'Steadier on the helm for a long passage.'],
  ['Only slightly balanced, so heavier to steer and less bite (grip on the water) going astern.', 'A partial skeg, one that covers only the top part of the blade, can be a weak point in itself if it is thin.'],
  ['Wear in the heel bearing at the bottom of the skeg.', 'Cracks where the skeg joins the hull, especially on the Moody 33, where the hull-to-skeg joint needed strengthening on some early boats {TWO}.'],
  ['Check the heel bearing for play and the skeg root for cracks or repairs.', 'Grab the blade and try to rock it: movement means bearing wear.'], fold=True)}

{card('hull--keel-hung-rudder', 'Keel-hung and transom-hung rudders', 'outboard (outside the hull) rudder', 'On a long-keel boat the rudder is hinged along the back edge of the keel: its stock comes up through a tube in the hull and its bottom end sits in a heel bearing on the keel. On smaller and older boats the rudder hangs on the outside of the transom (the flat back of the boat) on simple hinges: pins (pintles) that drop into eyes (gudgeons).',
  ['The keel-hung blade is protected along its whole length by the keel ahead of it.', 'A transom-hung rudder has no stock through the hull at all, so nothing to leak.'],
  ['Very strong and very protected.', 'A transom-hung rudder can be lifted off for repair without lifting the boat out.'],
  ['Unbalanced and heavy on the helm; poor going astern.', 'A transom-hung blade is exposed in a marina and can lift out of the water when the boat heels hard.'],
  ['Worn pintles and gudgeons that let the blade clonk (knock loosely).', 'Corroded fastenings at the transom; a worn heel bearing or stock tube on a keel-hung rudder.'],
  ['Lift the blade and feel for play at each hinge or bearing; check the fastenings inside the transom.'], fold=True)}

{card('hull--rudder-stock', 'Rudder stock, bearings and water in the blade', 'rudder post', 'The stock is the shaft the blade turns on. The blade itself is usually GRP over a foam core, and most of them let water in.',
  ['The stock is stainless steel, or aluminium on many boats built since the 2000s {ONE}, with a web (a flat plate) welded to it inside the blade. It turns in plastic bearings or roller bearings.', 'Water gets into the blade at the stock and along the glued seam between the two halves.'],
  ['A rudder is a bolt-on part: it can be taken off, repaired or replaced without touching the hull.'],
  ['Stainless inside a wet, airless foam core is exactly where crevice corrosion happens, and you cannot see it.', 'Nylon bearings absorb water and swell until they bind; acetal (Delrin) swells much less, and modern polyethylene or Vesconite bushes hardly at all. Roller bearings do not swell but fail suddenly rather than gradually.'],
  ['A German magazine survey found raised moisture in about 70% of the rudders it examined {ONE}. Signs: the blade weeps for weeks after lift-out, sometimes a brown, vinegary fluid; a moisture meter reads wetter than the hull; the blade is heavy.', 'Stiff steering after launch, easing as the bearings settle.'],
  ['Have the blade moisture-metered against the hull at lift-out and look for drips from the bottom edge days later.', 'Ask whether the rudder has ever been dried, drilled or rebuilt. Rinse the lower bearing with fresh water when the boat is out.'])}
{sources('rudders', [
  'Types: ' + a('https://www.pbo.co.uk/boats/do-you-know-your-rudders-71922','Practical Boat Owner, do you know your rudders') + ', ' + a('https://www.grabauinternational.com/news/choosing-a-blue-water-yacht-rudder-type/','Grabau International') + ', ' + a('https://www.morganscloud.com/2013/07/09/spade-rudders-ready-for-sea/','Attainable Adventure Cruising on spade rudders') + '. Bavaria 1060 spade rudder and Finnsailer 35 skeg-hung rudder: ' + a('https://www.listingsport.com/sailboats/bavaria/1060','Listings Port (Bavaria)') + ', ' + a('https://www.listingsport.com/sailboats/finnsailer/35','Listings Port (Finnsailer)') + '.',
  'Stocks and bearings: ' + a('https://jefa.dk/rudder-stock-materials/','Jefa on stock materials') + ', ' + a('https://www.proboat.com/2018/07/the-rudimentaries-of-rudders/','Professional BoatBuilder') + ', ' + a('https://uk.boats.com/how-to/how-to-replace-rudder-bearings/','boats.com on replacing bearings (the 1 mm play figure)') + ', ' + a('https://www.jefa.com/maintenance/maintenance.htm','Jefa maintenance') + '.',
  'Water in rudders: ' + a('https://www.yacht.de/en/repair/rudder-repair-new-rudder-blade-or-is-it-worth-repairing/','YACHT magazine (the 70% figure)') + ', ' + a('https://www.yachtingmonthly.com/gear/keeping-your-boat-afloat-how-to-find-and-fix-hull-moisture-97258','Yachting Monthly on finding hull moisture') + '.',
  'Moody 33 skeg joint: ' + a('https://forums.ybw.com/threads/moody-33-333-33s.5707/','YBW forum thread') + ' (anecdotal; also cited in the fleet section).'
])}

  <h3>Osmosis</h3>
  <p>Osmosis is the word every buyer of an old GRP boat learns first and understands least. It is water getting into the laminate and reacting with the resin, and it shows itself as blisters below the waterline. Ugly, often expensive, and rarely dangerous.</p>

{figure('fig-osmosis', 'osmosis section', '0 0 900 310', 'How an osmosis blister forms', 'Magnified section with sea water above the gelcoat; water molecules pass through the gelcoat into voids in the laminate, where they react with resin to form an acidic fluid that draws in more water and lifts the gelcoat into a blister.', g.osmosis(), 'Osmosis needs three things: a gelcoat that lets water through, voids in the laminate for it to collect in, and uncured resin for it to react with. Boats built with cheap polyester in the 1970s and 1980s have all three.')}

{card('hull--osmosis', 'Osmosis', 'blistering, “boat pox”', 'Gelcoat is not waterproof, only water-resistant. Over years, water molecules pass through it into the tiny voids and dry fibres that every hand-laid hull contains, where they react with leftover chemicals in the resin to make an acidic fluid rich in glycol (an alcohol-like by-product of the resin). That fluid pulls in more water by osmosis, the pressure rises, and the gelcoat lifts into a dome.',
  ['Blisters range from pinheads in the antifouling to coins and saucers in the gelcoat; when they are pierced they weep a sour-smelling fluid.', 'Almost all 1970s hulls have some blistering, and boats from around 1980 to 1990 are reported to be the most prone {TWO}; from the late 1980s builders moved to more water-resistant isophthalic resins, and a well-built hull from the 1990s rarely blisters.'],
  ['In most cases it is cosmetic: no yacht is known to have sunk from osmosis, and a blistered hull has usually been blistered for years.', 'Properly treated, with the hull dried first, an epoxy barrier usually cures it permanently.'],
  ['Advanced cases can degrade the laminate itself, and a heavily hydrolysed hull (one where the resin has broken down) is genuinely weaker.', 'Treatment is expensive and slow, and a poor treatment (epoxy over a wet hull) makes things worse.'],
  ['Blisters, usually found at the spring lift-out.', 'High moisture readings. Surveyors use meters such as the Sovereign and the Tramex; the numbers are not comparable between meters, and what matters is the difference between the underwater hull and a dry reference such as the topsides. Most surveyors admit the meter alone cannot predict blistering that has not yet appeared {ONE}.'],
  ['Look at the hull the day it comes out, before it dries, and again a week later.', 'A full treatment means peeling off the gelcoat, drying the hull (weeks in a shed, or one to two weeks with heated vacuum “hot-vac” panels), filling, and coating with epoxy (a tougher, more waterproof resin than the polyester the boat was built with). A UK yard quoted about £6,000 for a 10 m boat in 2005, and forum reports since then run at £5,000 to £7,000 and more {TWO}; prices vary by yard and year, so get a written quote, and ask for a written moisture record before the epoxy goes on.'], kind='fault')}
{sources('osmosis', [
  'Mechanism: ' + a('https://www.sea-help.eu/en/guide/gfk-polyester-osmosis-boat-hull/','SeaHelp guide') + ', ' + a('https://www.yachtsurveyors.co.uk/what-is-osmosis/','yachtsurveyors.co.uk') + ', ' + a('https://mast.tas.gov.au/wp-content/uploads/2020/06/Osmosis.pdf','Marine and Safety Tasmania') + ', ' + a('https://wiki.westerly-owners.co.uk/index.php?title=Osmosis','Westerly Owners wiki') + '.',
  'Which years are worst: ' + a('https://www.bmse.co.uk/articles/article4/','BMSE surveyors') + ' and ' + a('https://forums.ybw.com/threads/osmosis-the-truth.332631/','a YBW thread, “Osmosis, the truth”') + ' (anecdotal); the resin history is in the construction sources above.',
  'Detection and meters: ' + a('https://www.practical-sailor.com/boat-maintenance/moisture-meters-can-you-trust-them-we-test-five-models/','Practical Sailor moisture-meter test (the surveyors’ admission)') + ', ' + a('https://tramexmeters.com/learn/moisture-testing/boat-and-hull-surveys','Tramex on hull surveys') + '. Meter scales differ, so no single “threshold” reading is published here.',
  'Danger: ' + a('https://www.pbo.co.uk/expert-advice/osmosis-on-a-boat-will-it-cause-my-vessel-to-sink-84113','Practical Boat Owner, will osmosis sink my boat') + ', ' + a('https://www.craftinsure.com/blog/boat-osmosis/','Craftinsure') + '.',
  'Treatment and drying: ' + a('https://www.pbo.co.uk/expert-advice/osmosis-the-professional-treatment-26525','PBO, the professional treatment (about £6,000 for a 32-footer in 2005)') + ', ' + a('https://www.pbo.co.uk/expert-advice/diy-osmosis-repair-26475','PBO, DIY osmosis repair') + ', ' + a('https://marinesurveyor.com/hot-vac-a-real-cure-for-osmosis/','marinesurveyor.com on Hot-Vac') + ', ' + a('https://www.ukyachtsurveyors.com/article/osmosis-and-moisture-readings','UK Yacht Surveyors on moisture readings before epoxy') + '. Later forum quotes of £5,000–7,000 are anecdotal.'
])}

  <h3>Through-hulls and seacocks</h3>
  <p>A cruising boat of this size has several holes below the waterline: engine cooling water in, sinks and toilet in and out, the log (the speed sensor, a little paddle wheel) and the depth sensor, cockpit drains. Each has a fitting through the hull and, on anything modern, a valve on top of it. Knowing where every one is, and being able to shut it in the dark, is the first thing a new owner should learn.</p>

{figure('fig-seacock', 'seacock section', '0 0 900 330', 'A through-hull fitting and its seacock in section', 'Section through the hull: a threaded skin fitting with a flange outside, a backing pad inside, a seacock valve with its handle in line with the pipe (open), a hose tail with two hose clips, a reinforced hose leading away, and a softwood bung tied to the valve.', g.seacock(), 'Skin fitting, valve, hose tail, two clips, good hose: five parts, and every one of them has sunk a boat. The bung is for the day the metal lets go.')}

{card('hull--seacock', 'Skin fittings and seacocks', 'through-hulls, sea valves', 'The skin fitting is a threaded tube with a flange (a rim) that sits on the outside of the hull. The seacock is the valve screwed onto it inside. What they are made of decides how long they last, and how they are made decides how they fail.',
  ['<strong>Ball valves</strong>, a quarter turn from open to shut, are what almost every boat built since the 1990s has. <strong>Tapered-plug cocks</strong> (Blakes is the British make) are the traditional bronze type, screwed to the hull through a flange; they need dismantling and greasing every year, and lapping in (grinding the plug to its seat) when they weep, which is the one seacock job a Moody 33 or Sadler 32 owner will actually do. <strong>Gate valves</strong>, with a wheel you wind, are plumbing parts that should not be on a boat: they jam and you cannot see whether they are shut.', 'Bronze, an alloy of copper and tin, is the traditional material and lasts for decades in sea water. DZR brass (“dezincification-resistant”) is a cheaper copper-zinc alloy with a little arsenic added so the zinc does not leach out; many European boats built since the 1990s have it. Ordinary brass loses its zinc in sea water, turns pink and crumbly, and can fail in under five years. Composite fittings (glass-reinforced nylon such as TruDesign or Marelon) cannot corrode at all.'],
  ['A good bronze or composite seacock is a fit-and-forget item.', 'A ball valve is quick: a quarter turn shuts it.'],
  ['The standard boats of the 1990s and 2000s were built to, ISO 9093-1:1994, permitted brass and asked only for a five-year corrosion life, which is why so many boats of that era were fitted with valves that are now overdue {ONE}. It was replaced by ISO 9093:2020, which does not help boats already built.', 'Metal fittings need a bonding wire or an anode if stray currents (leaking electricity from the boat’s own wiring or the marina) are present; composite ones do not, but they are bulkier.'],
  ['Dezincification: pink patches, a crumbly surface, a handle that will not move.', 'Seized valves that have not been turned in years; rusted hose clips; perished (cracked, rotten) hose; a fitting bedded straight onto a thin hull without a backing pad.'],
  ['Turn every seacock at least once a season and leave the toilet and sink ones shut when you leave the boat.', 'At lift-out scrape a spot on each skin fitting: bright yellow is healthy, pink is dying. An unmarked yellow-metal fitting should be assumed to be plain brass unless it is stamped CR (corrosion-resistant) or DZR. Replace brass on sight and DZR or bronze on condition (when inspection shows it is going); no fixed interval is published.', 'Two stainless clips on every hose, and a tapered softwood bung of the right size tied to each valve.'])}
{sources('seacocks', [
  'Materials and types: ' + a('https://www.pbo.co.uk/gear/skin-fittings-and-seacocks-explained-97286','Practical Boat Owner, skin fittings and seacocks explained') + ', ' + a('https://www.pbo.co.uk/gear/dezincification-resistant-dzr-skin-fittings-explained-97302','PBO on DZR') + ', ' + a('https://www.pbo.co.uk/expert-advice/what-are-the-different-types-of-seacock-and-when-should-i-replace-them-71224','PBO on the types of seacock') + ', ' + a('https://www.yachtingmonthly.com/gear/seacock-misconceptions-busted-79012','Yachting Monthly, seacock misconceptions') + ', ' + a('https://sailmagazine.com/diy/know-how-thru-hulls-and-seacocks/','SAIL on composite fittings') + '.',
  'ISO 9093-1 and the five-year clause: ' + a('https://www.europarl.europa.eu/doceo/document/E-7-2012-005075_EN.html','European Parliament written question E-005075/2012') + '. ISO 9093:2020 is the current edition (' + a('https://www.iso.org/search.html?q=ISO%209093','ISO catalogue search') + ').',
  'Practice: ' + a('https://www.safe-skipper.com/seacock-maintenance/','Safe Skipper') + ', ' + a('https://www.yachtingmonthly.com/archive/essential-seacock-checks-4692','Yachting Monthly, essential seacock checks') + '.'
])}

  <h3>Antifouling and anodes</h3>
  <p>Two things go on the underwater hull every year: paint that stops weed and barnacles, and lumps of metal that corrode so that your propeller, shaft and saildrive leg do not.</p>

{card('hull--antifouling', 'Antifouling paint', 'bottom paint', 'A paint that slowly releases a biocide (a substance that kills growth), almost always copper since tin was banned, so that weed and barnacles cannot settle. It is renewed every year or two, and the rules on what you may use now differ from sea to sea.',
  ['<strong>Eroding (self-polishing)</strong> paints wear away in use, exposing fresh biocide: the usual choice for a cruising boat that moves.', '<strong>Hard</strong> paints leach biocide from a solid film that can be scrubbed and takes drying out: for fast boats and drying moorings.', '<strong>Copper-loaded epoxy</strong> (Coppercoat is the best-known) is applied once and lasts many seasons {ONE}.', '<strong>Biocide-free</strong> silicone or hard slippery coatings rely on growth not gripping; growing in importance as the rules tighten.'],
  ['A clean bottom is worth half a knot and a happier engine.', 'Modern eroding paints need no sanding between coats.'],
  ['Copper is a poison: authorities are restricting it, some marinas forbid scrubbing the hull while the boat is in the water, and the washing-down water must be collected rather than run into the sea in many yards.', 'The wrong paint on an aluminium saildrive leg (the underwater part of a saildrive engine, see the Engine section) corrodes it; use a copper-free product there.'],
  ['Heavy fouling from a paint that was not authorised for your water, or that was applied over a slippery old coat.', 'Flaking where too many seasons have built up.'],
  ['Check the rules for the water you keep the boat in before buying paint (table below).', 'Scrape a small patch at lift-out to see how many layers are on the hull; a thick, cracked build-up should be taken back to the gelcoat.'])}

  <details class="more more--table">
    <summary>Antifouling rules by sea and country (open the table)</summary>
    <div class="more__body">
  <div class="table-wrap">
    <table class="spec regs">
      <thead><tr><th>Where you keep the boat</th><th>What the rules say</th><th>What it means in practice</th></tr></thead>
      <tbody>
        <tr><th>All EU waters</th><td>Antifoulings are biocidal products under EU Regulation 528/2012 and need national authorisation in each country. Tin-based (TBT) paint was banned on boats under 25 m in France in 1982 and the UK in 1987 {ONE}, across the EC by a 1989 directive, and on all ships worldwide by the IMO: no new application from 2003, and none left on a hull from 2008. Cleaning a biocidal paint in the water is prohibited, or allowed only if the debris is collected, in most member states.</td><td>Buy paint sold in the country where the boat lives. Do not scrub a copper paint in the water in a marina.</td></tr>
        <tr><th>Baltic: Sweden</th><td>The chemicals agency KEMI approves paints by zone: only low-leach products on the east coast (the Baltic proper); no biocidal paint at all in the Gulf of Bothnia north of Örskär or in fresh water.</td><td>A boat moved from the west coast or from abroad may be wearing a paint that is not allowed. Many clubs use hull-washing pads instead.</td></tr>
        <tr><th>Baltic: Finland</th><td>Authorised only for sea areas, for boats over 7 m and up to 24 m {ONE}, with a capped copper release rate; forbidden in fresh water and inland waters.</td><td>Marine use is fine with an authorised product; lakes are paint-free.</td></tr>
        <tr><th>Baltic: Denmark</th><td>Biocidal antifouling is banned for boats mainly used in fresh water and for small craft under 200 kg in salt water; from 2025 private misuse can be fined; regional product lists apply and in-water cleaning needs collection of the debris and a permit.</td><td>A 5-tonne yacht in salt water may still use an approved product; check the current list.</td></tr>
        <tr><th>Baltic and North Sea: Germany</th><td>Only products approved by the federal authority BAuA may be used; no zoning, but the environment agency advises against any biocidal paint inland.</td><td>Straightforward on the coast; think twice on the lakes and canals.</td></tr>
        <tr><th>North Sea: Netherlands</th><td>Only Ctgb-authorised products, with copper content limited; inspectors now measure copper on hulls in the water and can order removal and fine the owner {TWO}.</td><td>Applies to boats with a Dutch home port. Keep the paint can and the receipt.</td></tr>
        <tr><th>North Sea and Channel: United Kingdom</th><td>The GB biocides regime, run by the Health and Safety Executive, separates amateur from professional-only products; the MCA’s guidance for pleasure vessels covers antifouling in MGN 599 {ONE}.</td><td>Amateur products are fine to apply yourself; some strong paints are professional-only.</td></tr>
        <tr><th>Channel: France</th><td>EU rules apply, with French authorisation of each product. Scraping, washing or painting a hull outside an approved careening area, with its wash-water treatment, is an offence {ONE}.</td><td>Use a product authorised in France.</td></tr>
        <tr><th>Mediterranean and Adriatic: Croatia, Greece, Italy, Spain</th><td>EU rules apply; no additional national zone rules were found {TBC}. Marina rules on collecting wash-down water and on in-water cleaning are common.</td><td>Ask the yard before you scrub or pressure-wash.</td></tr>
        <tr><th>Mediterranean and Black Sea: Turkey</th><td>The international ban on tin applies, and antifouling products fall under Turkey’s biocidal products regulation of 2009.</td><td>Confirm locally before lifting out or recoating.</td></tr>
        <tr><th>Black Sea: Bulgaria, Romania</th><td>EU rules apply; no additional national rules were found {TBC}.</td><td>Use a product authorised in the country.</td></tr>
      </tbody>
    </table>
    <p class="table-note">Rules change every few years and the copper actives (the active ingredients) are currently approved in the EU only until mid-2028; check the national authority before buying paint. Rows marked TBC are where no country-specific rule was found by search, not proof that none exists.</p>
  </div>
    </div>
  </details>

{card('hull--anodes', 'Sacrificial anodes', 'zincs', 'Lumps of a metal more willing to corrode than your shaft, propeller or saildrive leg, bolted on so that they dissolve instead. Which metal depends on the water.',
  ['Two different metals in sea water connected by a wire make a battery, and the less noble one (in plain words, the one that corrodes more easily) dissolves. An anode is deliberately the least noble metal on the boat.', 'It only protects what it is electrically connected to: bolted directly to the shaft or leg, or joined by a bonding wire inside the boat. Keel bolts, buried in the keel and the stub, are not normally bonded and are not protected by a hull anode.'],
  ['Cheap insurance for a propeller and shaft, and essential for an aluminium saildrive leg.'],
  ['The wrong metal either does nothing or vanishes in weeks.', 'Anodes that are painted over, or fitted to metal that is not bonded, protect nothing.'],
  ['An anode that is still shiny after a season is not working; one that is gone after three months means a stray-current or bonding problem.', 'Magnesium anodes used in sea water are consumed very quickly {TWO}.'],
  ['<strong>Sea water:</strong> zinc, or aluminium alloy, which lasts longer for the same size. <strong>Brackish water</strong> (part salt, part fresh) such as the Baltic: aluminium; one popular guide recommends magnesium, but the engine makers’ guidance is that magnesium is for fresh water only {TWO}. <strong>Fresh water:</strong> magnesium.', 'Fit anodes big enough that they are no more than about half consumed at the end of the season, and never mix anode metals on one bonding system.'])}
{sources('antifouling and anodes', [
  'Types: ' + a('https://www.pbo.co.uk/expert-advice/what-is-antifouling-paint-why-antifoul-your-boat-71638','Practical Boat Owner, what is antifouling') + ', ' + a('https://www.international-yachtpaint.com/sg/en/boat-paint-help/expert-advice/types-of-antifouling','International Paint, types of antifouling') + ', ' + a('https://coppercoat.com/coppercoat-leisure-antifoul-applications/what-is-coppercoat/faqs/','Coppercoat FAQ') + '.',
  'EU and international rules: ' + a('https://eur-lex.europa.eu/eli/reg/2012/528/oj/eng','Regulation (EU) 528/2012') + ', ' + a('https://www.emsa.europa.eu/protecting-the-marine-environment/anti-fouling.html','EMSA on the TBT ban') + ' (ships, AFS Convention in force 2008), ' + a('https://www.nautix.com/en/antifouling-regulations/','Nautix summary of regulations') + ', ' + a('https://www.sea-help.eu/en/news-general/biocide-antifouling-regulations/','SeaHelp on biocide regulations') + '. Small-craft TBT bans: ' + a('https://www.legislation.gov.uk/uksi/1987/783','the UK Control of Pollution (Anti-Fouling Paints and Treatments) Regulations 1987, SI 1987/783') + ' and ' + a('https://eur-lex.europa.eu/eli/dir/1989/677/oj','Council Directive 89/677/EEC') + ', which restricted organotin paints to vessels over 25 m; neither text could be fetched from this environment, so the mark stays until they are checked.',
  'Grid, cores and national rules (opened September 2026): ' + a('https://sailingmagazine.net/article-permalink-453.html','Sailing Magazine, Gib’Sea 33 test (2002)') + ', ' + a('https://moodyowners.org/wp/princess-records/Moody%2033/dwg%20Moody%2033%20-%20hull%20layup.pdf','Moody 33 hull lay-up drawing') + ' (PDF, Moody Owners Association), ' + a('https://finnsailer35.wordpress.com/finnsailer-35-information/','Finnsailer 35 owners’ site') + ', ' + a('https://www.imo.org/en/OurWork/Environment/Pages/Anti-fouling.aspx','IMO, anti-fouling systems') + ', ' + a('https://www.resmigazete.gov.tr/eskiler/2009/12/20091231m4-11.htm','Resmî Gazete, biocidal products regulation (2009)') + ', ' + a('https://www.coastalwiki.org/wiki/TBT_and_Imposex','Coastal Wiki, TBT and imposex') + ' (France, 1982); the French careening offence and the UK’s 1987 date from search results only.',
  'Sweden: ' + a('https://www.kemi.se/en/chemicals-in-our-everyday-lives/advice-on-chemicals-in-your-home/anti-fouling-paints/map-over-areas-where-different-types-of-anti-fouling-paints-are-allowed-to-use','KEMI zone map') + ', ' + a('https://www.transportstyrelsen.se/sv/sjofart/Fritidsbatar/Batliv-miljo/batbotten/regler-om-batbottenfarg/','Transportstyrelsen') + '. Finland: ' + a('https://tukes.fi/en/chemicals/biocides/national-authorisation-conditions-for-biocidal-products/authorisation-conditions-for-biocidal-antifouling-products-used-on-boats','Tukes authorisation conditions') + ' (the 7 m lower limit appears in Tukes’ conditions and has not been cross-checked elsewhere). Denmark: ' + a('https://eng.mst.dk/chemicals/biocides/legislation/statutory-order-restricting-the-import-sale-and-use-of-biocidal-anti-fouling','Danish EPA statutory order') + ', ' + a('https://www.yacht.de/en/diy/care/denmark-partial-ban-on-antifouling-paints-containing-biocides-update/','YACHT on the 2025 update') + '. Germany: ' + a('https://www.umweltbundesamt.de/themen/chemikalien/biozide/biozidprodukte/antifouling-mittel/antifouling-im-wassersport-tipps-umweltschonenden','Umweltbundesamt') + '. Netherlands: ' + a('https://www.yacht.de/en/the-netherlands/environmental-protection-netherlands-also-checks-antifouling-in-the-water/','YACHT on Dutch in-water checks') + ', ' + a('https://www.rivm.nl/bibliotheek/rapporten/2018-0086.pdf','RIVM report') + '. UK: ' + a('https://classicsailor.com/2018/09/antifouling-paints-and-the-biocidal-products-regulation/','Classic Sailor on the BPR') + ', ' + a('https://www.rya.org.uk/regulations/pleasure-craft-regulations/','RYA pleasure craft regulations') + '.',
  'Anodes: ' + a('https://www.yachtingmonthly.com/gear/guide-aluminium-anodes-70157','Yachting Monthly guide to aluminium anodes') + ', ' + a('https://www.pbo.co.uk/expert-advice/boat-anodes-a-practical-guide-for-sailors-85933','Practical Boat Owner anode guide (the one recommending magnesium for brackish water)') + ', ' + a('https://www.boatzincs.com/volvo-penta-saildrive-magnesium.html','Volvo Penta saildrive anode listing (magnesium marked fresh water only)') + ', ' + a('https://www.proboat.com/2015/04/the-mysteries-of-bonding-systems-revealed/','Professional BoatBuilder on bonding') + '.'
])}
{photo('hull-worn-shaft-anode.jpg', 'A heavily corroded anode clamped on a propeller shaft, against the red antifouling of the hull', 'A shaft anode that has done its job: most of it has corroded away and the shaft is untouched. Replace it before it is gone.', 'Springnuts', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0', 'https://commons.wikimedia.org/wiki/File:2022-01-18_sacrificial_galvanic_anode.jpg', 1280, 960)}

  <h3>The deck: core and joints</h3>
{card('hull--deck-core', 'Cored deck and core rot', 'soft deck, balsa rot', 'Decks and coachroofs (the raised cabin top) on this class are almost all sandwiches: a thin outer skin, a core of end-grain balsa or plywood, a thin inner skin. Stiff and light, until water gets into the core. Owners describe balsa-cored decks on the Sadler 32 and the Moody 33, the Moody with plywood under the chainplates, though one database lists the Moody 33S deck as single-skin {TWO}; the Bavaria 1060 has a sandwich deck of unstated core {ONE}; the Finnsailer 35’s hull and superstructure are solid GRP with no core, according to an owners’ site quoting its Lloyd’s build description {ONE}; the Gib’Sea 31 is {TBC}.',
  ['The two skins carry the loads and the core keeps them apart, the way the top and bottom flanges of a steel I-beam do the work and the thin web between them just holds them apart.', 'Every bolt through the deck passes through the core. When the sealant under the fitting fails, water follows the bolt into the core, and balsa soaks it up like a sponge; plywood wicks along the grain and delaminates (its layers come apart).'],
  ['A sound cored deck is stiffer and lighter than a solid one and does not sweat inside.'],
  ['Wet core is invisible from outside for years.', 'Repair means cutting a skin off, replacing the core and re-laminating: cheap materials, expensive labour.'],
  ['Soft, springy spots when you walk, usually around stanchion bases (the posts for the guard wires), chainplates (where the rigging wires anchor to the hull), the mast step, windlass and cleats.', 'Staining and drips on the cabin ceiling; weeping around bolt heads inside lockers; fittings that keep coming loose.'],
  ['Walk the whole deck in bare feet and press hard around every fitting.', 'Tap with a small plastic hammer: crisp is sound, dull is delaminated. A surveyor will add a moisture meter and sometimes an infrared camera; none of the three is foolproof on its own.', 'When re-bedding a fitting (taking it off and refitting it on fresh sealant), drill the holes oversize, fill them with epoxy and re-drill, so the core is sealed from the bolt for good.'], kind='fault')}
{sources('decks', [
  'Core materials and detection: ' + a('https://canadianboating.ca/tech/maintenance/cored-deck-repair/','Canadian Boating on cored deck repair') + ', ' + a('https://www.practical-sailor.com/boat-maintenance/the-multipurpose-core/','Practical Sailor on cores') + ', ' + a('https://www.cruisingworld.com/how-to/deck-repair-tips-sailboat/','Cruising World deck repair tips') + '.',
  'Repair: ' + a('https://www.epoxyworks.com/replacing-damaged-balsa-core/','Epoxyworks on replacing balsa core') + ', ' + a('https://www.practical-sailor.com/boat-maintenance/step-by-step-core-panel-fix/','Practical Sailor step-by-step panel fix') + '. No UK or EU cost bands were found; forum figures of two to three shop hours per 0.1 m² are anecdotal.',
  'Reference boats: Moody and Sadler decks from owners’ reports and the sources under each boat in the ' + a('#fleet','Fleet section') + ' (a class-association sheet cited here earlier turned out to describe the Moody 42, and was dropped); Bavaria 1060 sandwich deck per ' + a('https://www.listingsport.com/sailboats/bavaria/1060','Listings Port') + ' (single source).'
])}

  <h3 id="hull--checklist">The hull in one afternoon: a buyer’s checklist</h3>
  <ol>
    <li><strong>Walk round twice.</strong> First for the shape: sight along the topsides for flats and bumps from repairs, and along the keel joint from ahead and astern. Then for the surface: blisters, crazing, repairs, rust runs.</li>
    <li><strong>Keel.</strong> Joint hairline or smile? Rust at the joint? Inside, over the keel: cracked filler, wet nuts, cracked or lifted grid.</li>
    <li><strong>Rudder.</strong> Rock it for play, turn it for stiffness, look for drips from the bottom edge and cracks at the skeg root.</li>
    <li><strong>Every hole.</strong> Count the skin fittings outside, then find each seacock inside. Scrape, turn, look at the hose and the clips.</li>
    <li><strong>Deck.</strong> Bare feet and a plastic hammer around every fitting; ceiling and lockers for stains.</li>
    <li><strong>Ask three questions.</strong> Has she been aground? When were the keel bolts last looked at? When was she last metered for moisture, and what did it read against the topsides?</li>
    <li><strong>Then pay a surveyor.</strong> Out of the water, chosen by you. This list is for deciding which boats are worth the survey fee.</li>
  </ol>

  <h3>Worth watching</h3>
{videos([
 ('BJdohigH53A', 'Simple explanation of how to find GRP delamination with a hammer', 'The Marine Surveyor Notebook. Ben Sutcliffe marine', 'A marine surveyor tapping a hull with a ball-pein hammer, and what the different sounds mean.'),
 ('-3pxXF-6ud0', 'How to prevent osmosis blisters on your yacht hull', 'practicalboatowner', 'Why GRP hulls blister, and what owners can do about it.'),
 ('sF_xjbbJYZ0', 'Hammer test hull inspection', 'Sea Conquest Marine Surveys & Consultancy', 'A second surveyor’s hammer test, looking for soft spots and delamination.'),
])}

  <h3>Terms used in this section</h3>
  <h4 class="terms__group">Construction</h4>
{terms([
 ("gelcoat","Gelcoat","The coloured resin skin on the outside of a GRP moulding, a fraction of a millimetre thick, sprayed into the mould first. It gives the shine and most of the water resistance."),
 ("laminate","Laminate","The layers of glass fibre and resin behind the gelcoat that form the actual structure."),
 ("hull-laminate","Hull","The watertight shell of the boat. On this class a solid GRP laminate, thickest at the keel and thinnest in the topsides."),
 ("csm","Chopped-strand mat (CSM)","A felt of short glass fibres that soaks up resin and follows curves. Bulk and shape rather than strength."),
 ("woven-roving","Woven roving","A heavy woven glass cloth laid between layers of mat for strength."),
 ("resin","Resin","The liquid plastic that soaks the glass and sets hard. Polyester on all boats of this class; generally the cheap orthophthalic type until the 1980s and the more water-resistant isophthalic type afterwards, though some builders changed later; vinylester and epoxy are better still and dearer."),
 ("core","Core","The light filling, usually end-grain balsa or plywood, between the two skins of a sandwich deck."),
 ("outer-skin","Outer skin","The GRP layer on the weather side of a deck core. With the inner skin and the core it acts like a beam."),
 ("inner-skin","Inner skin","The GRP layer on the cabin side of a cored deck, usually thinner than the outer one."),
 ("deck-fitting","Deck fitting","Anything bolted through the deck: stanchion bases, cleats, tracks, the windlass. Each bolt hole is a path for water into the core unless it is sealed."),
 ("bedding","Bedding (sealant bed)","The flexible sealant under a deck fitting or skin fitting that keeps water out. It ages and must be renewed; owners talk of ten to twenty years, but there is no fixed life."),
 ("core-rot","Core rot","Wet, soft or rotten core inside a deck sandwich, felt as a springy deck."),
 ("backing-plate","Backing plate","A metal or plywood plate inside the boat that spreads the load of a bolted fitting over the laminate."),
 ("stringers","Stringers","Lengthwise ribs bonded inside the hull to stiffen the skin; floors run across, stringers run fore and aft."),
 ("print-through","Print-through","The weave of the cloth showing faintly through the gelcoat. Cosmetic."),
 ("crazing","Crazing","A web of fine cracks in the gelcoat only, at a hard spot or an old impact. Cosmetic, unlike a deep crack into the laminate."),
 ("hard-spot","Hard spot","A place where a bulkhead or fitting stops the hull flexing, so the gelcoat cracks there first."),
 ("hull-deck-joint","Hull-to-deck joint","Where the deck moulding meets the hull moulding, usually on an inward flange, bedded and bolted. The hardest leak on the boat to find."),
 ("flange","Flange","A lip or rim: on the hull, the inward ledge the deck sits on; on a skin fitting, the rim that sits against the outside of the hull."),
])}
  <h4 class="terms__group">Keel</h4>
{terms([
 ("fin-keel","Fin keel","A single short, deep keel bolted to the hull."),
 ("bilge-keels","Bilge keels","Two shallower keels, one each side, so the boat can dry out standing on them."),
 ("long-keel","Long keel","A keel that runs along most of the hull with the rudder hung at its back end."),
 ("centreboard","Centreboard","A board that swings or lifts up into a case or a ballasted stub to reduce draught."),
 ("keel-stub","Keel stub","The shallow moulded extension of the hull that a bolted keel is fastened to."),
 ("keel-casting","Keel casting","The cast-iron or lead keel itself. Iron is cheaper and rusts; lead is denser, softer and dearer."),
 ("keel-bolts","Keel bolts","The threaded rods that hold a bolted keel to the stub, with nuts inside the bilge."),
 ("keel-joint","Keel joint","The sealed face between keel and stub. A hairline when healthy."),
 ("keel-smile","The smile","A crack opening at the forward end of the keel joint after a grounding."),
 ("floors","Floors and grid","The internal ribs across the bottom of the hull that spread keel loads; on boats built since the mid-1980s often a bonded-in moulded grid, the matrix."),
 ("encapsulated-keel","Encapsulated keel","Ballast sealed inside the hull moulding, with no bolts."),
 ("grounding","Grounding","Touching the bottom. Gentle groundings are part of sailing; a hard one at speed is a structural event for a fin keel."),
 ("dry-out","Drying out","Sitting on the seabed as the tide goes out. Bilge keels stand up by themselves; a fin keel needs legs, a cradle or a wall to lean on."),
 ("lift-out","Lift-out and “on the hard”","Craning the boat ashore; a boat on the hard stands on props (supports), in a cradle or on a trailer. The only time the keel, rudder and skin fittings can be inspected properly."),
])}
  <h4 class="terms__group">Rudder</h4>
{terms([
 ("spade-rudder","Spade rudder","A rudder blade held only by its stock."),
 ("skeg-rudder","Skeg-hung rudder","A rudder supported at the bottom by a fixed fin, the skeg."),
 ("skeg-hull","Skeg","A fixed fin moulded into the hull just ahead of the rudder, carrying the heel bearing and protecting the blade."),
 ("keel-hung-rudder","Keel-hung rudder","A rudder hinged on the trailing (back) edge of a long keel, with its stock in a tube and its heel in a bearing on the keel."),
 ("transom-rudder","Transom-hung rudder","A rudder hung on the outside of the stern on pintles and gudgeons."),
 ("rudder-stock","Rudder stock","The shaft the rudder blade turns on, stainless steel or aluminium."),
 ("rudder-bearings","Rudder bearings","The bushes the stock turns in: plastic or roller. Play here is felt as a clonk at the wheel."),
 ("heel-bearing","Heel bearing","The bearing at the very bottom of a skeg-hung or keel-hung rudder, where the blade’s heel sits on the skeg or keel."),
 ("quadrant","Quadrant","The fan-shaped fitting on top of the stock that the steering cables pull on; on a tiller boat, the tiller head does the job."),
 ("pintle","Pintles and gudgeons","The pins and eyes that hinge a transom-hung rudder: the pintle is the pin, the gudgeon the eye it drops into."),
 ("gudgeon","Gudgeon","The eye half of a rudder hinge; the pintle is the pin."),
 ("tiller","Tiller","A lever fixed straight onto the rudder stock, the simplest steering there is."),
 ("crevice-corrosion","Crevice corrosion","Corrosion of stainless steel that starts in tight, wet gaps starved of oxygen: under a washer, inside a rudder, in a keel sump. Invisible until it fails."),
])}
  <h4 class="terms__group">Osmosis</h4>
{terms([
 ("osmosis","Osmosis","Water passing through the gelcoat into the laminate and reacting with the resin to form blisters."),
 ("blister","Blister","A dome in the gelcoat raised by fluid underneath. Pierce one and it weeps a sour liquid."),
 ("void","Void","A tiny air pocket or dry patch in the laminate where water can collect."),
 ("permeation","Permeation","Water molecules passing slowly through a coating that is water-resistant but not waterproof."),
 ("hydrolysis","Hydrolysis","The chemical reaction between water and polyester resin that makes the acidic fluid inside a blister."),
 ("moisture-meter","Moisture meter","An electronic meter held against the hull that indicates water in the laminate. Readings differ between makes; the comparison with a dry area of the same hull is what counts."),
 ("gel-peel","Gelcoat peeling","Machining the gelcoat off a blistered hull so it can dry before an epoxy barrier coat is applied."),
 ("epoxy-barrier","Epoxy barrier coat","Several coats of epoxy over a dried, peeled hull to keep water out."),
 ("hot-vac","Hot-vac","Heated vacuum panels applied to a peeled hull to dry it in a week or two instead of months."),
])}
  <h4 class="terms__group">Seacocks, paint and corrosion</h4>
{terms([
 ("skin-fitting","Skin fitting","A threaded tube with a flange that passes through the hull; the outside half of a through-hull."),
 ("backing-pad","Backing pad","A plywood or GRP pad inside the hull that gives a skin fitting a flat, strong seat."),
 ("seacock-body","Seacock","The valve on top of a skin fitting. Handle in line with the pipe means open; across it means shut."),
 ("ball-valve","Ball valve","A valve with a drilled ball inside: a quarter turn of the handle lines the hole up with the pipe (open) or across it (shut)."),
 ("hose-tail","Hose tail","The ribbed spigot the hose pushes onto."),
 ("hose-clips","Hose clips","Stainless-steel bands that clamp the hose to the tail. Two on every underwater hose."),
 ("hose","Reinforced hose","Wire- or fabric-reinforced hose that will not kink or collapse and is rated for below-waterline use."),
 ("bung","Softwood bung","A tapered wooden plug that can be hammered into a broken fitting to stop a leak. One tied to each seacock."),
 ("dzr","DZR brass","Dezincification-resistant brass, a copper-zinc alloy with arsenic added so the zinc does not leach out in sea water. Better than plain brass, not as good as bronze."),
 ("dezincification","Dezincification","Sea water dissolving the zinc out of brass, leaving a pink, porous, weak copper sponge."),
 ("antifouling-paint","Antifouling","Paint on the underwater hull that releases a biocide, usually copper, to stop weed and barnacles growing."),
 ("anode","Anode","A block of zinc, aluminium or magnesium bolted to the boat to corrode instead of the metal parts it is connected to."),
 ("galvanic-corrosion","Galvanic corrosion","What happens when two different metals sit in sea water and are electrically connected: the less noble one dissolves."),
 ("stray-current","Stray current","Electricity leaking into the water from faulty wiring on the boat or in the marina. It eats metal fittings far faster than ordinary galvanic corrosion."),
 ("bonding","Bonding","Wiring the underwater metal parts together inside the boat so that one anode protects them all."),
 ("survey","Survey","A professional inspection of the boat out of the water, with a written report. Always get one before buying a boat of this age."),
])}

  <div class="planned">
    <p>Planned for this section</p>
    <ul>
      <li>Photographs of faults: osmosis blisters, a keel smile, corroded keel bolts, a dezincified seacock, rudder bearing wear (still to be found under a CC licence)</li>
      <li>Confirmation of the rows still marked TBC in the antifouling table against each national authority</li>
      <li>Deck core and keel-encapsulation details for the Gib’Sea 31 and Finnsailer 35</li>
    </ul>
  </div>
</section>
'''
page = page.replace('{ONE}', ONE).replace('{TWO}', TWO).replace('{TBC}', TBC)
import re as _re
page = _re.sub(r' (<span class="(?:conf|tbc)[ "])', r'&nbsp;\1', page)
page = _re.sub(r'(?<=[^\s>]) ([¹²])', r'&nbsp;\1', page)
open(ROOT + 'sections/03-hull.html', 'w').write(page)

keys = re.findall(r'<li data-term="([^"]+)"', page)
dups = sorted(set(k for k in keys if keys.count(k) > 1))
parts = set(t for m in re.findall(r'class="part" data-term="([^"]+)"', page) for t in m.split())
anat = open(ROOT + 'sections/01-anatomy.html').read()
anat_keys = set(re.findall(r'<li data-term="([^"]+)"', anat))
print('duplicate keys in section:', dups)
print('keys clashing with anatomy:', sorted(set(keys) & anat_keys))
print('part terms without a definition anywhere:', sorted(parts - set(keys) - anat_keys))
print('literal tokens left:', page.count('{ONE}') + page.count('{TWO}') + page.count('{TBC}'))
ids = re.findall(r' id="([^"]+)"', page)
print('duplicate ids:', sorted(set(i for i in ids if ids.count(i) > 1)))
