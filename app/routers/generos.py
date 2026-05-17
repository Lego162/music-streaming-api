from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import generos_service
from app.schemas.genero import GeneroSchema

router = APIRouter()

@router.get("", response_model=list[GeneroSchema])
def get_generos(db: Session = Depends(get_db)):
    return generos_service.get_generos(db)