# Diagram builders for sections/04-rig.html. Bow to the RIGHT in every profile view.
from gen_hull_diagrams import part, label, lead, title, muted, bow, marker

def dim(x1, y1, x2, y2, mid, text, cls='dg-accent', dx=0, dy=0):
    """double-headed dimension arrow with a label at its middle (offset by dx, dy)"""
    return (f'        <path class="{cls}" d="M{x1},{y1} L{x2},{y2}" stroke-width="1.5" marker-start="url(#{mid})" marker-end="url(#{mid})"/>\n'
            + label((x1+x2)/2+dx, (y1+y2)/2+dy, text, 'dg-label', 'middle'))
def marker2(mid):
    return (f'      <defs><marker id="{mid}" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 Z" class="dg-arrow"/></marker></defs>')

# ---------------------------------------------------------------- rig types (viewBox 0 0 900 420)
def rig_types():
    P = [marker2('rt-arrow')]
    def boat(ox, masthead=True, tag=''):
        tag = ''
        t = []
        hull = f'<path class="dg-hull" d="M{ox+20},340 L{ox+272},340 C{ox+268},356 {ox+260},370 {ox+246},376 L{ox+40},376 C{ox+26},372 {ox+20},356 {ox+20},340 Z"/>'
        t.append('        ' + hull)
        t.append(f'        <line class="dg-waterline" x1="{ox+6}" y1="352" x2="{ox+290}" y2="352"/>')
        mx = ox + 150
        top = 46 if masthead else 40
        fs_y = top if masthead else top + 40
        t.append(part(f'rig-mast{tag}', f'        <rect class="dg-hull-dark shape" x="{mx-4}" y="{top}" width="8" height="{340-top}"/>\n' + label(mx, 40, 'Mast', 'dg-label small', 'middle')))
        t.append(part(f'rig-boom{tag}', f'        <rect class="dg-hull-dark shape" x="{ox+52}" y="286" width="{mx-ox-52}" height="6"/>\n' + label(ox+58, 280, 'Boom', 'dg-label small')))
        t.append(part(f'rig-forestay{tag}', f'        <line class="dg-line shape" x1="{mx}" y1="{fs_y}" x2="{ox+268}" y2="338"/>\n        <line class="hit" x1="{mx}" y1="{fs_y}" x2="{ox+268}" y2="338" stroke="transparent" stroke-width="14"/>\n' + label(ox+240, 150, 'Forestay', 'dg-label small')))
        t.append(part(f'rig-backstay{tag}', f'        <line class="dg-line shape" x1="{mx}" y1="{top}" x2="{ox+24}" y2="338"/>\n        <line class="hit" x1="{mx}" y1="{top}" x2="{ox+24}" y2="338" stroke="transparent" stroke-width="14"/>\n' + label(ox+34, 190, 'Backstay', 'dg-label small')))
        sp_y = 190
        t.append(part(f'rig-spreaders{tag}', f'        <rect class="dg-hull-dark shape" x="{mx-30}" y="{sp_y-2}" width="60" height="4"/>\n' + label(mx+36, sp_y-8, 'Spreader', 'dg-label small')))
        t.append(part(f'rig-cap-shroud{tag}', f'        <path class="dg-line shape" d="M{mx},{top+6} L{mx+30},{sp_y} L{mx+14},338 M{mx},{top+6} L{mx-30},{sp_y} L{mx-14},338"/>\n        <path class="hit" d="M{mx},{top+6} L{mx+30},{sp_y} L{mx+14},338" stroke="transparent" stroke-width="12" fill="none"/>\n' + label(mx+42, 262, 'Cap shroud', 'dg-label small')))
        t.append(part(f'rig-lower-shroud{tag}', f'        <path class="dg-line shape" d="M{mx},{sp_y+2} L{mx+22},338 M{mx},{sp_y+2} L{mx-22},338"/>\n        <path class="hit" d="M{mx},{sp_y+2} L{mx+22},338" stroke="transparent" stroke-width="12" fill="none"/>\n' + label(mx+30, 300, 'Lower shroud', 'dg-label small')))
        return t, mx, top, fs_y
    # panel 1 masthead
    t, mx, top, fs_y = boat(0, True, '')
    t.insert(0, title(150, 24, 'Masthead sloop'))
    t.append(part('dim-i', dim(mx-130, top, mx-130, 340, 'rt-arrow', 'I', dx=-12) + '\n' + lead(mx-130, top, mx-4, top, 'dg-thin')))
    t.append(part('dim-j', dim(mx+4, 330, 268, 330, 'rt-arrow', 'J', dy=-6) + '\n' + lead(mx+4, 324, mx+4, 340, 'dg-thin')))
    t.append(part('dim-p', dim(mx-14, 60, mx-14, 284, 'rt-arrow', 'P', dx=-14)))
    t.append(part('dim-e', dim(52, 322, mx-4, 322, 'rt-arrow', 'E', dy=-8)))
    t.append(muted(150, 400, 'Moody 33, Sadler 32, Bavaria 1060,'))
    t.append(muted(150, 414, 'Finnsailer 35'))
    P.append('      <g>\n' + '\n'.join(t) + '\n      </g>')
    # panel 2 fractional
    t, mx, top, fs_y = boat(300, False, '-f')
    t.insert(0, title(450, 24, 'Fractional sloop'))
    t.append(part('fractional-hounds', f'        <circle class="dg-accent-fill shape" cx="{mx}" cy="{fs_y}" r="6"/>\n' + label(mx+12, fs_y-8, 'Forestay meets the mast', 'dg-label small') + '\n' + label(mx+12, fs_y+6, 'below the top (7/8 here)', 'dg-label small')))
    t.append(muted(450, 400, 'most boats designed since the 1990s;'))
    t.append(muted(450, 414, 'Gib’Sea 33 (2002) ¹'))
    P.append('      <g>\n' + '\n'.join(t) + '\n      </g>')
    # panel 3 tuning words
    t = [title(750, 24, 'Three tuning words')]
    ox = 600
    t.append('        ' + f'<path class="dg-hull" d="M{ox+20},340 L{ox+272},340 C{ox+268},356 {ox+260},370 {ox+246},376 L{ox+40},376 C{ox+26},372 {ox+20},356 {ox+20},340 Z"/>')
    mx = ox + 150
    t.append(f'        <line class="dg-waterline" x1="{ox+6}" y1="352" x2="{ox+290}" y2="352"/>')
    t.append(f'        <line class="dg-thin" x1="{mx}" y1="46" x2="{mx}" y2="340" stroke-dasharray="4 3"/>')
    t.append(part('rake', f'        <path class="dg-hull-dark shape" d="M{mx-4},340 L{mx+2},340 L{mx-12},46 L{mx-20},46 Z"/>\n' + label(mx-30, 110, 'Rake: the whole', 'dg-label small', 'end') + '\n' + label(mx-30, 124, 'mast leans aft a little', 'dg-label small', 'end') + '\n' + lead(mx-28, 118, mx-14, 118)))
    t.append(part('pre-bend', f'        <path class="dg-accent shape" d="M{mx+40},340 Q{mx+66},190 {mx+40},46 M{mx+48},340 Q{mx+74},190 {mx+48},46" fill="none" stroke-width="2" stroke-dasharray="6 3"/>\n' + label(mx-30, 200, 'Pre-bend: the middle', 'dg-label small', 'end') + '\n' + label(mx-30, 214, 'bows forward slightly', 'dg-label small', 'end') + '\n' + lead(mx-28, 208, mx+52, 194)))
    t.append(part('forestay-sag', f'        <path class="dg-line shape" d="M{mx-12},46 Q{mx+40},200 {ox+268},338" fill="none" stroke-dasharray="5 3"/>\n        <path class="hit" d="M{mx-12},46 Q{mx+40},200 {ox+268},338" stroke="transparent" stroke-width="12" fill="none"/>\n' + label(ox+36, 300, 'Forestay sag: the wire bows', 'dg-label small') + '\n' + label(ox+36, 314, 'under load (seen from the side)', 'dg-label small') + '\n' + lead(ox+186, 296, ox+212, 250)))
    t.append(muted(750, 400, 'dashed: the mast with pre-bend; all exaggerated'))
    P.append('      <g>\n' + '\n'.join(t) + '\n      </g>')
    P.append(bow(895, 414))
    return '\n'.join(P)

