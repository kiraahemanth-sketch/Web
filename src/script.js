document.addEventListener('DOMContentLoaded', () => {
    // Sakura Petals Effect
    const sakuraContainer = document.getElementById('sakura-container');
    const petalCount = 30;

    for (let i = 0; i < petalCount; i++) {
        createPetal();
    }

    function createPetal() {
        const petal = document.createElement('div');
        petal.classList.add('sakura');

        const size = Math.random() * 10 + 5 + 'px';
        petal.style.width = size;
        petal.style.height = size;

        petal.style.left = Math.random() * 100 + 'vw';
        petal.style.opacity = Math.random() * 0.6 + 0.4;

        sakuraContainer.appendChild(petal);

        const duration = Math.random() * 5000 + 5000;
        const delay = Math.random() * 5000;

        animatePetal(petal, duration, delay);
    }

    function animatePetal(petal, duration, delay) {
        anime({
            targets: petal,
            translateY: [
                { value: -10, duration: 0 },
                { value: '105vh', duration: duration }
            ],
            translateX: [
                { value: 0, duration: 0 },
                { value: () => anime.random(-150, 150), duration: duration }
            ],
            rotate: {
                value: () => anime.random(0, 360),
                duration: duration
            },
            easing: 'linear',
            delay: delay,
            complete: () => {
                petal.style.left = Math.random() * 100 + 'vw';
                animatePetal(petal, duration, 0);
            }
        });
    }

    // Initial Hero Animations
    anime({
        targets: '.hero-content',
        opacity: [0, 1],
        translateY: [50, 0],
        duration: 1500,
        easing: 'easeOutExpo'
    });

    anime({
        targets: '.hero-image',
        opacity: [0, 1],
        scale: [0.8, 1],
        duration: 2000,
        easing: 'easeOutExpo',
        delay: 500
    });

    // Intersection Observer for Scroll Animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const revealCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = entry.target;
                let animationProps = {
                    targets: target,
                    opacity: [0, 1],
                    translateY: [30, 0],
                    duration: 1000,
                    easing: 'easeOutExpo'
                };

                if (target.classList.contains('news-item')) {
                    animationProps.translateX = [-30, 0];
                }

                anime(animationProps);
                observer.unobserve(target);
            }
        });
    };

    const observer = new IntersectionObserver(revealCallback, observerOptions);

    document.querySelectorAll('.char-card, .news-item, .section-title').forEach(el => {
        el.style.opacity = '0';
        observer.observe(el);
    });

    // Navbar scroll effect
    window.addEventListener('scroll', () => {
        const header = document.querySelector('header');
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
});
