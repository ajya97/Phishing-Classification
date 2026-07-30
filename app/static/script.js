/* ==========================================================================
   CyberShield AI — Frontend Interactions
   No backend logic is touched here. Form action/method/name are untouched.
   ========================================================================== */

document.addEventListener('DOMContentLoaded', function () {

  /* ------------------------------------------------------------------
     Footer year
  ------------------------------------------------------------------ */
  var yearEl = document.getElementById('year');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  /* ------------------------------------------------------------------
     AOS Animations
  ------------------------------------------------------------------ */
  if (window.AOS) {
    AOS.init({
      duration: 800,
      easing: 'ease-out-cubic',
      once: true,
      offset: 60
    });
  }

  /* ------------------------------------------------------------------
     Particles.js Background
  ------------------------------------------------------------------ */
  if (window.particlesJS && document.getElementById('particles-js')) {
    particlesJS('particles-js', {
      particles: {
        number: { value: 55, density: { enable: true, value_area: 900 } },
        color: { value: ['#3b82f6', '#22d3ee', '#60a5fa'] },
        shape: { type: 'circle' },
        opacity: { value: 0.35, random: true },
        size: { value: 2.5, random: true },
        line_linked: {
          enable: true,
          distance: 140,
          color: '#22d3ee',
          opacity: 0.12,
          width: 1
        },
        move: {
          enable: true,
          speed: 0.8,
          direction: 'none',
          random: true,
          straight: false,
          out_mode: 'out'
        }
      },
      interactivity: {
        detect_on: 'canvas',
        events: {
          onhover: { enable: true, mode: 'grab' },
          onclick: { enable: false },
          resize: true
        },
        modes: {
          grab: { distance: 140, line_linked: { opacity: 0.25 } }
        }
      },
      retina_detect: true
    });
  }

  /* ------------------------------------------------------------------
     Typed.js — Rotating words in hero
  ------------------------------------------------------------------ */
  var typedEl = document.getElementById('typed-text');
  if (typedEl && window.Typed) {
    new Typed('#typed-text', {
      strings: ['Phishing Links', 'Fake Login Pages', 'Malicious Redirects', 'Scam Websites'],
      typeSpeed: 55,
      backSpeed: 30,
      backDelay: 1500,
      startDelay: 300,
      loop: true,
      smartBackspace: true
    });
  }

  /* ------------------------------------------------------------------
     Counter Animation — Statistics Section
  ------------------------------------------------------------------ */
  var counters = document.querySelectorAll('.stat-number');

  function animateCounter(el) {
    var target = parseInt(el.getAttribute('data-count'), 10) || 0;
    var duration = 1600;
    var startTime = null;

    function step(timestamp) {
      if (!startTime) startTime = timestamp;
      var progress = Math.min((timestamp - startTime) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3); // ease-out-cubic
      el.textContent = Math.floor(eased * target);
      if (progress < 1) {
        requestAnimationFrame(step);
      } else {
        el.textContent = target;
      }
    }
    requestAnimationFrame(step);
  }

  if ('IntersectionObserver' in window && counters.length) {
    var counterObserver = new IntersectionObserver(function (entries, observer) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.4 });

    counters.forEach(function (counter) {
      counterObserver.observe(counter);
    });
  } else {
    counters.forEach(animateCounter);
  }

  /* ------------------------------------------------------------------
     GSAP — subtle hero entrance
  ------------------------------------------------------------------ */
  if (window.gsap) {
    gsap.from('.hero-badge', { opacity: 0, y: -16, duration: 0.7, ease: 'power2.out' });
    gsap.from('.hero-title', { opacity: 0, y: 24, duration: 0.8, delay: 0.1, ease: 'power2.out' });
    gsap.from('.hero-subtitle', { opacity: 0, y: 24, duration: 0.8, delay: 0.25, ease: 'power2.out' });
    gsap.from('.hero-scroll-cta', { opacity: 0, y: 24, duration: 0.8, delay: 0.4, ease: 'power2.out' });
  }

  /* ------------------------------------------------------------------
     Smooth Scrolling for in-page anchors
  ------------------------------------------------------------------ */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var targetId = this.getAttribute('href');
      if (targetId.length > 1) {
        var targetEl = document.querySelector(targetId);
        if (targetEl) {
          e.preventDefault();
          var offset = 90;
          var top = targetEl.getBoundingClientRect().top + window.pageYOffset - offset;
          window.scrollTo({ top: top, behavior: 'smooth' });
        }
      }
    });
  });

  /* ------------------------------------------------------------------
     URL Detection Form — validation + loading state
     IMPORTANT: This does NOT prevent the real submission to /predict.
     It only validates client-side and shows a loading state, then lets
     the native form POST proceed exactly as the backend expects.
  ------------------------------------------------------------------ */
  var predictForm = document.getElementById('predictForm');
  var urlInput = document.getElementById('urlInput');
  var detectBtn = document.getElementById('detectBtn');
  var formHint = document.getElementById('formHint');

  function isLikelyUrl(value) {
    if (!value) return false;
    var trimmed = value.trim();
    // Reasonably permissive check: requires at least one dot and no spaces,
    // and optionally a protocol. Backend remains the source of truth.
    var pattern = /^(https?:\/\/)?([\w-]+\.)+[\w-]{2,}(\/[^\s]*)?$/i;
    return pattern.test(trimmed);
  }

  if (predictForm && urlInput && detectBtn) {
    predictForm.addEventListener('submit', function (e) {
      var value = urlInput.value.trim();

      if (!isLikelyUrl(value)) {
        e.preventDefault();
        urlInput.classList.add('is-invalid-glow');
        if (formHint) {
          formHint.classList.add('hint-error');
          formHint.innerHTML = '<i class="fa-solid fa-circle-exclamation me-1"></i> Please enter a valid URL (e.g. https://example.com)';
        }
        urlInput.focus();
        setTimeout(function () {
          urlInput.classList.remove('is-invalid-glow');
        }, 450);
        return false;
      }

      // Valid — show loading state, then allow native submit to /predict
      detectBtn.setAttribute('disabled', 'true');
      detectBtn.querySelector('.btn-text').classList.add('d-none');
      detectBtn.querySelector('.btn-loader').classList.remove('d-none');
      // Note: form submits natively here (no e.preventDefault()),
      // hitting the Flask /predict route exactly as required.
    });

    urlInput.addEventListener('input', function () {
      urlInput.classList.remove('is-invalid-glow');
      if (formHint) {
        formHint.classList.remove('hint-error');
        formHint.innerHTML = '<i class="fa-solid fa-circle-info me-1"></i> Example: https://example.com';
      }
    });
  }

  /* ------------------------------------------------------------------
     Result Page — animated confidence progress bar
  ------------------------------------------------------------------ */
  var confidenceFill = document.querySelector('.confidence-fill');
  if (confidenceFill) {
    var confidenceValue = parseFloat(confidenceFill.getAttribute('data-confidence')) || 0;
    // Delay slightly so the width transition is visible on load
    setTimeout(function () {
      confidenceFill.style.width = Math.min(Math.max(confidenceValue, 0), 100) + '%';
    }, 300);
  }

  /* ------------------------------------------------------------------
     Navbar shadow on scroll
  ------------------------------------------------------------------ */
  var nav = document.querySelector('.navbar-glass');
  if (nav) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 30) {
        nav.style.boxShadow = '0 10px 30px rgba(0,0,0,0.35)';
      } else {
        nav.style.boxShadow = 'none';
      }
    });
  }

});