# ---------------------------------------------------------------- sail parts (viewBox 0 0 940 540)
def sail_parts():
    P = [marker('sp-arrow'), marker2('sp-arrow2')]
    P.append(title(470, 24, 'Mainsail and genoa of a masthead sloop, seen from the port side'))
    # deck line, mast, boom, forestay
    P.append('      <path class="dg-hull" d="M60,452 L860,452 C856,470 846,486 830,492 L90,492 C74,486 62,470 60,452 Z"/>')
    P.append('      <line class="dg-waterline" x1="40" y1="484" x2="880" y2="484"/>')
    P.append(part('rig-mast', '        <rect class="dg-hull-dark shape" x="356" y="60" width="8" height="392"/>'))
    P.append(part('rig-boom', '        <rect class="dg-hull-dark shape" x="150" y="408" width="210" height="7"/>'))
    P.append(part('gooseneck-fitting gooseneck', '        <rect class="dg-accent-fill shape" x="350" y="404" width="16" height="16" rx="3"/>\n' + label(372, 434, 'Gooseneck', 'dg-label small')))
    # genoa
    P.append(part('rig-forestay forestay', '        <line class="dg-line shape" x1="364" y1="64" x2="846" y2="450"/>'))
    genoa = 'M368,76 L838,446 L286,418 C300,300 340,180 368,76 Z'
    P.append(part('rig-genoa genoa', f'        <path class="dg-sail-2 shape" d="{genoa}" opacity=".92"/>\n' + label(560, 246, 'Genoa: its clew reaches past the mast', 'dg-label small on-sail') + '\n' + label(560, 260, '(130% here; the part behind the mast is the overlap)', 'dg-label small on-sail')))
    P.append(part('uv-strip', '        <path class="dg-hull-dark shape" d="M838,446 L286,418 L292,410 L830,438 Z"/><path class="dg-hull-dark shape" d="M286,418 C300,300 340,180 368,76 L376,80 C348,184 308,300 294,416 Z"/>\n' + label(620, 446, 'UV strip along leech and foot', 'dg-label small') + '\n' + lead(618, 442, 580, 432)))
    P.append(part('sail-clew', '        <circle class="dg-accent-fill shape" cx="288" cy="418" r="6"/>\n' + label(268, 434, 'Clew', 'dg-label small', 'end')))
    P.append(part('sail-tack', '        <circle class="dg-accent-fill shape" cx="836" cy="446" r="6"/>\n' + label(826, 436, 'Tack', 'dg-label small', 'end')))
    P.append(part('sail-head', '        <circle class="dg-accent-fill shape" cx="370" cy="78" r="6"/>'))
    P.append(part('genoa-sheet sheet', '        <path class="dg-accent shape" d="M288,420 L232,448" stroke-width="2.5"/>\n' + label(400, 474, 'Genoa sheet, aft to a car on the track', 'dg-label small') + '\n' + lead(398, 470, 262, 438)))
    P.append(part('genoa-car genoa-track', '        <rect class="dg-hull-dark shape" x="200" y="446" width="70" height="5"/><rect class="dg-accent-fill shape" x="226" y="441" width="14" height="10"/>'))
    P.append(part('furler-drum furler', '        <rect class="dg-hull-dark shape" x="836" y="436" width="16" height="16" rx="3"/>\n' + label(760, 512, 'Furling drum at the bow', 'dg-label small')))
    P.append(part('luff-telltales', '        <path class="dg-bad shape" d="M540,218 l14,-6 M600,266 l14,-6" stroke-width="2"/>\n' + label(620, 200, 'Luff telltales, both sides of the genoa', 'dg-label small') + '\n' + lead(618, 204, 556, 214)))
    # mainsail
    main = 'M360,72 L360,404 L156,404 C230,330 300,200 360,72 Z'
    P.append(part('rig-mainsail mainsail', f'        <path class="dg-sail shape" d="{main}" opacity=".9"/>'))
    # battens
    P.append(part('sail-battens battens', '        <path class="dg-line shape" d="M303,180 L340,190 M270,260 L330,268 M232,330 L320,334 M196,388 L300,386" stroke-width="2.5"/>\n' + label(250, 214, 'Battens', 'dg-label small on-main')))
    P.append(part('roach-area roach', '        <path class="shape-fill" d="M156,404 C230,330 300,200 360,72 L156,404 Z"/>\n        <path class="dg-thin" d="M360,72 L156,404" stroke-dasharray="4 3"/>\n' + label(232, 300, 'Roach', 'dg-label small on-main') + '\n' + label(232, 314, '(beyond the dotted line)', 'dg-label small on-main', 'middle')))
    P.append(part('sail-head', '        <rect class="dg-hull-dark shape" x="350" y="64" width="22" height="14"/>\n' + label(384, 72, 'Head (with headboard)', 'dg-label small')))
    P.append(part('sail-tack', '        <circle class="dg-accent-fill shape" cx="362" cy="402" r="6"/>\n' + label(376, 398, 'Tack', 'dg-label small')))
    P.append(part('sail-clew', '        <circle class="dg-accent-fill shape" cx="158" cy="402" r="6"/>\n' + label(146, 404, 'Clew', 'dg-label small', 'end')))
    P.append(part('luff', '        <line class="shape" x1="360" y1="80" x2="360" y2="400" stroke="transparent" stroke-width="10"/>\n' + label(340, 250, 'Luff (front edge, on the mast)', 'dg-label small on-main', 'end')))
    P.append(part('leech', '        <path class="shape" d="M156,404 C230,330 300,200 360,72" fill="none" stroke="transparent" stroke-width="12"/>\n' + label(186, 160, 'Leech (back edge)', 'dg-label small')))
    P.append(part('foot', '        <line class="shape" x1="160" y1="405" x2="356" y2="405" stroke="transparent" stroke-width="10"/>\n' + label(280, 430, 'Foot (along the boom)', 'dg-label small', 'end')))
    # reefs
    reefs = ''
    for y, xl in ((350, 198), (300, 233)):
        reefs += f'<circle class="dg-accent-fill shape" cx="362" cy="{y}" r="4"/><circle class="dg-accent-fill shape" cx="{xl+8}" cy="{y}" r="4"/>'
        reefs += ''.join(f'<line class="dg-line" x1="{x}" y1="{y-6}" x2="{x}" y2="{y+6}"/>' for x in range(xl+30, 356, 22))
    P.append(part('reef-cringle', '        ' + reefs + '\n' + label(400, 330, 'Reef cringles (rings) at luff and leech,', 'dg-label small on-sail') + '\n' + label(400, 344, 'reef points between: two rows here', 'dg-label small on-sail') + '\n' + lead(398, 336, 368, 350)))
    P.append(part('leech-line', '        <path class="dg-accent shape" d="M170,395 C240,326 300,210 352,90" fill="none" stroke-dasharray="2 3" stroke-width="1.5"/>\n' + label(120, 120, 'Leech line: a thin cord', 'dg-label small') + '\n' + label(120, 134, 'in the leech to stop flutter', 'dg-label small') + '\n' + lead(274, 128, 300, 210)))
    P.append(part('sail-telltales telltales', '        <path class="dg-bad shape" d="M214,352 l-16,6 M258,290 l-16,6 M296,222 l-16,6" stroke-width="2"/>\n' + label(120, 372, 'Telltales on the leech', 'dg-label small') + '\n' + lead(200, 368, 212, 352)))
    # controls
    P.append(part('ctl-halyard halyard', '        <path class="dg-accent shape" d="M361,64 L361,40 Q361,32 353,32" fill="none" stroke-width="2"/>\n' + label(300, 46, 'Main halyard', 'dg-label small', 'end') + '\n' + lead(302, 42, 352, 34)))
    P.append(part('ctl-outhaul outhaul', '        <path class="dg-accent shape" d="M158,411 L120,411" stroke-width="2.5" marker-end="url(#sp-arrow)"/>\n' + label(60, 415, 'Outhaul', 'dg-label small')))
    P.append(part('ctl-kicker kicker', '        <path class="dg-hull-dark shape" d="M356,450 L270,418 L272,410 L358,442 Z"/>\n' + label(296, 474, 'Kicker (vang)', 'dg-label small')))
    P.append(part('ctl-mainsheet mainsheet', '        <path class="dg-accent shape" d="M170,415 L170,448" stroke-width="2.5"/>\n' + label(120, 448, 'Mainsheet', 'dg-label small', 'end')))
    P.append(part('ctl-traveller traveller', '        <rect class="dg-hull-dark shape" x="130" y="448" width="80" height="5"/>\n' + label(60, 470, 'Traveller', 'dg-label small')))
    P.append(part('ctl-cunningham cunningham', '        <circle class="dg-accent-fill shape" cx="366" cy="376" r="4"/>\n' + label(400, 372, 'Cunningham cringle', 'dg-label small on-sail') + '\n' + lead(398, 374, 372, 376)))
    P.append(part('ctl-topping-lift topping-lift', '        <path class="dg-thin shape" d="M362,66 L152,404" stroke-dasharray="3 3"/>\n' + label(190, 60, 'Topping lift', 'dg-label small') + '\n' + lead(258, 62, 298, 170)))
    P.append(part('overlap', '        <path class="dg-accent shape" d="M362,440 L292,440" stroke-width="1.5" marker-start="url(#sp-arrow2)" marker-end="url(#sp-arrow2)"/>\n' + label(326, 452, 'overlap', 'dg-label small', 'middle')))
    P.append(bow(895, 530))
    P.append(muted(470, 530, 'the boat is drawn without its deck gear; sails are set for sailing to windward'))
    return '\n'.join(P)

