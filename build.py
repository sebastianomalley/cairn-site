# Builds every page from one shared header, journey rail and footer.
# Run: python3 build.py

# Paste your Stripe Payment Link here when it's ready. Until then the button says "Coming soon".
STRIPE_LINK = ""
WORKBOOK_PRICE = "$19"

STEPS = [
    ("what-is-a-doula.html", "One", "Understand", "What a doula is"),
    ("ways-i-help.html", "Two", "Explore", "Ways I can help"),
    ("how-it-works.html", "Three", "Connect", "How it works"),
    ("workbook.html", "Four", "At your pace", "The workbook"),
]
NAV = [("what-is-a-doula.html", "What is a doula"), ("ways-i-help.html", "Ways I help"),
       ("how-it-works.html", "How it works"), ("workbook.html", "Workbook")]

RINGS = '''<svg class="rings" viewBox="0 0 400 400" aria-hidden="true"><g fill="none" stroke="#F0C987" stroke-width=".7">
<circle cx="200" cy="200" r="60"/><circle cx="200" cy="200" r="95" opacity=".8"/><circle cx="200" cy="200" r="130" opacity=".6"/>
<circle cx="200" cy="200" r="165" opacity=".45"/><circle cx="200" cy="200" r="198" opacity=".3"/></g></svg>'''


def head(title, desc, current):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{l}</a>' for h, l in NAV)
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
<link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400;1,600&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
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
      <a class="btn" href="contact.html">Free consultation</a>
    </nav>
  </div>
</header>
<main id="main">
'''


def journey(current=None):
    items = "".join(
        f'<a href="{h}"{" aria-current=\"step\"" if h == current else ""}><span class="k">Step {n.lower()}</span>'
        f'<span class="t">{t}</span><span class="d">{d}</span></a>' for h, n, t, d in STEPS)
    return f'<nav class="journey" aria-label="Your path through this site">{items}</nav>'


def nxt(href, kicker, title):
    return f'''<section class="sec" style="padding-top:20px">
  <div class="wrap"><a class="next reveal" href="{href}"><div><div class="k">{kicker}</div><div class="t">{title}</div></div><span class="circle" aria-hidden="true">→</span></a></div>
</section>'''


FOOT = '''
</main>
<footer class="foot">
  <div class="wrap">
    <div class="row">
      <div>
        <a class="brand" href="index.html">Everything Is Already All Right<small>Jason O'Malley · End-of-Life Doula</small></a>
        <p style="margin-top:20px;max-width:38ch">Non-medical end-of-life support in Washington, DC, Northern Virginia, Florida and North Carolina, with virtual support anywhere. Every faith, culture and family welcome.</p>
      </div>
      <div><h4>The path</h4><a href="what-is-a-doula.html">What is a doula</a><a href="ways-i-help.html">Ways I can help</a><a href="how-it-works.html">How it works</a><a href="workbook.html">The workbook</a></div>
      <div><h4>Reach me</h4><a href="contact.html">Free consultation</a><a href="tel:+19177532905">(917) 753-2905</a><a href="resources.html">Resources</a><a href="https://jason-omalley.com">About me</a></div>
    </div>
    <div class="fine"><span>&copy; <span id="year">2026</span> Jason O'Malley</span><span>Doulas provide non-medical support. Nothing on this site is medical or legal advice.</span></div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
'''

P = {}

# ---------------------------------------------------------------- HOME
P["index.html"] = ("Everything Is Already All Right | End-of-life doula care with Jason O'Malley",
"Warm, non-medical end-of-life doula support for people of every faith, culture and family in DC, Northern Virginia, Florida and North Carolina.", f'''
<section class="hero">
  {RINGS}
  <div class="inner">
    <p class="eyebrow">End-of-life doula care</p>
    <h1>Everything is already <em>all right.</em></h1>
    <p class="lede">Warm, steady company for the end of a life, and for the people who love them. Whatever you believe, wherever you come from, you're welcome here.</p>
    <div class="btn-row">
      <a class="btn btn-gold" href="what-is-a-doula.html">Start here</a>
      <a class="btn btn-line" href="contact.html">Say hello</a>
    </div>
  </div>
