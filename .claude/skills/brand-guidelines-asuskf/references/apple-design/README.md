# Módulo Apple Design (HIG) — dentro de brand-guidelines-asuskf

Importado de **[dickwu/apple-design-skill](https://github.com/dickwu/apple-design-skill)**
(clonado 2026-10-08). Sirve para **revisar, auditar y mejorar** diseños ASUSKF con los
criterios de Apple Human Interface Guidelines.

| Archivo | Qué es |
|---|---|
| `REVIEW.md` | Proceso completo del revisor: principios, 5 lentes, formato de reporte, modo mejora |
| `hig-lookup.md` | Tabla de ruteo: tema → página HIG (generada) |
| `hig/*.md` | 123 páginas de HIG en el texto de Apple + `liquid-glass.md` (curada) |
| `cross-platform.md` | Vocabulario de Apple en Flutter, React Native, Tauri, Electron |
| `pull-hig.mjs` | Regenera `hig/` desde developer.apple.com (Node ≥ 18) |

## Uso rápido

1. Lee `REVIEW.md` (proceso) — no cargues todo `hig/`.
2. Siempre: `hig/accessibility.md`, `hig/layout.md`, `hig/typography.md`, `hig/color.md`.
3. Según la pantalla: rutea con `hig-lookup.md` (3–6 archivos más).
4. Cita como `archivo.md › Heading`. Sin cita = "juicio propio".
5. Cruza con la marca: tokens, logo desde archivo, contraste de Fog, un degradado por vista,
   vidrio solo en capa flotante (`hig/liquid-glass.md`, `hig/materials.md`).

## Mapeo HIG ↔ marca ASUSKF

| HIG | Decisión ASUSKF |
|---|---|
| Contraste 4.5:1 / 3:1 (`color.md`, `accessibility.md`) | Mist para texto pequeño; Fog solo ≥ 18px |
| Controles ≥ 44pt (`accessibility.md`) | `--ax-touch-min: 44px` en botones, toggle EN/ES, iconos |
| Motion opcional (`motion.md`) | Tokens de duración → 0 con `prefers-reduced-motion` |
| Branding difiere al contenido (`branding.md`) | Logo una vez por vista; color de marca para acción primaria |
| Liquid Glass solo en capa funcional (`liquid-glass.md`) | Blur en nav/overlays, no en tarjetas de contenido |
| Dark mode con colores semánticos (`dark-mode.md`) | `--ax-color-*` con variante light |
| Escritura clara (`writing.md`) | "Descargar CV", "Enviar correo": la etiqueta dice lo que pasa |

## Actualizar las páginas HIG

```bash
node references/apple-design/pull-hig.mjs --out references/apple-design/hig --lookup references/apple-design/hig-lookup.md
```

## Licencia / origen

El texto de las guías pertenece a Apple Inc. y se reproduce de las
[Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
públicas para revisión de diseño asistida por IA, con enlace a la fuente en cada archivo.
Ni este proyecto ni apple-design-skill están afiliados ni respaldados por Apple.
