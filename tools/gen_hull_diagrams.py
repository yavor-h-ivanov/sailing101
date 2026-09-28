# Diagram builders for sections/03-hull.html (imported by gen_hull.py). Bow to the RIGHT in every profile view.
def part(term, body, extra=''):
    return f'      <g class="part" data-term="{term}"{extra}>\n{body}\n      </g>'
def label(x, y, text, cls='dg-label', anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ''
    return f'        <text class="{cls}" x="{x}" y="{y}"{a}>{text}</text>'
def lead(x1, y1, x2, y2, cls='dg-lead'):
    return f'        <line class="{cls}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>'
def title(x, y, t):
    return f'      <text class="dg-title" x="{x}" y="{y}" text-anchor="middle">{t}</text>'
def muted(x, y, t, anchor='middle'):
    return f'      <text class="dg-muted" x="{x}" y="{y}" text-anchor="{anchor}">{t}</text>'
def bow(x, y):
    return f'      <text class="dg-muted" x="{x}" y="{y}" text-anchor="end">bow →</text>'
def marker(mid):
    return f'      <defs><marker id="{mid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 Z" class="dg-arrow"/></marker></defs>'

# ---------------------------------------------------------------- laminate (viewBox 0 0 940 360)
def laminate():
    P = [marker('lam-arrow')]
    P.append(title(210, 26, 'Solid GRP hull, magnified'))
    P.append(muted(210, 44, 'outside of the boat on the left'))
    P.append('      <rect class="dg-water" x="30" y="60" width="60" height="220"/>')
    P.append(muted(60, 176, 'sea'))
    P.append(part('gelcoat', '        <rect class="dg-hull-dark shape" x="90" y="60" width="14" height="220"/>\n' + label(97, 298, 'Gelcoat', 'dg-label small', 'middle')))
    layers = ''
    bands = [(104, 22, 'csm'), (126, 30, 'wr'), (156, 22, 'csm'), (178, 30, 'wr'), (208, 22, 'csm'), (230, 30, 'wr'), (260, 20, 'csm')]
    for x, w, kind in bands:
        fill = 'dg-hull' if kind == 'csm' else 'dg-hull-dark'
        layers += f'<rect class="{fill} shape" x="{x}" y="60" width="{w}" height="220" opacity="{".9" if kind=="csm" else ".55"}"/>'
        if kind == 'wr':
            layers += f'<path class="dg-thin" d="M{x+4},64 V276 M{x+12},64 V276 M{x+20},64 V276" opacity=".5"/>'
    P.append(part('laminate', '        ' + layers + '\n' + label(190, 316, 'Laminate: alternating layers of mat and cloth', 'dg-label small', 'middle')))
    P.append(part('csm', '        <rect class="shape-fill" x="156" y="60" width="22" height="220"/>\n' + label(300, 110, 'Chopped-strand mat') + '\n' + label(300, 124, '(short fibres, resin-rich)', 'dg-muted', 'start') + '\n' + lead(298, 108, 168, 120)))
    P.append(part('woven-roving', '        <rect class="shape-fill" x="178" y="60" width="30" height="220"/>\n' + label(300, 200, 'Woven roving') + '\n' + label(300, 214, '(heavy cloth, strong)', 'dg-muted', 'start') + '\n' + lead(298, 198, 195, 210)))
    P.append('      <rect class="dg-hull" x="280" y="60" width="10" height="220" opacity=".5"/>')
    P.append(muted(285, 296, 'inside'))
    P.append(muted(190, 338, 'thickest along the keel and at the bow, thinnest in the topsides'))
    # cored deck
    P.append(title(640, 26, 'Cored deck, magnified'))
    P.append(muted(640, 44, 'deck surface at the top, cabin below'))
    P.append(part('gelcoat', '        <rect class="dg-hull-dark shape" x="480" y="78" width="320" height="10"/>\n' + label(810, 86, 'Gelcoat', 'dg-label small')))
    P.append(part('outer-skin', '        <rect class="dg-hull shape" x="480" y="88" width="320" height="18"/>\n' + label(810, 101, 'Outer skin', 'dg-label small')))
    core = '<rect class="dg-sail-2 shape" x="480" y="106" width="320" height="44"/>' + ''.join(f'<path class="dg-thin" d="M{x},106 V150" opacity=".4"/>' for x in range(500, 800, 26))
    P.append(part('core', '        ' + core + '\n' + label(810, 132, 'Core: balsa or ply', 'dg-label small')))
    P.append(part('inner-skin', '        <rect class="dg-hull shape" x="480" y="150" width="320" height="14"/>\n' + label(810, 161, 'Inner skin', 'dg-label small')))
    P.append(muted(750, 184, 'cabin'))
    P.append(part('deck-fitting', '        <rect class="dg-hull-dark shape" x="570" y="64" width="60" height="14" rx="2"/><rect class="dg-hull-dark shape" x="596" y="52" width="8" height="12"/>\n        <path class="dg-line shape" d="M588,64 V174 M612,64 V174"/>\n        <rect class="dg-hull-dark shape" x="580" y="164" width="40" height="8"/><rect class="dg-thin shape" x="584" y="172" width="8" height="5"/><rect class="dg-thin shape" x="608" y="172" width="8" height="5"/>\n' + label(600, 206, 'Fitting bolted through, with a backing plate inside', 'dg-label small', 'middle')))
    P.append(part('bedding', '        <path class="dg-accent shape" d="M570,78 H630" stroke-width="3"/>\n' + label(530, 70, 'Sealant bed', 'dg-label small', 'end') + '\n' + lead(532, 74, 570, 78)))
    P.append(part('core-rot', '        <path class="dg-bad-fill shape" d="M612,106 C650,104 700,112 730,128 C700,144 650,150 612,150 Z" opacity=".4"/>\n        <path class="dg-accent" d="M582,82 L588,108 L610,128" stroke-dasharray="3 3" marker-end="url(#lam-arrow)"/>\n' + label(690, 246, 'Water past a failed seal soaks the core: a soft deck', 'dg-label small', 'middle') + '\n' + lead(700, 236, 710, 150)))
    return '\n'.join(P)

# ---------------------------------------------------------------- keel types (viewBox 0 0 900 300)
def keels():
    P = [marker('keel-arrow')]
    tiles = []
    hull = '<path class="dg-hull" d="M30,90 Q112,78 196,86 C201,102 191,118 176,124 C140,137 85,137 50,124 C40,118 32,105 30,90 Z"/>'
    # 1 fin
    t = ['        <line class="dg-waterline" x1="10" y1="110" x2="215" y2="110"/>']
    t.append(part('fin-keel', '        <path class="dg-hull-dark shape" d="M150,132 L134,215 L96,215 L84,132 Z"/>\n' + label(112, 255, 'Fin keel', 'dg-title', 'middle')))
    t.append(part('spade-rudder', '        <path class="dg-hull-dark shape" d="M62,128 L57,178 L46,178 L44,127 Z"/>\n' + label(46, 198, 'Spade rudder', 'dg-label small', 'middle')))
    t.append('        ' + hull)
    t.append(muted(20, 52, 'seen from the side', 'start'))
    t.append(muted(112, 275, 'Bavaria 1060, Gib’Sea 31,'))
    t.append(muted(112, 289, 'Sadler 32 (fin version)'))
    tiles.append('\n'.join(t))
    # 2 long keel: rudder ends at the waterline, stock above
    t = ['        <line class="dg-waterline" x1="10" y1="110" x2="215" y2="110"/>']
    t.append(part('long-keel', '        <path class="dg-hull shape" d="M30,90 Q112,78 196,86 C206,112 190,150 170,190 L64,196 C46,170 34,130 30,90 Z"/>\n' + label(112, 255, 'Long keel', 'dg-title', 'middle') + '\n' + label(120, 158, 'Ballast low in', 'dg-label small', 'middle') + '\n' + label(120, 172, 'the keel', 'dg-label small', 'middle')))
    t.append(part('keel-hung-rudder', '        <path class="dg-hull-dark shape" d="M64,196 C50,178 40,140 36,112 L24,116 C30,148 40,180 52,202 Z"/>\n        <rect class="dg-hull-dark shape" x="36" y="88" width="6" height="24"/>\n' + label(60, 222, 'Rudder hung behind the keel', 'dg-label small', 'middle')))
    t.append(muted(112, 275, 'Finnsailer 35, most motorsailers'))
    tiles.append('\n'.join(t))
    # 3 bilge keels from astern (no waterline; ground line)
    t = ['        <line class="dg-line" x1="20" y1="212" x2="205" y2="212"/>']
    t.append(part('bilge-keels', '        <path class="dg-hull-dark shape" d="M78,126 L58,212 L84,212 L100,130 Z"/><path class="dg-hull-dark shape" d="M147,126 L167,212 L141,212 L125,130 Z"/>\n' + label(112, 255, 'Bilge (twin) keels', 'dg-title', 'middle') + '\n' + label(112, 232, 'Sits upright when dried out', 'dg-label small', 'middle')))
    t.append('        <path class="dg-hull" d="M40,58 Q112,70 185,58 C186,108 152,136 112,141 C73,136 39,108 40,58 Z"/>')
    t.append(muted(20, 52, 'seen from astern, dried out', 'start'))
    t.append(muted(112, 275, 'Moody 33 (option), Sadler 32 (option)'))
    tiles.append('\n'.join(t))
    # 4 centreboard: proper ballast stub, board down plus ghost of the board raised, arrow
    t = ['        <line class="dg-waterline" x1="10" y1="110" x2="215" y2="110"/>']
    t.append(part('centreboard', '        <path class="dg-hull-dark shape" d="M160,132 L150,162 L74,162 L64,132 Z"/>\n        <path class="dg-hull-dark shape" d="M140,162 L124,222 L104,222 L96,162 Z" opacity=".6"/>\n        <path class="dg-hull-dark" d="M142,142 L82,146 L84,156 L142,154 Z" opacity=".3" stroke-dasharray="3 2"/>\n        <path class="dg-accent" d="M112,226 Q56,212 80,166" fill="none" stroke-dasharray="4 3" marker-end="url(#keel-arrow)"/>\n' + label(112, 255, 'Centreboard', 'dg-title', 'middle') + '\n' + label(112, 234, 'Board swings up into the ballast stub', 'dg-label small', 'middle')))
    t.append('        ' + hull)
    t.append(part('spade-rudder', '        <path class="dg-hull-dark shape" d="M62,128 L57,168 L46,168 L44,127 Z"/>'))
    t.append(muted(112, 275, 'Sadler 32 (option), Gib’Sea 31 DL'))
    tiles.append('\n'.join(t))
    for i, body in enumerate(tiles):
        P.append(f'      <g transform="translate({i*225},0)">\n{body}\n      </g>')
    P.append(bow(895, 296))
    return '\n'.join(P)

# ---------------------------------------------------------------- keel joint (viewBox 0 0 900 330), fore-and-aft section, bow right
def keel_joint():
    P = [marker('kj-arrow')]
    P.append(title(230, 24, 'Bolted-on keel: section along the boat'))
    P.append(title(700, 24, 'Encapsulated keel'))
    P.append(part('hull-laminate hull', '        <path class="dg-hull shape" d="M40,112 Q230,96 420,84 L420,100 Q230,112 40,128 Z"/>\n' + label(50, 172, 'Hull laminate', 'dg-label small') + '\n' + lead(84, 162, 92, 124)))
    P.append(part('keel-stub', '        <path class="dg-hull shape" d="M150,121 L310,109 L306,140 L154,152 Z"/>\n' + label(340, 152, 'Keel stub, part of the hull', 'dg-label small') + '\n' + lead(338, 148, 308, 134)))
    floors = ''
    for x in (172, 212, 252, 292):
        y = 112 - (x-150)*0.075
        floors += f'<rect class="dg-hull-dark shape" x="{x-3}" y="{y-34}" width="6" height="34"/>'
    P.append(part('floors', '        ' + floors + '\n' + label(50, 58, 'Floors: ribs across the', 'dg-label small') + '\n' + label(50, 72, 'hull that spread the load', 'dg-label small') + '\n' + lead(150, 68, 168, 80)))
    P.append(part('keel-casting', '        <path class="dg-hull-dark shape" d="M156,156 L304,144 L292,260 L200,270 Z"/>\n' + label(230, 300, 'Cast-iron or lead keel', 'dg-label', 'middle')))
    bolts = ''
    for x in (192, 232, 272):
        y = 112 - (x-150)*0.075
        bolts += f'<rect class="dg-hull-dark shape" x="{x-3}" y="{y-12}" width="6" height="{int(225-(y-12))}"/><rect class="dg-thin shape" x="{x-13}" y="{y-3}" width="26" height="4" fill="var(--dg-hull-dark)"/><rect class="dg-hull-dark shape" x="{x-8}" y="{y-12}" width="16" height="9"/>'
    P.append(part('keel-bolts', '        ' + bolts + '\n' + label(340, 62, 'Keel bolts: nuts and', 'dg-label small') + '\n' + label(340, 76, 'backing plates inside', 'dg-label small') + '\n' + lead(338, 70, 282, 96)))
    P.append(part('keel-joint', '        <path class="dg-accent shape" d="M154,152 L306,140" stroke-width="4"/>\n' + label(340, 186, 'Sealant joint', 'dg-label small') + '\n' + lead(338, 182, 308, 143)))
    P.append(part('keel-smile', '        <path d="M270,144 Q288,152 306,146" fill="none" stroke="var(--dg-bad)" stroke-width="3"/>\n        <circle class="dg-thin" cx="292" cy="146" r="16" stroke="var(--dg-bad)" stroke-dasharray="3 3"/>\n        <path class="dg-accent" d="M318,166 L302,196" stroke-dasharray="4 3" marker-end="url(#kj-arrow)"/>\n        <path class="dg-accent" d="M170,212 L184,182" stroke-dasharray="4 3" marker-end="url(#kj-arrow)"/>\n        <path class="dg-accent" d="M340,272 L300,266" stroke-width="2.5" marker-end="url(#kj-arrow)"/>\n' + label(340, 216, 'The “smile”: a crack opening at', 'dg-label small') + '\n' + label(340, 230, 'the forward end of the joint', 'dg-label small') + '\n' + label(340, 244, 'after a grounding (the keel is', 'dg-label small') + '\n' + label(340, 258, 'levered: aft end up, front down)', 'dg-label small') + '\n' + label(346, 286, 'impact', 'dg-muted', 'start') + '\n' + lead(338, 222, 310, 156)))
    P.append(bow(440, 318))
    P.append(part('encapsulated-keel', '        <path class="dg-hull shape" d="M520,112 Q690,96 860,84 L860,100 Q690,112 520,128 Z"/>\n        <path class="dg-hull shape" d="M600,121 L760,109 C764,160 758,230 748,270 L616,280 C606,230 598,160 600,121 Z"/>\n        <path class="dg-hull-dark shape" d="M614,135 C612,180 618,230 626,258 L738,250 C744,220 748,170 746,128 Z"/>\n        <path class="dg-thin" d="M630,150 L720,143 M632,180 L722,173 M636,210 L724,203 M640,240 L726,233" opacity=".6"/>\n' + label(680, 200, 'Iron ballast', 'dg-label small', 'middle') + '\n' + label(690, 300, 'Ballast sealed inside the GRP', 'dg-label', 'middle') + '\n' + label(786, 150, 'No bolts to corrode;', 'dg-label small') + '\n' + label(786, 164, 'a grounding can crack', 'dg-label small') + '\n' + label(786, 178, 'the skin and let water', 'dg-label small') + '\n' + label(786, 192, 'reach the metal', 'dg-label small') + '\n' + lead(784, 160, 762, 150)))
    return '\n'.join(P)

# ---------------------------------------------------------------- rudders (viewBox 0 0 900 300), bow right
def rudders():
    P = []
    tiles = []
    hull = '<path class="dg-hull" d="M20,60 Q112,54 205,66 L205,100 Q112,150 20,138 Z"/>'
    wl = '        <line class="dg-waterline" x1="10" y1="104" x2="215" y2="104"/>'
    t = [title(112, 26, 'Spade rudder'), wl, '        ' + hull]
    t.append(part('rudder-stock', '        <rect class="dg-hull-dark shape" x="108" y="40" width="8" height="106"/>\n' + label(102, 52, 'Stock', 'dg-label small', 'end')))
    t.append(part('rudder-bearings', '        <rect class="dg-accent-fill shape" x="102" y="74" width="20" height="8" opacity=".8"/><rect class="dg-accent-fill shape" x="102" y="134" width="20" height="8" opacity=".8"/>\n' + label(130, 92, 'Upper bearing', 'dg-label small') + '\n' + label(130, 150, 'Lower bearing, in the hull skin', 'dg-label small')))
    t.append(part('Quadrant', '        <path class="dg-hull-dark shape" d="M112,64 L80,56 Q112,44 144,56 Z"/>\n' + label(150, 52, 'Quadrant', 'dg-label small')))
    t.append(part('spade-rudder', '        <path class="dg-hull-dark shape" d="M126,142 L118,236 L96,236 L94,142 Z"/>\n' + label(112, 262, 'Blade on its stock alone', 'dg-label small', 'middle')))
    t.append(muted(112, 280, 'Bavaria 1060 and most')); t.append(muted(112, 293, 'production boats since 1990'))
    tiles.append('\n'.join(t))
    t = [title(112, 26, 'Skeg-hung rudder'), wl, '        ' + hull]
    t.append(part('skeg-hull skeg', '        <path class="dg-hull shape" d="M132,136 L166,140 L152,222 L138,222 Z"/>\n' + label(172, 190, 'Skeg', 'dg-label small')))
    t.append(part('rudder-stock', '        <rect class="dg-hull-dark shape" x="118" y="40" width="8" height="100"/>'))
    t.append(part('skeg-rudder', '        <path class="dg-hull-dark shape" d="M134,140 L126,236 L104,236 L104,138 Z"/>\n' + label(112, 262, 'Blade supported top and bottom', 'dg-label small', 'middle')))
    t.append(part('heel-bearing', '        <circle class="dg-accent-fill shape" cx="132" cy="220" r="5"/>\n' + label(140, 236, 'Heel bearing', 'dg-label small')))
    t.append(muted(112, 284, 'Moody 33, Sadler 32, Finnsailer 35 ¹'))
    tiles.append('\n'.join(t))
    t = [title(112, 26, 'Keel-hung rudder'), wl]
    t.append(part('long-keel', '        <path class="dg-hull shape" d="M20,60 Q112,54 205,66 L205,100 Q190,200 160,230 L100,230 Q60,200 40,132 Q30,100 20,60 Z"/>'))
    t.append(part('keel-hung-rudder', '        <path class="dg-hull-dark shape" d="M100,230 Q60,200 40,132 L26,136 Q46,206 86,240 Z"/>\n' + label(112, 262, 'Blade hinged on the back of the keel', 'dg-label small', 'middle')))
    t.append(part('heel-bearing', '        <circle class="dg-accent-fill shape" cx="92" cy="234" r="5"/>\n' + label(104, 222, 'Heel bearing', 'dg-label small')))
    t.append(part('rudder-stock', '        <rect class="dg-hull-dark shape" x="34" y="40" width="8" height="100"/>\n' + label(46, 76, 'Stock in a tube', 'dg-label small')))
    t.append(muted(112, 284, 'traditional long-keel boats'))
    tiles.append('\n'.join(t))
    t = [title(112, 26, 'Transom-hung rudder'), wl, '        <path class="dg-hull" d="M70,60 Q140,54 205,66 L205,100 Q140,150 70,138 Z"/>']
    t.append(part('transom-rudder', '        <path class="dg-hull-dark shape" d="M68,62 L66,236 L50,236 L52,62 Z"/>\n' + label(112, 262, 'Blade on the outside of the stern', 'dg-label small', 'middle')))
    t.append(part('pintle gudgeon', '        <circle class="dg-accent-fill shape" cx="62" cy="80" r="5"/><circle class="dg-accent-fill shape" cx="62" cy="128" r="5"/>\n' + label(74, 110, 'Pintles and gudgeons', 'dg-label small')))
    t.append(part('Tiller', '        <path class="dg-hull-dark shape" d="M60,58 L150,46 L150,52 L62,64 Z"/>\n' + label(160, 50, 'Tiller', 'dg-label small')))
    t.append(muted(112, 284, 'smaller and older boats'))
    tiles.append('\n'.join(t))
    for i, body in enumerate(tiles):
        P.append(f'      <g transform="translate({i*225},0)">\n{body}\n      </g>')
    P.append(muted(562, 298, 'dashed line: waterline'))
    P.append(bow(895, 296))
    return '\n'.join(P)

# ---------------------------------------------------------------- osmosis (viewBox 0 0 900 310)
def osmosis():
    P = [marker('os-arrow')]
    P.append(title(450, 26, 'How an osmosis blister forms (magnified section, water at the top)'))
    P.append('      <rect class="dg-water" x="40" y="44" width="820" height="50"/>')
    P.append(muted(450, 74, 'sea water'))
    P.append(part('gelcoat', '        <rect class="dg-hull-dark shape" x="40" y="94" width="820" height="14"/>\n        <path class="dg-hull-dark shape" d="M380,108 Q450,60 520,108 Z"/>\n' + label(60, 130, 'Gelcoat', 'dg-label small')))
    P.append(part('laminate', '        <rect class="dg-hull shape" x="40" y="108" width="820" height="150"/>\n' + label(60, 240, 'Laminate', 'dg-label small')))
    P.append(part('blister', '        <path class="dg-bad-fill shape" d="M392,108 Q450,66 508,108 Q450,150 392,108 Z" opacity=".5"/>\n' + label(450, 128, 'Blister', 'dg-label small', 'middle') + '\n' + label(600, 84, 'Blister: fluid lifting the gelcoat into a dome', 'dg-label small') + '\n' + lead(598, 88, 514, 92)))
    P.append(part('void', '        <ellipse class="dg-bad-fill shape" cx="450" cy="150" rx="26" ry="10" opacity=".4"/><ellipse class="dg-bad-fill shape" cx="300" cy="180" rx="14" ry="6" opacity=".4"/><ellipse class="dg-bad-fill shape" cx="600" cy="200" rx="18" ry="7" opacity=".4"/>\n' + label(640, 160, 'Voids and dry fibres in the laminate', 'dg-label small') + '\n' + lead(638, 156, 478, 150)))
    P.append(part('permeation', '        <path class="dg-accent" d="M200,72 V122" stroke-dasharray="3 3" stroke-width="1.5" marker-end="url(#os-arrow)"/><path class="dg-accent" d="M250,72 V136" stroke-dasharray="3 3" stroke-width="1.5" marker-end="url(#os-arrow)"/>\n' + label(120, 170, 'Water molecules pass slowly through the gelcoat', 'dg-label small') + '\n' + lead(118, 166, 200, 128)))
    P.append(part('hydrolysis', '        <rect class="shape-fill" x="60" y="266" width="780" height="34"/>\n' + label(450, 280, 'Hydrolysis: inside the laminate, water reacts with uncured resin to make an acidic fluid', 'dg-label small', 'middle') + '\n' + muted(450, 296, 'the fluid draws in more water and the rising pressure lifts the gelcoat')))
    return '\n'.join(P)

# ---------------------------------------------------------------- seacock (viewBox 0 0 900 330)
def seacock():
    P = []
    P.append(title(450, 24, 'Skin fitting and seacock, section through the hull'))
    P.append('      <rect class="dg-water" x="40" y="236" width="820" height="80"/>')
    P.append(muted(120, 286, 'sea'))
    P.append(part('hull-laminate hull', '        <rect class="dg-hull shape" x="40" y="212" width="820" height="24"/>\n' + label(852, 206, 'Hull', 'dg-label small', 'end')))
    P.append(part('skin-fitting through-hull', '        <path class="dg-hull-dark shape" d="M360,242 H540 L534,236 H366 Z"/>\n        <rect class="dg-hull-dark shape" x="426" y="156" width="48" height="86"/>\n        <path class="dg-thin" d="M430,166 H470 M430,176 H470 M430,186 H470 M430,196 H470" opacity=".5"/>\n' + label(600, 268, 'Skin fitting (through-hull): a threaded', 'dg-label small') + '\n' + label(600, 282, 'tube with a rim (flange) on the outside', 'dg-label small') + '\n' + lead(598, 272, 542, 240)))
    P.append(part('backing-pad', '        <rect class="dg-sail-2 shape" x="380" y="196" width="140" height="16"/>\n' + label(300, 214, 'Backing pad', 'dg-label small', 'end') + '\n' + lead(302, 210, 380, 204)))
    P.append(part('seacock-body seacock', '        <rect class="dg-hull-dark shape" x="404" y="126" width="92" height="30" rx="4"/>\n        <circle class="dg-hull shape" cx="450" cy="141" r="10"/><rect class="dg-line" x="446" y="133" width="8" height="16" fill="var(--dg-hull)"/>\n        <rect class="dg-hull-dark shape" x="460" y="138" width="44" height="6" rx="2"/><rect class="dg-hull-dark shape" x="500" y="84" width="8" height="58" rx="2"/>\n' + label(600, 126, 'Seacock: the valve. Handle in line', 'dg-label small') + '\n' + label(600, 140, 'with the pipe = open (as drawn);', 'dg-label small') + '\n' + label(600, 154, 'across the pipe = shut', 'dg-label small') + '\n' + lead(598, 134, 510, 120)))
    P.append(part('hose-tail', '        <rect class="dg-hull-dark shape" x="432" y="88" width="36" height="38"/><path class="dg-thin" d="M432,96 H468 M432,104 H468 M432,112 H468" opacity=".6"/>\n' + label(300, 124, 'Hose tail (ribbed spigot,', 'dg-label small', 'end') + '\n' + label(300, 138, 'under the hose)', 'dg-label small', 'end') + '\n' + lead(302, 122, 430, 118)))
    P.append(part('hose', '        <path class="dg-hull shape" d="M428,112 V72 Q428,32 468,32 H720 V72 H472 V112 Z"/>\n' + label(600, 94, 'Reinforced hose to the sink, toilet or engine', 'dg-label small')))
    P.append(part('hose-clips', '        <rect class="dg-accent-fill shape" x="428" y="92" width="44" height="5"/><rect class="dg-accent-fill shape" x="428" y="104" width="44" height="5"/>\n' + label(300, 96, 'Two stainless clips', 'dg-label small', 'end') + '\n' + lead(302, 92, 428, 94)))
    P.append(part('bung', '        <path class="dg-sail-2 shape" d="M120,130 L150,120 L156,154 Z"/><path class="dg-thin" d="M150,134 Q250,120 404,140" stroke-dasharray="1 4" stroke-linecap="round" stroke-width="2"/>\n' + label(60, 176, 'Softwood bung, tied on', 'dg-label small') + '\n' + label(60, 190, 'for emergencies', 'dg-label small')))
    return '\n'.join(P)
