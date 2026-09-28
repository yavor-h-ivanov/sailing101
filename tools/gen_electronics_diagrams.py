# Diagram builders for sections/08-electronics.html. Bow to the RIGHT in every side view.
import math
from gen_hull_diagrams import part, label, lead, title, muted, bow, marker
from gen_engine_diagrams import badge, arrow, lines, swatch

# ---------------------------------------------------------------- where the electronics live (viewBox 0 0 900 470)
def where():
    H = [title(450, 24, 'Where the electronics live on a 10 m yacht'), muted(450, 42, 'bow to the right; a typical fit, not any one boat')]
    P = []
    # sea and hull
    P.append('      <rect class="dg-water" x="0" y="360" width="900" height="110"/>')
    P.append('      <path class="dg-hull" d="M70,322 L820,322 C810,350 790,372 760,384 L180,392 C130,388 90,360 70,322 Z"/>')
    P.append('      <path class="dg-hull-dark" d="M430,388 L452,452 L520,452 L528,386 Z"/>')
    P.append('      <path class="dg-hull-dark" d="M150,388 L146,440 L168,440 L178,388 Z"/>')
    P.append('      <line class="dg-waterline" x1="0" y1="360" x2="900" y2="360"/>')
    P.append('      <path class="dg-hull" d="M300,322 L300,300 L610,300 L640,322 Z"/>')
    P.append(muted(470, 344, 'cabin', 'middle'))
    # rig
    P.append('      <rect class="dg-hull-dark" x="466" y="70" width="8" height="230"/>')
    P.append('      <line class="dg-line" x1="470" y1="70" x2="810" y2="320"/><line class="dg-line" x1="470" y1="70" x2="96" y2="320"/>')
    P.append('      <rect class="dg-hull-dark" x="250" y="276" width="216" height="6"/>')
    # masthead
    P.append(part('el-wind', '        <line class="dg-line" x1="474" y1="72" x2="520" y2="60"/><path class="dg-hull-dark shape" d="M520,52 L540,58 L520,64 Z"/><circle class="dg-hull shape" cx="514" cy="50" r="5"/><circle class="dg-hull shape" cx="526" cy="46" r="5"/>\n' + lines(560, 54, ['Masthead wind unit:', 'vane and cups'], 'dg-label small', 'start')))
    P.append(part('el-vhf-antenna', '        <line class="dg-line shape" x1="468" y1="70" x2="468" y2="18" stroke-width="3"/>\n' + lines(456, 26, ['VHF antenna: as high', 'as possible'], 'dg-label small', 'end')))
    P.append(part('el-tricolour', '        <rect class="dg-warn-fill shape" x="474" y="64" width="10" height="7" rx="2"/>\n' + lines(456, 88, ['Tricolour and anchor light'], 'dg-label small', 'end') + '\n' + lead(458, 84, 476, 70)))
    P.append(part('el-radar', '        <rect class="dg-hull shape" x="476" y="200" width="46" height="18" rx="9"/><line class="dg-line" x1="474" y1="218" x2="490" y2="226"/>\n' + lines(534, 206, ['Radar scanner (dome),', 'on a mast bracket'], 'dg-label small', 'start')))
    P.append(part('el-steaming', '        <rect class="dg-warn-fill shape" x="474" y="160" width="8" height="7" rx="2"/>\n' + lines(534, 166, ['Steaming light (motoring)'], 'dg-label small', 'start') + '\n' + lead(532, 163, 484, 164)))
    P.append(part('el-sternlight', '        <rect class="dg-warn-fill shape" x="90" y="300" width="8" height="7" rx="2"/>\n' + lines(20, 340, ['Sternlight'], 'dg-label small', 'start') + '\n' + lead(52, 330, 90, 306)))
    # stern and cockpit
    P.append('      <path class="dg-line" d="M96,322 V282 H170"/>')
    P.append(part('el-gps', '        <rect class="dg-hull shape" x="100" y="266" width="20" height="16" rx="8"/>\n' + lines(20, 232, ['GPS antenna (and on', 'some boats a separate', 'AIS antenna)'], 'dg-label small', 'start') + '\n' + lead(80, 262, 102, 270)))
    P.append(part('el-plotter', '        <rect class="dg-hull-dark shape" x="186" y="258" width="34" height="26" rx="3"/><rect class="dg-sea-fill" x="190" y="262" width="26" height="18"/><line class="dg-line" x1="203" y1="284" x2="203" y2="322" stroke-width="4"/>\n' + lines(150, 216, ['Chartplotter at', 'the helm'], 'dg-label small', 'start') + '\n' + lead(190, 226, 200, 258)))
    P.append(part('el-displays', '        <rect class="dg-hull-dark shape" x="284" y="300" width="14" height="12" rx="2"/><rect class="dg-hull-dark shape" x="284" y="286" width="14" height="12" rx="2"/>\n' + lines(250, 236, ['Instrument displays', 'on the bulkhead'], 'dg-label small', 'start') + '\n' + lead(282, 246, 290, 286)))
    # below decks
    P.append(part('el-navstation', '        <rect class="dg-hull-dark shape" x="332" y="330" width="44" height="18" rx="3"/><rect class="dg-hull-dark shape" x="332" y="350" width="44" height="12" rx="3"/>\n' + lines(300, 344, ['Chart table: fixed VHF', 'with DSC, AIS unit'], 'dg-label small', 'end') + '\n' + lead(302, 340, 332, 344)))
    P.append(part('el-fluxgate', '        <circle class="dg-hull shape" cx="560" cy="372" r="7"/>\n' + lines(700, 452, ['Fluxgate compass for the', 'autopilot, low and central'], 'dg-label small', 'start') + '\n' + lead(698, 448, 566, 376)))
    P.append(part('el-depth', '        <rect class="dg-hull-dark shape" x="640" y="378" width="14" height="10" rx="2"/>\n' + lines(700, 404, ['Depth transducer'], 'dg-label small', 'start') + '\n' + lead(698, 400, 654, 386)))
    P.append(part('el-log', '        <rect class="dg-hull-dark shape" x="600" y="382" width="14" height="10" rx="2"/><circle class="dg-hull" cx="607" cy="394" r="4"/>\n' + lines(700, 426, ['Log paddle wheel'], 'dg-label small', 'start') + '\n' + lead(698, 422, 612, 396)))
    P.append(part('el-sidelights', '        <rect class="dg-warn-fill shape" x="796" y="302" width="10" height="7" rx="2"/>\n' + lines(890, 290, ['Sidelights on', 'the pulpit'], 'dg-label small', 'end')))
    P.append(bow(890, 350))
    return '\n'.join(H) + '\n      <g transform="translate(0,40)">\n' + '\n'.join(P) + '\n      </g>'

