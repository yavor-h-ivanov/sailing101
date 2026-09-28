# Diagram builders for sections/12-seas.html.
import math
from gen_hull_diagrams import part, label, lead, title, muted, marker
from gen_engine_diagrams import badge, arrow, lines

def mlines(x, y, texts, anchor='middle', step=14):
    return '\n'.join(muted(x, y + i * step, t, anchor) for i, t in enumerate(texts))

def hull(x, y, heading, L=150, B=48, cls='dg-hull'):
    h = L / 2
    d = (f'M0,{-h} C{B*0.45},{-h*0.72} {B*0.52},{-h*0.1} {B*0.5},{h*0.35} L{B*0.42},{h} L{-B*0.42},{h} L{-B*0.5},{h*0.35} '
         f'C{-B*0.52},{-h*0.1} {-B*0.45},{-h*0.72} 0,{-h} Z')
    return f'<g transform="translate({x},{y}) rotate({heading})"><path class="{cls}" d="{d}"/></g>'

def wave(x0, x1, y, amp, wl, sharp=False):
    """a wave profile from x0 to x1 around height y; sharp=True gives short peaked crests."""
    pts = []
    n = int((x1 - x0) / 2)
    for i in range(n + 1):
        x = x0 + i * 2
        ph = (x - x0) / wl * 2 * math.pi
        if sharp:
            v = -(math.cos(ph) + 0.25 * math.cos(2 * ph)) / 1.1
        else:
            v = -math.cos(ph)
        pts.append(f'{x:.0f},{y + amp * v:.1f}')
    return ' '.join(pts)

# ---------------------------------------------------------------- wind against tide (viewBox 0 0 900 320)
def wind_tide():
    P = [marker('wt-arrow')]
    for ox, ttl in ((225, 'Wind with the tide'), (675, 'Wind against the tide')):
        P.append(title(ox, 26, ttl))
    P.append(muted(450, 44, 'side views; the same wind, force 5, in both'))
    P.append('      <line class="dg-thin" x1="450" y1="56" x2="450" y2="310" stroke-dasharray="3 5"/>')
    # left: long low waves
    P.append(f'      <polygon class="dg-water" points="20,300 {wave(20, 430, 190, 10, 140)} 430,300"/>')
    P.append(f'      <polyline class="dg-line" stroke="var(--dg-water-line)" stroke-width="2" points="{wave(20, 430, 190, 10, 140)}" fill="none"/>')
    P.append(part('wt-wind', '        <line class="dg-accent shape" x1="60" y1="96" x2="220" y2="96" stroke-width="3" marker-end="url(#wt-arrow)"/><line class="dg-accent" x1="560" y1="96" x2="720" y2="96" stroke-width="3" marker-end="url(#wt-arrow)"/>\n' + lines(60, 84, ['Wind'], 'dg-label small', 'start') + '\n' + lines(560, 84, ['Wind'], 'dg-label small', 'start')))
    P.append(part('wt-tide-with', '        <line class="dg-line shape" x1="80" y1="262" x2="240" y2="262" stroke-width="3" marker-end="url(#wt-arrow)"/>\n' + lines(250, 266, ['Tidal stream the same way'], 'dg-label small', 'start')))
    P.append(part('wt-long', lines(225, 140, ['Long, low waves: a lively', 'but comfortable sail'], 'dg-label small', 'middle')))
    # right: short steep breaking waves
    P.append(f'      <polygon class="dg-water" points="470,300 {wave(470, 880, 190, 22, 62, True)} 880,300"/>')
    P.append(f'      <polyline class="dg-line" stroke="var(--dg-water-line)" stroke-width="2" points="{wave(470, 880, 190, 22, 62, True)}" fill="none"/>')
    for i in range(6):
        cx = 470 + 62 * i + 62
        if cx < 870:
            P.append(f'      <path class="dg-thin" d="M{cx-6},{168} q8,-8 14,2" stroke-width="2"/>')
    P.append(part('wt-tide-against', '        <line class="dg-line shape" x1="800" y1="262" x2="640" y2="262" stroke-width="3" marker-end="url(#wt-arrow)"/>\n' + lines(630, 266, ['Tidal stream against the wind'], 'dg-label small', 'end')))
    P.append(part('wt-steep', lines(675, 140, ['Short, steep, breaking waves:', 'slamming, spray, and hard work'], 'dg-label small', 'middle')))
    return '\n'.join(P)

