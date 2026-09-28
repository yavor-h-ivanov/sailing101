# Diagram builders for sections/05-deck.html. Bow to the RIGHT in every profile view.
from gen_hull_diagrams import part, label, lead, title, muted, bow, marker
from gen_rig_diagrams import marker2, dim

# ---------------------------------------------------------------- wheel steering (viewBox 0 0 900 420), aft part of an aft-cockpit boat
def wheel_steering():
    P = [marker('ws-arrow')]
    P.append(title(560, 24, 'Cable-and-chain wheel steering, seen from the side'))
    P.append('      <path class="dg-hull" d="M60,200 L380,200 L380,290 L720,290 L720,200 L880,200 L880,406 C700,416 400,400 120,360 C90,356 70,340 60,300 Z"/>')
    P.append('      <line class="dg-waterline" x1="30" y1="352" x2="890" y2="352"/>')
    P.append(muted(800, 250, 'cabin', 'start'))
    P.append(muted(630, 282, 'cockpit sole', 'middle'))
    P.append(muted(250, 224, 'stern locker', 'start'))
    # inset: the quadrant seen from above, bow to the right
    P.append('      <rect class="dg-thin" x="12" y="6" width="226" height="178" rx="6" fill="none" stroke-dasharray="4 3"/>')
    P.append(label(20, 22, 'Quadrant seen from above', 'dg-label small'))
    P.append(muted(228, 176, 'bow →', 'end'))
    P.append(part('steering-quadrant quadrant', '        <path class="dg-hull-dark shape" d="M80,100 L130,68 A59.4,59.4 0 0 1 130,132 Z"/><circle class="dg-hull shape" cx="80" cy="100" r="6"/>\n        <rect class="dg-hull-dark shape" x="196" y="292" width="60" height="22"/>\n' + label(20, 38, 'A fan clamped to the stock;', 'dg-label small') + '\n' + label(20, 52, 'the cables lie in its rim', 'dg-label small') + '\n' + label(20, 196, 'Quadrant, edge on', 'dg-label small') + '\n' + lead(96, 200, 214, 292)))
    P.append(part('steering-cable', '        <path class="dg-accent shape" d="M228,92 L139,92 A59.4,59.4 0 0 0 130,68 M228,108 L139,108 A59.4,59.4 0 0 1 130,132" fill="none" stroke-width="2"/><circle class="dg-accent-fill" cx="130" cy="68" r="3"/><circle class="dg-accent-fill" cx="130" cy="132" r="3"/>\n        <path class="dg-accent shape" d="M486,240 L486,262 L470,300 L256,300 M514,240 L514,262 L500,310 L256,310" fill="none" stroke-width="2"/>\n        <path class="hit" d="M486,262 L470,300 L256,300 M514,262 L500,310 L256,310" stroke="transparent" stroke-width="12" fill="none"/>\n' + label(560, 340, 'Wire cables, one from each end', 'dg-label small') + '\n' + label(560, 354, 'of the chain, run aft under the', 'dg-label small') + '\n' + label(560, 368, 'sole to the quadrant’s rim', 'dg-label small') + '\n' + lead(558, 346, 440, 306)))
    P.append(part('rudder-stops', '        <rect class="dg-bad-fill shape" x="104" y="64" width="12" height="10"/><rect class="dg-bad-fill shape" x="104" y="126" width="12" height="10"/>\n' + label(142, 150, 'Rudder stops', 'dg-label small') + '\n' + label(142, 164, 'either side', 'dg-label small') + '\n' + lead(140, 150, 114, 136)))
    P.append(part('steer-stock rudder-stock', '        <rect class="dg-hull-dark shape" x="196" y="226" width="10" height="200"/>\n' + label(60, 262, 'Rudder stock', 'dg-label small') + '\n' + lead(124, 264, 194, 264)))
    P.append(part('rudder-tube', '        <rect class="dg-hull shape" x="190" y="322" width="22" height="50" opacity=".7"/>'))
    P.append(part('steer-bearings rudder-bearings', '        <rect class="dg-accent-fill shape" x="188" y="318" width="26" height="8"/><rect class="dg-accent-fill shape" x="188" y="362" width="26" height="8"/>\n' + label(60, 330, 'Bearings at the top', 'dg-label small') + '\n' + label(60, 344, 'and bottom of the', 'dg-label small') + '\n' + label(60, 358, 'rudder tube', 'dg-label small') + '\n' + lead(170, 340, 188, 324)))
    P.append(part('steer-rudder spade-rudder', '        <path class="dg-hull-dark shape" d="M212,372 L218,446 L182,446 L188,372 Z"/><path class="dg-thin" d="M218,446 L220,466 M182,446 L180,466 M176,446 H224" stroke-dasharray="3 3"/>\n' + label(60, 430, 'Rudder blade', 'dg-label small') + '\n' + label(60, 444, '(continues below)', 'dg-label small') + '\n' + lead(170, 434, 184, 430)))
    P.append(part('pedestal', '        <rect class="dg-hull shape" x="464" y="150" width="56" height="140" rx="4"/>\n' + label(560, 226, 'Pedestal: a hollow column', 'dg-label small') + '\n' + label(560, 240, 'bolted to the cockpit sole', 'dg-label small')))
    P.append(part('steer-wheel wheel', '        <ellipse class="dg-hull-dark shape" cx="487" cy="112" rx="10" ry="52"/><rect class="dg-hull-dark shape" x="483" y="108" width="24" height="8"/>\n' + label(560, 62, 'Wheel, on a short axle', 'dg-label small')))
    P.append(part('chain-sprocket', '        <circle class="dg-hull shape" cx="500" cy="112" r="14"/><circle class="dg-thin" cx="500" cy="112" r="7"/>\n        <path class="dg-line" d="M486,112 L486,240 M514,112 L514,240" stroke-dasharray="4 3"/>\n' + label(560, 106, 'Sprocket on the axle; a', 'dg-label small') + '\n' + label(560, 120, 'bicycle-type chain runs', 'dg-label small') + '\n' + label(560, 134, 'down inside the pedestal', 'dg-label small')))
    P.append(part('steering-sheave', '        <circle class="dg-accent-fill shape" cx="470" cy="300" r="7"/><circle class="dg-accent-fill shape" cx="500" cy="310" r="7"/>\n' + label(560, 300, 'Sheaves (pulleys) under the', 'dg-label small') + '\n' + label(560, 314, 'pedestal turn the cables aft', 'dg-label small') + '\n' + lead(558, 306, 508, 308)))
    P.append(part('emergency-tiller', '        <rect class="dg-hull-dark shape" x="192" y="218" width="18" height="12"/><path class="dg-hull-dark shape" d="M186,200 L216,200 L216,196 L186,196 Z"/>\n        <path class="dg-accent" d="M201,218 L201,206" stroke-dasharray="2 2" marker-end="url(#ws-arrow)"/>\n' + label(262, 170, 'Emergency tiller: a square socket on the stock head,', 'dg-label small') + '\n' + label(262, 184, 'under a deck plate; a bar drops in when the wheel fails', 'dg-label small') + '\n' + lead(260, 180, 212, 212)))
    P.append(part('autopilot-drive', '        <rect class="dg-hull shape" x="300" y="264" width="70" height="14" rx="3"/><path class="dg-hull-dark shape" d="M300,271 L206,264 L206,258 L300,265 Z"/><rect class="dg-thin shape" x="368" y="260" width="14" height="22" fill="var(--dg-hull-dark)"/>\n' + label(262, 410, 'Autopilot drive: a ram on a bracket pushes', 'dg-label small') + '\n' + label(262, 424, 'an arm clamped to the stock', 'dg-label small') + '\n' + lead(300, 400, 334, 280)))
    P.append(bow(890, 460))
    return '\n'.join(P)

