// NKOB-CREATORS shared JS
(() => {
  'use strict';
  const $ = s => document.querySelector(s);
  const $$ = s => Array.from(document.querySelectorAll(s));
  // Mobile nav
  const burger = $('.burger');
  const nav = $('.nav');
  if(burger && nav){
    burger.addEventListener('click', ()=>{
      nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', nav.classList.contains('open'));
    });
  }
  // Back to top
  const back = document.getElementById('back-to-top');
  if(back){
    window.addEventListener('scroll', ()=>{
      if(window.scrollY>400) back.classList.add('show'); else back.classList.remove('show');
    });
    back.addEventListener('click', ()=> window.scrollTo({top:0,behavior:'smooth'}));
  }
  // Intersection reveal
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('reveal'); io.unobserve(e.target); } });
  },{threshold:0.12});
  $$('section, .card, .project, .price').forEach(el=>io.observe(el));
  // Simple form handlers keep existing behavior
  $$('form').forEach(form=>{
    form.addEventListener('submit', e=>{
      // keep default behavior if action present
      const hasAction = !!form.getAttribute('action');
      if(!hasAction){
        e.preventDefault();
        // friendly UI response
        const btn = form.querySelector('button[type=submit]');
        const name = form.querySelector('input[name=name]')?.value || form.querySelector('input[type=email]')?.value || 'there';
        if(btn) btn.disabled=true;
        setTimeout(()=>{
          alert('Thanks '+name+" — your message was received (demo). We'll contact you shortly.");
          form.reset();
          if(btn) btn.disabled=false;
        },600);
      }
    });
  });
})();
