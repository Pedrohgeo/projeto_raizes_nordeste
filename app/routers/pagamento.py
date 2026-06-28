from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.pedido import Pedido
from app.enums import StatusPedido

router = APIRouter(
    prefix="/pagamentos",
    tags=["Pagamentos"]
)


@router.post("/mock/{pedido_id}")
def pagamento_mock(
    pedido_id: int,
    db: Session = Depends(get_db)
):
    # Busca o pedido
    pedido = db.query(Pedido).filter(
        Pedido.id == pedido_id
    ).first()

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado"
        )

    # Verifica se o pedido já foi pago
    if pedido.status != StatusPedido.AGUARDANDO_PAGAMENTO:
        raise HTTPException(
            status_code=400,
            detail="Este pedido já foi processado."
        )

    # Simula a aprovação do pagamento
    pedido.status = StatusPedido.RECEBIDO

    db.commit()
    db.refresh(pedido)

    return {
        "mensagem": "Pagamento aprovado com sucesso (Mock).",
        "pedido_id": pedido.id,
        "status": pedido.status.value,
        "transacao": "MOCK123456"
    }