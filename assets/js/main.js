/* NKOB CREATORS — interactions (vanilla JS, aucune dépendance) */
(function () {
  "use strict";
  var doc = document;
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, c) { return (c || doc).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || doc).querySelectorAll(s)); };

  /* ---------- header, burger, progress, back to top ---------- */
  var hdr = $(".hdr"), burger = $(".burger"), nav = $(".nav"), bar = $(".progress"), totop = $(".totop");
  function setMenu(open) {
    if (!burger || !nav) return;
    burger.setAttribute("aria-expanded", open ? "true" : "false");
    burger.setAttribute("aria-label", open ? "Fermer le menu" : "Ouvrir le menu");
    nav.classList.toggle("open", open);
    doc.body.style.overflow = open ? "hidden" : "";
  }
  if (burger) {
    burger.addEventListener("click", function () { setMenu(burger.getAttribute("aria-expanded") !== "true"); });
    $$("a", nav).forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
    doc.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });
  }
  var ticking = false;
  function onScroll() {
    var y = window.pageYOffset || doc.documentElement.scrollTop;
    var h = doc.documentElement.scrollHeight - window.innerHeight;
    if (hdr) hdr.classList.toggle("scrolled", y > 24);
    if (bar) bar.style.transform = "scaleX(" + (h > 0 ? Math.min(y / h, 1) : 0) + ")";
    if (totop) totop.classList.toggle("show", y > 700);
    ticking = false;
  }
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();
  if (totop) totop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }); });

  /* ---------- split headline into words ---------- */
  $$(".split").forEach(function (el) {
    var i = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = doc.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (part) {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.appendChild(doc.createTextNode(" ")); return; }
            var w = doc.createElement("span"), s = doc.createElement("span");
            w.className = "w"; s.textContent = part; s.style.setProperty("--i", i++); w.appendChild(s); frag.appendChild(w);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1) { walk(n); }
      });
    })(el);
  });

  /* ---------- reveal on scroll ---------- */
  var revealEls = $$(".rv, .split");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
    revealEls.forEach(function (el) { io.observe(el); });
  } else { revealEls.forEach(function (el) { el.classList.add("in"); }); }

  /* ---------- pointer glow on cards ---------- */
  $$(".card").forEach(function (c) {
    c.addEventListener("pointermove", function (e) {
      var r = c.getBoundingClientRect();
      c.style.setProperty("--mx", (e.clientX - r.left) + "px");
      c.style.setProperty("--my", (e.clientY - r.top) + "px");
    });
  });

  /* ---------- hero logo tilt + magnetic buttons (desktop pointers only) ---------- */
  var fine = window.matchMedia && window.matchMedia("(pointer: fine)").matches;
  var stage = $(".stage");
  if (stage && fine && !reduce) {
    var l3 = $(".logo3d", stage);
    doc.addEventListener("pointermove", function (e) {
      var r = stage.getBoundingClientRect();
      var dx = (e.clientX - (r.left + r.width / 2)) / window.innerWidth;
      var dy = (e.clientY - (r.top + r.height / 2)) / window.innerHeight;
      l3.style.setProperty("--ry", (dx * 26).toFixed(2) + "deg");
      l3.style.setProperty("--rx", (-dy * 22).toFixed(2) + "deg");
    });
  }
  if (fine && !reduce) {
    $$(".btn").forEach(function (b) {
      b.addEventListener("pointermove", function (e) {
        var r = b.getBoundingClientRect();
        b.style.setProperty("--bx", ((e.clientX - r.left - r.width / 2) * 0.18).toFixed(1) + "px");
        b.style.setProperty("--by", ((e.clientY - r.top - r.height / 2) * 0.28).toFixed(1) + "px");
      });
      b.addEventListener("pointerleave", function () { b.style.setProperty("--bx", "0px"); b.style.setProperty("--by", "0px"); });
    });
  }

  /* ---------- services index: highlight current section ---------- */
  var idx = $$(".svc-index a");
  if (idx.length && "IntersectionObserver" in window) {
    var map = {};
    idx.forEach(function (a) { map[a.getAttribute("href").slice(1)] = a; });
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { idx.forEach(function (a) { a.classList.remove("on"); }); if (map[en.target.id]) map[en.target.id].classList.add("on"); }
      });
    }, { rootMargin: "-35% 0px -60% 0px" });
    $$(".svc").forEach(function (s) { so.observe(s); });
  }

  /* ---------- portfolio : rendu depuis assets/js/projects-data.js ---------- */
  var grid = $("#pgrid");
  var data = window.NKOB_PROJECTS;
  if (grid && data && data.projects) {
    var cats = data.categories || {};
    var lb = $(".lb"), lbMedia = $("#lb-media"), lbT = $("#lb-title"), lbD = $("#lb-desc"), lbC = $("#lb-cat"), lbL = $("#lb-links"), lastFocus = null;
    var esc = function (s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };

    var limit = parseInt(grid.getAttribute("data-limit"), 10) || data.projects.length;
    grid.innerHTML = data.projects.slice(0, limit).map(function (p, i) {
      var thumb = p.image || p.poster || "";
      return '<button type="button" class="proj rv" data-cat="' + esc(p.category) + '" data-i="' + i + '" style="--d:' + ((i % 3) * 0.08) + 's" aria-haspopup="dialog">' +
        '<div class="thumb"><img src="' + esc(thumb) + '" alt="' + esc(p.alt || p.title) + '" width="1200" height="800" loading="lazy" decoding="async"></div>' +
        '<div class="cap"><div><span class="cat">' + esc(cats[p.category] || p.category) + '</span><h3>' + esc(p.title) + '</h3></div>' +
        (p.label ? '<span class="lbl">' + esc(p.label) + '</span>' : "") + '</div></button>';
    }).join("");
    $$(".proj", grid).forEach(function (el) { if ("IntersectionObserver" in window && !reduce) { io.observe(el); } else { el.classList.add("in"); } });

    var fwrap = $("#filters");
    if (fwrap) {
      var used = {}; data.projects.forEach(function (p) { used[p.category] = 1; });
      var html = '<button type="button" class="fbtn" aria-pressed="true" data-f="all">Tout</button>';
      Object.keys(cats).forEach(function (k) { if (used[k]) html += '<button type="button" class="fbtn" aria-pressed="false" data-f="' + k + '">' + esc(cats[k]) + "</button>"; });
      fwrap.innerHTML = html;
      fwrap.addEventListener("click", function (e) {
        var b = e.target.closest(".fbtn"); if (!b) return;
        $$(".fbtn", fwrap).forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        var f = b.getAttribute("data-f");
        $$(".proj", grid).forEach(function (el) { el.hidden = !(f === "all" || el.getAttribute("data-cat") === f); });
      });
    }

    function openLb(i) {
      var p = data.projects[i]; if (!p || !lb) return;
      lastFocus = doc.activeElement;
      lbMedia.innerHTML = "";
      if (p.video) {
        var v = doc.createElement("video"); v.controls = true; v.preload = "metadata"; v.playsInline = true;
        if (p.poster) v.poster = p.poster; v.src = p.video; v.setAttribute("aria-label", p.title); lbMedia.appendChild(v);
      } else {
        var im = doc.createElement("img"); im.src = p.image; im.alt = p.alt || p.title; lbMedia.appendChild(im);
      }
      lbC.textContent = (cats[p.category] || p.category) + (p.label ? " · " + p.label : "");
      lbT.textContent = p.title; lbD.textContent = p.description || "";
      lbL.innerHTML = (p.links || []).map(function (l) { return '<a class="btn btn-ghost" href="' + esc(l.url) + '" target="_blank" rel="noopener noreferrer">' + esc(l.label) + ' <span class="arr" aria-hidden="true">↗</span></a>'; }).join("") +
        '<a class="btn btn-primary" href="contact.html?service=' + encodeURIComponent(p.service || "") + '">Un projet similaire ? <span class="arr" aria-hidden="true">→</span></a>';
      lb.classList.add("open"); lb.setAttribute("aria-hidden", "false"); doc.body.style.overflow = "hidden";
      $(".lb-close", lb).focus();
    }
    function closeLb() {
      if (!lb || !lb.classList.contains("open")) return;
      lb.classList.remove("open"); lb.setAttribute("aria-hidden", "true"); doc.body.style.overflow = "";
      var v = $("video", lbMedia); if (v) v.pause(); lbMedia.innerHTML = "";
      if (lastFocus) lastFocus.focus();
    }
    grid.addEventListener("click", function (e) { var b = e.target.closest(".proj"); if (b) openLb(+b.getAttribute("data-i")); });
    if (lb) {
      $(".lb-close", lb).addEventListener("click", closeLb);
      lb.addEventListener("click", function (e) { if (e.target === lb) closeLb(); });
      doc.addEventListener("keydown", function (e) {
        if (e.key === "Escape") closeLb();
        if (e.key === "Tab" && lb.classList.contains("open")) { // simple focus trap
          var f = $$("a,button,video", lb).filter(function (x) { return !x.disabled; });
          if (!f.length) return; var first = f[0], last = f[f.length - 1];
          if (e.shiftKey && doc.activeElement === first) { e.preventDefault(); last.focus(); }
          else if (!e.shiftKey && doc.activeElement === last) { e.preventDefault(); first.focus(); }
        }
      });
    }
  }

  /* ---------- contact form : WhatsApp ou e-mail (site statique, sans serveur) ---------- */
  var form = $("#contact-form");
  if (form) {
    var WA = form.getAttribute("data-wa"), MAIL = form.getAttribute("data-mail");
    var qs = new URLSearchParams(window.location.search), pre = qs.get("service");
    if (pre && form.elements.service) { for (var k = 0; k < form.elements.service.options.length; k++) { if (form.elements.service.options[k].value === pre) form.elements.service.selectedIndex = k; } }
    var status = $("#form-status");
    function compose() {
      var f = form.elements;
      return {
        subject: "Demande de devis — " + (f.service.value || "projet") + " — " + f.name.value.trim(),
        body: "Bonjour NKOB CREATORS,\n\nNom : " + f.name.value.trim() + "\nE-mail : " + f.email.value.trim() +
          (f.phone.value.trim() ? "\nTéléphone : " + f.phone.value.trim() : "") +
          "\nService : " + (f.service.value || "À définir") + "\n\nMon projet :\n" + f.message.value.trim()
      };
    }
    function valid() {
      if (!form.checkValidity()) { form.reportValidity(); return false; } return true;
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault(); if (!valid()) return;
      var m = compose();
      window.open("https://wa.me/" + WA + "?text=" + encodeURIComponent(m.body), "_blank", "noopener");
      if (status) status.textContent = "WhatsApp s'ouvre avec votre message prêt à être envoyé.";
    });
    var mailBtn = $("#send-mail");
    if (mailBtn) mailBtn.addEventListener("click", function () {
      if (!valid()) return; var m = compose();
      window.location.href = "mailto:" + MAIL + "?subject=" + encodeURIComponent(m.subject) + "&body=" + encodeURIComponent(m.body);
      if (status) status.textContent = "Votre application e-mail s'ouvre avec votre message prêt à être envoyé.";
    });
  }

  var y = $("#year"); if (y) y.textContent = new Date().getFullYear();
})();
