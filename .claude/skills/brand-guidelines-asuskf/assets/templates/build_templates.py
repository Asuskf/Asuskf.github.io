"""Genera los HTML Tier 2 de la marca ASUSKF (autocontenidos, offline).

    python assets/templates/build_templates.py

Salidas (no editar a mano):
    assets/templates/ASUSKF_Brand_Cheatsheet.html
    assets/templates/ASUSKF_Landing_Starter.html

Fuentes de verdad que lee: assets/tokens/colors_and_type.css (tokens),
references/web-html.md (CSS de componentes, sección 4), assets/fonts, assets/logos,
assets/icons, assets/hexagons.
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
A = ROOT / "assets"
OUT = A / "templates"


def b64(p):
    return base64.b64encode((A / p).read_bytes()).decode()


def font_faces():
    return (
        "@font-face{font-family:'Plus Jakarta Sans';font-weight:200 800;font-display:swap;"
        f"src:url(data:font/woff2;base64,{b64('fonts/plus-jakarta-sans.woff2')}) format('woff2')}}\n"
        "@font-face{font-family:'Fira Code';font-weight:300 700;font-display:swap;"
        f"src:url(data:font/woff2;base64,{b64('fonts/fira-code.woff2')}) format('woff2')}}\n"
    )


def tokens():
    return (A / "tokens/colors_and_type.css").read_text(encoding="utf-8")


def components():
    md = (ROOT / "references/web-html.md").read_text(encoding="utf-8")
    sec = md.split("## 4.", 1)[1]
    return re.search(r"```css\n(.*?)```", sec, re.S).group(1)


def img(p, mime="image/png"):
    return f"data:{mime};base64,{b64(p)}"


def svg(p):
    return (A / p).read_text(encoding="utf-8").strip()


EXTRA = """
*{box-sizing:border-box}
a{color:var(--ax-color-link)}
.wrap{max-width:var(--ax-container);margin:0 auto;padding:0 var(--ax-space-6)}
.wrap-text{max-width:var(--ax-container-text);margin:0 auto;padding:0 var(--ax-space-6)}
section{padding:var(--ax-space-20) 0}
.alt{background:var(--ax-color-surface);border-block:1px solid var(--ax-color-border)}
.muted{color:var(--ax-color-text-secondary)}
.eyebrow{font-family:var(--ax-font-mono);font-size:var(--ax-text-sm);text-transform:uppercase;
  letter-spacing:var(--ax-tracking-widest);color:var(--ax-color-text-secondary)}
.grid{display:grid;gap:var(--ax-space-8)}
@media(min-width:768px){.g2{grid-template-columns:repeat(2,1fr)}.g3{grid-template-columns:repeat(3,1fr)}.g4{grid-template-columns:repeat(4,1fr)}}
.row{display:flex;flex-wrap:wrap;gap:var(--ax-space-3);align-items:center}
.icon{width:1.25rem;height:1.25rem;display:inline-flex}
.icon svg{width:100%;height:100%}
.theme-toggle{font-family:var(--ax-font-mono);font-size:var(--ax-text-xs);font-weight:var(--ax-weight-bold);
  min-height:var(--ax-touch-min);padding:0 var(--ax-space-4);border-radius:var(--ax-radius-pill);cursor:pointer;
  background:var(--ax-color-surface-2);color:var(--ax-color-signal);border:1px solid var(--ax-color-border-strong)}
[data-reveal]{opacity:0;transform:translateY(24px);transition:opacity var(--ax-dur-reveal) var(--ax-ease),transform var(--ax-dur-reveal) var(--ax-ease)}
[data-reveal].is-in{opacity:1;transform:none}
@media(max-width:767px){.ax-nav{padding:var(--ax-space-4)}.ax-nav .links{display:none}}
"""

JS = """
const rm = matchMedia('(prefers-reduced-motion: reduce)').matches;
document.querySelectorAll('[data-reveal]').forEach(el => {
  if (rm || !('IntersectionObserver' in window)) return el.classList.add('is-in');
  new IntersectionObserver(([e], o) => { if (e.isIntersecting) { el.classList.add('is-in'); o.disconnect(); } },
    { rootMargin: '0px 0px -60px' }).observe(el);
});
document.querySelectorAll('.theme-toggle').forEach(b => b.addEventListener('click', () => {
  const h = document.documentElement, t = h.dataset.theme === 'light' ? 'dark' : 'light';
  h.dataset.theme = t; b.textContent = t === 'light' ? 'DARK' : 'LIGHT';
  try { localStorage.setItem('ax-theme', t); } catch (e) {}
}));
try { const t = localStorage.getItem('ax-theme'); if (t) { document.documentElement.dataset.theme = t;
  document.querySelectorAll('.theme-toggle').forEach(b => b.textContent = t === 'light' ? 'DARK' : 'LIGHT'); } } catch (e) {}
