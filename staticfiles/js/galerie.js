document.addEventListener('DOMContentLoaded', function() {
    // Filtrage des éléments
    const filterBtns = document.querySelectorAll('.filter-btn');
    const galerieItems = document.querySelectorAll('.galerie-item');
    
    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Active le bouton cliqué
            filterBtns.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            
            const filter = this.getAttribute('data-filter');
            
            // Filtre les éléments
            galerieItems.forEach(item => {
                if (filter === 'all' || item.getAttribute('data-category') === filter) {
                    item.style.display = 'block';
                    setTimeout(() => {
                        item.style.opacity = '1';
                        item.style.transform = 'translateY(0)';
                    }, 100);
                } else {
                    item.style.opacity = '0';
                    item.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        item.style.display = 'none';
                    }, 300);
                }
            });
        });
    });
    
    // Lightbox functionality
    const quickViewBtns = document.querySelectorAll('.quick-view');
    const lightbox = document.querySelector('.lightbox');
    const lightboxImg = document.querySelector('.lightbox-img');
    const lightboxInfo = document.querySelector('.lightbox-info');
    const closeBtn = document.querySelector('.close-btn');
    
    quickViewBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const item = this.closest('.galerie-item');
            const imgSrc = item.querySelector('img').src;
            const title = item.querySelector('h3').textContent;
            const details = item.querySelector('.details').cloneNode(true);
            const price = item.querySelector('.price').cloneNode(true);
            
            lightboxImg.src = imgSrc;
            lightboxImg.alt = title;
            
            lightboxInfo.innerHTML = '';
            lightboxInfo.appendChild(document.createElement('h3')).textContent = title;
            lightboxInfo.appendChild(details);
            lightboxInfo.appendChild(price);
            
            lightbox.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    });
    
    closeBtn.addEventListener('click', function() {
        lightbox.classList.remove('active');
        document.body.style.overflow = 'auto';
    });
    
    lightbox.addEventListener('click', function(e) {
        if (e.target === lightbox) {
            lightbox.classList.remove('active');
            document.body.style.overflow = 'auto';
        }
    });
    
    // Animation au chargement
    const animateItems = function() {
        const items = document.querySelectorAll('.galerie-item');
        items.forEach((item, index) => {
            setTimeout(() => {
                item.style.opacity = '1';
                item.style.transform = 'translateY(0)';
            }, 100 * index);
        });
    };
    
    // Délai pour permettre le rendu initial
    setTimeout(animateItems, 300);
});