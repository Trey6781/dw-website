#!/usr/bin/env python3
"""Generate the Boat Sodas cooler decal artwork (standalone, font-free SVG)."""
import os, math

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- palette
NAVY   = "#0B2B45"
NAVY_D = "#071E31"
CREAM  = "#F7E7C6"
CREAM_D= "#EFD39B"
ORANGE = "#F2711C"
CORAL  = "#E14A32"
TEAL   = "#16787D"
TEAL_L = "#2FA0A0"
WHITE  = "#FFFFFF"

# ------------------------------------------------- custom letterforms
# Each glyph is drawn on a 62 x 100 box (baseline y=100, cap top y=0).
GLYPHS = {
"B": 'M0,0 H37 C52,0 62,11 62,25 C62,39 52,50 37,50 C52,50 62,61 62,75 '
     'C62,89 52,100 37,100 H0 Z '
     'M22,20 H35 C41,20 44,24 44,30 C44,36 41,40 35,40 H22 Z '
     'M22,60 H35 C41,60 44,64 44,70 C44,76 41,80 35,80 H22 Z',
"O": 'M31,0 C48,0 62,14 62,31 V69 C62,86 48,100 31,100 C14,100 0,86 0,69 '
     'V31 C0,14 14,0 31,0 Z '
     'M31,21 C40,21 44,27 44,35 V65 C44,73 40,79 31,79 C22,79 18,73 18,65 '
     'V35 C18,27 22,21 31,21 Z',
"A": 'M24,0 H38 L62,100 H41 L36,78 H26 L21,100 H0 Z '
     'M31,24 L25,58 H37 Z',
"T": 'M0,0 H62 V20 H42 V100 H20 V20 H0 Z',
"D": 'M0,0 H33 C50,0 62,14 62,31 V69 C62,86 50,100 33,100 H0 Z '
     'M22,20 H32 C40,20 44,26 44,34 V66 C44,74 40,80 32,80 H22 Z',
"S": 'M61,25 C55,9 44,0 30,0 C13,0 1,11 1,28 C1,42 10,50 26,55 L34,57.5 '
     'C41,59.5 43,62 43,67 C43,73 38,77 30,77 C22,77 15,73 10,66 L0,82 '
     'C7,93 18,100 31,100 C48,100 61,89 61,71 C61,57 52,49 36,44 L28,41.5 '
     'C21,39.5 19,37 19,32 C19,26 24,22 31,22 C38,22 44,26 47,33 Z',
}
ADV, GAP = 62, 14

def glyph_defs(prefix=""):
    return "\n".join(
        f'    <path id="{prefix}g{k}" fill-rule="evenodd" d="{v}"/>'
        for k, v in GLYPHS.items())

def word_width(word):
    return len(word) * ADV + (len(word) - 1) * GAP

def word(w, prefix=""):
    """<use> chain for a word, origin at left edge / cap top."""
    parts = []
    for i, ch in enumerate(w):
        parts.append(f'<use href="#{prefix}g{ch}" x="{i*(ADV+GAP)}" y="0"/>')
    return "".join(parts)

def wordmark(w, cx, top, target_w, fill, outline=None, ow=16, prefix=""):
    """Word scaled to target_w, centred on cx, cap-top at `top`."""
    s = target_w / word_width(w)
    g = f'<g transform="translate({cx - target_w/2:.2f},{top:.2f}) scale({s:.4f})">'
    body = word(w, prefix)
    out = ""
    if outline:
        out = (f'<g fill="{outline}" stroke="{outline}" stroke-width="{ow/s:.2f}" '
               f'stroke-linejoin="round">{body}</g>')
    return f'{g}{out}<g fill="{fill}">{body}</g></g>'

# ------------------------------------------------------------ scene bits
def sunburst(cx, cy, r, n=24, color=CREAM_D):
    """Alternating rays radiating from (cx,cy)."""
    out = []
    step = 360.0 / n
    for i in range(0, n, 2):
        a0 = math.radians(i * step - 90)
        a1 = math.radians((i + 1) * step - 90)
        x0, y0 = cx + r*math.cos(a0), cy + r*math.sin(a0)
        x1, y1 = cx + r*math.cos(a1), cy + r*math.sin(a1)
        out.append(f'<path d="M{cx},{cy} L{x0:.1f},{y0:.1f} L{x1:.1f},{y1:.1f} Z"/>')
    return f'<g fill="{color}">' + "".join(out) + "</g>"

def waves(y, w, color=CREAM, sw=9, amp=9, wl=90, phase=0):
    """A single horizontal wavy line across width w."""
    d = [f"M{-wl+phase},{y}"]
    x = -wl + phase
    while x < w + wl:
        d.append(f"q{wl/4:.1f},{-amp} {wl/2:.1f},0")
        d.append(f"q{wl/4:.1f},{amp} {wl/2:.1f},0")
        x += wl
    return (f'<path d="{" ".join(d)}" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round"/>')