</section>
{journey()}

<section class="sec">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">Welcome</p><h2>However you got here, <em>you're welcome.</em></h2></div></div>
    <div class="main reveal">
      <p class="lede">Maybe you're caring for someone you love. Maybe you're planning ahead. Maybe someone mentioned a "death doula" and you're quietly wondering what that even means.</p>
      <p>This can feel like a lot. That's normal. This site is set up to walk you through it one step at a time, at whatever pace feels okay. Nothing here asks you to commit to anything.</p>
      <p>If at any point you'd rather just talk, I'm a phone call away.</p>
    </div>
  </div>
</section>

<section class="sec tone-blush">
  <div class="wrap">
    <div class="narrow center" style="margin-bottom:56px">
      <p class="eyebrow">Where would you like to begin?</p>
      <h2>Three gentle <em>ways in</em></h2>
    </div>
    <div class="grid-3">
      <a class="path p1 reveal" href="what-is-a-doula.html"><span class="step-n">If you're curious</span><h3>Learn what a doula is</h3><p>What it looks like, how it's different from hospice, and why families bring one in.</p><span class="go arrow">Start reading </span></a>
      <a class="path p2 reveal" href="contact.html"><span class="step-n">If you'd like to talk</span><h3>A free 20-minute call</h3><p>Say hello, ask anything and get to know each other. No pressure and no script.</p><span class="go arrow">Book a time </span></a>
      <a class="path p3 reveal" href="workbook.html"><span class="step-n">If you'd rather go slow</span><h3>Start on your own</h3><p>The Leaving Well workbook lets you explore all of this privately, at your own pace.</p><span class="go arrow">See the workbook </span></a>
    </div>
  </div>
</section>

<section class="sec tone-dusk">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">For everyone</p><h2>Every faith, every family, <em>every way of saying goodbye.</em></h2></div></div>
    <div class="main reveal">
      <p class="lede">There's no one right way to die, grieve or remember. Your beliefs, your culture and your family's traditions lead. I follow.</p>
      <p class="muted-on-dark">I'll take the time to learn what matters to you, and help bring in the people and practices that make it feel like yours, from your faith leader to your grandmother's prayers to the music you grew up on.</p>
      <div class="welcome-list"><span>Any faith or none</span><span>Every culture and tradition</span><span>Every kind of family</span><span>LGBTQ+ welcome</span><span>People and their pets</span></div>
    </div>
  </div>
</section>

<section class="sec center">
  <div class="wrap">
    <p class="quote">"I'm not here to fix anything. I'm here to show up, and to make sure you don't have to do this alone."</p>
    <p class="quote-by">Jason O'Malley</p>
  </div>
</section>
{nxt("what-is-a-doula.html", "Step one", "So what <em>is</em> a death doula?")}
''')

# ---------------------------------------------------------------- STEP 1
P["what-is-a-doula.html"] = ("What is a death doula? | Everything Is Already All Right",
"What an end-of-life doula is, what it looks like, how it differs from hospice and why families bring one in.", f'''
<section class="hero small">
  {RINGS}
  <div class="inner">
    <p class="eyebrow">Step one · Understand</p>
    <h1>So what is a death doula, <em>really?</em></h1>
    <p class="lede">The short answer, the longer answer, and how it all fits with hospice.</p>
  </div>
</section>
{journey("what-is-a-doula.html")}

<section class="sec">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">In plain words</p><h2>A companion for the <em>end of life</em></h2></div></div>
    <div class="main reveal">
      <p class="lede">You've probably heard of birth doulas. They help bring a new life into the world with care and a steady hand. A death doula, also called an end-of-life doula, does the same at the other end of life.</p>
      <p>I'm not a doctor or a nurse. I don't give medical care. What I offer is companionship. Doulas call it companioning. It means being with you, listening, helping you plan, and making sure you and your family aren't figuring this out alone.</p>
      <p>Part guide, part planner, part calm person in the room.</p>
    </div>
  </div>
</section>

