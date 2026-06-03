# 📱 Especificaciones Frontend - Simulador DevOps

## 🎯 Objetivo

Desarrollar la interfaz de usuario responsiva, intuitiva y de alto rendimiento para la plataforma Simulador DevOps, garantizando una experiencia óptima en dispositivos móviles y escritorio.

## 👥 Usuarios Objetivo

- **Desarrolladores** - Preparación técnica
- **DevOps Engineers** - Certificaciones cloud
- **QA/Testers** - Conocimiento técnico
- **Estudiantes** - Aprendizaje autodidacta
- **Educadores** - Evaluación de alumnos

## 📋 Requisitos Funcionales

### 1. Pantalla de Configuración (Setup)

#### 1.1 Selector de Cantidad de Preguntas
- **UI Components:**
  - 5 botones: 10, 25, 50, 75, 100
  - 1 slider horizontal para selección custom (5-500)
  - Display del número seleccionado en grande (25px)

- **Comportamiento:**
  - Click en botón → actualiza cantidad
  - Slider → actualiza cantidad en tiempo real
  - Solo permite 10-100 si hay menos preguntas en categoría
  - Valida contra máximo disponible

- **Ejemplo HTML:**
```html
<div class="flex flex-wrap gap-2 mb-3">
  <button onclick="app.questionsCount=10; app.render();"
    class="px-4 py-2 rounded-lg font-bold">
    10
  </button>
  <!-- 25, 50, 75, 100 -->
</div>
<input type="range" min="5" max="100" value="25"
  onchange="app.questionsCount=parseInt(this.value); app.render();">
```

#### 1.2 Selector de Categoría
- **UI Components:**
  - Dropdown/Select dinámico
  - Carga categorías desde JSON
  - Opción "Todas" por defecto
  - Muestra 26+ categorías (alfabéticas)

- **Comportamiento:**
  - Al cambiar → actualiza contador de preguntas disponibles
  - Desactiva botón "Comenzar" si no hay preguntas
  - Valida selección contra BD

- **Ejemplo HTML:**
```html
<select onchange="app.selectedCategory=this.value; app.render();"
  class="w-full px-4 py-3 rounded-lg border-2 border-purple-300">
  <option value="Todas">Todas</option>
  <option value="Java 21">Java 21</option>
  <!-- Más categorías -->
</select>
```

#### 1.3 Display de Preguntas Disponibles
- **UI Components:**
  - Card con número grande
  - Texto descriptivo
  - Icono de confirmación ✓
  - Color verde para activo

- **Actualización Dinámica:**
  - Cambia al seleccionar categoría
  - Valida contra máximo disponible
  - Desactiva si es 0

#### 1.4 Botón "Comenzar Quiz"
- **Estados:**
  - HABILITADO: Cuando hay preguntas disponibles
  - DESHABILITADO: Cuando cantidad = 0
  - HOVER: Efecto de escala 1.05
  - ACTIVO: Inicia el quiz

- **Comportamiento:**
  - Click → `app.startQuiz()`
  - Transición suave a pantalla de quiz
  - Desaparece spinner de carga

#### 1.5 Estadísticas Generales
- **Display Cards:**
  - Total de preguntas: 2,240
  - Total de categorías: 27
  - Opciones por pregunta: 4

- **Ubicación:** Inferior de setup, no se ocultará

### 2. Pantalla de Quiz (Progreso)

#### 2.1 Header
- **Logo/Título:**
  - Icono 🧠 + "Quiz en Progreso"
  - Tamaño: 24px, bold

- **Botón "Configurar":**
  - Vuelve a setup
  - Reinicia el quiz (pregunta: ¿Estás seguro?)
  - Posición: Top right
  - Color: Gris

#### 2.2 Estadísticas en Tiempo Real
- **Grid 2x2 (mobile) / 1x4 (desktop):**
  ```
  PREGUNTA: 1/25    │ RESPONDIDAS: 3
  CORRECTAS: 2      │ PROGRESO: 8%
  ```

- **Componentes:**
  - Número grande (48px)
  - Etiqueta pequeña (12px, mayúsculas)
  - Colores: Azul (pregunta), Azul (respondidas), Verde (correctas), Púrpura (progreso)
  - Se actualiza en tiempo real

#### 2.3 Barra de Progreso General
- **Características:**
  - Ancho completo
  - Alto: 4px
  - Background: Gris claro
  - Fill: Gradiente púrpura → rosa
  - Transición smooth (0.3s)
  - Muestra: "3 de 25" en texto pequeño

#### 2.4 Tarjeta de Pregunta
- **Encabezado:**
  ```
  📌 CATEGORIA │ ⭐ DIFICULTAD │ 1/25
  ```
  - Badges con background color
  - Pequeño, uppercase
  - Alineado izq-izq-derecha

