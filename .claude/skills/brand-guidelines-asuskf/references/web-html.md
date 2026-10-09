# ASUSKF — Implementación web / HTML

Todo entregable HTML debe funcionar **offline** y abrir en cualquier navegador: fuentes,
logo e iconos embebidos como base64, tokens copiados inline. Rutas relativas al directorio
de la skill.

## 1. Esqueleto mínimo

```html
<!doctype html>
<html lang="es" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>ASUSKF</title>
  <link rel="icon" href="data:image/png;base64,{{asuskf-symbol-64.png}}">
  <style>
    /* 1) @font-face embebidas (sección 2) */
    /* 2) contenido completo de assets/tokens/colors_and_type.css */
    /* 3) componentes (sección 4) */
  </style>
</head>
<body>…</body>
</html>
```

`assets/templates/build_templates.py` ya hace todo esto: reutiliza sus funciones
`b64()`, `font_faces()` y `tokens()` en lugar de reescribirlas.

## 2. Fuentes embebidas (nunca Google Fonts CDN)

```python
import base64, pathlib
def b64(p): return base64.b64encode(pathlib.Path(p).read_bytes()).decode()
css = f"""
@font-face {{ font-family:'Plus Jakarta Sans'; font-weight:200 800; font-display:swap;
  src:url(data:font/woff2;base64,{b64('assets/fonts/plus-jakarta-sans.woff2')}) format('woff2'); }}
@font-face {{ font-family:'Fira Code'; font-weight:300 700; font-display:swap;
  src:url(data:font/woff2;base64,{b64('assets/fonts/fira-code.woff2')}) format('woff2'); }}
"""
```

El woff2 es subset *latin* (incluye á é í ó ú ñ ¿ ¡). Para griego/cirílico usa el TTF completo
(`font/ttf`, `format('truetype')`).

## 3. Logo

```html
<!-- Lockup nav -->
<a class="ax-brand" href="#" aria-label="ASUSKF — inicio">
  <img src="data:image/png;base64,{{asuskf-symbol-192.png}}" alt="" width="40" height="40">
  <span class="ax-wordmark">ASUSKF<span class="ax-cursor">_</span></span>
</a>

<!-- Hero: símbolo dentro del hexágono espectro (punta arriba) -->
<div class="ax-hex-hero"><img src="data:image/png;base64,{{asuskf-symbol-512.png}}" alt="Símbolo ASUSKF"></div>
```

Nunca generes el símbolo con SVG/canvas. El `clip-path` solo recorta la **foto/PNG oficial**.

## 4. Componentes (CSS con tokens)

```css
body { margin:0; background:var(--ax-color-bg); color:var(--ax-color-text);
  font-family:var(--ax-font-sans); line-height:var(--ax-leading-body); }
::selection { background: rgb(168 85 247 / 0.3); }
.mono { font-family:var(--ax-font-mono); }

/* Wordmark */
.ax-brand { display:flex; align-items:center; gap:var(--ax-space-3); text-decoration:none; color:inherit; }
.ax-brand img { border-radius:var(--ax-radius-md); box-shadow:var(--ax-shadow-glow-indigo); }
.ax-wordmark { font-family:var(--ax-font-mono); font-weight:var(--ax-weight-bold);
  font-size:var(--ax-text-xl); letter-spacing:var(--ax-tracking-tighter); }
.ax-cursor { color:var(--ax-color-signal); }

/* Nav flotante (único lugar con blur fuerte) */
.ax-nav { position:fixed; inset:0 0 auto; z-index:50; display:flex; justify-content:space-between;
  align-items:center; padding:var(--ax-space-6) var(--ax-space-8);
  background:var(--ax-color-nav-glass); backdrop-filter:blur(var(--ax-blur-glass));
  border-bottom:1px solid var(--ax-color-border); }
.ax-nav a { font-family:var(--ax-font-mono); font-size:var(--ax-text-sm); font-weight:var(--ax-weight-semibold);
  text-transform:uppercase; letter-spacing:var(--ax-tracking-widest); color:var(--ax-color-text-secondary);
  text-decoration:none; transition:color var(--ax-dur) var(--ax-ease); }
.ax-nav a:hover, .ax-nav a.ax-brand { color:var(--ax-color-text); }

/* Hexágono hero — punta arriba */
.ax-hex-hero { width:15rem; aspect-ratio:0.866; background:var(--ax-gradient-hex);
  clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%); }
.ax-hex-hero img { width:100%; height:100%; object-fit:cover; opacity:.8; }

/* Titular con degradado (uno por vista) */
.ax-hero-title { font-size:var(--ax-text-hero); font-weight:var(--ax-weight-extrabold);
  letter-spacing:var(--ax-tracking-tight); line-height:var(--ax-leading-tight); text-align:center; }
.ax-gradient-text { background:var(--ax-gradient-hero); -webkit-background-clip:text;
  background-clip:text; color:transparent; }

/* Título de sección: <h2 class="ax-section-title"><span class="num">01.</span> <span>Nombre<span class="ax-cursor">_</span></span></h2>
   (el "_" va DENTRO del span del nombre, si no el gap del flex lo separa) */
.ax-section-title { font-family:var(--ax-font-mono); font-size:var(--ax-text-4xl);
  font-weight:var(--ax-weight-bold); display:flex; align-items:center; gap:var(--ax-space-4); }
.ax-section-title .num { color:var(--ax-color-signal); font-size:var(--ax-text-2xl); }

/* Tarjeta */
.ax-card { background:var(--ax-color-surface-glass); border:1px solid var(--ax-color-border);
  border-radius:var(--ax-radius-2xl); padding:var(--ax-space-10);
  transition:transform var(--ax-dur) var(--ax-ease), border-color var(--ax-dur) var(--ax-ease); }
.ax-card:hover { border-color:var(--ax-color-accent); transform:translateY(var(--ax-hover-lift)); }

/* Botones */
.ax-btn { display:inline-flex; align-items:center; justify-content:center; gap:var(--ax-space-3);
  min-height:var(--ax-touch-min); padding:var(--ax-space-4) var(--ax-space-8);
  border-radius:var(--ax-radius-lg); font-weight:var(--ax-weight-bold); text-decoration:none;
  transition:all var(--ax-dur) var(--ax-ease); }
.ax-btn--primary { background:var(--ax-color-action-hero); color:var(--ax-color-text-on-accent);
  box-shadow:var(--ax-shadow-glow-indigo); }
.ax-btn--primary:hover { background:var(--ax-color-action-hero-hover); }
.ax-btn--ghost { background:var(--ax-color-surface-glass); color:var(--ax-color-text);
  border:1px solid rgb(16 185 129 / 0.5); box-shadow:var(--ax-shadow-glow-emerald); }
.ax-btn--ghost:hover { border-color:var(--ax-color-signal); }
.ax-btn:focus-visible, .ax-input:focus-visible { outline:2px solid var(--ax-color-focus); outline-offset:2px; }

/* Chips */
.ax-chip { font-family:var(--ax-font-mono); font-size:var(--ax-text-xs);
  padding:var(--ax-space-1) var(--ax-space-3); border-radius:var(--ax-radius-pill); border:1px solid; }
.ax-chip--violet  { color:var(--ax-violet-400);  background:rgb(168 85 247 / .1); border-color:rgb(168 85 247 / .2); }
.ax-chip--blue    { color:var(--ax-blue-400);    background:rgb(59 130 246 / .1); border-color:rgb(59 130 246 / .2); }
.ax-chip--emerald { color:var(--ax-emerald-400); background:rgb(16 185 129 / .1); border-color:rgb(16 185 129 / .2); }

/* Badge de estado (paper) */
.ax-badge { font-size:var(--ax-text-2xs); font-weight:var(--ax-weight-bold); text-transform:uppercase;
  letter-spacing:var(--ax-tracking-widest); padding:var(--ax-space-1) var(--ax-space-2); border-radius:var(--ax-radius-sm); }

/* Input */
.ax-input { width:100%; box-sizing:border-box; background:var(--ax-color-surface-2); color:var(--ax-color-text);
  padding:var(--ax-space-3); border-radius:var(--ax-radius-md); border:1px solid var(--ax-color-border-input); }
.ax-input:focus { border-color:var(--ax-color-focus); }

/* Punto "disponible" */
.ax-live { width:.5rem; height:.5rem; border-radius:50%; background:var(--ax-color-signal);
  animation:ax-pulse 2s var(--ax-ease) infinite; }
@keyframes ax-pulse { 50% { opacity:.5; } }
@media (prefers-reduced-motion: reduce) { .ax-live { animation:none; } }
```

