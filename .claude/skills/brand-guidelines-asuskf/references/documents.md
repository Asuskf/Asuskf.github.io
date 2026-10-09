# ASUSKF — Slides, PDF, DOCX y CV

## Principios comunes

- Fondo **Void/Deep Slate** por defecto (marca oscura). Documentos largos para imprimir
  pueden usar el tema **light** (tokens `[data-theme="light"]`): fondo blanco, texto Slate 900,
  acentos en variante 700.
- Logo: PNG oficial (`assets/logos/asuskf-symbol-*.png`) con su loseta — nunca sobre blanco
  sin la loseta; en documentos light colócalo dentro de un bloque Void redondeado.
- Wordmark `ASUSKF_` como texto vivo en Fira Code Bold + `_` esmeralda.
- Fuentes: TTF variables de `assets/fonts/`. Si la herramienta no lee variables, instancia
  pesos estáticos:
  ```bash
  python -m fontTools.varLib.instancer assets/fonts/PlusJakartaSans.ttf wght=800 -o PJS-ExtraBold.ttf
  python -m fontTools.varLib.instancer assets/fonts/FiraCode.ttf wght=700 -o FiraCode-Bold.ttf
  ```

## Slides (PPTX / Google Slides, 16:9)

| Slide | Composición |
|---|---|
| Portada | Void, símbolo 512 a la izquierda (o centrado en hexágono espectro), titular Jakarta ExtraBold con la última palabra en esmeralda o violeta-400, subtítulo `> rol` en Fira Code Mist |
| Divisor de sección | Void, `01.` esmeralda + `Nombre_` Fira Code 40pt, un hexágono `hex-outline` en Ice al 30% |
| Contenido | Deep Slate, título Fira Code `Nombre_`, cuerpo Jakarta 18–20pt Mist, tarjetas Graphite radio 16 |
| Métricas | 2–3 KPI Jakarta ExtraBold 60pt; uno en esmeralda, resto Snow; etiqueta Fira Code MAYÚSCULAS |
| Papers / estado | filas con badge Writing (ámbar) / Review (naranja) / Publicado (esmeralda) + texto |
| Cierre | Void, lockup `ASUSKF_`, enlaces (asuskf.github.io, LinkedIn, GitHub) en Fira Code |

Pie de contenido: `ASUSKF_` (izq.) + `asuskf.github.io` (der.), Fira Code 10pt Mist.
En python-pptx: rasteriza el logo a la medida con `add_picture`; nunca `add_shape` imitándolo.

## PDF / one-pager (HTML → Imprimir → Guardar PDF)

Construye en HTML con fuentes base64 (ver `web-html.md`) a tamaño Carta/A4:
`@page { size: A4; margin: 0 } body { width: 210mm }`. Activa
`-webkit-print-color-adjust: exact; print-color-adjust: exact;` para que el fondo oscuro
se imprima. Bloques que van juntos = un solo contenedor con `break-inside: avoid`.

## DOCX / CV

- Tema light: cuerpo Plus Jakarta Sans 10.5pt Slate 900; títulos Jakarta Bold;
  encabezados de sección Fira Code Bold MAYÚSCULAS con `_` final y una regla violeta-600
  de 2pt debajo.
- Cabecera: bloque Void con el lockup (símbolo + `ASUSKF_` blanco/esmeralda) y rol en Mist.
- Tablas: encabezado Slate 100, filas alternas Slate 50, bordes Slate 200.
- Chips de skills → texto Fira Code 9pt con fondo Slate 100 (no colores de acento en print).
