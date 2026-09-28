# Diagram builders for sections/11-navigation.html. Marks are drawn side-on (as seen from a boat), placed on plan-view charts.
import math
from gen_hull_diagrams import part, label, lead, title, muted, marker
from gen_rig_diagrams import marker2, dim
from gen_engine_diagrams import badge, arrow, lines

_clip = [0]

def mlines(x, y, texts, anchor='middle', step=14):
    return '\n'.join(muted(x, y + i * step, t, anchor) for i, t in enumerate(texts))

# ---------------------------------------------------------------- mark drawing
H = {'can': 40, 'cone': 48, 'pillar': 60}
def _outline(kind, x, y, s):
    if kind == 'can':
        return f'M{x-14*s},{y} L{x-14*s},{y-40*s} L{x+14*s},{y-40*s} L{x+14*s},{y} Z'
    if kind == 'cone':
        return f'M{x-17*s},{y} L{x-3*s},{y-46*s} Q{x},{y-49*s} {x+3*s},{y-46*s} L{x+17*s},{y} Z'
    return (f'M{x-20*s},{y} L{x-14*s},{y-12*s} L{x-7*s},{y-12*s} L{x-7*s},{y-60*s} L{x+7*s},{y-60*s} '
            f'L{x+7*s},{y-12*s} L{x+14*s},{y-12*s} L{x+20*s},{y} Z')

def _topmark(tm, x, ty, s):
    k = s
    tri_up = lambda b, h: f'M{x-7*k},{b} L{x+7*k},{b} L{x},{b-h} Z'
    tri_dn = lambda t, h: f'M{x-7*k},{t} L{x+7*k},{t} L{x},{t+h} Z'
    if tm == 'can':
        return f'<rect class="dg-mk dg-mk-red" x="{x-6*k}" y="{ty-12*k}" width="{12*k}" height="{12*k}"/>'
    if tm == 'cone':
        return f'<path class="dg-mk dg-mk-green" d="{tri_up(ty, 13*k)}"/>'
    if tm == 'N':
        return f'<path class="dg-mk dg-mk-black" d="{tri_up(ty, 11*k)} {tri_up(ty-14*k, 11*k)}"/>'
    if tm == 'S':
        return f'<path class="dg-mk dg-mk-black" d="{tri_dn(ty-11*k, 11*k)} {tri_dn(ty-25*k, 11*k)}"/>'
    if tm == 'E':
        return f'<path class="dg-mk dg-mk-black" d="{tri_dn(ty-11*k, 11*k)} {tri_up(ty-13*k, 11*k)}"/>'
    if tm == 'W':
        return f'<path class="dg-mk dg-mk-black" d="{tri_up(ty, 11*k)} {tri_dn(ty-25*k, 11*k)}"/>'
    if tm == 'balls':
        return f'<circle class="dg-mk dg-mk-black" cx="{x}" cy="{ty-5*k}" r="{5*k}"/><circle class="dg-mk dg-mk-black" cx="{x}" cy="{ty-17*k}" r="{5*k}"/>'
    if tm == 'redball':
        return f'<circle class="dg-mk dg-mk-red" cx="{x}" cy="{ty-6*k}" r="{6*k}"/>'
    if tm == 'x':
        return (f'<path class="dg-mk" d="M{x-6*k},{ty-13*k} L{x+6*k},{ty-1*k} M{x+6*k},{ty-13*k} L{x-6*k},{ty-1*k}" stroke="#15181c" stroke-width="{5*k}" stroke-linecap="round"/>'
                f'<path d="M{x-6*k},{ty-13*k} L{x+6*k},{ty-1*k} M{x+6*k},{ty-13*k} L{x-6*k},{ty-1*k}" stroke="#f2c200" stroke-width="{3*k}" stroke-linecap="round"/>')
    if tm == 'cross':
        return (f'<path d="M{x},{ty-15*k} L{x},{ty} M{x-7*k},{ty-8*k} L{x+7*k},{ty-8*k}" stroke="#15181c" stroke-width="{5*k}" stroke-linecap="round"/>'
                f'<path d="M{x},{ty-15*k} L{x},{ty} M{x-7*k},{ty-8*k} L{x+7*k},{ty-8*k}" stroke="#f2c200" stroke-width="{3*k}" stroke-linecap="round"/>')
    return ''

def mark(x, y, kind, bands, tm=None, s=1.0, vertical=False, cls='shape', chip=False):
    """a buoy at waterline point (x,y). bands: colour names top to bottom (or left to right if vertical)."""
    _clip[0] += 1
    cid = f'nvclip{_clip[0]}'
    d = _outline(kind, x, y, s)
    h = H[kind] * s
    out = [f'<defs><clipPath id="{cid}"><path d="{d}"/></clipPath></defs>']
    if chip:
        top = y - h - (40 if tm in ('N', 'S', 'E', 'W', 'balls') else 30) * s
        out.append(f'<rect class="dg-day" x="{x-28*s:.1f}" y="{top:.1f}" width="{56*s:.1f}" height="{y - top + 6*s:.1f}" rx="6"/>')
    out.append(f'<g clip-path="url(#{cid})">')
    n = len(bands)
    if vertical:
        w = 44 * s
        for i, c in enumerate(bands * 3):
            out.append(f'<rect class="dg-mk-{c}" x="{x - 22*s + i*w/(n*3):.1f}" y="{y-h-2}" width="{w/(n*3)+0.5:.1f}" height="{h+4}"/>')
    else:
        for i, c in enumerate(bands):
            out.append(f'<rect class="dg-mk-{c}" x="{x-24*s}" y="{y - h + i*h/n:.1f}" width="{48*s}" height="{h/n+0.5:.1f}"/>')
    out.append('</g>')
    out.append(f'<path class="dg-mk {cls}" d="{d}" fill="none"/>')
    if tm:
        out.append(f'<line class="dg-line" x1="{x}" y1="{y-h}" x2="{x}" y2="{y-h-8*s}" stroke-width="2"/>')
        out.append(_topmark(tm, x, y - h - 8*s, s))
    return ''.join(out)

def water(x, y, w):
    return f'<path class="dg-lead" d="M{x},{y} q6,-4 12,0 t12,0 t12,0 t12,0 t12,0 t12,0" transform="translate(0,0)" fill="none"/>' if w else ''

def glow(x, y, c, r=6):
    return f'<circle class="dg-lt dg-lt-{c}" cx="{x}" cy="{y}" r="{r*2}" opacity=".28"/><circle class="dg-lt dg-lt-{c}" cx="{x}" cy="{y}" r="{r}"/>'

