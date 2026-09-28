# Diagram builders for sections/09-sailing.html. In plan views the wind blows from the TOP.
import math
from gen_hull_diagrams import part, label, lead, title, muted, bow, marker
from gen_rig_diagrams import marker2
from gen_engine_diagrams import badge, arrow, lines, swatch

def _wedge(p0, p1, side, width, cls):
    """a thin filled sail from p0 to p1 with its belly to the side given (+1 starboard, -1 port), in local coords"""
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    L = math.hypot(dx, dy) or 1
    ux, uy = dx / L, dy / L
    px, py = -uy, ux
    if px * side < 0 or (abs(px) < 0.2 and py > 0):
        px, py = -px, -py
    mx, my = p0[0] + dx * 0.55 + px * width, p0[1] + dy * 0.55 + py * width
    return f'<path class="{cls}" d="M{p0[0]:.1f},{p0[1]:.1f} Q{mx:.1f},{my:.1f} {p1[0]:.1f},{p1[1]:.1f} Z" stroke-width="0.8"/>'

def boat(x, y, heading, boom=0, side=1, jib=True, flap=False, scale=1.0, cls='dg-hull shape', backed=False):
    """A small plan-view yacht at (x,y), heading in degrees clockwise from north (up).
    boom: angle of the boom from the centreline in degrees; side: +1 boom to starboard, -1 to port.
    The mainsail is a white wedge along the boom; the jib a cream wedge from the bow."""
    s = scale
    hull = f'<path class="{cls}" d="M0,{-32*s} C{8*s},{-22*s} {12*s},{-2*s} {9*s},{26*s} L{-9*s},{26*s} C{-12*s},{-2*s} {-8*s},{-22*s} 0,{-32*s} Z"/>'
    mast = (0, -6 * s)
    L = 30 * s
    b = math.radians(boom)
    E = (mast[0] + side * L * math.sin(b), mast[1] + L * math.cos(b))
    if flap:
        main = f'<path class="dg-line" d="M{mast[0]},{mast[1]} q4,6 0,10 q-4,6 0,10 q4,6 0,10" stroke-width="2.5"/>'
    else:
        main = _wedge(mast, E, side, 8.5 * s, 'dg-sail') + f'<line class="dg-line" x1="{mast[0]}" y1="{mast[1]}" x2="{E[0]:.1f}" y2="{E[1]:.1f}" stroke-width="2"/>'
    jibp = ''
    if jib:
        jside = -side if backed else side
        tack = (0, -30 * s)
        if flap:
            jibp = f'<path class="dg-line" d="M{tack[0]},{tack[1]} q-4,5 0,9 q4,5 0,9" stroke-width="2" opacity=".85"/>'
        else:
            jb = math.radians(max(boom * 0.6, 8))
            C = (tack[0] + jside * 28 * s * math.sin(jb), tack[1] + 28 * s * math.cos(jb))
            jibp = _wedge(tack, C, jside, 7.5 * s, 'dg-sail-2')
    return f'<g transform="translate({x:.1f},{y:.1f}) rotate({heading})">{hull}{jibp}{main}<circle class="dg-hull-dark" cx="{mast[0]}" cy="{mast[1]}" r="{2.2*s:.1f}"/></g>'

def wind_arrows(xs, y1, y2, mid='w-arrow'):
    return ''.join(f'<line class="dg-accent" x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" marker-end="url(#{mid})"/>' for x in xs)

