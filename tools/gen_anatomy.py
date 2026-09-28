# Generates sections/01-anatomy.html for Sailing 101.
# Geometry notes: profile at 52 units per metre (LOA ~10 m -> 520), mast 11.5 m above deck.
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
import html
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_common import compare as _compare, sources as _sources, a as _a, photo as _photo, photos as _photos

def part(term, body, extra=''):
    return f'      <g class="part" data-term="{term}"{extra}>\n{body}\n      </g>'

def label(x, y, text, cls='dg-label', anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ''
    return f'        <text class="{cls}" x="{x}" y="{y}"{a}>{text}</text>'

def lead(x1, y1, x2, y2, cls='dg-lead'):
    return f'        <line class="{cls}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>'

# ============================================================ PROFILE
def profile():
    P = []
    P.append('      <rect class="dg-water" x="40" y="740" width="820" height="130"/>')
    # underwater appendages first
    P.append(part('keel', '        <path class="dg-hull-dark shape" d="M505,780 L478,830 L410,830 L392,780 Z"/>\n' + label(447, 864, 'Fin keel', anchor='middle')))
    P.append(part('rudder', '        <path class="dg-hull-dark shape" d="M268,768 L256,822 L232,822 L230,766 Z"/>\n' + label(232, 842, 'Rudder', anchor='middle')))
    P.append(part('propeller', '        <line class="dg-line shape" x1="305" y1="792" x2="352" y2="780"/>\n        <ellipse class="dg-hull-dark shape" cx="305" cy="792" rx="3.5" ry="13"/>\n' + label(312, 842, 'Propeller and shaft') + '\n' + lead(320, 836, 307, 806)))
    # hull
    hull = 'M190,686 Q450,694 710,652 C716,676 700,712 688,740 C660,772 560,782 450,782 C340,782 250,770 212,745 Z'
    P.append(part('hull topsides', f'        <path class="dg-hull shape" d="{hull}"/>\n' + label(440, 728, 'Hull (topsides)', anchor='middle')))
    P.append(part('waterline boot-top', '        <line class="dg-waterline shape" x1="40" y1="740" x2="860" y2="740"/>\n        <path class="dg-thin" d="M214,733 L690,733" stroke-dasharray="2 3"/>\n        <line class="hit" x1="40" y1="740" x2="860" y2="740"/>\n' + label(50, 758, 'Waterline and boot top', 'dg-waterline-label')))
    P.append(part('antifouling', '        <rect class="shape-fill" x="215" y="742" width="470" height="38"/>\n' + label(600, 768, 'Antifouling', 'dg-label small')))
    # coachroof, cockpit, wheel
    P.append(part('coachroof', '        <path class="dg-hull shape" d="M358,694 L366,664 L575,652 L592,667 Z"/>\n        <rect class="dg-thin" x="385" y="668" width="70" height="8" rx="3"/><rect class="dg-thin" x="470" y="663" width="60" height="8" rx="3"/><rect class="dg-thin" x="542" y="659" width="24" height="8" rx="3"/>\n' + label(690, 708, 'Coachroof', anchor='middle') + '\n' + lead(668, 702, 584, 656)))
    P.append(part('cockpit', '        <path class="dg-line shape" d="M235,694 L240,686 L358,686"/>\n        <rect class="hit" x="236" y="668" width="122" height="28"/>\n' + label(292, 712, 'Cockpit', anchor='middle') + '\n' + lead(292, 702, 292, 694)))
    P.append(part('wheel', '        <circle class="dg-line shape" cx="270" cy="672" r="11"/>\n        <line class="dg-line shape" x1="270" y1="683" x2="270" y2="692"/>\n' + label(256, 640, 'Wheel', anchor='end') + '\n' + lead(258, 644, 268, 662)))
    P.append(part('traveller', '        <rect class="dg-hull-dark shape" x="350" y="684" width="16" height="5" rx="2"/>\n' + label(366, 704, 'Traveller') + '\n' + lead(366, 699, 358, 690)))
    P.append(part('chainplate', '        <rect class="dg-hull-dark shape" x="483" y="674" width="6" height="9"/><rect class="dg-hull-dark shape" x="499" y="673" width="6" height="9"/><rect class="dg-hull-dark shape" x="515" y="673" width="6" height="9"/>\n' + label(545, 712, 'Chainplates') + '\n' + lead(543, 707, 519, 683)))
    P.append(part('pushpit', '        <path class="dg-thin shape" d="M200,686 V655 M225,686 V655 M194,655 H232"/>\n        <rect class="hit" x="192" y="650" width="44" height="40"/>\n' + label(186, 660, 'Pushpit', anchor='end')))
    P.append(part('pulpit', '        <path class="dg-thin shape" d="M690,656 V622 M706,652 V622 M684,622 H712"/>\n        <rect class="hit" x="682" y="618" width="34" height="40"/>\n' + label(722, 610, 'Pulpit')))
    P.append(part('transom stern', '        <line class="hit" x1="190" y1="686" x2="212" y2="745"/>\n' + label(178, 720, 'Transom', anchor='end') + '\n' + lead(181, 716, 200, 716)))
    P.append(part('bow stem', '        <path class="hit" d="M710,652 C716,676 700,712 688,740"/>\n' + label(728, 640, 'Bow / stem') + '\n' + lead(740, 646, 706, 692)))
    # sails
    P.append(part('mainsail', '        <path class="dg-sail shape" d="M503,84 Q385,330 298,609 L504,609 Z"/>\n        <path class="dg-seam" d="M420,300 H480 M375,420 H470 M335,520 H460"/>\n' + label(415, 420, 'Mainsail', 'dg-label on-main', 'middle')))
    P.append(part('genoa headsail', '        <path class="dg-sail-2 shape" d="M506,95 L708,650 Q590,662 425,615 Q475,340 506,95 Z"/>\n' + label(575, 480, 'Genoa (headsail)', 'dg-label on-sail', 'middle')))
    # spars
    P.append(part('mast', '        <rect class="dg-hull-dark shape" x="499" y="73" width="6" height="581"/>\n' + label(488, 300, 'Mast', 'dg-label on-main', 'end') + '\n' + lead(490, 296, 498, 296, 'dg-lead on-sail')))
    P.append(part('masthead', '        <rect class="dg-hull-dark shape" x="495" y="69" width="14" height="6"/>\n' + label(516, 80, 'Masthead')))
    P.append(part('boom', '        <rect class="dg-hull-dark shape" x="294" y="609" width="210" height="5"/>\n' + label(330, 604, 'Boom', 'dg-label on-main')))
    P.append(part('gooseneck', '        <circle class="dg-hull-dark shape" cx="502" cy="611" r="4"/>\n' + label(492, 598, 'Gooseneck', 'dg-label on-main', 'end') + '\n' + lead(494, 602, 501, 608, 'dg-lead on-sail')))
    P.append(part('kicker', '        <line class="dg-line shape" x1="503" y1="653" x2="440" y2="614"/>\n        <line class="hit" x1="503" y1="653" x2="440" y2="614"/>\n' + label(446, 640, 'Kicker (vang)', anchor='end') + '\n' + lead(448, 637, 470, 634)))
    P.append(part('spreaders', '        <rect class="dg-hull-dark shape" x="496" y="357" width="14" height="6"/>\n' + label(518, 364, 'Spreaders', 'dg-label on-sail')))
    P.append(part('lower-shroud', '        <path class="dg-thin shape" d="M502,365 L486,676 M502,365 L518,676"/>\n        <path class="hit" d="M502,365 L486,676 M502,365 L518,676" style="fill:none"/>\n' + label(560, 540, 'Lower shrouds', 'dg-label on-sail') + '\n' + lead(558, 536, 511, 548, 'dg-lead on-sail')))
    # rigging lines
    P.append(part('mainsheet', '        <line class="dg-thin shape" x1="358" y1="614" x2="358" y2="684"/>\n        <line class="hit" x1="358" y1="614" x2="358" y2="684"/>\n' + label(352, 652, 'Mainsheet', anchor='end')))
    P.append(part('topping-lift', '        <line class="dg-thin shape" x1="500" y1="78" x2="296" y2="608" stroke-dasharray="4 4"/>\n        <line class="hit" x1="500" y1="78" x2="296" y2="608"/>\n' + label(300, 400, 'Topping lift', anchor='end') + '\n' + lead(303, 396, 372, 400)))
    P.append(part('forestay', '        <line class="dg-thin shape" x1="502" y1="76" x2="708" y2="652"/>\n        <line class="hit" x1="502" y1="76" x2="708" y2="652"/>\n' + label(585, 240, 'Forestay') + '\n' + lead(583, 236, 567, 250)))
    P.append(part('backstay', '        <line class="dg-thin shape" x1="500" y1="76" x2="196" y2="684"/>\n        <line class="hit" x1="500" y1="76" x2="196" y2="684"/>\n' + label(385, 250, 'Backstay', anchor='end') + '\n' + lead(388, 247, 410, 250)))
    # guardrails last so the label sits on top
    st = [(250,687),(330,686),(410,684),(470,680),(570,671),(650,661)]
    up = 'M200,655 ' + ' '.join(f'L{x},{y-31}' for x,y in st) + ' L700,622'
    lo = 'M200,671 ' + ' '.join(f'L{x},{y-16}' for x,y in st) + ' L700,638'
    posts = ' '.join(f'M{x},{y} V{y-31}' for x,y in st)
    P.append(part('guardrail stanchion', f'        <path class="dg-thin shape" d="{up}"/>\n        <path class="dg-thin shape" d="{lo}"/>\n        <path class="dg-thin shape" d="{posts}"/>\n        <path class="hit" d="{up}" style="fill:none"/>\n' + label(556, 628, 'Guardrails', 'dg-label small on-sail') + '\n' + lead(575, 632, 571, 641, 'dg-lead on-sail')))
    return '\n'.join(P)

# ============================================================ RIG FROM AHEAD
def rig():
    P = []
    P.append('      <rect class="dg-water" x="30" y="790" width="560" height="150"/>')
    P.append(part('keel', '        <path class="dg-hull-dark shape" d="M296,820 L324,820 L320,935 L300,935 Z"/>\n' + label(334, 900, 'Fin keel')))
    P.append(part('hull', '        <path class="dg-hull shape" d="M160,710 Q310,690 460,710 C462,760 430,802 370,822 L250,822 C190,802 158,760 160,710 Z"/>\n' + label(250, 812, 'Hull')))
    P.append(part('waterline', '        <line class="dg-waterline shape" x1="30" y1="790" x2="590" y2="790"/>\n        <line class="hit" x1="30" y1="790" x2="590" y2="790"/>\n' + label(82, 808, 'Waterline', 'dg-waterline-label')))
    P.append(part('coachroof', '        <path class="dg-hull shape" d="M220,712 L228,680 L392,680 L400,712 Z"/>\n' + label(240, 772, 'Coachroof', anchor='end') + '\n' + lead(232, 766, 226, 712)))
    P.append(part('chainplate', '        <rect class="dg-hull-dark shape" x="176" y="704" width="12" height="16" rx="1"/><rect class="dg-hull-dark shape" x="190" y="704" width="12" height="16" rx="1"/><rect class="dg-hull-dark shape" x="418" y="704" width="12" height="16" rx="1"/><rect class="dg-hull-dark shape" x="432" y="704" width="12" height="16" rx="1"/>\n' + label(80, 736, 'Chainplates') + '\n' + lead(158, 732, 178, 714)))
    P.append(part('rigging-screw', '        <rect class="dg-hull-dark shape" x="178" y="672" width="8" height="32" rx="2"/><rect class="dg-hull-dark shape" x="192" y="676" width="8" height="28" rx="2"/><rect class="dg-hull-dark shape" x="420" y="676" width="8" height="28" rx="2"/><rect class="dg-hull-dark shape" x="434" y="672" width="8" height="32" rx="2"/>\n' + label(536, 736, 'Rigging screws', anchor='end') + '\n' + lead(462, 732, 440, 702)))
    P.append(part('guardrail stanchion', '        <path class="dg-thin shape" d="M160,657 H270 M350,657 H460 M160,683 H270 M350,683 H460 M166,712 V657 M230,710 V657 M285,708 V657 M335,708 V657 M390,710 V657 M454,712 V657"/>\n        <path class="hit" d="M165,657 H270 M350,657 H455" style="fill:none"/>\n' + label(80, 640, 'Guardrails, two wires') + '\n' + lead(160, 644, 176, 657)))
    P.append(part('pulpit', '        <path class="dg-thin shape" d="M270,712 V660 Q310,645 350,660 V712"/>\n        <path class="hit" d="M270,712 V660 Q310,645 350,660 V712" style="fill:none"/>\n' + label(356, 636, 'Pulpit') + '\n' + lead(354, 640, 342, 654)))
    P.append(part('cap-shroud shroud', '        <path class="dg-thin shape" d="M310,76 L222,363 L182,704 M310,76 L398,363 L438,704"/>\n        <path class="hit" d="M310,76 L222,363 L182,704 M310,76 L398,363 L438,704" style="fill:none"/>\n' + label(395, 220, 'Cap shrouds') + '\n' + lead(393, 216, 360, 220)))
    P.append(part('lower-shroud shroud', '        <path class="dg-thin shape" d="M310,372 L196,704 M310,372 L424,704"/>\n        <path class="hit" d="M310,372 L196,704 M310,372 L424,704" style="fill:none"/>\n' + label(190, 520, 'Lower shrouds', anchor='end') + '\n' + lead(192, 516, 256, 520)))
    P.append(part('spreaders', '        <path class="dg-line shape" d="M310,370 L222,363 M310,370 L398,363" stroke-width="5"/>\n' + label(214, 360, 'Spreaders', anchor='end')))
    P.append(part('mast', '        <rect class="dg-hull-dark shape" x="304" y="72" width="12" height="608"/>\n' + label(268, 230, 'Mast', anchor='end') + '\n' + lead(270, 226, 303, 226)))
    P.append(part('masthead', '        <rect class="dg-hull-dark shape" x="298" y="66" width="24" height="8" rx="2"/>\n        <line class="dg-thin shape" x1="320" y1="66" x2="320" y2="34"/>\n        <circle class="dg-hull-dark" cx="300" cy="62" r="3"/>\n' + label(332, 60, 'Masthead')))
    P.append(part('forestay furler', '        <line class="dg-line shape" x1="310" y1="76" x2="310" y2="700" stroke-width="3"/><line class="dg-thin" x1="313" y1="76" x2="313" y2="690" opacity=".5"/>\n        <circle class="dg-hull-dark shape" cx="310" cy="700" r="12"/>\n        <line class="hit" x1="310" y1="120" x2="310" y2="690"/>\n' + label(336, 150, 'Forestay (in furler)') + '\n' + lead(343, 146, 312, 150) + '\n' + label(335, 772, 'Furling drum (really at the bow)', 'dg-label small') + '\n' + lead(333, 768, 316, 708)))
    return '\n'.join(P)

# ============================================================ DECK PLAN
HULL_PLAN = 'M70,150 C200,105 350,88 470,90 C640,92 800,150 880,230 C800,310 640,368 470,370 C350,372 200,355 70,310 Z'
def badge(x, y, n):
    return f'        <g class="badge"><circle class="badge__dot" cx="{x}" cy="{y}" r="12"/><text class="badge__n" x="{x}" y="{y+4.5}" text-anchor="middle">{n}</text></g>'

DECK = [
 ("bow-roller", "Bow roller", (905,214), '<rect class="dg-hull-dark shape" x="872" y="224" width="20" height="12" rx="2"/><line class="dg-thin" x1="753" y1="230" x2="872" y2="230" stroke-dasharray="4 4"/>'),
 ("pulpit", "Pulpit", (826,158), '<path class="dg-thin shape" d="M805,172 C850,186 872,212 878,230 C872,248 850,274 805,288"/><path class="hit" d="M805,172 C850,186 872,212 878,230 C872,248 850,274 805,288" style="fill:none"/>'),
 ("fairlead", "Fairleads", (868,274), '<path class="dg-hull-dark shape" d="M850,194 l10,-4 l3,6 l-10,4 z"/><path class="dg-hull-dark shape" d="M850,266 l10,4 l3,-6 l-10,-4 z"/>'),
 ("anchor-locker windlass", "Anchor locker and windlass", (800,244), '<rect class="dg-thin shape" x="760" y="205" width="60" height="50" rx="4"/><rect class="dg-hull-dark shape" x="735" y="222" width="18" height="16" rx="2"/><circle class="dg-line" cx="744" cy="230" r="4"/>'),
 ("foredeck", "Foredeck", (712,196), '<path class="shape-fill" d="M632,135 C700,140 790,170 858,230 C790,290 700,320 632,325 C640,290 640,170 632,135 Z"/>'),
 ("forehatch hatch", "Forehatch", (720,230), '<rect class="dg-thin shape" x="700" y="212" width="40" height="36" rx="4"/>'),
 ("toe-rail", "Toe rail", (640,76), '<path class="dg-thin shape" d="M78,158 C205,114 352,97 470,99 C636,101 790,156 866,230 C790,304 636,359 470,361 C352,363 205,346 78,302 Z"/><path class="hit" d="M78,158 C205,114 352,97 470,99 C636,101 790,156 866,230" style="fill:none"/><line class="dg-lead" x1="640" y1="88" x2="640" y2="100"/>'),
 ("guardrail stanchion", "Guardrail (two wires) on stanchions", (700,112), '<path class="dg-thin shape" d="M180,128 L300,106 L420,99 L600,108 L700,134 L800,175"/><path class="dg-thin shape" d="M180,332 L300,354 L420,361 L600,352 L700,326 L800,285"/><path class="hit" d="M180,128 L300,106 L420,99 L600,108 L700,134 L800,175" style="fill:none"/>' + ''.join(f'<circle class="dg-hull-dark" cx="{x}" cy="{y}" r="3"/>' for x,y in [(180,128),(300,106),(420,99),(600,108),(700,134),(180,332),(300,354),(420,361),(600,352),(700,326)]) + '<line class="dg-lead" x1="700" y1="124" x2="700" y2="132"/>'),
 ("jackstay", "Jackstays (clip your harness on here)", (650,152), '<path class="dg-thin shape" d="M245,126 L620,124 L770,196" stroke-dasharray="6 4"/><path class="dg-thin shape" d="M245,334 L620,336 L770,264" stroke-dasharray="6 4"/><path class="hit" d="M245,126 L620,124 L770,196" style="fill:none"/>'),
 ("dorade", "Dorade vents", (603,230), '<circle class="dg-thin shape" cx="600" cy="205" r="6"/><circle class="dg-thin shape" cx="600" cy="255" r="6"/>'),
 ("coachroof", "Coachroof and windows", (500,196), '<path class="dg-hull shape" d="M330,140 L560,140 C600,142 620,180 625,230 C620,280 600,318 560,320 L330,320 Z"/><rect class="dg-thin" x="400" y="148" width="55" height="12" rx="3"/><rect class="dg-thin" x="470" y="148" width="50" height="12" rx="3"/><rect class="dg-thin" x="400" y="300" width="55" height="12" rx="3"/><rect class="dg-thin" x="470" y="300" width="50" height="12" rx="3"/>'),
 ("chainplate", "Chainplates", (555,74), '<rect class="dg-hull-dark shape" x="541" y="97" width="8" height="8"/><rect class="dg-hull-dark shape" x="553" y="96" width="8" height="8"/><rect class="dg-hull-dark shape" x="565" y="97" width="8" height="8"/><rect class="dg-hull-dark shape" x="541" y="355" width="8" height="8"/><rect class="dg-hull-dark shape" x="553" y="356" width="8" height="8"/><rect class="dg-hull-dark shape" x="565" y="355" width="8" height="8"/><line class="dg-lead" x1="555" y1="86" x2="557" y2="95"/>'),
 ("mast", "Mast", (555,262), '<circle class="dg-hull-dark shape" cx="555" cy="230" r="9"/>'),
 ("genoa-track", "Genoa track and car", (420,131), '<line class="dg-line shape" x1="400" y1="118" x2="600" y2="118"/><rect class="dg-hull-dark shape" x="458" y="113" width="14" height="10" rx="2"/><line class="dg-line shape" x1="400" y1="342" x2="600" y2="342"/><rect class="dg-hull-dark shape" x="458" y="337" width="14" height="10" rx="2"/><line class="dg-thin" x1="458" y1="123" x2="272" y2="146" stroke-dasharray="3 4"/>'),
 ("side-deck", "Side deck", (360,131), '<path class="shape-fill" d="M330,104 L330,140 L560,140 L600,142 L610,105 Z" opacity="1"/>'),
 ("cleat", "Cleats (bow, midship, stern)", (500,101), '<rect class="dg-hull-dark shape" x="826" y="200" width="20" height="6" rx="3" transform="rotate(-25 836 203)"/><rect class="dg-hull-dark shape" x="826" y="254" width="20" height="6" rx="3" transform="rotate(25 836 257)"/><rect class="dg-hull-dark shape" x="490" y="106" width="20" height="6" rx="3"/><rect class="dg-hull-dark shape" x="490" y="348" width="20" height="6" rx="3"/><rect class="dg-hull-dark shape" x="88" y="160" width="20" height="6" rx="3" transform="rotate(-15 98 163)"/><rect class="dg-hull-dark shape" x="88" y="294" width="20" height="6" rx="3" transform="rotate(15 98 297)"/><line class="dg-lead" x1="500" y1="113" x2="500" y2="108"/>'),
 ("halyard-winch clutch", "Halyard winches and clutches", (458,170), '<circle class="dg-line shape" cx="370" cy="170" r="9"/><rect class="dg-thin shape" x="386" y="163" width="56" height="14" rx="3"/><path class="dg-thin" d="M400,163 V177 M414,163 V177 M428,163 V177"/><circle class="dg-line shape" cx="370" cy="290" r="9"/><rect class="dg-thin shape" x="386" y="283" width="56" height="14" rx="3"/><path class="dg-thin" d="M400,283 V297 M414,283 V297 M428,283 V297"/>'),
 ("sprayhood", "Sprayhood (folded down)", (338,309), '<path class="dg-thin shape" d="M318,168 L346,168 C356,185 356,275 346,292 L318,292" stroke-dasharray="5 4"/>'),
 ("companionway sliding-hatch", "Companionway and sliding hatch", (354,212), '<rect class="dg-thin shape" x="332" y="198" width="44" height="64" rx="3"/><line class="dg-line shape" x1="332" y1="198" x2="332" y2="262"/>'),
 ("boom", "Boom (stowed on the centreline)", (290,212), '<rect class="dg-hull-dark shape" x="250" y="226" width="305" height="8" rx="3" opacity=".7"/>'),
 ("traveller", "Mainsheet traveller", (338,183), '<line class="dg-line shape" x1="322" y1="160" x2="322" y2="300"/><rect class="dg-hull-dark shape" x="318" y="222" width="8" height="16" rx="2"/>'),
 ("winch primary-winch", "Primary (genoa) winches", (290,164), '<circle class="dg-line shape" cx="262" cy="150" r="11"/><circle class="dg-thin" cx="262" cy="150" r="5"/><circle class="dg-line shape" cx="262" cy="310" r="11"/><circle class="dg-thin" cx="262" cy="310" r="5"/>'),
 ("coaming", "Cockpit coaming", (200,134), '<path class="dg-thin shape" d="M130,146 L318,146 M130,314 L318,314"/><rect class="hit" x="130" y="140" width="188" height="12"/>'),
 ("cockpit", "Cockpit (seats both sides)", (232,250), '<rect class="hit" x="130" y="176" width="188" height="108" rx="6"/>'),
 ("wheel", "Wheel on its pedestal", (175,281), '<rect class="dg-hull-dark shape" x="172" y="192" width="6" height="76" rx="3"/><circle class="dg-line shape" cx="175" cy="230" r="7"/>'),
 ("cockpit-locker", "Cockpit lockers (under the seats)", (185,162), '<rect class="dg-thin shape" x="140" y="152" width="90" height="20" rx="3"/><path class="dg-thin" d="M150,154 L160,170 M170,154 L180,170 M190,154 L200,170 M210,154 L220,170"/><rect class="dg-thin shape" x="140" y="288" width="90" height="20" rx="3"/><path class="dg-thin" d="M150,290 L160,306 M170,290 L180,306 M190,290 L200,306 M210,290 L220,306"/>'),
 ("cockpit-drain", "Cockpit drains", (306,262), '<circle class="dg-thin shape" cx="306" cy="184" r="4"/><circle class="dg-thin shape" cx="306" cy="276" r="4"/><line class="dg-lead" x1="306" y1="274" x2="306" y2="250"/>'),
 ("gas-locker", "Gas locker (sealed, drains overboard)", (128,326), '<rect class="dg-thin shape" x="88" y="268" width="30" height="24" rx="3"/><circle class="dg-thin" cx="112" cy="272" r="2"/><line class="dg-lead" x1="120" y1="316" x2="108" y2="292"/>'),
 ("lazarette", "Lazarette (stern locker)", (102,230), '<rect class="dg-thin shape" x="84" y="200" width="36" height="60" rx="3"/>'),
 ("pushpit", "Pushpit", (74,132), '<path class="dg-thin shape" d="M82,150 L66,150 L66,310 L82,310 M66,180 L80,182 M66,280 L80,278"/><rect class="hit" x="60" y="146" width="26" height="168"/>'),
 ("transom stern", "Transom and bathing ladder", (46,232), '<path class="hit" d="M70,150 L70,310" style="stroke-width:14"/><path class="dg-thin shape" d="M60,216 H70 M60,230 H70 M60,244 H70 M60,212 V248"/>'),
]
def deck():
    P = [f'      <path class="dg-hull" d="{HULL_PLAN}"/>', '      <rect class="dg-hull-dark" x="130" y="176" width="188" height="108" rx="6" opacity=".5"/>']
    legend = []
    for i,(term,name,(bx,by),shapes) in enumerate(DECK,1):
        P.append(part(term, f'        {shapes}\n' + badge(bx,by,i), ' tabindex="-1"'))
        legend.append(f'      <li class="part" data-term="{term}"><span class="callouts__n" aria-hidden="true">{i}</span><button type="button" class="callouts__text">{name}</button></li>')
    return '\n'.join(P), '\n'.join(legend)

# ============================================================ COCKPIT CLOSE-UP (viewBox 0 0 900 480)
def cockpit():
    P = []
    P.append('      <text class="dg-title" x="450" y="24" text-anchor="middle">The ropes that come back to the cockpit</text>')
    P.append('      <text class="dg-muted" x="450" y="42" text-anchor="middle">seen from above, bow at the top; a typical layout: every boat differs, so label your own clutches</text>')
    # the deck, the coachroof aft end and the cockpit
    P.append('      <path class="dg-hull" d="M150,60 L750,60 L740,470 L160,470 Z" opacity=".6"/>')
    P.append('      <path class="dg-hull" d="M250,60 L650,60 L650,250 L250,250 Z"/>')
    P.append('      <path class="dg-hull" d="M230,250 L670,250 L660,470 L240,470 Z"/>')
    P.append('      <path class="dg-hull-dark" d="M300,262 L600,262 L596,462 L304,462 Z" opacity=".25"/>')
    # companionway hatch and sprayhood
    P.append(part('companionway', '        <rect class="dg-hull-dark shape" x="410" y="120" width="80" height="130" rx="4"/>'))
    P.append(label(450, 110, 'companionway hatch', 'dg-label small', 'middle'))
    # lines from the mast along the coachroof to the clutch banks
    names_p = [('halyard', 'main halyard'), ('reefing-line', 'reef 1'), ('reefing-line', 'reef 2'), ('kicker', 'kicker')]
    names_s = [('topping-lift', 'topping lift'), ('outhaul', 'outhaul'), ('cunningham', 'cunningham'), ('halyard', 'spare halyard')]
    for side, names, x0 in (('p', names_p, 330), ('s', names_s, 520)):
        for k, (term, nm) in enumerate(names):
            # the top label goes to the outermost rope on each side, so the leaders step inwards
            x = x0 + (k * 16 if side == 'p' else (3 - k) * 16)
            ly = 84 + k * 24
            lx, anchor_ = (138, 'end') if side == 'p' else (762, 'start')
            body = (f'        <line class="dg-line shape" x1="{x}" y1="62" x2="{x}" y2="196" stroke-width="3"/>\n'
                    f'        <rect class="dg-hull-dark shape" x="{x - 6}" y="196" width="12" height="22" rx="2"/>\n'
                    f'        <line class="dg-line shape" x1="{x}" y1="218" x2="{x}" y2="238" stroke-width="3"/>\n'
                    + label(lx, ly, nm, 'dg-label small', anchor_) + '\n'
                    + lead(lx + (4 if side == 'p' else -4), ly - 4, x, ly - 4) + '\n'
                    f'        <circle cx="{x}" cy="{ly - 4}" r="3" fill="var(--dg-lead)"/>')
            P.append(part(term, body))
    P.append(part('clutch', '        <rect class="shape-fill" x="320" y="192" width="64" height="30"/>\n        <rect class="shape-fill" x="512" y="192" width="64" height="30"/>\n'
                  + label(314, 211, 'clutches', 'dg-label small', 'end') + '\n' + label(584, 211, 'clutches', 'dg-label small', 'start')))
    # halyard winches on the coachroof, aft of the clutches
    for x in (300, 600):
        P.append(part('halyard-winch', f'        <circle class="dg-hull-dark shape" cx="{x}" cy="232" r="14"/><circle class="dg-hull shape" cx="{x}" cy="232" r="6"/>\n'
                      + (label(x - 20, 230, 'halyard', 'dg-label small', 'end') + '\n' + label(x - 20, 244, 'winch', 'dg-label small', 'end') if x < 450
                         else label(x + 20, 230, 'halyard', 'dg-label small', 'start') + '\n' + label(x + 20, 244, 'winch', 'dg-label small', 'start'))))
    # primary winches on the coamings, jib sheets from the jib cars on their tracks outside
    for x, sgn in ((250, -1), (650, 1)):
        P.append(part('winch', f'        <circle class="dg-hull-dark shape" cx="{x}" cy="360" r="17"/><circle class="dg-hull shape" cx="{x}" cy="360" r="7"/>'))
        P.append(part('genoa-track', f'        <line class="dg-hull-dark shape" x1="{x + sgn * 60}" y1="240" x2="{x + sgn * 60}" y2="310" stroke-width="6" stroke-linecap="round"/>'))
    P.append(part('sheet', '        <path class="dg-accent shape" d="M180,60 L190,300 L236,354" fill="none" stroke-width="3"/>\n'
                  '        <path class="dg-accent shape" d="M720,60 L710,300 L664,354" fill="none" stroke-width="3"/>\n'
                  + label(138, 330, 'jib sheet, through', 'dg-label small', 'end') + '\n' + label(138, 344, 'the car on its track,', 'dg-label small', 'end') + '\n'
                  + label(138, 358, 'to the primary winch', 'dg-label small', 'end') + '\n' + lead(142, 340, 186, 300)))
    P.append(label(762, 330, 'the other jib sheet', 'dg-label small', 'start'))
    P.append(label(762, 344, '(one each side)', 'dg-label small', 'start'))
    P.append(lead(758, 336, 714, 300))
    # the furling line, led aft along the starboard side to a cleat or clutch by the helm
    P.append(part('furling-line', '        <path class="dg-line shape" d="M735,60 L735,430 L662,440" fill="none" stroke-width="2" stroke-dasharray="2 3"/>\n'
                  + label(762, 426, 'furling line', 'dg-label small', 'start') + '\n' + label(762, 440, '(dotted), to a', 'dg-label small', 'start') + '\n'
                  + label(762, 454, 'cleat by the helm', 'dg-label small', 'start') + '\n' + lead(758, 432, 739, 432)))
    # mainsheet traveller across the cockpit
    P.append(part('traveller', '        <line class="dg-hull-dark shape" x1="320" y1="300" x2="580" y2="300" stroke-width="6" stroke-linecap="round"/><rect class="dg-hull shape" x="436" y="292" width="28" height="16" rx="3"/>'))
    P.append(part('mainsheet', '        <path class="dg-line shape" d="M450,292 L450,256" stroke-width="3"/><path class="dg-line shape" d="M464,300 L520,300" stroke-width="2" opacity=".0"/>'))
    P.append(label(450, 326, 'mainsheet traveller', 'dg-label small', 'middle'))
    P.append(label(450, 400, 'cockpit', 'dg-muted', 'middle'))
    return '\n'.join(P)

# ============================================================ BELOW DECKS
HULL_BELOW = 'M70,90 C200,45 350,28 470,30 C640,32 800,90 880,170 C800,250 640,308 470,310 C350,312 200,295 70,250 Z'
def box(x,y,w,h,cls='dg-thin shape',extra=''):
    return f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="3"{extra}/>'
def berth(x,y,w,h):
    return f'<rect class="dg-hull-dark shape" x="{x}" y="{y}" width="{w}" height="{h}" rx="3" opacity=".55"/>'
def L(x,y,t,cls='dg-label small',anchor='middle'):
    return label(x,y,t,cls,anchor)

def vberth(x0=660, x1=800):
    return (f'<path class="dg-hull-dark shape" d="M{x0},68 L{x1},118 L{x1},150 L{x0},150 Z" opacity=".55"/>'
            f'<path class="dg-hull-dark shape" d="M{x0},190 L{x1},190 L{x1},222 L{x0},272 Z" opacity=".55"/>')

def layout_common_fwd(P, xheads=580):
    P.append(part('chain-locker forepeak', f'<path class="dg-thin shape" d="M805,128 L805,212"/>\n' + L(842,166,'Chain') + '\n' + L(842,180,'locker')))
    P.append(part('forecabin v-berth', vberth(xheads+80, 800) + '\n' + L((xheads+80+800)/2,174,'Forecabin (V-berth)')))
    P.append(part('heads', box(xheads,58,80,92) + '\n' + L(xheads+40,100,'Heads') + '\n' + L(xheads+40,114,'(toilet)','dg-muted')))
    P.append(part('hanging-locker', box(xheads-6,190,92,92) + '\n' + L(xheads+40,232,'Hanging locker') + '\n' + L(xheads+40,246,'(wardrobe)','dg-muted')))

def layout_A():
    P = [f'      <path class="dg-hull" d="{HULL_BELOW}"/>']
    layout_common_fwd(P)
    P.append(part('saloon settee', berth(420,52,154,34) + berth(420,254,154,34) + '\n' + L(497,73,'Settee / sea berth') + '\n' + L(497,275,'Settee / sea berth') + '\n' + L(500,120,'Saloon','dg-label')))
    P.append(part('saloon-table', box(450,150,70,40) + '\n' + L(485,175,'Table')))
    P.append(part('mast', '<circle class="dg-hull-dark shape" cx="555" cy="170" r="6"/>\n' + L(555,158,'Mast')))
    P.append(part('chart-table', box(326,52,84,78) + '\n' + L(368,88,'Chart table') + '\n' + L(368,102,'switch panel','dg-muted')))
    P.append(part('galley', box(326,212,84,78) + '\n' + L(368,248,'Galley') + '\n' + L(368,262,'cooker, sink','dg-muted')))
    P.append(part('companionway-steps', box(292,150,24,40,'dg-thin shape') + '<path class="dg-thin" d="M298,150 V190 M304,150 V190 M310,150 V190"/>\n' + L(304,204,'Steps')))
    P.append(part('quarter-berth', berth(102,86,155,32) + '\n' + L(180,106,'Quarter berth')))
    P.append(part('cockpit', box(100,126,190,92,'dg-thin shape',' stroke-dasharray="5 4"') + '\n' + L(165,166,'Cockpit (on deck)') + '\n' + L(165,180,'(engine under the floor)','dg-muted')))
    P.append(part('engine', box(240,140,46,50,'dg-thin shape',' stroke-dasharray="4 3"') + '\n' + L(263,168,'Engine')))
    P.append(part('cockpit-locker', box(130,228,120,32) + '\n' + L(190,248,'Cockpit locker')))
    return '\n'.join(P)

def layout_B():
    P = [f'      <path class="dg-hull" d="{HULL_BELOW}"/>']
    P.append(part('chain-locker forepeak', '<path class="dg-thin shape" d="M805,128 L805,212"/>\n' + L(842,166,'Chain') + '\n' + L(842,180,'locker')))
    P.append(part('forecabin v-berth', vberth(660, 800) + '\n' + L(730,174,'Forecabin (V-berth)')))
    P.append(part('hanging-locker', box(574,58,92,92) + '\n' + L(620,100,'Hanging locker') + '\n' + L(620,114,'(wardrobe)','dg-muted')))
    P.append(part('heads', box(580,190,80,92) + '\n' + L(620,232,'Heads') + '\n' + L(620,246,'(toilet)','dg-muted')))
    P.append(part('saloon settee', berth(450,52,124,34) + berth(450,254,124,34) + '\n' + L(515,120,'Saloon','dg-label')))
    P.append(part('saloon-table', box(470,150,70,40) + '\n' + L(505,175,'Table')))
    P.append(part('mast', '<circle class="dg-hull-dark shape" cx="555" cy="170" r="6"/>\n' + L(573,174,'Mast','dg-label small','start')))
    P.append(part('chart-table', box(360,52,80,78) + '\n' + L(400,96,'Chart table')))
    P.append(part('galley', box(360,212,80,78) + '\n' + L(400,256,'Galley')))
    P.append(part('companionway-steps', box(336,150,22,40,'dg-thin shape') + '<path class="dg-thin" d="M341,150 V190 M347,150 V190 M353,150 V190"/>\n' + L(347,204,'Steps')))
    P.append(part('cockpit centre-cockpit', box(215,100,118,140,'dg-thin shape',' stroke-dasharray="5 4"') + '<rect class="dg-hull-dark shape" x="222" y="150" width="6" height="40" rx="3"/>\n' + L(288,160,'Centre cockpit') + '\n' + L(288,174,'(engine below)','dg-muted')))
    P.append(part('engine', box(240,185,80,40,'dg-thin shape',' stroke-dasharray="4 3"') + '\n' + L(280,210,'Engine')))
    P.append(part('aft-cabin', box(110,88,100,164) + berth(120,100,80,140) + '\n' + L(157,160,'Aft cabin') + '\n' + L(157,174,'double berth','dg-muted') + '\n' + L(157,186,'hatch to port','dg-muted')))
    return '\n'.join(P)

def layout_C():
    P = [f'      <path class="dg-hull" d="{HULL_BELOW}"/>']
    layout_common_fwd(P, xheads=610)
    P.append(part('saloon settee', '<path class="dg-hull-dark shape" d="M450,52 H604 V86 H484 V150 H450 Z" opacity=".55"/>' + berth(515,254,95,34) + '\n' + L(540,122,'Saloon','dg-label') + '\n' + L(547,70,'U-shaped dinette')))
    P.append(part('saloon-table', box(478,150,64,40) + '\n' + L(510,175,'Table')))
    P.append(part('mast', '<circle class="dg-hull-dark shape" cx="555" cy="170" r="6"/>\n' + L(573,174,'Mast','dg-label small','start')))
    P.append(part('galley', box(450,212,60,78) + '\n' + L(480,256,'Galley')))
    P.append(part('wheelhouse', box(260,56,190,230,'dg-thin shape',' stroke-width="2.5"') + '<rect class="dg-hull-dark shape" x="420" y="60" width="6" height="36" rx="3"/>\n' + L(392,78,'Inside helm','dg-label small','end') + '\n' + L(355,120,'Wheelhouse','dg-label') + '\n' + L(355,134,'(engine under the floor)','dg-muted') + box(280,224,80,40) + '\n' + L(320,248,'Chart table')))
    P.append(part('engine', box(300,150,110,48,'dg-thin shape',' stroke-dasharray="4 3"') + '\n' + L(355,178,'Engine')))
    P.append(part('aft-cabin', box(110,86,145,170) + berth(115,96,138,26) + berth(115,224,138,26) + '\n' + L(182,113,'Aft cabin, 2 singles') + '\n' + L(182,242,'and a washbasin','dg-muted')))
    P.append(part('cockpit', box(125,128,110,88,'dg-thin shape',' stroke-dasharray="5 4"') + '<rect class="dg-hull-dark shape" x="138" y="152" width="6" height="40" rx="3"/>\n' + L(186,166,'Aft cockpit') + '\n' + L(186,180,'(on deck)','dg-muted')))
    return '\n'.join(P)

def layout_D():
    P = [f'      <path class="dg-hull" d="{HULL_BELOW}"/>']
    layout_common_fwd(P)
    P.append(part('saloon settee', berth(420,52,154,34) + berth(420,254,154,34) + '\n' + L(500,120,'Saloon','dg-label')))
    P.append(part('saloon-table', box(450,150,70,40) + '\n' + L(485,175,'Table')))
    P.append(part('mast', '<circle class="dg-hull-dark shape" cx="555" cy="170" r="6"/>\n' + L(555,158,'Mast')))
    P.append(part('chart-table', box(326,52,84,78) + '\n' + L(368,96,'Chart table')))
    P.append(part('galley', box(326,212,84,78) + '\n' + L(368,256,'Galley')))
    P.append(part('companionway-steps', box(292,150,24,40,'dg-thin shape') + '<path class="dg-thin" d="M298,150 V190 M304,150 V190 M310,150 V190"/>\n' + L(304,204,'Steps')))
    P.append(part('aft-cabin', box(100,84,138,108) + berth(108,92,122,90) + '\n' + L(169,112,'Aft double cabin') + '\n' + L(169,126,'(under the cockpit)','dg-muted')))
    P.append(part('cockpit', box(120,140,170,60,'dg-thin shape',' stroke-dasharray="5 4"') + '\n' + L(200,216,'Cockpit (on deck)')))
    P.append(part('engine', box(244,150,40,40,'dg-thin shape',' stroke-dasharray="4 3"') + '\n' + L(264,174,'Engine')))
    P.append(part('cockpit-locker', box(130,228,120,32) + '\n' + L(190,248,'Cockpit locker')))
    return '\n'.join(P)

# ============================================================ TERMS
def terms(rows):
    out = ['  <ul class="terms">']
    for key, name, body in rows:
        out.append(f'    <li data-term="{key}"><b>{name}</b> {body}</li>')
    out.append('  </ul>')
    return '\n'.join(out)

T_DIR = [
 ("bow","Bow","The front end. <em>Forward</em> is towards it."),
 ("stern","Stern","The back end. <em>Aft</em> is towards it; <em>astern</em> is behind the boat."),
 ("port","Port","The left side when you face the bow. Its light at night is red."),
 ("starboard","Starboard","The right side when you face the bow. Green light."),
 ("quarter","Quarter","The back corners: the port quarter and the starboard quarter. Something \"on the quarter\" is behind and to one side."),
 ("amidships","Amidships","The middle of the boat, lengthwise. \"Midships!\" as a steering order means centre the wheel or tiller."),
 ("tack-gybe","Tack and gybe (the turns)","Turning the boat so that the wind crosses from one side to the other. Turning the bow through the wind is a <em>tack</em>; turning the stern through it, with the wind behind you, is a <em>gybe</em>. Both make the boom swing across. See <a href=\"#sailing\">Sailing fundamentals</a>."),
 ("centreline","Centreline","The imaginary line from bow to stern down the middle of the boat. The mast and the keel sit on it."),
 ("athwartships","Athwartships / fore-and-aft","Across the boat / along the boat."),
 ("inboard","Inboard / outboard","Towards the centreline / towards or beyond the side of the boat."),
 ("windward","Windward","The side the wind is coming from. Also called the <em>weather</em> side."),
 ("leeward","Leeward","(say \"loo-ard\") The side away from the wind."),
 ("ahead","Ahead / astern","In front of / behind the boat. Also the two gear directions of the engine."),
 ("abeam","Abeam","At right angles to the centreline, out to the side."),
 ("below","Below","Inside the cabin. <em>On deck</em> is outside."),
 ("heel","Heel","The boat leaning over under the push of the wind. Normal; heavy heel is slow."),
 ("helm","Helm","The steering position, the wheel or tiller itself, and the person steering (\"who has the helm?\")."),
]
T_HULL = [
 ("hull","Hull","The watertight body of the boat. On this class, glass-reinforced plastic (GRP, \"fibreglass\")."),
 ("topsides","Topsides","The hull above the waterline."),
 ("waterline","Waterline","Where the hull meets the water at rest."),
 ("boot-top","Boot top","The painted stripe just above the waterline that hides the dirty mark the water leaves."),
 ("antifouling","Antifouling","Paint below the waterline that slows weed and barnacle growth. Renewed every year or two."),
 ("keel","Keel","The fixed fin under the hull. Its heavy weight (the <em>ballast</em>) pulls the boat upright again after it heels, and its area stops the boat sliding sideways. Fin, bilge (twin) or long keel: see <a href=\"#hull\">Hull, keel and rudder</a>."),
 ("ballast","Ballast","The weight, usually cast iron or lead, built into or bolted under the keel to keep the boat upright. Roughly 30–45% of the boat's weight on this class."),
 ("rudder","Rudder","The steerable blade at the stern. Turned by a tiller or a wheel through the <em>rudder stock</em>, the shaft it hangs on."),
 ("skeg","Skeg","A fixed fin ahead of the rudder that supports it. A <em>spade</em> rudder has no skeg and stands on its stock alone."),
 ("propeller","Propeller and shaft","The propeller sits under the hull, aft of the keel, on a shaft from the engine. Some boats use a <em>saildrive</em> instead: a gearbox leg that hangs straight down through the hull, like the lower half of an outboard motor."),
 ("transom","Transom","The flat or near-flat surface across the stern. The <em>bathing platform</em> and <em>boarding ladder</em> are on or below it."),
 ("stem","Stem","The leading edge of the bow, where the two sides of the hull meet."),
 ("sheer","Sheer","The curve of the deck edge seen from the side, usually lowest a little behind the middle."),
 ("freeboard","Freeboard","Height of the deck above the water. About a metre on this class."),
 ("draught","Draught (draft)","Depth from the waterline to the bottom of the keel. Decides where you can float: 1.1 m for a Finnsailer 35, up to 1.7 m for a deep-fin Sadler 32."),
 ("length","Length overall, waterline length, beam","LOA is the hull from stem to stern (9.5–10.7 m for the boats on this page); LWL is the length at the waterline (the longer it is, the faster the boat can go); beam is the greatest width (3.1–3.5 m)."),
 ("displacement","Displacement","The boat's weight, equal to the water it pushes aside. About 3.7 to 6.2 tonnes for the five boats on this page."),
 ("through-hull","Through-hull / skin fitting","Any hole through the hull with a fitting: engine cooling water inlet, sink drains, the speed and depth sensors."),
 ("seacock","Seacock","The valve on a through-hull that lets you shut it. Learn where every one is."),
 ("stern-gland","Stern gland","The seal where the propeller shaft leaves the hull. It is allowed to drip a little; more than that sinks boats slowly."),
]
T_DECK = [
 ("coachroof","Coachroof","The raised cabin top, with the coachroof windows in its sides. Also called the cabin top."),
 ("side-deck","Side deck","The walkway between the coachroof and the edge of the deck. Narrow side decks make going forward awkward and wet."),
 ("foredeck","Foredeck","The deck forward of the mast, where the anchor and the headsail are handled."),
 ("cockpit","Cockpit","The sunken, open area near the back where the crew sits and steers."),
 ("centre-cockpit","Centre cockpit / aft cockpit","Where the cockpit sits. A centre cockpit (Moody 33) leaves room for a separate aft cabin behind it; an aft cockpit (Sadler 32, Bavaria 1060) is more common and gives a larger saloon."),
 ("coaming","Coaming","The raised edge around the cockpit that keeps water out and gives you a backrest. The primary winches usually sit on it."),
 ("companionway","Companionway","The opening and steps from the cockpit down into the cabin, closed by a sliding hatch on top and washboards in front."),
 ("sliding-hatch","Sliding hatch","The lid over the companionway that slides forward to open."),
 ("washboards","Washboards","Removable boards that close the companionway opening in bad weather."),
 ("sprayhood","Sprayhood","The folding canvas hood over the companionway. Keeps spray out of the cabin and off the helm. Americans call it a dodger; in Britain <em>dodgers</em> are the cloth panels on the guardrails."),
 ("bimini","Bimini","A sun awning over the cockpit. Common on Mediterranean boats."),
 ("pulpit","Pulpit","The stainless-steel rail around the bow."),
 ("pushpit","Pushpit","The stainless-steel rail around the stern. Also called the stern rail or, in American usage, the stern pulpit."),
 ("guardrail","Guardrails and stanchions","The two wires along each side of the deck (also called lifelines) and the vertical posts that hold them up. About 60 cm high; the lower wire is there to stop a foot going through."),
 ("jackstay","Jackstays","Flat webbing straps running along each side deck from cockpit to bow. In rough weather you clip your safety harness to them before leaving the cockpit."),
 ("toe-rail","Toe rail","The raised strip along the deck edge, often slotted aluminium, that stops your feet sliding off and gives you somewhere to attach blocks (pulleys)."),
 ("cleat","Cleat","A fitting for tying a rope to. There are usually two at the bow, two amidships (near the mast, for the springs, the diagonal mooring ropes) and two at the stern."),
 ("fender","Fender","The inflated rubber bumper you hang over the side to keep the hull off the pontoon or the boat next door."),
 ("fairlead","Fairlead","A fitting that guides a rope over the deck edge without rubbing it through, but does not hold it."),
 ("winch","Winch","A drum you wind a rope around so you can pull far harder than by hand. <em>Self-tailing</em> winches grip the rope for you. The largest, on the coamings, are the <em>primaries</em> for the genoa sheets."),
 ("halyard-winch","Halyard winches","Smaller winches on the coachroof (or on the mast on older boats) for hoisting sails and for reefing (making them smaller)."),
 ("clutch","Clutch (jammer)","A lever that grips a rope so you can take it off the winch and use the winch for another rope."),
 ("traveller","Mainsheet traveller","A slider on a track across the boat. Moving it changes where the mainsheet pulls from, so you can move the boom sideways without pulling it down."),
 ("genoa-track","Genoa track and car","A track along each side deck with a sliding fitting (the car) that holds the pulley the genoa sheet runs through, so you can change the angle of pull."),
 ("chainplate","Chainplates","The metal straps bolted to the hull or deck that the shrouds (the wires holding the mast up sideways) attach to, usually three a side for the cap shroud and the two lowers. A classic leak and corrosion point."),
 ("hatch","Hatch","Any opening in the deck with a lid."),
 ("forehatch","Forehatch","The hatch on the foredeck over the forecabin. It doubles as the emergency exit."),
 ("dorade","Dorade vent","A hooded air scoop on deck with a box under it, so air gets in but water drains back out. Named after the 1930s yacht that first carried them."),
 ("cockpit-locker","Cockpit locker","Deep stowage under the cockpit seats for fenders, mooring ropes and everything else."),
 ("cockpit-drain","Cockpit drains","Pipes from the cockpit floor to the sea, so a wave that fills the cockpit empties itself."),
 ("gas-locker","Gas locker","A sealed locker for the cooking-gas bottles with a drain overboard, so leaking gas cannot collect in the bottom of the boat. Often built into the lazarette area, but never simply \"in\" it."),
 ("lazarette","Lazarette","The stern locker, right aft, often holding the steering gear and the emergency tiller."),
 ("anchor-locker","Anchor locker","The bow locker where the anchor chain is stowed."),
 ("windlass","Windlass","The winch, manual or electric, that hauls the anchor chain in over the bow roller. Many older boats have none, and the chain comes up by hand."),
 ("bow-roller","Bow roller","The fitting at the stem over which the anchor chain runs, and where the anchor usually lives."),
 ("wheel","Wheel or tiller","What you steer with. A wheel stands on a pedestal in the cockpit; a tiller is a lever fixed straight onto the rudder stock. Every wheel-steered boat should also carry an <em>emergency tiller</em> for when the wheel gear fails; check that it is aboard."),
 ("bathing-platform","Bathing platform / boarding ladder","Stern access to the water. Usual on boats built since the 1990s, rare on the older British boats, which make do with a ladder hooked over the side."),
 ("grab-rail","Grab rails","The wooden or steel handrails along the coachroof and below decks. \"One hand for the boat\" means one hand on one of these."),
 ("bridgedeck","Bridgedeck","The raised step between the cockpit and the companionway that stops a cockpit full of water pouring below. The mainsheet traveller often sits on it."),
]
T_RIG = [
 ("mast","Mast","The vertical pole (a <em>spar</em>) that holds the sails up. Anodised aluminium on this class. <em>Deck-stepped</em> masts sit on the coachroof; <em>keel-stepped</em> masts pass through the deck to the keel."),
 ("masthead","Masthead","The top of the mast. It carries the pulleys (<em>sheaves</em>) the halyards run over, the wind instrument, the VHF radio aerial and usually an all-round white anchor light. Some boats also carry a tricolour navigation light up here; older boats have only deck-level navigation lights."),
 ("boom","Boom","The horizontal spar along the bottom of the mainsail. It swings across the boat when you tack or gybe (turn so the wind crosses to the other side). It hurts."),
 ("gooseneck","Gooseneck","The hinge that joins the boom to the mast and lets it swing sideways and lift."),
 ("masthead-rig","Masthead / fractional rig","Where the forestay meets the mast: at the very top (masthead rig, most of this class) or part way up (fractional rig)."),
 ("forestay","Forestay","Wire from the masthead to the bow. Stops the mast falling backwards and carries the headsail, usually inside a furler."),
 ("furler","Furler","A drum at the bottom of the forestay and a hollow tube (the foil) around the wire: pull the furling line and the genoa rolls up around the tube like a blind."),
 ("backstay","Backstay","Wire from the masthead to the stern. Stops the mast falling forwards. A <em>split backstay</em> forks to both quarters; an <em>adjuster</em> lets you tension it."),
 ("shroud","Shrouds","The wires that hold the mast up sideways. Without them the mast would fall over the side."),
 ("cap-shroud","Cap shrouds","The shrouds that run from the masthead over the spreader tips down to the chainplates."),
 ("lower-shroud","Lower shrouds","Shorter shrouds from the base of the spreaders to the deck, one forward and one aft on each side, that stop the middle of the mast bending. From the side they make a narrow V."),
 ("spreaders","Spreaders","Horizontal struts part way up the mast that push the cap shrouds out, so the wires pull at a better angle."),
 ("rigging-screw","Rigging screws (turnbuckles)","Threaded fittings at the bottom of each wire for tensioning it. Locked with split pins or wire."),
 ("spinnaker-pole","Spinnaker pole / whisker pole","A spar that holds the outer corner of a downwind sail away from the boat, on the side opposite the mainsail. Its own lines, the <em>uphaul</em> and <em>downhaul</em>, hold it up and down."),
 ("kicker","Kicker (vang)","A strut or rope-and-pulley system (a <em>tackle</em>) from the foot of the mast to the boom that stops the boom lifting. A <em>rod kicker</em> also holds the boom up when the sail is down."),
 ("topping-lift","Topping lift","A line from the masthead to the end of the boom that holds the boom up when the sail is down."),
 ("lazyjacks","Lazyjacks and stackpack","Lines from the mast to the boom that catch the mainsail as it comes down, often with a zipped sail cover (the stackpack) fixed to the boom."),
]
T_SAIL = [
 ("mainsail","Mainsail","The sail behind the mast, attached to the mast and the boom."),
 ("headsail","Headsail","Any sail forward of the mast. A <em>genoa</em> is large and overlaps the mast; a <em>jib</em> is smaller and does not; a <em>storm jib</em> is tiny and heavy."),
 ("genoa","Genoa","A large headsail whose back corner reaches aft of the mast. Sized by overlap: a \"135% genoa\" reaches back a distance equal to 135% of the mast-to-forestay distance."),
 ("spinnaker","Spinnaker / cruising chute / gennaker","Large, light, colourful sails for sailing downwind. Fun, occasionally chaotic."),
 ("corners","Head, tack, clew","The three corners of a sail: top, front-bottom, back-bottom. (\"Tack\" the corner is a different word from \"tack\" the turn, and from \"on port tack\", which says which side the wind is on.)"),
 ("sail-attachment","How sails attach","The mainsail's front edge runs up a groove in the mast on slides or a rope edge; a furling genoa's front edge runs up the groove in the furler tube; an old-style jib clips to the forestay with <em>hanks</em>."),
 ("edges","Luff, leech, foot","The three edges of a sail: front, back and bottom."),
 ("battens","Battens","Flat stiffeners in pockets along the back edge of the mainsail."),
 ("roach","Roach","The curved extra area of the mainsail's back edge beyond a straight line from head to clew."),
 ("telltales","Telltales","Ribbons on the sail that show which way the air is flowing over it."),
 ("reef","Reef","To make a sail smaller in strong wind. <em>Slab reefing</em> lowers the mainsail part way and ties the loose fold to the boom; <em>furling</em> rolls a sail around the furler tube on the forestay, or inside the mast or boom."),
 ("sailcloth","Sail cloth","Woven polyester (Dacron) on almost all cruising boats of this class. Laminates are lighter and hold shape but die faster in the sun."),
 ("sail-cover","Sail cover","Canvas over the furled mainsail on the boom. Sunlight is what kills sails; the cover greatly extends their life."),
]
T_ROPE = [
 ("line","Line","On a boat, ropes with a job are called lines. Each has its own name below."),
 ("halyard","Halyard","A line that hoists a sail up the mast: main halyard, genoa halyard, spinnaker halyard."),
 ("sheet","Sheet","A line that controls a sail's angle to the wind. Not the sail itself. The mainsheet and the two genoa sheets are the lines you touch most."),
 ("mainsheet","Mainsheet","The rope-and-pulley system from the boom down to the traveller that pulls the mainsail in and lets it out."),
 ("outhaul","Outhaul","Tensions the bottom edge of the mainsail along the boom."),
 ("cunningham","Cunningham","Tensions the front edge of the mainsail from just above the tack."),
 ("reefing-line","Reefing lines","Lines that pull the reinforced eyes (<em>cringles</em>) in the sail down to the boom when you reef. The small ties that gather the loose fold are the <em>reef points</em>."),
 ("furling-line","Furling line","Rolls the headsail up on its furler."),
 ("guy","Guy","The windward spinnaker sheet, which runs through the end of the pole and sets the pole's angle."),
 ("working-sheet","Working sheet / lazy sheet","The genoa has two sheets, one each side. The one under load is the working sheet; the slack one is the lazy sheet. They swap every tack."),
 ("shackle","Shackle and block","A shackle is a U-shaped metal link with a pin, for joining things. A block is a pulley."),
 ("preventer","Preventer","A line from the end of the boom forward to the bow, to stop the boom slamming across in an accidental gybe when sailing downwind."),
 ("warp","Warp","A mooring or anchoring rope. <em>Bow line, stern line</em> and two <em>springs</em> (diagonal lines that stop the boat surging forwards and backwards) are the standard set of four."),
 ("painter","Painter","The rope on the front of the dinghy, the small rubber or rigid boat you row or motor ashore in."),
]
T_BELOW = [
 ("saloon","Saloon","The main cabin with seating and a table. The settees usually double as sea berths."),
 ("settee","Settee / sea berth","The bench seats along each side of the saloon. With a <em>lee cloth</em> (a canvas side that stops you rolling out) rigged, the safest place to sleep at sea."),
 ("saloon-table","Saloon table","Fixed or folding, on the centreline or against one settee."),
 ("galley","Galley","The kitchen. The cooker swings on <em>gimbals</em> so it stays level as the boat heels. Almost always beside the companionway so the cook gets air."),
 ("heads","Heads","The toilet compartment, and the toilet itself. The word comes from the days when the crew's toilet was at the head (the bow) of the ship."),
 ("forecabin","Forecabin","The bow cabin, usually with a V-shaped double berth. Lively at sea, lovely in harbour."),
 ("forepeak","Forepeak","The very front compartment, in front of the forecabin's forward wall, where the anchor chain lives. Sailors also use the word loosely for the forecabin."),
 ("v-berth","V-berth","The two berths in the forecabin that meet at the bow, often with an infill cushion to make a double."),
 ("aft-cabin","Aft cabin","The stern cabin. On a centre-cockpit boat it is a separate room with its own hatch; on aft-cockpit boats from around 1980 onwards, and on most built after 1985, it is tucked under one side of the cockpit."),
 ("quarter-berth","Quarter berth","A single berth running aft under the cockpit side, typical of 1970s–80s boats. Good sea berth, awkward to climb into."),
 ("chart-table","Chart table (navigation station)","Where the charts (sea maps), instruments and electrical switch panel live, usually beside the companionway."),
 ("companionway-steps","Companionway steps","The ladder down from the cockpit. On most aft-cockpit boats the engine sits right behind it."),
 ("engine","Engine bay","Under the cockpit floor or behind the companionway steps on an aft-cockpit boat; under the cockpit on a centre-cockpit boat; under the wheelhouse floor on a motorsailer."),
 ("wheelhouse","Wheelhouse","The enclosed, glazed deckhouse of a motorsailer (a boat built to motor as much as to sail), with an inside steering position and often a table with seats (a <em>dinette</em>)."),
 ("hanging-locker","Hanging locker","The wardrobe. Often opposite the heads."),
 ("chain-locker","Chain locker","The compartment right in the bow where the anchor chain falls."),
 ("tanks","Tanks and batteries","Fresh water and diesel tanks sit low under the berths or the cabin floor; the batteries live in a ventilated box near the engine. Know where each is and how much it holds."),
 ("bilge","Bilge","The lowest inside part of the hull, under the floor, where water collects. The <em>bilge pump</em> empties it; know where its handle is kept."),
 ("sole","Sole","The cabin floor. <b>Deckhead</b> the ceiling. <b>Bulkhead</b> an internal wall."),
 ("lockers","Lockers","Cupboards. <b>Stowage</b> anywhere you put things."),
 ("holding-tank","Holding tank","Stores toilet waste for pumping out ashore. Required in many of the seas covered here."),
]

def figure(fid, short, viewbox, title, desc, body, caption, extra_html='', note='', wide=True, start=0):
    cls = 'diagram diagram--wide' if wide else 'diagram'
    return f'''  <figure class="{cls}" id="{fid}" data-short="{short}">
    <div class="diagram__scroll" data-start="{start}"><svg viewBox="{viewbox}" role="group" aria-labelledby="{fid}-title {fid}-desc">
      <title id="{fid}-title">{title}</title>
      <desc id="{fid}-desc">{desc}</desc>
{body}
    </svg></div>
{extra_html}    <figcaption><span class="caption">{caption}</span>{note}</figcaption>
  </figure>'''

deck_svg, deck_legend = deck()
LEGEND_HTML = '    <ol class="callouts">\n' + deck_legend + '\n    </ol>\n'
HINT = '<span class="diagram__hint">Labels link to definitions: click or tap a part to jump to its definition. In the lists below, a term with a small circle after it is on a drawing; click it to see where.</span>'

layouts = [
 ('fig-below-a', 'layout A', 'A. Aft cockpit, 1970s–80s style (typical of British boats of the era such as the Sadler 32 and the Moody 33S, the aft-cockpit version of the Moody 33; mirror-image versions are common)', 'Plan view of an aft-cockpit yacht: chain locker, forecabin with V-berth, heads to port opposite a hanging locker, saloon with settees and table, mast on the centreline, chart table to port and galley to starboard beside the companionway steps, engine under the steps, quarter berth to port, cockpit and a cockpit locker to starboard.', layout_A()),
 ('fig-below-b', 'layout B', 'B. Centre cockpit, Moody 33 Mk II type (heads to starboard, galley by the steps, aft-cabin hatch offset to port)', 'Plan view of a centre-cockpit yacht: forecabin, heads and locker, saloon, mast on the centreline, chart table and galley, companionway, a centre cockpit with the engine below it, and a separate aft cabin with a double berth reached by its own hatch from the cockpit.', layout_B()),
 ('fig-below-c', 'layout C', 'C. Motorsailer with wheelhouse (Finnsailer 35)', 'Plan view of a motorsailer: forecabin, heads and locker, saloon with a U-shaped dinette and galley, mast on the centreline, a raised wheelhouse with an inside helm and chart table over the engine, an aft cabin with two single berths and a washbasin, and a small aft cockpit on deck above it.', layout_C()),
 ('fig-below-d', 'layout D', 'D. Aft cockpit with an aft cabin (Bavaria 1060, Gib\'Sea 31 and most boats built after about 1985)', 'Plan view of a later aft-cockpit yacht: forecabin, heads and locker, saloon, mast on the centreline, chart table and galley beside the steps, engine under the steps, an aft double cabin tucked under the port side of the cockpit, and a cockpit locker to starboard.', layout_D()),
]
layout_figs = []
for fid, short, ttl, desc, body in layouts:
    body = body.replace('<g class="part" data-term="', '<g class="part" tabindex="-1" data-term="')
    layout_figs.append(f'''    <figure class="diagram diagram--layout diagram--wide" id="{fid}" data-short="{short}">
      <div class="diagram__scroll" data-start="0.6"><svg viewBox="0 0 940 330" role="group" aria-labelledby="{fid}-title {fid}-desc">
        <title id="{fid}-title">{html.escape(ttl)}</title>
        <desc id="{fid}-desc">{desc}</desc>
{body}
      </svg></div>
      <figcaption><span class="caption"><strong>{ttl}.</strong></span></figcaption>
    </figure>''')

page = f'''<section id="anatomy">
  <h2>Anatomy and terminology</h2>
  <p class="lead">Sailing has its own vocabulary because precision matters when someone shouts an instruction across a windy boat. Learn these words first; everything else on this page uses them. Every label on the diagrams links to its definition, and most terms link back to a diagram with one click.</p>

  <div class="first-words">
    <p>Seven words before anything else</p>
    <dl>
      <dt>Sloop</dt><dd>A boat with one mast and two sails: a mainsail behind the mast and a headsail in front of it. Every boat on this page is a sloop.</dd>
      <dt>Line</dt><dd>A rope with a job. Almost no rope on a boat is called a rope.</dd>
      <dt>Sheet</dt><dd>The line that pulls a sail in or lets it out. It is a rope, not a sail.</dd>
      <dt>Halyard</dt><dd>The line that hoists a sail up the mast.</dd>
      <dt>Helm</dt><dd>The wheel or tiller you steer with, and the person steering.</dd>
      <dt>Cockpit</dt><dd>The open, sunken area, usually near the back of the boat, where you sit and steer.</dd>
      <dt>Berth</dt><dd>A bed on a boat. Also a parking space in a harbour, which is why parking the boat is called berthing.</dd>
    </dl>
  </div>

  <h3>The boat in profile</h3>
  <p>A typical sloop of this size seen from the side, bow to the right, sails hoisted. This is the view you will see in every brochure and the one most terms are easiest to learn from. It is a <em>masthead</em> sloop: the forestay (the wire from the bow to the mast) goes to the very top of the mast. Drawn to proportion for a 10 m boat: the mast stands about 11 m above the deck. Labels that sit on the sails have dark ink; click any of them.</p>

{figure('fig-sloop-profile', 'profile view', '0 0 900 880', 'Profile of a masthead sloop cruising yacht with parts labelled', 'Side view of a fin-keel sloop drawn to proportion: hull, keel, rudder, propeller, coachroof, cockpit with wheel, mast, boom, gooseneck, kicker, mainsail, genoa, forestay, backstay, lower shrouds, spreaders, topping lift, mainsheet and traveller, pulpit, pushpit, two guardrail wires on stanchions, chainplates, waterline, boot top and antifouling.', profile(), 'A fin-keel sloop with a rudder on its own shaft (a spade rudder), wheel steering and a shaft-driven propeller. A Bavaria 1060 has this underwater shape; a Sadler 32 has a tiller and a rudder supported by a skeg; a Finnsailer 35 (a motorsailer, built to motor as much as to sail) has a long keel and a wheelhouse instead of an open cockpit. The cap shrouds (the wires holding the mast up sideways) are hidden behind the mast in this view.', note=HINT, start=0.55)}

  <h3>Directions and positions</h3>
{terms(T_DIR)}

  <h3>Hull and underwater parts</h3>
{terms(T_HULL)}

  <h3>The deck from above</h3>
  <p>The same boat with the sails down and the boom stowed on the centreline. This is where the working gear lives, and where you will spend most of your time when berthing (parking the boat in a harbour). Numbers run roughly from the bow aft and match the list beneath the drawing; both are clickable.</p>

{figure('fig-deck-plan', 'deck plan', '0 55 940 360', 'Deck plan of a cruising yacht seen from above', 'Plan view, bow to the right, with numbered callouts matched to a legend list: bow roller, pulpit, fairleads, anchor locker and windlass, foredeck, forehatch, toe rail, guardrails on stanchions, jackstays, dorade vents, coachroof, chainplates, mast, genoa track, side deck, cleats, halyard winches and clutches, sprayhood, companionway, boom, mainsheet traveller, primary winches, coaming, cockpit, wheel, cockpit lockers, cockpit drains, gas locker, lazarette, pushpit and transom.', deck_svg, 'A typical aft-cockpit deck layout, with the ropes that hoist the sails run along the cabin top to the cockpit, and the mast about 40% of the boat’s length from the bow. Details vary: the Sadler 32 has a tiller, the Moody 33 has its cockpit amidships with an aft cabin behind it, and older boats often keep the halyard winches on the mast.', extra_html=LEGEND_HTML, start=1)}

  <h3>Deck and cockpit</h3>
{terms(T_DECK)}

  <h3>The rig seen from ahead</h3>
  <p>Looking at the boat from directly in front shows what the profile hides: the mast is held up sideways by wires called shrouds, which are pushed outwards by the spreaders and anchored to the hull at the chainplates. Lose one of those wires and the mast may well come down.</p>

{figure('fig-rig-ahead', 'rig from ahead', '0 0 620 940', 'Rig of a single-spreader masthead sloop seen from ahead', 'Bow view: mast on the coachroof, one pair of spreaders, cap shrouds from the masthead over the spreader tips to the chainplates, lower shrouds from the spreader roots to the chainplates, rigging screws, forestay with its furling drum on the centreline, pulpit, two guardrail wires on stanchions, hull cross-section with fin keel and waterline.', rig(), 'A single-spreader masthead rig, the most common arrangement on this class. The forestay runs down the centreline in front of the mast, so from ahead the two overlap and the furling drum appears at the mast foot although it is really at the bow. Forward and aft lower shrouds also overlap in this view. The mast is drawn about 40% shorter than true scale so the drawing fits the page; on the profile view it is to scale.', note=HINT, wide=False, start=0.5)}

  <h3>Rig: spars and standing rigging</h3>
  <p>The <strong>rig</strong> is everything that holds the sails up. <strong>Standing rigging</strong> is the fixed wire that keeps the mast up. <strong>Running rigging</strong> is the rope you adjust while sailing.</p>
{terms(T_RIG)}

  <h3>Sails and their parts</h3>
  <p>The corners, edges, battens and reefing points are drawn on a mainsail and genoa in <a href="#fig-sail-parts">Rig and sails</a>.</p>
{terms(T_SAIL)}

  <h3>Running rigging: the ropes</h3>
{figure('fig-cockpit', 'cockpit ropes', '0 0 900 480', 'The ropes led back to the cockpit', 'Seen from above, bow at the top: the aft end of the coachroof with the companionway hatch in the middle. Four lines on each side run aft from the mast along the coachroof into a bank of clutches, with a halyard winch beside each bank; on one side the main halyard, two reefing lines and the kicker, on the other the topping lift, outhaul, cunningham and a spare halyard. In the cockpit the mainsheet traveller runs across the boat, the jib sheets come through the jib cars on their tracks to the primary winches on the coamings, and the furling line runs aft along the side deck.', cockpit(), 'Which rope goes to which clutch varies from boat to boat. Label every clutch, and learn them before you need to reef in the dark.', note=HINT)}
{terms(T_ROPE)}

  <h3>Below decks</h3>
  <p>Four ways of arranging the same 10 metres, bow to the right in every case. Compare where the cockpit sits and what that does to the cabins. These are typical layouts; individual boats and years differ.</p>

{chr(10).join(layout_figs)}
  <p class="diagram__note">Where the cockpit goes decides everything else. An aft cockpit gives the largest saloon. A centre cockpit gives a separate aft cabin at the cost of a smaller saloon and a helm further from the stern when berthing. A motorsailer trades sailing performance for a heated wheelhouse with an inside helm. From around 1980, first on French production boats, builders learned to fit an aft double cabin under one side of an aft cockpit, which is why a Bavaria 1060 sleeps more people than a Sadler 32 a metre shorter.</p>

{terms(T_BELOW)}

  <h3 id="anatomy--say-it">Words that are not said the way they are spelt</h3>
{_compare('Sailors’ pronunciations', ['Word', 'Said', 'Notes'], [
  ['leeward', '“LOO-ard”', 'the side away from the wind'],
  ['boatswain', '“BOH-sun”', 'usually written bosun, as in bosun’s chair'],
  ['coxswain', '“COX-un”', 'the person steering a small boat'],
  ['forecastle', '“FOHK-sul”', 'often written fo’c’sle; the space in the bow'],
  ['gunwale', '“GUN-ul”', 'sometimes written gunnel; the top edge of the hull'],
  ['sheave', '“shiv”, traditionally', 'the wheel inside a block'],
  ['bowline', '“BOH-lin”', 'the knot'],
], stack=True)}
{_compare('The same thing, British and American', ['British', 'American', 'What it is'], [
  ['kicker', 'vang', 'the line or strut that holds the boom down'],
  ['guardrails', 'lifelines', 'the wires round the deck edge'],
  ['sprayhood', 'dodger', 'the folding hood over the companionway'],
], stack=True)}
{_sources('pronunciations and British and American terms', [
  'Pronunciations: ' + _a('https://en.wikipedia.org/wiki/Glossary_of_nautical_terms_(A%E2%80%93L)', 'Wikipedia, glossary of nautical terms A–L') + ', ' + _a('https://en.wikipedia.org/wiki/Glossary_of_nautical_terms_(M%E2%80%93Z)', 'M–Z') + ', ' + _a('https://en.wikipedia.org/wiki/Boatswain', 'Wikipedia, boatswain') + ', ' + _a('https://en.wikipedia.org/wiki/Coxswain', 'Wikipedia, coxswain') + ', ' + _a('https://en.wikipedia.org/wiki/Bowline', 'Wikipedia, bowline') + '.',
  'British and American pairs: ' + _a('https://en.wikipedia.org/wiki/Sprayhood', 'Wikipedia, dodger (sprayhood)') + '; kicker and guardrails as sourced in <a href="#rig">Rig</a> and <a href="#deck">Deck</a>.',
  'Pages opened directly, September 2026.',
])}

  <h3 id="anatomy--real">Some of these parts on real boats</h3>
  <p>The drawings above simplify; here are eight of the parts as they look on deck and below. Each section has more.</p>
{_photos(_photo('deck-self-tailing-winch.jpg', 'A grey self-tailing winch with a red sheet wound round its drum and led into the jaws on top, and a winch handle fitted', 'A self-tailing winch: the sheet goes clockwise round the drum and into the jaws on top, which hold it while you wind the handle.', 'ThoKay', 'CC BY-SA 3.0', 'https://creativecommons.org/licenses/by-sa/3.0', 'https://commons.wikimedia.org/wiki/File:Self-tailing_Winch.jpg', 707, 900), _photo('rig-furler-drum.jpg', 'The drum of a headsail furler at the bow of a yacht, above the stemhead fitting, with its line wound on and mooring lines coiled on deck', 'The drum at the foot of a headsail furler, at the bow. Pulling the furling line turns the foil and rolls the sail up.', 'Pierre André', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0', 'https://commons.wikimedia.org/wiki/File:Port_Crouesty_024.jpg', 1280, 1707), _photo('deck-tiller-pilot.jpg', 'A black tiller pilot on a yacht’s cockpit seat, its push rod reaching towards the tiller, with its power lead', 'A tiller pilot (a Raymarine ST1000) on a small yacht: a peg at one end fits a socket in the cockpit seat, and the push rod at the other end moves the tiller.', 'Ilmari Karonen', 'public domain', '', 'https://commons.wikimedia.org/wiki/File:Boat_autopilot.jpg', 480, 640), _photo('electronics-helm-instruments.jpg', 'Instruments mounted on a yacht’s steering pedestal: a GPS plotter on top, two instrument displays, the steering compass and an autopilot control', 'The instruments at the wheel of a small cruising yacht: a GPS plotter (Standard Horizon) on top, two Navman repeaters, the steering compass, and an autopilot control.', 'Tim Sheerman-Chase', 'CC BY 2.0', 'https://creativecommons.org/licenses/by/2.0', 'https://commons.wikimedia.org/wiki/File:Yacht_Instruments,_Southerly_Pearl.jpg', 1280, 1920))}
{_photos(_photo('rig-mast-step.jpg', 'The black alloy foot of a mast sitting in a slotted track on a white coachroof, held by a pin, with turning blocks either side', 'The foot of a deck-stepped mast, in its track on the cabin roof. More in <a href="#rig--deck-stepped">Rig</a>.', 'Jeuwre', 'CC BY-SA 4.0', 'https://creativecommons.org/licenses/by-sa/4.0', 'https://commons.wikimedia.org/wiki/File:Mast_step.jpg', 960, 1440, 'https://commons.wikimedia.org/wiki/User:Jeuwre'),
  _photo('rig-gooseneck.jpg', 'The end of an aluminium boom joined to the mast by a black hinged fitting, with reefing lines entering the boom', 'The gooseneck, the hinge between boom and mast. More in <a href="#rig--boom">Rig</a>.', 'Craig Stanfill', 'CC BY-SA 2.0', 'https://creativecommons.org/licenses/by-sa/2.0', 'https://www.flickr.com/photos/35331737@N03/48069820207/', 1024, 683, 'https://www.flickr.com/photos/photo_fiend/'),
  _photo('engine-stern-gland.jpg', 'A propeller shaft in a dirty bilge running from the gearbox coupling into a bronze packed gland and a rubber hose held by clips, with printed labels', 'A packed stern gland, where the propeller shaft leaves the hull. More in <a href="#engine--stern-gland">Engine</a>.', 'Wikialoft', 'CC0 1.0', 'https://creativecommons.org/publicdomain/zero/1.0', 'https://commons.wikimedia.org/wiki/File:Small_boat_stuffing_box.jpg', 1024, 768, 'https://commons.wikimedia.org/wiki/User:Wikialoft'),
  _photo('engine-seawater-cock.jpg', 'A ball-valve seacock with a red lever, and a hose held on by a clip, in a yacht’s bilge', 'A seacock in place: a ball valve on a hole through the hull, with the hose clipped to its tail. More in <a href="#engine--raw-water-intake">Engine</a>.', 'PHGCOM', 'CC BY-SA 3.0', 'http://creativecommons.org/licenses/by-sa/3.0/', 'https://commons.wikimedia.org/wiki/File:Sea_water_cock.JPG', 768, 576))}

</section>
'''
open(ROOT + 'sections/01-anatomy.html', 'w').write(page)

# sanity: duplicate keys, part terms without definitions
import re
keys = re.findall(r'<li data-term="([^"]+)"', page)
dups = sorted(set(k for k in keys if keys.count(k) > 1))
parts = set(t for m in re.findall(r'class="part" data-term="([^"]+)"', page) for t in m.split())
print('duplicate term keys:', dups)
print('part terms without definition:', sorted(parts - set(keys)))
print('terms without a part:', len(set(keys) - parts), 'of', len(keys))
