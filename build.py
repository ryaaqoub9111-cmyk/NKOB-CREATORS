#!/usr/bin/env python3
"""Génère les pages HTML statiques du site NKOB CREATORS (Python 3, aucune dépendance).

Usage :  python3 tools/build.py            (depuis la racine du projet)
Contenu modifiable : tools/content/socials.json et tools/content/cv.json
Les pages sont écrites à la racine du site (dossier parent de /tools si "site/" n'existe pas).
"""
import json, os, html, datetime
from urllib.parse import quote

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = os.path.join(ROOT, "site") if os.path.isdir(os.path.join(ROOT, "site")) else ROOT
CONTENT = os.path.join(os.path.dirname(__file__), "content")
S = json.load(open(os.path.join(CONTENT, "socials.json"), encoding="utf-8"))
CV = json.load(open(os.path.join(CONTENT, "cv.json"), encoding="utf-8"))
BASE = S["website"].rstrip("/")
WA = S["whatsapp_number"]
MAIL = S["email"]
PHONE_FMT = "+212 611 073 479"
WA_TEXT = quote("Bonjour NKOB CREATORS, je souhaite discuter d'un projet.")
E = html.escape
TODAY = datetime.date.today().isoformat()

# ------------------------------------------------------------------ services
SERVICES = [
    dict(id="sites-web", n="01", cls="b1", title="Sites web & plateformes", short="Sites vitrines, sites d'entreprise, landing pages et WordPress : rapides, accessibles, pensés pour convertir.",
         tags=["Sites vitrines", "Landing pages", "WordPress", "Maintenance"], opt="Site web", color="#5b3df5",
         intro="Un site n'est pas une brochure : c'est votre meilleur commercial, disponible 24 h/24. Nous concevons des interfaces claires, rapides et responsives, avec des appels à l'action là où vos visiteurs en ont besoin.",
         do=["Conception UX/UI sur mesure", "Développement HTML, CSS et JavaScript", "Sites d'entreprise multi-pages", "Landing pages pour campagnes et lancements", "Sites WordPress faciles à mettre à jour", "Optimisation des performances et suivi statistique", "Maintenance : mises à jour, sauvegardes, corrections"],
         why=["Chargement rapide et pages prêtes pour le référencement", "Parcours pensé pour générer des demandes de contact", "Mobile d'abord, contenus multilingues possibles", "Contenu simple à faire évoluer"],
         who=["Entreprises et prestataires de services", "Créateurs et indépendants", "Événements et campagnes", "Commerces locaux"]),
    dict(id="tourisme", n="02", cls="b2", title="Tourisme & réservation", short="Calendriers de disponibilité, parcours de réservation et contenus multilingues pour riads, circuits et guides.",
         tags=["Réservation", "Multilingue", "Riads & circuits"], opt="Tourisme & réservation", color="#ff5fa2",
         intro="Le tourisme marocain mérite des sites à la hauteur de ses destinations. Nous créons des vitrines et des systèmes de réservation qui rassurent le voyageur et facilitent la demande.",
         do=["Sites pour riads, hôtels, circuits et guides", "Calendriers de disponibilité et formulaires de réservation", "Intégration de paiements et de confirmations selon vos besoins", "Contenus multilingues", "Pages de destination optimisées pour la recherche locale"],
         why=["Parcours de réservation clair, du mobile au bureau", "Mise en valeur de vos offres et de vos visuels", "Visibilité locale renforcée (Google Business, SEO)"],
         who=["Riads, maisons d'hôtes et hôtels", "Agences et organisateurs de circuits", "Guides et activités touristiques", "Restaurants et services de réservation"]),
    dict(id="seo", n="03", cls="b3", title="SEO & visibilité locale", short="Référencement naturel et fiche Google Business pour être trouvé au bon moment.",
         tags=["SEO", "Google Business", "Contenu"], opt="SEO & Google Business", color="#49e1f6",
         intro="Être beau ne suffit pas : il faut être trouvé. Nous travaillons votre visibilité sur Google et Maps pour attirer des visiteurs qualifiés, là où se trouvent vos clients.",
         do=["Recherche de mots-clés et optimisation des pages", "Calendrier de contenus", "Création et optimisation de la fiche Google Business Profile", "Conseils photos et gestion des avis", "Intégration de Google Maps sur votre site"],
         why=["Meilleure visibilité dans les recherches locales", "Visiteurs plus qualifiés", "Base technique saine pour la durée"],
         who=["Commerces, restaurants et services locaux", "Riads et tour-opérateurs", "Prestataires qui veulent plus de demandes entrantes"]),
    dict(id="reseaux", n="04", cls="b4", title="Réseaux sociaux & marketing", short="Contenus, visuels et campagnes pour faire grandir votre audience et vos demandes.",
         tags=["Social media", "Campagnes", "Analyse"], opt="Réseaux sociaux & marketing", color="#bd36eb",
         intro="Une présence cohérente et régulière vaut mieux que des publications au hasard. Nous planifions, créons et mesurons pour que vos réseaux servent vos objectifs.",
         do=["Calendriers éditoriaux mensuels", "Gabarits de marque et visuels", "Vidéos courtes pour les réseaux", "Campagnes payantes, créations et suivi des conversions (Google et réseaux sociaux)", "Reporting"],
         why=["Image de marque cohérente", "Contenu planifié, sans improvisation", "Décisions basées sur des mesures"],
         who=["Créateurs", "Entreprises touristiques", "Restaurants et commerces"]),
    dict(id="identite", n="05", cls="b5", title="Identité visuelle & design", short="Logo, charte, supports print et digitaux : une marque reconnaissable et durable.",
         tags=["Logo", "Charte", "Print & digital"], opt="Identité visuelle", color="#ff9a7a",
         intro="Votre identité est la première chose qu'on retient de vous. Nous construisons des systèmes visuels simples à décliner, de la carte de visite au réseau social.",
         do=["Logos et systèmes visuels", "Chartes graphiques", "Papeterie, menus et supports marketing", "Gabarits pour réseaux sociaux"],
         why=["Cohérence sur tous vos supports", "Une marque qui se démarque", "Fichiers livrés prêts à l'usage"],
         who=["Nouvelles marques et relances", "Artisans et ateliers", "Restaurants, hôtels, créateurs"]),
    dict(id="video-3d", n="06", cls="b6", title="Vidéo, photo & 3D", short="Montage, vidéos promotionnelles, retouche photo, rendus 3D et visuels immersifs pour raconter votre histoire.",
         tags=["Montage vidéo", "Vidéo promo", "Retouche photo", "Rendus 3D"], opt="Vidéo & photo", color="#2a55f0",
         intro="L'image en mouvement retient l'attention. Du montage pour les réseaux aux films promotionnels, en passant par les rendus 3D de produits et d'espaces, nous donnons du relief à votre message.",
         do=["Montage vidéo, étalonnage, sous-titres, formats adaptés aux plateformes", "Vidéos promotionnelles et de storytelling : du concept à la livraison", "Retouche photo et visuels produit", "Rendus 3D, turntables et visuels architecturaux", "Assets 3D optimisés pour le web"],
         why=["Messages plus mémorables", "Formats adaptés à chaque plateforme", "Qualité visuelle homogène avec votre identité"],
         who=["Destinations, hôtels et événements", "Lancements de produits", "Marques qui veulent se démarquer"]),
]

