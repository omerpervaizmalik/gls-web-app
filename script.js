// Set current year in footer
document.getElementById('year').textContent = new Date().getFullYear();

// Navbar Scroll Effect
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Intersection Observer for Scroll Animations
const observeElements = () => {
    const elements = document.querySelectorAll('.animate-on-scroll');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // If it's a container, stagger its children
                if (entry.target.classList.contains('animate-container')) {
                    const children = entry.target.children;
                    Array.from(children).forEach((child, index) => {
                        child.style.transitionDelay = `${index * 0.15}s`;
                        child.classList.add('is-visible');
                    });
                } else {
                    entry.target.classList.add('is-visible');
                }
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    });

    elements.forEach(element => {
        observer.observe(element);
    });
};

// Footer Links Logic
document.addEventListener('DOMContentLoaded', () => {
    const footerContainer = document.querySelector('.footer .container');
    if (footerContainer && typeof contentDB !== 'undefined' && contentDB.footer && contentDB.footer["Quick Links"]) {
        const linksRaw = contentDB.footer["Quick Links"].split('\n').filter(l => l.trim().length > 0);
        if (linksRaw.length > 0) {
            const linksHtml = linksRaw.map(l => {
                const text = l.replace('>', '').trim();
                let href = "https://iris.fbr.gov.pk/infosys/public/txplogin.xhtml";
                if (text === "Privacy Policy") href = "privacy-policy.html";
                if (text === "Terms of Service") href = "terms.html";
                if (text === "Help Center") href = "help.html";
                return `<a href="${href}" ${href.startsWith('http') ? 'target="_blank"' : ''} style="color: var(--gold-dim); margin: 0 10px; font-size: 0.8rem; text-decoration: none; transition: color 0.3s ease;">${text}</a>`;
            }).join(' | ');
            
            const linksDiv = document.createElement('div');
            linksDiv.style.marginTop = "1rem";
            linksDiv.style.borderTop = "1px solid rgba(212, 175, 55, 0.1)";
            linksDiv.style.paddingTop = "1rem";
            linksDiv.innerHTML = linksHtml;
            footerContainer.appendChild(linksDiv);
        }
    }
});

// Initialize after DOM load
document.addEventListener('DOMContentLoaded', observeElements);

// Remove splash screen after opening animation
window.addEventListener('load', () => {
    const splash = document.getElementById('splash-screen');
    if (splash) {
        setTimeout(() => {
            splash.style.opacity = '0';
            splash.style.transition = 'opacity 0.6s ease';
            setTimeout(() => {
                splash.remove();
            }, 600);
        }, 1800);
    }
});

// Mobile Menu Logic
document.addEventListener('DOMContentLoaded', () => {
    const menuBtn = document.getElementById('menu-btn');
    const navLinks = document.getElementById('nav-links');

    // Inject overlay backdrop for mobile nav
    const overlay = document.createElement('div');
    overlay.classList.add('nav-overlay');
    overlay.id = 'nav-overlay';
    document.body.appendChild(overlay);

    function openNav() {
        menuBtn.classList.add('active');
        navLinks.classList.add('active');
        overlay.classList.add('active');
        document.body.classList.add('nav-open');
        menuBtn.setAttribute('aria-expanded', 'true');
    }

    function closeNav() {
        menuBtn.classList.remove('active');
        navLinks.classList.remove('active');
        overlay.classList.remove('active');
        document.body.classList.remove('nav-open');
        menuBtn.setAttribute('aria-expanded', 'false');
    }

    if (menuBtn && navLinks) {
        menuBtn.addEventListener('click', () => {
            if (navLinks.classList.contains('active')) {
                closeNav();
            } else {
                openNav();
            }
        });

        // Close on overlay click
        overlay.addEventListener('click', closeNav);

        // Close on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && navLinks.classList.contains('active')) {
                closeNav();
            }
        });

        // On mobile: tap nav-link-main to toggle dropdown
        navLinks.querySelectorAll('li').forEach(li => {
            const trigger = li.querySelector('.nav-link-main');
            const dropdown = li.querySelector('.dropdown-menu');
            if (trigger && dropdown) {
                trigger.addEventListener('click', (e) => {
                    // Only intercept on mobile (menu-btn is visible)
                    if (window.getComputedStyle(menuBtn).display !== 'none') {
                        e.preventDefault();
                        const isOpen = li.classList.contains('mobile-open');
                        // Close all others
                        navLinks.querySelectorAll('li.mobile-open').forEach(openLi => {
                            openLi.classList.remove('mobile-open');
                        });
                        if (!isOpen) {
                            li.classList.add('mobile-open');
                        }
                    }
                });
            }
        });

        // Close menu when clicking a non-dropdown link
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', (e) => {
                // If it's a nav-link-main on mobile, handled above
                if (link.classList.contains('nav-link-main') && window.getComputedStyle(menuBtn).display !== 'none') {
                    return;
                }
                closeNav();
            });
        });
    }

    // Initialize Testimonial Carousel if on Index Page
    if (document.getElementById('testimonial-track')) {
        initTestimonialCarousel();
        initCounters();
    }
});

