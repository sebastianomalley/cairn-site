# Builds every page from one shared header, journey rail and footer.
# Run: python3 build.py
import re

# Paste your Stripe Payment Link here when it's ready. Until then the button says "Coming soon".
STRIPE_LINK = ""
WORKBOOK_PRICE = "$19"

# Book links. Each book shows two buttons, Bookshop.org and Amazon.
# Once you have accounts:
#   BOOKSHOP_ID = your Bookshop.org affiliate ID (the number in https://bookshop.org/a/12345/...)
#   AMAZON_TAG  = your Amazon Associates tracking tag (looks like yourname-20)
# Or paste a specific link for one title in BOOKSHOP_LINKS / AMAZON_LINKS.
BOOKSHOP_ID = "132116"
AMAZON_TAG = ""
BOOKSHOP_LINKS = {}
AMAZON_LINKS = {}

def affiliate_note():
    parts = []
    if BOOKSHOP_ID or BOOKSHOP_LINKS or AMAZON_TAG or AMAZON_LINKS:
        parts.append("Some of these are affiliate links. If you buy through them I may earn a small commission, at no extra cost to you.")
    if AMAZON_TAG or AMAZON_LINKS:
        parts.append("As an Amazon Associate I earn from qualifying purchases.")
    parts.append("Bookshop.org supports independent bookstores.")
    return " ".join(parts)

def _q(title, author):
    from urllib.parse import quote_plus
    return quote_plus(title + " " + author.split(" and ")[0])

# Each book's paperback ISBN, so the buttons open the book itself, not a search.
ISBNS = {
    "Final Gifts": "9781451667257",
    "Being Mortal": "9781250076229",
    "A Beginner's Guide to the End": "9781501157219",
    "The Art of Dying Well": "9781501135477",
    "Gone from My Sight": "9780962160318",
    "It's OK That You're Not OK": "9781622039074",
    "The Wild Edge of Sorrow": "9781583949764",
    "The Invisible String": "9780316486231",
    "Lifetimes": "9780553344028",
    "Goodbye, Friend": "9781608680863",
    "Smoke Gets in Your Eyes": "9780393351903",
}

# Bookshop doesn't stock these, so their Bookshop button falls back to a search.
NOT_ON_BOOKSHOP = {"Gone from My Sight"}

def _isbn10(isbn13):
    core = isbn13[3:12]
    s = sum((10 - i) * int(d) for i, d in enumerate(core)) % 11
    c = (11 - s) % 11
    return core + ("X" if c == 10 else str(c))

def bookshop_link(title, author):
    if title in BOOKSHOP_LINKS: return BOOKSHOP_LINKS[title]
    isbn = ISBNS.get(title) if title not in NOT_ON_BOOKSHOP else None
    if isbn:
        return f"https://bookshop.org/a/{BOOKSHOP_ID}/{isbn}" if BOOKSHOP_ID else f"https://bookshop.org/book/{isbn}"
    url = "https://bookshop.org/search?keywords=" + _q(title, author)
    if BOOKSHOP_ID: url += "&a_aid=" + BOOKSHOP_ID
    return url

def amazon_link(title, author):
    if title in AMAZON_LINKS: return AMAZON_LINKS[title]
    isbn = ISBNS.get(title)
    url = ("https://www.amazon.com/dp/" + _isbn10(isbn)) if isbn else ("https://www.amazon.com/s?k=" + _q(title, author) + "&i=stripbooks")
    if AMAZON_TAG: url += ("&" if "?" in url else "?") + "tag=" + AMAZON_TAG
    return url

# Real cover images go here once Bookshop approves you, e.g. COVER_IMAGES["Final Gifts"] = "https://...".
COVER_IMAGES = {}
# Show the cover images Bookshop serves for each ISBN. If one fails to load, the colored placeholder shows instead.
USE_BOOKSHOP_COVERS = True
_SPINES = ["#3E3352", "#8E5E6E", "#6F7F6A", "#C98A6B", "#5B4A72", "#A7766B", "#4F6470", "#B98B5E"]
_book_n = [0]

