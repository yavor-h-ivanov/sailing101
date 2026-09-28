# Diagram builders for sections/14-buying.html. Bow to the RIGHT in side views.
from gen_hull_diagrams import part, label, lead, title, muted, bow, marker
from gen_engine_diagrams import badge, arrow, lines

def mlines(x, y, texts, anchor='middle', step=14):
    return '\n'.join(muted(x, y + i * step, t, anchor) for i, t in enumerate(texts))

# ---------------------------------------------------------------- where to look on a viewing (viewBox 0 0 900 470)
def inspection():
    P = []
    P.append(title(450, 24, 'Where to look when viewing a used yacht'))
    P.append(muted(450, 42, 'a side view, bow to the right; follow the numbers'))
    P.append('      <rect class="dg-water" x="0" y="330" width="900" height="112"/>')
    P.append('      <path class="dg-hull" d="M90,292 L820,292 C810,322 790,344 760,356 L190,364 C140,360 100,334 90,292 Z"/>')
    P.append('      <line class="dg-waterline" x1="0" y1="330" x2="900" y2="330"/>')
    P.append('      <path class="dg-hull" d="M300,292 L300,272 L600,272 L630,292 Z"/>')
    P.append('      <path class="dg-hull-dark" d="M440,360 L462,432 L528,432 L536,358 Z"/>')
    P.append('      <path class="dg-hull-dark" d="M170,360 L164,420 L190,420 L200,362 Z"/>')
    P.append('      <rect class="dg-hull-dark" x="470" y="80" width="8" height="192"/>')
    P.append('      <line class="dg-line" x1="474" y1="80" x2="812" y2="292"/><line class="dg-line" x1="474" y1="80" x2="110" y2="292"/><line class="dg-line" x1="474" y1="80" x2="488" y2="292" stroke-width="1.5"/><rect class="dg-hull-dark" x="316" y="260" width="160" height="5" rx="2"/>')
    P.append('      <path class="dg-sail" d="M478,90 L478,262 L316,262 Z" opacity=".6"/>')
    pts = [
        ('by-hull', 330, 346, 'Hull below the waterline: blisters, repairs'),
        ('by-keel', 530, 372, 'Keel joint and bolts: the “smile”, rust'),
        ('by-rudder', 180, 392, 'Rudder: play in the bearings, weeping'),
        ('by-gland', 250, 352, 'Stern gland or saildrive seal'),
        ('by-seacocks', 410, 356, 'Seacocks and hoses: turn them, check clips'),
        ('by-chainplates', 500, 298, 'Chainplates: leaks and rust at the deck'),
        ('by-deck', 760, 284, 'Deck: soft spots, crazing, leaks'),
        ('by-mast-step', 474, 262, 'Mast step and the post under it'),
        ('by-rigging', 700, 222, 'Standing rigging: age, cracked swages'),
        ('by-sails', 420, 214, 'Sails: sun damage, stitching'),
        ('by-engine', 360, 310, 'Engine: start it from cold'),
        ('by-below', 560, 312, 'Below: stains, wiring, batteries, gas'),
    ]
    for n, (key, x, y, txt) in enumerate(pts, 1):
        body = badge(x, y, n) + f'<title>{n} {txt}</title>'
        P.append(part(key, f'        <circle class="shape-fill" cx="{x}" cy="{y}" r="14"/>\n' + body))
    P.append(bow(890, 318))
    return '\n'.join(P)

# ---------------------------------------------------------------- replacement cycles (viewBox 0 0 900 430)
def cycles():
    P = []
    P.append(title(450, 24, 'How often things wear out: rules of thumb'))
    P.append(muted(450, 42, 'years between replacements on a boat used every season; ranges, not promises'))
    x0, x1 = 300, 860
    yrs = 25
    sx = (x1 - x0) / yrs
    rows = [
        ('cy-service', 'Engine service, impeller', 1, 1),
        ('cy-antifouling', 'Antifouling, anodes', 1, 2),
        ('cy-safety', 'Liferaft service', 1, 3),
        ('cy-batteries', 'Batteries (lead-acid)', 3, 6),
        ('cy-gas-hose', 'Gas hose (by its date)', 5, 5),
        ('cy-seacocks-brass', 'Brass seacocks', 5, 10),
        ('cy-running', 'Running rigging (ropes)', 5, 10),
        ('cy-saildrive', 'Saildrive diaphragm', 7, 7),
        ('cy-hoses', 'Hoses below the waterline', 8, 15),
        ('cy-sails', 'Sails', 8, 15),
        ('cy-electronics', 'Electronics', 8, 15),
        ('cy-standing', 'Standing rigging (wire)', 10, 15),
        ('cy-cushions', 'Cushions and upholstery', 10, 20),
        ('cy-seacocks-bronze', 'Bronze or DZR seacocks', 15, 25),
        ('cy-engine', 'Engine rebuild or replacement', 20, 30),
    ]
    ax = 74 + len(rows) * 32 + 6
    P.append(f'      <line class="dg-line" x1="{x0}" y1="{ax}" x2="{x1}" y2="{ax}"/>')
    for yv in range(0, yrs + 1, 5):
        x = x0 + yv * sx
        P.append(f'      <line class="dg-thin" x1="{x:.0f}" y1="60" x2="{x:.0f}" y2="{ax}" stroke-dasharray="2 4"/>')
        P.append(label(round(x), ax + 18, f'{yv}', 'dg-muted', 'middle'))
    P.append(muted(x0 - 12, ax + 18, 'years:', 'end'))
    for i, (key, name, lo, hi) in enumerate(rows):
        y = 74 + i * 32
        hi_ = min(hi, yrs)
        w = max((hi_ - lo) * sx, 8)
        body = f'        <rect class="dg-accent-fill shape" x="{x0 + lo*sx - (4 if lo == hi else 0):.0f}" y="{y}" width="{w:.0f}" height="18" rx="4"/>'
        if hi > yrs:
            body += f'<path class="dg-accent-fill" d="M{x1},{y} l10,9 l-10,9 Z"/>'
        rng = ('every year' if lo == 1 else f'every {lo} years') if lo == hi else f'{lo} to {hi} years'
        body += '\n' + label(x0 - 12, y + 13, name, 'dg-label small', 'end')
        if hi >= yrs:
            body += '\n' + label(x0 + lo * sx - 8, y + 13, rng + (' or more' if hi > yrs else ''), 'dg-muted halo-wide', 'end')
        else:
            body += '\n' + label(x0 + hi_ * sx + 16 if lo != hi else x0 + lo * sx + 12, y + 13, rng, 'dg-muted halo-wide', 'start')
        P.append(part(key, body))
    return '\n'.join(P)