# ---------------------------------------------------------------- NMEA 0183 vs NMEA 2000 (viewBox 0 0 900 380)
def nmea():
    P = []
    P.append(title(210, 26, 'NMEA 0183: one talker, several listeners'))
    P.append(title(660, 26, 'NMEA 2000: one shared backbone'))
    P.append('      <line class="dg-thin" x1="430" y1="40" x2="430" y2="370" stroke-dasharray="3 5"/>')
    def box(x, y, w, h, t, key=None, lab=None):
        body = f'<rect class="dg-hull shape" x="{x}" y="{y}" width="{w}" height="{h}" rx="5"/>' + f'<text class="dg-label small" x="{x+w/2}" y="{y+h/2+4}" text-anchor="middle">{t}</text>'
        return body
    # 0183
    P.append(part('el-talker', '        ' + box(40, 150, 110, 44, 'GPS') + '\n' + lines(95, 138, ['Talker'], 'dg-label small', 'middle')))
    for i, (y, t) in enumerate(((70, 'Chartplotter'), (170, 'VHF with DSC'), (270, 'Autopilot'))):
        P.append('      <path class="dg-line" d="M150,172 C200,172 220,' + str(y + 22) + ' 280,' + str(y + 22) + '" stroke-width="2.5"/>')
        P.append('      ' + box(280, y, 120, 44, t))
    P.append(part('el-listeners', '        <rect class="shape-fill" x="280" y="70" width="120" height="244"/>\n' + lines(340, 340, ['Listeners: each wired', 'to the talker’s output'], 'dg-label small', 'middle')))
    P.append(part('el-multiplexer', '        <rect class="dg-hull-dark shape" x="40" y="250" width="110" height="36" rx="5"/>\n' + label(95, 272, 'Multiplexer', 'dg-label small', 'middle') + '\n' + lines(40, 312, ['Needed when two talkers', 'must reach one listener'], 'dg-label small', 'start')))
    # 2000 backbone
    P.append(part('el-backbone', '        <line class="dg-line shape" x1="470" y1="200" x2="870" y2="200" stroke-width="6"/>\n        <line class="hit" x1="470" y1="200" x2="870" y2="200"/>\n' + lines(660, 232, ['Backbone cable'], 'dg-label small', 'middle')))
    P.append(part('el-terminator', '        <rect class="dg-bad-fill shape" x="456" y="192" width="14" height="16" rx="3"/><rect class="dg-bad-fill shape" x="870" y="192" width="14" height="16" rx="3"/>\n' + lines(456, 250, ['Terminator'], 'dg-label small', 'start') + '\n' + lines(877, 250, ['Terminator'], 'dg-label small', 'end')))
    devs = [(500, 'Plotter'), (580, 'Wind'), (660, 'Depth, log'), (740, 'Autopilot'), (820, 'AIS')]
    for x, t in devs:
        P.append(f'      <path class="dg-line" d="M{x},200 V130" stroke-width="2.5"/><rect class="dg-hull-dark" x="{x-6}" y="194" width="12" height="12" rx="2"/>')
        P.append('      ' + box(x - 34, 90, 68, 40, t))
    P.append(part('el-drop', '        <path class="dg-line shape" d="M580,194 V130" stroke-width="2.5"/><rect class="dg-hull-dark shape" x="574" y="194" width="12" height="12" rx="2"/>\n' + lines(560, 70, ['T-piece and drop cable to each device'], 'dg-label small', 'middle')))
    P.append(part('el-power-tee', '        <path class="dg-wire-pos shape" d="M700,206 V290" stroke-width="2.5"/><rect class="dg-hull shape" x="688" y="290" width="24" height="16" rx="3"/><rect class="dg-hull-dark" x="694" y="194" width="12" height="12" rx="2"/>\n' + lines(724, 302, ['Power tee: 12 V, fused,', 'fed in once near the middle'], 'dg-label small', 'start')))
    P.append(muted(660, 346, 'devices can join anywhere; every device hears every other'))
    return '\n'.join(P)

