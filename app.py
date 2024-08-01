from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

PRODUTOS = [
  {
    "id":1,
    "nome": "Smartphone",
    "descricao": "Um celular inteligente",
    "preco": 1999.00,
    "disponivel": True
  },
  {
    "id":2,
    "nome": "Notebook",
    "descricao": "Um computador portátil",
    "preco": 3999.00,
    "disponivel": False
  }
]


#classe criada como modelo de um novo produto, para melhor formatação na hora do registro.
class Produto (BaseModel):
  """Classe de produto"""

  nome: str
  descricao: Optional[str] = None
  preco: float
  disponivel: Optional [bool] = True


@app.get("/produtos", tags=["produtos"])
def listar_produtos() -> list:
  """Listar Produtos"""
  return PRODUTOS

@app.get("/produtos/disponiveis", tags=["produtos"])
def listar_produtos_disponiveis() -> list:
  """Listar produtos disponiveis"""
  produtos_disponiveis = []
  for produto in PRODUTOS:
    if produto["disponivel"]:
      produtos_disponiveis.append(produto)
  return produtos_disponiveis

@app.get("/produtos/{produto_id}", tags=["produtos"])
def obter_produto(prodruto_id: int) -> dict:
  """Obter produto"""
  for produto in PRODUTOS:
    if produto["id"] == prodruto_id:
      return produto
  return {}

@app.post("/produtos", tags=["produtos"])
def criar_produto(produto: Produto) -> dict:
  """Criar produto"""
  produto = produto.dict()
  produto["id"] = len(PRODUTOS) + 1
  PRODUTOS.append(produto)
  return produto

@app.put("/produtos/{prodruto_id}", tags=["produtos"])
def atualizar_produto(produto_id: int, produto: Produto) -> dict:
  """Atualizar produto"""
  for index, prod in enumerate(PRODUTOS):
    if prod["id"] == produto_id:
      PRODUTOS[index] = produto
      return produto
  return {}

@app.delete("/produtos/{produto_id}", tags=["produtos"])
def deletar_produto(produto_id: int) -> dict:
  """Deletar produto"""
  for index, prod in enumerate(PRODUTOS):
    if prod["id"] == produto_id:
      PRODUTOS.pop(index)
      return {"message": "Produto removido com sucesso!"}
  return {}

