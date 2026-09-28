# Diagram builders for sections/06-engine.html. Bow to the RIGHT in every side view.
import math
from gen_hull_diagrams import part, label, lead, title, muted, bow, marker
from gen_rig_diagrams import marker2, dim

def badge(x, y, n):
    return f'        <circle class="badge__dot" cx="{x}" cy="{y}" r="10"/><text class="badge__n" x="{x}" y="{y+4}" text-anchor="middle">{n}</text>'

def arrow(x, y, deg, cls='dg-flow', s=7):
    # small flow arrowhead pointing along deg (0 = right, 90 = down)
    r = math.radians(deg)
    def pt(dx, dy):
        return f'{x + dx*math.cos(r) - dy*math.sin(r):.1f},{y + dx*math.sin(r) + dy*math.cos(r):.1f}'
    return f'      <path class="{cls}" d="M{pt(s,0)} L{pt(-s,-s*0.8)} L{pt(-s,s*0.8)} Z"/>'

def lines(x, y, texts, cls='dg-label small', anchor=None, step=14):
    return '\n'.join(label(x, y + i*step, t, cls if i == 0 else 'dg-label small', anchor) for i, t in enumerate(texts))

def swatch(x, y, cls, text, extra=''):
    return f'      <line class="{cls}" x1="{x}" y1="{y}" x2="{x+34}" y2="{y}"{extra}/>\n' + muted(x + 44, y + 4, text, 'start')

