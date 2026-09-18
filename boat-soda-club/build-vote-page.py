#!/usr/bin/env python3
"""Assemble the sticker-vote page, inlining each decal as a namespaced <symbol>."""
import re, os

SRC = os.path.dirname(os.path.abspath(__file__))
PIECES = [
    ("a", "brbsc-roundel-4.5in.svg", "0 0 1000 1000"),
    ("b", "brbsc-crest-4x5in.svg",   "0 0 800 1000"),
    ("c", "brbsc-banner-6x2in.svg",  "0 0 1200 400"),
    ("d", "brbsc-mini-2in.svg",      "0 0 600 600"),
]

def symbolize(key, fname, viewbox):
    s = open(os.path.join(SRC, fname)).read()
    inner = s[s.index(">", s.index("<svg")) + 1 : s.rindex("</svg>")]
    inner = re.sub(r"<(title|desc)>.*?</\1>", "", inner, flags=re.S)
    # namespace every id and every reference to one
    ids = set(re.findall(r'id="([^"]+)"', inner))
    for i in sorted(ids, key=len, reverse=True):
        p = f"{key}-{i}"
        inner = inner.replace(f'id="{i}"', f'id="{p}"')
        inner = inner.replace(f'href="#{i}"', f'href="#{p}"')
        inner = inner.replace(f'url(#{i})', f'url(#{p})')
    return f'<symbol id="sk-{key}" viewBox="{viewbox}">{inner}</symbol>'

SYMBOLS = "".join(symbolize(*p) for p in PIECES)
DIMS = {k: vb.split()[2:] for k, _, vb in PIECES}

def art(key, label):
    w, h = DIMS[key]
    return (f'<svg class="art" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">'
            f'<use href="#sk-{key}" x="0" y="0" width="{w}" height="{h}"/></svg>')

OPTIONS = [
    ("a", "The Roundel", "4.5&Prime; circle",
     "The whole scene: sunset over the pines, a tallboy standing in the river, club name around the ring. Made for the middle of a lid."),
    ("b", "The Crest", "4 &times; 5&Prime; shield",
     "Same idea, louder. The name does the work instead of the picture, and the ribbon carries the line."),
    ("c", "The Banner", "6 &times; 2&Prime;",
     "Wide and low for the front of the cooler, where a circle just floats in the middle of nothing."),
    ("d", "The Mini", "2&Prime; circle",
     "BRBSC and nothing else. Small enough for a tumbler, a rod tube, or the back glass of the truck."),
]

cards = "\n".join(f'''      <li class="opt">
        <div class="chip" aria-hidden="true">{k.upper()}</div>
        <div class="board">{art(k, name + " sticker design")}</div>
        <div class="say">
          <h2>{name}</h2>
          <p class="size">{size}</p>
          <p class="blurb">{blurb}</p>
        </div>
      </li>''' for k, name, size, blurb in OPTIONS)

COOLER_LID = '''<svg class="cooler" viewBox="0 0 600 430" role="img" aria-label="Cooler lid seen from above with the roundel centered">
        <ellipse cx="300" cy="404" rx="234" ry="16" fill="#04121e" opacity=".5"/>
        <rect x="58" y="52" width="484" height="330" rx="40" fill="#9aa3ab"/>
        <rect x="58" y="52" width="484" height="322" rx="40" fill="#c3cad1"/>
        <rect x="80" y="72" width="440" height="282" rx="30" fill="#b3bbc3"/>
        <rect x="100" y="90" width="400" height="246" rx="22" fill="#bcc4cb"/>
        <g fill="#8d969e">
          <rect x="120" y="108" width="64" height="12" rx="6"/><rect x="416" y="108" width="64" height="12" rx="6"/>
          <rect x="120" y="306" width="64" height="12" rx="6"/><rect x="416" y="306" width="64" height="12" rx="6"/>
        </g>
        <use href="#sk-a" x="188" y="101" width="224" height="224"/>
        <rect x="58" y="52" width="484" height="322" rx="40" fill="none" stroke="#8a939b" stroke-width="3"/>
      </svg>'''