- **Texto de Pregunta:**
  - Font: Bold, 20px (desktop) / 16px (mobile)
  - Color: Gris oscuro (gray-900)
  - Línea separadora gris claro
  - Padding: 20px horizontal
  - Altura mínima: 80px

#### 2.5 Opciones de Respuesta
- **Layout:** Stack vertical
- **Cada Opción:**
  ```
  ┌─────────────────────────────┐
  │ A. Texto de opción          │
  └─────────────────────────────┘
  ```

- **Estados:**
  - **SIN RESPONDER:**
    - Background: Blanco
    - Border: Gris claro, 2px
    - Hover: Border púrpura, bg púrpura claro
    - Cursor: pointer
  
  - **RESPONDIDA (CORRECTA):**
    - Background: Verde claro (green-50)
    - Border: Verde oscuro, 2px
    - Texto: Verde oscuro
    - Icono: ✅ a la derecha
    - Label: "Correcto" o "✓ Correcta"
  
  - **RESPONDIDA (INCORRECTA):**
    - Background: Rojo claro (red-50)
    - Border: Rojo oscuro, 2px
    - Texto: Rojo oscuro
    - Icono: ❌ a la derecha
    - Label: "Incorrecta"
  
  - **CORRECTA PERO NO SELECCIONADA:**
    - Background: Verde claro
    - Border: Verde 2px
    - Label: "✓ Correcta"
    - Sin efecto de error

- **Click en Opción:**
  - Ejecuta: `app.answerQuestion(index)`
  - Actualiza UI inmediatamente
  - Muestra explicación
  - Habilita "Siguiente"

#### 2.6 Sección de Explicación
- **Mostrado DESPUÉS de responder:**
  ```
  💡 Explicación:
  Texto detallado de por qué es correcta
  ```

- **Estilo:**
  - Border left: Azul 4px
  - Background: Azul claro (blue-50)
  - Padding: 16px
  - Font: 14px
  - Línea separadora superior gris

#### 2.7 Controles de Navegación
- **Botones (flex row):**
  1. **Anterior:**
     - Deshabilitado en pregunta 1
     - Color: Gris border
     - Hover: Background gris claro
  
  2. **Mostrar/Ocultar Explicación:**
     - Toggle: "👁️ Mostrar" ↔ "🙈 Ocultar"
     - Color: Gris background
     - Width: Flex-1
  
  3. **Siguiente:**
     - Deshabilitado hasta responder
     - Gradiente púrpura → rosa
     - Color: Blanco
     - Hover: Sombra, escala 1.02
     - Width: Flex-1
     - Width: Flex-1
     - Disabled opacity: 50%

#### 2.8 Botón de Reinicio
- **Mostrado si:** Hay respuestas
- **Ubicación:** Debajo de controles
- **Comportamiento:** 
  - Click → `app.resetQuiz()`
  - Limpia respuestas
  - Vuelve a pregunta 1
  - Mantiene categoría y cantidad

#### 2.9 Resultado Final
- **Mostrado si:** Respondidas === Total
- **Layout:**
  ```
  ┌─────────────────────────┐
  │   🎉 ¡Quiz Completado! │
  │                         │
  │ 20    │ 5    │ 80%     │
  │ Corr. │ Falsa│ Acierto │
  │                         │
  │ [Reiniciar] [Volver]   │
  └─────────────────────────┘
  ```

- **Colores:**
  - Background: Verde gradiente
  - Números: Verde (correctas), Rojo (incorrectas), Púrpura (porcentaje)
  - Font: Bold, 36px números

## 📐 Requisitos de Diseño

### Responsive Breakpoints

| Breakpoint | Ancho | Cambios |
|---|---|---|
| Mobile | 320-374px | Stack vertical completo |
| Mobile | 375-767px | 2 columnas stats |
| Tablet | 768-1023px | Ajuste padding |
| Desktop | 1024px+ | 4 columnas stats, máximo ancho 1200px |

### Paleta de Colores

```
Primario:     #667eea (Púrpura)
Secundario:   #764ba2 (Púrpura oscuro)
Acento:       #f093fb (Rosa)
Success:      #10b981 (Verde)
Error:        #ef4444 (Rojo)
Warning:      #f59e0b (Naranja)
Info:         #3b82f6 (Azul)
Neutral:      #f3f4f6 (Gris claro)
Dark:         #1f2937 (Gris oscuro)
```

### Tipografía

```
Font Family:  Segoe UI, Tahoma, Geneva, Verdana, sans-serif
Weights:      300 (light), 400 (normal), 600 (semibold), 700 (bold)

Sizes:
- Muy pequeño:   12px (labels)
- Pequeño:       14px (subtítulos)
- Normal:        16px (body)
- Título:        20px (pregunta en mobile)
- Título +10%:   24px (encabezados)
- Muy grande:    36px (números finales)
- Gigante:       48px (stats principales)
```