# ---------------------------------------------------------------- raw-water cooling (viewBox 0 0 900 480)
def cooling():
    H = []
    H.append(title(450, 24, 'Cooling: sea water in, through the heat exchanger, out with the exhaust'))
    H.append(muted(450, 42, 'stern on the left, bow to the right; not to scale; follow the numbers 1 to 8, starting at the seacock on the right'))
    H.append(swatch(24, 62, 'dg-pipe-sea', 'sea water'))
    H.append(swatch(170, 62, 'dg-pipe-hot', 'coolant (fresh water and antifreeze), a closed loop'))
    H.append('      <line class="dg-pipe-exh" x1="580" y1="62" x2="614" y2="62"/><line class="dg-pipe-sea" x1="580" y1="62" x2="614" y2="62" stroke-width="2" stroke-dasharray="5 7"/>')
    H.append(muted(624, 66, 'exhaust gas and sea water together', 'start'))
    P = []
    P.append('      <rect class="dg-water" x="0" y="300" width="900" height="140"/>')
    P.append('      <path class="dg-hull" d="M24,40 L24,318 C70,382 220,414 440,420 L900,420 L900,40"/>')
    P.append('      <line class="dg-waterline" x1="0" y1="300" x2="900" y2="300"/>')
    P.append('      <text class="dg-waterline-label" x="336" y="294" text-anchor="middle">waterline</text>')
    # engine, bed
    P.append('      <rect class="dg-hull-dark" x="370" y="270" width="250" height="12"/>')
    P.append(part('engine-block', '        <rect class="dg-hull-dark shape" x="370" y="160" width="230" height="110" rx="6"/>\n' + lines(485, 212, ['Engine block: the', 'coolant flows through', 'it and takes the heat'], 'dg-label small', 'middle')))
    # coolant loop (red)
    P.append('      <path class="dg-pipe-hot" d="M470,160 V132"/>')
    P.append('      <path class="dg-pipe-hot" d="M584,144 V132"/>')
    P.append('      <path class="dg-pipe-hot" d="M470,160 V174 H584 V160" stroke-dasharray="6 4"/>')
    P.append(arrow(530, 174, 0, 'dg-flow-hot'))
    P.append(arrow(584, 140, -90, 'dg-flow-hot'))
    P.append(arrow(470, 150, 90, 'dg-flow-hot'))
    P.append(part('thermostat', '        <rect class="dg-hull shape" x="572" y="144" width="24" height="16" rx="3"/>\n' + lines(640, 150, ['Thermostat: shuts the', 'coolant in until warm'], 'dg-label small') + '\n' + lead(638, 150, 598, 152)))
    # heat exchanger
    hx = '        <rect class="dg-hull shape" x="440" y="96" width="200" height="36" rx="18"/>' + ''.join(f'<line class="dg-thin" x1="458" y1="{y}" x2="622" y2="{y}"/>' for y in (106, 114, 122))
    P.append(part('heat-exchanger', hx + '\n' + badge(452, 80, 4) + '\n' + lines(470, 72, ['Heat exchanger: sea water in the tubes,', 'coolant around them'], 'dg-label small')))
    P.append(part('header-tank', '        <rect class="dg-hull-dark shape" x="604" y="84" width="20" height="12" rx="2"/>\n' + lines(720, 72, ['Filler cap: open', 'only when cold'], 'dg-label small') + '\n' + lead(718, 72, 624, 88)))
    # raw-water path (blue)
    P.append('      <path class="dg-pipe-sea" d="M700,384 V292"/>')
    P.append('      <path class="dg-pipe-sea" d="M720,244 C770,244 820,250 820,224"/>')
    P.append('      <path class="dg-pipe-sea" d="M820,156 V114 H642"/>')
    P.append('      <path class="dg-pipe-sea" d="M440,114 H400 V100 Q400,76 368,76 Q336,76 336,100 V178"/>')
    for x, y, d in ((700, 340, -90), (770, 246, 5), (820, 136, -90), (730, 114, 180), (420, 114, 180), (336, 140, 90)):
        P.append(arrow(x, y, d))
    P.append(part('cool-seacock', '        <rect class="dg-hull-dark shape" x="688" y="384" width="24" height="34" rx="3"/><line class="dg-line shape" x1="712" y1="392" x2="742" y2="380"/>\n' + badge(674, 398, 1) + '\n' + lines(760, 360, ['Seacock: open it', 'before you start'], 'dg-label small') + '\n' + lead(758, 364, 742, 380)))
    P.append(part('strainer', '        <rect class="dg-sea-fill shape" x="680" y="238" width="40" height="54" rx="6"/><rect class="dg-hull-dark shape" x="676" y="228" width="48" height="10" rx="2"/><path class="dg-thin" d="M688,246 V284 M700,246 V284 M712,246 V284"/>\n' + badge(664, 262, 2) + '\n' + lines(470, 334, ['Strainer: a jar that catches weed and', 'shells. Close the seacock before', 'opening it, wherever it is mounted'], 'dg-label small') + '\n' + lead(640, 330, 682, 292)))
    vanes = ''.join(f'<path class="dg-thin" d="M{820 + 8*math.cos(math.radians(a)):.1f},{190 + 8*math.sin(math.radians(a)):.1f} Q{820 + 22*math.cos(math.radians(a+25)):.1f},{190 + 22*math.sin(math.radians(a+25)):.1f} {820 + 27*math.cos(math.radians(a+50)):.1f},{190 + 27*math.sin(math.radians(a+50)):.1f}" stroke-width="3"/>' for a in range(0, 360, 45))
    P.append(part('impeller-pump', '        <circle class="dg-hull shape" cx="820" cy="190" r="34"/>' + vanes + '<circle class="dg-hull-dark" cx="820" cy="190" r="8"/>\n' + badge(772, 170, 3) + '\n' + lines(890, 262, ['Raw-water pump:', 'a rubber impeller', 'pushes the water on'], 'dg-label small', 'end')))
    P.append(part('anti-siphon', '        <circle class="dg-hull-dark shape" cx="368" cy="76" r="7"/><line class="dg-line" x1="368" y1="69" x2="368" y2="58"/>\n' + badge(392, 58, 5) + '\n' + lines(348, 4, ['Anti-siphon valve: lets air in, so that the', 'sea cannot siphon into the stopped engine'], 'dg-label small', 'end') + '\n' + lead(352, 16, 363, 70)))
    # mixing elbow and wet exhaust
    P.append(part('mixing-elbow', '        <path class="dg-hull-dark shape" d="M370,178 H338 Q310,178 310,206 V228 H332 V210 Q332,200 342,200 H370 Z"/>\n' + badge(350, 240, 6) + '\n' + lines(228, 124, ['Mixing elbow:', 'sea water is', 'sprayed into', 'the exhaust'], 'dg-label small')))
    P.append('      <path class="dg-pipe-exh" d="M321,228 C321,256 300,266 272,266"/>')
    P.append('      <path class="dg-pipe-exh" d="M212,250 V96 Q212,70 186,70 Q160,70 160,96 V230 Q160,250 140,250 H26"/>')
    P.append('      <path class="dg-pipe-sea" d="M321,228 C321,256 300,266 272,266 M212,250 V96 Q212,70 186,70 Q160,70 160,96 V230 Q160,250 140,250 H26" stroke-width="2" stroke-dasharray="5 7"/>')
    P.append(part('waterlock', '        <rect class="dg-hull-dark shape" x="190" y="250" width="82" height="62" rx="8"/>\n' + badge(284, 322, 7) + '\n' + lines(238, 346, ['Waterlock: a box that', 'catches the water so it', 'cannot run back'], 'dg-label small', 'middle')))
    P.append(part('exhaust-loop', '        <path class="shape-fill" d="M154,96 Q154,62 186,62 Q218,62 218,96 V120 H154 Z"/>\n' + lines(36, 96, ['High loop', '(gooseneck)'], 'dg-label small', 'start') + '\n' + lead(112, 96, 156, 90)))
    P.append(part('exhaust-outlet', '        <rect class="dg-hull-dark shape" x="20" y="242" width="10" height="16" rx="2"/>\n' + badge(46, 232, 8) + '\n' + lines(36, 278, ['Outlet: check water', 'is coming out'], 'dg-label small', 'start')))
    return '\n'.join(H) + '\n      <g transform="translate(0,86)">\n' + '\n'.join(P) + '\n      </g>'

