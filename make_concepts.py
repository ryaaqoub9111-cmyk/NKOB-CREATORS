"""Génère les visuels « concept » (SVG) du portfolio. Ce ne sont PAS des projets clients."""
import os
_R = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
_S = os.path.join(_R, "site") if os.path.isdir(os.path.join(_R, "site")) else _R
OUT = os.path.join(_S, "assets", "img", "concepts")
os.makedirs(OUT, exist_ok=True)
W, H = 1200, 800
def wrap(id_, c1, c2, body, tag):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>
<linearGradient id="a" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#bd36eb"/><stop offset="1" stop-color="#ff5fa2"/></linearGradient>
<linearGradient id="c" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#49e1f6"/><stop offset="1" stop-color="#5b3df5"/></linearGradient>
<filter id="b"><feGaussianBlur stdDeviation="40"/></filter></defs>
<rect width="{W}" height="{H}" fill="#0f0820"/><rect width="{W}" height="{H}" fill="url(#g)" opacity=".55"/>
<circle cx="980" cy="120" r="230" fill="#ff5fa2" opacity=".28" filter="url(#b)"/><circle cx="160" cy="720" r="260" fill="#5b3df5" opacity=".4" filter="url(#b)"/>
{body}
<text x="48" y="764" fill="#fff" fill-opacity=".7" font-family="Georgia,serif" font-style="italic" font-size="26">{tag}</text></svg>'''
def browser(x,y,w,h,inner):
    return f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="#150c2c" stroke="#fff" stroke-opacity=".2"/><circle cx="{x+30}" cy="{y+28}" r="6" fill="#ff5fa2"/><circle cx="{x+52}" cy="{y+28}" r="6" fill="#bd36eb"/><circle cx="{x+74}" cy="{y+28}" r="6" fill="#49e1f6"/><rect x="{x+110}" y="{y+16}" width="{w-150}" height="24" rx="12" fill="#fff" fill-opacity=".08"/>{inner}</g>'
files = {}
# web : booking flow
cal = "".join(f'<rect x="{720+(i%7)*50}" y="{300+(i//7)*50}" width="40" height="40" rx="10" fill="{"url(#a)" if i in (9,10,11,16) else "#fff"}" fill-opacity="{1 if i in (9,10,11,16) else .09}"/>' for i in range(28))
files["web"] = wrap("web","#5b3df5","#0f0820", browser(120,110,960,560,
  '<rect x="160" y="190" width="440" height="40" rx="10" fill="#fff" fill-opacity=".9"/><rect x="160" y="250" width="320" height="40" rx="10" fill="#fff" fill-opacity=".5"/>'
  '<rect x="160" y="330" width="380" height="14" rx="7" fill="#fff" fill-opacity=".25"/><rect x="160" y="360" width="340" height="14" rx="7" fill="#fff" fill-opacity=".25"/>'
  '<rect x="160" y="430" width="190" height="56" rx="28" fill="url(#a)"/><rect x="370" y="430" width="150" height="56" rx="28" fill="none" stroke="#fff" stroke-opacity=".35"/>'
  '<rect x="690" y="180" width="380" height="460" rx="24" fill="#fff" fill-opacity=".05" stroke="#fff" stroke-opacity=".15"/>'+cal+
  '<rect x="720" y="560" width="320" height="52" rx="26" fill="url(#c)"/>'), "Concept — réservation (non client)")
# tourism : dunes & sun
files["tourism"] = wrap("tourism","#d42d7d","#2a1050",
  '<circle cx="600" cy="330" r="150" fill="url(#a)"/><path d="M0 560 Q200 430 420 540 T820 520 T1200 500 V800 H0Z" fill="#2a1050"/><path d="M0 640 Q260 540 520 630 T1200 590 V800 H0Z" fill="#150c2c"/>'
  '<rect x="430" y="150" width="340" height="64" rx="32" fill="#0f0820" fill-opacity=".55" stroke="#fff" stroke-opacity=".3"/><rect x="460" y="172" width="180" height="14" rx="7" fill="#fff"/><circle cx="730" cy="182" r="13" fill="url(#c)"/>'
  '<g fill="#fff" fill-opacity=".85"><circle cx="300" cy="610" r="7"/><circle cx="880" cy="640" r="5"/></g>', "Concept — page d'atterrissage tourisme (non client)")
# branding : tiles + swatches
files["branding"] = wrap("branding","#bd36eb","#0f0820",
  '<rect x="150" y="130" width="420" height="420" rx="40" fill="#0f0820" stroke="#fff" stroke-opacity=".25"/><path d="M270 440V240l120 200V240" stroke="url(#a)" stroke-width="40" fill="none" stroke-linecap="round" stroke-linejoin="round"/><circle cx="450" cy="340" r="52" fill="none" stroke="url(#c)" stroke-width="30"/>'
  '<rect x="620" y="130" width="430" height="200" rx="32" fill="#fff"/><path d="M670 230h130M670 270h80" stroke="#150c2c" stroke-width="16" stroke-linecap="round"/><circle cx="990" cy="230" r="42" fill="url(#a)"/>'
  '<g><rect x="620" y="360" width="100" height="190" rx="24" fill="#bd36eb"/><rect x="740" y="360" width="100" height="190" rx="24" fill="#ff5fa2"/><rect x="860" y="360" width="100" height="190" rx="24" fill="#5b3df5"/><rect x="980" y="360" width="70" height="190" rx="24" fill="#49e1f6"/></g>', "Concept — identité visuelle (non client)")
# design : posters
def poster(x,y,r,col,sh):
    return f'<g transform="rotate({r} {x+130} {y+190})"><rect x="{x}" y="{y}" width="260" height="380" rx="18" fill="{col}"/>{sh}</g>'
files["design"] = wrap("design","#ff5fa2","#150c2c",
  poster(210,170,-8,"#0f0820",'<circle cx="340" cy="320" r="70" fill="url(#a)"/><rect x="240" y="470" width="180" height="16" rx="8" fill="#fff"/><rect x="240" y="500" width="120" height="12" rx="6" fill="#fff" fill-opacity=".5"/>')+
  poster(470,130,0,"url(#a)",'<path d="M500 450c40-120 120-120 160 0" stroke="#fff" stroke-width="22" fill="none" stroke-linecap="round"/><rect x="510" y="200" width="180" height="26" rx="13" fill="#fff"/><rect x="510" y="244" width="110" height="14" rx="7" fill="#fff" fill-opacity=".6"/>')+
  poster(730,170,8,"#fff",'<circle cx="860" cy="330" r="82" fill="url(#c)"/><rect x="770" y="470" width="180" height="16" rx="8" fill="#150c2c"/><rect x="770" y="500" width="130" height="12" rx="6" fill="#150c2c" fill-opacity=".4"/>'), "Concept — série d'affiches (non client)")
# video : storyboard
fr = "".join(f'<g><rect x="{110+i*250}" y="{250+(i%2)*40}" width="220" height="150" rx="16" fill="{["#5b3df5","#bd36eb","#ff5fa2","#2a55f0"][i]}" fill-opacity=".85"/><circle cx="{220+i*250}" cy="{325+(i%2)*40}" r="26" fill="#fff" fill-opacity=".9"/><path d="M{212+i*250} {312+(i%2)*40}l22 13-22 13z" fill="#150c2c"/></g>' for i in range(4))
files["video"] = wrap("video","#2a55f0","#0f0820", fr+'<rect x="110" y="520" width="980" height="14" rx="7" fill="#fff" fill-opacity=".15"/><rect x="110" y="520" width="520" height="14" rx="7" fill="url(#a)"/><circle cx="630" cy="527" r="14" fill="#fff"/><g fill="#fff" fill-opacity=".35"><rect x="110" y="570" width="300" height="40" rx="10"/><rect x="430" y="570" width="220" height="40" rx="10"/><rect x="670" y="570" width="420" height="40" rx="10"/></g>', "Concept — promo vidéo, storyboard (non client)")
# photo : frames
files["photo"] = wrap("photo","#49e1f6","#2a1050",
  '<rect x="150" y="150" width="520" height="400" rx="20" fill="#0f0820" stroke="#fff" stroke-opacity=".3"/><path d="M150 480l150-140 120 100 100-80 150 130v60a20 20 0 01-20 20H170a20 20 0 01-20-20z" fill="url(#c)" opacity=".9"/><circle cx="520" cy="250" r="40" fill="url(#a)"/>'
  '<rect x="710" y="150" width="340" height="190" rx="20" fill="#bd36eb" fill-opacity=".8"/><rect x="710" y="360" width="340" height="190" rx="20" fill="#ff5fa2" fill-opacity=".75"/><path d="M730 520l80-80 70 60 60-50 90 70" stroke="#fff" stroke-opacity=".8" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>', "Concept — série photo (non client)")
# digital : seo
bars = "".join(f'<rect x="{700+i*70}" y="{520-h}" width="46" height="{h}" rx="12" fill="url(#a)" fill-opacity="{.4+i*.12}"/>' for i,h in enumerate([90,140,190,260,330]))
files["digital"] = wrap("digital","#5b3df5","#150c2c",
  '<rect x="130" y="140" width="460" height="64" rx="32" fill="#fff" fill-opacity=".92"/><circle cx="170" cy="172" r="12" fill="none" stroke="#150c2c" stroke-width="5"/><rect x="200" y="164" width="260" height="16" rx="8" fill="#150c2c" fill-opacity=".6"/>'
  '<g><rect x="130" y="240" width="460" height="120" rx="22" fill="#fff" fill-opacity=".07" stroke="#fff" stroke-opacity=".15"/><rect x="160" y="270" width="280" height="16" rx="8" fill="url(#c)"/><rect x="160" y="304" width="380" height="12" rx="6" fill="#fff" fill-opacity=".4"/></g>'
  '<path d="M200 560c0-60 90-60 90 0 0 40-45 80-45 80s-45-40-45-80z" fill="url(#a)"/><circle cx="245" cy="560" r="18" fill="#fff"/>'+bars+'<path d="M690 520H1090" stroke="#fff" stroke-opacity=".3"/>', "Concept — SEO local (non client)")
for k,v in files.items():
    open(os.path.join(OUT,k+".svg"),"w",encoding="utf-8").write(v)
print(list(files))
