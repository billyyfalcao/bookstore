from fastapi import FastAPI, HTTPException

app = FastAPI()


livros = ["noites brancas", "a metamorfose", "crime e castigo"]

@app.get("/")
async def home():
    return {"message": "bem vindo a bookstore!"}

#listar livros 
@app.get ("/livros")
async def listar_livros ():
    return {"livros" : livros}

#adicionar livros 
@app.post ("/adicionar livros")
async def adicionar_livros (livro:str):
    livros.append(livro)

    return {"message": f"livro '{livro}' adicionado com sucesso!"}


#deletar livros 
@app.delete ("/excluir livros")
async def remover_livros (indicie:int):
        removido = livros.pop(indicie)

        return {"message": f"livro  '{removido}' removido com sucesso"}


#atualizar livros 
@app.put ("/atualizar livros")
async def atualizar_livros (indicie:int, new_livro: str):
    livros [indicie] = new_livro

    if indicie > len (livros) or indicie < 0:
         raise HTTPException (status_code=404, detail= "coloca oto")


    return {"message": f"Livro ' {new_livro}' atualizado com sucesso!"}