# ---------------------------------------------------------------- points of sail (viewBox 0 0 900 640)
def points_of_sail():
    P = [marker('w-arrow')]
    cx, cy, R = 450, 350, 220
    P.append(part('pos-wind', '        ' + wind_arrows((400, 450, 500), 24, 76) + '\n' + label(450, 100, 'TRUE WIND', 'dg-title', 'middle')))
    # no-go zone
    a = math.radians(45)
    P.append(part('pos-no-go', f'        <path class="dg-zone shape" d="M{cx},{cy} L{cx - R*math.sin(a):.1f},{cy - R*math.cos(a):.1f} A{R},{R} 0 0 1 {cx + R*math.sin(a):.1f},{cy - R*math.cos(a):.1f} Z"/>\n' + label(cx, 196, 'No-go zone', 'dg-label', 'middle') + '\n' + label(cx, 212, 'about 45° either side of the wind', 'dg-label small', 'middle')))
    P.append(f'      <circle class="dg-lead" cx="{cx}" cy="{cy}" r="{R}" stroke-dasharray="4 6"/>')
    spots = [(45, 10, 'pos-close-hauled'), (67, 25, 'pos-close-reach'), (90, 45, 'pos-beam-reach'), (135, 65, 'pos-broad-reach')]
    for th, bm, key in spots:
        for sgn in (1, -1):
            t = math.radians(th * sgn)
            x, y = cx + R * math.sin(t), cy - R * math.cos(t)
            P.append(part(key, '        ' + boat(x, y, th * sgn, boom=bm, side=sgn)))
    P.append(part('pos-run', '        ' + boat(cx, cy + R, 180, boom=85, side=1)))
    # labels
    L = [('pos-close-hauled', 648, 150, ['Close-hauled', 'about 45° to the wind, sails in tight'], 'start'),
         ('pos-close-reach', 700, 238, ['Close reach'], 'start'),
         ('pos-beam-reach', 716, 316, ['Beam reach', 'wind at 90°, often fastest'], 'start'),
         ('pos-broad-reach', 648, 540, ['Broad reach', 'wind behind the beam'], 'start'),
         ('pos-run', 450, 610, ['Run: wind dead astern, sails right out'], 'middle')]
    for key, x, y, t, anc in L:
        P.append(part(key, lines(x, y, t, 'dg-label', anc)))
    for key, x, y, t in (('pos-close-hauled', 252, 150, ['Close-hauled']), ('pos-close-reach', 200, 238, ['Close reach']), ('pos-beam-reach', 184, 316, ['Beam reach']), ('pos-broad-reach', 252, 540, ['Broad reach'])):
        P.append(part(key, lines(x, y, t, 'dg-label', 'end')))
    P.append(part('pos-starboard-tack', lines(95, 400, ['Starboard tack:', 'wind over the', 'starboard side,', 'boom out to port'], 'dg-label small', 'middle')))
    P.append(part('pos-port-tack', lines(815, 420, ['Port tack:', 'wind over the', 'port side, boom', 'out to starboard'], 'dg-label small', 'middle')))
    # head up / bear away arrows on the right
    P.append(marker2('pos-dir'))
    def arcpt(deg, r=262):
        return f'{cx + r*math.sin(math.radians(deg)):.1f},{cy - r*math.cos(math.radians(deg)):.1f}'
    P.append(part('pos-head-up', f'        <path class="dg-accent shape" d="M{arcpt(118)} A262,262 0 0 0 {arcpt(72)}" marker-end="url(#pos-dir)"/>\n' + lines(724, 268, ['head up: turn', 'towards the wind'], 'dg-label small', 'start')))
    P.append(part('pos-bear-away', f'        <path class="dg-accent shape" d="M{arcpt(-100)} A262,262 0 0 0 {arcpt(-148)}" marker-end="url(#pos-dir)"/>\n' + lines(200, 486, ['bear away: turn', 'away from the wind'], 'dg-label small', 'end')))
    P.append(muted(cx, cy + 60, 'the heading relative to the wind'))
    P.append(muted(cx, cy + 76, 'names the point of sail'))
    return '\n'.join(P)