# ---------------------------------------------------------------- fuel system (viewBox 0 0 900 400)
def fuel():
    P = []
    P.append(title(450, 24, 'Fuel: from the tank to the injectors, and where to bleed the air out'))
    P.append(muted(450, 42, 'schematic: the order of the parts is the same on almost every small diesel; where they sit on the engine differs'))
    P.append('      <line class="dg-line" x1="20" y1="84" x2="150" y2="84"/>')
    P.append(muted(24, 78, 'deck', 'start'))
    # tank
    P.append(part('fuel-tank', '        <rect class="dg-hull shape" x="40" y="150" width="190" height="150" rx="6"/><rect class="dg-fuel-fill" x="42" y="196" width="186" height="102" rx="4"/>\n' + lines(135, 176, ['Fuel tank'], 'dg-label', 'middle')))
    P.append(part('tank-sludge', '        <path class="dg-bad-fill shape" d="M44,286 H226 V296 Q226,298 224,298 H46 Q44,298 44,296 Z" opacity=".55"/>\n' + lines(20, 330, ['Water and sludge settle at the bottom;', 'rough seas stir them up'], 'dg-label small', 'start') + '\n' + lead(80, 318, 90, 298)))
    P.append(part('fuel-filler', '        <rect class="dg-hull-dark shape" x="56" y="76" width="30" height="8" rx="2"/><path class="dg-line" d="M71,84 V150" stroke-width="6"/>\n' + lines(78, 112, ['Filler'], 'dg-label small', 'start')))
    P.append(part('tank-vent', '        <path class="dg-thin shape" d="M122,150 V70 Q122,58 110,58 Q102,58 102,66" stroke-width="2.5"/>\n' + lines(130, 64, ['Vent'], 'dg-label small', 'start')))
    P.append(part('fuel-pickup', '        <path class="dg-pipe-fuel shape" d="M206,150 V270"/>\n' + lines(196, 236, ['Pickup'], 'dg-label small', 'end')))
    # supply line
    P.append('      <path class="dg-pipe-fuel" d="M206,150 V122 H330 V170"/>')
    P.append(part('fuel-shutoff', '        <path class="dg-hull-dark shape" d="M252,112 L272,132 L272,112 L252,132 Z"/><line class="dg-line" x1="262" y1="122" x2="262" y2="102"/>\n' + lines(262, 150, ['Shut-off valve'], 'dg-label small', 'middle')))
    P.append(part('primary-filter', '        <rect class="dg-hull-dark shape" x="306" y="170" width="48" height="26" rx="3"/><rect class="dg-sea-fill shape" x="310" y="196" width="40" height="64" rx="8"/><rect class="dg-fuel-fill" x="312" y="198" width="36" height="42" rx="6"/><line class="dg-line" x1="330" y1="260" x2="330" y2="272"/>\n' + lines(282, 294, ['Primary filter and water', 'separator: water sinks into', 'the bowl; drain it. After a', 'change, fill it with clean fuel'], 'dg-label small', 'start')))
    P.append('      <path class="dg-pipe-fuel" d="M354,182 H430"/>')
    P.append(part('lift-pump', '        <rect class="dg-hull-dark shape" x="430" y="166" width="46" height="34" rx="5"/><line class="dg-line shape" x1="476" y1="194" x2="498" y2="214" stroke-width="3"/>\n' + lines(424, 232, ['Lift pump, with a hand', 'priming lever'], 'dg-label small', 'start') + '\n' + lead(450, 222, 452, 202)))
    P.append('      <path class="dg-pipe-fuel" d="M476,176 H540 V178"/>')
    P.append(part('engine-filter', '        <rect class="dg-hull-dark shape" x="522" y="120" width="40" height="12" rx="2"/><rect class="dg-hull shape" x="526" y="132" width="32" height="46" rx="6"/><circle class="dg-accent-fill" cx="552" cy="116" r="4"/>\n' + badge(576, 102, 1) + '\n' + lines(504, 206, ['Engine fuel filter', '(fine filter)'], 'dg-label small', 'start') + '\n' + lead(534, 196, 540, 180)))
    P.append('      <path class="dg-pipe-fuel" d="M530,120 V96 H660 V150"/>')
    P.append(part('injection-pump', '        <rect class="dg-hull-dark shape" x="624" y="150" width="96" height="60" rx="6"/><circle class="dg-accent-fill" cx="640" cy="160" r="4"/>\n' + badge(612, 138, 2) + '\n' + lines(620, 236, ['Injection pump: raises', 'the fuel to very high', 'pressure, one cylinder', 'at a time'], 'dg-label small', 'start')))
    hp = ''
    for i, x in enumerate((780, 820, 860)):
        hp += f'<path class="dg-pipe-hp" d="M{700 - i*18},150 V{128 - i*8} H{x} V104"/>'
    P.append(part('hp-pipes', '        ' + hp + '\n' + lines(740, 170, ['High-pressure pipes: loosen', 'only to bleed, with a rag', 'round the nut, face and', 'hands clear of the spray'], 'dg-label small', 'start')))
    inj = ''.join(f'<rect class="dg-hull-dark shape" x="{x-7}" y="74" width="14" height="30" rx="3"/><path class="dg-hull-dark" d="M{x-3},104 L{x+3},104 L{x},114 Z"/>' for x in (780, 820, 860))
    P.append(part('injectors', '        ' + inj + '\n' + badge(754, 70, 3) + ''.join(f'<circle class="dg-accent-fill" cx="{x}" cy="108" r="3.5"/>' for x in (788, 828, 868)) + '\n' + lines(880, 128, ['Injectors'], 'dg-label small', 'end')))
    P.append(part('leak-off', '        <path class="dg-pipe-ret shape" d="M780,74 V62 H150 V150"/>\n' + lines(400, 56, ['Return (leak-off) line: fuel the injectors did not use goes back to the tank'], 'dg-label small', 'start')))
    P.append(arrow(300, 122, 0, 'dg-flow-fuel'))
    P.append(arrow(400, 182, 0, 'dg-flow-fuel'))
    P.append(arrow(600, 96, 0, 'dg-flow-fuel'))
    P.append(arrow(360, 62, 180, 'dg-flow-fuel'))
    P.append('      <circle class="dg-accent-fill" cx="30" cy="372" r="4"/>')
    P.append(muted(40, 376, 'bleed point. After running out of fuel or changing a filter, bleed 1 and then 2 with the priming lever:', 'start'))
    P.append(muted(40, 392, 'each opened until fuel comes out with no bubbles, then closed. Point 3 only if it still will not start, by cranking.', 'start'))
    return '\n'.join(P)

