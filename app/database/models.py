from sqlalchemy import Column, Integer, String 
from sqlalchemy.orm import declarative_base

Base = declarative_base ()

class LivroModel (Base):
    __tablename__ = "livros"

    id = Column ("id", Integer, primary_key=True, autoincrement=True)
    titulo = Column ("titulo", String (100))
    autor = Column ("autor", String(100))
    ano_publcicao = Column ("ano_publicacao", Integer)