# ---------------------------------------------------------------- steering types (viewBox 0 0 900 300)
def steering_types():
    P = [marker('st-arrow')]
    tiles = []
    def base(t, name):
        t.append(title(112, 24, name))
        t.append('        <path class="dg-hull" d="M20,150 L205,150 L205,250 C150,262 70,262 20,250 Z"/>')
        t.append(muted(112, 160, '', 'middle'))
    # 1 tiller
    t = []; base(t, 'Tiller')
    t.append(part('steer-stock rudder-stock', '        <rect class="dg-hull-dark shape" x="60" y="120" width="8" height="134"/>'))
    t.append(part('tiller-arm tiller', '        <path class="dg-hull-dark shape" d="M58,120 L190,104 L190,112 L60,128 Z"/>\n' + label(80, 150, 'Lever on the stock head', 'dg-label small')))
    t.append(part('tiller-extension', '        <path class="dg-line shape" d="M190,108 L112,60"/><circle class="dg-accent-fill shape" cx="190" cy="108" r="4"/>\n' + label(60, 52, 'Extension', 'dg-label small')))
    t.append(muted(112, 284, 'Sadler 32, Gib’Sea 31'))
    tiles.append('\n'.join(t))
    # 2 cable and chain
    t = []; base(t, 'Cable and chain')
    t.append(part('steer-stock rudder-stock', '        <rect class="dg-hull-dark shape" x="60" y="150" width="8" height="104"/>'))
    t.append(part('pedestal', '        <rect class="dg-hull shape" x="150" y="80" width="18" height="70"/>'))
    t.append(part('steer-wheel wheel', '        <ellipse class="dg-hull-dark shape" cx="159" cy="58" rx="5" ry="26"/>'))
    t.append(part('steering-quadrant quadrant', '        <rect class="dg-hull-dark shape" x="64" y="174" width="36" height="10"/>'))
    t.append(part('steering-cable', '        <path class="dg-accent shape" d="M154,150 L150,176 L100,177 M164,150 L168,186 L100,181" fill="none" stroke-width="1.5"/>\n        <path class="hit" d="M154,150 L150,176 L100,177 M164,150 L168,186 L100,181" stroke="transparent" stroke-width="10" fill="none"/>\n' + label(76, 210, 'Wires over sheaves', 'dg-label small') + '\n' + label(76, 224, 'to a flat quadrant', 'dg-label small')))
    t.append(muted(112, 270, 'the common wheel system;'))
    t.append(muted(112, 284, 'Moody 33 ², most wheel boats'))
    tiles.append('\n'.join(t))
    # 3 rod
    t = []; base(t, 'Rod (mechanical)')
    t.append(part('steer-stock rudder-stock', '        <rect class="dg-hull-dark shape" x="60" y="150" width="8" height="104"/>'))
    t.append(part('pedestal', '        <rect class="dg-hull shape" x="150" y="80" width="18" height="70"/>'))
    t.append(part('steer-wheel wheel', '        <ellipse class="dg-hull-dark shape" cx="159" cy="58" rx="5" ry="26"/>'))
    t.append(part('bevel-box', '        <rect class="dg-hull-dark shape" x="146" y="150" width="26" height="18" rx="3"/><rect class="dg-hull-dark shape" x="52" y="168" width="24" height="18" rx="3"/>\n' + label(76, 210, 'Gearboxes at each end', 'dg-label small')))
    t.append(part('torque-tube', '        <path class="dg-accent shape" d="M146,160 L76,176" stroke-width="5"/>\n' + label(76, 224, 'joined by a solid rod', 'dg-label small')))
    t.append(muted(112, 270, 'Whitlock, Jefa;'))
    t.append(muted(112, 284, 'Gib’Sea 33 (2002) ¹'))
    tiles.append('\n'.join(t))
    # 4 hydraulic
    t = []; base(t, 'Hydraulic')
    t.append(part('steer-stock rudder-stock', '        <rect class="dg-hull-dark shape" x="60" y="150" width="8" height="104"/>'))
    t.append(part('pedestal', '        <rect class="dg-hull shape" x="150" y="80" width="18" height="70"/>'))
    t.append(part('steer-wheel wheel', '        <ellipse class="dg-hull-dark shape" cx="159" cy="58" rx="5" ry="26"/>'))
    t.append(part('helm-pump', '        <rect class="dg-hull-dark shape" x="146" y="86" width="26" height="16" rx="3"/>\n' + label(20, 100, 'Pump behind', 'dg-label small') + '\n' + label(20, 114, 'the wheel', 'dg-label small') + '\n' + lead(96, 104, 144, 94)))
    t.append(part('hydraulic-hose', '        <path class="dg-accent shape" d="M150,102 L140,160 L96,172 M168,102 L176,168 L104,186" fill="none" stroke-width="1.5"/>\n        <path class="hit" d="M150,102 L140,160 L96,172 M168,102 L176,168 L104,186" stroke="transparent" stroke-width="10" fill="none"/>\n' + label(76, 210, 'Two hoses to a ram', 'dg-label small')))
    t.append(part('hydraulic-ram', '        <rect class="dg-hull shape" x="80" y="170" width="40" height="14" rx="3"/><path class="dg-hull-dark shape" d="M80,177 L66,168 L66,186 Z"/>\n' + label(76, 224, 'pushing a tiller arm', 'dg-label small')))
    t.append(muted(112, 270, 'two steering positions;'))
    t.append(muted(112, 284, 'motorsailers (Finnsailer 35 ²)'))
    tiles.append('\n'.join(t))
    for i, body in enumerate(tiles):
        P.append(f'      <g transform="translate({i*225},0)">\n{body}\n      </g>')
    P.append(bow(895, 296))
    return '\n'.join(P)

