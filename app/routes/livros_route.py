from fastapi import APIRouter, HTTPException

from app.schemas.livro import LivroSchema

router = APIRouter (
    prefix="/livros",
    tags= ["livros"],
)