# ---------------------------------------------------------------- terminals (viewBox 0 0 900 380)
def terminals():
    P = []
    tiles = []
    # 1 swage
    t = [title(112, 24, 'Swaged terminal')]
    t.append(part('rig-wire', '        <path class="dg-hull-dark shape" d="M108,40 L116,40 L116,150 L108,150 Z"/><path class="dg-thin" d="M110,44 L114,148 M114,44 L110,148" opacity=".7"/>\n' + label(126, 90, '1×19 stainless', 'dg-label small') + '\n' + label(126, 104, 'wire', 'dg-label small')))
    t.append(part('swage', '        <path class="dg-hull shape" d="M104,150 L120,150 L124,240 L112,262 L100,240 Z"/><circle class="dg-hull-dark shape" cx="112" cy="250" r="7"/>\n' + label(130, 200, 'Sleeve pressed', 'dg-label small') + '\n' + label(130, 214, 'onto the wire', 'dg-label small')))
    t.append(part('swage-crack', '        <path class="dg-bad" d="M106,168 L110,182 L106,196" fill="none" stroke-width="2"/>\n        <path class="dg-bad" d="M112,136 L100,124 M112,140 L98,140" stroke-width="2"/>\n' + label(20, 300, 'Faults: hairline cracks', 'dg-label small') + '\n' + label(20, 314, 'down the sleeve; broken', 'dg-label small') + '\n' + label(20, 328, 'strands where the wire', 'dg-label small') + '\n' + label(20, 342, 'enters (“meat hooks”)', 'dg-label small') + '\n' + lead(80, 296, 104, 190)))
    tiles.append('\n'.join(t))
    # 2 mechanical
    t = [title(112, 24, 'Mechanical terminal')]
    t.append(part('rig-wire', '        <path class="dg-hull-dark shape" d="M108,40 L116,40 L116,130 L108,130 Z"/>'))
    t.append(part('mechanical-terminal', '        <rect class="dg-hull shape" x="94" y="130" width="36" height="30" rx="3"/><path class="dg-thin" d="M98,138 H126 M98,146 H126 M98,154 H126" opacity=".6"/>\n        <path class="dg-accent-fill shape" d="M104,166 L120,166 L116,190 L108,190 Z"/>\n        <rect class="dg-hull shape" x="92" y="196" width="40" height="46" rx="4"/><circle class="dg-hull-dark shape" cx="112" cy="254" r="7"/>\n' + label(140, 150, 'Socket', 'dg-label small') + '\n' + label(140, 182, 'Cone wedged in', 'dg-label small') + '\n' + label(140, 196, 'the wire strands', 'dg-label small') + '\n' + label(140, 218, 'Body (Sta-Lok,', 'dg-label small') + '\n' + label(140, 232, 'Norseman or', 'dg-label small') + '\n' + label(140, 246, 'Hi-Mod)', 'dg-label small')))
    t.append(muted(112, 296, 'shown taken apart; screws together'))
    t.append(muted(112, 310, 'with hand tools; can be opened'))
    t.append(muted(112, 324, 'and inspected'))
    tiles.append('\n'.join(t))
    # 3 rigging screw + toggle + chainplate
    t = [title(112, 24, 'Rigging screw and chainplate')]
    t.append(part('rig-wire', '        <path class="dg-hull-dark shape" d="M108,36 L116,36 L116,70 L108,70 Z"/>'))
    t.append(part('rigging-screw-body rigging-screw', '        <path class="dg-hull shape" d="M100,70 L124,70 L124,150 L100,150 Z"/><path class="dg-thin" d="M104,80 H120 M104,90 H120 M104,100 H120 M104,120 H120 M104,130 H120 M104,140 H120" opacity=".6"/>\n' + label(132, 100, 'Rigging screw', 'dg-label small') + '\n' + label(132, 114, '(bottlescrew,', 'dg-label small') + '\n' + label(132, 128, 'turnbuckle)', 'dg-label small')))
    t.append(part('split-pin', '        <path class="dg-accent" d="M96,84 L128,84 M96,136 L128,136" stroke-width="2"/>\n' + label(92, 88, 'Split pins', 'dg-label small', 'end')))
    t.append(part('toggle', '        <path class="dg-hull-dark shape" d="M104,150 L120,150 L120,176 L104,176 Z"/><circle class="dg-hull-dark shape" cx="112" cy="188" r="9"/>\n' + label(132, 170, 'Toggle: a hinge', 'dg-label small') + '\n' + label(132, 184, 'so the wire can', 'dg-label small') + '\n' + label(132, 198, 'swing, not bend', 'dg-label small')))
    t.append(part('clevis-pin', '        <circle class="dg-accent-fill shape" cx="112" cy="188" r="4"/>\n' + label(92, 192, 'Clevis pin', 'dg-label small', 'end')))
    t.append('        <rect class="dg-hull" x="20" y="222" width="190" height="16"/>')
    t.append(muted(30, 250, 'deck', 'start'))
    t.append(part('chainplate-strap chainplate', '        <path class="dg-hull-dark shape" d="M106,196 L118,196 L118,300 L106,300 Z"/><circle class="dg-thin" cx="112" cy="252" r="3"/><circle class="dg-thin" cx="112" cy="272" r="3"/><circle class="dg-thin" cx="112" cy="292" r="3"/>\n        <rect class="dg-hull-dark shape" x="124" y="244" width="8" height="56"/><rect class="dg-hull-dark shape" x="92" y="244" width="8" height="56"/>\n' + label(136, 260, 'Chainplate strap', 'dg-label small') + '\n' + label(136, 274, 'bolted through a', 'dg-label small') + '\n' + label(136, 288, 'bulkhead or knee', 'dg-label small')))
    t.append(part('chainplate-leak', '        <path class="dg-bad" d="M104,214 L104,236 M120,214 L120,236" stroke-width="2" stroke-dasharray="2 2"/>\n' + label(20, 330, 'Fault: sealant fails where the', 'dg-label small') + '\n' + label(20, 344, 'strap passes the deck; water', 'dg-label small') + '\n' + label(20, 358, 'rots the wood and rusts the strap', 'dg-label small')))
    tiles.append('\n'.join(t))
    # 4 T-terminal and spreader tip
    t = [title(112, 24, 'At the mast and spreader')]
    t.append('        <rect class="dg-hull-dark" x="20" y="36" width="24" height="264"/>')
    t.append(part('t-terminal', '        <path class="dg-hull shape" d="M44,70 L60,70 L60,64 L74,64 L74,96 L60,96 L60,90 L44,90 Z"/><path class="dg-hull-dark shape" d="M74,76 L92,80 L92,86 L74,84 Z"/>\n' + label(96, 72, 'T-terminal: the wire’s', 'dg-label small') + '\n' + label(96, 86, 'end hooks into a slot', 'dg-label small') + '\n' + label(96, 100, 'in the mast wall', 'dg-label small')))
    t.append(part('spreader-root', '        <path class="dg-hull-dark shape" d="M44,214 L150,206 L150,216 L44,224 Z"/><rect class="dg-hull shape" x="44" y="190" width="18" height="32"/>\n' + label(96, 190, 'Spreader root', 'dg-label small') + '\n' + lead(94, 194, 62, 204)))
    t.append(part('spreader-tip', '        <circle class="dg-accent-fill shape" cx="152" cy="211" r="7"/><path class="dg-line shape" d="M110,120 L152,204 L172,340"/>\n        <path class="hit" d="M110,120 L152,204 L172,340" stroke="transparent" stroke-width="12" fill="none"/>\n' + label(50, 306, 'Spreader tip: the cap', 'dg-label small') + '\n' + label(50, 320, 'shroud is clamped or', 'dg-label small') + '\n' + label(50, 334, 'seized here, under a', 'dg-label small') + '\n' + label(50, 348, 'boot to protect sails', 'dg-label small') + '\n' + lead(100, 302, 148, 218)))
    t.append(muted(112, 366, 'Faults: cracked tang or T-slot,'))
    t.append(muted(112, 378, 'bent spreader, tip slid down the wire'))
    tiles.append('\n'.join(t))
    for i, body in enumerate(tiles):
        P.append(f'      <g transform="translate({i*225},0)">\n{body}\n      </g>')
    return '\n'.join(P)

