document.addEventListener("DOMContentLoaded", () => {
  // 1. Общая анимация fade-up (все кроме why-us и services)
  const commonFadeEls = document.querySelectorAll(".fade-up:not(.why-us-section):not(.services-section)");
  const commonObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.classList.add("visible");
        }, index * 150);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: "0px 0px -15% 0px"
  });
  commonFadeEls.forEach((el) => commonObserver.observe(el));

  
  // 2. Для services — запуск при -30%
  const servicesEl = document.querySelector(".services-section");
  if (servicesEl) {
    const servicesObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");

          // Анимация кнопок
          const serviceButtons = document.querySelectorAll(".service-button");
          serviceButtons.forEach((btn, i) => {
            setTimeout(() => {
              btn.classList.add("animated");
            }, i * 150);
          });
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: "0px 0px -30% 0px"
    });
    servicesObserver.observe(servicesEl);
  }

  // 3. Для секции "Почему мы" (why-us) — запуск при -20%
  const whyUsEls = document.querySelectorAll(".why-us-section.fade-up");
  if (whyUsEls.length) {
    const whyUsObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
          setTimeout(() => {
            entry.target.classList.add("visible");
          }, index * 150);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: "0px 0px -10% 0px" // отступ для старта анимации
    });

    // Наблюдаем за каждым элементом в секции
    whyUsEls.forEach(el => whyUsObserver.observe(el));
  }

});



// Получаем все карточки
const slides_whyus = document.querySelectorAll(".slide-whyus2");
const section = document.querySelector(".why-us2");

// Проверяем, что секция есть
if (section && slides_whyus.length > 0) {
  // Создаем контейнер для статической сетки
  const staticContainer = document.createElement("div");
  staticContainer.className = "why-us2-static";

  // Добавляем карточки в статический контейнер
  slides_whyus.forEach((slide) => {
    const clone = slide.cloneNode(true);
    clone.className = "slide-whyus2-static";
    staticContainer.appendChild(clone);
  });

  // Вставляем после исходной секции
  section.parentNode.insertBefore(staticContainer, section.nextSibling);

  // Скрываем оригинальную секцию
  section.style.display = "none";

  // Показываем статическую сетку
  staticContainer.style.display = "grid";
  staticContainer.style.opacity = "1";
}



// фильтрация для категорий на слайдере
const categoryButtons = document.querySelectorAll('.catalog-categories button');
const slides = document.querySelectorAll('.slide');

categoryButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    categoryButtons.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const category = btn.dataset.category;
    slides.forEach(slide => {
      if (slide.dataset.category === category || category === 'Все') {
        slide.style.display = 'flex';
      } else {
        slide.style.display = 'none';
      }
    });
  });
});
let activeCategory = null;

categoryButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const category = btn.dataset.category;

    if (activeCategory === category) {
      // Сброс фильтра
      activeCategory = null;
      categoryButtons.forEach(b => b.classList.remove('active'));
      slides.forEach(slide => slide.style.display = 'flex');
    } else {
      // Включаем фильтр
      activeCategory = category;
      categoryButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      slides.forEach(slide => {
        if (slide.dataset.category === category) {
          slide.style.display = 'flex';
        } else {
          slide.style.display = 'none';
        }
      });
    }
  });
  slides.forEach(slide => slide.classList.remove('active'));
});


const slider = document.querySelector('.catalog-slider');
let autoScrollPaused = false;
let pauseTimeout;

function pauseAutoScroll() {
  autoScrollPaused = true;
  clearTimeout(pauseTimeout);
  pauseTimeout = setTimeout(() => autoScrollPaused = false, 10000); // 10 секунд
}

// Слушаем все возможные действия пользователя
slider.addEventListener('mousedown', pauseAutoScroll);
slider.addEventListener('touchstart', pauseAutoScroll);
slider.addEventListener('touchmove', pauseAutoScroll);
slider.addEventListener('wheel', pauseAutoScroll, { passive: true });
categoryButtons.forEach(btn => btn.addEventListener('click', pauseAutoScroll));

// Один единственный интервал
setInterval(() => {
  if (!autoScrollPaused) {
    // Если мы в самом конце — возвращаемся к началу
    if (slider.scrollLeft + slider.clientWidth >= slider.scrollWidth - 5) {
      slider.scrollTo({ left: 0, behavior: 'smooth' });
    } else {
      // Иначе продолжаем листать
      slider.scrollBy({ left: slider.clientWidth / 2, behavior: 'smooth' });
    }
  }
}, 3000);

