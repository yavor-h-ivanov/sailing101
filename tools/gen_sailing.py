# Generates sections/09-sailing.html for Sailing 101.
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_common import *
import gen_sailing_diagrams as g


page = f'''<section id="sailing">
  <h2>Sailing fundamentals</h2>
  <p class="lead">A sail is a wing, not a bag. Once that idea lands, points of sail, trim and heel all make sense, and the two manoeuvres that frighten beginners, tacking and gybing, become routine. This section is the handling side of the boat; the parts are in <a href="#rig">Rig and sails</a>. In a hurry? Jump to <a href="#sailing--mob">man overboard</a>, <a href="#sailing--tacking">tacking</a>, <a href="#sailing--gybing">gybing</a> or <a href="#sailing--when-to-reef">when to reef</a>.</p>

  <details class="first-words" open>
    <summary>Nine words before anything else</summary>
    <dl>
      <dt>Windward and leeward</dt><dd>Windward is the side the wind comes from; leeward (said “loo-ard”) is the side it blows towards.</dd>
      <dt>Port tack and starboard tack</dt><dd>On port tack the wind comes over the port (left) side and the boom is out to starboard; on starboard tack, the other way round.</dd>
      <dt>Head up and bear away</dt><dd>To head up is to turn the bow towards the wind; to bear away is to turn it away.</dd>
      <dt>Sheet in and ease</dt><dd>To pull a sail in with its sheet, or let it out.</dd>
      <dt>Luffing</dt><dd>A sail flapping at its front edge because it is not sheeted in far enough, or the boat is pointing too close to the wind.</dd>
      <dt>Heel</dt><dd>The boat leaning over under the wind’s pressure.</dd>
      <dt>Helm</dt><dd>The tiller or wheel, and the person steering.</dd>
      <dt>Sailing by the lee</dt><dd>Running with the wind coming slightly from the same side as the boom: one step from an accidental gybe.</dd>
      <dt>Knots and Beaufort</dt><dd>Wind speed in knots (nautical miles an hour), or as a Beaufort force from 0 (calm) to 12 (hurricane).</dd>
    </dl>
    <p class="first-words__note">Tack, gybe, head to wind and the other verbs are also in the <a href="#rig--sailing-words">box at the top of Rig and sails</a>.</p>
  </details>
  <p class="conf-key"><b>Marks used below:</b> {ONE} single source; {TWO} sources disagree or anecdotal; {TBC} not yet verified. <b>How this section was checked:</b> in September 2026 the techniques and figures were checked by web search against the pages linked in the “Sources and confidence” blocks. The search results were read, but the pages themselves could not be opened from the editing session. What each Beaufort force means on a boat of this class is guidance, not a rule.</p>

  <h3>Points of sail</h3>
  <p>A boat’s heading relative to the wind has a name, and each name comes with a sail setting. A sailing boat cannot sail straight into the wind: the closest a cruising yacht of this class can point is about 45° either side of it, a little more, 50° or so, for a heavy long-keeled boat like the Finnsailer. To reach a place upwind, you zigzag, tacking from one side of the no-go zone to the other.</p>

{figure('fig-pos', 'points of sail', '0 0 900 640', 'The points of sail around the wind', 'A circle of boats seen from above, the wind blowing from the top. A pink sector about 45° either side of the wind is the no-go zone. Around the circle, on each side: close-hauled at about 45° with the sails pulled in tight, close reach, beam reach with the wind at 90°, broad reach with the wind behind the beam, and at the bottom a run with the wind dead astern and the sails right out. Boats on the right are on port tack with their booms to starboard; boats on the left on starboard tack with their booms to port. Arrows show heading up, towards the wind, and bearing away from it.', g.points_of_sail(), 'The rule of the sheets: the closer to the wind, the further in the sails; the further from the wind, the further out. The boom is always on the leeward side.', note=HINT)}

  <h4>Where is the wind?</h4>
  <p>Everything in this section starts from the wind’s direction, so find it first and keep checking it. Look at the arrow on the masthead (the wind indicator), the wind instrument’s pointer, or short pieces of wool tied to the shrouds; turn your face until you feel the wind equally on both cheeks and hear it equally in both ears; and look at the ripples on the water, which run with the wind. On a moving boat the masthead arrow, the instrument, the wool and your face all show the apparent wind, explained below; the ripples on the water show the true wind.</p>

  <h3>How a sail works</h3>
  <p>Close-hauled and on a reach, air flows round both sides of the curved sail as it does round an aircraft wing, and the sail is pulled to leeward and slightly forward. The keel stops the boat going sideways, so it goes forward instead; that is how a boat can sail at 45° to the wind. Running with the wind behind, the sail is simply pushed along. Trimming a sail means setting it at the angle, and with the curve, that keeps the air flowing smoothly over both sides.</p>

{figure('fig-sail-lift', 'sails as wings', '0 0 900 420', 'How a sail makes lift, and how the jib’s telltales show it', 'Left: a boat close-hauled on port tack, seen from above, the wind from the top. Airflow lines pass either side of the curved jib and mainsail. A blue arrow shows the total force from the sails, mostly sideways to leeward and a little forward; a green arrow its forward part, the drive; a red arrow the keel pushing back to windward. Right: three close-ups of a jib’s front edge with a blue telltale on the windward side and a red one, dashed, on the leeward side: both streaming when the sail is trimmed right; the windward one lifting when too close to the wind; the leeward one lifting when too far off it.', g.sail_lift(), 'Telltales are the cheapest instrument on the boat. The mnemonic: move the tiller towards the telltale that is misbehaving (on a wheel, turn away from it), or trim the sheet to cure it.')}

{compare('The sail controls and what they do', ['Control', 'What it does', 'Pull in, tighten or move to windward', 'Ease, or move to leeward'], [
  ['Sheets (jib and main)', 'set the sail’s angle to the wind', 'when the sail luffs, or you head up', 'when you bear away, or the leeward telltale lifts'],
  ['Genoa car on its track', 'sets where the jib sheet pulls from', 'move it forward when the top of the jib luffs first', 'move it aft when the bottom luffs first, or to spill wind from the top in a blow'],
  ['Mainsheet traveller', 'moves the boom across the boat without changing its twist (how far the top of the sail falls away to leeward of the bottom)', 'to windward in light wind, so the boat can sail a little closer to the wind', 'to leeward in a gust, to reduce heel'],
  ['Kicker (vang)', 'holds the boom down, which controls the twist', 'on a reach or run, to stop the boom lifting', 'close-hauled in light wind, to let the top of the sail open'],
  ['Outhaul', 'flattens or deepens the foot of the mainsail', 'flatter, in a stronger wind', 'fuller, in light wind and waves'],
  ['Halyard tension and cunningham', 'set the tension along the front edge', 'as the wind rises, or wrinkles run along the luff', 'as the wind drops'],
  ['Backstay (where adjustable)', 'bends the mast and tightens the forestay', 'for flatter sails upwind in a breeze', 'downwind and in light wind'],
], wide=True, stack=True)}
{figure('fig-twist', 'twist', '0 0 900 480', 'Twist in the mainsail, and what the sheet, kicker and traveller do to it', 'Three views of a mainsail from above, the boat outlined faintly with the bow at the top and the wind from the upper left. In each, three curved lines show the sail at the foot, the middle and the head. Left: an open leech, the head falling well away to leeward of the boom. Middle: a closed leech, the three lines nearly in line. Right: the same sail before and after the traveller is let down to leeward: all three lines swing out together, by about ten degrees, and keep the same spread.', g.twist(), 'The leech is the sail’s back edge; the kicker (or vang) is the rope or strut that holds the boom down. Upwind, the mainsheet sets the twist and the traveller sets the angle; off the wind, once the boom is out past the traveller, the kicker holds the boom down and sets the twist.', note=HINT)}
  <p>What the controls do, as parts, is in <a href="#rig--mainsail">Rig and sails</a>. On a cruising boat the sheets, the car and the traveller do most of the work; the rest is fine-tuning.</p>

  <h3>True wind and apparent wind</h3>
  <p>A moving boat makes its own wind, just as a cyclist feels a breeze on a still day. The wind you feel on board, and that the sails use, is the apparent wind: the true wind combined with the wind of the boat’s motion. Sailing upwind the apparent wind is stronger than the true wind and comes from further ahead; sailing downwind it is lighter, and still from a little further forward. That is why a run feels calm and warm, and why the wind seems to rise sharply when you turn to beat back home.</p>

{figure('fig-apparent', 'apparent wind', '0 0 900 390', 'How true wind and boat speed make the apparent wind', 'Two panels, the true wind blowing from the top of the page at 12 knots, each with a boat on port tack sailing at 6 knots and a triangle of arrows beside it. Left, close-hauled, the boat heading up and to the right, 45° off the wind: the true-wind arrow points down the page; the arrow of wind from the boat’s own motion points opposite to the boat’s heading; their sum, the apparent wind, is about 17 knots at about 30° off the bow. Right, on a broad reach, the boat heading down and to the right, 135° off the wind: the apparent wind is about 9 knots at about 106° off the bow.', g.apparent(), 'Worked for 12 knots of wind and 6 knots of boat speed (our arithmetic): close-hauled, the apparent wind is about 17 knots, 30° off the bow; on a broad reach, about 9 knots, 106° off the bow. The masthead instrument shows the apparent wind; the true wind is calculated.')}

  <h3 id="sailing--tacking">Tacking and gybing</h3>
  <p>Both are changes from one tack to the other. In a <strong>tack</strong> the bow turns through the wind; the sails flap for a few seconds and the jib is moved across. In a <strong>gybe</strong> the stern turns through the wind; the sails stay full, and the boom swings across the boat, which is why a gybe must be controlled.</p>

{figure('fig-tack-gybe', 'tacking and gybing', '0 0 900 440', 'The steps of a tack and a gybe', 'Two panels, the wind from the top. Left, a tack in four numbered positions: close-hauled on port tack; turning towards the wind after the call “Lee-oh”; head to wind with the sails flapping and the old jib sheet let off; close-hauled on the new, starboard tack with the jib sheeted in on the new side. Right, a gybe in four positions: on a broad reach on port tack; mainsheet hauled in so the boom is near the middle; stern through the wind with the boom crossing a short distance after the call “Gybe-oh”; eased out on the new tack.', g.tack_gybe(), 'The commands are a conversation: the helm asks, the crew answer “Ready”, and only then does the helm turn. Nobody’s head is in the boom’s path at the moment it crosses.')}

  <ol>
    <li><strong>Tacking.</strong> The jib has two sheets, one to each side: the <em>working</em> sheet is the one pulling the sail now, on the leeward side; the <em>lazy</em> sheet is slack, on the windward side, and becomes the working sheet after the tack. Helm: “Ready about?” Crew: take the working sheet out of its self-tailer or cleat and hold it, with its turns still on the winch, ready to let it go; put a couple of turns of the lazy sheet on the other winch. Crew: “Ready.” Helm: “Lee-oh”, and turns steadily towards the wind: on a tiller, push it away from you, to leeward; on a wheel, turn the wheel towards the wind, to windward.</li>
    <li>As the jib starts to flap, let the old sheet go completely. Keep turning through the wind until the sails fill on the new side and the boat is close-hauled again.</li>
    <li>Pull in the new jib sheet quickly while it is still slack, then winch the last of it; the mainsail looks after itself. Helm settles on the new course and checks the telltales.</li>
  </ol>
  <ol id="sailing--gybing">
    <li><strong>Gybing.</strong> Look to leeward first: the new course must be clear. Helm: “Stand by to gybe.” Crew: check everyone’s head is clear of the boom’s path and the mainsheet is free to run; take the preventer off if one is rigged; then answer “Ready”. In a strong wind, consider tacking round instead: a longer turn, but no boom crossing under load.</li>
    <li>Bear away slowly towards a run, turning away from the wind: on a tiller, pull it towards you, to windward; on a wheel, turn the wheel away from the wind, to leeward. Haul the mainsheet in until the boom is near the middle of the boat.</li>
    <li>Helm: “Gybe-oh”, and turns the stern through the wind. The boom crosses a short distance under control. Ease the mainsheet out quickly on the new side and steer to stop the boat rounding up; move the jib across.</li>
  </ol>

{card('sailing--accidental-gybe', 'The accidental gybe', 'crash gybe, sailing by the lee, preventer', 'On a run, if the helm lets the stern swing through the wind, or a wave throws it there, the boom crosses the whole width of the boat in a second, at head height, with all the wind’s force behind it. It is one of the commonest causes of serious injury on a sailing yacht {TWO}.',
  ['The danger is greatest dead downwind, and worst of all when sailing by the lee, with the wind coming slightly from the same side as the boom. A <strong>preventer</strong>, a line from the end of the boom forward to the bow and back to the cockpit, holds the boom out so that it cannot cross.'],
  ['Entirely avoidable: sail a broad reach instead of a dead run, rig a preventer, and gybe on purpose, under control.'],
  ['A preventer that cannot be released from the cockpit is itself dangerous: if the boat heels hard with the boom held out, the boom can dip in the water. Every crew member must know how to let it go.'],
  ['The boom lifting and the mainsail starting to collapse on a run (the wind is getting round behind it); the helm steering by the compass and forgetting the wind; a wave slewing (swinging) the stern round.'],
  ['On a run, keep the wind a few degrees off dead astern, rig a preventer, and keep heads below the boom’s height.'], kind='fault', fold=True)}
{sources('tacking and gybing', [
  'Tacking commands and sheet handling: ' + a('https://www.safe-skipper.com/tacking-a-sailing-boat/','Safe Skipper, tacking a sailing boat') + ', ' + a('https://en.wikipedia.org/wiki/Tacking_(sailing)','Wikipedia, tacking') + '.',
  'Preventers and the accidental gybe: ' + a('https://www.yachtingmonthly.com/sailing-skills/how-to-rig-a-preventer-and-boom-brake-our-expert-guide-98591','Yachting Monthly, rigging a preventer and boom brake') + ', ' + a('https://www.yachtingworld.com/expert-sailing-techniques/boom-preventers-125154','Yachting World, boom preventers') + '.',
  'Pointing angles: ' + a('https://en.wikipedia.org/wiki/Point_of_sail','Wikipedia, point of sail') + ', ' + a('https://sailingvirgins.com/blog/mastering-points-of-sail','Sailing Virgins, points of sail') + '.',
  'Checked by web search, September 2026; the pages could not be opened directly.',
])}

  <h3>Heel, balance and reefing</h3>
{figure('fig-balance', 'balance and heel', '0 0 900 390', 'Balance between sails and keel, and why a boat heels and comes back up', 'Two panels. Left, a side view with the sails’ centre of effort marked on the sails and the centre of lateral resistance marked on the keel; when the push of the sails is centred behind the keel’s resistance, the boat tries to turn into the wind. Right, a view from astern of a boat heeled by the wind: ballast low in the keel pulls down, and buoyancy, moved to the low side, pushes up, together turning the boat upright.', g.balance(), 'A ballasted keelboat resists heel more and more strongly as it heels, up to a large angle well beyond normal sailing heel; past that angle the push back weakens, and a boat knocked down beyond its angle of vanishing stability by a breaking wave will not come back up until another wave rolls it. In normal sailing, heel slows the boat, makes it hard to steer and wears out the crew; in rough weather, keep the hatches and the companionway closed so that a knockdown cannot flood the boat.')}

{card('sailing--weather-helm', 'Weather helm and being overpowered', 'rounding up, too much heel', 'A little weather helm, a gentle pull on the tiller or wheel as the boat tries to turn into the wind, is normal and makes a boat safe: let go and it heads into the wind and stops. Too much means the boat is carrying too much sail for the wind.',
  ['As the wind rises the boat heels more; heeled, the hull’s shape and the sails’ push both turn it towards the wind, and the rudder has to work harder to hold it straight. In a gust it may turn right up into the wind against the rudder (rounding up).'],
  ['The cure is simple and immediate: ease the mainsheet or the traveller in the gust, then reef.'],
  ['A boat carrying too much sail is slower, not faster: it heels, the rudder drags, and it skids sideways.'],
  ['The helm needing both hands; the rail (the edge of the deck) under water; the boat rounding up in gusts; the crew tired and wet.'],
  ['Most cruising yachts of this class sail best at moderate heel, around 10° to 20°; if you are regularly beyond 20° or so, reef: the boat will be faster as well as more comfortable.'], kind='fault', fold=True)}

  <h4 id="sailing--when-to-reef">When to reef</h4>
  <p>The old rule is the best one: reef when you first think about it, and before you have to. Reefing is easier and safer early, in harbour or in the lee of land (its sheltered side, where the land blocks the wind), than late in a rising wind. The mechanics of slab reefing and furling are in <a href="#rig--slab-reefing">Rig and sails</a>.</p>
{compare('The Beaufort scale and what it means on a 10 m cruising yacht', ['Force', 'Wind (knots)', 'Name', 'The sea', 'On a boat of this class (guidance)'], [
  ['0–1', 'under 4', 'calm, light air', 'flat, ripples', 'motor, or drift'],
  ['2', '4–6', 'light breeze', 'small wavelets', 'full sail, slow sailing'],
  ['3', '7–10', 'gentle breeze', 'large wavelets, a few white horses (breaking crests)', 'full sail; the best sailing for beginners'],
  ['4', '11–16', 'moderate breeze', 'small waves, frequent white horses', 'full sail or a first reef; the boat heels and goes well'],
  ['5', '17–21', 'fresh breeze', 'moderate waves, many white horses', 'first or second reef, part of the genoa furled'],
  ['6', '22–27', 'strong breeze', 'large waves, white foam crests, spray', 'second or third reef, small headsail; hard work for a new crew'],
  ['7', '28–33', 'near gale', 'sea heaps up, foam in streaks', 'deep reefs; not a wind to set out in'],
  ['8', '34–40', 'gale', 'moderately high waves, long streaks of foam', 'stay in harbour'],
], wide=True, stack=True)}
  <p>A forecast wind is an average; gusts are commonly 40% stronger, and in showers and squalls can be twice the average. Plan the sail for the gusts. Reef before turning upwind: running, the wind you feel is lighter than the true wind, and it rises sharply as you turn. The Navigation section covers forecasts.</p>

  <h3>Heaving to</h3>
{figure('fig-heave-to', 'heaving to', '0 0 900 320', 'A yacht hove to', 'A yacht seen from above on starboard tack, the wind from the top, lying about 50° off the wind. The jib is held on the windward side, pushing the bow away from the wind; the mainsail is eased and pushes the bow back up; the tiller is lashed to leeward. The boat drifts slowly, mostly to leeward.', g.heave_to(), 'Heaving to stops the boat without taking the sails down: for lunch, for reefing, for sorting out a problem, or to wait for daylight off a harbour.', start=0.5)}
  <ol>
    <li>Sailing close-hauled, tack, but do not let the jib sheet go: the jib stays sheeted on the old side, now the windward side (backed).</li>
    <li>Let the boat slow down; ease the mainsheet until the boat lies quietly at about 45° to 60° off the wind.</li>
    <li>Put the tiller to leeward and lash it there (on a wheel, turn it to windward and lock it). The backed jib pushes the bow off, the main and the rudder push it back up, and the boat balances, moving slowly forward and drifting to leeward.</li>
    <li>To sail on, free the tiller, let the jib sheet go and sheet it in on the other side, and bear away.</li>
  </ol>
  <p>Every boat heaves to a little differently; practise in a moderate breeze and find the settings for yours. Make sure there is plenty of sea room (open water with nothing to hit) to leeward.</p>

  <h3 id="sailing--mob">Man overboard</h3>
  <div class="callout danger">
    <p><strong>The moment someone goes over</strong> (the first steps happen together, shared out among the crew):</p>
    <ol>
      <li><strong>Shout “Man overboard!”</strong> so the whole crew knows.</li>
      <li><strong>Throw</strong> the lifebuoy and the danbuoy (a floating pole with a flag) towards the person, at once.</li>
      <li><strong>Point:</strong> one crew member does nothing but watch the person and point, all the time. A head in the waves is lost from sight in seconds.</li>
      <li><strong>Press the MOB button</strong> on the plotter or GPS to mark the position; send a DSC distress alert and a Mayday (see <a href="#electronics--mayday">Electronics</a>); the coastguard would rather stand down (call off the rescue) than arrive late.</li>
      <li><strong>Stop the boat near them</strong> with the quick stop: tack at once without letting the jib sheet go, so that the boat stops, hove to, close to the person.</li>
      <li><strong>Roll away the jib, pull the mainsail in to the middle, and check every rope is out of the water</strong>, then start the engine; keep the person in sight.</li>
      <li><strong>Come back slowly</strong>, nearly into the wind for the last part (or on a close reach under sail, easing the sheets to slow down), and stop with the person alongside on the leeward side, just forward of the cockpit and clear of the propeller {TWO} (some schools teach a windward pickup instead: agree one on your boat and practise it). Out of gear, and the engine stopped (killed) if you can, whenever the person is near the propeller.</li>
      <li><strong>Get them aboard</strong> with a lifting sling (a padded loop that goes under their arms, on a line to a halyard and a winch), or a boarding ladder; a person in wet clothes is far heavier than you think, and may be too cold to help.</li>
      <li><strong>Nobody goes into the water after them.</strong> A second person in the water is a second casualty.</li>
    </ol>
  </div>
{figure('fig-mob', 'man overboard', '0 0 900 490', 'The quick-stop man-overboard manoeuvre, seen from above', 'The wind blows from the top. 1: a yacht on a beam reach has just passed a person in the water, with a lifebuoy and a danbuoy thrown beside them. 2: the yacht has tacked at once without releasing the jib sheet and lies hove to, a short way to windward of the person. 3: a dashed line under engine runs from the hove-to boat away downwind, round in a loop and back. 4: the yacht has come back slowly and stopped about 25° off the wind, jib rolled away and mainsail in the middle, with the person alongside on its leeward side, just forward of the cockpit.', g.mob_quick_stop(), 'The quick stop keeps the boat close to the person: the tack stops it within a few boat lengths, and the engine brings it back. Keep pointing at the person the whole time.', note=HINT, start=0.4)}
  <h4 id="sailing--mob-under-sail">If the engine will not start: reach, tack, reach</h4>
  <p>With a rope round the propeller or an engine that will not start, come back under sail. Put the boat on a beam reach away from the person, with one crew pointing at them all the time, and sail a few boat lengths; tack, letting the jib flap or rolling it away; bear away to get downwind of them; then come up onto a close reach towards them. A close reach is the point of sail where you can slow down by easing the sheets and speed up by pulling them in, so you can creep up and stop with the person on the leeward side. If you end up head to wind below them, the boat stalls and drifts back: bear away, sail off and try again. It takes more room and more skill than the quick stop, so practise both.</p>
{figure('fig-mob-rtr', 'reach, tack, reach', '0 0 900 470', 'The reach–tack–reach man-overboard return under sail', 'The wind blows from the top. A person is in the water on the left. 1: a yacht sails away from them on a beam reach. 2: it tacks, head to wind with the sails flapping. 3: it bears away on a broad reach to get downwind of the person. 4: it rounds up onto a close reach and approaches the person slowly, sheets eased, with the person on its leeward side.', g.mob_reach_tack_reach(), 'The final approach is on a close reach, never head to wind: from there you can slow down, stop and, if it goes wrong, sail away.', note=HINT, start=0.3)}
  <p>Prevention is worth all of it: lifejackets on deck, harnesses clipped to the jackstays at night and in rough weather (see <a href="#deck--guardrails">Deck hardware</a>), one hand for yourself and one for the boat, and never relieving yourself over the side. Cold water takes the breath away in the first minute, before any swimming; a lifejacket keeps the head up through it. Practise the drill with a fender and a bucket on a line until the whole crew can do it.</p>

  <h3>Who gives way: the first rules</h3>
  <p>The full rules are in <a href="#navigation">Navigation</a>. The four a beginner needs on the first day come from the collision regulations (Rules 12(a), 13 and 18, Rule 17 for the stand-on vessel and Rule 9 for narrow channels). The boat that does not have to give way is the stand-on vessel: it must hold its course and speed, and must act itself if the other boat does not.</p>
  <ul>
    <li><strong>Port gives way to starboard:</strong> of two sailing boats on different tacks, the one on port tack keeps clear.</li>
    <li><strong>Windward gives way to leeward:</strong> of two on the same tack, the one to windward keeps clear.</li>
    <li><strong>The overtaking boat keeps clear</strong>, sail or power.</li>
    <li><strong>Power usually gives way to sail</strong>, but not a vessel fishing, a vessel restricted in its ability to manoeuvre, a vessel not under command, or one constrained by its draught; and a sailing boat under 20 m must not impede a ship that can only navigate in a narrow channel. A sailing boat motoring or motor-sailing (engine driving the propeller) is a power-driven vessel. Keep clear of anything big, early and obviously.</li>
  </ul>
{sources('heel, reefing, heaving to, man overboard and right of way', [
  'Heel and reefing: ' + a('https://www.spinnakersailing.com/optimal-angle-of-heeling/','Spinnaker Sailing, optimal angle of heel') + ', ' + a('https://www.morganscloud.com/jhhtips/sail-heal-angle/','Attainable Adventure Cruising, heel angle') + '; stability: ' + a('https://marine.marsh-design.com/content/understanding-monohull-sailboat-stability-curves','Marsh Marine Design, stability curves') + '.',
  'The Beaufort scale: ' + a('https://www.spc.noaa.gov/faq/tornado/beaufort.html','NOAA, Beaufort wind scale') + ', ' + a('https://www.dayskippertheory.co.uk/learn/meteorology/the-beaufort-scale','Day Skipper Theory, the Beaufort scale') + '. Gusts: ' + a('https://www.yachtingmonthly.com/sailing-skills/how-to-cope-with-gusts-and-squalls-74973','Yachting Monthly, gusts and squalls') + ', ' + a('https://www.bom.gov.au/resources/learn-and-explore/marine-knowledge-centre/wind-gusts-and-squalls','Bureau of Meteorology, wind, gusts and squalls') + '.',
  'Heaving to: ' + a('https://www.pbo.co.uk/seamanship/heaving-to-a-question-of-balance-87553','Practical Boat Owner, heaving to') + ', ' + a('https://en.wikipedia.org/wiki/Heaving_to','Wikipedia, heaving to') + '.',
  'Man overboard: ' + a('https://www.rya.org.uk/water-safety/man-overboard','RYA, man overboard') + ', ' + a('https://en.wikipedia.org/wiki/Man_overboard','Wikipedia, man overboard (quick stop and reach-turn-reach)') + ', ' + a('https://www.pbo.co.uk/seamanship/man-overboard-video-32081','Practical Boat Owner, reach-tack-reach') + ', ' + a('https://www.pbo.co.uk/seamanship/man-overboard-turns-getting-back-to-the-casualty-in-the-water-104939','Practical Boat Owner, man overboard turns') + '.',
  'Right of way: COLREGs Rules 9, 12, 13, 17 and 18, ' + a('https://www.navcen.uscg.gov/navigation-rules-amalgamated','USCG, International and Inland rules') + '.',
  'Checked by web search, September 2026; the pages could not be opened directly.',
])}

  <h3 id="sailing--first-sail">Your first sail: a crew briefing</h3>
  <ol>
    <li>Lifejackets: one each, fitted and done up; where the harnesses are and when to clip on.</li>
    <li>Where the lifebuoy, danbuoy, throwing line (a floating line in a bag, thrown to a person in the water) and MOB button are; who points.</li>
    <li>The boom’s path: where not to stand when tacking and gybing.</li>
    <li>How to start and stop the engine, and where the fuel and raw-water seacocks are.</li>
    <li>The VHF: channel 16, the DSC button and the Mayday card.</li>
    <li>The heads and the gas: the routines in <a href="#systems">Boat systems</a>.</li>
    <li>“One hand for yourself”: move along the high side, holding on, and stay low.</li>
    <li>Seasickness: tell the skipper early, stay on deck and look at the horizon.</li>
  </ol>

  <h3>Worth watching</h3>
{videos([
 ('agWYQ2YGiGg', 'Tacking and gybing by Yachting Monthly', 'Motor Boat & Yachting (a Yachting Monthly film)', 'Yachting Monthly’s short guide to both turns on a cruising yacht, posted on the Motor Boat &amp; Yachting channel.'),
 ('yuxCH_6tXko', 'Man overboard under sail: the quick-stop method', 'practicalboatowner', 'The quick stop filmed from a drone, so you can see the shape of the turn. Schools teach versions of it; compare it with the steps above.'),
 ('uQTOfns6OjU', 'How to heave to in a yacht: Skip Novak’s storm sailing', 'Yachting World', 'A very experienced high-latitude skipper on heaving to, as a storm tactic as well as a pause.'),
 ('xlexzR3yPKA', 'Man overboard under sail: the reach–tack–reach method', 'practicalboatowner', 'The other method many schools teach. Know both, and agree one for your boat.'),
 ('bnpcrjin7tc', 'Man overboard crew training: prevent, practise, prepare', 'Royal Yachting Association - RYA', 'The RYA on keeping people on board, and on practising the drill.'),
 ('_RQzQor7_vU', 'Heaving to', 'Stress Free Sailing with Duncan Wells', 'Heaving to as a way to stop and park the boat, from an instructor and author.'),
 ('HA5tEV2MNcI', 'How to tack and gybe safely: essential sailing manoeuvres', 'Sail & Motor Cruising Channel', 'A second take on the two turns, from a series of RYA skipper-skills tips.'),
 ('Er9iw7q_E_8', 'How to reef quickly and easily: Skip Novak’s storm sailing', 'Yachting World', 'Slab reefing, from the same series; there is another reefing video in <a href="#rig">Rig and sails</a>.'),
])}

  <h3>Terms used in this section</h3>
  <h4 class="terms__group">Points of sail</h4>
{terms([
 ("pos-wind","True wind","The wind as it blows over the water. In the plan views of this section it always blows from the top of the page."),
 ("pos-no-go","No-go zone","The sector about 45° either side of the wind that no sailing boat can sail into; you tack across it."),
 ("pos-close-hauled","Close-hauled","Sailing as close to the wind as the boat will go, about 45° off it, with the sails pulled in tight. Sailing upwind this way in a series of tacks is beating."),
 ("pos-close-reach","Close reach","Between close-hauled and a beam reach, the sails a little eased."),
 ("pos-beam-reach","Beam reach","The wind at 90° to the boat, on the beam; the sails about halfway out. Often the fastest point of sail."),
 ("pos-broad-reach","Broad reach","The wind behind the beam, the sails well out; fast and comfortable."),
 ("pos-run","Run","The wind dead astern, the sails right out; the boat rolls and the risk of an accidental gybe is highest."),
 ("pos-port-tack","Port tack","Sailing with the wind coming over the port side; the boom is out to starboard."),
 ("pos-starboard-tack","Starboard tack","Sailing with the wind coming over the starboard side; the boom is out to port. Against a boat on port tack it is the stand-on vessel: it holds its course and speed, and acts only if the other does not."),
 ("pos-head-up","Head up","Turn the bow towards the wind (also: luff up)."),
 ("pos-bear-away","Bear away","Turn the bow away from the wind."),
])}
  <h4 class="terms__group">Sails, wind and balance</h4>
{terms([
 ("sl-sails","Sails as wings","Curved sails set at a small angle to the wind, which the air flows round on both sides."),
 ("sl-flow","Airflow","The wind flowing smoothly round both sides of each sail when it is trimmed right."),
 ("sl-force","Total sail force","The push of the wind on the sails: mostly sideways to leeward, a little forward, when close-hauled."),
 ("sl-drive","Drive","The forward part of the sail force, which moves the boat ahead."),
 ("sl-keel-force","Keel force","The water’s push on the keel, to windward, which stops the boat going sideways."),
 ("leeway","Leeway","The small sideways slip of a boat through the water as it sails, a few degrees close-hauled."),
 ("tt-good","Telltales streaming","Both telltales flowing straight aft: the sail is trimmed right."),
 ("tt-windward","Windward telltale lifting","You are too close to the wind: bear away, or sheet in."),
 ("tt-leeward","Leeward telltale lifting","You are too far off the wind: head up, or ease the sheet."),
 ("aw-true","True wind arrow","The wind as it blows over the water."),
 ("aw-motion","Wind of the boat’s motion","The breeze the boat makes by moving, from dead ahead, equal to its speed."),
 ("aw-apparent","Apparent wind","The true wind and the boat’s own wind combined: what the crew and sails feel, and what the masthead instrument shows."),
 ("bl-ce","Centre of effort","The point where the sails’ total push is centred."),
 ("bl-clr","Centre of lateral resistance","The point where the hull and keel’s resistance to being pushed sideways is centred."),
 ("bl-weather-helm","Weather helm","The boat’s tendency to turn into the wind, felt as a pull on the helm; a little is normal, a lot means reef."),
 ("bl-heel-force","Heeling force","The sideways push of the wind that leans the boat over."),
 ("bl-ballast","Ballast","The lead or iron in the keel, low down, whose weight pulls the boat upright."),
 ("bl-buoyancy","Buoyancy","The water’s upward push, centred in the middle of the hull’s underwater shape, which moves to the low side as the boat heels."),
])}
  <h4 class="terms__group">Manoeuvres</h4>
{terms([
 ("tg-ready-about","“Ready about?”","The helm’s warning before a tack; the crew answer “Ready” when both jib sheets are prepared."),
 ("tg-lee-oh","“Lee-oh”","The helm’s call as the tack begins (the tiller goes to leeward)."),
 ("tg-head-to-wind","Head to wind","The moment in a tack when the bow points straight into the wind and the sails flap."),
 ("tg-new-tack","The new tack","Close-hauled on the other side, the jib sheeted in on the new side."),
 ("tg-stand-by","“Stand by to gybe”","The helm’s warning before a gybe: heads clear of the boom, preventer off."),
 ("tg-sheet-in","Mainsheet in","Hauling the boom towards the middle before a gybe, so that it only crosses a short way."),
 ("tg-gybe-oh","“Gybe-oh”","The helm’s call as the stern passes through the wind and the boom crosses."),
 ("tg-ease-out","Ease out","Letting the mainsheet out quickly on the new side after a gybe."),
 ("ht-backed-jib","Backed jib","A jib held on the windward side, as when hove to; the wind pushes it the wrong way and turns the bow off."),
 ("ht-main-eased","Eased mainsail","Let out when hove to, so that it balances the backed jib."),
 ("ht-helm-lashed","Helm lashed to leeward","When hove to, the tiller tied to the leeward side (a wheel turned to windward), so the rudder tries to turn the boat into the wind."),
 ("ht-drift","Drift when hove to","The slow movement of a hove-to boat, mostly to leeward, leaving a slick of smooth water to windward."),
 ("danbuoy","Danbuoy","A floating pole with a flag, thrown to a person overboard so that they can be seen from further away."),
])}
  <h4 class="terms__group">Twist</h4>
{terms([
 ("tw-open","Open leech","A mainsail with plenty of twist: the top falls away to leeward and spills wind. Ease the sheet upwind, or the kicker off the wind."),
 ("tw-closed","Closed leech","A mainsail with little twist: the top stays in line with the boom, for power upwind. Pulled too tight, the top stalls."),
 ("tw-traveller","Traveller let down","Moving the mainsheet traveller to leeward swings the whole sail out without changing its twist: the quick way to spill a gust."),
])}
  <h4 class="terms__group">Man overboard</h4>
{terms([
 ("mob-person","Person in the water","Keep them in sight, and keep pointing: a head in the waves disappears within seconds."),
 ("mob-shout","Shout, throw, point","The first seconds of a man overboard: shout to the crew, throw the lifebuoy and danbuoy, point at the person, press the MOB button, and send a Mayday."),
 ("mob-quick-stop","Quick stop","Stopping the boat close to a person in the water by tacking at once and leaving the jib sheeted, so that the boat heaves to."),
 ("mob-engine","Engine on, ropes in","Before the engine goes into gear: the jib rolled away, the mainsail pulled in to the middle, and every rope checked out of the water, so that none can foul the propeller."),
 ("mob-approach","Final approach","Slowly, nearly into the wind, stopping with the person alongside on the leeward side, just forward of the cockpit and clear of the propeller; in neutral, and the engine stopped if you can."),
 ("rtr-person","Person in the water (under sail)","The person being recovered; approach so that they end up on the leeward side."),
 ("rtr-away","Beam reach away","The first leg of a reach–tack–reach return: a few boat lengths away from the person on a beam reach."),
 ("rtr-tack","Tack, jib flapping","The turn at the end of the first leg, letting the jib flap or rolling it away so that it does not drive the boat."),
 ("rtr-downwind","Getting downwind","Bearing away after the tack so that the final approach can be made on a close reach from downwind of the person."),
 ("rtr-close-reach","Close-reach approach","The final approach under sail, on a close reach, easing the sheets to slow down and stopping with the person to leeward."),
])}

</section>
'''
finish(page, ROOT + 'sections/09-sailing.html', others=(ROOT + 'sections/03-hull.html', ROOT + 'sections/04-rig.html', ROOT + 'sections/05-deck.html', ROOT + 'sections/06-engine.html', ROOT + 'sections/07-systems.html', ROOT + 'sections/08-electronics.html', ROOT + 'sections/02-fleet.html', ROOT + 'sections/00-start.html'))
