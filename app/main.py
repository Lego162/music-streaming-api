from fastapi import FastAPI
from app.config import APP_NAME
from app.routers import generos

app = FastAPI(title=APP_NAME)

app.include_router(generos.router, prefix="/generos", tags=["Géneros"])
