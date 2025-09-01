import pandas as pd
import folium
from folium import plugins
import time
import threading
import webbrowser
import os
from datetime import datetime
import json
from flask import Flask, render_template_string, jsonify
import logging

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VehicleTracker:
    def __init__(self, csv_file='positions_log.csv', update_interval=20):
        """
        Inicializa el rastreador de vehículos
        
        Args:
            csv_file (str): Ruta al archivo CSV con las posiciones
            update_interval (int): Intervalo de actualización en segundos
        """
        self.csv_file = csv_file
        self.update_interval = update_interval
        self.vehicles = {}
        self.map_center = [0, 0]  # Centro inicial del mapa
        self.is_running = False
        
    def read_latest_positions(self):
        """
        Lee las últimas posiciones de cada vehículo desde el CSV
        """
        try:
            if not os.path.exists(self.csv_file):
                logger.warning(f"Archivo {self.csv_file} no encontrado")
                return {}
            
            # Leer el CSV
            df = pd.read_csv(self.csv_file)
            
            if df.empty:
                logger.info("CSV vacío, no hay datos para mostrar")
                return {}
            
            # Obtener la última posición de cada ID
            latest_positions = {}
            for vehicle_id in df['ID'].unique():
                vehicle_data = df[df['ID'] == vehicle_id].iloc[-1]
                latest_positions[vehicle_id] = {
                    'latitud': float(vehicle_data['LATITUD']),
                    'longitud': float(vehicle_data['LONGITUD']),
                    'rumbo': float(vehicle_data['RUMBO']),
                    'velocidad': float(vehicle_data['VELOCIDAD']),
                    'fechagps': vehicle_data['FECHAGPS'],
                    'fecharecibido': vehicle_data['FECHARECIBIDO']
                }
            
            # Actualizar el centro del mapa si hay vehículos
            if latest_positions:
                lats = [pos['latitud'] for pos in latest_positions.values()]
                lons = [pos['longitud'] for pos in latest_positions.values()]
                self.map_center = [sum(lats)/len(lats), sum(lons)/len(lons)]
            
            return latest_positions
            
        except Exception as e:
            logger.error(f"Error leyendo CSV: {e}")
            return {}
    
    def create_map(self, vehicles_data):
        """
        Crea el mapa con los vehículos
        
        Args:
            vehicles_data (dict): Diccionario con los datos de los vehículos
        """
        # Crear mapa centrado en la posición promedio
        m = folium.Map(
            location=self.map_center,
            zoom_start=12,
            tiles='OpenStreetMap'
        )
        
        # Agregar cada vehículo al mapa
        for vehicle_id, data in vehicles_data.items():
            # Crear icono personalizado para el vehículo
            vehicle_icon = folium.Icon(
                icon='car',
                color='red',
                icon_color='white'
            )
            
            # Crear popup con información del vehículo
            popup_html = f"""
            <div style="font-family: Arial, sans-serif; min-width: 200px;">
                <h4>Vehículo {vehicle_id}</h4>
                <p><strong>Latitud:</strong> {data['latitud']:.6f}</p>
                <p><strong>Longitud:</strong> {data['longitud']:.6f}</p>
                <p><strong>Rumbo:</strong> {data['rumbo']}°</p>
                <p><strong>Velocidad:</strong> {data['velocidad']} km/h</p>
                <p><strong>Fecha GPS:</strong> {data['fechagps']}</p>
                <p><strong>Fecha Recibido:</strong> {data['fecharecibido']}</p>
            </div>
            """
            
            # Agregar marcador al mapa
            folium.Marker(
                location=[data['latitud'], data['longitud']],
                popup=folium.Popup(popup_html, max_width=300),
                icon=vehicle_icon,
                tooltip=f"Vehículo {vehicle_id}"
            ).add_to(m)
            
            # Agregar label con el ID del vehículo
            folium.map.Marker(
                location=[data['latitud'], data['longitud']],
                icon=folium.DivIcon(
                    html=f'<div style="background-color: white; border: 2px solid black; padding: 2px 6px; border-radius: 3px; font-weight: bold; font-size: 12px;">{vehicle_id}</div>',
                    icon_size=(100, 20),
                    icon_anchor=(50, 10)
                )
            ).add_to(m)
        
        # Agregar control de capas
        folium.LayerControl().add_to(m)
        
        # Agregar escala
        folium.plugins.MousePosition().add_to(m)
        
        return m
    
    def save_map(self, map_obj, filename='vehicle_map.html'):
        """
        Guarda el mapa como archivo HTML
        
        Args:
            map_obj: Objeto del mapa de Folium
            filename (str): Nombre del archivo HTML
        """
        try:
            map_obj.save(filename)
            logger.info(f"Mapa guardado como {filename}")
        except Exception as e:
            logger.error(f"Error guardando mapa: {e}")
    
    def update_map_loop(self):
        """
        Bucle principal para actualizar el mapa
        """
        while self.is_running:
            try:
                # Leer las últimas posiciones
                vehicles_data = self.read_latest_positions()
                
                if vehicles_data:
                    # Crear y guardar el mapa
                    map_obj = self.create_map(vehicles_data)
                    self.save_map(map_obj)
                    logger.info(f"Mapa actualizado con {len(vehicles_data)} vehículos")
                else:
                    logger.info("No hay datos de vehículos para mostrar")
                
                # Esperar antes de la siguiente actualización
                time.sleep(self.update_interval)
                
            except Exception as e:
                logger.error(f"Error en el bucle de actualización: {e}")
                time.sleep(self.update_interval)
    
    def start_tracking(self):
        """
        Inicia el seguimiento de vehículos
        """
        self.is_running = True
        logger.info(f"Iniciando seguimiento con intervalo de {self.update_interval} segundos")
        
        # Crear y ejecutar el hilo de actualización
        update_thread = threading.Thread(target=self.update_map_loop)
        update_thread.daemon = True
        update_thread.start()
        
        # Abrir el mapa en el navegador
        webbrowser.open('file://' + os.path.abspath('vehicle_map.html'))
        
        try:
            while self.is_running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop_tracking()
    
    def stop_tracking(self):
        """
        Detiene el seguimiento de vehículos
        """
        self.is_running = False
        logger.info("Seguimiento detenido")

