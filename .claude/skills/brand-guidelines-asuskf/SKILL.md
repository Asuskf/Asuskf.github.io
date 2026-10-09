---
name: brand-guidelines-asuskf
description: >
  Aplica la identidad VISUAL oficial de ASUSKF (Kevin David Farinango — Data Science, ML
  Engineering, IA Generativa, Knowledge Graphs) a cualquier entregable — logo cubo-hexágono
  con nodos, paleta Void/Slate + espectro violeta→azul→esmeralda, Plus Jakarta Sans + Fira
  Code, firma "_" de cursor, tarjetas de vidrio y hexágono como acento — y revisa/mejora el
  diseño con los criterios de Apple Human Interface Guidelines incluidos. Úsala siempre que se
  cree o reestilice algo que deba verse como ASUSKF o como el sitio asuskf.github.io: páginas
  HTML/landing, el portafolio, dashboards, gráficos, slides, PDF/one-pagers, CV, posts sociales,
  sub-marcas ASUSKF Investing / ASUSKF Salud — aunque no digan "marca". También con "ponlo
  on-brand", "usa los colores de asuskf", "agrega el logo", "¿esto está en marca?", "revisa
  este diseño", "audita la UI/accesibilidad", "hazlo menos genérico".
---

# ASUSKF — Guía de Marca Visual

> **Versión** 1.0 · **Actualizado** 2026-10-08 · **Fuente** `asuskf.github.io`
> (repo `Asuskf/asuskf.github.io`) + logos oficiales · **Historial** `CHANGELOG.md`.
>
> Alcance: identidad **visual** (color, tipo, logo, iconos, forma, layout, motion) **más** un
> módulo de revisión de diseño basado en Apple HIG (`references/apple-design/`). No cubre voz
> ni copy, salvo las reglas de escritura de UI de la lente 5.

## AUTORIDAD DE ARCHIVOS — qué es canon

**Tier 1 — autoritativo**
- `SKILL.md` — reglas vinculantes (este archivo).
- `assets/tokens/colors_and_type.css` — fuente única de color, tipo, espaciado, radio, motion.
- Assets oficiales: `assets/logos/`, `assets/fonts/`, `assets/hexagons/`, `assets/icons/`.
- `references/*.md` — código de implementación por formato.
- `references/apple-design/` — Apple HIG (texto de Apple, citar, no parafrasear).

**Tier 2 — generado (no editar a mano; regenerar)**
- `assets/templates/ASUSKF_Brand_Cheatsheet.html` y `ASUSKF_Landing_Starter.html` → salen de
  `python assets/templates/build_templates.py`. Edita el script y re-ejecuta.

Nunca derives color, fuente o forma del logo desde fuera de Tier 1.

## ADHERENCIA — reglas duras (cada violación bloquea)

1. **Sin colores escritos a mano.** Nada de `#hex`/`rgb()` literal fuera del archivo de
   tokens: usa `var(--ax-…)`. Si un valor no existe como token, **para y avisa**.
2. **Sin px crudos** para espaciado/radio/tipo: usa `--ax-space-*`, `--ax-radius-*`, `--ax-text-*`.
3. **Solo dos familias:** Plus Jakarta Sans (display + cuerpo) y Fira Code (firma técnica).
   Servidas **localmente** desde `assets/fonts/` — nunca Google Fonts CDN en entregables.
4. **Offline primero.** Nada de CDN (Tailwind CDN, AOS, Typed.js) en entregables nuevos:
   embebe o reemplaza con CSS/JS local (ver `references/web-html.md`). El sitio en vivo usa
   CDN; eso es deuda técnica del sitio, no un patrón a copiar.
5. **Nunca dibujes, traces ni regeneres el símbolo.** El cubo-hexágono con nodos **solo** se
   coloca desde `assets/logos/asuskf-symbol-*.png` (`<img>` / data-URI / `add_picture`).
   Prohibido recrearlo con SVG, `clip-path`, canvas o IA generativa. El hexágono decorativo
   (`assets/hexagons/`) **no** es el logo y nunca lleva nodos encima.
