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
    <p>What follows is a map of the landscape, not legal advice. The national rules below were checked by web search in September 2026, and each is linked in the sources block; they change, so check each one with the country’s authority, your flag state, and for a charter the charter company, before you rely on it. Anything we could not confirm is marked {TBC}.</p>
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

  <h3>National rules for the waters on this site</h3>
  <p>A first orientation only. Where a country requires a licence, it usually accepts the licences of other countries that it recognises, and the ICC; it may still add conditions. Check each one before you go.</p>
{compare('Licence rules by country: a first orientation', ['Country', 'For a sailing yacht of 9 to 11 m', 'Notes'], [
  ['United Kingdom', 'no licence required for pleasure sailing', 'SRC and ship radio licence required for the VHF'],
  ['France', 'none for a sailing yacht, even with an engine above 4.5 kW; the permis is for motor boats above that', 'visiting skippers are generally judged by their flag state’s rules'],
  ['Netherlands', 'at sea, generally none; on inland waters the Klein Vaarbewijs for boats over 15 m or faster than 20 km/h', 'sea use rules differ from inland ones'],
  ['Germany', 'the Sportbootführerschein See (SBF See) in German coastal waters for a boat with an engine above 11.03 kW (15 PS), which includes most yachts of this size {TWO}', 'the SKS, SSS and SHS are higher, mostly voluntary, certificates'],
  ['Denmark, Sweden, Finland', 'Sweden: none under 12 m long and 4 m wide; Finland: none for boats of this size; Denmark: a certificate (duelighedsbevis) for some boats {TWO}', 'a radio certificate is still required'],
  ['Croatia', 'a recognised skipper’s licence and a radio certificate are required to skipper a yacht', 'plus the navigation permit and tourist tax (see <a href="#seas--adriatic">the Adriatic</a>)'],
  ['Italy', 'on an Italian-flagged yacht, the patente nautica beyond 6 miles from the coast or with an engine above 30 kW', 'visiting skippers need their own country’s equivalent'],
  ['Greece, Turkey', 'a recognised certificate to skipper; for a Greek charter, an ICC or RYA Coastal Skipper or higher (a Day Skipper certificate alone is no longer accepted) and a second experienced crew member', 'Turkey issues an electronic transit log to visiting yachts'],
  ['Bulgaria, Romania', 'both recognise the ICC; national certificates for their own boats', 'check with the harbour master before arriving'],
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
  'National rules: ' + a('https://blog.cannesyachtingfestival.com/en/what-licence-do-you-need-for-a-sailing-boat/','France') + ', ' + a('https://www.government.nl/topics/sailing-and-boating/obtaining-a-small-licence-klein-vaarbewijs-kvb','Netherlands (Government.nl)') + ', ' + a('https://skipper.adac.de/ratgeber/sportbootfuehrerschein-see-sbf-see','Germany (ADAC)') + ', ' + a('https://sjoassistans.se/nyheter/sjoassistans/go-boating-in-the-nordics/','the Nordic countries (Sjöassistans)') + ' ², ' + a('https://www.croatia-yachting-charter.com/en/blog/boat-licenses-croatia','Croatia') + ', ' + a('https://www.theboatplatform.com/it/blog/quando-serve-patente-nautica-guida','Italy') + ', ' + a('https://improvesailing.com/destinations/bareboat-charter-requirements-greece','Greece') + ', ' + a('https://www.gocekonline.com/en/blue-cruise-guide/sailing-and-navigation/transitlog-turkey-yachts','Turkey') + ', ' + a('https://www.noonsite.com/cruising-resources/european-union/','Noonsite, European Union') + '.',
  'Papers and borders: ' + a('https://oceanskies.com/guide/the-uk-ship-register-part-i-v-uk-small-ships-register-ssr-part-iii/','Part 1 and the SSR') + ', ' + a('https://oceanskies.com/guide/temporary-admission-temporary-importation-for-yachts-in-europe/','temporary admission') + ', ' + a('https://www.sailoscope.com/post/boat-insurance-requirements-by-country','insurance by country') + ', ' + a('https://www.rya.org.uk/boating-abroad/entry-and-exit-formalities/','RYA, entry and exit formalities') + ', ' + a('https://en.wikipedia.org/wiki/Schengen_Area','Wikipedia, Schengen Area') + ', ' + a('https://www.pya.org/news/schengen-ees-update','PYA, the Entry/Exit System') + ', ' + a('https://en.wikipedia.org/wiki/Electronic_Travel_Authorisation_(United_Kingdom)','Wikipedia, UK ETA') + '.',
  'Checked by web search, September 2026; the pages could not be opened directly. These rules change: check before you go.',
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

  <div class="planned">
    <p>Planned for this section</p>
    <ul>
      <li>A checked table of licence rules by country, flag, boat size and engine power, with links to the official sources</li>
      <li>Charter requirements by country</li>
      <li>Other countries’ training schemes and how they compare with the RYA’s</li>
    </ul>
  </div>
</section>
'''
finish(page, ROOT + 'sections/13-licences.html', others=(ROOT + 'sections/03-hull.html', ROOT + 'sections/04-rig.html', ROOT + 'sections/05-deck.html', ROOT + 'sections/06-engine.html', ROOT + 'sections/07-systems.html', ROOT + 'sections/08-electronics.html', ROOT + 'sections/09-sailing.html', ROOT + 'sections/10-manoeuvres.html', ROOT + 'sections/11-navigation.html', ROOT + 'sections/12-seas.html', ROOT + 'sections/02-fleet.html', ROOT + 'sections/00-start.html'))