# ---------------------------------------------------------------- shaft drive and saildrive (viewBox 0 0 900 380)
def drives():
    P = []
    P.append(title(225, 26, 'Shaft drive'))
    P.append(title(675, 26, 'Saildrive'))
    P.append('      <line class="dg-thin" x1="450" y1="40" x2="450" y2="350" stroke-dasharray="3 5"/>')
    # --- shaft panel; hull bottom is the straight line y = 196 + (x-20)*0.2207
    P.append('      <rect class="dg-water" x="0" y="150" width="446" height="210"/>')
    P.append('      <path class="dg-hull" d="M20,60 L20,196 L446,290 L446,60"/>')
    P.append('      <line class="dg-waterline" x1="0" y1="150" x2="446" y2="150"/>')
    P.append(part('engine-block', '        <rect class="dg-hull-dark shape" x="300" y="160" width="120" height="70" rx="6"/>\n' + label(360, 200, 'Engine', 'dg-label small', 'middle')))
    P.append(part('gearbox', '        <rect class="dg-hull shape" x="262" y="176" width="38" height="44" rx="4"/>\n' + lines(282, 120, ['Gearbox'], 'dg-label small', 'middle') + '\n' + lead(282, 124, 282, 174)))
    P.append(part('engine-mounts', '        <rect class="dg-sail-2 shape" x="308" y="230" width="20" height="12" rx="3"/><rect class="dg-sail-2 shape" x="392" y="230" width="20" height="12" rx="3"/>\n' + lines(372, 257, ['Flexible mounts'], 'dg-label small', 'middle')))
    P.append(part('shaft-coupling', '        <rect class="dg-hull-dark shape" x="246" y="190" width="14" height="22" rx="2"/>\n' + lines(222, 96, ['Flexible coupling'], 'dg-label small', 'middle') + '\n' + lead(230, 100, 252, 188)))
    P.append(part('prop-shaft', '        <line class="dg-line shape" x1="246" y1="201" x2="96" y2="246" stroke-width="5"/>\n        <line class="hit" x1="246" y1="201" x2="96" y2="246"/>\n' + lines(150, 150, ['Shaft'], 'dg-label small', 'middle') + '\n' + lead(154, 154, 200, 212)))
    P.append(part('shaft-gland', '        <rect class="dg-sail-2 shape" x="170" y="212" width="24" height="18" rx="3" transform="rotate(-17 182 221)"/>\n' + lines(210, 300, ['Stern gland: seals the', 'shaft where it leaves the hull'], 'dg-label small', 'start') + '\n' + lead(214, 290, 186, 230)))
    P.append(part('cutless', '        <path class="dg-hull-dark shape" d="M122,218 L128,218 L126,236 L118,236 Z"/><rect class="dg-hull-dark shape" x="106" y="234" width="30" height="12" rx="3" transform="rotate(-17 121 240)"/>\n' + lines(40, 330, ['P-bracket and cutless bearing: a', 'rubber-lined bearing near the propeller'], 'dg-label small', 'start') + '\n' + lead(110, 318, 118, 248)))
    P.append(part('propeller-en', '        <path class="dg-hull-dark shape" d="M94,246 L88,220 L82,222 L86,248 L82,272 L88,274 L94,250 Z"/>\n' + lines(64, 136, ['Propeller'], 'dg-label small', 'middle') + '\n' + lead(66, 140, 86, 220)))
    P.append(part('en-rudder', '        <path class="dg-hull-dark shape" d="M34,199 L58,204 L54,286 L32,280 Z"/>\n' + lines(24, 302, ['Rudder'], 'dg-label small', 'start')))
    P.append(muted(236, 372, 'the shaft slopes down, so the thrust is angled slightly'))
    # --- saildrive panel
    P.append('      <rect class="dg-water" x="454" y="150" width="446" height="210"/>')
    P.append('      <path class="dg-hull" d="M470,60 L470,176 C520,200 600,226 700,240 C780,250 840,254 900,254 L900,60"/>')
    P.append('      <line class="dg-waterline" x1="454" y1="150" x2="900" y2="150"/>')
    P.append(part('engine-block', '        <rect class="dg-hull-dark shape" x="660" y="130" width="130" height="70" rx="6"/>\n' + label(725, 170, 'Engine', 'dg-label small', 'middle')))
    P.append(part('sd-leg', '        <path class="dg-hull shape" d="M624,150 H660 V196 L654,204 L652,284 L632,284 L628,204 L624,196 Z"/><rect class="dg-hull shape" x="622" y="280" width="46" height="20" rx="10"/>\n' + lines(540, 96, ['Saildrive leg: gearbox and a', 'right-angle drive in one unit'], 'dg-label small', 'start') + '\n' + lead(600, 104, 636, 150)))
    P.append(part('sd-diaphragm', '        <path class="dg-sail-2 shape" d="M614,226 L666,232 L664,242 L612,236 Z"/>\n' + lines(700, 290, ['Rubber diaphragm: seals the', 'leg where it passes through', 'the hull; renewed on the', 'maker’s schedule'], 'dg-label small', 'start') + '\n' + lead(698, 286, 664, 238)))
    P.append(part('sd-anode', '        <rect class="dg-warn-fill shape" x="630" y="256" width="24" height="10" rx="3"/>\n' + lines(700, 354, ['Anode: protects the leg'], 'dg-label small', 'start') + '\n' + lead(698, 350, 654, 264)))
    P.append(part('propeller-en', '        <rect class="dg-hull-dark shape" x="610" y="283" width="14" height="14" rx="4"/><path class="dg-hull-dark shape" d="M616,284 L612,258 L606,260 L610,286 L606,312 L612,314 L616,290 Z"/>\n' + lines(596, 244, ['Propeller'], 'dg-label small', 'end') + '\n' + lead(582, 248, 608, 262)))
    P.append(part('en-rudder', '        <path class="dg-hull-dark shape" d="M488,185 L510,192 L506,272 L486,266 Z"/>\n' + lines(480, 300, ['Rudder'], 'dg-label small', 'start')))
    P.append(muted(676, 372, 'the thrust is level and the engine sits further forward'))
    P.append(bow(890, 76))
    P.append(bow(440, 76))
    return '\n'.join(P)

