# 🎮 Juego del Laberinto - El Aventurero

Un emocionante juego de laberinto donde debes guiar a un personaje desde el inicio hasta la meta, evitando las paredes y optimizando tu ruta.

## 🎯 Características del Juego

### ✨ **Funcionalidades Principales:**
- **Laberinto generado aleatoriamente** cada vez que juegas
- **Múltiples controles**: Teclado, mouse y touch
- **Sistema de puntuación** con bonificaciones por tiempo y eficiencia
- **Interfaz responsive** para PC y móviles
- **Diseño moderno** con gradientes y efectos visuales

### 🎮 **Mecánicas de Juego:**
- **Objetivo**: Llevar al personaje rojo (🔴) hasta la meta verde (🟢)
- **Obstáculos**: Paredes del laberinto que bloquean el paso
- **Puntuación**: Base de 100 puntos + bonificaciones
- **Dificultad**: Laberinto único cada partida

## 🚀 Cómo Jugar

### **Controles Disponibles:**

#### ⌨️ **Teclado:**
- **Flechas**: ↑ ↓ ← → para movimiento
- **WASD**: W (arriba), S (abajo), A (izquierda), D (derecha)

#### 🖱️ **Mouse:**
- **Click**: Hacer click en cualquier parte del canvas para mover hacia esa dirección

#### 📱 **Touch (Móviles):**
- **Toque**: Tocar la pantalla para mover hacia esa ubicación

### **Sistema de Puntuación:**

| Acción | Puntos |
|--------|--------|
| Completar laberinto | +100 |
| Bonus por tiempo rápido | +0 a +600 |
| Bonus por movimientos eficientes | +0 a +500 |
| **Total máximo** | **+1200** |

### **Cálculo de Puntuación:**
```javascript
Puntuación = 100 + Bonus_Tiempo + Bonus_Movimientos

Bonus_Tiempo = (300 - segundos_usados) × 2
Bonus_Movimientos = (100 - movimientos_usados) × 5
```

## 🛠️ Tecnologías Utilizadas

- **HTML5 Canvas** para el renderizado del juego
- **JavaScript ES6+** con programación orientada a objetos
- **CSS3** con gradientes, sombras y animaciones
- **Algoritmo Recursive Backtracking** para generación de laberintos
- **Responsive Design** para múltiples dispositivos

## 📁 Estructura del Proyecto

```
maze_game.html          # Juego completo (HTML + CSS + JavaScript)
README_MAZE_GAME.md     # Esta documentación
```

## 🎲 Algoritmo del Laberinto

El juego utiliza el algoritmo **Recursive Backtracking** para generar laberintos únicos:

1. **Inicialización**: Crear una cuadrícula llena de paredes
2. **Selección de inicio**: Comenzar en la celda (1,1)
3. **Recursión**: Para cada celda:
   - Marcar como visitada
   - Mezclar direcciones aleatoriamente
   - Intentar excavar en cada dirección
   - Si es posible, continuar recursivamente
4. **Finalización**: Asegurar que inicio y meta estén libres

### **Ventajas del Algoritmo:**
- ✅ **Garantiza solución**: Siempre hay un camino válido
- ✅ **Laberintos únicos**: Cada partida es diferente
- ✅ **Eficiente**: Generación rápida incluso en laberintos grandes
- ✅ **Balanceado**: Dificultad consistente entre partidas

## 🎨 Personalización

### **Cambiar Colores:**
```css
/* Personaje */
this.ctx.fillStyle = '#e74c3c';  // Rojo actual

/* Meta */
this.ctx.fillStyle = '#27ae60';  // Verde actual

/* Paredes */
this.ctx.fillStyle = '#2c3e50';  // Azul oscuro actual
```

### **Cambiar Tamaño:**
```javascript
this.cellSize = 20;  // Tamaño de celda actual
this.cols = 30;      // Columnas (600/20)
this.rows = 20;      // Filas (400/20)
```

### **Modificar Dificultad:**
```javascript
// Laberinto más grande = más difícil
this.canvas.width = 800;   // Más ancho
this.canvas.height = 600;  // Más alto
```

## 🔧 Instalación y Uso

### **Requisitos:**
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- No requiere instalación de software adicional

### **Ejecutar:**
1. Descargar `maze_game.html`
2. Abrir con cualquier navegador web
3. ¡Jugar inmediatamente!

### **Desplegar en Web:**
1. Subir `maze_game.html` a tu servidor web
2. Acceder desde cualquier dispositivo
3. El juego funciona offline una vez cargado

## 📱 Compatibilidad

### **Navegadores Soportados:**
- ✅ Chrome 60+
- ✅ Firefox 55+
- ✅ Safari 12+
- ✅ Edge 79+
- ✅ Opera 47+

### **Dispositivos:**
- ✅ **PC/Desktop**: Teclado + mouse
- ✅ **Tablets**: Touch + teclado virtual
- ✅ **Móviles**: Touch optimizado
- ✅ **Smart TVs**: Control remoto (navegación básica)

## 🎯 Consejos para Jugar

### **Estrategias:**
1. **Planifica tu ruta** antes de moverte
2. **Evita movimientos innecesarios** para maximizar puntuación
3. **Mantén la calma** - cada segundo cuenta
4. **Practica** - la experiencia mejora tu rendimiento

### **Optimización de Puntuación:**
- **Tiempo**: Completar en menos de 2 minutos para bonus máximo
- **Movimientos**: Usar menos de 50 movimientos para bonus máximo
- **Eficiencia**: Encontrar la ruta más directa

## 🐛 Solución de Problemas

### **Problemas Comunes:**

#### **El juego no responde:**
- Verificar que JavaScript esté habilitado
- Recargar la página
- Usar navegador actualizado

#### **Controles no funcionan:**
- Verificar que el canvas esté enfocado
- Probar diferentes métodos de control
- Reiniciar el juego

#### **Rendimiento lento:**
- Cerrar otras pestañas del navegador
- Verificar que el hardware sea compatible
- Usar navegador optimizado

## 🚀 Futuras Mejoras

### **Características Planificadas:**
- [ ] **Múltiples niveles** de dificultad
- [ ] **Power-ups** y elementos especiales
- [ ] **Modo multijugador** local
- [ ] **Sistema de vidas** y reinicio automático
- [ ] **Guardado de récords** en localStorage
- [ ] **Temas visuales** personalizables
- [ ] **Efectos de sonido** y música
- [ ] **Modo oscuro** automático

### **Mejoras Técnicas:**
- [ ] **WebGL** para renderizado 3D
- [ ] **Service Worker** para funcionamiento offline
- [ ] **PWA** (Progressive Web App)
- [ ] **API de Gamepad** para controles de consola

## 📄 Licencia

Este juego es de código abierto y está disponible bajo la licencia MIT. Puedes:
- ✅ Usar libremente para fines personales
- ✅ Modificar y distribuir
- ✅ Usar en proyectos comerciales
- ✅ Incluir en aplicaciones educativas

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Puedes:
- 🐛 Reportar bugs
- 💡 Sugerir nuevas características
- 🔧 Enviar mejoras de código
- 📖 Mejorar la documentación
- 🎨 Crear nuevos temas visuales

## 📞 Soporte

Para soporte o preguntas:
- Crear un issue en el repositorio
- Contactar al desarrollador
- Consultar la documentación

---

**¡Disfruta del juego y buena suerte en el laberinto! 🎮✨**