MOTIFS = {
    "sites-web": '<svg class="motif" viewBox="0 0 200 200" fill="none" aria-hidden="true"><rect x="30" y="40" width="140" height="110" rx="14" stroke="url(#mg1)" stroke-width="3"/><path d="M30 68h140" stroke="url(#mg1)" stroke-width="3"/><circle cx="48" cy="54" r="4" fill="#ff5fa2"/><rect x="48" y="88" width="50" height="40" rx="8" fill="url(#mg1)" opacity=".5"/><defs><linearGradient id="mg1" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#5b3df5"/><stop offset="1" stop-color="#bd36eb"/></linearGradient></defs></svg>',
    "tourisme": '<svg class="motif" viewBox="0 0 200 200" fill="none" aria-hidden="true"><circle cx="100" cy="86" r="34" fill="url(#mg2)" opacity=".85"/><path d="M10 150q40-50 90-10t90-20" stroke="url(#mg2)" stroke-width="3"/><path d="M10 172q50-40 90-8t90-14" stroke="url(#mg2)" stroke-width="2" opacity=".6"/><defs><linearGradient id="mg2" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#ff9a7a"/><stop offset="1" stop-color="#bd36eb"/></linearGradient></defs></svg>',
    "seo": '<svg class="motif" viewBox="0 0 200 200" fill="none" aria-hidden="true"><circle cx="92" cy="92" r="46" stroke="url(#mg3)" stroke-width="4"/><path d="M126 126l42 42" stroke="url(#mg3)" stroke-width="6" stroke-linecap="round"/><path d="M68 108l20-22 16 14 20-30" stroke="#ff5fa2" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><defs><linearGradient id="mg3" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#49e1f6"/><stop offset="1" stop-color="#5b3df5"/></linearGradient></defs></svg>',
    "reseaux": '<svg class="motif" viewBox="0 0 200 200" fill="none" aria-hidden="true"><circle cx="100" cy="100" r="22" fill="url(#mg4)"/><g stroke="url(#mg4)" stroke-width="3"><circle cx="100" cy="100" r="46"/><circle cx="100" cy="100" r="72" stroke-dasharray="4 8"/></g><circle cx="146" cy="100" r="8" fill="#49e1f6"/><circle cx="52" cy="62" r="6" fill="#ff5fa2"/><defs><linearGradient id="mg4" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#bd36eb"/><stop offset="1" stop-color="#ff5fa2"/></linearGradient></defs></svg>',
    "identite": '<svg class="motif" viewBox="0 0 200 200" fill="none" aria-hidden="true"><path d="M40 150V60l60 90V60" stroke="url(#mg5)" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/><circle cx="144" cy="104" r="22" stroke="url(#mg5)" stroke-width="12"/><defs><linearGradient id="mg5" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#ff9a7a"/><stop offset="1" stop-color="#bd36eb"/></linearGradient></defs></svg>',
    "video-3d": '<svg class="motif" viewBox="0 0 200 200" fill="none" aria-hidden="true"><rect x="28" y="56" width="110" height="88" rx="16" stroke="url(#mg6)" stroke-width="3"/><path d="M138 86l40-22v72l-40-22z" stroke="url(#mg6)" stroke-width="3" stroke-linejoin="round"/><path d="M70 82l30 18-30 18z" fill="url(#mg6)"/><defs><linearGradient id="mg6" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#2a55f0"/><stop offset="1" stop-color="#49e1f6"/></linearGradient></defs></svg>',
}

# ------------------------------------------------------------------ pages meta
PAGES = [
    ("index.html", "Accueil"), ("services.html", "Services"), ("portfolio.html", "Réalisations"),
    ("pricing.html", "Offre"), ("about.html", "À propos"), ("contact.html", "Contact"),
]

def socials_list():
    out = [("Instagram", S.get("instagram")), ("Facebook", S.get("facebook")), ("GitHub", S.get("github")),
           ("LinkedIn", S.get("linkedin")), ("Upwork", S.get("upwork")), ("Google Maps", S.get("google_maps"))]
    return [(n, u) for n, u in out if u]

def same_as():
    return [u for _, u in socials_list()]

def header(cur):
    AC = ' aria-current="page"'
    items = "".join(
        '<a href="%s"%s>%s</a>' % (h, AC if h == cur else "", E(t))
        for h, t in PAGES if h != "contact.html")
    cta = '<a class="cta" href="contact.html"%s>Demander un devis</a>' % (AC if cur == "contact.html" else "")
    return f'''<div class="bg-aurora" aria-hidden="true"><i></i><i></i><i></i></div><div class="grain" aria-hidden="true"></div><div class="progress" aria-hidden="true"></div>
<a class="skip" href="#main">Aller au contenu</a>
<header class="hdr"><div class="hdr-in">
<a class="brand" href="index.html" aria-label="NKOB CREATORS — accueil"><img src="assets/img/logo-nkob.webp" alt="" width="40" height="26"><b>NKOB</b><span>Creators</span></a>
<nav class="nav" id="nav" aria-label="Navigation principale">{items}{cta}</nav>
<button class="burger" type="button" aria-expanded="false" aria-controls="nav" aria-label="Ouvrir le menu"><span></span><span></span><span></span></button>
</div></header>'''

