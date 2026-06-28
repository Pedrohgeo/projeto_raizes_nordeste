from pydantic import BaseModel, EmailStr

from app.enums import PerfilUsuario


class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    perfil: PerfilUsuario


class UsuarioCreate(UsuarioBase):
    senha: str


class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        from_attributes = True