# Configuración del servidor Flask para actualizaciones en tiempo real
app = Flask(__name__)

@app.route('/')
def show_map():
    """
    Ruta principal que muestra el mapa
    """
    tracker = VehicleTracker()
    vehicles_data = tracker.read_latest_positions()
    
    if vehicles_data:
        map_obj = tracker.create_map(vehicles_data)
        return map_obj._repr_html_()
    else:
        return """
        <html>
        <head><title>Rastreador de Vehículos</title></head>
        <body>
            <h1>Rastreador de Vehículos</h1>
            <p>No hay datos de vehículos disponibles.</p>
            <p>Verifique que el archivo positions_log.csv contenga datos.</p>
        </body>
        </html>
        """

@app.route('/api/vehicles')
def get_vehicles():
    """
    API endpoint para obtener datos de vehículos en formato JSON
    """
    tracker = VehicleTracker()
    vehicles_data = tracker.read_latest_positions()
    return jsonify(vehicles_data)

def run_server(host='0.0.0.0', port=5000):
    """
    Ejecuta el servidor Flask
    
    Args:
        host (str): Host del servidor
        port (int): Puerto del servidor
    """
    logger.info(f"Iniciando servidor en http://{host}:{port}")
    app.run(host=host, port=port, debug=False)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Rastreador de Vehículos con Folium')
    parser.add_argument('--csv', default='positions_log.csv', help='Archivo CSV con las posiciones')
    parser.add_argument('--interval', type=int, default=20, help='Intervalo de actualización en segundos')
    parser.add_argument('--server', action='store_true', help='Ejecutar como servidor web')
    parser.add_argument('--host', default='0.0.0.0', help='Host del servidor')
    parser.add_argument('--port', type=int, default=5000, help='Puerto del servidor')
    
    args = parser.parse_args()
    
    if args.server:
        # Modo servidor web
        run_server(args.host, args.port)
    else:
        # Modo local con archivo HTML
        tracker = VehicleTracker(args.csv, args.interval)
        tracker.start_tracking()