# ---------------------------------------------------------------- anchor gear at the bow (viewBox 0 0 900 360)
def anchor_gear():
    P = [marker('ag-arrow')]
    P.append(title(450, 24, 'Anchor gear on the foredeck, seen from the side'))
    P.append('      <path class="dg-hull" d="M40,160 L720,160 C750,160 772,180 786,220 L806,300 L40,300 Z"/>')
    P.append('      <line class="dg-waterline" x1="20" y1="286" x2="880" y2="286"/>')
    P.append(muted(300, 250, 'forecabin', 'middle'))
    P.append(part('chain-locker-deck chain-locker', '        <rect class="dg-sail-2 shape" x="520" y="176" width="180" height="98"/>\n' + label(610, 250, 'Chain locker', 'dg-label small', 'middle')))
    P.append(part('bow-roller-fitting bow-roller', '        <path class="dg-hull-dark shape" d="M720,160 L784,160 L790,150 L790,140 L720,140 Z"/><circle class="dg-hull shape" cx="772" cy="150" r="9"/>\n' + label(640, 96, 'Bow roller: the chain runs over a wheel at', 'dg-label small') + '\n' + label(640, 110, 'the stem; the anchor lives on it when stowed', 'dg-label small') + '\n' + lead(760, 114, 770, 140)))
    P.append(part('anchor', '        <rect class="dg-hull-dark shape" x="780" y="145" width="64" height="7"/><path class="dg-hull-dark shape" d="M840,146 L852,150 L862,196 L880,208 L874,216 L850,200 L838,158 Z"/><path class="dg-hull-dark shape" d="M862,196 L846,214 L840,208 L856,190 Z"/>\n' + label(872, 240, 'Anchor stowed', 'dg-label small', 'end') + '\n' + label(872, 254, 'on the roller', 'dg-label small', 'end')))
    P.append(part('windlass-unit windlass', '        <rect class="dg-hull-dark shape" x="560" y="126" width="70" height="34" rx="4"/><circle class="dg-hull shape" cx="580" cy="140" r="12"/><path class="dg-thin" d="M572,132 L588,148 M588,132 L572,148"/>\n' + label(430, 60, 'Windlass: a winch for chain. Its notched wheel', 'dg-label small') + '\n' + label(430, 74, '(the gypsy) grips the links', 'dg-label small') + '\n' + lead(560, 78, 578, 126)))
    P.append(part('anchor-chain', '        <path class="dg-line shape" d="M772,141 L592,128 M580,152 L578,176 L576,250" stroke-width="3" stroke-dasharray="6 3"/>\n        <path class="hit" d="M772,141 L592,128 M580,152 L576,250" stroke="transparent" stroke-width="12" fill="none"/>\n' + label(300, 322, 'Chain: 8 or 10 mm, calibrated to fit the gypsy', 'dg-label small') + '\n' + lead(540, 316, 576, 252)))
    P.append(part('chain-stopper', '        <rect class="dg-hull-dark shape" x="674" y="128" width="5" height="32"/><rect class="dg-hull-dark shape" x="701" y="126" width="5" height="34"/><rect class="dg-hull-dark shape" x="674" y="152" width="32" height="8"/><path class="dg-accent-fill shape" d="M680,120 L700,130 L698,134 L682,126 Z"/>\n' + label(600, 322, 'Chain stopper: a hinged catch that', 'dg-label small') + '\n' + label(600, 336, 'takes the load off the windlass', 'dg-label small') + '\n' + lead(660, 318, 690, 164)))
    P.append(part('navel-pipe', '        <rect class="dg-hull shape" x="566" y="160" width="28" height="16"/>\n' + label(380, 200, 'Navel pipe: the hole the', 'dg-label small') + '\n' + label(380, 214, 'chain drops through', 'dg-label small') + '\n' + lead(500, 206, 564, 170)))
    P.append(part('mooring-cleat cleat', '        <path class="dg-hull-dark shape" d="M472,160 L488,160 L485,150 L475,150 Z"/><path class="dg-hull-dark shape" d="M452,144 L460,146 L500,146 L508,144 L504,150 L456,150 Z"/>\n' + label(380, 240, 'Cleat, bolted through', 'dg-label small') + '\n' + label(380, 254, 'a backing plate', 'dg-label small') + '\n' + lead(470, 236, 478, 162)))
    P.append(part('deck-fairlead fairlead', '        <path class="dg-hull-dark shape" d="M430,160 L446,160 L446,152 L430,152 Z"/>\n' + label(60, 130, 'Fairlead: guides a rope', 'dg-label small') + '\n' + label(60, 144, 'over the deck edge', 'dg-label small') + '\n' + lead(190, 140, 430, 156)))
    P.append(bow(890, 350))
    return '\n'.join(P)

