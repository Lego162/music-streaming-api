from sqlalchemy.orm import Session
from app.models.genero import Genero

def get_generos(db: Session) -> list[Genero]:
    return db.query(Genero).all()