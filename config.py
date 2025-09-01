# Configuración del Rastreador de Vehículos

# Archivo CSV con las posiciones
CSV_FILE = 'positions_log.csv'

# Intervalo de actualización en segundos
UPDATE_INTERVAL = 20

# Configuración del servidor web
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000

# Configuración del mapa
MAP_ZOOM_START = 12
MAP_TILES = 'OpenStreetMap'

# Configuración de capas de Google
GOOGLE_SATELLITE_URL = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}'
GOOGLE_STREETS_URL = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}'
GOOGLE_TERRAIN_URL = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}'

# Configuración de iconos
VEHICLE_ICON = 'car'
VEHICLE_COLOR = 'red'
VEHICLE_ICON_COLOR = 'white'

# Configuración de logging
LOG_LEVEL = 'INFO'