def footer():
    soc = "".join(f'<li><a href="{E(u)}" target="_blank" rel="noopener noreferrer">{E(n)} ↗</a></li>' for n, u in socials_list())
    return f'''<footer class="ftr"><div class="wrap">
<p class="ftr-big">Donnons vie à <span class="grad">votre&nbsp;projet.</span></p>
<div class="ftr-grid">
<div><a class="brand" href="index.html"><img src="assets/img/logo-nkob.webp" alt="" width="40" height="26"><b>NKOB</b><span>Creators</span></a>
<p style="margin-top:16px;color:var(--mut);max-width:34ch">Studio digital basé au Maroc : sites web, identité visuelle, vidéo et 3D.</p></div>
<div><h4>Navigation</h4><ul>{"".join(f'<li><a href="{h}">{E(t)}</a></li>' for h, t in PAGES)}</ul></div>
<div><h4>Contact</h4><ul>
<li><a href="https://wa.me/{WA}" target="_blank" rel="noopener noreferrer">WhatsApp {PHONE_FMT}</a></li>
<li><a href="mailto:{E(MAIL)}">{E(MAIL)}</a></li>
<li><a href="{E(BASE)}/">{E(BASE.replace("https://", ""))}</a></li></ul></div>
<div><h4>Suivez-nous</h4><ul>{soc}</ul></div>
</div>
<div class="ftr-bot"><span>© <span id="year">2026</span> NKOB CREATORS — Tous droits réservés</span>
<span><a href="privacy.html">Confidentialité</a> · <a href="terms.html">Conditions</a> · <a href="cookies.html">Cookies</a></span></div>
</div></footer>
<a class="wa-float" href="https://wa.me/{WA}?text={WA_TEXT}" target="_blank" rel="noopener noreferrer" aria-label="Écrire sur WhatsApp"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 20.5l1.7-5.4A8.4 8.4 0 1 1 21 11.5z"/></svg><span>WhatsApp</span></a>
<button class="totop" type="button" aria-label="Retour en haut">↑</button>
<script src="assets/js/main.js" defer></script>'''

def head(fname, title, desc, og_title=None, noindex=False, extra=""):
    url = f"{BASE}/" if fname == "index.html" else f"{BASE}/{fname}"
    robots = '<meta name="robots" content="noindex,follow">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large">'
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<script>document.documentElement.className+=" js"</script>
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
{robots}
<meta name="theme-color" content="#0a0614">
<link rel="canonical" href="{url}">
<link rel="icon" href="favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="assets/img/favicon-32.png"><link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png"><link rel="manifest" href="site.webmanifest">
<meta property="og:type" content="website"><meta property="og:locale" content="fr_FR"><meta property="og:site_name" content="NKOB CREATORS">
<meta property="og:title" content="{E(og_title or title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/img/og-cover.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Logo NKOB CREATORS">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="assets/fonts/fraunces-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/hanken-grotesk-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/styles.css">
{extra}
</head>
<body>
'''

def jsonld(extra_graph=None):
    org = {
        "@type": "ProfessionalService", "@id": f"{BASE}/#organization", "name": "NKOB CREATORS", "url": f"{BASE}/",
        "logo": f"{BASE}/assets/img/icon-512.png", "image": f"{BASE}/assets/img/og-cover.jpg",
        "description": "Studio digital basé au Maroc : création de sites web, identité visuelle, vidéo, 3D, SEO local et solutions pour le tourisme.",
        "telephone": "+212611073479", "email": MAIL, "areaServed": {"@type": "Country", "name": "Maroc"},
        "sameAs": same_as(), "knowsLanguage": "fr",
    }
    graph = [org, {"@type": "WebSite", "@id": f"{BASE}/#website", "url": f"{BASE}/", "name": "NKOB CREATORS", "inLanguage": "fr", "publisher": {"@id": f"{BASE}/#organization"}}]
    if extra_graph: graph += extra_graph
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False) + "</script>"

def write(fname, content):
    with open(os.path.join(SITE, fname), "w", encoding="utf-8") as f:
        f.write(content)
    print("écrit", fname)

def page(fname, title, desc, body, **kw):
    cur = fname
    return head(fname, title, desc, **kw) + header(cur) + "\n" + body + "\n" + footer() + "\n</body>\n</html>\n"

CTA_BLOCK = '''<section class="sec" aria-labelledby="cta-t"><div class="wrap" style="text-align:center">
<p class="eyebrow rv" style="justify-content:center">Prêt à démarrer ?</p>
<h2 class="h-lg rv" id="cta-t" style="margin:22px auto 26px;max-width:18ch">Parlons de <span class="grad">votre projet</span></h2>
<p class="lead rv" style="margin:0 auto 34px">Décrivez votre besoin en quelques lignes : nous revenons vers vous avec une proposition claire.</p>
<div class="rv" style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap"><a class="btn btn-primary" href="contact.html">Demander un devis <span class="arr" aria-hidden="true">→</span></a><a class="btn btn-wa" href="https://wa.me/%s" target="_blank" rel="noopener noreferrer">Écrire sur WhatsApp</a></div>
</div></section>''' % WA

# ------------------------------------------------------------------ INDEX
def build_index():
    bento = ""
    for s in SERVICES:
        bento += f'''<a class="card {s["cls"]} rv" href="services.html#{s["id"]}">{MOTIFS[s["id"]]}
