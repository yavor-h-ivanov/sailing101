# Diagram builders for sections/10-manoeuvres.html. Plan views: pontoon or quay at the bottom unless stated.
import math
from gen_hull_diagrams import part, label, lead, title, muted, bow, marker
from gen_rig_diagrams import marker2
from gen_engine_diagrams import badge, arrow, lines, swatch

def hull(x, y, heading=90, L=200, B=64, cls='dg-hull', extra=''):
    """plan-view hull centred at (x,y); heading in degrees clockwise from north (90 = bow to the right)."""
    h = L / 2
    d = (f'M0,{-h} C{B*0.45},{-h*0.72} {B*0.52},{-h*0.1} {B*0.5},{h*0.35} L{B*0.42},{h} L{-B*0.42},{h} L{-B*0.5},{h*0.35} '
         f'C{-B*0.52},{-h*0.1} {-B*0.45},{-h*0.72} 0,{-h} Z')
    return f'<g transform="translate({x},{y}) rotate({heading})"><path class="{cls}" d="{d}"{extra}/></g>'

def pt(x, y, heading, fx, fy):
    """world point of a boat-local point (fx across to starboard, fy forward positive)."""
    r = math.radians(heading)
    # local frame: forward = (sin r, -cos r), starboard = (cos r, sin r)
    return (x + fy * math.sin(r) + fx * math.cos(r), y - fy * math.cos(r) + fx * math.sin(r))

def pontoon(x1, x2, y, h=26):
    return f'<rect class="dg-hull-dark" x="{x1}" y="{y}" width="{x2-x1}" height="{h}" rx="3"/>'

def cleat(x, y):
    return f'<rect class="dg-line" x="{x-6}" y="{y-2}" width="12" height="4" rx="2" fill="var(--dg-line)"/>'

def fender(x, y, vertical=False):
    return f'<rect class="dg-sail-2" x="{x-9 if not vertical else x-5}" y="{y-5 if not vertical else y-9}" width="{18 if not vertical else 10}" height="{10 if not vertical else 18}" rx="5"/>'

# ---------------------------------------------------------------- prop walk and pivot point (viewBox 0 0 900 380)
def prop_walk():
    P = [marker('pw-arrow')]
    P.append(title(225, 26, 'Prop walk: the stern kicks sideways in astern'))
    P.append(title(675, 26, 'The pivot point'))
    P.append('      <line class="dg-thin" x1="450" y1="40" x2="450" y2="370" stroke-dasharray="3 5"/>')
    # left: boat bow up, going astern
    P.append('      <rect class="dg-water" x="20" y="50" width="410" height="310" rx="8"/>')
    P.append('      ' + hull(225, 200, 0, L=220, B=70))
    P.append(muted(225, 120, 'bow'))
    P.append(part('pw-astern', '        <line class="dg-accent shape" x1="300" y1="150" x2="300" y2="250" marker-end="url(#pw-arrow)" stroke-width="3"/>\n' + lines(312, 200, ['Going astern'], 'dg-label small', 'start')))
    P.append(part('pw-kick', '        <line class="shape" x1="215" y1="300" x2="130" y2="300" stroke="var(--dg-bad)" stroke-width="4" marker-end="url(#pw-arrow)"/>\n' + lines(40, 312, ['A right-handed', 'propeller pulls the', 'stern to port', '(left, bow up)'], 'dg-label small', 'start')))
    P.append(part('pw-prop', '        <ellipse class="dg-hull-dark shape" cx="225" cy="318" rx="16" ry="5"/>\n' + lines(250, 322, ['Propeller'], 'dg-label small', 'start')))
    # right: pivot point
    P.append('      <rect class="dg-water" x="470" y="50" width="410" height="310" rx="8"/>')
    P.append('      ' + hull(675, 205, 0, L=220, B=70, cls='dg-hull', extra=' opacity=".35"'))
    P.append('      <g transform="translate(675,165) rotate(22)">' + hull(0, 40, 0, L=220, B=70) + '</g>')
    P.append(part('pw-pivot', '        <circle class="dg-bad-fill shape" cx="675" cy="165" r="7"/>\n' + lines(484, 110, ['Turning ahead, the boat', 'pivots about a third of its', 'length back from the bow'], 'dg-label small', 'start') + '\n' + lead(590, 142, 668, 164)))
    P.append(part('pw-stern-swing', '        <path class="dg-accent shape" d="M668,326 Q640,330 624,312" marker-end="url(#pw-arrow)"/>\n' + lines(500, 346, ['The stern swings out much more than', 'the bow swings in: leave room for it'], 'dg-label small', 'start')))
    P.append(muted(675, 80, 'turning to starboard, going ahead'))
    return '\n'.join(P)

