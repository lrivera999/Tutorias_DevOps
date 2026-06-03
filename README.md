# 🚀 Simulador DevOps - Plataforma de Evaluación Técnica

## Descripción General

**Simulador DevOps** es una plataforma web interactiva para la evaluación y práctica de conocimientos técnicos en DevOps, Cloud, Contenedorización y Desarrollo de Software. Cuenta con más de **2,340 preguntas** distribuidas en **28 categorías** técnicas y soft skills.

## 📊 Estadísticas del Proyecto

| Métrica | Valor |
|---------|-------|
| **Total de Preguntas** | 2,340 |
| **Número de Categorías** | 28 |
| **Opciones por Pregunta** | 4 |
| **Respuestas Variadas** | Sí (Posiciones Aleatorias) |
| **Preguntas con Explicación** | 100% |
| **Diseño Responsivo** | Sí (Mobile + Desktop) |

## 🏗️ Arquitectura Actual

```
┌─────────────────────────────────────────────────────────────┐
│                    SIMULADOR DEVOPS                         │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  Frontend (HTML/CSS/JS)                                      │
│  ├── simulador-final.html (Interfaz Principal)              │
│  └── Tailwind CSS (Diseño Responsivo)                       │
│                                                               │
│  Data Layer                                                  │
│  ├── banco-preguntas-completo.json (Cache en Cliente)       │
│  └── banco_preguntas.db (Fuente de Verdad - SQLite)         │
│                                                               │
│  Utilidades                                                  │
│  └── generate_json.py (Sincronización BD → JSON)            │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

## 📂 Estructura de Carpetas

```
Simulador DevOps/
├── README.md                           # Este archivo
├── VISUALIZADOR.md                    # Guía de cómo visualizar el simulador
├── generate_json.py                   # Script para regenerar JSON desde BD
├── banco_preguntas.db                 # Base de datos SQLite (2,340 preguntas)
│
├── src/                               # Carpeta de recursos
│   ├── pages/
│   │   └── Simulador.html            # Interfaz web (HTML/CSS/JS vanilla)
│   └── dist/data/
│       └── banco-preguntas-completo.json  # JSON con todas las preguntas
│
└── specs/                             # Especificaciones técnicas
    ├── README.md                      # Índice de especificaciones
    ├── FRONTEND_SPECS.md             # Requerimientos para frontend
    └── BACKEND_SPECS.md              # Requerimientos para backend
```

## 🗄️ Esquema de Base de Datos

### Tabla: `preguntas`

```sql
CREATE TABLE preguntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria TEXT,              -- Nombre de la categoría
    subcategoria TEXT,           -- Subcategoría temática
    dificultad TEXT,             -- easy, medium, hard, very hard
    pregunta TEXT,               -- Enunciado de la pregunta
    opcionA TEXT,                -- Opción A
    opcionB TEXT,                -- Opción B
    opcionC TEXT,                -- Opción C
    opcionD TEXT,                -- Opción D
    respuestaCorrecta TEXT,      -- A, B, C o D
    argumentacion TEXT,          -- Explicación de la respuesta
    UNIQUE(pregunta, opcionA, opcionB)
)
```

## 📋 Categorías Disponibles

### Técnicas DevOps & Cloud (15)
- **CI/CD con Jenkins** (100) - Pipelines, stages, agents
- **Kubernetes** (100) - Orquestación, pods, services, deployments
- **Docker** (100) - Contenedores, imágenes, compose
- **AWS** (100) - EC2, S3, RDS, Lambda, VPC
- **GCP** (100) - Compute Engine, Cloud Storage, BigQuery
- **OpenShift** (100) - K8s enterprise, BuildConfig, Routes
- **DevOps** (105) - GitOps, feature toggles, observabilidad
- **Seguridad en Nube** (50) - IAM, encryption, compliance

### Tecnologías (7)
- **Java 21** (100) - Records, Sealed Classes, Virtual Threads
- **Spring Boot 3.5** (100) - Starters, Actuator, auto-config
- **ASP.NET Core** (101) - DI, middleware, Entity Framework
- **Software Architect** (101) - CQRS, Event Sourcing, patrones
- **Patrones de Diseño** (103) - Singleton, Factory, Observer
- **Microsoft Azure** (100) - AppService, Functions, Cosmos
- **Microsoft SQL Server** (100) - Índices, deadlocks, transactions

### Psicométricas (5)
- **Series** (100) - Secuencias numéricas
- **Secuencias** (100) - Patrones multiplicativos
- **Imagen Faltante** (100) - Patrones visuales
- **Razonamiento** (100) - Lógica deductiva
- **Porcentajes** (100) - Cálculos matemáticos

### Soft Skills & Otros (5)
- **Soft Skills - Trabajo en Equipo** (40)
- **Soft Skills - Comunicación** (40)
- **Soft Skills - Liderazgo** (40)
- **Soft Skills - Inteligencia Emocional** (40)
- **Soft Skills - Resolución** (40)
- **DAMA** (40) - Gestión de datos
- **Scrum Básico** (40) - Metodología ágil

## 🔄 Flujo de Datos

### 1. **Carga Inicial**
```
Browser carga simulador-final.html
    ↓