<span class="idx">{s["n"]}</span><h3>{E(s["title"])}</h3><p>{E(s["short"])}</p>
<div class="tags">{"".join(f'<span class="tag">{E(t)}</span>' for t in s["tags"])}</div><span class="go">Découvrir <span class="arr" aria-hidden="true">→</span></span></a>\n'''
    marquee = ["Sites web", "Identité visuelle", "Vidéo & motion", "Rendus 3D", "SEO local", "Réservation en ligne", "Réseaux sociaux", "WordPress"]
    mq = "".join(f"<span>{E(m)}</span>" for m in marquee * 2)
    steps = [("Découvrir", "Nous cernons vos objectifs, votre public et vos contraintes."), ("Planifier", "Architecture de l'information, périmètre et feuille de route."),
             ("Concevoir", "Interface, identité et prototypes pour recueillir vos retours."), ("Construire", "Développement responsive, optimisé pour le référencement, avec tests."),
             ("Lancer", "Mise en ligne, mesure d'audience et prise en main."), ("Accompagner", "Maintenance, évolutions et stratégie de croissance.")]
    steps_html = "".join(f'<div class="step rv"><div class="n">{i+1:02d}</div><h3>{E(t)}</h3><p>{E(d)}</p></div>' for i, (t, d) in enumerate(steps))
    faq = [("Combien de temps faut-il pour réaliser un site web ?", "Comptez en général 2 à 4 semaines pour un petit site, 4 à 8 semaines pour un site d'entreprise et 8 semaines ou plus pour une plateforme complexe. Les délais dépendent du périmètre et de la rapidité à fournir les contenus."),
           ("Proposez-vous de la maintenance après la mise en ligne ?", "Oui. Des forfaits de maintenance mensuels couvrent les mises à jour, les sauvegardes, la surveillance de sécurité et les petites modifications de contenu."),
           ("Travaillez-vous avec les acteurs du tourisme ?", "Oui, c'est l'une de nos spécialités : sites de riads et d'excursions, calendriers de disponibilité, parcours de réservation, contenus multilingues et visibilité locale."),
           ("Que dois-je préparer pour démarrer ?", "Un court descriptif de votre activité, vos objectifs, quelques exemples de sites ou de styles que vous aimez, et si possible votre logo et vos textes. Nous vous aidons à structurer le reste.")]
    faq_html = "".join(f'<details class="rv"><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in faq)
    faq_ld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}
    tools = ["HTML5", "CSS3", "JavaScript", "WordPress", "GitHub", "Canva", "Adobe", "Blender", "Google"]
    body = f'''<main id="main">
<section class="hero" aria-labelledby="h1"><div class="wrap hero-grid">
<div>
<p class="eyebrow rv">Studio digital · Maroc</p>
<h1 class="h-xl split" id="h1">Des expériences digitales qui <span class="grad">se remarquent</span> et qui convertissent.</h1>
<p class="lead rv" style="--d:.25s">NKOB CREATORS conçoit des sites web, des identités visuelles, des vidéos et des visuels 3D pour les entreprises, les créateurs et les acteurs du tourisme.</p>
<div class="hero-cta rv" style="--d:.35s"><a class="btn btn-primary" href="contact.html">Démarrer un projet <span class="arr" aria-hidden="true">→</span></a><a class="btn btn-ghost" href="portfolio.html">Voir les réalisations</a></div>
<a class="hero-offer rv" style="--d:.45s" href="pricing.html"><b>Offre</b><span>Création de site web dès <strong>2&nbsp;999&nbsp;DH</strong></span></a>
</div>
<div class="stage rv" style="--d:.2s" aria-hidden="true"><div class="glow"></div><div class="ring"></div><div class="ring r2"></div>
<div class="logo3d"><img src="assets/img/logo-nkob.webp" alt="" width="768" height="506" fetchpriority="high"></div>
<svg class="badge-rot" viewBox="0 0 128 128"><defs><path id="circ" d="M64 64m-48 0a48 48 0 1 1 96 0a48 48 0 1 1 -96 0"/></defs><text><textPath href="#circ">Studio digital • NKOB CREATORS • </textPath></text></svg><div class="badge-core">↗</div></div>
</div>
<div class="scroll-cue" aria-hidden="true"><i></i>Défiler</div></section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">{mq}</div></div>

<section class="sec" id="services" aria-labelledby="s-t"><div class="wrap">
<div class="sec-head"><span class="sec-num">01 / Services</span><h2 class="h-lg rv" id="s-t">Tout ce qu'il faut pour <span class="grad">exister en ligne</span>.</h2><p class="lead rv">Six expertises complémentaires, un seul interlocuteur, de la stratégie à la mise en ligne.</p></div>
<div class="bento">{bento}</div>
<p class="rv" style="margin-top:34px"><a class="btn btn-ghost" href="services.html">Voir tous les services en détail <span class="arr" aria-hidden="true">→</span></a></p>
</div></section>

<section class="sec" aria-labelledby="o-t" style="padding-top:0"><div class="wrap"><div class="offer rv"><div class="offer-grid">
<div><p class="price-pre">Offre de lancement · Création de site web</p><div class="price" id="o-t"><span>2&nbsp;999</span><small>DH · à partir de</small></div>
<p style="margin:22px 0 26px;font-size:1.15rem;max-width:44ch">Un site professionnel, rapide et responsive pour présenter votre activité et recevoir des demandes de clients.</p>
<div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-primary" style="background:#fff;color:#1b0f3a;box-shadow:none" href="pricing.html">Découvrir l'offre</a><a class="btn btn-ghost" href="contact.html?service=Site%20web">Demander un devis</a></div></div>
<ul class="checks"><li>Design sur mesure, adapté mobile, tablette et ordinateur</li><li>Structure pensée pour le référencement (SEO)</li><li>Boutons de contact direct : WhatsApp, e-mail</li><li>Mise en ligne et accompagnement à la prise en main</li></ul>
</div></div></div></section>

<section class="sec" id="realisations" aria-labelledby="p-t" style="padding-top:0"><div class="wrap">
<div class="sec-head"><span class="sec-num">02 / Réalisations</span><h2 class="h-lg rv" id="p-t">Des <span class="grad-cool">concepts</span> pour imaginer la suite.</h2><p class="lead rv">Voici des projets de démonstration, clairement identifiés comme tels. Vos propres réalisations pourront être ajoutées au même format.</p></div>
<div class="pgrid" id="pgrid"><noscript><p class="empty-note">Activez JavaScript pour parcourir les réalisations, ou ouvrez la <a href="portfolio.html">page Réalisations</a>.</p></noscript></div>
<p class="rv" style="margin-top:34px"><a class="btn btn-ghost" href="portfolio.html">Toutes les réalisations <span class="arr" aria-hidden="true">→</span></a></p>
</div></section>

<section class="sec" id="studio" aria-labelledby="w-t" style="padding-top:0"><div class="wrap split2">
<div><p class="eyebrow rv">Le studio</p><h2 class="h-lg rv" id="w-t" style="margin:22px 0">Un studio à taille humaine, <span class="grad">un seul interlocuteur</span>.</h2></div>
<div><p class="lead rv">NKOB CREATORS est un studio dirigé par son fondateur : création et technique sont réunies au même endroit. Les décisions sont plus rapides, la qualité plus constante, et vous échangez directement avec la personne qui réalise votre projet.</p>
<ul class="checks rv" style="margin:26px 0">
<li>Création et développement réunis, de la stratégie au lancement</li><li>Accent sur la performance et l'accessibilité</li><li>Connaissance du contexte marocain et du tourisme régional</li></ul>
<div class="skills rv" aria-label="Outils et technologies">{"".join(f"<span>{t}</span>" for t in tools)}</div>
<p class="fine rv">Outils utilisés au quotidien — ce ne sont ni des clients, ni des partenaires.</p>
<p class="rv" style="margin-top:28px"><a class="btn btn-ghost" href="about.html">En savoir plus <span class="arr" aria-hidden="true">→</span></a></p></div>
</div></section>