// Counter-Up Animation Logic
function initCounters() {
    const statsSection = document.querySelector('.stats-bar');
    const counters = document.querySelectorAll('.stat-number');
    let started = false;

    if (!statsSection || counters.length === 0) return;

    const startCounter = () => {
        counters.forEach(counter => {
            const target = +counter.getAttribute('data-target');
            const suffix = counter.getAttribute('data-suffix') || '';
            const duration = 2000; // 2 seconds
            const frameRate = 1000 / 60;
            const totalFrames = Math.round(duration / frameRate);
            let frame = 0;

            const updateCount = () => {
                frame++;
                const progress = frame / totalFrames;
                // Ease out expo for a premium feel
                const easeOutExpo = (x) => x === 1 ? 1 : 1 - Math.pow(2, -10 * x);
                const currentCount = Math.floor(target * easeOutExpo(progress));

                if (frame < totalFrames) {
                    counter.textContent = currentCount.toLocaleString() + suffix;
                    requestAnimationFrame(updateCount);
                } else {
                    counter.textContent = target.toLocaleString() + suffix;
                }
            };
            updateCount();
        });
    };

    const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting && !started) {
            // Reveal the stat items with stagger
            document.querySelectorAll('.stat-item').forEach((el, i) => {
                setTimeout(() => el.classList.add('is-visible'), i * 150);
            });
            startCounter();
            started = true;
        }
    }, { threshold: 0.3 });

    observer.observe(statsSection);
}

// Testimonial Carousel Logic
function initTestimonialCarousel() {
    const track = document.getElementById('testimonial-track');
    const dotContainer = document.getElementById('carousel-dots');
    
    if (!track || typeof contentDB === 'undefined' || !contentDB.home.Testimonials) return;

    // Parse Testimonials
    const rawContent = contentDB.home.Testimonials;
    const blocks = rawContent.split(/\d+\.\s+/).filter(b => b.trim().length > 0);
    
    const testimonials = blocks.map(block => {
        const lines = block.split('\n').map(l => l.trim()).filter(l => l.length > 0);
        const title = lines[0] || 'Client Success';
        const quoteMatch = block.match(/"([^"]+)"/);
        const quote = quoteMatch ? quoteMatch[1] : lines[1] || '';
        const meta = lines.find(l => l.includes('|') || l.includes('Service:')) || '';
        
        return { title, quote, meta };
    }).slice(0, 5); // Limit to top 5 for homepage performance

    // Inject Slides
    track.innerHTML = testimonials.map(t => `
        <div class="testimonial-slide">
            <div class="testimonial-card-inner">
                <p class="testimonial-text">${t.quote}</p>
                <div class="testimonial-author">${t.title}</div>
                <div class="testimonial-meta">${t.meta}</div>
            </div>
        </div>
    `).join('');

    // Inject Dots
    dotContainer.innerHTML = testimonials.map((_, i) => `
        <div class="dot ${i === 0 ? 'active' : ''}" data-index="${i}"></div>
    `).join('');

    const slides = document.querySelectorAll('.testimonial-slide');
    const dots = document.querySelectorAll('.dot');
    let currentIndex = 0;
    let autoPlayTimer;

    function goToSlide(index) {
        currentIndex = index;
        track.style.transform = `translateX(-${index * 100}%)`;
        dots.forEach(d => d.classList.remove('active'));
        dots[index].classList.add('active');
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % testimonials.length;
        goToSlide(currentIndex);
    }

    function startAutoPlay() {
        stopAutoPlay();
        autoPlayTimer = setInterval(nextSlide, 5000);
    }

    function stopAutoPlay() {
        if (autoPlayTimer) clearInterval(autoPlayTimer);
    }

    dots.forEach(dot => {
        dot.addEventListener('click', () => {
            const index = parseInt(dot.getAttribute('data-index'));
            goToSlide(index);
            startAutoPlay();
        });
    });

    // Start
    startAutoPlay();

    // Pause on hover
    track.addEventListener('mouseenter', stopAutoPlay);
    track.addEventListener('mouseleave', startAutoPlay);
}


