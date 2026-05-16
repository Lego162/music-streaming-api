# Music Streaming API

API REST en Python con FastAPI para una plataforma de streaming de música.

## Requisitos

- Python 3.10+
- MySQL (para etapas futuras)

## Setup

### 1. Crear y activar el entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

```bash
cp .env.example .env
# Editar .env con tus valores reales
```

### 4. Correr el servidor

```bash
uvicorn app.main:app --reload --port 8000
```

## Documentación interactiva

Con el servidor corriendo, abrí en el navegador:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

| Método | Ruta       | Descripción                        |
|--------|------------|------------------------------------|
| GET    | /generos   | Retorna la lista de géneros musicales |