# ---------------------------------------------------------------- anchors and scope (viewBox 0 0 900 320)
def anchors():
    P = [marker('an-arrow'), marker2('an-dim')]
    P.append(title(225, 24, 'Four anchor families'))
    tiles = []
    # plough (CQR/Delta)
    t = [part('anchor-plough', '        <rect class="dg-hull-dark shape" x="58" y="40" width="6" height="66" transform="rotate(-12 61 106)"/><path class="dg-hull-dark shape" d="M44,100 L102,126 L40,140 L50,120 Z"/>\n' + label(60, 156, 'Plough', 'dg-label', 'middle') + '\n' + label(60, 170, 'CQR, Delta', 'dg-label small', 'middle'))]
    tiles.append(t)
    t = [part('anchor-claw', '        <path class="dg-hull-dark shape" d="M60,40 L64,40 L64,104 C90,104 98,120 92,134 L80,126 C74,118 64,116 60,116 C56,116 46,118 40,126 L28,134 C22,120 30,104 60,104 Z"/>\n' + label(60, 156, 'Claw', 'dg-label', 'middle') + '\n' + label(60, 170, 'Bruce', 'dg-label small', 'middle'))]
    tiles.append(t)
    t = [part('anchor-newgen', '        <path class="dg-hull-dark shape" d="M60,40 L64,40 L64,112 L96,130 L88,138 L40,118 L36,110 Z"/><path class="dg-line shape" d="M34,110 A28,28 0 0 1 90,110" fill="none" stroke-width="3"/>\n' + label(60, 156, 'Scoop', 'dg-label', 'middle') + '\n' + label(60, 170, 'Rocna, Spade,', 'dg-label small', 'middle') + '\n' + label(60, 184, 'Mantus', 'dg-label small', 'middle'))]
    tiles.append(t)
    t = [part('anchor-danforth', '        <path class="dg-hull-dark shape" d="M60,40 L64,40 L64,116 L100,132 L96,138 L62,124 L28,138 L24,132 L60,116 Z"/><rect class="dg-hull-dark shape" x="20" y="112" width="84" height="4"/>\n' + label(60, 156, 'Flat (fluke)', 'dg-label', 'middle') + '\n' + label(60, 170, 'Danforth, Fortress', 'dg-label small', 'middle'))]
    tiles.append(t)
    for i, body in enumerate(tiles):
        P.append(f'      <g transform="translate({i*105+10},20)">\n' + '\n'.join(body) + '\n      </g>')
    P.append(muted(225, 228, 'silhouettes only, not to scale'))
    # scope diagram on the right: boat on the left, bow to the right, drawn to about 4.5 to 1
    P.append(title(670, 24, 'Scope: how much chain'))
    P.append('      <rect class="dg-water" x="460" y="190" width="436" height="60"/>')
    P.append('      <path class="dg-hull-dark" d="M460,250 L896,250 L896,260 L460,260 Z" opacity=".5"/>')
    P.append(muted(464, 278, 'seabed', 'start'))
    P.append('      <path class="dg-hull" d="M470,170 L560,170 L552,194 L478,194 Z"/>')
    P.append(bow(896, 278))
    P.append(part('anchor-chain', '        <path class="dg-line shape" d="M556,176 C590,236 660,250 866,250" fill="none" stroke-width="2.5" stroke-dasharray="6 3"/>\n        <path class="hit" d="M556,176 C590,236 660,250 866,250" stroke="transparent" stroke-width="12" fill="none"/>\n' + label(640, 96, 'The chain hangs in a curve and pulls', 'dg-label small') + '\n' + label(640, 110, 'the anchor along the bottom, not up', 'dg-label small') + '\n' + lead(700, 114, 640, 240)))
    P.append(part('anchor', '        <path class="dg-hull-dark shape" d="M866,250 L888,256 L894,250 L870,242 Z"/>'))
    P.append(part('scope-depth', dim(530, 176, 530, 250, 'an-dim', 'depth', dx=-28) + '\n' + lead(530, 176, 556, 176, 'dg-thin')))
    P.append(part('scope-ratio', label(730, 178, 'Chain out, along the curve: 4 to 5 × depth ²', 'dg-label small', 'middle') + '\n' + lead(700, 182, 700, 246) + '\n' + muted(678, 300, 'depth = water at high tide plus the height of the bow') + '\n' + muted(678, 314, 'drawn to scale here at about 4.5 to 1')))
    return '\n'.join(P)

