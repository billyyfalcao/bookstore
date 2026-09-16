from fastapi import APIRouter, HTTPException

from app.schemas.livro import LivroSchema

router = APIRouter (
    prefix="/livros",
    tags= ["livros"],
)

#banco de dados
livros = [
     LivroSchema(id=1, titulo="homem aranha", autor= "seila", ano_publicacao="2026"),
      LivroSchema(id=1, titulo="homem de ferro", autor= "seinaoman", ano_publicacao="2016"),

]

#listar livros 
@router.get ("/")
async def listar_livros ():
    return {"livros" : livros}

#adicionar livros 
@router.post ("/")
async def adicionar_livros (livro:LivroSchema):
    livros.append(livro)

    return {"message": f"livro '{livro}' adicionado com sucesso!"}


#deletar livros 
@router.delete ("/{index}")
async def remover_livros (indicie:int):
        removido = livros.pop(indicie)

        return {"message": f"livro  '{removido}' removido com sucesso"}


#atualizar livros 
@router.put ("/{index}")
async def atualizar_livros (indicie:int, livro:LivroSchema):
    livros [indicie] = livro 

    if indicie > len (livros) or indicie < 0:
         raise HTTPException (status_code=404, detail= "coloca oto")


    return {"message": f"Livro ' {livro}' atualizado com sucesso!"}