> Los `rgb(… / .1)` de chips son tintes alfa de un token existente; si los necesitas en otro
> sitio, añádelos como token en `colors_and_type.css` en lugar de repetirlos.

## 5. Reemplazos sin CDN

| Sitio en vivo usa | En entregables usa |
|---|---|
| Tailwind CDN | CSS de tokens + clases `ax-*` de arriba |
| AOS (scroll reveal) | `IntersectionObserver` + clase `.is-in` (abajo) |
| Typed.js | 20 líneas de JS (abajo) |
| Google Fonts | `@font-face` base64 |

```js
// Revelado al scroll — respeta reduced motion
const rm = matchMedia('(prefers-reduced-motion: reduce)').matches;
document.querySelectorAll('[data-reveal]').forEach(el => {
  if (rm) return el.classList.add('is-in');
  new IntersectionObserver(([e], o) => { if (e.isIntersecting) { el.classList.add('is-in'); o.disconnect(); } },
    { rootMargin: '0px 0px -100px' }).observe(el);
});
// CSS: [data-reveal]{opacity:0;transform:translateY(24px);transition:all var(--ax-dur-reveal) var(--ax-ease)}
//      [data-reveal].is-in{opacity:1;transform:none}

// Texto tipeado con cursor "_"
function typed(el, words, t = 60, b = 30) {
  if (rm) { el.textContent = words[0]; return; }
  let w = 0, i = 0, del = false;
  (function tick() {
    const s = words[w];
    i += del ? -1 : 1;
    el.textContent = s.slice(0, i);
    if (!del && i === s.length) { del = true; return setTimeout(tick, 1500); }
    if (del && i === 0) { del = false; w = (w + 1) % words.length; }
    setTimeout(tick, del ? b : t);
  })();
}
```

Pon el cursor como `<span class="ax-cursor" aria-hidden="true">_</span>` tras el elemento y
deja el texto completo en `aria-label` del contenedor para lectores de pantalla.

## 6. Tailwind (solo si el proyecto ya lo usa)

```js
// tailwind.config.js
theme: { extend: {
  fontFamily: { sans: ['Plus Jakarta Sans', 'sans-serif'], mono: ['Fira Code', 'monospace'] },
  colors: { void: '#020617', ice: '#9BB8D3', logo: { indigo: '#1D154C', navy: '#1B376D', ocean: '#0E4E79' } },
}}
```
Las paletas `slate`, `violet`, `purple`, `indigo`, `blue`, `emerald` de Tailwind coinciden con
los tokens. Sigue aplicando: un degradado por vista, Fog no para texto pequeño.