function typed(el, words, t = 60, b = 30) {
  if (!el) return;
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
typed(document.getElementById('typed'), ['MLOps Specialist', 'Graph Neural Networks Researcher', 'Financial Intelligence Systems']);
"""


def page(title, desc, body):
    return f"""<!doctype html>
<html lang="es" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{desc}">
<title>{title}</title>
<link rel="icon" href="{img('logos/asuskf-symbol-64.png')}">
<style>
{font_faces()}
{tokens()}
{components()}
{EXTRA}
</style>
</head>
<body>
{body}
<script>{JS}</script>
</body>
</html>
"""


def nav(links):
    items = "".join(f'<a href="{h}">{t}</a>' for t, h in links)
    return f"""<nav class="ax-nav" aria-label="Principal">
  <a class="ax-brand" href="#top" aria-label="ASUSKF — inicio">
    <img src="{img('logos/asuskf-symbol-192.png')}" alt="" width="40" height="40">
    <span class="ax-wordmark">ASUSKF<span class="ax-cursor">_</span></span>
  </a>
  <div class="row"><div class="row links" style="gap:var(--ax-space-8)">{items}</div>
  <button class="theme-toggle" type="button" aria-label="Cambiar tema">LIGHT</button></div>
</nav>"""


def section_title(num, name):
    n = f'<span class="num">{num}</span> ' if num else ""
    return f'<h2 class="ax-section-title" data-reveal>{n}<span>{name}<span class="ax-cursor">_</span></span></h2>'


# ---------------------------------------------------------------- Cheatsheet
SWATCHES = [
    ("Base", [("Void", "--ax-slate-950", "#020617"), ("Deep Slate", "--ax-slate-900", "#0F172A"),
              ("Graphite", "--ax-slate-800", "#1E293B"), ("Wire", "--ax-slate-700", "#334155"),
              ("Fog", "--ax-slate-500", "#64748B"), ("Mist", "--ax-slate-400", "#94A3B8"),
              ("Frost", "--ax-slate-200", "#E2E8F0"), ("Snow", "--ax-slate-100", "#F1F5F9")]),
    ("Espectro", [("Mind Violet", "--ax-violet-500", "#8B5CF6"), ("Violet 400", "--ax-violet-400", "#A78BFA"),
                  ("Violet 600", "--ax-violet-600", "#7C3AED"), ("Hero Indigo", "--ax-indigo-600", "#4F46E5"),
                  ("Signal Blue", "--ax-blue-500", "#3B82F6"), ("Blue 400", "--ax-blue-400", "#60A5FA"),
                  ("Growth Emerald", "--ax-emerald-400", "#34D399"), ("Negative", "--ax-red-400", "#F87171")]),
    ("Logo y sub-marcas", [("Logo Indigo", "--ax-logo-indigo", "#1D154C"), ("Logo Navy", "--ax-logo-navy", "#1B376D"),
                           ("Logo Ocean", "--ax-logo-ocean", "#0E4E79"), ("Logo Ice", "--ax-logo-ice", "#9BB8D3"),
                           ("Invest Forest", "--ax-invest-forest", "#053C25"), ("Invest Gold", "--ax-invest-gold", "#C9B97A"),
                           ("Health Navy", "--ax-health-navy", "#133250"), ("Health Sky", "--ax-health-sky", "#699DB3")]),
]


def swatch_grid():
    out = []
    for group, items in SWATCHES:
        cells = "".join(
            f'<div class="sw"><div class="chip-c" style="background:var({tok})"></div>'
            f'<strong>{name}</strong><code>{hexv}</code><code class="muted">{tok}</code></div>'
            for name, tok, hexv in items)
        out.append(f'<h3 class="eyebrow">{group}</h3><div class="sw-grid">{cells}</div>')
    return "".join(out)


def cheatsheet():
    icons = "".join(
        f'<figure class="ic"><span class="icon">{svg(p.relative_to(A))}</span><figcaption>{p.stem[5:]}</figcaption></figure>'
        for p in sorted((A / "icons").glob("icon-*.svg")))
    style = """<style>
.sw-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(8rem,1fr));gap:var(--ax-space-4);margin:var(--ax-space-4) 0 var(--ax-space-10)}
.sw{display:flex;flex-direction:column;gap:var(--ax-space-1);font-size:var(--ax-text-sm)}
.sw code{font-family:var(--ax-font-mono);font-size:var(--ax-text-xs)}
.chip-c{height:4.5rem;border-radius:var(--ax-radius-xl);border:1px solid var(--ax-color-border-strong)}
.spec{border-bottom:1px solid var(--ax-color-border);padding:var(--ax-space-4) 0}
.ic{display:flex;flex-direction:column;align-items:center;gap:var(--ax-space-2);margin:0;color:var(--ax-color-text-secondary);font-family:var(--ax-font-mono);font-size:var(--ax-text-xs)}
.ic .icon{width:2rem;height:2rem;color:var(--ax-color-text)}
.logo-tile{border-radius:var(--ax-radius-2xl);width:100%;height:auto;display:block}
.hexes{display:flex;gap:var(--ax-space-8);align-items:center}
.hexes svg{width:4rem;height:auto}
.do{border-left:3px solid var(--ax-color-signal);padding-left:var(--ax-space-4)}
.dont{border-left:3px solid var(--ax-color-negative);padding-left:var(--ax-space-4)}
</style>"""
    body = f"""{style}
{nav([('Color', '#color'), ('Tipo', '#tipo'), ('Componentes', '#comp'), ('Logo', '#logo')])}
<main id="top" style="padding-top:var(--ax-space-32)">
<div class="wrap">
  <p class="eyebrow">Guía de marca visual · v1.0</p>
  <h1 class="ax-hero-title" style="text-align:left">ASUSKF <span class="ax-gradient-text">Brand.</span></h1>
  <p class="mono muted" style="font-size:var(--ax-text-lg)">&gt; Simplificando lo complejo<span class="ax-cursor">_</span></p>