6. **Nunca fondo blanco detrás del logo.** Los PNG/JPG del logo son losetas cuadradas con su
   propio fondo oscuro: se colocan sobre superficies oscuras (Void/Slate) o con su loseta
   redondeada; jamás recortadas sobre blanco ni con el fondo removido.
7. **Accesibilidad no negociable** (lente 1 de Apple): contraste ≥ 4.5:1 texto normal,
   ≥ 3:1 texto ≥ 18px o bold; objetivos táctiles ≥ 44×44px; todo motion respeta
   `prefers-reduced-motion`.

## Tema — dark por defecto, light de primera clase

La marca nace **oscura** (Void `#020617`). Todo color es una variable en `:root`
(dark) y se sobreescribe con `[data-theme="light"]` (acentos oscurecidos para pasar AA).
Cambia con `<html data-theme="light">` o por sección. Nunca un selector de apariencia propio
dentro de una app nativa — respeta el del sistema (`dark-mode.md`).

---

## 01 — Logo

### Activos

| Archivo | Qué es | Uso |
|---|---|---|
| `assets/logos/asuskf-symbol-2048.png` | **Símbolo maestro**: cubo-hexágono de vidrio (hielo→lavanda) con circuito de 5 nodos, sobre degradado índigo→océano | Hero, portadas, avatar, OG image |
| `asuskf-symbol-512.png` / `-192` | Mismo, reducido | Web/app icon, tarjetas |
| `asuskf-symbol-64.png` / `-32` | Mismo, reducido | Favicon, nav (render a 40px) |
| `asuskf-investing-1024.jpg` / `-256` | **Sub-marca ASUSKF Investing**: emblema dorado sobre verde bosque, "@ASUSKF" | Contenido de finanzas / portafolio eToro |
| `asuskf-salud-1024.jpg` / `-256` | **Sub-marca ASUSKF Salud**: hexágono azul-verde con caduceo y circuito | Contenido de IA aplicada a salud |

### Wordmark — tipográfico, no un archivo

El wordmark de ASUSKF **es texto vivo**, tal como en el sitio: `ASUSKF_`
- Fira Code, **Bold (700)**, `letter-spacing: var(--ax-tracking-tighter)`, color texto.
- El guion bajo final `_` en **Growth Emerald** (`--ax-color-signal`). Es la firma de marca.
- Lockup horizontal: símbolo (40px, `--ax-radius-md`) + 12px de gap + wordmark.
- Siempre MAYÚSCULAS `ASUSKF`. En handles: `@Asuskf`. Pie: `© <año> ASUSKF`.

### Reglas del logo

- Espacio libre mínimo = ½ del ancho del símbolo en todos los lados.
- No deformar, rotar, recolorear, añadir contorno, ni poner el símbolo sobre fotos complejas.
- En tarjetas de vitrina el símbolo puede ir en **escala de grises → color en hover**
  (patrón del sitio). Nunca permanentemente desaturado como logo principal.
- El sparkle ✦ de la esquina inferior derecha es parte del arte: no recortar.
- Sub-marcas solo dentro de su contexto (Investing → finanzas; Salud → salud). La maestra
  manda en todo lo demás.

---

## 02 — Paleta de color

### Base — Slate (≈ 80% de cualquier composición)