<section class="sec tone-sand">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">Day to day</p><h2>What it can <em>look like</em></h2><p class="small" style="margin-top:14px">Every family is different. These are just a few examples.</p></div></div>
    <div class="main rows reveal">
      <div class="row"><span class="num">i.</span><div><h3>A conversation at the kitchen table</h3><p>Talking through what matters most, what scares you, and what you'd want if things get harder.</p></div></div>
      <div class="row"><span class="num">ii.</span><div><h3>Getting wishes on paper</h3><p>Helping you think through your choices and get them to the people who need them.</p></div></div>
      <div class="row"><span class="num">iii.</span><div><h3>Setting the room</h3><p>The music, the light, the readings or prayers, and who's there. Done your way.</p></div></div>
      <div class="row"><span class="num">iv.</span><div><h3>Sitting through the night</h3><p>Staying close so the family can sleep, eat or just breathe for a while.</p></div></div>
      <div class="row"><span class="num">v.</span><div><h3>The first hours after</h3><p>Helping the family through the first hours, honoring the rituals that matter to them.</p></div></div>
      <div class="row"><span class="num">vi.</span><div><h3>Checking in later</h3><p>Because grief doesn't end when the service does.</p></div></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="narrow center" style="margin-bottom:50px">
      <p class="eyebrow">Doula and hospice</p>
      <h2>Side by side, <em>never instead of</em></h2>
      <p class="lede">Hospice is wonderful, and I work alongside hospice teams, not in place of them. Here's how the two fit together.</p>
    </div>
    <table class="compare reveal">
      <thead><tr><th></th><th>Hospice team</th><th>End-of-life doula</th></tr></thead>
      <tbody>
        <tr><th>Focus</th><td data-l="Hospice">Medical comfort care, like managing pain and symptoms, with nursing visits.</td><td data-l="Doula">Emotional, practical and spiritual companionship for the person and the family.</td></tr>
        <tr><th>Who</th><td data-l="Hospice">Doctors, nurses, aides, social workers, chaplains and volunteers.</td><td data-l="Doula">One familiar person who gets to know you and your family.</td></tr>
        <tr><th>Time</th><td data-l="Hospice">Scheduled visits, with support on call.</td><td data-l="Doula">Unhurried time, including long visits and overnight vigils.</td></tr>
        <tr><th>When</th><td data-l="Hospice">Usually once someone has chosen comfort care near the end of life.</td><td data-l="Doula">Anytime, including years ahead, simply to plan.</td></tr>
        <tr><th>After</th><td data-l="Hospice">Bereavement support for the family.</td><td data-l="Doula">Present in the first hours, and checking in during the weeks that follow.</td></tr>
        <tr><th>Cost</th><td data-l="Hospice">Typically covered by Medicare, Medicaid and most insurance.</td><td data-l="Doula">Paid privately for now. Insurance doesn't cover doula care yet, though many of us are working to change that.</td></tr>
      </tbody>
    </table>
    <div class="who reveal">
      <div><h4>Palliative care</h4><p>Medical comfort care at any stage of a serious illness, often alongside treatment.</p></div>
      <div><h4>Chaplains and faith leaders</h4><p>Spiritual care within your tradition. I'm glad to work right alongside yours.</p></div>
      <div><h4>Social workers</h4><p>Help with resources, benefits and the practical systems around care.</p></div>
      <div><h4>Family and friends</h4><p>The heart of it all. My job is to support them, never to replace them.</p></div>
    </div>
  </div>
</section>

