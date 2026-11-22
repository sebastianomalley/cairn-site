# Builds the static pages from one shared header and footer.
# Run: python3 build.py

# Paste your Stripe Payment Link here when it's ready. Until then the buy button shows "Coming soon".
STRIPE_LINK = ""
WORKBOOK_PRICE = "$19"

PAGES = [("index.html", "Home"), ("getting-started.html", "Getting Started"),
         ("legacy-films.html", "Legacy Films"), ("workbook.html", "The Workbook")]


def head(title, desc, current):
    links = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if href == current else ""}>{label}</a>'
        for href, label in PAGES[1:])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='0' y1='0' x2='0' y2='1'%3E%3Cstop offset='0' stop-color='%234A2F45'/%3E%3Cstop offset='1' stop-color='%23E9A27A'/%3E%3C/linearGradient%3E%3C/defs%3E%3Ccircle cx='16' cy='16' r='15' fill='url(%23g)'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="mock-bar">Preview build. Not public yet.</div>
<header class="head">
  <div class="wrap">
    <a class="brand" href="index.html">Everything Is Already All Right<small>Jason O'Malley · End-of-Life Doula</small></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" aria-label="Main">
      {links}
      <a class="btn" href="contact.html"{" aria-current=\"page\"" if current == "contact.html" else ""}>Free consultation</a>
    </nav>
  </div>
</header>
<main id="main">
'''


FOOT = '''
</main>
<footer class="foot">
  <div class="wrap">
    <div class="row">
      <div>
        <a class="brand" href="index.html">Everything Is Already All Right<small>Jason O'Malley · End-of-Life Doula</small></a>
        <p style="margin-top:16px;max-width:40ch">Serving Washington, DC, Northern Virginia, Florida and North Carolina, with virtual support anywhere. <a href="tel:+19177532905" style="color:#F0C987;text-decoration:none;white-space:nowrap">(917) 753-2905</a></p>
      </div>
      <nav aria-label="Footer">
        <a href="getting-started.html">Getting Started</a><a href="legacy-films.html">Legacy Films</a><a href="workbook.html">The Workbook</a><a href="resources.html">Resources</a><a href="https://jason-omalley.com">About me</a>
      </nav>
    </div>
    <div class="fine"><span>&copy; <span id="year">2026</span> Jason O'Malley</span><span>Doulas provide non-medical support. Nothing here is medical or legal advice.</span></div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
'''

CONSULT = '''
<section class="sec center">
  <div class="narrow">
    <p class="eyebrow">Whenever you're ready</p>
    <h2>Start with a <em>free 20-minute</em> conversation.</h2>
    <p class="lede">No pressure and no script. We'll talk about what's going on, I'll answer your questions, and you decide what comes next.</p>
    <div class="btn-row" style="justify-content:center"><a class="btn" href="contact.html">Book a free consultation</a></div>
  </div>
</section>
'''

pages = {}

pages["index.html"] = ("Everything Is Already All Right | End-of-life doula care with Jason O'Malley",
"Warm, steady, non-medical end-of-life doula support in Washington, DC, Northern Virginia, Florida and North Carolina.", '''
<section class="hero">
  <div class="inner">
    <p class="eyebrow">End-of-life doula care</p>
    <h1>Everything is already <em>all right.</em></h1>
    <p class="lede">Warm, steady, human company for the end of a life, and for the people who love them.</p>
    <div class="btn-row">
      <a class="btn btn-gold" href="getting-started.html">Get started</a>
      <a class="btn btn-line" href="contact.html">Free consultation</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="narrow">
    <p class="eyebrow">First things first</p>
    <h2>Wait... a <em>death doula?</em></h2>
    <p class="lede">You've probably heard of birth doulas. They help bring a new life into the world with a lot of care and a steady hand. A death doula does the same thing at the other end of life.</p>
    <p>I'm not a doctor or a nurse. I'm the person who sits with you, listens, helps you plan, and makes sure you and your family aren't figuring this out alone. Part guide, part planner, part calm person in the room.</p>
  </div>
  <div class="wrap">
    <div class="doors">
      <a class="door d1 reveal" href="getting-started.html"><span class="n">Start here</span><h3>Getting started</h3><p>What a doula does and doesn't do, how working together works, and a free guide to read first.</p><span class="go">Read more</span></a>
      <a class="door d2 reveal" href="legacy-films.html"><span class="n">Something to keep</span><h3>Legacy films</h3><p>A short film of a life, told in a person's own voice, for the people who'll want to hear it again.</p><span class="go">Read more</span></a>
      <a class="door d3 reveal" href="workbook.html"><span class="n">At your own pace</span><h3>The workbook</h3><p>Not ready for a call? Leaving Well is a guided workbook you can start on your own, whenever you're ready.</p><span class="go">Take a look</span></a>
    </div>
  </div>