def can(cx, cy, w=84, h=134, rot=-9):
    """A cold one, floating."""
    x, y = -w/2, -h/2
    return f'''<g transform="translate({cx},{cy}) rotate({rot})">
      <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{CREAM}" stroke="{NAVY}" stroke-width="7"/>
      <rect x="{x}" y="{y+h*0.30:.1f}" width="{w}" height="{h*0.26:.1f}" fill="{CORAL}"/>
      <rect x="{x}" y="{y+h*0.30:.1f}" width="{w}" height="{h*0.26:.1f}" fill="none" stroke="{NAVY}" stroke-width="7"/>
      <rect x="{x+9:.1f}" y="{y+9:.1f}" width="{w-18}" height="9" rx="4.5" fill="{NAVY}" opacity=".25"/>
      <ellipse cx="0" cy="{y+4:.1f}" rx="{w/2-3:.1f}" ry="9" fill="{CREAM_D}" stroke="{NAVY}" stroke-width="7"/>
    </g>'''

def drop(cx, cy, s=1.0, color=CREAM):
    return (f'<path transform="translate({cx},{cy}) scale({s})" fill="{color}" '
            f'd="M0,-16 C7,-6 12,0 12,6 C12,13 6,18 0,18 C-6,18 -12,13 -12,6 '
            f'C-12,0 -7,-6 0,-16 Z"/>')

def star4(cx, cy, r=17, color=CREAM):
    k = r * 0.30
    return (f'<path fill="{color}" d="M{cx},{cy-r} Q{cx+k},{cy-k} {cx+r},{cy} '
            f'Q{cx+k},{cy+k} {cx},{cy+r} Q{cx-k},{cy+k} {cx-r},{cy} '
            f'Q{cx-k},{cy-k} {cx},{cy-r} Z"/>')

ARIAL = "'Arial Black','Helvetica Neue',Helvetica,Arial,sans-serif"

# =====================================================================
# 1. PRIMARY BADGE — 4.5in circle
# =====================================================================
def badge(size_in=4.5, path="boat-sodas-badge-4.5in.svg"):
    S = 1000
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="{size_in}in" height="{size_in}in" viewBox="0 0 {S} {S}">
  <title>Boat Sodas — cooler badge decal</title>
  <desc>Die-cut circular vinyl decal, {size_in}in diameter including white cut border.</desc>
  <defs>
{glyph_defs()}
    <clipPath id="inner"><circle cx="500" cy="500" r="382"/></clipPath>
    <path id="arcTop" d="M500,500 m-406,0 a406,406 0 0 1 812,0" fill="none"/>
    <path id="arcBot" d="M500,500 m-452,0 a452,452 0 0 0 904,0" fill="none"/>
  </defs>

  <!-- die-cut border -->
  <circle cx="500" cy="500" r="499" fill="{WHITE}"/>
  <!-- navy ring -->
  <circle cx="500" cy="500" r="478" fill="{NAVY}"/>
  <circle cx="500" cy="500" r="478" fill="none" stroke="{NAVY_D}" stroke-width="6"/>

  <!-- scene -->
  <g clip-path="url(#inner)">
    <circle cx="500" cy="500" r="382" fill="{CREAM}"/>
    {sunburst(500, 455, 620)}
    <circle cx="500" cy="455" r="222" fill="none" stroke="{CREAM}" stroke-width="14"/>
    <circle cx="500" cy="455" r="210" fill="{ORANGE}"/>
    <!-- horizon + water -->
    <rect x="100" y="642" width="800" height="300" fill="{TEAL}"/>
    <rect x="100" y="642" width="800" height="16" fill="{TEAL_L}"/>
    {waves(700, 900, CREAM, 9, 10, 110, 10)}
    {waves(762, 900, TEAL_L, 11, 11, 130, 60)}
    {can(500, 716)}
    {waves(742, 900, CREAM, 10, 10, 120, 40)}
    {waves(812, 900, CREAM, 8, 8, 100, 0)}
    {drop(378, 646, 0.8)}
    {drop(622, 656, 0.65)}
    {drop(430, 800, 0.5)}
    {drop(575, 812, 0.45)}
  </g>
  <circle cx="500" cy="500" r="382" fill="none" stroke="{CREAM}" stroke-width="12"/>
  <circle cx="500" cy="500" r="396" fill="none" stroke="{CREAM}" stroke-width="4"/>

  <!-- ring type -->
  <g font-family="{ARIAL}" font-weight="900" fill="{CREAM}">
    <text font-size="50" letter-spacing="7">
      <textPath xlink:href="#arcTop" href="#arcTop" startOffset="50%" text-anchor="middle">NO WAKE &#183; NO WORRIES</textPath>
    </text>
    <text font-size="42" letter-spacing="6">
      <textPath xlink:href="#arcBot" href="#arcBot" startOffset="50%" text-anchor="middle">ICE COLD SINCE LAUNCH</textPath>
    </text>
  </g>
  {star4(70, 500, 24, ORANGE)}
  {star4(930, 500, 24, ORANGE)}

  <!-- wordmark -->
  {wordmark("BOAT",  500, 300, 440, NAVY, CREAM, 18)}
  {wordmark("SODAS", 500, 468, 440, NAVY, CREAM, 18)}