# ---------------------------------------------------------------- stern glands (viewBox 0 0 900 320)
def stern_glands():
    P = []
    P.append(title(450, 20, 'Three kinds of stern gland, cut open along the shaft'))
    P.append('      <line class="dg-thin" x1="300" y1="40" x2="300" y2="272" stroke-dasharray="3 5"/><line class="dg-thin" x1="600" y1="40" x2="600" y2="272" stroke-dasharray="3 5"/>')
    def tube(x0, x1):
        return (f'      <rect class="dg-sea-fill" x="{x0}" y="154" width="{x1-x0}" height="32"/>'
                f'<rect class="dg-hull-dark" x="{x0}" y="144" width="{x1-x0}" height="10"/><rect class="dg-hull-dark" x="{x0}" y="186" width="{x1-x0}" height="10"/>')
    def shaft(x0, x1):
        return f'      <rect class="dg-hull" x="{x0}" y="162" width="{x1-x0}" height="16"/>'
    def clip(x):
        return f'<rect class="dg-thin" x="{x}" y="136" width="8" height="68" rx="2" stroke-width="2"/>'
    # 1 packed stuffing box
    P.append(title(150, 48, 'Packed stuffing box'))
    P.append(tube(16, 96))
    P.append(muted(56, 132, 'stern tube'))
    P.append(part('gland-hose', '        <rect class="dg-sail-2 shape" x="96" y="140" width="56" height="60" rx="4"/>' + clip(99) + clip(110) + clip(130) + clip(141) + '\n' + lines(92, 236, ['Hose, two clips', 'at each end'], 'dg-label small', 'start') + '\n' + lead(124, 224, 124, 202)))
    P.append(part('packing', '        <rect class="dg-hull-dark shape" x="152" y="136" width="56" height="68" rx="3"/>' + ''.join(f'<rect class="dg-sail-2" x="{x}" y="152" width="10" height="10"/><rect class="dg-sail-2" x="{x}" y="178" width="10" height="10"/>' for x in (160, 174, 188)) + '\n' + lines(16, 86, ['Packing rings', '(greased flax or PTFE)'], 'dg-label small', 'start') + '\n' + lead(120, 100, 176, 150)))
    P.append(part('follower', '        <rect class="dg-hull shape" x="208" y="146" width="20" height="48" rx="2"/><path class="dg-line shape" d="M196,142 H246 M196,198 H246"/><rect class="dg-hull-dark shape" x="236" y="136" width="10" height="12"/><rect class="dg-hull-dark shape" x="236" y="192" width="10" height="12"/>\n' + lines(292, 100, ['Follower and nuts:', 'squeeze the packing'], 'dg-label small', 'end') + '\n' + lead(250, 114, 240, 134)))
    P.append(shaft(10, 292))
    P.append(part('gland-drip', '        <path class="dg-flow shape" d="M222,208 C216,218 216,224 222,224 C228,224 228,218 222,208 Z"/><path class="dg-flow" d="M222,236 C218,242 218,246 222,246 C226,246 226,242 222,236 Z"/>\n' + lines(292, 280, ['Meant to drip slowly', 'while the shaft turns'], 'dg-label small', 'end') + '\n' + lead(240, 268, 224, 248)))
    # 2 face seal
    P.append(title(450, 48, 'Face seal (PSS type)'))
    P.append(tube(316, 386))
    P.append(muted(350, 132, 'stern tube'))
    bel = 'M386,140 ' + ' '.join(f'L{386 + 8*i},{140 if i % 2 == 0 else 132}' for i in range(1, 10)) + ' L458,200 ' + ' '.join(f'L{458 - 8*i},{200 if i % 2 == 0 else 208}' for i in range(1, 10)) + ' Z'
    P.append(part('bellows', f'        <path class="dg-sail-2 shape" d="{bel}"/>' + clip(390) + '\n' + lines(316, 250, ['Rubber bellows, compressed:', 'it pushes the carbon ring', 'against the collar'], 'dg-label small', 'start') + '\n' + lead(400, 238, 410, 210)))
    P.append(part('carbon-face', '        <rect class="dg-hull-dark shape" x="458" y="136" width="14" height="68" rx="2"/><path class="dg-thin" d="M465,136 V100" stroke-width="2.5"/>\n' + lines(454, 80, ['Carbon ring; the small', 'hose lets trapped air out'], 'dg-label small', 'end') + '\n' + lead(456, 88, 464, 100)))
    P.append(shaft(306, 592))
    P.append(part('seal-collar', '        <rect class="dg-hull shape" x="472" y="150" width="30" height="40" rx="2"/><circle class="dg-hull-dark" cx="487" cy="156" r="3"/><circle class="dg-hull-dark" cx="487" cy="184" r="3"/>\n' + lines(592, 80, ['Stainless collar,', 'screwed to the shaft;', 'turns with it'], 'dg-label small', 'end') + '\n' + lead(530, 112, 494, 150)))
    # 3 lip seal
    P.append(title(750, 48, 'Lip seal (Volvo type)'))
    P.append(tube(616, 716))
    P.append(muted(650, 132, 'stern tube'))
    P.append(shaft(606, 892))
    P.append(part('lip-seal', '        <path class="dg-sail-2 shape" d="M696,138 H800 Q812,138 812,150 V160 L798,162 V152 H716 V144 H696 Z M696,202 H800 Q812,202 812,190 V180 L798,178 V188 H716 V196 H696 Z"/>' + clip(700) + clip(724) + '<path class="dg-hull-dark" d="M784,152 L792,162 L776,162 Z M784,188 L792,178 L776,178 Z"/>\n' + lines(760, 92, ['Rubber seal slid over the stern', 'tube; its lips run on the shaft'], 'dg-label small', 'middle') + '\n' + lead(780, 104, 790, 138)))
    P.append(part('seal-grease', '        <rect class="dg-warn-fill shape" x="760" y="152" width="14" height="10" opacity=".7"/><rect class="dg-warn-fill shape" x="760" y="178" width="14" height="10" opacity=".7"/>\n' + lines(890, 250, ['Grease between the lips;', 'air is let out (“burped”)', 'after every launch'], 'dg-label small', 'end') + '\n' + lead(830, 238, 768, 190)))
    return '\n'.join(P)

