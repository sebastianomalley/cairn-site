// Mobile nav toggle
const toggle = document.querySelector('.nav-toggle');
const nav = document.getElementById('site-nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });
}

// Placeholder form handler.
// TODO: connect each form to a real service (Formspree, Netlify Forms, etc.)
// before launch. Right now it only shows a confirmation message.
document.querySelectorAll('form[data-mock]').forEach((form) => {
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const status = form.querySelector('.status');
    if (status) {
      status.textContent = 'Thanks, got it. I will be in touch soon.';
    }
    form.reset();
  });
});
