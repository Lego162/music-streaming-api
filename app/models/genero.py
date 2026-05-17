from sqlalchemy import Column, Integer, String
from app.database import Base

class Genero(Base):
    __tablename__ = "generos"

    genero_id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(200))