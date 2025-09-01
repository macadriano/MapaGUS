#!/bin/bash

echo "Instalando Rastreador de Vehículos..."
echo

echo "Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 no está instalado"
    echo "Por favor instala Python desde https://python.org"
    exit 1
fi

python3 --version

echo
echo "Instalando dependencias..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "ERROR: Error al instalar dependencias"
    exit 1
fi

echo
echo "Instalación completada exitosamente!"
echo
echo "Para ejecutar el rastreador:"
echo "  python3 start_tracker.py"
echo
echo "O directamente:"
echo "  python3 vehicle_tracker.py --server"
echo