| Nombre | Token | Hex | Rol | Contraste sobre Void |
|---|---|---|---|---|
| **Void** | `--ax-slate-950` | `#020617` | Fondo de página | — |
| **Deep Slate** | `--ax-slate-900` | `#0F172A` | Superficie, tarjetas, secciones alternas | — |
| **Graphite** | `--ax-slate-800` | `#1E293B` | Inputs, chips, superficie elevada | — |
| **Wire** | `--ax-slate-700` | `#334155` | Bordes de input, divisores | — |
| **Fog** | `--ax-slate-500` | `#64748B` | Solo texto ≥ 18px o no-texto | 4.24:1 ⚠️ |
| **Mist** | `--ax-slate-400` | `#94A3B8` | Texto secundario, nav | 7.87:1 ✅ |
| **Frost** | `--ax-slate-200` | `#E2E8F0` | `<strong>` dentro de párrafos | 16.36:1 ✅ |
| **Snow** | `--ax-slate-100` | `#F1F5F9` | Texto principal | 18.41:1 ✅ |

### Espectro ASUSKF — acentos (≈ 15%)

| Nombre | Token | Hex | Rol | Contraste |
|---|---|---|---|---|
| **Mind Violet** | `--ax-violet-500` | `#8B5CF6` | Color de marca: hover de borde, focus, hexágono | — |
| Mind Violet 400 | `--ax-violet-400` | `#A78BFA` | Texto acento en dark | 7.41:1 |
| Mind Violet 600 | `--ax-violet-600` | `#7C3AED` | Fill de CTA de formulario | blanco 5.70:1 |
| **Hero Indigo** | `--ax-indigo-600` | `#4F46E5` | CTA principal del hero | blanco 6.29:1 |
| **Signal Blue** | `--ax-blue-500` / `-400` | `#3B82F6` / `#60A5FA` | Enlaces, "Ver video →", serie 2 | 7.93:1 |
| **Growth Emerald** | `--ax-emerald-400` | `#34D399` | Cursor `_`, numerales `01.`, "disponible", publicado | 10.49:1 |

### Logo y sub-marcas (≈ 5%, solo en su contexto)

| Nombre | Hex | Origen |
|---|---|---|
| Logo Indigo / Navy / Ocean | `#1D154C` / `#1B376D` / `#0E4E79` | Degradado de fondo del símbolo |
| Logo Ice | `#9BB8D3` | Cara de vidrio y nodos |
| Invest Forest / Moss / Gold | `#053C25` / `#375235` / `#C9B97A` | ASUSKF Investing |
| Health Navy / Teal / Sky | `#133250` / `#377776` / `#699DB3` | ASUSKF Salud |

### Estados (papers / pipeline)

`--ax-color-status-writing` ámbar `#F59E0B` · `--ax-color-status-review` naranja `#F97316` ·
`--ax-color-status-published` esmeralda `#34D399`. Siempre con **texto** ("Review",
"Publicado"), nunca solo color.

### Degradados — la única excepción a "flat"

- **Infinitus Spectrum** `--ax-gradient-spectrum` (violeta→azul→esmeralda) y **Hero**
  `--ax-gradient-hero` (violeta→esmeralda): texto recortado (`background-clip: text`).
- **Hex** `--ax-gradient-hex` (violeta→azul, 135°): relleno del hexágono hero.
- **Regla:** **un** degradado protagonista por vista — el titular hero *o* el hexágono, no
  ambos compitiendo. Nunca degradados en fondos de sección, botones ni cuerpo de texto.

### Reglas de color

- Una idea = un color: **violeta** = marca/acción, **azul** = enlace/info, **esmeralda** =
  señal positiva/vivo/publicado. No intercambiar.
- Chips tintados: fondo acento al 10% + borde acento al 20% + texto acento 400
  (`bg-purple-500/10 border-purple-500/20 text-purple-400`).
- `Fog #64748B` **no** para texto < 18px sobre Void/Slate (falla AA). Usa **Mist**. (El sitio
  actual lo usa en "CON LA CONFIANZA DE" y en el pie — corregir.)
- Colores de terceros (LinkedIn `#0A66C2`, WhatsApp `#25D366`, eToro `#6FC82A`) solo en sus
  propios botones, nunca como color de marca.
- Light: usar la variante 700 de cada acento (tokens ya mapeados); nunca violeta-400 sobre blanco.

---

## 03 — Tipografía

