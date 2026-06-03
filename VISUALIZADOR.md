# 📺 Guía de Visualización - Simulador DevOps

## 🎯 Objetivo

Esta guía te ayudará a visualizar y usar el **Simulador DevOps** en tu navegador web de manera rápida y sencilla.

---

## 📋 Requisitos Previos

- ✅ Python 3.x instalado
- ✅ Navegador web moderno (Chrome, Firefox, Edge, Safari)
- ✅ La carpeta del proyecto: `Simulador DevOps/`

---

## 🚀 Pasos para Visualizar

### **Paso 1: Abrir Terminal/PowerShell**

#### En Windows:
```powershell
# Opción 1: Desde el explorador de archivos
# 1. Navega a: C:\bin\workspace\DevOps\Repasos\Simulador DevOps
# 2. Haz clic derecho en la carpeta vacía
# 3. Selecciona "Abrir PowerShell aquí"

# Opción 2: Manualmente
cd "C:\bin\workspace\DevOps\Repasos\Simulador DevOps"
```

#### En Mac/Linux:
```bash
cd ~/path/to/Simulador\ DevOps
```

---

### **Paso 2: Iniciar Servidor Local**

```bash
python -m http.server 8888 --directory .
```

**Salida esperada:**
```
Serving HTTP on 0.0.0.0 port 8888 (http://0.0.0.0:8888/) ...
```

---

### **Paso 3: Abrir en Navegador**

Haz clic en uno de estos enlaces o cópialo en tu navegador:

- **URL Principal:**
  ```
  http://localhost:8888/src/pages/Simulador.html
  ```

- **Con IP Local (para acceder desde otro dispositivo):**
  ```
  http://[TU_IP_LOCAL]:8888/src/pages/Simulador.html
  ```

---

## 📱 Estructura de Carpetas Importantes

```
Simulador DevOps/
│
├── src/pages/Simulador.html          ← El archivo que ves en el navegador
└── src/dist/data/banco-preguntas-completo.json  ← Los datos (2,340 preguntas)
```

---

## 🎮 Cómo Usar el Simulador

### **1. Pantalla de Configuración**

```
┌─────────────────────────────┐
│ 📊 Preguntas: [25]          │
│ [10] [25] [50] [75] [100]   │
│ 🎯 Categoría: [Todas ▼]     │
│ ✅ 2,340 preguntas disp.     │
│ [Comenzar Quiz (25)]         │
└─────────────────────────────┘
```

**Acciones:**
- Selecciona la **cantidad de preguntas** (10, 25, 50, 75, 100)
- Elige una **categoría** (Todas o una específica)
- Haz clic en **"Comenzar Quiz"**

### **2. Durante el Quiz**

```
┌─────────────────────────────┐
│ Pregunta: 1/25              │
│ Respondidas: 5              │
│ Correctas: 4                │
│ Progreso: 20%               │
│                             │
│ ¿Pregunta de ejemplo?       │
│ [A] Opción A                │
│ [B] Opción B                │
│ [C] Opción C                │
│ [D] Opción D                │
│                             │
│ [Anterior] [Mostrar] [Siguiente] │
└─────────────────────────────┘
```

**Acciones:**
- Haz clic en una **opción** para responder
- Lee la **explicación** de por qué es correcta
- Usa **"Siguiente"** para ir a la siguiente pregunta
- Usa **"Anterior"** para volver
- Usa **"Configurar"** para cambiar el quiz

### **3. Resultado Final**

Al terminar todas las preguntas:
```
┌─────────────────────────────┐
│ 🎉 ¡Quiz Completado!        │
│ Correctas: 20               │
│ Incorrectas: 5              │
│ Acierto: 80%                │
│ [Reiniciar] [Configurar]    │
└─────────────────────────────┘
```

---

## 📊 Categorías Disponibles

### Técnicas DevOps (15)
- Java 21
- Spring Boot 3.5
- ASP.NET Core
- Software Architect
- DevOps
- Patrones de Diseño
- Microsoft Azure
- Microsoft SQL Server
- Seguridad en Nube
- CI/CD con Jenkins
- Kubernetes
- Docker
- AWS
- GCP
- OpenShift

### Razonamiento (6)
- **Razonamiento Abstracto Mejorado** ✨ (NUEVO)
- Psicometrica - Series
- Psicometrica - Secuencias
- Psicometrica - Imagen Faltante
- Psicometrica - Razonamiento
- Psicometrica - Porcentajes

### Soft Skills (5)
- Trabajo en Equipo
- Comunicación
- Liderazgo
- Inteligencia Emocional
- Resolución

### Otros (2)
- DAMA
- Scrum Básico

---

## 🔧 Solución de Problemas

### **Problema: "No se puede acceder a http://localhost:8888"**