### Espaciado (Basado en Tailwind)

```
xs: 4px      (gap-1)
sm: 8px      (gap-2)
md: 12px     (gap-3)
lg: 16px     (gap-4)
xl: 24px     (gap-6)
2xl: 32px    (gap-8)
```

### Animaciones

```javascript
.smooth {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

// Hover effects:
- Button: scale(1.05), shadow
- Border change: 0.2s
- Color change: 0.3s
```

## 🎨 Estado de Componentes

### Button States

```
Default:     bg-gray-200, text-gray-900, cursor-pointer
Hover:       bg-gray-300, transform scale-102
Active:      bg-purple-600, text-white
Disabled:    opacity-50, cursor-not-allowed
Loading:     spinner animation
```

### Input States

```
Empty:       border-gray-300, bg-white
Focus:       border-purple-600, outline-none
Error:       border-red-500
Success:     border-green-500
Disabled:    bg-gray-100, opacity-50
```

## 🔄 Flujo de Interacción

```
1. Cargar → Setup
2. Seleccionar cantidad → Actualizar contador
3. Seleccionar categoría → Validar disponibilidad
4. Click "Comenzar Quiz" → Transición a Quiz
5. Leer pregunta → Click opción
6. Respuesta → Validación + Explicación
7. Click "Siguiente" → Pregunta siguiente
8. Última pregunta respondida → Mostrar resultado
9. Click "Reiniciar" → Volver a pregunta 1
10. Click "Configurar" → Volver a Setup
```

## ⚡ Requisitos de Performance

- **Time to Interactive:** < 2 segundos
- **First Contentful Paint:** < 1 segundo
- **Tamaño JSON máximo:** 10 MB
- **Cache busting:** Siempre usar ?v=Date.now()
- **Bundle tamaño:** < 100 KB (HTML + CSS)
- **JavaScript:** Vanilla JS, sin frameworks

## ♿ Accesibilidad

- ✅ WCAG 2.1 Level AA
- ✅ Semantic HTML (h1, button, select, etc.)
- ✅ ARIA labels donde sea necesario
- ✅ Contraste mínimo 4.5:1
- ✅ Texto descriptivo de botones
- ✅ Soporte para screen readers
- ✅ Navegación por teclado (Tab, Enter)
- ✅ Focus visible en todos los botones

## 🧪 Casos de Prueba Frontend

### Setup Screen
- [ ] Cargar página → Debería mostrar setup
- [ ] Seleccionar cantidad → Debería actualizar número
- [ ] Mover slider → Debería actualizar cantidad
- [ ] Cambiar categoría → Debería actualizar contador disponible
- [ ] Cantidad 0 → Botón deshabilitado
- [ ] Click "Comenzar" → Transición a quiz

### Quiz Screen
- [ ] Pregunta carga correctamente
- [ ] Opciones se mezclan aleatoriamente
- [ ] Click opción → Se marca correctamente
- [ ] Explicación aparece
- [ ] "Siguiente" habilitado
- [ ] Última pregunta → Muestra resultado
- [ ] "Reiniciar" limpia todo
- [ ] "Configurar" vuelve a setup

### Responsive
- [ ] Mobile 375px → Layout correcto
- [ ] Tablet 768px → 2 columnas
- [ ] Desktop 1024px → 4 columnas
- [ ] Botones clickeables en mobile
- [ ] Texto legible en todos los tamaños

### Edge Cases
- [ ] Sin conexión → JSON cache
- [ ] Muchas preguntas → Scroll sin lag
- [ ] Opciones largas → Wrap correctamente
- [ ] Explicación larga → Scroll dentro del card
- [ ] Múltiples clicks rápidos → Evitar doble-submit

## 📦 Dependencias Frontend

```
- HTML5 (nativo)
- Tailwind CSS (CDN)
- Vanilla JavaScript (nativo)
- Fetch API (nativo)
```

**NO usar:**
- React, Vue, Angular
- jQuery
- Bootstrap
- Cualquier framework JS

## 🚀 Mejoras Futuras

- [ ] Dark mode toggle
- [ ] Notificaciones toast
- [ ] Modal de confirmación
- [ ] Historial de respuestas
- [ ] Filtros avanzados
- [ ] Búsqueda de preguntas
- [ ] Exportar resultados
- [ ] Compartir quiz
- [ ] Modo offline (Service Worker)
- [ ] PWA instalable

---

**Documento:** Frontend Specifications v1.0
**Última actualización:** 2024
**Estado:** Aprobado ✅
