# Schematic maps for sections/12-seas.html. The land comes from coast_data.py (Natural Earth, public domain,
# built by make_coast.py); everything drawn on it is placed by latitude and longitude. Not for navigation.
import math
from coast_data import MAPS
from gen_hull_diagrams import part, marker

def _proj(name):
    w, s, e, n = MAPS[name]['extent']
    lat0 = math.radians((s + n) / 2)
    k = 900 / ((e - w) * math.cos(lat0))
    return lambda lat, lon: (round((lon - w) * math.cos(lat0) * k, 1), round((n - lat) * k, 1))

def _t(x, y, text, anchor='start', cls='dg-label small'):
    return f'<text class="{cls} dg-map-text" x="{x}" y="{y}" text-anchor="{anchor}">{text}</text>'

def draw(name, items, legend=('gate', 'area', 'wind', 'caution'), corner='bl'):
    """items: tuples, positions in degrees.
    ('port', lat, lon, label, anchor)            a harbour: small dot and name
    ('gate', lat, lon, label, anchor)            a tidal gate or race: red dot
    ('area', lat, lon, label, anchor)            a cruising area: italic name
    ('caution', lat, lon, label, anchor)         a warning: amber triangle
    ('wind', lat1, lon1, lat2, lon2, label, anchor)   a named wind, blowing from the first point to the second
    ('line', [(lat, lon), ...], label, anchor)   a route such as a canal, labelled at its middle
    ('sea', lat, lon, label)                     a sea name in muted capitals"""
    P = _proj(name)
    H = MAPS[name]['height']
    mid = f'map-{name}-arrow'
    out = [f'      <defs><marker id="{mid}" viewBox="0 0 10 10" refX="7" refY="5" markerUnits="userSpaceOnUse" markerWidth="15" markerHeight="15" orient="auto"><path d="M0,0 L10,5 L0,10 Z" style="fill: var(--dg-accent)"/></marker></defs>',
           f'      <rect class="dg-water" x="0" y="0" width="900" height="{H}"/>',
           f'      <path class="dg-land" d="{MAPS[name]["land"]}"/>']
    groups = {'port': [], 'gate': [], 'area': [], 'caution': [], 'wind': [], 'line': [], 'sea': []}
    def off(anchor):
        return {'start': 9, 'end': -9, 'middle': 0, 'below': 0, 'above': 0}[anchor]
    def dy(anchor):
        return {'below': 16, 'above': -10}.get(anchor, 4)
    def an(anchor):
        return 'middle' if anchor in ('below', 'above') else anchor
    for it in items:
        kind = it[0]
        if kind in ('port', 'gate', 'caution', 'area'):
            _, lat, lon, lab, anchor = it
            x, y = P(lat, lon)
            if kind == 'port':
                groups['port'].append(f'<circle cx="{x}" cy="{y}" r="3" fill="var(--dg-line)"/>' + _t(x + off(anchor), y + dy(anchor), lab, an(anchor)))
            elif kind == 'gate':
                groups['gate'].append(f'<circle class="dg-gate" cx="{x}" cy="{y}" r="6"/>' + _t(x + off(anchor) * 1.3, y + dy(anchor) * (1.2 if anchor in ('below', 'above') else 1), lab, an(anchor)))
            elif kind == 'caution':
                groups['caution'].append(f'<path class="dg-caution" d="M{x},{y - 8} L{x + 8},{y + 6} L{x - 8},{y + 6} Z"/>' + _t(x + off(anchor) * 1.4, y + 4, lab, anchor))
            else:
                groups['area'].append(_t(x, y, lab, anchor, 'dg-label dg-map-area'))
        elif kind == 'wind':
            _, la1, lo1, la2, lo2, lab, anchor = it
            (x1, y1), (x2, y2) = P(la1, lo1), P(la2, lo2)
            ly = y1 + (18 if anchor == 'below' else -6)
            groups['wind'].append(f'<line class="dg-map-wind" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" marker-end="url(#{mid})"/>'
                                  + _t(x1 + off(anchor), ly, lab, an(anchor), 'dg-label'))
        elif kind == 'line':
            _, pts, lab, anchor = it
            q = [P(a, b) for a, b in pts]
            d = 'M' + ' L'.join(f'{x},{y}' for x, y in q)
            x, y = q[len(q) // 2]
            groups['line'].append(f'<path d="{d}" fill="none" stroke="var(--dg-accent)" stroke-width="3" stroke-dasharray="6 4"/>' + _t(x + off(anchor), y - 8, lab, anchor))
        elif kind == 'sea':
            _, lat, lon, lab = it
            x, y = P(lat, lon)
            groups['sea'].append(f'<text class="dg-muted dg-map-text" x="{x}" y="{y}" text-anchor="middle" letter-spacing="2">{lab}</text>')
    out.append('      ' + ''.join(groups['sea']))
    out.append('      ' + ''.join(groups['line']))
    terms = {'gate': 'map-gate', 'area': 'map-area', 'wind': 'map-wind', 'caution': 'map-caution', 'port': 'map-port'}
    for kind in ('area', 'wind', 'port', 'gate', 'caution'):
        if groups[kind]:
            out.append(part(terms[kind], '        ' + '\n        '.join(groups[kind])))
    # legend, bottom left, on a panel
    rows = [k for k in legend if groups[k]]
    if rows:
        lh = 20 * len(rows) + 30
        y0 = H - lh - 10 if corner[0] == 'b' else 10
        x0 = 10 if corner[1] == 'l' else 900 - 188
        L = [f'<g transform="translate({x0 - 10},0)">', f'<rect x="10" y="{y0}" width="178" height="{lh}" rx="6" fill="var(--dg-halo)" stroke="var(--dg-lead)"/>',
             f'<text class="dg-label small" x="20" y="{y0 + 17}" font-weight="600">Schematic: not for navigation</text>']
        for i, k in enumerate(rows):
            yy = y0 + 36 + i * 20
            sym = {'gate': f'<circle class="dg-gate" cx="28" cy="{yy - 4}" r="6"/>',
                   'area': f'<text class="dg-label dg-map-area" x="20" y="{yy}">Aa</text>',
                   'wind': f'<line class="dg-map-wind" x1="18" y1="{yy - 4}" x2="38" y2="{yy - 4}" marker-end="url(#{mid})"/>',
                   'caution': f'<path class="dg-caution" d="M28,{yy - 12} L36,{yy + 2} L20,{yy + 2} Z"/>'}[k]
            txt = {'gate': 'tidal gate or race', 'area': 'cruising area', 'wind': 'named wind', 'caution': 'caution'}[k]
            L.append(sym + f'<text class="dg-label small" x="48" y="{yy}">{txt}</text>')
        L.append('</g>')
        out.append('      ' + ''.join(L))
    return '\n'.join(out)

def viewbox(name):
    return f'0 0 900 {MAPS[name]["height"]}'

# ---------------------------------------------------------------- the six seas
def channel():
    return draw('channel', [
        ('sea', 49.95, -1.2, 'ENGLISH CHANNEL'),
        ('area', 50.64, -1.20, 'Solent', 'middle'), ('area', 50.05, -4.45, 'West Country', 'middle'),
        ('area', 49.28, -2.95, 'Channel Islands', 'end'), ('area', 48.95, -3.35, 'North Brittany', 'middle'),
        ('port', 50.15, -5.07, 'Falmouth', 'end'), ('port', 50.37, -4.14, 'Plymouth', 'start'), ('port', 50.35, -3.58, 'Dartmouth', 'start'),
        ('port', 50.61, -2.45, 'Weymouth', 'end'), ('port', 50.71, -1.98, 'Poole', 'end'), ('port', 50.81, -0.10, 'Brighton', 'middle'),
        ('port', 51.12, 1.31, 'Dover', 'end'), ('port', 50.96, 1.85, 'Calais', 'start'), ('port', 49.93, 1.08, 'Dieppe', 'start'),
        ('port', 49.49, 0.11, 'Le Havre', 'start'), ('port', 49.65, -1.62, 'Cherbourg', 'below'), ('port', 49.46, -2.54, 'St Peter Port', 'end'),
        ('port', 48.65, -2.02, 'St Malo', 'start'), ('port', 48.72, -3.98, 'Roscoff', 'middle'),
        ('gate', 50.22, -3.64, 'Start Point', 'end'), ('gate', 50.515, -2.457, 'Portland Bill', 'end'), ('gate', 50.574, -2.058, 'St Alban’s Head', 'start'),
        ('gate', 49.72, -2.08, 'Alderney Race', 'end'), ('gate', 49.70, -1.25, 'Barfleur', 'start'), ('gate', 49.96, -5.20, 'the Lizard', 'end'),
        ('caution', 50.95, 1.30, 'Dover Strait: traffic separation scheme', 'end'),
    ], corner='br')

def north_sea():
    return draw('north-sea', [
        ('sea', 53.9, 3.0, 'NORTH SEA'),
        ('area', 53.62, 6.4, 'Wadden Sea', 'middle'), ('area', 52.72, 5.35, 'IJsselmeer', 'middle'), ('area', 51.62, 3.95, 'Zeeland', 'start'),
        ('port', 51.33, 1.42, 'Ramsgate', 'end'), ('port', 52.47, 1.75, 'Lowestoft', 'end'), ('port', 51.23, 2.92, 'Ostend', 'start'),
        ('port', 52.46, 4.58, 'IJmuiden', 'end'), ('port', 52.96, 4.76, 'Den Helder', 'end'), ('port', 53.17, 5.41, 'Harlingen', 'start'),
        ('port', 53.33, 6.93, 'Delfzijl', 'start'), ('port', 54.18, 7.89, 'Helgoland', 'end'), ('port', 53.87, 8.70, 'Cuxhaven', 'end'),
        ('port', 55.47, 8.45, 'Esbjerg', 'end'), ('port', 54.32, 10.14, 'Kiel', 'end'),
        ('line', [(53.89, 9.14), (54.07, 9.40), (54.30, 9.67), (54.37, 10.14)], 'Kiel Canal', 'end'),
        ('caution', 51.62, 1.25, 'shifting banks', 'start'), ('caution', 51.38, 2.45, 'banks', 'end'),
    ], legend=('area', 'caution'), corner='tl')

def baltic():
    return draw('baltic', [
        ('sea', 56.4, 18.2, 'BALTIC SEA'),
        ('area', 54.55, 11.0, 'Danish South Sea', 'middle'), ('area', 59.55, 19.25, 'Stockholm archipelago', 'end'),
        ('area', 60.42, 20.1, 'Åland', 'middle'), ('area', 59.92, 21.9, 'Archipelago Sea', 'middle'),
        ('port', 54.32, 10.14, 'Kiel', 'end'), ('port', 55.68, 12.57, 'Copenhagen', 'start'), ('port', 54.18, 12.08, 'Warnemünde', 'start'),
        ('port', 56.16, 15.59, 'Karlskrona', 'start'), ('port', 57.64, 18.29, 'Visby', 'end'), ('port', 59.33, 18.07, 'Stockholm', 'end'),
        ('port', 60.10, 19.94, 'Mariehamn', 'end'), ('port', 60.45, 22.27, 'Turku', 'start'), ('port', 60.17, 24.94, 'Helsinki', 'start'),
        ('port', 59.44, 24.75, 'Tallinn', 'end'), ('port', 54.35, 18.65, 'Gdańsk', 'end'),
        ('caution', 55.15, 19.6, 'GPS jamming reported', 'start'), ('caution', 54.72, 21.2, 'Russian waters: stay out', 'start'),
        ('caution', 59.95, 27.9, 'Russian waters', 'end'),
    ], legend=('area', 'caution'), corner='br')

def med():
    return draw('med', [
        ('sea', 37.6, 6.0, 'MEDITERRANEAN'),
        ('area', 39.05, 2.9, 'Balearics', 'middle'), ('area', 43.2, 7.9, 'Côte d’Azur', 'start'), ('area', 39.7, 7.9, 'Corsica and Sardinia', 'end'),
        ('area', 38.3, 19.35, 'Ionian', 'end'), ('area', 37.0, 25.9, 'Cyclades', 'start'), ('area', 36.15, 27.6, 'Dodecanese', 'end'),
        ('area', 43.5, 15.5, 'Adriatic: its own map', 'middle'),
        ('wind', 44.2, 4.75, 42.4, 5.7, 'mistral', 'end'), ('wind', 42.9, 2.3, 41.9, 4.0, 'tramontane', 'end'),
        ('wind', 40.3, 25.0, 38.0, 25.2, 'meltemi', 'start'), ('wind', 35.0, 15.6, 36.8, 13.4, 'sirocco', 'start'),
        ('wind', 37.6, 17.4, 36.3, 15.4, 'gregale', 'start'), ('wind', 41.2, 6.9, 42.35, 8.35, 'libeccio', 'below'),
    ], legend=('area', 'wind'))

def adriatic():
    return draw('adriatic', [
        ('sea', 42.6, 16.0, 'ADRIATIC'),
        ('area', 45.05, 13.25, 'Istria', 'end'), ('area', 45.02, 14.28, 'Kvarner', 'middle'), ('area', 43.75, 15.05, 'Kornati', 'end'),
        ('area', 43.05, 16.35, 'Central Dalmatia', 'end'), ('area', 42.55, 17.7, 'Dubrovnik', 'end'), ('area', 42.3, 18.75, 'Kotor', 'start'),
        ('port', 45.65, 13.77, 'Trieste', 'start'), ('port', 45.43, 12.33, 'Venice', 'start'), ('port', 44.87, 13.85, 'Pula', 'end'),
        ('port', 45.33, 14.44, 'Rijeka', 'start'), ('port', 44.12, 15.23, 'Zadar', 'start'), ('port', 43.51, 16.44, 'Split', 'start'),
        ('port', 42.65, 18.09, 'Dubrovnik', 'start'), ('port', 43.62, 13.51, 'Ancona', 'end'), ('port', 41.13, 16.87, 'Bari', 'end'),
        ('wind', 45.12, 15.3, 44.82, 14.92, 'bora: fiercest under the Velebit, at Senj', 'start'),
        ('wind', 45.8, 14.3, 45.58, 13.82, 'bora at Trieste', 'below'),
        ('wind', 41.35, 19.0, 42.55, 16.9, 'jugo', 'start'),
        ('wind', 44.3, 13.9, 43.6, 15.2, 'maestral (summer afternoons)', 'below'),
    ], legend=('area', 'wind'))

def black_sea():
    return draw('black-sea', [
        ('sea', 43.3, 34.0, 'BLACK SEA'),
        ('port', 43.40, 28.17, 'Balchik', 'start'), ('port', 43.20, 27.92, 'Varna', 'start'), ('port', 42.66, 27.73, 'Nesebar', 'start'),
        ('port', 42.50, 27.47, 'Burgas', 'end'), ('port', 42.42, 27.70, 'Sozopol', 'start'), ('port', 44.17, 28.65, 'Constanța', 'start'),
        ('port', 43.80, 28.58, 'Mangalia', 'start'), ('port', 41.01, 28.98, 'Istanbul and the Bosphorus', 'start'),
        ('caution', 44.0, 30.6, 'drifting mines reported since 2022', 'start'), ('caution', 45.9, 31.4, 'Ukraine: war zone, keep clear', 'start'),
        ('wind', 44.9, 32.6, 43.6, 31.0, 'north-easterlies, autumn and winter', 'start'),
    ], legend=('wind', 'caution'), corner='br')
