# Build standalone test pages for one section: python3 mktest.py 06-engine engine
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
import re, sys
S = os.environ.get('PREVIEW_DIR', os.path.join(ROOT, '.preview'))
os.makedirs(os.path.join(S, 'test'), exist_ok=True)
os.makedirs(os.path.join(S, 'shots'), exist_ok=True)
fn, sid = sys.argv[1], sys.argv[2]
src = open(f'{ROOT}sections/{fn}.html').read()
def wrap(body, theme):
    return ("<!DOCTYPE html><html lang=en data-theme=%s><head><meta charset=utf-8><meta name=viewport content='width=device-width'>"
            "<link rel=stylesheet href='http://localhost:8123/assets/css/site.css'></head><body><div class=layout style='grid-template-columns:1fr'>"
            "<main class=content id=content><section class=topic>%s</section></main></div></body></html>") % (theme, body)
for t in ('light', 'dark'):
    open(f'{S}/test/{sid}-{t}.html', 'w').write(wrap(src, t))
figs = re.findall(r'(  <figure class="diagram[^"]*" id="([^"]+)".*?</figure>)', src, re.S)
for body, fid in figs:
    for t in ('light', 'dark'):
        open(f'{S}/test/{fid}-{t}.html', 'w').write(wrap(body, t))
print('figures:', [f for _, f in figs])
