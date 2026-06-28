from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.enums import PerfilUsuario


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    senha: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    perfil: Mapped[PerfilUsuario] = mapped_column(
        Enum(PerfilUsuario),
        nullable=False
    )