</svg>
'''
    open(os.path.join(OUT, path), "w").write(svg)

# =====================================================================
# 2. BUMPER / LID BANNER — 6in x 2in
# =====================================================================
def bumper(path="boat-sodas-banner-6x2in.svg"):
    W, H = 1200, 400
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="6in" height="2in" viewBox="0 0 {W} {H}">
  <title>Boat Sodas — cooler banner decal</title>
  <desc>Die-cut banner vinyl decal, 6in x 2in including white cut border.</desc>
  <defs>
{glyph_defs()}
    <clipPath id="field"><rect x="26" y="26" width="{W-52}" height="{H-52}" rx="44"/></clipPath>
  </defs>
  <rect x="0" y="0" width="{W}" height="{H}" rx="62" fill="{WHITE}"/>
  <rect x="14" y="14" width="{W-28}" height="{H-28}" rx="52" fill="{NAVY}"/>
  <g clip-path="url(#field)">
    <rect x="26" y="26" width="{W-52}" height="{H-52}" fill="{CREAM}"/>
    {sunburst(600, 250, 900, 28)}
    <circle cx="600" cy="250" r="170" fill="none" stroke="{CREAM}" stroke-width="12"/>
    <circle cx="600" cy="250" r="160" fill="{ORANGE}"/>
    <rect x="0" y="296" width="{W}" height="120" fill="{TEAL}"/>
    <rect x="0" y="296" width="{W}" height="10" fill="{TEAL_L}"/>
    {waves(332, W, CREAM, 8, 8, 110, 20)}
    {waves(378, W, TEAL_L, 9, 8, 130, 70)}
    <g font-family="{ARIAL}" font-weight="900" fill="{CREAM}" font-size="40"
       letter-spacing="8" text-anchor="middle">
      <text x="600" y="368">NO WAKE &#183; NO WORRIES</text>
    </g>
  </g>
  {star4(96, 250, 24, NAVY)}
  {star4(1104, 250, 24, NAVY)}
  {wordmark("BOAT SODAS".replace(" ", ""), 600, 0, 0, NAVY) if False else ""}
  {bumper_wordmark()}
</svg>
'''
    open(os.path.join(OUT, path), "w").write(svg)

def bumper_wordmark():
    """BOAT + SODAS on one line with a wide word space."""
    b, s = word_width("BOAT"), word_width("SODAS")
    space = 46
    total = b + space + s
    target = 880
    k = target / total
    x0 = 600 - target/2
    body = (f'<g transform="translate(0,0)">{word("BOAT")}</g>'
            f'<g transform="translate({b+space},0)">{word("SODAS")}</g>')
    return (f'<g transform="translate({x0:.1f},112) scale({k:.4f})">'
            f'<g fill="{CREAM}" stroke="{CREAM}" stroke-width="{20/k:.1f}" '
            f'stroke-linejoin="round">{body}</g>'
            f'<g fill="{NAVY}">{body}</g></g>')

# =====================================================================
# 3. MINI BADGE — 2in circle (simplified for small scale)
# =====================================================================
def mini(path="boat-sodas-mini-2in.svg"):
    S = 600
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="2in" height="2in" viewBox="0 0 {S} {S}">
  <title>Boat Sodas — mini decal</title>
  <desc>Die-cut circular vinyl decal, 2in diameter. Simplified for small-scale legibility.</desc>
  <defs>
{glyph_defs()}
    <clipPath id="mi"><circle cx="300" cy="300" r="252"/></clipPath>
  </defs>
  <circle cx="300" cy="300" r="299" fill="{WHITE}"/>
  <circle cx="300" cy="300" r="284" fill="{NAVY}"/>
  <g clip-path="url(#mi)">
    <circle cx="300" cy="300" r="252" fill="{CREAM}"/>
    {sunburst(300, 262, 420, 20)}
    <circle cx="300" cy="262" r="158" fill="none" stroke="{CREAM}" stroke-width="12"/>
    <circle cx="300" cy="262" r="148" fill="{ORANGE}"/>
    <rect x="40" y="436" width="520" height="200" fill="{TEAL}"/>
    <rect x="40" y="436" width="520" height="10" fill="{TEAL_L}"/>
    {waves(480, 560, CREAM, 9, 9, 100, 10)}
    {waves(526, 560, TEAL_L, 9, 8, 110, 50)}
  </g>
  <circle cx="300" cy="300" r="252" fill="none" stroke="{CREAM}" stroke-width="10"/>
  {wordmark("BOAT",  300, 162, 274, NAVY, CREAM, 16)}
  {wordmark("SODAS", 300, 280, 274, NAVY, CREAM, 16)}
</svg>
'''
    open(os.path.join(OUT, path), "w").write(svg)

badge()
bumper()
mini()
print("wrote:", sorted(os.listdir(OUT)))