# ---------------------------------------------------------------- mast step (viewBox 0 0 900 360)
def mast_step():
    P = [marker('ms-arrow')]
    P.append(title(230, 24, 'Deck-stepped mast'))
    P.append(title(680, 24, 'Keel-stepped mast'))
    for ox in (0, 450):
        P.append(f'      <rect class="dg-hull" x="{ox+40}" y="150" width="380" height="14"/>')      # deck
        P.append(f'      <path class="dg-hull" d="M{ox+40},300 Q{ox+230},330 {ox+420},300 L{ox+420},316 Q{ox+230},346 {ox+40},316 Z"/>')  # hull bottom
        P.append(muted(ox+70, 190, 'cabin', 'start'))
        P.append(muted(ox+70, 140, 'deck', 'start'))
    # deck-stepped
    P.append(part('rig-mast', '        <rect class="dg-hull-dark shape" x="216" y="30" width="28" height="118"/>'))
    P.append(part('mast-step-plate', '        <rect class="dg-hull shape" x="200" y="140" width="60" height="12"/>\n' + label(270, 110, 'Mast step plate on deck;', 'dg-label small') + '\n' + label(270, 124, 'halyards exit at the base', 'dg-label small') + '\n' + lead(268, 120, 258, 142)))
    P.append(part('compression-post', '        <rect class="dg-hull-dark shape" x="222" y="164" width="16" height="140"/>\n' + label(250, 240, 'Compression post (or a', 'dg-label small') + '\n' + label(250, 254, 'bulkhead) carries the', 'dg-label small') + '\n' + label(250, 268, 'mast load down to the keel', 'dg-label small')))
    P.append(part('deck-compression', '        <path class="dg-bad" d="M160,150 Q230,166 300,150" fill="none" stroke-width="2" stroke-dasharray="4 3"/>\n' + label(60, 232, 'Fault: deck dished', 'dg-label small') + '\n' + label(60, 246, 'or post base rotten', 'dg-label small') + '\n' + label(60, 260, 'when the core is wet', 'dg-label small') + '\n' + lead(120, 228, 190, 160)))
    P.append(muted(230, 340, 'Moody 33, Sadler 32 and most of this class'))
    # keel-stepped
    P.append(part('rig-mast', '        <rect class="dg-hull-dark shape" x="666" y="30" width="28" height="272"/>'))
    P.append(part('partners', '        <rect class="dg-sail-2 shape" x="654" y="150" width="12" height="14"/><rect class="dg-sail-2 shape" x="694" y="150" width="12" height="14"/><path class="dg-hull shape" d="M646,150 L714,150 L714,140 L646,140 Z"/>\n' + label(714, 84, 'Partners: the hole in the', 'dg-label small') + '\n' + label(714, 98, 'deck, with wedges or', 'dg-label small') + '\n' + label(714, 112, 'Spartite round the mast', 'dg-label small') + '\n' + label(714, 126, 'and a boot over the top', 'dg-label small') + '\n' + lead(712, 120, 704, 146)))
    P.append(part('mast-heel', '        <rect class="dg-hull shape" x="650" y="298" width="60" height="10"/><path class="dg-hull-dark shape" d="M666,302 L694,302 L694,292 L666,292 Z" opacity=".5"/>\n' + label(720, 292, 'Mast heel on a step', 'dg-label small') + '\n' + label(720, 306, 'bolted to the keel floor', 'dg-label small')))
    P.append(part('mast-heel-corrosion', '        <path class="dg-bad-fill shape" d="M660,296 L700,296 L700,300 L660,300 Z" opacity=".7"/>\n        <path class="dg-accent" d="M680,60 L680,120" stroke-dasharray="3 3" marker-end="url(#ms-arrow)"/>\n' + label(470, 232, 'Fault: rain runs down', 'dg-label small') + '\n' + label(470, 246, 'inside the mast and', 'dg-label small') + '\n' + label(470, 260, 'pools at the heel;', 'dg-label small') + '\n' + label(470, 274, 'the aluminium corrodes', 'dg-label small') + '\n' + lead(560, 270, 660, 298)))
    P.append(muted(680, 340, 'stiffer and stronger; leaks at the partners; Finnsailer 35 TBC'))
    return '\n'.join(P)

