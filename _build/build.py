"""Stamp shared head / nav / contact / footer into each page body.
Each body file starts with:  <!--meta page|Title|Description-->
"""
import glob, os, re, sys

SRC = os.path.join(os.path.dirname(__file__), "pages")
OUT = sys.argv[1]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" href="assets/oeos-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body data-page="{page}">

<nav id="nav">
  <div class="wrap">
    <a href="index.html" class="brand"><img class="logo" src="assets/oeos-mark.png" alt="">One Eyed Octopus</a>
    <div class="links" id="links">
      <a href="index.html#games" data-page="games">Games</a>
      <a href="itihaas.html" data-page="itihaas">Itihaas</a>
      <a href="work.html" data-page="work">Work with us</a>
      <a href="studio.html" data-page="studio">Studio</a>
    </div>
    <a href="#contact" class="btn btn-primary">Contact</a>
    <button class="menu-btn" id="menuBtn" aria-label="Open menu">&#9776;</button>
  </div>
</nav>
"""

FOOT = """
<section class="contact site-contact" id="contact">
  <div class="wrap">
    <div class="cta-box reveal">
      <img class="octo logo" src="assets/oeos-mark.png" alt="">
      <span class="eyebrow">Contact</span>
      <h2>Let's build something together.</h2>
      <p class="lede">Investors, partners, press and studios: we'd love to hear from you.</p>
      <p style="margin-top:22px"><a href="mailto:oeostudios@gmail.com" class="btn btn-primary">oeostudios@gmail.com</a></p>
      <div class="people">
        <div class="person"><h4>Harsh Modi</h4><p>Business Development</p><a href="tel:+919029362879">+91 90293 62879</a></div>
        <div class="person"><h4>Saptesh Chaubal</h4><p>Executive Producer</p><a href="tel:+919890995327">+91 98909 95327</a></div>
        <div class="person"><h4>Vivek Vasudevan</h4><p>Creative Director</p><a href="tel:+61451200069">+61 451 200 069</a></div>
      </div>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <span>&copy; <span id="yr">2026</span> One Eyed Octopus Studios &middot; Made in India</span>
    <div class="footer-links">
      <a href="index.html#games">Games</a><a href="work.html">Work with us</a><a href="apps.html">Apps</a><a href="studio.html">Studio</a>
      <!-- TODO: add social links (Instagram, LinkedIn, X, Discord) -->
    </div>
  </div>
</footer>

<script src="assets/site.js"></script>
</body>
</html>
"""

for f in sorted(glob.glob(os.path.join(SRC, "*.html"))):
    body = open(f, encoding="utf-8").read()
    m = re.match(r"<!--meta ([\w-]+)\|(.*?)\|(.*?)-->\r?\n", body)
    page, title, desc = m.groups()
    html = HEAD.format(title=title, desc=desc, page=page) + body[m.end():] + FOOT
    name = os.path.basename(f)
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(html)
    print("built", name)