# ---------------------------------------------------------------- mooring lines alongside (viewBox 0 0 900 330)
def mooring_lines():
    P = []
    P.append(title(450, 24, 'Alongside a pontoon: the four lines'))
    P.append(muted(450, 42, 'seen from above, bow to the right'))
    P.append('      <rect class="dg-water" x="0" y="60" width="900" height="200"/>')
    P.append('      ' + pontoon(20, 880, 244, 34))
    P.append(muted(150, 300, 'pontoon'))
    x, y = 450, 196
    P.append('      ' + hull(x, y, 90, L=340, B=80))
    # boat cleats (world): bow cleat, stern cleat, midships cleats
    bowc = pt(x, y, 90, 30, 150)   # starboard bow
    sternc = pt(x, y, 90, 34, -150)
    midf = pt(x, y, 90, 38, 30)
    mida = pt(x, y, 90, 38, -40)
    pc = {'bow': (760, 252), 'stern': (140, 252), 'fs': (380, 252), 'as': (540, 252)}
    for k, (cx_, cy_) in pc.items():
        P.append('      ' + cleat(cx_, cy_))
    for fx in (340, 450, 560):
        P.append('      ' + fender(fx, 238))
    def line(key, a_, b_, lbl, lx, ly, anc='middle'):
        return part(key, f'        <line class="dg-line shape" x1="{a_[0]:.0f}" y1="{a_[1]:.0f}" x2="{b_[0]}" y2="{b_[1]}" stroke-width="3"/>\n        <line class="hit" x1="{a_[0]:.0f}" y1="{a_[1]:.0f}" x2="{b_[0]}" y2="{b_[1]}"/>\n' + lines(lx, ly, lbl, 'dg-label small', anc))
    P.append(line('ml-bow-line', bowc, pc['bow'], ['Bow line: holds the bow in;', 'stops the boat drifting back'], 800, 110) + lead(800, 128, 700, 240))
    P.append(line('ml-stern-line', sternc, pc['stern'], ['Stern line: holds the stern in;', 'stops the boat moving forward'], 100, 110) + lead(100, 128, 210, 242))
    P.append(line('ml-bow-spring', bowc, pc['fs'], ['Spring from the bow, leading aft:', 'stops the boat moving forward'], 560, 72, 'start') + lead(600, 90, 520, 236))
    P.append(line('ml-stern-spring', sternc, pc['as'], ['Spring from the stern, leading', 'forward: stops it moving back'], 340, 72, 'end') + lead(300, 90, 380, 238))
    P.append(part('ml-fenders', '        <rect class="shape-fill" x="330" y="232" width="240" height="12"/>\n' + lead(450, 312, 450, 244) + '\n' + lines(450, 326, ['Fenders between the hull and the pontoon, at the widest part'], 'dg-label small', 'middle')))
    P.append(bow(890, 150))
    return '\n'.join(P)