**Solución:**
1. Verifica que el servidor esté corriendo (debe ver el mensaje en PowerShell)
2. Si usa puerto 8888 en otro programa, intenta con otro puerto:
   ```bash
   python -m http.server 9999 --directory .
   # Luego abre: http://localhost:9999/src/pages/Simulador.html
   ```

### **Problema: "No se cargan las preguntas"**

**Solución:**
1. Verifica que exista el archivo: `src/dist/data/banco-preguntas-completo.json`
2. Abre la consola del navegador (F12) y busca errores
3. Verifica la ruta en el HTML: debe ser `../dist/data/banco-preguntas-completo.json`

### **Problema: El diseño se ve roto (sin colores)"**

**Solución:**
1. Recarga la página (Ctrl+Shift+R o Cmd+Shift+R)
2. Limpia el caché del navegador
3. Intenta en otro navegador

### **Problema: Las respuestas no se registran**

**Solución:**
1. Verifica que JavaScript esté habilitado en el navegador
2. Abre la consola (F12) para ver errores
3. Intenta en otro navegador

---

## 💾 Archivos Necesarios para Visualizar

Para que el simulador funcione, necesitas estos archivos:

| Archivo | Ubicación | Propósito |
|---------|-----------|----------|
| **Simulador.html** | `src/pages/` | Interfaz web |
| **banco-preguntas-completo.json** | `src/dist/data/` | Preguntas |

**Nota:** No necesitas:
- `banco_preguntas.db` (solo si vas a modificar preguntas)
- `generate_json.py` (solo si vas a regenerar el JSON)
- Archivos en `specs/` (solo si desarrollas backend)

---

## 📱 Acceso desde Otros Dispositivos

### **Desde otro dispositivo en la misma red:**

1. Obtén tu IP local en Windows:
```powershell
ipconfig
# Busca "IPv4 Address", ej: 192.168.1.100
```

2. En el otro dispositivo, abre:
```
http://192.168.1.100:8888/src/pages/Simulador.html
```

---

## 🌐 Despliegue en Producción

Si quieres publicar el simulador en internet:

### **Opción 1: GitHub Pages**
1. Sube los archivos a un repositorio GitHub
2. Activa GitHub Pages en las settings
3. URL: `https://tuusuario.github.io/simulador-devops`

### **Opción 2: Servidor Web (Nginx/Apache)**
1. Copia los archivos a `/var/www/simulador/`
2. Configura el servidor web
3. URL: `https://tudominio.com/simulador`

### **Opción 3: Servidor Node.js/Express**
1. Crea un servidor Express simple
2. Sirve los archivos estáticos
3. Despliega en Heroku, Vercel, etc.

---

## ✨ Características del Simulador

### ✅ Funcionando
- ✅ 2,340 preguntas disponibles
- ✅ 28 categorías diferentes
- ✅ Selector de cantidad (10-100)
- ✅ Selector de categoría dinámico
- ✅ Variación de respuestas (posiciones aleatorias)
- ✅ Validación inteligente
- ✅ Estadísticas en tiempo real
- ✅ Explicaciones detalladas
- ✅ Diseño responsivo (mobile + desktop)
- ✅ Reinicio de quiz
- ✅ Historial dentro de la sesión

### ⏳ Pendiente (Requiere Backend)
- ⏳ Guardar resultados entre sesiones
- ⏳ Cuenta de usuario
- ⏳ Historial histórico
- ⏳ Certificados
- ⏳ Rankings

---

## 📖 Documentación Relacionada

- **[README.md](README.md)** - Documentación general del proyecto
- **[specs/FRONTEND_SPECS.md](specs/FRONTEND_SPECS.md)** - Detalles técnicos frontend
- **[specs/BACKEND_SPECS.md](specs/BACKEND_SPECS.md)** - Detalles técnicos backend

---

## 🎓 Casos de Uso

### **Para Estudiar**
```
1. Selecciona una categoría específica
2. Elige cantidad de preguntas
3. Intenta responder sin mirar explicaciones
4. Lee las explicaciones después
5. Repite hasta dominar el tema
```

### **Para Evaluar**
```
1. Selecciona "Todas" las categorías
2. Elige cantidad máxima (100)
3. Registra el resultado final
4. Compara con evaluaciones anteriores
```

### **Para Repasar**
```
1. Selecciona categoría problema
2. Elige cantidad pequeña (10)
3. Revisa explicaciones de errores
4. Haz varias rondas
```

---

## 🆘 Soporte

Si tienes problemas:

1. **Verifica el navegador:** Chrome, Firefox, Edge (reciente)
2. **Limpia caché:** Ctrl+Shift+R
3. **Abre la consola:** F12 y busca errores rojo
4. **Revisa la estructura:** Verifica que los archivos estén en las carpetas correctas

---

## 📞 Contacto / Reporte de Bugs

Si encuentras un bug:
1. Abre la consola (F12)
2. Copia el error
3. Verifica que el JSON esté cargando correctamente

---

**¡Disfruta practicando!** 🚀

Última actualización: 2024
Versión: 2.1