<section class="sec tone-blush">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">Why a doula</p><h2>Why families <em>bring one in</em></h2></div></div>
    <div class="main rows reveal">
      <div class="row"><span class="num">i.</span><div><h3>Time</h3><p>The kind of long, unhurried time a busy care team often can't give.</p></div></div>
      <div class="row"><span class="num">ii.</span><div><h3>One familiar face</h3><p>The same person from the first conversation to the last day, and after.</p></div></div>
      <div class="row"><span class="num">iii.</span><div><h3>Care for the whole family</h3><p>Support for the caregivers, the kids, the far-away relatives, everyone.</p></div></div>
      <div class="row"><span class="num">iv.</span><div><h3>Your wishes, honored</h3><p>Someone who knows what you want and helps keep it at the center.</p></div></div>
      <div class="row"><span class="num">v.</span><div><h3>Less pressure later</h3><p>Planning ahead means fewer hard decisions in the hardest moments.</p></div></div>
      <div class="row"><span class="num">vi.</span><div><h3>Someone who isn't afraid of this</h3><p>A steady presence when everyone else is understandably overwhelmed.</p></div></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">Fair questions</p><h2>Things people <em>wonder</em></h2></div></div>
    <div class="main faq">
      <details><summary>What if I'm not comfortable talking about death?</summary><p>Most people aren't, at first. We go at your pace. Sometimes we talk about everything except death for a while, and that's okay too.</p></details>
      <details><summary>Do I need to be religious?</summary><p>Not at all. I support people of every faith and of no faith. Your beliefs and traditions lead, and I follow.</p></details>
      <details><summary>Isn't it all really sad?</summary><p>There are tears, sure. There's also a surprising amount of laughter, good stories and the occasional debate about the playlist.</p></details>
      <details><summary>Is it covered by insurance?</summary><p>Not yet. Doula care is paid privately today, though many doulas are advocating for that to change. We'll talk openly about cost on our first call.</p></details>
      <details><summary>Do you help with pets?</summary><p>Yes. I'm also certified to help families say goodbye to a beloved companion animal.</p></details>
    </div>
  </div>
</section>
{nxt("ways-i-help.html", "Step two", "Ways I can help, <em>your way</em>")}
''')

# ---------------------------------------------------------------- STEP 2
P["ways-i-help.html"] = ("Ways I can help | Everything Is Already All Right",
"End-of-life doula support you design yourself, from planning conversations to vigil support and legacy films.", f'''
<section class="hero small">
  {RINGS}
  <div class="inner">
    <p class="eyebrow">Step two · Explore</p>
    <h1>Take what helps. <em>Leave the rest.</em></h1>
    <p class="lede">Here are the ways I can support you. You don't need all of them. You get to design it.</p>
  </div>
</section>
{journey("ways-i-help.html")}

<section class="sec">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">You design it</p><h2>Built around <em>you</em></h2></div></div>
    <div class="main reveal">
      <p class="lede">Some people want one good conversation. Some want me there every step of the way. Most land somewhere in between.</p>
      <p>Whatever you choose, it's all about companioning you and the people you love, in a way that fits your life, your beliefs and your family. We'll shape it together on a free call, and it can change as things change.</p>
    </div>
  </div>
</section>

<section class="sec tone-sand">
  <div class="wrap">
    <p class="eyebrow">The menu</p>
    <h2 style="margin-bottom:46px">Before, during <em>and after</em></h2>
    <div class="menu reveal">
      <div class="item"><span class="when">Before</span><h3>Planning conversations</h3><p>Unhurried time to talk through what matters, what you want and what worries you.</p></div>
      <div class="item"><span class="when">Before</span><h3>Getting wishes in order</h3><p>Help thinking through your advance directive and getting it to the right people. Not legal advice, just a guide through it.</p></div>
      <div class="item"><span class="when">During</span><h3>Companioning visits</h3><p>Regular time together for conversation, comfort, reading aloud or simply sitting quietly.</p></div>
      <div class="item"><span class="when">During</span><h3>Vigil planning and presence</h3><p>Shaping the space for the final days, honoring your rituals and traditions, and keeping watch alongside your family.</p></div>
      <div class="item"><span class="when">During</span><h3>Respite for caregivers</h3><p>Someone trusted to stay close so the people caring for you can rest.</p></div>
      <div class="item"><span class="when">After</span><h3>The first hours and beyond</h3><p>Being there after a death, helping with next steps, and checking in through early grief.</p></div>
      <div class="item"><span class="when">Anytime</span><h3>Legacy projects</h3><p>Letters, recorded stories, memory books and other ways to leave something of yourself behind.</p></div>
      <div class="item"><span class="when">Anytime</span><h3>Companion animals</h3><p>Gentle support for families saying goodbye to a beloved pet.</p></div>
      <div class="item feature">
        <div><span class="when">Part of vigil and legacy support</span><h3 style="font-size:2.2rem">Legacy films</h3></div>
        <div><p>Before this work I spent years behind a camera. A legacy film is a short, personal portrait of a life told in your own voice, for the people who'll want to hear it again. We talk first, film somewhere that feels right, and nothing is shared without your okay.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">Your traditions lead</p><h2>Your way, <em>always</em></h2></div></div>
    <div class="main reveal">
      <p class="lede">Every culture has its own wisdom about death, and every family has its own way of saying goodbye.</p>
      <p>Whether that means prayers in a certain language, a faith leader at the bedside, specific rituals after a death, or no religion at all, I'll learn what matters to you and help make room for it. If I don't know something, I'll ask, and I'll listen.</p>
    </div>
  </div>
