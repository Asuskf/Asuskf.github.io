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