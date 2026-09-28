# Diagram builders for sections/13-licences.html.
from gen_hull_diagrams import part, label, lead, title, muted, marker
from gen_engine_diagrams import badge, arrow, lines

def mlines(x, y, texts, anchor='middle', step=14):
    return '\n'.join(muted(x, y + i * step, t, anchor) for i, t in enumerate(texts))

def box(x, y, w, h, cls='dg-hull'):
    return f'<rect class="{cls} shape" x="{x}" y="{y}" width="{w}" height="{h}" rx="8"/>'

# ---------------------------------------------------------------- which rules apply (viewBox 0 0 900 360)
def which_rules():
    P = [marker('wr-arrow')]
    P.append(title(450, 24, 'Three sets of rules apply at once'))
    P.append(muted(450, 42, 'a skipper needs to satisfy all three; where they overlap, the strictest wins'))
    cols = [
        ('lc-flag', 150, 'The boat’s flag', ['The country the boat is', 'registered in sets rules', 'for the boat and, often,', 'for its skipper:'], ['registration papers', 'radio licence and MMSI', 'skipper’s licence, if required', 'safety equipment']),
        ('lc-coastal', 450, 'The waters you are in', ['The country whose waters', 'you are in adds its own', 'rules for every boat,', 'whatever its flag:'], ['collision rules and speed limits', 'anchoring and nature reserves', 'fees, taxes and permits', 'entry and customs formalities', 'holding-tank rules']),
        ('lc-charter', 750, 'The charter company', ['On a chartered boat, the', 'company and its insurer', 'set the bar, often higher', 'than the law:'], ['a recognised licence, often the ICC', 'a radio certificate', 'a crew member with experience', 'a deposit and a check-out']),
    ]
    for key, cx, head, intro, items in cols:
        body = '        ' + box(cx - 140, 64, 280, 236) + '\n' + label(cx, 90, head, 'dg-title', 'middle') + '\n' + mlines(cx, 114, intro) + '\n'
        body += '\n'.join(label(cx - 122, 190 + i * 22, '• ' + t, 'dg-label small', 'start') for i, t in enumerate(items))
        P.append(part(key, body))
    return '\n'.join(P)

# ---------------------------------------------------------------- the RYA sail cruising scheme (viewBox 0 0 900 400)
def ladder():
    P = [marker('ld-arrow')]
    P.append(title(450, 24, 'The RYA sail cruising ladder, and where the ICC fits'))
    P.append(muted(450, 42, 'practical courses on the left, the matching shore-based (theory) courses on the right'))
    steps = [
        ('lc-competent-crew', 'Competent Crew', 'useful and safe on board'),
        ('lc-day-skipper', 'Day Skipper', 'skipper by day in familiar waters'),
        ('lc-coastal-skipper', 'Coastal Skipper', 'longer passages, some at night'),
        ('lc-ym-coastal', 'Yachtmaster Coastal', 'an exam, not a course'),
        ('lc-ym-offshore', 'Yachtmaster Offshore', 'an exam; professional, if endorsed'),
    ]
    theory = [None, 'Day Skipper theory', 'Coastal Skipper / Yachtmaster theory', None, None]
    for i, (key, name, note) in enumerate(steps):
        y = 330 - i * 62
        x = 120 + i * 60
        P.append(part(key, '        ' + box(x, y - 28, 250, 48) + '\n' + label(x + 16, y - 1, name, 'dg-label', 'start') + '\n' + muted(x + 16, y + 13, note, 'start')))
        if i < len(steps) - 1:
            P.append(f'      <path class="dg-lead" d="M{x+125},{y-26} L{x+160},{y-44}" marker-end="url(#ld-arrow)"/>')
        if theory[i]:
            P.append(part(key + '-theory', '        ' + box(x + 290, y - 22, 250, 36, 'dg-hull').replace('/>', ' stroke-dasharray="5 4"/>') + '\n' + label(x + 306, y + 1, theory[i], 'dg-label small', 'start')))
            P.append(f'      <line class="dg-thin" x1="{x+250}" y1="{y-4}" x2="{x+290}" y2="{y-4}" stroke-dasharray="3 4"/>')
    # ICC branch
    P.append(part('lc-icc', '        ' + box(470, 300, 270, 66, 'dg-hull-dark') + '\n' + label(486, 322, 'ICC', 'dg-title', 'start') + '\n' + mlines(486, 340, ['issued on Day Skipper practical', 'or on a separate assessment'], 'start')))
    P.append('      <path class="dg-lead" d="M400,286 C420,310 440,326 466,330" marker-end="url(#ld-arrow)" stroke-dasharray="5 4"/>')
    P.append(part('lc-support', lines(40, 72, ['Alongside: VHF Short Range Certificate,', 'First Aid, Sea Survival, Diesel Engine, Radar'], 'dg-label small', 'start')))
    return '\n'.join(P)
