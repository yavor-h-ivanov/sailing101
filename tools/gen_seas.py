# Generates sections/12-seas.html for Sailing 101.
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_common import *
import gen_seas_diagrams as g

NOSRC = ('No web pages could be checked for this section. The descriptions are general cruising knowledge, as in the standard pilot books and almanacs for each area; the forecast services are linked to their home pages. '
         'Local rules, fees and forecast channels change often and are marked {TBC}: check the pilot book, the almanac and the national authority before you go. Specific pages are to be linked in a later pass.')

page = f'''<section id="seas">
  <h2>Seas and cruising grounds</h2>
  <p class="lead">The same boat behaves like a different boat in different waters. A skipper who learned in the tideless Adriatic has to relearn passage timing in the English Channel; one who learned in the Channel has to learn to fear a clear sky over the Velebit mountains. This section is a first orientation for the six waters this site covers: the <a href="#seas--channel">English Channel</a>, the <a href="#seas--north-sea">North Sea</a>, the <a href="#seas--baltic">Baltic</a>, the <a href="#seas--med">Mediterranean</a>, the <a href="#seas--adriatic">Adriatic</a> and the <a href="#seas--black-sea">Black Sea</a>. It does not replace the pilot book for the area, which you should buy before you go.</p>

  <details class="first-words" open>
    <summary>Six words before anything else</summary>
    <dl>
      <dt>Pilot book</dt><dd>A guide to a coast for yachts: harbours, anchorages, dangers, local rules and weather. The first thing to buy for a new area.</dd>
      <dt>Fetch</dt><dd>The distance of open water the wind blows across. The longer the fetch, the bigger the waves.</dd>
      <dt>Tidal gate</dt><dd>A headland or channel that can be passed comfortably only at certain states of the tide (see <a href="#navigation">Navigation</a>).</dd>
      <dt>Overfalls</dt><dd>Rough, breaking water where a strong tidal stream runs over an uneven seabed or round a headland; a tide race.</dd>
      <dt>Fall wind</dt><dd>Cold air pouring down a mountainside onto the sea, like the bora: sudden and very gusty.</dd>
      <dt>Lead</dt><dd>In the skerries, a marked channel between the rocks.</dd>
    </dl>
  </details>
  <p class="conf-key"><b>Marks used below:</b> {ONE} single source; {TWO} sources disagree or anecdotal; {TBC} not yet verified. <b>Note:</b> this section was written without live source checks. The broad character of each sea is well known; anything that is a number, a rule, a fee or a date is marked {TBC} and must be checked in a current pilot book or with the national authority.</p>

  <h3>At a glance</h3>
{compare('Six cruising grounds compared', ['', 'Tide', 'Typical summer wind', 'Harbours and mooring', 'Season {TBC}', 'The thing to respect'], [
  ['English Channel', 'large: ranges of several metres, strong streams', 'westerlies from Atlantic depressions, and sea breezes', 'marinas with pontoons, drying harbours, moorings', 'May to September', 'the tidal streams at headlands, and shipping'],
  ['North Sea', 'moderate to large, with strong streams in the channels', 'westerlies, often fresh', 'marinas, drying harbours in the Wadden Sea', 'May to September', 'shallow banks, wind against tide, fog, shipping'],
  ['Baltic', 'almost none; the level moves with wind and pressure', 'light to moderate, variable', 'box berths (south), bow-to a rock (north), marinas', 'June to August at its best', 'rocks in the skerries, and cold water'],
  ['Mediterranean', 'small in most places', 'sea breezes, and strong named winds', 'stern-to with lazy lines, anchoring', 'April to October', 'the mistral and the meltemi'],
  ['Adriatic', 'small; up to about a metre in the north {TBC}', 'the afternoon maestral', 'marinas and town quays stern-to, buoys in bays', 'May to October', 'the bora, which can arrive suddenly'],
  ['Black Sea', 'almost none', 'moderate; north-easterlies in autumn', 'fewer marinas; fishing and commercial harbours', 'June to September', 'drifting mines since 2022, short steep seas and sudden storms'],
], wide=True, stack=True)}

  <h3 id="seas--channel">English Channel</h3>
  <p>Some of the strongest tidal streams and the largest tidal ranges in Europe, around a busy shipping lane, on a coast of fine harbours a day’s sail apart. It is where much of northern Europe learns to sail, and it teaches tide.</p>
  <ul>
    <li><strong>Tide:</strong> the range varies a lot along the coast. On the English side it is smallest around Poole, Weymouth and Portland, about two metres at springs, and larger to the east towards Dover and to the west in Devon and Cornwall {TBC}. The biggest ranges are on the French side: the Gulf of St Malo and the Channel Islands have among the largest tides in the world, well over 10 m at springs at St Malo {TBC}. A harbour you can enter at half tide may be a mudflat at low water.</li>
    <li><strong>Tidal gates:</strong> the streams run hardest round the headlands and through the gaps between the islands. Portland Bill, St Alban’s Head, Start Point, the Alderney Race (Raz Blanchard) and Cap de la Hague are the famous ones; the Alderney Race can run at more than 5 knots at springs {TBC}. Pass them near slack water, or with the stream, and never with a strong wind against it. Overfalls (tide races) are marked on the chart with wavy symbols.</li>
    <li><strong>Shipping:</strong> the Dover Strait traffic separation scheme is one of the busiest in the world, watched by the coastguard’s Channel Navigation Information Service on radar and AIS {TBC}. Cross it on a heading at right angles to the lanes, quickly, and keep a proper lookout; ferries cross the Channel at speed in every direction.</li>
    <li><strong>Weather:</strong> westerly depressions arrive off the Atlantic, some faster than forecast. The Solent and the big estuaries are sheltered; the open Channel is not, and a wind against the tide off a headland builds a dangerous sea.</li>
    <li><strong>Formalities:</strong> the UK is outside the EU and the Schengen area, so crossing to France, Belgium or the Netherlands and back needs customs and immigration formalities in both directions {TBC}. See <a href="#licences">Licences and qualifications</a>.</li>
  </ul>
{figure('fig-wind-tide', 'wind against tide', '0 0 900 320', 'Wind with the tide and wind against the tide', 'Two side views of the sea with the same wind blowing from left to right. Left: the tidal stream runs the same way as the wind, and the waves are long and low. Right: the tidal stream runs against the wind, and the waves are short and steep, with breaking crests.', g.wind_tide(), 'The same force 5 can be a pleasant sail or a punishing one, depending on which way the tide is running. In the Channel and the North Sea, plan headlands and estuary bars for when the wind and the tide go the same way.', note=HINT)}

  <h3 id="seas--north-sea">North Sea</h3>
  <p>Shallow, tidal and busy, with long coasts of sand and few natural harbours in places. A tough school with good rewards: the Dutch and German islands, the Wadden Sea, and the way into the Baltic.</p>
  <ul>
    <li><strong>Banks and channels:</strong> much of the southern North Sea is shallow, with sandbanks that shift. In the Wadden Sea, behind the Dutch, German and Danish islands, the channels between the banks are marked with buoys and withies (small branches on stakes) that are moved as the sand moves, and some harbours dry at low water: a place where bilge-keel, lifting-keel and flat-bottomed boats, which sit upright on the sand, are at home. A fin or long keel dries out only against a wall or with legs {TBC}.</li>
    <li><strong>Sea state:</strong> a shallow sea builds steep waves quickly, and a strong onshore wind against an ebb tide at a harbour entrance can make it impassable. Do not approach a shallow entrance in a strong onshore wind.</li>
    <li><strong>Offshore:</strong> wind farms, oil and gas platforms, and traffic separation schemes off the Dutch and German coasts. Many wind farms have rules on whether small craft may pass through, which differ from country to country {TBC}. Fog is common in spring and early summer.</li>
    <li><strong>The Kiel Canal</strong> (Nord-Ostsee-Kanal) links the Elbe at Brunsbüttel with the Baltic at Kiel, saving the long way round Denmark. Yachts may use it under engine, not sail, by day, for a fee {TBC}.</li>
  </ul>

  <h3 id="seas--baltic">Baltic</h3>
  <p>An almost tideless, brackish sea with two characters: the shallow, sandy south of Denmark and Germany, with small harbours everywhere, and the rocky skerry coasts of Sweden and Finland, with their thousands of islands and anchorages in the north.</p>
  <ul>
    <li><strong>Water:</strong> brackish, getting fresher to the north and east; less salt means less corrosion and, in the fresher north, less fouling {TBC}, and a boat floats a little deeper. It is cold: even in high summer, a person in the water cools quickly {TBC}.</li>
    <li><strong>Water level:</strong> no real tide, but the level rises and falls with the wind and air pressure, by tens of centimetres in ordinary weather and much more in a storm {TBC}. Check the local forecast of water level before entering a shallow harbour.</li>
    <li><strong>Skerries:</strong> in the Stockholm archipelago, the Åland Islands and the Finnish Archipelago Sea, you follow marked channels (leads) between rocks, many unmarked beyond them. Detailed charts, careful pilotage and the depth sounder are essential; keep to the lead unless you know the water.</li>
    <li><strong>Mooring:</strong> box berths between posts in Denmark and Germany (see <a href="#manoeuvres">Manoeuvres</a>); in Sweden and Finland, bow-to a rock with a stern anchor, or bow-to a pontoon with a stern buoy. For a stern buoy, come in slowly bow first, pass a line from the stern through the buoy’s ring as you pass it (a boathook helps), and pay it out as you go on to the pontoon; then take it tight to hold the bow off {TBC}.</li>
    <li><strong>The right of public access</strong> in Sweden and Finland allows anchoring and going ashore almost anywhere outside private gardens and nature reserves, for a short stay, with respect for landowners and wildlife {TBC}. Some bird and seal sanctuaries are closed to landing in the breeding season.</li>
    <li><strong>Season:</strong> short and bright: roughly June to August at its best, with very long days in the north. Many boats carry a diesel heater for the nights.</li>
    <li><strong>Military areas:</strong> several countries have naval firing and exercise areas marked on the charts, with warnings broadcast when they are active {TBC}. Stay out of Russian waters and any closed area.</li>
    <li><strong>GPS interference:</strong> jamming and spoofing of satellite positioning has been widely reported over parts of the Baltic in recent years {TBC}. Keep a paper chart, the logbook and the traditional ways of fixing position (see <a href="#navigation">Navigation</a>) ready, and be suspicious of a plotter position that jumps.</li>
  </ul>
{figure('fig-skerry', 'bow-to a rock', '0 0 900 400', 'Mooring bow-to a rock in the Scandinavian way', 'Seen from above: a rocky shore with trees at the top. A boat lies bow-to the rock, held by two bow lines spread wide to pins in the rock, and held off by a stern anchor dropped well out astern. Labels: check the depth all the way in; crew step ashore from the bow.', g.skerry(), 'Choose a rock sheltered from the forecast wind, with deep water close to it; approach slowly, dropping the stern anchor as you go, and have the bow crew ready with the lines and a rock pin and hammer {TBC}.')}

  <h3 id="seas--med">Mediterranean</h3>
  <p>Warm water, long seasons, deep bays, and very small tides in most places. The weather is usually kind in summer, and when it is not, it has a name.</p>
  <ul>
    <li><strong>Tide:</strong> small in most places, a few tens of centimetres, with exceptions such as the Gulf of Gabès in Tunisia and the northern Adriatic {TBC}. Streams are weak; currents are driven by the wind.</li>
    <li><strong>Winds</strong> (named, like all winds, for the direction they blow <em>from</em>): on settled days, sea breezes that build in the afternoon and die at night (see the drawing). Then the named winds:
      <ul>
        <li><strong>Mistral:</strong> a cold, dry north-westerly down the Rhône valley into the Gulf of Lion and towards Corsica and Sardinia, often under a clear sky, strong for days {TBC}. When one is forecast, stay in harbour or in a bay sheltered from the north-west; do not start a crossing of the Gulf of Lion.</li>
        <li><strong>Tramontane:</strong> a similar north-westerly off the Pyrenees, along the Catalan and Roussillon coasts.</li>
        <li><strong>Meltemi:</strong> the summer north wind of the Aegean, strongest in July and August and in the afternoon, often force 5 to 7 for days in the Cyclades {TBC}. Plan island hops for the mornings, before it builds; choose harbours and anchorages open to the south, and expect a rough passage going north.</li>
        <li><strong>Sirocco:</strong> a hot south or south-easterly from Africa, humid and hazy by the time it crosses the sea, sometimes carrying red dust.</li>
        <li><strong>Gregale:</strong> a strong north-easterly of the central Mediterranean, around Malta and the Ionian Sea, mostly in autumn and winter {TBC}.</li>
        <li><strong>Libeccio, levante and poniente:</strong> the south-westerly of the Ligurian Sea and Corsica, and the easterly and westerly of the Strait of Gibraltar and the Alboran Sea.</li>
      </ul></li>
    <li><strong>Sea state:</strong> a short, steep sea for the wind, because the fetch is limited.</li>
    <li><strong>Mooring:</strong> stern-to with lazy lines or your own anchor (see <a href="#manoeuvres--med">Manoeuvres</a>); marinas are expensive in high season.</li>
    <li><strong>Anchoring:</strong> the water is often deep right up to the shore, so anchorages are chosen carefully. Seagrass (<em>Posidonia</em>) meadows are protected, and anchoring on them is banned or restricted in parts of France, Spain and elsewhere {TBC}: anchor in sand, which shows as pale patches.</li>
  </ul>
{figure('fig-sea-breeze', 'sea breeze', '0 0 900 330', 'The sea breeze by day and the land breeze by night', 'Two cross-sections of a coast. Day: the sun heats the land, warm air rises over it, and a sea breeze blows onshore at the surface, with a return flow aloft. Night: the land cools faster than the sea, and a lighter land breeze blows offshore.', g.sea_breeze(), 'The sea breeze is the everyday wind of Mediterranean and Adriatic summers, and of many northern coasts on sunny days: calm in the morning, a good sailing breeze by early afternoon, fading at dusk.')}

  <h3 id="seas--adriatic">Adriatic</h3>
  <p>Croatia’s coast has more than a thousand islands, most of them in long chains parallel to the shore, with sheltered channels between them: short hops, clear water and anchorages everywhere. Slovenia, the Italian coast, Montenegro and Albania complete the sea.</p>
  <ul>
    <li><strong>Maestral:</strong> the summer afternoon north-westerly, a sea breeze of force 3 to 4, the best sailing wind of the season {TBC}. It fails when a change in the weather is coming.</li>
    <li><strong>Jugo</strong> (sirocco): a warm, humid south-easterly that builds over a day or two, with cloud, rain and a long swell, strongest in the south and on open coasts. It gives warning.</li>
    <li><strong>Bora</strong> (bura): the dangerous one. A cold north-easterly that falls off the coastal mountains, often behind a cold front, sometimes out of a clear sky. Its gusts are violent close under the mountains, especially below the passes: near Trieste, Senj, along the Velebit channel and under the Biokovo mountains at Makarska {TBC}. A cap of cloud on the mountain crests is the classic warning. When a bora is forecast, be in a harbour or an anchorage well sheltered from the north-east, with good holding, before it arrives, and stay there.</li>
    <li><strong>Formalities:</strong> Croatia requires a navigation permit (vignette) and a tourist tax for each person on board, arranged online or at the first port, plus a recognised skipper’s licence and a radio certificate for the skipper {TBC}. National parks such as Kornati, Krka and Mljet charge entry fees. See <a href="#licences">Licences and qualifications</a>.</li>
    <li><strong>Mooring:</strong> marinas, town quays stern-to with lazy lines, restaurant jetties (the owner expects you to eat there), and fee-paying mooring buoys in many bays.</li>
  </ul>
{figure('fig-bora', 'the bora', '0 0 900 370', 'How the bora falls off the mountains onto the sea', 'A cross-section with the sea on the left and coastal mountains and an inland plateau on the right. Cold, dense air piles up inland, pours over the crest under a cap of cloud, falls down the slope and accelerates, and hits the sea in violent gusts close under the mountains, tearing spray off the water. Further out the gusts ease.', g.bora(), 'A fall wind is strongest where the slopes are steepest and the passes funnel it, so the worst gusts are close to the mainland coast, not out at sea. Forecasts give warning of most boras, but a bora can still arrive suddenly, out of a clear sky; the local forecasts on VHF are the ones to listen to {TBC}.')}

  <h3 id="seas--black-sea">Black Sea</h3>
  <p>A large, enclosed, almost tideless sea, about half as salty as the ocean, with a short season of settled weather and fewer yachting facilities than the Mediterranean. The Bulgarian and Romanian coasts are the usual cruising ground for EU boats; Turkey’s long northern coast is more remote.</p>
  <ul>
    <li><strong>Sea state:</strong> in a strong wind the sea builds a short, steep chop quickly, and storms can arrive fast outside the summer months. Autumn and winter bring hard north-easterlies.</li>
    <li><strong>Harbours:</strong> Bulgaria has marinas and harbours at Balchik, Varna, Nesebar, Burgas and Sozopol, among others; Romania at Constanța and Mangalia. Many are fishing or commercial harbours with a yacht corner; facilities are thinner than further west {TBC}.</li>
    <li><strong>Safety:</strong> since the war in Ukraine began in 2022, drifting sea mines have been reported in the western Black Sea, and parts of the sea are closed or dangerous {TBC}. Read the current navigational warnings (NAVTEX and the national authorities) before every passage, and stay well clear of any restricted area.</li>
    <li><strong>Formalities:</strong> Bulgaria and Romania are in the EU, and joined the Schengen area for sea borders in 2024 and fully in 2025 {TBC}; Turkey is not, and a yacht entering Turkey needs the formalities for a non-EU country {TBC}. See <a href="#licences">Licences and qualifications</a>.</li>
  </ul>
{sources('seas', [NOSRC])}

  <h3 id="seas--forecasts">Where to get the forecast</h3>
  <p>Every coastal country has a national weather service with marine forecasts, and most broadcast them on VHF, usually announced first on channel 16. The channels and times change; check them in the almanac or pilot book for the area {TBC}.</p>
{compare('National weather services with marine forecasts', ['Country', 'Service', 'Notes'], [
  ['United Kingdom', a('https://www.metoffice.gov.uk/', 'Met Office'), 'shipping forecast and inshore waters forecast; coastguard broadcasts on VHF'],
  ['France', a('https://meteofrance.com/', 'Météo-France'), 'coastal forecasts; broadcasts by the French coastguard (CROSS) on VHF'],
  ['Netherlands, Germany', a('https://www.knmi.nl/', 'KNMI') + ', ' + a('https://www.dwd.de/', 'DWD'), 'North Sea and Baltic forecasts'],
  ['Denmark, Sweden, Finland', a('https://www.dmi.dk/', 'DMI') + ', ' + a('https://www.smhi.se/', 'SMHI') + ', ' + a('https://www.fmi.fi/', 'FMI'), 'Baltic forecasts, including water levels'],
  ['Croatia', a('https://meteo.hr/', 'DHMZ'), 'Adriatic forecasts, broadcast continuously on VHF by the coast radio stations {TBC}'],
  ['Italy, Greece', a('https://www.meteoam.it/', 'Aeronautica Militare') + ', ' + a('https://www.emy.gr/', 'HNMS'), 'Mediterranean and Aegean forecasts'],
  ['Bulgaria, Romania, Turkey', a('https://www.meteo.bg/', 'NIMH') + ', ' + a('https://www.meteoromania.ro/', 'ANM') + ', ' + a('https://www.mgm.gov.tr/', 'MGM'), 'Black Sea forecasts'],
], stack=True)}

  <h3>Worth watching</h3>
  <p>No videos have been found and checked for this section yet; they are listed as planned below.</p>

  <h3>Terms used in this section</h3>
  <h4 class="terms__group">Wind and tide</h4>
{terms([
 ("wt-wind","Wind","The same wind in both drawings: it is the tide that changes the sea."),
 ("wt-tide-with","Wind with tide","The tidal stream running the same way as the wind: the waves lengthen and flatten."),
 ("wt-tide-against","Wind against tide","The tidal stream running against the wind: the waves shorten, steepen and break. Worst off headlands and at bars."),
 ("wt-long","Long, low waves","The sea with wind and tide together."),
 ("wt-steep","Short, steep waves","The sea with wind against tide: uncomfortable, slow and, in a strong wind, dangerous."),
 ("sb-rising","Rising warm air","Air heated over sunny land rises, drawing in cooler air from the sea."),
 ("sb-sea-breeze","Sea breeze","A daytime onshore wind caused by the land heating up; it starts late in the morning and fades at dusk."),
 ("sb-land-breeze","Land breeze","A lighter night-time offshore wind, as the land cools below the sea’s temperature."),
])}
  <h4 class="terms__group">The bora</h4>
{terms([
 ("bo-cold-air","Cold air inland","Cold, dense air that collects over the land behind the coastal mountains, often after a cold front."),
 ("bo-cap-cloud","Cap cloud","A bank of cloud sitting on the mountain crest as the bora pours over it: the classic warning sign."),
 ("bo-fall","Fall wind","Air falling down a mountain slope and speeding up; the bora is one, the mistral partly one."),
 ("bo-gusts","Bora gusts","Violent, short gusts close under the mountains and below passes, strong enough to lay a yacht flat."),
 ("bo-sea","Further offshore","The gusts ease away from the coast, but a strong bora can still blow hard far out."),
])}
  <h4 class="terms__group">The skerries</h4>
{terms([
 ("sk-bow-lines","Bow lines to the rock","Two lines from the bow to rock pins, rings or trees, spread wide to stop the bow swinging."),
 ("sk-step","Stepping ashore","From the bow onto the rock, often with a folding bow ladder; the rock may be slippery."),
 ("sk-stern-anchor","Stern anchor","A kedge anchor dropped astern on the approach, often on a reel of webbing tape at the pushpit, that holds the boat off the rock."),
 ("sk-depth","Depth close in","Skerry shores are often steep-to, but rocks can lie just under the surface close to them; watch the sounder and look into the water."),
])}

  <div class="planned">
    <p>Planned for this section</p>
    <ul>
      <li>Source links, and the forecast channels and times for each country (written without live sources; see the note at the top)</li>
      <li>A map of each sea with its cruising areas, named winds and tidal gates</li>
      <li>Per-sea tables: water temperature, season, marina cost band, holding-tank rules</li>
      <li>Photos: a bora cap cloud over the Velebit, a Wadden Sea drying harbour, a Swedish skerry anchorage, the Alderney Race</li>
      <li>Videos, being checked before they are linked: sailing each sea, from people who live there</li>
    </ul>
  </div>
</section>
'''
page = page.replace('{TBC}: check the pilot book', 'TBC: check the pilot book')
finish(page, ROOT + 'sections/12-seas.html', others=(ROOT + 'sections/03-hull.html', ROOT + 'sections/04-rig.html', ROOT + 'sections/05-deck.html', ROOT + 'sections/06-engine.html', ROOT + 'sections/07-systems.html', ROOT + 'sections/08-electronics.html', ROOT + 'sections/09-sailing.html', ROOT + 'sections/10-manoeuvres.html', ROOT + 'sections/11-navigation.html', ROOT + 'sections/02-fleet.html', ROOT + 'sections/00-start.html'))
