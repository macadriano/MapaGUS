#!/usr/bin/env python3
"""
Script de prueba para verificar las capas de mapa de Google
"""

import folium
import webbrowser
import os

def test_google_layers():
    """Prueba las diferentes capas de Google"""
    
    # Coordenadas de ejemplo (Buenos Aires)
    center = [-34.6037, -58.3816]
    
    # Crear mapa base
    m = folium.Map(
        location=center,
        zoom_start=12,
        tiles='OpenStreetMap'
    )
    
    # Agregar capa de satélite de Google
    folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr='Google Satellite',
        name='Satélite Google',
        overlay=False
    ).add_to(m)
    
    # Agregar capa de calles de Google
    folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr='Google Streets',
        name='Calles Google',
        overlay=False
    ).add_to(m)
    
    # Agregar capa de terreno de Google
    folium.TileLayer(
        tiles='https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
        attr='Google Terrain',
        name='Terreno Google',
        overlay=False
    ).add_to(m)
    
    # Agregar marcador de prueba
    folium.Marker(
        location=center,
        popup='Punto de prueba - Buenos Aires',
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)
    
    # Agregar control de capas
    folium.LayerControl().add_to(m)
    
    # Guardar mapa
    filename = 'test_layers.html'
    m.save(filename)
    
    print(f"Mapa de prueba guardado como {filename}")
    print("Abriendo en el navegador...")
    
    # Abrir en navegador
    webbrowser.open('file://' + os.path.abspath(filename))
    
    return m

if __name__ == "__main__":
    print("Probando capas de Google...")
    test_google_layers()
    print("Prueba completada!")