# ---------------------------------------------------------------- the bora (viewBox 0 0 900 380)
def bora():
    P = [marker('bo-arrow')]
    P.append(title(450, 24, 'The bora: cold air falling off the mountains onto the sea'))
    P.append(muted(450, 42, 'a cross-section, north-east (inland) on the right; heights exaggerated'))
    P.append('      <rect class="dg-water" x="20" y="300" width="470" height="60"/>')
    P.append('      <path class="dg-land" d="M470,300 C520,290 560,240 600,190 C630,150 650,120 670,112 C700,118 730,150 780,166 C820,176 860,178 880,180 L880,360 L470,360 Z"/>')
    P.append(muted(780, 250, 'inland plateau', 'middle'))
    P.append(muted(640, 270, 'coastal mountains', 'middle'))
    P.append(part('bo-cold-air', '        <path class="dg-accent shape" d="M870,140 C820,132 760,116 700,100" stroke-width="3" marker-end="url(#bo-arrow)"/><path class="dg-accent" d="M870,164 C830,158 790,146 740,128" stroke-width="2" marker-end="url(#bo-arrow)"/>\n' + lines(876, 82, ['Cold, dense air', 'piles up inland'], 'dg-label small', 'end')))
    P.append(part('bo-cap-cloud', '        <path class="dg-sail shape" d="M600,100 C610,78 640,70 660,80 C676,66 708,70 716,90 C734,92 736,110 716,112 L604,112 C590,112 588,102 600,100 Z" stroke="var(--dg-line)" stroke-width="1.2"/>\n' + lines(500, 62, ['A cap of cloud on the crest,', 'often with a clear sky: a warning'], 'dg-label small', 'end') + '\n' + lead(502, 66, 604, 92)))
    P.append(part('bo-fall', '        <path class="dg-accent shape" d="M660,118 C620,160 580,230 510,286" stroke-width="4" marker-end="url(#bo-arrow)"/><path class="dg-accent" d="M640,122 C600,170 560,236 480,282" stroke-width="3" marker-end="url(#bo-arrow)"/>\n' + lines(560, 186, ['It falls down', 'the slope and', 'accelerates'], 'dg-label small', 'end')))
    P.append(part('bo-gusts', '        ' + ''.join(f'<path class="dg-accent" d="M{x},{296} l-40,-2" stroke-width="2.5" marker-end="url(#bo-arrow)"/>' for x in (460, 380, 300)) + '<path class="dg-thin" d="M300,292 q10,-10 22,-4 M360,292 q10,-10 22,-4 M420,292 q10,-10 22,-4" stroke-width="2"/>\n' + lines(40, 236, ['Violent gusts close under the mountains,', 'strongest below gaps and passes; spray', 'torn off the sea in white streaks'], 'dg-label small', 'start')))
    P.append(part('bo-sea', lines(40, 336, ['Further out the gusts ease, but a strong', 'bora can still reach far across the sea'], 'dg-label small', 'start')))
    return '\n'.join(P)

