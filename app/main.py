from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "abobora"}

@app.get ("/saudacao")
async def saudar(nome:str):
    return {"message": f"salve, {nome} seja bem vindo!" }