# Generates sections/14-buying.html for Sailing 101.
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_common import *
import gen_buying_diagrams as g


page = f'''<section id="buying">
  <h2>Buying and owning</h2>
  <p class="lead">A 30-year-old boat can be a bargain or a hole in the water. The difference is usually visible before you buy, if you know where to look, and the running costs are predictable if you are honest about them. Every part of the boat mentioned here has its own section, with what goes wrong: this one pulls them together into a viewing, a survey, a purchase and a first season. Jump to <a href="#buying--viewing">the viewing</a>, <a href="#buying--survey">the survey</a>, <a href="#buying--purchase">the purchase</a>, <a href="#buying--abroad">buying abroad</a>, <a href="#buying--costs">running costs</a> or <a href="#buying--first-season">the first season</a>.</p>

  <details class="first-words" open>
    <summary>Five words before anything else</summary>
    <dl>
      <dt>Survey</dt><dd>An inspection of the boat by a qualified, independent surveyor, out of the water, before you buy.</dd>
      <dt>Sea trial</dt><dd>A sail and motor to test the boat before the sale completes.</dd>
      <dt>Broker</dt><dd>An agent who sells boats for their owners; paid by the seller.</dd>
      <dt>Bill of sale</dt><dd>The document that transfers ownership of the boat.</dd>
      <dt>VAT-paid</dt><dd>A boat on which VAT has been paid, or that counts as paid; it can be kept in the EU without paying again.</dd>
    </dl>
  </details>
  <p class="conf-key"><b>Marks used below:</b> {ONE} single source; {TWO} sources disagree or anecdotal; {TBC} not yet verified. <b>How this section was checked:</b> in September 2026 by web search against the pages linked under “Sources and confidence”; the search results were read, but the pages themselves could not be opened from the editing session. Replacement intervals are rules of thumb.</p>

  <h3>Before you look at boats</h3>
  <ul>
    <li><strong>Decide what the boat is for:</strong> weekends from a marina, a summer cruise, living aboard, crossing seas. That decides the keel (a bilge keel for drying harbours, a fin for performance, a long keel for sea-kindliness), the cockpit, the heating and the budget. The <a href="#fleet">reference fleet</a> shows the range.</li>
    <li><strong>Sail on a few.</strong> Charter, crew for someone, or do a course on a similar boat. An afternoon at sea tells you more than a brochure.</li>
    <li><strong>Budget three things:</strong> the price; the first year’s catching up, which on an older boat is often a real fraction of the price {TWO}; and the running costs below. The cheapest boat is rarely the cheapest to own.</li>
    <li><strong>Where it will live</strong> decides much of the cost: find the berth, and its price, before the boat.</li>
  </ul>

  <h3 id="buying--viewing">Viewing a boat</h3>
{figure('fig-inspection', 'where to look', '0 0 900 450', 'Where to look when viewing a used yacht', 'A side view of a yacht, bow to the right, with twelve numbered points, matching the numbered list below the drawing: the hull below the waterline; the keel joint and keel bolts; the rudder; the stern gland or saildrive seal; the seacocks and hoses; the chainplates; the deck; the mast step and the post under it; the standing rigging; the sails; the engine; and below decks, for stains, wiring, batteries and gas.', g.inspection(), 'A first viewing is to decide whether a boat is worth a survey, not to replace one. Take a torch, a notebook, old clothes, and someone who knows boats. The numbers match the list below.', note=HINT)}
  <ol>
    <li><strong>Hull below the waterline</strong> (out of the water, or ask for a lift): blisters (see <a href="#hull--osmosis">osmosis</a>), old repairs, a wavy surface where the hull has been filled and faired. Moisture readings are for the surveyor.</li>
    <li><strong>Keel joint:</strong> a thin crack along the front of the joint between keel and hull (the “smile”) can be only filler, or the sign of a grounding. Inside, look at the keel bolts and the floors (the frames they pass through) for rust, weeping and cracks.</li>
    <li><strong>Rudder:</strong> grip the bottom and shake it: any clunk is wear in the bearings. Water weeping from the blade after lifting out means water inside.</li>
    <li><strong>Stern gland or saildrive:</strong> drips, corrosion, and the age of the saildrive’s rubber seal, which Volvo Penta asks to be replaced every seven years (many owners go longer {TWO}).</li>
    <li><strong>Seacocks and hoses:</strong> every one should turn; look for green or pink corrosion on bronze and brass, and two clips on every hose below the waterline.</li>
    <li><strong>Chainplates:</strong> rust stains, leaks and soft deck where they pass through; inside, the bulkheads or knees they are bolted to.</li>
    <li><strong>Deck:</strong> walk every part of it. A soft or springy area means the core under the skin is wet; tap it with a coin or a screwdriver handle: a dull sound instead of a sharp one means trouble. Crazing round fittings and stanchions can mean leaks.</li>
    <li><strong>Mast step:</strong> on a deck-stepped mast, a sagging deck around it, or a crushed or rotten post below, are serious.</li>
    <li><strong>Standing rigging:</strong> ask its age. Look for cracks in the swaged terminals, broken strands and rust. Many surveyors and insurers ask for rigging older than about ten years to be replaced, though insurers vary.</li>
    <li><strong>Sails:</strong> unroll them. Look for cloth that feels papery or chalky with sun damage, stretched and baggy shape, failed stitching and the UV strip on a furling genoa; ask before handling a seller’s sails roughly.</li>
    <li><strong>Engine:</strong> ask for it to be cold when you arrive, and start it yourself. It should start in seconds and settle; watch the exhaust for smoke and water (see <a href="#engine--faults">engine faults</a>), look for oil in the bilge, cracked mounts, and ask for the service history.</li>
    <li><strong>Below:</strong> stains on the headlining and lockers show old leaks; smell for damp, diesel and sewage. Look at the wiring behind the switch panel, the batteries’ dates, and the gas installation (see <a href="#systems">Boat systems</a>).</li>
  </ol>
  <p><a href="print/viewing-checklist.html">A printable viewing checklist</a> puts these twelve points and every section’s buyer’s checklist (hull, rig, deck, engine, systems, electronics) in one document to take to the boat.</p>
  <p><strong>Also look at:</strong> the hull-to-deck joint, inside and out, for leaks and cracks (see <a href="#hull">Hull</a>); the steering, turning the wheel or tiller from lock to lock for stiffness and play (see <a href="#deck">Deck</a>); the windows and hatches for crazing and leaks; the fuel tank, for rust on a steel one and water or diesel bug in a sample from the bottom (see <a href="#engine">Engine</a>); the date printed on the gas hose; on a keel-stepped mast, the heel of the mast and the step in the bilge, for corrosion; the internal grid or floors, for cracks where they meet the hull; the exhaust elbow, for rust and weeping; and the cutless bearing, by pushing the propeller sideways to feel for play. Check that the hull identification number on the transom matches the papers, and on a boat placed on the EU market since mid-1998 ask for the declaration of conformity that comes with the CE mark.</p>

  <h3 id="buying--survey">The survey</h3>
  <p>For a boat of this age, always: out of the water, by a surveyor you choose, who is not connected to the broker or the seller. The survey is also your negotiating document and your first year’s job list.</p>
  <ul>
    <li><strong>What it covers:</strong> the hull and deck, with moisture readings; the keel, rudder and steering; the seacocks and through-hulls; the deck fittings and chainplates; the systems and safety equipment. The engine and the rig are often only looked at, not tested: ask for a separate engine survey and a rigger’s inspection if it matters.</li>
    <li><strong>Insurers</strong> often ask for a survey for a boat of this age before they will insure it, and may make its recommendations conditions of cover.</li>
    <li><strong>A sea trial</strong> goes with it: the engine under load, the sails, the steering, the instruments, and everything that pumps.</li>
    <li><strong>Read the report as a price list.</strong> The serious items (structure, keel, rudder, rigging, engine) are for negotiation or walking away; the long list of small items is normal on any old boat.</li>
  </ul>

  <h3 id="buying--purchase">Making the purchase</h3>
  <ol>
    <li><strong>An offer subject to survey and sea trial,</strong> with a deposit, usually 10%, on the standard ABYA contract used by most UK brokers, held by the broker in a client account.</li>
    <li><strong>The survey,</strong> then a renegotiation if it finds something serious.</li>
    <li><strong>Title:</strong> check that the seller owns the boat outright, with no loan secured on it; ask for the bill of sale chain and, where the boat is on Part 1 of the UK register, a current transcript of registry, which shows the owner and any mortgage.</li>
    <li><strong>VAT evidence</strong> and the registration papers (see <a href="#licences--papers">the boat’s papers</a>).</li>
    <li><strong>Completion:</strong> the balance paid, a signed bill of sale, and the keys. Insurance from the moment you own it; register the boat and the radio licence in your name.</li>
  </ol>
{card('buying--private-or-broker', 'Broker, private sale or auction', 'yacht broker, private seller, salvage auction', 'Most boats of this class are sold through yacht brokers, some privately, and a few at auction.',
  ['A broker acts for the seller and is paid a commission by them; a good one handles the paperwork, holds the deposit safely and knows the boat’s history.'],
  ['A private sale can be cheaper, and the seller is the best source of the boat’s story.'],
  ['In a private sale you do the paperwork yourself, and the deposit and the title checks are your risk. An auction or salvage boat is sold as seen, usually without a survey.'],
  ['A seller who will not allow a survey or a lift-out; missing papers; a price well below similar boats.'],
  ['Whatever the route: a written agreement, an independent survey, and the papers checked before the money moves.'], fold=True)}

  <h3 id="buying--abroad">Buying abroad</h3>
  <ul>
    <li><strong>VAT:</strong> within the EU, a boat on which VAT has been paid in one member state can usually move to another without paying again, with the evidence to prove it. For older boats, one rule matters for the whole reference fleet: a boat that was in the EU before 1985 and still there at the start of 1993 is generally treated as VAT-paid, if you can prove its history; for countries that joined later the dates differ: for Finland, Sweden and Austria, in use before 1987 and in the EU at the end of 1994. A boat brought into the EU from outside, including from the UK since 2021, is imported: VAT and possibly duty are due, unless it qualifies for relief or temporary admission (up to 18 months for a non-EU boat of a non-EU resident).</li>
    <li><strong>The Recreational Craft Directive</strong> (not to be confused with the residual current device of the electrics): boats placed on the EU market since mid-1998 must carry the CE mark and a design category (A: beyond force 8 and 4 m waves; B: up to force 8 and 4 m; C: up to force 6 and 2 m; D: up to force 4 and 0.3 m). An older boat already in the EU is not affected; importing a boat that was never on the EU market can require a post-construction assessment.</li>
    <li><strong>Registration and flag:</strong> the boat takes the flag of your country, or keeps its old flag if the law allows it; the old registration is closed and the radio licence re-issued; if the flag changes, the boat also gets a new MMSI, and the DSC radio, the AIS and the EPIRB are reprogrammed and re-registered (see <a href="#licences--radio">Radio</a>).</li>
    <li><strong>Getting it home:</strong> sail it (a delivery crew, or a good first passage), or truck it. In much of Europe a load wider than 2.55 m needs a special permit, and wider ones an escort on many roads.</li>
  </ul>
{sources('buying', [
  'Viewing and survey: ' + a('https://www.practical-sailor.com/sailboat-reviews/used_sailboats/diy-survey-checklist-for-used-boat-buying/','Practical Sailor, DIY survey checklist') + ', ' + a('https://www.yachtworld.com/research/pre-purchase-yacht-surveys-need-know/','YachtWorld, pre-purchase surveys') + '; rigging age: ' + a('https://www.noonsite.com/report/when-to-replace-your-standing-rigging/','Noonsite, when to replace standing rigging') + '; saildrive seal: ' + a('https://www.pbo.co.uk/expert-advice/expert-answers/volvo-saildrive-seal-replacement-how-often-70454','Practical Boat Owner') + '; seacocks: ' + a('https://www.pbo.co.uk/gear/dezincification-resistant-dzr-skin-fittings-explained-97302','Practical Boat Owner, DZR fittings') + '; gas hose: ' + a('https://www.boatsafetyscheme.org/requirements-examinations-and-certification/non-private-boat-standards/part-7-lpg-installations/flexible-hose/','Boat Safety Scheme, flexible hose') + '.',
  'Purchase: ' + a('https://abya.co.uk/buying-a-boat/','ABYA, buying a boat') + ', ' + a('https://oceanskies.com/guide/the-uk-ship-register-part-i-v-uk-small-ships-register-ssr-part-iii/','Oceanskies, Part 1 and the SSR') + '.',
  'VAT and the RCD: ' + a('https://keystonelaw.com/keynotes/the-vat-problem-top-tips-for-yacht-buyers-and-owners/','Keystone Law, the VAT problem') + ', ' + a('https://www.boatshedsupport.com/article/12-vat-evidence','Boatshed, evidence of VAT status') + ', ' + a('https://oceanskies.com/guide/temporary-admission-temporary-importation-for-yachts-in-europe/','Oceanskies, temporary admission') + ', ' + a('https://en.wikipedia.org/wiki/Recreational_Craft_Directive','Wikipedia, Recreational Craft Directive') + ', ' + a('https://help.beneteau.com/hc/en-us/articles/360019581178-How-do-I-interpret-design-categories','Beneteau, design categories') + '; road transport: ' + a('https://www.sea-help.eu/en/guide/boat-trailer-regulationsr-part-2/','SeaHelp, trailer rules') + '.',
  'Checked by web search, September 2026; the pages could not be opened directly.',
])}

  <h3 id="buying--costs">Running costs</h3>
  <p>A common rule of thumb says that a boat costs about a tenth of its value a year to keep {TWO}; for an old, cheap boat the berth alone can cost more than that. List them honestly:</p>
  <ul>
    <li><strong>The berth:</strong> usually the biggest cost, and it varies hugely between countries, regions and marinas; a swinging mooring or a drying berth costs much less than a marina pontoon.</li>
    <li><strong>Insurance:</strong> third-party cover at least, often compulsory, and hull cover for the boat itself.</li>
    <li><strong>The annual lift-out:</strong> crane or travel-hoist, pressure wash, antifouling and anodes, and winter storage ashore where the season is short.</li>
    <li><strong>Maintenance:</strong> the engine service, and the replacements on a cycle below.</li>
    <li><strong>The unplanned item,</strong> every year.</li>
  </ul>
  <p>No one publishes national average prices for berths or yard work, so here are real examples: each marina’s or harbour’s own published tariff, for the dates given, with VAT included unless marked. They are one place each, not averages; the difference between them is the point. Marinas charge on the length overall, including the pulpit, a bowsprit or davits, and some on length times beam.</p>
{compare('Published tariffs for a boat of about 10&nbsp;m, 2026', ['Place', 'What', 'Price', 'Valid'], [
  ['Swanwick Marina, Hamble (Solent, UK)', 'marina berth, a year', '£995 a metre from 8.1 to 10 m, £1,055 from 10.1 to 12 m: about £9,550 for a 9.6 m boat, £11,200 for 10.6 m', '1 Oct 2026 to 30 Sep 2027'],
  ['Port Hamble (Solent, UK)', 'marina berth, a month', '£124.20 a metre up to 10 m, £150.60 over 10 m: about £1,240 a month for 10 m, some £14,900 over twelve months; a year’s berth by quote', 'to 31 Mar 2027'],
  ['Torquay harbour (Devon, UK)', 'harbour pontoon, a year', '£3,258 up to 10 m, £3,910 up to 12 m, with harbour dues (VAT not stated)', 'proposed for 2026/27'],
  ['Torquay harbour (Devon, UK)', 'swinging mooring, a year', '£1,724 up to 10 m, £1,906 up to 11 m', 'proposed for 2026/27'],
  ['Swanwick Marina', 'lift out, wash, up to 10 days ashore and relaunch', '£75 a metre from 9.1 to 12 m: about £750 for 10 m', 'from 1 Sep 2026'],
  ['La Rochelle (France)', 'marina berth, a year', 'charged on length × beam: about €3,000 to €3,400 for the boats of the reference fleet (€3,415 for a 10.06 × 3.48 m boat); waiting lists', '2026'],
  ['La Rochelle', 'travel-hoist out and back in within 24 hours', '€299.50 up to 5 t, €352 from 5 to 7.5 t; half price from October to February', '2026'],
  ['Kiel city marinas (Germany)', 'berth for the summer, 15 March to 14 November', '€49.50 a square metre of length × beam: about €1,730 for a 10 × 3.5 m boat', 'summer 2026'],
  ['Kiel city marinas', 'winter ashore outdoors, and the crane', '€15 a square metre (about €525 for the same boat); crane €81 a lift up to 5 t', '2026'],
], wide=True, stack=True)}
  <p>So a year of berth and yard for the same boat costs roughly €2,400 in Kiel and about eleven thousand pounds in a Solent marina. Insurance depends on the boat’s value and age, the waters and the skipper’s experience, and no insurer publishes a price for a boat like these. The last known figures: GJW Direct says its customers paid £440 a year on average (July 2026, across all its yacht policies); owners on a forum in 2015 reported about £180 to £310 a year for 30-foot boats insured for £26,000 to £30,000, with £3 million of third-party cover in home waters {TWO}; Practical Boat Owner reported premiums up 25 to 50 % after 2017 and about 5 to 10 % a year since (March 2024). Third-party cover of £3 to £5 million is usual. For today’s price, get quotes from {a('https://www.gjwdirect.com/yacht-sailing-boat-insurance/','GJW Direct')}, {a('https://www.navandgen.co.uk/','Navigators &amp; General')}, {a('https://www.craftinsure.com/yacht-insurance/','Craftinsure')}, {a('https://www.topsailinsurance.com/boat-insurance/yacht-insurance','Topsail')} or, in Europe, {a('https://www.pantaenius.com/','Pantaenius')}. Antifouling and an engine service have no reliable published figures: ask the yard.</p>
{sources('running costs', [
  'Tariffs, each opened and read in September 2026: ' + a('https://www.premiermarinas.com/media/sr1fkzux/swanwick-berthing.pdf','Swanwick berthing') + ' and ' + a('https://www.premiermarinas.com/media/fpvi0hj2/swanwick-boatyard.pdf','boatyard') + ' (PDF), ' + a('https://www.mdlmarinas.co.uk/_assets/port-hamble-july-2026-tariff.pdf','Port Hamble') + ' (PDF), ' + a('https://www.torbay.gov.uk/DemocraticServices/documents/s166735/2026-27%20Proposed%20Harbour%20Fees%20Charges.pdf','Torbay Council, proposed harbour fees 2026/27') + ' (PDF), ' + a('https://www.portlarochelle.com/en/calculate-your-annual-fee/','Port de La Rochelle, annual fee') + ' and ' + a('https://www.portlarochelle.com/en/prices/hoisting-service/','hoisting') + ', ' + a('https://sporthafen-kiel.de/preise','Sporthafen Kiel, prices') + '. The totals for particular boats are our own arithmetic from the published rates.',
  'Insurance, last known: ' + a('https://www.gjwdirect.com/yacht-sailing-boat-insurance/','GJW Direct, average premium') + ', ' + a('https://forums.ybw.com/threads/insurance-costs-for-a-30-foot-yacht.445747/','YBW, insurance for a 30-foot yacht (2015)') + ' (anecdotal), ' + a('https://www.pbo.co.uk/gear/how-to-find-the-best-boat-insurance-84130','Practical Boat Owner, finding the best boat insurance (2024)') + '.',
  'The rule of thumb: ' + a('https://www.yachttrading.com/yacht-encyclopedia/what-is-the-yacht-10-rule-a-guide-to-yacht-maintenance-costs-910/','Yachttrading, the 10% rule') + ' ² (sources give 7 to 15% depending on size and age).',
])}
{figure('fig-cycles', 'replacement cycles', '0 0 900 596', 'Rules of thumb for how often things wear out on a yacht', 'A chart of bars on a scale of 0 to 25 years. Antifouling and anodes: every year or two. The engine service and impeller: every year. Lead-acid batteries: 3 to 6 years. The gas hose: by the date printed on it, about every 5 years. A saildrive diaphragm: every 7 years. A liferaft service: every 1 to 3 years. Running rigging: 5 to 10 years. Standing rigging: 10 to 15. Sails: 8 to 15. Electronics: 8 to 15. Hoses below the waterline: 8 to 15. Brass seacocks: 5 to 10; bronze or DZR ones 15 to 25. Cushions and upholstery: 10 to 20. An engine rebuild or replacement: 20 to 30 years or more.', g.cycles(), 'Rules of thumb only: a boat that sails hard in the sun wears out faster than one that sits in a northern marina. Use them to ask the right question at a viewing: when was this last replaced?', start=0.22)}

  <h3 id="buying--sharing">Sharing a boat</h3>
  <p>A share in a boat costs a fraction of the price and the bills, and brings crew with it. It works when the partners agree about money, maintenance and time before they buy, and write it down; when it goes wrong, it is usually over one of those three.</p>
  <ul>
    <li><strong>A private syndicate</strong> is the usual form in the UK: the co-owners own shares in the boat itself, under a written syndicate agreement. It sets out each owner’s share; where the boat is kept; who maintains it; how the weeks are divided; how costs, including the unexpected ones, are split; who may skipper the boat, and with what experience, with each skipper named on the insurance; how disputes are settled; and how an owner leaves, usually by offering the share to the others first, who may have a say over a newcomer. The RYA has a template agreement for its members.</li>
    <li><strong>On Part 1 of the UK register</strong> (the Small Ships Register records no ownership), a boat is divided into 64 shares; up to 64 people can be registered as owners, and up to five as joint owners of the whole boat or of any share. These legal shares are separate from what your agreement says each partner pays and uses.</li>
    <li><strong>How many:</strong> four or five owners, with about four weeks each over a summer, is typical for a boat kept in the Mediterranean; ten or twelve is the upper end. With few owners, decisions have to be unanimous; with more, agree which ones (the sailing area, big spending) still need everyone. Keep a separate bank account for the boat, and a contingency fund.</li>
    <li><strong>Tell the insurer</strong> that the boat is shared, and have unequal shares noted on the policy.</li>
    <li><strong>In France,</strong> joint owners are either in <em>indivision</em>, where every decision needs everyone and any owner can force a sale, or in a <em>copropriété de navire</em>: a written contract lodged with customs, decisions by majority, and a manager (<em>gérant</em>), without whom every co-owner is liable without limit.</li>
    <li><strong>In Germany,</strong> an <em>Eignergemeinschaft</em> owns the boat together, and each owner can sell a share; a <em>Haltergemeinschaft</em> shares its use without owning it. Either needs a written contract.</li>
    <li><strong>Managed schemes</strong> are a different product: a company owns or runs the boat and sells shares or weeks in it, or a charter company leases your boat back for some years in return for weeks of use. Read what you own at the end, and what happens if the company fails.</li>
  </ul>
{sources('sharing a boat', [
  a('https://www.rya.org.uk/members-legal-advice/buying-owning/stay-afloat-by-sharing-a-boat/','RYA, sharing a boat') + ', ' + a('https://www.yachtingmonthly.com/cruising/cruising-life/shared-boat-ownership-all-the-fun-at-a-fraction-of-the-cost-100694','Yachting Monthly, shared boat ownership (2025)') + ', ' + a('https://www.legislation.gov.uk/uksi/1993/3138/regulation/2','Merchant Shipping (Registration of Ships) Regulations 1993, reg. 2') + ', ' + a('https://yachtinglawyers.com/boat-syndicates/','Yachting Lawyers, boat syndicates') + ', ' + a('https://www.argusdubateau.fr/actualite/acheter-en-copropriete','Argus du Bateau, buying in co-ownership') + ', ' + a('https://www.sea-help.eu/news-allgemein/halter-eignergemeinschaft-erklaert/','SeaHelp, Halter- and Eignergemeinschaft') + '.',
  'Opened and read in September 2026. This is a summary, not legal advice: have the agreement checked.',
])}

  <h3 id="buying--first-season">The first season: in a sensible order</h3>
  <ol>
    <li><strong>Safety first:</strong> the gas installation checked, the seacocks exercised and every hose clipped, fire extinguishers and a fire blanket, lifejackets serviced, a working bilge pump, the navigation lights.</li>
    <li><strong>The engine:</strong> a full service, a new impeller, fuel filters and belts, and a look at the exhaust elbow and mounts (see <a href="#engine">Engine</a>). Carry the spares.</li>
    <li><strong>The rig:</strong> a rigger’s inspection, and the standing rigging replaced if its age is unknown.</li>
    <li><strong>Electrics:</strong> the batteries tested, the wiring made safe, a battery monitor if there is none.</li>
    <li><strong>Learn the boat:</strong> where every seacock, pump and switch is; its prop walk; how it reefs. Write the boat’s own manual as you go.</li>
    <li><strong>Then comfort:</strong> the cushions, the galley, the heater. They can wait a season; the rest cannot.</li>
  </ol>
  <p>Most of the boats in the reference fleet have an owners’ association or an active forum. Join it before you buy: the members know each model’s weak points, and many boats change hands between them. What each boat of the reference fleet is known for, and what to look for on it, is under “Watch for” in <a href="#fleet">the fleet</a>.</p>

  <h3>Worth watching</h3>
{videos([
 ('F-i1dYYjBNY', 'Osmosis blisters', 'Hamble Marine Surveys Ltd', 'A surveyor on blisters found during a pre-purchase survey, and what they mean.'),
 ('1A6T0aW-R0o', 'This is what a dry boat sounds like… but just wait till you get to the anchor locker', 'practicalboatowner', 'A surveyor sounding a hull with a hammer and checking it with a moisture meter.'),
 ('bDOFLT0MAJw', 'Inspection checklist: sailboat buyers guide', 'Practical Sailor', 'A viewing checklist from an American boat-testing magazine.'),
 ('F1gUxS1IR4g', 'Buying a used sailboat? A survey could save you thousands', 'Sea Ox Sailing', 'A buyer’s view of a survey, and why it was worth paying for.'),
 ('JUKLiRx9Zgc', 'Boat hull osmosis: to buy or not to buy?', 'BoatBuy', 'How much blisters should change your offer.'),
])}

  <h3>Terms used in this section</h3>
  <h4 class="terms__group">The viewing</h4>
{terms([
 ("by-hull","Hull below the waterline","Where blisters, repairs and damage show: see Hull."),
 ("by-keel","Keel joint and bolts","Where the keel meets the hull, and the bolts that hold it on. A crack at the front of the joint is called the smile."),
 ("by-rudder","Rudder bearings","The bushes the rudder stock turns in; wear shows as play when you shake the blade."),
 ("by-gland","Stern gland or saildrive seal","Where the propeller shaft or the saildrive leg passes through the hull: see Engine."),
 ("by-seacocks","Seacocks and hoses","The valves on the through-hull fittings and the hoses on them: each should turn freely, with two clips on each hose."),
 ("by-chainplates","Chainplates","The metal straps that take the shrouds’ load into the hull; leaks where they pass through the deck rot and rust them."),
 ("by-deck","Deck core","The foam or balsa between the deck’s two skins; when wet it rots and the deck goes soft."),
 ("by-mast-step","Mast step","Where the mast stands on the deck or the keel; on a deck-stepped mast, the post below carries the load."),
 ("by-rigging","Standing rigging","The wires that hold the mast up; ask its age, and look at the swaged ends."),
 ("by-sails","Sails","Look for sun damage, stretch and failed stitching; unroll the genoa."),
 ("by-engine","Engine from cold","A cold start shows problems a warm engine hides."),
 ("by-below","Below decks","Stains, smells, wiring, batteries and the gas installation."),
])}
  <h4 class="terms__group">Replacement cycles</h4>
{terms([
 ("cy-antifouling","Antifouling and anodes","The paint that stops growth on the hull, and the zinc or aluminium blocks that protect metal underwater: renewed every year or two."),
 ("cy-service","Engine service","Oil, filters and the raw-water pump impeller: every season or a set number of hours."),
 ("cy-batteries","Batteries","Lead-acid batteries last about three to six years; less if they are often run flat."),
 ("cy-gas-hose","Gas hose","The flexible hose from the regulator: replaced by the date printed on it, about every five years (for the common Class 1 tubing)."),
 ("cy-saildrive","Saildrive diaphragm","The rubber seal where a saildrive leg passes through the hull: its maker gives a replacement interval, seven years for Volvo Penta."),
 ("cy-safety","Liferaft service","A liferaft is repacked and checked at a service station every one to three years, depending on the maker; lifejackets, flares and fire extinguishers also have dates."),
 ("cy-running","Running rigging","Halyards, sheets and control lines: they chafe and go stiff with sun and salt."),
 ("cy-standing","Standing rigging","Stainless steel wire and terminals fail from inside, often without warning; they are replaced by age."),
 ("cy-sails","Sails","Cruising sails lose shape and strength with sun and use."),
 ("cy-electronics","Electronics","Instruments and plotters age and become impossible to repair or connect."),
 ("cy-hoses","Hoses below the waterline","Hoses harden and crack with age; inspect them every year and replace them on a cycle."),
 ("cy-seacocks-brass","Brass seacocks","Ordinary brass loses its zinc in sea water (dezincification) and can last only about five years."),
 ("cy-seacocks-bronze","Bronze or DZR seacocks","Bronze and dezincification-resistant brass last much longer, but still need exercising and inspection."),
 ("cy-cushions","Cushions and upholstery","Foam flattens and covers fade: comfort, not safety."),
 ("cy-engine","Engine rebuild","A well-kept small diesel runs for thousands of hours; eventually it needs a rebuild or a new engine."),
])}

</section>
'''
finish(page, ROOT + 'sections/14-buying.html', others=(ROOT + 'sections/03-hull.html', ROOT + 'sections/04-rig.html', ROOT + 'sections/05-deck.html', ROOT + 'sections/06-engine.html', ROOT + 'sections/07-systems.html', ROOT + 'sections/08-electronics.html', ROOT + 'sections/09-sailing.html', ROOT + 'sections/10-manoeuvres.html', ROOT + 'sections/11-navigation.html', ROOT + 'sections/12-seas.html', ROOT + 'sections/13-licences.html', ROOT + 'sections/02-fleet.html', ROOT + 'sections/00-start.html'))