JavaScript ejecuta loadQuestions()
    ↓
Fetch: banco-preguntas-completo.json?v=Date.now()
    ↓
Parsea JSON y mapea categorías dinámicamente
    ↓
Renderiza interfaz de configuración
```

### 2. **Selección de Quiz**
```
Usuario selecciona:
  - Cantidad de preguntas (10, 25, 50, 75, 100)
  - Categoría (Todas + 26 específicas)
    ↓
Click "Comenzar Quiz"
    ↓
loadQuestionsByCategory() filtra preguntas
    ↓
shuffleOptions() mezcla opciones UNA SOLA VEZ
    ↓
Renderiza primera pregunta
```

### 3. **Validación de Respuesta**
```
Usuario hace click en opción
    ↓
answerQuestion(selectedIndex) guarda índice
    ↓
getStats() compara: selectedIndex === _shuffledCorrectIndex
    ↓
Marca verde si correcta, roja si incorrecta
    ↓
Muestra explicación
    ↓
Habilita botón "Siguiente"
```

### 4. **Regeneración de JSON**
```
Cambios en BD → python generate_json.py
    ↓
Lee todas las preguntas desde SQLite
    ↓
Agrupa por categoria → subcategoria → preguntas
    ↓
Genera banco-preguntas-completo.json
    ↓
Cliente carga con cache busting (?v=Date.now())
```

## 🚀 Procesos Actuales

### Agregar Nuevas Preguntas

**Opción 1: Insertar directamente en BD**
```bash
# Crear script Python para insertar en banco_preguntas.db
python script_nuevas_preguntas.py

# Regenerar JSON
python generate_json.py

# Refrescar navegador (cache busting automático)
```

**Opción 2: A través de API Backend (futuro)**
```
POST /api/questions
{
  "categoria": "string",
  "subcategoria": "string",
  "dificultad": "hard|very hard",
  "pregunta": "string",
  "opciones": ["A", "B", "C", "D"],
  "respuestaCorrecta": "A|B|C|D",
  "argumentacion": "string"
}
```

### Actualizar Categorías
```bash
# Actualizar tabla preguntas
UPDATE preguntas SET subcategoria='nueva' WHERE categoria='Java 21'

# Regenerar JSON
python generate_json.py

# Refrescar cliente
```

## 💾 Sincronización BD ↔ JSON

**Script: generate_json.py**
```python
# Lee BD SQLite
cursor.execute('SELECT * FROM preguntas GROUP BY categoria')

# Estructura jerárquica:
banco = {
  "banco": {
    "categorías": [
      {
        "nombre": "Java 21",
        "preguntas": [
          {
            "id": 1,
            "pregunta": "...",
            "opciones": [{"letra": "A", "texto": "..."}],
            "respuestaCorrecta": "A",
            "argumentacion": "..."
          }
        ]
      }
    ]
  }
}

