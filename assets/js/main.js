// asuskf.github.io — interacción sin dependencias (reemplaza AOS + Typed.js)
(() => {
    const root = document.documentElement;
    root.classList.add('js');
    const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
    const lang = root.lang.startsWith('es') ? 'es' : 'en';

    // --- Revelado al scroll (una sola vez) --------------------------------
    const revealables = document.querySelectorAll('[data-reveal]');
    if (reducedMotion || !('IntersectionObserver' in window)) {
        revealables.forEach(el => el.classList.add('is-in'));
    } else {
        const io = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (!entry.isIntersecting) return;
                entry.target.classList.add('is-in');
                io.unobserve(entry.target);
            });
        }, { rootMargin: '0px 0px -80px' });
        revealables.forEach(el => io.observe(el));
    }

    // --- Texto tipeado del hero -------------------------------------------
    const typedEl = document.getElementById('typed-hero');
    if (typedEl) {
        const words = JSON.parse(typedEl.dataset.words || '[]');
        if (reducedMotion || !words.length) {
            typedEl.textContent = words[0] || '';
        } else {
            let w = 0, i = 0, deleting = false;
            const tick = () => {
                const word = words[w];
                i += deleting ? -1 : 1;
                typedEl.textContent = word.slice(0, i);
                if (!deleting && i === word.length) { deleting = true; return setTimeout(tick, 1600); }
                if (deleting && i === 0) { deleting = false; w = (w + 1) % words.length; }
                setTimeout(tick, deleting ? 30 : 60);
            };
            tick();
        }
    }

    // --- Menú móvil -------------------------------------------------------
    const menuBtn = document.querySelector('.nav__menu-btn');
    const menu = document.getElementById('nav-menu');
    if (menuBtn && menu) {
        const setOpen = open => {
            menuBtn.setAttribute('aria-expanded', String(open));
            menu.dataset.open = String(open);
        };
        const mq = matchMedia('(max-width: 48rem)');
        const sync = () => setOpen(false);
        sync();
        mq.addEventListener('change', sync);
        menuBtn.addEventListener('click', () => setOpen(menuBtn.getAttribute('aria-expanded') !== 'true'));
        menu.addEventListener('click', e => { if (e.target.closest('a') && mq.matches) setOpen(false); });
        document.addEventListener('keydown', e => {
            if (e.key === 'Escape' && menuBtn.getAttribute('aria-expanded') === 'true') { setOpen(false); menuBtn.focus(); }
        });
    }

    // --- Formulario de contacto (abre el cliente de correo) ----------------
    const form = document.getElementById('contact-form');
    if (form) {
        const copy = {
            en: { subject: 'New Inquiry', name: 'Name', service: 'Service', message: 'Message' },
            es: { subject: 'Nueva Consulta', name: 'Nombre', service: 'Servicio', message: 'Mensaje' },
        }[lang];
        form.addEventListener('submit', e => {
            e.preventDefault();
            let firstInvalid = null;
            form.querySelectorAll('[required]').forEach(field => {
                const invalid = !field.value.trim();
                field.setAttribute('aria-invalid', String(invalid));
                if (invalid && !firstInvalid) firstInvalid = field;
            });
            if (firstInvalid) { firstInvalid.focus(); return; }
            const data = new FormData(form);
            const subject = encodeURIComponent(`${copy.subject}: ${data.get('service')}`);
            const body = encodeURIComponent(
                `${copy.name}: ${data.get('name')}\n${copy.service}: ${data.get('service')}\n\n${copy.message}:\n${data.get('message')}`
            );
            window.location.href = `mailto:kfarinango@protonmail.com?subject=${subject}&body=${body}`;
        });
        form.addEventListener('input', e => {
            if (e.target.getAttribute('aria-invalid') === 'true' && e.target.value.trim()) e.target.setAttribute('aria-invalid', 'false');
        });
    }

    // --- Carrusel infinito de clientes ------------------------------------
    const track = document.getElementById('carousel-track');
    if (track && !reducedMotion) {
        const originals = Array.from(track.children);
        originals.forEach(item => {
            const clone = item.cloneNode(true);
            clone.setAttribute('aria-hidden', 'true');
            clone.querySelectorAll('img').forEach(img => { img.alt = ''; });
            track.appendChild(clone);
        });
        const measure = () => {
            const firstClone = track.children[originals.length];
            if (firstClone) track.style.setProperty('--scroll-distance', `-${firstClone.offsetLeft}px`);
        };
        if (document.readyState === 'complete') measure(); else window.addEventListener('load', measure);
        window.addEventListener('resize', measure);
        track.dataset.animated = '';
    }
})();
