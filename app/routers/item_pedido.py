from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.item_pedido import ItemPedido
from app.schemas.item_pedido import (
    ItemPedidoCreate,
    ItemPedidoResponse
)

router = APIRouter(
    prefix="/itens-pedido",
    tags=["Itens do Pedido"]
)


@router.get("/", response_model=list[ItemPedidoResponse])
def listar_itens(db: Session = Depends(get_db)):
    return db.query(ItemPedido).all()


@router.post("/", response_model=ItemPedidoResponse)
def criar_item(
    item: ItemPedidoCreate,
    db: Session = Depends(get_db)
):
    novo_item = ItemPedido(**item.model_dump())

    db.add(novo_item)
    db.commit()
    db.refresh(novo_item)

    return novo_item


@router.put("/{item_id}", response_model=ItemPedidoResponse)
def atualizar_item(
    item_id: int,
    item: ItemPedidoCreate,
    db: Session = Depends(get_db)
):
    item_db = db.query(ItemPedido).filter(
        ItemPedido.id == item_id
    ).first()

    if not item_db:
        raise HTTPException(
            status_code=404,
            detail="Item não encontrado"
        )

    for campo, valor in item.model_dump().items():
        setattr(item_db, campo, valor)

    db.commit()
    db.refresh(item_db)

    return item_db


@router.delete("/{item_id}")
def excluir_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    item = db.query(ItemPedido).filter(
        ItemPedido.id == item_id
    ).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Item não encontrado"
        )

    db.delete(item)
    db.commit()

    return {
        "mensagem": "Item removido com sucesso!"
    }