COOLER_FRONT = '''<svg class="cooler" viewBox="0 0 600 430" role="img" aria-label="Cooler seen from the front with the banner on the body">
        <ellipse cx="300" cy="404" rx="226" ry="15" fill="#04121e" opacity=".5"/>
        <path d="M96,166 H504 L486,368 Q484,384 468,384 H132 Q116,384 114,368 Z" fill="#b3bbc3"/>
        <path d="M96,166 H504 L498,232 H102 Z" fill="#bcc4cb"/>
        <rect x="84" y="104" width="432" height="62" rx="22" fill="#c9d0d6"/>
        <rect x="84" y="104" width="432" height="26" rx="13" fill="#d4dade"/>
        <line x1="96" y1="166" x2="504" y2="166" stroke="#8f989f" stroke-width="3"/>
        <rect x="70" y="196" width="30" height="74" rx="14" fill="#8d969e"/>
        <rect x="500" y="196" width="30" height="74" rx="14" fill="#8d969e"/>
        <g fill="#3f464d"><rect x="186" y="140" width="54" height="86" rx="14"/><rect x="360" y="140" width="54" height="86" rx="14"/></g>
        <g fill="#6d757c"><rect x="198" y="152" width="30" height="20" rx="8"/><rect x="372" y="152" width="30" height="20" rx="8"/></g>
        <use href="#sk-c" x="186" y="258" width="228" height="76"/>
        <circle cx="470" cy="344" r="15" fill="#8d969e"/><circle cx="470" cy="344" r="7" fill="#6d757c"/>
        <rect x="140" y="384" width="74" height="14" rx="6" fill="#6d757c"/>
        <rect x="386" y="384" width="74" height="14" rx="6" fill="#6d757c"/>
      </svg>'''

