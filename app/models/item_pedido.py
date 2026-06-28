from sqlalchemy import Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    pedido_id: Mapped[int] = mapped_column(
        ForeignKey("pedidos.id"),
        nullable=False
    )

    produto_id: Mapped[int] = mapped_column(
        ForeignKey("produtos.id"),
        nullable=False
    )

    quantidade: Mapped[int] = mapped_column(nullable=False)

    preco_unitario: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    pedido = relationship("Pedido", back_populates="itens")
    produto = relationship("Produto")