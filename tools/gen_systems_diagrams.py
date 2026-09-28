# Diagram builders for sections/07-systems.html.
import math
from gen_hull_diagrams import part, label, lead, title, muted, bow, marker
from gen_engine_diagrams import badge, arrow, lines, swatch

def battery(x, y, w=100, h=60, name=''):
    return (f'<rect class="dg-hull-dark shape" x="{x}" y="{y}" width="{w}" height="{h}" rx="4"/>'
            f'<rect class="dg-hull" x="{x + w/2 - 8}" y="{y - 6}" width="16" height="6"/><rect class="dg-hull" x="{x + w/2 - 8}" y="{y + h}" width="16" height="6"/>'
            f'<text class="dg-label small" x="{x + w/2 - 22}" y="{y + 16}" text-anchor="middle">+</text><text class="dg-label small" x="{x + w/2 - 22}" y="{y + h - 6}" text-anchor="middle">−</text>'
            f'<text class="dg-label small" x="{x + w/2 + 8}" y="{y + h/2 + 4}" text-anchor="middle">{name}</text>')

def fuse(x, y):   # vertical fuse centred on x, spanning y..y+16
    return f'<rect class="dg-hull shape" x="{x-5}" y="{y}" width="10" height="16" rx="2"/><line class="dg-thin" x1="{x}" y1="{y+2}" x2="{x}" y2="{y+14}"/>'

def switch(cx, cy, r=14):
    return f'<circle class="dg-bad-fill shape" cx="{cx}" cy="{cy}" r="{r}" opacity=".85"/><rect class="dg-hull" x="{cx-3}" y="{cy-r+3}" width="6" height="{2*r-6}" rx="2"/>'