</div>

<section id="color"><div class="wrap">{section_title('01.', 'Paleta')}{swatch_grid()}
  <p class="muted"><strong>Fog</strong> solo para texto ≥ 18px (4.24:1 sobre Void). Texto pequeño secundario = <strong>Mist</strong> (7.87:1).</p>
</div></section>

<section id="tipo" class="alt"><div class="wrap">{section_title('02.', 'Tipografía')}
  <div class="spec"><p class="eyebrow">Hero · Plus Jakarta Sans 800</p><p class="ax-hero-title" style="text-align:left;margin:0">Simplificando lo <span class="ax-gradient-text">Complejo.</span></p></div>
  <div class="spec"><p class="eyebrow">Sección · Fira Code 700</p><p class="ax-section-title" style="margin:0"><span class="num">01.</span> <span>Ecosistema<span class="ax-cursor">_</span></span></p></div>
  <div class="spec"><p class="eyebrow">H3 · Plus Jakarta Sans 700</p><p style="font-size:var(--ax-text-3xl);font-weight:700;margin:0">ASUSKF Investing AI</p></div>
  <div class="spec"><p class="eyebrow">Cuerpo · Plus Jakarta Sans 400</p><p class="muted" style="font-size:var(--ax-text-lg);margin:0;max-width:60ch">Motor de decisiones autónomo que aprovecha <strong style="color:var(--ax-color-text-strong)">LLMs</strong> para análisis de sentimiento en tiempo real y gestión de portafolio.</p></div>
  <div class="spec"><p class="eyebrow">Terminal · Fira Code 400</p><p class="mono muted" style="font-size:var(--ax-text-xl);margin:0">&gt; Graph Neural Networks Researcher<span class="ax-cursor">_</span></p></div>
</div></section>

