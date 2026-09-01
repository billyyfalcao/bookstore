from fastapi import FastAPI 

app = FastAPI()


livros = ["noites brancas", "a metamorfose", "crime e castigo"]

@app.get("/")
async def home():
    return {"message": "bem vindo a bookstore!"}

#listar livros 
@app.get ("/livros")
async def listar_livros ():
    return {"livros" : livros}
    