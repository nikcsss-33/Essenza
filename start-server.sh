#!/bin/bash
# Start Essenza static server (enhanced) on port 8080
# Características añadidas:
# - Chequeo de puerto en uso
# - Fallback a servidor robusto serve.py
# - Mensajes claros y colores
# - Opción de cambiar puerto: ESSENZA_PORT=8090 ./start-server.sh

PORT="${ESSENZA_PORT:-8080}"
ROOT_DIR="$(pwd)"

RED="\033[0;31m"; GREEN="\033[0;32m"; YELLOW="\033[1;33m"; CYAN="\033[0;36m"; RESET="\033[0m"

echo -e "${CYAN}==============================${RESET}"
echo -e "${CYAN}  ESSENZA STATIC SERVER${RESET}"
echo -e "${CYAN}==============================${RESET}"
echo -e "📁 Directorio: ${ROOT_DIR}"
echo -e "🌐 Puerto: ${PORT}"
echo -e "🔗 URL: http://localhost:${PORT}"
echo -e ""

# Comprobar si el puerto está ocupado
if command -v lsof >/dev/null 2>&1; then
	if lsof -Pi :"${PORT}" -sTCP:LISTEN -t >/dev/null 2>&1; then
		PID="$(lsof -Pi :"${PORT}" -sTCP:LISTEN -t | head -n1)"
		echo -e "${YELLOW}⚠ El puerto ${PORT} está en uso por PID ${PID}.${RESET}"
		echo -e "${YELLOW}Intentando terminar proceso...${RESET}"
		if kill "${PID}" >/dev/null 2>&1; then
			echo -e "${GREEN}✔ Proceso ${PID} terminado.${RESET}"
		else
			echo -e "${RED}✖ No se pudo terminar el proceso. Ejecuta manualmente: kill ${PID}${RESET}"
			echo -e "${RED}Abortando inicio para evitar conflicto.${RESET}"
			exit 1
		fi
		sleep 1
	fi
else
	echo -e "${YELLOW}lsof no disponible, omitiendo chequeo de puerto.${RESET}"
fi

echo -e "${CYAN}Iniciando servidor...${RESET}"
echo -e "(Ctrl+C para detener)\n"

# Preferir servidor robusto si existe serve.py
if [ -f "serve.py" ]; then
	echo -e "${GREEN}Usando servidor robusto: serve.py${RESET}"
	exec python3 serve.py
else
	echo -e "${YELLOW}Fallback a: python3 -m http.server ${PORT}${RESET}"
	exec python3 -m http.server "${PORT}"
fi