# ---------------------------------------------------------------- how a sail works, telltales (viewBox 0 0 900 420)
def sail_lift():
    P = [marker('sl-arrow')]
    P.append(title(230, 24, 'Sails are wings'))
    P.append(muted(230, 42, 'close-hauled on port tack, seen from above; wind from the top'))
    P.append('      ' + wind_arrows((90, 140), 54, 100, 'sl-arrow'))
    P.append(label(115, 118, 'WIND', 'dg-label small', 'middle'))
    # airflow first, under the boat
    P.append(part('sl-flow', '        <path class="dg-thin shape" d="M150,70 C200,120 250,150 320,196 C350,216 380,250 396,290" stroke-dasharray="5 4"/><path class="dg-thin shape" d="M110,120 C160,170 200,200 236,250 C252,272 262,300 266,330" stroke-dasharray="5 4"/>\n' + lines(20, 404, ['Air flows smoothly round both sides of each sail'], 'dg-label small', 'start')))
    P.append('      <g transform="translate(250,240) rotate(45)"><path class="dg-hull" d="M0,-90 C32,-54 36,24 24,78 L-24,78 C-36,24 -32,-54 0,-90 Z"/></g>')
    P.append(part('sl-sails', '        <g transform="translate(250,240) rotate(45)"><path class="dg-line shape" d="M0,-84 Q14,-50 10,-20" stroke-width="4"/><path class="dg-line shape" d="M0,-16 Q14,20 16,60" stroke-width="4"/><circle class="dg-hull-dark" cx="0" cy="-16" r="4"/></g>\n' + lines(20, 170, ['Jib and mainsail, curved like', 'wings, set at a small angle', 'to the wind'], 'dg-label small', 'start') + '\n' + lead(150, 178, 232, 214)))
    # forces from the centre of the sails, world coords. heading NE = (0.707,-0.707), leeward SE = (0.707,0.707)
    ox, oy = 262, 230
    tot = (0.35 * 0.707 + 0.94 * 0.707, -0.35 * 0.707 + 0.94 * 0.707)
    L = 110
    P.append(part('sl-force', f'        <line class="dg-accent shape" x1="{ox}" y1="{oy}" x2="{ox + L*tot[0]:.0f}" y2="{oy + L*tot[1]:.0f}" marker-end="url(#sl-arrow)" stroke-width="3"/>\n' + lines(330, 330, ['Total force from the sails:', 'mostly sideways, to leeward,', 'and a little forward'], 'dg-label small', 'start') + '\n' + lead(372, 318, ox + L*tot[0] - 4, oy + L*tot[1] + 4)))
    d = 0.35 * L
    P.append(part('sl-drive', f'        <line class="shape" x1="{ox}" y1="{oy}" x2="{ox + d*0.707:.0f}" y2="{oy - d*0.707:.0f}" stroke="var(--dg-ok)" stroke-width="3" marker-end="url(#sl-arrow)"/>\n' + lines(330, 150, ['Drive: the forward part', 'of that force'], 'dg-label small', 'start') + '\n' + lead(328, 154, ox + d*0.707 + 4, oy - d*0.707)))
    k = 0.94 * L * 0.8
    kx, ky = 236, 262
    P.append(part('sl-keel-force', f'        <line class="shape" x1="{kx}" y1="{ky}" x2="{kx - k*0.707:.0f}" y2="{ky - k*0.707:.0f}" stroke="var(--dg-bad)" stroke-width="3" marker-end="url(#sl-arrow)"/>\n' + lines(20, 300, ['The keel pushes back to', 'windward, so the boat goes', 'ahead, slipping only a little', 'sideways (leeway)'], 'dg-label small', 'start') + '\n' + lead(150, 296, kx - k*0.707 + 6, ky - k*0.707 + 20)))
    # telltales, side view of the jib luff: blue = windward (near side), red dashed = leeward (seen through the cloth)
    P.append(title(700, 24, 'Reading the jib’s telltales'))
    P.append(muted(700, 42, 'wool threads either side of the jib, just behind its front edge'))
    rows = [(110, 'Both streaming aft: trimmed right', None, 0, 0, 'tt-good'),
            (220, 'Windward one lifting:', 'too close to the wind; bear away, or pull the sheet in', 1, 0, 'tt-windward'),
            (330, 'Leeward one lifting:', 'too far off the wind; head up, or let the sheet out', 0, 1, 'tt-leeward')]
    for y, t1, t2, wl, ll, key in rows:
        cloth = f'<path class="dg-sail shape" d="M520,{y-44} L520,{y+44} L610,{y+44} Q600,{y} 610,{y-44} Z"/><line class="dg-line" x1="520" y1="{y-44}" x2="520" y2="{y+44}" stroke-width="3"/>'
        ww = f'<path d="M532,{y-6} q10,-14 22,-14" stroke="var(--dg-accent)" stroke-width="3" fill="none"/>' if wl else f'<path d="M532,{y-6} h26" stroke="var(--dg-accent)" stroke-width="3" fill="none"/>'
        lw = f'<path d="M532,{y+6} q10,-14 22,-14" stroke="var(--dg-bad)" stroke-width="3" fill="none" stroke-dasharray="4 3"/>' if ll else f'<path d="M532,{y+6} h26" stroke="var(--dg-bad)" stroke-width="3" fill="none" stroke-dasharray="4 3"/>'
        txt = [t1] if t2 is None else [t1] + [t2[:t2.index(';')+1], t2[t2.index(';')+2:]]
        P.append(part(key, '        ' + cloth + ww + lw + '\n' + lines(626, y - 6, txt, 'dg-label small', 'start')))
    P.append(muted(700, 404, 'blue: windward telltale; red dashed: leeward one'))
    return '\n'.join(P)

