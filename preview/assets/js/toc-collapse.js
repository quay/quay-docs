/**
 * Collapsible left-hand TOC for Surge preview.
 * Nests subsection lists under their parent; click the chevron to expand/collapse.
 * Auto-expands ancestors of the current hash / scroll-spy active item.
 */
(function () {
  const toc = document.querySelector('#toc.toc2');
  if (!toc) return;

  function expandAncestors(link) {
    let li = link.closest('li');
    while (li && li !== toc) {
      if (li.classList.contains('toc-collapsible')) {
        li.classList.add('expanded');
        const btn = li.querySelector(':scope > .toc-chevron');
        if (btn) btn.setAttribute('aria-expanded', 'true');
      }
      const parentUl = li.parentElement;
      li = parentUl ? parentUl.closest('li') : null;
    }
  }

  toc.querySelectorAll('li').forEach((li) => {
    const childUl = li.querySelector(':scope > ul');
    const link = li.querySelector(':scope > a');
    if (!childUl || !link) return;

    li.classList.add('toc-collapsible');

    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'toc-chevron';
    btn.setAttribute('aria-label', 'Expand section');
    btn.setAttribute('aria-expanded', 'false');
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      const expanded = li.classList.toggle('expanded');
      btn.setAttribute('aria-expanded', expanded ? 'true' : 'false');
      btn.setAttribute('aria-label', expanded ? 'Collapse section' : 'Expand section');
    });

    li.insertBefore(btn, link);
  });

  function syncFromHash() {
    const hash = decodeURIComponent(window.location.hash || '');
    if (!hash) return;
    const target = toc.querySelector(`a[href="${hash}"]`);
    if (target) expandAncestors(target);
  }

  syncFromHash();
  window.addEventListener('hashchange', syncFromHash);

  // Expand parents when scroll-spy marks a nested item active
  if (window.jQuery) {
    const $ = window.jQuery;
    const anchors = $('body').find('h1[id], h2[id], h3[id], h4[id], h5[id], h6[id]');
    $(window).on('scroll', () => {
      const scrollTop = $(document).scrollTop();
      for (let i = anchors.length - 1; i >= 0; i--) {
        if (scrollTop > $(anchors[i]).offset().top - 75) {
          const active = toc.querySelector(`a[href="#${anchors[i].id}"]`);
          if (active) expandAncestors(active);
          break;
        }
      }
    });
  }
})();
