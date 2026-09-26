/* Sailing 101 — site script. Plain ES2017, no dependencies. */
(function () {
  'use strict';

  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  var content = $('#content');
  var tocEl = $('#toc');
  var loading = $('#loading');

  /* ------------------------------------------------------------------ theme */
  (function theme() {
    var btn = $('#theme-toggle');
    var media = window.matchMedia('(prefers-color-scheme: dark)');
    function current() {
      var t = document.documentElement.getAttribute('data-theme');
      if (t) return t;
      return media.matches ? 'dark' : 'light';
    }
    btn.addEventListener('click', function () {
      var next = current() === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      try { localStorage.setItem('s101-theme', next); } catch (e) {}
    });
  })();

  /* ------------------------------------------------------------ mobile menu */
  (function menu() {
    var sidebar = $('#sidebar'), scrim = $('#scrim'), open = $('#menu-toggle'), close = $('#menu-close');
    function set(state) {
      sidebar.classList.toggle('is-open', state);
      scrim.hidden = !state;
      open.setAttribute('aria-expanded', String(state));
    }
    open.addEventListener('click', function () { set(true); });
    close.addEventListener('click', function () { set(false); });
    scrim.addEventListener('click', function () { set(false); });
    tocEl.addEventListener('click', function (e) {
      if (e.target.closest('a') && window.matchMedia('(max-width: 960px)').matches) set(false);
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
  })();

  /* ---------------------------------------------------------------- helpers */
  function slugify(text) {
    return text.toLowerCase().normalize('NFKD').replace(/[̀-ͯ]/g, '')
      .replace(/['’]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 60);
  }
  function el(tag, attrs, children) {
    var n = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === 'text') n.textContent = attrs[k];
      else if (k === 'html') n.innerHTML = attrs[k];
      else n.setAttribute(k, attrs[k]);
    });
    (children || []).forEach(function (c) { n.appendChild(c); });
    return n;
  }
  function escapeHtml(s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  /* ------------------------------------------------------------ load sections */
  function loadSections() {
    return fetch('sections/sections.json', { cache: 'no-cache' })
      .then(function (r) { if (!r.ok) throw new Error('manifest ' + r.status); return r.json(); })
      .then(function (manifest) {
        return Promise.all(manifest.sections.map(function (s) {
          return fetch('sections/' + s.file, { cache: 'no-cache' }).then(function (r) {
            if (!r.ok) throw new Error(s.file + ' ' + r.status);
            return r.text();
          }).then(function (html) { return { meta: s, html: html }; });
        }));
      });
  }

  function inject(parts) {
    var frag = document.createDocumentFragment();
    parts.forEach(function (p, i) {
      var tpl = document.createElement('template');
      tpl.innerHTML = p.html.trim();
      var section = tpl.content.querySelector('section');
      if (!section) return;
      section.id = p.meta.id;
      section.classList.add('topic');
      section.dataset.status = p.meta.status || 'skeleton';
      section.dataset.index = String(i);
      // kicker with number and status badge
      var h2 = section.querySelector('h2');
      if (h2 && !section.querySelector('.kicker')) {
        var kicker = el('p', { 'class': 'kicker' });
        kicker.appendChild(el('span', { text: 'Section ' + i }));
        kicker.appendChild(el('span', { 'class': 'badge badge--' + section.dataset.status, text: section.dataset.status }));
        h2.parentNode.insertBefore(kicker, h2);
      }
      frag.appendChild(section);
    });
    loading.remove();
    content.appendChild(frag);
  }

  /* ----------------------------------------------------- ids, anchors, toc */
  function buildHeadings() {
    $$('.topic').forEach(function (section) {
      var used = {};
      $$('h3, h4', section).forEach(function (h) {
        var card = h.closest('.part-card');
        if (!h.id && card && card.id) { h.dataset.anchorId = card.id; return; }
        if (!h.id) {
          var base = section.id + '--' + slugify(h.textContent);
          var id = base, n = 2;
          while (used[id] || document.getElementById(id)) id = base + '-' + (n++);
          used[id] = true;
          h.id = id;
        }
      });
      $$('h2, h3, h4', section).forEach(function (h) {
        var id = h.dataset.anchorId || h.id || section.id;
        var a = el('a', { 'class': 'anchor', href: '#' + id, 'aria-label': 'Link to this heading', text: '#' });
        if (h.closest('summary')) a.addEventListener('click', function (e) { e.preventDefault(); history.replaceState(null, '', '#' + id); });
        a.addEventListener('click', function (e) {
          if (!navigator.clipboard) return;
          e.preventDefault();
          var url = location.origin + location.pathname + '#' + id;
          history.replaceState(null, '', '#' + id);
          navigator.clipboard.writeText(url).then(function () {
            a.classList.add('is-copied');
            setTimeout(function () { a.classList.remove('is-copied'); }, 1200);
          }).catch(function () {});
        });
        h.appendChild(a);
      });
    });
  }

  function buildToc() {
    var caretSvg = '<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true"><path d="m9 6 6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';
    $$('.topic').forEach(function (section, i) {
      var title = section.querySelector('h2');
      var li = el('li');
      var row = el('div', { 'class': 'toc__row' });
      var link = el('a', { href: '#' + section.id, 'data-target': section.id });
      link.appendChild(el('i', { 'class': 'status status--' + section.dataset.status, title: section.dataset.status }));
      link.appendChild(el('span', { 'class': 'toc__num', text: String(i) }));
      link.appendChild(el('span', { text: title ? title.firstChild.textContent.trim() : section.id }));
      row.appendChild(link);
      var subs = $$('h3', section);
      if (subs.length) {
        var caret = el('button', { 'class': 'toc__caret', 'aria-label': 'Toggle subsections', html: caretSvg });
        caret.addEventListener('click', function () { li.classList.toggle('is-open'); });
        row.appendChild(caret);
        var ol = el('ol');
        subs.forEach(function (h) {
          var a = el('a', { href: '#' + h.id, 'data-target': h.id, text: h.firstChild.textContent.trim() });
          ol.appendChild(el('li', null, [a]));
        });
        li.appendChild(row); li.appendChild(ol);
      } else {
        li.appendChild(row);
      }
      tocEl.appendChild(li);
    });
  }

  /* ---------------------------------------------------------- scroll spy */
  function scrollSpy() {
    var links = {};
    $$('a[data-target]', tocEl).forEach(function (a) { links[a.dataset.target] = a; });
    var headings = $$('.topic > h2, .topic h3').map(function (h) {
      return h.tagName === 'H2' ? h.closest('.topic') : h;
    });
    var activeSection = null, activeSub = null;
    function setActive(sectionId, subId) {
      if (sectionId !== activeSection) {
        if (activeSection && links[activeSection]) {
          links[activeSection].classList.remove('is-active');
          links[activeSection].closest('li').classList.remove('is-open');
        }
        activeSection = sectionId;
        if (links[sectionId]) {
          links[sectionId].classList.add('is-active');
          links[sectionId].closest('li').classList.add('is-open');
          scrollTocTo(links[sectionId]);
        }
      }
      if (subId !== activeSub) {
        if (activeSub && links[activeSub]) links[activeSub].classList.remove('is-active');
        activeSub = subId;
        if (subId && links[subId]) { links[subId].classList.add('is-active'); scrollTocTo(links[subId]); }
      }
    }
    function scrollTocTo(a) {
      var sb = $('#sidebar');
      var r = a.getBoundingClientRect(), s = sb.getBoundingClientRect();
      if (r.top < s.top + 60 || r.bottom > s.bottom - 60) {
        sb.scrollTo({ top: a.offsetTop - sb.clientHeight / 2, behavior: 'smooth' });
      }
    }
    var ticking = false;
    function update() {
      ticking = false;
      var offset = 56 + 24; // topbar + margin
      var probe = offset + 1;
      var sectionId = null, subId = null;
      for (var i = 0; i < headings.length; i++) {
        var h = headings[i];
        var top = h.getBoundingClientRect().top;
        if (top - probe <= 0) {
          if (h.classList.contains('topic')) { sectionId = h.id; subId = null; }
          else { subId = h.id; sectionId = h.closest('.topic').id; }
        } else break;
      }
      // if the section's own h3 that follows is below the fold, keep parent only
      if (!sectionId && headings.length) sectionId = headings[0].id;
      setActive(sectionId, subId);
      // progress
      var doc = document.documentElement;
      var max = doc.scrollHeight - window.innerHeight;
      $('#progress').style.width = (max > 0 ? (window.scrollY / max) * 100 : 0) + '%';
      $('#totop').hidden = window.scrollY < 600;
    }
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    window.addEventListener('resize', update);
    update();
  }

  /* -------------------------------------------------------------- search */
  function search() {
    var input = $('#search-input'), results = $('#search-results');
    var index = [];
    $$('.topic').forEach(function (section) {
      var sectionTitle = section.querySelector('h2').firstChild.textContent.trim();
      var crumbHeading = sectionTitle, crumbId = section.id;
      var nodes = $$('h2, h3, h4, p, li, dt, dd, figcaption, th, td, summary', section);
      nodes.forEach(function (n) {
        if (n.closest('.kicker') || n.closest('.planned') && n.tagName !== 'LI') return;
        var text = n.textContent.replace(/\s+/g, ' ').replace(/#$/, '').trim();
        if (!text || text.length < 3) return;
        if (/^H[234]$/.test(n.tagName)) {
          crumbHeading = text; crumbId = n.id || section.id;
          index.push({ type: 'heading', title: text, text: text, crumb: sectionTitle, id: crumbId, weight: n.tagName === 'H2' ? 5 : 3 });
        } else {
          var anchor = n.closest('h2, h3, h4') || n.closest('[id]');
          index.push({ type: 'text', title: crumbHeading, text: text, crumb: sectionTitle, id: (anchor && anchor.id) || crumbId, weight: n.tagName === 'DT' ? 3 : 1 });
        }
      });
    });

    var selected = -1, items = [];
    function tokens(q) { return q.toLowerCase().split(/\s+/).filter(Boolean); }
    function score(entry, toks) {
      var hay = (entry.title + ' ' + entry.text).toLowerCase();
      var s = 0;
      for (var i = 0; i < toks.length; i++) {
        var t = toks[i], pos = hay.indexOf(t);
        if (pos < 0) return 0;
        s += entry.weight;
        if (entry.title.toLowerCase().indexOf(t) >= 0) s += 2;
        if (new RegExp('\\b' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).test(hay)) s += 1;
      }
      return s;
    }
    function highlight(text, toks) {
      var out = escapeHtml(text);
      toks.forEach(function (t) {
        out = out.replace(new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<mark>$1</mark>');
      });
      return out;
    }
    function snippet(text, toks) {
      var lower = text.toLowerCase(), pos = -1;
      for (var i = 0; i < toks.length && pos < 0; i++) pos = lower.indexOf(toks[i]);
      var start = Math.max(0, pos - 50);
      var s = (start > 0 ? '…' : '') + text.slice(start, start + 140) + (start + 140 < text.length ? '…' : '');
      return s;
    }
    function render(q) {
      var toks = tokens(q);
      results.innerHTML = ''; items = []; selected = -1;
      if (!toks.length) { results.hidden = true; input.setAttribute('aria-expanded', 'false'); return; }
      var scored = [], seen = {};
      index.forEach(function (e) {
        var s = score(e, toks);
        if (s > 0) {
          var key = e.id + '|' + e.text.slice(0, 80);
          if (seen[key]) return; seen[key] = true;
          scored.push({ e: e, s: s });
        }
      });
      scored.sort(function (a, b) { return b.s - a.s; });
      scored.slice(0, 14).forEach(function (r) {
        var a = el('a', { 'class': 'search__item', href: '#' + r.e.id, role: 'option' });
        a.innerHTML = '<span class="search__crumb">' + escapeHtml(r.e.crumb) + '</span>' +
          '<span class="search__title">' + highlight(r.e.title, toks) + '</span>' +
          (r.e.type === 'text' ? '<span class="search__snip">' + highlight(snippet(r.e.text, toks), toks) + '</span>' : '');
        a.addEventListener('click', function () { close(); });
        results.appendChild(a); items.push(a);
      });
      if (!items.length) results.appendChild(el('div', { 'class': 'search__empty', text: 'No matches for “' + q + '”.' }));
      results.hidden = false; input.setAttribute('aria-expanded', 'true');
    }
    function close() { results.hidden = true; input.setAttribute('aria-expanded', 'false'); }
    function select(i) {
      if (!items.length) return;
      if (selected >= 0) items[selected].removeAttribute('aria-selected');
      selected = (i + items.length) % items.length;
      items[selected].setAttribute('aria-selected', 'true');
      items[selected].scrollIntoView({ block: 'nearest' });
    }
    input.addEventListener('input', function () { render(input.value.trim()); });
    input.addEventListener('focus', function () { if (input.value.trim()) render(input.value.trim()); });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); select(selected + 1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); select(selected - 1); }
      else if (e.key === 'Enter') { if (selected >= 0) { items[selected].click(); } else if (items[0]) { items[0].click(); } }
      else if (e.key === 'Escape') { close(); input.blur(); }
    });
    document.addEventListener('click', function (e) { if (!e.target.closest('#search')) close(); });
    document.addEventListener('keydown', function (e) {
      if (e.key === '/' && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)) { e.preventDefault(); input.focus(); input.select(); }
    });
  }


  /* --------------------------------------------- diagram <-> term links */
  function partLinks() {
    var partsByTerm = {};
    $$('figure.diagram .part[data-term]').forEach(function (p) {
      p.dataset.term.split(/\s+/).forEach(function (t) { (partsByTerm[t] = partsByTerm[t] || []).push(p); });
      var isSvg = typeof SVGElement !== 'undefined' && p instanceof SVGElement;
      if (isSvg) {
        if (!p.hasAttribute('tabindex')) p.setAttribute('tabindex', '0');
        if (!p.hasAttribute('role')) p.setAttribute('role', 'link');
      }
    });
    var termsByKey = {}, defByKey = {};
    $$('.terms li[data-term]').forEach(function (li) {
      var key = li.dataset.term;
      if (termsByKey[key]) { console.warn('duplicate term key', key); return; }
      if (!li.id) li.id = 'term-' + key;
      if (!li.hasAttribute('tabindex')) li.setAttribute('tabindex', '-1');
      termsByKey[key] = li;
      var b = li.querySelector('b');
      defByKey[key] = { name: b ? b.textContent.trim() : key, text: li.textContent.replace(b ? b.textContent : '', '').trim() };
    });
    // a definition strip under every drawing that has linked parts
    function tipFor(fig) {
      if (fig._tip) return fig._tip;
      var tip = el('p', { 'class': 'diagram__tip', 'aria-live': 'polite' });
      tip.appendChild(el('span', { 'class': 'diagram__tip-empty', text: 'Hover or tap a labelled part to read its definition here.' }));
      var scroll = fig.querySelector('.diagram__scroll');
      if (scroll && scroll.nextSibling) fig.insertBefore(tip, scroll.nextSibling); else fig.appendChild(tip);
      fig._tip = tip;
      return tip;
    }
    function jumpTo(li, siblings) {
      history.replaceState(null, '', '#' + li.id);
      li.scrollIntoView({ block: 'center' });
      flash(siblings, [li]);
      li.focus({ preventScroll: true });
    }
    function showTip(fig, key, siblings) {
      var tip = tipFor(fig), d = defByKey[key];
      tip.innerHTML = '';
      fig._tipKey = key || null;
      if (!d) { tip.appendChild(el('span', { 'class': 'diagram__tip-empty', text: 'Hover or tap a labelled part to read its definition here.' })); return; }
      tip.appendChild(el('b', { text: d.name }));
      tip.appendChild(el('span', { text: ' ' + d.text + ' ' }));
      var more = el('a', { 'class': 'diagram__tip-more', href: '#' + termsByKey[key].id, text: 'Full entry \u2192' });
      more.addEventListener('click', function (e) { e.preventDefault(); jumpTo(termsByKey[key], siblings || []); });
      tip.appendChild(more);
    }
    var coarse = window.matchMedia ? window.matchMedia('(pointer: coarse)') : { matches: false };
    function clearTip(fig) { showTip(fig, null); }
    function resetTapped(fig) {
      if (!fig._tapped) return;
      var p = fig._tapped; fig._tapped = null;
      p.dispatchEvent(new Event('mouseleave'));
    }
    var flashTimer = null, targets = [];
    function lit(nodes, on) { nodes.forEach(function (n) { n.classList.toggle('is-lit', on); }); }
    function clearTargets() { targets.forEach(function (n) { n.classList.remove('is-target'); }); targets = []; }
    function flash(nodes, keep) {
      if (flashTimer) clearTimeout(flashTimer);
      $$('.is-flash').forEach(function (n) { n.classList.remove('is-flash'); });
      clearTargets();
      nodes.forEach(function (n) { n.classList.add('is-flash'); });
      (keep || []).forEach(function (n) { n.classList.add('is-target'); targets.push(n); });
      flashTimer = setTimeout(function () { nodes.forEach(function (n) { n.classList.remove('is-flash'); }); flashTimer = null; }, 2600);
    }
    document.addEventListener('pointerdown', function (e) {
      if (targets.length && !e.target.closest('.is-target')) clearTargets();
      $$('figure.diagram').forEach(function (f) {
        if (f._tapped && !e.target.closest('.part') && !e.target.closest('.diagram__tip')) { resetTapped(f); $$('.is-lit', f).forEach(function (n) { n.classList.remove('is-lit'); }); clearTip(f); }
      });
    });
    function figureOf(p) { return p.closest('figure'); }
    function nearest(nodes, ref) {
      var svgOnly = nodes.filter(function (n) { return typeof SVGElement !== 'undefined' && n instanceof SVGElement; });
      if (svgOnly.length) nodes = svgOnly;
      var ry = ref.getBoundingClientRect().top, best = null, bd = Infinity;
      nodes.forEach(function (n) {
        var d = Math.abs(n.getBoundingClientRect().top - ry);
        if (d < bd) { bd = d; best = n; }
      });
      return best;
    }
    function showPart(target, all, li) {
      try { target.scrollIntoView({ block: 'center', inline: 'center' }); } catch (e) { figureOf(target).scrollIntoView({ block: 'center' }); }
      flash(all.concat(li ? [li] : []), [target]);
      target.focus({ preventScroll: true });
    }
    // term -> part
    Object.keys(termsByKey).forEach(function (key) {
      var li = termsByKey[key], parts = partsByTerm[key];
      var nameEl = li.querySelector('b');
      if (!parts || !nameEl) return;
      li.classList.add('has-part');
      var btn = el('button', { 'class': 'term__name', type: 'button', text: nameEl.textContent.trim(), title: 'Show on the nearest diagram' });
      nameEl.textContent = ''; nameEl.appendChild(btn);
      var figs = []; parts.forEach(function (p) { var f = figureOf(p); if (figs.indexOf(f) < 0) figs.push(f); });
      var layoutFigs = figs.filter(function (f) { return f.classList.contains('diagram--layout'); });
      var listed = figs.filter(function (f) { return !f.classList.contains('diagram--layout'); });
      if (layoutFigs.length) listed.push(layoutFigs);
      var where = el('span', { 'class': 'term__where' });
      where.appendChild(el('span', { text: 'Shown on: ' }));
      listed.forEach(function (f, i) {
        var group = Array.isArray(f) ? f : null;
        var first = group ? group[0] : f;
        var text = group ? (group.length > 1 ? 'layouts ' + group[0].dataset.short.replace('layout ', '') + '\u2013' + group[group.length - 1].dataset.short.replace('layout ', '') : group[0].dataset.short) : (f.dataset.short || 'diagram');
        var a = el('a', { href: '#' + first.id, text: text });
        a.addEventListener('click', function (e) {
          e.preventDefault();
          var candidates = parts.filter(function (p) { return group ? group.indexOf(figureOf(p)) >= 0 : figureOf(p) === f; });
          showPart(group ? nearest(candidates, li) : candidates[0], parts, li);
        });
        if (i) where.appendChild(el('span', { text: ', ' }));
        where.appendChild(a);
      });
      li.appendChild(where);
      btn.addEventListener('click', function () { showPart(nearest(parts, li), parts, li); });
      li.addEventListener('mouseenter', function () { lit(parts, true); });
      li.addEventListener('mouseleave', function () { lit(parts, false); });
    });
    // part -> term
    $$('figure.diagram .part[data-term]').forEach(function (p) {
      var keys = p.dataset.term.split(/\s+/);
      var li = null;
      for (var i = 0; i < keys.length && !li; i++) li = termsByKey[keys[i]];
      var siblings = []; keys.forEach(function (k) { (partsByTerm[k] || []).forEach(function (q) { if (siblings.indexOf(q) < 0) siblings.push(q); }); });
      var liKey = null;
      for (var j = 0; j < keys.length && !liKey; j++) if (termsByKey[keys[j]]) liKey = keys[j];
      var fig = figureOf(p);
      function go(e) {
        e.preventDefault();
        if (!li) return;
        // on a touch screen the first tap shows the definition strip; a second tap on the same part jumps
        if (fig && e.type === 'click' && coarse.matches && fig._tapped !== p) {
          resetTapped(fig); $$('.is-lit', fig).forEach(function (n) { n.classList.remove('is-lit'); });
          fig._tapped = p; showTip(fig, liKey, siblings); lit(siblings, true); return;
        }
        if (fig) fig._tapped = null;
        jumpTo(li, siblings);
      }
      p.addEventListener('click', go);
      p.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') go(e); });
      if (li) {
        var btn2 = p.querySelector('button.callouts__text');
        var name = defByKey[liKey].name;
        if (btn2) btn2.setAttribute('aria-label', name + ', see definition');
        else p.setAttribute('aria-label', name + ', see definition');
        if (fig) tipFor(fig);
        function on() { li.classList.add('is-lit'); lit(siblings, true); if (fig) showTip(fig, liKey, siblings); }
        function off() { if (fig && fig._tapped === p) return; li.classList.remove('is-lit'); lit(siblings, false); }
        p.addEventListener('mouseenter', on);
        p.addEventListener('mouseleave', off);
        p.addEventListener('focus', on);
        p.addEventListener('blur', off);
      }
    });
  }

  /* ------------------------------------ initial scroll of wide diagrams */
  function diagramStart() {
    function apply(initial) {
      $$('.diagram__scroll').forEach(function (w) {
        var overflow = w.scrollWidth > w.clientWidth + 2;
        w.classList.toggle('has-scroll', overflow);
        if (initial && overflow && w.dataset.start) w.scrollLeft = (w.scrollWidth - w.clientWidth) * (parseFloat(w.dataset.start) || 0);
      });
    }
    apply(true); window.addEventListener('resize', function () { apply(false); });
  }

  /* ----------------------------------------------- table overflow cue */
  function tableCues() {
    function check() {
      $$('.table-wrap').forEach(function (w) { w.classList.toggle('has-scroll', w.scrollWidth > w.clientWidth + 2); });
    }
    check(); window.addEventListener('resize', check);
  }

  /* --------------------------------------------------------- deep links */
  function jumpToHash() {
    if (!location.hash) return;
    var id = decodeURIComponent(location.hash.slice(1));
    var target = document.getElementById(id);
    if (target) target.scrollIntoView({ block: 'start' });
  }

  /* ------------------------------------------------------------------ init */
  loadSections().then(function (parts) {
    inject(parts);
    buildHeadings();
    buildToc();
    scrollSpy();
    search();
    partLinks();
    if (window.matchMedia && window.matchMedia('(max-width: 640px)').matches) $$('details.part-card--fold[open]').forEach(function (d) { d.open = false; }); $$('details.first-words[open]').forEach(function (d) { d.open = false; });
    tableCues();
    diagramStart();
    requestAnimationFrame(jumpToHash);
    window.addEventListener('hashchange', jumpToHash);
  }).catch(function (err) {
    loading.classList.add('is-error');
    loading.innerHTML = '<p><strong>Could not load the page sections</strong> (' + escapeHtml(String(err.message || err)) + ').</p>' +
      '<p>This page assembles itself from files in <code>sections/</code>, so it must be served over HTTP. ' +
      'Locally, run <code>python3 -m http.server 8000</code> in the project folder and open <code>http://localhost:8000/</code>.</p>';
  });
})();
