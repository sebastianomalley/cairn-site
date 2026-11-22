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

// Gentle reveal on scroll
const els = document.querySelectorAll('.reveal');
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