| Rol | Familia | Pesos | Uso |
|---|---|---|---|
| **Display / títulos / cuerpo** | **Plus Jakarta Sans** (variable 200–800 + itálica) | 300, 400, 700, **800** | Hero ExtraBold, H2–H4 Bold, párrafos Regular |
| **Firma técnica** | **Fira Code** (variable 300–700) | 400, 500, 700 | Wordmark, nav, títulos de sección `01. Ecosistema_`, chips, badges, CTA de formulario, notas, pie |

| Nivel | Familia | Tamaño | Peso | Detalles |
|---|---|---|---|---|
| Hero | Jakarta | `--ax-text-hero` (48→96px) | 800 | `tracking-tight`, última palabra con degradado |
| Título de sección | **Fira Code** | 36px | 700 | `<span emerald>01.</span> Nombre_` (snake_case + `_`) |
| H3 tarjeta | Jakarta | 30px | 700 | |
| H4 fila | Jakarta | 18px | 700 | |
| Cuerpo | Jakarta | 16–18px | 400 | `line-height 1.625`, Mist |
| Nav | Fira Code | 14px | 600 | MAYÚSCULAS, `tracking-widest`, Mist→Snow hover |
| Eyebrow / overline | Fira Code | 14px | 400 | MAYÚSCULAS, `tracking-widest`, Mist |
| Chip | Fira Code | 12px | 400 | pill tintado |
| Badge de estado | Jakarta | 10px | 700 | MAYÚSCULAS, `tracking-wider` |
| Subtítulo terminal | Fira Code | 18–20px | 400 | prefijo `> ` + texto tipeado + cursor `_` |

**Firmas tipográficas de ASUSKF** (usar con intención, no en todo):
1. **Sufijo `_`** en títulos de sección y wordmark — evoca el cursor de terminal.
2. **Numeral esmeralda** `01.` `02.` antes del título de sección — solo si las secciones son
   realmente una secuencia.
3. **Prompt `> `** antes de una línea tipeada (rotando roles: MLOps, GNN, Financial Intelligence).

Fuentes en `assets/fonts/`: TTF variable (PPTX/DOCX) y woff2 (HTML/PDF, subset latin con
tildes y ñ). Licencia SIL OFL 1.1 — los `OFL-*.txt` viajan con las fuentes.

---

## 04 — Forma: hexágono y nodos

El símbolo es un **hexágono punta-arriba** (cubo isométrico) atravesado por un **grafo de
nodos** — la marca habla de grafos, datos conectados y MLOps.

- **Orientación canónica: punta arriba** (como el símbolo). El sitio usa hoy un `clip-path`
  plano-arriba en `.hex-icon`; en piezas nuevas usa `assets/hexagons/` (punta arriba).
- Hexágono como **acento: 1 por vista** (máx. 2). Nunca teselado / panal de fondo.
- Usos: (a) marco del símbolo en el hero (`hex-spectrum`), (b) bullet/acento pequeño
  (`hex-solid` con `currentColor`), (c) contenedor de foto.
- **Motivo de nodos** (círculo + línea quebrada) permitido como ilustración de datos/grafos,
  trazo `--ax-logo-ice` o Mist, nunca encima del símbolo ni imitándolo.

## 05 — Iconos

Estilo **línea** (familia Heroicons outline, la del sitio): viewBox 24, `stroke-width 2`,
extremos y uniones redondeados, `stroke="currentColor"`, sin relleno.
Set en `assets/icons/`: `download`, `arrow-right`, `external`, `graph-nodes`, `chart-up`,
`paper`, `mail`, `talk`, `terminal`. Color: Mist en reposo; acento (esmeralda/azul) solo
dentro de un botón tintado; blanco sobre fill de acción. Icono solo-icono → `aria-label`.
Logos de terceros (GitHub, LinkedIn, WhatsApp, eToro) en su forma oficial, dentro de su botón.

## 06 — Superficies y componentes