# ---------------------------------------------------------------- propellers (viewBox 0 0 900 300)
def propellers():
    P = []
    def blade3(cx, cy, r, cls, extra=''):
        out = ''
        for a in (-90, 30, 150):
            out += f'<ellipse class="{cls}" cx="{cx + r*0.55*math.cos(math.radians(a)):.1f}" cy="{cy + r*0.55*math.sin(math.radians(a)):.1f}" rx="{r*0.5:.1f}" ry="{r*0.24:.1f}" transform="rotate({a} {cx + r*0.55*math.cos(math.radians(a)):.1f} {cy + r*0.55*math.sin(math.radians(a)):.1f})"{extra}/>'
        return out + f'<circle class="dg-hull" cx="{cx}" cy="{cy}" r="{r*0.18:.1f}"/>'
    P.append(title(150, 30, 'Fixed'))
    P.append(part('prop-fixed', '        ' + blade3(150, 130, 80, 'dg-hull-dark shape') + '\n' + lines(150, 238, ['Blades always open: simple and', 'strong, but the most drag when sailing'], 'dg-label small', 'middle')))
    P.append(muted(150, 48, 'seen from astern'))
    # folding: side view, shaft horizontal, blades open (solid) and folded (ghost)
    P.append(title(450, 30, 'Folding'))
    P.append(muted(450, 48, 'seen from the side, bow to the right'))
    P.append('      <rect class="dg-hull" x="420" y="124" width="120" height="12"/>')
    P.append(part('prop-folding', '        <rect class="dg-hull-dark shape" x="396" y="118" width="28" height="24" rx="8"/><path class="dg-hull-dark shape" d="M410,122 L402,62 L414,60 L420,120 Z M410,138 L402,198 L414,200 L420,140 Z"/><path class="dg-hull-dark" d="M398,120 L340,112 L338,122 L398,128 Z M398,140 L340,148 L338,138 L398,132 Z" opacity=".35" stroke-dasharray="4 3"/>\n' + lines(450, 238, ['The spinning shaft swings the blades open; when', 'sailing, the water folds them shut behind the hub'], 'dg-label small', 'middle') + '\n' + muted(350, 104, 'folded', 'middle')))
    # feathering: from astern, blades rotated edge-on (thin) when sailing
    P.append(title(750, 30, 'Feathering'))
    P.append(muted(750, 48, 'seen from astern'))
    thin = ''
    for a in (-90, 30, 150):
        cx, cy = 750 + 44*math.cos(math.radians(a)), 130 + 44*math.sin(math.radians(a))
        thin += f'<ellipse class="dg-hull-dark shape" cx="{cx:.1f}" cy="{cy:.1f}" rx="40" ry="5" transform="rotate({a} {cx:.1f} {cy:.1f})"/>'
    P.append(part('prop-feathering', '        ' + blade3(750, 130, 80, 'dg-hull-dark', ' opacity=".25"') + thin + '<circle class="dg-hull" cx="750" cy="130" r="14"/>\n' + lines(750, 238, ['Blades turn edge-on to the water when', 'sailing (solid); pale outline: under power'], 'dg-label small', 'middle')))
    return '\n'.join(P)

