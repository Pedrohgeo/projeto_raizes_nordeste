from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.produto import Produto
from app.schemas.produto import ProdutoCreate, ProdutoResponse

router = APIRouter(
    prefix="/produtos",
    tags=["Produtos"]
)


@router.get("/", response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = db.query(Produto).all()
    return produtos


@router.post("/", response_model=ProdutoResponse)
def criar_produto(
    produto: ProdutoCreate,
    db: Session = Depends(get_db)
):
    novo_produto = Produto(**produto.model_dump())

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto


@router.put("/{produto_id}", response_model=ProdutoResponse)
def atualizar_produto(
    produto_id: int,
    produto: ProdutoCreate,
    db: Session = Depends(get_db)
):
    produto_db = db.query(Produto).filter(
        Produto.id == produto_id
    ).first()

    if not produto_db:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    for campo, valor in produto.model_dump().items():
        setattr(produto_db, campo, valor)

    db.commit()
    db.refresh(produto_db)

    return produto_db


@router.delete("/{produto_id}")
def excluir_produto(
    produto_id: int,
    db: Session = Depends(get_db)
):
    produto = db.query(Produto).filter(
        Produto.id == produto_id
    ).first()

    if not produto:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    db.delete(produto)
    db.commit()

    return {
        "mensagem": "Produto excluído com sucesso!"
    }