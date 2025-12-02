#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = "/workspaces/Essenza"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

os.chdir(DIRECTORY)

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"🌐 Servidor Essenza iniciado en puerto {PORT}")
    print(f"📁 Sirviendo archivos desde: {DIRECTORY}")
    print(f"🔗 Abre tu navegador en: http://localhost:{PORT}")
    print("\nPresiona Ctrl+C para detener el servidor\n")
    httpd.serve_forever()
