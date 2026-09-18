#!/usr/bin/env python3
"""Broad River Boat Soda Club — cooler decal artwork (standalone, font-free SVG)."""
import os, math

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- palette
NAVY   = "#0B2B45"
NAVY_D = "#071E31"
CREAM  = "#F7E7C6"
CREAM_D= "#EFD39B"
ORANGE = "#F2711C"
GOLD   = "#F6A623"
CORAL  = "#D93D2B"
RIVER  = "#16787D"
RIVER_L= "#2FA0A0"
PINE   = "#14503F"
PINE_D = "#0E3B2E"
WHITE  = "#FFFFFF"
ARIAL  = "'Arial Black','Helvetica Neue',Helvetica,Arial,sans-serif"

# ------------------------------------------------- custom letterforms
# Each glyph sits on a 100-unit cap height, baseline y=100, cap top y=0.
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
"R": 'M0,0 H37 C52,0 62,11 62,27 C62,41 55,50 44,54 L62,100 H39 L25,58 '
     'H22 V100 H0 Z '
     'M22,20 H34 C40,20 43,24 43,29 C43,35 40,38 34,38 H22 Z',
"I": 'M0,0 H24 V100 H0 Z',
"V": 'M0,0 H22 L31,68 L40,0 H62 L45,100 H17 Z',
"E": 'M0,0 H62 V20 H22 V39 H55 V59 H22 V80 H62 V100 H0 Z',
"C": 'M62,22 L47,33 C42,26 37,22 31,22 C22,22 18,28 18,35 V65 C18,72 22,78 '
     '31,78 C37,78 42,74 47,67 L62,78 C55,92 44,100 31,100 C14,100 0,87 0,69 '
     'V31 C0,13 14,0 31,0 C44,0 55,8 62,22 Z',
"L": 'M0,0 H22 V80 H58 V100 H0 Z',
"U": 'M0,0 H22 V66 C22,74 26,79 31,79 C36,79 40,74 40,66 V0 H62 V67 '
     'C62,86 49,100 31,100 C13,100 0,86 0,67 V0 Z',
}
WIDTHS = {k: 62 for k in GLYPHS}
WIDTHS.update({"I": 24, "L": 58})
GAP, SPACE = 14, 40

def glyph_defs():
    return "\n".join(f'    <path id="g{k}" fill-rule="evenodd" d="{v}"/>'
                     for k, v in GLYPHS.items())

def text_width(txt):
    w, first = 0, True
    for ch in txt:
        if not first:
            w += GAP if ch != " " else 0
        if ch == " ":
            w += SPACE
        else:
            w += WIDTHS[ch]
        first = False
    return w

def text_uses(txt):
    out, x = [], 0
    for i, ch in enumerate(txt):
        if i:
            x += GAP if ch != " " and txt[i-1] != " " else 0
        if ch == " ":
            x += SPACE
            continue
        out.append(f'<use href="#g{ch}" x="{x}" y="0"/>')
        x += WIDTHS[ch]
    return "".join(out)

def setline(txt, cx, top, target_w, fill, outline=None, ow=16):
    """One line of custom type, scaled to target_w, centred on cx, cap-top `top`."""
    s = target_w / text_width(txt)
    body = text_uses(txt)
    out = (f'<g fill="{outline}" stroke="{outline}" stroke-width="{ow/s:.2f}" '
           f'stroke-linejoin="round">{body}</g>') if outline else ""
    return (f'<g transform="translate({cx - target_w/2:.2f},{top:.2f}) '
            f'scale({s:.4f})">{out}<g fill="{fill}">{body}</g></g>')

# ------------------------------------------------------------ scene bits
def sunburst(cx, cy, r, n=24, color=CREAM_D):
    out, step = [], 360.0 / n
    for i in range(0, n, 2):
        a0, a1 = math.radians(i*step - 90), math.radians((i+1)*step - 90)
        out.append(f'<path d="M{cx},{cy} L{cx+r*math.cos(a0):.1f},{cy+r*math.sin(a0):.1f} '
                   f'L{cx+r*math.cos(a1):.1f},{cy+r*math.sin(a1):.1f} Z"/>')
    return f'<g fill="{color}">' + "".join(out) + "</g>"