</section>
{nxt("how-it-works.html", "Step three", "How working together <em>works</em>")}
''')

# ---------------------------------------------------------------- STEP 3
P["how-it-works.html"] = ("How it works | Everything Is Already All Right",
"How to get started with an end-of-life doula, what happens on the free call, how hiring works and how your privacy is protected.", f'''
<section class="hero small">
  {RINGS}
  <div class="inner">
    <p class="eyebrow">Step three · Connect</p>
    <h1>Let's take it <em>one step at a time.</em></h1>
    <p class="lede">Here's exactly what happens, from first hello to working together.</p>
  </div>
</section>
{journey("how-it-works.html")}

<section class="sec">
  <div class="wrap">
    <p class="eyebrow">The process</p>
    <h2>Four simple <em>steps</em></h2>
    <div class="steps reveal">
      <div class="step"><h3>Read the free guide</h3><p>A short, friendly fold-out with the basics and some good questions to sit with.</p></div>
      <div class="step"><h3>Have a free call</h3><p>Twenty minutes to say hello, ask anything and see if we're a good fit.</p></div>
      <div class="step"><h3>Shape your plan</h3><p>We decide together what support looks like. You get a simple written agreement with the cost up front.</p></div>
      <div class="step"><h3>Begin</h3><p>We start wherever you are, and adjust as life changes.</p></div>
    </div>
  </div>
</section>

<section class="sec tone-blush">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">The free call</p><h2>Twenty minutes, <em>no pressure</em></h2></div></div>
    <div class="main rows reveal">
      <div class="row"><span class="num">i.</span><div><h3>Getting to know each other</h3><p>You hear a bit about me, and I hear a bit about you and what's going on.</p></div></div>
      <div class="row"><span class="num">ii.</span><div><h3>Your questions</h3><p>Anything at all, even the ones that feel strange to ask.</p></div></div>
      <div class="row"><span class="num">iii.</span><div><h3>What support could look like</h3><p>Some ideas based on what you've shared, so you can picture it.</p></div></div>
      <div class="row"><span class="num">iv.</span><div><h3>How hiring works</h3><p>Cost, scheduling and next steps, all out in the open.</p></div></div>
      <div class="row"><span class="num">v.</span><div><h3>Zero obligation</h3><p>Some people hire me. Some just feel better for having talked. Both are good outcomes.</p></div></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="download reveal">
      <div class="copy">
        <p class="eyebrow">Free download</p>
        <h3 style="font-size:2rem">Start with the guide</h3>
        <p style="color:var(--muted)">A friendly fold-out for anyone who's never heard the words "death doula." Easy to share with family.</p>
        <ul><li>What a doula is, and isn't</li><li>Questions people ask</li><li>Questions worth sitting with</li><li>Three small first steps</li></ul>
        <div class="btn-row" style="margin-top:26px"><a class="btn" href="downloads/death-doula-guide.pdf" download>Download the guide</a></div>
      </div>
      <div class="art"><span class="t">Let's talk about the part <em>nobody talks about.</em></span></div>
    </div>
  </div>
</section>

