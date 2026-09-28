# Shared helpers for the section generators (extracted from gen_hull.py).
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
import re
ONE = '<span class="conf conf--one" title="Single source: found in only one place and not independently confirmed">¹</span>'
TWO = '<span class="conf conf--conflict" title="Sources disagree, or the figure is anecdotal (forum, owner report)">²</span>'
EST = '<span class="est" title="Estimate: no published figure was found, so this is a reasoned estimate">est.</span>'
TBC = '<span class="tbc" title="To be confirmed: not yet verified against a reliable source">TBC</span>'
HINT = '<span class="diagram__hint">Every labelled part is a link: hover it (or tap it on a phone) to read its definition under the drawing; click it, tap it again or use “Full entry” to jump to the full entry. In the term lists, a name with a small circle after it is on a drawing; click it to see where.</span>'

def figure(fid, short, viewbox, title, desc, body, caption, note='', wide=True, start=0):
    cls = 'diagram diagram--wide' if wide else 'diagram'
    return f'''  <figure class="{cls}" id="{fid}" data-short="{short}">
    <div class="diagram__scroll" data-start="{start}"><svg viewBox="{viewbox}" role="group" aria-labelledby="{fid}-title {fid}-desc">
      <title id="{fid}-title">{title}</title>
      <desc id="{fid}-desc">{desc}</desc>
{body}
    </svg></div>
    <figcaption><span class="caption">{caption}</span>{note}</figcaption>
  </figure>'''

HEADS = {
  'part':  ('How it works', 'Positives', 'Negatives', 'Common faults', 'What to check'),
  'fault': ('What happens', 'The good news', 'The bad news', 'Signs', 'What to do'),
}
def card(cid, name, aka, intro, how, pros, cons, faults, check, kind='part', fold=False):
    def ul(items): return '\n'.join(f'          <li>{i}</li>' for i in items)
    h = HEADS[kind]
    aka_html = f'\n      <span class="part-card__aka">{aka}</span>' if aka else ''
    extra = ' part-card--fault' if kind == 'fault' else ''
    if fold:
        tag, head_open, head_close, top = 'details', '<summary class="part-card__head">', '</summary>', f'<details class="part-card part-card--fold{extra}" id="{cid}" open>'
    else:
        tag, head_open, head_close, top = 'article', '<div class="part-card__head">', '</div>', f'<article class="part-card{extra}" id="{cid}">'
    return f'''  {top}
    {head_open}
      <h4>{name}</h4>{aka_html}
    {head_close}
    <div class="part-card__body">
      <p>{intro}</p>
    </div>
    <div class="part-grid">
      <div class="how"><h5>{h[0]}</h5><ul>
{ul(how)}
      </ul></div>
      <div class="pros"><h5>{h[1]}</h5><ul>
{ul(pros)}
      </ul></div>
      <div class="cons"><h5>{h[2]}</h5><ul>
{ul(cons)}
      </ul></div>
      <div class="faults"><h5>{h[3]}</h5><ul>
{ul(faults)}
      </ul></div>
      <div class="check"><h5>{h[4]}</h5><ul>
{ul(check)}
      </ul></div>
    </div>
  </{tag}>'''

def terms(rows):
    out = ['  <ul class="terms">']
    for key, name, body in rows:
        out.append(f'    <li data-term="{key}"><b>{name}</b> {body}</li>')
    out.append('  </ul>')
    return '\n'.join(out)

def sources(title, items):
    lis = '\n'.join(f'        <li>{i}</li>' for i in items)
    return f'''  <details class="more">
    <summary>Sources and confidence: {title}</summary>
    <div class="more__body">
      <ul>
{lis}
      </ul>
    </div>
  </details>'''

def a(url, text=None):
    return f'<a href="{url}" rel="noopener">{text or url.split("/")[2]}</a>'

def compare(caption, head, rows, wide=False, stack=False):
    import re as _re
    th = ''.join(f'<th scope="col">{h or "<span class=sr-only>Feature</span>"}</th>' for h in head)
    def dl(i):
        if not (stack and i < len(head) and head[i]): return ''
        t = _re.sub(r'<[^>]+>', '', head[i])
        for tok in ('{TBC}', '{ONE}', '{TWO}', '{EST}', '¹', '²'): t = t.replace(tok, '')
        return ' data-label="' + t.replace('"', '').strip() + '"'
    body = '\n'.join('        <tr><th scope="row">' + r[0] + '</th>' + ''.join(f'<td{dl(j+1)}>{c}</td>' for j, c in enumerate(r[1:])) + '</tr>' for r in rows)
    cls = 'spec compare' + (' compare--wide' if wide else '') + (' compare--stack' if stack else '')
    return f'''  <div class="table-wrap">
    <table class="{cls}">
      <caption>{caption}</caption>
      <thead><tr>{th}</tr></thead>
      <tbody>
{body}
      </tbody>
    </table>
  </div>'''