# ---------------------------------------------------------------- engine tour (viewBox 0 0 900 470)
def engine_tour():
    P = []
    P.append(title(450, 24, 'A small marine diesel, seen from the side you service it from'))
    P.append(muted(450, 42, 'bow to the right, so the belt end faces forward; every make puts things in slightly different places'))
    # bed, mounts, feet
    P.append('      <rect class="dg-hull-dark" x="200" y="392" width="520" height="12"/>')
    P.append(part('engine-mounts', '        <path class="dg-line" d="M300,338 H280 V364 M620,338 H640 V364"/><rect class="dg-sail-2 shape" x="262" y="364" width="36" height="28" rx="5"/><rect class="dg-sail-2 shape" x="622" y="364" width="36" height="28" rx="5"/>\n' + lines(690, 444, ['Engine mounts: rubber', 'blocks on the engine bed'], 'dg-label small', 'start') + '\n' + lead(688, 440, 650, 394)))
    # block, sump, head, rocker cover
    P.append('      <rect class="dg-hull" x="300" y="200" width="320" height="150" rx="4"/>')
    P.append(part('sump', '        <path class="dg-hull-dark shape" d="M320,350 H600 V366 Q600,378 588,378 H332 Q320,378 320,366 Z"/>\n' + lines(560, 444, ['Sump: the oil', 'lives here'], 'dg-label small', 'start') + '\n' + lead(580, 432, 560, 378)))
    P.append('      <rect class="dg-hull-dark" x="310" y="160" width="300" height="40" rx="3"/>')
    P.append('      <rect class="dg-hull" x="320" y="130" width="280" height="30" rx="8"/>')
    P.append(part('oil-filler', '        <rect class="dg-hull-dark shape" x="350" y="118" width="26" height="12" rx="3"/>\n' + lines(300, 64, ['Oil filler cap'], 'dg-label small', 'start') + '\n' + lead(340, 68, 360, 118)))
    P.append(part('air-intake', '        <rect class="dg-hull-dark shape" x="420" y="104" width="80" height="26" rx="10"/>\n' + lines(420, 64, ['Air intake and filter'], 'dg-label small', 'start') + '\n' + lead(460, 68, 460, 104)))
    # heat exchanger with filler cap
    P.append(part('heat-exchanger', '        <rect class="dg-hull shape" x="540" y="96" width="150" height="32" rx="16"/>' + ''.join(f'<line class="dg-thin" x1="556" y1="{y}" x2="674" y2="{y}"/>' for y in (106, 118)) + '\n' + lines(580, 64, ['Heat exchanger'], 'dg-label small', 'start') + '\n' + lead(600, 68, 600, 96)))
    P.append(part('header-tank', '        <rect class="dg-hull-dark shape" x="650" y="84" width="20" height="12" rx="2"/>\n' + lines(720, 64, ['Coolant filler cap:', 'open only when cold'], 'dg-label small', 'start') + '\n' + lead(718, 64, 668, 86)))
    P.append(part('thermostat', '        <rect class="dg-hull-dark shape" x="610" y="160" width="26" height="22" rx="3"/>\n' + lines(598, 152, ['Thermostat'], 'dg-label small', 'end') + '\n' + lead(600, 154, 612, 166)))
    # front end: alternator, belt, crank pulley, raw-water pump
    P.append(part('alternator', '        <rect class="dg-hull-dark shape" x="636" y="166" width="62" height="44" rx="16"/><rect class="dg-hull shape" x="696" y="174" width="12" height="28" rx="2"/>\n' + lines(740, 186, ['Alternator: charges', 'the batteries'], 'dg-label small', 'start') + '\n' + lead(738, 182, 708, 186)))
    P.append(part('drive-belt', '        <rect class="dg-line shape" x="699" y="188" width="6" height="120" fill="currentColor" style="fill:var(--dg-line)"/><rect class="dg-hull shape" x="696" y="286" width="12" height="44" rx="2"/>\n' + lines(740, 244, ['Drive belt, seen edge-on,', 'round the crankshaft pulley'], 'dg-label small', 'start') + '\n' + lead(738, 240, 706, 250)))
    P.append(part('impeller-pump', '        <rect class="dg-hull-dark shape" x="636" y="292" width="50" height="38" rx="10"/><circle class="dg-hull" cx="661" cy="311" r="11"/>\n' + lines(740, 316, ['Raw-water pump: the', 'impeller is behind', 'the cover plate'], 'dg-label small', 'start') + '\n' + lead(738, 312, 686, 312)))
    # raw-water hoses
    P.append('      <path class="dg-pipe-sea" d="M661,330 V430"/>')
    P.append(arrow(661, 400, -90))
    P.append(muted(672, 428, 'from the strainer', 'start'))
    P.append('      <path class="dg-pipe-sea" d="M672,292 V254 Q672,240 690,240 H716 V126 Q716,112 692,112"/>')
    P.append('      <path class="dg-pipe-sea" d="M540,104 Q520,86 490,86 H290 Q262,86 262,112 V172"/>')
    P.append(arrow(400, 86, 180))
    # exhaust elbow and hose
    P.append(part('mixing-elbow', '        <path class="dg-hull-dark shape" d="M312,170 H258 Q236,170 236,192 V214 H256 V198 Q256,192 264,192 H312 Z"/>\n' + lines(16, 118, ['Exhaust (mixing) elbow:', 'sea water joins the', 'exhaust here'], 'dg-label small', 'start') + '\n' + lead(150, 140, 240, 180)))
    P.append('      <path class="dg-pipe-exh" d="M246,214 Q246,234 222,234 H140"/><path class="dg-pipe-sea" d="M246,214 Q246,234 222,234 H140" stroke-width="2" stroke-dasharray="5 7"/>')
    P.append(muted(132, 238, 'to the waterlock', 'end'))
    # gearbox, coupling, shaft, gear cable
    P.append('      <rect class="dg-hull-dark" x="282" y="210" width="18" height="140" rx="3"/>')
    P.append(part('gearbox', '        <rect class="dg-hull shape" x="200" y="250" width="82" height="80" rx="6"/><rect class="dg-hull-dark shape" x="186" y="276" width="14" height="28" rx="2"/>\n' + lines(150, 274, ['Gearbox'], 'dg-label small', 'end') + '\n' + lead(152, 270, 206, 276)))
    P.append(part('shaft-coupling', '        <rect class="dg-hull-dark shape" x="168" y="280" width="18" height="20" rx="2"/>\n' + lines(16, 320, ['Flexible coupling,', 'then the shaft'], 'dg-label small', 'start') + '\n' + lead(112, 316, 172, 300)))
    P.append('      <line class="dg-line" x1="168" y1="290" x2="20" y2="300" stroke-width="5"/>')
    P.append(part('gear-cable', '        <line class="dg-line shape" x1="240" y1="312" x2="226" y2="296" stroke-width="3"/><path class="dg-thin shape" d="M240,312 C240,368 160,372 60,374" stroke-width="2"/>\n        <path class="hit" d="M240,312 C240,368 160,372 60,374"/>\n' + lines(16, 394, ['Gear cable, from the', 'lever in the cockpit'], 'dg-label small', 'start')))
    # engine-side parts
    P.append(part('starter-motor', '        <rect class="dg-hull-dark shape" x="302" y="300" width="54" height="28" rx="12"/>\n' + lines(300, 444, ['Starter motor'], 'dg-label small', 'start') + '\n' + lead(330, 432, 330, 328)))
    P.append(part('oil-filter', '        <rect class="dg-hull-dark shape" x="370" y="286" width="34" height="50" rx="7"/>\n' + lines(390, 426, ['Oil filter'], 'dg-label small', 'start') + '\n' + lead(400, 414, 388, 338)))
    P.append(part('dipstick', '        <rect class="dg-hull-dark shape" x="418" y="204" width="7" height="60"/><circle class="dg-line shape" cx="421.5" cy="198" r="6" fill="none"/>\n' + lines(410, 238, ['Dipstick'], 'dg-label small', 'end')))
    P.append(part('lift-pump', '        <rect class="dg-hull-dark shape" x="444" y="262" width="32" height="28" rx="4"/><line class="dg-line shape" x1="476" y1="284" x2="492" y2="300" stroke-width="3"/>\n' + lines(470, 444, ['Lift pump, with', 'priming lever'], 'dg-label small', 'start') + '\n' + lead(480, 432, 462, 292)))
    P.append('      <path class="dg-pipe-fuel" d="M452,430 V290"/>')
    P.append(arrow(452, 400, -90, 'dg-flow-fuel'))
    P.append('      <path class="dg-pipe-fuel" d="M468,262 V214 Q468,206 476,206 H574"/>')
    P.append('      <path class="dg-pipe-fuel" d="M589,256 V268 H560"/>')
    P.append(part('engine-filter', '        <rect class="dg-hull shape" x="574" y="206" width="30" height="50" rx="6"/><circle class="dg-accent-fill" cx="598" cy="212" r="3.5"/>\n' + lines(608, 276, ['Fuel filter'], 'dg-label small', 'start') + '\n' + lead(612, 266, 600, 256)))
    P.append(part('injection-pump', '        <rect class="dg-hull-dark shape" x="490" y="226" width="70" height="54" rx="5"/><line class="dg-line shape" x1="560" y1="236" x2="578" y2="222" stroke-width="3"/>\n' + lines(484, 326, ['Injection pump, with', 'the throttle lever'], 'dg-label small', 'start') + '\n' + lead(498, 316, 498, 282)))
    P.append(part('stop-control', '        <line class="dg-line shape" x1="556" y1="276" x2="574" y2="290" stroke-width="3"/><circle class="dg-bad-fill shape" cx="576" cy="292" r="4"/>\n' + lines(568, 302, ['Stop lever'], 'dg-label small', 'end') + '\n' + lead(570, 298, 572, 293)))
    hp = ''.join(f'<path class="dg-pipe-hp" d="M{500 + i*20},226 V{214 - i*4} H{x} V186"/>' for i, x in enumerate((380, 460, 540)))
    inj = ''.join(f'<rect class="dg-hull-dark shape" x="{x-6}" y="166" width="12" height="20" rx="3"/>' for x in (380, 460, 540))
    P.append(part('injectors', '        ' + inj + hp + '\n' + lines(430, 152, ['Injectors'], 'dg-label small', 'middle') + '\n' + lead(440, 155, 456, 166)))
    return '\n'.join(P)