# ---------------------------------------------------------------- apparent wind (viewBox 0 0 900 400), wind from the top
def apparent():
    P = [marker('aw-arrow')]
    for mid, col in (('aw-arrow-l', 'var(--dg-line)'), ('aw-arrow-w', 'var(--dg-warn)')):
        P.append(f'      <defs><marker id="{mid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="{col}"/></marker></defs>')
    k = 10
    def vec(x1, y1, x2, y2, stroke, key, text, tx, ty, anc='start'):
        mk = {'var(--dg-line)': 'aw-arrow-l', 'var(--dg-warn)': 'aw-arrow-w'}.get(stroke, 'aw-arrow')
        return part(key, f'        <line class="shape" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="3" marker-end="url(#{mk})"/>\n' + lines(tx, ty, text, 'dg-label small', anc))
    P.append('      ' + wind_arrows((420, 480), 20, 60, 'aw-arrow'))
    P.append(label(450, 78, 'TRUE WIND', 'dg-label small', 'middle'))
    P.append('      <line class="dg-thin" x1="450" y1="90" x2="450" y2="390" stroke-dasharray="3 5"/>')
    for ox, hd, ttl in ((225, 45, 'Close-hauled on port tack'), (675, 135, 'Broad reach on port tack')):
        P.append(title(ox, 26, ttl))
        P.append(muted(ox, 44, '12 knots of true wind, 6 knots of boat speed'))
        bx, by = ox - 110, 250
        P.append('      ' + boat(bx, by, hd, boom=12 if hd == 45 else 60, side=1, scale=1.4, cls='dg-hull'))
        r = math.radians(hd)
        tw = (0, 12 * k)
        mw = (-math.sin(r) * 6 * k, math.cos(r) * 6 * k)
        aw = (tw[0] + mw[0], tw[1] + mw[1])
        S0 = (ox + 20, 110) if hd == 45 else (ox + 40, 130)
        M1 = (S0[0] + tw[0], S0[1] + tw[1])
        E1 = (M1[0] + mw[0], M1[1] + mw[1])
        P.append(vec(*S0, *M1, 'var(--dg-accent)', 'aw-true', ['True wind'], S0[0] + 10, S0[1] + 50))
        P.append(vec(*M1, *E1, 'var(--dg-line)', 'aw-motion', ['Wind of the boat’s', 'own motion'], (M1[0] + E1[0]) / 2 + 14 if hd == 45 else M1[0] + 12, (M1[1] + E1[1]) / 2 + 18 if hd == 45 else M1[1] + 20))
        P.append(vec(*S0, *E1, 'var(--dg-warn)', 'aw-apparent', ['Apparent wind'], (S0[0] + E1[0]) / 2 - 10, (S0[1] + E1[1]) / 2, 'end'))
        mag = math.hypot(*aw)
        src = (-aw[0], -aw[1])
        brg = math.degrees(math.atan2(src[0], -src[1])) % 360
        off = abs(((brg - hd) + 180) % 360 - 180)
        P.append(muted(ox, 360, f'apparent wind about {mag/k:.0f} knots, {off:.0f}° off the bow:'))
        P.append(muted(ox, 376, 'further forward than the true wind'))
    return '\n'.join(P)

# ---------------------------------------------------------------- tacking and gybing (viewBox 0 0 900 440)
def tack_gybe():
    P = [marker('tg-arrow')]
    P.append('      ' + wind_arrows((420, 480), 20, 64, 'tg-arrow'))
    P.append(label(450, 84, 'WIND', 'dg-label small', 'middle'))
    P.append(title(210, 26, 'Tacking: the bow turns through the wind'))
    P.append(title(690, 26, 'Gybing: the stern turns through the wind'))
    P.append('      <line class="dg-thin" x1="450" y1="96" x2="450" y2="430" stroke-dasharray="3 5"/>')
    # tack track
    P.append('      <path class="dg-lead" d="M110,400 L190,320 Q250,260 210,200 L130,120" stroke-dasharray="4 5"/>')
    steps = [(110, 400, 45, 10, 1, False, 1), (190, 320, 20, 6, 1, False, 2), (236, 256, 0, 0, 1, True, 3), (200, 186, -45, 10, -1, False, 4)]
    for x, y, h, bm, sd, fl, n in steps:
        P.append('      ' + boat(x, y, h, boom=bm, side=sd, flap=fl, scale=0.9))
        P.append(badge(x - 30, y + 6, n))
    P.append(part('tg-ready-about', lines(140, 414, ['1 “Ready about?”: crew ready', 'on both sheets; “Ready”'], 'dg-label small', 'start')))
    P.append(part('tg-lee-oh', lines(210, 350, ['2 “Lee-oh”: helm turns', 'the bow towards the wind'], 'dg-label small', 'start')))
    P.append(part('tg-head-to-wind', lines(270, 250, ['3 Head to wind: sails', 'flap; old jib sheet off'], 'dg-label small', 'start')))
    P.append(part('tg-new-tack', lines(20, 150, ['4 New tack: jib sheeted', 'in on the new side'], 'dg-label small', 'start')))
    # gybe track: SE to SW through a run
    P.append('      <path class="dg-lead" d="M560,130 L630,200 Q690,262 650,322 L590,392" stroke-dasharray="4 5"/>')
    gsteps = [(560, 130, 135, 65, 1, 1), (632, 204, 155, 20, 1, 2), (672, 270, 180, 0, 1, 3), (620, 356, 220, 65, -1, 4)]
    for x, y, h, bm, sd, n in gsteps:
        P.append('      ' + boat(x, y, h, boom=bm, side=sd, scale=0.9))
        P.append(badge(x + 32, y - 4, n))
    P.append(part('tg-stand-by', lines(610, 118, ['1 “Stand by to gybe”: check', 'the boom’s path is clear'], 'dg-label small', 'start')))
    P.append(part('tg-sheet-in', lines(700, 196, ['2 Mainsheet hauled in so the', 'boom is near the middle'], 'dg-label small', 'start')))
    P.append(part('tg-gybe-oh', lines(720, 274, ['3 “Gybe-oh”: the stern passes', 'through the wind, the boom', 'crosses a short distance'], 'dg-label small', 'start')))
    P.append(part('tg-ease-out', lines(660, 380, ['4 Ease the mainsheet out on', 'the new side; jib across'], 'dg-label small', 'start')))
    return '\n'.join(P)

