from datetime import datetime

from pydantic import BaseModel

from app.enums import CanalPedido, StatusPedido


class PedidoBase(BaseModel):
    usuario_id: int
    canal_pedido: CanalPedido


class PedidoCreate(PedidoBase):
    pass


class PedidoResponse(PedidoBase):
    id: int
    total: float
    status: StatusPedido
    data_criacao: datetime

    class Config:
        from_attributes = True