# NKOB CREATORS — Final website (French)

Static website (plain HTML + CSS + vanilla JavaScript). No framework, no build step required to run it, no external requests (fonts are self-hosted, no analytics, no CDN).

## Contents

```
index.html  services.html  portfolio.html  pricing.html  about.html  contact.html
privacy.html  terms.html  cookies.html  404.html  blog.html (redirect to home)
CNAME            -> nkob45.com (kept exactly as in your original files)
.nojekyll        -> tells GitHub Pages to serve files as-is (harmless elsewhere)
robots.txt  sitemap.xml  site.webmanifest  favicon.ico
assets/css/styles.css
assets/js/main.js            interactions (menu, animations, portfolio viewer, contact form)
assets/js/projects-data.js   portfolio data  <- edit this to add real projects
assets/fonts/                Fraunces + Hanken Grotesk (SIL OFL licences included)
assets/img/                  logo (transparent), icons, social cover image, concept visuals
assets/media/                put your real project images / videos here
tools/                       optional: build.py (regenerates the pages), check.py (link checker)
```

## Preview locally

Any static server works. With Python (installed on most computers):

```
cd NKOB-CREATORS-WEBSITE-FINAL     # the unzipped folder
python3 -m http.server 8000
```
Open http://localhost:8000. (Opening index.html by double-click also works, but use a server for the most faithful result.)

## Deploy to your existing hosting

Your original `CNAME` file (`nkob45.com`) suggests GitHub Pages, but your hosting provider was not stated, so check which applies:

* **GitHub Pages:** replace the repository content with the contents of this folder (the files must be at the repository root, next to `CNAME`), commit and push. Do not change DNS or the Pages settings.
* **cPanel / FTP / any shared host:** upload the *contents* of this folder (not the folder itself) into the web root (`public_html` or equivalent), overwriting the old files. Keep your existing DNS. `CNAME` and `.nojekyll` are not needed there but are harmless.
* **Netlify / Vercel / Cloudflare Pages:** publish the folder as-is (no build command, publish directory = root).

After upload, hard-refresh (Ctrl/Cmd+Shift+R) and test: all pages, the WhatsApp button, the contact form, and `https://nkob45.com/sitemap.xml`. Then submit the sitemap in Google Search Console.

Old filenames like `index(6).html` should not be uploaded: use the clean names above. `blog.html` is kept only as a redirect to the home page so old links do not break.

## Things you must complete (nothing was invented)

1. **Social links.** Only the real URLs found in your files are used: Instagram, Facebook, WhatsApp, e-mail, website. **GitHub, Upwork, LinkedIn and Google Maps URLs were not in your files**, so they do not appear. To add them, put the URL in `tools/content/socials.json`, then run `python3 tools/build.py`. Pages regenerate, links appear in the footer, contact page and structured data. (Or edit the footer in each HTML file by hand.)
2. **CV / experience / education.** No CV was provided. Fill `tools/content/cv.json` (examples below), put your PDF in `assets/cv/` and set `"cv_pdf": "assets/cv/cv.pdf"`, then run `python3 tools/build.py`: a "Parcours" section appears on `about.html`.
   ```json
   {"experience":[{"period":"2023 — 2024","title":"Your real title","place":"Employer / client","details":"What you did"}],
    "formation":[{"period":"2022","title":"Diploma","place":"School"}],
    "cv_pdf":"assets/cv/cv.pdf"}
   ```
3. **Real projects, screenshots, videos.** No project images or videos were provided. The portfolio currently shows 7 clearly labelled **"Concept"** visuals. To add real work: copy the files to `assets/media/`, then add an entry in `assets/js/projects-data.js` (a commented example is included; videos use `"video"` + `"poster"`). Delete the concept entries when you have enough real ones.
4. **Contact form.** A static site has no server, so the form opens WhatsApp (or your e-mail app) with the message pre-filled. If you want messages delivered silently to your inbox, you need a form service or a small backend — tell me which one you use and I can wire it in.
5. **Legal pages.** The privacy / terms / cookies pages are generic and contain no company registration details (none were provided). Have them reviewed and add your legal entity information if required.
6. **Offer wording.** "From 2,999 DH" is shown as requested. The included features list (responsive design, SEO-ready structure, contact buttons, publishing) is a conservative description; adjust it in `tools/build.py` (function `build_pricing`/`build_index`) or directly in `pricing.html` and `index.html` if your real offer differs.

## Editing content

* Edit the HTML pages directly, **or** edit `tools/build.py` and re-run it (it regenerates all pages from templates; direct edits to the generated HTML would be overwritten the next time you run it — choose one workflow).
* Colours and fonts: variables at the top of `assets/css/styles.css`.
* Check links/assets after changes: `python3 tools/check.py`.

## Tested

Static link/anchor/asset/ID/JSON-LD checks (`tools/check.py`), HTML parsing with html5lib, JavaScript syntax check, and real-browser tests (Chromium) at widths 360, 390, 768, 1024 and 1440 px: no horizontal overflow, no console errors, no failed requests, mobile menu, portfolio filter/viewer and contact form working. Not tested: Safari/Firefox, real phones, Lighthouse scores, the live hosting.