def mhull(x, y, heading, L=70, B=24, cls='dg-hull'):
    h = L / 2
    d = (f'M0,{-h} C{B*0.45},{-h*0.72} {B*0.52},{-h*0.1} {B*0.5},{h*0.35} L{B*0.42},{h} L{-B*0.42},{h} L{-B*0.5},{h*0.35} '
         f'C{-B*0.52},{-h*0.1} {-B*0.45},{-h*0.72} 0,{-h} Z')
    return f'<g transform="translate({x},{y}) rotate({heading})"><path class="{cls}" d="{d}"/></g>'

# ---------------------------------------------------------------- lateral marks (viewBox 0 0 900 420)
def lateral():
    P = [marker('lt-arrow')]
    P.append(title(225, 24, 'Entering harbour in IALA region A'))
    P.append(muted(225, 42, 'seen from above; the marks drawn side-on'))
    P.append('      <rect class="dg-water" x="20" y="56" width="410" height="350" rx="6"/>')
    P.append('      <path class="dg-land" d="M20,56 L110,56 C96,120 70,200 60,280 C54,330 50,370 44,406 L20,406 Z"/>')
    P.append('      <path class="dg-land" d="M430,56 L340,56 C356,120 380,200 390,280 C396,330 400,370 406,406 L430,406 Z"/>')
    P.append('      <rect class="dg-hull-dark" x="110" y="56" width="230" height="16"/>')
    P.append(muted(225, 90, 'harbour', 'middle'))
    for (x, y, sc) in ((140, 180, .7), (125, 270, .8), (110, 370, .9)):
        P.append('      ' + mark(x, y, 'can', ['red'], 'can', sc, cls=''))
    for (x, y, sc) in ((310, 180, .7), (325, 270, .8), (340, 370, .9)):
        P.append('      ' + mark(x, y, 'cone', ['green'], 'cone', sc, cls=''))
    P.append('      ' + mhull(225, 330, 0, 60, 22))
    P.append(part('nv-buoyage-direction', '        <line class="dg-accent shape" x1="225" y1="290" x2="225" y2="206" stroke-width="3" marker-end="url(#lt-arrow)"/>\n' + lines(214, 244, ['Direction', 'of buoyage'], 'dg-label small', 'end')))
    P.append(muted(86, 400, 'red to port', 'start'))
    P.append(muted(364, 400, 'green to starboard', 'end'))
    # right: the four lateral marks
    P.append(title(675, 24, 'The lateral marks'))
    P.append(muted(675, 42, 'light rhythms are examples; the chart gives each one'))
    xs = (525, 625, 725, 825)
    y = 190
    P.append('      <rect class="dg-water" x="470" y="' + str(y) + '" width="410" height="26"/>')
    P.append(part('nv-port-mark', '        ' + mark(xs[0], y, 'can', ['red'], 'can') + '\n' + lines(xs[0], 238, ['Port-hand', 'mark'], 'dg-label small', 'middle') + '\n' + mlines(xs[0], 270, ['red, can', 'red light,', 'e.g. Fl R 4s'], 'middle')))
    P.append(part('nv-stbd-mark', '        ' + mark(xs[1], y, 'cone', ['green'], 'cone') + '\n' + lines(xs[1], 238, ['Starboard-', 'hand mark'], 'dg-label small', 'middle') + '\n' + mlines(xs[1], 270, ['green, cone', 'green light,', 'e.g. Fl G 5s'], 'middle')))
    P.append(part('nv-pref-stbd', '        ' + mark(xs[2], y, 'can', ['red', 'green', 'red'], 'can') + '\n' + lines(xs[2], 238, ['Main channel', 'to starboard'], 'dg-label small', 'middle') + '\n' + mlines(xs[2], 270, ['red, green band', 'Fl(2+1) R'], 'middle')))
    P.append(part('nv-pref-port', '        ' + mark(xs[3], y, 'cone', ['green', 'red', 'green'], 'cone') + '\n' + lines(xs[3], 238, ['Main channel', 'to port'], 'dg-label small', 'middle') + '\n' + mlines(xs[3], 270, ['green, red band', 'Fl(2+1) G'], 'middle')))
    P.append(mlines(675, 336, ['Where two channels split, the modified marks show the', 'main one: treat them as the colour of their main body.', 'Shapes can be cans, cones, pillars or spars; colour', 'and topmark decide.'], 'middle'))
    return '\n'.join(P)

# ---------------------------------------------------------------- cardinal marks (viewBox 0 0 900 560)
def cardinals():
    P = []
    P.append(title(450, 24, 'Cardinal marks: pass on the side they are named after'))
    P.append(muted(450, 42, 'a north cardinal is north of the danger: pass north of it. All cardinal lights are white'))
    cx, cy = 450, 300
    P.append('      <rect class="dg-water" x="20" y="56" width="860" height="490" rx="6"/>')
    for ang in (45, 135, 225, 315):
        r = math.radians(ang)
        P.append(f'      <line class="dg-thin" x1="{cx}" y1="{cy}" x2="{cx + 330*math.sin(r):.0f}" y2="{cy - 230*math.cos(r):.0f}" stroke-dasharray="4 5"/>')
    P.append(part('nv-cb-danger', f'        <path class="dg-land shape" d="M{cx-26},{cy+6} L{cx-12},{cy-14} L{cx+6},{cy-10} L{cx+24},{cy+8} L{cx+4},{cy+18} Z"/>\n' + label(cx, cy + 40, 'the danger', 'dg-label small', 'middle')))
    for t, x, y in (('N', cx, 76), ('E', 868, cy + 4), ('S', cx, 540), ('W', 32, cy + 4)):
        P.append(label(x, y, t, 'dg-title', 'middle'))
    def card_(key, x, y, bands, tm, lx, ly, anc, name, txt):
        return part(key, '        ' + mark(x, y, 'pillar', bands, tm, .9, chip=True) + '\n' + lines(lx, ly, [name] + txt, 'dg-label small', anc))
    P.append(card_('nv-north', cx, 170, ['black', 'yellow'], 'N', cx + 40, 102, 'start', 'North cardinal', ['black over yellow; cones point up', 'Q or VQ: quick flashes, without a break']))
    P.append(card_('nv-south', cx, 470, ['yellow', 'black'], 'S', cx + 40, 476, 'start', 'South cardinal', ['yellow over black; cones down', 'Q(6)+LFl 15s or VQ(6)+LFl 10s:', 'six, then a long flash (6 o’clock)']))
    P.append(card_('nv-east', 690, cy + 26, ['black', 'yellow', 'black'], 'E', 730, cy + 60, 'start', 'East cardinal', ['black, yellow, black;', 'cones base to base', 'Q(3) 10s or VQ(3) 5s:', 'three (3 o’clock)']))
    P.append(card_('nv-west', 210, cy + 26, ['yellow', 'black', 'yellow'], 'W', 170, cy + 60, 'end', 'West cardinal', ['yellow, black, yellow;', 'cones point to point', 'Q(9) 15s or VQ(9) 10s:', 'nine (9 o’clock)']))
    P.append(mlines(40, 90, ['The black bands are where', 'the cones point.'], 'start'))
    return '\n'.join(P)