# ---------------------------------------------------------------- deck fittings (viewBox 0 0 900 380)
def deck_fittings():
    P = [marker('df-arrow')]
    # panel 1 bolt through a cored deck
    P.append(title(150, 24, 'Bolt through a cored deck, done right'))
    P.append(part('df-outer-skin outer-skin', '        <rect class="dg-hull shape" x="30" y="150" width="240" height="16"/>'))
    P.append(part('df-core core', '        <rect class="dg-sail-2 shape" x="30" y="166" width="240" height="40"/>' + ''.join(f'<path class="dg-thin" d="M{x},166 V206" opacity=".4"/>' for x in range(46, 270, 22)) + '\n' + label(40, 190, 'Balsa core', 'dg-label small on-sail')))
    P.append(part('df-inner-skin inner-skin', '        <rect class="dg-hull shape" x="30" y="206" width="240" height="12"/>'))
    P.append(part('epoxy-annulus', '        <rect class="dg-hull-dark shape" x="132" y="166" width="36" height="40" opacity=".55"/>\n' + label(30, 256, 'Epoxy ring: the hole was drilled', 'dg-label small') + '\n' + label(30, 270, 'oversize, filled with epoxy and', 'dg-label small') + '\n' + label(30, 284, 'redrilled, so the core is sealed', 'dg-label small') + '\n' + lead(110, 250, 136, 200)))
    P.append(part('df-bolt', '        <rect class="dg-hull-dark shape" x="146" y="120" width="8" height="118"/><rect class="dg-hull-dark shape" x="138" y="120" width="24" height="10"/>'))
    P.append(part('df-fitting deck-fitting', '        <rect class="dg-hull shape" x="100" y="130" width="100" height="14" rx="2"/>\n' + label(30, 110, 'Fitting base', 'dg-label small') + '\n' + lead(100, 112, 112, 130)))
    P.append(part('sealant-bed bedding', '        <path class="dg-accent shape" d="M100,146 H200" stroke-width="4"/><path class="dg-accent shape" d="M140,150 L146,158 L154,158 L160,150" fill="var(--dg-accent)"/>\n' + label(30, 46, 'Sealant bed, plus a countersink', 'dg-label small') + '\n' + label(30, 60, 'round the hole that holds a ring', 'dg-label small') + '\n' + label(30, 74, 'of sealant against the bolt', 'dg-label small') + '\n' + lead(170, 78, 158, 146)))
    P.append(part('df-backing backing-plate', '        <rect class="dg-hull-dark shape" x="110" y="218" width="80" height="8"/><rect class="dg-hull-dark shape" x="140" y="226" width="20" height="12"/>\n' + label(200, 224, 'Backing plate,', 'dg-label small') + '\n' + label(200, 238, 'washer, nut', 'dg-label small') + '\n' + lead(198, 228, 190, 222)))
    P.append(muted(150, 300, 'without the epoxy ring, a failed sealant bed'))
    P.append(muted(150, 314, 'lets water straight into the core'))
    # panel 2 stanchion and guardrail
    P.append(title(450, 24, 'Stanchion and guardrails'))
    P.append('      <rect class="dg-hull" x="330" y="300" width="230" height="14"/>')
    P.append(muted(340, 330, 'side deck', 'start'))
    P.append(part('toe-rail-edge toe-rail', '        <rect class="dg-hull-dark shape" x="546" y="286" width="14" height="14"/>\n' + label(540, 280, 'Toe rail', 'dg-label small', 'end')))
    P.append(part('stanchion', '        <rect class="dg-hull-dark shape" x="446" y="90" width="8" height="200"/>\n' + label(466, 160, 'Stanchion: a post', 'dg-label small') + '\n' + label(466, 174, 'about 600 mm high', 'dg-label small')))
    P.append(part('stanchion-base', '        <path class="dg-hull-dark shape" d="M436,300 L464,300 L460,284 L440,284 Z"/><rect class="dg-hull-dark shape" x="430" y="314" width="40" height="6"/>\n' + label(438, 262, 'Base, bolted through', 'dg-label small', 'end') + '\n' + label(438, 276, 'with a backing plate', 'dg-label small', 'end') + '\n' + lead(438, 280, 442, 290)))
    P.append(part('guardrail-wire guardrail', '        <path class="dg-line shape" d="M330,100 H560 M330,190 H560" stroke-width="2"/>\n        <path class="hit" d="M330,100 H560 M330,190 H560" stroke="transparent" stroke-width="12" fill="none"/>\n' + label(340, 92, 'Upper and lower guardrails (lifelines)', 'dg-label small')))
    P.append(part('pelican-hook', '        <path class="dg-accent-fill shape" d="M500,94 L520,94 L522,106 L498,106 Z"/>\n' + label(466, 122, 'Gate with a pelican hook', 'dg-label small') + '\n' + lead(500, 118, 508, 108)))
    P.append(part('stanchion-leak', '        <path class="dg-bad" d="M436,300 Q450,312 464,300" fill="none" stroke-width="2" stroke-dasharray="3 2"/>\n' + label(340, 350, 'Fault: a levered base leaks into the core', 'dg-label small') + '\n' + lead(420, 344, 446, 306)))
    P.append(muted(450, 378, 'plastic-covered wire hides its own rust;'))
    P.append(muted(450, 392, 'bare wire or Dyneema shows it'))
    # panel 3 windows
    P.append(title(750, 24, 'Two ways to fit a window'))
    P.append('      <rect class="dg-hull" x="640" y="60" width="16" height="32"/><rect class="dg-hull" x="640" y="158" width="16" height="32"/><rect class="dg-hull" x="640" y="220" width="16" height="42"/><rect class="dg-hull" x="640" y="308" width="16" height="42"/>')
    P.append(muted(650, 56, 'cabin side, in section', 'start'))
    P.append(part('framed-window', '        <rect class="dg-hull-dark shape" x="632" y="90" width="12" height="70"/><rect class="dg-hull-dark shape" x="652" y="90" width="12" height="70"/><rect class="dg-water shape" x="644" y="96" width="8" height="58"/><path class="dg-accent shape" d="M644,92 H652 M644,158 H652" stroke-width="4"/>\n' + label(680, 110, 'Framed: aluminium frames', 'dg-label small') + '\n' + label(680, 124, 'clamp the pane and a rubber', 'dg-label small') + '\n' + label(680, 138, 'gasket; the gasket and the', 'dg-label small') + '\n' + label(680, 152, 'frame sealant age and leak', 'dg-label small')))
    P.append(part('bonded-window', '        <rect class="dg-water shape" x="626" y="246" width="14" height="78"/><path class="dg-accent shape" d="M640,246 V262 M640,308 V324" stroke-width="4"/>\n' + label(680, 270, 'Bonded: an acrylic pane glued', 'dg-label small') + '\n' + label(680, 284, 'to the outside with a flexible', 'dg-label small') + '\n' + label(680, 298, 'adhesive, no frame; fails when', 'dg-label small') + '\n' + label(680, 312, 'the pane crazes or the glue lets go', 'dg-label small')))
    P.append(muted(750, 372, 'inside of the cabin to the right'))
    return '\n'.join(P)