| Componente | Receta (tokens) |
|---|---|
| **Nav** | fija, `--ax-color-nav-glass` + `backdrop-filter: blur(var(--ax-blur-glass))`, borde inferior `--ax-color-border` |
| **Tarjeta proyecto** | `--ax-color-surface-glass`, borde `--ax-color-border`, `--ax-radius-2xl`, padding 40px |
| **Tarjeta hover** | borde → `--ax-color-accent`, `translateY(var(--ax-hover-lift))`, `--ax-dur` |
| **Fila de paper** | surface-glass, `--ax-radius-lg`, padding 24px; publicado: borde esmeralda/20 + botón icono esmeralda |
| **Panel destacado** | degradado slate-900/80→slate-900/40, `--ax-radius-2xl`, `--ax-shadow-card` |
| **CTA primario** | fill `--ax-color-action-hero` (o `--ax-color-action`), texto blanco Bold, `--ax-radius-lg`, padding 16×32, `--ax-shadow-glow-indigo` |
| **CTA secundario** | surface-glass + borde esmeralda/50 → esmeralda en hover, glow esmeralda |
| **CTA de terceros** | pill `#111` + borde del color del tercero/50 |
| **Chip** | pill, acento/10 fondo, acento/20 borde, texto acento-400, Fira Code 12px |
| **Toggle EN/ES** | pill Deep Slate, activo = Graphite + texto esmeralda |
| **Input** | Graphite, borde Wire, `--ax-radius-md`, focus borde violeta (+ anillo visible) |
| **Indicador "disponible"** | punto 8px esmeralda con `pulse` (desactivado con reduced-motion) |

**Vidrio (glassmorphism) — regla Apple:** el blur pertenece a la **capa flotante funcional**
(nav, toasts, popovers). En tarjetas de contenido usa la superficie translúcida **sin** blur
pesado; nunca apiles vidrio sobre vidrio. Ver `references/apple-design/hig/liquid-glass.md`.

## 07 — Layout

- Contenedor `--ax-container` (1280px) para grids; `--ax-container-text` (1024px) para texto.
- Secciones con padding vertical 128px (`--ax-space-32`), laterales 24px; móvil 16px mín.
- Grids: 1 col → 2 (proyectos, `lg`) / 3 (charlas, casos, `md`); gap 32–40px.
- Ritmo de fondo: Void ↔ Deep Slate/30 alternando por sección, divisores `--ax-color-border`.
- Orden canónico de landing: Nav → Hero (hexágono + titular + `> tipeado` + 2 CTA) → Panel
  "Disponible" → Carrusel "Con la confianza de" → 01 Ecosistema → 02 Artículos → Charlas →
  Casos → Contacto → Pie.
- Logos de clientes: escala de grises 40% opacidad → color al hover, máscara de bordes difusa.

## 08 — Motion

- Revelado al scroll: fade-up / zoom, `--ax-dur-reveal` (1s), una sola vez (`once`).
  Escalonar 100–200ms entre hermanos, máximo 3 niveles.
- Hover: elevación −5px y cambio de borde en `--ax-dur`. Iconos: `scale 1.1` o `translateX`.
- Carrusel infinito 25s lineal, pausa en hover. Texto tipeado 60ms/30ms con cursor `_`.
- **Siempre** `prefers-reduced-motion`: sin revelados, sin pulse, carrusel estático, texto
  tipeado mostrado completo. El significado nunca depende de la animación.

## 09 — Aplicación por formato

| Produciendo… | Leer | Partir de |
|---|---|---|
| HTML / landing / artifact | `references/web-html.md` | `assets/templates/ASUSKF_Landing_Starter.html` |
| Hoja de referencia de marca | — | `assets/templates/ASUSKF_Brand_Cheatsheet.html` |
| Slides, PDF one-pager, DOCX, CV | `references/documents.md` | — |
| Gráficos / dashboards | §10 abajo + `references/apple-design/hig/charting-data.md` | — |
| Revisión / auditoría de diseño | §11 + `references/apple-design/README.md` | — |