# ---------------------------------------------------------------- other marks (viewBox 0 0 900 340)
def other_marks():
    P = []
    P.append(title(450, 24, 'The other four marks'))
    y = 150
    P.append('      <rect class="dg-water" x="20" y="' + str(y) + '" width="860" height="26"/>')
    xs = (120, 340, 560, 780)
    P.append(part('nv-isolated', '        ' + mark(xs[0], y, 'pillar', ['black', 'red', 'black'], 'balls', chip=True) + '\n' + lines(xs[0], 204, ['Isolated danger'], 'dg-label small', 'middle') + '\n' + mlines(xs[0], 224, ['black, red band(s),', 'two black balls', 'white light Fl(2)', 'a small danger right under it,', 'safe water all round'], 'middle')))
    P.append(part('nv-safe-water', '        ' + mark(xs[1], y, 'pillar', ['red', 'white'], 'redball', vertical=True, chip=True) + '\n' + lines(xs[1], 204, ['Safe water'], 'dg-label small', 'middle') + '\n' + mlines(xs[1], 224, ['red and white stripes,', 'one red ball', 'white light: Iso, Oc,', 'LFl 10s or Mo(A)', 'the start of a channel, or its middle'], 'middle')))
    P.append(part('nv-special', '        ' + mark(xs[2], y, 'pillar', ['yellow'], 'x', chip=True) + '\n' + lines(xs[2], 204, ['Special mark'], 'dg-label small', 'middle') + '\n' + mlines(xs[2], 224, ['yellow, yellow X', 'yellow light', 'not a navigation mark: a zone,', 'an outfall, a racing or data buoy;', 'the chart says what'], 'middle')))
    P.append(part('nv-wreck', '        ' + mark(xs[3], y, 'pillar', ['blue', 'yellow'], 'cross', vertical=True, chip=True) + '\n' + lines(xs[3], 204, ['Emergency wreck'], 'dg-label small', 'middle') + '\n' + mlines(xs[3], 224, ['blue and yellow stripes,', 'yellow upright cross', 'alternating blue and', 'yellow flashes', 'a new wreck, not yet on the chart'], 'middle')))
    return '\n'.join(P)

