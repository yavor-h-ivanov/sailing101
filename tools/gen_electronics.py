# Generates sections/08-electronics.html for Sailing 101.
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_common import *
import gen_electronics_diagrams as g


page = f'''<section id="electronics">
  <h2>Electronics</h2>
  <p class="lead">Instruments tell you how deep it is, how fast you are going and where the wind is; the radio lets you call for help; AIS and radar show you other ships; the plotter shows you where you are. Old boats carry every generation of them at once, some working, some not, all wired by different people. In a hurry? Jump to <a href="#electronics--mayday">the Mayday call</a>, <a href="#electronics--faults">faults by symptom</a> or <a href="#electronics--checklist">the buyer’s checklist</a>.</p>

  <details class="first-words" open>
    <summary>Seven words before anything else</summary>
    <dl>
      <dt>Transducer</dt><dd>A sensor through or on the hull: the depth sounder’s is a small cylinder that sends and hears sound pulses; the log’s is a little paddle wheel.</dd>
      <dt>VHF</dt><dd>Very high frequency: the marine radio used for calling other boats, marinas and the coastguard. It reaches about as far as the eye could see from the top of its antenna.</dd>
      <dt>DSC</dt><dd>Digital selective calling: a button on a modern VHF that sends a digital distress alert with your identity and position.</dd>
      <dt>MMSI</dt><dd>Maritime mobile service identity: the boat’s nine-digit radio number, issued with its radio licence.</dd>
      <dt>AIS</dt><dd>Automatic identification system: ships broadcast their name, position, course and speed by radio, and a plotter shows them.</dd>
      <dt>Chartplotter</dt><dd>A screen that shows an electronic chart with your position on it from GPS.</dd>
      <dt>NMEA</dt><dd>The standards (0183 and 2000) that let instruments of different makes share data.</dd>
    </dl>
    <p class="first-words__note">The autopilot’s drives are covered in <a href="#deck--autopilot">Deck hardware and steering</a> and the power the electronics use in <a href="#systems--monitor">Boat systems</a>.</p>
  </details>
  <p class="conf-key"><b>Marks used below:</b> {ONE} single source; {TWO} sources disagree or anecdotal; {TBC} not yet verified. <b>How this section was checked:</b> in September 2026 each figure and rule was checked by web search against the pages linked in the “Sources and confidence” block at the end of each topic. The search results were read, but the pages themselves could not be opened from the editing session, so a figure confirmed only that way is linked but not quoted. Anything not confirmed is still marked {TBC}.</p>

  <h3>What is where</h3>
{figure('fig-el-where', 'where it lives', '0 0 900 510', 'Where the electronics are fitted on a 10 m yacht', 'A side view of a sloop, bow to the right. At the masthead: the VHF antenna, the wind unit with its vane and cups, and the tricolour and anchor light. On the mast: a radar dome on a bracket and the steaming light. On the pushpit at the stern: the GPS antenna, and on some boats a separate AIS antenna. At the helm: the chartplotter; on the cabin bulkhead: instrument displays. Below, at the chart table: the fixed VHF with DSC and the AIS unit. Low and central: the autopilot’s fluxgate compass. Under the hull: the depth transducer and the log paddle wheel. On the bow pulpit: the sidelights.', g.where(), 'Every antenna wants to be high and every transducer wants clean, smooth water; everything in between is cable, and the cable through the mast foot and the deck is where most faults live.', note=HINT)}

  <h3>The instruments</h3>
{card('electronics--depth', 'Depth sounder', 'echo sounder, depth transducer, fishfinder', 'A transducer in the hull sends a pulse of sound down and times the echo from the bottom. The one instrument you cannot do without: every grounding in shallow water is a depth question.',
  ['It measures from the transducer, not from the surface or the keel. The display is set with an offset so that it shows either depth below the keel (most useful when entering harbour) or depth of water below the surface (what the chart and tide tables use): find out which yours shows, and write it on the display.', 'A shallow alarm set to the keel depth plus a margin is the cheapest safety device on the boat.'],
  ['Simple, reliable and cheap to replace; a modern fishfinder-type sounder shows the shape of the bottom, which helps when anchoring.'],
  ['Reads nothing, or nonsense, in aerated water, full of bubbles (in a boat’s wake, a tide race where the tidal stream runs fast over the seabed, or at speed), over soft mud, and in very deep water; a transducer inside the hull (shooting through the laminate) loses some range.'],
  ['Erratic readings from weed or antifouling paint of the wrong type on the transducer face; a corroded cable; an offset nobody knows.'],
  ['Compare the reading with a lead line (a weighted rope marked in metres) or the chart in a known depth; ask what the offset is.'], fold=True)}

{card('electronics--log', 'Log: speed through the water', 'paddle wheel, speed transducer, distance log', 'A small paddle wheel in a through-hull fitting that turns as the water flows past and gives speed through the water and distance run. GPS gives speed over the ground; the difference between the two is the tidal stream or current.',
  ['The paddle wheel sits in a housing with a blanking plug: pull the wheel out and push the plug in, quickly, to clean it; a flap valve on many types limits the water that comes in meanwhile.'],
  ['Speed through the water is what the sails and the true-wind calculation need, and what tells you how the boat is sailing.'],
  ['The wheel fouls with weed and barnacles in weeks in warm water, and the log reads low or nothing.'],
  ['A log that reads zero or much less than GPS in still water; a leaking housing seal; a blanking plug missing from the boat.'],
  ['Find the plug before you need it; clean the wheel at the start of each season and pull it when the boat is left for long.'], fold=True)}

{card('electronics--wind', 'Wind instruments', 'masthead unit, apparent wind, true wind', 'A vane and a set of spinning cups on a bracket at the masthead measure the wind the boat feels (the apparent wind). With the boat’s speed through the water, the instrument calculates the true wind: the wind over the water, as a boat drifting with the current would feel it.',
  ['Apparent wind is the true wind combined with the wind of the boat’s own motion: sailing towards the wind it is stronger than the true wind, sailing away from it lighter; and on every heading except dead ahead or dead astern it comes from further forward than the true wind. The Sailing section explains why this matters.'],
  ['Wind angle is the best guide to trimming and steering at night; wind speed tells you when to reef before the boat does.'],
  ['The masthead unit is the hardest part of the boat to reach; its bearings (the rings its spindle turns in, nothing to do with compass bearings) wear and its cable runs down the mast through a connector at the foot that corrodes.'],
  ['Cups that spin but a speed that reads zero (a cable or connector fault); a vane reading stuck at one angle; a true wind that swings about as the boat speeds up and slows down (the log is wrong).'],
  ['Watch the readings change as the boat turns in harbour; look at the connector at the mast foot.'], fold=True)}

{card('electronics--compass', 'Compass: steering compass and fluxgate', 'binnacle compass, bulkhead compass, hand-bearing compass, deviation', 'The steering compass on the pedestal or bulkhead needs no electricity and rarely fails; a fluxgate compass is an electronic sensor that gives the heading to the autopilot and the instruments; a hand-bearing compass is held up to take bearings of landmarks.',
  ['Any compass is pulled off magnetic north by iron and electrical fields near it on the boat. This error is called deviation, and it changes with the boat’s heading; a compass adjuster (a specialist) can reduce it and draw a deviation card, a table of the error on each heading. It is not the same as variation, the difference between magnetic north and true north, which depends on where you are and is printed on the chart (see <a href="#navigation">Navigation</a>).', 'The fluxgate wants to be low, near the boat’s centre where it moves least, and away from the engine, the keel bolts, loudspeakers and cables carrying current.'],
  ['A good steering compass is the backup to every electronic system on the boat.'],
  ['A loudspeaker, a mobile phone or a tin of food put next to it changes its reading; old compasses lose their fluid and gain a bubble.'],
  ['A bubble in the compass bowl; a card that sticks or swings wildly; an autopilot that wanders on some headings (fluxgate near iron); no compass light for night sailing.'],
  ['Compare the steering compass with the plotter’s course over the ground in calm water on several headings; keep phones and tools a metre away.'], fold=True)}

{card('electronics--plotter', 'Chartplotter and tablets', 'MFD, electronic charts, Navionics, C-MAP, navigation apps', 'A plotter shows your GPS position on an electronic chart. On a boat of this size it may be a fixed display at the helm, a multi-function display that also shows radar and AIS, or a tablet or phone running a navigation app with downloaded charts.',
  ['GPS gives a position to within a few metres; the chart underneath may be less accurate than that, because some surveys are old or were drawn on a different datum (the reference shape of the Earth). Treat the boat symbol as right and the chart as approximately right.', 'Electronic charts hide detail when zoomed out: a reef that shows at one scale can vanish at the next. This contributed to the grounding of the racing yacht Vestas Wind on a reef in the Indian Ocean in the 2014–15 Volvo Ocean Race. Zoom in along the route before you sail it.'],
  ['The biggest safety improvement in small-boat navigation in a generation: you know where you are.'],
  ['It fails with the batteries, the GPS signal, water in the connector or a flat tablet; charts go out of date.'],
  ['A plotter that loses its fix (the antenna or its connection); charts that are years old; a tablet that overheats in the sun and shuts down.'],
  ['Carry paper charts, or at least a second device with charts on its own battery, and know how to plot a position by hand (see Navigation).'], fold=True)}

  <h3>Radio: VHF and DSC</h3>
{card('electronics--vhf', 'Fixed VHF radio with DSC', 'marine VHF, channel 16, DSC distress button', 'The fixed set at the chart table, with its antenna at the masthead, is the boat’s main safety radio. It transmits at 25 W, or 1 W on its low-power setting for short range, and a modern set has DSC.',
  ['Channel 16 is the international distress, safety and calling channel, and is listened to by coastguards and ships; after the first contact you move to a working channel. Channel 70 is reserved for DSC and carries no voice.', 'Pressing the red distress button (under a flap, held for a few seconds) sends a digital Mayday with the boat’s MMSI and, if the set is connected to a GPS, its position. Many older installations were never connected to the GPS {TWO}, so they send no position: check yours.'],
  ['Everyone within range hears a voice call on channel 16, which is why VHF, not a phone, is the way to call for help at sea.'],
  ['Range is line of sight (see below). A set needs a ship radio licence for the boat and a trained, certificated operator (see Licences).'],
  ['Weak or no transmission from a corroded antenna connector at the masthead or mast foot, or water in the coaxial cable; a DSC set with no MMSI entered or no GPS connection; a microphone cable worn through.'],
  ['Make a radio check with a marina or another boat on a working channel (not channel 16) and ask how you sound; look for the MMSI on the set’s screen and the GPS position in its DSC menu.'], fold=True)}

{figure('fig-vhf-range', 'VHF range', '0 0 900 320', 'VHF range depends on the height of both antennas', 'A curved sea surface, exaggerated. A yacht on the left with a masthead antenna about 15 m up and a coastguard aerial on a hill on the right about 100 m up. A dashed line runs from each antenna down to the horizon point between them, where the two horizons meet. A rule of thumb underneath: range in nautical miles is about 2.2 times the sum of the square roots of the two antenna heights in metres.', g.vhf_range(), 'Worked from the rule of thumb (our arithmetic; sources give factors from about 2.2, the radio horizon, to 3 {TWO}): masthead to masthead, both 15 m, about 17 miles; masthead to a coastguard aerial at 100 m, about 30 miles; a handheld at 1.5 m to another handheld, about 5 miles. Real ranges vary with power, cable losses and the weather.')}

{card('electronics--handheld', 'Handheld VHF', 'portable VHF, floating handheld', 'A small waterproof radio with its own battery, transmitting at a few watts from a short aerial. It is the radio for the cockpit, the dinghy and the liferaft, and the backup when the main set or the mast is lost.',
  ['Many now have DSC and GPS built in; a DSC handheld needs its own MMSI, never the fixed set’s. Held at head height, their range is a few miles to another small boat and more to a coastguard aerial on a hill.'],
  ['Works when the boat’s electrics or antenna do not; floats (on many models); goes in the grab bag.'],
  ['Short range and limited battery; sets bought abroad may not have the European channel plan.'],
  ['A flat battery, a lost belt clip, a set on a different channel plan.'],
  ['Keep it charged, programmed with its own MMSI, and in the grab bag when offshore.'], fold=True)}

  <h4 id="electronics--radio-check">Making a radio check</h4>
  <ol>
    <li>Choose a working channel, never channel 16: a marina’s own channel, or a channel used between boats, such as 6, 8, 72 or 77, the channels UK guidance gives for talk between boats.</li>
    <li>Say: “(Marina name or ‘any station’), this is (boat name), radio check on channel (number), over.”</li>
    <li>The reply tells you how you sound: “loud and clear” is what you want; “weak” or “broken” means a look at the antenna and its connectors.</li>
    <li>Many sets can also make a DSC test call; how it works, and which coast stations accept one, varies by country {TBC}.</li>
  </ol>

  <h4 id="electronics--mayday">The Mayday call, by voice</h4>
  <div class="callout danger">
  <p>If a person or the boat is in grave and imminent danger: first press and hold the red DSC distress button, if the set has one: it sends your identity and position at once. Then, on channel 16, high power, speak slowly. Keep a card by the radio with the boat’s name, call sign (the letters and numbers issued with the ship radio licence) and MMSI, and read the position from the plotter, the GPS or the DSC set’s screen. Mayday is said as the English “may day”, Pan-Pan as “pahn-pahn”, Sécurité as “say-cure-ee-tay”.</p>
  <ol class="lettered">
    <li><span class="lettered__l">M</span><span class="lettered__t"><strong>MAYDAY, MAYDAY, MAYDAY.</strong></span></li>
    <li><span class="lettered__l">I</span><span class="lettered__t"><strong>Identify:</strong> “This is (boat name, three times), call sign, MMSI.” Then “MAYDAY (boat name) (call sign and MMSI once)”.</span></li>
    <li><span class="lettered__l">P</span><span class="lettered__t"><strong>Position:</strong> latitude and longitude from the plotter or GPS, or a bearing and distance from a charted point.</span></li>
    <li><span class="lettered__l">D</span><span class="lettered__t"><strong>Distress:</strong> what is happening, in a few words (“sinking”, “on fire”, “man overboard”).</span></li>
    <li><span class="lettered__l">A</span><span class="lettered__t"><strong>Assistance:</strong> what you need (“require immediate assistance”).</span></li>
    <li><span class="lettered__l">N</span><span class="lettered__t"><strong>Number of people</strong> on board.</span></li>
    <li><span class="lettered__l">I</span><span class="lettered__t"><strong>Information:</strong> anything that helps rescuers: “abandoning to liferaft”, the boat’s colour.</span></li>
    <li><span class="lettered__l">O</span><span class="lettered__t"><strong>OVER.</strong> Then listen. Repeat if there is no answer.</span></li>
  </ol>
  </div>
  <p>“Pan-Pan” (said three times) is for urgency without grave and imminent danger, such as an engine failure in open water or a crew member who needs medical advice; an engine failure close to rocks, with the boat being blown onto them, is a Mayday. “Sécurité” is for safety messages. The operator of the set needs a certificate (in the UK the Short Range Certificate, taught in a one-day RYA course) and the boat needs a ship radio licence: see <a href="#licences">Licences</a>.</p>
  <p><strong>If you hear someone else’s Mayday:</strong> write it down, stay off the air and listen. If no coastguard or other station answers within a few minutes, and you can help or relay it, answer it; the radio course teaches how.</p>
  <p><strong>A DSC alert sent by mistake</strong> must be cancelled at once: cancel it on the set as its manual describes, then on channel 16 say: “All stations, all stations, all stations, this is (boat name three times), call sign, MMSI, position. Cancel my distress alert of (date) at (time, in UTC). (Boat name), MMSI, out.” Follow your set’s manual: on most modern sets, do not switch the radio off before cancelling, because they send the alert again when switched back on (older procedures said the opposite {TWO}). Coastguards generally say that an accidental alert cancelled at once will not get you into trouble {ONE}.</p>
{sources('radio', [
  'Channels 16 and 70, DSC, powers: ' + a('https://www.navcen.uscg.gov/international-vhf-marine-radio-channels-freq','USCG, international VHF channels') + ', ' + a('https://en.wikipedia.org/wiki/Marine_VHF_radio','Wikipedia, marine VHF radio') + '.',
  'Channels between boats (6, 8, 72, 77): ' + a('https://www.offshoreblue.com/comms/vhf-uk.php','Offshore Blue, UK VHF channels') + ', ' + a('https://pzsc.org.uk/radio/channels/','Penzance Sailing Club channel guide') + '.',
  'Range rule: ' + a('https://www.offshoreblue.com/comms/vhf-capabilities.php','Offshore Blue, VHF range') + ' (gives about 3 × √h) and the standard radio-horizon figure of about 2.2 × √h; the worked figures are our arithmetic ²',
  'Distress alert and cancelling: ' + a('https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.493-16-202312-I!!PDF-E.pdf','ITU-R M.493-16') + ', ' + a('https://bluewatermiles.com/docs/gmdss-distress-cancel-procedure-card.pdf','Bluewater Miles cancel-procedure card') + ', ' + a('https://www.navcen.uscg.gov/dsc-distress','USCG on DSC distress') + ' ¹ for “no trouble if cancelled”, and ' + a('https://www.navcen.uscg.gov/instructions-for-canceling-false-distress-alert','USCG, cancelling a false distress alert') + ' for not switching off.',
  'Checked by web search, September 2026; the pages could not be opened directly. The DSC test call is still TBC.',
])}

  <h3>AIS and radar</h3>
{figure('fig-ais', 'what AIS shows', '0 0 900 400', 'What AIS shows on a plotter, and what it does not', 'Two panels. Left, a plotter screen: your own boat, another AIS boat, and a ship with its name, course and speed and a line showing where it will be, with the closest point of approach marked. Right, the same water as it really is: the same boats, plus yachts without AIS, fishing gear, buoys and swimmers, and a ship hidden behind an island, whose signal the land blocks.', g.ais(), 'Solid shapes: the boats now; pale shapes: where they will be at the closest point. AIS is the best collision-avoidance tool a small boat has had, and it shows only what transmits and what your antenna can hear. The look-out is still the law, and the most important safety device on board.')}

{card('electronics--ais', 'AIS: receiver or transponder', 'Class A, Class B, CPA, TCPA', 'An AIS receiver listens for ships’ broadcasts and shows them on the plotter; a transponder also broadcasts your own position so that ships see you. Commercial ships above a set size carry Class A sets, transmitting at 12.5 W every 2 to 10 seconds under way; yachts fit Class B transponders, the common type transmitting at 2 W about every 30 seconds when moving faster than 2 knots, and every 3 minutes when slower.',
  ['Each ship sends its identity, position, course, speed and heading. The plotter calculates the closest point of approach (CPA) and the time until then (TCPA), and can sound an alarm when a ship will pass within a distance you choose.', 'AIS uses VHF, so it has VHF range, and many boats share the masthead VHF antenna through a splitter. A transponder needs the boat’s MMSI.'],
  ['Names on the screen let you call a ship by name instead of “the ship off my port bow”; CPA takes the guesswork out of crossing a shipping lane.'],
  ['Many small boats and some fishing boats carry no AIS or switch it off; ships filter out small Class B targets on busy screens {TWO}; land and the curve of the Earth block it; a transponder adds to your electrical load.'],
  ['A transponder that is not transmitting (no MMSI entered, or a silent mode left on); a splitter that has failed and taken the VHF with it; targets that are all shown at wrong positions (the GPS source).'],
  ['Look at yourself on a phone app or a friend’s plotter to prove the transponder transmits. Set a CPA alarm (many sailors use about a mile in open water {TWO}); when a ship will pass close, act early and clearly, or call it by name on channel 16 or 13 (the international bridge-to-bridge channel for navigation between ships, used at low power). The rules for who gives way are in <a href="#navigation">Navigation</a>. Keep a look-out whatever the screen shows.'], fold=True)}

{card('electronics--radar', 'Radar', 'radar scanner, dome, MARPA, radar reflector', 'A rotating scanner, usually in a dome on a mast bracket, that shows everything that reflects radio waves: ships, land, buoys, heavy rain, and boats with no AIS. It is the tool for fog and for night passages in busy water.',
  ['The scanner sends pulses and times their echoes, so it sees targets in fog and darkness, including those without AIS. MARPA (mini automatic radar plotting aid) on many sets tracks a chosen target and gives its course and CPA, as AIS does.', 'A radar reflector on your own mast helps other ships’ radars see a GRP or wooden yacht, which reflects little by itself.'],
  ['The only instrument that shows a small fishing boat with no AIS in fog.'],
  ['Expensive, power-hungry and needs training to read: a screen of clutter from waves and rain means nothing to the untrained eye; a small yacht’s scanner is low, so its range is short.'],
  ['A scanner that no longer turns or shows no picture (the cable through the mast, or the magnetron, the transmitting valve of older pulse radars, which wears out; solid-state radars have none); a dome that has been hit by the genoa and cracked.'],
  ['On a boat with radar, ask for a demonstration in harbour and learn to read it in good visibility before you need it in fog.'], fold=True)}
{sources('AIS and radar', [
  'AIS classes, powers and reporting rates: ' + a('https://www.navcen.uscg.gov/types-of-ais','USCG, types of AIS (ITU-R M.1371)') + ', ' + a('https://navcen.uscg.gov/ais-class-a-reports','USCG, Class A reports') + ', ' + a('https://www.milltechmarine.com/faq.htm','Milltech Marine AIS FAQ') + '.',
  'Channel 13: ' + a('https://www.offshoreblue.com/comms/vhf-frequencies.php','Offshore Blue, channel designators') + '. The CPA distance is sailors’ practice, not a rule ².',
  'Checked by web search, September 2026; the pages could not be opened directly.',
])}

  <h3>Safety beacons and weather</h3>
{card('electronics--epirb', 'EPIRB, PLB and AIS man-overboard beacons', '406 MHz, Cospas-Sarsat, personal locator beacon, MOB beacon', 'Three kinds of beacon send a distress alert when switched on. An <strong>EPIRB</strong> belongs to the boat and alerts rescuers through satellites; a <strong>PLB</strong> is a smaller version that belongs to a person; an <strong>AIS man-overboard beacon</strong>, worn on a lifejacket, shows the person in the water on the AIS screens of your own boat and others nearby.',
  ['EPIRBs and PLBs transmit on 406 MHz to the Cospas-Sarsat satellites, which pass the alert to a rescue centre; beacons with built-in GPS send their position with it, while older ones without GPS are located by the satellites, less exactly and more slowly; a 121.5 MHz signal lets rescuers home in on it. The rescue centre knows who you are only if the beacon has been registered (in the UK, with the Maritime and Coastguard Agency’s beacon registry, free and required by law).', 'An AIS MOB beacon is short-range: it tells your own crew, and boats close by, exactly where the person is, which is what matters most in the first minutes.'],
  ['A registered EPIRB is the surest way of being found at sea; a PLB or AIS beacon on each lifejacket is a small price for finding a person overboard.'],
  ['Batteries and registrations expire; a beacon that is not registered or has the previous owner’s details wastes rescuers’ time.'],
  ['An expired battery; a registration in the previous owner’s name; an EPIRB bracket whose automatic release has corroded.'],
  ['Read the battery date and the registration; update the registration when you buy the boat; do the self-test the maker describes.'], fold=True)}

{card('electronics--weather', 'Navtex and weather on board', 'Navtex, weather forecasts, GRIB files', 'Navtex is a small receiver that prints or displays navigation and weather warnings and forecasts broadcast from coast stations on 518 kHz, in English, with national-language services on 490 kHz. A station reaches about 250 to 400 miles. Forecasts also come by VHF from coastguards, and by phone or satellite as GRIB files (wind forecasts shown on a chart).',
  ['Each Navtex station has a letter and a time slot; you choose which stations and which message types (gale warnings, forecasts, navigational warnings) to receive.'],
  ['Works far offshore, beyond the phone signal, with no subscription, and gale warnings arrive without anyone having to listen.'],
  ['Short text, sometimes in abbreviated forms; coverage and station letters differ between the seas covered here.'],
  ['A receiver set to the wrong stations, so nothing arrives; a set whose antenna cable was cut when the mast was last taken down.'],
  ['Set it up for the area and check that warnings arrive before leaving harbour. The Navigation section covers forecasts and how to read them.'], fold=True)}
{sources('beacons and weather', [
  'Beacons, 406 and 121.5 MHz: ' + a('https://www.rya.org.uk/water-safety/safety-equipment/406-mhz-epirb-plb/','RYA, 406 MHz EPIRB and PLB') + ', ' + a('https://www.navcen.uscg.gov/emergency-position-indicating-radiobeacon','USCG on EPIRBs') + '; UK registration: ' + a('https://register-406-beacons.service.gov.uk/','UK 406 MHz beacon registry') + '.',
  'Navtex frequencies, language and range: ' + a('https://www.rya.org.uk/water-safety/safety-equipment/navtex/','RYA, Navtex') + ', ' + a('https://en.wikipedia.org/wiki/NAVTEX','Wikipedia, NAVTEX') + ', ' + a('https://hnhs.gr/en/2015-05-28-16-58-21-2015-05-28-16-59-41-navtex/','Hellenic Navy Hydrographic Service, Navtex') + '.',
  'Checked by web search, September 2026; the pages could not be opened directly.',
])}

  <h3>Networks: how the instruments talk</h3>
{figure('fig-nmea', 'NMEA networks', '0 0 900 380', 'NMEA 0183 point-to-point wiring compared with an NMEA 2000 backbone', 'Two panels. Left: a GPS (the talker) with separate wires to a chartplotter, a VHF with DSC and an autopilot (the listeners), and a multiplexer shown as the device needed when two talkers must reach one listener. Right: a backbone cable with a terminator at each end, T-pieces along it with drop cables to a plotter, wind, depth and log, autopilot and AIS, and a power tee in the middle feeding it 12 V through a fuse.', g.nmea(), 'A 1990s boat has NMEA 0183: pairs of wires, one talker per pair. A boat refitted in the last fifteen years probably has NMEA 2000, under its own name or a maker’s (Raymarine SeaTalkNG, Simrad and B&G SimNet): one cable for everything.')}

{card('electronics--networks', 'NMEA 0183, NMEA 2000 and the old maker systems', 'SeaTalk, SeaTalkNG, SimNet, multiplexer, gateway', 'NMEA 0183 is an old serial standard: one device (the talker) sends sentences of text down a pair of wires to one or more listeners. NMEA 2000 is a network: every device plugs into one shared backbone cable and hears every other. Many boats of this age also have a maker’s own system of the 1980s and 1990s, such as Raymarine’s original SeaTalk.',
  ['On NMEA 0183, each output can feed a few inputs but each input can listen to only one output; getting data from the GPS and the wind instrument into one plotter needs a multiplexer. AIS data needs a faster 0183 port (38,400 baud against the usual 4,800).', 'On NMEA 2000 the backbone must have a terminator at each end and be powered once, through a fused power tee; each device hangs off a T-piece on a short drop cable. A gateway translates between old 0183 or SeaTalk devices and a 2000 network.'],
  ['NMEA 2000 makes adding a device a matter of one more T-piece; gateways let a good old instrument keep working.'],
  ['On an old boat, the wiring of 0183 connections is rarely drawn anywhere; mixed systems of three generations are fragile and slow to fault-find.'],
  ['Data missing on one display (a failed talker, a loose 0183 wire); the whole 2000 network dead (the power tee’s fuse, a missing terminator, water in a connector); two GPS positions fighting on one screen.'],
  ['Draw the network as you find it and keep the drawing on board; label every cable at both ends.'], fold=True)}
{sources('networks', [
  'NMEA 0183 speeds: ' + a('https://actisense.com/wp-content/uploads/2021/01/Everything-you-need-to-know-about-NMEA-0183-1.pdf','Actisense, everything about NMEA 0183') + ', ' + a('https://www.yachtd.com/downloads/ydng02.pdf','Yacht Devices NMEA 0183 gateway manual') + ', ' + a('https://support.vespermarine.com/hc/en-us/articles/210478126-Connecting-two-0183-devices-at-different-baud-rates-VHF-and-plotter','Vesper Marine on mixed baud rates') + '.',
  'NMEA 2000 backbone rules: the installation guides of Raymarine, Garmin and Navico (Simrad, B&G, Lowrance), and ' + a('https://www.nmea.org/','NMEA') + '.',
  'Checked by web search, September 2026; the pages could not be opened directly.',
])}

  <h3>Navigation lights</h3>
{card('electronics--lights', 'Navigation lights and LED conversions', 'sidelights, sternlight, tricolour, steaming light, anchor light', 'The international collision regulations say which lights a boat shows at night and in poor visibility; the Navigation section shows them. On a sailing yacht of this size: red and green sidelights at the bow, a white sternlight, and a steaming light on the mast when motoring; under sail alone, the three can be combined in a tricolour at the masthead; at anchor, an all-round white light.',
  ['A tricolour is allowed only for a sailing vessel under 20 m, and only under sail (Rule 25(b)); it is never shown together with the deck-level sidelights and sternlight. Once the engine is running, the boat is a power-driven vessel and shows its sidelights, sternlight and steaming light instead (a power-driven vessel under 12 m may instead show an all-round white light with its sidelights, Rule 23(d)).', 'LED lights use a fraction of the power of the old bulbs (see Boat systems). The regulations set the colour, the brightness and the arc of each light, and lights are type-approved to meet them.'],
  ['A masthead tricolour is seen from much further away than deck-level lights, and uses one bulb’s worth of power.'],
  ['An LED bulb pushed into an old fitting may not give the right colour, brightness or arc, so a proper LED conversion replaces the whole light with an approved one: approval covers a fitting and its light source together, never a bulb on its own.'],
  ['Green crust in the bulb holder; a sidelight that shines across the bow into the wrong sector; a masthead light nobody has seen working for years; a switch panel with the lights labelled wrongly.'],
  ['At dusk, walk round the boat on the pontoon with each light switch on in turn and see what shows.'], fold=True)}
{sources('lights', [
  'Tricolour and small power vessels: COLREGs Rules 23(d) and 25(b), ' + a('https://www.navcen.uscg.gov/navigation-rules-amalgamated','USCG, International and Inland rules side by side') + ', ' + a('https://seamanship.ie/col-regs-rule-25-sailing-vessel-lights/','The Seamanship Centre on Rule 25') + '.',
  'LED conversions: ' + a('https://www.marinelink.com/news/safety-transitioning-led-navigation-467745','MarineLink, transitioning to LED navigation lights') + '.',
  'Checked by web search, September 2026; the pages could not be opened directly.',
])}

  <h3 id="electronics--faults">Faults by symptom</h3>
{card('electronics--vhf-fault', 'The VHF nobody hears', 'antenna, coaxial cable, connectors', 'The commonest electronics fault on an old boat, and the most dangerous one to find out about in an emergency: the set lights up, receives, and transmits almost nothing because the signal is lost between the set and the masthead.',
  ['The antenna cable runs from the chart table, through the deck at the mast foot, up inside the mast to the antenna. Water gets into the connectors at the mast foot and the masthead, and into the cable itself, and the power goes into heating it instead of into the air.'],
  ['A new cable, connectors and antenna cost little compared with the peace of mind; a handheld is the proof and the backup.'],
  ['The fault is invisible until someone tells you that you sound weak or does not answer at all; the mast must often come down to renew the cable.'],
  ['Radio checks that come back “weak”; a green, corroded plug at the mast foot; nobody answering from a few miles off.'],
  ['Make a radio check at the start of every season and after the mast has been down; look at the mast-foot connector; carry a handheld and, offshore, an emergency antenna.'], kind='fault', fold=True)}

{card('electronics--n2k-fault', 'The dead NMEA 2000 network', 'backbone power, terminators, connectors', 'Every display blank at once, or showing dashes instead of numbers: the network, not the instruments, has failed.',
  ['An NMEA 2000 network needs power at one point (the power tee, with its fuse), a terminator at each end, and every connector dry and screwed home. Lose any of those and data stops for everyone.'],
  ['Once the fault is found it is usually a fuse, a plug or a terminator: cheap parts.'],
  ['Finding it means crawling behind panels along the whole backbone; a boat whose network was extended by several owners may have extra or missing terminators.'],
  ['All instruments blank together; data appearing and vanishing as the boat moves (a loose connector); a network that worked until a new device was added.'],
  ['Check the power-tee fuse, then count the terminators (two, one at each end), then work along the backbone connector by connector. Keep the network drawing on board.'], kind='fault', fold=True)}

{compare('Electronics faults by symptom', ['Symptom', 'Likely causes', 'What to do'], [
  ['No depth reading, or jumping numbers', 'aerated water (wake, tide race, speed); soft mud; fouled transducer face; a cable fault', 'slow down and check again; clean the transducer at the next haul-out; do not trust it near rocks'],
  ['Log reads zero or low', 'weed or barnacles on the paddle wheel', 'pull the wheel, blanking plug in at once, clean it, refit'],
  ['Wind speed zero while the cups spin', 'connector at the mast foot, or the cable in the mast', 'look at and clean the connector; the masthead unit can wait'],
  ['VHF receives but nobody hears you, or you sound weak', 'antenna connector at the masthead or mast foot, water in the coaxial cable, a failed splitter', 'try the handheld; do a radio check; check the connectors and the splitter'],
  ['Plotter says no position fix', 'GPS antenna or its cable, a failed internal antenna, a network fault', 'check the source setting and the antenna connection; use a tablet or phone meanwhile'],
  ['Autopilot wanders or steers in circles', 'fluxgate near iron or a new loudspeaker; wrong compass calibration; a worn drive', 'move the offending object; recalibrate as the manual says; steer by hand'],
  ['One display blank, others fine', 'its fuse or its drop cable', 'check the breaker and the connector'],
  ['Every NMEA 2000 display blank', 'the network power tee’s fuse; a missing terminator; water in a backbone connector', 'check the fuse and the two terminators first'],
  ['Your boat does not appear on other boats’ AIS', 'transponder in silent mode, no MMSI entered, a failed antenna or splitter', 'look for yourself on a phone app; check the settings'],
], wide=True, stack=True)}

  <h3>An old boat’s electronics: what to keep, what to replace</h3>
{compare('Upgrading the electronics on a 1980s boat', ['', 'Often found', 'What to do', 'Priority'], [
  ['Depth sounder', 'working 1980s or 1990s unit', 'keep if it reads correctly; replace the transducer if it does not', 'essential: must work'],
  ['VHF', 'an old set with no DSC, or DSC not connected to GPS', 'a DSC set connected to a GPS source, with the MMSI entered', 'essential'],
  ['Handheld VHF', 'none, or a dead battery', 'a floating DSC handheld with GPS', 'high'],
  ['AIS', 'none', 'a Class B transponder, sharing the VHF antenna through a splitter or with its own', 'high for coastal passages near shipping'],
  ['Plotter', 'none, or an old unit with out-of-date charts', 'a plotter at the helm, or a tablet in a waterproof case with current charts; keep paper as the backup', 'high'],
  ['Log and wind', 'old instruments, some working', 'keep them if they work; replace when the transducer or masthead unit fails', 'nice to have'],
  ['Autopilot', 'an old tiller or wheel pilot, or none', 'see Deck hardware and steering', 'high for short-handed sailing'],
  ['Radar', 'rare on boats of this size', 'worth it in fog-prone waters (the North Sea, the Channel, the Baltic in spring)', 'optional'],
  ['EPIRB and PLBs', 'none, or expired', 'a registered EPIRB offshore; a PLB or AIS beacon for each lifejacket', 'high offshore'],
], wide=True, stack=True)}

  <h3 id="electronics--checklist">The electronics in half an hour: a buyer’s checklist</h3>
  <ol>
    <li><strong>Depth:</strong> it reads, and you know whether below the keel or the surface.</li>
    <li><strong>VHF:</strong> a radio check with the marina; DSC, the MMSI and a GPS position on the set’s screen.</li>
    <li><strong>AIS:</strong> the boat appears on a phone app; targets appear on the plotter.</li>
    <li><strong>Plotter or tablet:</strong> a position fix, and charts no more than a year or two old.</li>
    <li><strong>Log and wind:</strong> readings change as the boat moves; the mast-foot connector is clean.</li>
    <li><strong>Compass:</strong> no bubble; the card swings freely; the light works.</li>
    <li><strong>Lights:</strong> every navigation light, one switch at a time, at dusk.</li>
    <li><strong>Beacons:</strong> EPIRB and PLB battery dates and registrations.</li>
    <li><strong>Behind the panel:</strong> a drawing of the network, or the start of one.</li>
  </ol>

  <h3>Worth watching</h3>
{videos([
 ('6ubt7BqAmdM', 'How to send a DSC distress alert', 'Leith Nautical Sailing Academy', 'A sea school’s demonstration for Day Skipper and SRC students: the red button first, then the Mayday on channel 16.'),
 ('PhosUOCSrQA', 'How to use a VHF radio to call for help: top tips from RYA trainer Lee Mosscrop', 'Sail & Motor Cruising Channel', 'An RYA trainer on calling for help by VHF, and what to say.'),
 ('UNseqNwwZ78', 'What is AIS? An introduction to using AIS on board small boats', 'Confidence Sailing', 'AIS explained for leisure boats rather than ships.'),
 ('oSuz8ooy0Nk', 'How to make a VHF DSC distress alert using manual input methods', 'Watersports Training', 'Choosing the nature of distress and typing in the position and time by hand, for a set with no GPS feed.'),
 ('IOkMc1-VGxg', 'How to send a Mayday distress call and Mayday relay', 'CompassSeaSchool', 'The words of the Mayday call, and passing on a Mayday for another boat.'),
 ('d6910bv6E_0', 'Radar vs AIS: which is better for collision avoidance?', 'followtheboat', 'A cruising sailor’s answer to the question in the AIS and radar part of this page.'),
 ('cXt1GeWXAhA', 'Effective use of Automatic Identification System (AIS)', 'The Nautical Institute', 'Made for ships’ officers: how the people on the ship you are watching use AIS.'),
])}

  <h3>Terms used in this section</h3>
  <h4 class="terms__group">On the boat</h4>
{terms([
 ("el-vhf-antenna","VHF antenna","The whip antenna at the masthead. The higher it is, the further the VHF reaches."),
 ("el-wind","Masthead wind unit","A vane (for direction) and spinning cups (for speed) on a bracket at the top of the mast."),
 ("el-tricolour","Tricolour and anchor light","A masthead light combining red, green and white sectors, for use under sail only, usually with an all-round white anchor light in the same housing."),
 ("el-radar","Radar scanner","The rotating antenna of the radar, usually inside a dome on a bracket on the mast."),
 ("el-steaming","Steaming light","A white light on the front of the mast, lit when the boat is motoring."),
 ("el-gps","GPS and AIS antennas","Small antennas, often on the pushpit, for the position receiver and, on some boats, a separate AIS antenna."),
 ("el-plotter","Chartplotter","A screen at the helm showing the chart and your position; many also show AIS, radar and instruments."),
 ("el-displays","Instrument displays","Small screens for depth, speed and wind, usually on the bulkhead by the companionway where the helm can see them."),
 ("el-navstation","Chart table electronics","The fixed VHF, the AIS unit and often the switch panel, at the chart table below."),
 ("el-fluxgate","Fluxgate compass","An electronic compass sensor that gives the heading to the autopilot and instruments. Mounted low and central, away from iron."),
 ("el-depth","Depth transducer","The sensor in the hull that sends and hears the sound pulses of the depth sounder."),
 ("el-log","Log paddle wheel","A little paddle wheel in a through-hull fitting that measures speed through the water. It fouls quickly."),
 ("el-sidelights","Sidelights","Red to port, green to starboard, on the bow pulpit, each showing from dead ahead to just behind the beam."),
 ("el-sternlight","Sternlight","A white light at the stern, showing astern and a little either side; shown with the sidelights, or replaced by the tricolour under sail."),
])}
  <h4 class="terms__group">Radio, AIS and networks</h4>
{terms([
 ("el-range-yacht","Masthead antenna height","About 15 m on a boat of this size: the main thing that sets VHF range."),
 ("el-range-coast","Coastguard aerial","Coastguard and coast-station aerials are on masts and hills, which is why they are heard much further off than other yachts."),
 ("el-horizon","Radio horizon","The distance at which an antenna’s signal meets the curve of the sea; two antennas can talk when their horizons meet."),
 ("el-own-boat","Own boat","Your position on the plotter, with a line showing your heading or course."),
 ("el-target","AIS target","A ship or boat shown by AIS, with its name, course, speed and a line showing where it will be in a few minutes."),
 ("el-cpa","CPA and TCPA","Closest point of approach, and time to it: how near an AIS target will pass, and when, if neither boat changes course or speed."),
 ("el-sleeping","Another AIS boat","Any vessel transmitting AIS, including other yachts with transponders."),
 ("el-no-ais","Not on AIS","Boats and objects that do not transmit AIS: many yachts, small fishing boats, fishing gear, buoys, swimmers."),
 ("el-shadow","Hidden target","A ship whose AIS signal is blocked by land, or is beyond VHF range, so it does not appear."),
 ("el-talker","Talker","The NMEA 0183 device that sends data, such as the GPS."),
 ("el-listeners","Listeners","NMEA 0183 devices that receive data from a talker; each input can listen to only one talker."),
 ("el-multiplexer","Multiplexer","A box that merges NMEA 0183 data from several talkers so one listener can hear them all."),
 ("el-backbone","NMEA 2000 backbone","The single shared cable of an NMEA 2000 network that every device joins."),
 ("el-terminator","Terminator","A plug that must close each end of an NMEA 2000 backbone; without both, the network misbehaves."),
 ("el-drop","T-piece and drop cable","The connector on the backbone and the short cable from it to each device."),
 ("el-power-tee","Power tee","The one point where 12 V, through a fuse, feeds an NMEA 2000 backbone."),
 ("dsc","DSC","Digital selective calling: sends a digital alert or call, with the boat’s MMSI and position, on channel 70."),
 ("mmsi","MMSI","The boat’s nine-digit radio identity, issued with the ship radio licence; entered in the DSC VHF and AIS transponder."),
 ("channel-16","Channel 16","The international VHF distress, safety and calling channel. Keep a watch on it at sea."),
 ("apparent-wind","Apparent wind","The wind felt on a moving boat: the true wind combined with the wind of the boat’s own motion."),
 ("true-wind","True wind","The wind as it would be felt by a boat drifting with the water; the instruments calculate it from the apparent wind and the speed through the water."),
 ("deviation","Deviation","The error of a compass caused by iron and electrical fields on the boat, different on each heading."),
 ("navtex","Navtex","A receiver for coast stations’ printed warnings and forecasts on 518 kHz, in English."),
 ("epirb","EPIRB","Emergency position-indicating radio beacon: the boat’s satellite distress beacon, on 406 MHz. Register it."),
 ("plb","PLB","Personal locator beacon: a small satellite distress beacon registered to a person."),
])}
  <h4 class="terms__group">Other words used here</h4>
{terms([
 ("nautical-mile","Nautical mile (NM)","1,852 m: one minute of latitude, which is why charts measure distance with the latitude scale. A knot is one nautical mile an hour."),
 ("call-sign","Call sign","The boat’s radio name in letters and numbers, issued with the ship radio licence."),
 ("coaxial","Coaxial cable","The round antenna cable with a central wire inside a braided screen. Water in it ruins VHF range."),
 ("splitter","Splitter","A box that lets the VHF and the AIS share one antenna."),
 ("grab-bag","Grab bag","A waterproof bag of essentials (handheld VHF, beacon, flares, water) ready to take into the liferaft."),
 ("mhz-khz","MHz and kHz","Megahertz and kilohertz: units of radio frequency. VHF marine radio is around 156 to 162 MHz; Navtex is 518 kHz."),
 ("channel-plan","Channel plan","The list of which VHF channel does what. Europe uses the international plan; sets bought in America may be set to theirs."),
 ("cog-sog","Course and speed over the ground","The GPS’s track and speed relative to the seabed, which include the effect of the tide or current."),
 ("gps-fix","Fix","A position: a GPS fix is the receiver’s calculated position. “No fix” means it cannot calculate one."),
 ("binnacle","Binnacle","The housing of the steering compass, usually on top of the wheel pedestal."),
 ("clutter","Clutter","False echoes on a radar screen from waves and rain, which can hide small targets."),
 ("sector","Arc (sector)","The angle through which a navigation light shows, set by the collision regulations."),
])}

  <div class="planned">
    <p>Planned for this section</p>
    <ul>
      <li>Photographs: a chartplotter at the helm, a tiller pilot, a corroded mast-foot connector</li>
    </ul>
  </div>
</section>
'''
finish(page, ROOT + 'sections/08-electronics.html', others=(ROOT + 'sections/03-hull.html', ROOT + 'sections/04-rig.html', ROOT + 'sections/05-deck.html', ROOT + 'sections/06-engine.html', ROOT + 'sections/07-systems.html', ROOT + 'sections/02-fleet.html', ROOT + 'sections/00-start.html'))