def waves(y, w, color=CREAM, sw=9, amp=9, wl=90, phase=0):
    d, x = [f"M{-wl+phase},{y}"], -wl + phase
    while x < w + wl:
        d.append(f"q{wl/4:.1f},{-amp} {wl/2:.1f},0 q{wl/4:.1f},{amp} {wl/2:.1f},0")
        x += wl
    return (f'<path d="{" ".join(d)}" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round"/>')

def pines(base, x0, x1, heights, color=PINE, widthf=0.42):
    """A silhouetted fir treeline standing on `base`."""
    n = len(heights)
    step = (x1 - x0) / (n - 1) if n > 1 else 0
    parts = [f'<rect x="{x0}" y="{base-4}" width="{x1-x0}" height="30" fill="{color}"/>']
    for i, h in enumerate(heights):
        x = x0 + i * step
        w = h * widthf
        parts.append(
            f'<path d="M{x:.1f},{base-h:.1f} Q{x+w*0.38:.1f},{base-h*0.42:.1f} '
            f'{x+w:.1f},{base:.1f} H{x-w:.1f} Q{x-w*0.38:.1f},{base-h*0.42:.1f} '
            f'{x:.1f},{base-h:.1f} Z" fill="{color}"/>')
    return "".join(parts)

def reflection(cx, top, rows, color=GOLD):
    """Shimmering sun reflection on the water."""
    parts = []
    for i, (dy, w, h) in enumerate(rows):
        parts.append(f'<rect x="{cx-w/2:.1f}" y="{top+dy:.1f}" width="{w}" height="{h}" '
                     f'rx="{h/2:.1f}" fill="{color}" opacity="{0.9 - i*0.11:.2f}"/>')
    return "".join(parts)

def tallboy(cx, cy, w=134, h=300, rot=-7, label=True, halo=0):
    """The hero can. It is, for the record, a soda."""
    x, y = -w/2, -h/2
    ow = w * 0.055                      # outline weight
    by, bh = y + h*0.26, h*0.48         # label band
    lbl = ""
    if label:
        fs = w * 0.27
        lbl = (f'<line x1="{x+w*0.14:.1f}" y1="{by+bh*0.5:.1f}" x2="{x+w*0.86:.1f}" '
               f'y2="{by+bh*0.5:.1f}" stroke="{CREAM}" stroke-width="{w*0.028:.1f}" opacity=".7"/>'
               f'<g font-family="{ARIAL}" font-weight="900" fill="{CREAM}" '
               f'text-anchor="middle" font-size="{fs:.1f}" letter-spacing="0.5">'
               f'<text x="0" y="{by + bh*0.38:.1f}">BOAT</text>'
               f'<text x="0" y="{by + bh*0.88:.1f}">SODA</text></g>')
    ring = ""
    if halo:
        ring = (f'<g fill="{CREAM}" stroke="{CREAM}" stroke-width="{halo*2}" stroke-linejoin="round">'
                f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w*0.17:.1f}"/>'
                f'<ellipse cx="0" cy="{y+w*0.05:.1f}" rx="{w/2-w*0.02:.1f}" ry="{w*0.13:.1f}"/></g>')
    return f'''<g transform="translate({cx},{cy}) rotate({rot})">
      {ring}
      <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w*0.17:.1f}" fill="{CREAM}"/>
      <rect x="{x}" y="{by:.1f}" width="{w}" height="{bh:.1f}" fill="{CORAL}"/>
      {lbl}
      <rect x="{x+w*0.10:.1f}" y="{y+h*0.07:.1f}" width="{w*0.13:.1f}" height="{h*0.13:.1f}"
            rx="{w*0.065:.1f}" fill="{WHITE}" opacity=".7"/>
      <rect x="{x}" y="{y+h*0.885:.1f}" width="{w}" height="{h*0.045:.1f}" fill="{NAVY}" opacity=".18"/>
      <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w*0.17:.1f}"
            fill="none" stroke="{NAVY}" stroke-width="{ow:.1f}"/>
      <ellipse cx="0" cy="{y+w*0.05:.1f}" rx="{w/2-w*0.02:.1f}" ry="{w*0.13:.1f}"
               fill="{CREAM_D}" stroke="{NAVY}" stroke-width="{ow:.1f}"/>
      <ellipse cx="{-w*0.09:.1f}" cy="{y+w*0.05:.1f}" rx="{w*0.19:.1f}" ry="{w*0.055:.1f}"
               fill="{NAVY}" opacity=".5"/>
      <circle cx="{w*0.15:.1f}" cy="{y+w*0.05:.1f}" r="{w*0.045:.1f}" fill="{NAVY}" opacity=".5"/>
    </g>'''

