# Generates sections/11-navigation.html for Sailing 101.
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_common import *
import gen_navigation_diagrams as g


page = f'''<section id="navigation">
  <h2>Navigation and passage planning</h2>
  <p class="lead">Knowing where you are, where you are going, what is in the way, and when the tide and the weather will let you go. The chartplotter does the arithmetic; you still have to do the thinking, and to notice when the plotter is wrong. In a hurry? Jump to <a href="#navigation--buoyage">buoys</a>, <a href="#navigation--lights">lights at night</a>, <a href="#navigation--colregs">who gives way</a> or <a href="#navigation--passage-plan">the passage plan</a>.</p>

  <details class="first-words" open>
    <summary>Nine words before anything else</summary>
    <dl>
      <dt>Nautical mile</dt><dd>1,852 m: one minute of latitude. Written M or nm. A cable is a tenth of a mile, about 185 m.</dd>
      <dt>Knot</dt><dd>One nautical mile an hour, about 1.85 km/h.</dd>
      <dt>Bearing</dt><dd>The direction of something from you, in degrees clockwise from north, always written with three figures: 045°, not 45°.</dd>
      <dt>Heading and course</dt><dd>The heading is where the bow points; the course is the direction you mean to go. The ground track is the way you actually move over the seabed.</dd>
      <dt>COG and SOG</dt><dd>Course and speed over the ground, from GPS. They differ from heading and speed through the water whenever there is tide or current.</dd>
      <dt>True and magnetic</dt><dd>Directions measured from the true (geographic) north pole, as on the chart, or from where a compass points.</dd>
      <dt>Chart datum</dt><dd>The level all charted depths are measured down from: in tidal waters, about the lowest tide there is.</dd>
      <dt>Springs and neaps</dt><dd>Tides with the biggest range (springs, around full and new moon) and the smallest (neaps, around the half moons). Nothing to do with the season.</dd>
      <dt>IALA region A</dt><dd>The buoyage system used in all the waters this site covers: red marks to port entering harbour.</dd>
    </dl>
    <p class="first-words__note">The first right-of-way rules are also in <a href="#sailing">Sailing fundamentals</a>; the instruments and AIS in <a href="#electronics">Electronics</a>.</p>
  </details>
  <p class="conf-key"><b>Marks used below:</b> {ONE} single source; {TWO} sources disagree or anecdotal; {TBC} not yet verified. <b>How this section was checked:</b> in September 2026 the rules, marks and figures were checked by web search against the pages linked under “Sources and confidence”. The search results were read, but the pages themselves could not be opened from the editing session. Always use a current chart and current tide tables: this page is for learning, not for navigating.</p>

  <h3>Position, distance and direction</h3>
  <ul>
    <li><strong>Latitude and longitude.</strong> A position is written like 50°45.3′N 001°17.2′W: degrees and minutes of latitude north or south of the equator, then of longitude east or west of Greenwich. GPS gives it on the WGS84 datum, the same as modern charts; a very old paper chart may use another, and its positions can be out by a few hundred metres, and some charts carry a note that they cannot be referred to WGS84 at all.</li>
    <li><strong>Distance.</strong> One minute of latitude is one nautical mile, so measure distances with dividers (a pair of hinged pointers, like a drawing compass with two points) on the <em>latitude</em> scale at the side of the chart, level with where you are. Never use the longitude scale along the top and bottom: its minutes shrink as you go north.</li>
    <li><strong>Speed, time and distance.</strong> Distance = speed × time. The six-minute rule: in six minutes (a tenth of an hour) a boat covers a tenth of its speed in miles, so at 5 knots, half a mile.</li>
    <li><strong>Through the water or over the ground.</strong> The log measures speed through the water; GPS measures speed over the ground. In a 2-knot foul tide (one running against you) a boat doing 5 knots through the water makes only 3 over the ground; in a fair tide, one going your way, 7. Leeway, the wind pushing the boat sideways, adds a few degrees between heading and track, more when close-hauled.</li>
  </ul>

{figure('fig-compass', 'three norths', '0 0 900 380', 'True, magnetic and compass north, and converting a course', 'Left: three arrows from one point. True north points straight up; magnetic north is a little to the west of it (the angle is the variation); compass north is a little to the east of magnetic north (the angle is the deviation). A thinner arrow shows the boat’s heading. Right: a worked example in five rows: true 100°, variation 3° west (add), magnetic 103°, deviation 2° east (subtract), compass 101°.', g.compass(), 'The chart works in true; the steering compass reads compass. Variation is printed on the chart’s compass rose with the year and its yearly change; deviation comes from a deviation card made for your boat, and on most small yachts with the compass well placed it is usually under 3° {ONE}.', note=HINT)}
  <p>A hand-bearing compass, held well away from the engine and the steel of the boat, has almost no deviation: use it for bearings of landmarks, and convert only for variation. Going back, from compass to true, reverse the arithmetic: a hand-bearing compass reads 215° on a lighthouse where the variation is 3° W; subtract the west, and the true bearing is 212°. Many modern navigators work in true throughout, with the plotter and the autopilot set to true, and only convert for the steering compass.</p>

  <h4>Fixing your position</h4>
  <ul>
    <li><strong>GPS</strong> on the plotter is the everyday answer. Write the position in the logbook every hour, with the time, the log reading and the course: if the electronics fail, that is where you start from.</li>
    <li><strong>A three-point fix:</strong> take compass bearings of three charted landmarks, well spread round the horizon, convert them to true and draw them on the chart. Where they cross is where you are; the small triangle they usually make (the “cocked hat”) shows how accurate the fix is.</li>
    <li><strong>A transit:</strong> two charted objects in line, a lighthouse and a church, say, put you exactly on the line through them. It is the most accurate position line there is, and the basis of leading lines into harbours.</li>
    <li><strong>Depth</strong> is a check: if the sounder reads 30 m where the chart says 8 m, something is wrong.</li>
    <li><strong>Dead reckoning (DR)</strong> is the position worked from course and distance run since the last fix; the <strong>estimated position (EP)</strong> adds the tidal stream and leeway.</li>
  </ul>

  <h3>Charts</h3>
  <p>A chart shows depths, drying areas, dangers, marks, lights, and the nature of the seabed. Its symbols are standard and listed in a booklet (for Admiralty charts, <em>Symbols and Abbreviations used on Admiralty Charts</em>, NP5011); learn the dozen common ones before your first passage: rocks awash and underwater, wrecks, depth contours, anchorages, and the magenta flare of a light.</p>
{figure('fig-datum', 'depths and heights', '0 0 900 400', 'How depths and heights are measured on a chart', 'A side view of the sea and seabed, with a drying rock on the left and a cliff with a lighthouse on the right. Three horizontal levels: a high-water level near the top, the sea as it is now in the middle, and chart datum, about the lowest tide, below it. Arrows show the drying height of the rock above chart datum; the height of tide from chart datum up to the sea surface; the charted depth from chart datum down to the seabed; the depth of water now, which is their sum; and the height of the light measured up from the high-water level.', g.datum(), 'Depths are measured down from chart datum, so the water is almost always deeper than charted. Heights of lights and clearances under bridges and power lines are measured up from a high-water level, so there is almost always more room than charted. In both cases the chart errs on the safe side.')}
  <ul>
    <li><strong>Depth over a drying bank</strong> = height of tide − drying height. A bank that dries 1.5 m has 1.4 m of water over it when the height of tide is 2.9 m.</li>
    <li><strong>Clearance under the keel</strong> = depth of water − the boat’s draught. Leave a safety margin on top: at least half a metre in calm, sheltered water, and much more in waves, which lift and drop the boat; a metre where the bottom is rock.</li>
  </ul>
  <p>In seas with almost no tide, charts use a mean sea level instead: in the Baltic, Swedish and Finnish charts now use the common Baltic Sea Chart Datum 2000, close to mean sea level. The real level moves with the wind and air pressure: a strong onshore wind can raise the water in a Baltic harbour noticeably, and an offshore one lower it.</p>
{card('navigation--electronic-charts', 'What the plotter does not show you', 'electronic chart, vector chart, raster chart, zoom', 'An electronic chart is either a raster chart (a scanned paper chart) or a vector chart (a database the plotter draws, adding or hiding detail as you zoom). Vector charts are the normal kind on plotters, and they have one dangerous habit.',
  ['A vector chart hides detail when zoomed out, to keep the screen readable. A route drawn at a small scale can pass straight over a rock that only appears when you zoom in. In the 2014–15 Volvo Ocean Race the yacht Vestas Wind ran onto a reef in the Indian Ocean that her navigators had not seen at the zoom level they were using: the independent report found the shoal shown only as a patch of deep-looking water at most zoom levels.'],
  ['The plotter knows where you are to within a few metres, all the time, which no paper chart can do. Use it.'],
  ['The survey behind the chart may be old: many coastal areas were last surveyed with lead lines, long ago, and the chart records how confident it is (the zones of confidence, or CATZOC, on vector charts, from A1, the best, to D, and U for unassessed). Charts need updating, and a plotter’s cartography is often years old.'],
  ['A route checked only on the plotter; nobody on board who has looked at a paper chart or zoomed in along the route; the plotter trusted over the depth sounder and the view out of the window.'],
  ['Check every route leg zoomed right in, or with the plotter’s route-check function; carry a paper chart or an independent second plotter for the area; keep a lookout.'], fold=True)}

  <h3>Tides and tidal streams</h3>
  <p>In the Channel, the North Sea and along the Atlantic coasts the sea rises and falls twice a day, about every 6 hours 12 minutes between high and low water, and the water moves with it as tidal streams. The Mediterranean has only small tides in most places, and the Baltic and the Black Sea almost none; there the water level and the currents follow the wind instead. The rest of this section matters wherever there is a tide.</p>
  <ul>
    <li><strong>Tide tables</strong> give the times and heights of high and low water at standard ports. Other places, the secondary ports, are worked out from a standard port with corrections printed in the tables or an almanac; the plotter and tide apps do this for you, but check them against the tables.</li>
    <li><strong>The range</strong> is the difference between high and low water: about 7 m at springs at Dover and nearly 5 m at Plymouth, but under 2 m at Poole; on the French side, much more at St Malo; much less everywhere at neaps.</li>
    <li><strong>Set and rate.</strong> A tidal stream or current is named for the direction it flows <em>towards</em>: a stream setting 090° flows to the east. That is the opposite of the wind, which is named for where it comes <em>from</em>. The direction is its set; its speed, in knots, its rate.</li>
    <li><strong>Tidal streams</strong> run hardest at mid-tide and slacken around high and low water. The chart gives them at tidal diamonds (a letter in a diamond, with a table of direction and rate for each hour before and after high water at a standard port); a tidal stream atlas shows them as arrows, hour by hour. In many places they run at a knot or two; round headlands and through narrow channels, such as Portland Bill or the Alderney Race, they run much faster: about 7 knots in the Portland Race and up to about 9 knots in the Alderney Race at springs, faster than a yacht motors.</li>
    <li><strong>Wind against tide</strong> raises short, steep seas. A passage that is comfortable with the tide can be dangerous against it, in the same wind; plan to pass headlands at slack water or with the tide. Such places are tidal gates: you can pass them comfortably only at certain states of the tide, so the passage is timed around them.</li>
  </ul>
{figure('fig-twelfths', 'rule of twelfths', '0 0 900 360', 'The rule of twelfths for how fast the tide rises', 'A graph of the tide rising from low water to high water over six hours in an S-shaped curve. Bars for each hour show the rise: one twelfth of the range in the first hour, two in the second, three in the third and fourth, two in the fifth and one in the sixth. For a range of 4.8 m these are 0.4, 0.8, 1.2, 1.2, 0.8 and 0.4 m.', g.twelfths(), 'The rule of twelfths gives the height of tide between high and low water well enough to decide whether there is water over a bar or a sill. Where the tide curve is irregular, use the tidal curve printed in the tide tables for that port.')}
  <p>Worked example: low water is 0.5 m at 1200 and high water is 5.3 m at 1800, a range of 4.8 m. At 1500, three hours after low water, the tide has risen 1 + 2 + 3 = 6 twelfths of the range, 2.4 m, so the height of tide is about 2.9 m. Add it to the charted depth to find the depth of water.</p>

  <h4 id="navigation--course-to-steer">Crossing a tidal stream</h4>
{figure('fig-tide-triangle', 'course to steer', '0 0 900 420', 'Working out a course to steer across a tidal stream', 'A chart with points A and B. The ground track is drawn from A to B. From A, a line for one hour of tidal stream, 2 knots to the east. From the end of it, a line 5 miles long (one hour at the boat’s speed) is swung to cut the ground track. That line is the course to steer, about 050° true against a track of 061° true; the distance from A to where it cuts the track is one hour’s progress over the ground, about 6.7 knots.', g.tide_triangle(), 'The boat is pointed upstream of its destination and crabs along the straight line. Steering straight at B instead, the tide would sweep the boat off in a curve, and you would sail further. Our worked figures, for illustration.')}
  <ol>
    <li>Draw the ground track from A to B.</li>
    <li>From A, draw one hour of tidal stream, direction and rate from the tidal diamond or atlas for that hour.</li>
    <li>From the end of the tide line, set the dividers to one hour of boat speed through the water and mark where they cut the ground track.</li>
    <li>The line from the end of the tide to that mark is the course to steer, in true. Allow a few degrees for leeway (steer a little into the wind), then convert to compass.</li>
    <li>The distance from A to the mark is the speed over the ground: use it for the time to B. On a long passage, the tide changes every hour; work the triangle for the whole passage at once, adding each hour’s tide, rather than one hour at a time.</li>
  </ol>
{sources('position, charts and tides', [
  'Datums: ' + a('https://iho.int/iho_pubs/standard/S-66/SN.1-Circ.213_Guidance_On_Chart_Datums_And_The_Accuracy_Of_Positions_On_Charts.PDF','IMO/IHO guidance on chart datums and positions') + ', ' + a('https://www.pbo.co.uk/gear/electronic-charts-reliability-106709','PBO, paper charts versus electronic charts') + '. Baltic datum: ' + a('https://ihr.iho.int/articles/the-baltic-sea-chart-datum-2000-bscd2000-implementation-of-a-common-reference-level-in-the-baltic-sea/','International Hydrographic Review, BSCD2000') + ', ' + a('https://www.sjofartsverket.se/en/services/hydrographic-information/nautical-charts/nautical-chart-production/reference-levels/mean-sea-level/','Swedish Maritime Administration, mean sea level') + '.',
  'Deviation: ' + a('https://sailingissues.com/navcourse3.html','Sailing Issues, the compass') + ' ¹. Keel clearance: ' + a('https://seatow.com/chart-datum-under-keel-clearance/','Sea Tow, chart datum and under-keel clearance') + '.',
  'Electronic charts: ' + a('https://www.yachtingworld.com/news/vestas-grounding-report-more-than-just-an-expensive-and-embarrassing-mistake-62635','Yachting World on the Vestas Wind report') + ', ' + a('https://www.hydro-international.com/content/article/charting-aspects-of-the-volvo-ocean-race-stranding','Hydro International, charting aspects') + '; zones of confidence: ' + a('https://www.admiralty.co.uk/news/CATZOC-dispelling-the-myths','Admiralty, CATZOC') + '.',
  'Tidal ranges and streams: ' + a('https://assets.publishing.service.gov.uk/media/5a79ff7f40f0b66eab998ff5/SEA8_TechRep_Hydrography.pdf','UK Government SEA 8 hydrography report') + ', ' + a('https://en.wikipedia.org/wiki/Tidal_range','Wikipedia, tidal range') + ', ' + a('https://en.wikipedia.org/wiki/Alderney_Race','Wikipedia, Alderney Race') + ', ' + a('https://www.yachtingmonthly.com/sailing-skills/the-uks-11-fiercest-tide-races-75304','Yachting Monthly, the UK’s fiercest tide races') + '.',
  'Checked by web search, September 2026; the pages could not be opened directly. The worked examples are our arithmetic.',
])}

  <h3 id="navigation--buoyage">Buoys and marks</h3>
  <p>All the waters this site covers use IALA region A. (Region B, used in the Americas, Japan, Korea and the Philippines, swaps the colours: red to starboard entering harbour.) A mark is identified first by its colour, then by its topmark, then at night by its light; the shape of the buoy (can, cone, pillar or spar) is only a help.</p>
{figure('fig-lateral', 'lateral marks', '0 0 900 420', 'Lateral marks in IALA region A', 'Left: a channel seen from above leading from the sea at the bottom into a harbour at the top, with red can-shaped marks on the left bank and green cone-shaped marks on the right, and a boat entering. An arrow shows the direction of buoyage, from the sea into harbour. Right: the four lateral marks side-on: the red port-hand mark with a can topmark; the green starboard-hand mark with a cone topmark; the preferred-channel-to-starboard mark, red with a green band; and the preferred-channel-to-port mark, green with a red band.', g.lateral(), 'Entering harbour, keep red marks on your port (left) hand and green on your starboard. Leaving, the other way round. Along a coast, the chart shows the direction of buoyage with an arrow symbol.', note=HINT)}
{figure('fig-cardinals', 'cardinal marks', '0 0 900 560', 'The four cardinal marks around a danger', 'A danger in the middle of the sea, seen from above, with lines dividing the sea into four quadrants: north, east, south and west. A cardinal mark stands in each. North: black over yellow, two cones pointing up, a continuous quick white light. East: black, yellow, black, two cones base to base, three flashes. South: yellow over black, two cones pointing down, six flashes and a long flash. West: yellow, black, yellow, two cones point to point, nine flashes.', g.cardinals(), 'Cardinals say where the safe water is: pass north of a north cardinal, east of an east one. The number of quick flashes follows a clock face: three for east (3 o’clock), six for south, nine for west; the south mark’s long flash stops a six being confused with a three or nine.')}
{figure('fig-other-marks', 'other marks', '0 0 900 330', 'Isolated danger, safe water, special and emergency wreck marks', 'Four marks side-on. The isolated danger mark: black with a red band, two black balls on top, a white light flashing in twos. The safe water mark: red and white vertical stripes, one red ball, a white light that is isophase, occulting, one long flash every 10 seconds or Morse A. The special mark: yellow with a yellow X, a yellow light. The emergency wreck marking buoy: blue and yellow vertical stripes, a yellow upright cross, alternating blue and yellow flashes.', g.other_marks(), 'Topmarks are the quick way to tell marks apart in daylight: two balls, a danger; one red ball, safe water; an X, special; a cross, a new wreck.')}

  <h4>Reading a light on the chart</h4>
{compare('Light characteristics', ['Abbreviation', 'Means', 'Example'], [
  ['F', 'fixed: a steady light', 'F R: a fixed red light'],
  ['Fl', 'flashing: the light is shorter than the dark', 'Fl 5s: one flash every 5 seconds'],
  ['Fl(2)', 'a group of flashes', 'Fl(2) 10s: two flashes every 10 seconds'],
  ['Fl(2+1)', 'a composite group', 'Fl(2+1) R 10s: a preferred-channel mark'],
  ['LFl', 'long flash: at least 2 seconds of light', 'LFl 10s: a safe water mark'],
  ['Q, VQ', 'quick (50 or 60 flashes a minute) and very quick (100 or 120)', 'VQ(3) 5s: an east cardinal'],
  ['Iso', 'isophase: equal light and dark', 'Iso 4s: 2 s on, 2 s off'],
  ['Oc', 'occulting: the light is longer than the dark', 'Oc(2) WRG 8s: a sectored light'],
  ['Al', 'alternating colours', 'Al WR 5s'],
  ['Mo(A)', 'Morse code letter A (short, long)', 'Mo(A) 8s: a safe water mark'],
], stack=True)}
  <p>A light marked <strong>Fl(2) 10s 15m 8M</strong> flashes twice every 10 seconds, white (no colour letter means white), stands 15 m above the chart’s high-water level, and has a nominal range of 8 nautical miles in clear weather. <strong>WRG</strong> means a sectored light: it shows white in the safe channel, and red or green on either side of it, so that a boat drifting off the leading line sees the colour change. Time a light with a stopwatch, counting the whole cycle from the start of one group to the start of the next.</p>
{sources('buoys and lights', [
  'IALA regions and marks: ' + a('https://en.wikipedia.org/wiki/Lateral_mark','Wikipedia, lateral mark') + ', ' + a('https://www.offshoreblue.com/nav/atons.php','Offshore Blue, IALA A and B') + ', ' + a('https://www.iala-aism.org/','IALA') + '.',
  'Light characteristics: ' + a('https://en.wikipedia.org/wiki/Light_characteristic','Wikipedia, light characteristic') + ', ' + a('https://www.marineinsight.com/marine-navigation/iala-buoyage-system-for-mariners-types-of-marks/','Marine Insight, IALA marks') + '.',
  'Checked by web search, September 2026; the pages could not be opened directly.',
])}

  <h3 id="navigation--lights">Lights and shapes on vessels</h3>
  <p>Between sunset and sunrise, and in poor visibility, every vessel shows lights that say what it is, which way it is heading and what it is doing (COLREGs Part C, Rules 20 to 31). By day some show black shapes instead.</p>
{figure('fig-nav-lights', 'navigation lights', '0 0 900 476', 'A yacht’s navigation lights and what another vessel’s lights tell you', 'Left: a yacht seen from above with the arcs of its lights: green starboard sidelight and red port sidelight, each 112.5° from dead ahead to 22.5° abaft the beam; a white sternlight, 135° astern; and, dashed, the white steaming light, 225° forward, used only under engine. Right: six night scenes: green and red together, a vessel coming straight at you; green only, her starboard side; red only, her port side; white only, a sternlight or an anchor light; a white light above red and green, a power-driven vessel heading at you; red or green alone high up, a sailing yacht’s tricolour.', g.nav_lights(), 'Under sail: sidelights and a sternlight (or the tricolour). Under engine, even with sails up: add the steaming light, because the boat is now a power-driven vessel under the rules. (A power-driven vessel under 12 m may instead show one all-round white light with its sidelights.)', note=HINT)}
  <p>The arcs are chosen so that the lights answer the question that matters at sea: can you see her port side or her starboard side? If you see a red light and a green light together, she is heading straight at you; if you see her white sternlight alone, you are behind her, and if you are catching her up you are the overtaking vessel and must keep clear.</p>
{figure('fig-vessel-lights', 'lights and shapes', '0 0 900 440', 'All-round lights and day shapes of vessels that need room', 'Eight panels, each with the all-round lights shown at night on the left and the black day shapes on the right. At anchor: one white light, one ball. Not under command: two red lights, two balls. Restricted in her ability to manoeuvre: red, white, red lights; ball, diamond, ball. Constrained by her draught: three red lights, a cylinder. Trawling: green over white, two cones point to point. Fishing other than trawling: red over white, the same cones. Pilot vessel: white over red, and by day flag H. A yacht motor-sailing: at night a steaming light and sidelights, by day a cone point down.', g.vessel_lights(), 'When these vessels are making way they also show their sidelights and sternlight; those restricted in their ability to manoeuvre or constrained by their draught, and big trawlers, show masthead lights too. Most of them are vessels you must keep clear of; the shapes by day and the lights at night tell you which.')}
  <p>Ships of 50 m and more show a second, higher steaming light aft, so that their heading can be read from the angle between the two. A vessel towing shows two or three steaming lights in a vertical line, depending on the length of the tow, and a yellow towing light above her sternlight; look for the tow behind, which carries its own lights but may be low in the water and hard to see (Rule 24).</p>

  <h3 id="navigation--colregs">The collision regulations</h3>
  <p>The International Regulations for Preventing Collisions at Sea (the COLREGs) apply to every vessel on the sea, a yacht as much as a tanker. Two terms first: a vessel is <em>under way</em> when she is not at anchor, made fast to the shore or aground, even if she is drifting; she is <em>making way</em> when she is actually moving through the water. The first rules for sailing boats are in <a href="#sailing">Sailing fundamentals</a>; these are the ones a skipper uses every day.</p>
{compare('The rules a yacht skipper uses most', ['Rule', 'What it says', 'In practice'], [
  ['5 Look-out', 'keep a proper look-out by sight and hearing at all times', 'someone looks all round, including under the genoa and astern, every few minutes'],
  ['6 Safe speed', 'go at a speed at which you can stop or avoid a collision', 'slow down in fog, in crowded water and at night'],
  ['7 Risk of collision', 'if the compass bearing of an approaching vessel does not appreciably change, risk of collision exists; it may exist even when the bearing changes, with a very large ship, a tow, or at close range', 'take bearings, or watch her against a stanchion: steady bearing, closing range, act. With a big ship, take bearings of her bow and her stern'],
  ['8 Action to avoid collision', 'act early, and make the change large enough to be obvious', 'one big turn, not several small ones, so that she sees your other sidelight, or your sails from a new angle'],
  ['9 Narrow channels', 'keep to the starboard side; small and sailing vessels must not impede a ship that can only use the channel', 'stay outside the buoyed channel where there is water; cross it as quickly as you safely can, never close ahead of a ship'],
  ['10 Traffic separation schemes', 'one-way shipping lanes, like a dual carriageway at sea; cross a lane on a heading at right angles to it, and do not impede ships in it', 'avoid them where you can; use the inshore traffic zone, the water between the scheme and the coast, meant for local and small craft'],
  ['12 Sailing vessels', 'port tack gives way to starboard; windward to leeward; on port, if in doubt, keep clear', 'see <a href="#sailing">Sailing fundamentals</a>'],
  ['13 Overtaking', 'a vessel coming up from more than 22.5° abaft the beam is overtaking and keeps clear, sail or power', 'the faster boat keeps out of the way, whatever it is'],
  ['14 and 15 Power-driven vessels', 'head-on, both turn to starboard; crossing, the one with the other on her starboard side keeps clear', 'under engine, a yacht is a power-driven vessel and follows these'],
  ['17 Stand-on vessel', 'the one not giving way holds course and speed, but must act if the other does not', 'hold on, watch, and act early if she is not turning; under engine, never turn to port for a vessel on your port side'],
  ['18 Responsibilities', 'a pecking order: not under command, restricted in ability to manoeuvre, constrained by draught, fishing, sailing, power', 'a sailing yacht keeps clear of vessels not under command, restricted or fishing, and must not impede one constrained by her draught'],
  ['19 Restricted visibility', 'no stand-on vessel in fog; avoid turning to port for a vessel ahead', 'radar and AIS if you have them, sound signals, slow down; head for shallow water out of the shipping'],
], wide=True, stack=True)}
  <p><strong>Sound signals</strong> (Rules 32, 34 and 35): a short blast lasts about a second, a prolonged blast four to six. In sight of each other, a power-driven vessel (including a yacht under engine) uses one short blast to mean “I am turning to starboard”; two short, “to port”; three short, “my engine is going astern”; five or more short and rapid, “I do not understand what you are doing”. In fog, a power-driven vessel making way sounds one prolonged blast at least every two minutes; a sailing vessel one prolonged and two short; a vessel at anchor rings a bell. A yacht under 12 m need only make “some other efficient sound signal” every two minutes, such as a foghorn.</p>
  <h4>Putting the lights and the rules together at night</h4>
  <ul>
    <li><strong>Motoring, you see a white light above a red one, on your starboard bow, its bearing steady.</strong> A power-driven vessel is crossing from your right to your left, showing you her port side. She has you on her port side, so you are the give-way vessel (Rule 15): turn to starboard, early and clearly, and pass behind her. The old rhyme: “If to starboard red appear, ’tis your duty to keep clear.”</li>
    <li><strong>Motoring, you see a white light above a green one, on your port bow, its bearing steady.</strong> She is crossing from your left, showing her starboard side: she must give way to you. Hold your course and speed (Rule 17), watch her, and act if she does not.</li>
    <li><strong>Under sail, you see a white light above both red and green, dead ahead.</strong> A power-driven vessel is heading straight for you. The rules say she gives way to you, but she may not have seen a yacht’s small lights: be ready to act early, and turn well clear if the bearing stays steady.</li>
    <li><strong>Under sail, you see another yacht’s red or green light.</strong> Lights do not show which tack she is on. If you are on port tack and see a sailing vessel to windward whose tack you cannot tell, keep clear (Rule 12(a)(iii)); in any doubt at night, keep clear anyway.</li>
  </ul>
{card('navigation--ship-crossing', 'A ship on a steady bearing', 'risk of collision, big ship, AIS', 'Out at sea, one of the commonest dangerous situations for a yacht is a ship that seems far away and gets close fast: a container ship at 20 knots covers a mile in three minutes, and from her bridge a small yacht can be hard to see.',
  ['Take a compass bearing of the ship, or line her up against a stanchion while holding the boat steady. A few minutes later, look again. If the bearing has not changed and she is getting closer, you are on a collision course. With a very large ship at close range, take bearings of her bow and her stern: there can be a risk of collision even while the bearing of her middle is changing.'],
  ['AIS on the plotter shows her closest point of approach (CPA) and the time to it, and a VHF call by name reaches her bridge.'],
  ['A ship cannot stop or turn quickly: many take miles to stop. In a narrow channel or a traffic lane she may be unable to turn at all, and the rules say you must not impede her.'],
  ['The bearing staying steady; her bow and both sidelights, or her masthead lights one above the other, pointing at you; AIS showing a CPA under a mile.'],
  ['Act early and obviously: a large turn, usually to pass behind her, or start the engine and get out of the way. If in doubt, call her on VHF channel 16 by name or position. Never try to cross close ahead.'], kind='fault', fold=True)}
{sources('lights, shapes and the collision rules', [
  'The collision regulations, all rules quoted: ' + a('https://www.navcen.uscg.gov/navigation-rules-amalgamated','USCG, International and Inland rules side by side') + '; towing lights: ' + a('https://ialacolreg.com/en/colreg/rule-24','Rule 24') + '.',
  'Checked by web search, September 2026; the pages could not be opened directly.',
])}

  <h3>Weather</h3>
  <ul>
    <li><strong>Forecasts.</strong> National services broadcast forecasts for sea areas and inshore waters: in the UK, the Met Office shipping forecast and inshore waters forecast on BBC Radio 4, and the coastguard’s maritime safety information on VHF, announced first on channel 16. NAVTEX, a small receiver on 518 kHz, prints forecasts and warnings in English; 490 kHz carries national ones. Other countries have their own; the <a href="#seas--forecasts">Seas section</a> lists them.</li>
    <li><strong>GRIB files</strong> are raw computer-model forecasts (GFS, ECMWF and others) that apps and plotters draw as wind arrows. They are good for the big picture and poor at local effects: gusts, sea breezes, winds funnelling round headlands and down valleys. Compare them with the official forecast, and add a third for the gusts.</li>
    <li><strong>The barometer</strong> reads air pressure in hectopascals (hPa, the same as millibars). A steady fall means a depression is coming; a fast one means strong wind soon. In shipping-forecast terms, a fall of more than about 3.5 hPa in three hours is “falling quickly”, and more than 6 hPa “very rapidly”: a warning of strong wind. Log the reading every few hours.</li>
    <li><strong>Depressions and fronts.</strong> In the northern hemisphere the wind blows anticlockwise round a low; stand with your back to the wind and the low is on your left (Buys Ballot’s law). As a warm front passes, cloud lowers, rain sets in and the wind veers (shifts clockwise); at the cold front behind it, squalls and heavy showers, a sharp veer, then clearing skies and a gusty wind.</li>
    <li><strong>Sea breezes.</strong> On a sunny day the land heats up and draws in a breeze off the sea from late morning, often force 3 or 4 by afternoon, dying at dusk; at night a lighter land breeze may blow off the shore. <strong>Katabatic winds</strong> pour down mountain slopes, strongest at night and in the morning, and can be violent where mountains meet the sea.</li>
    <li><strong>The named winds</strong> of each sea, such as the mistral, bora, meltemi and sirocco, are in the Seas section.</li>
    <li><strong>Fog</strong> at sea forms when warm, moist air crosses cold water (advection fog), most often in spring and early summer, and can last for days; radiation fog forms over land on clear, still nights and drifts into harbours and estuaries, usually clearing by late morning. Fog with shipping about is one of the most dangerous things a small boat can meet: see Rule 19 above.</li>
  </ul>

  <h3 id="navigation--passage-plan">Passage planning</h3>
  <p>SOLAS chapter V, regulation 34, requires every vessel going to sea, a yacht included, to plan the voyage; in the UK this is law for pleasure craft through the Merchant Shipping (Safety of Navigation) Regulations 2020. The Maritime and Coastguard Agency asks a yacht skipper to think about the weather, the tides, the limitations of the boat, the crew, the navigational dangers, a contingency plan, and leaving details with someone ashore. Written down, a plan for a day passage fits on one page:</p>
  <ol>
    <li><strong>Where and when:</strong> departure, destination and distance; the time to leave so that the tide is with you at the headlands and there is water over the bar (a bank of sand or shingle across a harbour or river entrance) or the sill (a low wall that keeps water in a marina) at both ends.</li>
    <li><strong>The route:</strong> waypoints checked zoomed in on the plotter and on a paper chart; courses and distances between them; dangers along the way and how you will clear them.</li>
    <li><strong>Tides:</strong> times and heights at both ends; tidal streams for each hour; tidal gates.</li>
    <li><strong>Weather:</strong> the forecast for the whole passage and the next day, and the limit you will not go out in.</li>
    <li><strong>Bolt holes:</strong> ports of refuge along the route, with the state of tide needed to enter each.</li>
    <li><strong>The pilotage plan</strong> for entering the harbour (pilotage is navigating by eye close to land, from mark to mark): marks to look for in order; leading lines (two marks or lights kept in line to stay in a safe channel); clearing bearings (a bearing of a landmark that keeps you clear of a danger as long as it stays above or below a set figure); depths; where to berth; written large enough to read in the cockpit.</li>
    <li><strong>Boat and crew:</strong> fuel and water, the engine checks, the safety kit; who is on board, their experience, seasickness, and a watch plan if it is a long day.</li>
    <li><strong>Information ashore:</strong> someone knows where you are going and when you expect to arrive, and what to do if you do not; the RYA’s SafeTrx app, which did this in the UK, closed at the end of 2025, so leave the plan with a trusted person who knows when to call the coastguard.</li>
  </ol>
{sources('weather and passage planning', [
  'Pressure tendency terms: ' + a('https://weather.metoffice.gov.uk/guides/coast-and-sea','Met Office, guide to marine forecasts') + ', ' + a('https://www.gjwdirect.com/blog/understanding-marine-forecasts/','GJW Direct, shipping forecast terms') + '. Sea breezes: ' + a('https://www.yachtingmonthly.com/sailing-skills/understand-sea-breeze-49027','Yachting Monthly, understanding a sea breeze') + '. Navtex: ' + a('https://www.rya.org.uk/water-safety/safety-equipment/navtex/','RYA, Navtex') + '.',
  'Passage planning: ' + a('https://www.rya.org.uk/regulations/solas-v-regulations/','RYA, SOLAS V for pleasure vessels') + ', ' + a('https://www.gov.uk/government/publications/mgn-599-m-amendment-1-m-pleasure-vessels-regulations-and-exemptions-guidance-and-best-practice-advice/mgn-599-m-amendment-1m-pleasure-vessels-regulations-and-exemptions-guidance-and-best-practice-advice','MCA, MGN 599 for pleasure vessels') + '. SafeTrx closure: ' + a('https://www.pbo.co.uk/news/boaters-beware-rya-safetrx-vessel-tracking-safety-app-will-soon-close-100567','Practical Boat Owner') + '.',
  'Checked by web search, September 2026; the pages could not be opened directly.',
])}

  <h3>Worth watching</h3>
  <p>No videos have been found and checked for this section yet; they are listed as planned below.</p>

  <h3>Terms used in this section</h3>
  <h4 class="terms__group">Direction</h4>
{terms([
 ("nv-true","True north","The direction of the geographic north pole; chart grids and chart bearings use it."),
 ("nv-magnetic","Magnetic north","Where a compass free of the boat’s influence points. It differs from true north by the variation."),
 ("nv-compass-n","Compass north","Where the boat’s own steering compass points, pulled a little by the boat’s iron and wiring."),
 ("nv-heading","Heading","The direction the bow points, in degrees."),
 ("nv-variation","Variation","The angle between true and magnetic north at a place, printed on the chart with its year and yearly change. West or east."),
 ("nv-deviation","Deviation","The error of a particular compass on a particular boat, which changes with the boat’s heading; listed on a deviation card."),
])}
  <h4 class="terms__group">Charts and tides</h4>
{terms([
 ("nv-hat","High-water level","The level heights of lights and clearances are measured from: mean high water springs (MHWS) or highest astronomical tide (HAT), as the chart states."),
 ("nv-sea-level","Sea level now","The actual surface of the sea, which moves up and down with the tide."),
 ("nv-chart-datum","Chart datum","The level charted depths are measured from; in tidal waters about the lowest astronomical tide (LAT), so the sea rarely falls below it."),
 ("nv-drying","Drying height","The height of a rock or bank above chart datum, underlined on the chart; it is uncovered at low tide."),
 ("nv-charted-depth","Charted depth","The depth below chart datum printed on the chart."),
 ("nv-height-of-tide","Height of tide","How far the sea is above chart datum at a given time, from the tide tables."),
 ("nv-depth","Depth of water","Charted depth plus the height of tide: what the sounder should read (allowing for where its transducer is)."),
 ("nv-light-height","Height of a light","Measured from the chart’s high-water level to the light itself; the higher, the further it can be seen."),
 ("nv-tide-curve","Tide curve","The rise of the tide from low to high water: slow at first, fastest at mid-tide, slow again near high water."),
 ("nv-mid-tide","Mid-tide","The middle two hours of the rise or fall, when the height changes fastest and the stream runs hardest."),
 ("nv-ground-track","Ground track","The line over the seabed from where you are to where you are going; drawn with two arrowheads."),
 ("nv-tide-vector","Tidal stream vector","One hour of tidal stream, direction and rate, drawn with three arrowheads."),
 ("nv-water-track","Water track","The course to steer through the water, drawn with one arrowhead; its length is one hour of boat speed."),
 ("nv-sog","Speed over the ground","How far you move over the seabed in an hour: the distance along the ground track to where the water track cuts it."),
])}
  <h4 class="terms__group">Buoys and marks</h4>
{terms([
 ("nv-buoyage-direction","Direction of buoyage","The direction lateral marks are arranged for: from the sea into harbour, or along a coast as shown on the chart."),
 ("nv-port-mark","Port-hand mark","Red, can-shaped or with a can topmark, red light: keep it on your port (left) side going with the direction of buoyage."),
 ("nv-stbd-mark","Starboard-hand mark","Green, cone-shaped or with a cone topmark pointing up, green light: keep it on your starboard side going with the direction of buoyage."),
 ("nv-pref-stbd","Preferred channel to starboard","Red with a broad green band, light Fl(2+1) R: the main channel is to starboard; treat it as a port-hand mark."),
 ("nv-pref-port","Preferred channel to port","Green with a broad red band, light Fl(2+1) G: the main channel is to port; treat it as a starboard-hand mark."),
 ("nv-danger","The danger","A rock, shoal or wreck that the cardinal marks are placed around."),
 ("nv-north","North cardinal","Black over yellow, two cones pointing up, continuous quick flashes. Safe water is to its north."),
 ("nv-east","East cardinal","Black, yellow, black, two cones base to base, three quick flashes. Safe water is to its east."),
 ("nv-south","South cardinal","Yellow over black, two cones pointing down, six quick flashes and a long flash. Safe water is to its south."),
 ("nv-west","West cardinal","Yellow, black, yellow, two cones point to point, nine quick flashes. Safe water is to its west."),
 ("nv-isolated","Isolated danger mark","Black with red bands, two black balls, white light Fl(2): a small danger right under it, with safe water all round."),
 ("nv-safe-water","Safe water mark","Red and white vertical stripes, one red ball, a white light that is isophase, occulting, one long flash every 10 seconds or Morse A: safe water all round, often the start of a channel."),
 ("nv-special","Special mark","Yellow, a yellow X, a yellow light: marks something that is not a navigation hazard, such as an outfall, a zone or a data buoy."),
 ("nv-wreck","Emergency wreck marking buoy","Blue and yellow vertical stripes, a yellow upright cross, alternating blue and yellow flashes: a new wreck not yet on the charts."),
])}
  <h4 class="terms__group">Lights and shapes</h4>
{terms([
 ("nv-steaming","Steaming light","A white masthead light showing forward over 225°, shown by power-driven vessels, and by a yacht under engine."),
 ("nv-green","Starboard sidelight","A green light showing from dead ahead to 22.5° abaft the starboard beam."),
 ("nv-red","Port sidelight","A red light showing from dead ahead to 22.5° abaft the port beam."),
 ("nv-stern","Sternlight","A white light showing over 135° astern."),
 ("nv-tricolour","Tricolour","Red, green and white sectors in one masthead lantern, allowed for a sailing vessel under 20 m under sail only."),
 ("nv-anchored","At anchor","One all-round white light (two for a vessel of 50 m or more), one black ball by day."),
 ("nv-nuc","Not under command","Unable to manoeuvre, for example with a broken engine or steering: two all-round red lights, two balls."),
 ("nv-ram","Restricted in ability to manoeuvre","Doing work that stops her getting out of the way, such as dredging or laying cable: red, white, red lights; ball, diamond, ball."),
 ("nv-cbd","Constrained by her draught","A deep ship that cannot leave the deep water: three all-round red lights, a cylinder."),
 ("nv-trawling","Trawling","Dragging a net: green over white all-round lights, two cones point to point."),
 ("nv-fishing","Fishing other than trawling","With nets or lines out: red over white all-round lights, two cones point to point."),
 ("nv-pilot","Pilot vessel","On pilotage duty: white over red all-round lights; flag H by day."),
 ("nv-motorsailing","Motor-sailing","Under sail with the engine driving the propeller: a power-driven vessel under the rules. By day, a black cone point down in the rigging."),
])}

  <div class="planned">
    <p>Planned for this section</p>
    <ul>
      <li>Source links for the rules, the buoyage and the forecast services (written without live sources; see the note at the top)</li>
      <li>Diagrams: a three-point fix and a transit; a secondary port calculation; a clearing bearing; the lights of a ship seen from ahead, abeam and astern</li>
      <li>A printable passage plan template</li>
      <li>Worked examples: a tidal cross-Channel passage, an Adriatic island hop, a Baltic skerry passage</li>
      <li>Videos, being checked before they are linked: chartwork basics, tidal heights, the collision rules</li>
    </ul>
  </div>
</section>
'''
finish(page, ROOT + 'sections/11-navigation.html', others=(ROOT + 'sections/03-hull.html', ROOT + 'sections/04-rig.html', ROOT + 'sections/05-deck.html', ROOT + 'sections/06-engine.html', ROOT + 'sections/07-systems.html', ROOT + 'sections/08-electronics.html', ROOT + 'sections/09-sailing.html', ROOT + 'sections/10-manoeuvres.html', ROOT + 'sections/02-fleet.html', ROOT + 'sections/00-start.html'))