<section class="sec tone-dusk">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">Privacy</p><h2>Your story <em>stays yours</em></h2></div></div>
    <div class="main rows reveal">
      <div class="row"><span class="num">i.</span><div><h3>Confidential, always</h3><p>What you share with me stays with me. Confidentiality is written into our agreement.</p></div></div>
      <div class="row"><span class="num">ii.</span><div><h3>Nothing shared without your okay</h3><p>Stories, photos and films are never shared or posted without your written permission.</p></div></div>
      <div class="row"><span class="num">iii.</span><div><h3>Only what's needed</h3><p>I keep only the notes I need to support you well, and I keep them secure.</p></div></div>
      <div class="row"><span class="num">iv.</span><div><h3>Not a medical provider</h3><p>I don't provide medical care or keep medical records. Your care team handles that.</p></div></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">Practical questions</p><h2>The <em>logistics</em></h2></div></div>
    <div class="main faq">
      <details><summary>How much does it cost?</summary><p>It depends on what you'd like support with, so we'll talk it through on the free call. Everything is agreed in writing before we begin, with no surprises.</p></details>
      <details><summary>Is it covered by insurance?</summary><p>Not yet. Doula care is paid privately today, though many of us are working to change that.</p></details>
      <details><summary>Where do you work?</summary><p>In person in Washington, DC, Northern Virginia, Florida and North Carolina, and virtually anywhere.</p></details>
      <details><summary>What if I'm not ready for all this?</summary><p>That's completely okay. You can read, sit with it, and come back when you're ready. Or start on your own with the workbook.</p></details>
      <details><summary>Can I just talk once?</summary><p>Of course. One conversation is sometimes exactly what someone needs.</p></details>
    </div>
  </div>
</section>

<section class="sec" style="padding-top:20px">
  <div class="wrap grid-2">
    <a class="next reveal" href="contact.html"><div><div class="k">Ready to talk?</div><div class="t">Book a free <em>20-minute call</em></div></div><span class="circle" aria-hidden="true">→</span></a>
    <a class="next reveal" href="workbook.html" style="background: radial-gradient(ellipse 70% 90% at 100% 100%, rgba(232,212,166,.9), transparent 65%), linear-gradient(120deg, #3F5E50, #6E8576);"><div><div class="k">Not quite ready?</div><div class="t">Start at <em>your own pace</em></div></div><span class="circle" aria-hidden="true">→</span></a>
  </div>
</section>
''')

# ---------------------------------------------------------------- STEP 4
buy = (f'<a class="btn" href="{STRIPE_LINK}">Buy the workbook</a>' if STRIPE_LINK
       else '<a class="btn" href="contact.html?interest=workbook">Coming soon · Join the list</a>')
P["workbook.html"] = ("Leaving Well workbook | Everything Is Already All Right",
"Leaving Well, a guided end-of-life planning and legacy workbook you can start on your own, at your own pace.", f'''
{journey("workbook.html")}
<section class="sec tight-top">
  <div class="wrap wb-hero">
    <div class="reveal">
      <p class="eyebrow">Step four · At your own pace</p>
      <h1 style="font-size:clamp(3rem,6.6vw,5.6rem)">Leaving <em>Well</em></h1>
      <p class="lede">Not ready for a call? That's completely okay. Start here, privately, whenever you're ready.</p>
      <p>Leaving Well is a guided workbook that walks you through many of the same questions I explore with the people I support. It's warm, a little fun, and nothing like a form at the doctor's office. For some people it's all they need. For others it's a comfortable first step.</p>
      <div class="price-box"><span class="price">{WORKBOOK_PRICE}</span><span class="small">Fillable, printable PDF · 16 pages</span></div>
      <div class="btn-row" style="margin-top:18px">{buy}</div>
    </div>
    <img class="book reveal" src="img/workbook-cover.jpg" alt="The Leaving Well workbook cover, a dusk gradient from deep midnight into warm apricot">
  </div>
</section>