# ---------------------------------------------------------------- 12 V system (viewBox 0 0 900 540)
def electrics():
    H = []
    H.append(title(450, 24, 'A typical 12 V system: two banks, their switches, and what charges them'))
    H.append(muted(450, 42, 'schematic, not a wiring diagram for any particular boat'))
    H.append(swatch(24, 62, 'dg-wire-pos', 'positive (12 V)'))
    H.append(swatch(190, 62, 'dg-wire-neg', 'negative'))
    H.append(swatch(320, 62, 'dg-wire-ac', '230 V from shore'))
    H.append(swatch(500, 62, 'dg-wire-earth', 'shore earth'))
    P = []
    # ---- house positive bar
    P.append('      <path class="dg-wire-pos" d="M232,300 H640"/>')
    P.append(part('house-bank', '        ' + battery(260, 336, name='House 1') + battery(380, 336, name='House 2') + '\n' + lines(250, 372, ['House bank: runs', 'everything except', 'the starter'], 'dg-label small', 'end')))
    P.append('      <path class="dg-wire-pos" d="M310,330 V300 M430,330 V300"/>')
    P.append(part('main-fuse', '        ' + fuse(310, 306) + fuse(430, 306) + '\n' + lines(250, 328, ['Main fuses, close', 'to each battery'], 'dg-label small', 'end') + '\n' + lead(252, 324, 304, 314)))
    # negatives and shunt
    P.append('      <path class="dg-wire-neg" d="M310,402 V414 H430 V402 M430,414 H470"/>')
    P.append(part('shunt', '        <rect class="dg-hull shape" x="470" y="406" width="54" height="16" rx="2"/><path class="dg-thin" d="M480,410 V418 M490,410 V418 M500,410 V418 M510,410 V418"/>\n' + lines(470, 470, ['Shunt: measures every amp in and out'], 'dg-label small', 'start') + '\n' + lead(496, 458, 496, 422)))
    P.append('      <path class="dg-wire-neg" d="M524,414 H600 V436 H200 M810,402 V436 H600"/>')
    P.append(part('neg-bus', '        <rect class="dg-hull-dark shape" x="180" y="430" width="30" height="12" rx="2"/>\n' + lines(176, 440, ['Negative busbar'], 'dg-label small', 'end')))
    # ---- solar and MPPT
    grid = ''.join(f'<line class="dg-thin" x1="{x}" y1="64" x2="{x}" y2="96"/>' for x in (270, 290, 310, 330)) + '<line class="dg-thin" x1="250" y1="80" x2="350" y2="80"/>'
    P.append(part('solar-panel', f'        <rect class="dg-sea-fill shape" x="250" y="64" width="100" height="32" rx="2"/>{grid}\n' + lines(250, 56, ['Solar panel'], 'dg-label small', 'start')))
    P.append('      <path class="dg-wire-pos" d="M300,96 V120"/>')
    P.append(part('mppt', '        <rect class="dg-hull shape" x="266" y="120" width="68" height="30" rx="4"/>\n' + label(300, 139, 'MPPT', 'dg-label small', 'middle') + '\n' + lines(308, 174, ['Solar', 'controller'], 'dg-label small', 'start')))
    P.append('      <path class="dg-wire-pos" d="M300,150 V300"/>')
    # ---- house isolator and panel
    P.append(part('house-switch', '        ' + switch(430, 262) + '\n' + lines(450, 282, ['House switch'], 'dg-label small', 'start')))
    P.append('      <path class="dg-wire-pos" d="M430,300 V276 M430,248 V214"/>')
    rows = ['Navigation lights', 'Instruments and VHF', 'Autopilot', 'Fridge', 'Cabin lights', 'Water pump', 'USB and 12 V sockets']
    br = ''.join(f'<rect class="dg-hull-dark" x="404" y="{84 + i*18}" width="14" height="10" rx="2"/><text class="dg-label small" x="424" y="{93 + i*18}">{t}</text>' for i, t in enumerate(rows))
    P.append(part('dc-panel', f'        <rect class="dg-hull shape" x="390" y="70" width="180" height="144" rx="6"/>{br}\n' + lines(480, 60, ['Distribution panel: a breaker per circuit'], 'dg-label small', 'middle')))
    P.append(part('battery-monitor', '        <rect class="dg-sea-fill shape" x="576" y="168" width="30" height="24" rx="3"/>\n' + lines(614, 160, ['Battery monitor:', 'reads the shunt'], 'dg-label small', 'start')))
    # ---- bilge pump direct
    P.append('      <path class="dg-wire-pos" d="M600,300 V330"/>')
    P.append(part('bilge-direct', '        ' + fuse(600, 330) + '<rect class="dg-hull shape" x="580" y="352" width="40" height="30" rx="6"/>\n' + label(600, 371, 'bilge', 'dg-label small', 'middle') + '<path class="dg-wire-neg" d="M600,382 V436"/>' + '\n' + lines(628, 360, ['Bilge pump: fused,', 'straight from the', 'battery, so it works', 'with the switch off'], 'dg-label small', 'start')))
    # ---- start side
    P.append(part('start-battery', '        ' + battery(760, 336, name='Start') + '\n' + lines(890, 458, ['Start battery:', 'only for the engine'], 'dg-label small', 'end') + '\n' + lead(862, 446, 846, 396)))
    P.append('      <path class="dg-wire-pos" d="M810,330 V276 M810,248 V220"/>')
    P.append(part('start-switch', '        ' + switch(810, 262) + '\n' + lines(792, 286, ['Engine switch'], 'dg-label small', 'end')))
    P.append(part('sys-alternator', '        <circle class="dg-hull-dark shape" cx="810" cy="150" r="30"/><path class="dg-thin" d="M796,150 Q803,138 810,150 T824,150" stroke-width="2"/>\n' + lines(772, 138, ['Alternator on', 'the engine'], 'dg-label small', 'end')))
    P.append('      <path class="dg-wire-pos" d="M810,180 V220 H880 M810,220 H700"/>')
    P.append(muted(895, 212, 'to the starter', 'end'))
    P.append(part('dcdc', '        <rect class="dg-hull shape" x="610" y="204" width="90" height="32" rx="4"/>\n' + label(655, 224, 'DC-DC or VSR', 'dg-label small', 'middle') + '\n' + lines(655, 256, ['Split charging: feeds', 'the house bank too'], 'dg-label small', 'middle')))
    P.append('      <path class="dg-wire-pos" d="M610,220 H580 V300"/>')
    P.append(part('link-switch', '        <path class="dg-wire-pos" d="M640,300 H694"/>' + switch(706, 300, 10) + '<path class="dg-wire-pos" d="M716,300 H810"/>\n' + lines(706, 326, ['Emergency link'], 'dg-label small', 'middle')))
    # ---- shore power (left)
    P.append(part('shore-inlet', '        <rect class="dg-hull-dark shape" x="20" y="100" width="34" height="40" rx="6"/><circle class="dg-hull" cx="37" cy="120" r="10"/>\n' + lines(20, 90, ['Shore inlet'], 'dg-label small', 'start')))
    P.append('      <path class="dg-wire-ac" d="M54,114 H100"/>')
    P.append('      <path class="dg-wire-earth" d="M54,128 H70 V190 H100"/>')
    P.append(part('galvanic-isolator', '        <rect class="dg-hull shape" x="100" y="178" width="56" height="26" rx="4"/>\n' + label(128, 195, 'GI', 'dg-label small', 'middle') + '\n' + lines(20, 232, ['Galvanic isolator, in', 'the earth wire: blocks', 'the small currents', 'that eat anodes'], 'dg-label small', 'start') + '\n' + lead(96, 218, 112, 204)))
    P.append(part('rcd', '        <rect class="dg-hull shape" x="100" y="96" width="92" height="40" rx="4"/><rect class="dg-hull-dark" x="110" y="106" width="20" height="20" rx="2"/><rect class="dg-hull-dark" x="138" y="106" width="12" height="20" rx="2"/><rect class="dg-hull-dark" x="156" y="106" width="12" height="20" rx="2"/>\n' + lines(146, 90, ['RCD and breakers'], 'dg-label small', 'middle')))
    P.append(part('polarity-light', '        <circle class="dg-warn-fill shape" cx="180" cy="116" r="5"/>\n' + lines(206, 116, ['Polarity', 'light'], 'dg-label small', 'start') + '\n' + lead(204, 112, 186, 116)))
    P.append('      <path class="dg-wire-ac" d="M180,136 V150 H214 V282"/>')
    P.append('      <path class="dg-wire-earth" d="M156,190 H176 V282"/>')
    P.append(part('shore-charger', '        <rect class="dg-hull shape" x="160" y="282" width="72" height="36" rx="4"/>\n' + label(196, 304, 'Charger', 'dg-label small', 'middle') + '\n' + lines(20, 292, ['Battery charger:', 'works on shore', 'power'], 'dg-label small', 'start')))
    return '\n'.join(H) + '\n      <g transform="translate(0,50)">\n' + '\n'.join(P) + '\n      </g>'

