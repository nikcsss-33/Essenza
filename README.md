# ESSENZA - Sitio Web de Lujo

Sitio web elegante y sofisticado para **Essenza**, una empresa multinacional italiana de productos de belleza e higiene femenina de lujo.

## Características

- **Diseño Responsivo**: Adaptado para todos los dispositivos (desktop, tablet, móvil)
- **Interfaz Elegante**: Paleta de colores premium (#790000, #b47532) y tipografía sofisticada (Elephant Pro)
- **Efecto 3D Interactivo**: Imágenes de produ
- **Imágenes SVG Optimizadas**: Gráficos vectoriales escalables de alta calidad
- **Personalización**: Sistema de consultas para productos personalizados (opcional)
- **12 Tiendas Globales**: Páginas individuales para cada boutique en capitales del lujo mundial
- **Navegación Fluida**: Scroll suave, menú desplegable y navegación interactiva
- **Formularios Interactivos**: Validación de datos y notificaciones en tiempo real
- **Animaciones Avanzadas**: Efectos visuales 3D con transformaciones CSS y seguimiento de mouse
- **SEO Optimizado**: Estructura semántica HTML5

## Estructura del Proyecto

```
Essenza/
├── index.html          # Página principal
├── perfumes.html       # Página de perfumes
├── lociones.html       # Página de lociones
├── maquillaje.html     # Página de maquillaje
├── skincare.html       # Página de cuidado de piel
├── styles.css          # Estilos y diseño con efectos 3D
├── script.js           # Funcionalidad JavaScript con interactividad 3D
├── test-images.html    # Página de prueba de imágenes
├── cleanup-images.sh   # Script de limpieza de archivos
├── assets/
│   └── images/         # Imágenes de productos (SVG)
│       ├── perfume-1.svg
│       ├── lotion-1.svg
│       ├── makeup-1.svg
│       ├── skincare-1.svg
│       ├── personalization-1.svg
│       ├── personalization-2.svg
│       └── personalization-3.svg
├── tiendas/            # Páginas individuales de tiendas
│   ├── milan.html
│   ├── paris.html
│   ├── monaco.html
│   ├── nueva-york.html
│   ├── londres.html
│   ├── dubai.html
│   ├── tokio.html
│   ├── hong-kong.html
│   ├── singapur.html
│   ├── beverly-hills.html
│   ├── zurich.html
│   └── cannes.html
└── README.md           # Este archivo
```

## Paleta de Colores

- **Vino Tinto Profundo**: `#790000` - Color primario
- **Carbón Profundo**: `#2C2C2C` - Color secundario
- **Bronce Cálido**: `#b47532` - Color de acento
- **Crema**: `#FAF8F5` - Fondo claro
- **Negro Rico**: `#1A1A1A` - Fondo oscuro

### Colores de Personalización
- **Dorado Suave**: `#D4A574`
- **Beige Cálido**: `#E8C4A0`
- **Castaño Dorado**: `#C19A6B`
- **Tierra Tostada**: `#B8956A`
- **Bronce Oscuro**: `#A8896C`

## Cómo Usar

### Opción 1: Puerto 8080 (Recomendado)
```bash
# Linux/Mac
python3 -m http.server 8080

# Windows (desde PowerShell)
python -m http.server 8080
```

### Opción 2: Usar script automático
```bash
# Ejecutar script de inicio
./start-server.sh

# O en Windows
start-server.bat
```

### Opción 3: Puerto personalizado
```bash
python3 -m http.server [número_de_puerto]
```

### URLs de Acceso
- **Sitio principal**: `http://localhost:8080`
- **Estado del servidor**: `http://localhost:8080/server-status.html`
- **Test de imágenes**: `http://localhost:8080/test-images.html`
- **Página de perfumes**: `http://localhost:8080/perfumes.html`
- **Página de lociones**: `http://localhost:8080/lociones.html`
- **Página de maquillaje**: `http://localhost:8080/maquillaje.html`
- **Página de skincare**: `http://localhost:8080/skincare.html`

### Funcionalidades del Sitio
1. **Limpiar archivos antiguos** (opcional, primera vez):
   ```bash
   bash cleanup-images.sh
   ```

2. **Abrir el sitio**: Simplemente abre `index.html` en tu navegador

3. **Probar imágenes**: Abre `test-images.html` para verificar que las imágenes SVG cargan correctamente

4. **Navegación**: Usa el menú superior para moverte entre secciones

5. **Efecto 3D**: Pasa el mouse sobre las imágenes de productos para ver el efecto 3D interactivo

6. **Personalización**: Completa el formulario en la sección "Personalización"

7. **Tiendas**: Haz clic en cualquier tienda para ver información detallada

8. **Contacto**: Envía mensajes a través del formulario de contacto

## 📱 Secciones del Sitio

1. **Hero**: Imagen principal con llamada a la acción
2. **Sobre Nosotros**: Historia y valores de la marca
3. **Productos**: Catálogo de perfumes, lociones, maquillaje y cuidado
4. **Personalización**: Formulario para solicitar productos personalizados
5. **Tiendas**: Ubicaciones en ciudades de lujo alrededor del mundo
6. **Contacto**: Formulario y datos de contacto

## Tecnologías

- **HTML5**: Estructura semántica
- **CSS3**: Diseño responsive con Flexbox y Grid
- **JavaScript (Vanilla)**: Interactividad sin dependencias
- **Google Fonts**: Playfair Display y Montserrat

## Funcionalidades JavaScript

- Menú responsive con hamburguesa
- Menú desplegable para productos
- Scroll suave entre secciones
- Validación de formularios
- Sistema de notificaciones
- Animaciones al hacer scroll
- Navegación activa según sección visible
- **Efecto 3D Interactivo**: 
  - Rotación de imágenes según posición del mouse (±15°)
  - Sombras dinámicas que se adaptan a la inclinación
  - Efecto de brillo que sigue el cursor
  - Parallax effect en las tarjetas
  - Transiciones suaves con cubic-bezier

## Personalización

Para personalizar el sitio:

1. **Colores**: Modifica las variables CSS en `:root` en `styles.css`
2. **Tipografía**: Cambia las fuentes en Google Fonts y actualiza variables
3. **Contenido**: Edita el texto directamente en `index.html`
4. **Imágenes**: Reemplaza las imágenes SVG en `assets/images/`

## Compatibilidad

- Chrome/Edge (últimas versiones)
- Firefox (últimas versiones)
- Safari (últimas versiones)
- Responsive: Mobile, Tablet, Desktop

## Contacto

Para consultas sobre la implementación del sitio web:
- Email: info@essenza.com
- Teléfono: +39 02 xxxx xxxx

---

**ESSENZA** - *Bellezza Italiana*  
© 2025 Todos los derechos reservados