#!/usr/bin/env python3
"""
Servidor estático robusto para Essenza.
Incluye:
- Cabeceras cache control mínimas.
- Manejo de MIME types extendido.
- Listado de directorios limpio (opcional).
- Log mejorado.
Usar cuando http.server simple falle en entorno integrado.
"""
import http.server
import socketserver
import mimetypes
import os
import sys
from datetime import datetime

PORT = int(os.environ.get("ESSENZA_PORT", "8080"))
ROOT = os.path.abspath(os.environ.get("ESSENZA_ROOT", "."))

EXTRA_TYPES = {
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".svg": "image/svg+xml; charset=utf-8",
    ".html": "text/html; charset=utf-8",
    ".woff": "font/woff",
    ".woff2": "font/woff2",
}
for ext, mt in EXTRA_TYPES.items():
    mimetypes.add_type(mt, ext, strict=False)

class StaticHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def log_message(self, format, *args):  # noqa: D401
        sys.stderr.write(f"[{datetime.now().strftime('%H:%M:%S')}] {self.address_string()} - " + format%args + "\n")

    def end_headers(self):
        # Añadir cabeceras para reducir problemas caching en desarrollo
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def list_directory(self, path):
        # Listado minimalista (puedes personalizar o desactivar)
        try:
            entries = os.listdir(path)
        except OSError:
            self.send_error(404, "No se puede listar el directorio")
            return None
        entries.sort(key=lambda e: e.lower())
        out = ["<html><head><title>Índice</title><meta charset='utf-8'>",
               "<style>body{font-family:Arial;padding:30px;background:#F7F4EF;color:#44231D;}a{color:#6F1A17;text-decoration:none;}a:hover{text-decoration:underline;}li{margin:4px 0;}h1{font-size:1.4rem;margin-bottom:1rem;}footer{margin-top:2rem;font-size:.75rem;color:#44231D;opacity:.7}</style>",
               "</head><body>",
               f"<h1>Índice de {os.path.relpath(path, ROOT) or '/'} </h1>",
               "<ul>"]
        for e in entries:
            full = os.path.join(path, e)
            disp = e + ("/" if os.path.isdir(full) else "")
            out.append(f"<li><a href='{disp}'>{disp}</a></li>")
        out.extend(["</ul>", "<footer>Essenza Static Server</footer>", "</body></html>"])
        encoded = "".join(out).encode("utf-8", "surrogateescape")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)
        return None

if __name__ == "__main__":
    os.chdir(ROOT)
    print("\n============================")
    print(" ESSENZA STATIC SERVER ")
    print("============================")
    print(f"📁 Raíz: {ROOT}")
    print(f"🌐 Puerto: {PORT}")
    print("🔗 URL: http://localhost:" + str(PORT))
    print("Presiona Ctrl+C para detener.\n")
    try:
        with socketserver.TCPServer(("", PORT), StaticHandler) as httpd:
            httpd.serve_forever()
    except OSError as e:
        print(f"Error al iniciar servidor: {e}")
        print("Sugerencias: \n- Verifica si el puerto está ocupado (lsof -i :8080).\n- Cambia el puerto: ESSENZA_PORT=8090 python3 serve.py")
        sys.exit(1)