def book(title, author, why):
    i = _book_n[0]; _book_n[0] += 1
    tilt = (-3, 2, -1.5, 3, -2, 1.5)[i % 6]
    spine = (f'<span class="st">{title}</span><span class="sa">{author.split(" and ")[0].split()[-1]}</span>')
    src = COVER_IMAGES.get(title)
    if not src and USE_BOOKSHOP_COVERS and ISBNS.get(title) and title not in NOT_ON_BOOKSHOP:
        src = f"https://images-us.bookshop.org/ingram/{ISBNS[title]}.jpg?width=300"
    img = (f'<img src="{src}" alt="Cover of {title}" loading="lazy" onerror="this.remove()">' if src else "")
    cover = (f'<span class="cover spine" style="--c:{_SPINES[i % len(_SPINES)]};--t:{tilt}deg">{spine}{img}</span>')
    return (f'<li>{cover}<div class="info"><b><i>{title}</i></b><span class="by">{author}</span><span class="why">{why}</span>'
            f'<span class="buy"><a href="{bookshop_link(title, author)}" target="_blank" rel="noopener sponsored">Bookshop.org</a>'
            f'<a href="{amazon_link(title, author)}" target="_blank" rel="noopener sponsored">Amazon</a></span></div></li>')

import hashlib as _h
CSS_V = _h.md5(open("css/style.css","rb").read()).hexdigest()[:8]

STEPS = [
    ("what-is-a-doula.html", "One", "Understand", "What a doula is"),
    ("ways-i-help.html", "Two", "Explore", "Ways I can help"),
    ("how-it-works.html", "Three", "Connect", "How it works"),
    ("resources.html", "Four", "At your pace", "Free guide and workbook"),
]
NAV = [("what-is-a-doula.html", "What is a doula"), ("ways-i-help.html", "Ways I help"),
       ("how-it-works.html", "How it works"), ("resources.html", "Resources"), ("about.html", "About")]

ORBS = '<div class="orbs" aria-hidden="true"><span></span><span></span><span></span></div>'


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
<link rel="icon" href="img/eiaar-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;1,400;1,600&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v={CSS_V}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="mock-bar">Preview build. Not public yet.</div>
<header class="head">
  <div class="wrap">
    <a class="brand" href="doula.html" aria-label="Everything Is Already All Right, end-of-life doula care, home"><img src="img/eiaar-doula-horizontal-ink.svg" alt="Everything Is Already All Right, end-of-life doula care" width="240" height="64"></a>
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


def nxt(href, kicker, title, cls=""):
    return (f'<a class="next-band {cls}" href="{href}"><span class="wrap"><span><span class="k">{kicker}</span>'
            f'<span class="t">{title}</span></span><span class="circle" aria-hidden="true">→</span></span></a>')


FOOT = '''
</main>
<footer class="foot">
  <div class="wrap">
    <div class="row">
      <div>
        <a class="brand" href="doula.html" aria-label="End-of-life doula care home"><img src="img/eiaar-doula-horizontal-cream.svg" alt="Everything Is Already All Right, end-of-life doula care" width="240" height="64"></a>
        <p style="margin-top:20px;max-width:38ch">Non-medical end-of-life support in Washington, DC, Northern Virginia, Florida and North Carolina, with virtual support anywhere. Every faith, culture and family welcome.</p>
      </div>
      <div><h4>The path</h4><a href="what-is-a-doula.html">What is a doula</a><a href="ways-i-help.html">Ways I can help</a><a href="how-it-works.html">How it works</a><a href="resources.html">Resources</a><a href="workbook.html">The workbook</a></div>
      <div><h4>Reach me</h4><a href="contact.html">Free consultation</a><a href="tel:+19177532905">(917) 753-2905</a><a href="downloads/what-is-a-death-doula-guide.pdf">Free guide</a><a href="about.html">About Jason</a></div>
    </div>
    <div class="fine"><span>&copy; <span id="year">2026</span> <a href="index.html" style="display:inline;color:inherit">Everything Is Already All Right</a></span><span>Doulas provide non-medical support. Nothing on this site is medical or legal advice.</span></div>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
'''

P = {}

