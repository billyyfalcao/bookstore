from fastapi import FastAPI

from app.database.conection import db
from app.database.models import Base
from app.routes import livros_route

Base.metadata.create_all (bind = db)

app = FastAPI()

app.include_router(livros_route.router)

@app.get("/")
async def home():
    return {"message": "bem vindo a bookstore!"}