def drop(cx, cy, s=1.0, color=CREAM):
    return (f'<path transform="translate({cx},{cy}) scale({s})" fill="{color}" '
            f'd="M0,-16 C7,-6 12,0 12,6 C12,13 6,18 0,18 C-6,18 -12,13 -12,6 '
            f'C-12,0 -7,-6 0,-16 Z"/>')

def star4(cx, cy, r=18, color=CREAM):
    k = r * 0.30
    return (f'<path fill="{color}" d="M{cx},{cy-r} Q{cx+k},{cy-k} {cx+r},{cy} '
            f'Q{cx+k},{cy+k} {cx},{cy+r} Q{cx-k},{cy+k} {cx-r},{cy} '
            f'Q{cx-k},{cy-k} {cx},{cy-r} Z"/>')

def write(name, svg):
    open(os.path.join(OUT, name), "w").write(svg)

# =====================================================================
# 1. ROUNDEL — 4.5in circle. Scene-forward club patch.
# =====================================================================
def roundel():
    write("brbsc-roundel-4.5in.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     width="4.5in" height="4.5in" viewBox="0 0 1000 1000">
  <title>Broad River Boat Soda Club — roundel decal</title>
  <desc>Die-cut circular vinyl decal, 4.5in diameter including white cut border.</desc>
  <defs>
{glyph_defs()}
    <clipPath id="inner"><circle cx="500" cy="500" r="382"/></clipPath>
    <path id="arcTop" d="M500,500 m-404,0 a404,404 0 0 1 808,0" fill="none"/>
    <path id="arcBot" d="M500,500 m-444,0 a444,444 0 0 0 888,0" fill="none"/>
  </defs>

  <circle cx="500" cy="500" r="499" fill="{WHITE}"/>
  <circle cx="500" cy="500" r="478" fill="{NAVY}"/>

  <g clip-path="url(#inner)">
    <circle cx="500" cy="500" r="382" fill="{CREAM}"/>
    {sunburst(500, 350, 640)}
    <circle cx="500" cy="350" r="187" fill="none" stroke="{CREAM}" stroke-width="14"/>
    <circle cx="500" cy="350" r="175" fill="{ORANGE}"/>
    <!-- far bank -->
    {pines(616, 90, 910, [86,132,104,150,118,168,126,152,110,138,96,120,88], PINE_D, 0.40)}
    {pines(628, 70, 930, [70,112,92,130,104,146,112,132,96,120,80,104,72,96], PINE, 0.44)}
    <!-- river -->
    <rect x="80" y="624" width="840" height="320" fill="{RIVER}"/>
    <rect x="80" y="624" width="840" height="12" fill="{RIVER_L}"/>
    {reflection(500, 648, [(0,300,14),(30,250,12),(62,196,11),(96,140,10),(130,92,9)])}
    {waves(690, 920, CREAM, 9, 10, 120, 10)}
    {waves(756, 920, RIVER_L, 11, 11, 140, 60)}
    <!-- shoal rocks -->
    <ellipse cx="190" cy="742" rx="62" ry="26" fill="{NAVY}" opacity=".55"/>
    <ellipse cx="826" cy="776" rx="54" ry="22" fill="{NAVY}" opacity=".55"/>
    {tallboy(500, 548, 152, 322)}
    {waves(676, 920, CREAM, 10, 10, 130, 55)}
    {waves(820, 920, CREAM, 8, 9, 110, 0)}
    {drop(362, 470, 0.9)}
    {drop(640, 452, 0.72)}
    {drop(330, 588, 0.6)}
  </g>
  <circle cx="500" cy="500" r="382" fill="none" stroke="{CREAM}" stroke-width="12"/>
  <circle cx="500" cy="500" r="397" fill="none" stroke="{CREAM}" stroke-width="4"/>

  <g font-family="{ARIAL}" font-weight="900" fill="{CREAM}">
    <text font-size="72" letter-spacing="8">
      <textPath xlink:href="#arcTop" href="#arcTop" startOffset="50%" text-anchor="middle">BROAD RIVER</textPath>
    </text>
    <text font-size="50" letter-spacing="6">
      <textPath xlink:href="#arcBot" href="#arcBot" startOffset="50%" text-anchor="middle">BOAT SODA CLUB</textPath>
    </text>
  </g>
  {star4(72, 500, 24, ORANGE)}
  {star4(928, 500, 24, ORANGE)}
</svg>
''')

# =====================================================================
# 2. CREST — 4in x 5in shield. Type-forward, punchline on the ribbon.
# =====================================================================
SH_W = ("M74,26 H726 Q774,26 774,74 V560 C774,776 628,912 400,978 "
        "C172,912 26,776 26,560 V74 Q26,26 74,26 Z")
SH_N = ("M86,44 H714 Q756,44 756,86 V558 C756,762 618,890 400,954 "
        "C182,890 44,762 44,558 V86 Q44,44 86,44 Z")
SH_C = ("M106,70 H694 Q730,70 730,106 V554 C730,740 602,860 400,920 "
        "C198,860 70,740 70,554 V106 Q70,70 106,70 Z")

def crest():
    shape = "M104,492 H696 L672,523 L696,554 H104 L128,523 Z"
    ribbon = (f'<path d="{shape}" fill="{NAVY}"/>'
              f'<path d="{shape}" fill="none" stroke="{CREAM}" stroke-width="5"/>'
              f'<g font-family="{ARIAL}" font-weight="900" fill="{CREAM}" font-size="28" '
              f'letter-spacing="1" text-anchor="middle">'
              f'<text x="400" y="532">IF ANYBODY ASKS, IT&#8217;S A SODA</text></g>')
    write("brbsc-crest-4x5in.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="4in" height="5in" viewBox="0 0 800 1000">
  <title>Broad River Boat Soda Club — crest decal</title>
  <desc>Die-cut shield vinyl decal, 4in x 5in including white cut border.</desc>
  <defs>
{glyph_defs()}
    <clipPath id="field"><path d="{SH_C}"/></clipPath>
  </defs>
  <path d="{SH_W}" fill="{WHITE}" stroke="{WHITE}" stroke-width="40" stroke-linejoin="round"/>
  <path d="{SH_N}" fill="{NAVY}"/>
  <path d="{SH_C}" fill="{CREAM}"/>
  <g clip-path="url(#field)">
    {sunburst(400, 300, 720, 28)}
    <circle cx="400" cy="300" r="197" fill="none" stroke="{CREAM}" stroke-width="13"/>
    <circle cx="400" cy="300" r="185" fill="{ORANGE}"/>
    {pines(594, 60, 740, [30,46,36,52,40,54,38,48,32,44,30], PINE_D, 0.40)}
    {pines(604, 44, 756, [26,40,32,46,36,48,34,42,28,38,26,36], PINE, 0.44)}
    <rect x="40" y="604" width="720" height="360" fill="{RIVER}"/>
    <rect x="40" y="604" width="720" height="10" fill="{RIVER_L}"/>
    {reflection(400, 624, [(0,150,9),(24,110,8),(50,72,7)])}
    {waves(660, 760, CREAM, 8, 8, 110, 20)}
    {waves(752, 760, RIVER_L, 9, 8, 130, 70)}
    {ribbon}
    <ellipse cx="400" cy="838" rx="96" ry="19" fill="{NAVY}" opacity=".28"/>
    {tallboy(400, 705, 143, 280, -6, True, 13)}
    {waves(822, 760, CREAM, 9, 9, 120, 10)}
    {drop(286, 620, 0.7)}
    {drop(520, 664, 0.58)}
    {drop(268, 740, 0.48)}
  </g>
  <path d="{SH_C}" fill="none" stroke="{NAVY}" stroke-width="7"/>

  {setline("BROAD RIVER", 400, 92, 384, NAVY)}
  {star4(152, 120, 16, ORANGE)}
  {star4(648, 120, 16, ORANGE)}
  {setline("BOAT", 400, 150, 300, NAVY, CREAM, 15)}
  {setline("SODA", 400, 262, 300, NAVY, CREAM, 15)}
  {setline("CLUB", 400, 374, 300, NAVY, CREAM, 15)}
</svg>
''')