<section class="sec" id="methode" aria-labelledby="m-t" style="padding-top:0"><div class="wrap">
<div class="sec-head"><span class="sec-num">03 / Méthode</span><h2 class="h-lg rv" id="m-t">Un processus simple, <span class="grad">transparent</span>.</h2><p class="lead rv">Six étapes pour rester dans les délais et garder le contrôle à chaque jalon.</p></div>
<div class="steps">{steps_html}</div></div></section>

<section class="sec" id="faq" aria-labelledby="f-t" style="padding-top:0"><div class="wrap split2">
<div><p class="eyebrow rv">FAQ</p><h2 class="h-lg rv" id="f-t" style="margin-top:22px">Les questions <span class="grad">fréquentes</span>.</h2></div>
<div class="faq">{faq_html}</div></div></section>

{CTA_BLOCK}
</main>
<script src="assets/js/projects-data.js" defer></script>'''
    # le portfolio de l'accueil montre les 3 premiers concepts : géré via data-limit
    body = body.replace('id="pgrid"', 'id="pgrid" data-limit="3"')
    t = "NKOB CREATORS — Studio digital au Maroc : sites web, branding, vidéo & 3D"
    d = "NKOB CREATORS conçoit sites web, identités visuelles, vidéos et visuels 3D pour entreprises, créateurs et acteurs du tourisme au Maroc. Création de site dès 2 999 DH."
    write("index.html", page("index.html", t, d, body, extra=jsonld([faq_ld])))

# ------------------------------------------------------------------ SERVICES
def build_services():
    idx = "".join(f'<a href="#{s["id"]}"><span>{s["n"]}</span>{E(s["title"].split(" & ")[0] if len(s["title"])>26 else s["title"])}</a>' for s in SERVICES)
    secs = ""
    for s in SERVICES:
        lst = lambda arr: "".join(f"<li>{E(x)}</li>" for x in arr)
        secs += f'''<article class="svc" id="{s["id"]}" aria-labelledby="{s["id"]}-t">
<div class="svc-top"><div><span class="eyebrow rv">{s["n"]} — Service</span><h2 class="h-lg rv" id="{s["id"]}-t" style="margin:18px 0 18px">{E(s["title"])}</h2><p class="lead rv">{E(s["intro"])}</p></div>
<div class="svc-art rv" style="background:radial-gradient(circle at 30% 20%,{s["color"]}66,transparent 70%),rgba(255,255,255,.03)">{MOTIFS[s["id"]].replace('class="motif"', 'class=""')}</div></div>
<div class="cols"><div class="card rv"><h4>Ce que nous faisons</h4><ul>{lst(s["do"])}</ul></div><div class="card rv" style="--d:.08s"><h4>Vos bénéfices</h4><ul>{lst(s["why"])}</ul></div><div class="card rv" style="--d:.16s"><h4>Pour qui ?</h4><ul>{lst(s["who"])}</ul></div></div>
<p class="rv" style="margin-top:28px"><a class="btn btn-primary" href="contact.html?service={E(s["opt"].replace(" ", "%20").replace("&", "%26"))}">Demander ce service <span class="arr" aria-hidden="true">→</span></a></p></article>'''
    body = f'''<main id="main"><section class="page-hero"><div class="wrap"><p class="eyebrow rv">Services</p>
<h1 class="h-xl split">Une offre <span class="grad">complète</span>, un seul studio.</h1>
<p class="lead rv" style="--d:.2s">Sites web, tourisme et réservation, référencement, réseaux sociaux, identité visuelle, vidéo et 3D : chaque service comprend stratégie, réalisation et accompagnement.</p></div></section>
<section class="sec" style="padding-top:40px"><div class="wrap svc-layout"><nav class="svc-index" aria-label="Sommaire des services">{idx}</nav><div>{secs}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><ol class="steps" style="list-style:none;padding:0;margin:0"><li class="step rv"><div class="n">01</div><h3>Parlez-nous de votre projet</h3><p>Via le formulaire, WhatsApp ou par e-mail.</p></li><li class="step rv"><div class="n">02</div><h3>Recevez une proposition</h3><p>Nous revenons avec une proposition et un calendrier.</p></li><li class="step rv"><div class="n">03</div><h3>Lancement</h3><p>Réunion de lancement, puis jalons de validation.</p></li></ol>
<p class="fine rv">Besoin spécifique ou forfait sur mesure ? Contactez-nous pour un devis adapté.</p></div></section>
{CTA_BLOCK}</main>'''
    offers = [{"@type": "Service", "name": s["title"], "description": s["intro"], "provider": {"@id": f"{BASE}/#organization"}, "areaServed": "Maroc", "url": f"{BASE}/services.html#{s['id']}"} for s in SERVICES]
    write("services.html", page("services.html", "Services — Sites web, SEO, branding, vidéo, 3D | NKOB CREATORS",
        "Création de sites web et plateformes de réservation, SEO local, réseaux sociaux, identité visuelle, vidéo et 3D : découvrez tous les services de NKOB CREATORS.", body, extra=jsonld(offers)))

# ------------------------------------------------------------------ PORTFOLIO
def build_portfolio():
    body = '''<main id="main"><section class="page-hero"><div class="wrap"><p class="eyebrow rv">Réalisations</p>