# ---------------------------------------------------------------- HOME
P["doula.html"] = ("End-of-Life Doula Care | Everything Is Already All Right",
"Warm, non-medical end-of-life doula support for people of every faith, culture and family in DC, Northern Virginia, Florida and North Carolina.", f'''
<section class="hero">
  {ORBS}
  <div class="inner">
    <p class="eyebrow">End-of-life doula care</p>
    <h1>You don't have to do this <em>alone.</em></h1>
    <p class="lede">Warm, steady company for the end of a life, and for the people who love them. Whatever you believe, wherever you come from, you're welcome here.</p>
    <div class="btn-row">
      <a class="btn btn-gold" href="what-is-a-doula.html">Start here</a>
      <a class="btn btn-line" href="contact.html">Say hello</a>
    </div>
  </div>
</section>
<section class="sec tone-sage">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">So glad you're here</p><h2>This might be for you <em>if...</em></h2><p class="side-note">Nothing here asks you to commit to anything. Take it one step at a time.</p></div></div>
    <ul class="main fit-list reveal">
      <li>You or someone you love has received a hard diagnosis</li>
      <li>You're caring for a parent, partner or friend and feeling stretched thin</li>
      <li>Hospice is involved, and you'd like more time and support around it</li>
      <li>You want your wishes written down while there's no rush</li>
      <li>You're not sure what to expect at the end and want someone steady beside you</li>
      <li>Your family has its own faith, culture or traditions you want honored</li>
      <li>You've lost someone and don't know where to start</li>
      <li class="fit-aside">Saying goodbye to an animal companion? I'm trained in that too. <a href="ways-i-help.html#animals">Here's how I help</a></li>
    </ul>
  </div>
</section>

<section class="sec tone-peach" style="padding-bottom:70px">
  <div class="narrow center">
    <p class="eyebrow">Where would you like to begin?</p>
    <h2>Three gentle <em>ways in</em></h2>
  </div>
</section>
<div class="paths">
  <a class="path p1" href="what-is-a-doula.html"><span class="step-n">If you're curious</span><h3>Learn what a doula is</h3><p>What it looks like, how it fits with hospice, and why families bring one in.</p><span class="go arrow">Start reading </span></a>
  <a class="path p2" href="contact.html"><span class="step-n">If you'd like to talk</span><h3>A free 20-minute call</h3><p>Say hello, ask anything and get to know each other. No pressure and no script.</p><span class="go arrow">Book a time </span></a>
  <a class="path p3" href="resources.html"><span class="step-n">If you'd rather go slow</span><h3>Start on your own</h3><p>A free guide to read, and the Leaving Well workbook to fill in privately, at your own pace.</p><span class="go arrow">See resources </span></a>
</div>

<section class="sec tone-dusk">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">For everyone</p><h2>Every faith, every family, <em>every way of saying goodbye.</em></h2></div></div>
    <div class="main reveal">
      <p class="lede">There's no one right way to die, grieve or remember. Your beliefs, your culture and your family's traditions lead. I follow.</p>
      <p class="muted-on-dark">I'll take the time to learn what matters to you, and help bring in the people and practices that make it feel like yours, from your faith leader to your grandmother's prayers to the music you grew up on.</p>
    </div>
  </div>
</section>

<section class="sec center tone-lav">
  <div class="wrap">
    <p class="quote">"I'm not here to fix anything. I'm here to show up, and to make sure you don't have to do this alone."</p>
    <p class="quote-by">Jason O'Malley</p>
  </div>
</section>
''')