## 10 — Visualización de datos

- Fondo Void o Deep Slate; rejilla `--ax-color-border-strong`; ejes Fira Code 12px Mist.
- Orden de series: **Violet 400 → Blue 400 → Emerald 400 → Ice → Mist**. Una serie destacada
  en esmeralda (positivo) o violeta (marca); el resto en Mist.
- KPI: número Jakarta ExtraBold (o Fira Code para métricas técnicas), etiqueta MAYÚSCULAS
  Fira Code Mist. Ej.: "99.8% reducción de costos de IA".
- Finanzas (Investing): positivo `--ax-color-positive` (esmeralda), negativo
  `--ax-color-negative` (rojo `#F87171` dark / `#B91C1C` light). Rojo solo para dato negativo o error.
- Nunca color como única codificación: etiquetas directas o patrones.

## 11 — Revisión de diseño con Apple HIG (módulo integrado)

Incluye la skill *apple-design* (dickwu/apple-design-skill): 123 páginas de Apple Human
Interface Guidelines + guía de Liquid Glass + traducción a Flutter/React Native/Tauri/Electron.

**Cuándo:** "revisa / audita / critica este diseño", "¿es buena UI?", "hazlo menos genérico",
antes de entregar cualquier pantalla o landing importante.

**Cómo (resumen; detalle en `references/apple-design/REVIEW.md`):**
1. Contexto: plataforma, framework, artefacto, tesis de la pantalla.
2. Cargar siempre `accessibility.md`, `layout.md`, `typography.md`, `color.md` (+
   `designing-for-ios.md`/`-macos.md` si aplica, + `cross-platform.md` si no es nativo). Luego
   3–6 páginas según lo que haya en pantalla (ruteo en `hig-lookup.md`). Nunca todo el directorio.
3. Cinco lentes en orden: **Accesibilidad → Convenciones → Visual/craft → Interacción → Contenido**.
4. Reporte: Summary · Critical · Improvements · Craft notes · What works · Platform notes;
   cada hallazgo con *What / Why (cita `archivo.md › Heading`) / Fix* y severidad.
5. **Además** valida contra esta guía: tokens, logo desde archivo, `_` y numerales con
   sentido, un solo degradado, hexágono 1×vista, contraste de Fog.

**Para web**, Apple aplica como principios (accesibilidad, color, tipo, layout, escritura),
no como convenciones de plataforma — dilo en el reporte.

**Lente craft aplicada a ASUSKF:** la estética "casi-negro + un acento neón" es una de las
plantillas genéricas que Apple/la skill señalan. Lo que hace a ASUSKF **inconfundible** es:
el **símbolo cubo-hexágono con nodos**, la **voz de terminal** (`_`, `> `, Fira Code) y el
**espectro violeta→esmeralda**. Gasta la audacia ahí y deja el resto en silencio.

## Referencia rápida

**Marca**: ASUSKF · wordmark `ASUSKF_` (Fira Code Bold, `_` esmeralda) · web asuskf.github.io
**Base**: Void `#020617` · Deep Slate `#0F172A` · Graphite `#1E293B` · Mist `#94A3B8` · Snow `#F1F5F9`
**Espectro**: Violet `#8B5CF6`/`#A78BFA` · Indigo `#4F46E5` · Blue `#3B82F6`/`#60A5FA` · Emerald `#34D399`
**Logo**: Indigo `#1D154C` · Navy `#1B376D` · Ocean `#0E4E79` · Ice `#9BB8D3`
**Tipos**: Plus Jakarta Sans (todo) · Fira Code (firma técnica)
**Forma**: hexágono punta-arriba, 1 por vista · nodos · radios 8/12/16/24px · pill para chips
**Estilo**: oscuro · técnico · vidrio solo flotante · un degradado por vista · AA siempre
