# Knot drawings for sections/10-manoeuvres.html: a rope drawn from a spline, with its crossings found
# automatically and the upper strand redrawn at each one, so over and under read clearly.
import math
from gen_hull_diagrams import part, label, lead, title, muted
from gen_engine_diagrams import lines

W_EDGE, W_ROPE = 15, 10.5          # stroke widths: dark edge, rope colour

def _spline(pts, n=14):
    """Catmull-Rom through pts, n samples per span; returns a list of (x, y)."""
    P = [pts[0]] + list(pts) + [pts[-1]]
    out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for k in range(n):
            t = k / n
            t2, t3 = t * t, t * t * t
            out.append(tuple(0.5 * (2 * p1[j] + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2
                                    + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3) for j in (0, 1)))
    out.append(tuple(pts[-1]))
    return out

def _cross(a, b, c, d):
    """intersection point of segments ab and cd, or None."""
    d1 = (b[0] - a[0], b[1] - a[1]); d2 = (d[0] - c[0], d[1] - c[1])
    den = d1[0] * d2[1] - d1[1] * d2[0]
    if abs(den) < 1e-9: return None
    t = ((c[0] - a[0]) * d2[1] - (c[1] - a[1]) * d2[0]) / den
    u = ((c[0] - a[0]) * d1[1] - (c[1] - a[1]) * d1[0]) / den
    return (t, u) if 0 <= t < 1 and 0 <= u < 1 else None

def crossings(S):
    """list of (i, j) sample indices, i < j, where the rope crosses itself, in order of i."""
    X = []
    for i in range(len(S) - 1):
        for j in range(i + 3, len(S) - 1):
            if _cross(S[i], S[i + 1], S[j], S[j + 1]): X.append((i, j))
    return X

def _d(S):
    return 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in S)

def _strand(S, end_from):
    """the rope drawn once: edge, then colour, with the working end (from sample end_from) in the end colour."""
    o = [f'<path class="dg-rope-edge" d="{_d(S)}" stroke-width="{W_EDGE}"/>',
         f'<path class="dg-rope" d="{_d(S[:end_from + 1])}" stroke-width="{W_ROPE}"/>',
         f'<path class="dg-rope-end" d="{_d(S[end_from:])}" stroke-width="{W_ROPE}"/>']
    return o

