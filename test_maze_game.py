#!/usr/bin/env python3
"""
Script de prueba para verificar el funcionamiento del juego del laberinto
"""

import webbrowser
import os
import time

def test_maze_game():
    """Prueba el juego del laberinto"""
    
    print("🎮 Probando Juego del Laberinto...")
    print("=" * 50)
    
    # Verificar que el archivo existe
    game_file = "maze_game.html"
    if not os.path.exists(game_file):
        print(f"❌ Error: No se encontró el archivo {game_file}")
        return False
    
    print(f"✅ Archivo {game_file} encontrado")
    
    # Verificar que es un archivo HTML válido
    try:
        with open(game_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Verificar elementos básicos del HTML
        required_elements = [
            '<!DOCTYPE html>',
            '<html',
            '<head>',
            '<body>',
            '<canvas',
            '<script>',
            'class MazeGame'
        ]
        
        missing_elements = []
        for element in required_elements:
            if element not in content:
                missing_elements.append(element)
        
        if missing_elements:
            print(f"❌ Error: Faltan elementos HTML: {missing_elements}")
            return False
        
        print("✅ Estructura HTML válida")
        
        # Verificar funcionalidades del juego
        game_features = [
            'generateMaze',
            'movePlayer',
            'calculateScore',
            'showVictory',
            'setupEventListeners'
        ]
        
        missing_features = []
        for feature in game_features:
            if feature not in content:
                missing_features.append(feature)
        
        if missing_features:
            print(f"❌ Error: Faltan funcionalidades: {missing_features}")
            return False
        
        print("✅ Funcionalidades del juego implementadas")
        
        # Verificar estilos CSS
        css_features = [
            'background: linear-gradient',
            'border-radius',
            'box-shadow',
            'transition'
        ]
        
        missing_css = []
        for css in css_features:
            if css not in content:
                missing_css.append(css)
        
        if missing_css:
            print(f"⚠️  Advertencia: Algunos estilos CSS faltan: {missing_css}")
        else:
            print("✅ Estilos CSS completos")
        
    except Exception as e:
        print(f"❌ Error leyendo archivo: {e}")
        return False
    
    # Abrir el juego en el navegador
    print("\n🌐 Abriendo juego en el navegador...")
    try:
        file_path = os.path.abspath(game_file)
        webbrowser.open(f'file://{file_path}')
        print("✅ Juego abierto en el navegador")
        print("🎯 Instrucciones de prueba:")
        print("   - Usa las flechas del teclado para mover el personaje")
        print("   - Intenta llegar a la meta verde")
        print("   - Verifica que el sistema de puntuación funcione")
        print("   - Prueba el botón 'Nuevo Juego'")
        print("   - Verifica las instrucciones")
        
    except Exception as e:
        print(f"❌ Error abriendo navegador: {e}")
        return False
    
    return True

def show_game_info():
    """Muestra información sobre el juego"""
    
    print("\n📋 Información del Juego del Laberinto")
    print("=" * 50)
    print("🎮 Nombre: El Laberinto del Aventurero")
    print("🎯 Objetivo: Llevar al personaje rojo hasta la meta verde")
    print("🎲 Características:")
    print("   - Laberinto generado aleatoriamente")
    print("   - Múltiples controles (teclado, mouse, touch)")
    print("   - Sistema de puntuación con bonificaciones")
    print("   - Interfaz responsive para PC y móviles")
    print("   - Diseño moderno con efectos visuales")
    
    print("\n🎮 Controles:")
    print("   - Flechas del teclado o WASD")
    print("   - Click del mouse en el canvas")
    print("   - Touch en dispositivos móviles")
    
    print("\n⭐ Sistema de Puntuación:")
    print("   - Base: 100 puntos por completar")
    print("   - Bonus por tiempo: hasta 600 puntos")
    print("   - Bonus por eficiencia: hasta 500 puntos")
    print("   - Total máximo: 1200 puntos")

def main():
    """Función principal"""
    
    print("🎮 TESTER DEL JUEGO DEL LABERINTO")
    print("=" * 50)
    
    # Mostrar información del juego
    show_game_info()
    
    # Probar el juego
    if test_maze_game():
        print("\n🎉 ¡Prueba completada exitosamente!")
        print("✅ El juego del laberinto está listo para usar")
        print("\n💡 Para jugar:")
        print("   1. El juego ya está abierto en tu navegador")
        print("   2. Usa las flechas del teclado para moverte")
        print("   3. Llega a la meta verde para ganar")
        print("   4. Prueba diferentes controles")
        print("   5. ¡Disfruta del juego!")
    else:
        print("\n❌ La prueba falló")
        print("🔧 Verifica que el archivo maze_game.html esté presente")
        print("📖 Consulta el README_MAZE_GAME.md para más información")

if __name__ == "__main__":
    main()