document.addEventListener("DOMContentLoaded", () => {
  const slides = document.querySelectorAll(".slide");

  slides.forEach(slide => {
    slide.addEventListener("click", (e) => {
      // сначала убираем выделение со всех карточек
      slides.forEach(s => s.classList.remove("active"));

      // добавляем только на ту, по которой кликнули
      slide.classList.add("active");

      // чтобы клик по кнопке внутри карточки не ломал выделение
      e.stopPropagation();
    });
  });

  // клик вне карточек сбрасывает выделение
  document.addEventListener("click", () => {
    slides.forEach(s => s.classList.remove("active"));
  });
});




const swiper = new Swiper('.services-slider .swiper', {
  loop: true,
  autoplay: {
    delay: 3000,
    disableOnInteraction: false, // автоплей не отключаем
  },
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
});

let autoplayTimeout;

function pauseAutoplayOnClick() {
  // Останавливаем автоплей
  swiper.autoplay.stop();
  
  // Очищаем предыдущий таймер (если есть)
  clearTimeout(autoplayTimeout);
  
  // Запускаем автоплей через 10 секунд
  autoplayTimeout = setTimeout(() => {
    swiper.autoplay.start();
  }, 10000);
}

// Вешаем обработчик только на клик/тап
swiper.el.addEventListener('click', pauseAutoplayOnClick);
swiper.el.addEventListener('touchstart', pauseAutoplayOnClick, { passive: true });



// Cекция 7, модальное окно
const openBtn = document.getElementById('openModal-rw');
const modal = document.getElementById('reviewsModal-rw');
const closeBtn = document.getElementById('closeModal-rw');
const reviewsList = document.querySelector('.reviews-list-rw');
const prevArrow = document.querySelector('.carousel-arrow-prev-rw');
const nextArrow = document.querySelector('.carousel-arrow-next-rw');
const mainView = document.querySelector('.main-view-rw');
const fullReviewView = document.querySelector('.full-review-view-rw');
const backArrow = document.querySelector('.back-arrow-rw');
const fullReviewContent = document.querySelector('.full-review-content-rw');

if (openBtn && modal && closeBtn && reviewsList && prevArrow && nextArrow && mainView && fullReviewView && backArrow && fullReviewContent) {
  let isScrolling = false;

  function openModal() {
    modal.style.display = 'flex';
    document.documentElement.classList.add('no-scroll-rw');
    modal.setAttribute('aria-hidden', 'false');
    setTimeout(() => {
      modal.classList.add('active'); // Добавляем класс для анимации
      mainView.classList.add('active');
    }, 10); // Небольшая задержка для триггера transition
    closeBtn.focus();
    reviewsList.scrollTo({ left: 0, behavior: 'auto' });
    mainView.style.display = 'flex';
    fullReviewView.style.display = 'none';
    processReviews();
  }
  
  function closeModal() {
    modal.classList.remove('active');
    mainView.classList.remove('active');
    fullReviewView.classList.remove('active');
    document.documentElement.classList.remove('no-scroll-rw');
    modal.setAttribute('aria-hidden', 'true');
    setTimeout(() => {
      modal.style.display = 'none'; // Скрываем после завершения анимации
    }, 300); // Соответствует длительности transition
    openBtn.focus();
  }

  function isAtEnd() {
    const tolerance = 10;
    return reviewsList.scrollLeft + reviewsList.clientWidth >= reviewsList.scrollWidth - tolerance;
  }

  function isAtStart() {
    return reviewsList.scrollLeft <= 10;
  }

  function scrollCarousel(direction) {
    if (isScrolling) return;
    
    isScrolling = true;
    
    const card = reviewsList.querySelector('.review-card-rw');
    if (!card) return;
    
    const cardWidth = card.offsetWidth;
    const gap = parseInt(getComputedStyle(reviewsList).gap) || 0;
    const scrollAmount = (cardWidth + gap) * direction;
    
    if (direction === 1 && isAtEnd()) {
      reviewsList.scrollTo({ left: 0, behavior: 'smooth' });
    } else if (direction === -1 && isAtStart()) {
      reviewsList.scrollTo({ left: reviewsList.scrollWidth, behavior: 'smooth' });
    } else {
      reviewsList.scrollBy({ left: scrollAmount, behavior: 'smooth' });
    }
    
    setTimeout(() => { isScrolling = false; }, 400);
  }

  function processReviews() {
    const cards = document.querySelectorAll('.review-card-rw');
    cards.forEach(card => {
      const textElem = card.querySelector('.review-text-rw');
      const fullText = card.dataset.fullText;
      const textBox = card.querySelector('.review-text-box-rw');
      
      const existingMore = textBox.querySelector('.more-rw');
      if (existingMore) existingMore.remove();
      
      textElem.textContent = fullText;
      textElem.style.display = '-webkit-box';
      
      if (textElem.scrollHeight > textElem.clientHeight) {
        const more = document.createElement('span');
        more.className = 'more-rw';
        more.textContent = '...';
        more.addEventListener('click', () => showFullReview(card));
        textBox.appendChild(more);
        more.style.display = 'block';
      } else {
        textElem.style.display = 'block';
      }
    });
  }

  function showFullReview(card) {
    fullReviewContent.innerHTML = `
      <p class="review-name-rw">${card.querySelector('.review-name-rw').textContent}</p>
      <p class="review-service-rw">${card.querySelector('.review-service-rw').textContent}</p>
      <p class="review-text-rw">${card.dataset.fullText}</p>
    `;
    
    mainView.classList.remove('active');
    mainView.style.display = 'none';
    fullReviewView.style.display = 'flex';
    setTimeout(() => {
      fullReviewView.classList.add('active');
    }, 10);
  }

  backArrow.addEventListener('click', () => {
    fullReviewView.classList.remove('active');
    fullReviewView.style.display = 'none';
    mainView.style.display = 'flex';
    setTimeout(() => {
      mainView.classList.add('active');
    }, 10);
  });

  prevArrow.addEventListener('click', (e) => {
    e.preventDefault();
    scrollCarousel(-1);
  });
  
  nextArrow.addEventListener('click', (e) => {
    e.preventDefault();
    scrollCarousel(1);
  });

  openBtn.addEventListener('click', openModal);
  closeBtn.addEventListener('click', closeModal);

  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.style.display === 'flex') closeModal();
  });

  let touchStartX = 0;
  
  reviewsList.addEventListener('touchstart', (e) => {
    touchStartX = e.touches[0].clientX;
  });
  
  reviewsList.addEventListener('touchend', (e) => {
    const touchEndX = e.changedTouches[0].clientX;
    const diffX = touchStartX - touchEndX;
    
    if (Math.abs(diffX) > 50) {
      scrollCarousel(diffX > 0 ? 1 : -1);
    }
  });

  reviewsList.addEventListener('scroll', () => {
    isScrolling = true;
    clearTimeout(reviewsList.scrollTimeout);
    reviewsList.scrollTimeout = setTimeout(() => {
      isScrolling = false;
    }, 100);
  });
}