def video(vid, title, channel, why, pending=False):
    import html as _html
    title, channel = _html.escape(title, quote=False), _html.escape(channel, quote=False)
    cls = 'video-card is-pending' if pending else 'video-card'
    thumb = '' if pending else f'<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy">'
    return f'''  <div class="{cls}">
    <a class="video-card__thumb" href="https://www.youtube.com/watch?v={vid}" rel="noopener" tabindex="-1" aria-hidden="true">{thumb}</a>
    <div>
      <p class="video-card__title"><a href="https://www.youtube.com/watch?v={vid}" rel="noopener">{title}</a></p>
      <p class="video-card__channel">{channel}</p>
      <p class="video-card__why">{why}</p>
    </div>
  </div>'''

def photo(src, alt, caption, author, licence, licence_url, source_url, w, h, author_url=''):
    """A CC-licensed or public-domain photo stored under assets/img/, with the credit the licence asks for."""
    who = f'<a href="{author_url}" rel="noopener">{author}</a>' if author_url else author
    lic = f'<a href="{licence_url}" rel="noopener">{licence}</a>' if licence_url else licence
    host = 'Flickr' if 'flickr.com' in source_url else 'Wikimedia Commons'
    return (f'  <figure class="photo">\n'
            f'    <img src="assets/img/{src}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async">\n'
            f'    <figcaption>{caption} <span class="credit">Photo: {who}, {lic}, via <a href="{source_url}" rel="noopener">{host}</a>.</span></figcaption>\n'
            f'  </figure>')

def photos(*figs):
    """Two or more photos side by side."""
    return '  <div class="figure-row">\n' + '\n'.join('  ' + f.replace('\n', '\n  ') for f in figs) + '\n  </div>'

VIDEO_NOTE = ('Videos are linked, not embedded. Each was chosen by its title, channel and description, and its title and channel '
              'were confirmed with YouTube in September 2026; they were not watched in full from the editing session, so check that '
              'a video matches your boat before copying it, and where a video and this page disagree, follow the boat’s manual or your instructor.')

NUMBER_WORDS = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight'}

def videos(items, show=3, note=''):
    """A 'Worth watching' block: the shared note, the first `show` cards, the rest folded."""
    cards = [video(*i) for i in items]
    out = f'  <p>{VIDEO_NOTE}{(" " + note) if note else ""}</p>\n' + '\n'.join(cards[:show])
    rest = cards[show:]
    if rest:
        n = len(rest)
        out += (f'\n  <details class="more">\n    <summary>{NUMBER_WORDS[n]} more video{"s" if n > 1 else ""}</summary>\n'
                '    <div class="more__body">\n' + '\n'.join(rest) + '\n    </div>\n  </details>')
    return out

def finish(page, path, anatomy=ROOT + 'sections/01-anatomy.html', others=()):
    page = page.replace('{ONE}', ONE).replace('{TWO}', TWO).replace('{TBC}', TBC).replace('{EST}', EST)
    # keep a confidence mark on the same line as the word before it
    page = re.sub(r' (<span class="(?:conf|tbc)[ "])', r'&nbsp;\1', page)
    page = re.sub(r'(?<=[^\s>]) ([¹²])', r'&nbsp;\1', page)
    open(path, 'w').write(page)
    keys = re.findall(r'<li data-term="([^"]+)"', page)
    dups = sorted(set(k for k in keys if keys.count(k) > 1))
    parts = set(t for m in re.findall(r'class="part" data-term="([^"]+)"', page) for t in m.split())
    other_keys = set()
    for f in (anatomy,) + tuple(others):
        other_keys |= set(re.findall(r'<li data-term="([^"]+)"', open(f).read()))
    print('duplicate keys in section:', dups)
    print('keys clashing with other sections:', sorted(set(keys) & other_keys))
    print('part terms without a definition anywhere:', sorted(parts - set(keys) - other_keys))
    print('literal tokens left:', page.count('{ONE}') + page.count('{TWO}') + page.count('{TBC}') + page.count('{EST}'))
    ids = re.findall(r' id="([^"]+)"', page)
    print('duplicate ids:', sorted(set(i for i in ids if ids.count(i) > 1)))
