// Travel Map Implementation
document.addEventListener('DOMContentLoaded', function() {
  // Travel data injected from Jekyll
  const travelData = window.travelData || [];

  // Build values object for svgMap
  const values = {};
  travelData.forEach(country => {
    values[country.code] = { visited: 1 };
  });

  // Initialize svgMap
  const map = new svgMap({
    targetElementID: 'travel-map',
    colorMin: '#E8D5F2',
    colorMax: '#9B59B6',
    colorNoData: '#E5E5E5',
    hideFlag: true,
    noDataText: 'Not visited yet',
    data: {
      data: {
        visited: {
          name: 'Visited'
        }
      },
      applyData: 'visited',
      values: values
    }
  });

  // Modal elements
  const modal = document.getElementById('travel-modal');
  const modalTitle = modal.querySelector('.travel-modal__title');
  const modalYear = modal.querySelector('.travel-modal__year');
  const modalCaption = modal.querySelector('.travel-modal__caption');
  const modalPhoto = modal.querySelector('.travel-modal__photo');
  const modalDots = modal.querySelector('.travel-modal__dots');
  const prevBtn = modal.querySelector('.travel-modal__nav--prev');
  const nextBtn = modal.querySelector('.travel-modal__nav--next');
  const closeBtn = modal.querySelector('.travel-modal__close');
  const backdrop = modal.querySelector('.travel-modal__backdrop');

  let currentCountry = null;
  let currentPhotoIndex = 0;

  // Find country data by code
  function getCountryByCode(code) {
    return travelData.find(c => c.code === code);
  }

  // Update photo display
  function showPhoto(index) {
    if (!currentCountry || !currentCountry.photos) return;

    const photos = currentCountry.photos;
    currentPhotoIndex = ((index % photos.length) + photos.length) % photos.length;

    const photoPath = `/assets/images/travel/${photos[currentPhotoIndex]}`;
    modalPhoto.src = photoPath;
    modalPhoto.alt = `${currentCountry.name} - Photo ${currentPhotoIndex + 1}`;

    // Update dots
    const dots = modalDots.querySelectorAll('.travel-modal__dot');
    dots.forEach((dot, i) => {
      dot.classList.toggle('active', i === currentPhotoIndex);
    });

    // Show/hide nav buttons based on photo count
    const showNav = photos.length > 1;
    prevBtn.style.display = showNav ? '' : 'none';
    nextBtn.style.display = showNav ? '' : 'none';
  }

  // Create dots for photo navigation
  function createDots(count) {
    modalDots.innerHTML = '';
    if (count <= 1) return;

    for (let i = 0; i < count; i++) {
      const dot = document.createElement('button');
      dot.className = 'travel-modal__dot';
      dot.setAttribute('aria-label', `Go to photo ${i + 1}`);
      dot.addEventListener('click', () => showPhoto(i));
      modalDots.appendChild(dot);
    }
  }

  // Open modal for a country
  function openModal(countryCode) {
    const country = getCountryByCode(countryCode);
    if (!country) return;

    currentCountry = country;
    currentPhotoIndex = 0;

    modalTitle.textContent = country.name;
    modalYear.textContent = country.year ? `Visited in ${country.year}` : '';
    modalCaption.textContent = country.caption || '';

    createDots(country.photos ? country.photos.length : 0);
    showPhoto(0);

    modal.hidden = false;
    document.body.style.overflow = 'hidden';
    closeBtn.focus();
  }

  // Close modal
  function closeModal() {
    modal.hidden = true;
    document.body.style.overflow = '';
    currentCountry = null;
  }

  // Event listeners for modal
  closeBtn.addEventListener('click', closeModal);
  backdrop.addEventListener('click', closeModal);
  prevBtn.addEventListener('click', () => showPhoto(currentPhotoIndex - 1));
  nextBtn.addEventListener('click', () => showPhoto(currentPhotoIndex + 1));

  // Keyboard navigation
  document.addEventListener('keydown', function(e) {
    if (modal.hidden) return;

    switch (e.key) {
      case 'Escape':
        closeModal();
        break;
      case 'ArrowLeft':
        showPhoto(currentPhotoIndex - 1);
        break;
      case 'ArrowRight':
        showPhoto(currentPhotoIndex + 1);
        break;
    }
  });

  // Add click handlers to visited countries on the map
  setTimeout(() => {
    const svgContainer = document.querySelector('#travel-map .svgMap-map-wrapper');
    if (!svgContainer) return;

    svgContainer.addEventListener('click', function(e) {
      const country = e.target.closest('[data-id]');
      if (!country) return;

      const countryCode = country.getAttribute('data-id');
      if (getCountryByCode(countryCode)) {
        openModal(countryCode);
      }
    });

    // Add cursor pointer to visited countries
    travelData.forEach(country => {
      const el = svgContainer.querySelector(`[data-id="${country.code}"]`);
      if (el) {
        el.style.cursor = 'pointer';
      }
    });
  }, 100);
});
