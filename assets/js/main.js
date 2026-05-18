// Inicializar Animaciones de Scroll (AOS)
AOS.init({
    duration: 1000,
    once: true,
    offset: 100
});

// Inicializar Efecto de Escritura en el Hero
document.addEventListener('DOMContentLoaded', function() {
    new Typed('#typed-hero', {
        strings: [
            'MLOps Specialist', 
            'Graph Neural Networks Researcher', 
            'Financial Intelligence Systems'
        ],
        typeSpeed: 60,
        backSpeed: 30,
        loop: true,
        cursorChar: '_'
    });
});

document.addEventListener('DOMContentLoaded', () => {
    // --- Manejador para INGLÉS ---
    const formEn = document.getElementById('contactFormEn');
    if (formEn) {
        formEn.addEventListener('submit', (e) => {
            e.preventDefault(); // Evita que la página se recargue
            const name = document.getElementById('nameEn').value;
            const service = document.getElementById('serviceEn').value;
            const message = document.getElementById('messageEn').value;

            // Configuramos el Asunto y el Cuerpo limpio
            const subject = encodeURIComponent(`New Inquiry: ${service}`);
            const body = encodeURIComponent(`Name: ${name}\nService: ${service}\n\nMessage:\n${message}`);

            window.location.href = `mailto:kfarinango@protonmail.com?subject=${subject}&body=${body}`;
        });
    }

    // --- Manejador para ESPAÑOL ---
    const formEs = document.getElementById('contactFormEs');
    if (formEs) {
        formEs.addEventListener('submit', (e) => {
            e.preventDefault();

            const name = document.getElementById('nameEs').value;
            const service = document.getElementById('serviceEs').value;
            const message = document.getElementById('messageEs').value;

            const subject = encodeURIComponent(`Nueva Consulta: ${service}`);
            const body = encodeURIComponent(`Nombre: ${name}\nServicio: ${service}\n\nMensaje:\n${message}`);

            window.location.href = `mailto:kfarinango@protonmail.com?subject=${subject}&body=${body}`;
        });
    }
});

document.addEventListener("DOMContentLoaded", () => {
    const track = document.getElementById("carousel-track");
    if (!track) return;

    // 1. Clonar los logos dinámicamente para crear el bucle infinito perfecto
    const originalItems = Array.from(track.children);
    originalItems.forEach(item => {
        const clone = item.cloneNode(true);
        track.appendChild(clone);
    });

    // 2. Configuración de la animación
    let speed = 1; // Velocidad en píxeles por cuadro (puedes usar decimales como 0.5 para ir más lento)
    let scrollAmount = 0;
    let isPaused = false;

    function animateCarousel() {
        if (!isPaused) {
            scrollAmount += speed;

            // Al llegar exactamente a la mitad del ancho total (el grupo original), reiniciamos a 0
            const halfWidth = track.scrollWidth / 2;
            if (scrollAmount >= halfWidth) {
                scrollAmount = 0;
            }

            track.style.transform = `translateX(-${scrollAmount}px)`;
        }
        // Solicita el siguiente cuadro de animación nativo del navegador (60fps+)
        requestAnimationFrame(animateCarousel);
    }

    // 3. Controladores de eventos para pausar al pasar el mouse
    track.addEventListener("mouseenter", () => isPaused = true);
    track.addEventListener("mouseleave", () => isPaused = false);

    // 4. Iniciar la animación asegurando que las imágenes ya cargaron su tamaño real
    if (document.readyState === "complete") {
        animateCarousel();
    } else {
        window.addEventListener("load", animateCarousel);
    }
});