# ---------------------------------------------------------------- VHF range (viewBox 0 0 900 320)
def vhf_range():
    P = []
    P.append(title(450, 24, 'VHF range: the radio horizon'))
    P.append(muted(450, 42, 'VHF travels in nearly straight lines, so range depends on how high both antennas are; curvature exaggerated'))
    # curved sea
    P.append('      <path class="dg-water" d="M0,250 Q450,170 900,250 L900,320 L0,320 Z"/>')
    P.append('      <path class="dg-waterline" d="M0,250 Q450,170 900,250"/>')
    # yacht on left
    P.append('      <path class="dg-hull" d="M60,236 L150,232 L142,246 L70,248 Z"/>')
    P.append(part('el-range-yacht', '        <rect class="dg-hull-dark shape" x="104" y="120" width="4" height="114"/><line class="dg-line shape" x1="106" y1="120" x2="106" y2="100" stroke-width="3"/>\n' + lines(118, 152, ['Yacht masthead', 'antenna, about 15 m'], 'dg-label small', 'start')))
    # coast station on right
    P.append('      <path class="dg-hull-dark" d="M770,246 L820,160 L900,150 L900,262 Z"/>')
    P.append(part('el-range-coast', '        <rect class="dg-hull-dark shape" x="838" y="80" width="6" height="76"/><line class="dg-line shape" x1="841" y1="80" x2="841" y2="58" stroke-width="3"/>\n' + lines(756, 64, ['Coastguard aerial on a hill,', 'often 100 m or more up'], 'dg-label small', 'end')))
    # line of sight
    P.append(part('el-horizon', '        <path class="dg-accent shape" d="M106,100 L312,214 L841,58" stroke-dasharray="6 5"/>\n' + lines(560, 256, ['Each antenna sees to its own horizon; the higher', 'one sees much further, so the horizons meet', 'nearer the lower antenna'], 'dg-label small', 'middle')))
    P.append('      <text class="dg-label small" x="450" y="290" text-anchor="middle">range in nautical miles ≈ 2.2 × (√ height 1 + √ height 2), heights in metres (rule of thumb, TBC)</text>')
    return '\n'.join(P)