# ---------------------------------------------------------------- sea breeze and land breeze (viewBox 0 0 900 330)
def sea_breeze():
    P = [marker('sb-arrow')]
    P.append(title(225, 26, 'Day: the sea breeze'))
    P.append(title(675, 26, 'Night: the land breeze'))
    P.append('      <line class="dg-thin" x1="450" y1="40" x2="450" y2="320" stroke-dasharray="3 5"/>')
    for ox in (0, 450):
        P.append(f'      <rect class="dg-water" x="{ox+20}" y="240" width="220" height="70"/>')
        P.append(f'      <path class="dg-land" d="M{ox+240},240 L{ox+430},230 L{ox+430},310 L{ox+240},310 Z"/>')
        P.append(muted(ox + 130, 290, 'sea', 'middle'))
        P.append(muted(ox + 335, 290, 'land', 'middle'))
    # day: sun, rising air over land, onshore surface wind, return aloft
    P.append('      <circle class="dg-warn-fill" cx="380" cy="70" r="16"/>')
    P.append(part('sb-rising', '        <path class="dg-accent shape" d="M350,200 C350,170 350,150 350,120" stroke-width="3" marker-end="url(#sb-arrow)"/>\n' + lines(362, 160, ['Land heats;', 'warm air', 'rises'], 'dg-label small', 'start')))
    P.append('      <path class="dg-accent" d="M310,110 C240,100 150,100 90,110" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#sb-arrow)"/>')
    P.append('      <path class="dg-accent" d="M80,130 C70,170 70,200 80,220" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#sb-arrow)"/>')
    P.append(part('sb-sea-breeze', '        <path class="dg-accent shape" d="M90,226 C160,226 240,226 310,222" stroke-width="4" marker-end="url(#sb-arrow)"/>\n' + lines(110, 206, ['Sea breeze onshore, from late morning'], 'dg-label small', 'start')))
    P.append(mlines(200, 84, ['return flow aloft'], 'middle'))
    # night: land cools, offshore land breeze
    P.append('      <path class="dg-hull-dark" d="M830,60 a16,16 0 1,0 12,26 a12,12 0 1,1 -12,-26 Z"/>')
    P.append(part('sb-land-breeze', '        <path class="dg-accent shape" d="M760,226 C690,226 610,226 540,222" stroke-width="3" marker-end="url(#sb-arrow)"/>\n' + lines(560, 206, ['A lighter land breeze offshore'], 'dg-label small', 'start')))
    P.append(mlines(675, 110, ['the land cools faster than', 'the sea; the flow reverses'], 'middle'))
    return '\n'.join(P)

# ---------------------------------------------------------------- mooring to a skerry (viewBox 0 0 900 400)
def skerry():
    P = [marker('sk-arrow')]
    P.append(title(450, 24, 'Mooring bow-to a rock, Scandinavian style'))
    P.append(muted(450, 42, 'seen from above; the rock shore at the top'))
    P.append('      <rect class="dg-water" x="20" y="56" width="860" height="330"/>')
    P.append('      <path class="dg-land" d="M20,56 L880,56 L880,96 C800,110 760,96 700,120 C640,142 560,126 500,112 C450,104 400,118 350,110 C300,102 240,130 180,118 C120,108 60,120 20,112 Z"/>')
    P.append('      <path class="dg-ok-fill" d="M300,76 a12,12 0 1,0 0.1,0 Z M620,78 a12,12 0 1,0 0.1,0 Z" opacity=".6"/>')
    P.append(muted(820, 82, 'rock, trees', 'middle'))
    x, y = 450, 200
    P.append('      ' + hull(x, y, 0))
    bowp = (x, y - 70)
    P.append(part('sk-bow-lines', f'        <line class="dg-line shape" x1="{bowp[0]-4}" y1="{bowp[1]}" x2="360" y2="112" stroke-width="3"/><line class="dg-line shape" x1="{bowp[0]+4}" y1="{bowp[1]}" x2="560" y2="118" stroke-width="3"/><circle class="dg-hull-dark" cx="360" cy="112" r="5"/><circle class="dg-hull-dark" cx="560" cy="118" r="5"/>\n' + lines(600, 150, ['Two bow lines ashore, spread wide:', 'to rock pins hammered into cracks,', 'rings, or trees'], 'dg-label small', 'start') + '\n' + lead(598, 148, 540, 124)))
    P.append(part('sk-step', lines(300, 170, ['Crew step ashore', 'from the bow, often', 'with a bow ladder'], 'dg-label small', 'end') + '\n' + lead(302, 166, 440, 138)))
    P.append(part('sk-stern-anchor', f'        <line class="dg-line shape" x1="{x}" y1="{y+75}" x2="{x}" y2="343" stroke-width="2.5" stroke-dasharray="7 4"/><g class="dg-line" fill="none" stroke-width="2.5" stroke-linecap="round"><circle cx="{x}" cy="347" r="4"/><path d="M{x},351 L{x},374 M{x-8},357 L{x+8},357 M{x-14},366 Q{x-10},378 {x},376 Q{x+10},378 {x+14},366"/></g>\n' + lines(470, 320, ['Stern anchor, dropped well out on the way in, often on a', 'reel of webbing tape at the pushpit; it holds the boat off the rock'], 'dg-label small', 'start')))
    P.append(part('sk-depth', lines(40, 290, ['Check the depth all the way in:', 'many skerry shores drop steeply,', 'but not all, and rocks lie close in'], 'dg-label small', 'start')))
    return '\n'.join(P)
