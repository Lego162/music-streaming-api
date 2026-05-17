from pydantic import BaseModel

class GeneroSchema(BaseModel):
    genero_id: int
    nombre: str
    #descripcion: str | None

    model_config = {"from_attributes": True}