def tap(x, y):
    return f'<path class="dg-hull-dark shape" d="M{x-10},{y} H{x+10} V{y+10} H{x+4} V{y+30} Q{x+4},{y+40} {x+14},{y+40} V{y+48} Q{x-4},{y+48} {x-4},{y+30} V{y+10} H{x-10} Z"/>'

# ---------------------------------------------------------------- water (viewBox 0 0 900 430)
def water():
    H = []
    H.append(title(450, 24, 'Fresh water: tank, pump, and hot water from the engine'))
    H.append(muted(450, 42, 'schematic'))
    H.append(swatch(24, 62, 'dg-pipe-cold', 'cold fresh water'))
    H.append(swatch(200, 62, 'dg-pipe-hot', 'hot water'))
    H.append(swatch(340, 62, 'dg-pipe-ret', 'engine coolant (never mixes with the water)'))
    H.append(swatch(700, 62, 'dg-wire-ac', '230 V from shore'))
    P = []
    P.append('      <line class="dg-line" x1="20" y1="30" x2="880" y2="30"/>')
    P.append(muted(876, 24, 'deck', 'end'))
    P.append(part('water-filler', '        <rect class="dg-hull-dark shape" x="64" y="22" width="34" height="8" rx="2"/><path class="dg-line" d="M81,30 V170" stroke-width="6"/>\n' + lines(106, 56, ['Deck filler: marked WATER;', 'diesel in here is a disaster'], 'dg-label small', 'start')))
    P.append(part('water-tank', '        <rect class="dg-hull shape" x="40" y="170" width="190" height="120" rx="6"/><rect class="dg-water" x="42" y="200" width="186" height="88" rx="4"/>\n' + lines(135, 190, ['Water tank'], 'dg-label', 'middle')))
    P.append('      <path class="dg-thin" d="M200,170 V120 Q200,110 210,110 H232" stroke-width="2.5"/>')
    P.append(muted(238, 114, 'vent', 'start'))
    P.append('      <path class="dg-pipe-cold" d="M230,272 H262"/>')
    P.append(part('water-strainer', '        <rect class="dg-sea-fill shape" x="262" y="260" width="28" height="24" rx="4"/>\n' + lines(276, 250, ['Strainer'], 'dg-label small', 'middle')))
    P.append('      <path class="dg-pipe-cold" d="M290,272 H310"/>')
    P.append(part('water-pump', '        <rect class="dg-hull-dark shape" x="310" y="248" width="58" height="46" rx="8"/><circle class="dg-hull" cx="339" cy="271" r="12"/>\n' + lines(339, 316, ['Pressure pump:', 'switches itself on', 'when a tap opens'], 'dg-label small', 'middle')))
    P.append('      <path class="dg-pipe-cold" d="M368,272 H430 V120 H790 V150 M660,120 V150 M446,120 V350 H460 V336"/>')
    P.append(part('accumulator', '        <rect class="dg-sea-fill shape" x="392" y="180" width="30" height="64" rx="12"/><line class="dg-pipe-cold" x1="422" y1="220" x2="430" y2="220"/>\n' + lines(384, 170, ['Accumulator: a', 'pressure cushion'], 'dg-label small', 'end') + '\n' + lead(386, 176, 400, 184)))
    P.append(arrow(560, 120, 0, 'dg-flow'))
    # calorifier
    coil = 'M540,306 ' + ' '.join(f'L{548 + 12*i},{290 if i % 2 == 0 else 322}' for i in range(0, 8))
    P.append(part('calorifier', '        <rect class="dg-hull shape" x="450" y="276" width="190" height="60" rx="26"/>\n' + lines(708, 372, ['Calorifier: an insulated', 'hot-water tank'], 'dg-label small', 'start') + '\n' + lead(706, 368, 636, 326)))
    P.append(part('coolant-coil', f'        <path class="dg-pipe-ret shape" d="{coil}"/><path class="dg-pipe-ret" d="M632,306 H700 M632,320 H700"/>\n' + lines(750, 290, ['Coil: hot engine coolant', 'heats the water while', 'you motor'], 'dg-label small', 'start') + '\n' + lead(748, 296, 700, 310)))
    P.append(muted(708, 342, 'to and from the engine', 'start'))
    P.append(part('immersion', '        <path class="dg-line shape" d="M476,306 l6,-8 l6,16 l6,-16 l6,16 l6,-8" stroke-width="2"/><path class="dg-wire-ac" d="M506,312 V380"/>\n' + lines(516, 392, ['Immersion heater:', '230 V, on shore power'], 'dg-label small', 'start')))
    P.append('      <path class="dg-pipe-hot" d="M620,276 V140 H810 V150 M680,140 V150"/>')
    P.append(part('mixing-valve', '        <rect class="dg-hull-dark shape" x="610" y="226" width="20" height="20" rx="4"/><path class="dg-pipe-cold" d="M610,236 H590 V120" stroke-width="3"/>\n' + lines(640, 238, ['Mixing valve: adds cold water', 'so the taps cannot scald'], 'dg-label small', 'start')))
    P.append(part('taps', '        ' + tap(670, 150) + tap(800, 150) + '\n' + lines(670, 214, ['Galley tap'], 'dg-label small', 'middle') + '\n' + lines(800, 214, ['Basin and shower'], 'dg-label small', 'middle')))
    return '\n'.join(H) + '\n      <g transform="translate(0,56)">\n' + '\n'.join(P) + '\n      </g>'

