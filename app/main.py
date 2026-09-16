from fastapi import FastAPI, HTTPException

from app.database.conection import db
from app.database.models import Base
from app.routes import livros_route
from app.schemas.livro import LivroSchema

Base.metadata.create_all (bind = db)

app = FastAPI()

app.include_router(livros_route.router)

@app.get("/")
async def home():
    return {"message": "bem vindo a bookstore!"}