<h1 class="h-xl split">Un aperçu de <span class="grad">notre univers</span>.</h1>
<p class="lead rv" style="--d:.2s">Concepts de démonstration couvrant nos principaux services. Chaque projet est clairement étiqueté : les entrées « Concept » ne sont pas des projets clients.</p></div></section>
<section class="sec" style="padding-top:40px"><div class="wrap"><div class="filters" id="filters" role="group" aria-label="Filtrer les réalisations"></div>
<div class="pgrid" id="pgrid"><noscript><p class="empty-note">Le portfolio interactif nécessite JavaScript. Contactez-nous pour recevoir des études de cas.</p></noscript></div>
<p class="empty-note rv">Vous voulez voir une étude de cas pour un service précis ? <a href="contact.html">Écrivez-nous</a> avec votre brief.</p></div></section>
<div class="lb" role="dialog" aria-modal="true" aria-hidden="true" aria-labelledby="lb-title"><button class="lb-close" type="button" aria-label="Fermer">✕</button>
<div class="lb-box"><div class="lb-media" id="lb-media"></div><div class="lb-info"><span class="eyebrow" id="lb-cat"></span><h3 id="lb-title"></h3><p id="lb-desc" style="color:var(--mut)"></p><div id="lb-links" style="display:flex;flex-wrap:wrap;gap:10px;margin-top:auto"></div></div></div></div>
''' + CTA_BLOCK + '''</main>
<script src="assets/js/projects-data.js" defer></script>'''
    write("portfolio.html", page("portfolio.html", "Réalisations & concepts — NKOB CREATORS",
        "Parcourez les concepts de démonstration de NKOB CREATORS : sites web, tourisme, identité visuelle, design graphique, vidéo, photo et SEO.", body, extra=jsonld()))

# ------------------------------------------------------------------ PRICING (offre)
def build_pricing():
    body = f'''<main id="main"><section class="page-hero"><div class="wrap"><p class="eyebrow rv">Offre</p>
<h1 class="h-xl split">Votre site web dès <span class="grad">2&nbsp;999&nbsp;DH</span>.</h1>
<p class="lead rv" style="--d:.2s">Un site professionnel, clair et rapide pour présenter votre activité et recevoir des demandes, avec un prix de départ transparent.</p></div></section>
<section class="sec" style="padding-top:30px"><div class="wrap"><div class="offer rv"><div class="offer-grid">
<div><p class="price-pre">Création de site web · à partir de</p><div class="price"><span>2&nbsp;999</span><small>DH</small></div>
<p style="margin:22px 0 26px;font-size:1.1rem;max-width:44ch">Le point de départ pour lancer ou moderniser votre présence en ligne. Le tarif final dépend du périmètre (nombre de pages, fonctionnalités, contenus) et est précisé dans un devis écrit.</p>
<a class="btn btn-primary" style="background:#fff;color:#1b0f3a;box-shadow:none" href="contact.html?service=Site%20web">Demander mon devis <span class="arr" aria-hidden="true">→</span></a></div>
<ul class="checks"><li>Design sur mesure et responsive (mobile, tablette, ordinateur)</li><li>Structure et balisage pensés pour le référencement</li><li>Pages rapides et accessibles</li><li>Boutons de contact direct : WhatsApp, e-mail</li><li>Mise en ligne et prise en main</li></ul></div>
<p class="fine">Prix « à partir de » en dirhams marocains. Les options (réservation en ligne, multilingue, contenus supplémentaires, etc.) sont chiffrées dans le devis.</p></div></div></section>
<section class="sec" style="padding-top:0" aria-labelledby="pq-t"><div class="wrap"><div class="sec-head"><span class="sec-num">Sur devis</span><h2 class="h-lg rv" id="pq-t">Des projets plus <span class="grad">ambitieux</span> ?</h2><p class="lead rv">Pour les besoins plus larges, nous établissons une proposition sur mesure après un échange sur vos objectifs.</p></div>
<div class="cols">
<div class="card rv"><h4>Sites d'entreprise</h4><ul><li>Multi-pages et structure de contenu</li><li>Blog, formulaires, CRM</li><li>Sur devis</li></ul></div>
<div class="card rv" style="--d:.08s"><h4>Tourisme & réservation</h4><ul><li>Calendrier de disponibilité</li><li>Parcours de réservation</li><li>Sur devis</li></ul></div>
<div class="card rv" style="--d:.16s"><h4>Identité, vidéo & 3D</h4><ul><li>Branding complet</li><li>Vidéos promotionnelles, rendus 3D</li><li>Sur devis</li></ul></div></div></div></section>
{CTA_BLOCK}</main>'''
    offer_ld = [{"@type": "Offer", "name": "Création de site web", "description": "Site web professionnel responsive, à partir de 2 999 DH.", "priceCurrency": "MAD", "price": "2999", "priceSpecification": {"@type": "PriceSpecification", "price": "2999", "priceCurrency": "MAD", "minPrice": "2999"}, "seller": {"@id": f"{BASE}/#organization"}, "url": f"{BASE}/pricing.html"}]
    write("pricing.html", page("pricing.html", "Création de site web dès 2 999 DH — NKOB CREATORS",
        "Offre de création de site web professionnel à partir de 2 999 DH : design sur mesure, responsive, optimisé SEO. Demandez votre devis auprès de NKOB CREATORS.", body, extra=jsonld(offer_ld)))

# ------------------------------------------------------------------ ABOUT
def build_about():
    tools = ["HTML5", "CSS3", "JavaScript", "WordPress", "GitHub", "Canva", "Adobe", "Blender", "SEO local", "Google Business Profile"]
    cvhtml = ""
    def tl(items):
        return '<ol class="timeline" style="list-style:none;padding:0">' + "".join(
            f'<li><time>{E(i.get("period",""))}</time><h3>{E(i.get("title",""))}</h3><p style="color:var(--mut)">{E(i.get("place",""))}{(" — " + E(i["details"])) if i.get("details") else ""}</p></li>' for i in items) + "</ol>"
    if CV.get("experience") or CV.get("formation"):
        cvhtml = '<section class="sec" style="padding-top:0" aria-labelledby="cv-t"><div class="wrap"><div class="sec-head"><span class="sec-num">Parcours</span><h2 class="h-lg rv" id="cv-t">Expérience & <span class="grad">formation</span></h2></div><div class="split2">'
        if CV.get("experience"): cvhtml += f'<div class="rv"><h3 class="h-md" style="margin-bottom:24px">Expérience</h3>{tl(CV["experience"])}</div>'
        if CV.get("formation"): cvhtml += f'<div class="rv"><h3 class="h-md" style="margin-bottom:24px">Formation</h3>{tl(CV["formation"])}</div>'
        cvhtml += '</div>'
        if CV.get("cv_pdf"): cvhtml += f'<p class="rv" style="margin-top:30px"><a class="btn btn-ghost" href="{E(CV["cv_pdf"])}" download>Télécharger le CV (PDF)</a></p>'
        cvhtml += '</div></section>'
    body = f'''<main id="main"><section class="page-hero"><div class="wrap"><p class="eyebrow rv">À propos</p>