</section>
''' + CONSULT)

pages["getting-started.html"] = ("Getting started | Everything Is Already All Right",
"What an end-of-life doula is and isn't, how working together works, and a free guide.", '''
<section class="hero small">
  <div class="inner">
    <p class="eyebrow">Getting started</p>
    <h1>Here's how this <em>works.</em></h1>
    <p class="lede">No need to have anything figured out. Start by reading, then let's talk.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="narrow" style="margin:0">
      <p class="eyebrow">The basics</p>
      <h2>What a doula is, <em>and isn't</em></h2>
    </div>
    <div class="two">
      <div class="panel is"><h3>What I do</h3><ul>
        <li>Talk through the big stuff, the small stuff and what nobody else wants to bring up</li>
        <li>Help you get your wishes written down and into the right hands</li>
        <li>Plan the vigil, the music, light and who's in the room</li>
        <li>Give your family a break so they can rest and just be family</li>
        <li>Stay through the last days and the hours after</li>
        <li>Help with letters, recorded stories and legacy projects</li>
        <li>Check in with the family in the weeks that follow</li>
      </ul></div>
      <div class="panel isnt"><h3>What I don't do</h3><ul>
        <li>Medical care of any kind. That's your doctor and hospice team.</li>
        <li>Legal advice. I'll point you to the right forms and people.</li>
        <li>Replace hospice. I work alongside them.</li>
        <li>Tell you how to feel, what to believe or how to grieve</li>
        <li>Share your story with anyone without your okay</li>
      </ul></div>
    </div>
  </div>
</section>

<section class="sec band">
  <div class="wrap">
    <p class="eyebrow">How we'd work together</p>
    <h2>Three simple <em>steps.</em></h2>
    <div class="steps">
      <div class="step"><h3>Read the guide</h3><p>Download the free guide below. It covers the basics and a few good questions to start thinking about.</p></div>
      <div class="step"><h3>Free 20-minute call</h3><p>We talk about what's going on and what you need. You ask me anything. No pressure to sign up.</p></div>
      <div class="step"><h3>Choose your path</h3><p>Work with me on a plan built around you, or start on your own with the Leaving Well workbook.</p></div>
    </div>
    <p class="lede" style="margin-top:50px;max-width:56ch">Every family is different, so there's no one-size package. We'll shape the support and the cost together after our first conversation. The workbook is included when we work together.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="download reveal">
      <div><p class="eyebrow">Free download</p><h3>Let's talk about the part nobody talks about</h3><p>A friendly fold-out guide for anyone who's never heard the words "death doula." Easy to share with family.</p></div>
      <a class="btn" href="downloads/death-doula-guide.pdf" download>Download the guide</a>
    </div>
  </div>
</section>