def rope(pts, overs, end_frac=0.25, n=14, reach=5, flags=None, obstacle='', debug=False):
    """draw a rope through pts.
    overs[k] is True if, at the k-th visible crossing (ordered along the rope by its first pass), the first pass
    is on top, False if the second pass is. The last end_frac of the rope is the working end, in its own colour.
    flags, one per point, for a rope round an object: 'o' on top of the object, 'u' under or behind it (hidden),
    'd' clear of it. The rope is drawn, then the obstacle over it, then the 'o' runs again on top."""
    S = _spline(pts, n)
    F = None
    if flags:
        assert len(flags) == len(pts)
        F = [flags[min(k // n, len(pts) - 1)] for k in range(len(S))]
    X = [(i, j) for i, j in crossings(S) if not F or (F[i] != 'u' and F[j] != 'u')]
    if debug: print('crossings', len(X), [(i, j, tuple(round(v) for v in S[i])) for i, j in X])
    assert len(X) == len(overs), (len(X), len(overs), [tuple(round(v) for v in S[i]) for i, j in X])
    end_from = int(len(S) * (1 - end_frac))
    def piece(a, b):
        seg = S[max(0, a): b + 1]
        if len(seg) < 2: return []
        colour_split = min(max(end_from - max(0, a), 0), len(seg) - 1)
        o = [f'<path class="dg-rope-edge" d="{_d(seg[1:-1] if len(seg) > 4 else seg)}" stroke-width="{W_EDGE}"/>']
        if colour_split > 0: o.append(f'<path class="dg-rope" d="{_d(seg[:colour_split + 1])}" stroke-width="{W_ROPE}"/>')
        if colour_split < len(seg) - 1: o.append(f'<path class="dg-rope-end" d="{_d(seg[colour_split:])}" stroke-width="{W_ROPE}"/>')
        return o
    o = [f'<path class="dg-rope-edge" d="{_d(S)}" stroke-width="{W_EDGE}"/>']
    o += piece(0, len(S) - 1)[1:]
    if obstacle:
        o.append(obstacle)
        k = 0
        while k < len(S):
            if F[k] == 'o':
                m = k
                while m < len(S) and F[m] == 'o': m += 1
                o += piece(k - 1, m)
                k = m
            else: k += 1
    for k, top in enumerate(overs):
        i, j = X[k]
        c = i if top else j
        o += piece(c - reach, c + reach + 1)
    ex, ey = S[-1]
    o.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="{W_EDGE/2:.1f}" fill="var(--dg-rope-edge)"/>')
    return '\n'.join('      ' + x for x in o), S

def at(S, frac):
    x, y = S[int((len(S) - 1) * frac)]
    return round(x), round(y)

def _g(dx, dy, body):
    return f'    <g transform="translate({dx},{dy})">\n{body}\n    </g>'

def mapper(c, to, k):
    """a function mapping drawing coordinates (centred on c) to panel coordinates (centred on to), scaled by k."""
    return lambda x, y: (round(to[0] + k * (x - c[0]), 1), round(to[1] + k * (y - c[1]), 1))

def _rail(M, x1, y1, x2, y2):
    (a, b), (c, d) = M(x1, y1), M(x2, y2)
    return f'<rect class="dg-hull-dark" x="{a}" y="{b}" width="{round(c - a, 1)}" height="{round(d - b, 1)}" rx="{round((d - b) / 2, 1)}"/>'

def _txt(x, y, texts, anchor='start'):
    return lines(round(x), round(y), texts, 'dg-label small', anchor)

# ---------------------------------------------------------------- the bowline (drawn about 225,185; panel 450 x 400)
def bowline(dx=0):
    M = mapper((225, 185), (225 + dx, 212), 1.14)
    pts = [(228, 52), (227, 110), (229, 158),                      # standing part, down to the crossing
           (212, 176), (192, 200), (196, 234), (230, 248), (264, 232), (272, 200), (258, 174), (236, 160),   # the small loop
           (212, 150), (186, 144), (160, 156), (146, 195), (145, 250), (168, 298), (225, 318), (275, 308),  # the big loop
           (298, 280), (296, 250), (276, 228), (256, 200), (248, 160), (252, 122), (248, 94),               # up through the small loop
           (228, 80), (206, 90), (200, 122), (206, 160), (214, 200), (216, 236), (214, 272)]                # behind, and back down
    r, S = rope([M(*p) for p in pts], [True, False, False, True, True, False, False], end_frac=0.3)
    P = [title(225 + dx, 28, 'Bowline: a loop that will not slip'), r]
    x, y = M(228, 60)
    P.append(part('kn-bw-standing', _txt(x + 14, y + 4, ['Standing part'])))
    x, y = M(190, 205)
    P.append(part('kn-bw-small-loop', _txt(40 + dx, y + 30, ['Small loop, the end', 'side on top']) + '\n' + lead(128 + dx, y + 26, x - 6, y + 4)))
    x, y = M(250, 86)
    P.append(part('kn-bw-collar', _txt(x + 22, y - 6, ['The end: up through', 'the small loop, round', 'behind the standing', 'part, back down', 'through the loop'])))
    x, y = M(214, 272)
    P.append(part('kn-bw-tail', _txt(x + 14, y + 6, ['End inside', 'the loop'])))
    x, y = M(300, 280)
    P.append(part('kn-bw-loop', _txt(x + 4, y + 22, ['The loop: its size', 'stays fixed', 'under load'])))
    return '\n'.join(P)

# ---------------------------------------------------------------- the clove hitch on a rail, a fender hanging from it
def clove_hitch(dx=450):
    M = mapper((205, 165), (215 + dx, 176), 1.85)
    P = [((196, 244), 'd'), ((195, 222), 'd'), ((195, 200), 'd'),
         ((196, 180), 'o'), ((197, 165), 'o'), ((198, 151), 'o'), ((196, 142), 'd'),          # up the front, over the top
         ((188, 152), 'u'), ((176, 165), 'u'), ((166, 178), 'u'), ((161, 188), 'd'),          # down behind, under
         ((170, 180), 'o'), ((201, 165), 'o'), ((233, 151), 'o'), ((242, 146), 'd'),          # the crossing turn
         ((238, 160), 'u'), ((224, 168), 'u'), ((215, 178), 'u'), ((211, 188), 'd'),          # down behind, under
         ((214, 180), 'o'), ((215, 165), 'o'), ((216, 151), 'o'), ((217, 133), 'd'), ((220, 116), 'd'), ((224, 102), 'd')]
    rail = _rail(M, 105, 152, 318, 178)
    r, S = rope([M(*p) for p, f in P], [False, True], end_frac=0.22, flags=[f for p, f in P], obstacle=rail)
    out = [title(225 + dx, 28, 'Clove hitch: quick, on a rail'), r]
    fx, fy = M(196, 244)
    out.append(f'      <rect class="dg-sail-2" x="{fx - 26}" y="{fy - 4}" width="52" height="60" rx="22"/>')
    out.append(muted(fx + 34, fy + 36, 'fender', 'start'))
    x, y = M(195, 222)
    out.append(part('kn-cl-standing', _txt(x - 40, y + 4, ['Standing part,', 'to the fender'], 'end')))
    x, y = M(240, 146)
    out.append(part('kn-cl-cross', _txt(x + 40, y - 50, ['The crossing turn', 'traps both parts', 'under it']) + '\n' + lead(x + 36, y - 46, x - 12, y + 10)))
    x, y = M(224, 102)
    out.append(part('kn-cl-end', _txt(x + 16, y + 6, ['End: add a half hitch', 'on a smooth rail'])))
    x, y = M(318, 178)
    out.append(muted(x - 4, y + 20, 'guardrail', 'end'))
    return '\n'.join(out)

# ---------------------------------------------------------------- a round turn and two half hitches on a rail
def round_turn(dx=0):
    M = mapper((210, 160), (190 + dx, 200), 1.45)
    P = [((168, 305), 'd'), ((182, 240), 'd'), ((195, 150), 'd'), ((200, 110), 'd'),
         ((202, 96), 'o'), ((204, 83), 'o'), ((206, 70), 'o'), ((207, 61), 'd'),              # first turn
         ((212, 72), 'u'), ((216, 84), 'u'), ((220, 96), 'u'), ((222, 105), 'd'),
         ((224, 96), 'o'), ((226, 83), 'o'), ((228, 70), 'o'), ((230, 61), 'd'),              # second turn
         ((235, 72), 'u'), ((239, 84), 'u'), ((243, 96), 'u'), ((248, 108), 'd'),
         ((240, 130), 'd'), ((222, 152), 'd'), ((198, 170), 'd'), ((174, 168), 'd'), ((168, 152), 'd'),   # first half hitch
         ((190, 144), 'd'), ((216, 140), 'd'), ((244, 146), 'd'), ((256, 168), 'd'),
         ((244, 192), 'd'), ((212, 212), 'd'), ((166, 214), 'd'), ((156, 198), 'd'),          # second half hitch
         ((184, 190), 'd'), ((214, 186), 'd'), ((250, 196), 'd'), ((260, 222), 'd'), ((256, 256), 'd'), ((250, 282), 'd')]
    rail = _rail(M, 128, 70, 296, 96)
    r, S = rope([M(*p) for p, f in P], [True, False, True, False, True, True], end_frac=0.2, flags=[f for p, f in P], obstacle=rail)
    out = [title(225 + dx, 28, 'Round turn and two half hitches'), r]
    x, y = M(242, 70)
    out.append(part('kn-rt-turn', _txt(x + 96, y + 4, ['Round turn: two', 'full turns take the', 'load, so you can', 'tie or untie it', 'under strain']) + '\n' + lead(x + 92, y + 10, x + 4, y + 30)))
    x, y = M(256, 170)
    out.append(part('kn-rt-hitches', _txt(x + 24, y + 4, ['Two half hitches', 'round the standing', 'part, both the', 'same way']) + '\n' + lead(x + 20, y, x + 4, y)))
    x, y = M(178, 260)
    out.append(part('kn-rt-standing', _txt(x - 20, y + 4, ['Standing part:', 'the load'], 'end')))
    x, y = M(128, 96)
    out.append(muted(x + 4, y + 18, 'rail or ring', 'start'))
    return '\n'.join(out)

# ---------------------------------------------------------------- a cleat hitch, seen from above
def _cleat(M):
    pts = [(130, 180), (130, 170), (150, 168), (190, 168), (196, 160), (254, 160), (260, 168), (300, 168), (320, 170), (320, 180),
           (320, 190), (300, 192), (260, 192), (254, 200), (196, 200), (190, 192), (150, 192), (130, 190)]
    q = [M(*p) for p in pts]
    f = lambda i: f'{q[i][0]},{q[i][1]}'
    d = (f'M{f(0)} C{f(1)} {f(2)} {f(3)} L{f(4)} L{f(5)} L{f(6)} C{f(7)} {f(8)} {f(9)} '
         f'C{f(10)} {f(11)} {f(12)} L{f(13)} L{f(14)} L{f(15)} C{f(16)} {f(17)} {f(0)} Z')
    return f'<path class="dg-hull-dark" d="{d}"/>'

OVERS_CLEAT = [False, False, True]
def cleat_hitch(dx=450):
    M = mapper((225, 185), (225 + dx, 212), 1.7)
    P = [((206, 290), 'd'), ((212, 250), 'd'), ((234, 216), 'd'), ((270, 210), 'd'), ((292, 204), 'd'),
         ((304, 194), 'u'), ((306, 180), 'u'), ((304, 166), 'u'), ((292, 150), 'd'),         # under the far horn
         ((250, 144), 'd'), ((200, 144), 'd'), ((160, 150), 'd'),
         ((146, 166), 'u'), ((144, 180), 'u'), ((146, 194), 'u'), ((158, 210), 'd'),         # under the near horn: a full turn
         ((190, 196), 'o'), ((225, 180), 'o'), ((260, 164), 'o'), ((272, 158), 'd'),         # first diagonal
         ((280, 170), 'u'), ((282, 180), 'u'), ((280, 190), 'u'), ((270, 203), 'd'),
         ((256, 194), 'o'), ((225, 180), 'o'), ((192, 166), 'o'), ((178, 157), 'd'),         # second diagonal
         ((170, 170), 'u'), ((168, 180), 'u'), ((170, 190), 'u'), ((178, 204), 'd'),         # the locking turn
         ((190, 184), 'o'), ((216, 172), 'o'), ((242, 161), 'o')]
    r, S = rope([M(*p) for p, f in P], OVERS_CLEAT, end_frac=0.13, flags=[f for p, f in P], obstacle=_cleat(M))
    out = [title(225 + dx, 28, 'Cleat hitch, seen from above'), r]
    x, y = M(208, 262)
    out.append(part('kn-ct-lead', _txt(x - 16, y + 4, ['Line from the boat:', 'lead it to the', 'far horn first'], 'end')))
    x, y = M(190, 144)
    out.append(part('kn-ct-turn', _txt(x - 20, y - 16, ['A full turn round the base'], 'middle')))
    x, y = M(262, 196)
    out.append(part('kn-ct-eights', _txt(x + 16, y + 52, ['Figures of eight', 'over the horns']) + '\n' + lead(x + 12, y + 46, x - 4, y + 4)))
    x, y = M(242, 161)
    out.append(part('kn-ct-lock', _txt(x + 46, y - 58, ['Locking turn: the', 'end under the last', 'cross, alongside it']) + '\n' + lead(x + 42, y - 50, x + 4, y - 4)))
    return '\n'.join(out)

# ---------------------------------------------------------------- the figures (viewBox 0 0 900 400 each)
def knots_loops():
    return '\n'.join(['      <line class="dg-thin" x1="450" y1="44" x2="450" y2="390" stroke-dasharray="3 5"/>', bowline(0), clove_hitch(450)])

def knots_hitches():
    return '\n'.join(['      <line class="dg-thin" x1="450" y1="44" x2="450" y2="390" stroke-dasharray="3 5"/>', round_turn(0), cleat_hitch(450)])
