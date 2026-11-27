// Nav toggle
const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    document.body.classList.toggle('nav-open', open);
    toggle.setAttribute('aria-expanded', open);
    toggle.textContent = open ? 'Close' : 'Menu';
  });
  nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
    nav.classList.remove('open');
    document.body.classList.remove('nav-open');
    toggle.setAttribute('aria-expanded', false);
    toggle.textContent = 'Menu';
  }));
}

// Respect reduced motion for the hero video
const vid = document.querySelector('.hero video');
if (vid && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  vid.removeAttribute('autoplay');
  vid.pause();
}

// Lists arrive one line at a time
document.querySelectorAll('.fit-list, .menu, .shelf ul, .res-list, .steps, .rows').forEach(list => {
  list.classList.add('stagger');
  list.classList.remove('reveal');
  [...list.children].forEach((c, i) => c.style.setProperty('--i', Math.min(i, 10)));
});

// Gentle reveal on scroll
const els = document.querySelectorAll('.reveal, .stagger');
if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: 0.12 });
  els.forEach(el => io.observe(el));
} else {
  els.forEach(el => el.classList.add('in'));
}

// Contact form (Web3Forms)
const form = document.getElementById('contactForm');
if (form) {
  const status = document.getElementById('formStatus');
  form.addEventListener('submit', e => {
    e.preventDefault();
    status.textContent = 'Sending...';
    fetch('https://api.web3forms.com/submit', { method: 'POST', headers: { 'Accept': 'application/json' }, body: new FormData(form) })
      .then(r => r.json())
      .then(d => {
        if (d.success) { form.reset(); status.textContent = "Thank you. I'll be in touch soon."; }
        else { status.textContent = 'Something went wrong. Please call or text (917) 753-2905.'; }
      })
      .catch(() => { status.textContent = 'Something went wrong. Please call or text (917) 753-2905.'; });
  });
}

const y = document.getElementById('year');
if (y) y.textContent = new Date().getFullYear();

// Pre-check the workbook option when coming from the workbook page
if (new URLSearchParams(location.search).get('interest') === 'workbook') {
  const w = document.getElementById('int-workbook');
  if (w) w.checked = true;
}

// Pre-select "An animal companion" when coming from the companion animals page
if (new URLSearchParams(location.search).get('for') === 'animal') {
  const a = document.getElementById('for-animal');
  if (a) a.checked = true;
}

// Depth: background glows drift a little slower than the page
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const orbs = document.querySelectorAll('.hero .orbs');
  const bands = document.querySelectorAll('.tone-dusk, .next-band');
  let ticking = false;
  const update = () => {
    const vh = window.innerHeight;
    orbs.forEach(o => { o.style.setProperty('--par', (window.scrollY * 0.25).toFixed(1) + 'px'); });
    bands.forEach(b => {
      const r = b.getBoundingClientRect();
      if (r.bottom < 0 || r.top > vh) return;
      const p = (vh - r.top) / (vh + r.height);
      b.style.setProperty('--bgy', (20 + p * 60).toFixed(1) + '%');
    });
    ticking = false;
  };
  window.addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  update();
}
