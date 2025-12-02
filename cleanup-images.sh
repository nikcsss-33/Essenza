cd /workspaces/Essenza/assets/images
rm -f *.svg *.jpg *.jpeg *.png
ls -la#!/bin/bash
# Script para ELIMINAR TODAS las imágenes del proyecto

echo "🗑️  Eliminando TODAS las imágenes..."

cd /workspaces/Essenza/assets/images

# Eliminar TODOS los archivos de imágenes
rm -f *.svg *.jpg *.jpeg *.png

echo "Todas las imágenes eliminadas"
echo ""
echo "📁 Archivos restantes:"
ls -lh

echo ""
echo "Todas las imágenes han sido eliminadas."
