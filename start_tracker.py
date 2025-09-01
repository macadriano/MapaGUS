#!/usr/bin/env python3
"""
Script de inicio simple para el Rastreador de Vehículos
"""

from vehicle_tracker import VehicleTracker, run_server
import sys

def main():
    print("=== Rastreador de Vehículos ===")
    print("1. Modo local (archivo HTML)")
    print("2. Modo servidor web")
    
    choice = input("Seleccione el modo (1 o 2): ").strip()
    
    if choice == "1":
        print("\nIniciando en modo local...")
        tracker = VehicleTracker()
        tracker.start_tracking()
    elif choice == "2":
        print("\nIniciando servidor web...")
        print("El mapa estará disponible en: http://localhost:5000")
        run_server()
    else:
        print("Opción no válida")
        sys.exit(1)

if __name__ == "__main__":
    main()
