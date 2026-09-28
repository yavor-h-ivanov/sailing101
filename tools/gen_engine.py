# Generates sections/06-engine.html for Sailing 101.
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_common import *
import gen_engine_diagrams as g

page = f'''<section id="engine">
  <h2>Engine and drivetrain</h2>
  <p class="lead">A small marine diesel of 18 to 75 hp, turning a propeller through a gearbox and either a shaft or a saildrive. It is simple, long-lived and forgiving of age, and it is the part of the boat most likely to spoil your day when it is neglected: almost every engine failure at sea is fuel, cooling water or electrics, not the engine itself. In a hurry? <a href="#engine--daily-check">Jump to the daily check</a> or <a href="#engine--faults">to faults by symptom</a>.</p>

  <details class="first-words" open>
    <summary>Seven words before anything else</summary>
    <dl>
      <dt>Raw water</dt><dd>Sea water (or lake water) pumped in to cool the engine and then sent out with the exhaust.</dd>
      <dt>Coolant</dt><dd>Fresh water and antifreeze sealed inside the engine, in a loop like a car’s. Most engines of this age have both a raw-water and a coolant side; some older ones use sea water only.</dd>
      <dt>Impeller</dt><dd>The rubber paddle wheel in the raw-water pump. It wears, and it dies in minutes if it runs dry.</dd>
      <dt>Bleeding</dt><dd>Letting air out of the fuel system after it has run dry or a filter has been changed. A diesel will not run on air.</dd>
      <dt>Ahead, neutral, astern</dt><dd>The three positions of the gearbox: forward, disconnected, and reverse. Astern is the sailor’s word for backwards.</dd>
      <dt>Stern gland</dt><dd>The seal where the propeller shaft leaves the hull, keeping the sea out while the shaft turns.</dd>
      <dt>Saildrive</dt><dd>An alternative to a shaft: a leg like the bottom half of an outboard motor (the clamp-on engine of a dinghy), bolted through the hull under the engine.</dd>
    </dl>
    <p class="first-words__note">Seacock (a valve on a hole through the hull), anode and the other hull words are explained in <a href="#hull">Hull, keel and rudder</a>; the sailing verbs are in the <a href="#rig--sailing-words">box at the top of Rig and sails</a>.</p>
  </details>
  <p class="conf-key"><b>Marks used below:</b> {ONE} means the fact comes from a single source; {TWO} means sources disagree or the figure is anecdotal (a forum, a broker’s listing of one boat, or an owner report); {TBC} means not yet verified. Figures, dates and makers’ rules that are unmarked are supported by at least two sources listed under “Sources and confidence” at the end of each topic. How a part works is described from standard marine-engineering practice and is not marked.</p>

  <h3>The engine at a glance</h3>
  <p>Open the engine box of any boat in the reference fleet and you will find the same parts in roughly the same places, whether the engine is a 1970s Thornycroft or a 2002 Volvo. The drawing shows a generic three-cylinder engine. Learn where seven things are before you ever need them: the <strong>dipstick</strong>, the <strong>coolant cap</strong>, the <strong>raw-water pump</strong>, the <strong>fuel filter</strong> on the engine, and two things that are usually not on the engine but near it: the raw-water <strong>strainer</strong> and the <strong>primary fuel filter</strong> (both drawn in the cooling and fuel diagrams below). Then the <strong>stop control</strong>: a lever on the engine, worked by a pull knob or a button at the helm.</p>


{figure('fig-engine-tour', 'engine tour', '0 0 900 470', 'A small marine diesel seen from the side, with the parts you check and service', 'A three-cylinder diesel on rubber mounts, bow to the right. On top: oil filler cap, air intake and filter, heat exchanger with its coolant filler cap. At the front (belt end): thermostat housing, alternator, drive belt and the raw-water pump with a hose from the strainer. On the side: injectors on the cylinder head with high-pressure pipes from the injection pump, the engine fuel filter, the lift pump with its priming lever, the dipstick, the oil filter and the starter motor. At the back: the exhaust mixing elbow with its hose to the waterlock, and the gearbox with its gear cable and the flexible coupling to the shaft.', g.engine_tour(), 'A generic engine, not any one make: on a Yanmar or Volvo the filters and pump may be on the other side or at the front. The raw-water hose (blue) runs from the strainer through the pump and the heat exchanger to the exhaust elbow; the fuel pipe (amber) runs from the tank through the lift pump and filter to the injection pump.', note=HINT)}
{photo('engine-yanmar-2gm20.jpg', 'A small two-cylinder marine diesel in its engine space, seen from the belt end, with its pulleys, belts and pumps', 'A Yanmar 2GM20, a two-cylinder diesel of the size found in many boats of this class, seen from the belt end. The parts are the ones in the drawing, but every make puts them in different places.', 'PHGCOM', 'CC BY-SA 3.0', 'http://creativecommons.org/licenses/by-sa/3.0/', 'https://commons.wikimedia.org/wiki/File:Yanmar_2GM20.JPG', 1280, 1293)}

  <details class="first-words first-words--closed">
    <summary>Inside the engine: the words the rest of this section uses (open if engines are new to you)</summary>
    <dl>
      <dt>Cylinder and piston</dt><dd>Each cylinder is a tube in the engine block with a piston sliding up and down inside it. Small boat diesels have one to four.</dd>
      <dt>Crankshaft and connecting rods</dt><dd>The rods join the pistons to the crankshaft, which turns their up-and-down movement into rotation. The crankshaft drives the gearbox at the back and the belt at the front.</dd>
      <dt>Cylinder head, valves and rocker cover</dt><dd>The head is the casting that closes the tops of the cylinders; its valves let air in and exhaust out. The rocker cover is the lid over the valve gear, where the oil filler usually is.</dd>
      <dt>Head gasket</dt><dd>The seal between block and head. When it fails, coolant, oil and combustion gas get where they should not.</dd>
      <dt>Camshaft</dt><dd>A shaft with bumps (cams) that opens the valves at the right moment; on many engines it also works the lift pump.</dd>
      <dt>Piston rings and valve guides</dt><dd>The rings seal the piston in its cylinder; the guides hold the valves. Worn, they let oil into the cylinders to be burnt (blue smoke).</dd>
      <dt>Stroke</dt><dd>One movement of a piston up or down its cylinder; the injection pump delivers a measured squirt of fuel for each firing stroke.</dd>
      <dt>Compression and firing</dt><dd>A diesel squeezes air so hard that it gets hot enough to light the fuel sprayed into it. When that happens the engine <em>fires</em> or <em>catches</em>. A compression test measures how well each cylinder still squeezes.</dd>
      <dt>Cranking, or turning over</dt><dd>The starter motor spinning the engine before it fires.</dd>
      <dt>Revs, tick-over and rated revs</dt><dd>Revs are engine turns per minute (rpm). Tick-over is the slowest steady speed, in neutral; rated revs are the maximum the maker designed it for under full load.</dd>
      <dt>Horsepower (hp) and kilowatts (kW)</dt><dd>Two units for the engine’s power: 1 hp is about 0.75 kW. Boats of this size have 18 to 40 hp; the Finnsailer’s motorsailer engine has about 75.</dd>
      <dt>Marinised</dt><dd>A car, van or tractor engine converted for a boat, with a heat exchanger, a raw-water pump, a wet exhaust and marine electrics.</dd>
    </dl>
  </details>

  <h3>Cooling</h3>
  <p>A diesel turns about a third of its fuel into work and most of the rest into heat, and all that heat has to go overboard. Most engines built since the 1990s, and many before, are cooled <strong>indirectly</strong>: coolant circulates inside the engine and gives its heat to sea water in a heat exchanger, and the sea water then goes out with the exhaust. Many small engines of the 1970s and 1980s (the Bukh DV20 and Volvo 2002 of later Sadler 32s among them) are cooled <strong>directly</strong>: sea water runs through the engine itself. Either way, the sea-water side is where the trouble is.</p>

{figure('fig-cooling', 'cooling path', '0 0 900 526', 'The raw-water cooling path from seacock to exhaust outlet', 'A schematic side view of the boat, stern on the left, bow on the right, with the waterline marked. Sea water enters through a seacock in the bottom (1), passes a strainer above the waterline (2) and the raw-water pump with its impeller (3), runs through the tubes of the heat exchanger on top of the engine (4), rises over an anti-siphon valve in a loop above the engine (5), and is sprayed into the exhaust at the mixing elbow (6). Exhaust and water fall into a waterlock box (7), are pushed up over a high loop and out of an outlet in the transom above the waterline (8). A separate red loop shows coolant circulating between the engine block, the thermostat and the heat exchanger.', g.cooling(), 'Follow the numbers. A fault anywhere from 1 to 4 means an overheating engine; a fault at 5 to 7 can let the sea into the engine. On a directly cooled engine there is no heat exchanger or coolant loop: the sea water goes through the engine block itself.', start=1)}

{card('engine--raw-water-intake', 'Seacock and strainer', 'raw-water intake, sea strainer, weed trap', 'The cooling water comes in through a skin fitting and a seacock in the bottom of the boat, then through a strainer: a jar with a basket that catches weed, shells, jellyfish and plastic before they reach the pump.',
  ['Open the seacock before starting and close it when leaving the boat. The strainer’s lid unscrews or unclips; the basket lifts out to be rinsed.', 'Always close the seacock before opening the strainer, wherever it is mounted: one that is above the waterline in harbour can be below it when the boat heels or is loaded.'],
  ['Cheap and easy to see: a clear jar shows at a glance whether water is flowing and whether it is choked.'],
  ['A strainer lid that does not seal lets air into the pump, and the engine overheats with a strainer that looks clean.'],
  ['A seacock left closed after a winter, or only partly open, is a common cause of overheating {TWO}; a strainer full of weed; a cracked jar; a lid sealing ring that has hardened.'],
  ['Part of the daily check: look at the strainer, rinse it if it has anything in it, and make sure the seacock handle is fully open. The Hull section covers seacocks themselves.'], fold=True)}
{photo('engine-seawater-cock.jpg', 'A ball-valve seacock with a red lever, and a hose held on by a clip, in a yacht’s bilge', 'The engine’s raw-water seacock on a small yacht: a ball valve with a lever, and the intake hose clipped to its tail.', 'PHGCOM', 'CC BY-SA 3.0', 'http://creativecommons.org/licenses/by-sa/3.0/', 'https://commons.wikimedia.org/wiki/File:Sea_water_cock.JPG', 768, 576)}

{card('engine--impeller', 'Raw-water pump and impeller', 'sea-water pump, Jabsco-type pump', 'A small pump at the front of the engine, driven by the belt or by gears, with a flexible rubber impeller spinning in a cam-shaped housing: the vanes bend as they pass the cam and squeeze the water on.',
  ['The rubber vanes seal against the housing and are lubricated by the water they pump. Run dry, they overheat and tear in a very short time.', 'A cover plate held by a few screws gives access; the impeller slides off its shaft, usually with pliers or a puller.'],
  ['Pumps well, primes itself, and a new impeller costs little; changing one is a twenty-minute job on a good installation.'],
  ['The vanes take a set and crack with age even when the boat is not used. On many installations the pump is hard to reach: a mirror and a short screwdriver help.'],
  ['Missing or cracked vanes after a dry run or a blocked intake. If vanes are missing, the pieces must be found: they lodge downstream, usually in the heat exchanger’s tube stack, and block it; a leaking pump seal drips water onto the engine.'],
  ['Beta Marine’s schedule is to check it every year or 250 hours and change it if worn; Volvo’s for its small D1 engines is every 12 months or 200 hours {ONE}. Most owners simply change it every year, and carry two spares with a new cover gasket.'], fold=True)}
{photo('engine-impeller.jpg', 'A black rubber impeller with six vanes, on a white background', 'A rubber impeller. This one is from an outboard’s water pump, but the flexible vanes are the same idea as in an inboard raw-water pump.', 'LittleGun', 'CC BY-SA 3.0', 'https://creativecommons.org/licenses/by-sa/3.0', 'https://commons.wikimedia.org/wiki/File:02_Impeller.jpg', 1280, 912)}

{card('engine--heat-exchanger', 'Heat exchanger, thermostat and coolant', 'indirect or fresh-water cooling, header tank', 'A tube bundle in a casing, often on top of or at the front of the engine: sea water flows through the tubes and coolant around them. On small engines the header tank and its pressure cap are usually part of the same casting.',
  ['A thermostat keeps the coolant inside the engine until it is warm, then opens to send it through the heat exchanger. An engine-driven circulating pump moves the coolant; the drive belt usually turns both this pump and the alternator.', 'A direct-cooled engine has no heat exchanger: a thermostat controls how much sea water passes through the block. Salt and scale build up inside such an engine in warm water, and some owners have converted them to indirect cooling {TWO}.'],
  ['Indirect cooling keeps salt out of the engine and lets it run at its proper temperature, which is kinder to it.'],
  ['More parts: a pressure cap, a second pump, hoses, coolant to change every few years (Volvo gives 2 to 4 {ONE}).', 'The tube stack (the bundle of small tubes inside) blocks with scale, impeller pieces and debris, and small ones corrode.'],
  ['A slowly rising temperature over a season (a scaled or blocked tube stack); a heat exchanger that has corroded or cracked where it is mounted {TWO}; coolant in the sea-water side or sea water in the coolant from a failed tube.'],
  ['Check the coolant level cold, as part of the daily check; never open the pressure cap on a hot engine. Beta has the tube stack removed and cleaned at service, with new O-rings (the rubber sealing rings at its ends); a retailer’s note says every five years on smaller Volvo engines {ONE}.'], fold=True)}

{card('engine--exhaust', 'Exhaust elbow, waterlock and anti-siphon valve', 'mixing elbow, injection bend, water muffler, vented loop, siphon break', 'After the heat exchanger the sea water is sprayed into the hot exhaust at the <strong>mixing elbow</strong> and cools it; gas and water then fall into the <strong>waterlock</strong>, a box low in the boat, and are pushed up over a high loop and out of the transom.',
  ['The waterlock holds the water that is in the exhaust hose when the engine stops, so that it cannot run back into the engine; the high loop (gooseneck) stops following waves pushing water up the exhaust.', 'Where the injection point is close to or below the waterline, sea water can siphon through the pump and heat exchanger into the exhaust and fill the engine while it stands. An anti-siphon valve at the top of a loop in the raw-water hose lets air in and breaks the siphon. Vetus says one is needed when the injection point is less than 15 cm above the waterline, with the valve itself at least 40 cm above it, and it must stay above the waterline at every angle of heel; the Yanmar figure quoted by owners is 18 inches, about 46 cm {TWO}.'],
  ['A wet exhaust is quiet and cool enough to run in rubber hose.'],
  ['The elbow is where hot gas, salt water and steel meet, and it rusts and chokes with carbon from the inside; on older engines it is a routine replacement part. Anti-siphon valves stick shut or open with salt.'],
  ['Falling water flow at the outlet, a rising temperature and black smoke from a choked elbow; rust weeping at the elbow flange; a vent valve encrusted with salt, spitting water, or stuck.'],
  ['Look at the elbow for weeping rust at every service and ask how old it is; clean or renew the anti-siphon valve with the impeller.'], fold=True)}

{card('engine--hydrolock', 'Hydrolock: the sea inside the engine', 'water in the cylinders', 'The one cooling fault that can destroy an engine outright. Water fills the exhaust system back to the engine and gets into a cylinder; water does not compress, so the next time the piston rises something bends or breaks.',
  ['It happens almost always during starting or just after stopping. The commonest cause: an engine that is cranked over and over without starting, while the raw-water pump keeps filling the exhaust with water that no exhaust gas is pushing out. The waterlock overflows back to the engine. A waterlock that is too small or mounted too high, and siphoning past a missing or stuck anti-siphon valve, do the same.'],
  ['Entirely preventable once you know the mechanism.'],
  ['The damage is expensive: bent connecting rods, cracked pistons, blown head gaskets.'],
  ['The engine will not turn over, or turns and stops with a thud; water when an injector is removed; milky oil on the dipstick after an attempt to start.'],
  ['Crank for no longer at a time than the engine manual allows. If the engine has not fired after a few attempts, close the raw-water seacock while you keep trying, and open it again the moment the engine runs. If the waterlock is full, drain it before trying again. If you suspect water in the cylinders, do not keep cranking: get help.'], kind='fault', fold=True)}
{sources('cooling', [
  'How it works: ' + a('https://www.pbo.co.uk/expert-advice/how-to-service-a-marine-engine-cooling-system-87085','PBO on servicing a cooling system') + ', ' + a('https://www.safe-skipper.com/boat-engine-cooling-systems/','Safe Skipper') + ', ' + a('https://www.discoverboating.com/resources/engine-cooling-systems-explained','Discover Boating') + '; direct cooling: ' + a('https://www.asap-supplies.com/engine-spares-by-model/volvo-penta/2001-2002-2003-2003t-series/2002','ASAP Supplies on the Volvo 2002') + ', ' + a('https://www.sailnet.com/threads/bukh-dv20-cooling-system.103832/','SailNet on the Bukh DV20') + ' (anecdotal).',
  'Impeller: ' + a('https://www.manualslib.com/manual/795178/Beta-Marine-Bv1903.html?page=7','Beta Marine service schedule') + ', ' + a('https://www.manualslib.com/manual/1598855/Volvo-Penta-D1-Series.html?page=48','Volvo Penta D1 manual (via ManualsLib)') + '; missing vanes: ' + a('https://www.tadiesels.com/assets/docs/tech/marine_engine_overheating.pdf','Trans Atlantic Diesels on overheating') + '; the partly closed seacock from ' + a('https://forums.ybw.com/threads/thornycroft-90-sea-water-pump.237893/','a YBW thread') + ' (anecdotal).',
  'Heat exchanger: ' + a('https://fybmarine.shop/volvo-penta-heat-exchanger-service-kit-for-volvo-penta-2002-2003-engines','FYB Marine (five-year note)') + ', ' + a('https://forums.ybw.com/threads/volvo-penta-2003.527254/','YBW on the Volvo 2003 mounting') + ' (anecdotal).',
  'Exhaust and siphoning: ' + a('https://sailmagazine.com/diy/hydrolock-headache/','Sail magazine, hydrolock headache') + ', ' + a('https://boatingmag.com/boats/how-to-prevent-hydrolock/','Boating on preventing hydrolock') + ', ' + a('https://webshop.vetus.com/en/products/exhaust-systems/air-vents','Vetus air vents (the 15 cm and 40 cm figures)') + ', ' + a('https://forums.ybw.com/threads/yanmar-3gm30-ehaust-manifold-mixing-ellbow-and-anti-siphon.240770/','the Yanmar figure as quoted on YBW') + ' (anecdotal), ' + a('https://www.pbo.co.uk/expert-advice/exhaust-elbow-repair-step-by-step-94055','PBO on exhaust elbow repair') + '.'
])}

  <h3>Fuel</h3>
  <p>Most engines that stop at sea stop because of fuel: dirt, water, air, or an empty tank. The fuel system has more parts than it seems, and each is a place where air can get in or dirt can collect. A diesel’s injection pump works at pressures that make even a pinhole leak dangerous, so the high-pressure side is left alone; everything up to the injection pump is yours to understand.</p>

{figure('fig-fuel', 'fuel system', '0 0 900 400', 'The fuel system from tank to injectors, with the bleed points numbered', 'A schematic of the fuel system. A tank with a deck filler, a vent and a pickup pipe, with water and sludge in its bottom. The fuel runs through a shut-off valve to the primary filter and water separator with a clear bowl, then through the lift pump with its hand priming lever and on to the engine fuel filter (bleed point 1), then to the injection pump (2), which sends fuel at high pressure through three steel pipes to the injectors (3). A dashed return line carries unused fuel from the injectors back to the tank. Blue dots mark the bleed points.', g.fuel(), 'Air gets in wherever a joint is opened or the tank runs low in rough water (a seaway); bleeding pushes it out, in the order of the fuel’s flow. The primary filter is upstream of the lift pump, so the priming lever cannot push air out of it: after changing it, fill its bowl with clean fuel before refitting. Some engines bleed themselves with an electric lift pump; older ones need every step.')}

{card('engine--tank', 'Tank, water and diesel bug', 'fuel contamination, FAME, biodiesel, B7', 'The tank on a boat of this age is often steel or aluminium, sometimes the original, with a filler on deck, a vent, a pickup pipe that stops short of the bottom, and rarely any way of draining the sump beneath it. Water gets in through the filler’s seal, the vent and condensation on the tank walls.',
  ['Water sinks to the bottom. At the boundary between water and diesel, bacteria, moulds and yeasts live on the fuel and grow into a dark slime, “diesel bug”, which blocks filters.', 'All road diesel sold in the UK and the EU to the EN 590 standard may contain up to 7 % biodiesel (FAME), and in practice most does. FAME attracts water and gives the bug more to live on; the RYA advises assuming up to 7 % is in your tank, and adding a biocide or other treatment when you fill up.'],
  ['Clean fuel in a clean tank keeps for years; a tank kept full over the winter has less air to breathe and so less condensation.'],
  ['A tank that has never been cleaned holds decades of sludge, and heavy weather stirs it up: “that biomass breaks loose in rough weather and heads straight for your filters and injectors” (Attainable Adventure Cruising). That is why old boats stop in the worst possible place, at the worst possible time. A heavy dose of biocide in a badly infected tank can itself block filters as the dead matter drops out.', 'On the Moody 33 the original steel tank is reported to rust and to come out only in pieces; on the Sadler 32 metal tanks are reported to corrode at the drain plug {TWO}.'],
  ['Black or brown slime in the primary filter bowl; water in the bowl; filters that block after a rough passage; an engine that surges and dies in a seaway and restarts in calm water.'],
  ['Look in the filter bowl before buying, and ask when the tank was last cleaned. Buy fuel from busy pumps; keep the filler cap seal and vent in good order; carry spare filters, because you will need them at sea first.'], kind='fault', fold=True)}

{card('engine--filters', 'Fuel filters and water separator', 'primary filter, pre-filter, Racor, CAV, secondary filter, fine filter', 'Two filters in series: a <strong>primary</strong> filter and water separator between the tank and the lift pump, usually on a bulkhead with a clear bowl; and a finer <strong>engine</strong> (secondary) filter on the engine itself, just before the injection pump.',
  ['Water is heavier than diesel and settles into the primary filter’s bowl, where it can be seen and drained with the tap at the bottom. The engine filter catches the fine particles that would wear the injection pump and injectors.'],
  ['Cheap insurance: the injection pump and injectors cost far more than a lifetime of filters.'],
  ['Every filter change opens the system and lets air in, so it must be bled afterwards.'],
  ['A bowl with a layer of water or black slime; a filter so blocked that the engine only runs at low revs; air leaks at a badly seated filter, which make the engine run rough and stop.'],
  ['Drain any water from the bowl as part of the daily check. Change both filters at the interval in the engine manual, before any long passage, and at once after a bout of contamination; carry spares and know how to bleed.'], fold=True)}

{card('engine--bleeding', 'Air in the fuel: bleeding the engine', 'priming, venting', 'A diesel that has run out of fuel, or has had a filter changed, has air in its pipes and will not run until the air has been pushed out. On most engines of this age this is done by hand, with the lift pump’s priming lever and the bleed screws, in the order the fuel flows.',
  ['If you changed the primary filter, fill its bowl with clean fuel first: the lift pump draws through it but cannot push air out of it. Then, at the engine fuel filter’s bleed screw (point 1), open the screw about half a turn and work the priming lever until fuel comes out with no bubbles; close the screw while still pumping. Do the same at the injection pump’s bleed screw (point 2).', 'Only if the engine still will not start: wrap a rag round one injector union (the nut on the pipe at the injector, point 3), keep hands and face well clear, crack it open half a turn to one turn and crank the engine until fuel comes out clear, then tighten. The fuel there is at injection pressure even on the starter: never do this with the engine running.', 'If the priming lever does nothing, the camshaft is holding the lift pump; turn the engine over briefly and try again.'],
  ['A fifteen-minute job once you have done it in harbour, and it gets a stopped engine going at sea.'],
  ['Fuel on the engine and in the bilge; a wrong move on the injector pipes can split them.'],
  ['An engine that starts and then dies after a filter change; one that stopped because the tank ran low in a swell.'],
  ['Do it once in harbour with someone who knows the engine, so you know where the screws are and what spanner fits. Keep the engine stop control in, and rags under everything.'], kind='fault', fold=True)}

{card('engine--injection', 'Lift pump, injection pump and injectors', 'fuel pump, diesel pump, injector nozzles', 'The <strong>lift pump</strong> draws fuel from the tank and pushes it through the filters; the <strong>injection pump</strong> raises it to very high pressure and sends it, cylinder by cylinder, at exactly the right moment, to the <strong>injectors</strong>, which spray it into the cylinders as a fine mist. Fuel the injectors do not use goes back to the tank through the return (leak-off) line.',
  ['The throttle lever on the injection pump sets how much fuel each stroke delivers, and so the engine’s speed. The stop control shuts the fuel off inside the pump.'],
  ['Well-filtered, they run for thousands of hours.'],
  ['Everything here is precision work for a diesel specialist; the high-pressure pipes and joints are not to be opened with the engine running.'],
  ['A worn or dribbling injector gives black smoke, knocking and hard starting; a failing lift pump starves the engine at higher revs; weeping at a leak-off pipe.'],
  ['Look for diesel on the engine and around the injectors; ask when the injectors were last serviced, and by whom.'], fold=True)}
{sources('fuel', [
  'Filters and bleeding: ' + a('https://www.pbo.co.uk/expert-advice/bleeding-the-fuel-system-on-your-boat-92060','PBO, bleeding the fuel system') + ', ' + a('https://www.boatus.com/expert-advice/expert-advice-archive/2015/october/bleeding-a-marine-diesel-engine','BoatUS on bleeding a diesel') + ', ' + a('https://www.cruisingworld.com/how/bleed-out-air/','Cruising World, bleed out the air') + ', ' + a('https://www.onboardwithmarkcorke.com/on_board/2009/01/bleeding-a-diesel-engine.html','On Board with Mark Corke') + '.',
  'FAME and diesel bug: ' + a('https://www.crownoil.co.uk/fuel-specifications/en-590/','Crown Oil on EN 590') + ', ' + a('https://en.wikipedia.org/wiki/EN_590','EN 590 (Wikipedia)') + ', ' + a('https://www.rya.org.uk/knowledge/safety/have-a-plan/engine-checks-preventing-fuel-contamination','RYA on preventing fuel contamination') + ', ' + a('https://www.yachtingmonthly.com/news/biodiesel-warning-to-boat-owners-84168','Yachting Monthly biodiesel warning') + ', ' + a('https://www.yachtingworld.com/practical-cruising/diesel-bug-the-causes-and-cures-135792','Yachting World on diesel bug') + ', ' + a('https://www.practical-sailor.com/boat-maintenance/diesel-biocides-take-on-contaminated-boat-fuel/','Practical Sailor on biocides') + ', ' + a('https://www.morganscloud.com/2012/03/30/diesel-fuel-contamination/','Attainable Adventure Cruising on fuel contamination') + '. Fleet tank faults from ' + a('https://forums.ybw.com/','YBW threads') + ' (anecdotal; see the Boat systems research).'
])}

  <h3>Starting, stopping and the alarm panel</h3>
{card('engine--starting', 'Glow plugs, starter and stop control', 'heater plugs, preheat, stop solenoid, stop cable', 'A diesel has no spark: it fires when air squeezed in the cylinder gets hot enough to light the fuel. A cold engine needs help, from <strong>glow plugs</strong> (small electric heaters in each cylinder, switched by a key position or a button) on most small engines, and the <strong>starter motor</strong> spins it until it fires. It stops only when its fuel is cut off.',
  ['Preheat for the time the manual gives, then crank; if it does not fire within a few seconds, stop, wait and try again rather than cranking on (see Hydrolock above).', 'The stop is either a pull cable and knob that shuts the fuel off at the injection pump (pulled out to stop, pushed back in to run), or a solenoid (an electric switch that moves a lever) worked by the key or a stop button. On some engines the solenoid must be powered to stop; on others it must be powered to run, so a failure either leaves the engine running or stops it. A pull cable is the simplest to fix {TWO}.'],
  ['A healthy small diesel starts at once, even after a winter, with a good battery and clean fuel.'],
  ['Turning the key off does not stop a diesel with a mechanical stop, and turning the battery switch off with the engine running can destroy the diodes (one-way electrical valves) inside the alternator.'],
  ['Slow cranking (a weak battery or corroded cables, the commonest cause); white smoke and a reluctant start in the cold (failed glow plugs); a stop cable that sticks half out so the engine starts and then dies.'],
  ['Know which stop system your engine has, where the handle or button is, and how to stop it by hand at the injection pump if the solenoid fails.'], fold=True)}

{card('engine--alarms', 'Alarm panel, alternator and belt', 'engine panel, oil pressure alarm, temperature alarm, charge light', 'The panel by the helm carries the key, the rev counter and usually three warning lights with a buzzer: <strong>oil pressure</strong>, <strong>coolant temperature</strong> and <strong>alternator charging</strong>. The alternator is driven by the same belt that often drives the coolant pump.',
  ['The lights come on with the key and go out when the engine is running properly. One marine engineer gives typical trigger points of about 104 °C for the temperature alarm and about 0.5 bar for the oil-pressure alarm {ONE}.'],
  ['A working buzzer is the difference between a new impeller and a new engine.'],
  ['Buzzers fail silently and senders (the small sensors screwed into the engine) corrode; a loose belt runs the coolant pump slowly and charges the batteries less well long before it squeals.'],
  ['No buzzer when the key is turned (test it every time); a charge light that glows dimly (a slack or worn belt, or an alternator going); black dust around the belt, or a belt with a shiny, glazed face where it has been slipping.'],
  ['Oil-pressure alarm: stop the engine at once; there is no safe way to keep running. Temperature alarm: slow down and stop as soon as it is safe, then work back along the cooling path from the seacock. Check the belt tension and wear with the engine off, as part of the daily check.'], fold=True)}
  <h4 id="engine--start-stop">Starting and stopping, step by step</h4>
  <p>Every engine manual has its own version; this is the common pattern for the small diesels on this class.</p>
  <ol>
    <li><strong>Before starting:</strong> engine battery switch on; raw-water seacock open; fuel shut-off open; gear lever in neutral; stop control pushed fully in (the run position); throttle opened a little if the manual says so.</li>
    <li><strong>Preheat</strong> with the glow plugs for the time the manual gives, longer in the cold.</li>
    <li><strong>Crank</strong> for no longer than the manual allows, and let go of the key the moment it fires. If it does not fire, wait, then try again; after a few attempts close the raw-water seacock (see Hydrolock).</li>
    <li><strong>Check at once:</strong> water coming out of the exhaust within a few seconds, and the oil-pressure and charge lights out. No water: stop the engine and look at the seacock, strainer and impeller.</li>
    <li><strong>To stop:</strong> neutral, tick-over for a minute or two after hard running; pull the stop knob (or press stop) and hold it until the engine stops; push the knob back in, or it will not start next time; then turn the key off. The battery switch comes last, never with the engine running.</li>
    <li><strong>Leaving the boat:</strong> close the raw-water seacock and the fuel shut-off if that is the boat’s routine.</li>
  </ol>
{sources('starting and alarms', [
  a('https://www.sailboatliveaboard.com/marine-diesel-glow-plugs.html','Sailboat Liveaboard on glow plugs') + '; stop systems: ' + a('https://www.trawlerforum.com/threads/q-energize-to-stop-or-energize-to-run-solenoid.8873/','Trawler Forum') + ', ' + a('https://www.sailnet.com/threads/diesel-stop-solenoid.85204/','SailNet') + ' (anecdotal), ' + a('https://www.yachtingmonthly.com/gear/how-to-stop-a-marine-diesel-engine-properly-93818','Yachting Monthly on stopping a diesel') + '; alarms: ' + a('https://stevedmarineconsulting.com/onboard-alarms-part-i/?print=print','Steve D’Antonio, onboard alarms') + ' (single source for the trigger points); belt: ' + a('https://www.endeavour-sailing.co.uk/images/pdf/diesel-engine-checks.pdf','Endeavour Sailing engine checks') + '.'
])}

  <h3 id="engine--daily-check">The daily check: WOBBLE</h3>
  <p>RYA training centres teach a six-letter check before the engine is started each day. Two schools, Endeavour Sailing and Equinox, give the same letters; other versions add batteries or leaks.</p>
  <ol class="lettered">
    <li><span class="lettered__l">W</span><span class="lettered__t"><strong>Water filter.</strong> Look at the raw-water strainer through its jar. If there is weed or debris, close the seacock, rinse the basket, refit the lid with its seal seated, and reopen the seacock.</span></li>
    <li><span class="lettered__l">O</span><span class="lettered__t"><strong>Oil.</strong> With the engine cold and the boat level: pull the dipstick, wipe it, push it fully back, pull it again and read where the oil reaches between the two marks. Black is normal in a diesel, and it goes black quickly; milky or grey is not (see <a href="#engine--faults">faults</a>). Check the gearbox the same way where it has its own dipstick.</span></li>
    <li><span class="lettered__l">B</span><span class="lettered__t"><strong>Belt.</strong> Engine off. The manual gives how far the belt should move under thumb pressure midway along its longest run: about 10 mm for a Volvo Penta D1 or D2, 8 to 10 mm for a Yanmar YM; look for cracks, fraying and a shiny, glazed face that means it has been slipping, and for black dust around it.</span></li>
    <li><span class="lettered__l">B</span><span class="lettered__t"><strong>Bilges.</strong> Torch under the engine: oil, fuel, coolant (often green, blue or pink) or more water than usual. Look at the stern gland.</span></li>
    <li><span class="lettered__l">L</span><span class="lettered__t"><strong>Levels.</strong> Coolant, cold, between the marks on the header tank or expansion bottle, or just below the filler neck; fuel in the tank; any water in the primary filter bowl drained.</span></li>
    <li><span class="lettered__l">E</span><span class="lettered__t"><strong>Engine and exhaust</strong>, once it is running (see <a href="#engine--start-stop">starting</a>): a steady spurt of water with the exhaust gas, the oil-pressure and charge lights out, and no new noise.</span></li>
  </ol>

{compare('Service intervals on a small diesel: what the makers say. The Beta Marine column is its every-year-or-250-hours service.', ['', 'Beta Marine', 'Other makers and notes'], [
  ['Engine oil and oil filter', 'change', 'Yanmar YM: oil at 50 hours, then every 150 hours or a year, the filter every 250 hours; Volvo Penta D1: oil and filter every 200 hours or once a year'],
  ['Raw-water impeller', 'check, change if worn', 'Volvo Penta D1: check it every 500 hours or once a year; most owners simply change it every year'],
  ['Air filter', 'check', ''],
  ['Fuel filters', 'change', 'Yanmar YM: every 250 hours or a year; Volvo D1: filter and pre-filter every 500 hours or once a year; and whenever the bowl shows water or dirt'],
  ['Anodes on the engine (if fitted)', 'check, replace when needed', 'Beta: six-monthly or more often in some waters'],
  ['Coolant', '', 'Volvo: every 2 to 4 years {ONE}'],
  ['Heat exchanger tube stack', 'remove and clean at service', 'retailer’s note for small Volvos: every 5 years {ONE}'],
  ['Saildrive oil', '', '200 hours or two years, or 400 hours: sources disagree {TWO}'],
  ['Saildrive diaphragm', '', 'Volvo Penta: every seven years; Yanmar: at least every six years for the SD20 and SD50 (in a 2004 manual), every five for the SD25'],
  ['Shaft seals', '', 'PSS face seal: bellows every six years; Volvo lip seal: every 500 hours or every fifth year'],
])}
  <p><strong>Fuel use at cruising revs,</strong> read from the makers’ curves: a Volvo Penta D1-30 about 2.9 litres an hour at 2,400 rpm and 4.4 at 2,800; a Yanmar 3YM30 about 2.2 at 2,500 rpm and 3.0 at 2,750. Flat out, both burn two or three times as much for little more speed, so cruising a few hundred revs below the maximum saves a lot of fuel.</p>
{sources('makers’ figures', [
  a('https://j109.org/docs/volvo_d1-30_operators_manual.pdf','Volvo Penta D1-30 operator’s manual') + ' and ' + a('https://www.manualslib.com/manual/1598855/Volvo-Penta-D1-Series.html','D1 series manual') + ', ' + a('https://j109.org/docs/yanmar_ym_series_operations_manual_v2_21jan09.pdf','Yanmar YM operation manual') + ', ' + a('https://j109.org/docs/yanmar_sd20_saildrive_operations.pdf','Yanmar SD20 manual') + ', ' + a('https://www.manualslib.com/manual/2205561/Yanmar-Sd25.html','Yanmar SD25 manual') + ', ' + a('https://www.shaftseal.com/marine/pss-maintenance-kit.html','PSS maintenance') + ', ' + a('https://www.volvopenta.com/marine/parts/maintenance-parts/anodes/','Volvo Penta, anodes') + ', ' + a('https://www.frenchmarine.com/DataSheets/D1-30.pdf','D1-30 data sheet') + ' and ' + a('https://www.frenchmarine.com/DataSheets/3YM30.pdf','3YM30 data sheet') + ' (fuel curves), ' + a('https://www.mepratuote.fi/en/product/29-hp-213-kw-yanmar-3ym30-km2p-2-211/','Meprat, Yanmar 3YM30 price') + '.',
  'Makers’ manuals and data sheets opened in September 2026 (some through copies hosted by owners’ associations and dealers); the fuel figures are our reading of the curves, to within about 0.2 litres an hour.',
])}

  <h3 id="engine--faults">When it goes wrong: faults by symptom</h3>
  <p>Diagnose from the outside in: battery and switches before the starter, fuel before the injection pump, the sea-water intake before the heat exchanger. Most faults are cheap ones.</p>
{compare('Faults by symptom', ['Symptom', 'Likely causes, commonest first', 'What to do'], [
  ['Nothing happens, or a click, when the key is turned', 'battery switch off; flat engine battery; corroded or loose battery or starter cable; the gear lever not in neutral on engines with a neutral switch', 'check the battery switch and voltage, clean and tighten the terminals'],
  ['Turns over but will not fire', 'no fuel (tank low, shut-off valve closed); air in the fuel; blocked filter; stop cable not pushed fully in; glow plugs not used or failed in the cold', 'check fuel and the stop control, preheat, bleed; after a few attempts close the raw-water seacock while cranking (hydrolock)'],
  ['Starts, then dies', 'air leak or blocked filter; water in the fuel; blocked tank vent; stop cable half out', 'look in the filter bowl, check the vent, bleed'],
  ['Temperature alarm or steam, little water at the exhaust', 'seacock closed; strainer choked; impeller failed; blocked heat exchanger or elbow', 'slow down, stop when safe, work along the cooling path from the seacock'],
  ['Temperature alarm with plenty of water at the exhaust', 'the coolant side: low coolant, a slack or broken belt (the coolant pump has stopped), a thermostat stuck shut, a scaled heat exchanger', 'stop when safe; let it cool before opening the cap; check the belt and coolant'],
  ['Oil-pressure light or alarm', 'low oil; a failing oil pump; occasionally a faulty sender', 'stop the engine at once; check the dipstick; do not run it again until the cause is found'],
  ['Charge light on', 'slack or broken belt (watch the temperature: the same belt may drive the coolant pump); an alternator or wiring fault', 'check the belt; if it is broken, stop the engine'],
  ['Stops suddenly under way', 'fuel: tank low in a seaway, a blocked filter, water in the fuel; rope round the propeller; the stop cable pulled by a foot or a line', 'neutral; check the filter bowl, the fuel and the propeller; bleed if it ran dry'],
  ['Knocking or a new, rhythmic noise', 'a sticking or dribbling injector; loose mounts or coupling; worn bearings inside the engine', 'reduce revs; look at mounts and coupling; get it checked before a passage'],
  ['No water from the exhaust', 'the same as above, starting at the seacock', 'stop the engine now; the rubber exhaust hose and waterlock will burn'],
  ['Black smoke', 'too much load (a fouled propeller or bottom, or rope round the prop); a choked air filter; worn injectors; a choked exhaust elbow', 'ease the throttle; check the air filter and the prop'],
  ['White smoke', 'a cold start (clears in a minute or two); if it persists, unburnt fuel or coolant getting into the cylinders', 'if it does not clear and the coolant level falls, stop and get help'],
  ['Blue smoke', 'oil being burnt: worn valve guides or piston rings, or an overfilled sump', 'check the oil level; plan an overhaul'],
  ['Vibration', 'rope, net or weed on the propeller; a damaged blade; misalignment; failed mounts or cutless bearing', 'stop and look over the stern; check mounts and coupling'],
  ['Milky oil on the dipstick', 'condensation in an engine run only briefly and never warmed (often harmless under the rocker cover); or a head gasket, a cracked head, an oil cooler, or sea water back through the exhaust', 'change the oil and watch; if it returns, get it diagnosed before running it again'],
  ['In gear, engine revs, but the boat does not move', 'gear cable off or broken; a worn gearbox or spline (known on the Volvo MS2B); coupling slipping on the shaft; propeller lost or a folding prop jammed', 'check the cable at the gearbox; look over the stern'],
], wide=True, stack=True)}
{sources('faults', [
  'Overheating: ' + a('https://yachtmate.fr/blog/en/engine-overheating-cooling-system.html','Yachtmate') + ', ' + a('https://www.tadiesels.com/assets/docs/tech/marine_engine_overheating.pdf','Trans Atlantic Diesels') + '. Smoke: ' + a('https://www.boats.com/how-to/diesel-engine-smoke-blue-black-or-white/','boats.com') + ', ' + a('https://www.cruisingworld.com/how/read-those-smoke-signals/','Cruising World, read those smoke signals') + '. Water in the oil: ' + a('https://www.sailboatliveaboard.com/water-in-marine-diesel-engine-oil.html','Sailboat Liveaboard') + ', ' + a('https://forums.ybw.com/threads/water-in-engine-oil.593013/','YBW') + ' (anecdotal). MS2B spline: ' + a('https://saltwaterdiesels.com/volvo-penta-2002/','Saltwater Diesels') + '. The remaining rows are standard fault-finding practice and are not individually sourced.'
])}

  <h3>Gearbox, shaft and saildrive</h3>
  <p>Behind the engine sits a gearbox that gives ahead, neutral and astern, usually with a reduction so the propeller turns slower than the engine. From there the power reaches the water in one of two ways, drawn below. On the reference fleet the Moody 33, Sadler 32 and Finnsailer 35 have shafts; every Bavaria 1060 found has a saildrive {TWO}; and 2002 Gib’Sea 33s are listed with both {TBC}.</p>

{figure('fig-drives', 'shaft and saildrive', '0 0 900 380', 'Shaft drive compared with saildrive, seen from the side', 'Two panels, bow to the right. Left: an engine and gearbox on flexible mounts drive, through a flexible coupling, a shaft that slopes down through a stern gland and a P-bracket with a cutless bearing to a propeller just ahead of the rudder. Right: an engine sits further forward with a saildrive leg bolted beneath its aft end, passing through the hull at a rubber diaphragm; an anode sits on the leg and the propeller spins level behind the leg’s lower unit.', g.drives(), 'A shaft is the traditional drive, and every yard can work on it; a saildrive is compact and quiet but has a large hole in the hull sealed by rubber, and an aluminium leg in salt water.')}

{compare('Shaft drive or saildrive', ['', 'Shaft drive', 'Saildrive'], [
  ['Where the boat is holed', 'a small stern tube, sealed by the stern gland', 'a large hole under the engine, sealed by a rubber diaphragm'],
  ['Seals to renew', 'packing, or a face or lip seal', 'the diaphragm (Volvo: every seven years) and the leg’s shaft seals'],
  ['Alignment', 'must be checked; mounts sag and hulls flex', 'none: engine and leg are one unit'],
  ['Corrosion', 'bronze and stainless; anode on the shaft', 'an aluminium leg; its anodes must be kept up'],
  ['Thrust', 'angled slightly downwards', 'level; less vibration and prop walk'],
  ['On the reference fleet', 'Moody 33, Sadler 32, Finnsailer 35', 'Bavaria 1060 {TWO}; Gib’Sea 33 {TBC}'],
])}

{card('engine--gearbox', 'Gearbox and gear lever', 'reverse gear, Hurth, ZF, Volvo MS, Kanzaki, TMP, Borg Warner', 'A small box bolted to the back of the engine, worked by a cable from the lever in the cockpit. On a saildrive the gearbox is inside the leg. Many boats of this class have a single lever that also works the throttle: straight up is neutral, forward is ahead, back is astern, and pushing further opens the throttle. Older boats often have two separate levers, one for the gears and one for the throttle.',
  ['Inside, Hurth (now ZF) boxes engage through a stack of friction plates; Volvo MS and Kanzaki boxes use a cone clutch (a cone pressed into a matching cup), which needs a firm, positive shift. With every type, change gear at tick-over and pause in neutral.', 'Under sail with the engine off: the ZF Hurth manual says the propeller may freewheel in neutral with no harm, never to leave it in forward, and that reverse can be used to lock the shaft. Volvo Penta’s advice for its MS gearboxes and saildrives has changed between editions: a 2019 manual says astern for a folding propeller and neutral or astern for a fixed one, with the engine run for five minutes, in neutral, every four hours of sailing; a 2006 manual said neutral for a fixed propeller. Yanmar says neutral. Follow the manual for your engine.'],
  ['Robust and simple; it needs oil at the right level and a properly adjusted cable.'],
  ['Slamming it into gear at high revs wears cone clutches; a gear cable stretched out of adjustment gives a gearbox that will not quite engage.'],
  ['Slipping or failing to engage; a clunk on engagement from worn damper plates (between engine and gearbox); the Volvo 2002’s MS2B has a spline (the ridged joint between two shafts) that “can wear out at an alarming rate”, with a known fix kit.'],
  ['Check the gearbox oil with the engine’s; move the lever through its range with the engine off and watch the lever on the gearbox move fully to each position.'], fold=True)}

{card('engine--mounts', 'Engine mounts, coupling and alignment', 'flexible mounts, R&D coupling, Centaflex, Aquadrive, engine bed', 'The engine sits on four rubber mounts on its bed (the two strong rails built into the hull under it), so its vibration does not reach the hull; the shaft is joined to the gearbox by a coupling, often a flexible one. Engine and shaft must line up exactly.',
  ['With a flexible mount, the engine moves on its rubber; the flexible coupling takes up small movements. A constant-velocity joint (Aquadrive and similar) takes the thrust on its own bearing and lets the engine move more freely, at more cost.', 'Alignment is checked at the coupling with the shaft disconnected: the two faces must meet evenly all round, to within the limit in the engine or coupling maker’s instructions. It is checked again after launching, when the hull has settled.'],
  ['Good mounts and alignment mean a quiet, smooth boat and a stern gland and cutless bearing that last.'],
  ['Rubber sags, perishes and softens in diesel, and on some installations the bolts rust solid in wooden beds (reported on the Moody 33 {TWO}); a misaligned shaft wears everything aft of it.'],
  ['Vibration at a particular rev range; a stern gland that keeps leaking; rubber cracked, bulging or oily; the engine sitting visibly lower on one mount.'],
  ['Look at each mount with a torch, feel for cracks, and watch the engine rock while someone puts it briefly into ahead and astern at the mooring.'], fold=True)}

{card('engine--cutless', 'Cutless bearing and P-bracket', 'shaft bearing, stern bearing', 'A rubber-lined tube, lubricated by the sea, that supports the shaft just ahead of the propeller, in a bronze P-bracket (a single strut; two struts make an A-bracket) or in the aft end of the stern tube (the tube moulded into the hull that the shaft runs through) or a skeg.',
  ['Water flows along grooves in the rubber and lubricates it; the shaft runs on a film of water.'],
  ['Cheap and long-lived when the shaft is aligned and the water is clean.'],
  ['Wears faster in muddy water and with a misaligned shaft; replacement usually means a lift out and a press.'],
  ['Play when the propeller is pushed hard sideways with the boat out of the water; a knocking or vibration under way; a P-bracket loose in the hull.'],
  ['On the hard, grab the propeller and push it up, down and sideways: any clear movement at the bearing means a new one.'], fold=True)}

{figure('fig-stern-glands', 'stern glands', '0 0 900 300', 'Three kinds of stern gland, cut open along the shaft', 'Three panels, each showing a shaft passing out of a stern tube, the sea on the left. Left: a packed stuffing box with a hose and double clips on the stern tube, a body holding rings of packing round the shaft, and a follower tightened by nuts, with drips below. Middle: a face seal with a rubber bellows clipped to the stern tube, a carbon ring on its end with a small vent hose, and a stainless collar fixed to the shaft pressing against the carbon. Right: a lip seal, a rubber sleeve clipped over the stern tube whose lips run on the shaft, with grease between them.', g.stern_glands(), 'The packed gland drips by design and fails slowly; the face and lip seals are dry but depend on rubber that ages. Every one of them is joined to the stern tube by hose and clips that are below the waterline.')}

{card('engine--stern-gland', 'Stern gland (shaft seal)', 'stuffing box, packed gland, PSS, face seal, lip seal, Volvo seal, oil-fed gland', 'Where the shaft leaves the hull something has to let it spin while keeping the sea out. Three families are drawn above; the Sadler 32 adds a fourth, an oil-fed gland made by Halyard and fitted from about 1982, with a reservoir of hypoid gear oil (a thick gearbox oil) {TWO}. All of them sit on the stern tube, the tube moulded into the hull that the shaft runs through.',
  ['<strong>Stuffing box:</strong> rings of greased flax or PTFE (a slippery plastic, the one on non-stick pans) packing squeezed round the shaft by a follower. It is meant to drip while the shaft turns, to lubricate and cool the packing; about a drip a minute is one figure given {ONE}. Some have a remote greaser, a screw-down grease cup that pushes fresh grease into the packing.', '<strong>Face seal (PSS type):</strong> a carbon ring on a rubber bellows presses against a stainless collar screwed to the shaft. Dry; needs its vent to let air out after launching.', '<strong>Lip seal (Volvo type):</strong> a rubber sleeve slid over the stern tube, with lips that run on the shaft and grease between them. It must be “burped”, squeezed to let trapped air out, after every launch.'],
  ['Stuffing box: cheap, adjustable, repackable afloat in an emergency, and it fails slowly and visibly. Face and lip seals: a dry bilge and no adjustment.'],
  ['Stuffing box: drips, needs adjusting, and wears a groove in the shaft over decades. Face and lip seals: rubber that ages, and a failure that can be a sudden flood rather than a drip. PSS gives six years for its bellows; Volvo Penta gives 500 hours or five years for its lip seal.'],
  ['An over-tightened stuffing box that runs hot and scores the shaft; hose clips rusted through on the hose that joins gland to stern tube; a face-seal collar that has slipped along the shaft, letting the carbon face open; a lip seal run dry after launch and now leaking; on the Sadler’s oil-fed gland, an oil level that falls noticeably between seasons, which means new seals {TWO}.'],
  ['After a motoring passage feel the gland: warm is fine, hot is not. Count the drips at rest and under way. Two stainless clips at each end of every hose, neither rusted. Ask when the bellows or lip seal was last replaced; no answer means now.'], fold=True)}

{card('engine--saildrive', 'Saildrive leg, diaphragm and anodes', 'Volvo 110S, 120S, 130S, Yanmar SD, sail drive', 'A leg containing a right-angle drive and the gearbox, bolted under the engine and passing through a large hole in the hull, sealed by a thick rubber diaphragm. Volvo Penta popularised it and it is standard on most production boats since the 1990s; every Bavaria 1060 found has a Volvo 2003 engine on one {TWO}.',
  ['The diaphragm is the only thing keeping the sea out of that hole, and Volvo Penta’s instruction is explicit: replace it every seven years. Insurers may take a dim view of a claim on a boat where that has not been done. It means lifting the engine and leg, a big yard job.', 'The leg is aluminium, which corrodes more readily than any other metal in the drive. Its anodes (a ring or block of more easily corroded metal, bolted on so that it corrodes instead) must be renewed before they are half gone.'],
  ['Level thrust, low vibration, easy installation, and much less prop walk (the stern’s sideways kick in reverse, see Propellers) than a shaft.'],
  ['A rubber seal below the engine that has a fixed life; an aluminium leg that suffers badly from any stray electric current in a marina, or from the wrong antifouling or anode; the leg’s own oil to check and change.'],
  ['Milky oil in the leg (water getting past its propeller-shaft seals); corrosion pitting or bubbling paint on the leg; anodes eaten away; a diaphragm with no documented date.'],
  ['Ask for the date the diaphragm was last changed and see the invoice. Look at the leg and anodes on the hard. Volvo Penta now says aluminium anodes in salt and brackish water (zinc will do in salt), magnesium in fresh water only, and never an antifouling with copper oxide on the leg, nor paint on the anodes; Yanmar fits zinc and says no paint with copper in it. Follow the manual, especially in the brackish Baltic.'], fold=True)}
{sources('drivetrain', [
  'Gearboxes: ' + a('https://manualzz.com/doc/en/4546927/owner-s-manual-hbw-english-italiano','ZF Hurth HBW owner’s manual') + ', ' + a('https://marinedieselbasics.com/marine-transmission-gearbox-manuals/zf-transmissions-manuals/zf-hurth-hbw-50-owners/','Marine Diesel Basics (the same manual)') + '; Volvo MS under sail: ' + a('https://forums.ybw.com/threads/volvo-120s-and-ms2-gearbox-query.450196/','YBW') + ' (anecdotal, conflicting); Kanzaki: ' + a('https://forums.sailboatowners.com/threads/neutral-or-not-kanzaki-km2p-1.114588/','Sailboat Owners') + ' (anecdotal); MS2B spline: ' + a('https://saltwaterdiesels.com/volvo-penta-2002/','Saltwater Diesels') + '.',
  'Mounts: ' + a('https://forums.ybw.com/threads/moody-thornycoft-t90-engine-mountings.108918/','YBW on Moody T90 mountings') + ' (anecdotal). Stern glands: ' + a('https://www.pbo.co.uk/gear/dripless-shaft-seals-pbo-buyers-guide-17357','PBO buyer’s guide to dripless seals') + ', ' + a('https://forums.ybw.com/threads/stern-glands-deep-sea-seals-or-traditional-type.372852/','YBW') + ' (anecdotal); Sadler oil-fed gland: ' + a('https://forums.ybw.com/threads/sadler-sterngland.87011/','YBW') + ', ' + a('https://forums.ybw.com/threads/oil-fed-stern-gland.484639/','YBW') + ' (anecdotal) and ' + a('http://www.lucasyachting.co.uk/wp-content/uploads/2017/10/cautionary-tales.pdf','Lucas Yachting, cautionary tales') + '.',
  'Saildrive: ' + a('https://www.sailboat-cruising.com/Saildrive-Maintenance-and-Volvo-Penta.html','sailboat-cruising.com on Volvo’s seven-year rule') + ', ' + a('https://www.pbo.co.uk/expert-advice/expert-answers/volvo-saildrive-seal-replacement-how-often-70454','PBO expert answer') + ', ' + a('https://dale-sailing.co.uk/chandlery/product/volvo-penta-21389074-rubber-diaphragm-seal-kit-for-all-saildrives/','Dale Sailing (the seal kit)') + '. Bavaria 1060 saildrives from ' + a('https://www.boats.com/sailing-boats/1985-bavaria-bavaria-1060-9991645/','boats.com') + ' and ' + a('https://www.uwjachtmakelaar.nl/en/sailboat/164433/bavaria-1060/','White Whale Yachtbrokers') + ' (one boat each).'
])}

  <h3>Propellers</h3>
{figure('fig-props', 'propellers', '0 0 900 280', 'Fixed, folding and feathering propellers', 'Three drawings. A fixed three-bladed propeller seen from astern. A folding two-bladed propeller seen from the side, its blades open at right angles to the shaft and, in ghost, folded back behind the hub. A feathering three-bladed propeller seen from astern, its blades turned edge-on as when sailing, with the powered position in ghost.', g.propellers(), 'The pale outlines show the other position of the blades. The propeller is a compromise between pushing well under engine and dragging little under sail. Fixed propellers are the cheapest and the most common on boats of this age.')}

{card('engine--propellers', 'Propellers', 'fixed, folding (Gori, Flexofold, Brunton), feathering (Max-Prop, Kiwiprop, Autoprop)', 'Boats of this class left the factory with a fixed two- or three-bladed bronze propeller; many have since been given a folding or feathering one. On the fleet boats found: a Brunton four-blade folding and a three-blade feathering propeller on re-engined Moody 33s, an Autoprop on a Gib’Sea 33, and a Volvo folding propeller on a re-engined Bavaria 1060 {TWO}.',
  ['A propeller is described by its diameter and its pitch, both in inches even in Europe: pitch is how far it would move forward in one turn if it screwed through the water like a bolt through a nut. Diameter and pitch are matched to the engine’s power and the gearbox reduction; a mismatch shows as an engine that will not reach its rated revs (too much pitch, and black smoke) or races without pushing (too little).', 'A folding propeller’s blades are swung open by the spinning shaft and folded shut behind the hub by the water when sailing. A feathering propeller turns its blades edge-on to the flow when sailing, and turns them round for astern, so it pushes as hard backwards as forwards.'],
  ['Folding and feathering propellers can add noticeably to speed under sail on a small boat, which is why racers fit them.'],
  ['They cost several times a fixed propeller, have moving parts to wear and grease, and a folding propeller can be weak in astern. A gearbox of the opposite rotation, after a new engine, needs a propeller of the opposite hand.'],
  ['A fouled propeller (weed, barnacles) that loses half its thrust; a bent blade after a grounding or a rope; worn hinge pins on a folding prop; a feathering prop whose grease has washed out and that no longer changes pitch.'],
  ['On the hard, spin it: every blade the same, no wobble, hinges or feathering smooth. Anti-foul it with a propeller coating, and clean it before a season.'], fold=True)}
  <p><strong>Prop walk.</strong> In astern, a propeller also pushes the stern sideways, strongly on a shaft-driven long-keel boat like the Finnsailer, less on a saildrive. Which way depends on the propeller’s hand: a right-handed propeller (turning clockwise, seen from astern, when going ahead) pulls the stern to port in astern. Find out on your own boat in open water before you need it; <a href="#manoeuvres">Manoeuvres under engine</a> shows how to use it.</p>
{sources('propellers', [
  'Fleet propellers from individual listings: ' + a('https://www.apolloduck.us/boat/moody-33-mki-for-sale/795008','a Moody 33 Mk I') + ', ' + a('https://davidmorrisboats.co.uk/our-boats/p/moody-33','a Moody 33') + ', ' + a('https://www.parker-adams.co.uk/gibsea-33/','a Gib’Sea 33') + ', ' + a('https://www.uwjachtmakelaar.nl/en/sailboat/164433/bavaria-1060/','a Bavaria 1060') + ' (one boat each); opposite rotation from ' + a('https://forums.ybw.com/threads/what-did-you-replace-your-bukh-dv20-with.301439/','YBW') + ' (anecdotal). The descriptions of pitch, folding and feathering and of prop walk are standard practice, not individually sourced; no drag figures were found.'
])}

  <h3>Repowering</h3>
{card('engine--repower', 'Repowering: when and what', 'new engine, re-engining, Beta, Yanmar, Volvo, Vetus, Nanni', 'Many boats of this class are on their second or third engine. A new engine is the biggest single spend most owners make, and a recently repowered boat is worth more; an original fifty-year-old engine is not necessarily a reason to walk away, if it runs well and parts exist.',
  ['The usual replacements are Beta Marine (Kubota-based and popular in the UK, with a 25 hp model that fits boats of about 4 tonnes {TWO}), Yanmar 3YM, Volvo Penta D1, Vetus and Nanni. Moody 33 owners have fitted Beta 28, 30 and 35 and a Sole 44; Sadler 32 owners Beta 25 and 28 and Volvo D1-30 {TWO}.', 'What else changes: often the engine beds, coupling, shaft, propeller, cutless bearing, exhaust mixing box and siphon break, the panel and cables, and the fuel pipes. A different gearbox rotation needs a propeller of the other hand.'],
  ['A new engine brings reliability, fuel economy, parts on every shelf and a warranty, and often lower weight.'],
  ['The engine price is the smaller part: one Moody 33 owner’s quotes were £4,840 to £5,604 for the engine, plus about £1,500 in parts and about £1,000 in fitting {TWO}; a Sadler owner put a whole job at about £6,000 {TWO}. Both are from undated forum threads, probably a decade or more old. Newer figures: a Finnish dealer listed a Yanmar 3YM30 with gearbox and panel at €11,184 in September 2026 (list price €13,980; VAT not stated) {ONE}, and a UK dealer lists the same engine with gearbox at £9,582 with VAT (undated page, seen September 2026). Beta Marine does not publish prices openly: the last known is £6,349 for a Beta 30 (Yachting Monthly, 2012). Yachting Monthly re-engined its Hallberg-Rassy 34 with a Beta 25 for just under £8,000 in all, parts and fitting included, in 2024. For today’s prices ask ' + a('https://betamarine.co.uk/seagoing-pricing-ordering/','Beta Marine') + ' or a dealer such as ' + a('https://www.frenchmarine.com/Product.aspx?PID=77','French Marine') + '.'],
  ['Spares supply: the Watermota Sea Panther of early Sadler 32s depends mainly on one specialist; the Thornycroft T90, Bukh DV20, Volvo 2002 and 2003 and Perkins 4.236 are all still supported.'],
  ['Before buying an old-engined boat, price parts for its engine, and have an engineer do a compression test and an oil analysis (a laboratory test of an oil sample that shows wear metals, fuel or coolant); before repowering, ask a specialist to quote the whole job, not the engine.'], fold=True)}
{sources('repowering', [
  'Prices: ' + a('https://www.frenchmarine.com/Product.aspx?PID=77','French Marine, Yanmar 3YM30') + ', ' + a('https://www.yachtingmonthly.com/archive/replacing-an-old-engine-costs-and-contacts-2680','Yachting Monthly, replacing an old engine (2012)') + ', ' + a('https://www.yachtingmonthly.com/gear/how-we-installed-a-new-engine-on-our-yacht-98437','Yachting Monthly, how we installed a new engine (2024)') + '.',
  a('https://forums.ybw.com/threads/beta-vs-vetus-vs-yanmar-re-engine-moody-33.352612/','YBW, Beta vs Vetus vs Yanmar on a Moody 33') + ', ' + a('https://forums.ybw.com/threads/best-re-engine-choice-for-sadler-32.473563/','YBW, best re-engine for a Sadler 32') + ', ' + a('https://forums.ybw.com/threads/sadler-32-and-watermota-sea-panther.494475/','YBW on the Watermota') + ' (all anecdotal, undated); ' + a('https://betamarineusa.com/portfolio/beta-25-saildrive/','Beta Marine Beta 25') + '. Spares: ' + a('https://stephensonmarine.co.uk/watermotaseapantherspares.html','Stephenson Marine (Watermota)') + ', ' + a('https://www.asap-supplies.com/engine-spares-by-model/thornycroft/90','ASAP Supplies (Thornycroft 90)') + ', ' + a('https://shop.tnorrismarine.co.uk/collections/bukh-service-parts','T. Norris Marine (Bukh)') + ', ' + a('https://fybmarine.shop/volvo-penta-2002-service-and-spare-parts','FYB Marine (Volvo 2002)') + ', ' + a('https://www.tadiesels.com/perkins-4236.html','Trans Atlantic Diesels (Perkins 4.236)') + '.'
])}

  <h3>The reference fleet below the cockpit</h3>
{compare('Engines and drives on the reference boats', ['', 'Engine as built', 'Cooling', 'Drive and gearbox', 'Fuel tank', 'Spares and known issues'], [
  ['Moody 33', 'Thornycroft T90, a marinised BMC 1.5 four-cylinder, 35 hp (26 kW); a T80 on some Mk IIs is claimed by one site {ONE}', 'heat exchanger', 'shaft; TMP gearbox on one original engine {TWO}', '91 or 144 L {TWO}', 'BMC parts still widely available in the UK; rusting sump, tight access, mount bolts rusted into the wooden beds {TWO}'],
  ['Sadler 32', 'Watermota Sea Panther 30 hp to about 1982; Bukh DV20 (two-cylinder, 20 hp) to about 1986; then Volvo Penta 2002 (two-cylinder, 18 hp)', 'raw water on most Bukh and Volvo 2002 engines; heat exchanger on some', 'shaft; Volvo 2002 with the MS2B gearbox', '40 to 85 L on individual boats {TWO}', 'Watermota: one main specialist; Bukh and Volvo well supported; packed gland early, Halyard oil-fed gland from about 1982 {TWO}'],
  ['Bavaria 1060', 'Volvo Penta 2003, three-cylinder, 28 hp, on the boats found; an 18 hp saildrive package, probably a Volvo 2002, is also quoted {TWO}', '{TBC}', 'saildrive (Volvo 120S) on every boat found {TWO}', '80 or 100 L {TWO}', 'parts available; diaphragm age; heat exchanger mounting can break {TWO}'],
  ['Gib’Sea 31', 'not found: a Renault-Couach 17 hp and Yanmars of 27 and 30 hp on individual boats {TWO}', '{TBC}', '{TBC}', '61 L {ONE}', '{TBC}'],
  ['Gib’Sea 33 (2002)', 'Volvo Penta MD2020, two-cylinder, 18 to 19 hp, on most listings; a Yanmar 3GM30 and Volvos of 29 to 34 hp on others {TWO}', '{TBC}', 'saildrive on one boat, shaft on others {TBC}', '70 to 95 L {TWO}', 'parts available'],
  ['Finnsailer 35', 'Perkins 4.236 four-cylinder, quoted at 72 or 75 hp (the rating depends on the duty, how hard and how long it is expected to run) {TWO}', 'heat exchanger {TWO}', 'shaft; hydraulic reduction gearbox; three-blade propeller {TWO}', '300 to 450 L quoted, steel {TWO}', 'over two million 4.236s built; parts still found, some getting scarce {TWO}'],
], wide=True, stack=True)}
{sources('the fleet', [
  'Moody 33: ' + a('https://www.yachtsnet.co.uk/archives/moody-33/moody-33.htm','Yachtsnet archive') + ', ' + a('https://sailboatdata.com/sailboat/moody-33s/','sailboatdata (33S)') + ', ' + a('https://www.asap-supplies.com/engine-spares-by-model/thornycroft/90','ASAP Supplies') + ', ' + a('https://www.moodyowners.info/threads/thornycroft-t90.25896/','Moody Owners (the TMP gearbox)') + ', ' + a('https://forums.ybw.com/threads/thornycroft-38hb-t90.255630/','YBW on the T90') + ' (anecdotal).',
  'Sadler 32: ' + a('https://www.lucasyachting.co.uk/sadler-and-starlight/sadler-32-yacht/','Lucas Yachting') + ', ' + a('https://www.sailboat-cruising.com/Sadler-32.html','sailboat-cruising.com') + ', ' + a('https://www.asap-supplies.com/engine-spares-by-model/volvo-penta/2001-2002-2003-2003t-series/2002','ASAP on the Volvo 2002') + ', ' + a('https://www.manualslib.com/manual/1000932/Bukh-Dv10.html?page=178','the Bukh DV10/DV20 manual') + '; tanks from individual listings.',
  'Bavaria 1060: ' + a('https://www.boats.com/sailing-boats/1985-bavaria-bavaria-1060-9991645/','boats.com') + ', ' + a('https://esailing.nl/en/boats/sold-boats/999/bavaria-1060','eSailing') + ', ' + a('https://sailboatdata.com/sailboat/bavaria-1060/','sailboatdata') + '. Gib’Sea 31: ' + a('https://poole.boatshed.com/gib_sea_31-boat-22156.html','Boatshed') + ', ' + a('https://www.rightboat.com/boats-for-sale/gib-sea/31/rb529420','Rightboat') + ' (one boat each). Gib’Sea 33: ' + a('https://www.boats.com/sailing-boats/2002-gib-sea-33-9624245/','boats.com') + ', ' + a('https://www.yachtall.com/en/boat/dufour-gib-sea-33-s302454','Yachtall') + ', ' + a('https://www.parker-adams.co.uk/gibsea-33/','Parker Adams') + '.',
  'Finnsailer 35: ' + a('https://larochelle.boatshed.com/finnsailer_35-boat-334110.html','Boatshed La Rochelle') + ', ' + a('https://sailboatdata.com/sailboat/finnsailer-35/','sailboatdata') + ', ' + a('https://forums.ybw.com/threads/perkins-4-236-81-73-or-50-hp.419780/','YBW on 4.236 ratings') + ' (anecdotal), ' + a('https://en.wikipedia.org/wiki/Perkins_4.236','Perkins 4.236 (Wikipedia)') + '.'
])}

  <h3 id="engine--checklist">The engine in one hour: a buyer’s checklist</h3>
  <ol>
    <li><strong>Cold start.</strong> Ask for the engine not to be run before you arrive; feel it is cold, then watch it start. Smoke that clears in a minute is normal.</li>
    <li><strong>Water at the exhaust</strong> within a few seconds of starting, and no alarm lights.</li>
    <li><strong>Dipstick and coolant.</strong> Oil black is normal in a diesel, but not milky or grey, and not smelling of diesel; coolant clean, not rusty, at the right level.</li>
    <li><strong>Fuel.</strong> Look in the primary filter bowl for water and black slime; ask when the tank was cleaned.</li>
    <li><strong>Underneath.</strong> Torch under the engine: oil, diesel, coolant or rust in the drip tray and bilge; the state of the mounts.</li>
    <li><strong>The sea-water side.</strong> The strainer, the impeller’s age, the exhaust elbow for weeping rust, the waterlock and the anti-siphon valve.</li>
    <li><strong>Drive.</strong> Stern gland and its hose clips, or the saildrive diaphragm date on an invoice; cutless bearing and propeller on the hard.</li>
    <li><strong>Under way.</strong> Full revs in ahead for a few minutes: it should reach the rated revs without black smoke or overheating. Astern firmly. No vibration at any speed.</li>
    <li><strong>Paperwork.</strong> Engine hours, service invoices, a manual on board; for an old engine, the price of an impeller, a filter set and a gasket kit.</li>
    <li><strong>Then the engineer.</strong> An oil analysis and a compression test tell you more about a forty-year-old engine than anything you can see.</li>
  </ol>

  <h3>Worth watching</h3>
{videos([
 ('maX1ZkfUNbU', 'RYA Competent Crew: daily engine checks (WOBBLE)', 'First Class Sailing', 'The daily check on this page, as a sea school teaches it on its Competent Crew course.'),
 ('-sMh3MZLEvw', 'How to check and change a marine diesel water impeller', 'Yachting Monthly', 'The impeller job from the cooling card: getting the old one out, what missing vanes look like, and fitting the new one.'),
 ('DyIfCmjDB2Q', 'Diesel fuel systems, part 2: bleeding the system', 'Motor Boat & Yachting', 'Getting the air out after a filter change or running the tank dry: the job that revives most engines that will not start.'),
 ('6cPRVzIXDbM', 'Bleeding a marine diesel engine', 'BoatUS', 'A second, American, walk through the same job. The idea is the same on every engine; the order of the bleed screws is in your engine’s manual.'),
 ('KWMAHEdL-B0', 'How to check your marine diesel engine: RYA diesel yacht engine training', 'Halcyon Yachts - International Yacht Delivery', 'A longer check from a yacht delivery company, in the style of the RYA diesel engine course.'),
 ('D8nkoGnmLU8', 'Penta 120S saildrive: how the inner gear selector operates', 'magnumxs1100', 'Inside a Volvo Penta 120S saildrive, and what the cone clutch does when you move the lever.'),
])}

  <h3>Terms used in this section</h3>
  <h4 class="terms__group">The engine</h4>
{terms([
 ("engine-block","Engine block","The main casting of the engine, holding the cylinders and crankshaft. On an indirectly cooled engine the coolant flows through passages inside it."),
 ("sump","Sump","The oil pan at the bottom of the engine. The oil lives here; the dipstick reads its level."),
 ("dipstick","Dipstick","A steel rod reaching into the sump; pulled out and wiped, it shows the oil level between two marks. Check it cold and level, every day you use the engine."),
 ("oil-filler","Oil filler cap","The cap on the rocker cover where oil is added. Fill a little at a time and recheck the dipstick: too much is as bad as too little."),
 ("oil-filter","Oil filter","A spin-on canister that cleans the oil; changed with the oil."),
 ("air-intake","Air intake and filter","Where the engine breathes. A choked air filter gives black smoke and lost power."),
 ("injectors","Injectors","Nozzles in the cylinder head that spray fuel into each cylinder as a fine mist, at very high pressure."),
 ("starter-motor","Starter motor","The electric motor that spins the engine until it fires. Slow cranking is nearly always the battery or its cables, not the starter."),
 ("alternator","Alternator","The engine’s generator, driven by the belt; it charges the batteries while the engine runs."),
 ("drive-belt","Drive belt","The rubber belt from the crankshaft pulley to the alternator and, usually, the coolant pump. Loose, it squeals and charges poorly; worn, it breaks. Carry a spare."),
 ("stop-control","Stop control","The lever on the injection pump that cuts the fuel off, worked by a pull knob at the helm (out to stop, back in to run) or by a solenoid from a stop button or the key."),
 ("engine-mounts","Engine mounts","Rubber blocks between the engine’s feet and its bed that stop vibration reaching the hull. They sag, crack and soften in diesel."),
])}
  <h4 class="terms__group">Cooling and exhaust</h4>
{terms([
 ("cool-seacock","Engine seacock","The valve on the cooling-water intake in the bottom of the boat. Open before starting, closed when leaving the boat."),
 ("strainer","Raw-water strainer","A jar with a basket that catches weed and debris before the pump. The W of WOBBLE, the daily engine check."),
 ("impeller-pump","Raw-water pump and impeller","A belt- or gear-driven pump whose rubber impeller pushes sea water through the cooling system. Change the impeller every year; it dies quickly if run dry."),
 ("heat-exchanger","Heat exchanger","A tube bundle where the sea water, in the tubes, takes heat from the coolant around them. It blocks with scale and impeller debris."),
 ("header-tank","Header tank and coolant cap","The coolant filler, usually on top of the heat exchanger, with a pressure cap. Check the level cold; never open it hot."),
 ("thermostat","Thermostat","A valve that keeps the coolant in the engine until it is warm, then lets it through the heat exchanger. Stuck shut, the engine overheats; stuck open, it runs cold."),
 ("anti-siphon","Anti-siphon valve","A valve at the top of a loop in the raw-water hose that lets air in when the engine stops, so the sea cannot siphon into the exhaust and the engine. Needed when the injection point is near or below the waterline."),
 ("mixing-elbow","Exhaust (mixing) elbow","The bend where sea water is sprayed into the hot exhaust. It corrodes and chokes with carbon from the inside; a routine replacement on older engines."),
 ("waterlock","Waterlock","A box low in the exhaust run that holds the water in the hose when the engine stops, so it cannot run back into the engine."),
 ("exhaust-loop","High loop (gooseneck)","A loop in the exhaust hose high under the deck, which stops following seas driving water back up the exhaust."),
 ("exhaust-outlet","Exhaust outlet","Where the exhaust and cooling water leave the boat, usually in the transom. Look for water here every time you start."),
 ("hydrolock","Hydrolock","Water in a cylinder: it does not compress, so the engine stops with a thud or breaks. Usually caused by cranking too long, or by siphoning."),
])}
  <h4 class="terms__group">Fuel</h4>
{terms([
 ("fuel-tank","Fuel tank","Steel, aluminium or plastic, under a cockpit locker or berth. Water and sludge collect in its bottom."),
 ("tank-sludge","Water and sludge","What settles in the bottom of an old tank: water, rust and diesel bug. Heavy weather stirs it into the filters."),
 ("fuel-filler","Fuel filler","The deck cap you fill through. Its seal keeps rain and spray out of the tank; do not confuse it with the water filler."),
 ("tank-vent","Tank vent","A small pipe from the tank to a swan-neck outlet on the hull side, letting air in as fuel is used. Blocked, the engine starves; badly placed, it lets sea water in."),
 ("fuel-pickup","Pickup","The pipe inside the tank that draws fuel, ending a little above the bottom so it misses the water and sludge, until a rough sea stirs them up."),
 ("fuel-shutoff","Fuel shut-off valve","A valve at or near the tank that cuts the fuel off, for filter changes and in a fire."),
 ("primary-filter","Primary filter and water separator","The first filter after the tank, usually with a clear bowl in which water settles and can be drained. Not a bleed point for the priming lever: after changing it, fill its bowl with clean fuel."),
 ("lift-pump","Lift pump","A small pump on the engine that draws fuel from the tank and pushes it through the filters. Its hand priming lever is how you bleed the system."),
 ("engine-filter","Engine fuel filter","The fine filter on the engine before the injection pump. Bleed point 1."),
 ("injection-pump","Injection pump","Raises the fuel to very high pressure and sends it to each injector in turn. The throttle and stop levers are on it. Bleed point 2; specialist work beyond that."),
 ("hp-pipes","High-pressure pipes","Steel pipes from the injection pump to the injectors. Never loosen them with the engine running: the fuel is at a pressure that can pierce skin. Cracked open at the injector while the engine is cranked, and only if it still will not start, they are the last bleed point (see bleeding the engine, above)."),
 ("leak-off","Return (leak-off) line","A small pipe that carries the fuel the injectors did not use back to the tank."),
 ("diesel-bug","Diesel bug","Bacteria, moulds and yeasts that grow where water meets diesel in a tank, forming a slime that blocks filters."),
 ("fame","FAME (biodiesel)","Fatty acid methyl ester, blended into road diesel: up to 7 % under the European EN 590 standard (B7). It attracts water and feeds diesel bug."),
])}
  <h4 class="terms__group">Drivetrain and propellers</h4>
{terms([
 ("gearbox","Gearbox","Bolted behind the engine: ahead, neutral and astern, usually with a reduction. Worked by a cable from the cockpit lever."),
 ("gear-cable","Gear cable","The push-pull cable from the cockpit lever to the gearbox. A stretched or loose cable gives a gearbox that will not fully engage."),
 ("shaft-coupling","Shaft coupling","The joint between the gearbox and the shaft, often a flexible one. Alignment is checked here."),
 ("prop-shaft","Propeller shaft","The stainless or bronze shaft from the coupling, through the stern gland, to the propeller."),
 ("shaft-gland","Stern gland","The seal where the shaft leaves the hull: a packed stuffing box, a face seal or a lip seal. The full card is above."),
 ("cutless","Cutless bearing and P-bracket","A rubber-lined, water-lubricated bearing near the propeller, carried in a bronze strut (the P-bracket). Play here means a new one."),
 ("propeller-en","Propeller","Pushes the boat by screwing through the water; described by diameter and pitch, in inches. Fixed, folding or feathering."),
 ("en-rudder","Rudder","The blade that steers; the Hull, keel and rudder section covers it."),
 ("sd-leg","Saildrive leg","An aluminium leg with the gearbox and a right-angle drive, bolted under the engine and through the hull."),
 ("sd-diaphragm","Saildrive diaphragm","The thick rubber seal between the saildrive leg and the hull. Volvo Penta says renew it every seven years."),
 ("sd-anode","Saildrive anode","A block or ring of a more easily corroded metal on the leg, which corrodes so the aluminium leg does not. Renew before it is half gone."),
 ("gland-hose","Gland hose and clips","The short, reinforced rubber hose that joins the stern gland to the stern tube, with two stainless clips at each end. It is below the waterline."),
 ("packing","Packing","Rings of greased flax or PTFE squeezed round the shaft in a stuffing box. Renewed a ring or two at a time."),
 ("follower","Follower","The part of a stuffing box that the nuts tighten to squeeze the packing. A little at a time, and never so tight the gland runs hot."),
 ("gland-drip","Gland drip","The slow drip of a packed gland while the shaft turns, which lubricates and cools the packing."),
 ("bellows","Bellows","The rubber tube in a face seal, compressed so it presses the carbon ring against the collar. It ages, and its maker gives it a life."),
 ("carbon-face","Carbon ring","The stationary ring in a face seal; the collar spins against it and the water between them lubricates it."),
 ("seal-collar","Stainless collar","The ring screwed to the shaft in a face seal. If it slips, the seal opens."),
 ("lip-seal","Lip seal","A rubber sleeve on the stern tube with lips running on the shaft, as fitted by Volvo. Burp it after launch."),
 ("seal-grease","Seal grease","The water-resistant grease packed between the lips of a lip seal."),
 ("prop-fixed","Fixed propeller","Blades fixed in position: cheap, strong and the most drag under sail."),
 ("prop-folding","Folding propeller","Blades hinged so that they fold shut behind the hub when sailing and swing open when the shaft turns."),
 ("prop-feathering","Feathering propeller","Blades that turn edge-on to the water when sailing and reverse their pitch for astern."),
 ("prop-walk","Prop walk","The sideways kick of the stern in astern, caused by the propeller. A right-handed propeller walks the stern to port."),
])}
  <h4 class="terms__group">Other words used here</h4>
{terms([
 ("stern-tube","Stern tube","The tube moulded into the hull that the propeller shaft runs through; the stern gland is clamped to its inner end."),
 ("engine-bed","Engine bed","The two strong rails built into the hull that the engine mounts are bolted to."),
 ("o-ring","O-ring","A rubber sealing ring, round in section. Renewed whenever the joint it seals is opened."),
 ("tube-stack","Tube stack","The bundle of small tubes inside a heat exchanger that the sea water runs through."),
 ("sender","Sender","A small sensor screwed into the engine that tells the panel the oil pressure or the temperature."),
 ("solenoid","Solenoid","An electric switch that moves something: a stop lever, the starter’s engagement, a gas valve."),
 ("diode","Diode","A one-way valve for electricity. The alternator has several; switching the battery off with the engine running can destroy them."),
 ("spline","Spline","A shaft with ridges along it that fits a grooved hole, so the two turn together."),
 ("cone-clutch","Cone clutch","A gearbox clutch in which a cone is pressed into a matching cup; used by Volvo MS and Kanzaki boxes. Shift firmly, at tick-over."),
 ("hypoid-oil","Hypoid oil","A thick gear oil (grades such as 80W-90) used in gearboxes and the Sadler’s oil-fed stern gland."),
 ("ptfe","PTFE","A slippery plastic (the coating on non-stick pans), used for stern-gland packing and tape."),
 ("seaway","Seaway","Rough water with waves: “in a seaway” means with the boat moving about."),
 ("duty-rating","Duty rating","How hard and how long an engine is rated to run; the same engine is sold at different horsepowers for different duties."),
 ("compression-test","Compression test","A gauge screwed into each cylinder in turn to measure how well it seals; low or uneven readings mean wear."),
 ("oil-analysis","Oil analysis","A laboratory test of an oil sample that shows wear metals, fuel, soot or coolant in the oil."),
])}

  <div class="planned">
    <p>Planned for this section</p>
    <ul>
      <li>Photographs of faults: an impeller with missing vanes, a corroded exhaust elbow, a worn cutless bearing, a corroded saildrive leg (still to be found under a CC licence)</li>
      <li>Factory engine, drive and tank figures for the Gib’Sea 31 and Gib’Sea 33, and the Moody 33’s original gearbox and gland</li>
      <li>A current published price for a Beta Marine engine</li>
    </ul>
  </div>
</section>
'''
finish(page, ROOT + 'sections/06-engine.html', others=(ROOT + 'sections/03-hull.html', ROOT + 'sections/04-rig.html', ROOT + 'sections/05-deck.html', ROOT + 'sections/02-fleet.html', ROOT + 'sections/00-start.html'))
