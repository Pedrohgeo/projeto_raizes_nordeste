from fastapi import FastAPI

from app.config import settings
from app.database import Base, engine

# Importa os modelos
from app.models import Usuario, Produto, Pedido, ItemPedido

from app.routers.produto import router as produto_router
from app.routers.usuario import router as usuario_router
from app.routers.pedido import router as pedido_router
from app.routers.item_pedido import router as item_pedido_router
from app.routers.pagamento import router as pagamento_router

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


@app.get("/")
def home():
    return {
        "status": "online",
        "mensagem": f"Bem-vindo à {settings.APP_NAME}"
    }

app.include_router(produto_router)
app.include_router(usuario_router)
app.include_router(pedido_router)
app.include_router(item_pedido_router)
app.include_router(pagamento_router)