# ---------------------------------------------------------------- gas (viewBox 0 0 900 470)
def gas():
    H = []
    H.append(title(450, 24, 'Gas: from a sealed locker to the cooker'))
    H.append(muted(450, 42, 'schematic, stern on the left; the parts in order along the pipe'))
    P = []
    P.append('      <rect class="dg-water" x="0" y="330" width="900" height="80"/>')
    P.append('      <path class="dg-hull" d="M24,30 L24,346 C70,380 220,396 440,400 L900,400 L900,30"/>')
    P.append('      <line class="dg-waterline" x1="0" y1="330" x2="900" y2="330"/>')
    P.append('      <text class="dg-waterline-label" x="892" y="324" text-anchor="end">waterline</text>')
    P.append('      <line class="dg-line" x1="300" y1="250" x2="900" y2="250"/>')
    P.append(muted(892, 244, 'cabin sole', 'end'))
    P.append('      <line class="dg-line" x1="330" y1="30" x2="330" y2="250" stroke-width="4"/>')
    P.append(muted(336, 244, 'bulkhead', 'start'))
    # locker
    P.append(part('sys-gas-locker', '        <path class="dg-hull-dark shape" d="M60,70 H300 V230 H60 Z" fill-opacity=".35"/><rect class="dg-hull-dark shape" x="54" y="62" width="252" height="10" rx="2"/>\n' + lines(64, 56, ['Gas locker: sealed to the inside of the boat, opens only at the top'], 'dg-label small', 'start')))
    P.append(part('gas-cylinder', '        <path class="dg-hull shape" d="M104,222 V128 Q104,112 132,112 Q160,112 160,128 V222 Z"/><rect class="dg-hull-dark" x="126" y="100" width="12" height="12"/>\n' + lines(132, 176, ['Cylinder,', 'upright', 'and strapped'], 'dg-label small', 'middle')))
    P.append(part('gas-regulator', '        <rect class="dg-hull-dark shape" x="140" y="88" width="34" height="18" rx="4"/>\n' + lines(178, 76, ['Regulator'], 'dg-label small', 'end') + '\n' + lead(162, 80, 158, 88)))
    P.append('      <path class="dg-pipe-gas" d="M174,96 H196"/>')
    P.append(part('gas-drain', '        <path class="dg-thin shape" d="M80,230 V270 Q80,286 64,286 H26" stroke-width="4"/>\n' + lines(40, 302, ['Drain from the bottom: falls all the way, at least', '19 mm bore, outlet at least 75 mm above the waterline'], 'dg-label small', 'start')))
    P.append(part('gas-solenoid', '        <rect class="dg-hull-dark shape" x="250" y="84" width="30" height="24" rx="3"/>\n' + lines(265, 150, ['Solenoid', 'valve'], 'dg-label small', 'middle') + '\n' + lead(265, 138, 265, 108)))
    P.append('      <path class="dg-pipe-gas" d="M222,96 H250 M280,96 H560"/>')
    P.append(part('bubble-tester', '        <rect class="dg-hull-dark shape" x="196" y="86" width="26" height="12" rx="2"/><rect class="dg-sea-fill shape" x="198" y="98" width="22" height="28" rx="4"/><circle class="dg-hull" cx="205" cy="116" r="2.5"/><circle class="dg-hull" cx="212" cy="108" r="2"/>\n' + lines(230, 196, ['Bubble tester:', 'bubbles mean', 'a leak'], 'dg-label small', 'start') + '\n' + lead(228, 188, 214, 126)))
    P.append(part('gas-valve', '        <path class="dg-hull-dark shape" d="M560,86 L580,106 L580,86 L560,106 Z"/><line class="dg-line" x1="570" y1="96" x2="570" y2="76"/>\n' + lines(570, 68, ['Isolating valve by the cooker'], 'dg-label small', 'middle')))
    P.append('      <path class="dg-pipe-gas" d="M580,96 C620,96 616,150 650,150" stroke-dasharray="3 3"/>')
    # cooker on gimbals
    P.append(part('cooker', '        <rect class="dg-hull shape" x="650" y="134" width="150" height="96" rx="4"/><rect class="dg-hull-dark" x="662" y="128" width="40" height="6" rx="2"/><rect class="dg-hull-dark" x="742" y="128" width="40" height="6" rx="2"/><rect class="dg-hull-dark" x="664" y="164" width="122" height="54" rx="3" fill-opacity=".5"/><circle class="dg-hull-dark" cx="650" cy="146" r="5"/><circle class="dg-hull-dark" cx="800" cy="146" r="5"/>\n' + lines(725, 116, ['Gimballed cooker: flame-failure', 'device on every burner'], 'dg-label small', 'middle')))
    P.append(part('gas-alarm', '        <rect class="dg-warn-fill shape" x="560" y="362" width="26" height="14" rx="3"/><path class="dg-thin" d="M573,362 V262 H316 V116 H282" stroke-dasharray="4 4"/>\n' + lines(890, 360, ['Gas alarm sensor, low in the bilge: gas is heavier', 'than air and sinks. It shuts the solenoid valve'], 'dg-label small', 'end')))
    P.append(part('co-alarm', '        <rect class="dg-hull-dark shape" x="836" y="60" width="30" height="20" rx="4"/><circle class="dg-bad-fill" cx="851" cy="70" r="4"/>\n' + lines(880, 100, ['CO alarm'], 'dg-label small', 'end')))
    return '\n'.join(H) + '\n      <g transform="translate(0,50)">\n' + '\n'.join(P) + '\n      </g>'

