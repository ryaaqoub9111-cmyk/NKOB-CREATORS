#!/usr/bin/env python3
"""Vérifications statiques : liens internes, ancres, ressources, IDs, alt, JSON-LD, HTML strict."""
import os, re, sys, json, glob
from html.parser import HTMLParser
_R = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ROOT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else (os.path.join(_R, "site") if os.path.isdir(os.path.join(_R, "site")) else _R)
pages = sorted(glob.glob(os.path.join(ROOT, "*.html")))
errors, warns = [], []
class P(HTMLParser):
    def __init__(s): super().__init__(); s.links=[]; s.ids=[]; s.res=[]; s.imgs=[]; s.h1=0; s.ld=[]; s._ld=False; s.labels=set(); s.inputs=[]; s.title=""; s._t=False; s.desc=None
    def handle_starttag(s,t,a):
        a=dict(a)
        if "id" in a: s.ids.append(a["id"])
        if t=="a" and "href" in a: s.links.append(a["href"])
        if t in("img","script","source","video") and a.get("src"): s.res.append(a["src"])
        if t=="link" and a.get("href") and a.get("rel") in("stylesheet","icon","apple-touch-icon","manifest","preload"): s.res.append(a["href"])
        if t=="img": s.imgs.append(a)
        if t=="h1": s.h1+=1
        if t=="script" and a.get("type")=="application/ld+json": s._ld=True
        if t=="label" and "for" in a: s.labels.add(a["for"])
        if t in("input","select","textarea"): s.inputs.append(a)
        if t=="title": s._t=True
        if t=="meta" and a.get("name")=="description": s.desc=a.get("content")
    def handle_endtag(s,t):
        if t=="script": s._ld=False
        if t=="title": s._t=False
    def handle_data(s,d):
        if s._ld: s.ld.append(d)
        if s._t: s.title+=d
def strip(u): return u.split("#")[0].split("?")[0]
all_ids={}
parsed={}
for f in pages:
    p=P(); p.feed(open(f,encoding="utf-8").read()); parsed[os.path.basename(f)]=p
    all_ids[os.path.basename(f)]=set(p.ids)
for name,p in parsed.items():
    if len(p.ids)!=len(set(p.ids)): errors.append(f"{name}: ID dupliqués {[i for i in set(p.ids) if p.ids.count(i)>1]}")
    if name not in("blog.html",):
        if p.h1!=1: errors.append(f"{name}: {p.h1} balises h1")
        if not p.title or not p.desc: errors.append(f"{name}: title/description manquant")
        elif len(p.desc)>175: warns.append(f"{name}: description longue ({len(p.desc)})")
    for l in p.links:
        if re.match(r"(https?:|mailto:|tel:|javascript:)",l): continue
        if l.startswith("#"):
            if l[1:] and l[1:] not in p.ids: errors.append(f"{name}: ancre {l} introuvable")
            continue
        tgt=strip(l); frag=l.split("#")[1] if "#" in l else None
        if not tgt: continue
        path=os.path.join(ROOT,tgt)
        if not os.path.exists(path): errors.append(f"{name}: lien cassé {l}")
        elif frag and tgt.endswith(".html") and frag not in all_ids.get(tgt,set()): errors.append(f"{name}: ancre {l} introuvable")
    for r in p.res:
        if re.match(r"(https?:|data:)",r): 
            if r.startswith("http"): warns.append(f"{name}: ressource externe {r}")
            continue
        if not os.path.exists(os.path.join(ROOT,strip(r))): errors.append(f"{name}: ressource manquante {r}")
    for im in p.imgs:
        if "alt" not in im: errors.append(f"{name}: img sans alt {im.get('src')}")
    for i in p.inputs:
        if i.get("type") in("hidden","submit","button"): continue
        if i.get("id") not in p.labels and not i.get("aria-label"): errors.append(f"{name}: champ sans label {i}")
    for blob in p.ld:
        try: json.loads(blob)
        except Exception as e: errors.append(f"{name}: JSON-LD invalide {e}")
# html5lib strict
try:
    import html5lib
    for f in pages:
        parser=html5lib.HTMLParser(strict=False); parser.parse(open(f,encoding="utf-8").read())
        for (line,col),code,data in parser.errors:
            if code in("expected-doctype-but-got-start-tag",): continue
            errors.append(f"{os.path.basename(f)}:{line}:{col} html5lib {code} {data}")
except ImportError: warns.append("html5lib absent : validation HTML stricte non exécutée")
# assets referenced from css/js data
css=open(os.path.join(ROOT,"assets/css/styles.css"),encoding="utf-8").read()
for m in re.findall(r'url\("?([^")]+)"?\)',css):
    if m.startswith("data:"): continue
    if not os.path.exists(os.path.normpath(os.path.join(ROOT,"assets/css",m))): errors.append(f"CSS: fichier manquant {m}")
js=open(os.path.join(ROOT,"assets/js/projects-data.js"),encoding="utf-8").read()
for m in re.findall(r'"(assets/[^"]+)"',js):
    if "…" in m or "mon-projet" in m or "ma-video" in m: continue
    if not os.path.exists(os.path.join(ROOT,m)): errors.append(f"projects-data.js: fichier manquant {m}")
# sitemap
sm=open(os.path.join(ROOT,"sitemap.xml"),encoding="utf-8").read()
for loc in re.findall(r"<loc>https://[^/]+/([^<]*)</loc>",sm):
    if loc and not os.path.exists(os.path.join(ROOT,loc)): errors.append(f"sitemap: {loc} absent")
total=sum(os.path.getsize(os.path.join(dp,f)) for dp,_,fs in os.walk(ROOT) for f in fs)
print(f"{len(pages)} pages vérifiées — {total/1024:.0f} Ko au total")
for w in warns: print("AVERT:",w)
for e in errors: print("ERREUR:",e)
print("RÉSULTAT:", "OK" if not errors else f"{len(errors)} erreur(s)")
sys.exit(1 if errors else 0)