# ---------------------------------------------------------------- springing off (viewBox 0 0 900 360)
def springing():
    P = [marker('sp-arrow')]
    P.append(title(225, 26, 'Stern out: motor ahead against a bow spring'))
    P.append(title(675, 26, 'Bow out: motor astern against a stern spring'))
    P.append('      <line class="dg-thin" x1="450" y1="40" x2="450" y2="350" stroke-dasharray="3 5"/>')
    for ox in (0, 450):
        P.append(f'      <rect class="dg-water" x="{ox+10}" y="50" width="430" height="230"/>')
        P.append('      ' + pontoon(ox + 20, ox + 430, 270, 28))
    # left: bow spring; boat angled stern out (heading 70 means bow down towards pontoon slightly)
    x, y, h = 225, 212, 104
    P.append('      ' + hull(x, y, 90, L=260, B=64, extra=' opacity=".3"'))
    P.append('      ' + hull(x, y, h, L=260, B=64))
    bc = pt(x, y, h, 26, 118)
    P.append('      ' + cleat(250, 278))
    P.append(part('sp-bow-spring', f'        <line class="dg-line shape" x1="{bc[0]:.0f}" y1="{bc[1]:.0f}" x2="250" y2="278" stroke-width="3"/>\n        <line class="hit" x1="{bc[0]:.0f}" y1="{bc[1]:.0f}" x2="250" y2="278"/>\n' + lines(200, 320, ['Bow spring, doubled back so', 'it can be slipped from on board'], 'dg-label small', 'middle')))
    P.append(part('sp-bow-fender', f'        {fender(bc[0] + 4, bc[1] + 16)}\n' + lines(420, 350, ['Fender at the bow'], 'dg-label small', 'end')))
    P.append(part('sp-stern-out', '        <path class="dg-accent shape" d="M104,236 Q92,200 104,168" marker-end="url(#sp-arrow)"/>\n' + lines(30, 90, ['Gently ahead, steering as if to', 'turn towards the pontoon: the', 'stern swings out; then slip the', 'spring and reverse clear'], 'dg-label small', 'start')))
    # right: stern spring
    x2, y2, h2 = 675, 212, 76
    P.append('      ' + hull(x2, y2, 90, L=260, B=64, extra=' opacity=".3"'))
    P.append('      ' + hull(x2, y2, h2, L=260, B=64))
    sc = pt(x2, y2, h2, 30, -118)
    P.append('      ' + cleat(650, 278))
    P.append(part('sp-stern-spring', f'        <line class="dg-line shape" x1="{sc[0]:.0f}" y1="{sc[1]:.0f}" x2="650" y2="278" stroke-width="3"/>\n        <line class="hit" x1="{sc[0]:.0f}" y1="{sc[1]:.0f}" x2="650" y2="278"/>\n' + lines(700, 320, ['Stern spring, doubled back', 'so it can be slipped'], 'dg-label small', 'middle')))
    P.append(part('sp-stern-fender', f'        {fender(sc[0] - 4, sc[1] + 16)}\n' + lines(480, 350, ['Fender at the quarter'], 'dg-label small', 'start')))
    P.append(part('sp-bow-out', '        <path class="dg-accent shape" d="M796,236 Q808,200 796,168" marker-end="url(#sp-arrow)"/>\n' + lines(870, 90, ['Gently astern: the bow swings', 'out; then slip the spring', 'and motor ahead clear'], 'dg-label small', 'end')))
    P.append(bow(440, 64))
    P.append(bow(890, 64))
    return '\n'.join(P)

# ---------------------------------------------------------------- coming alongside (viewBox 0 0 900 340)
def alongside():
    P = [marker('al-arrow')]
    P.append(title(450, 24, 'Coming alongside port side to: slowly, into the wind or the tide'))
    P.append(muted(450, 42, 'seen from above; the boat approaches from the right and stops against the pontoon'))
    P.append('      <rect class="dg-water" x="0" y="56" width="900" height="220"/>')
    P.append('      ' + pontoon(20, 480, 262, 30))
    P.append(part('al-wind', '        <line class="dg-accent shape" x1="20" y1="100" x2="100" y2="100" marker-end="url(#al-arrow)" stroke-width="3"/><line class="dg-accent" x1="20" y1="130" x2="100" y2="130" marker-end="url(#al-arrow)" stroke-width="3"/>\n' + lines(24, 84, ['Wind or tide from ahead'], 'dg-label small', 'start')))
    P.append(part('al-track', '        <path class="dg-lead shape" d="M840,120 L520,200 Q420,224 280,232" stroke-dasharray="5 5"/>\n' + lines(520, 84, ['Approach at a shallow angle,', 'slowly: no faster than you would', 'be happy to touch the pontoon at'], 'dg-label small', 'start')))
    P.append('      ' + hull(740, 144, 256, L=150, B=48, extra=' opacity=".35"'))
    P.append('      ' + hull(480, 208, 260, L=150, B=48, extra=' opacity=".6"'))
    P.append('      ' + hull(260, 234, 270, L=150, B=48))
    P.append(badge(740, 190, 1))
    P.append(badge(480, 250, 2))
    P.append(badge(260, 200, 3))
    P.append(part('al-neutral', lines(500, 300, ['2 Neutral early; turn to lie parallel', 'as the bow nears the pontoon'], 'dg-label small', 'start')))
    P.append(part('al-stop', '        <path class="shape" d="M350,214 L350,246" stroke="var(--dg-bad)" stroke-width="3"/>\n' + arrow(350, 250, 90, 'dg-bad-fill') + '\n' + lines(150, 134, ['3 A short burst astern to stop. A right-handed', 'propeller kicks the stern to port: here, towards', 'the pontoon, which helps (red arrow)'], 'dg-label small', 'start')))
    P.append(part('al-step-off', lines(250, 318, ['Crew step off (never jump): the midships line', 'first, then the bow and stern lines, then springs'], 'dg-label small', 'middle')))
    return '\n'.join(P)