# ---------------------------------------------------------------- heads (viewBox 0 0 900 460)
def heads():
    H = []
    H.append(title(450, 24, 'A sea toilet below the waterline, with a holding tank'))
    H.append(muted(450, 42, 'schematic; one common layout of several'))
    H.append(swatch(24, 62, 'dg-pipe-sea', 'sea water in'))
    H.append(swatch(170, 62, 'dg-pipe-waste', 'waste out'))
    P = []
    P.append('      <rect class="dg-water" x="0" y="200" width="900" height="200"/>')
    P.append('      <path class="dg-hull" d="M0,20 H900 V330 C700,350 200,350 0,330 Z"/>')
    P.append('      <line class="dg-waterline" x1="0" y1="200" x2="900" y2="200"/>')
    P.append('      <text class="dg-waterline-label" x="20" y="194" text-anchor="start">waterline</text>')
    P.append('      <line class="dg-line" x1="0" y1="20" x2="900" y2="20"/>')
    P.append(muted(24, 14, 'deck', 'start'))
    P.append('      <line class="dg-line" x1="200" y1="300" x2="560" y2="300"/>')
    # toilet
    P.append(part('toilet', '        <path class="dg-hull shape" d="M330,236 H420 Q416,280 396,290 H354 Q334,280 330,236 Z"/><rect class="dg-hull-dark" x="324" y="228" width="102" height="8" rx="3"/><rect class="dg-hull-dark" x="360" y="290" width="30" height="10"/>\n' + lines(378, 372, ['Toilet bowl, below', 'the waterline'], 'dg-label small', 'middle') + '\n' + lead(378, 360, 378, 292)))
    P.append(part('heads-pump', '        <rect class="dg-hull-dark shape" x="434" y="236" width="24" height="56" rx="4"/><line class="dg-line shape" x1="446" y1="236" x2="446" y2="200" stroke-width="3"/><rect class="dg-hull-dark" x="436" y="192" width="20" height="8" rx="2"/>\n' + lines(446, 182, ['Hand pump'], 'dg-label small', 'middle')))
    P.append(part('joker-valve', '        <path class="dg-accent-fill shape" d="M448,292 L456,300 L448,308 Z"/>\n' + lines(508, 286, ['Joker valve:', 'one-way flap'], 'dg-label small', 'start') + '\n' + lead(506, 292, 457, 300)))
    # inlet
    P.append(part('heads-inlet-seacock', '        <rect class="dg-hull-dark shape" x="240" y="330" width="22" height="18" rx="3"/>\n' + lines(250, 372, ['Inlet seacock'], 'dg-label small', 'middle')))
    P.append('      <path class="dg-pipe-sea" d="M251,330 V318 H428 V286"/>')
    P.append('      <path class="dg-pipe-sea" d="M434,250 H290 V70 Q290,50 310,50 Q330,50 330,70 V228"/>')
    P.append(part('vented-loop', '        <circle class="dg-hull-dark shape" cx="310" cy="50" r="7"/><circle class="dg-hull-dark shape" cx="516" cy="50" r="7"/>\n' + lines(104, 70, ['Vented loops, well above', 'the waterline: stop the', 'sea siphoning into the', 'bowl and the boat'], 'dg-label small', 'start') + '\n' + lead(204, 58, 302, 52)))
    # discharge
    P.append('      <path class="dg-pipe-waste" d="M446,300 V312 H496 V70 Q496,50 516,50 Q536,50 536,70 V250 H580"/>')
    P.append(part('y-valve', '        <path class="dg-hull-dark shape" d="M580,240 H604 L616,230 L620,236 L608,250 L620,264 L616,270 L604,260 H580 Z"/>\n' + lines(548, 106, ['Y-valve: to the', 'tank or overboard,', 'where allowed'], 'dg-label small', 'start') + '\n' + lead(600, 138, 598, 238)))
    P.append('      <path class="dg-pipe-waste" d="M618,233 Q640,190 660,150 M618,267 V330"/>')
    P.append(part('overboard-seacock', '        <rect class="dg-hull-dark shape" x="607" y="330" width="22" height="18" rx="3"/>\n' + lines(618, 372, ['Overboard seacock'], 'dg-label small', 'middle')))
    # holding tank
    P.append(part('sys-holding-tank', '        <rect class="dg-hull shape" x="660" y="84" width="170" height="96" rx="8"/><rect class="dg-hull-dark" x="662" y="136" width="166" height="42" rx="6" fill-opacity=".45"/>\n' + lines(745, 108, ['Holding tank'], 'dg-label', 'middle') + '\n' + lines(745, 124, ['above the waterline'], 'dg-label small', 'middle')))
    P.append(part('pump-out', '        <path class="dg-pipe-waste shape" d="M700,84 V20"/><rect class="dg-hull-dark shape" x="686" y="12" width="28" height="8" rx="2"/>\n' + lines(692, 44, ['Deck pump-out: emptied', 'by a marina pump'], 'dg-label small', 'end')))
    P.append(part('tank-vent-heads', '        <path class="dg-thin shape" d="M810,84 V70 Q810,56 824,56 H872" stroke-width="2.5"/><rect class="dg-hull-dark shape" x="848" y="48" width="24" height="16" rx="3"/>\n' + lines(890, 214, ['Vent with a', 'smell filter'], 'dg-label small', 'end') + '\n' + lead(868, 202, 860, 64)))
    P.append('      <path class="dg-pipe-waste" d="M760,180 V330"/>')
    P.append(part('tank-seacock', '        <rect class="dg-hull-dark shape" x="749" y="330" width="22" height="18" rx="3"/>\n' + lines(760, 372, ['Tank drain: open only', 'where discharge is allowed'], 'dg-label small', 'middle')))
    return '\n'.join(H) + '\n      <g transform="translate(0,80)">\n' + '\n'.join(P) + '\n      </g>'