# Guarda en JSON
```

## 🎯 Funcionalidades Principales

### ✅ Implementadas

| Funcionalidad | Estado | Detalles |
|---|---|---|
| Selector de cantidad | ✅ | 10, 25, 50, 75, 100 |
| Selector de categoría | ✅ | Dinámico desde JSON |
| Variación de respuestas | ✅ | Mezcla aleatoria |
| Validación inteligente | ✅ | Compara índice shuffled |
| Estadísticas en tiempo real | ✅ | Contador de correctas |
| Explicaciones | ✅ | Se muestran post-respuesta |
| Navegación | ✅ | Anterior, Siguiente, Reiniciar |
| Diseño responsivo | ✅ | Mobile 375px + Desktop 1200px+ |
| Cache busting | ✅ | ?v=Date.now() en fetch |

### ⏳ Pendientes de Implementar

| Funcionalidad | Prioridad | Notas |
|---|---|---|
| Autenticación de usuarios | Media | Usuario/contraseña |
| Persistencia de resultados | Media | Guardar scores en BD |
| Reportes y estadísticas | Baja | Análisis de desempeño |
| Exportar resultados | Baja | CSV/PDF |
| API REST completa | Alta | CRUD de preguntas |
| Gestión admin | Alta | Panel para gestionar Q&A |
| Integración OAuth | Baja | Google/GitHub login |
| Búsqueda de preguntas | Media | Búsqueda por texto |
| Filtros avanzados | Baja | Por dificultad, tags |

## 🔧 Tecnologías Utilizadas

### Frontend (Actual)
- **HTML5** - Estructura semántica
- **Tailwind CSS** - Diseño responsivo
- **Vanilla JavaScript** - Lógica sin frameworks
- **Fetch API** - Carga de datos

### Backend (Actual)
- **Python 3.x** - Scripts de utilidad
- **SQLite3** - Base de datos embebida
- **http.server** - Servidor local para preview

### Herramientas
- **PowerShell** - Automatización Windows
- **Git** - Control de versiones
- **Claude Code** - Desarrollo asistido

## 📡 Endpoints Planeados (Backend)

### Lectura
```
GET /api/categories              → Lista todas las categorías
GET /api/categories/{id}/count   → Número de preguntas por categoría
GET /api/questions               → Todas las preguntas (con filtros)
GET /api/questions/{id}          → Pregunta específica
GET /api/quiz/random/{count}     → {count} preguntas aleatorias
GET /api/quiz/category/{cat}/{count} → {count} preguntas de categoría
```

### Escritura (Admin)
```
POST /api/questions              → Crear pregunta
PUT /api/questions/{id}          → Actualizar pregunta
DELETE /api/questions/{id}       → Eliminar pregunta
POST /api/categories             → Crear categoría
PUT /api/categories/{id}         → Actualizar categoría
```

### Análisis
```
POST /api/quiz/submit            → Enviar respuestas para evaluación
GET /api/results/{userId}        → Histórico de resultados
GET /api/analytics/category/{id} → Estadísticas por categoría
```

## 🚀 Cómo Ejecutar

### Localmente

1. **Navegar a la carpeta**
```bash
cd "C:\bin\workspace\DevOps\Repasos\Simulador DevOps"
```

2. **Iniciar servidor local**
```bash
python -m http.server 8888 --directory .
```

3. **Abrir en navegador**
```
http://localhost:8888/src/pages/Simulador.html
```

4. **Usar el simulador**
   - Seleccionar cantidad de preguntas
   - Seleccionar categoría
   - Click "Comenzar Quiz"
   - Responder preguntas
   - Ver explicaciones
   - Reiniciar quiz

**Para instrucciones detalladas, ver [VISUALIZADOR.md](VISUALIZADOR.md)**

## 📝 Actualizar Base de Datos

### Opción 1: Script Python
```bash
# Crear script con nuevas preguntas
python mi_script_nuevas_preguntas.py

# Regenerar JSON
python generate_json.py

# Refrescar navegador
```

### Opción 2: SQL Directo (futuro)
```bash
# Usar UI Admin para agregar/editar preguntas
# Cambios se sincronizan automáticamente
```

## 📊 Estructura JSON Generada

```json
{
  "banco": {
    "titulo": "Banco Completo de 2240 Preguntas",
    "totalPreguntas": 2240,
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
            "argumentacion": "Tecnología para crear y ejecutar contenedores."
          }
        ]
      }
    ]
  }
}
```

## 🔐 Seguridad (Actual)

- ✅ No hay datos sensibles en el cliente
- ✅ Validación en lado del cliente
- ✅ Cache busting previene resultados stale
- ⚠️ Sin autenticación (pendiente)
- ⚠️ Sin HTTPS (local solo)
- ⚠️ Sin rate limiting (pendiente)

## 📈 Próximos Pasos

### Corto Plazo
1. Crear API REST backend (Node.js/Python)
2. Implementar autenticación
3. Base de datos en servidor (PostgreSQL)
4. Panel admin para gestionar preguntas

### Mediano Plazo
1. Persistencia de resultados de usuario
2. Reportes y analytics
3. Sistema de tags/filtros avanzados
4. Modo competitivo (leaderboard)

### Largo Plazo
1. App móvil (React Native)
2. Integración con LMS
3. Sistema de certificación
4. Análisis ML de desempeño

## 📞 Soporte

Para reportar bugs o sugerir mejoras, consulta la documentación en `specs/`.

---

**Última actualización:** 2024
**Versión:** 2.0
**Estado:** Producción ✅