# ---------------------------------------------------------------- heaving to (viewBox 0 0 900 320)
def heave_to():
    P = [marker('ht-arrow')]
    P.append(title(450, 24, 'Heaving to: parking the boat at sea'))
    P.append('      ' + wind_arrows((120, 170), 40, 90, 'ht-arrow'))
    P.append(label(145, 108, 'WIND', 'dg-label small', 'middle'))
    # boat on starboard tack about 50 deg off the wind, heading NW (-50)
    x, y, h = 470, 170, -50
    P.append('      ' + boat(x, y, h, boom=40, side=-1, jib=False, scale=2.4).replace('dg-hull shape', 'dg-hull'))
    # backed jib: on the windward side
    P.append(part('ht-backed-jib', f'        <g transform="translate({x},{y}) rotate({h})"><path class="dg-line shape" d="M0,-67 Q22,-40 38,-12" stroke-width="5"/></g>\n' + lines(560, 70, ['Jib backed: held on the windward', 'side, pushing the bow away'], 'dg-label small', 'start') + '\n' + lead(558, 74, 506, 120)))
    P.append(part('ht-main-eased', lines(250, 150, ['Mainsail eased: it', 'pushes the bow back', 'towards the wind'], 'dg-label small', 'start') + '\n' + lead(352, 154, 470, 196)))
    P.append(part('ht-helm-lashed', f'        <g transform="translate({x},{y}) rotate({h})"><line class="dg-accent shape" x1="0" y1="64" x2="-16" y2="40" stroke-width="4"/></g>\n' + lines(620, 230, ['Tiller lashed to leeward', '(wheel turned to windward):', 'the rudder tries to turn', 'the boat into the wind'], 'dg-label small', 'start') + '\n' + lead(618, 226, 532, 236)))
    P.append(part('ht-drift', '        <path class="dg-accent shape" d="M470,262 L439,299" stroke-dasharray="6 4" marker-end="url(#ht-arrow)"/>\n' + lines(430, 300, ['Slow drift, mostly to leeward'], 'dg-label small', 'end')))
    P.append(muted(450, 316, 'the forces balance: the boat lies quietly at about 45° to 60° off the wind, moving slowly'))
    return '\n'.join(P)

# ---------------------------------------------------------------- balance and heel (viewBox 0 0 900 360)
def balance():
    P = [marker('bl-arrow')]
    P.append(title(250, 24, 'Balance: sails against keel'))
    P.append(title(700, 24, 'Heel: wind against ballast'))
    P.append('      <line class="dg-thin" x1="480" y1="40" x2="480" y2="386" stroke-dasharray="3 5"/>')
    # side view left, bow right
    P.append('      <rect class="dg-water" x="0" y="250" width="476" height="140"/>')
    P.append('      <path class="dg-hull" d="M40,240 L440,240 C430,262 410,272 380,276 L90,280 C66,276 48,262 40,240 Z"/>')
    P.append('      <line class="dg-waterline" x1="0" y1="250" x2="476" y2="250"/>')
    P.append('      <path class="dg-hull-dark" d="M210,278 L196,340 L246,340 L262,276 Z"/><path class="dg-hull-dark" d="M78,276 L72,322 L92,322 L98,276 Z"/>')
    P.append('      <rect class="dg-hull-dark" x="246" y="50" width="6" height="190"/>')
    P.append('      <path class="dg-sail" d="M252,56 L252,226 L96,226 Z"/><path class="dg-sail-2" d="M246,62 L420,236 L262,232 Z" opacity=".8"/>')
    P.append(part('bl-ce', '        <circle class="dg-accent-fill shape" cx="200" cy="168" r="8"/>\n' + lines(20, 140, ['Centre of effort: where', 'the sails’ push is centred'], 'dg-label small', 'start') + '\n' + lead(150, 150, 194, 164)))
    P.append(part('bl-clr', '        <circle class="dg-bad-fill shape" cx="230" cy="300" r="8"/>\n' + lines(270, 330, ['Centre of lateral resistance:', 'where the keel and hull', 'resist being pushed sideways'], 'dg-label small', 'start') + '\n' + lead(268, 326, 238, 304)))
    P.append(part('bl-weather-helm', lines(20, 50, ['Push behind the resistance:', 'the boat tries to turn into', 'the wind (weather helm).', 'Reefing the main moves the', 'push forward and eases it'], 'dg-label small', 'start')))
    P.append(bow(470, 236))
    # heel view from astern, right
    P.append('      <rect class="dg-water" x="484" y="250" width="416" height="140"/>')
    P.append('      <line class="dg-waterline" x1="484" y1="250" x2="900" y2="250"/>')
    P.append('      <g transform="rotate(20 690 250)"><path class="dg-hull" d="M620,210 L760,210 C760,250 730,276 690,280 C650,276 620,250 620,210 Z"/><rect class="dg-hull-dark" x="684" y="278" width="12" height="60"/><rect class="dg-hull-dark" x="676" y="330" width="28" height="16" rx="6"/><rect class="dg-hull-dark" x="686" y="60" width="6" height="150"/></g>')
    P.append(part('bl-heel-force', '        <line class="dg-accent shape" x1="560" y1="130" x2="660" y2="160" stroke-width="3" marker-end="url(#bl-arrow)"/>\n' + lines(500, 100, ['The wind heels the boat'], 'dg-label small', 'start')))
    P.append(part('bl-ballast', '        <circle class="dg-hull-dark shape" cx="660" cy="333" r="5"/><line class="dg-bad-fill" x1="660" y1="333" x2="660" y2="378" stroke="var(--dg-bad)" stroke-width="3" marker-end="url(#bl-arrow)"/>\n' + lines(640, 360, ['Ballast in the', 'keel pulls down'], 'dg-label small', 'end')))
    P.append(part('bl-buoyancy', '        <circle class="dg-accent-fill shape" cx="720" cy="262" r="5"/><line x1="720" y1="262" x2="720" y2="222" stroke="var(--dg-ok)" stroke-width="3" marker-end="url(#bl-arrow)"/>\n' + lines(890, 190, ['Buoyancy moves to the', 'low side and pushes up;', 'the two together turn', 'the boat upright'], 'dg-label small', 'end')))
    return '\n'.join(P)