# ---------------------------------------------------------------- bilge pumps (viewBox 0 0 900 420)
def bilge():
    H = []
    H.append(title(450, 24, 'Bilge pumps, seen from astern'))
    H.append(muted(450, 42, 'one electric pump with a float switch, one high-water alarm, one manual pump worked from the cockpit'))
    P = []
    P.append('      <rect class="dg-water" x="0" y="150" width="900" height="240"/>')
    P.append('      <path class="dg-hull" d="M140,30 C140,160 250,290 420,310 L420,380 L480,380 L480,310 C650,290 760,160 760,30 Z"/>')
    P.append('      <line class="dg-waterline" x1="0" y1="150" x2="900" y2="150"/>')
    P.append('      <text class="dg-waterline-label" x="892" y="144" text-anchor="end">waterline</text>')
    P.append('      <path class="dg-line" d="M214,200 H686"/>')
    P.append(muted(620, 194, 'cabin sole', 'end'))
    P.append('      <path class="dg-water" d="M360,290 Q450,310 540,290 L530,300 Q450,318 370,300 Z"/>')
    P.append(part('electric-bilge', '        <rect class="dg-hull-dark shape" x="424" y="276" width="30" height="26" rx="5"/>\n' + lines(350, 240, ['Electric pump in the lowest', 'point of the bilge'], 'dg-label small', 'end') + '\n' + lead(352, 244, 426, 280)))
    P.append(part('float-switch', '        <rect class="dg-warn-fill shape" x="462" y="284" width="18" height="10" rx="3"/>\n' + lines(560, 330, ['Float switch: starts', 'the pump automatically'], 'dg-label small', 'start') + '\n' + lead(558, 326, 480, 292)))
    P.append(part('high-water-alarm', '        <rect class="dg-bad-fill shape" x="488" y="250" width="18" height="10" rx="3"/>\n' + lines(890, 232, ['High-water alarm float,', 'higher: a siren if the', 'water keeps rising'], 'dg-label small', 'end') + '\n' + lead(772, 240, 506, 256)))
    P.append(part('bilge-outlet', '        <path class="dg-pipe-sea shape" d="M439,276 V220 Q439,206 452,206 H600 Q640,206 650,120 L660,60 Q664,44 680,44 H700 Q716,44 720,60 L736,110"/><rect class="dg-hull-dark shape" x="728" y="104" width="22" height="12" rx="3"/>\n' + lines(890, 60, ['Discharge rises high,', 'then out through the', 'hull above the waterline'], 'dg-label small', 'end')))
    P.append(part('manual-bilge', '        <rect class="dg-hull-dark shape" x="210" y="54" width="46" height="34" rx="6"/><line class="dg-line shape" x1="256" y1="60" x2="300" y2="40" stroke-width="4"/>\n' + lines(24, 70, ['Manual pump, worked', 'from the cockpit'], 'dg-label small', 'start')))
    P.append('      <path class="dg-pipe-sea" d="M233,88 V180 Q233,196 250,196 H380 Q400,196 400,220 V286" stroke-dasharray="7 5"/>')
    P.append(part('strum-box', '        <rect class="dg-hull shape" x="390" y="286" width="22" height="16" rx="3"/><path class="dg-thin" d="M394,292 H408 M394,297 H408"/>\n' + lines(300, 350, ['Strum box: a strainer on', 'the manual pump’s hose'], 'dg-label small', 'middle') + '\n' + lead(340, 336, 396, 302)))
    P.append('      <path class="dg-pipe-sea" d="M210,72 H160 L152,110" stroke-dasharray="7 5"/>')
    P.append(muted(24, 124, 'outlet above the waterline', 'start'))
    return '\n'.join(H) + '\n      <g transform="translate(0,40)">\n' + '\n'.join(P) + '\n      </g>'
