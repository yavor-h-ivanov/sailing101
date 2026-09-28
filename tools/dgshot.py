# python3 dgshot.py module func viewbox [theme] [width]: render one diagram function to shots/dg-func-theme.png
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
import sys, subprocess, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
S = os.environ.get('PREVIEW_DIR', os.path.join(ROOT, '.preview'))
os.makedirs(os.path.join(S, 'test'), exist_ok=True)
os.makedirs(os.path.join(S, 'shots'), exist_ok=True)
mod, fn, vb = sys.argv[1:4]
theme = sys.argv[4] if len(sys.argv) > 4 else 'light'
w = sys.argv[5] if len(sys.argv) > 5 else '1000'
m = importlib.import_module(mod)
body = getattr(m, fn)()
_, _, vw, vh = vb.split()
h = int(int(w) * int(vh) / int(vw)) + 120
html = ("<!DOCTYPE html><html lang=en data-theme=%s><head><meta charset=utf-8><link rel=stylesheet href='http://localhost:8123/assets/css/site.css'></head>"
        "<body><main class=content><figure class='diagram diagram--wide'><div class=diagram__scroll><svg viewBox='%s'>%s</svg></div></figure></main></body></html>") % (theme, vb, body)
open(f'{S}/test/dg-{fn}-{theme}.html', 'w').write(html)
BIN = '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell'
out = f'{S}/shots/dg-{fn}-{theme}.png'
subprocess.run(['timeout', '60', BIN, '--headless=new', '--no-sandbox', '--disable-gpu', '--hide-scrollbars', f'--window-size={w},{h}', '--virtual-time-budget=1500', f'--screenshot={out}', f'http://localhost:8124/dg-{fn}-{theme}.html'], capture_output=True)
print(out)