<section id="comp"><div class="wrap">{section_title('03.', 'Componentes')}
  <div class="row" style="margin-bottom:var(--ax-space-8)">
    <a class="ax-btn ax-btn--primary" href="#comp">Ver ecosistema</a>
    <a class="ax-btn ax-btn--ghost" href="#comp"><span class="icon" style="color:var(--ax-color-signal)">{svg('icons/icon-download.svg')}</span>Descargar CV</a>
  </div>
  <div class="row" style="margin-bottom:var(--ax-space-8)">
    <span class="ax-chip ax-chip--violet">Proyectos B2B</span><span class="ax-chip ax-chip--blue">Capacitación</span><span class="ax-chip ax-chip--emerald">Charlas</span>
    <span class="ax-badge" style="color:var(--ax-color-status-writing);background:rgb(245 158 11 / .1)">Writing</span>
    <span class="ax-badge" style="color:var(--ax-color-status-review);background:rgb(249 115 22 / .1)">Review</span>
    <span class="ax-badge" style="color:var(--ax-color-status-published);background:rgb(16 185 129 / .1)">Publicado</span>
  </div>
  <div class="grid g2">
    <article class="ax-card"><h3 style="font-size:var(--ax-text-2xl);margin-top:0">Tarjeta de proyecto</h3>
      <p class="muted">Superficie translúcida sin blur pesado, borde 5%, radio 24px. Hover: borde violeta + elevación.</p>
      <div class="row"><span class="ax-chip ax-chip--emerald">LLMs</span><span class="ax-chip ax-chip--blue">FinTech</span></div></article>
    <form class="ax-card" onsubmit="return false" aria-label="Ejemplo de formulario">
      <h3 class="mono" style="margin-top:0">Sistema_de_Contacto</h3>
      <label class="eyebrow" for="n">Nombre</label><input class="ax-input" id="n" placeholder="Tu nombre">
      <p class="row" style="margin-top:var(--ax-space-4)"><span class="ax-live" aria-hidden="true"></span> Disponible para consultoría</p>
    </form>
  </div>
</div></section>

<section id="logo" class="alt"><div class="wrap">{section_title('04.', 'Logo_y_Forma')}
  <div class="grid g3">
    <figure style="margin:0"><img class="logo-tile" src="{img('logos/asuskf-symbol-512.png')}" alt="Símbolo ASUSKF"><figcaption class="muted mono" style="font-size:var(--ax-text-xs)">asuskf-symbol · maestra</figcaption></figure>
    <figure style="margin:0"><img class="logo-tile" src="{img('logos/asuskf-investing-256.jpg', 'image/jpeg')}" alt="ASUSKF Investing"><figcaption class="muted mono" style="font-size:var(--ax-text-xs)">asuskf-investing · finanzas</figcaption></figure>
    <figure style="margin:0"><img class="logo-tile" src="{img('logos/asuskf-salud-256.jpg', 'image/jpeg')}" alt="ASUSKF Salud"><figcaption class="muted mono" style="font-size:var(--ax-text-xs)">asuskf-salud · salud</figcaption></figure>
  </div>
  <h3 class="eyebrow" style="margin-top:var(--ax-space-12)">Hexágonos (punta arriba, 1 por vista)</h3>
  <div class="hexes" style="color:var(--ax-color-accent)">{svg('hexagons/hex-spectrum.svg')}{svg('hexagons/hex-solid.svg')}<span style="color:var(--ax-logo-ice)">{svg('hexagons/hex-outline.svg')}</span></div>
  <h3 class="eyebrow" style="margin-top:var(--ax-space-12)">Iconos de línea</h3>
  <div class="grid g4" style="grid-template-columns:repeat(auto-fill,minmax(6rem,1fr))">{icons}</div>
  <div class="grid g2" style="margin-top:var(--ax-space-12)">
    <div class="do"><strong>Sí</strong><p class="muted">Logo desde archivo sobre fondo oscuro · un degradado por vista · <code>_</code> esmeralda · Mist para texto pequeño · motion con reduced-motion.</p></div>
    <div class="dont"><strong>No</strong><p class="muted">Redibujar el símbolo · logo sobre blanco · panal de hexágonos · degradados en botones · Fog en texto &lt; 18px · CDN en entregables.</p></div>
  </div>
</div></section>
</main>
<footer class="wrap mono muted" style="padding:var(--ax-space-12) var(--ax-space-6);font-size:var(--ax-text-xs);text-align:center">© 2026 ASUSKF · asuskf.github.io</footer>"""
    return page("ASUSKF Brand", "Hoja de referencia de la marca visual ASUSKF", body)


# ---------------------------------------------------------------- Landing
def landing():
    proj = lambda t, d, chips: f"""<article class="ax-card" data-reveal><h3 style="font-size:var(--ax-text-3xl);margin-top:0">{t}</h3>
      <p class="muted" style="font-size:var(--ax-text-lg)">{d}</p><div class="row">{chips}</div></article>"""
    paper = lambda st, color, t: f"""<div class="ax-card" data-reveal style="padding:var(--ax-space-6);border-radius:var(--ax-radius-lg);display:flex;justify-content:space-between;align-items:center;gap:var(--ax-space-4)">
      <div><span class="ax-badge" style="color:var({color})">{st}</span><h4 style="font-size:var(--ax-text-lg);margin:var(--ax-space-2) 0 0">{t}</h4></div>
      <a class="ax-btn" href="#" aria-label="Descargar artículo" style="padding:var(--ax-space-3);color:var(--ax-color-signal);background:var(--ax-color-surface-2)"><span class="icon">{svg('icons/icon-download.svg')}</span></a></div>"""
    body = f"""{nav([('Proyectos', '#projects'), ('Investigación', '#papers'), ('Contacto', '#contact')])}
