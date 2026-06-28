from datetime import datetime

from sqlalchemy import DateTime, Enum, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.enums import CanalPedido, StatusPedido


class Pedido(Base):
    __tablename__ = "pedidos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    usuario_id: Mapped[int] = mapped_column(
        ForeignKey("usuarios.id"),
        nullable=False
    )

    total: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )

    status: Mapped[StatusPedido] = mapped_column(
        Enum(StatusPedido),
        default=StatusPedido.AGUARDANDO_PAGAMENTO
    )

    canal_pedido: Mapped[CanalPedido] = mapped_column(
        Enum(CanalPedido),
        nullable=False
    )

    data_criacao: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    usuario = relationship("Usuario")
    itens = relationship(
        "ItemPedido",
        back_populates="pedido",
        cascade="all, delete-orphan"
    )