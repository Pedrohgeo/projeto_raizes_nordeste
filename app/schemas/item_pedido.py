from pydantic import BaseModel


class ItemPedidoBase(BaseModel):
    pedido_id: int
    produto_id: int
    quantidade: int
    preco_unitario: float


class ItemPedidoCreate(ItemPedidoBase):
    pass


class ItemPedidoResponse(ItemPedidoBase):
    id: int

    class Config:
        from_attributes = True