<section class="sec tight">
  <div class="narrow">
    <p class="eyebrow">Fair questions</p>
    <h2>Questions people <em>ask me</em></h2>
    <div class="faq">
      <details><summary>Isn't that what hospice does?</summary><p>Hospice is wonderful and takes care of the medical side. I work alongside them on the emotional and practical side, and I can spend the kind of long, unhurried time with you that a care team often can't.</p></details>
      <details><summary>Do I have to be sick to call you?</summary><p>Not at all. Some of the best planning happens years ahead, over coffee, with no rush at all.</p></details>
      <details><summary>Isn't it all really sad?</summary><p>There are tears, sure. There's also a surprising amount of laughter, great stories and the occasional debate about the playlist.</p></details>
      <details><summary>Do I need to be religious?</summary><p>Nope. I meet you where you are, whatever you believe or don't.</p></details>
      <details><summary>Do you help with pets?</summary><p>Yes. I'm also certified to help families say goodbye to a beloved companion animal.</p></details>
      <details><summary>Is what I tell you private?</summary><p>Yes. What you share with me stays with me. I don't share your story, photos or film with anyone without your written okay.</p></details>
      <details><summary>Does insurance cover this?</summary><p>Not usually. Doula care is typically paid privately. We'll talk openly about cost on our first call.</p></details>
    </div>
  </div>
</section>
''' + CONSULT)

pages["legacy-films.html"] = ("Legacy films | Everything Is Already All Right",
"Short legacy films that tell a life in a person's own voice.", '''
<section class="hero small" style="background: radial-gradient(ellipse 70% 60% at 80% 110%, #F0C987, transparent 70%), linear-gradient(110deg, #3E4E6A, #7A5A6E 55%, #E9A27A);">
  <div class="inner">
    <p class="eyebrow">Legacy films</p>
    <h1>Your story, <em>in your own voice.</em></h1>
    <p class="lede">A short film of a life, made for the people who will want to hear you tell it again.</p>
  </div>
</section>

<section class="sec">
  <div class="narrow">
    <p class="eyebrow">Why I do this</p>
    <h2>Before this work, I spent years <em>behind a camera.</em></h2>
    <p class="lede">Photos hold a face. A film holds the way someone laughs, the pause before the punchline, the way they say your name.</p>
    <p>A legacy film is a short, personal portrait. We sit down together, I ask good questions, and you tell it your way. The funny parts, the hard parts and the stuff nobody's heard before. It's yours to keep and share however you like, or not at all.</p>
  </div>
</section>

<section class="sec band lav">
  <div class="wrap">
    <p class="eyebrow">How it goes</p>
    <h2>Simple, <em>unhurried</em>, yours.</h2>
    <div class="steps">
      <div class="step"><h3>We talk first</h3><p>What do you want to say, and who is it for? We choose the questions and the place together.</p></div>
      <div class="step"><h3>We film</h3><p>At home or somewhere that matters to you. One relaxed session, with breaks whenever you need them.</p></div>
      <div class="step"><h3>You keep it</h3><p>I edit it into a short film you can watch, share and pass down. Nothing is shared without your okay.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <p class="quote">"Tell me about a time you laughed so hard you couldn't stop."</p>
  <p class="center" style="margin-top:18px;color:var(--muted)">One of the questions I like to start with.</p>
</section>

<section class="sec tight center">
  <div class="narrow">
    <p class="lede">Legacy films can be part of our work together or a project on their own. Every film is different, so we'll talk through it on a free call.</p>
    <div class="btn-row" style="justify-content:center"><a class="btn" href="contact.html">Ask about a legacy film</a></div>
  </div>