# ---------------------------------------------------------------- winch, clutch, cleat (viewBox 0 0 900 340)
def winch():
    P = [marker('wn-arrow')]
    # winch cutaway
    P.append(title(200, 24, 'Self-tailing winch, cut open'))
    P.append(part('winch-drum', '        <path class="dg-hull shape" d="M160,120 L280,120 L288,240 L152,240 Z"/>\n' + label(300, 190, 'Drum: the rope is wound', 'dg-label small') + '\n' + label(300, 204, 'round it three or four turns', 'dg-label small')))
    P.append(part('self-tailing-jaws', '        <path class="dg-hull-dark shape" d="M148,104 L292,104 L288,120 L152,120 Z"/><path class="dg-hull-dark shape" d="M152,88 L288,88 L292,104 L148,104 Z"/>\n' + label(300, 100, 'Self-tailing jaws: two sprung', 'dg-label small') + '\n' + label(300, 114, 'discs that grip the rope tail', 'dg-label small')))
    P.append(part('stripper-arm', '        <path class="dg-accent-fill shape" d="M140,96 L160,84 L166,96 Z"/>\n' + label(30, 80, 'Stripper arm feeds', 'dg-label small') + '\n' + label(30, 94, 'the tail off the jaws', 'dg-label small')))
    P.append(part('winch-handle-socket', '        <rect class="dg-hull-dark shape" x="210" y="60" width="20" height="28"/>\n' + label(300, 66, 'Handle socket', 'dg-label small') + '\n' + lead(298, 64, 232, 70)))
    P.append(part('winch-gears', '        <circle class="dg-thin shape" cx="220" cy="180" r="34" fill="none" stroke-width="3" stroke-dasharray="6 4"/><circle class="dg-thin shape" cx="220" cy="180" r="14" fill="none" stroke-width="3"/>\n' + label(30, 170, 'Gears inside give', 'dg-label small') + '\n' + label(30, 184, 'two speeds', 'dg-label small') + '\n' + lead(120, 178, 186, 180)))
    P.append(part('pawls', '        <path class="dg-arrow shape" d="M190,214 L202,208 L202,220 Z"/><path class="dg-arrow shape" d="M250,214 L238,208 L238,220 Z"/>\n' + label(20, 226, 'Pawls: sprung', 'dg-label small') + '\n' + label(20, 240, 'catches that let', 'dg-label small') + '\n' + label(20, 254, 'the drum turn one', 'dg-label small') + '\n' + label(20, 268, 'way; springs fail', 'dg-label small') + '\n' + lead(130, 232, 188, 216)))
    P.append(part('winch-base', '        <rect class="dg-hull-dark shape" x="140" y="240" width="160" height="14"/>\n' + label(308, 250, 'Base, bolted through', 'dg-label small') + '\n' + label(308, 264, 'the deck', 'dg-label small')))
    P.append(muted(220, 300, 'strip, wash, light grease on the gears,'))
    P.append(muted(220, 314, 'oil on the pawls, once a year'))
    # rope clutch
    P.append(title(560, 24, 'Rope clutch'))
    P.append(part('clutch-body rope-clutch', '        <rect class="dg-hull shape" x="480" y="150" width="160" height="60" rx="6"/>\n' + label(560, 262, 'Body, bolted to the coachroof', 'dg-label small', 'middle')))
    P.append(part('clutch-cam', '        <path class="dg-hull-dark shape" d="M530,150 L590,150 L580,186 L540,186 Z"/>\n' + label(480, 110, 'Toothed cam presses', 'dg-label small') + '\n' + label(480, 124, 'the rope onto the base', 'dg-label small') + '\n' + lead(540, 128, 556, 150)))
    P.append(part('clutch-lever', '        <path class="dg-accent shape" d="M560,150 L644,176" stroke-width="5"/><path class="dg-thin" d="M560,150 L620,84" stroke-dasharray="3 3"/>\n' + label(600, 70, 'Lever down (drawn): holds.', 'dg-label small') + '\n' + label(600, 84, 'Lifted (dotted): releases', 'dg-label small')))
    P.append(part('clutch-rope', '        <path class="dg-line shape" d="M460,196 H660" stroke-width="8" opacity=".6"/>\n        <path class="dg-accent" d="M660,196 L700,196" stroke-width="2" marker-end="url(#wn-arrow)"/>\n' + label(680, 220, 'to the winch', 'dg-label small', 'middle')))
    P.append(muted(560, 300, 'holds a loaded line; release it under'))
    P.append(muted(560, 314, 'load only with the line on a winch'))
    # cleat
    P.append(title(800, 24, 'Horn cleat'))
    P.append(part('horn-cleat cleat', '        <path class="dg-hull-dark shape" d="M788,170 L812,170 L806,150 L794,150 Z"/><path class="dg-hull-dark shape" d="M740,138 L750,144 L850,144 L860,138 L856,150 L744,150 Z"/>\n' + label(800, 200, 'Two horns on a stem', 'dg-label small', 'middle')))
    P.append(part('cleat-backing backing-plate', '        <rect class="dg-hull shape" x="730" y="170" width="140" height="10"/><rect class="dg-hull-dark shape" x="760" y="180" width="80" height="8"/><path class="dg-line" d="M796,160 V190 M804,160 V190" stroke-width="2.5"/>\n' + label(800, 230, 'Deck and backing plate', 'dg-label small', 'middle')))
    P.append(part('cleat-load', '        <path class="dg-accent" d="M744,140 L706,112" stroke-width="2" marker-end="url(#wn-arrow)"/>\n' + label(800, 256, 'Mooring loads pull sideways', 'dg-label small', 'middle') + '\n' + label(800, 270, 'and up at once: the two bolts', 'dg-label small', 'middle') + '\n' + label(800, 284, 'take shear and tension together', 'dg-label small', 'middle')))
    return '\n'.join(P)

