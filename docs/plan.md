# Music Streaming API — Plan de Proyecto

## Stack tecnológico

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) — moderno, rápido, y con documentación automática (Swagger UI). Ideal para aprender.
- **Servidor**: `uvicorn` — servidor ASGI ligero para correr FastAPI.
- **DB (futura)**: `mysql-connector-python` — se incluye en requirements pero se usa más adelante.
- **Config**: `python-dotenv` — para leer variables del `.env`.

---

## Estructura de archivos

```
api/
├── app/
│   ├── __init__.py
│   ├── main.py              # Punto de entrada, instancia FastAPI y registra routers
│   ├── config.py            # Lee variables de entorno con dotenv
│   ├── routers/
│   │   ├── __init__.py
│   │   └── generos.py       # Endpoint GET /generos — solo maneja HTTP
│   └── services/
│       ├── __init__.py
│       └── generos_service.py  # Lógica de negocio — devuelve los géneros
├── .env                     # Variables de entorno (no se sube a git)
├── .env.example             # Ejemplo de variables (sí se sube a git)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Archivos clave

### `requirements.txt`
- `fastapi`
- `uvicorn[standard]`
- `python-dotenv`
- `mysql-connector-python`

### `.env` (con valores de ejemplo)
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

### `app/main.py`
- Crea la instancia `FastAPI`
- Incluye el router de `generos` con el prefijo `/generos`

### `app/services/generos_service.py`
- Función `get_generos()` que retorna la lista dummy de géneros
- Aquí vivirá la lógica real de DB en el futuro (sin tocar el router)

### `app/routers/generos.py`
- Endpoint `GET /generos`
- Llama a `generos_service.get_generos()` y retorna el resultado
- El router no contiene lógica de negocio, solo maneja la capa HTTP

---

## Pasos de setup (comandos para ejecutar)

1. Crear y activar el entorno virtual
2. Instalar dependencias desde `requirements.txt`
3. Correr el servidor con `uvicorn`

---

## Endpoint inicial

`GET /generos` → respuesta dummy:
```json
{
  "generos": ["Pop", "Rock", "Reggaeton", "Jazz", "Hip-Hop", "Electrónica", "Cumbia", "Salsa"]
}
```

FastAPI también genera documentación automática en `/docs` (Swagger UI) — muy útil para explorar la API visualmente.
