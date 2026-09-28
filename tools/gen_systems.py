# Generates sections/07-systems.html for Sailing 101.
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_common import *
import gen_systems_diagrams as g

page = f'''<section id="systems">
  <h2>Boat systems</h2>
  <p class="lead">Electricity, fresh water, gas, heating, the toilet and the bilge pumps. None of it is complicated on a boat of this size, but all of it lives in a damp, moving, salty box, most of it has been added to by thirty years of owners, and two parts of it, the gas and the heads, can hurt you. In a hurry? Jump to the four routines: <a href="#systems--switch-routine">battery switches</a>, <a href="#systems--gas-routine">gas</a>, <a href="#systems--heads-routine">the heads</a> and <a href="#systems--bilge-routine">a rising bilge</a>; or to <a href="#systems--checklist">the buyer’s checklist</a>.</p>

  <details class="first-words" open>
    <summary>Eight words before anything else</summary>
    <dl>
      <dt>12 V</dt><dd>The boat’s electricity: direct current (DC) from batteries at about 12 volts, like a car’s. Some boats also have 230 V from a marina socket.</dd>
      <dt>House and start batteries</dt><dd>The house battery (or bank of several) runs lights, instruments and the fridge; a separate start battery is kept only for starting the engine.</dd>
      <dt>Amp-hours (Ah)</dt><dd>How much a battery holds, or how much the boat uses: a 1 amp load for 10 hours uses 10 Ah.</dd>
      <dt>Shore power</dt><dd>230 V from a socket on the pontoon (the floating jetty), through a cable to an inlet on the boat.</dd>
      <dt>Calorifier</dt><dd>The boat’s hot-water tank, heated by the engine’s coolant and, on shore power, by an electric element.</dd>
      <dt>LPG</dt><dd>Bottled gas for cooking: butane or propane. It is heavier than air, so a leak sinks into the bilge and waits.</dd>
      <dt>Heads</dt><dd>The boat’s toilet, and the compartment it is in.</dd>
      <dt>Holding tank</dt><dd>A tank the toilet empties into, instead of straight into the sea, so it can be pumped out in a marina or emptied far offshore.</dd>
    </dl>
    <p class="first-words__note">Seacocks and skin fittings (valves and fittings on holes through the hull) are explained in <a href="#hull">Hull, keel and rudder</a>; the engine’s own cooling, fuel and alternator are in <a href="#engine">Engine and drivetrain</a>.</p>
  </details>
  <p class="conf-key"><b>Marks used below:</b> {ONE} means the fact comes from a single source; {TWO} means sources disagree or the figure is anecdotal (a forum, a broker’s listing of one boat, or an owner report); {TBC} means not yet verified; {EST} marks our estimate where no source gives the figure. Figures, dates, standards and rules that are unmarked are supported by at least two sources, a maker’s data sheet or the regulator itself, listed under “Sources and confidence” at the end of each topic. How a part works is described from standard practice and is not marked.</p>

  <h3>Electrics</h3>
  <details class="first-words first-words--closed">
    <summary>Electricity in six words (open if volts and amps are new to you)</summary>
    <dl>
      <dt>Volts (V)</dt><dd>The electrical “pressure”. A boat’s DC system is nominally 12 V; a charging battery sits at about 13 to 14.5 V, a resting full lead-acid battery at about 12.7 V.</dd>
      <dt>Amps (A)</dt><dd>The flow of current. A cabin LED draws a fraction of an amp; a windlass or starter motor draws hundreds.</dd>
      <dt>Watts (W)</dt><dd>Power: volts × amps. A 24 W light on 12 V draws 2 A.</dd>
      <dt>DC and AC</dt><dd>Direct current flows one way, from batteries. Alternating current, the 230 V from a marina socket, reverses fifty times a second and is far more dangerous.</dd>
      <dt>Fuse and breaker</dt><dd>A fuse is a thin link that melts if too much current flows, before the cable overheats; a circuit breaker is a switch that trips for the same reason and can be reset.</dd>
      <dt>Live, neutral and earth</dt><dd>The three wires of a 230 V supply: live carries the current, neutral returns it, and earth is the safety wire that carries a fault away.</dd>
    </dl>
  </details>
  <p>A boat of this age left the factory with one or two lead-acid batteries, an alternator on the engine and a small switch panel. Most have since gained a shore-power charger, a fridge, an autopilot, a plotter, solar panels and several generations of wiring. The drawing shows how a sound modern 12 V system is arranged; use it to make sense of the one you find.</p>

{figure('fig-electrics', '12 V system', '0 0 900 540', 'A typical 12 V system with two battery banks, their switches and charging sources', 'A schematic. Two house batteries in parallel and a separate start battery, each with a main fuse close to it. The house bank feeds a positive bar; a house switch leads from it to a distribution panel with a breaker for each circuit and a battery monitor. A solar panel charges the bar through an MPPT controller, a shore-power charger feeds it from a 230 V inlet through an RCD and breakers with a polarity light and a galvanic isolator in the earth wire, and a DC-DC charger or VSR carries charge from the alternator and start battery. An engine switch joins the start battery to the alternator and starter. An emergency link switch can join the two banks. A bilge pump is wired, with its own fuse, straight from the battery. The house negatives pass through a shunt to a negative busbar that the start battery also joins.', g.electrics(), 'The two principles: the engine can always be started from its own battery, whatever the house bank has been through; and the main fuses and the automatic bilge pump are on the battery side of the switches, so they work whatever the switches are set to. The heavy cable from the start battery to the starter motor is usually left unfused, as the American ABYC standard allows.', note=HINT, start=0.3)}

{card('systems--batteries', 'Batteries and battery switches', 'house bank, start battery, 1-2-both switch, isolators, emergency parallel', 'Most boats of this age have lead-acid batteries, flooded (with caps to top up) or sealed AGM, in a box low in the boat. Listings for the reference boats show two or three batteries on most, all fitted by later owners; how they were built is not recorded {TBC}.',
  ['Lead-acid batteries last longest if they are never taken below about half charge and are fully recharged often. A “100 Ah” battery therefore gives about 50 Ah of use.', 'Many boats of this age have a single rotary <strong>1-2-both-off</strong> switch. It works, but “both” left on flattens the start battery with the house loads, and “off” with the engine running can damage the alternator. The better arrangement, drawn above, is a separate switch for each bank, an emergency link switch to join them if the start battery is flat, and a device that shares the charge automatically (see Charging).'],
  ['Simple, cheap and forgiving; a flooded battery can be checked cell by cell with a hydrometer (a float that reads the acid’s strength).'],
  ['Heavy; they lose charge on their own over the winter (up to about 10 % a month for flooded batteries, less for AGM, and less in the cold), and a flat lead-acid battery freezes and sulphates (hardens inside) and does not recover.'],
  ['Corroded terminals with white or green crust; a battery box with no lid or strap, which lets a battery move in a seaway; cells that need a lot of topping up (overcharging); batteries of different ages and types in one bank, which drags the good ones down.'],
  ['Look at the terminals, the straps and the cables; read the date on each battery. With a multimeter, after the batteries have rested for a few hours with nothing charging or drawing: about 12.7 V is full and about 12.1 V is half charged for a flooded lead-acid battery (Trojan’s figures, after six hours’ rest); check your battery maker’s table.'], fold=True)}

  <h4 id="systems--switch-routine">Battery switches: which position when</h4>
  <ol>
    <li><strong>Two separate switches</strong> (the layout drawn above): both on while you are aboard; engine switch on to start; house switch off, and engine switch off, when you leave the boat. The emergency link switch stays off unless the start battery is flat, and goes off again once the engine runs.</li>
    <li><strong>A 1-2-both-off switch:</strong> start the engine on the start battery (often “1”). With no relay or splitter fitted, the alternator charges only the battery selected, so turn to “both” while the engine runs to charge both; if a VSR or splitter is fitted it does that for you. Once the engine is off, select the house battery (“2”). Never leave it on “both” at anchor, or the house loads will flatten the start battery too.</li>
    <li><strong>Never</strong> turn a switch to “off”, or through “off”, with the engine running: the alternator can be damaged. Many rotary switches pass through “both” on the way between 1 and 2 for exactly this reason.</li>
    <li><strong>Leaving the boat:</strong> switches off, except any circuit wired direct for the bilge pump or a solar controller.</li>
  </ol>

  <p>The four battery types found on boats: <strong>flooded</strong> lead-acid, with liquid acid and caps to top up; <strong>AGM</strong>, sealed, with the acid soaked into glass-fibre mats; <strong>gel</strong>, sealed, with the acid set as a gel; and <strong>lithium iron phosphate</strong> (LiFePO4), a different chemistry altogether (see the lithium card). A charger works in stages: a bulk charge, then an absorption stage at a set voltage, then a lower float voltage that holds the battery full.</p>
{compare('Battery types at a glance', ['', 'Flooded lead-acid', 'AGM (absorbed glass mat)', 'Gel', 'Lithium (LiFePO4)'], [
  ['Charging voltage: absorption (the main charge) / float (holding it full)', '14.1–14.7 / 13.2 V (Trojan)', '14.3 / 13.3 V at 25 °C (Lifeline)', '14.1–14.4 / 13.5–13.8 V (Victron)', '14.2 / 13.5 V (Victron)'],
  ['Usable capacity', 'about half: stay above 50 % charge', 'about half', 'about half', 'most of it: 80 % or more'],
  ['Life, in charge-and-discharge cycles', 'a few hundred to 50 % {TWO}', '400 to 80 % discharge, 600 to 50 % (Victron)', '500 to 80 %, 750 to 50 % (Victron)', '2,500 at 80 %, 5,000 at 50 % (Victron)'],
  ['Weight of 100 Ah', 'about 25–30 kg {TBC}', 'about 26 kg (Victron Super Cycle)', 'about 29 kg (Victron)', 'about 14 kg (Victron)'],
  ['Needs', 'topping up with distilled water; ventilation', 'correct charge voltages', 'gentle charging: no more than about 20 A for a 100 Ah battery', 'a battery management system, charging stopped below 0 °C, alternator protection'],
  ['Fits an old boat as it is', 'yes', 'yes, with the charger set for AGM', 'yes, with the charger set for gel', 'no: the charging system must be redesigned'],
], wide=True, stack=True)}

{card('systems--charging', 'Charging: alternator, split charging, shore charger and solar', 'VSR, diode splitter, DC-DC charger, smart regulator, MPPT, PWM', 'Four sources charge a boat’s batteries: the engine’s alternator, a mains charger on shore power, solar panels and, on some boats, a wind generator. The trick is to share the alternator’s charge between the start and house banks without joining them all the time.',
  ['A <strong>diode splitter</strong> feeds both banks through one-way electrical valves, but loses about 0.7 V on the way, so the house bank may never get past about 80 % unless the alternator senses the battery voltage {TWO}. A <strong>voltage-sensing relay (VSR)</strong>, an automatic switch, joins the banks when it sees charging voltage and separates them when charging stops, with almost no loss. A <strong>DC-DC charger</strong> takes current from the start side and charges the house bank at the right voltage for its type, limiting the load on the alternator.', 'The alternator’s voltage regulator (nothing to do with the gas regulator) holds about 14 V on a standard alternator, so charging slows down as the batteries approach about 80 %: an hour of motoring takes a half-flat bank to roughly 70–80 % {TWO}. Solar controllers are PWM (which pulls the panel down to battery voltage) or MPPT (which converts the panel’s best voltage down, and gains typically 20 to 30 % in real conditions).'],
  ['A few square metres of solar and an MPPT controller cover the daily use of a modest boat on a sunny coast, which is why they are the most popular upgrade.'],
  ['Every added source needs its own fuse and a charger matched to the battery type; a charger set for flooded batteries slowly cooks an AGM.'],
  ['An alternator that charges the start battery but not the house bank (a failed relay or splitter); a charge light that glows dimly; a charger that hums and gets hot; solar panels shaded by the boom, which lose most of their output.'],
  ['With the engine running, measure the voltage at each bank: about 14 V or more means both are charging. Read the settings on the charger and solar controller and check they match the battery type.'], fold=True)}

{card('systems--monitor', 'Battery monitor and a power budget', 'shunt, amp-hour counter, state of charge', 'A battery monitor counts every amp that goes into and out of the house bank through a shunt (a precise resistor in the negative cable), and shows the state of charge in percent. Voltage alone is a rough guide for lead-acid and useless for lithium, whose voltage hardly changes until it is almost empty.',
  ['Work out a daily budget: for each load, amps × hours used per day = amp-hours, then add about 20 %. Figures found for the main loads: a compressor fridge 30 to 60 Ah a day in summer; a below-deck autopilot from about 0.5 A in calm water to 4 or 5 A in a seaway, a Raymarine ST2000 tiller pilot 0.5 to 1.5 A in use; an LED tricolour masthead light about 0.3 A, against about 2 A for the old 25 W bulb.'],
  ['The one instrument that stops arguments about whether the batteries are “fine”.'],
  ['A monitor must be set up for the battery type and capacity, and synchronised (told “this is full” after a full charge; most do it by themselves) or its percentage drifts.'],
  ['A monitor that reads 100 % every morning whatever happened (not synchronised); a bank that falls below half charge every night (the loads outgrow the batteries).'],
  ['Count the loads you will really use; compare with half the house bank’s amp-hours for lead-acid; if the budget does not fit, fit less or charge more.'], fold=True)}

{compare('A worked power budget for a day at sea and a night at anchor, from makers’ figures for typical kit: an illustration, not a measurement', ['Load', 'Typical kit and its maker’s figure', 'Amps', 'Hours a day', 'Amp-hours'], [
  ['Fridge, in summer', 'Isotherm gives 23 Ah a day for its 49-litre Cruise at 25&nbsp;°C outside; more in a hot boat', '–', '–', '40'],
  ['Instruments and plotter', 'two Raymarine i70s displays, 0.14 A each; a 7-inch Garmin plotter, 1.5 A', '1.8', '8', '14'],
  ['Tiller pilot, under way', 'Raymarine ST2000+, 0.5 to 1.5 A', '1', '4', '4'],
  ['VHF, listening', 'Standard Horizon GX2400E on standby', '0.55', '10', '5.5'],
  ['AIS transponder', 'Vesper XB-8000, 4 W', '0.33', '24', '8'],
  ['Cabin lights', 'three Hella EuroLED, 0.33 A each', '1', '3', '3'],
  ['Anchor light', 'Hella NaviLED, 1 W or less', '0.08', '10', '1'],
  ['Phones and a tablet', '', '–', '–', '3 {TBC}'],
  ['Total, plus 20 %', '', '', '', 'about 95'],
], stack=True)}
  <p class="table-note">About 95 Ah a day needs a lead-acid house bank of at least 190 Ah, used down to half, or more charging (see <a href="#systems--charging">charging and solar</a>).</p>
{photo('systems-battery-corrosion.jpg', 'An old blue marine battery whose top and terminals are crusted with green and white corrosion', 'What neglect looks like: a marine battery with its terminals and top thick with corrosion. Clean terminals, tight connections and a dry, strapped-down box prevent it.', 'joannapoe', 'CC BY-SA 2.0', 'https://creativecommons.org/licenses/by-sa/2.0/', 'https://www.flickr.com/photos/94661162@N00/6008980014/', 765, 1024, 'https://www.flickr.com/photos/jopoe/')}

{card('systems--wiring', 'Fuses, cables and the panel', 'main fuse, breakers, voltage drop, tinned cable, busbars', 'Every positive cable needs protection close to where the power comes from, sized to protect the cable, not the device on the end. The American ABYC standard, which most marine electricians work to, puts the fuse within 178 mm of the battery, or within 1.8 m if the cable is sheathed (enclosed in a protective sleeve or conduit) along its whole length. The European standard (ISO 13297, which replaced ISO 10133) says as close as possible and gives no figure.',
  ['Cable is sized by the voltage it loses along its length (the voltage drop): ABYC allows 3 % (0.36 V at 12 V) for navigation lights, bilge pumps and electronics, and 10 % for lighting and other non-critical loads. Long runs to the masthead or the bow need much thicker cable than their current suggests.', 'Marine cable is tinned (each copper strand coated with tin) and finely stranded; plain copper blackens and corrodes in salt air, and the corrosion creeps up under the insulation.'],
  ['A tidy panel with labelled breakers, busbars (metal bars that many cables bolt to) and crimped terminals (squeezed on with a tool, not soldered or twisted) sealed with heat-shrink sleeve is easy to fault-find and lasts decades.'],
  ['Every previous owner has added something; household cable, twisted joints and taped connections are common, and they fail under vibration and damp.'],
  ['Green or black cable ends under the insulation; hot or discoloured terminals; fuses wrapped in foil; wires with no fuse at all; a “spaghetti” of cables behind the panel with no labels.'],
  ['Open the panel and look behind it; follow the main cables from the batteries to the switches and fuses; feel the terminals after the fridge and autopilot have run for an hour.'], fold=True)}

{card('systems--shore', 'Shore power: RCD, polarity and galvanic isolator', '230 V, inlet, residual current device, polarity reversal, isolation transformer', 'A 230 V system on a boat starts at an inlet, goes through a residual current device (RCD) and breakers, and feeds the battery charger, sockets and perhaps a water-heater element. Yachting Monthly says every AC installation must have an RCD, of the A type suitable for mobile installations; for protecting people it trips at no more than 30 mA, and the small-craft standard ISO 13297 (2000 edition) asked for a double-pole 30 mA device tripping within 100 milliseconds. The main breaker should be double-pole, switching both live and neutral, so the boat is fully disconnected even when the polarity is reversed.',
  ['Live and neutral can arrive swapped: Continental domestic plugs go in either way round, and marina pedestals and adaptors abroad are sometimes wired wrongly, even though the round blue marina plug itself fits only one way. ISO 13297 requires a polarity indicator; if it lights, a changeover switch or a reversing lead puts it right.', 'The shore earth wire connects the boat’s underwater metals to every other boat on the pontoon, and small currents flow between them, eating anodes. A <strong>galvanic isolator</strong> in the earth wire blocks these small currents (up to about 1.4 V) while still passing a fault current (the large current of a short to earth, which must reach the shore to trip the breaker); an <strong>isolation transformer</strong>, which passes the power across magnetically, removes the connection altogether and is the safest, heaviest and most expensive answer.'],
  ['Shore power runs the charger, the heater and the kettle in a marina and keeps the batteries full over a winter afloat.'],
  ['Mains electricity and sea water are a dangerous mix; home-made installations and domestic extension leads kill.'],
  ['No RCD, or one that has never been tested; a shore lead that is cracked or has been joined; anodes that vanish in a season in a marina (stray current, and no galvanic isolator); a polarity light that is always on.'],
  ['Press the RCD’s test button; look at the shore lead and the inlet; ask whether a galvanic isolator is fitted, and how fast the anodes go.'], fold=True)}

{card('systems--lithium', 'Lithium batteries on an old boat', 'LiFePO4, BMS, load dump', 'Lithium iron phosphate (LiFePO4) batteries are about 60 % lighter than lead-acid for the same capacity, can use most of their capacity, and last thousands of cycles. They are also “not a straightforward drop-in replacement” (Yachting World): the charging system around them has to change.',
  ['Every lithium battery has a battery management system (BMS) that disconnects it to protect the cells: when a cell goes above about 3.65 V, when it is too cold to charge (below 0 °C, which damages the cells for good), and when discharged too far.', 'Two problems follow for the alternator. If the BMS disconnects while the alternator is charging hard, the voltage spikes (a “load dump”, over 100 V for a fraction of a second) and can destroy the alternator’s diodes. And lithium accepts so much current that an ordinary alternator can overheat. Victron’s answer, and the usual one, is a DC-DC charger between the alternator side and the lithium bank.'],
  ['Done properly, the best house bank there is: light, deep and long-lived.'],
  ['Done badly, a risk to the alternator, the electronics and, in the worst cases, the boat; insurers increasingly ask who installed it.'],
  ['Lithium batteries charged straight from an unmodified alternator; no protection against charging in frost; a BMS that cuts out with no warning and takes the instruments with it.'],
  ['Ask who designed the installation and to what standard; see the DC-DC charger or the alternator protection; check the chargers are set for lithium.'], kind='fault', fold=True)}
{sources('electrics', [
  'Batteries: ' + a('https://www.trojanbattery.com/resources/battery-maintenance','Trojan battery maintenance') + ', ' + a('https://lifelinebatteries.com/wp-content/uploads/2015/12/6-0101F-Lifeline-Technical-Manual-Final-5-06-19.pdf','Lifeline technical manual') + ', ' + a('https://www.victronenergy.com/upload/documents/Datasheet-GEL-and-AGM-Batteries-EN.pdf','Victron gel and AGM data sheet') + ', ' + a('https://www.victronenergy.com/upload/documents/Datasheet-12,8-&-25,6-Volt-lithium-iron-phosphate-batteries-Smart-EN.pdf','Victron LiFePO4 data sheet') + '; depth of discharge and AGM cycles from ' + a('https://www.renogy.com/blogs/general-solar/what-is-depth-of-discharge-for-battery','Renogy') + ' and ' + a('https://diysolarforum.com/threads/agm-question-dod-vs-life-expectancy.8297/','a forum') + ' (anecdotal); weights from retailer comparisons (' + a('https://outbax.com.au/blogs/post/12v-100ah-lithium-lifepo4-vs-agm-battery-camping-rv-comparison','Outbax') + ', ' + a('https://www.anernstore.com/blogs/diy-solar-guides/lifepo4-vs-agm-12v-100ah-battery','Anern') + '). Switches: ' + a('https://marinehowto.com/1-2-both-battery-switch-considerations/','Marine How To on 1-2-both switches') + ', ' + a('https://forums.ybw.com/threads/1-2-both-battery-switch-query.401492/','YBW') + ' (anecdotal). Self-discharge: ' + a('https://marinehowto.com/winter-battery-storage-self-discharge-characteristics/','Marine How To') + '.',
  'Charging: ' + a('https://48north.com/boats-and-gear/necessary-or-nice-voltage-sensing-relays/','48° North on VSRs') + ', ' + a('https://forums.ybw.com/threads/diode-v-vsr.124302/','YBW on diodes') + ' and ' + a('https://forums.ybw.com/threads/alternator-regulator-voltage.186562/','on regulator voltage') + ' (anecdotal), ' + a('https://www.victronenergy.com/blog/2019/10/10/new-product-orion-tr-smart-dc-dc-charger/','Victron on DC-DC chargers') + ', ' + a('https://www.victronenergy.com/upload/documents/Technical-Information-Which-solar-charge-controller-PWM-or-MPPT.pdf','Victron, PWM or MPPT') + ', ' + a('https://xantrex.com/about-xantrex/blog/marine/mppt-vs-pwm-solar-charge-controllers-which-one-should-you-choose-for-your-boat/','Xantrex on MPPT gains') + '.',
  'Monitoring and loads: ' + a('https://www.victronenergy.com/battery-monitors/smart-battery-shunt','Victron SmartShunt') + ', ' + a('https://www.whensailing.com/blog/electrical-needs-cruising-sailboat-power-consumption','When Sailing on consumption') + ', ' + a('https://privilege-marine.com/how-to-calculate-power-consumption-on-a-sailing-boat/','Privilege Marine on the budget method') + ', ' + a('https://www.sea-help.eu/en/guide/electricity-current-consumption-yacht-boat/','SEA-HELP on autopilots') + ', ' + a('https://defender.com/en_us/raymarine-st2000-tiller-pilot-a12005','Raymarine ST2000 specification') + ', ' + a('https://www.practical-sailor.com/sails-rigging-deckgear/practical-sailor-tracks-down-the-best-led-tri-color-light/','Practical Sailor on LED tricolours') + '.',
  'Wiring: ' + a('https://www.bluesea.com/support/articles/Circuit_Protection/99/DC_Main_Overcurrent_Protection_Requirements','Blue Sea Systems on ABYC fuse location') + ', ' + a('https://marinehowto.com/battery-banks-over-current-protection/','Marine How To') + ', ' + a('https://www.iso.org/standard/45867.html','ISO 10133 (withdrawn)') + ', ' + a('https://cdn.standards.iteh.ai/samples/69551/4f5da7667b4642e2880fe10a27cd4c70/ISO-13297-2020.pdf','ISO 13297 sample') + ', ' + a('https://www.westmarine.com/west-advisor/Marine-Wire-Terminal-Tech-Specs.html','West Marine on voltage drop') + ', ' + a('https://www.12voltplanet.co.uk/news/now-stocking-corrosion-resistant-tinned-copper-cable-for-marine-environments.html','12 Volt Planet on tinned cable') + '.',
  'Shore power and lithium: ' + a('https://www.yachtingmonthly.com/gear/how-to-install-shore-power-on-a-yacht-96465','Yachting Monthly on shore power') + ', ' + a('https://electrical.theiet.org/wiring-matters/years/2023/97-september-2023/polarity-indication-on-boats-why-it-s-important-to-get-it-right/','IET Wiring Matters on polarity') + ', ' + a('https://passagemaker.com/technical/galvanic-isolators-and-isolation-transformers/','PassageMaker on isolators and transformers') + ', ' + a('https://goodoldboat.com/galvanic-isolator/','Good Old Boat') + '; ' + a('https://www.yachtingworld.com/gear-reviews/lithium-boat-batteries-upgrade-electrics-128151','Yachting World on lithium') + ', ' + a('https://www.morganscloud.com/2022/04/25/why-lithium-battery-load-dumps-matter/','Attainable Adventure Cruising on load dumps') + ', ' + a('https://www.victronenergy.com/blog/2019/10/07/careful-alternator-charging-lithium/','Victron, careful: alternator charging lithium') + ', ' + a('https://lithiumbattery.online/low-temperature-charging-and-bms/','on charging below 0 °C') + '.'
])}

  <h3>Fresh water</h3>
{figure('fig-water', 'fresh water', '0 0 900 490', 'The fresh-water system: tank, pressure pump, accumulator, calorifier and taps', 'A schematic. A deck filler and a vent lead to the water tank. From the tank the water runs through a strainer to a pressure pump, past an accumulator, and along the cold line to the galley tap and the basin and shower. A branch feeds the calorifier, an insulated tank with a coil through which engine coolant flows and an immersion heater worked by shore power; its hot outlet runs to the same taps.', g.water(), 'Cold water in blue, hot in red. The engine coolant runs through the calorifier’s coil in its own sealed circuit and never touches the water you drink.')}

{card('systems--water-tanks', 'Water tanks and filling', 'fresh-water tank, bladder, deck filler, Milton', 'The reference boats carry 100 to 570 litres of water, in one or two tanks under berths or the saloon floor. Tanks are stainless steel, polyethylene or flexible bladders; on boats this old they are often replacements.',
  ['A stainless tank does not corrode if it is of the marine grade (316L) and well welded, but it is heavy, dear and can crack at the welds; polyethylene is light, cheap and inert (it does not react with the water); a flexible bladder fits odd spaces at about half the cost of a custom tank, but can taint the water and chafe {TWO}.'],
  ['Clean water from a clean tank keeps for weeks; two tanks with a valve between them mean a leak or contamination costs half your water, not all of it.'],
  ['Diesel pumped into the water filler happens far more often than anyone admits, and the smell may never leave the tank.'],
  ['Stale or musty water (a tank that has not been cleaned); a split bladder; a filler cap with no seal or no label; a vent full of spiders.'],
  ['Read the label on every deck filler before the nozzle goes in. Sterilise tanks at the start of each season with a sodium hypochlorite product (the chemical in household bleach) at the maker’s dose (Puriclean, for example: a teaspoon to 4.5 litres, left for one to twelve hours), then flush two or three times.'], fold=True)}

{card('systems--water-pump', 'Pressure pump, accumulator and foot pumps', 'Jabsco, Shurflo, Whale, Gusher Galley', 'An electric pump that switches itself on when the pressure drops, when a tap opens, and off when it closes. An accumulator, a small tank with a rubber diaphragm and a cushion of air, stores some pressure so the pump does not start and stop with every splash.',
  ['A strainer before the pump catches debris from the tank. The accumulator smooths the flow, stops the knocking of pipes (water hammer) and saves wear on the pump.', 'A foot pump at the galley sink, such as the Whale Gusher Galley (up to about 15 L/min, and happy to run dry), uses far less water than a tap and keeps working when the batteries or the pressure pump do not; it can be plumbed to the fresh tank or to a seacock for washing up in sea water.'],
  ['Hot and cold running water on a small boat; a foot pump as a backup costs little.'],
  ['A pressure system empties a tank quickly without anyone noticing, and a leak anywhere keeps the pump running until the tank is dry.'],
  ['A pump that runs on and off by itself with all taps shut (a leak, or a failed non-return valve, a one-way valve that should hold the pressure); a pump that runs but gives no water (an empty tank, or an air lock: a bubble of air trapped in the pipe); a blocked strainer.'],
  ['Turn the pump on and listen with everything shut: silence means no leaks. Switch it off when leaving the boat.'], fold=True)}

{card('systems--calorifier', 'Calorifier and hot water', 'water heater, twin-coil, immersion element', 'An insulated tank of 20 to 40 litres with a coil inside through which hot coolant from the engine flows. Twenty or thirty minutes of motoring gives hot water for several hours. Most have a 230 V immersion element for shore power, and a twin-coil unit can take a second heat source such as a diesel water heater.',
  ['The coolant and the water never mix: heat passes through the wall of the coil. Water heated by the engine can be hot enough to scald (the makers give no maximum), so a thermostatic mixing valve on the hot outlet adds cold water before it reaches the taps. A non-return valve on the cold feed stops hot water pushing back, and a pressure-relief valve lets water out as it expands when heated.'],
  ['Free hot water after any passage under engine.'],
  ['The coolant hoses to the calorifier are long and have to be bled of air, and a leaking coil lets coolant into the drinking water or water into the engine.'],
  ['A relief valve dripping all the time; scalding water at the taps (no mixing valve); a calorifier that never gets hot (air in the coolant loop); green or sweet-tasting water (a leaking coil).'],
  ['Ask for hot water after the engine has run; look at the hoses and clips; drain it for the winter (see Laying up).'], fold=True)}
{sources('fresh water', [
  'Tanks: ' + a('https://forums.ybw.com/threads/water-tank-stainless-or-plastic.427082/','YBW, stainless or plastic') + ', ' + a('https://www.cruisersforum.com/forums/f115/water-bladder-vs-tank-167022.html','Cruisers Forum on bladders') + ' (anecdotal); diesel in the water tank: ' + a('https://www.pointseast.com/boatloads-of-shame/','Points East') + ', ' + a('https://www.practical-sailor.com/blog/decontaminating-a-tainted-water-tank','Practical Sailor') + '; sterilising doses only from ' + a('https://forums.ybw.com/threads/water-tanks-cleaning-and-milton-tabs.203781/','YBW') + ' (anecdotal, so not given here).',
  'Pumps and hot water: ' + a('https://www.fisheriessupply.com/plumbing/water-tanks-and-accessories/jabsco','Jabsco accumulators') + ', ' + a('https://www.xylem.com/en-us/resources/videos/accumulator-tanks-explained/','Xylem, accumulators explained') + ', ' + a('https://defender.com/en_us/whale-gusher-mk3-manual-galley-foot-pump','Whale Gusher Galley') + ', ' + a('https://www.practical-sailor.com/boat-maintenance/install-a-water-saver-a-galley-foot-pump/','Practical Sailor on foot pumps') + ', ' + a('https://newarkcylinders.co.uk/the-ins-and-outs-of-marine-calorifiers/','Newark Cylinders on calorifiers') + ', ' + a('https://www.yachtingmonthly.com/gear/how-to-install-hot-water-onboard-a-yacht-93988','Yachting Monthly on hot water') + '. Calorifier sizes and heating times are typical figures, not sourced.'
])}

  <h3 id="systems--gas-rules">Gas</h3>
  <p>Bottled gas is the one system on the boat that can blow it apart. LPG is heavier than air: a leak flows downhill into the bilge and collects there, invisible, until a spark finds it. Every rule below exists because of that.</p>

{figure('fig-gas', 'gas system', '0 0 900 470', 'The gas system from a sealed locker to the cooker', 'A schematic side view, stern on the left. A sealed gas locker in the cockpit holds an upright, strapped cylinder with its regulator, a bubble tester and a solenoid valve; a drain from the bottom of the locker falls to an outlet in the transom above the waterline. The pipe leaves the top of the locker, runs through a bulkhead to an isolating valve by the cooker, then by a flexible hose to a gimballed cooker. A gas alarm sensor low in the bilge is wired to the solenoid valve, and a carbon monoxide alarm is mounted high on a bulkhead.', g.gas(), 'In order along the pipe: cylinder, regulator, bubble tester and solenoid valve (all inside the locker), isolating valve, cooker. The locker drain and the sensor both work on the same fact: gas sinks.')}

{card('systems--gas-locker', 'Gas locker, cylinder and pipework', 'LPG locker, ISO 10239, regulator, solenoid valve', 'The international standard for gas on small craft, ISO 10239, requires the cylinder to be in a locker that is sealed from the inside of the boat up to at least the height of the cylinder valve, opens only from the top, and drains from its bottom through a pipe that falls all the way to an outlet at least 75 mm above the loaded waterline, with a bore (inside diameter) of at least 19 mm.',
  ['The cylinder stands upright and strapped, so that liquid gas cannot reach the regulator. The regulator reduces the cylinder’s pressure to the cooker’s working pressure (in millibars, mbar: thousandths of the air’s own pressure). Inside the locker come the bubble tester and a solenoid valve (an electric valve), worked by a switch in the galley, so the gas can be turned off at the cylinder from below; then a solid copper pipe (or approved hose) runs in one piece to the galley.', 'Fit a regulator with over-pressure protection: in Europe since 2001, one meeting EN 12864 Annex M {TWO}.'],
  ['A correctly built locker makes a leak at the cylinder or regulator harmless: the gas pours overboard.'],
  ['Many boats of this age have lockers that do not drain, drain into the cockpit, or have a hole for the pipe low in the side. Cockpit lockers used for gas and for everything else at once are common, and dangerous.'],
  ['A locker drain that is blocked, kinked or ends below the waterline; the pipe leaving through the side of the locker below the valve; a perished hose from regulator to pipe (hoses carry a date); a cylinder lying on its side.'],
  ['The bucket test: pour water into the locker and watch it all go overboard. Read the date on the hose. Have an annual check by a registered gas engineer (Gas Safe in the UK).'], fold=True)}

{card('systems--gas-safety', 'Leak testing, alarms and the cooker', 'bubble tester, gas alarm, flame-failure device, gimballed cooker, carbon monoxide alarm', 'Three defences stop a leak becoming an explosion: a bubble tester to find leaks, a gas alarm to warn of gas in the bilge, and flame-failure devices on the cooker that shut the gas off when a flame blows out.',
  ['LPG has a strong smell added so that leaks can be noticed. A <strong>bubble tester</strong> sits in the locker just after the regulator; with the solenoid on, the cooker’s isolating valve open and every burner tap shut, press its button and watch: bubbles in the little window mean gas is flowing somewhere, which means a leak. A <strong>gas alarm</strong> has its sensor at the lowest point near the galley, and closes the solenoid valve when it detects gas; the valve stays shut until it is reset by hand. A <strong>flame-failure device</strong> on each burner shuts that burner’s gas if the flame goes out; older, cheaper cookers had one only on the oven.', 'The cooker hangs on gimbals so it stays level as the boat heels and rolls, typically through 20° to 30°, but not when the boat pitches or slams: pans need clamps and fiddles (rails) as well. Lock the gimbals in harbour.'],
  ['A thirty-second bubble test each time the gas is turned on is the best habit on the boat.'],
  ['Sensors age and are poisoned by cleaning products; flame-failure devices stick; old cookers have none.'],
  ['A bubble tester that bubbles; a gas alarm with no power or no date; burners that go out in a draught and keep hissing; the smell of gas in a locker or the bilge.'],
  ['If the tester bubbles: gas off at the cylinder; find the leak with leak-detector spray or soapy water brushed on each joint, never a flame; do not use the gas until it is fixed, by a gas engineer if you are not sure.'], kind='fault', fold=True)}

  <h4 id="systems--gas-routine">Gas: on, test, light, off</h4>
  <ol>
    <li><strong>On:</strong> open the valve on the cylinder in the locker; switch the solenoid on at the galley panel.</li>
    <li><strong>Test:</strong> cooker isolating valve open, every burner tap shut; press the bubble tester and watch for ten seconds. Bubbles: stop, and see the leak card above.</li>
    <li><strong>Light:</strong> match or lighter ready first, then open the burner tap, push it in to hold the flame-failure valve open, light it, and keep it pushed in for a few seconds until the flame holds.</li>
    <li><strong>Off:</strong> burners off; switch the solenoid off; at the end of the day, and always when leaving the boat, close the cylinder valve too.</li>
  </ol>
  <div class="callout warn">
    <p><strong>If you smell gas, or the gas alarm sounds:</strong> put out any flame. Turn the gas off by hand at the cylinder, not with the solenoid switch. Do not work any electrical switch, on or off, do not start the engine, and do not run the electric bilge pump; if its float switch starts it by itself, there is nothing you can do about that, which is why you get off the boat if the smell is strong. Open every hatch. Pump or bail by hand to get the gas out of the bilge. Nothing electrical goes back on until the smell has gone, and the gas alarm is not reset until the cause has been found.</p>
  </div>

{card('systems--gas-europe', 'Butane, propane and cylinders across Europe', 'Calor, Campingaz, Gasol, AGA, Primagaz, adaptors', 'Two gases are sold as LPG. Butane boils at about −0.5 to −1 °C, so it stops vaporising (turning from liquid to gas) and coming out of the cylinder when it is cold; a Calor dealer calls it sluggish below about 5 °C. Propane boils at −42 °C and works in any weather. In the Baltic and North Sea in spring and autumn, propane is the one to have.',
  ['UK boats traditionally use 28 mbar regulators for butane and 37 mbar for propane; “Euro” regulators at 30 mbar take either {TWO}. Cylinders and their valves differ from country to country, and a Calor cylinder cannot be exchanged abroad.', 'The usual answer is to keep your own regulator and carry adaptors, or to use Campingaz, which is sold widely around Europe but costs more per kilogram. In Scandinavia the composite cylinders sold in Sweden and Norway need their own hose or adaptor, and many yachts only have room for a small round cylinder there.'],
  ['With the right adaptor, most European gas can be used on most boats.'],
  ['Further south and east: in Greece, Petrogaz sells steel cylinders of 3 to 25 kg and composite ones of 7.5 and 10 kg, and Campingaz is sold in the islands; in Croatia, Petrol sells 7.5 and 10 kg cylinders, exchanged empty for full with the same supplier after a first deposit of €30 to €50; in Turkey, Aygaz’s household cylinder is 12 kg with a 29 mbar kitchen regulator. In Bulgaria the gas is a propane-butane mix in 10 kg cylinders about 59 cm tall: measure your gas locker first. They are lent against a deposit and exchanged full for empty by distributors such as Toplivo Gas, which has offices in Varna and Burgas {ONE}. Valves vary and a UK regulator may not fit, so buy the matching regulator with the cylinder. Never fill a cylinder at a car LPG pump: it is forbidden {ONE}. Nowhere will exchange a Calor cylinder. Plan to buy a local cylinder and the regulator that fits it, and ask a Campingaz stockist or the first marina which one you need before you run out.'],
  ['A regulator for the wrong gas or pressure; a pile of home-made adaptors; a cylinder bought abroad that does not fit the locker.'],
  ['Before cruising abroad, find out what the next country sells and buy the adaptor at home.'], fold=True)}
{sources('gas', [
  'Standard and locker: ' + a('https://montymariner.co.uk/wp-content/uploads/2017/03/ISO-10239-Small-Craft-LPG-Systems.pdf','ISO 10239 summary') + ', ' + a('https://cdn.standards.iteh.ai/samples/81921/3ba9afd247ed4c448416f7d638627d20/ISO-10239-2025.pdf','ISO 10239:2025 sample') + ', ' + a('https://marineheating.co.uk/lpg-gas-safety-certificate/','Marine Heating') + ', ' + a('https://www.yachtingmonthly.com/gear/marine-gas-safety-checks-for-peace-of-mind-on-board-83661','Yachting Monthly gas safety checks') + '. Regulators: ' + a('https://www.yachtingmonthly.com/gear/everything-you-need-to-know-about-a-yachts-gas-system-95109','Yachting Monthly on gas systems') + ', ' + a('http://www.marinecooker.co.uk/gas-regulators.htm','Marine Cooker') + ', ' + a('https://forums.ybw.com/threads/gas-regulators-changes-in-mbar.264747/','YBW') + ' (anecdotal).',
  'Safety devices: ' + a('https://www.gasproducts.co.uk/8mm-alde-marine-boat-gas-leak-detector-bubble-tester.html','Alde bubble tester') + ', ' + a('https://www.yachtingmonthly.com/sailing-skills/crash-test-boat-gas-explosion-29779','Yachting Monthly crash-test boat, gas explosion') + ', ' + a('https://www.boatsafetyscheme.org/requirements-examinations-and-certification/non-private-boat-standards/part-8-appliances-flueing-ventilation/flame-supervision-device-fsd/','Boat Safety Scheme on flame supervision') + ', ' + a('https://marineheating.co.uk/lpg-gas-cooker/','Marine Heating on cookers') + ', ' + a('https://theboatgalley.com/stove-gimbals/','The Boat Galley on gimbals') + '.',
  'Gases and cylinders: ' + a('https://en.wikipedia.org/wiki/Butane','butane') + ' and ' + a('https://en.wikipedia.org/wiki/Propane','propane') + ' (Wikipedia), ' + a('https://www.harringtonsreading.co.uk/propane-or-butane-whats-the-difference-a-practical-guide-to-choosing-calor-gas/','a Calor dealer') + ', ' + a('https://forums.ybw.com/threads/gas-cylinders-for-cruising.445180/','YBW on cruising abroad') + ' (anecdotal), ' + a('https://www.gok-blog.de/en/2025/12/12/gas-supply-in-scandinavia-what-do-i-need-to-consider-when-travelling-with-a-motorhome-or-caravan/','GOK on Scandinavia') + ', ' + a('https://www.norwegiancruisingguide.com/chapters/changing-to-a-norwegian-propane-system/','Norwegian Cruising Guide') + '.'
])}

  <h3>Heating and ventilation</h3>
{card('systems--heater', 'Diesel blown-air heaters', 'Eberspächer Airtronic, Webasto Air Top, Espar', 'A small burner in a sealed box, somewhere out of the way, that draws fuel from the engine’s tank through its own pump and blows warm air through ducts into the cabins. The standard way to heat a boat in the Baltic and the North Sea, and fitted by later owners to several reference boats {TWO}.',
  ['The Eberspächer Airtronic D2, the commonest size on a boat this length, gives 0.85 to 2.2 kW of heat for 0.10 to 0.28 litres of diesel an hour and 8 to 34 W of electricity; the Webasto Air Top 2000 STC is similar (0.9 to 2 kW, 0.12 to 0.24 L/h). Starting takes much more current for a minute or two while the glow pin (a small electric heater) lights the burner {TWO}.', 'Combustion air comes in and exhaust goes out through the hull in sealed pipes; the cabin air it heats is a separate circuit. The heater should draw its fuel through its own pickup (a separate pipe into the tank, often a standpipe that stops short of the bottom), not from the engine’s fuel line, so that a heater fault cannot starve the engine, and the tank runs out for the heater before it does for the engine.'],
  ['Dry, even heat from the fuel tank you already have, at a cost of about a litre of diesel a night; the difference between a four-month and a six-month season up north.'],
  ['It needs a service every year or two, often with the unit taken out; it dislikes being run on low power for hours, which carbons it up; the start current is hard on a tired battery.'],
  ['Smoke and a smell of fumes (a carboned burner or glow-pin screen); failure to start; blowing cold air; the exhaust pipe hot inside a locker full of ropes.'],
  ['Run it for twenty minutes before buying; look at the exhaust run from end to end; ask for the service record; fit a carbon monoxide alarm whatever else you do.'], fold=True)}

{card('systems--co', 'Carbon monoxide', 'CO, BS EN 50291-2 alarm', 'An invisible, odourless gas from any burning fuel: a cooker, a heater, the engine, or the next boat’s generator. In a closed cabin it kills in the night.',
  ['In December 2019 two people died on the motor cruiser <em>Diversion</em> at York. The accident investigators found that carbon monoxide had leaked from the diesel heater’s exhaust: an owner-installed heater with the wrong, not gas-tight, car silencer, wrapped in exhaust tape that hid the leak, never serviced, and no CO alarm on board.'],
  ['A CO alarm to BS EN 50291-2 (the type made for boats and caravans, not the domestic -1 type) costs little and wakes you up; the RYA recommends one, and inland in the UK they have been compulsory since 2019.'],
  ['Headaches and drowsiness, the first signs, are easy to blame on a long day.'],
  ['No alarm, or an alarm past its date; a heater exhaust with joints in lockers or sleeping cabins; running the engine or a generator in a closed harbour next to other boats.'],
  ['Fit one CO alarm in the saloon and one where people sleep; test it; replace it by its date. If it sounds: get everyone into fresh air on deck, turn off the heater, cooker and engine, open every hatch, and get medical help for anyone with a headache, sickness or drowsiness.'], kind='fault', fold=True)}

{card('systems--ventilation', 'Stoves and ventilation', 'Refleks, Dickinson, dorade vent, mushroom vent, condensation', 'A drip-feed diesel stove (Refleks from Denmark, Dickinson Newport from Canada) burns diesel fed by gravity from a small tank, needs no electricity, and is silent. Ventilation matters as much as heat: a warm boat with no airflow is a wet one.',
  ['The Refleks 66M, the smallest, uses about 0.1 to 0.3 L of diesel an hour; the Dickinson Newport, sold for boats of 9 to 11 m, gives about 1.9 to 4.8 kW. Their flue (chimney) goes up through the coachroof, so they cannot always be used under way.', 'A dorade vent is a cowl (a scoop-shaped vent) on a box with a water trap: air goes down, spray does not. Mushroom vents, often with small solar fans, keep a trickle of air moving; condensation forms at night, when a solar fan has stopped.'],
  ['A stove is the warmest, driest heat there is, with a real flame to look at.'],
  ['It must be lit and tended; its flue needs a deck fitting and a cap; in a closed cabin it uses the air you are breathing, so ventilation is essential.'],
  ['Black soot on the deckhead (the cabin ceiling) above the stove; mildew in lockers and on the hull lining; a boat that smells damp the moment the hatch opens.'],
  ['Open lockers and look for mould; ask how the boat is aired over the winter.'], fold=True)}
{sources('heating', [
  a('https://www.krueger.co.uk/wp-content/uploads/2020/09/DOC014-Airtronic-D2-Product-Data-Sheet.pdf','Eberspächer Airtronic D2 data sheet') + ', ' + a('https://www.webasto.com/en-us/heating/marine-heaters/air-top-2000-stc-marine.html','Webasto Air Top 2000 STC') + '; start current from ' + a('https://forums.ybw.com/threads/eberspacher-current-draw.343835/','YBW') + ' (anecdotal); ' + a('https://assets.publishing.service.gov.uk/media/607572d2d3bf7f400b462d33/2021-03-Diversion-Report.pdf','MAIB report on Diversion') + ', ' + a('https://www.boatsafetyscheme.org/stay-safe-advice/carbon-monoxide-co/','Boat Safety Scheme on CO') + ', ' + a('https://www.rya.org.uk/water-safety/carbon-monoxide-safety/carbon-monoxide/','RYA on carbon monoxide') + '; ' + a('https://marineheating.co.uk/boat-appliances/refleks-boat-stoves/refleks-66m/','Refleks 66M') + ', ' + a('https://www.fisheriessupply.com/dickinson-marine-newport-diesel-heater','Dickinson Newport') + ', ' + a('https://www.boatlore.com/general-maintenance_ventilation.html','Boatlore on ventilation') + '. Fitted heaters on the fleet from individual listings.'
])}

  <h3>Heads and holding tanks</h3>
{figure('fig-heads', 'heads and holding tank', '0 0 900 520', 'A marine toilet below the waterline with vented loops, a Y-valve and a holding tank', 'A schematic side view. Sea water comes in through an inlet seacock and rises over a vented loop well above the waterline before reaching the hand pump beside the toilet bowl, which sits below the waterline. The discharge passes the joker valve, rises over a second vented loop and reaches a Y-valve, which sends it either to an overboard seacock or into a holding tank. The tank has a deck pump-out pipe, a vent with a smell filter, and a drain with its own seacock for emptying at sea.', g.heads(), 'Sea water in blue, waste in grey. Every hose here is below the waterline at some point, and two seacocks are open whenever the toilet is used.')}

{card('systems--toilet', 'The marine toilet', 'Jabsco, Lavac, Blake, joker valve', 'A hand-pumped toilet that brings in sea water to flush and pumps the bowl out. The Jabsco is the commonest; the Lavac, made since 1963, seals its lid and pumps the bowl empty so that the vacuum draws in the flush; the bronze-and-porcelain Blake is the traditional British one.',
  ['On a Jabsco, a lever on the pump switches between flush and dry; each stroke pumps water in and waste out. The joker valve, a rubber flap shaped like a duck’s bill at the outlet, stops waste flowing back into the bowl; Jabsco says change it every year, a ten-minute job.', 'The rule: only human waste and a little toilet paper. Anything else, wet wipes above all, blocks it.'],
  ['Simple, repairable and cheap to keep: every chandlery sells the service kit.'],
  ['Everyone who has owned a boat has had to take one apart. Seals and valves harden, and the discharge hose scales up (lines with a hard crust) from salts in sea water and urine.'],
  ['Water creeping back into the bowl (joker valve); a stiff pump; a smell that will not go away (the hoses); water leaking round the pump shaft.'],
  ['Flush it through, and pump it dry; look for scale in the discharge hose and damp around the base. Carry a joker valve and a service kit.'], fold=True)}

{card('systems--vented-loops', 'Vented loops, seacocks and hoses', 'anti-siphon loop, siphon break, sanitation hose', 'A toilet mounted below the waterline, as most are on boats this size, can siphon the sea into the bowl and sink the boat if its seacocks are left open. Jabsco requires a vented loop on both the inlet and the discharge wherever the toilet is below the waterline, upright or heeled.',
  ['The hose loops up well above the waterline; a small valve at the top of the loop lets air in and breaks any siphon. Both seacocks should still be closed whenever the boat is left, and on many boats after every use at sea.', 'Sanitation hose should be the low-permeation type, which smells cannot pass through (Trident Sani-Shield, Dometic OdorSafe, Raritan SaniFlex): ordinary hose lets the smell through its walls. The rag test: wrap a hot, damp cloth round the hose, let it cool, and sniff the cloth.'],
  ['A properly looped installation cannot flood the boat, even with the seacocks open.'],
  ['Vented-loop valves block with salt and stop working; they are hidden behind panels and forgotten.'],
  ['A bowl that fills slowly by itself; a vented loop that drips (its valve is stuck open) or never breathes (stuck shut); scale up to 13 mm thick inside old discharge hose.'],
  ['Find both loops and both seacocks. Flush a cup or two of white vinegar through the system once a week to slow the scaling; badly scaled hose is replaced, not cleaned.'], fold=True)}

{card('systems--holding-tank', 'Holding tank', 'black-water tank, Y-valve, deck pump-out, macerator', 'A tank the toilet can empty into, with a deck fitting for a marina pump-out, a vent with a smell filter, and usually a drain through its own seacock (or a macerator pump) for emptying at sea where that is allowed. None of the older reference boats is likely to have been built with one, since they predate the rules {EST} (the 2002 Gib’Sea 33 may have been: check); many have been fitted with tanks since, and ready-made replacements are sold for the Moody 33.',
  ['A Y-valve after the toilet sends the waste either to the tank or straight overboard. A tank mounted above the waterline can drain by gravity, which is simpler and more reliable than a pump {TWO}.'],
  ['It lets you use the toilet in harbour and in the many places where discharge is banned (below).'],
  ['Space is short on a 10 m boat, and a tank that is badly vented or plumbed smells. Pump-out stations are scarce in some countries.'],
  ['A smell in the heads that returns however often it is cleaned; a Y-valve seized in one position; a vent filter that has never been changed.'],
  ['Find out where the tank is, how full it is, and how it is emptied; check the Y-valve moves.'], fold=True)}

  <h4 id="systems--heads-routine">Using the heads</h4>
  <ol>
    <li>Open both seacocks (inlet and outlet) and check which way the Y-valve is set: to the tank in harbour and wherever discharge is banned.</li>
    <li>Use it; only human waste and a little paper.</li>
    <li>Pump with the lever on flush until the bowl is clean, then keep pumping: Jabsco asks for seven full strokes for every metre of discharge hose, Lavac for eight to ten pulls, a pause, and five or six more, so the waste clears the whole length of hose and does not sit in it.</li>
    <li>Switch to dry and pump the bowl empty; leave the lever on dry, so the bowl cannot fill by siphoning.</li>
    <li>Close both seacocks when the boat is left, and on many boats after every use at sea.</li>
  </ol>

  <details class="more">
    <summary>Where you may empty a toilet: the rules found, country by country</summary>
    <div class="more__body">
{compare('Where you may empty a toilet: international and Baltic rules', ['Waters', 'Rule for private yachts', 'Notes'], [
  ['International (MARPOL Annex IV)', 'does not apply', 'ships of 400 GT and above or certified for more than 15 people; the RYA: no international rule requires a pleasure craft to fit a holding tank'],
  ['Baltic special area', 'does not apply to yachts', 'passenger ships only: new ones from 1 June 2019, existing ones on the St Petersburg route from 1 June 2023, other existing ones in between {TBC}; HELCOM asks its member states to extend rules to pleasure craft, and not all have'],
  ['Sweden', 'no toilet waste anywhere in lakes, internal waters or the 12-mile territorial sea, since 1 April 2015', 'foreign boats included; marinas must offer disposal'],
  ['Finland', 'no untreated discharge within 12 nautical miles {TWO}', 'holding tanks required on new boats with a toilet from 1 July 2000'],
  ['Germany', 'no discharge on sea waterways; German boats to 12 nautical miles', 'Baltic: tank required on boats built after 2003, and on 1980–2003 boats only if over 11.5 m long and 3.8 m wide, so not on any reference boat'],
  ['Denmark', 'no emptying in harbours; zones to 2 nautical miles', 'tanks required on boats built after 2000, and on post-1980 boats over 10.5 m and 2.8 m beam; those may not empty within 12 nautical miles {TWO}'],
  ['Poland', 'national rule not yet in force {TWO}', 'some marinas seal the tank valve for the stay'],
], wide=True, stack=True)}
{compare('Where you may empty a toilet: Atlantic, Channel and Mediterranean coasts, and the Black Sea', ['Waters', 'Rule for private yachts', 'Notes'], [
  ['France', 'boats built from 1 January 2008 need a tank to use French ports and anchorages', 'no discharge in ports or within 3 nautical miles {TWO}'],
  ['Spain', 'no untreated discharge within 12 nautical miles {ONE}', ''],
  ['Croatia', 'a holding tank on every boat with a toilet, required from the end of 2021 {TWO}', 'whether it binds foreign-flagged private yachts was not confirmed; few marinas have pump-outs'],
  ['Greece', 'a tank is not a legal requirement, but the discharge rules make one a practical necessity {TWO}', 'distance limits {TBC}'],
  ['Turkey', 'no black or grey water discharge anywhere, even beyond 3 nautical miles', 'pump-outs recorded on the digital Blue Card; fines up to 5,000 US dollars in 2026 guides {TWO}'],
  ['Italy', 'no toilet discharge in harbours, marinas, at moorings or in bathing zones, under local harbour-master ordinances {ONE}', 'outside them, a yacht of this size (certified for fewer than 15 people) may empty its tank only more than 3 nautical miles offshore, moving at 4 knots or more; rules vary by harbour, so ask the harbour master’s office (Capitaneria di porto)'],
  ['Bulgaria', 'no wastewater discharge in internal waters or within 12 nautical miles, except into shore facilities {ONE}', 'applies to foreign yachts too; no marina pump-outs found, so keep the tank closed inside 12 nautical miles'],
  ['Romania', 'reported: no untreated wastewater from any vessel into Romanian waters (Water Law 107/1996, Art. 22, not verified) {TBC}', 'keep the tank closed in Romanian waters'],
], wide=True, stack=True)}
    </div>
  </details>
  <p>These rules change and are enforced differently from one harbour to the next; check the current rule for each country before you go. The EU Recreational Craft Directive now requires any toilet in a new boat to be connected only to a holding tank or a treatment system, with a standard deck fitting for pumping out and seacocks that can be secured closed, and its earlier version asked for a tank or provision for one {TBC}; the reference boats predate both, except perhaps the 2002 Gib’Sea 33.</p>
{sources('heads and rules', [
  'Toilets: ' + a('https://www.xylem.com/en-in/support/video-library/replace-manual-toilet-joker-valve/','Jabsco on the joker valve') + ', ' + a('https://www.fisheriessupply.com/lavac-toilet-popular-model-manual-toilet','Lavac') + ', ' + a('https://www.practical-sailor.com/systems-propulsion/vacuum-flush-toilets-for-sailboats-reduce-water-use-onboard/','Practical Sailor') + ', ' + a('https://marinestore.co.uk/blakes-lavac-taylors-products.html','Blakes Lavac Taylors') + '; vented loops: ' + a('https://productimageserver.com/literature/ownersManual/31422OM.pdf','Jabsco owner’s manual') + '; hose: ' + a('https://www.practical-sailor.com/systems-propulsion/marine-sanitation-hose-test/','Practical Sailor hose test') + ', ' + a('https://www.raritaneng.com/blog/marine-sanitation-hoses/','Raritan') + '; scale: ' + a('https://www.boatus.com/expert-advice/expert-advice-archive/2012/july/marine-toilet-maintenance','BoatUS on toilet maintenance') + '; tanks: ' + a('https://www.tek-tanks.com/product/moody-33-waste-tank/','Tek-Tanks (Moody 33)') + ', ' + a('https://forums.ybw.com/threads/holding-tank-moody.214709/','YBW') + ' (anecdotal).',
  'Rules: ' + a('https://www.imo.org/en/ourwork/environment/pages/sewage-default.aspx','IMO on sewage') + ', ' + a('https://www.rya.org.uk/boating-abroad/holding-tanks/','RYA on holding tanks abroad') + ', ' + a('https://www.guardiacostiera.gov.it/portale/documents/123907/1091340/DIVIETO+ALLE+UNITA%E2%80%99+DA+DIPORTO+DI+EFFETTUARE+SCARICHI+IN+MARE+DAI+SERVIZI+DI+IGIENICI+DI+BORDO+NELL%E2%80%99AMBITO+DELLE+ACQUE+PORTUALI.pdf/e12304b9-ce6d-c397-c454-e5c9ee767652?version=1.0&t=1738080137911null','Italian Coast Guard ordinance, Carloforte, 2011') + ' (an example of the local rule), ' + a('https://www.marad.bg/sites/default/files/upload/documents/2022-03/Nar_plavaneto_i_gran_rejim_27042012_0.pdf','Bulgaria, Decree 293/2009, Art. 7 (text consolidated to 2012)') + ', Romania’s Water Law 107/1996, Art. 22 (quoted by secondary sources; the official portal could not be read), ' + a('https://www.dnv.com/news/2017/baltic-sea-first-marpol-special-area-for-sewage-100367/','DNV on the Baltic special area') + ', ' + a('https://helcom.fi/publications/ships-sewage-in-the-baltic-sea-new-special-area-regulations/','HELCOM') + ', ' + a('https://www.noonsite.com/report/european-black-and-grey-water-regulations/','Noonsite, European black-water rules') + ', ' + a('https://www.transportstyrelsen.se/en/shipping/Environmental-protection/waste/sewage/','Swedish Transport Agency') + ', ' + a('https://www.tek-tanks.com/sanitation-systems/holding-tank-regulations/','Tek-Tanks on regulations') + ', ' + a('https://www.boote-magazin.de/en/travel-and-charter/territories/baltic-sea-protection-action-plan-politicians-call-for-tougher-rules-for-recreational-skippers/','Boote on German rules') + ', ' + a('https://www.rya.org.uk/boating-abroad/country-specific-advice/france/','RYA on France') + ', ' + a('https://www.rya.org.uk/boating-abroad/country-specific-advice/spain/','RYA on Spain') + ', ' + a('https://hrcak.srce.hr/file/293109','a Croatian paper') + ', ' + a('https://www.yacht.de/en/travel-charter/turkey/turkey-environmental-regulations-across-the-board/','Yacht on Turkey') + ', ' + a('https://sailarmada.com/blue-card-turkey-sailing','on the Blue Card') + ', ' + a('https://eur-lex.europa.eu/eli/dir/2013/53/oj/eng','Directive 2013/53/EU') + '.'
])}

  <h3>Bilge pumps</h3>
{figure('fig-bilge', 'bilge pumps', '0 0 900 440', 'Electric and manual bilge pumps seen from astern', 'A cross-section of the hull seen from astern. In the lowest point of the bilge an electric pump sits beside a float switch, with a high-water alarm float mounted higher. Its discharge rises high under the deck and leaves through the hull above the waterline. A manual pump in the cockpit draws through a hose with a strum box (strainer) in the bilge and discharges through its own outlet above the waterline.', g.bilge(), 'Two pumps with separate hoses and outlets: one that works on its own, and one that works when the electrics do not.')}

{card('systems--bilge-pumps', 'Bilge pumps and alarms', 'Whale Gusher, Rule, float switch, strum box, high-water alarm', 'Every boat should have at least one electric pump with an automatic float switch and one manual pump that can be worked from the cockpit, each with its own hose and outlet. A high-water alarm, a second float mounted higher with a siren, tells you when the water is winning; the routine below says what to do when it sounds.',
  ['A big manual diaphragm pump such as the Whale Gusher 10 moves about 65 litres a minute at a brisk 70 strokes. Electric pumps are rated at zero lift, pumping on the level with no hose; in Practical Sailor’s test, lifting salt water 1.5 m at 12.2 V, they delivered between two-thirds and one and a half times their rating: do not rely on the box.', 'The international standard for bilge pumping, ISO 15083, covers normal bilge water, rain, spray and seepage, and “does not set requirements for bilge pumps… designed for damage control”. A certification body’s checklist gives its minimum capacity per pump: 15 litres a minute for a boat of 6 to 12 m, with manual pumps rated at no more than 45 strokes a minute.', 'How many pumps: design categories (the sea conditions a boat is certified for, from A, open ocean, to D, sheltered water; see <a href="#buying--abroad">Buying</a>) came in with boats sold from mid-1998, so older boats have none, but a 9–11 m cruiser should meet the rule for A to C. There, the standard’s 2003 edition asks for two pumps: a fixed main pump (with an open cockpit helm it may be hand-operated if the water rises less than 1.5 m to leave the boat; with a wheelhouse helm it is powered) and a second, manual or powered pump that you can reach easily; category D needs only one {ONE}. The 2020 edition, amended in 2022, adds for new boats that the system be permanently installed and switched on from near the helm. On a viewing, find both pumps and work each one.'],
  ['A working automatic pump and alarm deal with a leaking gland or a hatch left open without anyone being on board.'],
  ['No bilge pump on a yacht keeps up with a real hole: a 38 mm fitting broken 0.6 m below the waterline lets in roughly 140 to 235 litres a minute, depending on the source {TWO}, far more than a typical electric pump delivers. The answer to a failed seacock is a wooden bung, not a pump.'],
  ['A float switch jammed by debris; a pump wired through the main switch, so it stops when the boat is left; a manual pump with a split diaphragm or no handle; a discharge that shares a hose, so one pump just recirculates through the other.'],
  ['Lift the float by hand and hear the pump run; pour a bucket in and work the manual pump from the cockpit; keep the bilge clean, because hair, sawdust and cable ties block pumps; tie a softwood bung to every seacock.'], fold=True)}

  <h4 id="systems--bilge-routine">When the bilge is filling, or the high-water alarm sounds</h4>
  <ol>
    <li><strong>Pump first:</strong> check the electric pump is running and start the manual pump; put a crew member on it.</li>
    <li><strong>Taste it:</strong> salt water is coming from the sea; fresh water is a tank, a pipe or the calorifier (turn the water pump off).</li>
    <li><strong>Find it, in order:</strong> the stern gland or saildrive seal; every seacock and hose, starting with the engine’s and the heads’; the cockpit drains; the log and depth transducers; the rudder tube. Close seacocks you do not need.</li>
    <li><strong>Stop it:</strong> a failed seacock or hose takes a softwood bung, hammered in; a broken transducer takes its blanking plug or a bung.</li>
    <li><strong>If the water is winning:</strong> call for help early, by DSC and a Pan-Pan or a Mayday (see <a href="#electronics--mayday">Electronics</a>), while you still have power and time.</li>
  </ol>
{sources('bilge pumps', [
  a('https://www.iso.org/standard/72972.html','ISO 15083') + ', ' + a('https://www.fisheriessupply.com/whale-gusher-10-mk3-manual-pump','Whale Gusher 10') + ', ' + a('https://www.practical-sailor.com/safety-seamanship/20-electric-bilge-pumps-tested/','Practical Sailor, 20 electric bilge pumps tested') + ', ' + a('https://www.boatus.com/expert-advice/expert-advice-archive/2026/february/double-duty','BoatUS on second pumps') + '; flooding rates from ' + a('https://passagemaker.com/lifestyle/is-your-bilge-pump-up-to-the-job/','PassageMaker') + ' and ' + a('https://sailmagazine.com/diy/know-how-is-your-bilge-pump-up-to-the-job/','Sail') + ', which disagree by a factor of 1.6.'
])}

  <h3>The reference fleet: tanks and systems</h3>
{compare('Tanks and systems on the reference boats', ['', 'Fresh water', 'Fuel', 'Systems found (on individual boats)', 'Known system faults'], [
  ['Moody 33', '182 L (33S) {ONE}', '91 or 144 L {TWO}; plastic replacements of about 90 L', 'two or three batteries, calorifier and Eberspächer heating added {TWO}; ready-made holding tanks sold for it', 'the original steel fuel tank rusts at its lower seams and has had to be cut out in pieces {TWO}'],
  ['Sadler 32', 'about 200 L {TWO}', '40 to 85 L, depending on the source and the boat {TWO}', 'Jabsco toilet, calorifier and Eberspächer heating common {TWO}; no holding tank on the boats found', 'the metal fuel tank corrodes at its brass drain plug and is hard to remove {TWO}'],
  ['Bavaria 1060', 'about 400 L {ONE}', '80 or 100 L {TWO}', 'Webasto heating, calorifier and a holding tank on one boat {TWO}', 'none found'],
  ['Gib’Sea 31', '254 L {ONE}; less on individual boats', '61 L {ONE}', 'two batteries and a charger; manual or chemical toilet {TWO}', 'none found'],
  ['Gib’Sea 33 (2002)', 'about 200 to 330 L {TWO}', '70 to 95 L {TWO}', 'three batteries, calorifier, Eberspächer heating, holding tank on some {TWO}', 'none found'],
  ['Finnsailer 35', '570 L {ONE}; 250 L on one boat', '300 to 450 L {TWO}', 'hot-air heating (an Eberspächer D4 on one), calorifier with immersion heater {TWO}', 'none found'],
], wide=True, stack=True)}
{sources('the fleet', [
  a('https://www.yachtdatabase.com/en/review.jsp?id=Moody+33S','yachtdatabase (Moody 33S)') + ', ' + a('https://www.moodyowners.info/threads/33s-fuel-tank.25345/','Moody Owners on the fuel tank') + ', ' + a('https://www.devalk.nl/en/brochure_full/809779/SADLER-32.html','a Sadler 32 at De Valk') + ', ' + a('https://sailboatdata.com/sailboat/sadler-32/','sailboatdata (Sadler 32)') + ', ' + a('https://forums.ybw.com/threads/diesel-tanks-replacement.527203/','YBW on Sadler tanks') + ' (anecdotal), ' + a('https://www.yachtdatabase.com/en/review.jsp?id=Bavaria+1060','yachtdatabase (Bavaria 1060)') + ', ' + a('https://www.yachtingcompany.nl/en/yachts_for_sale/957252/bavaria_1060/','a Bavaria 1060 listing') + ', ' + a('https://sailboatdata.com/sailboat/gibsea-31/','sailboatdata (Gib’Sea 31)') + ', ' + a('https://www.boats.com/reviews/boats/gibsea-33-the-latest-from-dufour/','boats.com review (Gib’Sea 33)') + ', ' + a('https://www.parker-adams.co.uk/gibsea-33/','a Gib’Sea 33 at Parker Adams') + ', ' + a('https://www.yachtdatabase.com/en/review.jsp?id=Finnsailer+35','yachtdatabase (Finnsailer 35)') + ', ' + a('https://larochelle.boatshed.com/finnsailer_35-boat-334110.html','a Finnsailer 35 at Boatshed') + '.'
])}

  <h3 id="systems--layup">Laying up and recommissioning</h3>
  <p>The systems in this section are what suffers most over a winter. Most of the damage is done by frost, flat batteries and still, damp air.</p>
  <ol>
    <li><strong>Water:</strong> drain the tanks, the pump, the accumulator, every tap and shower and the calorifier, opening the lowest drains; or, where the boat stays afloat and freezes, pump non-toxic propylene-glycol antifreeze through each tap (never the ethylene-glycol kind made for car engines).</li>
    <li><strong>Heads:</strong> ashore, drain and flush everything; afloat, flush antifreeze through the toilet, its hoses and the holding tank.</li>
    <li><strong>Batteries:</strong> charge them fully, then either disconnect them or keep them on a proper maintenance charger; recharge every couple of months if disconnected.</li>
    <li><strong>Gas:</strong> off at the cylinder; take the cylinder home if the boat is ashore.</li>
    <li><strong>Air:</strong> leave lockers and cushions open and vents clear so the air keeps moving.</li>
    <li><strong>In spring:</strong> refill and flush the water system through every tap; open and close every seacock several times and grease those with grease points; check battery terminals, charge fully and check flooded cells with a hydrometer; a bubble test or leak-down test on the gas; a new joker valve and a rag test of the heads hoses; a heater service and a CO alarm in date.</li>
  </ol>
{sources('laying up', [
  a('https://www.harbourguides.com/articles/WINTERISING-YOUR-BOAT','Harbour Guides on winterising') + ', ' + a('https://www.westmarine.com/west-advisor/Winterizing-Potable-Water-Systems.html','West Marine on potable water') + ', ' + a('https://www.batterytender.com/blogs/battery-tender-blog/marine-battery-winter-storage-best-practices-for-off-season-care','Battery Tender on winter storage') + ', ' + a('https://www.boatus.com/documents/boatus/spring-commissioning-checklist.pdf','BoatUS spring commissioning checklist') + ', ' + a('https://www.practical-sailor.com/boat-maintenance/spring-inspection-checklist-for-boats/','Practical Sailor spring inspection') + '.'
])}

  <h3 id="systems--checklist">The systems in one hour: a buyer’s checklist</h3>
  <ol>
    <li><strong>Batteries:</strong> dates, terminals, straps; resting voltages; which switch does what.</li>
    <li><strong>Behind the panel:</strong> fuses on every circuit, labelled cables, no household wire or taped joints.</li>
    <li><strong>Charging:</strong> with the engine running, about 14 V or more at each bank; the charger and solar settings match the batteries.</li>
    <li><strong>Shore power:</strong> press the RCD test button; look at the shore lead; ask about the anodes.</li>
    <li><strong>Water:</strong> run the pump with everything shut and listen; run each tap hot and cold after the engine has run.</li>
    <li><strong>Gas:</strong> the bucket test on the locker drain; the hose date; a bubble test; the flame-failure devices on every burner.</li>
    <li><strong>Heater:</strong> run it for twenty minutes; follow the exhaust pipe from end to end; a CO alarm in date.</li>
    <li><strong>Heads:</strong> both seacocks and both vented loops found; flush and dry; the rag test on the hoses; where the holding tank is and how it empties.</li>
    <li><strong>Bilge:</strong> lift the float and hear the pump; work the manual pump; a bung by every seacock.</li>
  </ol>

  <h3>Worth watching</h3>
{videos([
 ('DJBTei8NqBw', 'What you need to know about boat electrical, part 1', 'Clark’s Adventure', '12 V basics, for owners who have never opened the switch panel.'),
 ('WUBzCBvIGqg', 'Dangerous gas locker, and why every owner should do the bucket test', 'practicalboatowner', 'The bucket test from the gas routine on this page, and what a dangerous locker looks like.'),
 ('uqYkXa5AWe8', 'Replacing the joker valve in a Jabsco manual marine toilet', 'Jabsco Flojet Rule', 'The maker’s own video of the annual job in the toilet card.'),
 ('ycTi1SLmods', 'Boat electrical wiring made easy, from the ground up, part 1', 'Boat Fittings', 'A longer guide to wiring a boat from the battery outwards.'),
 ('P_lejUM3A6U', 'Jabsco twist-lock marine toilet service: full strip-down and rebuild', 'Mothership Adrift Boat Maintenance', 'The whole toilet, piece by piece, for when a new joker valve is not enough.'),
 ('pu_d5EHNVWI', 'LPG gas bubble tester on a boat', 'Marine Heating Solutions', 'How the bubble tester in the gas line is used and read.'),
 ('59zurwJKVjg', 'Eberspächer Airtronic D2 service and rebuild', 'Learn My Craft', 'Servicing one of the two common diesel heaters. The same heater is fitted to boats and vehicles, so the installation shown may not be a boat’s.'),
])}

  <h3>Terms used in this section</h3>
  <h4 class="terms__group">Electrics</h4>
{terms([
 ("house-bank","House bank","The battery or batteries that run everything except the starter: lights, instruments, fridge, autopilot."),
 ("start-battery","Start battery","A battery kept only for starting the engine, so that the engine starts whatever the house bank has been through."),
 ("main-fuse","Main fuse","A large fuse close to each battery that protects the main cable. ABYC puts it within 178 mm of the battery."),
 ("house-switch","House switch","The battery switch that connects the house bank to the panel. Off when leaving the boat."),
 ("start-switch","Engine switch","The battery switch for the start battery, alternator and starter. Never off while the engine runs."),
 ("link-switch","Emergency link switch","A switch that joins the two banks, to start the engine from the house bank if the start battery is flat. Normally off."),
 ("dcdc","Split charging (VSR or DC-DC charger)","A device that lets the alternator charge both banks without joining them for good: a voltage-sensing relay joins them while charging; a DC-DC charger charges the house bank at its own voltage."),
 ("sys-alternator","Alternator","The engine-driven generator that charges the batteries while the engine runs; the Engine section covers its belt."),
 ("solar-panel","Solar panel","Panels on the sprayhood, a frame or the deck. Shade on part of one cuts most of its output."),
 ("mppt","MPPT controller","A solar controller that converts the panel’s best voltage to battery voltage, typically 20 to 30 % better than the simpler PWM type."),
 ("shore-charger","Battery charger","A mains charger that runs on shore power. Set it for the battery type."),
 ("dc-panel","Distribution panel","The panel of breakers or fuses, one per circuit, fed through the house switch."),
 ("battery-monitor","Battery monitor","A display that counts amp-hours in and out through the shunt and shows the state of charge."),
 ("shunt","Shunt","A precise resistor in the house bank’s negative cable that the battery monitor measures every amp through."),
 ("neg-bus","Negative busbar","The bar where every negative cable joins; the start battery and house bank share it."),
 ("bilge-direct","Bilge pump supply","The automatic bilge pump’s own fused supply, straight from the battery, so it works with the house switch off."),
 ("shore-inlet","Shore-power inlet","The socket on the boat that the shore lead plugs into."),
 ("rcd","RCD","Residual current device: a switch that cuts the 230 V supply in a fraction of a second if current leaks to earth, as it would through a person."),
 ("polarity-light","Polarity light","A warning light that shows live and neutral have arrived swapped, common with Continental plugs."),
 ("galvanic-isolator","Galvanic isolator","A device in the shore earth wire that blocks the small currents between boats that eat anodes, while still passing a fault current."),
 ("amp-hour","Amp-hour (Ah)","A unit of battery capacity or use: one amp for one hour."),
 ("voltage-drop","Voltage drop","The voltage lost along a cable; too much and equipment misbehaves. ABYC allows 3 % for important circuits."),
 ("bms","Battery management system (BMS)","The electronics inside a lithium battery that protect it, by disconnecting it, from over-charge, deep discharge and charging in frost."),
])}
  <h4 class="terms__group">Water</h4>
{terms([
 ("water-filler","Water filler","The deck fitting for filling the water tank, marked WATER. Read it before the fuel nozzle goes in."),
 ("water-tank","Water tank","Stainless, plastic or a flexible bladder; 100 to 570 litres on the reference boats."),
 ("water-strainer","Water strainer","A small filter before the pressure pump that catches debris from the tank."),
 ("water-pump","Pressure pump","An electric pump that starts when a tap opens and stops when it closes."),
 ("accumulator","Accumulator","A small tank with a diaphragm and an air cushion that stores pressure so the pump does not cycle constantly."),
 ("calorifier","Calorifier","An insulated hot-water tank heated by engine coolant through a coil, and by an electric element on shore power."),
 ("coolant-coil","Calorifier coil","The coil inside the calorifier that engine coolant flows through; it heats the water without mixing with it."),
 ("immersion","Immersion heater","An electric element in the calorifier, worked by shore power."),
 ("taps","Taps","Mixer taps at the galley and basin, fed by the cold and hot lines; a foot pump often sits beside the galley one."),
])}
  <h4 class="terms__group">Gas, heating and air</h4>
{terms([
 ("sys-gas-locker","Gas locker","A locker sealed from the inside of the boat, opening only at the top, draining overboard from its bottom: 19 mm bore at least, outlet at least 75 mm above the waterline."),
 ("gas-cylinder","Gas cylinder","Butane or propane, stood upright and strapped in the locker. Different in every country."),
 ("gas-regulator","Regulator","The valve on the cylinder that reduces its pressure to the cooker’s: 28 or 37 mbar in the UK tradition, 30 mbar for Euro regulators."),
 ("gas-drain","Gas locker drain","The pipe from the bottom of the gas locker that carries leaking gas overboard. Test it with a bucket of water."),
 ("gas-solenoid","Solenoid valve","An electric valve at the locker, switched from the galley, that turns the gas off at source; the gas alarm closes it."),
 ("bubble-tester","Bubble tester","A small window of liquid in the gas pipe: with everything off, press the button, and bubbles mean a leak."),
 ("gas-valve","Isolating valve","A hand valve by the cooker that shuts off its supply."),
 ("cooker","Gimballed cooker","A cooker hung on pivots so it stays level as the boat heels and rolls; each burner should have a flame-failure device."),
 ("gas-alarm","Gas alarm","A sensor low in the bilge near the galley that sounds and closes the solenoid valve when it detects gas."),
 ("co-alarm","Carbon monoxide alarm","An alarm that detects the odourless gas from any burning fuel. Buy one made to BS EN 50291-2 (the boat and caravan type), and fit one where people sleep."),
 ("butane","Butane","The gas in blue Calor cylinders; stops vaporising near 0 °C, so it fails in the cold."),
 ("propane","Propane","The gas in red Calor cylinders and most Northern European ones; works down to about −40 °C."),
 ("diesel-heater","Diesel heater","A sealed burner that draws diesel from the tank and blows warm air through ducts; Eberspächer and Webasto are the usual makes."),
 ("sys-dorade","Dorade vent","A cowl vent on a box with a water trap, so air goes below and spray does not."),
])}
  <h4 class="terms__group">Heads and bilge</h4>
{terms([
 ("toilet","Toilet bowl","On most boats of this size it sits below the waterline, which is why its hoses need vented loops."),
 ("heads-pump","Heads pump","The hand pump beside the bowl that flushes and empties it."),
 ("joker-valve","Joker valve","A rubber duckbill valve at the toilet outlet that stops waste flowing back. Change it every year."),
 ("heads-inlet-seacock","Inlet seacock","The valve on the toilet’s sea-water intake. Closed after use and whenever the boat is left."),
 ("vented-loop","Vented loop","A loop of hose high above the waterline with a small valve at the top that breaks any siphon."),
 ("y-valve","Y-valve","A two-way valve that sends the toilet’s waste to the holding tank or straight overboard."),
 ("overboard-seacock","Overboard seacock","The valve on the toilet’s discharge. Closed after use and whenever the boat is left."),
 ("sys-holding-tank","Holding tank","A tank for toilet waste, emptied by a marina pump-out or, far enough offshore and where allowed, through its own seacock."),
 ("pump-out","Deck pump-out","The deck fitting a marina’s pump-out hose connects to."),
 ("tank-vent-heads","Holding-tank vent","A vent pipe from the holding tank to the hull side, with a carbon filter against the smell."),
 ("tank-seacock","Tank drain seacock","The seacock under the holding tank for emptying it at sea."),
 ("electric-bilge","Electric bilge pump","A submersible pump in the lowest point of the bilge. Rated at zero lift, so it pumps less than the box says."),
 ("float-switch","Float switch","A switch that starts the electric pump automatically when the water rises."),
 ("high-water-alarm","High-water alarm","A second float, higher than the first, that sounds a siren if the water keeps rising."),
 ("bilge-outlet","Bilge pump outlet","The discharge through the hull, above the waterline, reached through a high loop so the sea cannot flow back."),
 ("manual-bilge","Manual bilge pump","A big diaphragm pump worked from the cockpit, such as the Whale Gusher 10, about 65 litres a minute at a brisk pace."),
 ("strum-box","Strum box","A strainer on the end of a bilge pump’s suction hose that keeps debris out of the pump."),
 ("mixing-valve","Mixing valve","A thermostatic valve on the calorifier’s hot outlet that blends in cold water so the taps cannot scald."),
])}
  <h4 class="terms__group">Other words used here</h4>
{terms([
 ("absorption-float","Absorption and float","Two stages of battery charging: absorption holds a set voltage until the battery is nearly full; float then holds a lower voltage to keep it full."),
 ("cycle","Cycle","One discharge and recharge of a battery. Battery life is counted in cycles to a given depth of discharge."),
 ("relay","Relay","A switch worked by electricity rather than by hand."),
 ("fault-current","Fault current","The large current that flows when a live wire touches earth; it is what trips a breaker or RCD."),
 ("isolation-transformer","Isolation transformer","A transformer that passes shore power to the boat magnetically, with no wire connection to the shore earth: the safest and dearest way to stop galvanic corrosion."),
 ("macerator","Macerator","An electric pump that chops waste as it pumps it out of a holding tank."),
 ("black-grey-water","Black and grey water","Black water is toilet waste; grey water is from sinks and showers. Some countries ban discharging both."),
 ("gross-tonnage","GT (gross tonnage)","A measure of a ship’s internal volume, used to decide which rules apply. International sewage rules start at 400 GT, far above any yacht."),
 ("zero-lift","Zero lift","A pump’s rating with no height to lift the water and no hose: the best case, never reached in a boat."),
 ("leak-down-test","Leak-down test","A gas test with a pressure gauge: pressurise the pipe, close the cylinder, and see whether the pressure falls."),
 ("sulphation","Sulphation","Hard crystals that grow on the plates of a lead-acid battery left discharged. They cut its capacity for good."),
 ("vaporise","Vaporise","Turn from liquid to gas. LPG is stored as a liquid and vaporises in the cylinder to feed the cooker."),
])}

{sources('makers’ figures', [
  a('https://www.trojanbattery.com/resources/battery-maintenance','Trojan, battery maintenance') + ', ' + a('https://www.victronenergy.com/upload/documents/Datasheet-GEL-and-AGM-Batteries-EN.pdf','Victron, gel and AGM data sheet') + ', ' + a('https://www.victronenergy.com/upload/documents/Datasheet-AGM-Super-Cycle-battery-EN.pdf','Victron, AGM Super Cycle') + ', ' + a('https://www.victronenergy.com/upload/documents/Datasheet-12,8-&-25,6-Volt-lithium-iron-phosphate-batteries-Smart-EN.pdf','Victron, lithium Smart') + ', ' + a('https://www.hse.gov.uk/electricity/faq.htm','HSE, electrical safety') + ', ' + a('https://xanthiona.com/wp-content/uploads/2010/03/iso-13297-ac-current.pdf','ISO 13297:2000 (a copy)') + ', ' + a('https://foxschandlery.com/products/puriclean-powder-water-cleaner-and-purifier','Puriclean') + ', ' + a('https://www.westmarine.com/on/demandware.static/-/Sites-wm-master-catalog/default/dwe9ae61d8/images/legacy-pdf/Isotemp_Basic_Slim_Slim_Square_Water_Heaters.pdf','Isotemp calorifier manual') + ', ' + a('https://www.legislation.gov.uk/eudr/2013/53/annex/I','Directive 2013/53/EU, Annex I') + ', ' + a('https://www.westmarine.com/on/demandware.static/-/Sites-wm-master-catalog/default/dw73ff68f5/images/legacy-pdf/JabscoTwistnLockManualToilets.pdf','Jabsco manual toilet') + ', ' + a('https://www.sparesmarine.co.uk/_webedit/uploaded-files/All%20Files/Lavac%20Marine%20Toilets.pdf','Lavac instructions') + '.',
  'Power budget: ' + a('https://www.manualslib.com/manual/1750428/Indel-Webasto-Isotherm-Cruise-Classic.html?page=25','Isotherm Cruise manual') + ', ' + a('https://www.raymarine.com/en-us/our-products/marine-instruments/i70s-series/i70s-instrument','Raymarine i70s') + ', ' + a('https://www8.garmin.com/manuals/webhelp/gpsmap_touch/EN-US/GUID-29B68C4C-2208-4BC0-9636-8416C94E9CAE.html','Garmin GPSMAP specifications') + ', ' + a('https://rowlandsmarine.co.uk/content/raymarine-st1000plus-st2000plus-tiller-pilots-user-guide.pdf','Raymarine ST2000+ guide') + ', ' + a('https://standardhorizon.co.uk/product/gx2400e/','Standard Horizon GX2400E') + ', ' + a('https://www.landfallnavigation.com/product-assets/AISXB8000Transponder.pdf','Vesper XB-8000') + ', ' + a('https://www.hellamarine.com/en/products/interior-exterior-lamps/euroled-130/white-euroled-lamps.html','Hella EuroLED') + ', ' + a('https://www.hellamarine.com/shop/navigation-lights/all-round-360/naviled-compact-all-round-360/2-nm-naviled-360-compact-all-round-white-navigation-lamps/','Hella NaviLED all-round') + '.',
  'Bilge pumps and gas abroad: ' + a('https://www.imci.org/site/document/applications_checklists/Checklists/Checklist_Evaluation_Module_B_G_en240408.pdf','IMCI checklist summarising ISO 15083') + ' (PDF), ' + 'GOST ISO 15083-2016 (the Russian national standard, an identical translation of the 2003 edition, with its pump table), ' + a('https://cdn.standards.iteh.ai/samples/83709/0b0fbe807252496ab75f2faafb756b15/ISO-15083-2020-Amd-1-2022.pdf','ISO 15083:2020 Amendment 1 (2022), preview') + ', ' + a('https://jachtbouw.nl/leden/kennisbank-richtlijn-pleziervaartuigen-en-ce/bijlage-1-richtlijn-pleziervaartuigen-en-opmerkingen/','Dutch boatbuilders’ association on the RCD (in Dutch)') + ', ' + a('https://www.petrogaz.gr/products/lpg/cylinder-individuals/','Petrogaz cylinders') + ', ' + a('https://www.noonsite.com/place/greece/dodecanese/kalimnos/view/fuel-and-lpg/','Noonsite, Kalymnos') + ', ' + a('https://www.petrol.hr/za-dom/energija/ukapljeni-naftni-plin','Petrol, LPG in Croatia') + ', ' + a('https://www.noonsite.com/report/croatia-cruising-notes/','Noonsite, Croatia notes') + ', ' + a('https://kurumsal.aygaz.com.tr/en/cylindergas/products','Aygaz cylinders') + ' and ' + a('https://kurumsal.aygaz.com.tr/en/cylindergas/frequently-asked-questions','Aygaz FAQ') + ' (29 mbar kitchen regulator). Bulgaria: ' + a('https://store.toplivogas.com/lpg-cylinder.html','Toplivo Gas cylinders') + ', ' + a('https://store.toplivogas.com/lpg.html','Toplivo Gas offices') + ', ' + a('https://enders.bg/reducir-ventil-za-gaz-kak-da-izberete-pravilnia/','Enders on Bulgarian valves (in Bulgarian)') + ', ' + a('https://www.damtn.government.bg/wp-content/uploads/2025/01/Palnene%20na%20butilki%20sgasten%20gaz.pdf','DAMTN on filling cylinders, 2025 (in Bulgarian)') + '.',
  'Opened in September 2026; the ISO 13297 figure is from its 2000 edition, since superseded, and the later editions were not checked.',
])}

  <div class="planned">
    <p>Planned for this section</p>
    <ul>
      <li>Photographs: a correctly built gas locker, scaled heads hose, a diesel heater installation (still to be found under a CC licence)</li>
      <li>Holding-tank rules and marina pump-outs in Italy, Bulgaria and Romania; the pump table of ISO 15083’s 2020 edition</li>
    </ul>
  </div>
</section>
'''
finish(page, ROOT + 'sections/07-systems.html', others=(ROOT + 'sections/03-hull.html', ROOT + 'sections/04-rig.html', ROOT + 'sections/05-deck.html', ROOT + 'sections/06-engine.html', ROOT + 'sections/02-fleet.html', ROOT + 'sections/00-start.html'))