# ---------------------------------------------------------------- two-station hydraulic steering, schematic (viewBox 0 0 900 420)
def hydraulic_steering():
    from gen_engine_diagrams import lines
    P = [marker('hy-arrow')]
    P.append(title(450, 24, 'Hydraulic steering with two helms: a schematic'))
    P.append(muted(450, 42, 'not any particular boat’s plumbing: follow your system’s manual'))
    def pump(x, name):
        body = (f'        <rect class="dg-hull shape" x="{x}" y="110" width="80" height="64" rx="6"/>'
                f'<ellipse class="dg-hull-dark shape" cx="{x - 14}" cy="142" rx="9" ry="44"/>'
                f'<rect class="dg-hull-dark" x="{x - 10}" y="138" width="14" height="8"/>\n'
                + lines(x + 40, 96, [name], 'dg-label small', 'middle'))
        return part('helm-pump', body)
    def lockv(x):
        return part('hp-lock', f'        <circle class="dg-accent-fill shape" cx="{x + 40}" cy="160" r="6"/>')
    P.append(pump(110, 'Wheelhouse helm'))
    P.append(pump(400, 'Cockpit helm'))
    P.append(lockv(110)); P.append(lockv(400))
    P.append(part('hp-lock', lines(530, 120, ['lock valves in each pump:', 'the rudder cannot turn the', 'wheel, and two helms can', 'share one ram'], 'dg-label small', 'start') + '\n' + lead(526, 130, 446, 158)))
    # the two hoses: A (upper, y=250 on the right) and B (lower, y=292)
    A = 'M130,174 L130,250 L690,250'
    A2 = 'M420,174 L420,250'
    hop = lambda x, y: f'L{x - 6},{y} A6,6 0 0 1 {x + 6},{y}'
    B = f'M170,174 L170,244 A6,6 0 0 1 170,256 L170,292 L790,292 L790,274'
    B2 = f'M460,174 L460,244 A6,6 0 0 1 460,256 L460,292'
    hose = ''.join(f'<path class="dg-line shape" d="{d}" stroke-width="3" fill="none"/>' for d in (A, A2, B, B2))
    dots = '<circle cx="420" cy="250" r="4" fill="var(--dg-line)"/><circle cx="460" cy="292" r="4" fill="var(--dg-line)"/>'
    flow = ('<path class="dg-accent" d="M560,250 L600,250" marker-end="url(#hy-arrow)"/>'
            '<path class="dg-accent" d="M600,292 L560,292" marker-end="url(#hy-arrow)"/>')
    P.append(part('hydraulic-hose', f'        {hose}{dots}{flow}\n' + lines(240, 240, ['two hoses carry the oil'], 'dg-label small', 'start')))
    # bypass valve between the hoses, near the ram
    P.append(part('bypass-valve', '        <path class="dg-line shape" d="M640,250 L640,292" stroke-width="3"/><circle cx="640" cy="250" r="4" fill="var(--dg-line)"/><circle cx="640" cy="292" r="4" fill="var(--dg-line)"/>'
                  '<path class="dg-bad-fill shape" d="M630,262 L650,262 L630,280 L650,280 Z"/>\n'
                  + lines(582, 332, ['Bypass valve: open,', 'oil flows straight across', 'and the wheels are', 'disconnected, so the', 'emergency tiller can steer'], 'dg-label small', 'start') + '\n' + lead(640, 320, 640, 284)))
    # the ram, its rod and the tiller arm on the stock (seen from above)
    P.append(part('hydraulic-ram', '        <rect class="dg-hull-dark shape" x="690" y="238" width="110" height="36" rx="5"/>'
                  '<rect class="dg-hull shape" x="738" y="240" width="10" height="32"/>'
                  '<path class="dg-line shape" d="M748,256 L848,256" stroke-width="4"/>\n'
                  + lines(745, 226, ['Ram'], 'dg-label small', 'middle')))
    P.append(part('steer-stock', '        <path class="dg-hull-dark shape" d="M848,252 L862,300 L852,302 L840,258 Z"/>'
                  '<circle class="dg-hull shape" cx="858" cy="304" r="12"/><circle class="dg-line" cx="858" cy="304" r="4" fill="var(--dg-line)"/>\n'
                  + lines(892, 206, ['tiller arm on', 'the rudder stock'], 'dg-label small', 'end') + '\n' + lead(872, 224, 858, 290)))
    P.append(part('emergency-tiller', lines(892, 396, ['the emergency tiller fits', 'the top of the stock'], 'dg-label small', 'end') + '\n' + lead(870, 384, 860, 318)))
    # an autopilot pump teed in, dashed
    P.append(part('hp-autopilot', '        <rect class="dg-thin shape" x="500" y="330" width="70" height="40" rx="5" fill="none" stroke-dasharray="4 3"/>'
                  '<path class="dg-thin" d="M520,330 L520,298 A6,6 0 0 1 520,286 L520,250 M550,330 L550,292" stroke-dasharray="4 3" fill="none"/>'
                  '<circle cx="520" cy="250" r="3.5" fill="var(--dg-line)"/><circle cx="550" cy="292" r="3.5" fill="var(--dg-line)"/>\n'
                  + lines(360, 344, ['autopilot pump,', 'if fitted, teed into', 'the same hoses'], 'dg-label small', 'start')))
    P.append(muted(450, 408, 'turning either wheel pumps oil to one end of the ram and draws it from the other'))
    return '\n'.join(P)