<section class="sec tone-sage">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">What's inside</p><h2>Eight short sections, <em>any order</em></h2><p class="small" style="margin-top:14px">Plus twelve story prompts, a resource guide for DC, Virginia, Florida and North Carolina, and room for notes.</p></div></div>
    <ul class="main inside reveal">
      <li><i>01</i><div><b>The Basics</b><span>The practical page, out of the way first.</span></div></li>
      <li><i>02</i><div><b>What Matters Most</b><span>The human stuff before the medical stuff.</span></div></li>
      <li><i>03</i><div><b>How I Want to Be Cared For</b><span>Your wishes in your own words.</span></div></li>
      <li><i>04</i><div><b>My People</b><span>Who you want close and who you trust.</span></div></li>
      <li><i>05</i><div><b>Setting the Room</b><span>The soundtrack, the light, the feeling.</span></div></li>
      <li><i>06</i><div><b>The Stories</b><span>What you've learned and what goes to whom.</span></div></li>
      <li><i>07</i><div><b>After I'm Gone</b><span>How you'd like to be remembered.</span></div></li>
      <li><i>08</i><div><b>Where Things Live</b><span>No digging through the junk drawer.</span></div></li>
    </ul>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="center"><p class="eyebrow">Take a peek</p><h2>Three sample <em>pages</em></h2><p class="small">Tap any page to see it full size.</p></div>
    <div class="samples">
      <figure class="reveal"><a href="img/workbook-sample-1.jpg" target="_blank" rel="noopener"><img src="img/workbook-sample-1.jpg" alt="Sample page titled First, a promise, explaining that this is not a form at the doctor's office"></a><figcaption>First, a promise</figcaption></figure>
      <figure class="reveal"><a href="img/workbook-sample-3.jpg" target="_blank" rel="noopener"><img src="img/workbook-sample-3.jpg" alt="Sample page titled How I Want to Be Cared For, with choices about where to be at the end, comfort or clarity, and treatments to welcome or skip"></a><figcaption>How I Want to Be Cared For</figcaption></figure>
      <figure class="reveal"><a href="img/workbook-sample-2.jpg" target="_blank" rel="noopener"><img src="img/workbook-sample-2.jpg" alt="Sample page titled Setting the Room, with prompts for the soundtrack, light and atmosphere, touch and words"></a><figcaption>Setting the Room</figcaption></figure>
    </div>
  </div>
</section>

<section class="sec tone-blush">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">Good to know</p><h2>If you'd like <em>more support later</em></h2></div></div>
    <div class="main reveal">
      <p class="lede">The workbook is included with all of my doula support. If you start with it on your own and later decide you'd like to work together, the cost of the workbook comes off your first invoice.</p>
      <div class="credit"><span class="ico">✓</span><div><b style="font-family:var(--serif);font-size:1.3rem;font-weight:600">Your workbook counts toward services</b><br><span class="small">Just mention it when we talk.</span></div></div>
      <p class="small" style="margin-top:22px">Leaving Well is for reflection and planning. It isn't a legal document, and your answers stay with you.</p>
    </div>
  </div>
