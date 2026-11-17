// Nav background on scroll
const nav = document.getElementById('nav');
const onScroll = () => nav.classList.toggle('scrolled', scrollY > 20);
addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Mobile menu
const links = document.getElementById('links');
document.getElementById('menuBtn').onclick = () => links.classList.toggle('open');
links.querySelectorAll('a').forEach(a => (a.onclick = () => links.classList.remove('open')));

// Highlight the current page in the nav
const page = document.body.dataset.page;
links.querySelectorAll('a').forEach(a => {
  if (a.dataset.page === page) a.classList.add('active');
});

// Reveal on scroll
const io = new IntersectionObserver(
  es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }),
  { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
);
document.querySelectorAll('.reveal').forEach(el => {
  const sibs = [...el.parentElement.children].filter(c => c.classList.contains('reveal'));
  if (sibs.length > 1) el.style.transitionDelay = (sibs.indexOf(el) % 4) * 90 + 'ms';
  io.observe(el);
});

// Lightbox
const lb = document.createElement('div');
lb.className = 'lb';
lb.innerHTML = '<img alt="">';
document.body.append(lb);
const lbImg = lb.querySelector('img');
document.querySelectorAll('.shots img,.strip img,.mp .stack img,.gallery img,.minis img,[data-zoom]').forEach(img => {
  img.style.cursor = 'zoom-in';
  img.addEventListener('click', e => { e.preventDefault(); lbImg.src = img.src; lbImg.alt = img.alt; lb.classList.add('open'); });
});
lb.onclick = () => lb.classList.remove('open');
addEventListener('keydown', e => { if (e.key === 'Escape') lb.classList.remove('open'); });

const yr = document.getElementById('yr');
if (yr) yr.textContent = new Date().getFullYear();
