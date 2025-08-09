// static/js/nav.js
document.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.getElementById('mobile-menu-toggle');
  const navMenu = document.getElementById('mobile-nav');

  toggleBtn?.addEventListener('click', () => {
    navMenu?.classList.toggle('active');
    toggleBtn?.classList.toggle('open');  // animate icon
  });
});

