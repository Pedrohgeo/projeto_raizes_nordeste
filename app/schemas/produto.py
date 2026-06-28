from pydantic import BaseModel


class ProdutoBase(BaseModel):
    nome: str
    descricao: str | None = None
    preco: float
    qtd_estoque: int


class ProdutoCreate(ProdutoBase):
    pass


class ProdutoResponse(ProdutoBase):
    id: int

    class Config:
        from_attributes = True