# ---------------------------------------------------------------- reefing and furling (viewBox 0 0 900 400)
def reefing():
    P = [marker('rf-arrow')]
    # panel 1 slab reefing
    P.append(title(180, 24, 'Slab reefing, first reef tucked in'))
    P.append(part('rig-mast', '        <rect class="dg-hull-dark shape" x="300" y="40" width="8" height="300"/>'))
    P.append(part('rig-boom', '        <rect class="dg-hull-dark shape" x="60" y="300" width="248" height="7"/>'))
    P.append(part('rig-mainsail mainsail', '        <path class="dg-sail shape" d="M304,60 L304,280 L128,296 C190,230 240,150 304,60 Z" opacity=".9"/>'))
    P.append(part('reef-cringle', '        <circle class="dg-accent-fill shape" cx="308" cy="280" r="5"/><circle class="dg-accent-fill shape" cx="128" cy="296" r="5"/>'))
    P.append(part('rams-horn', '        <path class="dg-hull-dark shape" d="M306,292 C322,292 326,276 314,270 C308,266 300,272 304,280" fill="none" stroke-width="3"/>\n' + label(372, 268, 'Luff cringle dropped', 'dg-label small') + '\n' + label(372, 282, 'over the ram’s horn', 'dg-label small') + '\n' + label(372, 296, 'at the gooseneck', 'dg-label small') + '\n' + lead(370, 280, 322, 280)))
    P.append(part('reefing-pennant reefing-line', '        <path class="dg-accent shape" d="M64,306 L64,286 L128,296 L128,306" fill="none" stroke-width="2"/>\n' + label(20, 362, 'Reefing line: from the boom end up through', 'dg-label small') + '\n' + label(20, 376, 'the leech cringle, down to the boom, forward to a winch', 'dg-label small')))
    P.append(part('reef-bundle', '        <path class="dg-sail-2 shape" d="M128,296 C180,278 250,272 306,282 C300,300 200,308 128,306 Z" opacity=".7"/>\n        <path class="dg-line" d="M180,282 L180,304 M230,278 L230,304 M270,278 L270,304" stroke-dasharray="3 2"/>\n' + label(210, 330, 'Slab of sail below the reef, folded onto', 'dg-label small', 'middle') + '\n' + label(210, 344, 'the boom and tied with the reef points', 'dg-label small', 'middle')))
    P.append(muted(180, 392, 'the reefed sail is smaller, flatter and lower'))
    # panel 2 in-mast furling section
    P.append(title(520, 24, 'In-mast furling (from above)'))
    P.append(part('inmast-section', '        <path class="dg-hull-dark shape" d="M470,140 C470,90 550,90 550,140 L550,210 L470,210 Z"/><path class="dg-hull shape" d="M478,140 C478,98 542,98 542,140 L542,202 L478,202 Z"/>\n        <rect class="dg-hull shape" x="502" y="200" width="16" height="30"/>\n' + label(510, 250, 'Slot in the back of the mast', 'dg-label small', 'middle')))
    P.append(part('mandrel', '        <circle class="dg-hull-dark shape" cx="510" cy="150" r="9"/><circle class="dg-thin" cx="510" cy="150" r="22" fill="none"/><circle class="dg-thin" cx="510" cy="150" r="30" fill="none"/>\n' + label(566, 128, 'Sail rolled on a rod', 'dg-label small') + '\n' + label(566, 142, '(mandrel) inside the mast', 'dg-label small') + '\n' + lead(564, 132, 542, 146)))
    P.append(part('inmast-jam', '        <path class="dg-bad" d="M490,170 Q510,190 530,170" fill="none" stroke-width="2.5"/>\n' + label(566, 190, 'Fault: a loose roll jams', 'dg-label small') + '\n' + label(566, 204, 'in the slot, half out', 'dg-label small')))
    P.append(muted(510, 314, 'no battens; the slot faces aft'))
    # panel 3 headsail furler (drawn at its old coordinates, shifted 30 units left as a group)
    P.append('      <g transform="translate(-30,0)">')
    P.append(title(780, 24, 'Headsail furler'))
    P.append(part('furler-foil', '        <rect class="dg-hull shape" x="776" y="60" width="10" height="250"/><path class="dg-thin" d="M781,60 L781,310" opacity=".5"/>\n' + label(796, 200, 'Foil: a grooved', 'dg-label small') + '\n' + label(796, 214, 'tube around', 'dg-label small') + '\n' + label(796, 228, 'the forestay', 'dg-label small')))
    P.append(part('halyard-swivel', '        <rect class="dg-accent-fill shape" x="770" y="60" width="22" height="18" rx="3"/>\n' + label(796, 74, 'Halyard swivel', 'dg-label small')))
    P.append(part('halyard-wrap', '        <path class="dg-bad" d="M781,58 Q790,44 802,36" fill="none" stroke-width="2"/>\n        <path class="dg-line" d="M781,58 L781,30" stroke-dasharray="3 2"/>\n' + label(796, 100, 'Halyard wrap: the', 'dg-label small') + '\n' + label(796, 114, 'halyard winds round', 'dg-label small') + '\n' + label(796, 128, 'the foil if it leaves', 'dg-label small') + '\n' + label(796, 142, 'the swivel too flat', 'dg-label small')))
    P.append(part('furler-drum furler', '        <rect class="dg-hull-dark shape" x="762" y="310" width="38" height="30" rx="4"/><path class="dg-thin" d="M766,318 H796 M766,326 H796 M766,334 H796" opacity=".6"/>\n        <path class="dg-accent" d="M762,326 L716,326" stroke-width="2" marker-end="url(#rf-arrow)"/>\n' + label(700, 316, 'Furling line', 'dg-label small', 'end') + '\n' + label(700, 330, 'to the cockpit', 'dg-label small', 'end') + '\n' + label(780, 366, 'Drum on the bow fitting', 'dg-label small', 'middle')))
    P.append(muted(780, 386, 'forestay inside cannot be inspected'))
    P.append('      </g>')
    return '\n'.join(P)