# ---------------------------------------------------------------- turning in a narrow fairway (viewBox 0 0 900 440)
def turn_tight():
    P = [marker('tt-arrow')]
    P.append(title(450, 24, 'Turning round in a narrow fairway'))
    P.append(muted(450, 42, 'seen from above; a right-handed propeller, so the boat turns to starboard (clockwise), where prop walk helps'))
    P.append('      <rect class="dg-water" x="0" y="52" width="900" height="348"/>')
    P.append('      ' + pontoon(0, 900, 52, 12))
    P.append('      ' + pontoon(0, 900, 388, 12))
    for bx in range(60, 900, 110):
        P.append('      ' + hull(bx, 104, 0, L=80, B=30, extra=' opacity=".55"'))
        P.append('      ' + hull(bx, 336, 180, L=80, B=30, extra=' opacity=".55"'))
    P.append(muted(20, 162, 'start: bow to the left (dashed)', 'start'))
    P.append(muted(20, 178, 'end: bow to the right', 'start'))
    cx, cy = 450, 222
    for h, op in ((330, '.3'), (30, '.45')):
        P.append('      ' + hull(cx, cy, h, L=150, B=48, extra=f' opacity="{op}"'))
    P.append('      ' + hull(cx - 24, cy + 18, 270, L=150, B=48, extra=' opacity=".75" stroke-dasharray="5 4"'))
    P.append('      ' + hull(cx, cy, 90, L=150, B=48))
    P.append(part('tt-rotation', '        <path class="dg-accent shape" d="M362,190 A92,92 0 0 1 520,160" stroke-width="3" marker-end="url(#tt-arrow)"/>\n' + lines(532, 168, ['turning clockwise, on the spot'], 'dg-label small', 'start')))
    P.append(badge(cx - 112, cy + 24, 1))
    P.append(badge(cx + 88, cy + 6, 4))
    P.append(part('tt-ahead', lines(24, 196, ['1 Helm hard to starboard, then a', 'short, firm burst ahead: the bow', 'turns before the boat gathers way'], 'dg-label small', 'start')))
    P.append(part('tt-astern', lines(24, 262, ['2 Neutral, then a burst astern: the', 'boat stops, and prop walk kicks the', 'stern to port, the same way round'], 'dg-label small', 'start')))
    P.append(part('tt-repeat', lines(600, 196, ['3 Repeat, leaving the helm hard', 'over: short bursts, never long', 'enough to move far'], 'dg-label small', 'start')))
    P.append(part('tt-room', lines(600, 262, ['4 Turned round in a little more', 'than her own length. Turned the', 'other way, prop walk fights you'], 'dg-label small', 'start')))
    return '\n'.join(P)

