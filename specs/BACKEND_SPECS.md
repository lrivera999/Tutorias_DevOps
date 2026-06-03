# 🔧 Especificaciones Backend - Simulador DevOps

## 🎯 Objetivo

Desarrollar una API REST robusta, segura y escalable que sirva como fuente única de verdad para las preguntas del simulador, permitiendo gestión completa de datos, autenticación, análisis y administración.

## 🏗️ Arquitectura Backend

```
┌─────────────────────────────────────────┐
│         Frontend (HTML/JS)              │
└──────────────┬──────────────────────────┘
               │ HTTP/REST
┌──────────────▼──────────────────────────┐
│      API Gateway / Load Balancer        │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│      Express.js / FastAPI Server        │
│  ├─ Auth Middleware                     │
│  ├─ Logger Middleware                   │
│  ├─ Error Handler                       │
│  └─ Rate Limiter                        │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│      Database Layer                     │
│  ├─ PostgreSQL (Producción)             │
│  ├─ SQLite (Desarrollo)                 │
│  └─ Redis Cache                         │
└─────────────────────────────────────────┘
```

## 💾 Esquema de Base de Datos (PostgreSQL)

### Tabla: `users`
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    role ENUM('user', 'admin', 'instructor') DEFAULT 'user',
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);
```

### Tabla: `categories`
```sql
CREATE TABLE categories (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    icon VARCHAR(10),
    color VARCHAR(7),
    question_count INT DEFAULT 0,
    is_active BOOLEAN DEFAULT true,
    sort_order INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Tabla: `questions`
```sql
CREATE TABLE questions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    category_id UUID NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
    subcategory VARCHAR(100),
    difficulty VARCHAR(20) CHECK (difficulty IN ('easy', 'medium', 'hard', 'very_hard')),
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer CHAR(1) CHECK (correct_answer IN ('A', 'B', 'C', 'D')),
    explanation TEXT NOT NULL,
    is_active BOOLEAN DEFAULT true,
    created_by UUID NOT NULL REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(question, option_a, option_b)
);

CREATE INDEX idx_questions_category ON questions(category_id);
CREATE INDEX idx_questions_difficulty ON questions(difficulty);
```

### Tabla: `quiz_sessions`
```sql
CREATE TABLE quiz_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    category_id UUID REFERENCES categories(id),
    question_count INT NOT NULL,
    total_questions INT NOT NULL,
    correct_answers INT DEFAULT 0,
    incorrect_answers INT DEFAULT 0,
    score DECIMAL(5,2),
    duration_seconds INT,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    status VARCHAR(20) DEFAULT 'in_progress'
);

CREATE INDEX idx_quiz_sessions_user ON quiz_sessions(user_id);
CREATE INDEX idx_quiz_sessions_category ON quiz_sessions(category_id);
```

### Tabla: `quiz_responses`
```sql
CREATE TABLE quiz_responses (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    quiz_session_id UUID NOT NULL REFERENCES quiz_sessions(id) ON DELETE CASCADE,
    question_id UUID NOT NULL REFERENCES questions(id),
    user_answer CHAR(1) NOT NULL,
    is_correct BOOLEAN NOT NULL,
    answer_time_seconds INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_quiz_responses_session ON quiz_responses(quiz_session_id);
```

### Tabla: `audit_logs`
```sql
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    action VARCHAR(100) NOT NULL,
    entity_type VARCHAR(50) NOT NULL,
    entity_id UUID,
    old_values JSONB,
    new_values JSONB,
    ip_address INET,
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🔌 API Endpoints

### Autenticación

#### POST /api/auth/register
Registra nuevo usuario
```
REQUEST:
{
  "username": "jdoe",
  "email": "john@example.com",
  "password": "Secure123!",
  "first_name": "John",
  "last_name": "Doe"
}

RESPONSE (201):
{
  "id": "uuid",
  "username": "jdoe",
  "email": "john@example.com",
  "token": "jwt_token",
  "expires_in": 3600
}

ERRORS:
- 400: Username/email ya existe
- 422: Datos inválidos
```

#### POST /api/auth/login
Autentica usuario
```
REQUEST:
{
  "username": "jdoe",
  "password": "Secure123!"
}

RESPONSE (200):
{
  "id": "uuid",
  "username": "jdoe",
  "token": "jwt_token",
  "expires_in": 3600,
  "role": "user"
}

ERRORS:
- 401: Credenciales inválidas
- 400: Campos requeridos faltantes
```

#### POST /api/auth/refresh
Refresca token JWT
```
REQUEST:
{
  "refresh_token": "refresh_token"
}

RESPONSE (200):
{
  "token": "new_jwt_token",
  "expires_in": 3600
}

ERRORS:
- 401: Token inválido/expirado
```

#### POST /api/auth/logout
Cierra sesión
```
REQUEST: (sin body, auth requerida)

RESPONSE (200):
{
  "message": "Logged out successfully"
}
```

### Categorías

#### GET /api/categories
Lista todas las categorías
```
QUERY PARAMS:
- page: int (default: 1)
- limit: int (default: 20)
- sort: string (name, question_count)
- is_active: boolean (default: true)

RESPONSE (200):
{
  "data": [
    {
      "id": "uuid",
      "name": "Docker",
      "description": "...",
      "icon": "🐳",
      "question_count": 100,
      "sort_order": 1
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 27,
    "pages": 2
  }
}
```

#### GET /api/categories/{id}
Obtiene categoría específica
```
RESPONSE (200):
{
  "id": "uuid",
  "name": "Docker",
  "description": "...",
  "icon": "🐳",
  "question_count": 100,
  "questions": [...]
}
```

#### POST /api/categories
Crea nueva categoría (ADMIN)
```
REQUEST (auth + admin):
{
  "name": "New Category",
  "description": "...",
  "icon": "📚",
  "color": "#667eea",
  "sort_order": 28
}

RESPONSE (201):
{
  "id": "uuid",
  "name": "New Category",
  ...
}

ERRORS:
- 401: No autenticado
- 403: No es admin
- 409: Categoría ya existe
```

#### PUT /api/categories/{id}
Actualiza categoría (ADMIN)
```
REQUEST (auth + admin):
{
  "name": "Updated Name",
  "description": "..."
}

RESPONSE (200): Categoría actualizada

ERRORS:
- 404: No encontrada
- 403: No es admin
```

#### DELETE /api/categories/{id}
Elimina categoría (ADMIN)
```
RESPONSE (204): Sin contenido

ERRORS:
- 404: No encontrada
- 403: No es admin
- 409: Categoría tiene preguntas
```

### Preguntas

#### GET /api/questions
Lista preguntas con filtros
```
QUERY PARAMS:
- category_id: uuid
- difficulty: easy|medium|hard|very_hard
- search: string (busca en pregunta)
- page: int
- limit: int
- random: boolean (si true, devuelve random)
- count: int (cantidad a devolver si random=true)

RESPONSE (200):
{
  "data": [
    {
      "id": "uuid",
      "category_id": "uuid",
      "question": "¿Qué es Docker?",
      "options": [
        {"letter": "A", "text": "..."},
        {"letter": "B", "text": "..."},
        {"letter": "C", "text": "..."},
        {"letter": "D", "text": "..."}
      ],
      "difficulty": "hard",
      "subcategory": "Contenedor",
      "explanation": "..."
    }
  ],
  "pagination": {...}
}
```

#### GET /api/questions/{id}
Obtiene pregunta específica
```
RESPONSE (200): Pregunta completa con explicación
```

#### POST /api/questions
Crea pregunta (ADMIN/INSTRUCTOR)
```
REQUEST (auth + admin|instructor):
{
  "category_id": "uuid",
  "question": "¿Qué es Docker?",
  "option_a": "...",
  "option_b": "...",
  "option_c": "...",
  "option_d": "...",
  "correct_answer": "A",
  "difficulty": "hard",
  "subcategory": "Contenedor",
  "explanation": "Tecnología para..."
}

RESPONSE (201): Pregunta creada

ERRORS:
- 422: Datos inválidos
- 403: Sin permisos
- 409: Pregunta ya existe
```

#### PUT /api/questions/{id}
Actualiza pregunta (ADMIN/INSTRUCTOR)
```
REQUEST: Misma estructura que POST

RESPONSE (200): Pregunta actualizada

ERRORS:
- 404: No encontrada
- 403: Sin permisos
- 409: Duplicada
```

#### DELETE /api/questions/{id}
Elimina pregunta (ADMIN)
```
RESPONSE (204): Sin contenido

ERRORS:
- 404: No encontrada
- 403: Solo admin
```

#### GET /api/questions/random/{count}
Obtiene {count} preguntas aleatorias
```
QUERY PARAMS:
- category_id: uuid (opcional)

RESPONSE (200):
{
  "data": [preguntas],
  "count": int
}
```

### Quiz

#### POST /api/quiz/start
Inicia nueva sesión de quiz
```
REQUEST (auth):
{
  "category_id": "uuid" (opcional, null para todas),
  "question_count": 25
}

RESPONSE (201):
{
  "session_id": "uuid",
  "questions": [...],
  "total": 25,
  "category": "Docker"
}
```

#### POST /api/quiz/submit
Envía respuestas y califica quiz
```
REQUEST (auth):
{
  "session_id": "uuid",
  "responses": [
    {
      "question_id": "uuid",
      "user_answer": "A",
      "answer_time_seconds": 15
    }
  ]
}

RESPONSE (200):
{
  "session_id": "uuid",
  "total_questions": 25,
  "correct_answers": 20,
  "incorrect_answers": 5,
  "score": 80.0,
  "percentage": "80%",
  "duration_seconds": 300,
  "details": [
    {
      "question_id": "uuid",
      "is_correct": true,
      "user_answer": "A",
      "correct_answer": "A",
      "explanation": "..."
    }
  ]
}
```

#### GET /api/quiz/sessions
Historial de quiz del usuario
```
QUERY PARAMS:
- page: int
- limit: int
- category_id: uuid (opcional)

RESPONSE (200):
{
  "data": [
    {
      "id": "uuid",
      "category": "Docker",
      "score": 80.0,
      "total_questions": 25,
      "completed_at": "2024-01-15T10:30:00Z",
      "duration_seconds": 300
    }
  ],
  "pagination": {...}
}
```

#### GET /api/quiz/sessions/{id}
Obtiene detalles de sesión específica
```
RESPONSE (200):
{
  "session": {...},
  "responses": [...]
}
```

### Análisis (Analytics)

#### GET /api/analytics/user
Estadísticas del usuario actual (AUTH)
```
RESPONSE (200):
{
  "total_quizzes": 50,
  "average_score": 75.5,
  "total_questions_answered": 1250,
  "correct_answers": 940,
  "accuracy": 75.2,
  "best_category": "Docker",
  "worst_category": "GCP",
  "total_study_hours": 25.5,
  "streak_days": 7,
  "recent_scores": [...]
}
```

#### GET /api/analytics/category/{id}
Estadísticas generales de categoría
```
QUERY PARAMS:
- period: day|week|month|all (default: all)

RESPONSE (200):
{
  "category": "Docker",
  "total_attempts": 1500,
  "average_score": 72.3,
  "difficulty_distribution": {
    "easy": 0.25,
    "medium": 0.35,
    "hard": 0.25,
    "very_hard": 0.15
  },
  "most_missed_questions": [...],
  "trending": "up"
}
```

#### GET /api/analytics/leaderboard
Ranking de usuarios (públicos)
```
QUERY PARAMS:
- period: week|month|all
- limit: int (default: 100)
- category_id: uuid (opcional)

RESPONSE (200):
{
  "period": "month",
  "data": [
    {
      "rank": 1,
      "username": "jdoe",
      "score": 92.5,
      "quiz_count": 10,
      "category": "Docker"
    }
  ]
}
```

### Admin

#### GET /api/admin/users
Lista todos usuarios (ADMIN)
```
QUERY PARAMS:
- page: int
- limit: int
- role: user|admin|instructor
- is_active: boolean

RESPONSE (200):
{
  "data": [usuarios],
  "pagination": {...}
}
```

#### PUT /api/admin/users/{id}/role
Cambia rol de usuario (ADMIN)
```
REQUEST:
{
  "role": "instructor|admin|user"
}

RESPONSE (200): Usuario actualizado
```

#### POST /api/admin/audit-logs
Lista logs de auditoría (ADMIN)
```
QUERY PARAMS:
- action: string
- entity_type: string
- user_id: uuid
- date_from: ISO date
- date_to: ISO date

RESPONSE (200): Logs con paginación
```

#### POST /api/admin/backup
Crea backup de BD (ADMIN)
```
RESPONSE (200):
{
  "backup_id": "uuid",
  "size_mb": 15.2,
  "created_at": "2024-01-15T10:30:00Z",
  "download_url": "..."
}
```

## 🔐 Seguridad

### Autenticación
- ✅ JWT (JSON Web Tokens)
- ✅ Refresh tokens con rotación
- ✅ Expiración configurable (1 hora access, 7 días refresh)
- ✅ HTTPS obligatorio en producción
- ✅ CORS configurado para dominios autorizados

### Autorización
- ✅ Role-Based Access Control (RBAC)
  - `user`: Acceso a quiz y resultados personales
  - `instructor`: CRUD de preguntas (propias)
  - `admin`: Acceso total + gestión usuarios
- ✅ Validación de permisos en cada endpoint
- ✅ Auditoría de cambios

### Validación
- ✅ Validación de entrada (schema + tipos)
- ✅ Sanitización de datos
- ✅ Rate limiting (100 requests/min por IP)
- ✅ SQL injection prevention (prepared statements)
- ✅ XSS protection (response headers)
- ✅ CSRF tokens para POST/PUT/DELETE

### Encriptación
- ✅ Passwords: bcrypt (salt rounds: 12)
- ✅ Datos sensibles: AES-256
- ✅ HTTPS/TLS 1.2+

## 📊 Error Handling

### Formato de Respuesta
```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Descripción del error",
    "details": {
      "field": "email",
      "reason": "Email ya existe"
    },
    "request_id": "uuid"
  }
}
```

### Códigos HTTP
- `200 OK` - Éxito
- `201 Created` - Recurso creado
- `204 No Content` - Éxito sin respuesta
- `400 Bad Request` - Datos inválidos
- `401 Unauthorized` - No autenticado
- `403 Forbidden` - Sin permisos
- `404 Not Found` - Recurso no encontrado
- `409 Conflict` - Recurso duplicado
- `422 Unprocessable Entity` - Validación falló
- `429 Too Many Requests` - Rate limit
- `500 Internal Server Error` - Error servidor
- `503 Service Unavailable` - Mantenimiento

## 🚀 Performance

### Caching
- ✅ Redis para caché de consultas frecuentes
  - Categorías: 1 hora
  - Preguntas por categoría: 30 minutos
  - Leaderboard: 15 minutos
- ✅ HTTP caching headers (ETag, Last-Modified)
- ✅ Compresión gzip de respuestas

### Optimización BD
- ✅ Índices en queries frecuentes
- ✅ Paginación en endpoints de lista
- ✅ Query optimization y EXPLAIN ANALYZE
- ✅ Connection pooling (20-30 conexiones)

### Monitoreo
- ✅ Logging estructurado (Winston/Bunyan)
- ✅ Métricas (Prometheus)
- ✅ APM (Application Performance Monitoring)
- ✅ Alertas en errores 5xx

## 🧪 Testing Backend

### Cobertura Requerida
- ✅ Unit tests: 80%+ cobertura
- ✅ Integration tests: APIs principales
- ✅ E2E tests: Flujos críticos
- ✅ Load testing: 1000 concurrent users
- ✅ Security testing: OWASP Top 10

### Herramientas
```
Test Framework: Jest / Pytest
Assertion:      Chai / Pytest assertions
Mocking:        Sinon / unittest.mock
Load Testing:   Artillery / Locust
Security:       OWASP ZAP / npm audit
```

## 📦 Stack Recomendado

### Opción 1: Node.js + Express
```
- Runtime: Node.js 18+
- Framework: Express.js
- Auth: Passport.js + JWT
- Validation: Joi / Yup
- ORM: Sequelize / Prisma
- Database: PostgreSQL
- Caching: Redis
- Logging: Winston
- Testing: Jest
```

### Opción 2: Python + FastAPI
```
- Runtime: Python 3.10+
- Framework: FastAPI
- Auth: python-jose + JWT
- Validation: Pydantic
- ORM: SQLAlchemy
- Database: PostgreSQL
- Caching: Redis
- Logging: structlog
- Testing: Pytest
```

### Infraestructura
```
- Cloud: AWS / GCP / Azure
- Container: Docker
- Orchestration: Kubernetes
- CI/CD: GitHub Actions / GitLab CI
- Database: Managed PostgreSQL
- Cache: Managed Redis
- Monitoring: CloudWatch / Datadog
- CDN: CloudFront / Cloudflare
```

## 🔄 Integración con Frontend

### Headers Requeridos
```
Authorization: Bearer {jwt_token}
Content-Type: application/json
Accept: application/json
X-Request-ID: {uuid}
User-Agent: {client}
```

### CORS
```javascript
{
  origins: ['https://example.com'],
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  headers: ['Content-Type', 'Authorization'],
  max_age: 3600
}
```

## 📈 Roadmap Backend

### Fase 1 (MVP)
- [ ] API REST básica (CRUD de preguntas)
- [ ] Autenticación JWT
- [ ] Quiz engine
- [ ] Persistencia de resultados
- [ ] PostgreSQL en producción

### Fase 2 (Enhanced)
- [ ] Leaderboard y rankings
- [ ] Analytics y reportes
- [ ] Admin panel backend
- [ ] Integración con LMS
- [ ] Sistema de certificados

### Fase 3 (Advanced)
- [ ] Machine learning (recomendaciones)
- [ ] Sistema de badges/achievements
- [ ] Integración OAuth (Google/GitHub)
- [ ] Exportación de datos
- [ ] API GraphQL

## 🚢 Deployment

### Desarrollo
```bash
npm install
npm run dev
# http://localhost:3000
```

### Staging
```bash
docker build -t simulador-api:latest .
docker run -p 3000:3000 simulador-api:latest
```

### Producción
```bash
# Deploy con Kubernetes
kubectl apply -f deployment.yaml

# Variables de entorno
DATABASE_URL=postgresql://...
JWT_SECRET=...
REDIS_URL=...
NODE_ENV=production
```

---

**Documento:** Backend Specifications v1.0
**Última actualización:** 2024
**Estado:** Aprobado ✅
