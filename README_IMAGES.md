Generar imágenes realistas etiquetadas

Qué he creado:
- `tools/generate_labelled_images.py` — script Pillow que compone logo + texto sobre cada foto de perfume.
- `assets/README_GENERATION.md` — instrucciones paso a paso.
- `preview_etiquetas.html` — plantilla para previsualizar las imágenes generadas en el sitio.

Siguiente paso (opcional):
- Si quieres que yo ejecute el script aquí y genere las imágenes, sube los ficheros (los attachments que compartiste) a `assets/inputs/` dentro del workspace: `rosa.jpg`, `ambra.jpg`, `fiori.jpg`, `logo.png`. Luego lo ejecuto y te muestro la vista previa.

Comandos rápidos:

```bash
# instalar Pillow
python3 -m pip install --user Pillow
# ejecutar generador
python3 tools/generate_labelled_images.py
# abrir preview (si el servidor ya está en marcha en :8080):
# http://localhost:8080/preview_etiquetas.html
```
