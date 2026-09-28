# Generates sections/10-manoeuvres.html for Sailing 101.
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_common import *
import gen_manoeuvres_diagrams as g
import gen_knots_diagrams as kn


page = f'''<section id="manoeuvres">
  <h2>Manoeuvres under engine</h2>
  <p class="lead">Nobody is watching when you sail beautifully offshore. Everybody is watching when you berth. A five-tonne boat with one propeller, no brakes and a keel that wants to pivot behaves nothing like a car, and berthing it is learnable: slowly, with a plan, with the crew briefed, and with the wind and tide on your side. In a hurry? Jump to <a href="#manoeuvres--alongside">coming alongside</a>, <a href="#manoeuvres--med">stern-to</a> or <a href="#manoeuvres--briefing">the crew briefing</a>.</p>

  <details class="first-words" open>
    <summary>Nine words before anything else</summary>
    <dl>
      <dt>Prop walk</dt><dd>The sideways kick of the stern when the propeller turns, strongest in astern.</dd>
      <dt>Pivot point</dt><dd>The point the boat turns about, about a third of the way back from the bow when going ahead.</dd>
      <dt>Steerage way</dt><dd>Enough speed through the water for the rudder to work. Below it, the boat does not steer.</dd>
      <dt>Warps and springs</dt><dd>Warps are mooring lines. Springs are the two that run diagonally and stop the boat moving forward or back.</dd>
      <dt>Fenders</dt><dd>Air-filled cushions hung over the side between the boat and the pontoon or another boat.</dd>
      <dt>Windage</dt><dd>How much the wind pushes the boat: the bow, with little keel under it, blows off fastest.</dd>
      <dt>Slip a line</dt><dd>Let go a line that is doubled back on board, so it can be pulled in without anyone ashore.</dd>
      <dt>Way</dt><dd>The boat’s movement through the water. “Keep a little way on” means keep moving slowly; “gathering way”, speeding up.</dd>
      <dt>Take a turn</dt><dd>Wrap a line once round a cleat or bollard. The friction lets one person hold a heavy boat, and the line can still be eased.</dd>
    </dl>
  </details>
  <p class="conf-key"><b>Marks used below:</b> {ONE} single source; {TWO} sources disagree or anecdotal; {TBC} not yet verified. <b>How this section was checked:</b> in September 2026 the techniques and figures were checked by web search against the pages linked under “Sources and confidence”. The search results were read, but the pages themselves could not be opened from the editing session. Methods that come mainly from sailors’ forums are marked {TWO}.</p>

  <h3>The physics you must accept</h3>
{figure('fig-prop-walk', 'prop walk and pivot', '0 0 900 380', 'Prop walk in astern, and the pivot point when turning ahead', 'Two panels seen from above. Left: a boat, bow up the page, going astern; a red arrow at the stern shows it kicking to port, which is what a right-handed propeller does. Right: a boat turning to starboard going ahead, pivoting about a point a third of its length back from the bow; its stern swings out much further than its bow swings in.', g.prop_walk(), 'Which way your boat walks depends on its propeller’s hand; the drawing shows the common right-handed case. Find out on your own boat in open water before you need it.', note=HINT)}
  <ul>
    <li><strong>Prop walk.</strong> In astern the propeller pushes the stern sideways before the boat starts to move. A right-handed propeller (clockwise seen from astern when going ahead) walks the stern to port. It is strong on shaft drives and long keels, weaker on saildrives.</li>
    <li><strong>The pivot point</strong> is about a third of the way aft from the bow going ahead, and moves aft going astern. Turning ahead, the stern swings out: leave room for it beside pontoons and other boats.</li>
    <li><strong>No water flow, no steering.</strong> At very low speed the rudder does nothing. A short burst of ahead (a “kick”) over the rudder turns the stern without building speed.</li>
    <li><strong>Wind on the bow</strong> blows it off faster than you can correct at low speed. Wind and tide decide your approach, not your preference: approach into whichever is stronger. A tide from ahead keeps water flowing past the rudder while you stop over the ground, so the boat still steers; a wind from ahead slows the boat and keeps the bow from blowing off, but gives no steering.</li>
    <li><strong>Keel type matters.</strong> Fin-keel boats, such as the Bavaria 1060 on its saildrive, steer well astern once moving; a long-keel boat (Finnsailer 35) barely steers astern at all and turns wide.</li>
  </ul>

{card('manoeuvres--prop-walk-test', 'Finding your boat’s prop walk', 'right-handed, left-handed, paddle wheel effect', 'Prop walk is also called the paddle wheel effect: the propeller acts a little like a paddle wheel at the stern. Ten minutes in open water with no wind tells you more than any book. Do it before the first time you berth the boat.',
  ['With the boat stopped, put the engine astern at moderate revs and watch the stern: the way it kicks is the way it will always kick. Then try going ahead from stopped with the rudder central, and turning a full circle each way ahead and astern.'],
  ['Once known, prop walk is a tool: berth on the side the stern walks towards, and a burst astern both stops the boat and pulls the stern in.'],
  ['On the wrong side, a burst astern throws the stern away from the pontoon just as you step off.'],
  ['A boat whose owner does not know which way it walks; a propeller changed for one of the other hand after a new engine, so the old habits are wrong.'],
  ['Write the answer on a card by the engine controls: “walks to port in astern”.'], fold=True)}

  <h3>Lines, fenders and knots</h3>
{figure('fig-mooring-lines', 'mooring lines', '0 0 900 340', 'The four mooring lines of a boat alongside a pontoon', 'A boat alongside a pontoon, seen from above, bow to the right. A bow line runs forward from the bow to the pontoon and a stern line aft from the stern. A spring from the bow leads aft to the pontoon and stops the boat moving forward; a spring from the stern leads forward and stops it moving back. Fenders hang between the hull and the pontoon at the widest part.', g.mooring_lines(), 'Bow and stern lines hold the boat in; the springs stop it surging forward and back. In a marina with little tide, short lines and springs keep the boat still; where the tide rises and falls a lot, lines must be long enough to allow for it.')}
  <ul>
    <li><strong>Lines:</strong> at least four, each longer than the boat, plus two longer ones for springs and awkward berths; about 12 to 14 mm on a boat of this size (a common rule is a millimetre of diameter per foot of length), braided polyester or nylon {TWO} (nylon stretches more and absorbs snatching in a swell). Chafe where they pass through fairleads kills them.</li>
    <li><strong>Fenders:</strong> four to six, sized for the boat (makers’ guides give about 200 to 250 mm diameter for a 10 m yacht), and a fender board (a plank hung outside the fenders, so they roll on it and not on the posts) for rough walls. Hang them at the height of the pontoon, not the waterline, and adjust them before arriving.</li>
    <li><strong>Knots:</strong> the <strong>bowline</strong> (a loop that will not slip or jam: the loop of a mooring line), the <strong>round turn and two half hitches</strong> (to a ring or post, and can be undone under load), the <strong>clove hitch</strong> (quick, for fenders on a guardrail; it can slip on a smooth wire, so add a half hitch), and the <strong>cleat hitch</strong> (a turn, figures of eight and a locking turn on a cleat). Learn them from the drawings below, a sailing school or a video until your hands tie them in the dark.</li>
  </ul>
{figure('fig-knots-loops', 'bowline and clove hitch', '0 0 900 400', 'The bowline and the clove hitch', 'Two drawings. Left, a bowline: the standing part comes down from the top into a small loop, with the part towards the end lying on top. The end, drawn in orange, comes up through the small loop from behind, goes round behind the standing part, and goes back down through the small loop, finishing inside the big loop below. Right, a clove hitch on a guardrail, with a fender hanging from it: the line goes up over the rail, round it, crosses diagonally over itself, goes round again, and the end comes out upwards under the diagonal, so the diagonal traps both parts.', kn.knots_loops(), 'The bowline’s mnemonic: the rabbit (the end) comes up out of the hole, runs round the back of the tree (the standing part), and goes back down the hole. Pull it tight by the standing part against the loop. A clove hitch can work loose if the load pulls from different directions: add a half hitch, or use a round turn and two half hitches instead.')}
{figure('fig-knots-hitches', 'round turn and cleat hitch', '0 0 900 400', 'A round turn and two half hitches, and a cleat hitch', 'Two drawings. Left, a round turn and two half hitches on a rail: the line comes up from below, goes twice round the rail, then down, and makes two half hitches round its own standing part, both tied the same way; the end is in orange. Right, a cleat hitch seen from above: the line from the boat is led to the far horn first, takes a full turn round the base of the cleat, crosses diagonally over the top in a figure of eight round the horns, and finishes with a locking turn whose end, in orange, lies under the last diagonal, alongside the one beneath.', kn.knots_hitches(), 'The round turn takes the strain, so the half hitches can be tied, or untied, while the line is under load. On a cleat, one full turn and one or two figures of eight are enough; a heap of extra turns is slower to cast off and no stronger.')}

  <h3 id="manoeuvres--alongside">Coming alongside</h3>
{figure('fig-alongside', 'coming alongside', '0 0 900 340', 'Coming alongside a pontoon port side to, into the wind', 'A pontoon at the bottom left, the wind or tide from the left. A boat approaches from the right at a shallow angle in three positions: approaching slowly; in neutral, turning to lie parallel as the bow nears the pontoon; and stopped alongside with a short burst astern, which with a right-handed propeller also kicks the stern to port, towards the pontoon, shown by a red arrow.', g.alongside(), 'Slow is safe: at walking pace a mistake is usually a job for the fenders, not the repair yard, but a five-tonne boat still hits hard, so slower is better. Go round again as often as it takes; there is no prize for the first attempt.')}
  <ol>
    <li><strong>Plan</strong> on the way in: which side, which lines, where the wind and tide come from, where to stop. Fenders and lines ready on that side. Each line is led “outside everything”: from its cleat out through the fairlead and over the top of the guardrails, not under them, so it runs straight to the shore without snagging.</li>
    <li><strong>Brief</strong> the crew: who steps off with which line, and in what order (see <a href="#manoeuvres--briefing">the briefing</a>).</li>
    <li><strong>Approach</strong> into the wind or tide, whichever is stronger, at a shallow angle and at the slowest speed that still steers.</li>
    <li><strong>Neutral early</strong>; steer to lie parallel as the bow reaches the pontoon; a short burst astern to stop.</li>
    <li><strong>Step off, never jump</strong>, with the midships line (a line from a cleat near the middle of the boat, which holds both ends in at once) or the bow line, and take a turn round a cleat at once; then the bow and stern lines, then the springs.</li>
    <li>Never put a hand or foot between the boat and the pontoon to fend off. Let the fenders do it.</li>
  </ol>
  <p><strong>Wind blowing off the pontoon</strong>: come in at a steeper angle and a little faster, get the midships line on at once, and hold the boat in with gentle ahead against it, steering away from the pontoon (tiller pushed towards it, wheel turned away from it), while the other lines go on. <strong>Wind blowing onto the pontoon</strong>: stop parallel to it about a boat’s width off, and let the wind blow you down onto the fenders.</p>
{card('manoeuvres--blown-off', 'Blown off the pontoon', 'bow blowing off, missed line', 'One of the commonest berthing failures: the boat stops, the crew is not yet ashore, and the wind takes the bow away from the pontoon faster than anyone can pull it back.',
  ['At walking pace the bow, with little keel under it, has nothing to hold it against the wind; within seconds the gap is too wide to step.'],
  ['Nobody is hurt if nobody jumps: motor away, go round, and come in again with a new plan.'],
  ['A crew member who jumps the gap, or holds on to a line as the boat moves away, can end up in the water between the boat and the pontoon.'],
  ['A long approach in neutral in a crosswind; the crew waiting at the bow instead of amidships; lines not ready.'],
  ['Come in steeper and a little faster, step off amidships with the midships line, and hold the boat in against it with gentle ahead.'], kind='fault', fold=True)}

  <h3>Leaving a berth: springing off</h3>
{figure('fig-springing', 'springing off', '0 0 900 360', 'Springing the stern or the bow out from a pontoon', 'Two panels, bow to the right, the pontoon at the bottom. Left: a bow spring runs from the bow aft to the pontoon, a fender at the bow; the boat motors gently ahead against it, steering towards the pontoon, and its stern swings out. Right: a stern spring runs from the stern forward to the pontoon, a fender at the quarter; the boat motors gently astern against it and its bow swings out.', g.springing(), 'Springing off is the answer when the wind pins the boat to the pontoon. The spring, doubled back so it can be slipped from on board, does the work; the engine only needs gentle revs.')}
  <ol>
    <li>Take off every line except the one spring you need (the stern line and the other spring last, just before you start); double it back (round the pontoon cleat and back to the boat) so it can be slipped.</li>
    <li>A fender at the point that will press on the pontoon: the bow for a bow spring, the quarter for a stern spring.</li>
    <li><strong>Stern out:</strong> gently ahead against the bow spring, steering as if to turn towards the pontoon (on a tiller, push it away from the pontoon; on a wheel, turn it towards the pontoon): the stern swings out. When it points well clear, neutral, slip the spring, and reverse out.</li>
    <li><strong>Bow out:</strong> gently astern against the stern spring: the bow swings out. When clear, neutral, slip the spring, and motor ahead.</li>
    <li>Get the slipped line aboard fast, before it finds the propeller.</li>
  </ol>
  <h4>An ordinary departure</h4>
  <p>When the wind is light or blowing you off the pontoon, no spring is needed. Start the engine and let it warm up; take off the slack lines first, and leave until last the one or two that are taking the load (usually those leading upwind or up-tide), doubled back so they can be slipped from on board. Let the wind or a little ahead take the boat clear, slip the last lines, get them aboard, and bring the fenders in once you are well clear.</p>
{card('manoeuvres--prop-fouled', 'A line round the propeller', 'fouled prop, wrapped shaft', 'A mooring line, a lazy line or a dropped sheet that finds the propeller winds itself round the shaft in a second and stops the engine, usually at the worst moment.',
  ['Ropes in the water near the stern, and the engine in gear. Slipped lines, lazy lines and dinghy painters are the usual culprits.'],
  ['Prevention is simple: every line out of the water before the engine goes into gear; neutral whenever a line is near the stern.'],
  ['Once wrapped, the engine stalls and the boat has no power; in a harbour it drifts onto whatever is downwind. Cutting the line free usually means going into the water, which is for a diver or a calm day, not for a beginner.'],
  ['The engine labouring and stopping just after a line was let go; a line from the stern that will not pull in.'],
  ['Neutral at once, stop the engine, and do not try to restart it in gear. Get a line ashore or drop the anchor to stop the drift, then call for help: the marina or a tow. Outside a harbour you still have the sails; if you are drifting into danger, a Pan-Pan (see Electronics). On a shaft drive a loose wrap can sometimes be cleared by turning the shaft by hand, with the engine stopped {TWO}.'], kind='fault', fold=True)}

  <h3 id="manoeuvres--finger">Marina finger berths</h3>
  <p>Most northern European marinas have short floating fingers between boats. Going in bow first {TWO}: fenders on both sides, a midships line ready on the finger’s side; motor in slowly and stop with a burst astern as the bow nears the main pontoon; the crew steps onto the finger by the shrouds, not the bow, and puts the midships line on the finger’s outer (after) cleat, where it stops the boat going further forward. That only works if the cleat is aft of the boat’s middle cleat; on a very short finger, use a stern line to it instead. Then a bow line to the main pontoon, a stern line, and springs.</p>
  <p>Reversing out: take the lines off except the midships line, and let prop walk choose the first move. In astern the stern will kick one way before the boat moves (to port with a right-handed propeller), so the bow will end up pointing the other way (to starboard); plan the turn in the fairway that way round, and keep the rudder straight until the boat gathers sternway; then it steers. The crew can walk the boat back along the finger, holding a shroud, and step aboard by the shrouds while the finger is still alongside, before the boat gathers way.</p>
{figure('fig-finger', 'finger berth', '0 0 900 440', 'Going bow first into a finger berth', 'Seen from above, the main pontoon along the bottom and two short floating fingers standing up from it, each about two-thirds of a boat long. A yacht has motored in along a dashed arrow and lies bow down towards the main pontoon, with the left finger on its starboard side and a neighbouring yacht on its port side, fenders on both sides. A thick line runs from the middle of the boat back to the cleat at the outer end of the finger, and a crew member stands on the finger by the shrouds. Two bow lines go to the main pontoon, a stern line to the finger’s outer cleat, and two dashed springs to its middle cleat.', g.finger_berth(), 'The midships line is the one that matters: put it on first, and the boat can no longer reach the main pontoon. Fingers are short and bouncy, so step off where the boat is widest.', note=HINT)}
{photo('manoeuvres-marina-fingers.jpg', 'A marina full of yachts and motor boats moored side by side on pontoons with short fingers between them', 'Newhaven Marina, on the English Channel: boats on pontoons, each with a short finger alongside.', 'Paul Gillett', 'CC BY-SA 2.0', 'https://creativecommons.org/licenses/by-sa/2.0', 'https://commons.wikimedia.org/wiki/File:Newhaven_Marina_-_geograph.org.uk_-_1758189.jpg', 1280, 960)}

  <h3 id="manoeuvres--turning">Turning in a narrow fairway</h3>
{figure('fig-turn-tight', 'turning in a fairway', '0 0 900 410', 'Turning a boat round in a narrow fairway with short bursts ahead and astern', 'Seen from above: a fairway between two rows of berthed boats. A boat turns clockwise on the spot, shown in four overlapping positions, from bow to the left to bow to the right. Labels give the steps: helm hard to starboard and a short burst ahead; neutral and a burst astern, in which prop walk kicks the stern to port; repeat; turned round in little more than its own length.', g.turn_tight(), 'Turn the way prop walk helps: to starboard with a right-handed propeller. Short, firm bursts are the key: each one turns the boat without moving it far.')}
  <p>Helm hard to starboard means the wheel turned to starboard, or the tiller pushed to port. Hold the helm firmly in the bursts astern, or the rudder will slam over. Practise it in open water first, with a fender in the water to mark your spot. A long-keel boat like the Finnsailer needs more room and more bursts; a fin-keel boat can often turn in its own length.</p>

  <h3 id="manoeuvres--med">Stern-to with lazy lines</h3>
{figure('fig-med-moor', 'stern-to mooring', '0 0 900 424', 'Mooring stern-to a quay with a lazy line', 'Seen from above, the quay at the bottom and a ground chain lying along the harbour bed near the top. Three boats lie stern-to the quay side by side. The middle one has two crossed stern lines to bollards on the quay and a heavy mooring line from the ground chain made fast at its bow; a thin lazy line runs from the quay out to the mooring line, and has been picked up at the stern and walked forward to the bow. Fenders hang on both sides.', g.med_moor(), 'Common in the Mediterranean, Adriatic and Aegean. The marina’s staff often hand you the lazy line from a dinghy or the quay.')}
  <ol>
    <li>Fenders out on both sides, stern lines ready at the stern (one each side), the passerelle (a gangplank from the stern to the quay) or a plank ready, and someone with a boathook (a pole with a hook on the end, for picking up lines).</li>
    <li>Line up the gap well out, then reverse in slowly and straight; prop walk will try to swing the stern, so start the approach allowing for it and use short bursts ahead to correct.</li>
    <li>A crew member steps ashore or passes the stern lines to the marina staff, to be put round bollards (short posts on the quay) or rings; in a crosswind the windward line first. Take a turn on board at once.</li>
    <li>Pick up the lazy line at the stern, walk it forward outside the guardrails and everything else, and pull the heavy mooring line up to a bow cleat until the boat is held off the quay. Keep the lazy line out of the propeller: neutral while it is being lifted near the stern; then gentle ahead to hold the boat off the quay while the crew tightens the mooring line.</li>
    <li>Adjust the stern lines so the stern is a step or a plank’s length from the quay.</li>
  </ol>
  <p>Where there are no lazy lines, the boat lays its own anchor: drop it three to five boat lengths out, reverse in paying out chain, take the stern lines ashore, then tighten the chain. Bows-to is the same with the anchor off the stern, and gives more privacy from the quay; it is the better choice for a long-keel boat like the Finnsailer, which barely steers astern: going astern, the propeller’s wash runs past the long keel and hardly reaches the rudder.</p>

  <h3>Box berths between posts</h3>
{figure('fig-box-berth', 'box berth', '0 0 900 420', 'Entering a box berth between posts', 'Seen from above, the quay at the top. A boat enters bow first between two posts at the outer end of its box. Stern lines run from each quarter to the posts, the loops dropped over them as the boat passes; bow lines run from the bow to the quay. Arrows show a crosswind from the left.', g.box_berth(), 'Box berths with posts are common all over northern Europe: in Dutch, German and Danish harbours, and in Scandinavia. The trick is the stern lines: they go over the posts as you pass, before the bow reaches the quay.')}
  <ol>
    <li>Prepare two long stern lines with a big loop in each, and two bow lines; fenders are rarely needed, except at the bow.</li>
    <li>Choose a box the right width: boxes are marked with the maximum beam or length on the posts in some harbours, and an empty box may show a green sign (you may use it) or a red one (the owner is coming back).</li>
    <li>Enter slowly, bow first; as the stern passes the posts, drop the loop over the windward post first, then the leeward one; the helm keeps a little way on.</li>
    <li>Use the stern lines as brakes: the crew surges them (lets them slip slowly round a cleat under tension) to slow the boat before the bow reaches the quay, as well as a burst astern.</li>
    <li>The crew steps ashore from the bow with the bow lines; the bow is often high above the quay, so step down carefully. Then tighten the stern lines so the boat is held off the quay.</li>
  </ol>

  <h3>Mooring buoys, anchoring and rafting</h3>
  <ul>
    <li><strong>Picking up a buoy:</strong> approach slowly into the wind or tide, whichever is stronger, so the boat stops at the buoy; the crew on the bow points at it, because the helm loses sight of it under the bow. Pick it up with a boathook and pass your own line through the buoy’s ring or strop, never tie to the small pick-up buoy alone.</li>
    <li><strong>Anchoring:</strong> choose a spot with room to swing, the right depth and a good seabed on the chart; approach heading the way the boats already anchored nearby are lying (into whichever is stronger, wind or tide); stop; lower the anchor to the bottom and pay out chain as the boat drifts back (how much is in <a href="#deck--chain">Deck hardware</a>); set it with a gentle burst astern; then check it holds, with a transit on the beam (two landmarks in line, watched for a steady shift) or the plotter’s anchor alarm.</li>
    <li><strong>Swinging room:</strong> at anchor the boat swings round the anchor in a circle whose radius is about the length of chain let out plus the boat’s length; so do the boats near you, which may have different amounts of chain.</li>
    <li><strong>Rafting up:</strong> alongside another boat, with fenders between, your own bow and stern lines to the shore or pontoon as well as lines to the other boat, and springs; the biggest boat on the inside. Cross the other boat by its foredeck, never its cockpit.</li>
  </ul>
{figure('fig-buoy', 'picking up a buoy', '0 0 900 360', 'Picking up a mooring buoy', 'Seen from above, wind or tide from the top. A yacht approaches a red mooring buoy from below, shown faintly further back and again at the buoy, and stops with the buoy at its bow. A crew member on the bow points at the buoy. The small pick-up buoy floats beside the mooring buoy on a short line.', g.buoy_pickup(), 'Approach against whichever is stronger, wind or tidal stream, so that it stops the boat for you. Look at how moored boats are lying to see which it is. If you miss, go round and try again; never grab at a buoy that is going past.', note=HINT, start=0.5)}
{figure('fig-swinging', 'swinging room', '0 0 900 470', 'Swinging room at anchor', 'Seen from above, wind from the top. Two anchored yachts lie downwind of their anchors, each with a dashed circle showing where it can swing. The left boat has less chain out and a smaller circle; the right boat more chain and a bigger circle. The circles overlap in a shaded lens between them. A faint second outline shows the left boat after the wind shifts to blow from the west, lying to the east of its anchor and reaching into the overlap.', g.swinging(), 'Your whole circle must stay clear of other boats, the shore and the shallows at low water. Look at where the other boats’ anchors are likely to be, not where the boats are now, and ask how much chain they have out.', note=HINT)}
{figure('fig-raft', 'rafting up', '0 0 900 420', 'Three yachts rafted up alongside a pontoon', 'Seen from above, the pontoon at the bottom. The biggest yacht lies against the pontoon, a smaller one outside it and the smallest outside that, with fenders between each pair. Bow and stern lines and crossed springs join each boat to the one inside it. The two outer boats each have their own long bow and stern lines to the pontoon, and the inside boat has springs to the pontoon as well as bow and stern lines. A dotted path runs from the outer boat across the foredecks to the pontoon.', g.raft(), 'The inside boat carries the load of the whole raft: ask before you tie up alongside, and agree when each boat plans to leave, because an inside boat leaving means the outer boats must move.', note=HINT, start=0.5)}
{sources('manoeuvres', [
  'Prop walk and steering astern: ' + a('https://www.pbo.co.uk/seamanship/prop-walk-how-to-use-it-to-your-best-advantage-97756','Practical Boat Owner, prop walk') + ', ' + a('https://sailmagazine.com/cruising/walking-the-prop/','Sail magazine, walking the prop') + ', ' + a('https://en.wikipedia.org/wiki/Propeller_walk','Wikipedia, propeller walk') + '.',
  'Lines and fenders: ' + a('https://jimmygreen.com/knowledge-centre/mooring-warp-length-and-configuration/','Jimmy Green, mooring warps') + ', ' + a('https://jimmygreen.com/knowledge-centre/fender-size-guide/','Jimmy Green, fender size guide') + '.',
  'Alongside, springs and wind off the berth: ' + a('https://www.yachtingmonthly.com/sailing-skills/springing-on-and-off-29899','Yachting Monthly, springing on and off') + ', ' + a('https://www.pbo.co.uk/seamanship/springing-off-and-on-a-pontoon-90572','Practical Boat Owner, springing off and on') + ', ' + a('https://www.morganscloud.com/2017/07/14/coming-alongside-docking-taming-the-wind/','Attainable Adventure Cruising, taming the wind') + '.',
  'Finger berths: ' + a('https://forums.ybw.com/threads/berthing-single-handed-at-a-finger-pontoon.467249/','YBW forum, finger pontoons') + ' ².',
  'Stern-to: ' + a('https://www.rya.org.uk/boating-abroad/med-mooring-stern-to/','RYA, Med mooring stern-to') + ', ' + a('https://sailingissues.com/yachting-guide/mediterranean-mooring.html','Sailing Issues, Mediterranean mooring') + '. Box berths: ' + a('https://www.yachtingmonthly.com/sailing-skills/expert-guide-box-berthing-62853','Yachting Monthly, box berthing') + ', ' + a('https://www.yachtingmonthly.com/sailing-skills/how-to-use-box-mooring-70853','Yachting Monthly, box moorings') + '.',
  'Checked by web search, September 2026; the pages could not be opened directly.',
])}

  <h3>Worth watching</h3>
{videos([
 ('1TMB4-EPMAI', 'Boat handling: prop wash and prop walk, with Simon Jinks', 'Royal Yachting Association - RYA', 'The RYA’s own explanation of the two effects in “The physics you must accept”.'),
 ('rkg4iGqOo_8', 'Tom Cunliffe explains how to make anchoring stress-free', 'MDL Marinas', 'Anchoring a cruising yacht, from a well-known British instructor and author.'),
 ('8TBK7XOChqE', 'Leon explains: Mediterranean mooring stern-to in Malta', 'Leon Schulz, Reginasailing', 'Stern-to with a lazy line on a modern fin-keeled boat with a spade rudder, the kind you are likely to charter.'),
 ('jULddr4KA50', 'Docking stern-to in Croatia with lazy lines: Sharpen Up, episode one', '45 Degrees Sailing', 'The same manoeuvre in a Croatian marina.'),
 ('BtmXFLyGeH8', 'Prop walk explained: what it is and how to use it to your advantage', 'Motor Boat & Yachting', 'Using prop walk on purpose. It is made for motor boats, but a propeller behaves the same way under a yacht.'),
 ('DGV-JP1ksMw', 'How to use prop walk to back in: docking guide', 'Adriatic Sailing Academy', 'Reversing into a berth with the help of prop walk, from a sailing school.'),
 ('TJeeTR3-oc8', 'Marina berthing tips for yacht sailors', 'Windcraft Yachts', 'Coming into a marina berth, from a yacht company.'),
 ('6Mz9mAwVvgE', 'How to moor a yacht securely', 'Yachting Monthly', 'Lines and springs once you are in: the part of berthing that decides whether you sleep.'),
])}

  <h3 id="manoeuvres--briefing">The crew briefing: what to say so nobody jumps</h3>
  <ol>
    <li>“We are going alongside port side to, bow into the wind.”</li>
    <li>“Fenders on the port side at pontoon height; lines at the bow, the stern and midships, led outside the guardrails and back on board.”</li>
    <li>“(Name), you step off with the midships line when I say, and take a turn on the nearest cleat. Step, do not jump.”</li>
    <li>“(Name), you take the bow line; I will take the stern.”</li>
    <li>“If it goes wrong, we go round again. Nobody fends off with hands or feet.”</li>
  </ol>
  <p>Say it before you enter the harbour, not on the approach, and ask each person to say back what they are doing.</p>

  <h3>Terms used in this section</h3>
  <h4 class="terms__group">How the boat behaves</h4>
{terms([
 ("pw-astern","Going astern","Moving backwards under engine."),
 ("pw-kick","Stern kick","The sideways push of the stern from prop walk, strongest as the propeller starts turning in astern."),
 ("pw-prop","Propeller hand","A right-handed propeller turns clockwise, seen from astern, going ahead; a left-handed one the other way. The hand sets the direction of prop walk."),
 ("pw-pivot","Pivot point","The point the boat turns about: about a third of its length from the bow going ahead, further aft going astern."),
 ("pw-stern-swing","Stern swing","When the boat turns ahead, the stern swings out much further than the bow swings in."),
 ("tt-rotation","Turning on the spot","Turning the boat round in little more than its own length with short bursts ahead and astern."),
 ("tt-ahead","Burst ahead, helm hard over","A short, firm burst ahead with the rudder hard over: water from the propeller hits the rudder and turns the boat before it gathers way."),
 ("tt-astern","Burst astern in a turn","A burst astern that stops the boat; prop walk kicks the stern, and if you turn the right way it continues the turn."),
 ("tt-repeat","Repeat the bursts","Keep alternating ahead and astern with the helm left hard over until the boat faces the new way."),
 ("tt-room","Room to turn","A fin-keel boat can turn in about its own length; a long keel needs more."),
])}
  <h4 class="terms__group">Lines and knots</h4>
{terms([
 ("ml-bow-line","Bow line","A mooring line from the bow forward to the pontoon or quay: it holds the bow in and stops the boat drifting back."),
 ("ml-stern-line","Stern line","A mooring line from the stern aft to the pontoon or quay: it holds the stern in and stops the boat moving forward."),
 ("ml-bow-spring","Spring from the bow","A line from the bow leading aft to the pontoon; it stops the boat moving forward. Used to spring the stern out."),
 ("ml-stern-spring","Spring from the stern","A line from the stern leading forward to the pontoon; it stops the boat moving back. Used to spring the bow out."),
 ("ml-fenders","Fenders","Air-filled cushions hung between hull and pontoon at pontoon height."),
])}
  <h4 class="terms__group">Coming alongside and leaving</h4>
{terms([
 ("sp-bow-spring","Bow spring, doubled back","The bow spring led round the pontoon cleat and back on board, so it can be let go from the boat."),
 ("sp-bow-fender","Bow fender","A fender at the bow, where the boat pivots against the pontoon when springing the stern out."),
 ("sp-stern-out","Stern out","The stern swinging away from the pontoon as the boat motors gently ahead against the bow spring."),
 ("sp-stern-spring","Stern spring, doubled back","The stern spring led round the pontoon cleat and back on board, ready to slip."),
 ("sp-stern-fender","Quarter fender","A fender at the quarter, where the boat pivots when springing the bow out."),
 ("sp-bow-out","Bow out","The bow swinging away from the pontoon as the boat motors gently astern against the stern spring."),
 ("al-wind","Wind or tide from ahead","Approach into whichever is stronger. A tide from ahead lets the rudder work while you stop over the ground; a wind from ahead slows the boat and keeps the bow from blowing off."),
 ("al-track","Approach track","A shallow angle to the pontoon, slowly."),
 ("al-neutral","Neutral early","Take the engine out of gear well before the pontoon and let the boat’s way carry it in."),
 ("al-stop","Burst astern","A short push in astern to stop the boat; port side to with a right-handed propeller, it also pulls the stern in."),
 ("al-step-off","Stepping off","The crew step, never jump, onto the pontoon, with a line, and take a turn on a cleat at once."),
])}
  <h4 class="terms__group">Stern-to and box berths</h4>
{terms([
 ("md-fenders","Fenders on both sides","Stern-to, the boats either side are touching distance away."),
 ("md-stern-lines","Stern lines","Two lines from the stern quarters to bollards or rings on the quay, often crossed."),
 ("md-lazy-line","Lazy line","A light line tied at the quay that leads to the heavy mooring line; picked up at the stern and walked forward."),
 ("md-mooring-line","Mooring line","The heavy line from the ground chain, made fast at the bow to hold the boat off the quay."),
 ("md-ground-chain","Ground chain","A heavy chain along the harbour bed that the mooring lines are fixed to."),
 ("bx-posts","Box posts","Wooden or steel posts at the outer end of a box berth."),
 ("bx-stern-lines","Stern lines to the posts","Lines with big loops dropped over the posts as the boat passes, windward first."),
 ("bx-bow-lines","Bow lines to the quay","Lines from the bow to the quay, taken ashore by a crew member stepping off the bow."),
 ("bx-wind","Crosswind","Wind across the box: take the windward lines first, and keep a little way on."),
])}
  <h4 class="terms__group">The four knots</h4>
{terms([
 ("kn-bw-standing","Standing part","The long part of the line, which takes the load; the knot is tied with the other end."),
 ("kn-bw-small-loop","Small loop","The first step of a bowline: a small loop in the standing part, with the part towards the end lying on top."),
 ("kn-bw-collar","Round the standing part","The end comes up through the small loop, round behind the standing part, and back down through the loop."),
 ("kn-bw-tail","End inside the loop","In the usual bowline the end finishes inside the big loop; leave a tail at least a few times the line’s diameter."),
 ("kn-bw-loop","The loop","The bowline’s loop keeps its size under load, and the knot can be undone after it has been loaded."),
 ("kn-cl-standing","Standing part","On a fender line, the part that goes down to the fender."),
 ("kn-cl-cross","Crossing turn","The diagonal turn of a clove hitch, which lies over both parts of the line and grips them against the rail."),
 ("kn-cl-end","The end","A clove hitch can slip on a smooth rail or wire: a half hitch round the standing part makes it secure."),
 ("kn-rt-turn","Round turn","Two full turns round a ring, post or rail. The friction takes the load, so the knot can be tied or untied under strain."),
 ("kn-rt-hitches","Two half hitches","The end taken twice round the standing part and under itself, both the same way, which together make a clove hitch round the line."),
 ("kn-rt-standing","Standing part","The part of the line that takes the load, here from the boat."),
 ("kn-ct-lead","Lead to the far horn","Take the line to the far side of the cleat first, so the first turn runs round the base and holds without jamming."),
 ("kn-ct-turn","Full turn","One complete turn round the base of the cleat, under both horns."),
 ("kn-ct-eights","Figures of eight","Diagonal turns over the top of the cleat, round one horn and then the other."),
 ("kn-ct-lock","Locking turn","A final turn twisted so the end lies under the last diagonal: it holds the hitch without extra turns."),
])}
  <h4 class="terms__group">Knots and anchoring</h4>
{terms([
 ("bowline","Bowline","A fixed loop that does not slip or jam, and can be undone after a load."),
 ("cleat-hitch","Cleat hitch","A turn round the cleat, figures of eight over its horns, and a locking turn."),
 ("clove-hitch","Clove hitch","Two turns round a rail or post, the second crossing over the first, with both parts trapped under the crossing: quick to tie and adjust, but it can slip if the pull changes direction."),
 ("transit","Transit","Two fixed objects seen in line. At anchor, take one on the beam and check it often: a steady shift one way, not a swing back and forth, means the anchor is dragging."),
])}
  <h4 class="terms__group">Buoys, swinging room and rafting</h4>
{terms([
 ("bp-buoy","Mooring buoy","A large buoy on a heavy chain to a sinker on the seabed, laid for boats to tie to; often with a small pick-up buoy on a line."),
 ("bp-slow","Approach to a buoy","Slowly, against the wind or tide, so that the boat stops with the buoy at the bow."),
 ("bp-point","Pointing at the buoy","The bow crew points at the buoy all the way in, because the helm loses sight of it under the bow."),
 ("bp-own-line","Your own line","A line from the boat through the buoy’s ring or strop and back on board, so it can be slipped from on deck; never tie to the pick-up buoy alone."),
 ("sw-circle","Swinging circle","The circle a boat at anchor can swing round: radius about the chain let out plus the boat’s length."),
 ("sw-neighbour","Neighbour’s circle","A nearby boat’s swinging circle, bigger if it has more chain out."),
 ("sw-overlap","Overlapping circles","Where two boats’ swinging circles overlap, they can meet if they swing differently."),
 ("rf-fenders","Fenders in a raft","Fenders between every pair of rafted boats, at the widest point of the hulls."),
 ("rf-shore-lines","Shore lines","In a raft, the outer boats’ own bow and stern lines to the shore or pontoon, so that the inside boat does not hold the whole raft."),
 ("rf-breast-springs","Springs in a raft","Springs from each boat to the one inside it, to stop the boats surging forward and back against each other."),
 ("rf-cross","Crossing a raft","Walk across other boats by their foredecks, never through their cockpits."),
])}
  <h4 class="terms__group">Finger berths</h4>
{terms([
 ("fb-fenders","Fenders on both sides","In a finger berth the boat can touch the finger on one side and the neighbour on the other, so fenders go on both."),
 ("fb-midships","Midships line to the finger","From the boat’s middle cleat back to the finger’s outer (after) cleat: on first, it stops the boat going any further forward."),
 ("fb-step","Stepping onto a finger","By the shrouds, where the boat is widest and the finger is alongside; never from the bow."),
 ("fb-stop","Stopping in the berth","Slowly in, and a short burst astern as the bow nears the main pontoon."),
 ("fb-lines","Lines in a finger berth","After the midships line: two bow lines to the main pontoon, a stern line to the finger’s outer cleat, and springs to its middle cleat."),
])}

</section>
'''
finish(page, ROOT + 'sections/10-manoeuvres.html', others=(ROOT + 'sections/03-hull.html', ROOT + 'sections/04-rig.html', ROOT + 'sections/05-deck.html', ROOT + 'sections/06-engine.html', ROOT + 'sections/07-systems.html', ROOT + 'sections/08-electronics.html', ROOT + 'sections/09-sailing.html', ROOT + 'sections/02-fleet.html', ROOT + 'sections/00-start.html'))
