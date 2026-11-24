(function () {
  // Site root, worked out from wherever this page lives (GitHub Pages now, your own domain later).
  var BASE = location.href.replace(/desk\/.*$/, '');
  var F = 'desk/files/';

  var ITEMS = [
    { g: 'formsList', id: 'intake', name: 'Client intake', note: 'After the free call', url: F + 'cairn-client-intake.pdf', subj: 'Getting to know you',
      msg: "Here's a short intake form so I can get to know you and your family before we meet. Fill in whatever feels right, and skip anything that doesn't. We can finish it together." },
    { g: 'formsList', id: 'agreement', name: 'Services agreement', note: 'Before work begins', url: F + 'cairn-services-agreement.pdf', subj: 'Our agreement',
      msg: "Here's our services agreement. Take your time reading it, and let me know if you have any questions before signing." },
    { g: 'formsList', id: 'care', name: 'Care and support plan', note: 'First few visits', url: F + 'cairn-care-plan.pdf', subj: 'Your care and support plan',
      msg: "Here's the care and support plan we talked about, so everyone is on the same page. We'll update it together as things change." },
    { g: 'formsList', id: 'vigil', name: 'Vigil plan', note: 'For the final days', url: F + 'cairn-vigil-plan.pdf', subj: 'Vigil plan',
      msg: "Here's the vigil plan, so everyone keeping watch knows how they'd like these days to feel and who to call. Feel free to share it with family." },
    { g: 'formsList', id: 'consent', name: 'Legacy and film consent', note: 'Before any recording', url: F + 'cairn-legacy-consent.pdf', subj: 'Legacy project consent',
      msg: "Here's the consent form for the legacy project. Nothing is recorded or shared without it, and you can change your mind at any time." },
    { g: 'formsList', id: 'after', name: 'After a death checklist', note: 'For the family', url: F + 'cairn-after-a-death.pdf', subj: 'A checklist for the days ahead',
      msg: "I'm so sorry. There's no rush with any of this. When you're ready, here's a gentle checklist for the days and weeks ahead. I'm here if you need anything." },
    { g: 'formsList', id: 'near', name: 'Near the end handout', note: 'For families', url: F + 'cairn-near-the-end.pdf', subj: 'What you might notice near the end',
      msg: "Here's a short handout on what you might notice in the final days. I hope it makes things a little less frightening. Call me or the hospice nurse anytime." },
    { g: 'formsList', id: 'notes', name: 'Visit notes', note: 'Your records only', url: F + 'cairn-visit-notes.pdf', subj: 'Visit notes', mine: true,
      msg: 'Visit notes form.' },
    { g: 'booksList', id: 'workbook', name: 'Leaving Well workbook', note: 'Full paid file', url: F + 'leaving-well-workbook-k7q2.pdf', subj: 'Your Leaving Well workbook', paid: true,
      msg: "Here's your copy of the Leaving Well workbook. You can type right into it on your computer, tablet or phone, save as you go, or print it. Take it one page at a time." },
    { g: 'booksList', id: 'guide', name: 'Free guide', note: 'What is a death doula?', url: 'downloads/what-is-a-death-doula-guide.pdf', subj: 'What exactly is a death doula?',
      msg: "Here's a short, friendly guide to what a death doula is and how I can help. No pressure, just something to read when you have a moment." },
    { g: 'booksList', id: 'wbpage', name: 'Workbook page', note: 'Preview and buy', url: 'workbook.html', subj: 'The Leaving Well workbook',
      msg: "Here's the Leaving Well workbook if you'd like to start at your own pace. You can see a few sample pages there." },
    { g: 'pagesList', id: 'home', name: 'Homepage', note: 'Start here', url: '', subj: 'Cairn End-of-Life Doula Care',
      msg: "Here's my website, if you'd like to learn more about what I do." },
    { g: 'pagesList', id: 'what', name: 'What is a doula', note: 'Step one', url: 'what-is-a-doula.html', subj: 'What is a death doula?',
      msg: "Here's a page that explains what a death doula is and how it fits with hospice." },
    { g: 'pagesList', id: 'call', name: 'Free consultation', note: 'Booking form', url: 'contact.html', subj: "Let's talk",
      msg: "Here's where you can set up a free 20-minute call. No pressure, just a chance to say hello." }
  ];

  var who = document.getElementById('who'), msg = document.getElementById('msg');
  var outLink = document.getElementById('outLink');
  var current = ITEMS[0], link = '', edited = false;

  function full(u) { return BASE + u; }
  function greet() { var n = who.value.trim(); return n ? 'Hi ' + n + ',\n\n' : 'Hi,\n\n'; }
  function compose() { return greet() + current.msg + '\n\n' + link + '\n\nJason O\'Malley\nCairn End-of-Life Doula Care\n(917) 753-2905'; }

  function update() {
    link = full(current.url);
    outLink.textContent = link;
    if (!edited) msg.value = current.mine ? link : compose();
    document.getElementById('warn').hidden = !current.paid;
    document.getElementById('textBtn').href = 'sms:&body=' + encodeURIComponent(msg.value);
    document.getElementById('mailBtn').href = 'mailto:?subject=' + encodeURIComponent(current.subj) + '&body=' + encodeURIComponent(msg.value);
    document.getElementById('openBtn').href = link;
  }

  ITEMS.forEach(function (it, i) {
    var l = document.createElement('label');
    l.className = 'pick-item';
    l.innerHTML = '<input type="radio" name="doc"><span><b></b><small></small></span>';
    l.querySelector('b').textContent = it.name;
    l.querySelector('small').textContent = it.note;
    var r = l.querySelector('input');
    if (i === 0) r.checked = true;
    r.addEventListener('change', function () { current = it; edited = false; update(); });
    document.getElementById(it.g).appendChild(l);
  });

  who.addEventListener('input', function () { edited = false; update(); });
  msg.addEventListener('input', function () { edited = true; update(); });

  function copy(text, btn) {
    function done() { var t = btn.textContent; btn.textContent = 'Copied'; setTimeout(function () { btn.textContent = t; }, 1400); }
    function fallback() { var ta = document.createElement('textarea'); ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0'; document.body.appendChild(ta); ta.select(); try { document.execCommand('copy'); done(); } catch (e) {} ta.remove(); }
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(done, fallback); else fallback();
  }
  document.getElementById('copyBtn').addEventListener('click', function () { copy(link, this); });
  document.getElementById('copyMsgBtn').addEventListener('click', function () { copy(msg.value, this); });
  update();

  var ul = document.getElementById('quickList');
  ITEMS.forEach(function (it) {
    var li = document.createElement('li');
    li.innerHTML = '<span><b></b><small></small></span><span class="q-btns"><a target="_blank" rel="noopener">Open</a><button type="button">Copy</button></span>';
    li.querySelector('b').textContent = it.name;
    li.querySelector('small').textContent = full(it.url).replace(/^https?:\/\//, '');
    li.querySelector('a').href = full(it.url);
    li.querySelector('button').addEventListener('click', function () { copy(full(it.url), this); });
    ul.appendChild(li);
  });
})();
