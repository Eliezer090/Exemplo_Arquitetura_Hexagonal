from typing import List
import inject
from src.domain.interfaces.pedido.pedido import Pedido
from src.domain.interfaces.pedido.pedidoInterface import PedidoInterface


class PostPedido:
    @inject.autoparams()
    def __init__(self, pedidointerface: PedidoInterface):
        self.__pedinterface = pedidointerface

    def execute(self, pedido: Pedido) -> List[Pedido]:
        return self.__pedinterface.post_pedido(pedido)
