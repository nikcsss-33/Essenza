#!/usr/bin/env python3
"""
Script para actualizar todas las páginas de tiendas con estética editorial Essenza
"""

import os
import re
from pathlib import Path

def update_store_page(filepath):
    """Actualiza una página de tienda con la estética editorial"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. Eliminar Google Fonts import
        content = re.sub(
            r'<link[^>]*fonts\.googleapis\.com[^>]*>\s*',
            '',
            content,
            flags=re.IGNORECASE
        )
        content = re.sub(
            r'<link rel="preconnect"[^>]*>\s*',
            '',
            content
        )
        
        # 2. Añadir Elephant Pro override justo después del styles.css
        if '<style>' not in content and "* { font-family: 'Elephant'" not in content:
            content = content.replace(
                '<link rel="stylesheet" href="../styles.css">',
                '<link rel="stylesheet" href="../styles.css">\n    <style>\n        * { font-family: \'Elephant\', serif !important; }\n    </style>'
            )
        
        # 3. Actualizar hero gradientes a color sólido
        content = re.sub(
            r'background:\s*linear-gradient\(135deg,\s*#790000[^)]+\)',
            'background: #790000',
            content
        )
        
        # 4. Actualizar padding del hero
        content = re.sub(
            r'(class="hero"[^>]*style="[^"]*?)padding:\s*4rem\s+0',
            r'\1padding: 100px 60px',
            content
        )
        
        # 5. Actualizar padding de secciones about
        content = re.sub(
            r'(class="about"[^>]*style="[^"]*?)padding:\s*4rem\s+0',
            r'\1padding: 100px 0',
            content
        )
        
        # 6. Actualizar colores de fondo
        content = content.replace('#FAF8F5', '#FFFAF7')
        content = content.replace('#F0EBE3', '#FCE4C8')
        
        # 7. Actualizar border-radius a flat (eliminar)
        content = re.sub(r'border-radius:\s*8px;?\s*', '', content)
        
        # 8. Actualizar cajas con gradiente a color sólido con borde
        content = re.sub(
            r'background:\s*linear-gradient\([^)]+\);\s*padding:\s*2rem;[^"]*border-radius:\s*8px;',
            'background: #FCE4C8; padding: 2.5rem; border-left: 4px solid #790000;',
            content
        )
        content = re.sub(
            r'background:\s*linear-gradient\([^)]+\);\s*padding:\s*2rem;',
            'background: #FCE4C8; padding: 2.5rem; border-left: 4px solid #790000;',
            content
        )
        
        # 9. Actualizar colores de texto
        content = content.replace('color: #2C2C2C', 'color: #501010')
        content = content.replace('color: #6B6B6B', 'color: #501010')
        content = content.replace('var(--color-text-muted)', '#501010')
        
        # 10. Añadir líneas doradas al hero si no existen
        if 'hero-title' in content and 'position: relative; width: 100%; height: 8px' not in content:
            # Buscar el hero-content y añadir líneas
            hero_pattern = r'(<div class="hero-content"[^>]*>)\s*(<h2 class="hero-title">)'
            if re.search(hero_pattern, content):
                golden_line_top = '''
            <div style="position: relative; width: 100%; height: 8px; margin: 0 auto 2.5rem;">
                <div style="position: absolute; top: 0; left: 0; width: 100%; height: 1px; background: #FFE88C;"></div>
                <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 3px; background: #B47532;"></div>
            </div>
            '''
                content = re.sub(hero_pattern, r'\1' + golden_line_top + r'\2', content)
            
            # Añadir línea después del título
            title_pattern = r'(</h2>)\s*(<p class="hero-subtitle">)'
            if re.search(title_pattern, content):
                golden_line_middle = '''
            <div style="position: relative; width: 100%; height: 8px; margin: 1.5rem auto;">
                <div style="position: absolute; top: 0; left: 0; width: 100%; height: 1px; background: #FFE88C;"></div>
                <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 3px; background: #B47532;"></div>
            </div>
            '''
                content = re.sub(title_pattern, r'\1' + golden_line_middle + r'\2', content)
        
        # Solo escribir si hubo cambios
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error procesando {filepath}: {e}")
        return False

def main():
    # Directorio de tiendas
    stores_dir = Path('/workspaces/Essenza/tiendas')
    
    if not stores_dir.exists():
        print(f"Directorio no encontrado: {stores_dir}")
        return
    
    # Encontrar todos los archivos HTML
    html_files = list(stores_dir.glob('**/*.html'))
    
    print(f"Encontrados {len(html_files)} archivos HTML en tiendas/")
    print("Actualizando páginas con estética editorial...\n")
    
    updated = 0
    for html_file in html_files:
        relative_path = html_file.relative_to('/workspaces/Essenza')
        if update_store_page(html_file):
            print(f"✓ Actualizado: {relative_path}")
            updated += 1
        else:
            print(f"○ Sin cambios: {relative_path}")
    
    print(f"\n{'='*60}")
    print(f"Completado: {updated}/{len(html_files)} páginas actualizadas")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
