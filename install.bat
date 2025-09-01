@echo off
echo Instalando Rastreador de Vehículos...
echo.

echo Verificando Python...
python --version
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en el PATH
    echo Por favor instala Python desde https://python.org
    pause
    exit /b 1
)

echo.
echo Instalando dependencias...
pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: Error al instalar dependencias
    pause
    exit /b 1
)

echo.
echo Instalación completada exitosamente!
echo.
echo Para ejecutar el rastreador:
echo   python start_tracker.py
echo.
echo O directamente:
echo   python vehicle_tracker.py --server
echo.
pause