# ---------------------------------------------------------------- AIS (viewBox 0 0 900 400)
def ais():
    P = []
    P.append(title(225, 26, 'What the plotter shows'))
    P.append(title(675, 26, 'What is really out there'))
    P.append('      <line class="dg-thin" x1="450" y1="40" x2="450" y2="390" stroke-dasharray="3 5"/>')
    def tri(x, y, rot, cls, extra=''):
        return f'<path class="{cls}" d="M{x},{y-12} L{x+8},{y+10} L{x-8},{y+10} Z" transform="rotate({rot} {x} {y})"{extra}/>'
    for ox, screen in ((0, True), (450, False)):
        P.append(f'      <rect class="{"dg-sea-fill" if screen else "dg-water"}" x="{30+ox}" y="50" width="390" height="320" rx="10"/>')
        P.append(f'      <path class="dg-hull" d="M{300+ox},50 L{420+ox},50 L{420+ox},170 C{380+ox},160 {330+ox},130 {300+ox},50 Z" opacity=".8"/>')
    P.append(muted(390, 74, 'land', 'middle'))
    P.append('      <path class="dg-hull" d="M290,262 Q306,226 350,230 Q384,240 366,270 Q330,288 290,262 Z" opacity=".8"/>')
    P.append(muted(330, 256, 'island', 'middle'))
    # left: plotter
    P.append(part('el-sleeping', '        ' + tri(100, 110, 30, 'dg-accent-fill shape') + '\n' + lines(60, 142, ['Another AIS boat'], 'dg-label small', 'start')))
    P.append(part('el-own-boat', '        ' + tri(120, 330, 0, 'dg-accent-fill shape') + '<line class="dg-line" x1="120" y1="318" x2="120" y2="230" stroke-dasharray="4 4"/>\n' + lines(136, 350, ['You, with your course line'], 'dg-label small', 'start')))
    P.append(part('el-target', '        ' + tri(330, 210, 260, 'dg-warn-fill shape') + '<line class="dg-line" x1="318" y1="212" x2="150" y2="242" stroke-dasharray="6 3"/>\n' + lines(412, 124, ['Ship: name, course, speed,', 'and a line showing where', 'it will be in a few minutes'], 'dg-label small', 'end') + '\n' + lead(340, 160, 332, 198)))
    P.append(part('el-cpa', '        ' + tri(120, 252, 0, 'dg-accent-fill', ' opacity=".35"') + tri(190, 236, 260, 'dg-warn-fill', ' opacity=".45"') + '<line class="shape" x1="128" y1="250" x2="180" y2="238" stroke="var(--dg-bad)" stroke-width="3"/>\n' + lines(46, 176, ['CPA: the closest the two', 'boats will be, and when', '(TCPA). Pale shapes: both', 'at that moment'], 'dg-label small', 'start') + '\n' + lead(112, 222, 150, 244)))
    # right: reality
    P.append('      ' + tri(550, 110, 30, 'dg-accent-fill'))
    P.append('      ' + tri(570, 330, 0, 'dg-accent-fill'))
    P.append('      ' + tri(780, 210, 260, 'dg-warn-fill'))
    P.append(part('el-no-ais', '        <path class="dg-hull shape" d="M640,160 L652,184 L628,184 Z"/><path class="dg-hull shape" d="M690,286 L702,310 L678,310 Z"/><circle class="dg-hull shape" cx="600" cy="220" r="5"/><circle class="dg-hull shape" cx="630" cy="230" r="5"/><line class="dg-thin" x1="600" y1="220" x2="630" y2="230" stroke-dasharray="3 3"/>\n' + lines(598, 148, ['Yachts without AIS'], 'dg-label small', 'start') + '\n' + lines(616, 252, ['Fishing gear, buoys,', 'swimmers'], 'dg-label small', 'middle')))
    P.append('      <path class="dg-hull" d="M740,262 Q756,226 800,230 Q834,240 816,270 Q780,288 740,262 Z" opacity=".8"/>')
    P.append('      <line class="dg-thin" x1="574" y1="320" x2="846" y2="214" stroke-dasharray="3 4"/>')
    P.append(part('el-shadow', '        <path class="dg-warn-fill shape" d="M852,200 L864,224 L840,224 Z" stroke="var(--dg-line)" stroke-dasharray="3 2"/>\n' + lines(890, 330, ['A ship behind the island:', 'land blocks the signal'], 'dg-label small', 'end') + '\n' + lead(860, 318, 852, 226)))
    P.append(muted(450, 392, 'filled: boats with AIS; outline: without it; dashed edge: an AIS ship you cannot hear'))
    return '\n'.join(P)
