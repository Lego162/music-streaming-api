from fastapi import APIRouter
from app.services import generos_service

router = APIRouter()


@router.get("")
def get_generos():
    generos = generos_service.get_generos()
    return {"generos": generos}