# ---------------------------------------------------------------- man overboard: the quick stop (viewBox 0 0 900 490)
def mob_quick_stop():
    P = [marker('mob-arrow')]
    P.append(title(450, 24, 'Man overboard: the quick stop'))
    P.append('      ' + wind_arrows((60, 100), 44, 92, 'mob-arrow'))
    P.append(label(80, 110, 'WIND', 'dg-label small', 'middle'))
    sc = 1.4
    # 1: the boat on a beam reach, just past the person
    P.append('      ' + boat(432, 282, 90, boom=55, side=1, scale=sc))
    P.append('      <path class="dg-lead" d="M477,282 C570,282 580,190 532,166" stroke-width="1.8" stroke-dasharray="5 5" marker-end="url(#mob-arrow)"/>')
    # 2: hove to after the tack, jib backed on the windward side
    bx, by, bh = 508, 140, -50
    P.append('      ' + boat(bx, by, bh, boom=40, side=-1, jib=False, scale=sc))
    P.append(f'      <g transform="translate({bx},{by}) rotate({bh})"><path class="dg-sail-2" d="M0,-42 Q16,-30 24,-6 Q10,-16 0,-42 Z" stroke-width="0.8"/><path class="dg-line" d="M0,-42 Q14,-24 24,-6" stroke-width="2"/></g>')
    # 3: under engine, away downwind, round, and back up nearly into the wind
    P.append('      <path class="dg-accent" d="M532,170 C660,240 640,450 500,452 C380,454 316,440 330,322" fill="none" stroke-dasharray="7 5" marker-end="url(#mob-arrow)"/>')
    # 4: stopped about 25 degrees off the wind, jib rolled away, main in the middle, the person alongside to leeward
    h4 = -25
    b4x, b4y = 318, 272
    P.append('      ' + boat(b4x, b4y, h4, boom=2, side=-1, jib=False, scale=sc))
    px, py = 298, 284
    P.append(part('mob-person', f'        <circle class="dg-accent-fill shape" cx="{px}" cy="{py}" r="7"/>\n'
                  f'        <circle class="dg-accent shape" cx="{px - 30}" cy="{py + 6}" r="9" fill="none" stroke-width="4"/>\n'
                  f'        <line class="dg-line shape" x1="{px - 46}" y1="{py - 24}" x2="{px - 46}" y2="{py + 16}" stroke-width="2"/><path class="dg-accent-fill shape" d="M{px - 46},{py - 24} L{px - 32},{py - 19} L{px - 46},{py - 14} Z"/>\n'
                  + label(px - 12, py + 26, 'person', 'dg-label small', 'middle') + '\n' + label(px - 30, py - 8, 'lifebuoy', 'dg-label small', 'end') + '\n' + label(px - 52, py - 26, 'danbuoy (pole with a flag)', 'dg-label small', 'end')))
    P.append(badge(474, 318, 1))
    P.append(badge(560, 118, 2))
    P.append(badge(652, 330, 3))
    P.append(badge(262, 346, 4))
    P.append(part('mob-shout', lines(398, 352, ['1 Shout “Man overboard!”; throw', 'the lifebuoy and danbuoy; point', 'at them; press the MOB button;', 'send a Mayday'], 'dg-label small', 'start')))
    P.append(part('mob-quick-stop', lines(610, 72, ['2 Tack at once, leaving the jib sheet', 'cleated: the boat stops itself (heaves', 'to) close to the person'], 'dg-label small', 'start') + '\n' + lead(608, 100, 572, 114)))
    P.append(part('mob-engine', lines(672, 318, ['3 Jib rolled away, mainsail pulled', 'in to the middle, every rope out of', 'the water; then engine on. Motor', 'away downwind and turn back'], 'dg-label small', 'start')))
    P.append(part('mob-approach', lines(30, 396, ['4 Come back slowly, nearly into the wind;', 'stop with them alongside on the downwind', '(leeward) side, just forward of the cockpit,', 'clear of the propeller; in neutral, engine', 'stopped if you can'], 'dg-label small', 'start') + '\n' + lead(220, 392, 256, 356)))
    P.append(swatch(672, 438, 'dg-lead" stroke-width="1.8" stroke-dasharray="5 5', 'under sail'))
    P.append(swatch(672, 458, 'dg-accent" stroke-dasharray="7 5', 'under engine'))
    P.append(muted(450, 484, 'schools teach variations; agree one method on your boat and practise it with a fender'))
    return '\n'.join(P)