</section>
''')

buy = (f'<a class="btn" href="{STRIPE_LINK}">Buy the workbook</a>' if STRIPE_LINK
       else '<a class="btn" href="contact.html?interest=workbook">Coming soon. Get on the list</a>')

pages["workbook.html"] = ("Leaving Well workbook | Everything Is Already All Right",
"Leaving Well, a guided end-of-life planning and legacy workbook you can start on your own.", f'''
<section class="sec">
  <div class="wrap wb-hero">
    <div>
      <p class="eyebrow">The workbook</p>
      <h1 style="font-size:clamp(3rem,6.6vw,5.4rem)">Leaving <em>Well</em></h1>
      <p class="lede">Big questions, good stories, and the things your people will thank you for writing down.</p>
      <p>Not ready for a call? That's completely fine. Leaving Well is a guided workbook you can work through on your own time, at your kitchen table, with someone you love or by yourself. It's warm, a little fun, and nothing like a form at the doctor's office.</p>
      <div class="price">{WORKBOOK_PRICE}<small>Fillable PDF · 16 pages</small></div>
      <div class="btn-row" style="margin-top:20px">{buy}</div>
      <p class="fine-note">Included free when we work together.</p>
    </div>
    <img class="book" src="img/workbook-cover.jpg" alt="The Leaving Well workbook cover, a dusk gradient from deep midnight into warm apricot">
  </div>
</section>

<section class="sec band sage">
  <div class="wrap">
    <p class="eyebrow">What's inside</p>
    <h2>Eight short sections, <em>any order you like</em></h2>
    <ul class="inside">
      <li><b>The Basics</b><span>The practical page. Let's get it out of the way first.</span></li>
      <li><b>What Matters Most</b><span>Before the medical stuff, the human stuff.</span></li>
      <li><b>How I Want to Be Cared For</b><span>Your wishes in your own words.</span></li>
      <li><b>My People</b><span>Who you want close and who you trust to speak for you.</span></li>
      <li><b>Setting the Room</b><span>The soundtrack, the light and how it should feel.</span></li>
      <li><b>The Stories</b><span>What you've learned and what should go to whom.</span></li>
      <li><b>After I'm Gone</b><span>The song that must play, and the one that must not.</span></li>
      <li><b>Where Things Live</b><span>So nobody has to dig through the junk drawer.</span></li>
    </ul>
    <p style="margin-top:26px">Plus twelve story prompts, a resource guide for DC, Virginia, Florida and North Carolina, and room for notes.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <p class="eyebrow center">Take a peek</p>
    <h2 class="center">Two sample <em>pages</em></h2>
    <div class="samples">
      <figure class="reveal"><img src="img/workbook-sample-1.jpg" alt="Sample page titled First, a promise, explaining that this is not a form at the doctor's office"><figcaption>First, a promise</figcaption></figure>
      <figure class="reveal"><img src="img/workbook-sample-2.jpg" alt="Sample page titled Setting the Room, with prompts for the soundtrack, light and atmosphere, touch and words"><figcaption>Setting the Room</figcaption></figure>
    </div>
    <p class="fine-note center" style="margin-top:30px">This workbook is for reflection and planning. It is not a legal document. Your answers stay with you.</p>
  </div>
