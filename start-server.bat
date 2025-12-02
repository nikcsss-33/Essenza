@echo off
echo ========================================
echo    ESSENZA - Servidor Web de Lujo
echo ========================================
echo.
echo Iniciando servidor en puerto 8080...
echo.
echo URL de acceso: http://localhost:8080
echo.
echo Presiona Ctrl+C para detener el servidor
echo.
python3 -m http.server 8080
pause