# ---------------------------------------------------------------- twist, kicker and traveller (viewBox 0 0 900 480)
def twist():
    def chord(mx, my, ang, L, cls, width=2.5, dash='', op=''):
        a = math.radians(ang)
        ex, ey = mx + L * math.sin(a), my + L * math.cos(a)
        cx, cy = mx + L * 0.5 * math.sin(a) + 12 * math.cos(a), my + L * 0.5 * math.cos(a) - 12 * math.sin(a)
        d = f' stroke-dasharray="{dash}"' if dash else ''
        o = f' opacity="{op}"' if op else ''
        return f'<path class="{cls}" d="M{mx},{my} Q{cx:.1f},{cy:.1f} {ex:.1f},{ey:.1f}" fill="none" stroke-width="{width}"{d}{o}/>', (ex, ey)
    def para(x, y, texts):
        return '\n'.join(muted(x, y + 15 * k, t) for k, t in enumerate(texts))
    def sail(mx, my, angs, op=''):
        out = []
        for ang, cls, w, dash in zip(angs, ('dg-line', 'dg-line', 'dg-accent'), (2.5, 1.5, 2.5), ('', '5 4', '')):
            path, e = chord(mx, my, ang, 170, cls, w, dash, op)
            out.append('        ' + path)
        return out, e
    def outline(mx, my):
        return (f'      <g opacity=".35"><path class="dg-hull" d="M{mx},{my - 70} C{mx + 34},{my - 40} {mx + 44},{my + 60} {mx + 36},{my + 196} '
                f'L{mx - 36},{my + 196} C{mx - 44},{my + 60} {mx - 34},{my - 40} {mx},{my - 70} Z"/></g>')
    P = [marker('tw-arrow')]
    P.append(title(450, 24, 'Twist: how far the top of the mainsail falls away'))
    P.append(muted(450, 44, 'the mainsail seen from above, bow at the top; the boat is sailing as close to the wind as it can'))
    P.append('      <line class="dg-accent" x1="20" y1="70" x2="62" y2="100" marker-end="url(#tw-arrow)"/><line class="dg-accent" x1="20" y1="100" x2="62" y2="130" marker-end="url(#tw-arrow)"/>')
    P.append(label(40, 150, 'WIND', 'dg-label small', 'middle'))
    P.append('      <line class="dg-line" x1="280" y1="462" x2="314" y2="462" stroke-width="2.5"/>' + muted(322, 466, 'foot (the boom)', 'start'))
    P.append('      <line class="dg-line" x1="450" y1="462" x2="484" y2="462" stroke-width="1.5" stroke-dasharray="5 4"/>' + muted(492, 466, 'middle', 'start'))
    P.append('      <line class="dg-accent" x1="570" y1="462" x2="604" y2="462" stroke-width="2.5"/>' + muted(612, 466, 'head (the top)', 'start'))
    panels = [
        (170, 'tw-open', 'Open leech: sheet or kicker eased', (8, 20, 34), ['The top twists away and spills', 'wind: less power and less lean', '(heel), for gusts or when overpowered']),
        (450, 'tw-closed', 'Closed leech: sheet or kicker on', (8, 12, 16), ['The top stays nearly in line with', 'the boom: more power upwind. Too', 'tight and the top stalls (loses drive)']),
    ]
    for mx, key, head, angs, text in panels:
        my = 132
        P.append(outline(mx, my))
        body, _ = sail(mx, my, angs)
        body.insert(0, f'        <circle class="dg-hull-dark" cx="{mx}" cy="{my}" r="5"/>')
        P.append(part(key, '\n'.join(body) + '\n' + label(mx + 30, 356, head, 'dg-label', 'middle')))
        P.append(label(mx - 10, my + 4, 'mast', 'dg-label small', 'end'))
        P.append(para(mx + 30, 376, text))
    mx, my = 740, 132
    P.append(outline(mx, my))
    tb = [f'        <circle class="dg-hull-dark" cx="{mx}" cy="{my}" r="5"/>']
    before, _ = sail(mx, my, (2, 6, 10), '.3')
    after, _ = sail(mx, my, (13, 17, 21))
    tb += before + after
    tb.append(f'        <line class="dg-hull-dark" x1="{mx - 34}" y1="{my + 172}" x2="{mx + 34}" y2="{my + 172}" stroke-width="4" stroke-linecap="round"/>')
    tb.append(f'        <line class="dg-accent" x1="{mx - 20}" y1="{my + 186}" x2="{mx + 30}" y2="{my + 186}" stroke-width="2" marker-end="url(#tw-arrow)"/>')
    tb.append(label(mx + 40, my + 190, 'traveller let down', 'dg-label small', 'start'))
    P.append(part('tw-traveller', '\n'.join(tb) + '\n' + label(mx, 376, 'Traveller let down to leeward', 'dg-label', 'middle')))
    P.append(label(mx - 10, my + 4, 'mast', 'dg-label small', 'end'))
    P.append(para(mx, 396, ['The faint lines show the sail before', 'the traveller moved. The whole sail', 'swings out and the twist stays the', 'same: the quick way to spill a gust']))
    return '\n'.join(P)

