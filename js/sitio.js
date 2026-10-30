// Menú móvil compartido
(function () {
  const btn = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.nav');
  if (!btn || !nav) return;
  btn.addEventListener('click', () => {
    const abierto = nav.classList.toggle('abierto');
    btn.setAttribute('aria-expanded', abierto ? 'true' : 'false');
    btn.textContent = abierto ? 'Cerrar' : 'Menú';
  });
})();
