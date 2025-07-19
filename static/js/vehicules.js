document.addEventListener('DOMContentLoaded', function() {
  // Filtrage des véhicules
  const filterBtns = document.querySelectorAll('.filter-btn');
  const vehiculeCards = document.querySelectorAll('.vehicule-card');
  
  filterBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      // Active le bouton cliqué
      filterBtns.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');
      
      const filter = this.getAttribute('data-filter');
      
      // Filtre les cartes
      vehiculeCards.forEach(card => {
        if (filter === 'all' || card.getAttribute('data-category') === filter) {
          card.style.display = 'block';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 100);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'translateY(20px)';
          setTimeout(() => {
            card.style.display = 'none';
          }, 300);
        }
      });
    });
  });
  
  // Smooth scroll pour les ancres
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        window.scrollTo({
          top: targetElement.offsetTop - 80,
          behavior: 'smooth'
        });
      }
    });
  });
  
  // Menu mobile
  const menuToggle = document.querySelector('.menu-toggle');
  const navUl = document.querySelector('nav ul');
  
  if (menuToggle) {
    menuToggle.addEventListener('click', function() {
      navUl.classList.toggle('show');
    });
  }
});