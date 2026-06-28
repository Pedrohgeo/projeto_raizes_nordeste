from enum import Enum


class PerfilUsuario(str, Enum):
    CLIENTE = "CLIENTE"
    ATENDENTE = "ATENDENTE"
    COZINHA = "COZINHA"
    ADMIN = "ADMIN"


class StatusPedido(str, Enum):
    AGUARDANDO_PAGAMENTO = "AGUARDANDO_PAGAMENTO"
    RECEBIDO = "RECEBIDO"
    EM_PREPARACAO = "EM_PREPARACAO"
    PRONTO = "PRONTO"
    ENTREGUE = "ENTREGUE"
    RECUSADO = "RECUSADO"


class CanalPedido(str, Enum):
    APP = "APP"
    TOTEM = "TOTEM"
    BALCAO = "BALCAO"
    PICKUP = "PICKUP"
    WEB = "WEB"