# =====================================================================
# 3. BANNER — 6in x 2in, for the long front panel
# =====================================================================
def banner():
    write("brbsc-banner-6x2in.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="6in" height="2in" viewBox="0 0 1200 400">
  <title>Broad River Boat Soda Club — banner decal</title>
  <desc>Die-cut banner vinyl decal, 6in x 2in including white cut border.</desc>
  <defs>
{glyph_defs()}
    <clipPath id="field"><rect x="26" y="26" width="1148" height="348" rx="44"/></clipPath>
  </defs>
  <rect x="0" y="0" width="1200" height="400" rx="62" fill="{WHITE}"/>
  <rect x="14" y="14" width="1172" height="372" rx="52" fill="{NAVY}"/>
  <g clip-path="url(#field)">
    <rect x="26" y="26" width="1148" height="348" fill="{CREAM}"/>
    {sunburst(600, 214, 900, 28)}
    <circle cx="600" cy="214" r="126" fill="none" stroke="{CREAM}" stroke-width="11"/>
    <circle cx="600" cy="214" r="116" fill="{ORANGE}"/>
    {pines(280, 10, 1190, [46,72,58,84,64,90,68,96,70,88,60,80,54,74,48,68,44,62], PINE_D, 0.40)}
    {pines(292, -10, 1210, [38,62,50,74,56,80,60,86,62,78,52,70,46,64,40,58,36,54,42], PINE, 0.44)}
    <rect x="0" y="288" width="1200" height="120" fill="{RIVER}"/>
    <rect x="0" y="288" width="1200" height="9" fill="{RIVER_L}"/>
    {reflection(600, 300, [(0,160,9),(20,120,8),(42,80,7)])}
    {waves(322, 1200, CREAM, 8, 8, 120, 20)}
    {waves(376, 1200, RIVER_L, 9, 8, 140, 70)}
    <g font-family="{ARIAL}" font-weight="900" fill="{CREAM}" font-size="34"
       letter-spacing="3.5" text-anchor="middle">
      <text x="600" y="358">IF ANYBODY ASKS, IT&#8217;S A SODA</text>
    </g>
  </g>
  {setline("BROAD RIVER", 600, 56, 300, NAVY, CREAM, 11)}
  {setline("BOAT SODA CLUB", 600, 126, 930, NAVY, CREAM, 17)}
  {star4(96, 200, 22, NAVY)}
  {star4(1104, 200, 22, NAVY)}
</svg>
''')

# =====================================================================
# 4. MINI — 2in monogram. Ring type dropped; it will not read that small.
# =====================================================================
def mini():
    write("brbsc-mini-2in.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" width="2in" height="2in" viewBox="0 0 600 600">
  <title>Broad River Boat Soda Club — mini monogram decal</title>
  <desc>Die-cut circular vinyl decal, 2in diameter. Monogram for small-scale legibility.</desc>
  <defs>
{glyph_defs()}
    <clipPath id="mi"><circle cx="300" cy="300" r="252"/></clipPath>
  </defs>
  <circle cx="300" cy="300" r="299" fill="{WHITE}"/>
  <circle cx="300" cy="300" r="284" fill="{NAVY}"/>
  <g clip-path="url(#mi)">
    <circle cx="300" cy="300" r="252" fill="{CREAM}"/>
    {sunburst(300, 248, 420, 20)}
    <circle cx="300" cy="248" r="150" fill="none" stroke="{CREAM}" stroke-width="12"/>
    <circle cx="300" cy="248" r="139" fill="{ORANGE}"/>
    {pines(412, 30, 570, [54,80,64,92,72,84,62,76,52], PINE_D, 0.40)}
    {pines(424, 20, 580, [44,68,54,80,62,74,54,66,44,60], PINE, 0.44)}
    <rect x="40" y="420" width="520" height="200" fill="{RIVER}"/>
    <rect x="40" y="420" width="520" height="9" fill="{RIVER_L}"/>
    {waves(462, 560, CREAM, 9, 9, 100, 10)}
    {waves(512, 560, RIVER_L, 9, 8, 110, 50)}
  </g>
  <circle cx="300" cy="300" r="252" fill="none" stroke="{CREAM}" stroke-width="10"/>
  {setline("BRBSC", 300, 218, 320, NAVY, CREAM, 15)}
</svg>
''')

roundel(); crest(); banner(); mini()
print("wrote:", sorted(f for f in os.listdir(OUT) if f.endswith(".svg")))