# ---------------------------------------------------------------- stern-to with lazy lines (viewBox 0 0 900 420)
def med_moor():
    P = [marker('md-arrow')]
    P.append(title(450, 24, 'Stern-to with lazy lines (Mediterranean mooring)'))
    P.append(muted(450, 42, 'seen from above, the quay at the bottom'))
    P.append('      <rect class="dg-water" x="0" y="56" width="900" height="300"/>')
    P.append('      <rect class="dg-hull-dark" x="0" y="356" width="900" height="50"/>')
    P.append(muted(120, 386, 'quay'))
    # neighbouring boats stern-to (bow up, heading 0, stern at the quay)
    for bx in (300, 600):
        P.append('      ' + hull(bx, 250, 0, L=190, B=66))
    # our boat reversing in (heading 0, i.e. bow up) between them
    P.append('      ' + hull(450, 250, 0, L=190, B=66))
    for fx in (406, 494):
        P.append('      ' + fender(fx, 290, True))
    P.append(part('md-fenders', '        <rect class="shape-fill" x="400" y="276" width="100" height="30"/>\n' + lines(450, 398, ['Fenders out on both sides'], 'dg-label small', 'middle')))
    # stern lines to the quay bollards, crossed
    P.append(part('md-stern-lines', '        <line class="dg-line shape" x1="428" y1="342" x2="470" y2="360" stroke-width="3"/><line class="dg-line shape" x1="472" y1="342" x2="430" y2="360" stroke-width="3"/><circle class="dg-hull" cx="470" cy="364" r="5"/><circle class="dg-hull" cx="430" cy="364" r="5"/>\n' + lines(520, 346, ['Two stern lines to the quay, crossed'], 'dg-label small', 'start') + '\n' + lead(518, 344, 474, 352)))
    # lazy line: from the quay out to the ground chain, lifted to the bow
    P.append(part('md-lazy-line', '        <path class="dg-thin shape" d="M440,362 C420,330 380,300 370,250 C362,200 380,140 450,118" stroke-dasharray="4 3" stroke-width="2"/>\n' + lines(40, 124, ['Lazy line: a light line from the quay to the mooring line,', 'picked up at the stern and walked forward outside everything'], 'dg-label small', 'start') + '\n' + lead(360, 142, 366, 200)))
    P.append(part('md-mooring-line', '        <path class="dg-line shape" d="M450,152 L450,80" stroke-width="4"/><rect class="dg-hull-dark shape" x="80" y="66" width="740" height="8" rx="3" opacity=".6"/>\n' + lines(470, 96, ['Heavy mooring line from the chain, made fast at the bow'], 'dg-label small', 'start')))
    P.append(part('md-ground-chain', '        <rect class="dg-hull-dark shape" x="80" y="66" width="740" height="8" rx="3" opacity=".6"/>\n' + lines(40, 96, ['Ground chain along the harbour bed'], 'dg-label small', 'start')))
    return '\n'.join(P)

# ---------------------------------------------------------------- box berth (viewBox 0 0 900 420)
def box_berth():
    P = [marker('bx-arrow')]
    P.append(title(450, 24, 'Box berth between posts (Baltic and North Sea harbours)'))
    P.append(muted(450, 42, 'seen from above, the quay or pontoon at the top; the boat goes in bow first'))
    P.append('      <rect class="dg-water" x="0" y="96" width="900" height="320"/>')
    P.append('      <rect class="dg-hull-dark" x="0" y="56" width="900" height="40"/>')
    P.append(muted(450, 82, 'quay'))
    # posts
    for px in (360, 540):
        for py in (330,):
            P.append(f'      <circle class="dg-hull-dark" cx="{px}" cy="{py}" r="10"/>')
    P.append(part('bx-posts', '        <circle class="shape-fill" cx="360" cy="330" r="12"/><circle class="shape-fill" cx="540" cy="330" r="12"/>\n' + lines(570, 350, ['Posts at the outer end of the box'], 'dg-label small', 'start')))
    # boat heading 0 (bow up) going in
    P.append('      ' + hull(450, 214, 0, L=210, B=70))
    P.append(part('bx-stern-lines', '        <path class="dg-line shape" d="M424,312 L360,330 M476,312 L540,330" stroke-width="3"/>\n' + lines(160, 360, ['Stern lines: loops dropped over each', 'post as the boat passes between them,', 'windward post first'], 'dg-label small', 'start') + '\n' + lead(300, 352, 380, 326)))
    P.append(part('bx-bow-lines', '        <path class="dg-line shape" d="M438,114 L410,96 M462,114 L490,96" stroke-width="3"/>\n' + lines(560, 130, ['Bow lines to the quay: a crew', 'member steps ashore from the bow'], 'dg-label small', 'start') + '\n' + lead(558, 126, 488, 100)))
    P.append(part('bx-wind', '        <line class="dg-accent shape" x1="80" y1="200" x2="170" y2="200" marker-end="url(#bx-arrow)" stroke-width="3"/><line class="dg-accent" x1="80" y1="230" x2="170" y2="230" marker-end="url(#bx-arrow)" stroke-width="3"/>\n' + lines(40, 166, ['Crosswind: take the', 'windward lines first'], 'dg-label small', 'start')))
    return '\n'.join(P)
