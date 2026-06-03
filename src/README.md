# 📁 Carpeta `src/` - Recursos del Simulador

## 📂 Estructura

```
src/
├── pages/
│   └── Simulador.html                ← Interfaz principal del simulador
│
└── dist/data/
    └── banco-preguntas-completo.json ← Base de datos de preguntas (2,340)
```

---

## 📄 Archivos

### **pages/Simulador.html**

**Descripción:** Interfaz web completa del simulador DevOps.

**Contenido:**
- HTML5 semántico
- Tailwind CSS para estilos responsivos
- Vanilla JavaScript (sin frameworks)
- Lógica de quiz completa

**Ruta de acceso:**
```
http://localhost:8888/src/pages/Simulador.html
```

**Características:**
- ✅ Interfaz responsiva (mobile + desktop)
- ✅ Carga dinámica de preguntas desde JSON
- ✅ Validación de respuestas
- ✅ Estadísticas en tiempo real
- ✅ Explicaciones después de cada pregunta
- ✅ Soporte para 28 categorías
- ✅ Selector de cantidad (10-100)
- ✅ Navegación (Anterior/Siguiente)
- ✅ Reinicio de quiz

**Dependencias Externas:**
- Tailwind CSS (CDN)
- Fetch API (nativa del navegador)

---

### **dist/data/banco-preguntas-completo.json**

**Descripción:** Base de datos JSON con todas las preguntas del simulador.

**Ubicación relativa desde Simulador.html:**
```javascript
// En Simulador.html línea 47:
fetch('../dist/data/banco-preguntas-completo.json?v=' + Date.now())
```

**Estructura del JSON:**
```json
{
  "banco": {
    "titulo": "Banco Completo de 2340 Preguntas",
    "totalPreguntas": 2340,
    "categorías": [
      {
        "id": "docker",
        "nombre": "Docker",
        "totalPreguntas": 100,
        "preguntas": [
          {
            "id": 1,
            "subcategoria": "Contenedor",
            "dificultad": "hard",
            "pregunta": "¿Qué es Docker?",
            "opciones": [
              {"letra": "A", "texto": "Contenedorizador"},
              {"letra": "B", "texto": "Framework"},
              {"letra": "C", "texto": "Base de datos"},
              {"letra": "D", "texto": "Servidor web"}
            ],
            "respuestaCorrecta": "A",
            "argumentacion": "Descripción de por qué A es correcta..."
          }
        ]
      }
    ]
  }
}
```

**Datos Incluidos:**
- **Total preguntas:** 2,340
- **Categorías:** 28
- **Opciones por pregunta:** 4 (A, B, C, D)
- **Explicaciones:** 100% de preguntas

**Categorías:**
- 15 Técnicas DevOps/Cloud
- 6 Razonamiento
- 5 Soft Skills
- 2 Otros

---

## 🔧 Ajustes Realizados

### Rutas de Archivos

El HTML fue actualizado para buscar el JSON en la ubicación correcta:

**Antes:**
```javascript
fetch('banco-preguntas-completo.json?v=' + Date.now())
```

**Después:**
```javascript
fetch('../dist/data/banco-preguntas-completo.json?v=' + Date.now())
```

Esta ruta relativa permite que el HTML acceda al JSON sin importar dónde se sirva el proyecto.

---

## 📡 Cache Busting

El simulador usa cache busting para garantizar que siempre carga la versión más reciente del JSON:

```javascript
fetch('../dist/data/banco-preguntas-completo.json?v=' + Date.now())
```

El parámetro `?v=` con un timestamp asegura que los navegadores siempre descarguen el archivo más reciente.

---

## 🚀 Cómo Servir

### **Localmente (Desarrollo)**

```bash
# Desde la carpeta raíz del proyecto
cd "C:\bin\workspace\DevOps\Repasos\Simulador DevOps"

# Iniciar servidor
python -m http.server 8888 --directory .

# Acceder
http://localhost:8888/src/pages/Simulador.html
```

### **En Producción**

```bash
# Opción 1: Nginx
# Sirve la carpeta raíz como static files

# Opción 2: Apache
# Configura DocumentRoot en el directorio raíz

# Opción 3: Node.js
# Usa express.static() en la carpeta raíz
```

---

## 📊 Información del Archivo JSON

| Propiedad | Valor |
|-----------|-------|
| **Tamaño** | ~1.7 MB |
| **Formato** | JSON válido |
| **Codificación** | UTF-8 |
| **Estructura** | Jerárquica (categorías → preguntas) |
| **Actualización** | Regenerada automáticamente desde BD |

**Para regenerar:** Ejecuta `python generate_json.py` desde la carpeta raíz.

---

## 🔄 Relación con Base de Datos

### Flujo de Datos

```
banco_preguntas.db (SQLite)
    ↓
    ↓ python generate_json.py
    ↓
src/dist/data/banco-preguntas-completo.json
    ↓
    ↓ fetch() en Simulador.html
    ↓
JavaScript App
    ↓
    ↓ renderiza en navegador
    ↓
Usuario ve las preguntas
```

---

## ⚙️ Mantenimiento

### Agregar Nuevas Preguntas

1. Modificar `banco_preguntas.db`
2. Ejecutar: `python generate_json.py`
3. El JSON se regenera automáticamente
4. Refrescar navegador (cache busting automático)

### Verificar Integridad

```bash
# Validar JSON
python -m json.tool src/dist/data/banco-preguntas-completo.json

# Contar preguntas
grep -o '"id":' src/dist/data/banco-preguntas-completo.json | wc -l
```

---

## 📱 Responsive Design

El HTML se adapta automáticamente a:

- **Mobile:** 375px - 767px (Stack vertical)
- **Tablet:** 768px - 1023px (2 columnas)
- **Desktop:** 1024px+ (4 columnas)

Todos los elementos son clickeables en pantallas pequeñas con áreas suficientes.

---

## 🔐 Seguridad

- ✅ Sin datos sensibles en el cliente
- ✅ Validación en lado del cliente
- ✅ HTTPS recomendado en producción
- ✅ Cache busting previene respuestas stale
- ⚠️ Sin autenticación (no hay cuentas de usuario)

---

## 📖 Documentación Relacionada

- **[../README.md](../README.md)** - Documentación general
- **[../VISUALIZADOR.md](../VISUALIZADOR.md)** - Cómo visualizar el simulador
- **[../specs/FRONTEND_SPECS.md](../specs/FRONTEND_SPECS.md)** - Especificaciones técnicas

---

## 🎯 Próximos Pasos

Para expandir el simulador:

1. **Backend API** - Para persistencia de datos
2. **Autenticación** - Para cuentas de usuario
3. **Base de datos servidor** - PostgreSQL en lugar de SQLite
4. **Dashboard** - Para administración de preguntas
5. **Analytics** - Para trackear desempeño

---

**Última actualización:** 2024  
**Versión:** 2.1  
**Estado:** ✅ Funcional
