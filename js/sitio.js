// Menú móvil compartido
(function () {
  const btn = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.nav');
  if (!btn || !nav) return;
  btn.addEventListener('click', () => {
    const abierto = nav.classList.toggle('abierto');
    btn.setAttribute('aria-expanded', abierto ? 'true' : 'false');
    var en = document.documentElement.lang === 'en';
    btn.textContent = abierto ? (en ? 'Close' : 'Cerrar') : (en ? 'Menu' : 'Menú');
  });
})();

// Selector de idioma: conserva el enlace a una ficha (#H76) al cambiar de idioma
(function () {
  var l = document.querySelector('.nav a.lang');
  if (!l) return;
  l.addEventListener('click', function () {
    if (location.hash) l.setAttribute('href', l.getAttribute('href').split('#')[0] + location.hash);
  });
})();
