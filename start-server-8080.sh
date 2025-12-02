#!/bin/bash
# Inicio persistente del servidor Essenza en 8080 usando nohup
# Uso: ./start-server-8080.sh  (o ESSENZA_PORT=8090 ./start-server-8080.sh)

PORT="${ESSENZA_PORT:-8080}"
LOG="server_${PORT}.log"

if command -v lsof >/dev/null 2>&1; then
  if lsof -Pi :"${PORT}" -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "[WARN] Puerto ${PORT} ocupado. Abortando."
    exit 1
  fi
fi

if [ -f serve.py ]; then
  echo "[INFO] Lanzando serve.py en puerto ${PORT} (background)"
  ESSENZA_PORT="${PORT}" nohup python3 serve.py > "${LOG}" 2>&1 &
else
  echo "[INFO] Lanzando http.server en puerto ${PORT} (background)"
  nohup python3 -m http.server "${PORT}" > "${LOG}" 2>&1 &
fi

PID=$!
echo "[OK] Servidor iniciado PID=${PID}"
echo "[LOG] Revisa salida en ${LOG}"
echo "[URL] http://localhost:${PORT}"

echo "Para detener: kill ${PID}"