<main id="top">
<section style="min-height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;padding-top:var(--ax-space-20)" class="wrap">
  <div class="ax-hex-hero" data-reveal><img src="{img('logos/asuskf-symbol-512.png')}" alt="Símbolo ASUSKF"></div>
  <h1 class="ax-hero-title" data-reveal>Simplificando lo <br><span class="ax-gradient-text">Complejo.</span></h1>
  <p class="mono muted" style="font-size:var(--ax-text-xl);text-align:center" aria-label="MLOps Specialist, Graph Neural Networks Researcher, Financial Intelligence Systems">&gt; <span id="typed" aria-hidden="true"></span><span class="ax-cursor" aria-hidden="true">_</span></p>
  <div class="row" style="justify-content:center;margin-top:var(--ax-space-6)">
    <a class="ax-btn ax-btn--primary" href="#projects">Ver ecosistema</a>
    <a class="ax-btn ax-btn--ghost" href="#"><span class="icon" style="color:var(--ax-color-signal)">{svg('icons/icon-download.svg')}</span>Descargar CV</a>
  </div>
</section>

<div class="wrap-text"><div class="ax-card" data-reveal style="background:linear-gradient(to right, rgb(15 23 42 / .8), rgb(15 23 42 / .4));box-shadow:var(--ax-shadow-card)">
  <h2 class="row" style="font-size:var(--ax-text-2xl);margin-top:0"><span class="ax-live" aria-hidden="true"></span>Disponible para consultoría y charlas</h2>
  <p class="muted"><strong style="color:var(--ax-color-text-strong)">[Rol principal]</strong> — [propuesta de valor en una o dos frases, con una métrica real].</p>
  <div class="row"><span class="ax-chip ax-chip--violet">Proyectos B2B</span><span class="ax-chip ax-chip--blue">Capacitación corporativa</span><span class="ax-chip ax-chip--emerald">Charlas tecnológicas</span></div>
</div></div>

<section id="projects"><div class="wrap">{section_title('01.', 'Ecosistema')}
  <div class="grid g2" style="margin-top:var(--ax-space-12)">
    {proj('[Proyecto A]', '[Descripción del proyecto y su impacto.]', '<span class="ax-chip ax-chip--emerald">LLMs</span><span class="ax-chip ax-chip--blue">FinTech</span>')}
    {proj('[Proyecto B]', '[Descripción del proyecto y su impacto.]', '<span class="ax-chip ax-chip--emerald">NLP</span><span class="ax-chip ax-chip--violet">MLOps</span>')}
  </div></div></section>

<section id="papers" class="alt"><div class="wrap-text">{section_title('02.', 'Artículos_Científicos')}
  <div class="grid" style="gap:var(--ax-space-4);margin-top:var(--ax-space-12)">
    {paper('Review', '--ax-color-status-review', '[Título del artículo en revisión]')}
    {paper('Publicado', '--ax-color-status-published', '[Título del artículo publicado]')}
  </div></div></section>

<section id="contact"><div class="wrap-text" style="max-width:42rem">
  <form class="ax-card" onsubmit="return false" data-reveal>
    <h2 class="mono" style="text-align:center;margin-top:0">Sistema_de_Contacto</h2>
    <label class="eyebrow" for="name">Nombre</label><input class="ax-input" id="name" required>
    <label class="eyebrow" for="msg" style="display:block;margin-top:var(--ax-space-4)">Mensaje</label><textarea class="ax-input" id="msg" rows="4" required></textarea>
    <button class="ax-btn ax-btn--primary mono" type="submit" style="width:100%;margin-top:var(--ax-space-6);border:0;background:var(--ax-color-action)">Enviar correo</button>
  </form>
</div></section>
</main>
<footer class="mono muted" style="padding:var(--ax-space-12);text-align:center;font-size:var(--ax-text-xs);border-top:1px solid var(--ax-color-border)">© 2026 ASUSKF</footer>"""
    return page("ASUSKF Landing", "Landing de inicio con la marca ASUSKF", body)


if __name__ == "__main__":
    for name, html in (("ASUSKF_Brand_Cheatsheet.html", cheatsheet()), ("ASUSKF_Landing_Starter.html", landing())):
        (OUT / name).write_text(html, encoding="utf-8")
        print(f"{name}: {len(html) // 1024} KB")
