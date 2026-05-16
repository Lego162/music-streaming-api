# Contexto del Proyecto — Music Streaming API

Este archivo es un resumen del estado actual del proyecto para que un agente de IA pueda continuar el desarrollo desde este punto.

---

## Descripción general

API REST en Python para una plataforma de streaming de música. El objetivo a largo plazo es conectar con una base de datos MySQL que contiene información de reproducciones. El proyecto es de uso educativo, orientado a practicar el desarrollo con asistencia de agentes de IA (Cursor).

---

## Stack

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3.12 |
| Framework | FastAPI 0.136.1 |
| Servidor | Uvicorn 0.47.0 |
| Config | python-dotenv 1.2.2 |
| DB (pendiente) | mysql-connector-python 9.7.0 |

---

## Estructura del proyecto

```
api/
├── app/
│   ├── __init__.py
│   ├── main.py                  # Instancia FastAPI, registra routers
│   ├── config.py                # Lee variables de entorno con dotenv
│   ├── routers/
│   │   ├── __init__.py
│   │   └── generos.py           # Endpoint GET /generos
│   └── services/
│       ├── __init__.py
│       └── generos_service.py   # Lógica de negocio de géneros (dummy por ahora)
├── docs/
│   ├── plan.md                  # Plan original del proyecto
│   └── context.md               # Este archivo
├── .env                         # Variables de entorno reales (no en git)
├── .env.example                 # Plantilla de variables de entorno
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Entorno de desarrollo

- Entorno virtual en `.venv/` (Python venv), activar con `source .venv/bin/activate`
- Dependencias instaladas con `pip install -r requirements.txt`
- Servidor: `uvicorn app.main:app --reload --port 8000`

---

## Variables de entorno (`.env`)

```
APP_NAME=MusicStreamingAPI
APP_ENV=development
APP_PORT=8000

DB_HOST=localhost
DB_PORT=3306
DB_NAME=music_streaming
DB_USER=root
DB_PASSWORD=secret
```

Las variables de DB están declaradas y leídas en `app/config.py`, pero **aún no se usan** — la conexión a MySQL es trabajo futuro.

---

## Endpoints implementados

| Método | Ruta | Estado | Descripción |
|---|---|---|---|
| GET | `/generos` | Funcional (dummy) | Retorna lista de géneros musicales |

### Respuesta actual de `GET /generos`

```json
{
  "generos": ["Pop", "Rock", "Reggaeton", "Jazz", "Hip-Hop", "Electrónica", "Cumbia", "Salsa"]
}
```

La lista está hardcodeada en `app/services/generos_service.py`. Cuando se integre MySQL, solo ese archivo cambia — el router no se toca.

---

## Repositorio

- **GitHub**: https://github.com/Lego162/music-streaming-api
- **Rama activa**: `master`
- **Último commit**: `feat: initial project setup with GET /generos endpoint`

---

## Próximas etapas sugeridas

1. **Conexión a MySQL** — implementar la conexión en un módulo `app/database.py` usando `mysql-connector-python` y las variables de `app/config.py`.
2. **Reemplazar dummy data** — actualizar `generos_service.get_generos()` para consultar la tabla de géneros en la DB.
3. **Nuevos recursos** — agregar endpoints para artistas, canciones, reproducciones, etc.
4. **Modelos de respuesta** — definir esquemas con Pydantic para tipar las respuestas de la API.
5. **Manejo de errores** — agregar handlers globales para errores de DB y validación.