# ---------------------------------------------------------------- a yacht's navigation lights (viewBox 0 0 900 480)
def nav_lights():
    P = []
    P.append(title(230, 24, 'A yacht’s lights, seen from above'))
    P.append(muted(230, 42, 'the arcs each light shows; not to scale'))
    cx, cy = 230, 250
    def sector(b1, b2, R, cls):
        p1 = (cx + R * math.sin(math.radians(b1)), cy - R * math.cos(math.radians(b1)))
        p2 = (cx + R * math.sin(math.radians(b2)), cy - R * math.cos(math.radians(b2)))
        large = 1 if (b2 - b1) % 360 > 180 else 0
        return f'<path class="{cls} shape" d="M{cx},{cy} L{p1[0]:.1f},{p1[1]:.1f} A{R},{R} 0 {large} 1 {p2[0]:.1f},{p2[1]:.1f} Z"/>'
    P.append(part('nv-steaming', '        ' + sector(-112.5, 112.5, 190, 'dg-arc-white') + '\n' + lines(40, 70, ['Steaming light (masthead light):', 'white, 225°, forward; under engine only'], 'dg-label small', 'start')))
    P.append(part('nv-green', '        ' + sector(0, 112.5, 130, 'dg-arc-green') + '\n' + lines(372, 186, ['Starboard', 'sidelight: green,', '112.5°, dead ahead', 'to 22.5° abaft', 'the beam'], 'dg-label small', 'start')))
    P.append(part('nv-red', '        ' + sector(-112.5, 0, 130, 'dg-arc-red') + '\n' + lines(88, 196, ['Port sidelight:', 'red, 112.5°'], 'dg-label small', 'end')))
    P.append(part('nv-stern', '        ' + sector(112.5, 247.5, 120, 'dg-arc-white') + '\n' + lines(cx, 400, ['Sternlight: white, 135°, astern'], 'dg-label small', 'middle')))
    P.append('      ' + mhull(cx, cy, 0, 64, 22))
    P.append(part('nv-tricolour', f'        <circle class="dg-warn-fill shape" cx="{cx}" cy="{cy-4}" r="4"/>\n' + mlines(cx, 420, ['Under sail, a boat under 20 m may show all three', 'in one tricolour lantern at the masthead instead;', 'never with the steaming light or the sidelights on'], 'middle')))
    # right: what you see
    P.append(title(690, 24, 'What you see of another boat at night'))
    tiles = [
        (('green', 'red'), ['Green on the left, red on the', 'right: coming straight at you'], None),
        (('green',), ['Green only: her starboard side;', 'she is crossing to your right'], None),
        (('red',), ['Red only: her port side;', 'she is crossing to your left'], None),
        (('white',), ['White only: her sternlight (you', 'are overtaking), or at anchor'], None),
        (('green', 'red'), ['White above red and green: a', 'power vessel heading at you'], 'white'),
        (('red',), ['Red or green high up alone:', 'a sailing yacht’s tricolour'], 'high'),
    ]
    for i, (cols, txt, extra) in enumerate(tiles):
        tx = 490 + (i % 2) * 206
        ty = 54 + (i // 2) * 132
        P.append(f'      <rect class="dg-night" x="{tx}" y="{ty}" width="198" height="124" rx="6"/>')
        P.append(f'      <line class="dg-night-line" x1="{tx+12}" y1="{ty+80}" x2="{tx+186}" y2="{ty+80}"/>')
        ly = ty + 60
        if extra == 'high':
            P.append('      ' + glow(tx + 99, ty + 22, cols[0]))
        else:
            if len(cols) == 2:
                P.append('      ' + glow(tx + 84, ly, cols[0]) + glow(tx + 114, ly, cols[1]))
            else:
                P.append('      ' + glow(tx + 99, ly, cols[0]))
            if extra == 'white':
                P.append('      ' + glow(tx + 99, ty + 26, 'white'))
        for j, t in enumerate(txt):
            P.append(f'      <text class="dg-night-text" x="{tx+99}" y="{ty+100+j*14}" text-anchor="middle">{t}</text>')
    return '\n'.join(P)

# ---------------------------------------------------------------- lights and shapes of other vessels (viewBox 0 0 900 440)
def vessel_lights():
    P = []
    P.append(title(450, 24, 'Lights and day shapes that say what a vessel is doing'))
    P.append(muted(450, 42, 'in each panel: the all-round lights shown at night (left) and the black shapes shown by day (right)'))
    def shape(kind, x, y):
        if kind == 'ball':
            return f'<circle class="dg-mk on-day dg-mk-black" cx="{x}" cy="{y}" r="8"/>'
        if kind == 'diamond':
            return f'<path class="dg-mk on-day dg-mk-black" d="M{x},{y-11} L{x+8},{y} L{x},{y+11} L{x-8},{y} Z"/>'
        if kind == 'cylinder':
            return f'<rect class="dg-mk on-day dg-mk-black" x="{x-7}" y="{y-12}" width="14" height="24"/>'
        if kind == 'cones-together':
            return f'<path class="dg-mk on-day dg-mk-black" d="M{x-8},{y-16} L{x+8},{y-16} L{x},{y-2} Z M{x-8},{y+14} L{x+8},{y+14} L{x},{y} Z"/>'
        if kind == 'cone-down':
            return f'<path class="dg-mk on-day dg-mk-black" d="M{x-8},{y-7} L{x+8},{y-7} L{x},{y+8} Z"/>'
        return ''
    tiles = [
        ('nv-anchored', 'At anchor', ['white'], ['ball'], 'one white light, one ball'),
        ('nv-nuc', 'Not under command', ['red', 'red'], ['ball', 'ball'], '“red over red, the captain is dead”'),
        ('nv-ram', 'Restricted in ability|to manoeuvre', ['red', 'white', 'red'], ['ball', 'diamond', 'ball'], 'dredging, laying cable, and so on'),
        ('nv-cbd', 'Constrained by|her draught', ['red', 'red', 'red'], ['cylinder'], 'a big ship confined to deep water'),
        ('nv-trawling', 'Trawling', ['green', 'white'], ['cones-together'], '“green over white, trawling tonight”'),
        ('nv-fishing', 'Fishing, not trawling', ['red', 'white'], ['cones-together'], '“red over white, fishing at night”'),
        ('nv-pilot', 'Pilot vessel on duty', ['white', 'red'], [], '“white over red, pilot ahead”'),
        ('nv-motorsailing', 'Yacht motor-sailing', ['steaming'], ['cone-down'], 'by day: a cone, point down'),
    ]
    for i, (key, name, lts, shp, note) in enumerate(tiles):
        tx = 16 + (i % 4) * 222
        ty = 60 + (i // 4) * 190
        body = [f'<rect class="dg-night" x="{tx}" y="{ty}" width="112" height="130" rx="6"/>',
                f'<rect class="dg-day" x="{tx+116}" y="{ty}" width="88" height="130" rx="6"/>',
                f'<line class="dg-night-line" x1="{tx+56}" y1="{ty+14}" x2="{tx+56}" y2="{ty+120}"/>',
                f'<line class="dg-day-line" x1="{tx+160}" y1="{ty+10}" x2="{tx+160}" y2="{ty+120}"/>']
        if lts == ['steaming']:
            body.append(glow(tx + 56, ty + 34, 'white'))
            body.append(glow(tx + 42, ty + 92, 'green') + glow(tx + 70, ty + 92, 'red'))
            body.append(f'<text class="dg-night-text" x="{tx+56}" y="{ty+60}" text-anchor="middle">steaming light</text>')
            body.append(f'<text class="dg-night-text" x="{tx+56}" y="{ty+116}" text-anchor="middle">and sidelights</text>')
        else:
            n = len(lts)
            top = ty + 65 - (n - 1) * 14
            for j, c in enumerate(lts):
                body.append(glow(tx + 56, top + j * 28, c))
        if shp:
            n = len(shp)
            top = ty + 65 - (n - 1) * 15
            for j, k in enumerate(shp):
                body.append(shape(k, tx + 160, top + j * 30))
        else:
            body.append(f'<rect x="{tx+128}" y="{ty+46}" width="64" height="40" fill="#e3eaf1"/><text class="dg-day-text" x="{tx+160}" y="{ty+62}" text-anchor="middle">by day:</text><text class="dg-day-text" x="{tx+160}" y="{ty+78}" text-anchor="middle">flag H</text>')
        body.append(f'<rect class="shape-fill" x="{tx}" y="{ty}" width="204" height="130"/>')
        lab = name.split('|')
        P.append(part(key, '        ' + ''.join(body) + '\n' + lines(tx + 102, ty + 150, lab, 'dg-label small', 'middle') + '\n' + label(tx + 102, ty + 150 + 14 * len(lab), note, 'dg-muted', 'middle')))
    return '\n'.join(P)

# ---------------------------------------------------------------- true, magnetic, compass (viewBox 0 0 900 380)
def compass():
    P = [marker('cp-arrow')]
    P.append(title(230, 24, 'Three norths'))
    P.append(muted(230, 42, 'angles exaggerated'))
    ox, oy = 230, 340
    def ray(deg, L, cls, key, text, tx, ty, anc='middle'):
        r = math.radians(deg)
        x2, y2 = ox + L * math.sin(r), oy - L * math.cos(r)
        return part(key, f'        <line class="{cls} shape" x1="{ox}" y1="{oy}" x2="{x2:.1f}" y2="{y2:.1f}" stroke-width="3" marker-end="url(#cp-arrow)"/>\n' + lines(tx, ty, text, 'dg-label small', anc))
    P.append(ray(0, 260, 'dg-line', 'nv-true', ['True north', '(the chart’s grid)'], 230, 64))
    P.append(ray(-16, 236, 'dg-accent', 'nv-magnetic', ['Magnetic north'], 120, 106, 'middle'))
    P.append(ray(-8, 200, 'dg-accent', 'nv-compass-n', ['Compass north'], 330, 150, 'start') + lead(328, 146, 205, 150))
    P.append(ray(100, 140, 'dg-lead', 'nv-heading', ['Heading', '100° true'], 378, 352, 'start'))
    P.append(part('nv-variation', f'        <path class="dg-warn-fill" d="M{ox},{oy-180} A180,180 0 0 0 {ox-180*math.sin(math.radians(16)):.1f},{oy-180*math.cos(math.radians(16)):.1f} L{ox},{oy} Z" opacity=".35"/>\n' + lines(40, 200, ['Variation: the angle', 'from true to magnetic,', 'here west. It changes', 'with place and year.'], 'dg-label small', 'start')))
    P.append(part('nv-deviation', f'        <path class="dg-bad-fill" d="M{ox-110*math.sin(math.radians(16)):.1f},{oy-110*math.cos(math.radians(16)):.1f} A110,110 0 0 1 {ox-110*math.sin(math.radians(8)):.1f},{oy-110*math.cos(math.radians(8)):.1f} L{ox},{oy} Z" opacity=".45"/>\n' + lines(40, 290, ['Deviation: the boat’s own', 'iron and wiring pull the', 'compass, here east.', 'It changes with heading.'], 'dg-label small', 'start')))
    # right: the ladder
    P.append(title(690, 24, 'Converting a course: an example'))
    rows = [('True', '100°', '(from the chart)'), ('Variation', '3° W', 'add west'), ('Magnetic', '103°', ''), ('Deviation', '2° E', 'subtract east'), ('Compass', '101°', '(steer this)')]
    for i, (n, v, note) in enumerate(rows):
        y = 70 + i * 50
        box = (i % 2 == 0)
        if box:
            P.append(f'      <rect class="dg-hull" x="540" y="{y}" width="220" height="36" rx="6"/>')
        P.append(label(556, y + 23, n, 'dg-label', 'start'))
        P.append(label(700, y + 23, v, 'dg-title', 'middle'))
        if note:
            P.append(muted(776, y + 23, note, 'start'))
        if i < 4:
            P.append(arrow(650, y + 44, 90, 'dg-flow'))
    P.append(mlines(690, 336, ['“Tele-Vision Makes Dull Company”: True, Variation, Magnetic,', 'Deviation, Compass. Going down the list add west, subtract east;', 'going up (compass to true), the opposite.'], 'middle'))
    return '\n'.join(P)

# ---------------------------------------------------------------- chart datum, depths and heights (viewBox 0 0 900 420)
def datum():
    P = [marker2('dt-arrow')]
    P.append(title(450, 24, 'Depths and heights on a chart'))
    P.append(muted(450, 42, 'a side view; heights exaggerated'))
    CD, SEA, HW = 250, 200, 140
    P.append(f'      <rect class="dg-water" x="20" y="{SEA}" width="720" height="{380-SEA}"/>')
    P.append(f'      <path class="dg-hull-dark" d="M20,380 L20,300 C120,300 140,{CD-18} 170,{CD-18} C200,{CD-18} 210,300 300,330 C400,352 520,344 620,300 C680,270 720,200 740,150 L760,60 L880,60 L880,380 Z"/>')
    P.append('      <rect class="dg-hull" x="800" y="40" width="18" height="30"/><circle class="dg-warn-fill" cx="809" cy="36" r="6"/>')
    P.append(part('nv-hat', f'        <line class="dg-level shape" x1="20" y1="{HW}" x2="760" y2="{HW}"/>\n' + lines(24, HW - 8, ['High-water level (MHWS or HAT; the chart says which)'], 'dg-label small', 'start')))
    P.append(part('nv-sea-level', f'        <line class="dg-waterline shape" x1="20" y1="{SEA}" x2="740" y2="{SEA}"/>\n' + lines(24, SEA - 8, ['The sea now'], 'dg-label small', 'start')))
    P.append(part('nv-chart-datum', f'        <line class="dg-level shape" x1="20" y1="{CD}" x2="740" y2="{CD}" stroke="var(--dg-bad)"/>\n' + lines(24, CD + 18, ['Chart datum: about the lowest tide (LAT)'], 'dg-label small', 'start')))
    P.append(part('nv-drying', '        ' + dim(170, CD, 170, CD - 18, 'dt-arrow', '', 'dg-accent') + '\n' + lines(196, 164, ['Drying height: above chart', 'datum; underlined on the chart'], 'dg-label small', 'start') + '\n' + lead(196, 182, 174, CD - 12)))
    P.append(part('nv-charted-depth', '        ' + dim(420, CD, 420, 338, 'dt-arrow', '', 'dg-accent') + '\n' + lines(430, 304, ['Charted depth:', 'below chart datum'], 'dg-label small', 'start')))
    P.append(part('nv-height-of-tide', '        ' + dim(330, SEA, 330, CD, 'dt-arrow', '', 'dg-accent') + '\n' + lines(340, 222, ['Height of tide:', 'from the tide tables'], 'dg-label small', 'start')))
    P.append(part('nv-depth', '        ' + dim(560, SEA, 560, 317, 'dt-arrow', '', 'dg-accent') + '\n' + lines(570, 218, ['Depth of water now =', 'charted depth +', 'height of tide'], 'dg-label small', 'start')))
    P.append(part('nv-light-height', '        ' + dim(840, HW, 840, 36, 'dt-arrow', '', 'dg-accent') + '\n' + lines(730, 76, ['Heights of lights', 'and clearances', 'under bridges'], 'dg-label small', 'end') + '\n' + lead(732, 84, 836, 90)))
    return '\n'.join(P)

# ---------------------------------------------------------------- course to steer (viewBox 0 0 900 420)
def tide_triangle():
    P = [marker('tt3-arrow')]
    P.append(title(330, 24, 'Course to steer across a tidal stream'))
    P.append(muted(330, 42, 'one hour of it, drawn on the chart; north up'))
    A = (110, 360)
    B = (560, 110)
    k = 58  # px per nautical mile
    tide = (2.0 * k, 0)          # 2 knots setting east
    T = (A[0] + tide[0], A[1] + tide[1])
    # ground track direction unit
    gx, gy = B[0] - A[0], B[1] - A[1]
    gl = math.hypot(gx, gy); ux, uy = gx / gl, gy / gl
    # find point C on A + t*u with |C - T| = 5 knots
    sp = 5.0 * k
    fx, fy = A[0] - T[0], A[1] - T[1]
    b = 2 * (fx * ux + fy * uy); c = fx * fx + fy * fy - sp * sp
    t = (-b + math.sqrt(b * b - 4 * c)) / 2
    C = (A[0] + t * ux, A[1] + t * uy)
    P.append(f'      <rect class="dg-water" x="20" y="56" width="620" height="350" rx="6"/>')
    P.append(f'      <circle class="dg-line" cx="{A[0]}" cy="{A[1]}" r="5" fill="var(--dg-line)"/><circle class="dg-line" cx="{B[0]}" cy="{B[1]}" r="5" fill="var(--dg-line)"/>')
    P.append(label(A[0] - 14, A[1] + 20, 'A', 'dg-title', 'middle'))
    P.append(label(B[0] + 14, B[1] - 10, 'B', 'dg-title', 'middle'))
    def arrows_on(p, q, n, cls):
        ang = math.degrees(math.atan2(q[1] - p[1], q[0] - p[0]))
        out = []
        for i in range(n):
            f = 0.5 + (i - (n - 1) / 2) * 0.06
            out.append(arrow(p[0] + (q[0] - p[0]) * f, p[1] + (q[1] - p[1]) * f, ang, cls))
        return '\n'.join(out)
    P.append(part('nv-ground-track', f'        <line class="dg-line shape" x1="{A[0]}" y1="{A[1]}" x2="{B[0]}" y2="{B[1]}" stroke-width="2.5"/>\n' + arrows_on(A, C, 2, 'dg-flow') + '\n' + lines(250, 196, ['1 Ground track, A to B', '(two arrows)'], 'dg-label small', 'end')))
    P.append(part('nv-tide-vector', f'        <line class="dg-accent shape" x1="{A[0]}" y1="{A[1]}" x2="{T[0]}" y2="{T[1]}" stroke-width="3"/>\n' + arrows_on(A, T, 3, 'dg-flow') + '\n' + lines(A[0] + 30, A[1] + 30, ['2 One hour of tidal stream from A:', '2 knots east (three arrows)'], 'dg-label small', 'start')))
    ang0 = math.degrees(math.atan2(C[1] - T[1], C[0] - T[0]))
    P.append(part('nv-water-track', f'        <line class="dg-warn-fill shape" x1="{T[0]}" y1="{T[1]}" x2="{C[0]:.1f}" y2="{C[1]:.1f}" stroke="var(--dg-warn)" stroke-width="3"/>\n'
                  + f'        <path class="dg-lead" d="M{T[0] + sp*math.cos(math.radians(ang0-12)):.1f},{T[1] + sp*math.sin(math.radians(ang0-12)):.1f} A{sp},{sp} 0 0 1 {T[0] + sp*math.cos(math.radians(ang0+12)):.1f},{T[1] + sp*math.sin(math.radians(ang0+12)):.1f}" stroke-dasharray="4 4"/>\n'
                  + arrows_on(T, C, 1, 'dg-flow') + '\n' + lines(390, 316, ['3 From the end of the tide, 5 miles', '(one hour at your speed) to cut the', 'track: the course to steer (one arrow)'], 'dg-label small', 'start')))
    P.append(part('nv-sog', lines(C[0] - 30, C[1] - 44, ['A to here: one hour’s progress', 'over the ground'], 'dg-label small', 'end') + '\n' + lead(C[0] - 28, C[1] - 36, C[0] - 4, C[1] - 4)))
    # right panel: reading
    brg = (math.degrees(math.atan2(C[0] - T[0], -(C[1] - T[1]))) % 360)
    gtb = (math.degrees(math.atan2(gx, -gy)) % 360)
    sog = t / k
    P.append(title(770, 90, 'This example'))
    P.append(lines(770, 116, [f'Track A to B: {gtb:03.0f}° true', 'Tide: 2 knots, setting 090°', '(flowing towards the east)', 'Boat speed: 5 knots', f'Course to steer: about {brg:03.0f}° true', f'Speed over ground: about {sog:.1f} knots'], 'dg-label small', 'middle', step=20))
    P.append(mlines(770, 262, ['Then allow for leeway', '(the wind pushing the boat', 'sideways) and convert', 'to a compass course.', 'Our arithmetic, for', 'illustration only.'], 'middle', step=16))
    return '\n'.join(P)

# ---------------------------------------------------------------- rule of twelfths (viewBox 0 0 900 360)
def twelfths():
    P = []
    P.append(title(450, 24, 'The rule of twelfths: how fast the tide rises'))
    P.append(muted(450, 42, 'from low water to high water in about six hours; a range of 4.8 m in this example'))
    x0, y0, w, h = 120, 300, 600, 220
    P.append(f'      <line class="dg-line" x1="{x0}" y1="{y0}" x2="{x0+w}" y2="{y0}"/><line class="dg-line" x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0-h-10}"/>')
    tw = [1, 2, 3, 3, 2, 1]
    cum = 0
    pts = []
    for i in range(61):
        tt = i / 60
        f = (1 - math.cos(math.pi * tt)) / 2
        pts.append(f'{x0 + tt*w:.1f},{y0 - f*h:.1f}')
    for i, n in enumerate(tw):
        bx = x0 + i * w / 6
        top = y0 - (cum + n) / 12 * h
        bot = y0 - cum / 12 * h
        P.append(f'      <rect class="dg-accent-fill" x="{bx+10:.0f}" y="{top:.1f}" width="{w/6-20:.0f}" height="{bot-top:.1f}" opacity=".35"/>')
        P.append(label(bx + w / 12, top - 8, f'{n}/12: {4.8*n/12:.1f} m', 'dg-label small', 'middle'))
        P.append(label(bx + w / 12, y0 + 18, f'hour {i+1}', 'dg-muted', 'middle'))
        cum += n
    P.append(part('nv-tide-curve', f'        <polyline class="dg-line shape" points="{" ".join(pts)}" fill="none" stroke-width="3"/>\n' + lines(x0 + w + 12, y0 - h + 4, ['High water', '4.8 m above', 'low water'], 'dg-label small', 'start')))
    P.append(label(x0 - 8, y0 + 4, 'LW', 'dg-label small', 'end'))
    P.append(part('nv-mid-tide', lines(x0 + w / 2 - 40, y0 - h / 2 - 84, ['Hours 3 and 4: half the', 'range in two hours; the', 'stream runs hardest now'], 'dg-label small', 'end') + '\n' + lead(x0 + w / 2 - 36, y0 - h / 2 - 66, x0 + w / 2, y0 - h / 2)))
    P.append(mlines(450, 350, ['A rough guide only: it fails where tides are irregular, such as the double high water at Southampton.'], 'middle'))
    return '\n'.join(P)

# ---------------------------------------------------------------- a three-point fix and a transit (viewBox 0 0 900 440)
def _church(x, y):
    return f'<rect class="dg-hull-dark" x="{x-6}" y="{y-6}" width="12" height="12"/><path d="M{x},{y-18} L{x},{y-6} M{x-5},{y-13} L{x+5},{y-13}" stroke="var(--dg-line)" stroke-width="2"/>'
def _lighthouse(x, y):
    return f'<path class="dg-hull-dark" d="M{x-6},{y+8} L{x-3},{y-12} L{x+3},{y-12} L{x+6},{y+8} Z"/><circle class="dg-lt dg-lt-yellow" cx="{x}" cy="{y-15}" r="4"/>'
def _tower(x, y):
    return f'<path class="dg-hull-dark" d="M{x-7},{y+8} L{x},{y-16} L{x+7},{y+8} Z"/>'

def fix_transit():
    P = []
    P.append(title(450, 24, 'Fixing your position by eye'))
    P.append(muted(225, 46, 'a three-point fix: three bearings, one triangle'))
    P.append(muted(675, 46, 'a transit: two marks in line'))
    P.append('      <line class="dg-thin" x1="450" y1="56" x2="450" y2="430" stroke-dasharray="3 5"/>')
    # left: coast along the top, three landmarks, bearings to the boat
    P.append('      <path class="dg-land" d="M10,60 L440,60 L440,120 C380,150 330,110 280,140 C230,170 170,120 120,150 C80,170 40,140 10,160 Z"/>')
    A, B, C = (40, 150), (230, 118), (420, 110)
    boat = (228, 330)
    # the three bearing lines, each slightly off, to make a small cocked hat
    offs = [(-13, 6), (10, -10), (6, 13)]
    body = []
    for (lx, ly), (ox, oy) in zip((A, B, C), offs):
        tx, ty = boat[0] + ox, boat[1] + oy
        ex, ey = lx + (tx - lx) * 1.12, ly + (ty - ly) * 1.12
        body.append(f'        <line class="dg-accent shape" x1="{lx}" y1="{ly}" x2="{ex:.0f}" y2="{ey:.0f}" stroke-width="1.8"/>')
    P.append('      ' + _church(*A) + _lighthouse(*B) + _tower(*C))
    P.append(label(A[0], A[1] - 26, 'church', 'dg-label small', 'middle'))
    P.append(label(B[0] + 24, B[1] - 16, 'lighthouse', 'dg-label small', 'start'))
    P.append(label(C[0] + 10, C[1] - 24, 'radio mast', 'dg-label small', 'end'))
    P.append(part('nv-fix', '\n'.join(body) + '\n' + lines(20, 400, ['Three bearings, well spread round the', 'horizon, drawn on the chart from the', 'landmarks'], 'dg-label small', 'start') + '\n' + lead(150, 386, 205, 362)))
    P.append(part('nv-cocked-hat', f'        <circle class="dg-lead shape" cx="{boat[0] + 2}" cy="{boat[1] + 2}" r="22" fill="none" stroke-dasharray="3 3"/>\n'
                  + lines(318, 236, ['The small triangle', '(the “cocked hat”):', 'you are in or near it;', 'the smaller, the better'], 'dg-label small', 'start') + '\n' + lead(340, 282, 252, 322)))
    # right: a transit; lighthouse in front of a church, the line out to sea
    P.append('      <path class="dg-land" d="M460,60 L890,60 L890,110 C820,140 760,100 700,130 C640,160 560,120 460,150 Z"/>')
    L1, L2 = (660, 150), (620, 96)
    P.append('      ' + _lighthouse(*L1) + _church(*L2))
    P.append(label(L1[0] + 14, L1[1] + 4, 'lighthouse', 'dg-label small', 'start'))
    P.append(label(L2[0] + 14, L2[1] + 2, 'church', 'dg-label small', 'start'))
    dx, dy = L1[0] - L2[0], L1[1] - L2[1]
    ex, ey = L1[0] + dx * 5.2, L1[1] + dy * 5.2
    P.append(part('nv-transit-line', f'        <line class="dg-accent shape" x1="{L2[0]}" y1="{L2[1]}" x2="{ex:.0f}" y2="{ey:.0f}" stroke-width="2" stroke-dasharray="8 4"/>\n'
                  + lines(470, 400, ['When the two are in line, you', 'are somewhere on this line: the', 'most accurate position line there is'], 'dg-label small', 'start') + '\n' + lead(600, 386, 838, 390)))
    P.append('      ' + mhull(800, 330, -35, L=46, B=16))
    # what the helmsman sees
    P.append('      <rect class="dg-day" x="730" y="176" width="140" height="84" rx="6"/>')
    P.append('      <rect x="794" y="226" width="12" height="12" fill="#15181c"/><path d="M800,214 L800,226 M795,219 L805,219" stroke="#15181c" stroke-width="2"/>'
             '<path d="M794,254 L797,234 L803,234 L806,254 Z" fill="#15181c"/><circle class="dg-lt dg-lt-yellow" cx="800" cy="231" r="4"/>')
    P.append(f'      <line class="dg-day-line" x1="738" y1="252" x2="862" y2="252"/>')
    P.append(f'      <text class="dg-day-text" x="800" y="194" text-anchor="middle">from the boat:</text>')
    P.append(f'      <text class="dg-day-text" x="800" y="208" text-anchor="middle">one behind the other</text>')
    return '\n'.join(P)

# ---------------------------------------------------------------- a clearing bearing (viewBox 0 0 900 430)
def clearing_bearing():
    P = [marker('cb-arrow')]
    P.append(title(450, 24, 'A clearing bearing'))
    P.append(muted(450, 42, 'a compass bearing of a landmark that keeps you clear of a danger you cannot see'))
    Lx, Ly = 720, 108
    P.append('      <rect class="dg-water" x="0" y="56" width="900" height="360"/>')
    # the safe side, trimmed at the lighthouse: the bearing means nothing east of it
    px, py = 446, 300
    dx, dy = Lx - px, Ly - py
    brg = round(math.degrees(math.atan2(dx, -dy)))
    k = (396 - Ly) / (py - Ly)
    sx, sy = Lx - dx * k, Ly - dy * k
    P.append(f'      <path class="dg-ok-fill" d="M{sx:.0f},{sy:.0f} L{Lx},{Ly} L{Lx},396 Z" opacity=".22"/>')
    P.append('      <path class="dg-land" d="M0,56 L900,56 L900,96 C820,100 760,86 700,120 C640,150 560,110 500,140 C460,160 450,190 420,190 C390,190 380,150 330,140 C260,126 160,150 0,130 Z"/>')
    P.append('      ' + _lighthouse(Lx, Ly))
    P.append(label(Lx + 14, Ly + 4, 'lighthouse', 'dg-label small', 'start'))
    rocks = ''.join(f'<path d="M{x-5},{y} L{x},{y-6} L{x+5},{y}" stroke="var(--dg-line)" stroke-width="1.6" fill="none"/>' for x, y in ((400, 214), (416, 222), (430, 212), (388, 228), (408, 236)))
    P.append(part('nv-cb-danger', '        ' + rocks + f'\n        <circle class="dg-lead shape" cx="410" cy="222" r="26" fill="none" stroke-dasharray="3 3"/>\n'
                  + lines(250, 222, ['Rocks just under', 'the surface'], 'dg-label small', 'end') + '\n' + lead(254, 220, 382, 222)))
    # the line that would just touch the danger, and the clearing line drawn with a margin outside it
    tx, ty = 426, 250
    tk = (300 - Ly) / (ty - Ly)
    P.append(f'      <line class="dg-lead" x1="{Lx}" y1="{Ly}" x2="{Lx - (Lx - tx) * tk:.0f}" y2="300" stroke-dasharray="2 4"/>')
    ex_ = Lx - (Lx - tx) * tk
    P.append(lines(ex_ - 8, 318, ['line just touching the rocks;', 'the clearing line has a margin', 'outside it'], 'dg-label small', 'end'))
    rot = math.degrees(math.atan2(Ly - py, Lx - px))
    mxl, myl = (Lx + px) / 2, (Ly + py) / 2
    P.append(part('nv-clearing', f'        <line class="dg-accent shape" x1="{Lx}" y1="{Ly}" x2="{sx:.0f}" y2="{sy:.0f}" stroke-width="2.4" stroke-dasharray="10 5"/>\n'
                  + f'        <text class="dg-label" x="{mxl - 6:.0f}" y="{myl - 10:.0f}" text-anchor="middle" transform="rotate({rot:.1f} {mxl - 6:.0f} {myl - 10:.0f})">{brg:03d}°</text>\n'
                  + lines(600, 230, ['Clearing line: from anywhere', f'on it the lighthouse is at {brg:03d}°'], 'dg-label small', 'start') + '\n' + lead(640, 236, 660, 150)))
    P.append('      ' + mhull(420, 360, 80, L=46, B=16))
    P.append(part('nv-safe-side', lines(470, 364, [f'Safe side: keep the lighthouse at', f'not more than {brg:03d}° (“NMT {brg:03d}°”)'], 'dg-label small', 'start')))
    P.append('      ' + mhull(330, 240, 80, L=46, B=16))
    P.append(part('nv-danger-side', lines(40, 290, [f'Danger side: the lighthouse', f'at more than {brg:03d}°'], 'dg-label small', 'start') + '\n' + lead(170, 290, 310, 248)))
    P.append('      <line class="dg-line" x1="860" y1="180" x2="860" y2="140" stroke-width="2" marker-end="url(#cb-arrow)"/>' + label(860, 198, 'N', 'dg-label', 'middle'))
    P.append(muted(450, 426, 'watch the bearing with a hand-bearing compass as you go; take the number from the chart and correct it for variation'))
    return '\n'.join(P)

# ---------------------------------------------------------------- a ship's lights from three sides (viewBox 0 0 900 330)
def ship_views():
    P = []
    P.append(title(450, 24, 'A big ship at night, seen from three sides'))
    P.append(muted(450, 42, 'a power-driven vessel of 50 m or more: two white masthead lights (the rear one higher),'))
    P.append(muted(450, 57, 'a green sidelight on her right (starboard) side, a red on her left (port), and a white sternlight'))
    panels = [
        ('nv-ship-ahead', 'Head on', ['Green on your left, red on your', 'right, the white lights one above', 'the other: she is coming at you']),
        ('nv-ship-abeam', 'From her right-hand (starboard) side', ['Green, and the white lights', 'spread apart, the lower one at', 'the bow: she is crossing to your right']),
        ('nv-ship-astern', 'From astern', ['One white sternlight: you are', 'overtaking, or she is moving', 'away from you']),
    ]
    for i, (key, name, text) in enumerate(panels):
        tx, ty, w, h = 30 + i * 290, 70, 260, 170
        b = [f'<rect class="dg-night" x="{tx}" y="{ty}" width="{w}" height="{h}" rx="6"/>',
             f'<line class="dg-night-line" x1="{tx + 10}" y1="{ty + 140}" x2="{tx + w - 10}" y2="{ty + 140}" stroke-width="1"/>']
        cx = tx + w / 2
        if i == 0:
            b.append(f'<path class="dg-night-line" d="M{cx - 36},{ty + 140} L{cx - 30},{ty + 110} L{cx + 30},{ty + 110} L{cx + 36},{ty + 140}" stroke-width="1"/>')
            b += [glow(cx, ty + 54, 'white'), glow(cx, ty + 82, 'white'), glow(cx - 28, ty + 118, 'green'), glow(cx + 28, ty + 118, 'red')]
        elif i == 1:
            b.append(f'<path class="dg-night-line" d="M{cx - 110},{ty + 116} L{cx + 96},{ty + 116} L{cx + 116},{ty + 140} L{cx - 104},{ty + 140} Z" stroke-width="1"/>')
            b += [glow(cx - 60, ty + 50, 'white'), glow(cx + 60, ty + 80, 'white'), glow(cx + 10, ty + 108, 'green')]
            b.append(f'<text class="dg-night-text" x="{cx + 96}" y="{ty + 160}" text-anchor="middle">bow →</text>')
        else:
            b.append(f'<path class="dg-night-line" d="M{cx - 36},{ty + 140} L{cx - 36},{ty + 110} L{cx + 36},{ty + 110} L{cx + 36},{ty + 140}" stroke-width="1"/>')
            b.append(glow(cx, ty + 104, 'white'))
        b.append(f'<rect class="shape-fill" x="{tx}" y="{ty}" width="{w}" height="{h}"/>')
        P.append(part(key, '        ' + ''.join(b) + '\n' + label(cx, ty + h + 22, name, 'dg-label', 'middle')))
        P.append(mlines(cx, ty + h + 40, text))
    return '\n'.join(P)
