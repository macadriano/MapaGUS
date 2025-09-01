# Rastreador de Vehículos con Folium

Un sistema simple para mostrar vehículos en un mapa en tiempo real usando Folium y Python.

## Características

- ✅ Muestra vehículos en un mapa interactivo
- ✅ Iconos de vehículos con tooltips informativos
- ✅ Labels con ID del equipo GPS
- ✅ Actualización automática cada 20 segundos (configurable)
- ✅ Soporte para múltiples vehículos
- ✅ Modo local (archivo HTML) y servidor web
- ✅ API REST para obtener datos de vehículos

## Instalación

### 1. Requisitos del Sistema

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### 2. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3. Verificar Instalación

```bash
python -c "import folium, pandas, flask; print('Todas las dependencias instaladas correctamente')"
```

## Uso

### Modo Local (Archivo HTML)

```bash
python vehicle_tracker.py
```

Este modo:
- Lee el archivo `positions_log.csv`
- Actualiza el mapa cada 20 segundos
- Abre automáticamente el navegador con el mapa
- Guarda el mapa como `vehicle_map.html`

### Modo Servidor Web

```bash
python vehicle_tracker.py --server
```

Este modo:
- Inicia un servidor web en `http://localhost:5000`
- Permite acceso desde cualquier dispositivo en la red
- Actualiza el mapa en tiempo real

### Opciones de Línea de Comandos

```bash
# Usar archivo CSV personalizado
python vehicle_tracker.py --csv mi_archivo.csv

# Cambiar intervalo de actualización (en segundos)
python vehicle_tracker.py --interval 30

# Ejecutar como servidor con host y puerto personalizados
python vehicle_tracker.py --server --host 192.168.1.100 --port 8080
```

### Script de Inicio Simple

```bash
python start_tracker.py
```

Este script te permite elegir entre modo local o servidor web de forma interactiva.

## Estructura del Archivo CSV

El archivo `positions_log.csv` debe tener la siguiente estructura:

```csv
ID,LATITUD,LONGITUD,RUMBO,VELOCIDAD,FECHAGPS,FECHARECIBIDO
001,-34.6037,-58.3816,90,45,2024-01-15 10:30:00,2024-01-15 10:30:05
002,-34.6040,-58.3820,180,30,2024-01-15 10:30:00,2024-01-15 10:30:05
```

### Campos Requeridos:

- **ID**: Identificador único del vehículo/equipo GPS
- **LATITUD**: Latitud en formato decimal (ej: -34.6037)
- **LONGITUD**: Longitud en formato decimal (ej: -58.3816)
- **RUMBO**: Dirección en grados (0-360)
- **VELOCIDAD**: Velocidad en km/h
- **FECHAGPS**: Fecha y hora del GPS
- **FECHARECIBIDO**: Fecha y hora de recepción

## Configuración

Puedes modificar la configuración editando el archivo `config.py`:

```python
# Intervalo de actualización en segundos
UPDATE_INTERVAL = 20

# Puerto del servidor web
SERVER_PORT = 5000

# Configuración del mapa
MAP_ZOOM_START = 12
```

## Publicación en Producción

### Opción 1: Servidor Local

```bash
# Ejecutar en segundo plano
nohup python vehicle_tracker.py --server --host 0.0.0.0 --port 5000 &

# Verificar que está ejecutándose
ps aux | grep vehicle_tracker
```

### Opción 2: Docker (Recomendado)

Crear un `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "vehicle_tracker.py", "--server", "--host", "0.0.0.0", "--port", "5000"]
```

Construir y ejecutar:

```bash
docker build -t vehicle-tracker .
docker run -d -p 5000:5000 -v $(pwd):/app vehicle-tracker
```

### Opción 3: Servidor Web (Apache/Nginx)

1. **Configurar Apache con mod_wsgi:**

```apache
<VirtualHost *:80>
    ServerName tu-dominio.com
    
    WSGIDaemonProcess vehicle-tracker python-path=/ruta/a/tu/app
    WSGIProcessGroup vehicle-tracker
    WSGIScriptAlias / /ruta/a/tu/app/vehicle_tracker.py
    
    <Directory /ruta/a/tu/app>
        Require all granted
    </Directory>
</VirtualHost>
```

2. **Configurar Nginx como proxy:**

```nginx
server {
    listen 80;
    server_name tu-dominio.com;
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Opción 4: Servicios en la Nube

#### Heroku

1. Crear `Procfile`:
```
web: python vehicle_tracker.py --server --host 0.0.0.0 --port $PORT
```

2. Desplegar:
```bash
heroku create mi-rastreador
git push heroku main
```

#### Google Cloud Platform

1. Crear `app.yaml`:
```yaml
runtime: python39
entrypoint: python vehicle_tracker.py --server --host 0.0.0.0 --port $PORT

env_variables:
  PORT: 8080
```

2. Desplegar:
```bash
gcloud app deploy
```

## API REST

El servidor web incluye endpoints API:

### Obtener datos de vehículos

```bash
curl http://localhost:5000/api/vehicles
```

Respuesta:
```json
{
  "001": {
    "latitud": -34.6037,
    "longitud": -58.3816,
    "rumbo": 90,
    "velocidad": 45,
    "fechagps": "2024-01-15 10:30:00",
    "fecharecibido": "2024-01-15 10:30:05"
  }
}
```

## Solución de Problemas

### Error: "No module named 'folium'"

```bash
pip install folium
```

### Error: "Archivo CSV no encontrado"

Verificar que el archivo `positions_log.csv` existe en el directorio del proyecto.

### Error: "Puerto ya en uso"

Cambiar el puerto:
```bash
python vehicle_tracker.py --server --port 8080
```

### El mapa no se actualiza

Verificar que el archivo CSV tiene datos válidos y que el formato es correcto.

## Personalización

### Cambiar Iconos de Vehículos

Editar en `vehicle_tracker.py`:

```python
vehicle_icon = folium.Icon(
    icon='truck',  # Cambiar a 'car', 'motorcycle', etc.
    color='blue',  # Cambiar color
    icon_color='white'
)
```

### Agregar Más Información al Tooltip

Modificar la variable `popup_html` en el método `create_map()`.

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Soporte

Para reportar problemas o solicitar nuevas características, crear un issue en el repositorio del proyecto.
