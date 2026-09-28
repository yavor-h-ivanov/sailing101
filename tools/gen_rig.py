# Generates sections/04-rig.html for Sailing 101.
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_common import *
import gen_rig_diagrams as g

page = f'''<section id="rig">
  <h2>Rig and sails</h2>
  <p class="lead">The mast, its wires and the sails are the engine of a sailing boat. They are also the part most likely to fail suddenly and expensively, so this section is about what holds the mast up, what the sails are made of, how they are made smaller when the wind gets up, and what to look at before you trust a forty-year-old rig with your family. Lengths are in metres; a “32-footer” in a quoted price is a boat of about 9.8 m. In a hurry? <a href="#rig--checklist">Jump to the rig check</a>.</p>

  <div class="first-words">
    <p>Seven words before anything else</p>
    <dl>
      <dt>Spar</dt><dd>Any pole in the rig: the mast (vertical) and the boom (horizontal, along the bottom of the mainsail). Aluminium on this class.</dd>
      <dt>Standing and running rigging</dt><dd>Standing rigging is the fixed wire that holds the mast up. Running rigging is the rope you pull: halyards hoist sails, sheets pull them in and out, reefing lines shrink them.</dd>
      <dt>Stay and shroud</dt><dd>A stay runs fore and aft: the forestay holds the mast forward, the backstay holds it aft. A shroud runs to the side: cap shrouds to the top, held out by the spreaders (struts part way up the mast), lower shrouds to the middle.</dd>
      <dt>Terminal</dt><dd>The metal fitting on the end of a wire. Most rig failures start here, not in the wire.</dd>
      <dt>Chainplate</dt><dd>The metal strap on the hull or deck that a shroud or stay is attached to.</dd>
      <dt>Luff, leech, foot</dt><dd>The front, back and bottom edges of any sail. Head, tack and clew are its top, front and back corners.</dd>
      <dt>Reef and furl</dt><dd>To reef is to make a sail smaller because the wind has got up: a “slab” reef folds the bottom of the mainsail onto the boom. To furl is to roll a sail up on a rotating tube: the genoa (the big front sail) around the forestay, sometimes the mainsail inside the mast.</dd>
    </dl>
  </div>
  <details class="first-words first-words--verbs" id="rig--sailing-words" open>
    <summary>Six sailing words this section cannot avoid</summary>
    <dl>
      <dt>Tack (verb)</dt><dd>To turn the bow through the wind so that it blows on the other side of the sails. Also the front corner of a sail, and “tacked to the bow” means attached there by that corner. Three meanings, one word.</dd>
      <dt>Gybe</dt><dd>To turn the stern through the wind. The boom swings across the boat, fast; this is when it hurts people.</dd>
      <dt>Head up, bear away</dt><dd>To steer closer to the wind, and to steer further from it.</dd>
      <dt>Head to wind</dt><dd>Pointing straight into the wind, sails flapping: the position for hoisting, dropping and furling sails.</dd>
      <dt>Downwind, a run</dt><dd>Sailing with the wind behind you; a run is dead downwind, with the boom let right out.</dd>
      <dt>Sheet in, trim</dt><dd>To pull a sail’s sheet (the rope on its back corner) so the sail comes closer to the boat’s centreline. Trim is the general word for adjusting a sail’s angle and shape.</dd>
    </dl>
    <p class="first-words__note">The Sailing section covers all of these properly.</p>
  </details>
  <p class="conf-key"><b>Marks used below:</b> {ONE} means the fact comes from a single source; {TWO} means sources disagree or the figure is anecdotal (a forum or owner report); {TBC} means not yet verified. Everything unmarked is supported by at least two sources listed under “Sources and confidence” at the end of each topic.</p>

  <h3>How a rig stays up</h3>
  <p>A sloop rig is a tripod of wire. The forestay pulls the top of the mast forward, the backstay pulls it aft, and the cap shrouds pull it down each side, bent outwards over the spreaders so that they pull at a useful angle. Lower shrouds hold the middle of the mast. Every wire is in tension; the mast is in compression, pushing down on the deck or the keel with a force of several tonnes. Take any one wire away and the mast usually comes down. Everything below follows from that.</p>

{figure('fig-rig-types', 'rig types', '0 0 900 420', 'Masthead and fractional sloop rigs, and three tuning words', 'Left: a masthead sloop in profile, bow to the right, with the forestay and backstay meeting at the top of the mast, one pair of spreaders, cap and lower shrouds, and the rig dimensions I, J, P and E marked. Middle: a fractional sloop with the forestay meeting the mast below the top. Right: a mast drawn with exaggerated rake, pre-bend and forestay sag.', g.rig_types(), 'Bow to the right. Every boat in the reference fleet except the 2002 Gib’Sea 33 is a masthead sloop (the Gib’Sea 31 is listed as masthead by one database and as fractional by another {TWO}): forestay to the very top, a big overlapping genoa (one whose back corner reaches past the mast) doing much of the work. I, J, P and E are the four numbers a sailmaker asks for.', note=HINT)}

{compare('Masthead and fractional rigs at a glance', ['', 'Masthead', 'Fractional'], [
  ['Forestay attaches', 'at the top of the mast', 'part way up, typically 7/8 of the height'],
  ['Which sail does the work', 'a big overlapping genoa', 'the mainsail; headsails are small'],
  ['Tuning', 'simple: tighten the backstay and the forestay follows', 'more involved: the backstay bends the mast to flatten the main'],
  ['Handling', 'big genoa, big winches, more effort to tack (turn through the wind)', 'small jib, easy to tack; main needs reefing sooner'],
  ['Spreaders', 'usually straight (“in line”), one pair on this size', 'often swept aft, which limits how far the boom can go out downwind'],
  ['On the reference fleet', 'Moody 33, Sadler 32, Bavaria 1060, Finnsailer 35, Gib’Sea 31 {TWO}', 'Gib’Sea 33 (2002): swept spreaders, deck-stepped, plus a babystay'],
])}

{card('rig--masthead', 'Masthead sloop', 'the 1970s to 1980s standard', 'Forestay and backstay both attach at the masthead. The foretriangle (the space between mast, forestay and deck) is big, so the genoa is big and the mainsail relatively small. The Harlé Gib’Sea 33 of the 1970s was described by owners as “a very short mast with a big overlapping jib”, which is the archetype {ONE}.',
  ['The backstay pulls directly against the forestay, so backstay tension is forestay tension: tighten it and the genoa luff straightens and the boat sails closer to the wind.', 'The mast is stayed at one point at the top and one at the spreaders, so it stands stiff and straight; there is little to tune.'],
  ['Simple, forgiving and strong; one pair of spreaders and six or seven wires.', 'Powerful in light wind thanks to the large genoa.', 'Easy to buy sails for and to tune by feel.'],
  ['A 130 to 150% genoa is a big sail to sheet in on a 9.8 m boat: bigger winches, more winding, and it is the sail that gets rolled away first when the boat is simply overpowered.', 'Overlapping headsails are the most expensive sail on the boat and wear on the spreader tips and shrouds.'],
  ['Genoa chafe at the spreader tips (fit boots: soft covers over the tips).', 'Halyard wrap on the furler (see Reefing and furling).'],
  ['Which sail powers the boat: on a masthead rig a tired genoa costs more speed than a tired main.', 'Shortening sail on a masthead cruiser, as instructors teach it: roll some genoa away when the boat heels too much, put a reef in the main when the helm gets heavy, and by 18 to 20 knots of wind do both.'], fold=True)}

{card('rig--fractional', 'Fractional sloop', '7/8 rig; most boats since the 1990s', 'The forestay meets the mast below the top, commonly at seven-eighths of its height. Headsails are smaller and the mainsail is the main engine. The 2002 Gib’Sea 33 is the fractional boat in the reference fleet: deck-stepped mast on a compression post, spreaders swept aft with the shrouds taken to the toe rail (the outer edge of the deck), and a babystay (a short inner forestay) to stop the middle of the mast moving {ONE}.',
  ['Pulling the backstay bends the top of the mast aft, which flattens the mainsail and lets you take power out of it without reefing.', 'Swept spreaders let the cap shrouds also pull the mast forward, so the boat may not need running backstays (a pair of removable backstays that are set up on the windward side and let go on each tack).'],
  ['Small, easy jib: tacking is quick and the winches can be smaller.', 'Better to windward, and downwind the small headsail is less blanketed (starved of wind) by the mainsail.'],
  ['Needs more understanding to tune: the mast is meant to bend, and the wrong tension inverts it (bows it the wrong way).', 'With swept spreaders the boom cannot go out square on a run and the main chafes on the spreaders; downwind sailing angles are narrower.'],
  ['Mast pumping (the middle of the mast flexing fore and aft in waves) when the lowers or babystay are slack.', 'Reefing downwind: the battens (the stiff strips in the mainsail) catch on the swept spreaders.'],
  ['Ask who tuned the rig and when; look at the mast from the side and from behind for a straight, slightly forward-bowed shape.'], fold=True)}

{card('rig--spreaders', 'Spreaders', 'crosstrees', 'Struts part way up the mast that push the cap shrouds outwards so the wires pull at a wider, more useful angle. One pair on almost every 9 to 11 m boat of this era; two pairs let a designer use a thinner mast and bring the chainplates further inboard.',
  ['A spreader must bisect the angle of the shroud, the same angle above and below the tip, so that it is only ever in compression; it therefore tilts slightly upwards.', 'The shroud is clamped or seized (bound with wire) to the spreader tip so it cannot jump out when the leeward shroud goes slack.'],
  ['Single spreaders: fewer terminals (six per side with double lowers, a forward and an aft lower shroud each side) and, since “many mast failures are actually the result of a rigging terminal failure”, fewer things to break; easy to tune from the deck.'],
  ['Double spreaders need someone to go aloft (up the mast) to tune them, and have more terminals.', 'Swept spreaders (see Fractional sloop) limit downwind sailing.'],
  ['Play where the spreader meets the mast (the root); fatigue cracks at the root bracket; corrosion inside the tip fitting; a tip that has slid down the wire; a spreader knocked out of its angle by a halyard or a sail.', 'Isomat masts, fitted to many 1980s European production boats, are known for play at the spreader roots {TWO}; which spar maker the Bavaria 1060 used is {TBC}.'],
  ['From the deck with binoculars, and from a chair aloft (up the mast) once a season: the root does not move, the tips are seized and booted, both spreaders are at the same angle.'], fold=True)}

  <h3>Mast: on the deck or on the keel</h3>
  <p>A mast stands either on a plate on the deck, with a post or a bulkhead underneath carrying the load down to the keel, or it passes through a hole in the deck and stands on a step bolted to the keel floors. Most boats of this class are deck-stepped; the Moody 33S was advertised as deck-stepped with a single spreader and Proctor spars {ONE}, the Sadler 32 is deck-stepped with its original Proctor mast, and the 2002 Gib’Sea 33 is deck-stepped on a compression post. Which the Bavaria 1060 and Finnsailer 35 are is {TBC}; the Gib’Sea 31 is said to have changed from keel-stepped to deck-stepped in 1982, on the word of one listing site {TBC}.</p>

{figure('fig-mast-step', 'mast step', '0 0 900 360', 'Deck-stepped and keel-stepped masts in section', 'Left: a mast standing on a step plate on the deck, with a compression post below it carrying the load to the keel; a dished deck marks the fault. Right: a mast passing through the deck partners, wedged and booted, standing on a heel fitting bolted to the keel floor; corrosion at the heel where water pools is marked.', g.mast_step(), 'Deck-stepped is easier to lift out and leaks less; keel-stepped is stiffer and stronger but leaks at the deck and corrodes at the heel. Either way the load has to reach the keel through something you can inspect. Which reference boats are which is given in the text, with its marks.')}

{card('rig--deck-stepped', 'Deck-stepped mast', 'compression post, mast step plate', 'The mast heel sits in a cast or fabricated plate on the coachroof. Under the plate a compression post, a metal or timber pillar, or a main bulkhead carries the load down to the hull structure.',
  ['The mast pushes down with the combined tension of all the shrouds and stays: on a boat this size, several tonnes. The post transfers that straight to the keel floors.', 'Halyards leave the mast at the base and are led aft over the coachroof to the cockpit.'],
  ['The mast can be lifted off with a crane in an hour and re-stepped just as fast.', 'No hole in the deck to leak.', 'Easier to tune, because the foot cannot move.'],
  ['Everything depends on the post and the deck under the plate.', 'Halyards and cables slap inside the mast in a marina unless they are held in a conduit (a tube); older Proctor masts had none {TWO}.'],
  ['A dished (sunken) deck around the plate: the balsa core under the mast is wet and crushed.', 'A post whose foot has rotted, or that does not land on the keel floor, or that stands off-centre from the mast; cracked woodwork and doors that no longer close as the deck drops.'],
  ['Sight along the coachroof for a dip at the mast, tap the deck around the plate, and look at the foot of the post inside for rot, rust or crushing.', 'Check the drain holes in the heel plate are clear so water does not sit in the mast foot.'], fold=True)}

{photo('rig-mast-step.jpg', 'The black alloy foot of a mast sitting in a slotted track on a white coachroof, held by a pin, with turning blocks either side', 'The foot of a deck-stepped mast: the heel casting sits in a track on the coachroof and is held by a pin, with turning blocks for the lines led aft. White powder or pitting where the heel meets the step is corrosion worth a closer look.', 'Jeuwre', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0', 'https://commons.wikimedia.org/wiki/File:Mast_step.jpg', 960, 1440, 'https://commons.wikimedia.org/wiki/User:Jeuwre')}

{card('rig--keel-stepped', 'Keel-stepped mast', 'partners, mast collar, Spartite', 'The mast passes through a reinforced hole in the deck, the partners, and stands on a step on the keel floors. Wedges or a poured polyurethane chock (Spartite) hold it in the partners, and a rubber or canvas boot keeps most of the rain out.',
  ['The load goes straight to the keel with no post in the way, and the deck holds the mast sideways, so the mast can carry more compression and its bend can be controlled better.'],
  ['Stiffer and stronger for the same section; the mast has a better chance of staying up if a wire fails, because the partners hold it.'],
  ['Rain runs down inside the mast and pools at the heel, where the aluminium sits against stainless fastenings and bilge water: “corrosion at the heel is probably the most common problem with keel-stepped aluminium spars”.', 'The partners leak: water down the mast into the cabin is a classic complaint.', 'Cold, noise and a mast in the middle of the saloon.'],
  ['Corroded, powdery or holed mast heel, only seen when the mast is lifted; wedges that have fallen out; a boot clamped with a stainless band that has itself corroded the tube.'],
  ['At every lift-out with the mast down, look at the heel and the step; keep the step bone dry with clear drain holes.', 'Spartite, on the market since 1993, fills the partners completely and stops both leaks and wedge loss, but it can make the mast hard to unstep.'], fold=True)}
{sources('rig types and masts', [
  'Masthead vs fractional: ' + a('https://en.wikipedia.org/wiki/Fractional_rig','Wikipedia, fractional rig') + ', ' + a('https://www.sailboat-cruising.com/Masthead-vs-Fractional-Rig.html','sailboat-cruising.com') + ', ' + a('https://mandurahyachtacademy.au/full-vs-fractional-rig/','Mandurah Yacht Academy') + '. Harlé Gib’Sea 33 rig character: ' + a('https://www.hisse-et-oh.com/sailing/gib-sea-33-harle-point-point-point','Hisse-et-Oh owners (single source)') + '. Gib’Sea 33 (2002) rig: ' + a('https://www.boats.com/reviews/boats/gibsea-33-the-latest-from-dufour/','boats.com review') + ' and ' + a('https://www.bateaux.com/plaisance/voiliers/gib-sea-33-REF5ahWJqMHjzE,/1/fiche-technique','bateaux.com data sheet') + '.',
  'Spreaders: ' + a('https://goodoldboat.com/a-strong-word-for-the-single-spreader-rig/','Good Old Boat, a strong word for the single-spreader rig') + ', ' + a('https://goodoldboat.com/spreaders-101/','Good Old Boat, Spreaders 101') + ', ' + a('https://www.morganscloud.com/2011/09/02/parallel-swept-back-spreaders/','Attainable Adventure Cruising on swept spreaders') + ', ' + a('https://www.pantaenius.com/de-en/insights/journal/article/the-most-common-causes-of-rig-failure/','Pantaenius, the most common causes of rig failure') + '. Bavaria 1060 spreader play: ' + a('https://forums.ybw.com/threads/isomat-mast.475619/','YBW forum thread') + ' (anecdotal).',
  'Deck vs keel stepped: ' + a('https://www.sailboat-cruising.com/Deck-stepped-vs-Keel-stepped-mast.html','sailboat-cruising.com') + ', ' + a('https://www.riggingdoctor.com/life-aboard/2020/5/20/deck-stepped-vs-keel-stepped-mast','Rigging Doctor') + ', ' + a('https://www.practical-sailor.com/blog/sailboat-rig-inspection-tips/','Practical Sailor on heel corrosion') + ', ' + a('https://www.practical-sailor.com/boat-maintenance/keeping-willow-from-weeping/','Practical Sailor on Spartite') + ', ' + a('https://goodoldboat.com/wedging-the-mast/','Good Old Boat on wedging') + '.',
  'Reference boats: Moody 33S deck-stepped, single spreader, Proctor spars per a ' + a('https://www.yachtworld.com/yacht/1980-moody-33s-8019490/','1980 sale listing') + ' (single source); Kemp masts on many Moody 33s per ' + a('https://forums.ybw.com/threads/diy-boat-measuring-for-2nd-hand-sail-selection-moody-33.301607/','a YBW thread') + '; Sadler 32 per ' + a('https://martinleaning.co.uk/content/219-sadler-32','Martin Leaning’s rigging page') + ' and ' + a('https://forums.ybw.com/threads/sadler-32-what-should-i-look-for.170275/','YBW owners') + '; Gib’Sea 31 stepping change per ' + a('https://www.listingsport.com/sailboats/gib-sea/31','Listings Port') + ' (single, unverified source).'
])}

  <h3>Standing rigging: the wires and what they end in</h3>
  <p>On this class the standing rigging is 1×19 stainless-steel wire: nineteen strands twisted into one stiff, low-stretch rope, 5 to 7 mm thick on a 9 to 10 m boat {TWO}. The wire almost never breaks in the middle. It breaks at its ends, in the terminals, and at the fittings the terminals attach to. So a rig check is a check of ends.</p>

{figure('fig-terminals', 'rig terminals', '0 0 900 380', 'The ends of a shroud: swaged terminal, mechanical terminal, rigging screw and chainplate, and the mast end', 'Four panels. A swaged terminal with hairline cracks and broken strands marked; a mechanical terminal shown in section with its cone and body; a rigging screw with split pins, a toggle and clevis pin above a chainplate strap that passes through the deck to a bulkhead, with the leak path marked; and the mast wall with a T-terminal in its slot, a spreader root and a spreader tip with the cap shroud seized to it.', g.terminals(), 'The lower ends live in salt spray and are where most wires fail. Swages cannot be opened; mechanical terminals can. Toggles let a wire swing without bending; split pins stop everything falling apart.')}

{card('rig--wire-terminals', 'Wire and terminals', 'swage, Sta-Lok, Norseman, Hi-Mod', 'A swaged terminal is a stainless sleeve squeezed onto the wire by a machine at the rigger’s. A mechanical terminal is screwed together on the wire with hand tools: a cone is pushed into the strands and a body clamps them. Both are as strong as the wire when new; they age differently.',
  ['The wire runs into the terminal and stops. Salt water runs down the wire and into the top of the sleeve, where it sits without oxygen; that is where stainless steel suffers crevice corrosion (rust that starts in a tight, wet gap) and cracks.', 'Mechanical terminals drain better and can be unscrewed to inspect the wire; in Practical Sailor’s pull tests, swaged and mechanical terminals alike broke at or above the wire’s rated strength, apart from one early Norseman sample {ONE}.'],
  ['Swages are cheap and neat and are what every production boat left the factory with.', 'Mechanical terminals can be fitted by an owner on a mooring, reused on new wire, and opened for inspection.'],
  ['A swage cannot be inspected inside; a “seemingly harmless rust stain” on it is the typical sign of crevice corrosion.', 'Each terminal ends in an eye (a ring) or a fork (two prongs) that a clevis pin passes through; a T-terminal (see the drawing) hooks into the mast instead.', 'Rod rigging (solid bar) and Dyform (compacted-strand wire) are stronger and stretch less, but rod fails without warning and both cost more; 1×19 remains the cruising choice.'],
  ['Hairline cracks running lengthways down the sleeve; broken strands standing proud where the wire enters (“meat hooks”, which will cut your hand); rust weeping from the top of a swage; a bent or cracked eye or fork.', 'A common compromise is swages aloft, where they stay dry, and mechanical terminals at the deck.'],
  ['Run a cloth or a gloved hand up each wire from the deck; look at each lower swage with a magnifier and a straight edge; dye-penetrant spray finds cracks a magnifier misses.', 'Ask the age of the rig and for the rigger’s invoice; if nobody knows, assume it is original.'], fold=True)}

{card('rig--screws-pins', 'Rigging screws, toggles and pins', 'bottlescrew, turnbuckle, clevis pin, split pin', 'The rigging screw at the bottom of each wire is a threaded barrel that tensions it. Below it a toggle, a small hinge, lets the wire swing so that it is never bent at the terminal; a forestay carrying a furler should have a toggle at both ends of its screw. Clevis pins join the parts; split pins stop the clevis pins walking out.',
  ['Tension is set by turning the barrel; once set, it is locked with split pins or seizing wire so that vibration cannot unwind it.', 'Every joint has to be in line: a rigging screw that leans, a fork bearing on one side, a clevis pin at an angle or a toggle hard against the deck will fatigue and crack.'],
  ['Simple, visible, cheap to replace.'],
  ['Split pins are tiny and are what actually keeps the mast up; a missing one is a common find on a survey.', 'Threads seize with salt and age; a screw that will not turn cannot be tensioned or slackened.'],
  ['Missing or straightened split pins; pins that do not fill their holes; bent forks; cracked toggles; rust in the threads; a rigging screw run out to the end of its thread because the wire has stretched or was cut too short.'],
  ['Every season, with the mast up: look at every clevis pin and split pin in place, and replace any doubtful split pin (never re-use one: they work-harden). Open the legs about 30 degrees and tape over them so they do not tear sails or fingers.', 'Pull clevis pins out to inspect them only with the mast down, or with that one wire fully slackened while the others hold the mast: a pin will not come out of a loaded shroud, and taking wires off one at a time with the rig under tension is how masts come down.'], fold=True)}

{card('rig--chainplates', 'Chainplates', 'shroud plates; a tang is the same thing on the mast', 'The stainless straps that the shrouds and stays are attached to. On this class they usually pass through the deck and bolt to a bulkhead or a knee (a triangular bracket) inside, under a small stainless cover plate bedded in sealant.',
  ['The shroud pulls up on the strap; the strap pulls up on the bulkhead; the bulkhead is bonded to the hull. The sealant under the cover plate is all that keeps water out of the slot.'],
  ['Straps bolted to a bulkhead spread the load well and are easy to see from inside a locker.'],
  ['Where the strap passes through the deck it is wet, starved of oxygen and heavily loaded: exactly the recipe for crevice corrosion, hidden by the cover plate.', 'The Moody chainplate design, a strap on a plywood part-bulkhead with a small sealing plate screwed to the deck, was “common to many Moody models”: the sealant hardens and cracks, water enters the balsa deck and the plywood, and in the worst case “the ply goes soggy, letting the bolts tear through” {TWO}. On one boat a backstay plate came out in two halves {TWO}. Sadler 32 owners report the same leak into the balsa side decks {TWO}.'],
  ['Rust stains around the cover plates; soft or springy deck a hand’s width inboard of the shrouds; water stains, delamination or rot on the bulkhead inside; elongated (oval) pin holes; hairline cracks at the top of the strap.'],
  ['Lift the cover plates every few years, dig out the old sealant and re-bed (butyl tape, a sticky sealant tape that never fully hardens, is the owners’ favourite); look at the bulkhead from inside the locker with a torch; on any boat with an original rig, have the straps pulled and inspected, or replaced, when the rig is renewed.'], fold=True)}

{card('rig--boom', 'Boom, gooseneck, kicker and topping lift', 'vang, kicking strap', 'The boom carries the foot of the mainsail. It hinges on the mast at the gooseneck, is pulled down by the kicker (called the vang in America), and is held up when the sail is down by the topping lift, a line from the masthead to its end.',
  ['The kicker stops the boom lifting and the top of the sail twisting off downwind; on a rigid (gas-strut) kicker it also holds the boom up, so the topping lift can go.', 'Loads at the gooseneck and the kicker attachment are among the highest in the rig, so “failures there are so common”.'],
  ['A rigid kicker means one line fewer and no topping lift to foul the leech.'],
  ['A gooseneck is a hinge in two planes taking a shock load every gybe (see the six words above); pins and castings wear.', 'The boom is at head height: it hurts, and it kills people every year. A preventer (a line holding the boom out so it cannot swing across, see Sailing) is the answer.'],
  ['Worn or cracked gooseneck fittings and pins; cracks in the boom at the kicker attachment; corrosion under fittings where stainless screws meet aluminium; a topping lift chafed through at the masthead.'],
  ['Wobble the boom at the gooseneck; look at the kicker bracket on the boom and the mast for cracks and white corrosion; check that the sheaves (the grooved wheels the lines run over) at the boom end turn.'], fold=True)}

{photo('rig-gooseneck.jpg', 'The end of an aluminium boom joined to the mast by a black hinged fitting, with reefing lines entering the boom', 'A gooseneck: the hinged fitting that joins the boom (right) to the mast (left). This one is on a modern catamaran, but monohulls use the same parts. Play in the pins is the wear to look for.', 'Craig Stanfill', 'CC BY-SA 2.0', 'https://creativecommons.org/licenses/by-sa/2.0', 'https://www.flickr.com/photos/35331737@N03/48069820207/', 1024, 683, 'https://www.flickr.com/photos/photo_fiend/')}

{card('rig--backstay', 'Backstay and its adjuster', 'split backstay, backstay tensioner', 'On a masthead rig the backstay is the wire that sets forestay tension. Many boats have a way to change it under way: a split backstay with a tackle pulling the two legs together, or a mechanical or hydraulic adjuster on a single backstay. (A tackle is a rope led through pulleys, called blocks, to multiply your pull.)',
  ['Tighten the backstay and the forestay straightens: the genoa gets flatter and the boat sails closer to the wind in a breeze. Ease it in light wind for a fuller, more powerful genoa.', 'Shrouds are set at about 15 to 20% of the wire’s breaking load; a backstay adjuster is cranked up towards 30% only in strong wind, and eased again after.'],
  ['Cheap performance and comfort on a masthead boat; on a fractional boat it is the main way of flattening the mainsail.'],
  ['An adjuster left cranked up in the marina fatigues the whole rig; a backstay with an insulator in it (to use the wire as a long-range radio aerial) or a wind generator hung on it is a weak point.'],
  ['Cracked or seized adjuster; a split-backstay plate with elongated holes; the tackle chafing the leech of the mainsail.'],
  ['Ease it when you leave the boat; check the masthead end of the backstay from aloft, since it is the one wire you cannot reach from the deck.'], fold=True)}

  <div class="callout">
    <span class="callout__title">When to replace the wires</span>
    <p>The wire looks fine right up to the day a swage lets go, so riggers and insurers go by age. Budget for new rigging on any boat of this age whose rig history you do not know.</p>
  </div>
{compare('Standing rigging: life and cost', ['', 'What the sources say'], [
  ['Working life', 'ten years for a cruising boat, say the riggers and magazines; fifteen years or 20,000 nautical miles at the very outside'],
  ['Insurers', 'Pantaenius: a rigger’s check if the rig is over fifteen years old, replacement if a boat over twenty-five years old still has its original rig, otherwise rig damage is excluded {ONE}. Topsail: some policies require the rigging to be replaced, or exclude claims from rig failure, once it is over a stated age, typically five to ten years; others set no age but expect regular inspection. The policy wordings of Navigators &amp; General and Craftinsure set no age, but exclude wear and tear, and N&G asks for evidence of maintenance on boats over three years old. Read your own policy’s rigging clause'],
  ['Professional re-rig, 9 to 12 m boat, UK', '£2,500 to £4,500 in a 2023–24 guide; owners quote £1,200 to £1,600 fitted for 9 to 9.5 m boats {TWO}'],
  ['Do it yourself', 'about £1,500 in wire and mechanical terminals for a 10 m boat in 2025 {TWO}, plus the crane to lift the mast'],
])}

  <h4>Tuning in three words (optional reading)</h4>
  <ul>
    <li><strong>Rake</strong> is the whole mast leaning aft, one to two degrees, so the boat has a touch of weather helm (wants to turn gently into the wind). Hang a weight on the main halyard and measure how far aft of the mast foot it hangs: roughly 2 to 3 cm for every metre of mast, so 25 to 40 cm on the 12 to 13 m masts of this fleet.</li>
    <li><strong>Pre-bend</strong> is the middle of the mast bowed slightly forward by the lower shrouds, so that it cannot bow the other way (invert) under load. In-line masthead rigs of this era are usually set straight or nearly so; one guide suggests up to 10 cm on a stiff masthead rig {ONE}.</li>
    <li><strong>Tension</strong> is set with the rigging screws and measured with a gauge or a folding rule: cap shrouds at about 15% of the wire’s breaking load (3 mm of stretch over a 2 m length of 1×19 wire, whatever its size, by Seldén’s rule), lowers a little less and adjusted until the mast is straight when you sight up the track, backstay to suit the wind. Log the numbers so you can check them again.</li>
    <li><strong>Pumping</strong> is the middle of the mast flexing fore and aft in waves: a sign the lowers or babystay are slack (racing boats add checkstays, thin running backstays to the middle of the mast, for this). <strong>Inversion</strong> is the mast bowing aft in the middle: bad for the sail and, on a fractional rig, dangerous.</li>
  </ul>
{sources('standing rigging', [
  'Wire and terminals: ' + a('https://www.practical-sailor.com/sails-rigging-deckgear/screw-on-rigging-terminals/','Practical Sailor on screw-on terminals') + ', ' + a('https://www.practical-sailor.com/sails-rigging-deckgear/mechanical-terminal-pull-test','Practical Sailor pull test') + ', ' + a('https://www.practical-sailor.com/blog/detecting-and-dealing-with-stainless-steel-corrosion/','Practical Sailor on crevice corrosion') + ', ' + a('https://www.sailboat-cruising.com/sailboat-standing-rigging.html','sailboat-cruising.com') + ', ' + a('https://martinleaning.co.uk/content/16-choosing-the-right-wire-for-yacht-standing-rigging','Martin Leaning on wire choice') + '. Wire sizes for this class from ' + a('https://goodoldboat.com/standing-rigging/','Good Old Boat') + ' and a ' + a('https://forums.ybw.com/threads/rules-of-thumb-for-rigging-size.464159/','YBW thread') + ' (anecdotal).',
  'Screws, toggles, pins and inspection: ' + a('https://www.yachtingmonthly.com/gear/rig-check-how-to-inspect-and-tune-your-standing-rigging-for-maximum-safety-103254','Yachting Monthly rig check') + ', ' + a('https://www.yachtingmonthly.com/gear/yacht-rigging-your-essential-pre-season-rig-check-guide-92558','Yachting Monthly pre-season guide') + ', ' + a('https://www.sailboatliveaboard.com/yacht-stainless-rigging-terminals-and-installation.html','sailboatliveaboard.com on terminals') + ', ' + a('https://www.pbo.co.uk/expert-advice/metal-fatigue-in-rig-components-crack-detection-by-dye-penetrant-83250','PBO on dye-penetrant testing') + '.',
  'Chainplates: ' + a('https://www.practical-sailor.com/sails-rigging-deckgear/how-to-inspect-your-sailboats-chainplates/','Practical Sailor') + ', ' + a('https://www.cruisingworld.com/how/chainplates-101-inspect-and-refit/','Cruising World') + '. Moody: ' + a('https://forums.ybw.com/threads/buying-advice-for-moodys-28-30-31.549206/','YBW buying advice') + ', ' + a('https://www.moodyowners.info/threads/moody-31-chainplate-leak.21765/','Moody owners’ forum') + ', ' + a('https://forums.ybw.com/threads/inspecting-chainplates-properly.630481/','YBW on inspecting chainplates') + '. Sadler 32: ' + a('https://forums.ybw.com/threads/sadler-32-what-should-i-look-for.170275/','YBW thread 170275') + ', ' + a('https://forums.ybw.com/threads/viewing-sadler-32-what-should-i-look-out-for.384695/','thread 384695') + '.',
  'Boom, kicker, backstay: ' + a('https://www.morganscloud.com/2020/11/16/rigid-vangs/','Attainable Adventure Cruising on rigid vangs') + ', ' + a('https://www.practical-sailor.com/sails-rigging-deckgear/solid-vang-showdown/','Practical Sailor vang test') + ', ' + a('https://sailmagazine.com/cruising/tension-aloft/','SAIL, tension aloft') + ', ' + a('https://www.yacht.de/en/care/rig-trim-trimming-the-backstay-understanding-and-optimising-tensioner-systems/','YACHT on backstay tensioners') + '.',
  'Replacement interval and insurers: ' + a('https://www.pbo.co.uk/expert-advice/expert-answers/when-should-i-replace-standing-rigging-on-my-boat-97675','PBO, when should I replace standing rigging') + ', ' + a('https://www.yachtingworld.com/practical-cruising/pip-hare-check-replace-standing-rigging-127894','Yachting World, Pip Hare') + ', ' + a('https://www.yacht.de/en/insurance-how-old-can-the-rig-be/','YACHT, how old can the rig be (Pantaenius rule)') + ', ' + a('https://www.pantaenius.com/uk-en/insights/journal/article/check-the-rig-3/','Pantaenius, check the rig') + '; other insurers from ' + a('https://forums.ybw.com/threads/standing-rigging-age-and-insurance.146822/','YBW thread 146822') + ' and ' + a('https://forums.ybw.com/threads/insurance-and-standing-rigging.454487/','thread 454487') + ' (anecdotal). Costs: ' + a('https://improvesailing.com/cost/cost-to-replace-standing-rigging-in-the-uk','Improve Sailing UK cost guide') + ', ' + a('https://forums.ybw.com/threads/rigging-costs.600464/','YBW rigging costs 2025') + ' (anecdotal); ' + a('https://www.topsailinsurance.com/news/does-the-replacement-of-rigging-impact-my-boat-insurance','Topsail, rigging and insurance') + ', ' + a('https://www.geounderwriting.com/media/rc0pibbn/yacht-and-motorboat-policy-wording.pdf','Navigators &amp; General policy wording') + ' (PDF), ' + a('https://www.craftinsure.com/yacht-insurance/','Craftinsure') + '.',
  'Tuning: ' + a('https://www.pbo.co.uk/seamanship/rig-tuning-a-practical-guide-for-sailors-79113','PBO rig tuning guide') + ', ' + a('https://support.seldenmast.com/files/595-540-E.pdf','Seldén, Hints and advice on rigging and tuning') + ', ' + a('https://uk.boats.com/how-to/how-to-tune-the-rig-on-your-yacht/','boats.com on tuning') + ', ' + a('https://www.pbo.co.uk/expert-advice/how-to-set-up-your-rig-67093','PBO, how to set up your rig') + '.'
])}

  <h3>Sails</h3>
  <p>A sail is a wing made of cloth. Its three edges and three corners have names that every instruction and every sailmaker’s form uses, so learn them first from the drawing; the controls that change its shape are drawn with it.</p>

{figure('fig-sail-parts', 'sail parts', '0 0 940 540', 'Mainsail and genoa with their edges, corners and controls', 'A masthead sloop seen from the port side, bow to the right. The mainsail shows its head with headboard, tack, clew, luff, leech, foot, roach beyond the dotted line, four battens, two rows of reef cringles and points, a leech line, leech telltales and a Cunningham cringle, with the main halyard, topping lift, outhaul, kicker, mainsheet and traveller. The genoa on the forestay shows head, tack, clew, luff telltales, its overlap past the mast, the UV strip along leech and foot, the sheet to a car on the track, and the furling drum at the bow.', g.sail_parts(), 'Bow to the right; sails set for sailing to windward. Every edge, corner and control is a term below.')}

{card('rig--mainsail', 'Mainsail', 'main', 'The sail on the mast and boom. On a masthead rig it is the smaller sail, but it is the one with reefs in it and the one whose shape you control most.',
  ['The luff slides up a groove in the mast on a rope sewn into its edge (a bolt rope) or on small plastic slides; the foot runs along the boom or is loose-footed, attached only at the clew. Battens hold the roach out; full-length battens hold the whole sail flat and quiet.', 'Shape is controlled by halyard (luff tension), outhaul (foot depth), kicker (twist) and mainsheet and traveller (angle and twist).'],
  ['Cheap to make well; lasts longest of the sails because a cover keeps the sun off it.'],
  ['Needs a cover on every day it is not used; ultraviolet light destroys polyester thread and cloth.'],
  ['Stitching chalky and breaking along the leech; batten pockets chafed through at the spreaders; a torn headboard; a leech line that has jammed and hooked the leech; a sail that has stretched into a deep bag (“blown out”); cloth that has been left to flog (flap violently) in the wind, which breaks down the fibres.'],
  ['Hoist it on the mooring and look: horizontal wrinkles from the luff mean the halyard is slack, vertical ones that it is too tight; a leech that hooks to windward rather than streaming aft is a tired sail.'], fold=True)}

{card('rig--genoa', 'Genoa, jib and overlap', 'headsail; racing boats number theirs No. 1 (biggest) to No. 4', 'A headsail is any sail set on the forestay. A jib fits inside the foretriangle; a genoa is bigger and overlaps the mast. Its size is given as a percentage of J, the foretriangle base: 100% is a working jib (the everyday headsail that fits inside the foretriangle), 130 to 135% the usual all-round cruising genoa, 150% a light-wind sail.',
  ['On a furler, one genoa does the work of a wardrobe: roll some away and it becomes a smaller sail, though a baggier and less efficient one; a foam or rope luff pad helps it keep shape part-rolled.', 'The sheet lead (the car, a sliding block on the side-deck track) moves forward as the sail is rolled so that the sheet still pulls from the middle of the clew, evenly on foot and leech.'],
  ['Convenient and safe: the sail is changed from the cockpit.'],
  ['A 135% genoa rolled to 100% has all its cloth bunched at the luff and sets badly; in a gale it is no substitute for a small, flat jib.', 'The UV strip along leech and foot protects the rolled sail but adds weight where you least want it.'],
  ['UV strip rotted, stitching gone, foot and leech tapes worn; leech flutter that the leech line cannot cure; a luff tape torn out of the foil groove.'],
  ['Unroll it on a calm day and look at the leech and the UV strip; a sailmaker can replace a strip for a fraction of the price of a sail.'], fold=True)}

{card('rig--cloth', 'Sail cloth and how sails die', 'Dacron, laminate, blown out', 'Almost every cruising sail on this class is woven polyester, sold as Dacron: tough, cheap and the least able to hold its shape. Laminates (film and fibres glued in layers) hold shape better and weigh less but die sooner; Hydranet, a polyester weave with a Dyneema grid, sits between them at a premium price.',
  ['Sails wear by hours in the sun and by flogging (flapping hard when not filled), not by years: woven polyester is good for roughly 3,500 to 4,000 hours, which is fifteen seasons for a weekend cruiser and two or three for a charter boat.', 'Long before the cloth tears, it stretches. The deepest part of the sail (the draft) moves aft, the leech hooks, and the sail cannot be flattened: the boat heels more, sails less close to the wind and pulls harder on the helm. That is a “blown-out” sail.'],
  ['Woven polyester can be repaired by any sailmaker, patched on board and re-stitched more than once.'],
  ['A new suit for a 9.8 m boat, a fully battened main and a furling genoa with UV strip, was quoted at £2,300 to £3,800 in 2013 and owners report material prices roughly doubled since {TWO}.'],
  ['Chalky, powdery stitching that you can pull apart with a fingernail; cloth that crackles, or that has gone limp and soft; brown mildew; batten pockets and clew rings pulling out.'],
  ['Look at the stitching first, on the leech and around the reef cringles; ask the age; a sail loft (a sailmaker’s workshop) can measure the shape and tell you whether a recut is worth it.'], kind='fault', fold=True)}

{card('rig--inventory', 'What sails a cruising boat needs', 'storm jib, trysail, cruising chute', 'A coastal cruiser of this size needs to cope with winds over 25 knots and with drifting home in five knots. The usual set is a mainsail with two or three reefs, a furling genoa of 130 to 135%, something for a gale, and something for light wind downwind.',
  ['A storm jib is a small, flat, heavy sail clipped (hanked) to an inner forestay or set over the rolled genoa in a sleeve; the racing rule of thumb sizes it at no more than 5% of I squared, about 7 m² on a boat with a 12 m foretriangle. A trysail replaces the main in a gale, sets on its own track and needs no boom; the rule gives 17.5% of P times E, about 6 m² on a Sadler 32.', 'A spinnaker is a big, light, balloon-shaped sail for sailing downwind. A cruising chute is an asymmetric (lopsided) spinnaker cut for a small crew, attached by its tack to the bow without a pole and hoisted and dropped through a snuffer (a sock). A symmetric spinnaker needs a pole and more hands but sails deeper downwind.'],
  ['With a genoa and a chute most crews never miss the rest.'],
  ['Storm sails live in a locker for years and are needed on the one day nobody has practised setting them; a rolled-up genoa is not a storm sail.'],
  ['Storm sails that have never been out of the bag; a chute with no snuffer; a spinnaker pole with a seized end fitting.'],
  ['Set every sail in the locker once, in harbour, before you need it.'], fold=True)}
{sources('sails', [
  'Parts: ' + a('https://en.wikipedia.org/wiki/Sail_components','Wikipedia, sail components') + ', ' + a('https://improvesailing.com/sailboat/parts-of-a-sail-explained','Improve Sailing') + ', ' + a('https://www.yachtingmonthly.com/sailing-skills/sail-care-how-to-get-the-best-from-your-sails-with-proper-cleaning-and-basics-repairs-103535','Yachting Monthly on sail care') + '.',
  'Cloth and life: ' + a('https://www.northsails.com/en-us/blogs/north-sails-blog/cruising-sail-durability','North Sails on cruising sail durability (the hours figures)') + ', ' + a('https://www.cruisingworld.com/how-long-do-sails-last/','Cruising World') + ', ' + a('https://www.yachtingmonthly.com/sailing-skills/when-to-replace-yacht-sails-and-how-to-make-old-sails-last-longer-91872','Yachting Monthly, when to replace sails') + ', ' + a('https://phantom-watersports.com/blogs/sailmaking/dacron-vs-hydranet-which-sailcloth-is-best-for-cruising','on Hydranet') + '. Prices: ' + a('https://forums.ybw.com/threads/costs-of-sails-for-a-32.363825/','YBW, costs of sails for a 32 (2013)') + ' and ' + a('https://forums.ybw.com/threads/cost-of-new-sails-for-24ft-yacht.608105/','YBW 2024 thread') + ' (anecdotal).',
  'Overlap and inventory: ' + a('https://www.uksailmakers.com/encyclopedia/genoas-and-other-jibs/','UK Sailmakers encyclopedia, genoas') + ', ' + a('https://www.northsails.com/en-us/blogs/north-sails-blog/cruising-sail-inventories-day-vs-coastal-vs-bluewater','North Sails on cruising inventories') + '. Storm sails: ' + a('https://www.uksailmakers.com/encyclopedia-4-10-storm-sails/','UK Sailmakers on storm sails (the OSR sizing)') + ', ' + a('https://www.upffront.com/blog/guides-4/do-you-need-a-set-of-storm-sails-131','Upffront') + '. Chutes: ' + a('https://uk.boats.com/how-to/choosing-the-right-sails-spinnaker-vs-cruising-chute/','boats.com, spinnaker vs cruising chute') + ', ' + a('https://www.northsails.com/en-us/blogs/north-sails-blog/asymmetrical-vs-symmetrical-spinnakers-know-the-difference','North Sails') + '. The example areas use the Sadler 32 dimensions from ' + a('https://goodoldboat.com/saildata/boat/sadler-32/','Good Old Boat sail data') + ' (I 12.13 m, P 10.52 m, E 3.20 m).'
])}

  <h3>Reefing and furling</h3>
  <p>Reefing is making the mainsail smaller; furling is rolling a sail away on a rotating tube. Both exist so that a small crew can shorten sail before the boat is overpowered. The rule every instructor repeats: if you are wondering whether to reef, reef. On most boats of this size the first reef goes in at around 18 knots of wind when sailing towards it.</p>

{figure('fig-reefing', 'reefing and furling', '0 0 900 400', 'Slab reefing, in-mast furling and a headsail furler', 'Left: a mainsail with its first reef tucked in, the luff cringle on the ram’s horn at the gooseneck, the reefing line from the boom end up through the leech cringle and back down, and the slab of sail below the reef tied with the reef points. Middle: a section through a furling mast seen from above, with the sail rolled on a mandrel inside and the slot at the back; a jam is marked. Right: a headsail furler with its foil over the forestay, halyard swivel at the top with the halyard-wrap fault marked, and the drum and furling line at the bottom.', g.reefing(), 'Slab reefing is the simplest and gives the best sail; in-mast furling is the most convenient and the one that jams; the headsail furler is on nearly every boat and fails mostly through halyard wrap.')}

{card('rig--slab-reefing', 'Slab (jiffy) reefing', 'two-line, single-line', 'The mainsail has one to three rows of reinforced eyes, cringles, at luff and leech. To reef, you ease the halyard, hook the luff cringle over a horn at the gooseneck (or pull it down with a luff line), winch the leech cringle down to the boom with the reefing line, re-tension the halyard, and tie the loose slab of sail with the reef points.',
  ['The reef takes a horizontal slab off the bottom of the sail: it gets smaller, flatter and its centre of effort (the point where the wind’s push on the sail acts) drops, which is exactly what you want in wind.', 'Single-line reefing pulls luff and leech down with one line led aft to the cockpit: convenient, but the line runs through many blocks, adds friction and if it jams or breaks “you would be in a tough spot”. Two-line systems are more reliable.'],
  ['On more than three-quarters of yachts; the best-setting reefed sail; nothing to jam, no moving parts inside a spar; the sail can always be dropped.'],
  ['Someone may have to go to the mast in a rising wind, unless the lines are led aft.', 'Reef points tied too tight, or before the leech reefing line is winched down, tear the sail.'],
  ['Reefing lines chafed through inside the boom; a leech cringle pulled out; a ram’s horn bent open.'],
  ['Practise putting a reef in and taking it out again (“shaking it out”) on a calm day until it takes two minutes.'], fold=True)}

{card('rig--inmast', 'In-mast and in-boom furling', 'furling main', 'The mainsail rolls around a rod (the mandrel) inside a hollow, slotted mast, or around a mandrel inside an oversized boom. Neither is common on boats of this age and size; the reference fleet left the factory with slab reefing {TBC}. Both are common on boats built since the 2000s and are sometimes retrofitted.',
  ['In-mast: a furling line turns the mandrel and the sail rolls in through the slot at the back of the mast; the sail has no battens (or vertical ones) and little or no roach, so it is smaller and flatter than a slab-reefed main.', 'In-boom: the sail rolls down into the boom, keeps its battens and roach and can still be dropped if the system jams, but the boom must be at exactly the right angle when furling or the sail rolls forward and jams.'],
  ['Any amount of reef, from the cockpit, in seconds; no reef points, no folding the sail on the boom, no cover.'],
  ['In-mast: worse sail shape, less area, more weight up the mast, and if it jams half out you cannot get the sail down. Yachting Monthly found most problems came from the sail not furling properly inside the mast; the sailor Pete Goss said he “would never have in-mast furling”.', 'In-boom: expensive, and unforgiving about boom angle.'],
  ['Jams caused by too much halyard tension (vertical creases), the wrong boom angle so the luff does not feed straight, too little outhaul, a baggy old sail, or furling while the sail is flapping. A furling main gets baggier as it ages and jams more.'],
  ['Furl head to wind or just off it, ease the outhaul as you furl and keep a little tension on it; replace the sail when it starts to jam rather than fighting it.'], fold=True)}

{card('rig--furler', 'Headsail furler', 'roller reefing, Furlex, Harken, Profurl, Plastimo', 'A grooved aluminium tube, the foil, fits over the forestay in sections. The sail’s luff slides up the groove; a drum at the bottom turns the foil when you pull the furling line, and a swivel at the top lets the foil rotate under the halyard. Furlex (Seldén), Harken and Profurl are the common makes on this class.',
  ['Pull the furling line and the whole sail rolls up around the foil like a blind; ease it and the sheet pulls the sail out again.', 'The forestay is inside the foil and cannot be seen. Its lower swage lives inside the drum: a rigger should inspect it whenever the mast is down.'],
  ['One sail, made smaller from the cockpit, by one person, in any wind.'],
  ['A partly rolled genoa is a poor sail. Sealed-bearing units (Profurl) are fine until the seals fail, then rust fast; stainless-ball units want a fresh-water rinse.'],
  ['<strong>Halyard wrap</strong>, “the most common cause of furling problems”: if the halyard leaves the swivel at too flat an angle (Seldén asks for 5 to 10 degrees) or is slack, it winds around the foil, locks the furler and can eventually break the forestay. Cures: full halyard tension, a short strop (a length of rope or wire) between the head of the sail and the swivel so the swivel sits close to the masthead, or a halyard deflector on the mast.', 'Loose foil joints and missing screws; a drum full of line that has jumped its groove; a swivel that will not turn; a furling line led at a bad angle that overrides (crosses over itself and jams) on the drum.'],
  ['Never winch a furling line hard: if it will not come, something is wrapped. Look up before you pull.', 'Rinse the drum and swivel, check the foil joints, and have the hidden forestay swage looked at when the rig is down.'], kind='fault', fold=True)}
{sources('reefing and furling', [
  'Slab and single-line (the “more than three-quarters” figure is Practical Sailor’s): ' + a('https://goodoldboat.com/mainsail-reefing-101/','Good Old Boat, mainsail reefing 101') + ', ' + a('https://www.sailboat-cruising.com/Single-Line-Reefing.html','sailboat-cruising.com on single-line reefing') + ', ' + a('https://www.practical-sailor.com/sails-rigging-deckgear/reefing-preferences-from-the-pros/','Practical Sailor, reefing preferences from the pros') + '. When to reef: ' + a('https://www.yachtingmonthly.com/sailing-skills/how-to-reef-to-sail-safely-through-any-weather-74194','Yachting Monthly, how to reef') + ', ' + a('https://www.yachtingmonthly.com/sailing-skills/essential-reefing-tips-for-cruisers-33642','Yachting Monthly, essential reefing tips') + '.',
  'In-mast and in-boom: ' + a('https://www.yachtingmonthly.com/sailing-skills/mainsail-furling-systems-an-expert-guide-75261','Yachting Monthly expert guide') + ', ' + a('https://www.yachtingmonthly.com/sailing-skills/troubleshooting-problems-with-your-yacht-rigging-83649','Yachting Monthly troubleshooting') + ', ' + a('https://www.yachtingmonthly.com/cruising-life/why-i-would-never-have-in-mast-furling-pete-goss-93695','Pete Goss in Yachting Monthly') + ', ' + a('https://www.bavariayachts.com/we-are-bavaria/stories/operate-in-mast-furling-system-correctly/','Bavaria on operating in-mast furling') + ', ' + a('https://www.morganscloud.com/2022/10/09/in-mast-in-boom-or-slab-reefing-convenience-and-reliability/','Attainable Adventure Cruising') + '.',
  'Headsail furlers and halyard wrap: ' + a('https://www.practical-sailor.com/sails-rigging-deckgear/headsail-roller-furlers/','Practical Sailor on roller furlers') + ', ' + a('https://www.pbo.co.uk/gear/headsail-furling-how-to-choose-the-right-system-74554','PBO on choosing a furler') + ', ' + a('https://sailmagazine.com/diy/beat-the-wrap-2/','SAIL, beat the wrap') + ', ' + a('https://theyachtrigger.com/blogs/the-on-deck-channel/halyard-wrap-diagnosis-prevention-and-repair','The Yacht Rigger on halyard wrap') + ', ' + a('https://www.cruisingworld.com/how-to/headsail-furlers-maintenance/','Cruising World on furler maintenance') + '. Forestay failure from twisted furling sails: ' + a('https://www.pantaenius.com/at-en/insights/journal/article/the-most-common-causes-of-rig-failure-1/','Pantaenius') + '.'
])}
{photo('rig-furler-drum.jpg', 'The drum of a headsail furler at the bow of a yacht, above the stemhead fitting, with its line wound on and mooring lines coiled on deck', 'The drum at the foot of a headsail furler, at the bow. Pulling the furling line turns the foil and rolls the sail up.', 'Pierre André', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0', 'https://commons.wikimedia.org/wiki/File:Port_Crouesty_024.jpg', 1280, 1707)}

  <h3>Running rigging and deck gear</h3>
{card('rig--ropes', 'Halyards, sheets and chafe', 'polyester braid, Dyneema', 'Halyards hoist sails, sheets pull them in and out, and both are rope: polyester double braid on most cruising boats, sometimes with a Dyneema core for halyards. Rope does not fail from age as much as from chafe, one spot rubbing on one sheave or one clutch for years.',
  ['Polyester braid grips in clutches and on winches, resists sun, flakes tidily and is cheap. Dyneema (a very strong polyethylene fibre) hardly stretches and is as strong as wire, which suits halyards, but it is slippery in knots and clutches and melts at about 150 °C, so a fast-running winch drum can glaze it.', 'Old masts built for wire halyards have narrow sheaves (the grooved wheels at the masthead) that chew rope; the sheave should match the rope.'],
  ['Cheap, inspectable, replaceable by an owner: tie the new rope to the old and pull it through.'],
  ['Halyards chafe at the masthead sheave and in the rope clutch (the jaw that holds them, see the next card); genoa sheets chafe where they pass through fairleads (guides on the deck edge) and on the shrouds; internal halyards slap in the mast at night.'],
  ['A halyard with a shiny, flattened spot where it sits in the clutch; a fuzzy cover at the masthead exit; a sheet with a hard, glazed patch; a sheave that no longer turns.'],
  ['On passage, ease and re-tension halyards a few centimetres so the same spot does not sit in the clutch; look at the masthead sheaves from up the mast once a season; turn a halyard end for end to double its life.'], fold=True)}

{card('rig--clutches', 'Clutches, lines led aft, winches and lazyjacks', 'rope clutch, stackpack', 'On most boats of this age the halyards and reefing lines have been led aft over the coachroof through rope clutches to a winch by the companionway, so that hoisting and reefing can be done from the cockpit. Lazyjacks are lines from the mast to the boom that catch the mainsail as it drops; a stackpack is a zip-up bag on the boom that the lazyjacks feed.',
  ['A clutch holds a loaded line so the winch can be freed for the next one; it holds far more than a cam cleat (two spring-loaded jaws that grip a rope pulled through them), which is for hand loads, though less than the rope itself will take.', 'Every block (pulley) and deck organiser (a row of small pulleys on the coachroof) on the way aft adds friction, so a line led aft needs more effort or a winch.'],
  ['Safety for a small crew: nobody goes to the mast in strong wind.', 'Lazyjacks and a stackpack make dropping the main a one-person job and keep the deck clear.'],
  ['Friction and clutter; a jammed reefing line at the mast that you now cannot reach.', 'Battens snag in the lazyjacks on the hoist unless the boat is head to wind; a stackpack flaps and can hide the reef cringles.'],
  ['Clutches with worn cams that let the line creep; a winch that spins freely both ways has lost its pawl springs (the small spring-loaded catches inside).'],
  ['Winches are stripped, cleaned and lightly greased once a year; a Lewmar 40 two-speed self-tailing winch (one that grips the rope itself so you can wind with both hands) is typical for the genoa on a 9 to 10 m boat {ONE}. The Deck section covers them further.'], fold=True)}
{sources('running rigging', [
  a('https://www.yachtingmonthly.com/gear/rope-rigging-deck-gear-how-to-choose-the-right-rope-77241','Yachting Monthly, how to choose the right rope') + ', ' + a('https://jimmygreen.com/content/49-running-rigging-rope-fibres-and-construction-explained','Jimmy Green on rope fibres') + ', ' + a('https://www.yachtingworld.com/expert-sailing-techniques/pip-hare-top-tips-preventing-chafe-lines-sails-hardware-125217','Yachting World, Pip Hare on chafe') + ', ' + a('https://forums.sailboatowners.com/threads/do-i-need-new-sheaves-for-all-rope-halyard.159185/','on sheaves for rope halyards') + ' (forum).',
  a('https://sailmagazine.com/diy/know-how-cleats-clutches-and-jammers/','SAIL on cleats, clutches and jammers') + ', ' + a('https://www.upffront.com/blog/guides-4/prepping-your-cockpit-with-clutches-and-deck-organisers-a-sailors-guide-218','Upffront on clutches and organisers') + ', ' + a('https://www.harken.com/en/support/tech-articles/choosing-winches/','Harken on choosing winches') + ', ' + a('https://forums.ybw.com/threads/what-size-of-winch.297673/','YBW on winch size (the Lewmar 40 figure, anecdotal)') + ', ' + a('https://www.modernsailing.com/article/sailing-lazy-jacks-and-stack-packs','Modern Sailing on lazyjacks and stackpacks') + '.'
])}

  <h3>Trim in ten lines</h3>
  <p>Trim is the shape and angle of the sails. Beginners are told a great deal about it; these ten lines are enough for a season.</p>
  <ol>
    <li><strong>Halyard</strong> sets luff tension. Horizontal wrinkles from the luff: too slack. A hard vertical crease along the luff: too tight. More tension moves the deepest part of the sail forward, which you want as the wind rises.</li>
    <li><strong>Outhaul</strong> sets how deep the foot of the main is. Ease it for power in light wind; pull it tight to flatten the sail when it blows.</li>
    <li><strong>Kicker</strong> holds the boom down so the top of the sail does not twist off and spill wind. Sailing away from the wind it is the control that stops the boom lifting in the air.</li>
    <li><strong>Mainsheet and traveller</strong> set the boom’s angle. The traveller lets you move the boom without pulling it down; drop it to leeward in a gust to spill wind without touching the sheet.</li>
    <li><strong>Genoa sheet and car</strong>: the car forward makes the sail fuller and closes the leech; aft flattens the foot and opens the leech. As you roll a furling genoa away, move the car forward.</li>
    <li><strong>Backstay</strong>, if adjustable: tighten in a breeze to flatten both sails, ease in light wind.</li>
    <li><strong>Luff telltales on the genoa</strong> (short ribbons either side of the sail near its front edge): both streaming aft, the sail is right. Windward one lifting: bear away (steer away from the wind) or sheet in. Leeward one stalled and dancing: head up (steer towards the wind) or ease the sheet.</li>
    <li><strong>Leech telltales on the main</strong> should stream; the top one is allowed to stall about half the time when sailing to windward.</li>
    <li><strong>Weather helm</strong> is the boat wanting to turn into the wind. A little is normal and safe. A lot means the main is too powerful: drop the traveller, ease the sheet, flatten with outhaul and halyard, then reef.</li>
    <li><strong>Reef early.</strong> When the boat heels past comfortable, the helm gets heavy or the autopilot struggles, the boat will go just as fast with less sail.</li>
  </ol>
{sources('trim', [
  a('https://sailmagazine.com/diy/mainsail-trim-101/','SAIL, mainsail trim 101') + ', ' + a('https://sailmagazine.com/diy/a-quick-guide-to-sail-trim/','SAIL, a quick guide to sail trim') + ', ' + a('https://www.practical-sailor.com/sails-rigging-deckgear/reading-the-telltales-on-your-sails/','Practical Sailor, reading the telltales') + ', ' + a('https://sailing-blog.nauticed.org/sail-telltales/','NauticEd on telltales') + ', ' + a('https://www.breezada-blog.com/posts/sail-trim-for-beginners-main-jib-cruising-guide','Breezada, sail trim for beginners') + '.'
])}

  <h3>Going up the mast</h3>
  <ul>
    <li>Two halyards: one that lifts you, winched on a self-tailing winch with a clutch as backup, and a second, safety halyard tied to your harness, not to the chair. Tie bowlines (the standard loop knot that cannot slip); do not trust snap shackles with your weight.</li>
    <li>Bounce-test just above the deck. Use halyards that run over the masthead sheaves, not ones on external blocks. Wear a helmet and shoes; tools on lanyards; a phone to send a photo down.</li>
    <li>The person on the winch does nothing else until you are down. A bosun’s chair with a rigid seat and pockets is more comfortable than a harness alone; climbing systems with ascenders (Topclimber, ATN, Mastclimber) let one person go up alone, after practising in harbour.</li>
    <li>What to look at up there, in order: masthead sheaves and the halyard exits; the forestay and backstay terminals and their toggles; the T-terminals or tangs where the cap shrouds meet the mast; the spreader roots and tips; the lower shroud terminals; every split pin. Take photographs of all of it.</li>
  </ul>
{sources('going aloft', [
  a('https://www.yachtingmonthly.com/sailing-skills/mast-climbing-for-shorthanded-crews-72579','Yachting Monthly, mast climbing for short-handed crews') + ', ' + a('https://www.yachtingmonthly.com/gear/7-mast-climbing-methods-and-gear-on-test-84008','Yachting Monthly, seven mast-climbing methods on test') + ', ' + a('https://www.gjwdirect.com/blog/mast-climbing/','GJW Direct on mast climbing') + ', ' + a('https://www.practical-sailor.com/blog/going-aloft-sans-butterflies/','Practical Sailor, going aloft') + ', ' + a('https://www.morganscloud.com/2022/11/18/going-up-the-mast-part-2-fundamentals/','Attainable Adventure Cruising, going up the mast') + '.'
])}

  <h3 id="rig--checklist">The rig in one afternoon: a check from the deck, then aloft</h3>
  <ol>
    <li><strong>Age first.</strong> Ask when the standing rigging was replaced and who did it. No answer means original. Ten years is the working life; a survey will say so.</li>
    <li><strong>Every lower terminal.</strong> Magnifier, straight edge, gloved hand up the wire. Cracks down the swage, proud strands, rust weeping from the top, bent forks.</li>
    <li><strong>Every rigging screw.</strong> Split pins present, opened and taped; toggles at the bottom (both ends on the forestay); nothing leaning or bearing on one side; threads not seized or run out.</li>
    <li><strong>Chainplates.</strong> Rust at the deck plates, soft deck inboard of the shrouds, and the bulkhead behind them from inside the lockers.</li>
    <li><strong>Mast foot.</strong> Deck-stepped: a dip in the coachroof and the compression post below. Keel-stepped: the partners for leaks and, when the mast is out, the heel for corrosion.</li>
    <li><strong>Furler.</strong> Look up at the halyard angle at the swivel; turn the drum by hand; count the foil screws; ask when the forestay inside was last seen.</li>
    <li><strong>Boom.</strong> Gooseneck play, kicker bracket cracks, reefing lines inside the boom, sheaves at the end.</li>
    <li><strong>Sails.</strong> Hoist them. Stitching, UV strip, batten pockets, cringles, and shape: a leech that hooks and a bag that will not flatten mean new sails within the price.</li>
    <li><strong>Then a rigger aloft</strong>: masthead fittings, T-terminals, spreader roots and tips, the backstay’s top end, every split pin. Photographs of everything, dated.</li>
  </ol>

  <h3>Worth watching</h3>
{videos([
 ('yb54_TcQ860', 'How to check your rigging', 'Yachting Monthly', 'A professional rigger walks a deck-level rig check with a screwdriver, a straight edge and a good set of eyes: the exact routine in the checklist above.'),
 ('rqZa3L9P2kg', 'How to inspect your own rigging', 'Rigging Doctor', 'What end-of-life shrouds and terminals look like, from a rigger who replaces them for a living.'),
 ('TEU092iV0ck', 'DIY Sta-Lok standing rigging on an old sailboat', 'Sailboat Story', 'Replacing 38-year-old lower shrouds with mechanical terminals on an Endeavour 32, a boat of the same size and age as the reference fleet.'),
 ('941A-Cg3Z3E', 'How to climb a mast solo at sea', 'Yachting Monthly', 'The ascender kit and routine for going up alone, with the helmet advice most people ignore. A job for an experienced sailor, not a first season.'),
 ('nfXrEbJwRrM', 'How to reef safely and without fuss', 'MDL Marinas, presented by Tom Cunliffe', 'Slab reefing on a cruising yacht demonstrated by a well-known British instructor and author.'),
 ('K4NqjZJSndU', 'How to climb a mast with a bosun’s chair', 'West Marine', 'An assisted climb with two halyards, bowlines rather than shackles, and the bounce test.'),
 ('2EDGdi1lpV4', 'Servicing a Seldén Furlex furler', 'Sailing Yacht Salty Lass', 'A drum and swivel service on the furler fitted to more boats of this class than any other.'),
 ('W0ezqssvuvI', 'How to set a sail and use telltales', 'Phils Watersports', 'A beginner’s telltale lesson that matches the ten trim lines above.'),
])}

  <h3>Terms used in this section</h3>
  <h4 class="terms__group">Rig geometry</h4>
{terms([
 ("rig-mast","Mast","The vertical aluminium spar that carries the sails. Deck-stepped on most of this class; see the mast cards for the two ways of standing it up."),
 ("rig-boom","Boom","The horizontal spar along the foot of the mainsail, hinged to the mast at the gooseneck. At head height, and it swings across the boat without warning in a gybe."),
 ("rig-forestay","Forestay","The wire from the top of the mast (or, on a fractional rig, part way up) to the bow. It holds the mast forward and carries the headsail, usually inside a furler foil."),
 ("rig-backstay","Backstay","The wire from the masthead to the stern. It holds the mast aft and, on a masthead rig, sets the tension of the forestay."),
 ("rig-cap-shroud","Cap shrouds","The side wires from the masthead over the spreader tips to the chainplates. The main sideways support of the mast."),
 ("rig-lower-shroud","Lower shrouds","Shorter side wires from the spreader roots to the deck, one forward and one aft each side on most boats, that hold the middle of the mast and set its pre-bend."),
 ("rig-spreaders","Spreaders","Struts part way up the mast that hold the cap shrouds out so that they pull at a wider angle. One pair on almost every boat of this class."),
 ("fractional-hounds","Hounds","The point on a fractional rig where the forestay meets the mast, below the top. A 7/8 rig has its hounds seven-eighths of the way up."),
 ("dim-i","I","The height of the foretriangle: from the deck by the mast to where the forestay meets the mast. Sailmakers size headsails and storm jibs from it."),
 ("dim-j","J","The base of the foretriangle: from the front of the mast at deck level to the forestay fitting on the bow. Genoa overlap is a percentage of J."),
 ("dim-p","P","The mainsail luff length: from the top of the boom to the highest point the head may be hoisted to (the black band on the mast)."),
 ("dim-e","E","The mainsail foot length, from the mast to the black band on the boom. Mainsail area is roughly half of P times E."),
 ("rake","Rake","The whole mast leaning aft, one to two degrees on a cruising boat, which gives a little weather helm."),
 ("pre-bend","Pre-bend","A slight forward bow in the middle of the mast, set by the lower shrouds, so the mast cannot bow the wrong way under load."),
 ("forestay-sag","Forestay sag","The forestay bowing to leeward under the pull of the headsail. More backstay tension means less sag and a flatter, higher-pointing genoa."),
 ("mast-pumping","Pumping and inversion","Pumping: the middle of the mast flexing fore and aft in waves. Inversion: the mast bowing aft in the middle. Both mean the lowers or babystay are slack, and inversion can bring a fractional mast down."),
 ("running-backstays","Running backstays and checkstays","Removable backstays, set up on the windward side and let go on each tack, that support a fractional mast from behind; checkstays are lighter ones to the middle of the mast that stop pumping. Racing gear, rare on this fleet."),
])}
  <h4 class="terms__group">Standing rigging</h4>
{terms([
 ("rig-wire","1×19 wire","Stainless-steel rigging wire of nineteen strands twisted into one: stiff, low-stretch, 5 to 7 mm on this class. Dyform is the same idea with compacted strands; rod is a solid bar."),
 ("swage","Swaged terminal","A stainless sleeve squeezed onto the end of a wire by a rigger’s machine. Strong, neat, and impossible to inspect inside."),
 ("swage-crack","Swage cracks and meat hooks","The two visible signs of a dying terminal: hairline cracks running down the sleeve, and broken strands standing proud where the wire enters."),
 ("mechanical-terminal","Mechanical terminal","A screw-together end fitting (Sta-Lok, Norseman, Hi-Mod) that clamps the wire’s strands over a cone. Fitted with hand tools, reusable and inspectable."),
 ("rigging-screw-body","Rigging screw","The threaded barrel at the bottom of each wire that tensions it: a bottlescrew in Britain, a turnbuckle in America. Locked with split pins or wire."),
 ("toggle","Toggle","A small hinge between the rigging screw and the chainplate that lets the wire swing so it is never bent at its terminal."),
 ("clevis-pin","Clevis pin","The stout cross-pin that joins a fork to an eye, held in by a split pin."),
 ("split-pin","Split pin","The bent wire pin (a cotter pin) that stops a clevis pin walking out. The smallest part of the rig and the one that keeps the mast up. Never re-use one."),
 ("chainplate-strap","Chainplate","The stainless strap the shroud attaches to, passing through the deck and bolted to a bulkhead or knee. The place a Moody or a Sadler leaks."),
 ("chainplate-leak","Chainplate leak","Water past the cover plate on deck into the balsa core and the plywood bulkhead below, hidden until the deck goes soft or the strap corrodes in the slot."),
 ("t-terminal","T-terminal and tang","A T-shaped fitting (also called a T-ball) on the mast end of a shroud that hooks into a slot in the mast wall; the older alternative is a tang, a strap riveted to the mast that the shroud pins to. Check for wear in the slot and cracking at the neck."),
 ("spreader-root","Spreader root","Where the spreader meets the mast. It must not move; cracks in the bracket and play in the root are common causes of rig failure."),
 ("spreader-tip","Spreader tip","The outer end of the spreader, where the cap shroud is clamped or seized to it and covered with a boot so the genoa does not chafe."),
 ("crevice-corrosion-rig","Crevice corrosion (rigging)","Stainless steel rusting from inside a tight, wet, airless gap: the top of a swage, the slot round a chainplate, under a cover plate. A rust stain is the warning."),
 ("babystay","Babystay","A short inner forestay from part way up the mast to the foredeck that stops the middle of the mast pumping. The 2002 Gib’Sea 33 has one."),
])}
  <h4 class="terms__group">Mast and boom</h4>
{terms([
 ("mast-step-plate","Mast step plate","The plate on the coachroof that a deck-stepped mast stands in; halyards exit the mast just above it."),
 ("compression-post","Compression post","The pillar or bulkhead under a deck-stepped mast that carries its downward load to the keel."),
 ("deck-compression","Dished deck","A sunken area around the mast step: the core under the plate has got wet and crushed, or the post below has given."),
 ("partners","Partners","The reinforced hole in the deck that a keel-stepped mast passes through, packed with wedges or Spartite and covered by a boot."),
 ("mast-heel","Mast heel and step","The bottom of a keel-stepped mast and the fitting on the keel floors it stands on."),
 ("mast-heel-corrosion","Heel corrosion","Aluminium at the mast heel rotting where rain that ran down inside the mast pools against stainless fastenings and bilge water. Only visible with the mast out."),
 ("gooseneck-fitting","Gooseneck","The two-way hinge joining the boom to the mast. High loads, worn pins."),
 ("ctl-kicker","Kicker (vang)","The strut or tackle from the foot of the mast to the boom that pulls the boom down. A rigid kicker also holds it up."),
 ("ctl-topping-lift","Topping lift","The line from the masthead to the boom end that holds the boom up when the sail is down."),
])}
  <h4 class="terms__group">Sails</h4>
{terms([
 ("rig-mainsail","Mainsail","The sail set on the mast and boom: the one with the reefs in it and the one you shape most."),
 ("rig-genoa","Genoa","A headsail big enough to overlap the mast; a jib is one that does not. Sized as a percentage of J."),
 ("sail-head","Head","The top corner of a sail. On a mainsail it carries a stiff plate, the headboard, that the halyard shackles to."),
 ("sail-tack","Tack","The front lower corner of a sail: at the gooseneck on the main, at the furler drum on the genoa."),
 ("sail-clew","Clew","The back lower corner, where the outhaul (main) or the sheets (genoa) attach."),
 ("luff","Luff","The front edge of a sail: on the mast for the main, on the forestay for the genoa. Its tension comes from the halyard."),
 ("leech","Leech","The back, free edge of a sail. Where a tired sail hooks and a good one streams."),
 ("foot","Foot","The bottom edge of a sail; on the mainsail it runs along the boom."),
 ("roach-area","Roach","The curved extra area of the mainsail outside a straight line from head to clew, held out by the battens. In-mast furling sails have none."),
 ("sail-battens","Battens","Stiff strips in pockets across the mainsail that support the roach and stop the leech flapping. Full-length battens run right to the mast."),
 ("reef-cringle","Reef cringles and points","Reinforced eyes at luff and leech for each reef, with short ties (reef points) between them to bundle the spare sail."),
 ("leech-line","Leech line","A thin cord sewn into the leech that is tightened just enough to stop the edge fluttering."),
 ("sail-telltales","Leech telltales","Ribbons on the mainsail leech that should stream aft; the top one may stall half the time to windward."),
 ("luff-telltales","Luff telltales","Ribbons either side of the genoa near its luff that show whether the sail is at the right angle to the wind: both streaming is right."),
 ("ctl-cunningham","Cunningham","A cringle a little above the tack with a tackle that tensions the luff without touching the halyard."),
 ("uv-strip","UV strip","A sacrificial strip of acrylic or polyester along the leech and foot of a furling genoa that faces the sun when the sail is rolled. The first part of the sail to rot."),
 ("sail-cloth-term","Dacron and laminates","Dacron is woven polyester, the cheap, tough, shape-losing cloth on almost all cruising sails; laminates are lighter and hold shape but die sooner."),
 ("blown-out","Blown out","A sail that has stretched into a deep bag with its draft aft and a hooked leech: more heel, more weather helm, less speed."),
 ("overlap","Overlap","How far a genoa reaches past the mast, given as a percentage of J: 100% is a jib, 130 to 135% the usual cruising genoa, 150% a light-air sail."),
 ("storm-sails","Storm jib and trysail","A small, flat, heavy headsail and a small mainsail-substitute on its own track, for gales. Sized by rule of thumb from I and from P and E."),
 ("cruising-chute","Cruising chute","An asymmetric spinnaker cut for short-handed sailing, set from the bow without a pole and handled through a snuffer (a sock)."),
])}
  <h4 class="terms__group">Reefing and furling</h4>
{terms([
 ("rams-horn","Ram’s horn","The curved hook at the gooseneck that the luff reef cringle drops over when slab reefing."),
 ("reefing-pennant","Reefing line","The line from the end of the boom up through the leech reef cringle and back down, which pulls the back of the sail down to the boom."),
 ("reef-bundle","Reef bundle","The slab of sail below a reef, folded onto the boom and tied loosely with the reef points."),
 ("inmast-section","In-mast furling","A mainsail that rolls up inside a hollow, slotted mast. Convenient; no roach; jams if it is furled badly or the sail is old."),
 ("mandrel","Mandrel","The rod inside a furling mast or boom that the sail rolls around."),
 ("inmast-jam","Furling jam","A furling mainsail stuck half in and half out because the roll was loose or creased; the reason some sailors refuse in-mast furling."),
 ("furler-foil","Furler foil","The grooved aluminium tube over the forestay that the genoa’s luff slides up and that rotates to roll the sail."),
 ("furler-drum","Furling drum","The spool at the bottom of the foil that the furling line winds on and off."),
 ("halyard-swivel","Halyard swivel","The bearing at the top of the foil that lets the sail and foil turn while the halyard stays still."),
 ("halyard-wrap","Halyard wrap","The commonest furler fault: a halyard leaving the swivel at too flat an angle winds round the foil, jams the furler and can eventually break the forestay."),
])}
  <h4 class="terms__group">Running rigging and controls</h4>
{terms([
 ("ctl-halyard","Halyard","The rope that hoists a sail: main, genoa and spinnaker halyards. Sets luff tension once the sail is up."),
 ("ctl-outhaul","Outhaul","The line that pulls the clew of the mainsail out along the boom: tighter is flatter."),
 ("ctl-mainsheet","Mainsheet","The tackle that pulls the boom in and lets it out. The line you touch most."),
 ("ctl-traveller","Traveller","A track across the cockpit or coachroof that the mainsheet block slides along, moving the boom sideways without pulling it down."),
 ("genoa-sheet","Genoa sheets","The two ropes, one each side, from the genoa’s clew back through a car on the track to the primary winches."),
 ("genoa-car","Genoa car","The sliding block (a pulley on a slider) on the side-deck track that sets the sheet angle. Forward for a fuller sail, aft for a flatter one."),
 ("tackle","Tackle","A rope led back and forth through two blocks (pulleys) so that one pull moves the load with several times the force: the mainsheet, the kicker and a backstay adjuster are all tackles."),
 ("dyneema","Dyneema","A very strong, very low-stretch polyethylene fibre used in halyard cores. Slippery and melts at about 150 °C."),
 ("rope-clutch","Rope clutch","A lever-operated jaw that holds a loaded line so that the winch can be used for another."),
 ("lazyjacks-stackpack","Lazyjacks and stackpack","Lines from the mast to the boom that catch the falling mainsail, and the zip-up bag on the boom they feed."),
 ("bosuns-chair","Bosun’s chair","The seat you are winched up the mast in. Always with a second, safety halyard tied to your harness."),
])}

  <div class="planned">
    <p>Planned for this section</p>
    <ul>
      <li>Photographs of faults: a cracked swage, meat hooks, a corroded mast heel, a leaking chainplate, halyard wrap (still to be found under a CC licence)</li>
      <li>I, J, P and E for the Moody 33 and the Gib’Sea 33, spar makers for the Bavaria 1060 and Finnsailer 35, and how each is stepped</li>
    </ul>
  </div>
</section>
'''
finish(page, ROOT + 'sections/04-rig.html', others=(ROOT + 'sections/03-hull.html', ROOT + 'sections/02-fleet.html', ROOT + 'sections/00-start.html'))
