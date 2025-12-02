#!/usr/bin/env python3
"""
Generador simple de imágenes etiquetadas para perfumes (Pillow).

Uso:
 1. Coloca las fotos de botellas en `assets/inputs/` con nombres:
    - rosa.jpg (o .png)
    - ambra.jpg
    - fiori.jpg
    - logo.png (logo con fondo transparente preferible)
 2. Instala Pillow: `pip install Pillow`
 3. Ejecuta: `python3 tools/generate_labelled_images.py`
 4. Salida: `assets/generated/` con archivos JPEG

El script coloca el logo centrado arriba y un rótulo de texto con marca, nombre y edición.
"""
import os
from PIL import Image, ImageDraw, ImageFont

# Config
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
INPUT_DIR = os.path.join(ROOT, 'assets', 'inputs')
OUTPUT_DIR = os.path.join(ROOT, 'assets', 'generated')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Perfumes a procesar (nombre de archivo -> metadata)
PERFUMES = {
    'rosa.jpg': {
        'brand': 'ESSENZA',
        'name': 'Rosa di Milano',
        'edition': 'Signature',
        'notes': 'Rosa Italiana · Jazmín · Sándalo'
    },
    'ambra.jpg': {
        'brand': 'ESSENZA',
        'name': 'Ambra Veneziana',
        'edition': 'Noches de Serenidad',
        'notes': 'Ámbar · Vainilla · Especias Orientales'
    },
    'fiori.jpg': {
        'brand': 'ESSENZA',
        'name': 'Fiori di Toscana',
        'edition': 'Fresco Mediterráneo',
        'notes': 'Lavanda · Bergamota · Cedro'
    }
}

# Permite fuentes personalizadas vía variable FONT_PATH, sino usa la fuente por defecto.
FONT_PATH = os.environ.get('ESSENZA_FONT')  # e.g. '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

def load_font(size, bold=False):
    if FONT_PATH and os.path.isfile(FONT_PATH):
        try:
            return ImageFont.truetype(FONT_PATH, size=size)
        except Exception:
            pass
    # Fallback a una fuente integrada
    try:
        return ImageFont.truetype('DejaVuSans.ttf', size=size)
    except Exception:
        return ImageFont.load_default()


def process_image(filename, meta):
    in_path = os.path.join(INPUT_DIR, filename)
    if not os.path.isfile(in_path):
        print(f"[WARN] No existe: {in_path} — omitiendo")
        return

    img = Image.open(in_path).convert('RGBA')
    w, h = img.size
    print(f"Procesando {filename} — tamaño {w}x{h}")

    # Crear capa para composiciones
    canvas = Image.new('RGBA', (w, h), (255,255,255,0))
    canvas.paste(img, (0,0))

    draw = ImageDraw.Draw(canvas)

    # Logo
    logo_path_png = os.path.join(INPUT_DIR, 'logo.png')
    if os.path.isfile(logo_path_png):
        try:
            logo = Image.open(logo_path_png).convert('RGBA')
            # Escalar logo: 22% del ancho de la imagen, máximo 400px
            logo_w = min(int(w * 0.22), 400)
            logo_h = int(logo_w * logo.size[1] / logo.size[0])
            logo = logo.resize((logo_w, logo_h), Image.LANCZOS)
            logo_x = (w - logo_w) // 2
            logo_y = int(h * 0.06)
            canvas.paste(logo, (logo_x, logo_y), logo)
        except Exception as e:
            print(f"Error cargando logo: {e}")

    # Area de texto (panel semitransparente en la parte inferior central)
    panel_height = int(h * 0.24)
    panel_width = int(w * 0.86)
    panel_x = (w - panel_width) // 2
    panel_y = h - panel_height - int(h * 0.04)

    # Rectángulo semitransparente
    panel_color = (255, 255, 255, 220)  # blanco con opacidad
    # Borde dorado
    border_color = (189, 153, 85, 255)
    draw.rounded_rectangle([panel_x, panel_y, panel_x + panel_width, panel_y + panel_height], radius=18, fill=panel_color, outline=border_color, width=4)

    # Texto
    brand_font = load_font(int(panel_height * 0.22))
    name_font = load_font(int(panel_height * 0.28))
    small_font = load_font(int(panel_height * 0.12))

    # Escribir marca centrada arriba dentro del panel
    brand_text = meta.get('brand', '')
    bw, bh = draw.textsize(brand_text, font=brand_font)
    draw.text((panel_x + (panel_width - bw) // 2, panel_y + int(panel_height * 0.06)), brand_text, fill=(72,34,29,255), font=brand_font)

    # Nombre principal (mayor)
    name_text = meta.get('name', '')
    nw, nh = draw.textsize(name_text, font=name_font)
    draw.text((panel_x + (panel_width - nw) // 2, panel_y + int(panel_height * 0.32)), name_text, fill=(42,20,15,255), font=name_font)

    # Edición y notas, alineados al centro y con letter spacing simple
    edition = meta.get('edition', '')
    notes = meta.get('notes', '')
    ex, ey = panel_x + int(panel_width*0.06), panel_y + int(panel_height * 0.72)
    draw.text((ex, ey), f"—Edición: {edition}—", fill=(80,40,30,220), font=small_font)
    draw.text((ex, ey + int(panel_height * 0.12)), notes, fill=(80,40,30,220), font=small_font)

    # Exportar como JPEG (fondo blanco)
    out = Image.new('RGB', (w,h), (255,255,255))
    out.paste(canvas, mask=canvas.split()[3])

    out_name = os.path.splitext(filename)[0] + '_labelled.jpg'
    out_path = os.path.join(OUTPUT_DIR, out_name)
    out.save(out_path, quality=94)
    print(f"Guardado -> {out_path}")


if __name__ == '__main__':
    for fname, meta in PERFUMES.items():
        process_image(fname, meta)
    print('\nHecho. Revisa `assets/generated/` para las imágenes.')