// Бесконечная карусель для секции "Наши работы"
function initInfiniteCarousel() {
  const track = document.querySelector('.works-track');
  const slides = document.querySelectorAll('.works-slide');
  
  if (!track || slides.length === 0) return;
  
  // Рассчитываем общую ширину одного набора слайдов
  let singleSetWidth = 0;
  slides.forEach(slide => {
    singleSetWidth += slide.offsetWidth + parseInt(getComputedStyle(track).gap);
  });
  
  // Клонируем слайды столько раз, чтобы заполнить экран + запас
  const viewportWidth = window.innerWidth;
  const neededClones = Math.ceil(viewportWidth / singleSetWidth) + 2;
  
  for (let i = 0; i < neededClones; i++) {
    slides.forEach(slide => {
      const clone = slide.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      track.appendChild(clone);
    });
  }
  
  let animationId;
  let position = 0;
  const speed = 0.8; // пикселей за кадр
  
  function animate() {
    position -= speed;
    
    // Сбрасываем позицию когда уехали на ширину оригинальных слайдов
    if (Math.abs(position) >= singleSetWidth) {
      position = 0;
    }
    
    track.style.transform = `translate3d(${position}px, 0, 0)`;
    animationId = requestAnimationFrame(animate);
  }
  
  // Запускаем анимацию
  animate();
  
  // Пауза при наведении
  track.addEventListener('mouseenter', () => {
    cancelAnimationFrame(animationId);
  });
  
  track.addEventListener('mouseleave', () => {
    animationId = requestAnimationFrame(animate);
  });
  
  // Переинициализация при ресайзе
  window.addEventListener('resize', () => {
    cancelAnimationFrame(animationId);
    // Очищаем клоны
    const allSlides = track.querySelectorAll('.works-slide');
    const originalSlides = Array.from(allSlides).slice(0, slides.length);
    track.innerHTML = '';
    originalSlives.forEach(slide => track.appendChild(slide));
    // Перезапускаем
    setTimeout(initInfiniteCarousel, 100);
  });
}

document.addEventListener('DOMContentLoaded', initInfiniteCarousel);


// Обработчик для всех якорных ссылок
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', function(e) {
    e.preventDefault();
    const targetId = this.getAttribute('href');
    const targetElement = document.querySelector(targetId);
    
    if (targetElement) {
      gsap.to(window, {
        duration: 1,
        scrollTo: targetElement
      });
    } else {
      console.warn(`Элемент ${targetId} не найден`);
    }
  });
});