HTML = f'''<title>Boat Soda Sticker Vote</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Barlow:wght@400;500;600;700&display=swap">
<style>
  :root{{
    --navy:#071E31; --navy-2:#0B2B45; --navy-3:#0f3a5c;
    --cream:#F7E7C6; --cream-dim:#c3cfd8;
    --orange:#F2711C; --gold:#F6A623; --teal:#2FA0A0;
    --board:#d8c9a8; --board-2:#d2c19d;
    --display:"Alfa Slab One",Rockwell,"Roboto Slab",Georgia,serif;
    --body:"Barlow","Helvetica Neue",Helvetica,Arial,sans-serif;
  }}
  *{{box-sizing:border-box}}
  body{{
    margin:0; background:var(--navy);
    background-image:repeating-linear-gradient(135deg,#0B2B45 0 34px,#0c3050 34px 68px);
    color:var(--cream); font-family:var(--body); font-size:17px; line-height:1.55;
    -webkit-font-smoothing:antialiased;
  }}
  .wrap{{max-width:760px; margin:0 auto; padding-inline:16px}}
  h1,h2{{font-family:var(--display); font-weight:400; text-wrap:balance; margin:0}}
  p{{margin:0}}

  .mast{{
    padding-block:44px 34px; text-align:center;
    border-bottom:4px solid var(--orange);
    background:linear-gradient(180deg,rgba(7,30,49,.4),rgba(7,30,49,.92));
  }}
  .eyebrow{{
    font-size:12px; font-weight:700; letter-spacing:.22em; text-transform:uppercase;
    color:var(--gold); margin-bottom:14px;
  }}
  .mast h1{{font-size:clamp(34px,8vw,54px); line-height:1.04; letter-spacing:-.5px}}
  .mast .lede{{margin:16px auto 0; max-width:34em; color:var(--cream-dim); font-size:clamp(16px,2.4vw,18px)}}

  .ballot{{list-style:none; margin:0; padding:0; display:grid; gap:24px; padding-block:34px}}
  .opt{{
    display:grid; grid-template-columns:auto 1fr; gap:10px 16px;
    align-items:start;
    background:var(--navy-2); border:1px solid rgba(247,231,198,.14);
    border-radius:18px; padding:18px;
  }}
  .chip{{
    grid-row:1; grid-column:1;
    width:56px; height:56px; border-radius:50%;
    background:var(--orange); color:#fff;
    font-family:var(--display); font-size:28px; line-height:56px; text-align:center;
    box-shadow:0 4px 14px rgba(0,0,0,.4);
  }}
  .board{{
    grid-row:1; grid-column:2;
    background:repeating-linear-gradient(90deg,var(--board) 0 64px,var(--board-2) 64px 66px),var(--board);
    border-radius:12px; padding:20px; display:flex; justify-content:center;
  }}
  .art{{width:100%; max-width:100%; height:auto; filter:drop-shadow(0 6px 12px rgba(0,0,0,.26))}}
  .opt:nth-child(1) .art{{max-width:310px}}
  .opt:nth-child(2) .art{{max-width:245px}}
  .opt:nth-child(4) .art{{max-width:190px}}
  .say{{grid-row:2; grid-column:2}}
  .say h2{{font-size:26px; line-height:1.1}}
  .size{{
    font-size:12px; font-weight:700; letter-spacing:.16em; text-transform:uppercase;
    color:var(--teal); margin-top:5px;
  }}
  .blurb{{margin-top:9px; color:var(--cream-dim)}}

  .onit{{padding-block:34px; border-top:1px solid rgba(247,231,198,.14)}}
  .onit h2{{font-size:24px}}
  .onit .note{{margin-top:8px; color:var(--cream-dim)}}
  .pair{{display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:20px}}
  .shot{{background:var(--navy-2); border:1px solid rgba(247,231,198,.14); border-radius:16px; padding:14px}}
  .cooler{{width:100%; height:auto; display:block}}
  .shot figcaption{{
    margin-top:10px; font-size:12px; font-weight:700; letter-spacing:.13em;
    text-transform:uppercase; color:var(--cream-dim); text-align:center;
  }}

  .close{{
    margin-block:8px 44px; text-align:center;
    border:2px dashed rgba(242,113,28,.6); border-radius:18px; padding:28px 20px;
    background:rgba(11,43,69,.6);
  }}
  .close h2{{font-size:clamp(24px,5vw,32px)}}
  .letters{{
    display:flex; justify-content:center; gap:12px; flex-wrap:wrap; margin-top:18px;
    font-family:var(--display); font-size:30px; color:var(--gold);
  }}
  .letters span{{
    width:58px; height:58px; line-height:58px; border-radius:50%;
    border:2px solid rgba(246,166,35,.5);
  }}
  .close p{{margin-top:16px; color:var(--cream-dim)}}

  footer{{
    border-top:4px solid var(--orange); background:var(--navy-2);
    text-align:center; padding-block:22px; font-size:13px; letter-spacing:.1em;
    text-transform:uppercase; color:var(--cream-dim);
  }}

  @media (max-width:560px){{
    .opt{{grid-template-columns:1fr; gap:14px}}
    .chip{{grid-row:1; grid-column:1}}
    .board{{grid-row:2; grid-column:1}}
    .say{{grid-row:3; grid-column:1}}
    .pair{{grid-template-columns:1fr}}
  }}
  @media (prefers-reduced-motion:reduce){{*{{animation:none!important;transition:none!important}}}}
</style>

<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">{SYMBOLS}</svg>

<header class="mast">
  <div class="wrap">
    <div class="eyebrow">Broad River Boat Soda Club</div>
    <h1>Pick the sticker</h1>
    <p class="lede">Four designs for the coolers. Have a look, then text your letter to the group.</p>
  </div>
</header>

<main class="wrap">
  <ol class="ballot">
{cards}
  </ol>

  <section class="onit">
    <h2>On the cooler</h2>
    <p class="note">A 45-quart rotomolded cooler, so you can judge it at the size it will actually live.</p>
    <div class="pair">
      <figure class="shot">{COOLER_LID}<figcaption>Roundel on the lid</figcaption></figure>
      <figure class="shot">{COOLER_FRONT}<figcaption>Banner on the front</figcaption></figure>
    </div>
  </section>

  <section class="close">
    <h2>Text your letter to the group</h2>
    <div class="letters"><span>A</span><span>B</span><span>C</span><span>D</span></div>
    <p>Whichever wins goes on the coolers. Nothing says we can&rsquo;t print the runner-up for the truck.</p>
  </section>
</main>

<footer>If anybody asks, it&rsquo;s a soda</footer>
'''

out = os.path.join(SRC, "vote-page.html")
open(out, "w").write(HTML)
print("wrote", out, len(HTML), "bytes")
