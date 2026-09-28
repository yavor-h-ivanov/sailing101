# Generates sections/13-licences.html for Sailing 101.
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_common import *
import gen_licences_diagrams as g


page = f'''<section id="licences">
  <h2>Licences and qualifications</h2>
  <p class="lead">Whether you legally need a licence depends on the flag of the boat, the waters you are in, and sometimes the size of the engine or the boat. Whether you should get trained does not depend on anything: a week’s course teaches more than a season of trial and error, and makes the trial and error safer. Jump to <a href="#licences--icc">the ICC</a>, <a href="#licences--radio">radio licences</a> or <a href="#licences--papers">the boat’s papers</a>.</p>

  <details class="first-words" open>
    <summary>Five words before anything else</summary>
    <dl>
      <dt>Flag state</dt><dd>The country a boat is registered in; its laws follow the boat.</dd>
      <dt>ICC</dt><dd>The International Certificate of Competence: a certificate of a skipper’s competence that many countries accept.</dd>
      <dt>SRC</dt><dd>The Short Range Certificate: the VHF radio operator’s qualification.</dd>
      <dt>Schengen</dt><dd>The group of European countries with no passport control between them. Not the same as the EU.</dd>
      <dt>Port of entry</dt><dd>A harbour where a boat arriving from abroad can clear customs and immigration.</dd>
    </dl>
  </details>

  <div class="callout warn">
    <span class="callout__title">Rules change and vary by country</span>
    <p>What follows is a map of the landscape, not legal advice. The national rules below were checked against official pages in September 2026 where those could be opened, and each is linked in the sources block; they change, so check each one with the country’s authority, your flag state, and for a charter the charter company, before you rely on it. Anything we could not confirm is marked {TBC}.</p>
  </div>
  <p class="conf-key"><b>Marks used below:</b> {ONE} single source; {TWO} sources disagree or anecdotal; {TBC} not yet verified. <b>How this section was checked:</b> by web search against the pages linked under “Sources and confidence”; the search results were read, but the pages themselves could not be opened from the editing session.</p>

  <h3>Which rules apply to you</h3>
{figure('fig-which-rules', 'which rules apply', '0 0 900 316', 'The three sets of rules a skipper must satisfy', 'Three panels side by side. The boat’s flag: the country it is registered in sets rules on registration papers, the radio licence and MMSI, a skipper’s licence if its law requires one, and safety equipment. The waters you are in: the coastal country adds its own rules for every boat, whatever its flag, on collision rules and speed limits, anchoring and nature reserves, fees, taxes and permits, entry and customs, and holding tanks. The charter company: on a chartered boat, the company and its insurer set their own requirements, often a recognised licence such as the ICC, a radio certificate and an experienced crew member.', g.which_rules(), 'The same skipper on the same boat may need nothing on one side of a border and a licence on the other; and a charter company can ask for more than any law does.', note=HINT)}
  <p>Many countries do not require a licence to sail a private yacht of this size under their own flag, but expect a visiting foreign skipper to hold whatever their own country would require, or a recognised certificate such as the ICC. Others require a licence of everyone in their waters. And almost everywhere, anyone using a marine VHF radio needs an operator’s certificate, and the boat needs a radio licence.</p>

  <h3>Training: the RYA ladder</h3>
  <p>The Royal Yachting Association’s scheme is the best known in Europe, and its certificates are recognised in many countries and by most charter companies {TWO}; other countries have their own (see below). Courses are run by recognised training centres, on their boats or yours.</p>
{figure('fig-ladder', 'training ladder', '0 0 900 380', 'The RYA sail cruising scheme and where the ICC fits', 'A staircase of five boxes: Competent Crew, Day Skipper, Coastal Skipper, Yachtmaster Coastal and Yachtmaster Offshore. Beside Day Skipper and Coastal Skipper are the matching shore-based theory courses. A dashed arrow leads from Day Skipper to the ICC, issued on the Day Skipper practical certificate or on a separate assessment. A note lists the supporting courses: VHF Short Range Certificate, First Aid, Sea Survival, Diesel Engine and Radar.', g.ladder(), 'For an owner of a boat of this class, Day Skipper (theory and practical) plus the VHF certificate is the usual first target, and enough for the ICC.')}
  <ul>
    <li><strong>Competent Crew</strong> (five days afloat): steering, sail handling, ropework and safety; being useful on board. No experience needed; a shorter taster course exists too.</li>
    <li><strong>Day Skipper</strong>: the theory course (in a classroom or online) covers chartwork, tides, the collision rules, weather and safety; the practical course (five days aboard) covers skippering a yacht on short passages by day in waters you know.</li>
    <li><strong>Coastal Skipper</strong>: longer passages, night sailing and more demanding conditions, with its own theory course, shared with the Yachtmaster.</li>
    <li><strong>Yachtmaster Coastal and Offshore</strong> (and, above them, Yachtmaster Ocean, for ocean passages and astronavigation): exams, not courses, with minimum sea time and miles logged; with a commercial endorsement, a Yachtmaster certificate is a professional qualification.</li>
    <li><strong>Supporting courses:</strong> the VHF Short Range Certificate (SRC), First Aid, Sea Survival, Diesel Engine and Radar. The SRC and the diesel course are the two most useful to a new owner.</li>
  </ul>

  <h3 id="licences--icc">The International Certificate of Competence (ICC)</h3>
  <p>The ICC comes from UNECE Resolution 40, a resolution of the United Nations Economic Commission for Europe that each country chooses whether to apply. It lets a country issue a certificate that other countries can accept as evidence that a skipper is competent. It is the document most Mediterranean, Adriatic and inland-waterway authorities, and many charter companies, want to see from a visiting skipper.</p>
  <ul>
    <li><strong>Getting one:</strong> in the UK the RYA issues it to eligible applicants who hold the Day Skipper practical certificate (or higher), or who pass an ICC assessment at a training centre. Other countries that apply the resolution issue their own, often against their national licence.</li>
    <li><strong>Categories:</strong> it states what it covers: sail or power, coastal or inland waters, and the size of boat. A <strong>CEVNI</strong> endorsement, after a short test on the European inland waterway rules, is needed for the rivers and canals of mainland Europe.</li>
    <li><strong>Limits:</strong> not every country accepts it. A country usually issues its ICC only to its own citizens or residents, with some exceptions, so an EU resident cannot simply get one from the RYA; some countries accept an ICC only if its holder is a citizen or resident of the country that issued it; and some refuse an ICC issued abroad to their own nationals; the RYA’s own eligibility rules for non-UK applicants have changed over the years {TWO}. An RYA ICC is valid for five years.</li>
  </ul>

  <h3 id="licences--radio">Radio: two licences</h3>
  <ul>
    <li><strong>The operator’s certificate</strong> for the person: the Short Range Certificate (SRC), a one-day course and exam, covers VHF and DSC. Anyone may use the radio in a real distress emergency; otherwise the operator, or the person directly supervising, needs one; in the UK, using a VHF without one is an offence.</li>
    <li><strong>The ship radio licence</strong> for the boat, from the flag state (in the UK, from Ofcom). It comes with the boat’s call sign and its MMSI, the nine-digit number programmed into the DSC radio and the AIS (see <a href="#electronics">Electronics</a>). When a boat changes hands the seller surrenders the licence and the new owner applies for one in their own name; in the UK the call sign and MMSI stay with the boat for life. When a boat changes flag it gets a new MMSI, because the first three digits are the country’s code: the DSC radio and the AIS must be reprogrammed (some only by a dealer), and the EPIRB recoded with the new country and re-registered. A PLB is registered to its owner, not the boat.</li>
    <li>A handheld DSC VHF has its own MMSI and, in the UK, its own licence (a ship portable radio licence, registered to the person, valid only in UK waters), unless it is programmed with the boat’s MMSI, which ties it to that boat (see <a href="#electronics--mayday">Electronics</a>).</li>
  </ul>

  <h3 id="licences--national">National rules for the waters on this site</h3>
  <p>For a sailing yacht of 9 to 11 m with an inboard diesel, in private use. Two questions: what a skipper needs on a boat registered in that country, and what a visiting skipper needs on a boat from somewhere else. Many countries simply ask a visitor for whatever the boat’s flag state requires; a UK-flagged boat, whose flag state requires nothing, is then best covered by an ICC.</p>
{compare('Licence rules by country, checked against official pages in September 2026', ['Country', 'On a boat registered there', 'Visiting skipper on a foreign boat', 'Notes'], [
  ['United Kingdom', 'no licence for pleasure use of a boat under 24 m and 80 gross tonnes', 'the same', 'the VHF needs an operator’s certificate (the SRC) and a ship radio licence'],
  ['France', 'at sea, none for a sailing yacht, whatever its engine: the permis plaisance is for motor boats above 4.5 kW. On rivers and canals a yacht with an engine above 4.5 kW needs the permis with the inland option', 'must hold what the boat’s flag state requires; an ICC is recommended on inland waters', 'a French-flagged boat carries French rules into foreign waters'],
  ['Netherlands', 'none for a sailing yacht of this size, at sea or inland: the Klein Vaarbewijs is for boats of 15 m or longer, or faster than 20 km/h', 'at sea, only what the flag state requires; inland, an ICC for boats of 15 m or longer, or faster than 20 km/h', 'the IJsselmeer and the Wadden Sea count as inland waters'],
  ['Germany', 'the Sportbootführerschein See (SBF See) on German sea waterways for a boat with an engine of more than 11.03 kW (15 PS), under sail or power: most yachts of this size', 'a visitor who lives abroad and stays less than a year needs no German licence if their home country requires none; if it requires one, or applies UNECE Resolution 40 (the UK does, according to the RYA), the home licence or an ICC. So a UK resident should carry an ICC', 'the rule follows where the skipper lives, not the flag. The SKS, SSS and SHS are higher certificates, voluntary for private use'],
  ['Denmark', 'none under 15 m (speedboats and jet skis excepted); from 15 to 24 m, a Yachtskipper certificate', 'only what the flag state requires', 'foreign certificates are not recognised on Danish-registered boats; Denmark does not take part in the ICC scheme'],
  ['Sweden', 'none for a boat under 12 m long and 4 m wide (jet skis excepted)', 'only what the flag state requires', ''],
  ['Finland', 'none up to 24 m; above that, an ICC', 'only what the flag state requires; an ICC is accepted if asked for', ''],
  ['Croatia', 'a certificate of competence (for this size, in practice the voditelj brodice category B)', 'qualified under the flag state’s rules; if it sets none (the UK, for example), a certificate Croatia recognises: the ICC, or the RYA Day Skipper practical or the SBF See, these two for yachts up to 18 m only. With a VHF aboard, a radio operator’s certificate as well', 'plus the navigation permit and tourist tax (see <a href="#seas--adriatic">the Adriatic</a>)'],
  ['Italy', 'the patente nautica beyond 6 nautical miles from the coast, or with a larger engine (above 2,000 cc for a diesel without a turbo, 1,300 cc with one, and in any case above 30 kW)', 'evidence of competence, seldom inspected; the ICC is generally accepted', 'the rule covers sailing yachts too'],
  ['Greece', '{TBC}', 'evidence of competence (the ICC is recommended), with a letter from your embassy or consulate certifying the body that issued it, and a Greek translation of the certificate', 'a transit log for boats from outside the EU, the UK included, and the TEPAI cruising tax for boats over 7 m. For a charter, see below'],
  ['Turkey', 'since 17 July 2026, an amateur skipper’s certificate: the ADB 10 for boats up to 10 m overall, the ADB 24 up to 24 m', 'evidence of competence (the ICC is generally accepted)', 'a transit log, surrendered on departure; now largely electronic ¹'],
  ['Bulgaria', '{TBC}: Bulgaria issues a small-craft skipper’s certificate under UNECE Resolution 40', '{TBC}', 'check with the harbour master before arriving'],
  ['Romania', '{TBC}: the Romanian Naval Authority issues its own international certificates', '{TBC}', 'check with the harbour master before arriving'],
], wide=True, stack=True)}
  <p><strong>An example:</strong> a UK owner with the RYA Day Skipper practical, an ICC and an SRC, on their own UK-flagged boat, is covered wherever the table says “only what the flag state requires” or that the ICC is accepted; Germany asks a UK resident for exactly that ICC, Croatia for the SRC as well, and Greece adds the embassy letter and the Greek translation. On inland waters (French rivers and canals with an engine above 4.5 kW, Dutch inland waters for boats of 15 m or longer) the ICC needs its inland (CEVNI) endorsement. Bulgaria and Romania are still to be confirmed.</p>

  <h3 id="licences--charter">Chartering a yacht</h3>
  <p>For a bareboat charter (a yacht without a skipper) of 9 to 11 m. The law is only the floor: the charter company and its insurer set their own standard, and it decides whether you get the boat. Most ask for a sailing CV (a list of your recent passages and the boats you skippered) as well as the certificate; send both when you book.</p>
{compare('Bareboat charter requirements by country, September 2026', ['Country', 'Skipper', 'VHF certificate', 'Crew and other conditions'], [
  ['United Kingdom', 'no legal qualification; the charter company sets its own standard', 'an SRC to use the radio, as on any boat', 'none in law'],
  ['France', 'no permis for a sailing yacht at sea; companies ask for a sailing CV', '{TBC}', 'on canals a hired boat may be exempt from the permis'],
  ['Netherlands', 'no licence under 15 m; companies judge your experience ¹', '{TBC}', '{TBC}'],
  ['Germany', 'German skippers need the SBF See (the engine is above 11.03 kW), and many companies also want the SKS or proof of experience. A visitor from the UK: an ICC under the visitor rule above; some companies also accept a home-country qualification written into the charter contract (one Kiel company), or RYA certificates held by British skippers (another); ask when you book' 'an SRC where a DSC radio is fitted; one company removes the radio on small yachts for skippers without one ¹', 'a pyrotechnics certificate (for flares) may be asked for ¹'],
  ['Denmark, Sweden', 'no certificate required by law for this size; companies’ own rules {TBC}', '{TBC}', '{TBC}'],
  ['Croatia', 'a certificate valid under the flag state’s rules or Croatia’s, checked at handover: the ICC (up to 24 m), or the RYA Day Skipper practical or SBF See (up to 18 m)', 'required when a VHF is fitted; some companies accept it from anyone on board, others ask the skipper', 'at least one qualified skipper over 18'],
  ['Italy', 'an accepted licence, usually the ICC; there is no official list', 'usually asked for {TBC}', ''],
  ['Greece', 'the ICC, or the RYA Coastal Skipper practical or higher; sources disagree on whether the RYA Day Skipper certificate alone is accepted ²', 'sources disagree ²', 'a second crew member over 18 on the crew list, whom some companies want to be experienced ²; the port authority checks the papers before you leave'],
  ['Turkey', 'a foreign certificate, within its limits; companies ask for the ICC, RYA Day Skipper, SBF See or equivalent, with a sailing CV', '{TBC}', '{TBC}'],
], wide=True, stack=True)}

  <h3 id="licences--schemes">Other countries’ training schemes</h3>
  <p>No country publishes an official equivalence with the RYA scheme, so the right-hand column is our own reading of each official level description, a rough guide only. The one official cross-reference is Croatia’s list of the foreign certificates it accepts, and what each allows in Croatian waters.</p>
{compare('Training schemes compared with the RYA ladder (our reading, not official)', ['Certificate', 'What it covers', 'Nearest RYA level'], [
  ['Germany: SBF See', 'the legal licence for boats with an engine above 11.03 kW on German sea waterways; mostly motor handling and the rules', 'Day Skipper theory in scope, but it proves no sailing skill'],
  ['Germany: SKS', 'coastal waters up to 12 nautical miles from the mainland; needs the SBF See', 'Day Skipper to Coastal Skipper'],
  ['Germany: SSS and SHS', 'SSS: up to 30 nautical miles offshore and the whole of the Baltic, North Sea, Channel, Irish Sea, Mediterranean and Black Sea; SHS: worldwide', 'SSS: Coastal Skipper to Yachtmaster Offshore; SHS: Yachtmaster Offshore to Ocean'],
  ['Netherlands: CWO Jachtvaren I to IV', 'I: crew; II: skipper by day, up to force 4; III: skipper by day and night, up to force 6; IV: full responsibility in all conditions, by exam', 'I: Competent Crew; II: Day Skipper; III: Coastal Skipper; IV: Yachtmaster'],
  ['Netherlands: Klein Vaarbewijs I and II', 'the legal inland licence for boats of 15 to 25 m or faster than 20 km/h; II adds the IJsselmeer, the Wadden Sea and the Oosterschelde', 'no match: nearest the ICC’s inland (CEVNI) endorsement'],
  ['France: FFVoile niveaux 3, 4 and 5', '3: crew; 4: watch leader, sails a chosen coastal area alone but under a skipper when others are aboard; 5: skipper by day and night, with a “hauturier” add-on for passages over 24 hours', '3: Competent Crew; 4: between Competent Crew and Day Skipper; 5: Coastal Skipper'],
  ['France: permis plaisance, côtière and hauturière', 'motor-boat licences; the hauturière adds a written chartwork exam for going beyond 6 nautical miles', 'no sailing equivalent; the hauturière is theory only'],
  ['Sweden: förarintyg, kustskepparintyg, utsjöskepparintyg', 'navigation theory near land; the coast in darkness and poor visibility; open-sea passages', 'Day Skipper theory; Coastal Skipper; Yachtmaster Offshore theory'],
  ['Denmark: duelighedsbevis, Yachtskipper 3rd and 1st grade', 'theory and practical test; skipper of yachts up to 24 m in northern European waters; the same on all seas, with sea time', 'Day Skipper; Coastal Skipper or Yachtmaster Coastal; Yachtmaster Offshore'],
  ['Finland: saaristolaivuri, rannikkolaivuri, avomerilaivuri', 'theory exams: inshore by day; the coast, tides and darkness; ocean and celestial navigation ¹', 'Day Skipper theory; Coastal Skipper theory; Yachtmaster Ocean theory'],
  ['Croatia: voditelj brodice B', 'private boats and yachts up to 30 gross tonnes; an oral exam, with no compulsory course or practical, that includes the radio', 'nearest Day Skipper, but by exam only'],
  ['Italy: patente nautica, category A', 'within 12 nautical miles, or without limits (adding a chartwork exam), sail and motor', 'within 12 nautical miles: about Day Skipper; without limits: about Coastal Skipper'],
], wide=True, stack=True)}

  <h3 id="licences--papers">The boat’s own papers</h3>
  <p>Carry the originals, or certified copies where the law allows, in a waterproof folder by the chart table.</p>
  <ul>
    <li><strong>Registration.</strong> Most countries require a yacht going abroad to be registered: in the UK on Part 1 of the register (full title) or the cheaper Small Ships Register, which records the boat but not its ownership {TBC}.</li>
    <li><strong>Proof of ownership:</strong> the bill of sale, and the builder’s certificate where it survives.</li>
    <li><strong>VAT status:</strong> inside the EU, evidence that VAT has been paid on the boat, or that it is exempt. A boat without it can be charged VAT when customs find it; a non-EU boat owned by a non-EU resident can instead stay up to 18 months under temporary admission. The rules for boats entering the EU from outside, including from the UK, are in <a href="#buying--abroad">Buying abroad</a>.</li>
    <li><strong>Insurance:</strong> third-party cover is compulsory in many countries, often with a minimum amount, and marinas ask to see the certificate: Italy, Spain, Croatia and Greece require it, Germany does not. Check that the policy covers the waters you are going to.</li>
    <li><strong>Radio licence</strong> and the skipper’s certificates.</li>
    <li><strong>A crew list</strong>, with names, nationalities and passport numbers, is asked for in many countries, and required for entering from outside the Schengen area.</li>
    <li><strong>Local papers:</strong> Croatia’s vignette and tourist tax receipt, Turkey’s transit log, and so on.</li>
  </ul>
{card('licences--crossing-borders', 'Crossing a border by sea', 'customs, immigration, Schengen, Brexit', 'Between two countries of the Schengen area, a yacht with EU, EEA or Swiss crew usually sails from one to the other with no passport control; between two countries of the EU customs union, with no customs. The two are not the same: Norway is in Schengen but outside the EU customs union, and Ireland and Cyprus are in the EU but outside Schengen. Local permits, taxes and reporting apply either way. Everywhere else, arriving by sea is like arriving by air: the boat and each person on it must enter the country properly.',
  ['Arriving from outside the area, the skipper goes first to a port of entry, flies the yellow Q flag if the country still asks for it, and reports to customs and immigration (in person, by phone, or online) before anyone else goes ashore. France asks for the Q flag only if you have goods to declare.'],
  ['Inside Schengen there is normally no passport control, and inside the EU customs union no customs, for a VAT-paid boat and EU, EEA or Swiss crew; local rules still apply, such as Croatia’s vignette, Greece’s cruising tax (TEPAI) and reporting to the harbour master, and temporary border checks are possible.'],
  ['Since the UK left the EU, a crossing between the UK and France, Belgium or the Netherlands is a customs and immigration crossing in both directions. Non-EU crew, British crew included, can stay in the Schengen area for 90 days in any 180, and are now registered in the EU’s Entry/Exit System when they arrive; non-British crew entering the UK may need an Electronic Travel Authorisation, and the UK asks for an online pleasure craft report. The EU’s Entry/Exit System, in force since October 2025, is still being rolled out at sea borders.'],
  ['A crew member who stays aboard without being cleared in; a boat whose VAT status cannot be shown; a boat that forgot to clear out of one country before entering the next.'],
  ['Read the entry rules for each country before you go, carry the papers above, and ask the marina or harbour master on arrival: they deal with it every day.'], kind='fault', fold=True)}
{sources('licences and papers', [
  'RYA scheme and the ICC: ' + a('https://www.rya.org.uk/our-services/icc/','RYA, ICC application') + ', ' + a('https://www.rya.org.uk/course-finder/competent-crew-practical-course/','RYA, Competent Crew') + ', ' + a('https://en.wikipedia.org/wiki/Day_Skipper','Wikipedia, Day Skipper') + ', ' + a('https://en.wikipedia.org/wiki/International_Certificate_of_Competence','Wikipedia, ICC') + ', ' + a('https://unece.org/','UNECE') + '.',
  'Radio: ' + a('https://www.ofcom.org.uk/spectrum/radio-equipment/ships-radio','Ofcom, ship radio and ship portable radio') + ', ' + a('https://www.rya.org.uk/regulations/licensing-onboard-electronics/','RYA, licensing onboard electronics') + '.',
  'National rules: ' + a('https://www.rya.org.uk/regulations/pleasure-craft-regulations/','RYA, pleasure craft regulations') + ', ' + a('https://www.rya.org.uk/boating-abroad/country-specific-advice/','RYA, country-specific advice') + ' (each country’s page), ' + a('https://www.mer.gouv.fr/le-permis-plaisance-permis-de-conduire-les-bateaux-de-plaisance-moteur','France, Ministère de la Mer') + ', ' + a('https://www.government.nl/topics/sailing-and-boating/obtaining-a-small-licence-klein-vaarbewijs-kvb','Netherlands, Government.nl') + ', ' + a('https://www.gesetze-im-internet.de/spfv/BJNR101610017.html','Germany, SpFV') + ' and ' + a('https://www.elwis.de/DE/Sportschifffahrt/Sportbootfuehrerscheine/Sportbootfuehrerscheine-node.html','ELWIS') + ', ' + a('https://www.soefartsstyrelsen.dk/fritidssejlads/beviser-og-certifikater/duelighedsbevis','Denmark, Søfartsstyrelsen') + ' and ' + a('https://www.soefartsstyrelsen.dk/fritidssejlads/beviser-og-certifikater/brug-af-udenlandske-beviser-i-danmark','foreign certificates') + ', ' + a('https://www.transportstyrelsen.se/sv/sjofart/fritidsbatar/Kunskap-och-kompetens/','Sweden, Transportstyrelsen') + ', ' + a('https://traficom.fi/fi/veneily/veneilyn-patevyydet/kansainvalinen-huviveneenkuljettajankirja','Finland, Traficom') + ', ' + a('https://narodne-novine.nn.hr/clanci/sluzbeni/2013_07_97_2189.html','Croatia, decree on foreign yachts') + ' and ' + a('https://mmpi.gov.hr/UserDocsImages/dokumenti/MORE/More%205_26/TABLICE%20MoU%20HR-EN%2021-5_26/TABLICA%20MoU%20HRV%2021-5_26.pdf','the Ministry’s list of accepted certificates') + ' (PDF), ' + a('https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-07-18;171~art39','Italy, D.Lgs. 171/2005 art. 39') + ', ' + a('https://www.resmigazete.gov.tr/eskiler/2026/01/20260117-12.htm','Turkey, Resmî Gazete 17 January 2026') + ', ' + a('https://www.gocekonline.com/en/blue-cruise-guide/sailing-and-navigation/transitlog-turkey-yachts','Turkey, transit log (Göcek Online)') + ', ' + a('https://www.marad.bg/bg/node/2648','Bulgaria, Maritime Administration') + ', ' + a('https://www.noonsite.com/cruising-resources/european-union/','Noonsite, European Union') + '.',
  'Charter: ' + a('https://assets.publishing.service.gov.uk/media/691e23cb513046b952c500df/The_sport_or_pleasure_vessel_code.pdf','UK, Sport or Pleasure Vessel Code') + ' (PDF), ' + a('https://www.sunsail.com/fr/blog/niveau-requis-pour-louer-un-voilier','Sunsail (France)') + ', ' + a('https://www.charterzentrum.de/yachtcharter-ostsee/infoseiten/fragen-yachtcharter.html','Charterzentrum') + ', ' + a('https://www.pc-ostsee.de/ostsee/service','PCO Kiel') + ', ' + a('https://www.ostseecharter.info/charter_kiel_ostsee.html','Ostseecharter Kiel') + ', ' + a('https://www.boot.de/de/Wassertourismus/Themen_Wassertourismus/Yachtcharter/Segelcharter/Ratgeber_Yachtcharter/Welche_Scheine_brauche_ich_als_Charterer','boot Düsseldorf') + ', ' + a('https://narodne-novine.nn.hr/clanci/sluzbeni/2017_04_42_972.html','Croatia, charter regulation') + ', ' + a('https://www.moorings.com/yacht-charter/resumes-requirements','Moorings') + ', ' + a('https://plainsailing.com/blog/minimum-qualifications-for-bareboat-chartering','PlainSailing') + ', ' + a('https://improvesailing.com/destinations/bareboat-charter-requirements-italy','Improve Sailing, Italy') + ' and ' + a('https://improvesailing.com/destinations/bareboat-charter-requirements-greece','Greece') + ', ' + a('https://www.filovent.com/us/faq/destinations/greece/boat-license-regulations-greece','Filovent') + ', ' + a('https://www.sunsail.com/uk/blog/qualifications-for-yacht-charter','Sunsail (UK)') + ', ' + a('https://www.gocekonline.com/en/blue-cruise-guide/plan-your-trip/amateur-sailor-license-adb-guide','Göcek Online, ADB guide') + '.',
  'Training schemes: ' + a('https://www.elwis.de/DE/Sportschifffahrt/Sportbootfuehrerscheine/Sportbootfuehrerscheine-node.html','ELWIS') + ', ' + a('https://cwo.nl/leren-varen/jachtvaren','CWO Jachtvaren') + ', ' + a('https://espaces.ffvoile.fr/media/cimldvov/niveaux_techniques_croisiere.pdf','FFVoile cruising levels') + ' (PDF), ' + a('https://www.transportstyrelsen.se/sv/sjofart/Fritidsbatar/Kunskap-och-kompetens/Utbildning-for-fritidsbat/','Transportstyrelsen, training') + ', ' + a('https://www.soefartsstyrelsen.dk/fritidssejlads/beviser-og-certifikater/yachtskipperbevis','Søfartsstyrelsen, Yachtskipper') + ', ' + a('https://traficom.fi/fi/veneily/veneilyn-patevyydet/veneilyn-teoriatutkinnot','Traficom, theory exams') + ', ' + a('https://www.iusinfo.hr/aktualno/u-sredistu/stjecanje-uvjerenja-o-osposobljenosti-za-voditelja-brodice-svjedodzbe-o-osposobljenosti-za-zapovjednika-jahte-u-republici-hrvatskoj-56530','IUS-INFO, Croatian certificates') + ', ' + a('https://it.wikipedia.org/wiki/Patente_nautica_italiana','Wikipedia (Italian), patente nautica') + '.',
  'Papers and borders: ' + a('https://oceanskies.com/guide/the-uk-ship-register-part-i-v-uk-small-ships-register-ssr-part-iii/','Part 1 and the SSR') + ', ' + a('https://oceanskies.com/guide/temporary-admission-temporary-importation-for-yachts-in-europe/','temporary admission') + ', ' + a('https://www.sailoscope.com/post/boat-insurance-requirements-by-country','insurance by country') + ', ' + a('https://www.rya.org.uk/boating-abroad/entry-and-exit-formalities/','RYA, entry and exit formalities') + ', ' + a('https://en.wikipedia.org/wiki/Schengen_Area','Wikipedia, Schengen Area') + ', ' + a('https://www.pya.org/news/schengen-ees-update','PYA, the Entry/Exit System') + ', ' + a('https://en.wikipedia.org/wiki/Electronic_Travel_Authorisation_(United_Kingdom)','Wikipedia, UK ETA') + '.',
  'National rules and charter law: official pages opened and read in September 2026, except Greece’s own-flag rule and Romania, whose official pages could not be opened (hence {TBC}); charter-company practice from the companies’ own pages. Papers and borders: checked by web search. These rules change: check before you go.',
])}

  <h3>Choosing a sailing school</h3>
  <ul>
    <li>Look for a centre recognised by the national body (the RYA, or its equivalent), with instructors qualified for the course.</li>
    <li>Ask the maximum number of students per boat (often four or five students to one instructor) and how many hours a day are spent sailing.</li>
    <li>Do the practical course on a boat like the one you will sail, or on your own boat: many schools offer own-boat tuition.</li>
    <li>Do the theory course first, in the winter. The practical week goes further if the chartwork and the collision rules are already familiar.</li>
  </ul>

  <h3>Worth watching</h3>
{videos([
 ('5hArHpw1gxE', 'RYA Day Skipper: practical skills and continuous assessment, with Emma Muddiman', 'Royal Yachting Association - RYA', 'The RYA on what the Day Skipper practical covers, and how you are assessed during the week.'),
 ('viAo7JEJO7o', 'International Certificate of Competence (ICC)', 'PowerboatTrainingUK', 'How the ICC is obtained, from a training centre.'),
 ('QkcCC5GHN8k', 'What to expect on RYA Competent Crew: learn to sail', 'First Class Sailing', 'The first rung of the ladder, from a sea school.'),
 ('qILuIhnQsZs', 'RYA Day Skipper course: all you need to know', 'Ola Lily', 'A student’s account of the theory and practical courses: what to bring and what to expect.'),
 ('Ji0cI_Ss1jo', 'Day Skipper pre-practical preparation', 'Ardent Training', 'What to do before the practical week.'),
 ('HnWPVk-uBL0', 'How to obtain an International Certificate of Competency (ICC)', 'Australian Sailing - Training', 'The ICC as issued outside the UK, by Australian Sailing.'),
])}

  <h3>Terms used in this section</h3>
  <h4 class="terms__group">Which rules apply</h4>
{terms([
 ("lc-flag","Flag state","The country a boat is registered in. Its laws apply to the boat wherever it goes."),
 ("lc-coastal","Coastal state","The country whose waters the boat is in. Its rules apply to every boat there, whatever its flag."),
 ("lc-charter","Charter requirements","What a charter company and its insurer ask of a skipper and crew; often more than the law."),
])}
  <h4 class="terms__group">Training</h4>
{terms([
 ("lc-competent-crew","Competent Crew","The RYA’s first practical course: being useful and safe on board."),
 ("lc-day-skipper","Day Skipper","The RYA course for skippering a yacht by day in familiar waters; the usual first target for an owner."),
 ("lc-day-skipper-theory","Day Skipper theory","The shore-based course in chartwork, tides, collision rules, weather and safety."),
 ("lc-coastal-skipper","Coastal Skipper","The RYA course for longer passages, including at night."),
 ("lc-coastal-skipper-theory","Coastal Skipper / Yachtmaster theory","The advanced shore-based course, shared by the Coastal Skipper and the Yachtmaster exams."),
 ("lc-ym-coastal","Yachtmaster Coastal","An exam, with minimum sea time, showing competence to skipper on coastal passages."),
 ("lc-ym-offshore","Yachtmaster Offshore","An exam, with more sea time and passages, showing competence to skipper offshore."),
 ("lc-icc","ICC","The International Certificate of Competence, under UNECE Resolution 40: a certificate other countries can accept as proof of competence."),
 ("lc-support","Supporting courses","Short courses alongside the ladder: the VHF Short Range Certificate, First Aid, Sea Survival, Diesel Engine and Radar."),
])}

</section>
'''
finish(page, ROOT + 'sections/13-licences.html', others=(ROOT + 'sections/03-hull.html', ROOT + 'sections/04-rig.html', ROOT + 'sections/05-deck.html', ROOT + 'sections/06-engine.html', ROOT + 'sections/07-systems.html', ROOT + 'sections/08-electronics.html', ROOT + 'sections/09-sailing.html', ROOT + 'sections/10-manoeuvres.html', ROOT + 'sections/11-navigation.html', ROOT + 'sections/12-seas.html', ROOT + 'sections/02-fleet.html', ROOT + 'sections/00-start.html'))
