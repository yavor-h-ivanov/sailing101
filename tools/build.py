# Rebuilds everything generated in the repository, then writes a single-file preview shell.
#   python3 tools/build.py            regenerate all sections, print pages, glossary and image credits
#   python3 tools/build.py --preview  the same, then write .preview/artifact/index.html: index.html with
#                                     the stylesheet and script inlined, for hosts that serve the page and
#                                     the section fragments but not the assets folder as linked files
# Standard library only. Stops at the first generator that fails.
import os, re, subprocess, sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)

# Section generators in page order; 02-fleet.html is hand-written. The glossary reads every section,
# and the image credits read every photo, so they run last.
ORDER = ['start', 'anatomy', 'hull', 'rig', 'deck', 'engine', 'systems', 'electronics', 'sailing',
         'manoeuvres', 'navigation', 'seas', 'licences', 'buying', 'print', 'glossary', 'image_credits']


def run(name):
    script = os.path.join(TOOLS, f'gen_{name}.py')
    r = subprocess.run([sys.executable, script], cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stdout + r.stderr)
        sys.exit(f'gen_{name}.py failed')
    bad = [l for l in r.stdout.splitlines()
           if re.search(r'literal tokens left: [1-9]|duplicate ids: \[.+\]|dup ids: [1-9]', l)]
    if bad:
        sys.exit(f'gen_{name}.py: ' + '; '.join(bad))
    print(f'  gen_{name}.py ok')


def preview():
    page = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    css = open(os.path.join(ROOT, 'assets/css/site.css'), encoding='utf-8').read()
    js = open(os.path.join(ROOT, 'assets/js/site.js'), encoding='utf-8').read()
    link = '<link rel="stylesheet" href="assets/css/site.css">'
    script = '<script src="assets/js/site.js"></script>'
    assert page.count(link) == 1 and page.count(script) == 1, 'index.html asset tags changed'
    page = page.replace(link, '<style>\n' + css + '\n</style>')
    page = page.replace(script, '<script>\n' + js.replace('</script', '<\\/script') + '\n</script>')
    page = re.sub(r'<title>.*?</title>', '<title>Sailing 101</title>', page, count=1, flags=re.S)
    out = os.path.join(ROOT, '.preview', 'artifact')
    os.makedirs(out, exist_ok=True)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(page)
    print(f'  preview shell: .preview/artifact/index.html ({len(page) // 1024} KB)')


if __name__ == '__main__':
    for n in ORDER:
        run(n)
    if '--preview' in sys.argv:
        preview()
