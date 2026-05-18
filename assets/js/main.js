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

    // 1. Clonamos el grupo original de logos
    const originalItems = Array.from(track.children);
    originalItems.forEach(item => {
        const clone = item.cloneNode(true);
        track.appendChild(clone);
    });

    // 2. Calculamos la distancia exacta hasta el primer clon (píxel perfecto)
    function calculateDistance() {
        const firstClone = track.children[originalItems.length];
        if (firstClone) {
            // offsetLeft nos da la posición exacta donde inicia el segundo bloque de logos
            const distance = firstClone.offsetLeft;
            track.style.setProperty('--scroll-distance', `-${distance}px`);
        }
    }

    // 3. Nos aseguramos de medir cuando las imágenes ya tengan su tamaño real en pantalla
    if (document.readyState === "complete") {
        calculateDistance();
    } else {
        window.addEventListener("load", calculateDistance);
    }

    // Recalcular si el usuario rota la pantalla o cambia el tamaño de la ventana
    window.addEventListener("resize", calculateDistance);
});