</section>
{nxt("contact.html", "Whenever you're ready", "Say hello on a <em>free call</em>")}
''')

# ---------------------------------------------------------------- CONTACT
P["contact.html"] = ("Free consultation | Everything Is Already All Right",
"Book a free 20-minute consultation with Jason O'Malley, end-of-life doula.", '''
<section class="sec tight-top">
  <div class="wrap contact-grid">
    <div class="side">
      <p class="eyebrow">Free 20-minute consultation</p>
      <h1 style="font-size:clamp(2.8rem,6vw,4.8rem)">Let's just <em>say hello.</em></h1>
      <p class="lede">Tell me a little about what's going on and I'll reach out to find a time to talk.</p>
      <div class="expect">
        <div><i>i.</i><span>We get to know each other</span></div>
        <div><i>ii.</i><span>You ask anything you like</span></div>
        <div><i>iii.</i><span>We talk about what support could look like and what it costs</span></div>
        <div><i>iv.</i><span>You decide what's next, with no pressure at all</span></div>
      </div>
      <p class="eyebrow" style="margin-top:40px">Rather talk now?</p>
      <a class="phone-big" href="tel:+19177532905">(917) 753-2905</a>
      <p class="small">Call or text. If I don't pick up, I'm probably with someone, and I'll get back to you.</p>
      <div class="privacy"><b>A note on privacy.</b> What you share stays with me. Please keep medical details out of this form. We can talk about specifics on the phone.</div>
    </div>
    <form class="form" id="contactForm">
      <input type="hidden" name="access_key" value="19f84a20-0e99-46cd-95c0-8a7e95db971e">
      <input type="hidden" name="subject" value="New doula inquiry from the website">
      <input type="hidden" name="from_name" value="Everything Is Already All Right">
      <input type="checkbox" name="botcheck" style="display:none">
      <div class="field"><label for="name">Your name</label><input id="name" name="name" required autocomplete="name"></div>
      <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email"></div>
      <div class="field"><label for="phone">Phone <span class="small">(optional)</span></label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
      <div class="field"><span class="lab">Who is this for?</span>
        <div class="chips">
          <label><input type="radio" name="for" value="Me"><span>Me</span></label>
          <label><input type="radio" name="for" value="Someone I love"><span>Someone I love</span></label>
          <label><input type="radio" name="for" value="A pet"><span>A pet</span></label>
          <label><input type="radio" name="for" value="I work in care"><span>I work in care</span></label>
        </div>
      </div>
      <div class="field"><span class="lab">What would you like to talk about?</span>
        <div class="chips">
          <label><input type="checkbox" name="interest[]" value="Just saying hello"><span>Just saying hello</span></label>
          <label><input type="checkbox" name="interest[]" value="Doula support"><span>Doula support</span></label>
          <label><input type="checkbox" name="interest[]" value="Legacy film"><span>A legacy film</span></label>
          <label><input type="checkbox" name="interest[]" value="Workbook" id="int-workbook"><span>The workbook</span></label>
        </div>
      </div>
      <div class="field"><label for="msg">Anything you'd like me to know</label><textarea id="msg" name="message" placeholder="A few lines is plenty."></textarea></div>
      <button class="btn" type="submit">Send</button>
      <p class="form-note">I'll only use your information to get back to you.</p>
      <p class="form-status" id="formStatus" role="status"></p>
    </form>
  </div>
</section>
''')

# ---------------------------------------------------------------- RESOURCES
P["resources.html"] = ("Resources | Everything Is Already All Right",
"Advance directive resources for DC, Virginia, Florida and North Carolina.", '''
<section class="sec tight-top">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">Resources</p><h1 style="font-size:clamp(2.8rem,5.4vw,4.4rem)">Make it <em>official</em></h1><p class="small">An advance directive lets you name who speaks for you and write down your medical wishes. Every state has its own version, so always check the official source.</p></div></div>
    <div class="main res-list">
      <div><b>CaringInfo</b><p>Free advance directive forms for every state. Helpline 800-658-8898.</p><a href="https://www.caringinfo.org/planning/advance-directives/by-state/">https://www.caringinfo.org/planning/advance-directives/by-state/</a></div>
      <div><b>The Conversation Project</b><p>Free guides for talking with family about what matters.</p><a href="https://theconversationproject.org">https://theconversationproject.org</a></div>
      <div><b>DC MOST form</b><p>Medical orders for people who are seriously ill in DC. Ask your doctor.</p><a href="https://dchealth.dc.gov/most">https://dchealth.dc.gov/most</a></div>
      <div><b>Virginia Advance Directive Registry</b><p>Store yours so providers can find it.</p><a href="https://www.connectvirginia.org/adr/">https://www.connectvirginia.org/adr/</a></div>
      <div><b>Florida advance directives</b><p>Living will, health care surrogate and donation forms.</p><a href="https://quality.healthfinder.fl.gov/report-guides/advance-directives">https://quality.healthfinder.fl.gov/report-guides/advance-directives</a></div>
      <div><b>North Carolina Advance Health Care Directive Registry</b><p>Documents must be notarized to register.</p><a href="https://www.sosnc.gov/ahc">https://www.sosnc.gov/ahc</a></div>
      <div class="privacy">These links go to outside organizations. I'm not a lawyer or a medical provider, so when in doubt, ask your doctor, hospice team or an attorney.</div>
    </div>
  </div>
</section>
''')

for fname, (title, desc, body) in P.items():
    with open(fname, "w") as f:
        f.write(head(title, desc, fname) + body + FOOT)
print("built", len(P))
