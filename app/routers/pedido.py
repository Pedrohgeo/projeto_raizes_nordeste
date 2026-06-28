from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.pedido import Pedido
from app.schemas.pedido import PedidoCreate, PedidoResponse

router = APIRouter(
    prefix="/pedidos",
    tags=["Pedidos"]
)

#Lista de pedidos
@router.get("/", response_model=list[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    return db.query(Pedido).all()

#criar pedido
@router.post("/", response_model=PedidoResponse)
def criar_pedido(
    pedido: PedidoCreate,
    db: Session = Depends(get_db)
):
    novo_pedido = Pedido(**pedido.model_dump())

    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)

    return novo_pedido

#Atualizar pedido
@router.put("/{pedido_id}", response_model=PedidoResponse)
def atualizar_pedido(
    pedido_id: int,
    pedido: PedidoCreate,
    db: Session = Depends(get_db)
):
    pedido_db = db.query(Pedido).filter(
        Pedido.id == pedido_id
    ).first()

    if not pedido_db:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado"
        )

    for campo, valor in pedido.model_dump().items():
        setattr(pedido_db, campo, valor)

    db.commit()
    db.refresh(pedido_db)

    return pedido_db

#Excluir pedido
@router.delete("/{pedido_id}")
def excluir_pedido(
    pedido_id: int,
    db: Session = Depends(get_db)
):
    pedido = db.query(Pedido).filter(
        Pedido.id == pedido_id
    ).first()

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado"
        )

    db.delete(pedido)
    db.commit()

    return {
        "mensagem": "Pedido excluído com sucesso!"
    }
