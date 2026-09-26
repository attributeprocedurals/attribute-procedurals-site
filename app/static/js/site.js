const menu = document.querySelector('.menu-btn');
const links = document.querySelector('.nav-links');
if (menu) menu.addEventListener('click', () => {
  const open = links.classList.toggle('open');
  menu.setAttribute('aria-expanded', String(open));
});
links?.querySelectorAll('a').forEach(a => a.addEventListener('click', () => links.classList.remove('open')));