# ---------------------------------------------------------------- STEP 1
P["what-is-a-doula.html"] = ("What is a death doula? | Everything Is Already All Right",
"What an end-of-life doula is, what it looks like, how it differs from hospice and why families bring one in.", f'''
<section class="hero small">
  {ORBS}
  <div class="inner">
    <p class="eyebrow">Step one · Understand</p>
    <h1>What exactly is a <em>death doula?</em></h1>
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

<section class="sec tone-sage">
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
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">Part of the team</p><h2>One more person <em>in your corner</em></h2></div></div>
    <div class="main reveal">
      <p class="lede">I work alongside everyone involved in your care. Your doctors, nurses, hospice team, faith leaders and family all stay right where they are. I don't replace anyone. I add another layer of support, and help everyone stay connected to what you want.</p>
      <div class="who" style="grid-template-columns:repeat(2,1fr);margin-top:30px">
        <div><h4>Doctors and nurses</h4><p>Your medical care, diagnosis and treatment.</p></div>
        <div><h4>Hospice and palliative care</h4><p>Comfort-focused medical care, at home or in a facility.</p></div>
        <div><h4>Chaplains and faith leaders</h4><p>Spiritual care within your tradition. I'm glad to work right alongside yours.</p></div>
        <div><h4>Social workers</h4><p>Resources, benefits and the practical systems around care.</p></div>
        <div><h4>Family and friends</h4><p>The heart of it all. My job is to support them, never to replace them.</p></div>
        <div><h4>Your doula</h4><p>Non-medical companionship, planning and presence for you and everyone around you.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="sec tone-sand">
  <div class="wrap">
    <div class="narrow center" style="margin-bottom:50px">
      <p class="eyebrow">A common question</p>
      <h2>Isn't that what <em>hospice</em> does?</h2>
      <p class="lede">It's one of the questions I hear most. The short answer is no, and the two work beautifully together. Hospice provides medical comfort care. A doula offers time, companionship and practical support. Here's the difference.</p>
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
  </div>
</section>

<section class="sec tone-peach">
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
  {ORBS}
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
      <div class="item"><span class="when">Before</span><h3>Help with the paperwork</h3><p>Advance directives, naming a health care agent, talking with your doctor about a POLST or MOST form, organ donation, funeral pre-planning, and pulling together where important papers live. I walk you through it and help get it to the right people. I'm not a lawyer, so legal questions go to one.</p></div>
      <div class="item"><span class="when">During</span><h3>Companioning visits</h3><p>Regular time together for conversation, comfort, reading aloud or simply sitting quietly.</p></div>
      <div class="item"><span class="when">During</span><h3>Vigil planning and presence</h3><p>Shaping the space for the final days, honoring your rituals and traditions, and keeping watch alongside your family.</p></div>
      <div class="item"><span class="when">During</span><h3>Respite for caregivers</h3><p>Someone trusted to stay close so the people caring for you can rest.</p></div>
      <div class="item"><span class="when">After</span><h3>The first hours and beyond</h3><p>Being there after a death, helping with next steps, and checking in through early grief.</p></div>
      <div class="item"><span class="when">Anytime</span><h3>Legacy projects</h3><p>Letters, recorded stories, memory books and other ways to leave something of yourself behind.</p></div>
      <div class="item feature">
        <div><span class="when">Part of vigil and legacy support</span><h3 style="font-size:2.2rem">Legacy films</h3></div>
        <div><p>Before this work I spent years behind a camera. A legacy film is a short, personal portrait of a life told in your own voice, for the people who'll want to hear it again. We talk first, film somewhere that feels right, and nothing is shared without your okay.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="sec tone-sage" id="animals">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">Companion animals</p><h2>For the animals <em>we love, too</em></h2></div></div>
    <div class="main reveal">
      <p class="lede">Most of my work is with people and the families around them. I'm also trained in companion animal end-of-life care.</p>
      <p>Losing a pet is real grief. I can help you plan a peaceful goodbye, be there at home or at the vet, and sit with you and your family afterward. Just mention it when we talk.</p>
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
  {ORBS}
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
      <div class="step"><h3>Read the free guide</h3><p>A short, friendly read with the basics and a few gentle questions to sit with.</p></div>
      <div class="step"><h3>Have a free call</h3><p>Twenty minutes to say hello, ask anything and see if we're a good fit.</p></div>
      <div class="step"><h3>Shape your plan</h3><p>We decide together what support looks like. You get a simple written agreement with the cost up front.</p></div>
      <div class="step"><h3>Begin</h3><p>We start wherever you are, and adjust as life changes.</p></div>
    </div>
  </div>
</section>

<section class="sec tone-peach">
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
        <p style="color:var(--muted)">A short, friendly read for anyone who's never heard the words "death doula." Easy to share with family.</p>
        <ul><li>What a doula is, and isn't</li><li>Questions people ask</li><li>Doula and hospice, side by side</li><li>Questions worth sitting with, no answers required</li></ul>
        <div class="btn-row" style="margin-top:26px"><a class="btn" href="downloads/what-is-a-death-doula-guide.pdf" download>Download the guide</a></div>
      </div>
      <img class="book" src="img/guide-cover.jpg" alt="Cover of the free guide, What exactly is a death doula?" style="max-width:300px;justify-self:center;transform:rotate(2deg)">
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

<div class="next-split">
{nxt("contact.html", "Ready to talk?", "Book a free <em>20-minute call</em>")}
{nxt("resources.html", "Not quite ready?", "Start at <em>your own pace</em>", "sage")}
</div>
''')

# ---------------------------------------------------------------- STEP 4
buy = (f'<a class="btn" href="{STRIPE_LINK}">Buy the workbook</a>' if STRIPE_LINK
       else '<a class="btn" href="contact.html?interest=workbook">Get the workbook</a>')