<h1 class="h-xl split">Créativité, technique et <span class="grad">narration</span>.</h1>
<p class="lead rv" style="--d:.2s">NKOB CREATORS réunit création, développement et stratégie pour construire des expériences numériques utiles, belles et accessibles.</p></div></section>
<section class="sec" style="padding-top:40px"><div class="wrap split2">
<div><h2 class="h-md rv">Notre approche</h2></div>
<div><p class="lead rv">Nous sommes un studio indépendant, basé au Maroc et dirigé par son fondateur. Notre démarche est centrée sur l'humain : nous écoutons, prototypons, puis affinons avec vous.</p>
<p class="rv" style="color:var(--mut)">Nous pensons que la technologie doit être belle, accessible et durable. C'est pourquoi chaque projet vise des pages rapides, lisibles sur tous les écrans et faciles à faire évoluer.</p>
<p class="rv" style="color:var(--mut)">Au-delà des projets clients, nous développons des projets personnels — films courts, art génératif, expériences interactives — et nous partageons notre savoir-faire à travers des ateliers et du mentorat auprès de jeunes designers.</p></div></div></section>
<section class="sec" style="padding-top:0" aria-labelledby="sk-t"><div class="wrap"><div class="sec-head"><span class="sec-num">Compétences</span><h2 class="h-lg rv" id="sk-t">Outils & <span class="grad-cool">savoir-faire</span></h2><p class="lead rv">Les outils que nous utilisons au quotidien.</p></div>
<div class="skills rv">{"".join(f"<span>{t}</span>" for t in tools)}</div>
<div class="cols" style="margin-top:44px"><div class="card rv"><h4>Valeurs</h4><ul><li>Écoute et transparence</li><li>Qualité constante</li><li>Accessibilité et sobriété</li></ul></div><div class="card rv" style="--d:.08s"><h4>Domaines</h4><ul><li>Web et tourisme</li><li>Identité visuelle</li><li>Vidéo et 3D</li></ul></div><div class="card rv" style="--d:.16s"><h4>Contact direct</h4><ul><li><a href="https://wa.me/{WA}" target="_blank" rel="noopener noreferrer">WhatsApp {PHONE_FMT}</a></li><li><a href="mailto:{E(MAIL)}">{E(MAIL)}</a></li></ul></div></div></div></section>
{cvhtml}
{CTA_BLOCK}</main>'''
    write("about.html", page("about.html", "À propos — NKOB CREATORS, studio digital au Maroc",
        "Découvrez NKOB CREATORS : studio digital indépendant basé au Maroc, qui réunit création, développement et stratégie pour entreprises, créateurs et tourisme.", body, extra=jsonld()))

# ------------------------------------------------------------------ CONTACT
def build_contact():
    opts = ["Site web", "Landing page", "WordPress", "Tourisme & réservation", "SEO & Google Business", "Réseaux sociaux & marketing", "Identité visuelle", "Vidéo & photo", "3D & visualisation", "Maintenance & support", "Autre / à définir"]
    opt_html = '<option value="">Choisissez un service</option>' + "".join(f'<option value="{E(o)}">{E(o)}</option>' for o in opts)
    soc = "".join(f'<a href="{E(u)}" target="_blank" rel="noopener noreferrer"><span><small>Réseau</small>{E(n)}</span><span aria-hidden="true">↗</span></a>' for n, u in socials_list())
    body = f'''<main id="main"><section class="page-hero"><div class="wrap"><p class="eyebrow rv">Contact</p>
<h1 class="h-xl split">Lançons <span class="grad">votre projet</span>.</h1>
<p class="lead rv" style="--d:.2s">Décrivez-nous votre besoin : nous vous répondons avec une proposition claire.</p></div></section>
<section class="sec" style="padding-top:40px"><div class="wrap contact-grid">
<form class="form card rv" id="contact-form" data-wa="{WA}" data-mail="{E(MAIL)}" aria-label="Formulaire de demande de devis">
<div class="row2"><div class="fld"><label for="f-name">Nom *</label><input class="inp" id="f-name" name="name" autocomplete="name" required></div>
<div class="fld"><label for="f-email">E-mail *</label><input class="inp" id="f-email" type="email" name="email" autocomplete="email" required></div></div>
<div class="row2"><div class="fld"><label for="f-phone">Téléphone / WhatsApp</label><input class="inp" id="f-phone" type="tel" name="phone" autocomplete="tel"></div>
<div class="fld"><label for="f-service">Service souhaité</label><select id="f-service" name="service">{opt_html}</select></div></div>
<div class="fld"><label for="f-msg">Votre projet *</label><textarea id="f-msg" name="message" required placeholder="Objectifs, délais souhaités, exemples de sites que vous aimez…"></textarea></div>
<div class="form-actions"><button class="btn btn-wa" type="submit">Envoyer via WhatsApp</button><button class="btn btn-ghost" type="button" id="send-mail">Envoyer par e-mail</button></div>
<p class="form-note" id="form-status" role="status" aria-live="polite">Ce site est statique : votre message s'ouvre dans WhatsApp ou dans votre application e-mail, prêt à être envoyé. Rien n'est enregistré sur notre site.</p></form>
<aside class="clist rv" style="--d:.1s" aria-label="Coordonnées">
<a href="https://wa.me/{WA}" target="_blank" rel="noopener noreferrer"><span><small>WhatsApp</small>{PHONE_FMT}</span><span aria-hidden="true">↗</span></a>
<a href="mailto:{E(MAIL)}"><span><small>E-mail</small>{E(MAIL)}</span><span aria-hidden="true">→</span></a>
<a href="{E(BASE)}/"><span><small>Site web</small>{E(BASE.replace("https://", ""))}</span><span aria-hidden="true">→</span></a>
{soc}
<div class="card" style="padding:22px"><small style="color:var(--dim);letter-spacing:.14em;text-transform:uppercase;font-size:.78rem">Où nous trouver</small><p style="margin:8px 0 0">À distance, sur rendez-vous. Studio basé au Maroc.</p></div></aside>
</div></section></main>'''
    write("contact.html", page("contact.html", "Contact & devis — NKOB CREATORS",
        "Contactez NKOB CREATORS par WhatsApp (+212 611 073 479) ou par e-mail pour demander un devis : site web, branding, vidéo, 3D, SEO.", body, extra=jsonld()))

# ------------------------------------------------------------------ LEGAL
def legal(fname, title, desc, h1, content):
    body = f'<main id="main"><section class="page-hero"><div class="wrap"><p class="eyebrow">Informations légales</p><h1 class="h-lg" style="margin:22px 0 10px;max-width:none">{h1}</h1><p class="fine">Dernière mise à jour : {datetime.date.today().strftime("%d/%m/%Y")}</p></div></section><section class="sec" style="padding-top:20px"><div class="wrap prose">{content}</div></section></main>'
    write(fname, page(fname, title, desc, body, extra=jsonld()))

def build_legal():
    legal("privacy.html", "Politique de confidentialité — NKOB CREATORS", "Politique de confidentialité du site NKOB CREATORS : données collectées, finalités et vos droits.", "Politique de confidentialité", f'''
