from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)


@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()


@router.post("/", response_model=UsuarioResponse)
def criar_usuario(
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    novo_usuario = Usuario(**usuario.model_dump())

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario


@router.put("/{usuario_id}", response_model=UsuarioResponse)
def atualizar_usuario(
    usuario_id: int,
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):
    usuario_db = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if not usuario_db:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    for campo, valor in usuario.model_dump().items():
        setattr(usuario_db, campo, valor)

    db.commit()
    db.refresh(usuario_db)

    return usuario_db


@router.delete("/{usuario_id}")
def excluir_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    db.delete(usuario)
    db.commit()

    return {
        "mensagem": "Usuário excluído com sucesso!"
    }