P["workbook.html"] = ("Leaving Well workbook | Everything Is Already All Right",
"Leaving Well, a guided end-of-life planning and legacy workbook you can start on your own, at your own pace.", f'''
{journey("resources.html")}
<section class="sec tight-top tone-mist">
  <div class="wrap wb-hero">
    <div class="reveal">
      <p class="small" style="margin-bottom:18px"><a href="resources.html" style="text-decoration:none">← All resources</a></p>
      <p class="eyebrow">The workbook</p>
      <h1 style="font-size:clamp(3rem,6.6vw,5.6rem)">Leaving <em>Well</em></h1>
      <p class="lede">Not ready for a call? That's completely okay. Start here, privately, whenever you're ready.</p>
      <p>Leaving Well is a guided workbook that walks you through many of the same questions I explore with the people I support. It's warm, a little fun, and nothing like a form at the doctor's office. For some people it's all they need. For others it's a comfortable first step.</p>
      <div class="price-box"><span class="price">{WORKBOOK_PRICE}</span><span class="small">Instant download · 16 pages</span></div>
      <div class="btn-row" style="margin-top:18px">{buy}</div>
      <p class="small" style="margin-top:16px">Type right into it on your computer, tablet or phone the moment it downloads, save as you go, or print it if you prefer pen and paper.</p>
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

<section class="sec tone-peach">
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
      <input type="hidden" name="from_name" value="Everything Is Already All Right website">
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
"A free guide to death doulas, the Leaving Well workbook, and advance directive resources for DC, Virginia, Florida and North Carolina.", f'''
<section class="hero small">
  {ORBS}
  <div class="inner">
    <p class="eyebrow">Step four · At your own pace</p>
    <h1>Read, reflect, <em>at your own pace.</em></h1>
    <p class="lede">Not ready for a call? That's completely okay. Start with something to read, or something to fill in.</p>
  </div>
</section>
{journey("resources.html")}

<section class="sec tone-peach">
  <div class="wrap feature">
    <img class="book reveal" src="img/guide-cover.jpg" alt="Cover of the free guide, What exactly is a death doula?">
    <div class="reveal">
      <p class="eyebrow">Free download</p>
      <h2>What exactly is a <em>death doula?</em></h2>
      <p>A short, friendly read for anyone who's never heard the words. What a doula does, how it fits with hospice, the questions people ask, and a few gentle ones to sit with. Easy to share with family.</p>
      <div class="btn-row"><a class="btn" href="downloads/what-is-a-death-doula-guide.pdf" download>Download the free guide</a></div>
    </div>
  </div>
</section>

<a class="wb-teaser" href="workbook.html">
  <span class="wrap feature flip">
    <span class="copy">
      <span class="eyebrow">The workbook · {WORKBOOK_PRICE}</span>
      <span class="h">Leaving <em>Well</em></span>
      <span class="p">A guided, fillable workbook that walks you through the same questions I explore with the people I support. What matters most, how you want to be cared for, setting the room, the stories you want told. Warm, a little fun, and nothing like a form at the doctor's office.</span>
      <span class="btn">Take a look inside</span>
    </span>
    <img class="book" src="img/workbook-cover.jpg" alt="Cover of the Leaving Well workbook">
  </span>
</a>

<section class="sec tone-lav" id="reading">
  <div class="wrap">
    <p class="eyebrow">Recommended reading</p>
    <h2>Books I <em>trust</em></h2>
    <p style="max-width:56ch">Some go-to reads for families, caregivers and anyone curious. Take what helps.</p>
    <div class="shelves"><div class="shelf"><h3>For anyone facing the end, and the people beside them</h3><ul>{book("Final Gifts", "Maggie Callanan and Patricia Kelley", "Two hospice nurses on understanding what the dying may be trying to tell us.")}{book("Being Mortal", "Atul Gawande", "A surgeon on what matters most at the end of life, and how medicine can honor it.")}{book("A Beginner's Guide to the End", "BJ Miller and Shoshana Berger", "Warm, practical and surprisingly funny. The paperwork, the care, the feelings.")}{book("The Art of Dying Well", "Katy Butler", "A clear guide to planning for a good end, stage by stage.")}{book("Gone from My Sight", "Barbara Karnes", "The small booklet many hospices hand families about the final weeks.")}{book("Smoke Gets in Your Eyes", "Caitlin Doughty", "A funny, honest look at death from a funeral director.")}</ul></div><div class="shelf-col"><div class="shelf"><h3>For grief</h3><ul>{book("It's OK That You're Not OK", "Megan Devine", "Grief without the pressure to get over it.")}{book("The Wild Edge of Sorrow", "Francis Weller", "On grief as something we carry together.")}</ul></div><div class="shelf"><h3>For children</h3><ul>{book("The Invisible String", "Patrice Karst", "A gentle picture book about staying connected to the people we love.")}{book("Lifetimes", "Bryan Mellonie and Robert Ingpen", "A simple way to talk with kids about beginnings and endings.")}</ul></div></div></div>
    <div class="shelves shelves-animals"><div class="shelf"><h3>For companion animals</h3><p class="shelf-note">For anyone saying goodbye to an animal they love.</p><ul>{book("Goodbye, Friend", "Gary Kowalski", "For anyone who has loved and lost an animal.")}</ul></div></div>
    <p class="small" style="margin-top:26px">{affiliate_note()}</p>
  </div>
</section>

<section class="sec tone-sand">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">Official forms</p><h2>Make it <em>official</em></h2><p class="small">An advance directive lets you name who speaks for you and write down your medical wishes. Every state has its own version, so always check the official source.</p></div></div>
    <div class="main res-list">
      <div><b>CaringInfo</b><p>Free advance directive forms for every state. Helpline 800-658-8898.</p><a href="https://www.caringinfo.org/planning/advance-directives/by-state/">https://www.caringinfo.org/planning/advance-directives/by-state/</a></div>
      <div><b>The Conversation Project</b><p>Free guides for talking with family about what matters.</p><a href="https://theconversationproject.org">https://theconversationproject.org</a></div>
      <div><b>DC MOST form</b><p>Medical orders for people who are seriously ill in DC. Ask your doctor.</p><a href="https://dchealth.dc.gov/most">https://dchealth.dc.gov/most</a></div>
      <div><b>Virginia Advance Directive Registry</b><p>Store yours so providers can find it.</p><a href="https://www.vdh.virginia.gov/commissioner/advance-health-care-directive-registry/">https://www.vdh.virginia.gov/commissioner/advance-health-care-directive-registry/</a></div>
      <div><b>Florida advance directives</b><p>Living will, health care surrogate and donation forms.</p><a href="https://quality.healthfinder.fl.gov/report-guides/advance-directives">https://quality.healthfinder.fl.gov/report-guides/advance-directives</a></div>
      <div><b>North Carolina Advance Health Care Directive Registry</b><p>Documents must be notarized to register.</p><a href="https://www.sosnc.gov/divisions/advance_healthcare_directives">https://www.sosnc.gov/divisions/advance_healthcare_directives</a></div>
      <div class="privacy">These links go to outside organizations. I'm not a lawyer or a medical provider, so when in doubt, ask your doctor, hospice team or an attorney.</div>
    </div>
  </div>
</section>
{nxt("contact.html", "Whenever you're ready", "Say hello on a <em>free call</em>")}
''')

P["about.html"] = ("About Jason | Everything Is Already All Right",
"Jason O'Malley, certified end-of-life doula, on why he does this work.", f'''
<section class="hero small">
  {ORBS}
  <div class="inner">
    <p class="eyebrow">About</p>
    <h1>Hi, I'm <em>Jason.</em></h1>
    <p class="lede">Certified end-of-life doula, and the person who'll be sitting with you.</p>
  </div>
</section>

<section class="sec tone-mist">
  <div class="wrap about-intro">
    <img class="about-photo reveal" src="img/jason.jpg" alt="Jason O'Malley, smiling, with a grey beard">
    <div class="reveal">
      <p class="eyebrow">My story</p>
      <h2>Death has always been <em>in my space.</em></h2>
      <p>When I was a very young boy, I climbed into my grandfather's casket to lay with him. I didn't know it then, but I was already learning how to be near death without being afraid of it.</p>
      <p>When I was 29, I lost my brother unexpectedly. He was 25. Since then I've walked alongside my father and my godmother through the end of their lives, and now my uncle as he makes his own transition.</p>
      <p>Somewhere along the way I noticed that death always seemed to find its way into my life. Instead of turning away, I started to lean in. Each time, I showed up a little more present and a little more capable.</p>
    </div>
  </div>
</section>

<section class="sec tone-peach">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">Why this work</p><h2>An honor and <em>a privilege</em></h2></div></div>
    <div class="main reveal">
      <p>When I learned that end-of-life doulas were a real thing, and that you could train to do this work, I signed up. I completed the University of Vermont's End-of-Life Doula program, and its Companion Animal End-of-Life Doula program too.</p>
      <p>It's an honor and a privilege to walk alongside someone in this space. I've seen firsthand the difference it makes to feel seen, heard and valued, not just to the last breath but beyond. That's what I bring with me.</p>
      <p>I want to be in this space, and I want to do the best job in this role that I possibly can.</p>
    </div>
  </div>
</section>

<section class="sec tone-dusk center">
  <div class="wrap">
    <p class="quote" style="color:var(--cream)">"It's not a job. It's just <em style="color:var(--gold)">who I am.</em>"</p>
    <p class="lede" style="max-width:46ch;margin:26px auto 0">I can be whatever a person needs in this space and time, even if that's just someone to sit in it with them.</p>
  </div>
</section>

<section class="sec tone-lav">
  <div class="wrap">
    <div class="center"><p class="eyebrow">The crew at home</p><h2>Peanut, Buster <em>and Juju</em></h2></div>
    <div class="dogs">
      <figure class="reveal" style="--tilt:-3deg"><img src="img/peanut.jpg" alt="Peanut, a tan Shih Tzu, lying on a stone patio with his tongue out"><figcaption>Peanut</figcaption></figure>
      <figure class="reveal" style="--tilt:2deg"><img src="img/buster.jpg" alt="Buster, a grey and white Shih Tzu, looking back over his shoulder with his tongue out"><figcaption>Buster</figcaption></figure>
      <figure class="reveal" style="--tilt:-1.5deg"><img src="img/juju.jpg" alt="Juju, a black and white pup in a red plaid harness, standing behind a pink tennis ball"><figcaption>Juju</figcaption></figure>
    </div>
    <p class="center small" style="margin-top:30px">My Shih Tzus, plus Juju, on loan from my girlfriend. They're a big part of why I trained in companion animal care too.</p>
  </div>
</section>

<section class="sec tone-sand">
  <div class="wrap split">
    <div class="side"><div class="stick"><p class="eyebrow">Training and membership</p><h2>The <em>details</em></h2></div></div>
    <div class="main res-list">
      <div><b>Certified End-of-Life Doula</b><p>University of Vermont, 2025</p><a href="https://learn.uvm.edu/program/end-of-life-doula-certificate/">https://learn.uvm.edu/program/end-of-life-doula-certificate/</a></div>
      <div><b>Companion Animal End-of-Life Doula</b><p>University of Vermont, 2026</p><a href="https://learn.uvm.edu/program/end-of-life-doula-certificate/">https://learn.uvm.edu/program/end-of-life-doula-certificate/</a></div>
      <div><b>Member, National End-of-Life Doula Alliance (NEDA)</b><p>A national nonprofit that sets standards of practice for end-of-life doulas</p><a href="https://nedalliance.org/">https://nedalliance.org/</a></div>
      <div><b>Background</b><p>Years in film, live events and teaching, which is where the legacy films come from</p></div>
      <p class="small" style="margin-top:20px">Insured as an end-of-life doula. Doulas provide non-medical support.</p>
    </div>
  </div>
</section>
{nxt("contact.html", "Whenever you're ready", "Let's say hello on a <em>free call</em>")}
''')

TONES = ["tone-mist", "tone-peach", "tone-sage", "tone-lav", "tone-sand"]
def tone_sections(body):
    out, prev, i = [], None, 0
    for m in re.finditer(r'<section class="sec([^"]*)"', body):
        cls = m.group(1)
        found = re.search(r"tone-\w+", cls)
        if found:
            prev = found.group(0); continue
        pick = next(t for t in TONES[i:] + TONES[:i] if t != prev)
        i = (TONES.index(pick) + 1) % len(TONES)
        out.append((m.start(), m.end(), f'<section class="sec{cls} {pick}"'))
        prev = pick
    for a, b, rep in reversed(out):
        body = body[:a] + rep + body[b:]
    return body

for fname, (title, desc, body) in P.items():
    with open(fname, "w") as f:
        f.write(head(title, desc, fname) + tone_sections(body) + FOOT)
print("built", len(P))