// ==========================================================================
// A11Y (ACCESSIBILITY) WIDGET INJECTION & LOGIC
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
    // Inject HTML
    const a11yHTML = `
    <button class="a11y-widget-btn" id="a11y-widget-btn" aria-label="Open Accessibility Menu" aria-haspopup="true" aria-expanded="false">
        <svg viewBox="0 0 24 24">
            <path d="M12 2c1.1 0 2 .9 2 2s-.9 2-2 2-2-.9-2-2 .9-2 2-2zm9 7h-6v13h-2v-6h-2v6H9V9H3V7h18v2z"/>
        </svg>
    </button>
    
    <div class="a11y-panel" id="a11y-panel" role="dialog" aria-modal="true" aria-labelledby="a11y-title">
        <div class="a11y-panel-header">
            <h3 id="a11y-title">Accessibility Tools</h3>
            <button class="a11y-close" id="a11y-close" aria-label="Close Accessibility Menu">&times;</button>
        </div>
        <div class="a11y-controls">
            
            <div class="a11y-setting-row">
                <span class="a11y-setting-label">Text Size</span>
                <div class="a11y-btn-group">
                    <button class="a11y-toggle-btn" id="btn-text-decrease" aria-label="Decrease text size">A-</button>
                    <button class="a11y-toggle-btn" id="btn-text-reset" aria-label="Default text size">A</button>
                    <button class="a11y-toggle-btn" id="btn-text-increase" aria-label="Increase text size">A+</button>
                </div>
            </div>
            
            <div class="a11y-setting-row">
                <span class="a11y-setting-label">High Contrast</span>
                <button class="a11y-toggle-btn" id="tgl-contrast" aria-pressed="false">Toggle</button>
            </div>
            
            <div class="a11y-setting-row">
                <span class="a11y-setting-label">Highlight Links</span>
                <button class="a11y-toggle-btn" id="tgl-links" aria-pressed="false">Toggle</button>
            </div>
            
            <div class="a11y-setting-row">
                <span class="a11y-setting-label">Readable Font</span>
                <button class="a11y-toggle-btn" id="tgl-font" aria-pressed="false">Toggle</button>
            </div>
            
            <div class="a11y-setting-row">
                <span class="a11y-setting-label">Pause Animations</span>
                <button class="a11y-toggle-btn" id="tgl-motion" aria-pressed="false">Toggle</button>
            </div>

            <div class="a11y-setting-row" style="justify-content: center; margin-top: 10px;">
                <button class="a11y-toggle-btn" id="btn-a11y-reset" style="width: 100%;">Reset All Settings</button>
            </div>
        </div>
    </div>
    `;
    
    document.body.insertAdjacentHTML('beforeend', a11yHTML);

    // DOM Elements
    const widgetBtn = document.getElementById('a11y-widget-btn');
    const panel = document.getElementById('a11y-panel');
    const closeBtn = document.getElementById('a11y-close');
    
    const tglContrast = document.getElementById('tgl-contrast');
    const tglLinks = document.getElementById('tgl-links');
    const tglFont = document.getElementById('tgl-font');
    const tglMotion = document.getElementById('tgl-motion');
    const btnIncrease = document.getElementById('btn-text-increase');
    const btnDecrease = document.getElementById('btn-text-decrease');
    const btnReset = document.getElementById('btn-text-reset');
    const btnResetAll = document.getElementById('btn-a11y-reset');

    // State Default
    let a11yState = {
        contrast: false,
        links: false,
        font: false,
        motion: false,
        textSize: 0 // 0: normal, 1: large, 2: xlarge
    };

    // Load from LocalStorage
    const savedState = localStorage.getItem('gls_a11y_state');
    if (savedState) {
        try {
            a11yState = JSON.parse(savedState);
            applyState();
        } catch(e) {}
    }

    function saveState() {
        localStorage.setItem('gls_a11y_state', JSON.stringify(a11yState));
    }

    // Toggle Panel
    const togglePanel = () => {
        const isOpen = panel.classList.contains('open');
        if (isOpen) {
            panel.classList.remove('open');
            widgetBtn.setAttribute('aria-expanded', 'false');
        } else {
            panel.classList.add('open');
            widgetBtn.setAttribute('aria-expanded', 'true');
        }
    };

    widgetBtn.addEventListener('click', togglePanel);
    closeBtn.addEventListener('click', togglePanel);

    // Applying Classes and updating buttons
    function applyState() {
        const bd = document.body;
        const hl = document.documentElement;

        // Contrast
        if(a11yState.contrast) { bd.classList.add('a11y-high-contrast'); tglContrast.classList.add('active'); tglContrast.setAttribute('aria-pressed', 'true'); }
        else { bd.classList.remove('a11y-high-contrast'); tglContrast.classList.remove('active'); tglContrast.setAttribute('aria-pressed', 'false'); }

        // Links
        if(a11yState.links) { bd.classList.add('a11y-highlight-links'); tglLinks.classList.add('active'); tglLinks.setAttribute('aria-pressed', 'true'); }
        else { bd.classList.remove('a11y-highlight-links'); tglLinks.classList.remove('active'); tglLinks.setAttribute('aria-pressed', 'false'); }

        // Font
        if(a11yState.font) { bd.classList.add('a11y-readable-font'); tglFont.classList.add('active'); tglFont.setAttribute('aria-pressed', 'true'); }
        else { bd.classList.remove('a11y-readable-font'); tglFont.classList.remove('active'); tglFont.setAttribute('aria-pressed', 'false'); }

        // Motion
        if(a11yState.motion) { bd.classList.add('a11y-reduced-motion'); tglMotion.classList.add('active'); tglMotion.setAttribute('aria-pressed', 'true'); }
        else { bd.classList.remove('a11y-reduced-motion'); tglMotion.classList.remove('active'); tglMotion.setAttribute('aria-pressed', 'false'); }

        // Text Size
        hl.classList.remove('a11y-text-large', 'a11y-text-xlarge');
        btnIncrease.classList.remove('active');
        btnDecrease.classList.remove('active');
        btnReset.classList.remove('active');
        
        if (a11yState.textSize === 1) { hl.classList.add('a11y-text-large'); btnIncrease.classList.add('active'); }
        else if (a11yState.textSize === 2) { hl.classList.add('a11y-text-xlarge'); btnIncrease.classList.add('active'); } // Reuse active or style specifically
        else if (a11yState.textSize === -1) { /* Assuming decrease reduces size if we implement it, but for standard a11y we just reset */ }
        else { btnReset.classList.add('active'); }
    }

    // Listeners
    tglContrast.addEventListener('click', () => { a11yState.contrast = !a11yState.contrast; applyState(); saveState(); });
    tglLinks.addEventListener('click', () => { a11yState.links = !a11yState.links; applyState(); saveState(); });
    tglFont.addEventListener('click', () => { a11yState.font = !a11yState.font; applyState(); saveState(); });
    tglMotion.addEventListener('click', () => { a11yState.motion = !a11yState.motion; applyState(); saveState(); });

    btnIncrease.addEventListener('click', () => {
        if(a11yState.textSize < 2) a11yState.textSize++;
        applyState(); saveState();
    });
    btnDecrease.addEventListener('click', () => {
        if(a11yState.textSize > 0) a11yState.textSize--;
        applyState(); saveState();
    });
    btnReset.addEventListener('click', () => {
        a11yState.textSize = 0;
        applyState(); saveState();
    });
    btnResetAll.addEventListener('click', () => {
        a11yState = { contrast: false, links: false, font: false, motion: false, textSize: 0 };
        applyState(); saveState();
    });

});