</section>
''' + CONSULT)

pages["contact.html"] = ("Free consultation | Everything Is Already All Right",
"Book a free 20-minute consultation with Jason O'Malley, end-of-life doula.", '''
<section class="sec" style="padding-top:40px">
  <div class="wrap contact-grid">
    <div>
      <p class="eyebrow">Free 20-minute consultation</p>
      <h1 style="font-size:clamp(2.8rem,6vw,4.6rem)">No pressure, <em>no script.</em></h1>
      <p class="lede">Tell me a little about what's going on and I'll reach out to set up a time to talk.</p>
      <p style="margin-top:30px" class="eyebrow">Rather talk now?</p>
      <a class="phone-big" href="tel:+19177532905">(917) 753-2905</a>
      <p>Call or text. If I don't pick up, I'm probably with someone, and I'll call you back.</p>
      <div class="privacy"><strong>A note on privacy.</strong> What you share with me stays with me. Please keep medical details out of this form. We can talk about specifics on the phone.</div>
    </div>
    <form class="form" id="contactForm">
      <input type="hidden" name="access_key" value="19f84a20-0e99-46cd-95c0-8a7e95db971e">
      <input type="hidden" name="subject" value="New doula inquiry from the website">
      <input type="hidden" name="from_name" value="Everything Is Already All Right">
      <input type="checkbox" name="botcheck" style="display:none">
      <div class="field"><label for="name">Your name</label><input id="name" name="name" required autocomplete="name"></div>
      <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email"></div>
      <div class="field"><label for="phone">Phone <span style="font-size:.85rem;color:var(--muted)">(optional)</span></label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field"><span class="lab">Who is this for?</span>
        <div class="chips">
          <label><input type="radio" name="for" value="Me"><span>Me</span></label>
          <label><input type="radio" name="for" value="Someone I love"><span>Someone I love</span></label>
          <label><input type="radio" name="for" value="A pet"><span>A pet</span></label>
          <label><input type="radio" name="for" value="I work in care"><span>I work in care</span></label>
        </div>
      </div>
      <div class="field"><span class="lab">What are you curious about?</span>
        <div class="chips">
          <label><input type="checkbox" name="interest[]" value="Doula support"><span>Doula support</span></label>
          <label><input type="checkbox" name="interest[]" value="Legacy film"><span>A legacy film</span></label>
          <label><input type="checkbox" name="interest[]" value="Workbook" id="int-workbook"><span>The workbook</span></label>
          <label><input type="checkbox" name="interest[]" value="Not sure yet"><span>Not sure yet</span></label>
        </div>
      </div>
      <div class="field"><label for="msg">Anything you'd like me to know</label><textarea id="msg" name="message" placeholder="A few lines is plenty."></textarea></div>
      <button class="btn" type="submit">Send</button>
      <p class="form-note">I'll only use your info to get back to you.</p>
      <p class="form-status" id="formStatus" role="status"></p>
    </form>
  </div>
</section>
''')

pages["resources.html"] = ("Resources | Everything Is Already All Right",
"Advance directive resources for DC, Virginia, Florida and North Carolina.", '''
<section class="sec" style="padding-top:40px">
  <div class="narrow">
    <p class="eyebrow">Resources</p>
    <h1 style="font-size:clamp(2.8rem,6vw,4.6rem)">Make it <em>official.</em></h1>
    <p class="lede">An advance directive lets you name who speaks for you and write down your medical wishes. Every state has its own version. Always check the official source.</p>
    <div class="res-list">
      <div><b>CaringInfo</b><p>Free advance directive forms for every state. Helpline 800-658-8898.</p><a href="https://www.caringinfo.org/planning/advance-directives/by-state/">https://www.caringinfo.org/planning/advance-directives/by-state/</a></div>
      <div><b>The Conversation Project</b><p>Free guides for talking with family about what matters.</p><a href="https://theconversationproject.org">https://theconversationproject.org</a></div>
      <div><b>DC MOST form</b><p>Medical orders for people who are seriously ill in DC. Ask your doctor.</p><a href="https://dchealth.dc.gov/most">https://dchealth.dc.gov/most</a></div>
      <div><b>Virginia Advance Directive Registry</b><p>Store yours so providers can find it.</p><a href="https://www.connectvirginia.org/adr/">https://www.connectvirginia.org/adr/</a></div>
      <div><b>Florida advance directives</b><p>Living will, health care surrogate and donation forms.</p><a href="https://quality.healthfinder.fl.gov/report-guides/advance-directives">https://quality.healthfinder.fl.gov/report-guides/advance-directives</a></div>
      <div><b>North Carolina Advance Health Care Directive Registry</b><p>Documents must be notarized to register.</p><a href="https://www.sosnc.gov/ahc">https://www.sosnc.gov/ahc</a></div>
    </div>
    <div class="privacy">These links go to outside organizations. I'm not a lawyer or a medical provider, so when in doubt, ask your doctor, hospice team or an attorney.</div>
  </div>
</section>
''')

for fname, (title, desc, body) in pages.items():
    with open(fname, "w") as f:
        f.write(head(title, desc, fname) + body + FOOT)
print("built", len(pages))