# ---------------------------------------------------------------- man overboard under sail: reach, tack, reach (viewBox 0 0 900 470)
def mob_reach_tack_reach():
    P = [marker('rtr-arrow')]
    P.append(title(450, 24, 'Man overboard under sail alone: reach, tack, reach'))
    P.append('      ' + wind_arrows((60, 100), 44, 92, 'rtr-arrow'))
    P.append(label(80, 110, 'WIND', 'dg-label small', 'middle'))
    sc = 1.3
    px, py = 300, 250
    # 1: away on a beam reach
    P.append('      ' + boat(430, 250, 90, boom=55, side=1, scale=sc))
    # 2: tack
    P.append('      <path class="dg-lead" d="M472,250 L570,250 C650,250 655,170 600,172" stroke-width="1.8" stroke-dasharray="5 5" marker-end="url(#rtr-arrow)"/>')
    P.append('      ' + boat(610, 190, 0, flap=True, scale=sc, cls='dg-hull'))
    # 3: bear away on a broad reach to get downwind of the person
    P.append('      <path class="dg-lead" d="M592,196 L470,330" stroke-width="1.8" stroke-dasharray="5 5" marker-end="url(#rtr-arrow)"/>')
    P.append('      ' + boat(500, 300, 222, boom=60, side=-1, scale=sc))
    # 4: round up onto a close reach towards the person, sheets eased, stopping with them to leeward
    P.append('      <path class="dg-lead" d="M460,344 C430,366 380,300 358,272" stroke-width="1.8" stroke-dasharray="5 5" marker-end="url(#rtr-arrow)"/>')
    cx, cy, ch = 318, 232, -50
    P.append('      ' + boat(cx, cy, ch, flap=True, scale=sc))
    P.append(part('rtr-person', f'        <circle class="dg-accent-fill shape" cx="{px}" cy="{py}" r="7"/>\n'
                  f'        <circle class="dg-accent shape" cx="{px - 30}" cy="{py + 12}" r="9" fill="none" stroke-width="4"/>\n'
                  + label(px - 10, py + 30, 'person', 'dg-label small', 'middle')))
    P.append(badge(430, 290, 1))
    P.append(badge(652, 200, 2))
    P.append(badge(540, 330, 3))
    P.append(badge(262, 212, 4))
    P.append(part('rtr-away', lines(360, 400, ['1 Beam reach away from them for a few', 'boat lengths; one crew points all the time'], 'dg-label small', 'start') + '\n' + lead(420, 388, 430, 302)))
    P.append(part('rtr-tack', lines(672, 150, ['2 Tack; let the jib', 'flap, or roll it away'], 'dg-label small', 'start')))
    P.append(part('rtr-downwind', lines(600, 330, ['3 Bear away to get', 'downwind of them'], 'dg-label small', 'start')))
    P.append(part('rtr-close-reach', lines(30, 150, ['4 Come up onto a close reach towards', 'them; ease the sheets to slow down, and', 'stop with them on the leeward side'], 'dg-label small', 'start') + '\n' + lead(160, 196, 256, 208)))
    P.append(muted(450, 452, 'head to wind below them, the boat stalls and drifts back: bear away, sail off and try again'))
    return '\n'.join(P)
