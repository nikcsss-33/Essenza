Instrucciones para generar imágenes etiquetadas

1) Prepara las imágenes que quieres usar (las que has adjuntado). Ponlas en:
   `assets/inputs/`
  - `rosa.jpg`  (foto para Rosa di Milano)
  - `ambra.jpg` (foto para Ambra Veneziana)
  - `fiori.jpg` (foto para Fiori di Toscana)
   - `logo.png`  (logo de ESSENZA, preferible con fondo transparente)

2) Instala dependencias (en tu entorno o contenedor):

```bash
python3 -m pip install --user --upgrade pip
python3 -m pip install --user Pillow
```

3) Ejecuta el generador:

```bash
python3 tools/generate_labelled_images.py
```

4) Salida: `assets/generated/` con las imágenes resultantes (JPG).

Notas:
- Puedes definir una fuente personalizada exportando `ESSENZA_FONT` al path de la fuente ttf antes de ejecutar.
  Ejemplo:

```bash
export ESSENZA_FONT=/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
python3 tools/generate_labelled_images.py
```

- Si quieres que yo ejecute el script aquí, sube las imágenes (rosa/ambra/fiori/logo) a `assets/inputs/` y te lo ejecuto y muestro la vista previa.
