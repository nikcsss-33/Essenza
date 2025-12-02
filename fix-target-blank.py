#!/usr/bin/env python3
import re

# Leer el archivo
with open('/workspaces/Essenza/mas-tiendas.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Reemplazar todos los target="_blank"
content = content.replace(' target="_blank"', '')

# Escribir el archivo
with open('/workspaces/Essenza/mas-tiendas.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Todos los enlaces corregidos en mas-tiendas.html")