<p>NKOB CREATORS respecte votre vie privée. Cette page explique quelles informations peuvent être traitées lorsque vous nous contactez.</p>
<h2>Données que vous nous transmettez</h2><p>Ce site n'enregistre aucune donnée sur un serveur. Le formulaire de contact prépare un message (nom, e-mail, téléphone facultatif, service souhaité, description du projet) qui s'ouvre dans WhatsApp ou dans votre application e-mail : c'est vous qui décidez de l'envoyer. Si vous nous écrivez, nous utilisons ces informations uniquement pour répondre à votre demande et établir un devis.</p>
<h2>Services tiers</h2><p>Si vous cliquez sur WhatsApp, Instagram, Facebook ou un autre lien externe, vous quittez ce site et les conditions du service concerné s'appliquent.</p>
<h2>Vos droits</h2><p>Conformément à la législation marocaine applicable en matière de protection des données personnelles (loi n° 09-08), vous pouvez demander l'accès, la rectification ou la suppression des données que vous nous avez communiquées en écrivant à <a href="mailto:{E(MAIL)}">{E(MAIL)}</a>.</p>
<h2>Cookies</h2><p>Voir notre <a href="cookies.html">politique de cookies</a>.</p>''')
    legal("terms.html", "Conditions générales — NKOB CREATORS", "Conditions d'utilisation du site et cadre général des prestations de NKOB CREATORS.", "Conditions générales", f'''
<p>En consultant ce site et en nous transmettant une demande de projet, vous acceptez les présentes conditions.</p>
<h2>Prestations</h2><p>Les prestations sont définies pour chaque projet dans un devis écrit : périmètre, livrables, délais et modalités de paiement y sont précisés. Les tarifs « à partir de » affichés sur ce site sont indicatifs et ne constituent pas une offre ferme.</p>
<h2>Contenus du site</h2><p>Les visuels étiquetés « Concept » sont des démonstrations et ne représentent pas des projets clients. Les textes, visuels et le logo NKOB CREATORS sont protégés ; toute reproduction sans autorisation est interdite.</p>
<h2>Responsabilité</h2><p>Nous apportons le plus grand soin à l'exactitude des informations de ce site, sans garantie d'absence d'erreur. Les liens externes sont fournis à titre d'information.</p>
<h2>Contact</h2><p>Pour toute question : <a href="mailto:{E(MAIL)}">{E(MAIL)}</a>.</p>''')
    legal("cookies.html", "Politique de cookies — NKOB CREATORS", "NKOB CREATORS n'utilise aucun cookie de suivi : informations sur les cookies et le stockage sur ce site.", "Politique de cookies", f'''
<p>Ce site n'utilise aucun cookie publicitaire ni outil de mesure d'audience tiers, et ne dépose pas de cookie de suivi.</p>
<h2>Polices et ressources</h2><p>Les polices de caractères sont hébergées sur le site lui-même : aucune requête n'est envoyée à un service de polices externe.</p>
<h2>Liens externes</h2><p>Les services vers lesquels vous êtes redirigé (WhatsApp, réseaux sociaux) peuvent déposer leurs propres cookies selon leurs politiques.</p>
<h2>Questions</h2><p>Contact : <a href="mailto:{E(MAIL)}">{E(MAIL)}</a>.</p>''')

# ------------------------------------------------------------------ 404, blog redirect, SEO files
def build_misc():
    body = '<main id="main"><section class="page-hero"><div class="wrap" style="text-align:center"><p class="eyebrow" style="justify-content:center">Erreur 404</p><h1 class="h-xl" style="margin:22px auto;max-width:12ch">Page <span class="grad">introuvable</span>.</h1><p class="lead" style="margin:0 auto 30px">Le lien que vous avez suivi n\'existe plus ou a été déplacé.</p><a class="btn btn-primary" href="index.html">Retour à l\'accueil</a></div></section></main>'
    write("404.html", page("404.html", "Page introuvable — NKOB CREATORS", "Cette page n'existe pas.", body, noindex=True).replace("<head>", '<head>\n<base href="/">', 1))
    write("blog.html", f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Redirection — NKOB CREATORS</title><meta name="robots" content="noindex,follow"><link rel="canonical" href="{BASE}/"><meta http-equiv="refresh" content="0;url=index.html"></head><body><p>Cette page a été retirée. <a href="index.html">Retour à l'accueil</a>.</p></body></html>
''')
    pages = ["", "services.html", "portfolio.html", "pricing.html", "about.html", "contact.html", "privacy.html", "terms.html", "cookies.html"]
    prio = {"": "1.0", "services.html": "0.9", "pricing.html": "0.9", "portfolio.html": "0.8", "contact.html": "0.8", "about.html": "0.7"}
    urls = "".join(f"<url><loc>{BASE}/{p}</loc><lastmod>{TODAY}</lastmod><priority>{prio.get(p, '0.3')}</priority></url>" for p in pages)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    write("site.webmanifest", json.dumps({"name": "NKOB CREATORS", "short_name": "NKOB", "lang": "fr", "start_url": "/", "display": "standalone", "background_color": "#0a0614", "theme_color": "#0a0614",
        "icons": [{"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    build_index(); build_services(); build_portfolio(); build_pricing(); build_about(); build_contact(); build_legal(); build_misc()
